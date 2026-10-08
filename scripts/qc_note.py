#!/usr/bin/env python3
"""QC a single note pasted back from an outsourced extraction chat.

Usage:
    .venv/bin/python scripts/qc_note.py A--Lu-2025
    .venv/bin/python scripts/qc_note.py --path /tmp/note.md --stem A--Lu-2025
    .venv/bin/python scripts/qc_note.py --stdin --stem A--Lu-2025 < /tmp/note.md

This script is deliberately NOT part of `build_matrix.py`. The builder is the
authority for corpus-wide validation; this is the fast per-paper gate you run
while working through the handoff queue, before the full rebuild.

Three passes, in order:

  1. normalize  - repair damage that comes from copy/paste through a chat UI.
  2. depth gate - reject notes that validate but are too thin to be useful.
  3. scope      - report this paper's own errors and gaps.

normalize is the reason this exists. Pasted Markdown reliably arrives with
smart quotes, non-breaking spaces, and tables whose pipe count has drifted.
Each of those is invisible to a human reader and fatal to the parser.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "review" / "notes"
METADATA = ROOT / "literature" / "conversions" / "metadata.json"

# --- depth gate ------------------------------------------------------------
# Reference notes in this repo run 3,200-6,700 words with 15-152 evidence rows.
# These floors are set at the low end of that observed range, not at the median,
# so a genuinely shorter paper still passes. The escape hatch is documented
# absence, never padding: see the "sparse is allowed" case below.
MIN_WORDS = 2_500
MIN_EFFECT_ROWS = 12
MIN_QUOTE_ROWS = 8

# Documents the paper type whose notes are legitimately short. An institutional
# report is not an under-read journal article.
SHORT_FORM_TYPES = {"report", "institutional-report", "working-paper", "book-chapter"}

EVIDENCE_HEADER = "| Outcome | Metric | Value | CI | p | Locator |"
QUOTE_HEADER = "| Text | Locator | Module |"

REQUIRED_SECTIONS = [
    "## Summary",
    "## Method",
    "## Limitations and Gaps",
    "## Statistical Evidence",
    "## Quotes",
]

# Modules that must exist in the taxonomy; resolved from the validator so this
# script cannot drift out of sync with it.
TAXONOMY = ROOT / "config" / "taxonomy.yaml"


# --------------------------------------------------------------------------
# pass 1: normalize
# --------------------------------------------------------------------------

SMART = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "′": "'", "″": '"',
    "–": "-", "—": "-", "‒": "-", "―": "-",
    "…": "...", " ": " ", " ": " ", " ": " ",
    "​": "", "‌": "", "‍": "", "﻿": "",
    "−": "-", "×": "x",
}


def normalize(text: str) -> tuple[str, list[str]]:
    """Repair paste damage. Returns (clean_text, list_of_repairs_made)."""
    repairs: list[str] = []

    original = text
    for bad, good in SMART.items():
        if bad in text:
            text = text.replace(bad, good)
    if text != original:
        repairs.append("smart punctuation / nbsp / zero-width normalized")

    # A chat may re-wrap a fenced block, so strip any wrapper the user pasted
    # along with the note itself.
    fence = re.match(r"^\s*```(?:markdown|md)?\s*\n(.*?)\n?```\s*$", text, re.S)
    if fence:
        text = fence.group(1) + "\n"
        repairs.append("fenced code wrapper stripped")

    # Unify line endings and drop trailing whitespace.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))

    # Collapse 3+ blank lines to one blank line.
    text = re.sub(r"\n{3,}", "\n\n", text)
    if text != original:
        repairs.append("whitespace collapsed")

    # --- table repair ------------------------------------------------------
    # Two failure modes matter:
    #   (a) a row whose cell count differs from the header's, which the parser
    #       drops silently -- the most damaging one, because it loses findings;
    #   (b) an unescaped `|` inside a cell, which shifts every later column.
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        # Find this table's header to know the expected column count.
        header_cols = None
        for j in range(i, max(-1, i - 4), -1):
            if lines[j].startswith("|") and not re.match(r"^\|\s*:?-+", lines[j]):
                header_cols = lines[j].count("|") - 1
                break
        if not header_cols:
            continue
        if i > 0 and not (lines[i - 1].startswith("|") or lines[i - 1] == ""):
            continue  # not a table row after a header

        cells = line.split("|")[1:-1]
        if len(cells) == header_cols:
            continue
        if len(cells) > header_cols:
            # An unescaped pipe inside a cell: fold the surplus back into the
            # widest cell rather than dropping data.
            merged = cells[header_cols - 1] + "|" + "|".join(cells[header_cols - 1:])
            cells = cells[: header_cols - 1] + [merged]
            repairs.append(f"line {i + 1}: extra pipe folded into last cell")
        else:
            repairs.append(
                f"line {i + 1}: SHORT row ({len(cells)}/{header_cols} cells) -- "
                "check this row, findings may be lost"
            )
        lines[i] = "|" + "|".join(f" {c.strip()} " for c in cells) + "|"
    text = "\n".join(lines)

    return text, repairs


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def section(text: str, heading: str) -> str | None:
    m = re.search(
        r"^" + re.escape(heading) + r"[ \t]*\n(.*?)(?=^## |\Z)", text, re.M | re.S
    )
    return m.group(1) if m else None


def count_rows(block: str) -> int:
    """Data rows in a markdown table, excluding header and separator."""
    if block is None:
        return 0
    first = block.strip().split("\n")[0].strip().lower()
    if first.startswith("not reported") or first.startswith("not applicable"):
        return 0
    rows = 0
    for line in block.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|\s*:?-{2,}", line):
            continue
        rows += 1
    return max(0, rows - 1)  # discount the header row


def is_documented_absence(block: str | None) -> bool:
    """True when the note explicitly justifies a sparse table.

    This is the escape hatch the plan called for: a paper that genuinely
    reports no outcome statistics must be allowed to say so. The bar is that
    it *says so*, not that the table is long.
    """
    if block is None:
        return False
    # Prose either leads the section ("Not reported. <why>") or states the
    # absence inside the first sentences before any table begins. Accept both,
    # but require the words to actually be there -- an empty table is not an
    # absence statement.
    head = " ".join(block.strip().split("\n")[:4]).lower()
    if "|" in head:
        head = head.split("|", 1)[0]
    return ("not reported" in head or "not applicable" in head
            or "no outcome statistics" in head
            or "reports no statistic" in head)


def load_module_ids() -> set[str]:
    text = TAXONOMY.read_text(encoding="utf-8")
    return set(re.findall(r"^\s*-\s*id:\s*([a-z_]+)", text, re.M))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stem", nargs="?", help="paper_id, e.g. A--Lu-2025")
    ap.add_argument("--path", type=Path, help="read the note from this path")
    ap.add_argument("--stdin", action="store_true", help="read the note from stdin")
    ap.add_argument("--write", action="store_true",
                    help="write the normalized text back to review/notes/{stem}.md")
    ap.add_argument("--min-words", type=int, default=MIN_WORDS)
    ap.add_argument("--min-effects", type=int, default=MIN_EFFECT_ROWS)
    ap.add_argument("--min-quotes", type=int, default=MIN_QUOTE_ROWS)
    args = ap.parse_args()

    if not args.stem:
        ap.error("stem is required (or pass --stem)")
    stem = args.stem

    if args.path:
        raw = args.path.read_text(encoding="utf-8")
        src = str(args.path)
    elif args.stdin:
        raw = sys.stdin.read()
        src = "<stdin>"
    else:
        target = NOTES / f"{stem}.md"
        if not target.exists():
            print(f"FAIL  no note at {target}")
            return 2
        raw = target.read_text(encoding="utf-8")
        src = str(target)

    problems: list[str] = []
    notes: list[str] = []

    # A generated stub is not a note and has nothing to QC. build_matrix.py
    # writes one for every paper with no authored note, so this is the expected
    # state for the whole un-extracted queue -- report it and stop.
    if "status: not extracted" in raw or "status: stub" in raw:
        print(f"=== qc_note: {stem} ===")
        print("STUB  not extracted yet -- nothing to check.")
        return 0

    # ---- pass 1: normalize ------------------------------------------------
    text, repairs = normalize(raw)
    for r in repairs:
        notes.append(f"normalized: {r}")

    # ---- structural checks ------------------------------------------------
    if not text.startswith("---"):
        problems.append("no YAML frontmatter: file must start with `---`")
    if "status: extracted" not in text:
        problems.append("frontmatter lacks `status: extracted`")

    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    pid = None
    if fm:
        pidm = re.search(r"^paper_id:\s*(\S+)", fm.group(1), re.M)
        pid = pidm.group(1) if pidm else None
        if pid and pid != stem:
            problems.append(f"paper_id `{pid}` != expected `{stem}`")
    else:
        problems.append("frontmatter is not closed by a second `---`")

    for h in REQUIRED_SECTIONS:
        if section(text, h) is None:
            problems.append(f"missing required section `{h}`")

    method = section(text, "## Method")
    if method is not None:
        if "**Design.**" not in method:
            problems.append("`## Method` lacks a `**Design.**` line")
        if "**Sample.**" not in method:
            problems.append("`## Method` lacks a `**Sample.**` line")

    limits = section(text, "## Limitations and Gaps")
    if limits is not None and not limits.strip().startswith("-"):
        problems.append("`## Limitations and Gaps` needs at least one `-` bullet")

    ev = section(text, "## Statistical Evidence")
    qt = section(text, "## Quotes")

    def has_header(block: str | None, header: str) -> bool:
        """Match the fixed header row, ignoring cell padding.

        A chat commonly rewrites `| Outcome | Metric |` as `|Outcome|Metric|`.
        That is still the same header, so compare normalized cells rather than
        raw text.
        """
        if block is None:
            return False
        want = [c.strip() for c in header.strip("|").split("|")]
        for line in block.splitlines():
            if not line.startswith("|"):
                continue
            got = [c.strip() for c in line.strip().strip("|").split("|")]
            if got == want:
                return True
        return False

    if ev is not None and not has_header(ev, EVIDENCE_HEADER):
        problems.append("Statistical Evidence header must be exactly "
                        "`| Outcome | Metric | Value | CI | p | Locator |`")
    if qt is not None and not has_header(qt, QUOTE_HEADER):
        problems.append("Quotes header must be exactly "
                        "`| Text | Locator | Module |`")

    # ---- module ids -------------------------------------------------------
    valid = load_module_ids()

    def clean_cell(c: str) -> str:
        # A cell pasted from a chat can carry a trailing Markdown escape or a
        # stray backtick, so trim whitespace, backticks, and backslashes.
        return c.strip().strip("`").strip().rstrip("\\").strip().strip("`").strip()

    def module_of(row: str) -> str:
        cells = row.split("|")[1:-1]
        return clean_cell(cells[-1]) if cells else ""

    declared = re.search(r"^modules:\s*\[(.*?)\]", fm.group(1) if fm else "", re.M)
    if declared:
        for mid in [clean_cell(x) for x in declared.group(1).split(",") if x.strip()]:
            if mid not in valid:
                problems.append(f"unknown module id `{mid}` (typo? see config/taxonomy.yaml)")
    for row in (qt or "").split("\n"):
        row = row.strip()
        if not row.startswith("|") or re.match(r"^\|\s*:?-{2,}", row):
            continue
        mid = module_of(row)
        if mid and mid != "Module" and mid not in valid:
            problems.append(f"Quotes table uses unknown module id `{mid}`")

    # ---- forbidden placeholders ------------------------------------------
    for bad, label in [
        (r"\bLorem ipsum\b", "Lorem ipsum"),
        (r"\bTBD\b", "TBD"),
        (r"\bTODO\b", "TODO"),
        (r"\[unclear\]", "[unclear]"),
        (r"\bunknown\b", "unknown"),
        (r"\bN/A\b", "N/A"),
    ]:
        if re.search(bad, text, re.I):
            problems.append(f"contains forbidden placeholder `{label}`")

    # ---- quotes: verbatim discipline -------------------------------------
    if qt:
        for line in qt.split("\n"):
            line = line.strip()
            if not line.startswith("|") or re.match(r"^\|\s*:?-{2,}", line):
                continue
            cells = line.split("|")[1:-1]
            if len(cells) != 3:
                continue
            text_cell, _, module_cell = (clean_cell(c) for c in cells)
            if text_cell in ("Text", ""):
                continue
            body = text_cell.strip('"').strip()
            if len(body.split()) > 40:
                problems.append(f"quote exceeds 40 words: \"{body[:60]}...\"")
            if module_cell and module_cell != "Module" and module_cell not in valid:
                problems.append(f"quote module `{module_cell}` is not a taxonomy id")

    # ---- pass 2: depth gate ----------------------------------------------
    words = len(text.split())
    n_ev, n_qt = count_rows(ev), count_rows(qt)
    sparse_ok = is_documented_absence(ev)

    # Genre discount. An institutional report or a short conference paper is
    # legitimately shorter than a 30-page journal article, so the word floor
    # scales to the form rather than punishing it for being what it is. The
    # evidence-row floor never moves: that is the part that measures whether
    # the results section was actually read.
    ptype = ""
    if fm:
        tm = re.search(r"^type:\s*(.+)$", fm.group(1), re.M)
        ptype = tm.group(1).strip().strip("\"'").lower() if tm else ""
    short_form = ptype in SHORT_FORM_TYPES or "report" in ptype
    word_floor = int(args.min_words * 0.6) if short_form else args.min_words

    if words < word_floor:
        if not sparse_ok:
            problems.append(
                f"TOO THIN: {words} words < {word_floor}"
                + (f" (discounted for `{ptype}`)" if short_form else "")
                + ", and the evidence table is not a documented absence"
            )
        else:
            notes.append(f"sparse but documented: {words} words with a justified "
                         "empty evidence table (allowed)")
    elif words < args.min_words and short_form:
        notes.append(f"short form ({ptype}): {words} words, "
                     f"floor discounted to {word_floor} -- accepted")
    if n_ev < args.min_effects and not sparse_ok:
        problems.append(
            f"TOO THIN: {n_ev} evidence rows < {args.min_effects}. Read the whole "
            "results section. If the paper truly reports no outcome statistics, "
            "replace the table with `Not reported.` plus one sentence of evidence "
            "for that claim -- do not pad with design parameters."
        )
    if n_qt < args.min_quotes and not is_documented_absence(qt):
        problems.append(f"TOO THIN: {n_qt} quote rows < {args.min_quotes}")

    # ---- report -----------------------------------------------------------
    print(f"=== qc_note: {stem} ===")
    print(f"source   {src}")
    print(f"size     {words} words, {n_ev} evidence rows, {n_qt} quotes")
    for n in notes:
        print(f"note     {n}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  FAIL  {p}")
    else:
        print("\nPASS  no structural or depth problems found.")
        print("      Still run: .venv/bin/python scripts/build_matrix.py --check")

    if args.write and not problems and text != raw:
        (NOTES / f"{stem}.md").write_text(text, encoding="utf-8")
        print(f"\nwrote normalized note to {NOTES / f'{stem}.md'}")

    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
