# BUDI-Literature — Agent Guide

**Thesis**: Development of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning. The project was named BUDI, then TAYA; Topical Outline V4 (09.26) and Chapter 2 V3 (09.26) use **BUDGIE**.
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **self-contained RRL corpus and matrix generator** for the BUDI thesis. It contains:
- Curated paper corpus (markdown conversions + structured summaries)
- The bibliographic authority for that corpus (`metadata.json`)
- PDF fetch and conversion pipeline
- The module taxonomy that organises the corpus (`config/taxonomy.yaml`)
- A generated review matrix, long evidence tables, and per-paper notes (`review/`)

It does **not** contain thesis documents, application code, or ML model implementations — those live in **BUDI-Base** (documentation) and **BUDI-App** / **BUDI-ML** (code) respectively.

**There is no scoring pipeline.** Relevance scores, tiers, embeddings, and a corpus manifest were removed on 2026-09-30. A paper's outline modules are assigned during extraction, and coverage is a count of those assignments. Do not reintroduce a scoring stage.

---

## Coding Standards

| Standard | Location |
|----------|----------|
| RRL naming conventions | `docs/standards/rrl-naming-conventions.md` |
| RRL processing workflow | `docs/standards/rrl-workflow.md` |
| RRL summary format | `docs/standards/summary-format.md` |
| Generated review layout and matrix columns | `docs/standards/review-layout.md` |
| Documentation formatting | `docs/standards/documentation-format.md` |

Enforcement: Follow the naming conventions for all paper files. Use the summary JSON schema for all summaries. The design rule is **edits go in `config/` and the summaries, never in `scripts/build_matrix.py`**.

---

## Top-Level Directory Layout

```
BUDI-Literature/
  AGENTS.md              # This file
  INDEX.md               # Master navigation index
  README.md              # Project overview and quick start
  requirements.txt       # Python dependencies
  config/                # taxonomy.yaml — module namespace (single source of truth)
  scripts/               # fetch, convert, and matrix generation
  literature/            # Corpus: conversions, bucket, papers (gitignored)
  review/                # Generated matrix, data/*.csv, notes/, synthesis/
  docs/                  # Standards and documentation
  skills/                # Agent-facing extraction contracts
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| `config/taxonomy.yaml` | The 20 module ids across the 5 Topical Outline V4 sections — the single source of truth for what modules exist |
| `docs/standards/rrl-workflow.md` | Full processing workflow (fetch → convert → summarize → build → verify) |
| `docs/standards/summary-format.md` | JSON schema for `_summarized.json` files, including `modules[]` and `module_rationale` |
| `docs/standards/review-layout.md` | Generated `review/` tree, matrix columns, tag namespace, validator rules |
| `docs/standards/rrl-naming-conventions.md` | File naming rules for the corpus |
| `docs/standards/documentation-format.md` | Shared documentation formatting rules |
| `literature/conversions/metadata.json` | Bibliographic sidecar: verified titles, authors, venues, DOIs, keyed by source-PDF SHA-256 |
| `review/literature-review-matrix.md` | **Generated** 15-column index over the whole corpus — never hand-edit |
| `review/data/themes.csv` | **Generated** per-module coverage tally — read before requesting new sources |
| `review/data/screening.csv` | **Generated** intake triage queue |
| `review/data/quotes.csv` | **Generated** one record per extracted quotation |
| `review/data/effects.csv` | **Generated** one record per statistical result |
| `review/validation.md` | **Generated** validation errors and informational gaps |
| `review/notes/{stem}.md` | **Generated** one readable note per paper |
| `review/synthesis/` | **Hand-written** cross-paper synthesis — the only authored part of `review/` |
| `skills/literature-review-summarizer.md` | Extraction contract for `_summarized.json`, including the module assignment rules |
| `docs/NEW-SCOPE-SOURCES.md` | Prioritised manual-download list. Its prioritization predates the current taxonomy and needs a re-pass |

`docs/OUTLINE-V4-COVERAGE_OLD.md` is the retired hand-maintained coverage view; `review/data/themes.csv` now generates the same figure from live assignments. The docs under `docs/standards/batch-*-algorithm-screening.md`, `docs/standards/bucket-bucket-triage.md`, `docs/standards/migration-workflow.md`, and `docs/notes-to-improve-lrm.md` are **historical records** of completed work, not current specs.

---

## Corpus Structure

Every curated paper has up to three files:

| File | Location |
|------|----------|
| `{stem}.pdf` | `literature/papers/` (fetched, gitignored) |
| `{stem}_marked.md` | `literature/conversions/` |
| `{stem}_summarized.json` | `literature/conversions/` (same folder as `_marked.md`) |

Plus one corpus-wide file: `literature/conversions/metadata.json`.

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.
Full reference: `docs/standards/rrl-naming-conventions.md`

### Corpus Layout

Conversions live flat in `literature/conversions/`, one `{stem}_marked.md` per
paper, named by its bibliographically correct first author. Do not reintroduce
per-intake subdirectories: `scripts/common.py` discovers the corpus with
`rglob("*_marked.md")`, and a nested layout only obscures the corpus (93 papers as of 2026-09-30) when
auditing stems, duplicates, or citation metadata.

Intake provenance is tracked in git history, not in the directory layout. The
earlier `batch-1..6` and `batch-7` conversion working files were flattened or
removed as superseded.

---

## Processing Pipeline

### 1. Fetch PDFs

```bash
# From a sibling directory:
python3 scripts/fetch_pdfs.py --source local --path ../BUDI-Base/archived-literature/papers/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/archives/

