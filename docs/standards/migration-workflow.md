# Literature Migration Workflow

Documents the process for migrating relevant literature from Odin-Paper to Odin-Literature.

## Overview

Odin-Paper contains ~518 source PDFs in `literature/papers/` (Git LFS tracked). These need to be screened, assessed, and migrated to Odin-Literature in small batches.

## Workflow

### 1. Selection

- **Who:** Researcher (final decision)
- **Input:** Odin-Paper/literature/papers/ (518 PDFs across batch-1..6)
- **Output:** Shortlist of 10-20 PDFs per batch
- **Strategy:** Start with batch-6 (18 papers, newest), or curated shortlist

### 2. Intake

Place selected PDFs in `Odin-Literature/literature/bucket/`.

```bash
# Copy PDFs from Odin-Paper to Odin-Literature bucket
cp ../Odin-Paper/literature/papers/batch-6/*.pdf literature/bucket/
```

### 3. Pre-assessment (Automated)

Run scoring pipeline on bucket contents to pre-assess relevance and redundancy:

```bash
# Fetch into papers/ directory
python3 scripts/fetch_pdfs.py --source local --path literature/bucket/

# Convert PDFs to Markdown
python3 scripts/prepare_pdf.py literature/papers/ --page-aware

# Move to new batch directory
mkdir -p literature/conversions/batch-7
mv literature/papers/*_marked.md literature/papers/*_summarized.json \
   literature/conversions/batch-7/

# Build embeddings and score
python3 scripts/embed.py --force
python3 scripts/score.py
```

### 4. Review

- **Who:** Researcher
- **Input:** scores/report.md, scores/index.json, scores/redundancy.json
- **Action:** Review relevance tiers, quality scores, redundancy clusters
- **Decision:** Validate which papers to keep, cull, or flag for manual review

### 5. Post-processing (After Validation)

After researcher validates papers:

1. **Summarize** — AI agent fills `_summarized.json` (schema: `docs/standards/summary-format.md`)
2. **Compile** — Group by topic, generate literature review sections
3. **Synthesize** — Cross-paper analysis and gap identification

## Batch Strategy

- Process 10-20 papers at a time
- Start with batch-6 (newest, likely most relevant)
- Or researcher provides curated shortlist
- Validate workflow before scaling to full corpus

## Files Involved

| Location | Purpose |
|----------|---------|
| `Odin-Paper/literature/papers/` | Source PDFs (Git LFS) |
| `Odin-Literature/literature/bucket/` | Intake staging area |
| `Odin-Literature/literature/conversions/` | Converted Markdown + summaries |
| `Odin-Literature/scores/` | Relevance/quality scores |
| `Odin-Literature/config/modules.yaml` | Module definitions for scoring |

## Notes

- PDFs are Git LFS tracked in both repos
- The scoring pipeline operates on Markdown conversions, not raw PDFs
- `cache/` is regenerable; only `scores/` and `literature/conversions/` are committed
- Old topic codes (1.A-14.C) in summaries follow the previous thesis outline
