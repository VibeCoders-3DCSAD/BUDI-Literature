# BUDI-Literature

Self-contained Review of Related Literature (RRL) corpus and matrix generator for
the BUDGIE thesis.

A paper enters the corpus as a PDF, becomes a markdown conversion and an authored
note, and is then projected into a generated review matrix. There is no scoring
stage: which outline modules a paper belongs to is decided during extraction,
and the matrix is a count of those assignments.

## What's Here

| Directory / File | Purpose |
| :--- | :--- |
| `config/taxonomy.yaml` | **The single source of truth** for the module namespace: 20 modules across the 5 Topical Outline V4 sections |
| `literature/conversions/` | The curated corpus, flat, one `{stem}_marked.md` per paper, plus `metadata.json`, the page-1 verified bibliographic authority |
| `review/notes/` | **Authored** one extraction note per paper, `review/notes/{stem}.md` — the source of truth for everything except the bibliographic block |
| `review/` | **Generated** matrix, CSV tables, and `validation.md`; `review/notes/` and `review/synthesis/` are authored |
| `literature/bucket/` | Raw candidate PDFs for intake |
| `literature/papers/` | Fetched source PDFs (gitignored; use `scripts/fetch_pdfs.py`) |
| `scripts/` | Fetch, convert, and matrix generation |
| `skills/` | Agent-facing extraction contract for the note at `review/notes/{stem}.md` |
| `docs/standards/` | Naming conventions, note schema, review layout, workflow documentation |

Intake provenance lives in git history; earlier per-batch subdirectories were flattened or removed as superseded.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

A paper enters the corpus as a PDF, becomes a markdown conversion and an authored
note, and is then projected into a generated review matrix. There is no scoring
stage: which outline modules a paper belongs to is decided during extraction,
and the matrix is a count of those assignments.

### 1. Fetch PDFs

```bash
# From a sibling directory (e.g. BUDI-Base/archived-literature/papers/):
python3 scripts/fetch_pdfs.py --source local --path ../BUDI-Base/archived-literature/papers/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/pdf-archives/

# From a remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

PDFs land in `literature/papers/` (gitignored). SHA-256 hashes are printed for each file.

Optional inspection before converting:

```bash
python3 scripts/count_pdf_pages.py literature/papers/
python3 scripts/check_dupe_pdfs.py literature/papers/ --cascade
```

### 2. Convert

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
```

Produces `{stem}_marked.md` (with metadata frontmatter). Move it into the corpus
root:

```bash
mv literature/papers/{stem}_marked.md literature/conversions/
```

### 3. Extract into a note

Use an AI agent to write `review/notes/{stem}.md`, the authored extraction record
for the paper. Note grammar: `docs/standards/note-format.md`. Extraction
contract, including the module assignment rules:
`skills/literature-review-summarizer.md`.

The one field that cannot be skipped is frontmatter `modules[]` — the ids from
`config/taxonomy.yaml` that this paper genuinely covers, each with a
`module_rationale` clause. The agent replaces the whole file, so it never edits a
generated stub in place.

### 4. Build the matrix

```bash
python3 scripts/build_matrix.py           # regenerate review/
python3 scripts/build_matrix.py --check   # validate only; exit 1 on any error
```

Reads `metadata.json`, every `review/notes/*.md`, and `config/taxonomy.yaml`, then
writes `review/literature-review-matrix.md`, the five CSVs under `data/`, and
`validation.md` — plus a note stub for any paper that has no note. It never
overwrites an existing note.

The matrix is generated — never hand-edit it. Column definitions, the tag
namespace, and the validator rules are in `docs/standards/review-layout.md`.

## How coverage is computed

There is no scoring. A paper is assigned to zero or more taxonomy modules during
extraction, and the coverage tables count those assignments:

| Question | Answer |
| :--- | :--- |
| How many papers support `sarima`? | Count rows in `review/data/themes.csv` |
| Which papers are in `model_algorithm_integration`? | `papers` / `paper_ids` in `themes.csv`, or `data/screening.csv` |
| What does a paper report? | `review/notes/{stem}.md` |
| What are the exact figures? | `review/data/effects.csv` |
| What did they say, verbatim? | `review/data/quotes.csv` |

No relevance score, weight, tier, or priority exists anywhere in the pipeline. A
module with no papers is a gap in the corpus, not a reason to loosen assignment.

## Adapting when the thesis changes

The design rule is: **edits go in `config/`, never in code.**

| Change | What to do |
|--------|-----------|
| New/renamed/removed module | Edit `config/taxonomy.yaml` -> `python3 scripts/build_matrix.py` |
| A paper extracted or re-read | Rewrite `review/notes/{stem}.md` -> `python3 scripts/build_matrix.py` |
| A conversion added or changed | `python3 scripts/build_matrix.py` |
| A bibliographic correction | Edit `literature/conversions/metadata.json` -> `python3 scripts/build_matrix.py` |
| Topics come from a different outline | Replace `config/taxonomy.yaml`, then re-tag the `modules[]` frontmatter of existing notes |

Renaming a module is not a free operation: the ids are stored in every note's
frontmatter `modules[]` and in the `Module` column of each `## Quotes` table, so
a rename leaves the corpus reporting the old namespace until the notes are
retagged.

## Generated reference

| File | Purpose |
| :--- | :--- |
| `review/literature-review-matrix.md` | Generated 15-column index over the corpus |
| `review/data/papers.csv` | The same 15 columns plus a controlled `tags` column |
| `review/data/screening.csv` | Intake triage: status, module count, DOI and venue completeness |
| `review/data/quotes.csv` | One row per extracted quotation |
| `review/data/effects.csv` | One row per statistical result |
| `review/data/themes.csv` | Per-module coverage tally |
| `review/validation.md` | Errors and informational gaps from the last build |

Authored, never generated: `review/notes/{stem}.md` (one readable extraction note
per paper) and `review/synthesis/`.

## Notes

- The generated tree is committed so the corpus is browsable without running anything.
- Only `review/data/*.csv` is force-tracked; other `*.csv` outputs stay ignored.
- Batch structure is by intake run, not by topic. Re-organize by topic when the topical outline is finalized.
- Bibliographic metadata lives in `literature/conversions/metadata.json` (page-1 verified) and overrides note frontmatter. There is no `refs.bib`.
- Old topic codes (`1.A`-`14.C`) and the retired `topic_tags` / `topic_relevance` fields predate `config/taxonomy.yaml` and the note pipeline. Do not write them.

## Navigation

See [INDEX.md](INDEX.md) for the full repository index, and
[docs/standards/rrl-workflow.md](docs/standards/rrl-workflow.md) for the
step-by-step processing workflow.
