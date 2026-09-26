# BUDI-Literature — Repository Index

- **Project:** Development of BUDI: A Personalized Intelligent Finance Management Application for Filipinos Using Classification, Forecasting, Optimization, and Anomaly Detection Models for Improving Savings and Debt
- **Institution:** University of Makati | Group 4, III-DCSAD
- **Last indexed:** 2026-08-31

---

## How to Use This Index

| Need | Go to |
| :--- | :--- |
| Project overview, setup, and pipeline | `README.md` |
| Relevance scoring module definitions (the source of truth) | `config/modules.yaml` |
| Curated paper corpus | `literature/conversions/` |
| RRL processing workflow | `docs/standards/rrl-workflow.md` |
| Structured summary JSON schema | `docs/standards/summary-format.md` |
| Corpus file naming rules | `docs/standards/rrl-naming-conventions.md` |
| Pipeline scripts | `scripts/` |
| Generated scores (ranked report) | `scores/report.md` |
| Thesis documentation (system spec, PRD, chapters) | **BUDI-Base** |
| ML service and training pipeline | **BUDI-ML** |

---

## Repository Map

| Path | Purpose |
| :--- | :--- |
| `AGENTS.md` | Agent navigation guide, standards, and repository conventions. |
| `INDEX.md` | This file. Master navigation index. |
| `README.md` | Project overview, setup, and pipeline. |
| `config/` | Relevance module definitions (single source of truth). |
| `scripts/` | Fetch, convert, embed, and score pipeline. |
| `literature/` | Corpus: conversions, bucket (intake), papers (gitignored). |
| `scores/` | Generated, committed outputs. |
| `docs/` | Standards and workflow documentation. |

---

## config/

| File | Purpose |
| :--- | :--- |
| `modules.yaml` | Relevance module definitions, scoring weights, and tier thresholds. The single source of truth for what is "relevant." |

---

## scripts/

| Script | Purpose |
| :--- | :--- |
| `fetch_pdfs.py` | Fetch PDFs from a local archive or remote source. |
| `prepare_pdf.py` | Convert PDFs to Markdown with metadata and page-aware extraction. |
| `count_pdf_pages.py` | List PDFs with page counts. |
| `check_dupe_pdfs.py` | Find duplicate PDFs by hash cascade. |
| `embed.py` | Build/cache text, BERT embeddings, TF-IDF, BM25. |
| `score.py` | Score corpus against module queries. |
| `manifest.py` | Build corpus manifest from conversions. |
| `common.py` | Shared helpers (corpus paths, text cleaning, frontmatter parsing). |

---

## literature/

The curated corpus. Each curated paper has up to three files (see `docs/standards/rrl-naming-conventions.md`).

| Path | Purpose |
| :--- | :--- |
| `literature/conversions/` | Committed corpus: `{stem}_marked.md` and `{stem}_summarized.json` per batch. |
| `literature/bucket/` | Raw candidate PDFs awaiting intake (gitignored). |
| `literature/papers/` | Fetched source PDFs, organized by local/international and algorithm-specific (gitignored). |

---

## scores/

Generated, committed outputs. All are browsable without running the pipeline.

| File | Purpose |
| :--- | :--- |
| `index.json` | Per-paper x module scores. |
| `report.md` | Human-readable ranked report by module. |
| `manifest.json` | Corpus manifest of all papers. |
| `redundancy.json` | Near-duplicate clusters with keep/cull decisions. |
| `validation.md` | Sanity check of automated scores vs existing annotations. |

---

## docs/

| Path | Purpose |
| :--- | :--- |
| `docs/standards/rrl-workflow.md` | Full processing workflow (fetch → convert → summarize → score). |
| `docs/standards/summary-format.md` | JSON schema for `_summarized.json` files. |
| `docs/standards/rrl-naming-conventions.md` | Corpus file naming rules. |
| `docs/standards/migration-workflow.md` | Cross-repository migration workflow from BUDI-Base. |
| `docs/NEW-SCOPE-SOURCES.md` | Download checklist for new-scope literature sources. |
| `docs/standards/documentation-format.md` | Shared documentation formatting rules. |

---

## Cross-References

| Task | Use |
| :--- | :--- |
| Thesis documents (system spec, PRD, chapters) | **BUDI-Base** |
| ML service and training pipeline | **BUDI-ML** |
| Migration of papers from BUDI-Base | `docs/standards/migration-workflow.md` |
