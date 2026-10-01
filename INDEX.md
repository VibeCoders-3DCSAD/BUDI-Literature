# BUDI-Literature — Repository Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-10-01

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Project overview, setup, and pipeline | `README.md` |
| Module namespace — the source of truth | `config/taxonomy.yaml` |
| Curated paper corpus | `literature/conversions/` |
| Literature review matrix (generated) | `review/literature-review-matrix.md` |
| Per-module coverage (read before requesting new sources) | `review/data/themes.csv` |
| RRL processing workflow | `docs/standards/rrl-workflow.md` |
| Note schema for `review/notes/{stem}.md` | `docs/standards/note-format.md` |
| Matrix columns, tag namespace, validator rules | `docs/standards/review-layout.md` |
| Extraction contract for agents | `skills/literature-review-summarizer.md` |
| Corpus file naming rules | `docs/standards/rrl-naming-conventions.md` |
| Pipeline scripts | `scripts/` |
| Thesis documentation (system spec, PRD, chapters) | **BUDI-Base** |
| ML service and training pipeline | **BUDI-ML** |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `README.md` | Project overview, setup, and pipeline. |
| `config/` | Module namespace (single source of truth). |
| `scripts/` | Fetch, convert, and matrix generation. |
| `literature/` | Corpus: conversions, bucket (intake), papers (gitignored). |
| `review/` | Generated matrix, CSV tables, and validation; authored `notes/` and `synthesis/`. |
| `docs/` | Standards and workflow documentation. |
| `skills/` | Agent-facing contracts for corpus processing. |

---

## skills/

Contracts handed to an agent that does the work. They describe the output shape, not the tooling.

| File | Purpose |
| :--- | :--- |
| `literature-review-summarizer.md` | How to extract one paper into an authored note at `review/notes/{stem}.md`, including the `modules[]` assignment rules. Supersedes the retired 56-column matrix inserter. |

---

## config/

| File | Purpose |
| :--- | :--- |
| `taxonomy.yaml` | The 20 module ids across the 5 Topical Outline V4 sections, with leaf structure and provenance. The single source of truth for what modules exist. |

Replaced `modules.yaml` (weights, query wording, tier thresholds) on 2026-09-30.
There are no weights and no tiers: a paper's modules are assigned during
extraction, and coverage is a count of assignments.

---

## scripts/

| Script | Purpose |
| :--- | :--- |
| `fetch_pdfs.py` | Fetch PDFs from a local archive or remote source. |
| `prepare_pdf.py` | Convert PDFs to Markdown with metadata and page-aware extraction. |
| `count_pdf_pages.py` | List PDFs with page counts. |
| `check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade. |
| `build_matrix.py` | Build the generated review tree, long tables, and validation report. |
| `common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing). |

---

## literature/

The curated corpus. Each curated paper has up to three files — the fetched PDF,
the conversion, and the extraction note (see
`docs/standards/rrl-naming-conventions.md`).

| Path | Purpose |
| :--- | :--- |
| `literature/conversions/` | Committed corpus: one `{stem}_marked.md` per paper, plus `metadata.json`. The extraction note lives under `review/notes/`. |
| `literature/conversions/metadata.json` | Bibliographic sidecar: verified titles, authors, venues, DOIs, keyed by source-PDF SHA-256. |
| `literature/bucket/` | Raw candidate PDFs awaiting intake (gitignored). |
| `literature/papers/` | Fetched source PDFs (gitignored). |

---

## review/

Generated from `metadata.json`, the authored notes in `review/notes/*.md`, and
`config/taxonomy.yaml`. `review/notes/` and `review/synthesis/` are authored and
never overwritten; the matrix, `data/*.csv`, and `validation.md` are regenerated
by `scripts/build_matrix.py` on every full build.

| Path | Purpose |
| :--- | :--- |
| `review/literature-review-matrix.md` | Generated 15-column index over the whole corpus. |
| `review/validation.md` | Generated validation errors and informational gaps. |
| `review/data/papers.csv` | The 15 matrix columns plus a controlled `tags` column. |
| `review/data/screening.csv` | Intake triage: status, module count, DOI and venue completeness. |
| `review/data/quotes.csv` | Generated: one record per extracted quotation. |
| `review/data/effects.csv` | Generated: one record per statistical result. |
| `review/data/themes.csv` | Generated: per-module coverage tally. |
| `review/notes/{stem}.md` | **Authored**: one extraction note per paper — the source of truth for everything but the bibliographic block. A paper with no note gets a generated stub. |
| `review/synthesis/` | **Authored** cross-paper synthesis. Nothing overwrites it. |

---

## docs/ — live standards

| Path | Purpose |
| :--- | :--- |
| `docs/standards/rrl-workflow.md` | Full processing workflow (fetch → convert → extract → build → verify). |
| `docs/standards/note-format.md` | Schema for `review/notes/{stem}.md`, including `modules[]` and `module_rationale`. |
| `docs/standards/review-layout.md` | The `review/` tree, matrix columns, tag namespace, validator rules. |
| `docs/standards/rrl-naming-conventions.md` | Corpus file naming rules. |
| `docs/standards/documentation-format.md` | Shared documentation formatting rules. |
| `docs/NEW-SCOPE-SOURCES.md` | Download checklist for new-scope sources. Prioritization predates the current taxonomy and needs a re-pass. |

---

## docs/ — historical records

Dated records of work already done. Kept for rationale and audit; **not** current
specs. They describe the retired scoring pipeline or completed intake runs, and
their module names and column layouts do not match `config/taxonomy.yaml`.

| Path | What it records |
| :--- | :--- |
| `docs/standards/matrix-format_OLD.md` | The 17-column matrix layout, `scores/` inputs, and tag namespace. Superseded by `docs/standards/review-layout.md`. |
| `docs/standards/summary-format_OLD.md` | The retired `_summarized.json` extraction schema. The JSON files are gone; `docs/standards/note-format.md` replaces them. |
| `docs/OUTLINE-V4-COVERAGE_OLD.md` | Hand-maintained per-leaf coverage for the retired 22-module taxonomy. Superseded by `review/data/themes.csv`. |
| `docs/notes-to-improve-lrm.md` | The 2026-09-30 proposal that shaped the generated-matrix approach. |
| `docs/standards/migration-workflow.md` | Deprecated: the 518-PDF cross-repository migration. |
| `docs/standards/bucket-bucket-triage.md` | Triage of the 26-PDF intake batch. |
| `docs/standards/batch-1..6-algorithm-screening.md` | Screening of the first six intake batches. |

Per `docs/standards/documentation-format.md`, superseded documents are kept for
audit trails rather than deleted; they carry a deprecation notice at the top.

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Thesis documents (system spec, PRD, chapters) | **BUDI-Base** |
| ML service and training pipeline | **BUDI-ML** |
| Migration of papers from BUDI-Base | `docs/standards/migration-workflow.md` (deprecated) |
