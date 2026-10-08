"""Build the generated literature review matrix and its long tables.

    python3 scripts/build_matrix.py            # build all generated outputs
    python3 scripts/build_matrix.py --check    # validate only, exit 1 on error

`review/literature-review-matrix.md` is a generated view, not a database. It is
rebuilt from three sources, in this order of authority:

    literature/paper-markdowns/metadata.json   bibliographic metadata (page-1 verified)
    review/notes/{stem}.md                    extraction, including module assignment
    config/taxonomy.yaml                      the module namespace

A paper is assigned to zero or more modules of `config/taxonomy.yaml` by whoever
reads it during extraction. There is no relevance scoring: no weights, no
thresholds, no similarity numbers. Coverage per module is tallied from those
assignments, so the taxonomy and the corpus are never out of step.

Nothing in the matrix is hand-written. To correct a value, edit the source above
and re-run. Column definitions: `docs/standards/review-layout.md`. Note grammar:
`docs/standards/note-format.md`.

Generated outputs:
    review/literature-review-matrix.md   lean 15-column index, one row per paper
    review/data/papers.csv               the same projection, for spreadsheets
    review/data/screening.csv            corpus triage inventory
    review/data/quotes.csv               one record per extracted quotation
    review/data/effects.csv              one record per statistical result
    review/data/themes.csv               per-module coverage tally
    review/validation.md                 what passed, what failed, what is missing

`review/notes/` and `review/synthesis/` are authored. This script never
overwrites an existing note; it writes a stub only for a paper that has none, so
the set of unextracted papers stays visible without erasing extraction work.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from common import (
    DEFAULT_CONFIG,
    DEFAULT_CORPUS,
    DEFAULT_NOTES,
    DEFAULT_REVIEW,
    REPO_ROOT,
    WS,
    corpus_paths,
    load_note,
)

DEFAULT_METADATA = DEFAULT_CORPUS / "metadata.json"

NOT_REPORTED = "Not reported"
NOT_APPLICABLE = "Not applicable"
UNVERIFIED = "Unverified"

CELL_CAP = 200

# A DOI is only "reported" if it can be a DOI. Guards against the line-break
# artifact in A--Abdullahi-2025 ("10.1 109/ACCESS.2025.3587231") and against
# invented DOIs, which this repo has already had to retract once.
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")

CONTROLLED_TYPES = {
    "journal-article", "conference-paper", "book", "book-chapter", "thesis",
    "preprint", "report", "working-paper", "dataset", "dashboard", "webpage", "other",
}

PAPER_TYPES = {
    "journal article": "journal-article",
    "review article": "journal-article",
    "conference paper": "conference-paper",
    "book": "book",
    "book chapter": "book-chapter",
    "thesis or dissertation": "thesis",
    "preprint": "preprint",
    "report": "report",
    "institutional report": "report",
    "working paper": "working-paper",
    "dataset": "dataset",
    "institutional dashboard": "dashboard",
    "webpage": "webpage",
    "other": "other",
}

DESIGNATION_BY_PREFIX = {"L": "local", "I": "international", "A": "algorithm"}
LEGACY_ALGORITHM_PREFIXES = {"AI", "IA", "AL", "LA"}

PUNCT = re.compile(r"[^\w\s]")

# Language a paper uses when it contradicts itself. Checked in `limitations` so
# an acknowledged discrepancy cannot be silently reconciled away.
DISCREPANCY_RE = re.compile(
    r"inconsisten|discrepan|contradict|mismatch|conflict|differ|both report|"
    r"not reproduc|internal(?:ly)? (?:inconsisten|inconsistenc)|does not match",
    re.IGNORECASE,
)
# Result figures quoted inside a discrepancy entry: a percentage, or a decimal.
# Deliberately excludes bare integers, because a page or table number in the
# same sentence is not a result and would fire on every entry.
QUOTED_NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)+%?|\d+(?:[.,]\d+)+\s*%")

# Fill-rate verdicts below this many extracted rows are noise: with 2 rows a
# single empty cell reads as a 50% gap.
MIN_ROWS_FOR_FILL_VERDICT = 10

class Findings:
    """Collects validation results, separating errors from informational gaps."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.gaps: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def gap(self, msg: str) -> None:
        self.gaps.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def cap(text: str, limit: int = CELL_CAP) -> str:
    text = WS.sub(" ", (text or "").strip())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def letter_suffixed_group(stems: list[str]) -> bool:
    """True when a set of stems is one author's several works in one year.

    `I--Yang-2024` and `I--Yang-2024b` are the documented letter-suffix
    convention, not a duplicate. Two stems with *no* suffix, or a suffix that
    does not correspond to a base stem present in the set, is a real ambiguity.
    """
    suffixed: dict[str, list[str]] = defaultdict(list)
    for stem in stems:
        # The suffix is appended to the year, not to the stem: the format is
        # {Prefix}--{Author}-{Year}{Suffix}, so `I--Yang-2024b` splits as
        # author `Yang`, year `2024`, suffix `b`.
        head, _, author = stem.partition("--")
        if "-" not in author:
            continue
        name, _, yearsuffix = author.rpartition("-")
        base, suffix = yearsuffix[:4], yearsuffix[4:]
        if base.isdigit() and len(suffix) == 1 and suffix.isalpha():
            suffixed[f"{head}--{name}-{base}"].append(suffix)
    if len(suffixed) != 1:
        return False
    head, suffixes = next(iter(suffixed.items()))
    # Every suffixed stem needs an unsuffixed base in the same set.
    return head in stems and len(suffixes) == len(stems) - 1


