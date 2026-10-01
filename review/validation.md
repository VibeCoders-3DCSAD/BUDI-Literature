# Literature Review Matrix Validation

- Generated: **2026-10-01T03:15:23.311078+00:00**
- Papers: **93** | extracted: **2** | not extracted: **91**
- Errors: **0** | informational gaps: **7**

Regenerate with `python3 scripts/build_matrix.py --check` (exit 1 on any error).
Rules are defined in `docs/standards/review-layout.md`.

## Counts

| Check | Count |
| :--- | ---: |
| `malformed_doi` | 0 |
| `metadata_disagreement` | 0 |
| `unmarked` | 0 |
| `duplicate_doi` | 0 |
| `duplicate_title` | 0 |
| `year_mismatch` | 0 |
| `bad_type` | 0 |
| `bad_module_ids` | 0 |
| `note_grammar_errors` | 0 |
| `blank_cells` | 0 |
| `effect_conflicts` | 0 |
| `unrecorded_discrepancies` | 0 |
| `modules_covered` | 3 |
| `modules_total` | 20 |
| `papers_unassigned` | 91 |
| `extracted` | 2 |
| `not_extracted` | 91 |
| `no_doi` | 42 |
| `unverified_venue` | 5 |
| `no_type` | 74 |

## Errors

None. Every rule passed.

## Informational Gaps

- Same first author and year (zhang|2026): A--ZhangHou-2026, I--ZhangLu-2026 — check for a re-entry.
- 17 of 20 modules have no paper assigned: financial_planning, budgeting, savings_debt_management, income_expense_management, pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, sarima, linear_programming, interquartile_range, development_methodology, data_collection, model_development, system_development, software_quality_evaluation, system_performance_evaluation.
- 91 papers have no module assignment yet.
- Fill-rate verdicts suppressed: only 2 of 93 papers are extracted (need 10).
- 42 entries have no DOI in metadata.json.
- 5 entries carry an unverified venue: A--DSouza-2026, L--Abila-2026, L--Francisco-2026, I--Yoganandham-2025, L--Atento-2025.
- 74 entries have no publication type recorded.

## Corpus Composition

| Year | Papers |
| :--- | ---: |
| 2026 | 22 |
| 2025 | 41 |
| 2024 | 18 |
| 2023 | 12 |

| Designation | Papers |
| :--- | ---: |
| algorithm | 49 |
| international | 24 |
| local | 20 |
