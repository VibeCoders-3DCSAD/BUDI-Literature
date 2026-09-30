"""Build the generated literature review matrix and its long tables.

    python3 scripts/build_matrix.py            # build all outputs
    python3 scripts/build_matrix.py --check    # validate only, exit 1 on error

`docs/literature-review-matrix.md` is a generated view, not a database. It is
rebuilt from three sources, in this order of authority:

    literature/conversions/metadata.json   bibliographic metadata (page-1 verified)
    scores/index.json                      relevance tiers from config/modules.yaml
    literature/conversions/*_summarized.json  extraction

Nothing in the matrix is hand-written. To correct a value, edit the source above
and re-run. Schema and column definitions: docs/standards/matrix-format.md

Outputs:
    docs/literature-review-matrix.md   lean 17-column index, one row per corpus paper
    scores/quotes.json                 one record per extracted quotation
    scores/effects.json                one record per statistical result
    scores/matrix-validation.md        what passed, what failed, what is missing

Stdlib only — no pandas, and `.gitignore` ignores `*.csv`, so long tables are
JSON to match the rest of the committed generated outputs.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from common import DEFAULT_CONFIG, DEFAULT_CORPUS, DEFAULT_SCORES, REPO_ROOT, corpus_paths, load_summary

DEFAULT_MATRIX = REPO_ROOT / "docs" / "literature-review-matrix.md"
DEFAULT_METADATA = DEFAULT_CORPUS / "metadata.json"
DEFAULT_INDEX = DEFAULT_SCORES / "index.json"

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
WS = re.compile(r"\s+")

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


def paper_type(summary: dict, meta: dict) -> str:
    """Controlled type label, from the summary first, then metadata."""
    raw = summary.get("type") or meta.get("publication_type") or ""
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


def design_slug(study_design: str) -> str | None:
    """Map a free-text design label onto one controlled `method/` tag."""
    label = WS.sub(" ", (study_design or "").strip())
    if not label or label in (NOT_REPORTED, NOT_APPLICABLE):
        return None
    head = label.split(":")[0].split("(")[0].lower()
    haystack = f"{head} {label.lower()}"
    for tag, needles in DESIGN_METHODS:
        if any(needle in haystack for needle in needles):
            return tag
    return "other"


MAX_THEME_TAGS = 5


def build_tags(stem: str, scores: dict, thresholds: dict, summary: dict, meta: dict) -> str:
    """Controlled tags: modules over threshold, scope, method, status, quality.

    Theme tags are the top `MAX_THEME_TAGS` by score, not every module that
    clears the floor: broad reviews legitimately clear eighteen, and an
    eighteen-tag cell is the sparse-cell problem the matrix exists to avoid.
    The full per-module ranking stays in `scores/index.json`.
    """
    tags: list[str] = []
    floor = thresholds.get("supporting_min", 0.30)
    qualifying = [
        (module_id, score)
        for module_id, score in (scores.get("scores") or {}).items()
        if isinstance(score, (int, float)) and score >= floor
    ]
    qualifying.sort(key=lambda kv: (-kv[1], kv[0]))
    tags = [f"theme/{module_id}" for module_id, _ in qualifying[:MAX_THEME_TAGS]]
    extra = len(qualifying) - len(tags)
    if extra > 0:
        tags.append(f"theme/+{extra}more")

    scope = designation_of(stem)
    if scope != NOT_REPORTED:
        tags.append(f"scope/{scope}")

    method = design_slug(summary.get("study_design") or "")
    if method:
        tags.append(f"method/{method}")

    tags.append("status/not-extracted" if not summary else "status/extracted")

    if meta.get("venue_unverified") or not normalize_doi(str(meta.get("doi") or "")):
        tags.append("quality/metadata-partial")

    return "; ".join(tags)


def first_limitation(summary: dict) -> str:
    limits = summary.get("limitations") or []
    for item in limits:
        if isinstance(item, str) and item.strip():
            return cap(item)
    return NOT_REPORTED


def collect_long_tables(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Project per-paper quotes/effects into flat cross-paper records."""
    quotes: list[dict] = []
    effects: list[dict] = []
    for row in rows:
        summary = row["_summary"]
        for q in summary.get("quotes") or []:
            if not isinstance(q, dict):
                continue
            quotes.append({
                "paper_id": row["paper_id"],
                "text": WS.sub(" ", str(q.get("text") or "").strip()),
                "locator": str(q.get("locator") or NOT_REPORTED),
                "theme": str(q.get("theme") or NOT_REPORTED),
            })
        for e in summary.get("effects") or []:
            if not isinstance(e, dict):
                continue
            record = {
                "paper_id": row["paper_id"],
                "outcome": WS.sub(" ", str(e.get("outcome") or "").strip()),
                "metric": WS.sub(" ", str(e.get("metric") or "").strip()),
                "value": str(e.get("value") or NOT_REPORTED),
                "locator": str(e.get("locator") or NOT_REPORTED),
            }
            for optional in ("ci", "p"):
                if e.get(optional):
                    record[optional] = str(e[optional])
            effects.append(record)
    return quotes, effects