# From remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

### 2. Convert

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
# Then move the pair into the corpus root:
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/
```

### 3. Summarize

Use an AI agent to fill `_summarized.json` (schema: `docs/standards/summary-format.md`,
extraction contract: `skills/literature-review-summarizer.md`). The two fields
that matter most are `modules[]` — the taxonomy ids this paper covers, each with
a `module_rationale` clause — and the one-record-per-result `effects[]` /
`quotes[]` tables.

### 4. Build the review matrix

```bash
python3 scripts/build_matrix.py         # regenerate the whole review/ tree
python3 scripts/build_matrix.py --check # validate only, exit 1 on any error
```

### 5. Verify and read coverage

```bash
python3 scripts/build_matrix.py --check
```

Gaps are informational; errors mean the corpus contradicts itself. To decide what
to source next, read `review/data/themes.csv` — a module with zero papers is a
gap in the corpus, not a reason to loosen an assignment.

---

## Script Reference

| Script | Purpose |
|--------|---------|
| `scripts/fetch_pdfs.py` | Fetch PDFs from local archive or remote source |
| `scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata and page-aware extraction |
| `scripts/count_pdf_pages.py` | List PDFs with page counts (optional filtering) |
| `scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |
| `scripts/build_matrix.py` | Build the generated review tree, long tables, and validation report |
| `scripts/common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing) |

---

## Python Environment

A `.venv/` exists (gitignored). Install dependencies from the repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Important Gotchas

- **PDFs are not committed.** Use `scripts/fetch_pdfs.py` to obtain them. The matrix build operates entirely on markdown conversions — PDFs are only needed for conversion.
- **`review/` is generated except `review/synthesis/`.** Never hand-edit the matrix, the CSVs, or the notes: `scripts/build_matrix.py` overwrites them from `metadata.json`, the `_summarized.json` files, and `config/taxonomy.yaml`. To change a value, fix the source and rebuild. Run `build_matrix.py --check` after any extraction; it exits 1 on an error.
- **A rename is cheap now, a module rename is not.** Corpus stems are keys in `metadata.json`; renaming one means editing the sidecar too. Renaming or removing a *module* id is worse: the ids live inside every `_summarized.json`, so the corpus keeps reporting the old namespace until summaries are retagged. `--check` reports retired vocabulary as a gap rather than an error so you can size the retag first.
- **Stems name the first author, but source PDF filenames often do not.** Seven corpus stems were built from filenames and turned out to name a later author. Each was corrected on 2026-09-26 after reading page 1. Verify any stem against the PDF before citing it. `literature/conversions/metadata.json` is the citation authority and records verification per entry (all 93 entries verified from page 1 as of 2026-09-30; the file wraps them under an `entries` key, so count there, not at the top level).
- **A paper that contradicts itself is not an extraction bug.** `A--Aldrees-2025` reports different headline figures in its abstract and its conclusion. Keep both with their locators and record the discrepancy in `limitations`; the validator flags the conflict and deliberately does not choose.
- **Never score or rank a paper.** Assigning a module says where the paper sits in the outline, not how good it is. `high`/`medium`/`low` relevance, weights, and tiers were all retired with `config/modules.yaml`.
- **Batch structure is by intake run**, not by topic. Re-organize by topic when the topical outline is finalized.
- **`topic_tags`, `topic_relevance`, and `quotes[].theme` are retired.** They are still *read* so pre-taxonomy summaries are not lost, and any that survive are reported as gaps telling you to re-tag into `modules[]`. Do not write them.
