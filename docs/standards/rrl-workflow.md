# RRL Processing Workflow

Workflow for adding and processing literature in the Review of Related Literature.

All steps happen within **Odin-Literature**. No cross-repo transfers required.

## Steps

### 1. Fetch PDFs

Obtain source PDFs from a local archive or remote source:

```bash
# From a sibling directory (e.g. Odin-Paper/archived-literature/papers/):
python3 scripts/fetch_pdfs.py --source local --path ../Odin-Paper/archived-literature/papers/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/pdf-archives/

# From a remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

PDFs are placed in `literature/papers/` (gitignored). The script computes SHA-256 hashes for each PDF.

Optional: inspect fetched PDFs before converting:

```bash
python3 scripts/count_pdf_pages.py literature/papers/
python3 scripts/count_pdf_pages.py literature/papers/ --lte 20   # only short papers
python3 scripts/check_dupe_pdfs.py literature/papers/ --cascade  # find duplicates
```

### 2. Convert

Run the PDF-to-Markdown converter:

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
```

Produces `{stem}_marked.md` with YAML frontmatter (conversion metadata, SHA-256 hash, page count) and an empty `{stem}_summarized.json`.

Options:
- `--page-aware`: Add `<!-- PAGE N -->` markers extracted via pdfminer.six
- `--json-sidecar`: Write a separate `{stem}_conversion_meta.json`

Move the converted pair into a batch directory:

```bash
mkdir -p literature/conversions/batch-N
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/batch-N/
```

Start a new `batch-N` directory (next number) when adding a group of papers.

### 3. Summarize

Use an AI agent to fill `{stem}_summarized.json` with a structured summary. Feed the agent the corresponding `_marked.md` file.

The summarizer is **objective and unbiased** — it describes what the paper says without application-specific framing. Page and paragraph references are included in structured `citations` objects.

See `docs/standards/summary-format.md` for the JSON schema.

### 4. Score

Compute embeddings and scores:

```bash
python3 scripts/embed.py        # rebuild caches when conversions change
python3 scripts/score.py        # relevance/quality tiers, redundancy, validation
```

`score.py` ranks every paper against the thesis modules (BERT 0.5 / TF-IDF 0.3 / BM25 0.2) and assigns tiers: **crucial** (>=0.45), **supporting** (>=0.30), **cull** (<0.30). Redundant near-duplicates are flagged (threshold 0.98). Outputs land in `scores/`.

### 5. Adapt to Thesis Changes

The thesis outline, architecture, and algorithm selections change often. When they do, edit **only** `config/modules.yaml` (module queries, weights, tier thresholds, redundancy threshold) and re-run `score.py`. No code changes needed.

## Python Dependencies

Install from repository root:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

| Package | Required By |
|---------|------------|
| `markitdown` | `prepare_pdf.py` |
| `pypdf` | `count_pdf_pages.py`, `prepare_pdf.py` (--page-aware) |
| `PyPDF2` | `check_dupe_pdfs.py` |
| `pdfminer.six` | `prepare_pdf.py` (--page-aware) |
| `numpy` | `embed.py`, `score.py` |
| `scikit-learn` | `embed.py` (TF-IDF) |
| `rank-bm25` | `embed.py` (BM25) |
| `sentence-transformers` | `embed.py`, `score.py` (BERT) |
| `PyYAML` | `score.py` |
| `joblib` | `embed.py`, `score.py` |

## Intake Runbook — Batch 7 (17 verified papers)

Concrete, ready-to-run steps for the current intake (the 17 PDFs staged in
`literature/papers/`). Execute these only when processing actually starts.

### 0. Prerequisite (done during prep)

- PDFs are already staged flat in `literature/papers/` (moved from `bucket/`).
- Dependencies installed from `requirements.txt` (includes `markitdown[pdf]`).
- Destination `literature/conversions/batch-7/` exists.

### 1. Convert

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
```

Produces `{stem}_marked.md` + empty `{stem}_summarized.json` for all 17 PDFs.
Preview page counts first if useful:
```bash
python3 scripts/count_pdf_pages.py literature/papers/
```

> Note: `prepare_pdf.py` scans only the flat `literature/papers/` top level for
> `.pdf`. The `international/` and `local/` subdirectories are reserved for future
> designation-based categorization and are intentionally left out of conversion.

### 2. Rename & move into the batch

Assign canonical stems per `docs/standards/rrl-naming-conventions.md`
(`{Prefix}--{AuthorLastName}-{Year}`), then move each `_marked.md` +
`_summarized.json` pair into `literature/conversions/batch-7/`.

```bash
mkdir -p literature/conversions/batch-7
# rename + move each pair; e.g.
mv "literature/papers/I--Hajj-2023_marked.md" \
   "literature/papers/I--Hajj-2023_summarized.json" \
   literature/conversions/batch-7/
```

### 3. Summarize (AI agent)

Fill each `{stem}_summarized.json` using the corresponding `_marked.md` as input.
Schema + field rules: `docs/standards/summary-format.md`.

### 4. Score

```bash
python3 scripts/embed.py --force   # rebuild caches (conversions changed)
python3 scripts/score.py           # relevance tiers, redundancy, validation
```

Regenerates `scores/`. This replaces the stale 518-paper scoring outputs.

### 5. Manifest

```bash
python3 scripts/manifest.py        # refresh scores/manifest.json
```

---

## Script Reference

| Script | Purpose |
|--------|---------|
| `scripts/fetch_pdfs.py` | Fetch PDFs from local archive or remote source |
| `scripts/prepare_pdf.py` | Convert PDFs to Markdown with metadata |
| `scripts/count_pdf_pages.py` | List PDFs with page counts |
| `scripts/check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade |
| `scripts/embed.py` | Build/cache text, BERT embeddings, TF-IDF, BM25 |
| `scripts/score.py` | Score corpus against module queries |
| `scripts/manifest.py` | Build corpus manifest from conversions |
| `scripts/common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing) |