def validate(rows: list[dict], f: Findings, modules: dict, redundancy: dict) -> dict:
    """Apply every rule in docs/standards/matrix-format.md."""
    known_modules = set(modules)
    stats: dict = {}

    # --- DOI shape -------------------------------------------------------
    bad_doi = []
    for row in rows:
        # Validate both sides. The row renders metadata.json, but a summary can
        # carry its own DOI, and a malformed one must not slip through just
        # because the metadata value happens to be well-formed.
        for source, doi in (
            ("metadata", row["doi"]),
            ("summary", str(row["_summary"].get("doi") or "")),
        ):
            doi = doi.strip()
            if not doi or doi == NOT_REPORTED:
                continue
            if not DOI_RE.match(normalize_doi(doi)):
                bad_doi.append(f"{row['paper_id']} ({source}): `{doi}`")
    for item in bad_doi:
        f.error(f"Malformed DOI — {item}. Expected `10.NNNN/suffix` with no spaces.")
    stats["malformed_doi"] = len(bad_doi)

    # --- summary vs metadata agreement -----------------------------------
    # metadata.json is the citation authority, so a summary that disagrees is
    # wrong, not merely different. Checked on the normalized DOI so a
    # case difference or a doi.org prefix is not reported as a conflict.
    disagree = []
    for row in rows:
        s = row["_summary"]
        if not s:
            continue
        for field in ("year", "title", "doi"):
            a, b = row["_meta"].get(field), s.get(field)
            if not b:
                continue
            if field == "doi":
                if normalize_doi(str(a or "")) != normalize_doi(str(b)):
                    disagree.append(f"{row['paper_id']}.{field}: metadata `{a or NOT_REPORTED}` vs summary `{b}`")
            elif str(a or "").strip().lower() != str(b).strip().lower():
                disagree.append(f"{row['paper_id']}.{field}: metadata `{a or NOT_REPORTED}` vs summary `{b}`")
    for item in disagree:
        f.error(f"Summary disagrees with metadata.json — {item}. metadata.json wins; fix the summary.")
    stats["metadata_disagreement"] = len(disagree)

    # --- corpus / score resolvability ------------------------------------
    unmarked = [r["paper_id"] for r in rows if not r["_marked"]]
    for stem in unmarked:
        f.error(f"`{stem}` is in the matrix but has no `_marked.md` in the corpus.")
    unscored = [r["paper_id"] for r in rows if not r["_scored"]]
    for stem in unscored:
        f.error(
            f"`{stem}` has a conversion but no entry in scores/index.json — "
            f"run `python3 scripts/embed.py && python3 scripts/score.py`."
        )
    stats["unmarked"], stats["unscored"] = len(unmarked), len(unscored)

    # --- duplicates ------------------------------------------------------
    by_doi: dict[str, list[str]] = defaultdict(list)
    by_title: dict[str, list[str]] = defaultdict(list)
    by_author_year: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        # The "Not reported" sentinel is not a DOI: 42 entries lack one, and
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
        f.error(f"Stem year disagrees with metadata year — {item}. Rename the stem and re-run embed.py.")
    stats["year_mismatch"] = len(mismatched)

    # --- controlled vocabularies -----------------------------------------
    bad_type = [
        f"{r['paper_id']}: `{r['type']}`"
        for r in rows
        if r["type"] != NOT_REPORTED and r["type"] not in CONTROLLED_TYPES
    ]
    for item in bad_type:
        f.error(f"Uncontrolled `type` value — {item}. See matrix-format.md for the list.")
    stats["bad_type"] = len(bad_type)

    bad_theme: set[str] = set()
    bad_method: set[str] = set()
    known_methods = {tag for tag, _ in DESIGN_METHODS} | {"other"}
    for row in rows:
        for tag in row["tags"].split("; "):
            prefix, _, value = tag.partition("/")
            if not value:
                bad_theme.add(tag)
            elif prefix == "theme" and not value.startswith("+"):
                if value not in known_modules:
                    bad_theme.add(tag)
            elif prefix == "method" and value not in known_methods:
                bad_method.add(tag)
            elif prefix not in ("theme", "scope", "method", "status", "quality"):
                bad_theme.add(tag)
    for tag in sorted(bad_method):
        f.error(f"Tag `{tag}` is not a controlled `method/` value. See DESIGN_METHODS in build_matrix.py.")
    for tag in sorted(bad_theme):
        f.error(f"Tag `{tag}` is not a known theme, scope, status, or quality tag.")
    stats["bad_theme_tags"] = len(bad_theme)

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
        for e in row["_summary"].get("effects") or []:
            if isinstance(e, dict) and e.get("metric") and e.get("value"):
                key = (WS.sub(" ", str(e.get("outcome") or "").strip()).lower(), str(e["metric"]))
                effects_by_paper[row["paper_id"]][key].add(str(e["value"]))
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
            str(x) for x in (row["_summary"].get("limitations") or []) if isinstance(x, str)
        )
        if not DISCREPANCY_RE.search(limits):
            continue
        # A discrepancy entry that quotes figures is only honest if those
        # figures survive in `effects[]`. A summary that describes the
        # contradiction but keeps one number has silently reconciled it, which
        # is the failure this catches.
        recorded_values = " ".join(
            str(e.get("value") or "")
            for e in (row["_summary"].get("effects") or [])
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

    # --- redundancy (carried through from score.py) -----------------------
    for cluster in (redundancy or {}).get("clusters", []):
        f.gap(
            f"Near-duplicate cluster ({len(cluster['papers'])} papers, "
            f"max cosine {cluster.get('max_similarity', 0):.3f}): keep "
            f"`{cluster['keep']}`, cull {', '.join(cluster['cull'])}."
        )

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


COLUMNS = [
    "paper_id", "first_author", "year", "title", "venue", "doi", "type",
    "designation", "tier", "best_module", "relevance", "tags", "design",
    "sample", "key_finding", "gap", "status",
]


def row_sort_key(row: dict) -> tuple:
    year = row["year"]
    return (0 if year.isdigit() else 1, -int(year) if year.isdigit() else 0, row["paper_id"])


def assemble_rows(metadata: dict, index: dict, summaries: dict, marked: set[str]) -> list[dict]:
    papers = index.get("papers") or {}
    rows = []
    for stem in sorted(set(metadata) | set(papers)):
        meta = metadata.get(stem) or {}
        scored = papers.get(stem) or {}
        summary = summaries.get(stem) or {}
        doi = normalize_doi(str(meta.get("doi") or ""))
        rows.append({
            "paper_id": stem,
            "first_author": first_author(meta, stem),
            "year": str(meta.get("year") or NOT_REPORTED),
            "title": cap(meta.get("title") or NOT_REPORTED, 140),
            "venue": venue_of(meta),
            "doi": doi or NOT_REPORTED,
            "type": paper_type(summary, meta),
            "designation": designation_of(stem),
            "tier": scored.get("tier") or NOT_REPORTED,
            "best_module": scored.get("best_module") or NOT_REPORTED,
            "relevance": f"{scored['best_score']:.3f}" if isinstance(scored.get("best_score"), (int, float)) else NOT_REPORTED,
            "tags": build_tags(stem, scored, index.get("tiers") or {}, summary, meta),
            "design": cap(summary.get("study_design") or NOT_REPORTED),
            "sample": cap(summary.get("sample") or NOT_REPORTED),
            "key_finding": cap(summary.get("tldr") or NOT_REPORTED),
            "gap": first_limitation(summary),
            "status": "extracted" if summary else "not extracted",
            "_meta": meta,
            "_summary": summary,
            "_scored": bool(scored),
            "_marked": stem in marked,
        })
    rows.sort(key=row_sort_key)
    return rows


def render_matrix(rows: list[dict], generated: str, stats: dict) -> str:
    lines = [
        "---",
        "document-type: matrix",
        "generated-by: scripts/build_matrix.py",
        f"generated: {generated}",
        "---",
        "",
        "# Literature Review Matrix of BUDGIE",
        "",
        f"**Generated file — do not edit.** Rebuild with `python3 scripts/build_matrix.py`.",
        "",
        f"- Corpus: **{len(rows)}** papers | **{stats.get('extracted', 0)}** extracted, "
        f"**{stats.get('not_extracted', 0)}** not extracted",
        "- Bibliographic source: `literature/conversions/metadata.json` (page-1 verified)",
        "- Relevance source: `scores/index.json` (from `config/modules.yaml`)",
        "- Extraction source: `literature/conversions/{stem}_summarized.json`",
        "- Column definitions and validation rules: `docs/standards/matrix-format.md`",
        "",
        "Long evidence tables: [`quotes.json`](../scores/quotes.json) | "
        "[`effects.json`](../scores/effects.json) | "
        "[`matrix-validation.md`](../scores/matrix-validation.md)",
        "",
    ]

    # Theme view: a paper relevant to several leaves should be findable from any.
    by_module: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        if row["best_module"] != NOT_REPORTED:
            by_module[row["best_module"]].append(row)
    if by_module:
        lines += [
            "## By Theme",
            "",
            "Best-scoring module per paper. `scripts/score.py` produces the full",
            "per-module ranking in `scores/report.md`.",
            "",
            "| Module | Papers | Crucial | Supporting |",
            "| :--- | ---: | ---: | ---: |",
        ]
        for module_id in sorted(by_module, key=lambda m: (-len(by_module[m]), m)):
            members = by_module[module_id]
            crucial = sum(1 for r in members if r["tier"] == "crucial")
            supporting = sum(1 for r in members if r["tier"] == "supporting")
            lines.append(f"| `{module_id}` | {len(members)} | {crucial} | {supporting} |")
        lines.append("")

    lines += [
        "## All Papers",
        "",
        "| " + " | ".join(COLUMNS) + " |",
        "|" + "|".join([" --- "] * len(COLUMNS)) + "|",
    ]
    for row in rows:
        cells = []
        for col in COLUMNS:
            value = str(row[col]).replace("|", "\\|")
            cells.append(value)
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    return "\n".join(lines)


def render_validation(rows: list[dict], f: Findings, stats: dict, generated: str, tiers: dict) -> str:
    lines = [
        "# Literature Review Matrix Validation",
        "",
        f"- Generated: **{generated}**",
        f"- Papers: **{len(rows)}** | extracted: **{stats.get('extracted', 0)}** | "
        f"not extracted: **{stats.get('not_extracted', 0)}**",
        f"- Errors: **{len(f.errors)}** | informational gaps: **{len(f.gaps)}**",
        f"- Thresholds: crucial >= {tiers.get('crucial_min')}, supporting >= {tiers.get('supporting_min')}",
        "",
        "Regenerate with `python3 scripts/build_matrix.py --check` (exit 1 on any error).",
        "Rules are defined in `docs/standards/matrix-format.md`.",
        "",
    ]

    lines += ["## Counts", "", "| Check | Count |", "| :--- | ---: |"]
    for key, value in stats.items():
        lines.append(f"| `{key}` | {value} |")
    lines.append("")

    lines += ["## Errors", ""]
    if f.errors:
        lines += [f"1. {e}" for e in f.errors]
    else:
        lines.append("None. Every rule passed.")
    lines.append("")

    lines += ["## Informational Gaps", ""]
    if f.gaps:
        lines += [f"- {g}" for g in f.gaps]
    else:
        lines.append("None.")
    lines.append("")

    if not rows:
        lines += ["## Corpus", "", "No papers found.", ""]
    else:
        years = Counter(r["year"] for r in rows)
        designations = Counter(r["designation"] for r in rows)
        tiers_seen = Counter(r["tier"] for r in rows)
        lines += [
            "## Corpus Composition",
            "",
            "| Year | Papers |",
            "| :--- | ---: |",
        ]
        for year in sorted(years, key=lambda y: (-int(y) if y.isdigit() else 0, y)):
            lines.append(f"| {year} | {years[year]} |")
        lines += ["", "| Designation | Papers |", "| :--- | ---: |"]
        for key in sorted(designations):
            lines.append(f"| {key} | {designations[key]} |")
        lines += ["", "| Tier | Papers |", "| :--- | ---: |"]
        for key in sorted(tiers_seen):
            lines.append(f"| {key} | {tiers_seen[key]} |")
        lines.append("")

    return "\n".join(lines)


def load_yaml(path: str | Path) -> dict:
    import yaml  # local import: only the builder needs it, and score.py owns the rest

    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the generated literature review matrix.")
    ap.add_argument("--corpus", default=str(DEFAULT_CORPUS))
    ap.add_argument("--metadata", default=str(DEFAULT_METADATA))
    ap.add_argument("--index", default=str(DEFAULT_INDEX))
    ap.add_argument("--config", default=str(DEFAULT_CONFIG))
    ap.add_argument("--redundancy", default=str(DEFAULT_SCORES / "redundancy.json"))
    ap.add_argument("--out", default=str(DEFAULT_MATRIX))
    ap.add_argument("--quotes", default=str(DEFAULT_SCORES / "quotes.json"))
    ap.add_argument("--effects", default=str(DEFAULT_SCORES / "effects.json"))
    ap.add_argument("--validation", default=str(DEFAULT_SCORES / "matrix-validation.md"))
    ap.add_argument("--check", action="store_true", help="Validate only; write nothing, exit 1 on error.")
    args = ap.parse_args()

    metadata = json.loads(Path(args.metadata).read_text(encoding="utf-8")).get("entries", {})
    index = json.loads(Path(args.index).read_text(encoding="utf-8"))
    redundancy = json.loads(Path(args.redundancy).read_text(encoding="utf-8")) if Path(args.redundancy).exists() else {}

    config = load_yaml(args.config)
    modules = {m["id"]: m for m in (config.get("modules") or [])}
    tiers = index.get("tiers") or config.get("tiers") or {}

    summaries = {}
    marked: set[str] = set()
    for stem, md_path, json_path in corpus_paths(args.corpus):
        marked.add(stem)
        summaries[stem] = load_summary(json_path) or {}

    rows = assemble_rows(metadata, index, summaries, marked)
    if not rows:
        raise SystemExit(f"No papers found in {args.corpus} or {args.metadata}")

    f = Findings()
    stats = validate(rows, f, modules, redundancy)
    quotes, effects = collect_long_tables(rows)

    generated = datetime.now(timezone.utc).isoformat()
    validation_md = render_validation(rows, f, stats, generated, tiers)

    if not args.check:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(render_matrix(rows, generated, stats), encoding="utf-8")
        Path(args.quotes).write_text(
            json.dumps({"generated_at": generated, "count": len(quotes), "quotes": quotes},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        Path(args.effects).write_text(
            json.dumps({"generated_at": generated, "count": len(effects), "effects": effects},
                       ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        Path(args.validation).write_text(validation_md, encoding="utf-8")

    print(f"{len(rows)} papers | {stats.get('extracted', 0)} extracted | "
          f"{len(quotes)} quotes | {len(effects)} effects | "
          f"{len(f.errors)} errors | {len(f.gaps)} gaps")
    for e in f.errors[:20]:
        print(f"  ERROR  {e}")
    for g in f.gaps[:20]:
        print(f"  gap    {g}")
    if len(f.errors) > 20:
        print(f"  ... and {len(f.errors) - 20} more errors (see the validation report)")

    if args.check and not f.ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
