# BUDI-Literature — Agent Guide

**Thesis**: Development of BUDGIE: A Personal Financial Management App Using SARIMA to Improve Financial Planning. The project was named BUDI, then TAYA; Topical Outline V4 (09.26) and Chapter 2 V3 (09.26) use **BUDGIE**.
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **self-contained RRL corpus and scoring repository** for the BUDI thesis. It contains:
- Curated paper corpus (markdown conversions + structured summaries)
- PDF fetch, conversion, and scoring pipeline
- Module configuration for relevance scoring
- Generated scores (relevance, quality, redundancy)

It does **not** contain thesis documents, application code, or ML model implementations — those live in **BUDI-Base** (documentation) and **BUDI-App** / **BUDI-ML** (code) respectively.

---

## Coding Standards

| Standard | Location |
|----------|----------|
| RRL naming conventions | `docs/standards/rrl-naming-conventions.md` |
| RRL processing workflow | `docs/standards/rrl-workflow.md` |
| RRL summary format | `docs/standards/summary-format.md` |

Enforcement: Follow the naming conventions for all paper files. Use the summary JSON schema for all summaries.

---

## Top-Level Directory Layout

```
BUDI-Literature/
  AGENTS.md              # This file
  README.md              # Project overview and quick start
  requirements.txt       # Python dependencies
  config/                # Module definitions (single source of truth)
  scripts/               # Processing pipeline
  literature/            # Corpus: conversions, bucket, papers (gitignored)
  scores/                # Generated outputs (committed)
  cache/                 # Regenerable embeddings/cache (gitignored)
  docs/                  # Standards and documentation
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| `config/modules.yaml` | Module definitions, weights, tier thresholds — the single source of truth for relevance |
| `docs/standards/rrl-workflow.md` | Full processing workflow (fetch → convert → summarize → score) |
| `docs/standards/summary-format.md` | JSON schema for `_summarized.json` files |
| `docs/standards/matrix-format.md` | Generated matrix columns, tag namespace, validator rules |
| `docs/standards/rrl-naming-conventions.md` | File naming rules for the corpus |
| `literature/conversions/metadata.json` | Bibliographic sidecar: verified titles, authors, venues, DOIs, keyed by source-PDF SHA-256 |
| `docs/OUTLINE-V4-COVERAGE.md` | Crucial/supporting paper counts per Outline V4 leaf — read before requesting new sources |
| `docs/NEW-SCOPE-SOURCES.md` | Prioritised manual-download list, re-prioritised against Outline V4 |
| `scores/report.md` | Human-readable ranked report |
| `scores/index.json` | Machine-readable per-paper scores |
| `docs/literature-review-matrix.md` | **Generated** 17-column index over the whole corpus — never hand-edit |
| `scores/quotes.json` | Generated: one record per extracted quotation |
| `scores/effects.json` | Generated: one record per statistical result |
| `scores/redundancy.json` | Near-duplicate clusters |
| `scores/validation.md` | Sanity check of automated scores vs existing annotations |
| `scores/matrix-validation.md` | Generated: matrix validation errors and informational gaps |
| `skills/literature-review-summarizer.md` | Extraction contract for `_summarized.json` (supersedes the retired 56-column matrix inserter) |

---

## Corpus Structure

Every curated paper has up to three files:

| File | Location |
|------|----------|
| `{stem}.pdf` | `literature/papers/` (fetched, gitignored) |
| `{stem}_marked.md` | `literature/conversions/` |
| `{stem}_summarized.json` | `literature/conversions/` (same folder as `_marked.md`) |

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.
Full reference: `docs/standards/rrl-naming-conventions.md`

### Corpus Layout

Conversions live flat in `literature/conversions/`, one `{stem}_marked.md` per
paper, named by its bibliographically correct first author. Do not reintroduce
per-intake subdirectories: `scripts/common.py` discovers the corpus with
`rglob("*_marked.md")`, and a nested layout only obscures the corpus (92 papers as of 2026-09-27) when
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
```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
# Then move the pair into the corpus root:
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/
```

### 3. Summarize

Use an AI agent to fill `_summarized.json` (schema: `docs/standards/summary-format.md`,
extraction contract: `skills/literature-review-summarizer.md`).

### 4. Score

```bash
python3 scripts/embed.py        # rebuild caches when conversions change
python3 scripts/score.py        # relevance/quality tiers, redundancy, validation
```

### 5. Build the matrix

```bash
python3 scripts/build_matrix.py         # regenerate matrix + quotes/effects + validation
python3 scripts/build_matrix.py --check # validate only, exit 1 on any error
```

### 6. Adapt

Edit `config/modules.yaml` (module queries, weights, thresholds) → re-run `score.py`, then `build_matrix.py`. No code changes needed.

---

## Script Reference

| Script | Purpose |
|--------|---------|
| `scripts/fetch_pdfs.py` | Fetch PDFs from local archive or remote source |
| `scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata and page-aware extraction |
| `scripts/count_pdf_pages.py` | List PDFs with page counts (optional filtering) |
| `scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |
| `scripts/embed.py` | Build/cache text, BERT embeddings, TF-IDF, BM25 |
| `scripts/score.py` | Score corpus against module queries |
| `scripts/manifest.py` | Build corpus manifest from conversions |
| `scripts/build_matrix.py` | Build the generated review matrix, long tables, and validation report |
| `scripts/common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing) |

---

## Python Environment

A `.venv/` exists (gitignored). Install dependencies from the repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

For CPU-only torch (smaller):
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## Important Gotchas

- **PDFs are not committed.** Use `scripts/fetch_pdfs.py` to obtain them. The scoring pipeline operates entirely on markdown conversions — PDFs are only needed for conversion.
- **`cache/` is regenerable.** Run `python3 scripts/embed.py --force` to rebuild. Only `scores/` and `literature/conversions/` are committed.
- **Old topic codes (1.A–14.C)** in `_summarized.json` files follow the previous thesis outline. The current module definitions in `config/modules.yaml` supersede them for scoring purposes.
- **Stems name the first author, but source PDF filenames often do not.** Seven corpus stems were built from filenames and turned out to name a later author. Each was corrected on 2026-09-26 after reading page 1. Verify any stem against the PDF before citing it. `literature/conversions/metadata.json` is the citation authority and records verification per entry (all 93 entries verified from page 1 as of 2026-09-30; the file wraps them under an `entries` key, so count there, not at the top level).
- **A rename invalidates the caches.** `embed.py` keys `cache/embeddings_stems.json` by stem, so renaming a conversion makes `score.py` fail with a `KeyError` on the old stem. Re-run `embed.py` after any rename, not just `score.py`.
- **`config/modules.yaml` was realigned to Outline V4 on 2026-09-26.** Measure corpus coverage against `docs/OUTLINE-V4-COVERAGE.md` before proposing new sources; three outline leaves currently have zero crucial-tier papers.
- **Generated scores are committed** so the scored corpus is browsable without running anything.
- **Batch structure is by intake run**, not by topic. Re-organize by topic when the topical outline is finalized.
- **`docs/literature-review-matrix.md` is generated.** Never hand-edit it: `scripts/build_matrix.py` overwrites it from `metadata.json`, `scores/index.json`, and the `_summarized.json` files. To change a value, fix the source and rebuild. Run `build_matrix.py --check` after any extraction; it exits 1 on an error.
- **A paper that contradicts itself is not an extraction bug.** `A--Aldrees-2025` reports different headline figures in its abstract and its conclusion. Keep both with their locators and record the discrepancy in `limitations`; the validator flags the conflict and deliberately does not choose.
