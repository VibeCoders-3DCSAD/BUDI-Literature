# Literature Review Matrix Validation

- Generated: **2026-11-18T10:44:58.981218+00:00**
- Papers: **53** | extracted: **51** | not extracted: **2**
- Errors: **0** | informational gaps: **12**

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
| `effect_conflicts` | 3 |
| `unrecorded_discrepancies` | 6 |
| `modules_covered` | 19 |
| `modules_total` | 19 |
| `papers_unassigned` | 2 |
| `extracted` | 51 |
| `not_extracted` | 2 |
| `no_doi` | 29 |
| `unverified_venue` | 0 |
| `no_type` | 0 |

## Errors

None. Every rule passed.

## Informational Gaps

- Same first author and year (bangkosentralngpilipinas|2026): L--BangkoSentral-2026a, L--BangkoSentral-2026b — check for a re-entry.
- `A--Alenazi-2023` reports apps as 27 / 398 for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Alenazi-2023` reports apps as 533 / 94 for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Gulbakyt-2025` reports iterations to convergence as 100 iterations / under 100 iterations for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Hamdare-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 3.2, 3.6.2, 3.6.2, 4.1, 4.1, 4.4, 4.4. Either restore them or stop claiming a discrepancy.
- `I--Ganong-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 19,893, 19,893, 2.1, 2.1, 2.1, 2.1, 5.2.3. Either restore them or stop claiming a discrepancy.
- `L--Esperanza-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.121, 0.179, 0.245, 0.302, 5.2%, 6.1%, 75,000, 9.4%. Either restore them or stop claiming a discrepancy.
- `I--Danahy-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 10,000, 2.1, 2.1, 2.1, 2.2, 2.2, 2.2, 3.1. Either restore them or stop claiming a discrepancy.
- `I--Simonse-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.097, 0.484, 0.609, 0.694, 0.797, 4.2, 5.1, 5.1, 5.1, 5.1. Either restore them or stop claiming a discrepancy.
- `I--Sapiri-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 4.2, 4.3, 4.3, 998.789. Either restore them or stop claiming a discrepancy.
- 2 papers have no module assignment yet.
- 29 entries have no DOI in metadata.json.

## Corpus Composition

| Year | Papers |
| :--- | ---: |
| 2026 | 8 |
| 2025 | 17 |
| 2024 | 11 |
| 2023 | 7 |
| 2022 | 4 |
| 2018 | 1 |
| 2015 | 1 |
| 2008 | 1 |
| 2007 | 1 |
| 1996 | 1 |
| 1977 | 1 |

| Designation | Papers |
| :--- | ---: |
| algorithm | 12 |
| international | 27 |
| local | 14 |
