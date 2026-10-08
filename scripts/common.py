"""Shared helpers for the literature review pipeline.

Everything here is deterministic and dependency-light so the pipeline stays
fast to re-run when the corpus or config changes. Nothing in this module knows
about topic taxonomies or relevance scoring; it deals only in paths, text
cleaning, frontmatter, and the note grammar.

The note grammar is specified in `docs/standards/note-format.md`. `load_note`
turns an authored note into the same flat shape the matrix builder consumes, so
a note and a retired `_summarized.json` are interchangeable to callers.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = REPO_ROOT / "literature" / "paper-markdowns"
DEFAULT_REVIEW = REPO_ROOT / "review"
DEFAULT_NOTES = DEFAULT_REVIEW / "notes"
DEFAULT_CONFIG = REPO_ROOT / "config" / "taxonomy.yaml"

WS = re.compile(r"\s+")

# Section headings the builder requires, and the tables it parses out of them.
EFFECT_COLUMNS = ("Outcome", "Metric", "Value", "CI", "p", "Locator")
QUOTE_COLUMNS = ("Text", "Locator", "Module")
REQUIRED_SECTIONS = (
    "Summary", "Method", "Limitations and Gaps", "Statistical Evidence", "Quotes",
)
ANCHORS = ("Design", "Sample")


def corpus_paths(
    corpus_dir: str | Path | None = None, notes_dir: str | Path | None = None
) -> list[tuple[str, Path, Path | None]]:
    """Return [(stem, marked_md_path, note_path|None)] sorted by stem.

    Notes live outside the corpus, in `review/notes/`, so a paper is the union of
    its conversion and its note. A conversion with no note is an unextracted
    paper, not a broken corpus.
    """
    root = Path(corpus_dir) if corpus_dir else DEFAULT_CORPUS
    note_root = Path(notes_dir) if notes_dir else DEFAULT_NOTES
    papers = []
    for md in sorted(root.rglob("*_marked.md")):
        stem = md.name[: -len("_marked.md")]
        note_path = note_root / f"{stem}.md"
        papers.append((stem, md, note_path if note_path.exists() else None))
    return papers


_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_PAGE_RE = re.compile(r"<!--\s*PAGE\s*\d+\s*-->", re.IGNORECASE)
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def strip_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def parse_frontmatter(md_text: str) -> dict:
    """Parse the YAML-ish frontmatter into a dict. Best-effort, tolerant."""
    m = _FRONTMATTER_RE.match(md_text)
    if not m:
        return {}
    meta: dict = {}
    for line in m.group(0).splitlines():
        line = line.strip()
        if not line or line == "---" or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip().strip('"'), value.strip().strip('"')
        if not key:
            continue
        meta[key] = value
    return meta


def clean_text(md_text: str) -> str:
    text = strip_frontmatter(md_text)
    text = _PAGE_RE.sub(" ", text)
    text = _IMAGE_RE.sub(" ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def read_marked(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def corpus_fingerprint(papers: list[tuple[str, Path, Path | None]]) -> str:
    h = hashlib.sha256()
    for stem, md, note in sorted(papers, key=lambda p: p[0]):
        for path in (md, note):
            if path is None:
                continue
            st = path.stat()
            h.update(f"{stem}|{path.name}|{st.st_mtime_ns}|{st.st_size}\n".encode())
    return h.hexdigest()


# --- note grammar -------------------------------------------------------------
# Parsed here rather than in the matrix builder so any future tool reads a note
# the same way. The output shape deliberately matches the retired summary schema
# (`tldr`, `study_design`, `sample`, `limitations`, `quotes`, `effects`,
# `modules`) so the builder's row assembly is unchanged by the switch.

_HEADING_RE = re.compile(r"^##[ \t]+(.+?)[ \t]*$", re.MULTILINE)
_ANCHOR_RE = re.compile(r"^\*\*(\w[\w ]*?)\.\*\*[ \t]*(.*)$")
_CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")
_BULLET_RE = re.compile(r"^[-*][ \t]+(.*\S)[ \t]*$", re.MULTILINE)
_ROW_SPLIT_RE = re.compile(r"\n{2,}")


def _sections(body: str) -> dict[str, str]:
    """Map `## Heading` -> the text under it, in document order."""
    out: dict[str, str] = {}
    marks = list(_HEADING_RE.finditer(body))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out[m.group(1).strip().casefold()] = body[m.end():end].strip("\n")
    return out


def _anchors(text: str) -> dict[str, str]:
    """Collect `**Label.** value` pairs, joining wrapped continuation lines."""
    out: dict[str, str] = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = _ANCHOR_RE.match(lines[i].strip())
        if not m:
            i += 1
            continue
        label, buf = m.group(1).strip().casefold(), [m.group(2).strip()]
        j = i + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if not nxt or nxt.startswith(("#", "-", "*", ">")) or _ANCHOR_RE.match(nxt):
                break
            buf.append(nxt)
            j += 1
        out[label] = WS.sub(" ", " ".join(x for x in buf if x)).strip()
        i = j
    return out


def _bullets(text: str) -> list[str]:
    return [m.group(1).strip() for m in _BULLET_RE.finditer(text)]


_ABSENCE_RE = re.compile(
    r"not (?:reported|applicable)\b|no outcome statistics\b|"
    r"reports? no (?:statistic|result|outcome|quantitative)",
    re.IGNORECASE,
)


def _declares_absence(text: str) -> bool:
    """True when a table-less section explicitly states that it has no records.

    `docs/standards/note-format.md` requires `## Statistical Evidence` and
    `## Quotes` to state absence rather than be dropped, so a note that writes
    `Not reported.` has answered the question the section exists to answer. The
    declaration has to be prose, not an empty section: a missing section and an
    empty one are different claims, and only the second is a stated absence.
    """
    head = " ".join(ln.strip() for ln in text.strip().splitlines() if ln.strip())[:400]
    return bool(head) and bool(_ABSENCE_RE.search(head))


def _table(text: str, columns: tuple[str, ...], label: str) -> tuple[list[dict], list[str]]:
    """Parse the first markdown table under `text` and check its header exactly."""
    errors: list[str] = []
    lines = [ln.strip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln]
    if not lines:
        return [], [f"`{label}` section is empty; write `Not reported.` if there are no records"]

    header_idx = next((i for i, ln in enumerate(lines) if ln.startswith("|")), None)
    if header_idx is None:
        if _declares_absence(text):
            return [], []
        return [], [f"`{label}` has no table; write `Not reported.` if there are no records"]

    def cells(line: str) -> list[str]:
        inner = line.strip().strip("|")
        return [c.replace("\\|", "|").strip() for c in _CELL_SPLIT_RE.split(inner)]

    header = tuple(c.strip().casefold() for c in cells(lines[header_idx]))
    if header != tuple(c.casefold() for c in columns):
        errors.append(
            f"`{label}` header must be exactly {' | '.join(columns)}; found {' | '.join(cells(lines[header_idx]))}"
        )
        return [], errors

    rows: list[dict] = []
    for ln in lines[header_idx + 1:]:
        if not ln.startswith("|"):
            break
        if re.fullmatch(r"[:\-\s|]+", ln):
            continue
        values = cells(ln)
        if len(values) != len(columns):
            errors.append(
                f"`{label}` row has {len(values)} cells, expected {len(columns)}: {ln[:80]}"
            )
            continue
        record = {c: v for c, v in zip(columns, values)}
        # `—` and the empty string both mean "the paper does not print this".
        for key in ("CI", "p"):
            if key in record and record[key] in ("", "—", "-"):
                record[key] = ""
        if label == "Quotes":
            text_value = record["Text"]
            if len(text_value) >= 2 and text_value[0] == '"' and text_value[-1] == '"':
                record["Text"] = text_value[1:-1].strip()
        if not any(record.values()):
            continue
        rows.append(record)
    return rows, errors


def load_note(path: Path | None) -> dict | None:
    """Parse an authored note into the flat shape the matrix builder consumes.

    Returns None when the file is absent. A file that exists but does not parse
    returns a dict whose `status` is `not extracted` and whose `_errors` explains
    why, so a broken note is reported rather than silently treated as missing.
    """
    if not path or not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"status": "not extracted", "_errors": [f"unreadable: {exc}"], "modules": []}

    errors: list[str] = []
    frontmatter: dict = {}
    m = _FRONTMATTER_RE.match(text)
    body = text
    if m:
        try:
            loaded = yaml.safe_load(m.group(1).strip())
            if isinstance(loaded, dict):
                frontmatter = loaded
            else:
                errors.append("frontmatter is not a YAML mapping")
        except yaml.YAMLError as exc:
            errors.append(f"frontmatter is not valid YAML: {str(exc).splitlines()[0]}")
        body = text[m.end():]
    else:
        errors.append("missing frontmatter block")

    status = str(frontmatter.get("status") or "").strip()
    if status not in ("extracted", "not extracted"):
        errors.append(
            f"frontmatter `status` must be `extracted` or `not extracted`, found {status!r}"
        )
        status = ""

    data: dict = {
        "paper_id": str(frontmatter.get("paper_id") or "").strip(),
        "status": status,
        "type": str(frontmatter.get("type") or "").strip(),
        "modules": [str(x).strip() for x in (frontmatter.get("modules") or []) if str(x).strip()],
        "module_rationale": frontmatter.get("module_rationale") or {},
        "frontmatter": frontmatter,
        "body": body,
        "_errors": errors,
    }

    if status != "extracted":
        return data

    sections = _sections(body)
    for name in REQUIRED_SECTIONS:
        if name.casefold() not in sections:
            errors.append(f"missing required section `## {name}`")

    summary = sections.get("summary", "")
    paragraph = next(
        (p.strip() for p in _ROW_SPLIT_RE.split(summary) if p.strip() and not p.strip().startswith(("#", "|", ">", "-"))),
        "",
    )
    data["tldr"] = WS.sub(" ", paragraph)
    if not data["tldr"]:
        errors.append("`## Summary` has no paragraph; it supplies the matrix `key_finding`")

    method = _anchors(sections.get("method", ""))
    for label in ANCHORS:
        data[{"Design": "study_design", "Sample": "sample"}[label]] = method.get(label.casefold(), "")
        if not method.get(label.casefold()):
            errors.append(f"`## Method` has no `**{label}.**` line")

    limitations = _bullets(sections.get("limitations and gaps", ""))
    data["limitations"] = limitations
    if not limitations:
        errors.append("`## Limitations and Gaps` has no bullet; the first one supplies the matrix `gap`")

    data["effects"], eff_errors = _table(sections.get("statistical evidence", ""), EFFECT_COLUMNS, "Statistical Evidence")
    errors += eff_errors
    data["quotes"], quote_errors = _table(sections.get("quotes", ""), QUOTE_COLUMNS, "Quotes")
    errors += quote_errors
    return data
