# Odin-Literature — Agent Guide

**Thesis**: Development of Odin: A Personal Finance Management Application for Filipino Working Young Adults Using Random Forest, LSTM, and Isolation Forest
**Group 4, III-DCSAD, University of Makati**

---

## Repository Role

This is the **self-contained RRL corpus and scoring repository** for the Odin thesis. It contains:
- Curated paper corpus (markdown conversions + structured summaries)
- PDF fetch, conversion, and scoring pipeline
- Module configuration for relevance scoring
- Generated scores (relevance, quality, redundancy)

It does **not** contain thesis documents, application code, or ML model implementations — those live in **Odin-Paper** (documentation) and **Odin-App** / **Odin-ML** (code) respectively.

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
Odin-Literature/
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
| `docs/standards/rrl-naming-conventions.md` | File naming rules for the corpus |
| `scores/report.md` | Human-readable ranked report |
| `scores/index.json` | Machine-readable per-paper scores |
| `scores/redundancy.json` | Near-duplicate clusters |
| `scores/validation.md` | Sanity check of automated scores vs existing annotations |

---

## Corpus Structure

Every curated paper has up to three files:

| File | Location |
|------|----------|
| `{stem}.pdf` | `literature/papers/` (fetched, gitignored) |
| `{stem}_marked.md` | `literature/conversions/batch-<N>/` |
| `{stem}_summarized.json` | `literature/conversions/batch-<N>/` (same folder as `_marked.md`) |

### File Prefix Convention

`L--` = local (Philippine), `I--` = international, `A--` = algorithm/system focus.
Full reference: `docs/standards/rrl-naming-conventions.md`

### Batch Structure

Conversions are organized by intake run: `literature/conversions/batch-1/` through `batch-6/`.
Start a new `batch-N` directory (next number) when adding a group of papers.

---

## Processing Pipeline

### 1. Fetch PDFs

```bash
# From a sibling directory:
python3 scripts/fetch_pdfs.py --source local --path ../Odin-Paper/literature/papers/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/archives/

# From remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

### 2. Convert

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
# Then move the pair into a batch directory:
mkdir -p literature/conversions/batch-N
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/batch-N/
```

### 3. Summarize

Use an AI agent to fill `_summarized.json` (schema: `docs/standards/summary-format.md`).

### 4. Score

```bash
python3 scripts/embed.py        # rebuild caches when conversions change
python3 scripts/score.py        # relevance/quality tiers, redundancy, validation
```

### 5. Adapt

Edit `config/modules.yaml` (module queries, weights, thresholds) → re-run `score.py`. No code changes needed.

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
- **Generated scores are committed** so the scored corpus is browsable without running anything.
- **Batch structure is by intake run**, not by topic. Re-organize by topic when the topical outline is finalized.
