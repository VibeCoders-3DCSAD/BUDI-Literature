# RRL Processing Workflow

Workflow for adding and processing literature in the Review of Related Literature.

All steps happen within **BUDI-Literature**. No cross-repo transfers required.

## Steps

### 1. Fetch PDFs

Obtain source PDFs from a local archive or remote source:

```bash
# From a sibling directory (e.g. BUDI-Base/archived-literature/papers/):
python3 scripts/fetch_pdfs.py --source local --path ../BUDI-Base/archived-literature/papers/

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

Move the converted pair into the corpus root:

```bash
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/
```

The corpus is flat; do not create per-intake subdirectories. See
`docs/standards/rrl-naming-conventions.md`.

### 3. Summarize

Use an AI agent to fill `{stem}_summarized.json` with a structured summary. Feed the agent the corresponding `_marked.md` file.

The summarizer is **objective and unbiased** — it describes what the paper says without application-specific framing. Page and paragraph references are included in structured `citations` objects.

See `docs/standards/summary-format.md` for the JSON schema, and
`skills/literature-review-summarizer.md` for the output contract: the extraction
fields (`study_design`, `sample`, `context`, `software`, `quotes[]`, `effects[]`)
that step 5 builds the matrix from, and the rule for a paper that reports
contradictory figures.

Bibliographic fields (`title`, `authors`, `year`, `venue`, `doi`) are copied from
`literature/conversions/metadata.json`, the page-1-verified citation authority.
The agent does not re-derive them.

### 4. Score

Compute embeddings and scores:

```bash
python3 scripts/embed.py        # rebuild caches when conversions change
python3 scripts/score.py        # relevance/quality tiers, redundancy, validation
```

`score.py` ranks every paper against the thesis modules (BERT 0.5 / TF-IDF 0.3 / BM25 0.2) and assigns tiers: **crucial** (>=0.45), **supporting** (>=0.30), **cull** (<0.30). Redundant near-duplicates are flagged (threshold 0.98). Outputs land in `scores/`.

### 5. Build the Matrix

Regenerate the literature review matrix from the three sources:

```bash
python3 scripts/build_matrix.py           # build matrix + long tables + validation
python3 scripts/build_matrix.py --check   # validate only, exit 1 on any error
```

Inputs, in order of authority: `metadata.json` (bibliographic), `scores/index.json`
(relevance), `{stem}_summarized.json` (extraction). Outputs:

| File | Contents |
|------|----------|
| `docs/literature-review-matrix.md` | 17-column index, one row per corpus paper, plus a theme-count view. |
| `scores/quotes.json` | One record per extracted quotation. |
| `scores/effects.json` | One record per statistical result. |
| `scores/matrix-validation.md` | Validation errors and informational gaps. |

**Never hand-edit the matrix.** Fix the source and rebuild. Column definitions,
the tag namespace, and every validation rule are in
`docs/standards/matrix-format.md`.

### 6. Adapt to Thesis Changes

The thesis outline, architecture, and algorithm selections change often. When they do, edit **only** `config/modules.yaml` (module queries, weights, tier thresholds, redundancy threshold), then re-run `score.py` followed by `build_matrix.py`. No code changes needed.

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
- Destination `literature/conversions/` is the flat corpus root.

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

### 2. Rename & move into the corpus

Assign canonical stems per `docs/standards/rrl-naming-conventions.md`
(`{Prefix}--{AuthorLastName}-{Year}`), then move each `_marked.md` +
`_summarized.json` pair into `literature/conversions/`.

```bash
# rename + move each pair; e.g.
mv "literature/papers/I--Hajj-2023_marked.md" \
   "literature/papers/I--Hajj-2023_summarized.json" \
   literature/conversions/
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

### 6. Matrix

```bash
python3 scripts/build_matrix.py    # refresh the matrix and long tables
```

Run this after any step that changes a score, a stem, or a summary.

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
| `scripts/build_matrix.py` | Build the generated review matrix, long tables, and validation report |
| `scripts/common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing) |