def normalize_title(title: str) -> str:
    return WS.sub(" ", PUNCT.sub("", (title or "").lower())).strip()


def normalize_doi(doi: str) -> str:
    """Strip a resolver prefix and lowercase, without repairing a split DOI.

    A DOI containing an internal space is a PDF line-break artifact. It is left
    intact here so the validator reports it rather than the builder quietly
    inventing a join point.
    """
    doi = (doi or "").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    return doi.lower()


def paper_type(note: dict, meta: dict) -> str:
    """Controlled type label, from the note frontmatter first, then metadata."""
    raw = note.get("type") or meta.get("publication_type") or ""
    if not raw:
        return NOT_REPORTED
    key = WS.sub(" ", str(raw).strip().lower())
    return PAPER_TYPES.get(key, str(raw).strip().lower())


def designation_of(stem: str) -> str:
    prefix = stem.split("--", 1)[0]
    if prefix in LEGACY_ALGORITHM_PREFIXES:
        return "algorithm"
    return DESIGNATION_BY_PREFIX.get(prefix, NOT_REPORTED)


def first_author(meta: dict, stem: str) -> str:
    """First author from metadata, else derived from the stem author segment.

    Seven stems were built from filenames and named a later author; metadata.json
    records the page-1 verified correction, so prefer it and fall back only.
    """
    recorded = meta.get("first_author")
    if recorded:
        return str(recorded)
    authors = meta.get("authors") or []
    if authors:
        return str(authors[0]).split(",")[0].strip()
    parts = stem.split("--", 1)
    if len(parts) == 2:
        return parts[1].rsplit("-", 1)[0]
    return NOT_REPORTED


def venue_of(meta: dict) -> str:
    venue = cap(meta.get("venue") or "", 80)
    if not venue:
        return NOT_REPORTED
    if meta.get("venue_unverified"):
        return f"{venue} ({UNVERIFIED})"
    return venue


def slug(text: str) -> str:
    return PUNCT.sub("", WS.sub("-", (text or "").strip().lower())).strip("-")


def assigned_modules(note: dict) -> list[str]:
    """Module ids assigned during extraction, de-duplicated, in taxonomy order.

    Order is applied by the caller against the taxonomy, so this only has to
    return a clean set.
    """
    out: list[str] = []
    for value in note.get("modules") or []:
        if isinstance(value, str) and value.strip() and value.strip() not in out:
            out.append(value.strip())
    return out


def section_names(modules: list[str], module_section: dict[str, str], section_name: dict[str, str]) -> str:
    """Human-readable outline sections a paper's modules fall under."""
    names: list[str] = []
    for module in modules:
        sid = module_section.get(module)
        if sid and section_name.get(sid) and section_name[sid] not in names:
            names.append(section_name[sid])
    return "; ".join(names) if names else NOT_REPORTED


def first_limitation(note: dict) -> str:
    """The paper's own first stated limitation, which the matrix shows as `gap`."""
    limits = note.get("limitations") or []
    for item in limits:
        if isinstance(item, str) and item.strip():
            return cap(item)
    return NOT_REPORTED


# A `method/` tag is one controlled word, so map the free-text design label onto
# a fixed vocabulary rather than slugging a whole sentence into the cell. The
# first phrase before a colon or parenthesis is the design proper; the rest is
# usually the paper explaining that it states no formal label.
DESIGN_METHODS: list[tuple[str, tuple[str, ...]]] = [
    ("slr", ("systematic literature review", "systematic review", "scoping review", "prisma")),
    ("meta-analysis", ("meta-analysis", "meta analysis")),
    ("literature-review", ("literature review", "review article", "narrative review", "state of the art")),
    ("qualitative", ("qualitative", "interview", "thematic analysis", "case study", "grounded theory")),
    ("survey", ("survey", "questionnaire", "cross-sectional")),
    ("experimental", ("experiment", "experimental", "randomized", "controlled trial", "a/b test")),
    ("benchmark", ("benchmark", "comparative evaluation", "comparative benchmark")),
    ("design-science", ("design science", "design and evaluation", "artifact", "prototype", "framework design")),
    ("dataset", ("dataset", "data description", "secondary data")),
    ("simulation", ("simulation", "synthetic", "monte carlo")),
    ("conceptual", ("conceptual", "theoretical", "position paper", "framework proposal")),
]


def design_method(study_design: str) -> str:
    """Map a free-text design label onto one controlled `method/` value."""
    label = WS.sub(" ", (study_design or "").strip())
    if not label or label in (NOT_REPORTED, NOT_APPLICABLE):
        return ""
    head = label.split(":")[0].split("(")[0].lower()
    haystack = f"{head} {label.lower()}"
    for tag, needles in DESIGN_METHODS:
        if any(needle in haystack for needle in needles):
            return tag
    return "other"


