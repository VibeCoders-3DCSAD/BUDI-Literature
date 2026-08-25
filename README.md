# Odin-Literature

Self-contained Review of Related Literature (RRL) corpus and scoring pipeline
for the Odin thesis. **No LLMs, no token APIs, no agents.**

## What lives here

- `literature/conversions/batch-1..6/` — every curated paper as:
  - `{stem}_marked.md` — full-text markdown conversion (with YAML metadata frontmatter)
  - `{stem}_summarized.json` — structured summary (metadata, `odin_topics`, findings, citations)
- `literature/bucket/` — raw candidate PDFs for intake
- `literature/papers/` — fetched source PDFs (gitignored; use `scripts/fetch_pdfs.py`)
- `config/modules.yaml` — **the single source of truth** for what "relevant" means
- `scripts/` — fetch, convert, embed, and score pipeline
- `scores/` — generated, committed outputs (see below)
- `docs/standards/` — naming conventions, summary schema, workflow documentation

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
# CPU-only torch first (smaller), then the rest:
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
```

## Full Pipeline

### 1. Fetch PDFs

```bash
# From a sibling directory (e.g. Odin-Paper/literature/papers/):
python3 scripts/fetch_pdfs.py --source local --path ../Odin-Paper/literature/papers/

# From a .zip archive:
python3 scripts/fetch_pdfs.py --source local --path /path/to/pdf-archives/

# From a remote URL:
python3 scripts/fetch_pdfs.py --source remote --url https://example.com/papers.zip
```

PDFs land in `literature/papers/` (gitignored). SHA-256 hashes are printed for each file.

Optional: inspect before converting:

```bash
python3 scripts/count_pdf_pages.py literature/papers/
python3 scripts/check_dupe_pdfs.py literature/papers/ --cascade
```

### 2. Convert

```bash
python3 scripts/prepare_pdf.py literature/papers/ --page-aware
```

Produces `{stem}_marked.md` (with metadata frontmatter) + empty `{stem}_summarized.json`.

Move into a batch directory:

```bash
mkdir -p literature/conversions/batch-N
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/batch-N/
```

### 3. Summarize

Use an AI agent to fill `_summarized.json` with a structured summary.
Schema: `docs/standards/summary-format.md`.

### 4. Score

```bash
python3 scripts/embed.py            # --force to rebuild; resumable
python3 scripts/score.py            # --modules a,b to score a subset
python3 scripts/manifest.py         # rebuild manifest if conversions changed
```

## How relevance & quality are computed

For each paper x module in `config/modules.yaml`:

| Signal | Method | Weight |
|--------|--------|--------|
| Semantic relevance | BERT document embedding vs module query (`all-MiniLM-L6-v2`, local CPU) | 0.5 |
| Lexical relevance | TF-IDF cosine similarity | 0.3 |
| Lexical ranking | BM25 | 0.2 |

Quality is rule-based: sample size, national-source mention (FIES/PSA/BSP), recency, page count, and designation (local/algorithm-specific). Near-duplicate papers are clustered by embedding cosine similarity.

## Adapting when the thesis changes

The design rule is: **edits go in `config/`, never in code.**

| Change | What to do |
|--------|-----------|
| New/renamed/removed module, or new query wording | Edit `config/modules.yaml` -> `python3 scripts/score.py` |
| Thresholds (crucial/supporting, redundancy) | Edit `config/modules.yaml` -> `python3 scripts/score.py` |
| A conversion or new paper added/changed | `python3 scripts/embed.py` -> `python3 scripts/score.py` |
| Topics now come from a different outline | Replace the `modules:` block in `config/modules.yaml` |

## Scores reference

- `scores/index.json` — per-paper x module scores, best module, tier, quality, redundancy info
- `scores/report.md` — per-module ranked tables, prime cull candidates, near-duplicate clusters
- `scores/redundancy.json` — duplicate clusters with `keep`/`cull` decisions
- `scores/validation.md` — sanity check of automated scores vs existing annotations

## Notes

- Generated scores are committed so the scored corpus is browsable without running anything.
- `cache/` is gitignored (regenerable). Only ~101 MB of markdown is committed.
- Batch structure is by intake run, not by topic. Re-organize when the topical outline is finalized.
- Old topic codes (`1.A`-`14.C`) in summaries follow the previous thesis outline. Module definitions in `config/modules.yaml` supersede them for scoring.
