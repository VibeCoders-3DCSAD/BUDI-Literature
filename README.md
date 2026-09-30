# BUDI-Literature

Self-contained Review of Related Literature (RRL) corpus and scoring pipeline
for the BUDI thesis. **No LLMs, no token APIs, no agents.**

## What lives here

- `literature/conversions/` — the curated paper corpus, flat (one file pair per paper):
  - `{stem}_marked.md` — full-text markdown conversion (with YAML metadata frontmatter)
  - `{stem}_summarized.json` — structured summary (metadata, `topic_tags`, findings, citations)
  - (Intake provenance lives in git history; earlier per-batch subdirectories were flattened or removed as superseded.)
- `literature/bucket/` — raw candidate PDFs for intake
- `literature/papers/` — fetched source PDFs (gitignored; use `scripts/fetch_pdfs.py`)
- `config/modules.yaml` — **the single source of truth** for what "relevant" means
- `scripts/` — fetch, convert, embed, and score pipeline
- `scores/` — generated, committed outputs (see below)
- `skills/` — agent-facing extraction contract for `_summarized.json`
- `docs/standards/` — naming conventions, summary schema, matrix format, workflow documentation

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
# From a sibling directory (e.g. BUDI-Base/archived-literature/papers/):
python3 scripts/fetch_pdfs.py --source local --path ../BUDI-Base/archived-literature/papers/

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

Move into the corpus root:

```bash
mv literature/papers/{stem}_marked.md literature/papers/{stem}_summarized.json \
   literature/conversions/
```

### 3. Summarize

Use an AI agent to fill `_summarized.json` with a structured summary.
Schema: `docs/standards/summary-format.md`. Output contract:
`skills/literature-review-summarizer.md`.

### 4. Score

```bash
python3 scripts/embed.py            # --force to rebuild; resumable
python3 scripts/score.py            # --modules a,b to score a subset
python3 scripts/manifest.py         # rebuild manifest if conversions changed
```

### 5. Build the literature review matrix

```bash
python3 scripts/build_matrix.py           # regenerate matrix + long tables + validation
python3 scripts/build_matrix.py --check   # validate only; exit 1 on any error
```

Reads `metadata.json`, `scores/index.json`, and every `_summarized.json`, then
writes `docs/literature-review-matrix.md`, `scores/quotes.json`,
`scores/effects.json`, and `scores/matrix-validation.md`. The matrix is
generated — never hand-edit it. Column rules: `docs/standards/matrix-format.md`.

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
| A conversion or new paper added/changed | `python3 scripts/embed.py` -> `python3 scripts/score.py` -> `python3 scripts/build_matrix.py` |
| A paper summarized or re-read | `python3 scripts/build_matrix.py` |
| Topics now come from a different outline | Replace the `modules:` block in `config/modules.yaml` |

## Scores reference

- `scores/index.json` — per-paper x module scores, best module, tier, quality, redundancy info
- `scores/report.md` — per-module ranked tables, prime cull candidates, near-duplicate clusters
- `scores/redundancy.json` — duplicate clusters with `keep`/`cull` decisions
- `scores/validation.md` — sanity check of automated scores vs existing annotations
- `scores/quotes.json`, `scores/effects.json` — long evidence tables extracted per paper
- `scores/matrix-validation.md` — matrix validation errors and informational gaps
- `docs/literature-review-matrix.md` — generated 17-column index over the corpus

## Notes

- Generated scores are committed so the scored corpus is browsable without running anything.
- `cache/` is gitignored (regenerable). Only ~101 MB of markdown is committed.
- Batch structure is by intake run, not by topic. Re-organize when the topical outline is finalized.
- Bibliographic metadata lives in `literature/conversions/metadata.json` (page-1 verified) and overrides conversion frontmatter. There is no `refs.bib`.
- Old topic codes (`1.A`-`14.C`) in summaries follow the previous thesis outline. Module definitions in `config/modules.yaml` supersede them for scoring.