def build_tags(stem: str, note: dict, meta: dict, modules: list[str]) -> str:
    """Controlled tags: modules, scope, method, status, quality.

    Module tags come from the extraction, so there is no ranking to truncate and
    no `+Nmore`: a paper legitimately belongs to four modules and says so.
    """
    tags = [f"module/{m}" for m in modules]
    scope = designation_of(stem)
    if scope != NOT_REPORTED:
        tags.append(f"scope/{scope}")
    method = design_method(note.get("study_design") or "")
    if method:
        tags.append(f"method/{method}")
    tags.append("status/extracted" if note else "status/not-extracted")
    if meta.get("venue_unverified") or not normalize_doi(str(meta.get("doi") or "")):
        tags.append("quality/metadata-partial")
    return "; ".join(tags)


COLUMNS = [
    "paper_id", "first_author", "year", "title", "venue", "doi", "type",
    "designation", "section", "modules", "design", "sample", "key_finding",
    "gap", "status",
]


def row_sort_key(row: dict) -> tuple:
    year = row["year"]
    return (0 if year.isdigit() else 1, -int(year) if year.isdigit() else 0, row["paper_id"])


def assemble_rows(
    metadata: dict,
    notes: dict,
    marked: set[str],
    module_order: list[str],
    module_section: dict[str, str],
    section_name: dict[str, str],
) -> list[dict]:
    """One row per corpus paper, from metadata plus whatever note exists.

    A paper with no note still gets a row: its bibliographic columns are real and
    its extraction columns read `Not reported`, so the coverage gap is visible in
    the matrix instead of being a set of absent files. A generated stub is treated
    as no note at all — it is a placeholder that says so.
    """
    rows = []
    for stem in sorted(set(metadata) | set(notes)):
        meta = metadata.get(stem) or {}
        note = notes.get(stem) or {}
        # A stub is a placeholder that says so, so it is not extraction. Only a
        # note whose frontmatter claims `extracted` fills the extraction columns —
        # but the full parse result is still kept, so a note that *tries* to be an
        # extraction and fails to parse is reported rather than ignored.
        extracted = note.get("status") == "extracted"
        content = note if extracted else {}
        doi = normalize_doi(str(meta.get("doi") or ""))
        modules = assigned_modules(content)
        # Present module ids in taxonomy order, then anything unknown at the end
        # so the validator can report it without the order looking arbitrary.
        ordered = [m for m in module_order if m in modules]
        ordered += [m for m in modules if m not in module_order]
        rows.append({
            "paper_id": stem,
            "first_author": first_author(meta, stem),
            "year": str(meta.get("year") or NOT_REPORTED),
            "title": cap(meta.get("title") or NOT_REPORTED, 140),
            "venue": venue_of(meta),
            "doi": doi or NOT_REPORTED,
            "type": paper_type(content, meta),
            "designation": designation_of(stem),
            "section": section_names(ordered, module_section, section_name),
            "modules": "; ".join(ordered) if ordered else NOT_REPORTED,
            "design": cap(content.get("study_design") or NOT_REPORTED),
            "sample": cap(content.get("sample") or NOT_REPORTED),
            "key_finding": cap(content.get("tldr") or NOT_REPORTED),
            "gap": first_limitation(content),
            "status": "extracted" if extracted else "not extracted",
            "tags": build_tags(stem, content, meta, ordered),
            "_meta": meta,
            "_note": note,
            "_marked": stem in marked,
        })
    rows.sort(key=row_sort_key)
    return rows


def collect_long_tables(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Project per-paper quotes/effects into flat cross-paper records.

    The note parser keys rows by their Markdown table headers (`Text`, `Module`,
    `Outcome`, `CI`, `p`); the CSVs use lowercase snake_case, so map across here
    rather than mutating what the note records hold.
    """
    quotes: list[dict] = []
    effects: list[dict] = []
    for row in rows:
        note = row["_note"]
        for q in note.get("quotes") or []:
            if not isinstance(q, dict):
                continue
            quotes.append({
                "paper_id": row["paper_id"],
                "text": WS.sub(" ", str(q.get("Text") or "").strip()),
                "locator": str(q.get("Locator") or NOT_REPORTED),
                "module": str(q.get("Module") or NOT_REPORTED),
            })
        for e in note.get("effects") or []:
            if not isinstance(e, dict):
                continue
            record = {
                "paper_id": row["paper_id"],
                "outcome": WS.sub(" ", str(e.get("Outcome") or "").strip()),
                "metric": WS.sub(" ", str(e.get("Metric") or "").strip()),
                "value": str(e.get("Value") or NOT_REPORTED),
                "locator": str(e.get("Locator") or NOT_REPORTED),
            }
            for optional, note_key in (("ci", "CI"), ("p", "p")):
                if e.get(note_key):
                    record[optional] = str(e[note_key])
            effects.append(record)
    return quotes, effects


def validate(rows: list[dict], f: Findings, taxonomy: dict) -> dict:
    """Apply every rule in docs/standards/review-layout.md."""
    known_modules = {m["id"] for m in taxonomy.get("modules") or []}
    known_methods = {tag for tag, _ in DESIGN_METHODS} | {"other"}
    stats: dict = {}

    # --- DOI shape -------------------------------------------------------
    bad_doi = []
    for row in rows:
        # Validate both sides. The row renders metadata.json, but a note can
        # carry its own DOI in its frontmatter, and a malformed one must not slip
        # through just because the metadata value happens to be well-formed.
        for source, doi in (
            ("metadata", row["doi"]),
            ("note", str(row["_note"].get("frontmatter", {}).get("doi") or "")),
        ):
            doi = doi.strip()
            if not doi or doi == NOT_REPORTED:
                continue
            if not DOI_RE.match(normalize_doi(doi)):
                bad_doi.append(f"{row['paper_id']} ({source}): `{doi}`")
    for item in bad_doi:
        f.error(f"Malformed DOI — {item}. Expected `10.NNNN/suffix` with no spaces.")
    stats["malformed_doi"] = len(bad_doi)

    # --- note vs metadata agreement ---------------------------------------
    # metadata.json is the citation authority, so a note that disagrees is
    # wrong, not merely different. The note's bibliographic values live in its
    # frontmatter. Checked on the normalized DOI so a case difference or a
    # doi.org prefix is not reported as a conflict.
    disagree = []
    for row in rows:
        fm = row["_note"].get("frontmatter") or {}
        if not fm:
            continue
        for field in ("year", "title", "doi"):
            a, b = row["_meta"].get(field), fm.get(field)
            if not b or b in (NOT_REPORTED, NOT_APPLICABLE):
                # A note that says `Not reported` is not disagreeing with a
                # missing value; it is echoing the placeholder (stubs do this).
                continue
            if field == "doi":
                if normalize_doi(str(a or "")) != normalize_doi(str(b)):
                    disagree.append(f"{row['paper_id']}.{field}: metadata `{a or NOT_REPORTED}` vs note `{b}`")
            elif str(a or "").strip().lower() != str(b).strip().lower():
                disagree.append(f"{row['paper_id']}.{field}: metadata `{a or NOT_REPORTED}` vs note `{b}`")
    for item in disagree:
        f.error(f"Note disagrees with metadata.json — {item}. metadata.json wins; fix the note.")
    stats["metadata_disagreement"] = len(disagree)

    # --- corpus resolvability --------------------------------------------
    unmarked = [r["paper_id"] for r in rows if not r["_marked"]]
    for stem in unmarked:
        f.error(f"`{stem}` is in the matrix but has no `_marked.md` in the corpus.")
    stats["unmarked"] = len(unmarked)

    # --- duplicates ------------------------------------------------------
    by_doi: dict[str, list[str]] = defaultdict(list)
    by_title: dict[str, list[str]] = defaultdict(list)
    by_author_year: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        # The "Not reported" sentinel is not a DOI: many entries lack one, and
        # grouping them would report every missing DOI as a duplicate.
        if row["doi"] != NOT_REPORTED:
            by_doi[normalize_doi(row["doi"])].append(row["paper_id"])
        by_title[normalize_title(row["title"])].append(row["paper_id"])
        by_author_year[f"{slug(row['first_author'])}|{row['year']}"].append(row["paper_id"])

    dup_doi = {k: v for k, v in by_doi.items() if k and len(v) > 1}
    dup_title = {k: v for k, v in by_title.items() if k and len(v) > 1}
    for doi, stems in dup_doi.items():
        f.error(f"Duplicate DOI `{doi}`: {', '.join(stems)}")
    for title, stems in dup_title.items():
        f.error(f"Duplicate title \"{title}\": {', '.join(stems)}")

    for key, stems in by_author_year.items():
        if "|" not in key or len(stems) < 2 or not key.strip("|"):
            continue
        # A trailing letter suffix is the documented convention for several
        # works by one author in one year (I--Yang-2024, I--Yang-2024b), so
        # that is not a re-entry. Anything else is worth a look.
        if letter_suffixed_group(stems):
            continue
        f.gap(f"Same first author and year ({key}): {', '.join(stems)} — check for a re-entry.")
    stats["duplicate_doi"] = len(dup_doi)
    stats["duplicate_title"] = len(dup_title)

    # --- stem vs metadata year -------------------------------------------
    mismatched = []
    for row in rows:
        parts = row["paper_id"].split("--", 1)
        if len(parts) != 2:
            continue
        stem_year = parts[1].rsplit("-", 1)[-1]
        meta_year = str(row["_meta"].get("year") or "")
        if stem_year.isdigit() and meta_year.isdigit() and stem_year != meta_year:
            mismatched.append(f"{row['paper_id']}: stem {stem_year} vs metadata {meta_year}")
    for item in mismatched:
        f.error(f"Stem year disagrees with metadata year — {item}. Rename the stem and re-convert.")
    stats["year_mismatch"] = len(mismatched)

    # --- controlled vocabularies -----------------------------------------
    bad_type = [
        f"{r['paper_id']}: `{r['type']}`"
        for r in rows
        if r["type"] != NOT_REPORTED and r["type"] not in CONTROLLED_TYPES
    ]
    for item in bad_type:
        f.error(f"Uncontrolled `type` value — {item}. See review-layout.md for the list.")
    stats["bad_type"] = len(bad_type)

    bad_module: set[str] = set()
    bad_method: set[str] = set()
    bad_prefix: set[str] = set()
    for row in rows:
        for tag in row["tags"].split("; "):
            prefix, _, value = tag.partition("/")
            if not value:
                bad_prefix.add(tag)
            elif prefix == "module" and value not in known_modules:
                bad_module.add(f"{row['paper_id']}: module/{value}")
            elif prefix == "method" and value not in known_methods:
                bad_method.add(tag)
            elif prefix not in ("module", "scope", "method", "status", "quality"):
                bad_prefix.add(tag)
    for item in sorted(bad_module):
        f.error(f"Unknown module id — {item}. See config/taxonomy.yaml.")
    for tag in sorted(bad_method):
        f.error(f"Tag `{tag}` is not a controlled `method/` value. See DESIGN_METHODS in build_matrix.py.")
    for tag in sorted(bad_prefix):
        f.error(f"Tag `{tag}` is not a known module, scope, method, status, or quality tag.")
    stats["bad_module_ids"] = len(bad_module)

    # --- note grammar ------------------------------------------------------
    # Structural faults in an authored note are errors, not gaps: they mean the
    # file cannot be read as a note, and a column is silently empty because of it.
    grammar: list[str] = []
    for row in rows:
        note = row["_note"]
        if not note:
            continue
        for message in note.get("_errors") or []:
            grammar.append(f"`{row['paper_id']}`: {message}")
        declared = str((note.get("frontmatter") or {}).get("paper_id") or "").strip()
        if declared and declared != row["paper_id"]:
            grammar.append(f"`{row['paper_id']}`: frontmatter `paper_id` is `{declared}`")
        rationale = note.get("module_rationale") or {}
        if not isinstance(rationale, dict):
            grammar.append(f"`{row['paper_id']}`: `module_rationale` must be a mapping of id to clause")
            rationale = {}
        assigned = set(note.get("modules") or [])
        for module in sorted(assigned - set(rationale)):
            grammar.append(f"`{row['paper_id']}`: module `{module}` has no `module_rationale` clause")
        for module in sorted(set(rationale) - assigned):
            grammar.append(f"`{row['paper_id']}`: `module_rationale` explains `{module}`, which is not in `modules[]`")
    for item in grammar:
        f.error(f"Note grammar — {item}. See docs/standards/note-format.md.")
    stats["note_grammar_errors"] = len(grammar)

    # --- no silent blanks -------------------------------------------------
    blank = [f"{r['paper_id']}.{k}" for r in rows for k, v in r.items() if not k.startswith("_") and not str(v).strip()]
    for item in blank[:20]:
        f.error(f"Empty cell — {item}. Use `{NOT_REPORTED}`, `{NOT_APPLICABLE}`, or `{UNVERIFIED}`.")
    stats["blank_cells"] = len(blank)

    # --- same outcome + metric, two values (a finding about the paper) ----
    # Keyed on outcome AND metric together: `accuracy` legitimately has four
    # different values in a comparison table, one per model, and the outcome
    # field is what distinguishes them. Only a repeat of the *same* measurement
    # with a different number is a discrepancy.
    effects_by_paper: dict[str, dict[tuple[str, str], set]] = defaultdict(lambda: defaultdict(set))
    for row in rows:
        for e in row["_note"].get("effects") or []:
            if isinstance(e, dict) and e.get("Metric") and e.get("Value"):
                key = (WS.sub(" ", str(e.get("Outcome") or "").strip()).lower(), str(e["Metric"]))
                effects_by_paper[row["paper_id"]][key].add(str(e["Value"]))
    conflicts = 0
    for paper, measures in sorted(effects_by_paper.items()):
        for (_outcome, metric), values in sorted(measures.items()):
            if len(values) > 1:
                conflicts += 1
                f.gap(
                    f"`{paper}` reports {metric} as {' / '.join(sorted(values))} for the same "
                    f"outcome — keep both with their locators and note it in `limitations`. "
                    f"This is a discrepancy in the paper, not in the extraction."
                )
    stats["effect_conflicts"] = conflicts

    # --- acknowledged discrepancies must be recorded, not smoothed over ---
    # A paper that contradicts itself should say so in `limitations`, and the
    # matrix `gap` column shows `limitations[0]`. Silently reconciling the
    # numbers is the failure this catches.
    unrecorded = 0
    for row in rows:
        limits = " ".join(
            str(x) for x in (row["_note"].get("limitations") or []) if isinstance(x, str)
        )
        if not DISCREPANCY_RE.search(limits):
            continue
        # A discrepancy entry that quotes figures is only honest if those
        # figures survive in `effects[]`. A note that describes the
        # contradiction but keeps one number has silently reconciled it, which
        # is the failure this catches.
        recorded_values = " ".join(
            str(e.get("Value") or "")
            for e in (row["_note"].get("effects") or [])
            if isinstance(e, dict)
        )
        dropped = []
        for match in QUOTED_NUMBER_RE.findall(limits):
            number = match.strip()
            bare = number.rstrip("%").strip()
            # Tolerate a thousands separator on either side of the comparison.
            if bare in recorded_values or bare.replace(",", "") in recorded_values.replace(",", ""):
                continue
            dropped.append(number)
        if dropped:
            unrecorded += 1
            f.gap(
                f"`{row['paper_id']}` describes a discrepancy in `limitations` but these figures are "
                f"absent from `effects[]`: {', '.join(sorted(dropped))}. Either restore them or stop "
                f"claiming a discrepancy."
            )
    stats["unrecorded_discrepancies"] = unrecorded

    # --- module coverage (informational) ---------------------------------
    by_module: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if row["modules"] == NOT_REPORTED:
            continue
        for module in str(row["modules"]).split("; "):
            by_module[module].append(row["paper_id"])
    uncovered = [m["id"] for m in taxonomy.get("modules") or [] if not by_module.get(m["id"])]
    unassigned = [r["paper_id"] for r in rows if r["modules"] == NOT_REPORTED]
    if uncovered:
        f.gap(
            f"{len(uncovered)} of {len(known_modules)} modules have no paper assigned: "
            f"{', '.join(uncovered)}."
        )
    if unassigned:
        f.gap(f"{len(unassigned)} papers have no module assignment yet.")
    stats["modules_covered"] = len(by_module)
    stats["modules_total"] = len(known_modules)
    stats["papers_unassigned"] = len(unassigned)

    # --- fill rates -------------------------------------------------------
    extracted = [r for r in rows if r["status"] == "extracted"]
    if len(extracted) >= MIN_ROWS_FOR_FILL_VERDICT:
        for key in ("design", "sample", "key_finding", "gap"):
            filled = sum(1 for r in extracted if r[key] not in (NOT_REPORTED, NOT_APPLICABLE))
            rate = filled / len(extracted) * 100
            if rate < 50:
                f.gap(f"Column `{key}` is under 50% filled ({rate:.0f}%) — reconsider keeping it.")
    else:
        f.gap(
            f"Fill-rate verdicts suppressed: only {len(extracted)} of {len(rows)} papers are "
            f"extracted (need {MIN_ROWS_FOR_FILL_VERDICT})."
        )
    stats["extracted"] = len(extracted)
    stats["not_extracted"] = len(rows) - len(extracted)

    # --- metadata completeness (informational) ---------------------------
    no_doi = [r["paper_id"] for r in rows if r["doi"] == NOT_REPORTED]
    unverified_venue = [r["paper_id"] for r in rows if UNVERIFIED in r["venue"]]
    no_type = [r["paper_id"] for r in rows if r["type"] == NOT_REPORTED]
    if no_doi:
        f.gap(f"{len(no_doi)} entries have no DOI in metadata.json.")
    if unverified_venue:
        f.gap(f"{len(unverified_venue)} entries carry an unverified venue: {', '.join(unverified_venue)}.")
    if no_type:
        f.gap(f"{len(no_type)} entries have no publication type recorded.")
    stats.update(no_doi=len(no_doi), unverified_venue=len(unverified_venue), no_type=len(no_type))

    return stats


# --- rendering ------------------------------------------------------------

def md_cell(value: str) -> str:
    """Escape a value for a Markdown table cell."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_matrix(rows: list[dict], quotes: list[dict], effects: list[dict], generated: str, taxonomy: dict) -> str:
    by_module: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if row["modules"] == NOT_REPORTED:
            continue
        for module in str(row["modules"]).split("; "):
            by_module[module].append(row["paper_id"])

    section_name = {s["id"]: s["name"] for s in taxonomy.get("sections") or []}
    module_of = {m["id"]: m for m in taxonomy.get("modules") or []}

    lines = [
        "---",
        "document-type: matrix",
        "generated-by: scripts/build_matrix.py",
        f"generated: {generated}",
        "---",
        "",
        "# Literature Review Matrix of BUDGIE",
        "",
        "**Generated file — do not edit.** Rebuild with `python3 scripts/build_matrix.py`.",
        "",
        f"- Corpus: **{len(rows)}** papers | **{sum(1 for r in rows if r['status'] == 'extracted')}** extracted, "
        f"**{sum(1 for r in rows if r['status'] != 'extracted')}** not extracted",
        "- Bibliographic source: `literature/paper-markdowns/metadata.json` (page-1 verified)",
        f"- Taxonomy: `config/taxonomy.yaml` — {len(module_of)} modules in {len(section_name)} outline sections",
        "- Extraction source: `review/notes/{stem}.md` (authored)",
        "- Column definitions and validation rules: `docs/standards/review-layout.md`",
        "",
        f"Long tables: [`data/papers.csv`](data/papers.csv) | [`data/screening.csv`](data/screening.csv) | "
        f"[`data/quotes.csv`](data/quotes.csv) ({len(quotes)}) | "
        f"[`data/effects.csv`](data/effects.csv) ({len(effects)}) | "
        f"[`data/themes.csv`](data/themes.csv) | [`validation.md`](validation.md)",
        "",
        "Per-paper notes: [`notes/`](notes/). Hand-written synthesis: [`synthesis/`](synthesis/).",
        "",
        "## Coverage by Module",
        "",
        "Counted from the `modules[]` assignment in each note. A module with no papers is a",
        "gap in the corpus, not a gap in the taxonomy.",
        "",
        "| Section | Module | Papers |",
        "| :--- | :--- | ---: |",
    ]
    for section in taxonomy.get("sections") or []:
        for module in taxonomy.get("modules") or []:
            if module.get("section") != section["id"]:
                continue
            stems = by_module.get(module["id"], [])
            lines.append(
                f"| {md_cell(section['name'])} | `{module['id']}` | {len(stems)} |"
            )
    lines += [
        "",
        "## All Papers",
        "",
        "| " + " | ".join(COLUMNS) + " |",
        "| " + " | ".join("---" for _ in COLUMNS) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_cell(row[c]) for c in COLUMNS) + " |")
    lines.append("")
    return "\n".join(lines)


def render_note_stub(row: dict) -> str:
    """A placeholder note for a paper that has not been read yet.

    Deliberately thin. The bibliographic block is real, so the stub doubles as a
    citation card, and it names the contract to follow. `build_matrix.py` writes
    this only when no note file exists and never rewrites one that does, so a stub
    is replaced by writing the real note as a whole new file.
    """
    meta = row["_meta"]
    out = [
        "---",
        f"paper_id: {row['paper_id']}",
        f"first_author: {json.dumps(row['first_author'], ensure_ascii=False)}",
        f"year: {row['year']}",
        f"title: {json.dumps(meta.get('title') or NOT_REPORTED, ensure_ascii=False)}",
        f"venue: {json.dumps(row['venue'], ensure_ascii=False)}",
        f"doi: {json.dumps(row['doi'], ensure_ascii=False)}",
        f"designation: {row['designation']}",
        "status: not extracted",
        "modules: []",
        "generated-by: scripts/build_matrix.py",
        "---",
        "",
        f"# {meta.get('title') or row['paper_id']}",
        "",
        f"`{row['paper_id']}` \u2014 {row['first_author']} ({row['year']}), *{row['venue']}*",
        "",
        "## Not extracted",
        "",
        "This paper is in the corpus but has not been read. Its bibliographic block above is",
        "page-1 verified; there is no extraction, so `modules[]` is empty and every matrix",
        "column that would come from the paper reads `Not reported`.",
        "",
        "To extract it, follow `skills/literature-review-summarizer.md` and write this whole",
        "file as a full note per `docs/standards/note-format.md`. This stub will not be",
        "rewritten by the builder, so replace it rather than editing it in place.",
        "",
        f"Conversion: [`{row['paper_id']}_marked.md`](../../literature/paper-markdowns/{row['paper_id']}_marked.md)",
        "",
    ]
    return "\n".join(out)


def render_validation(rows: list[dict], f: Findings, stats: dict, generated: str) -> str:
    lines = [
        "# Literature Review Matrix Validation",
        "",
        f"- Generated: **{generated}**",
        f"- Papers: **{len(rows)}** | extracted: **{stats.get('extracted', 0)}** | "
        f"not extracted: **{stats.get('not_extracted', 0)}**",
        f"- Errors: **{len(f.errors)}** | informational gaps: **{len(f.gaps)}**",
        "",
        "Regenerate with `python3 scripts/build_matrix.py --check` (exit 1 on any error).",
        "Rules are defined in `docs/standards/review-layout.md`.",
        "",
        "## Counts",
        "",
        "| Check | Count |",
        "| :--- | ---: |",
    ]
    for key, value in stats.items():
        lines.append(f"| `{key}` | {value} |")
    lines += ["", "## Errors", ""]
    lines += [f"1. {e}" for e in f.errors] if f.errors else ["None. Every rule passed."]
    lines += ["", "## Informational Gaps", ""]
    lines += [f"- {g}" for g in f.gaps] if f.gaps else ["None."]
    lines += ["", "## Corpus Composition", "", "| Year | Papers |", "| :--- | ---: |"]
    years = Counter(r["year"] for r in rows)
    for year in sorted(years, key=lambda y: (-int(y) if y.isdigit() else 0, y)):
        lines.append(f"| {year} | {years[year]} |")
    lines += ["", "| Designation | Papers |", "| :--- | ---: |"]
    for key, value in sorted(Counter(r["designation"] for r in rows).items()):
        lines.append(f"| {key} | {value} |")
    lines.append("")
    return "\n".join(lines)


def write_csv(path: Path, fieldnames: list[str], records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow(record)


def load_yaml(path: str | Path) -> dict:
    import yaml  # local import: only the builder needs it

    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the generated literature review matrix.")
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    ap.add_argument("--metadata", default=str(DEFAULT_METADATA))
    ap.add_argument("--config", default=str(DEFAULT_CONFIG))
    ap.add_argument("--out", default=str(DEFAULT_REVIEW / "literature-review-matrix.md"))
    ap.add_argument("--data", default=str(DEFAULT_REVIEW / "data"))
    ap.add_argument("--notes", default=str(DEFAULT_REVIEW / "notes"))
    ap.add_argument("--validation", default=str(DEFAULT_REVIEW / "validation.md"))
    ap.add_argument("--check", action="store_true", help="Validate only; write nothing, exit 1 on error.")
    args = ap.parse_args()

    metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8")).get("entries", {})
    taxonomy = load_yaml(args.config)
    sections = taxonomy.get("sections") or []
    taxonomy_modules = taxonomy.get("modules") or []
    section_name = {s["id"]: s["name"] for s in sections}
    module_section = {m["id"]: m.get("section") for m in taxonomy_modules}
    module_order = [m["id"] for m in taxonomy_modules]

    # A paper is the union of its conversion and its note, so a note with no
    # conversion still surfaces. Only a note that parses as `extracted` counts as
    # extraction; a stub is a placeholder, not evidence.
    notes: dict[str, dict] = {}
    marked: set[str] = set()
    for stem, md, note_path in corpus_paths(args.corpus, args.notes):
        marked.add(stem)
        note = load_note(note_path)
        if note:
            notes[stem] = note

    rows = assemble_rows(metadata, notes, marked, module_order, module_section, section_name)
    quotes, effects = collect_long_tables(rows)

    f = Findings()
    stats = validate(rows, f, taxonomy)

    if args.check:
        print(f"papers: {len(rows)}  extracted: {stats.get('extracted', 0)}  "
              f"modules: {stats.get('modules_covered', 0)}/{stats.get('modules_total', 0)}")
        print(f"errors: {len(f.errors)}  gaps: {len(f.gaps)}")
        for e in f.errors:
            print(f"  ERROR  {e}")
        for g in f.gaps:
            print(f"  gap    {g}")
        if not f.ok:
            raise SystemExit(1)
        return

    generated = datetime.now(timezone.utc).isoformat()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_matrix(rows, quotes, effects, generated, taxonomy), encoding="utf-8")

    data = Path(args.data)
    write_csv(data / "papers.csv", COLUMNS + ["tags"], rows)
    write_csv(
        data / "screening.csv",
        ["paper_id", "first_author", "year", "designation", "type", "status",
         "module_count", "modules", "has_doi", "venue_verified", "converted"],
        [
            {
                "paper_id": r["paper_id"],
                "first_author": r["first_author"],
                "year": r["year"],
                "designation": r["designation"],
                "type": r["type"],
                "status": r["status"],
                "module_count": 0 if r["modules"] == NOT_REPORTED else len(str(r["modules"]).split("; ")),
                "modules": r["modules"],
                "has_doi": "yes" if r["doi"] != NOT_REPORTED else "no",
                "venue_verified": "no" if UNVERIFIED in r["venue"] else "yes",
                "converted": "yes" if r["_marked"] else "no",
            }
            for r in rows
        ],
    )
    write_csv(
        data / "quotes.csv",
        ["paper_id", "text", "locator", "module"],
        quotes,
    )
    write_csv(
        data / "effects.csv",
        ["paper_id", "outcome", "metric", "value", "ci", "p", "locator"],
        [dict(e, ci=e.get("ci", ""), p=e.get("p", "")) for e in effects],
    )

    by_module: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if row["modules"] == NOT_REPORTED:
            continue
        for module in str(row["modules"]).split("; "):
            by_module[module].append(row["paper_id"])
    themes = [
        {
            "section": section_name.get(module_section.get(m["id"], ""), NOT_REPORTED),
            "module_id": m["id"],
            "module_name": m.get("name", ""),
            "papers": len(by_module.get(m["id"], [])),
            "paper_ids": "; ".join(by_module.get(m["id"], [])) or NOT_REPORTED,
        }
        for m in taxonomy_modules
    ]
    write_csv(data / "themes.csv", ["section", "module_id", "module_name", "papers", "paper_ids"], themes)

    # Notes are authored. Create a stub only for a paper that has none, and never
    # touch a file that already exists — an extraction is not this script's to
    # overwrite. Removing a note whose paper left the corpus is still correct,
    # because that is a stale artefact rather than someone's work.
    notes = Path(args.notes)
    notes.mkdir(parents=True, exist_ok=True)
    expected = {f"{row['paper_id']}.md" for row in rows}
    for stale in notes.glob("*.md"):
        if stale.name not in expected:
            stale.unlink()
    written = 0
    for row in rows:
        target = notes / f"{row['paper_id']}.md"
        if target.exists():
            continue
        target.write_text(render_note_stub(row), encoding="utf-8")
        written += 1

    Path(args.validation).write_text(render_validation(rows, f, stats, generated), encoding="utf-8")

    print(f"wrote {out.relative_to(REPO_ROOT)}  ({len(rows)} papers)")
    print(f"wrote {len(list(data.glob('*.csv')))} csv in {data.relative_to(REPO_ROOT)}  "
          f"({len(quotes)} quotes, {len(effects)} effects)")
    print(f"wrote {written} note stubs in {notes.relative_to(REPO_ROOT)}  "
          f"({len(rows) - written} authored notes left untouched)")
    print(f"wrote {Path(args.validation).relative_to(REPO_ROOT)}")
    print(f"errors: {len(f.errors)}  gaps: {len(f.gaps)}")
    for e in f.errors:
        print(f"  ERROR  {e}")
    if not f.ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
