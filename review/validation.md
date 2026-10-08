# Literature Review Matrix Validation

- Generated: **2026-10-08T11:29:16.293432+00:00**
- Papers: **97** | extracted: **97** | not extracted: **0**
- Errors: **0** | informational gaps: **56**

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
| `effect_conflicts` | 4 |
| `unrecorded_discrepancies` | 44 |
| `modules_covered` | 20 |
| `modules_total` | 20 |
| `papers_unassigned` | 1 |
| `extracted` | 97 |
| `not_extracted` | 0 |
| `no_doi` | 45 |
| `unverified_venue` | 5 |
| `no_type` | 58 |

## Errors

None. Every rule passed.

## Informational Gaps

- Same first author and year (zhang|2026): A--ZhangHou-2026, I--ZhangLu-2026 — check for a re-entry.
- Same first author and year (bangkosentralngpilipinas|2026): L--BangkoSentral-2026a, L--BangkoSentral-2026b — check for a re-entry.
- Same first author and year (yang|2024): I--Yang-2024a, I--Yang-2024b — check for a re-entry.
- Same first author and year (bangkosentralngpilipinas|2023): L--BangkoSentral-2023a, L--BangkoSentral-2023b — check for a re-entry.
- `A--Alenazi-2023` reports apps as 27 / 398 for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Alenazi-2023` reports apps as 533 / 94 for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Gulbakyt-2025` reports iterations to convergence as 100 iterations / under 100 iterations for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Olabintan-2026` reports ROC-AUC as 0.7137 / 0.714 for the same outcome — keep both with their locators and note it in `limitations`. This is a discrepancy in the paper, not in the extraction.
- `A--Chikoore-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 8.00. Either restore them or stop claiming a discrepancy.
- `A--Jayaprakashnarayan-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.951, 0.951, 14,563. Either restore them or stop claiming a discrepancy.
- `A--Olabintan-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 7.2, 7.2, 7.2, 7.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2, 9.2. Either restore them or stop claiming a discrepancy.
- `A--Patra-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.1. Either restore them or stop claiming a discrepancy.
- `A--ZhangHou-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.2.1, 4.1, 4.1, 4.2, 4.2, 4.2, 4.2. Either restore them or stop claiming a discrepancy.
- `L--Abila-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.70, 2.3, 2.4, 2.4, 2.4, 2.5. Either restore them or stop claiming a discrepancy.
- `L--Cruz-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2,451,596, 20,001, 50,000, 6.3.2, 7.1, 99.49%. Either restore them or stop claiming a discrepancy.
- `L--Erno-2026` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.00, 2.755. Either restore them or stop claiming a discrepancy.
- `A--Ayari-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 20.6%, 76.2%. Either restore them or stop claiming a discrepancy.
- `A--ChenTan-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.1, 1.2, 1.2, 1.3, 2.2, 83,770. Either restore them or stop claiming a discrepancy.
- `A--Hamdare-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 3.2, 3.6.2, 3.6.2, 4.1, 4.1, 4.4, 4.4. Either restore them or stop claiming a discrepancy.
- `A--John-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.016, 0.25, 1.1, 2.1, 3.1, 3.2, 3.2, 3.2, 3.2, 3.3, 3.3, 4.1, 4.3, 4.3, 4.4, 4.5, 4.5, 4.5, 5.1, 5.4, 5.4. Either restore them or stop claiming a discrepancy.
- `A--KaraSenguler-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 5.4. Either restore them or stop claiming a discrepancy.
- `A--Pretnar-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.09, 1.29, 2.3, 3.1, 5.1, 6.44. Either restore them or stop claiming a discrepancy.
- `A--Shaha-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.3, 5.1, 5.1.1, 5.1.2, 7.4, 7.4. Either restore them or stop claiming a discrepancy.
- `A--Sujon-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.403. Either restore them or stop claiming a discrepancy.
- `A--Yachamaneni-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.4, 2.4, 4.3, 4.4. Either restore them or stop claiming a discrepancy.
- `I--Andresen-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.1, 2.1, 2.1, 2.3, 3.3, 3.3, 4.1, 4.1, 4.1, 4.2.1. Either restore them or stop claiming a discrepancy.
- `I--Dheepiga-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.50, 3.088, 3.269. Either restore them or stop claiming a discrepancy.
- `I--Gan-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.115, 2.3, 2.5, 2.5, 2.5, 2.6, 2.6, 3.4. Either restore them or stop claiming a discrepancy.
- `I--Ganong-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 19,893, 19,893, 2.1, 2.1, 2.1, 2.1, 5.2.3. Either restore them or stop claiming a discrepancy.
- `I--RSingh-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.4, 3.4, 4.1, 4.1, 4.1, 4.2, 4.3, 4.3, 4.3, 4.3, 4.3. Either restore them or stop claiming a discrepancy.
- `I--Yuttama-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 102.3, 37.75%, 62.25%. Either restore them or stop claiming a discrepancy.
- `L--Atento-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.8, 3.8, 3.8, 3.8, 3.8. Either restore them or stop claiming a discrepancy.
- `L--Bulan-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.05, 0.05, 3.1, 3.1, 3.2, 3.2, 3.4, 3.4, 3.4, 3.5, 3.5, 3.5. Either restore them or stop claiming a discrepancy.
- `L--Esperanza-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.121, 0.179, 0.245, 0.302, 5.2%, 6.1%, 75,000, 9.4%. Either restore them or stop claiming a discrepancy.
- `L--PSA-2025` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 74.7, 74.7%. Either restore them or stop claiming a discrepancy.
- `A--ChenJ-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.2, 3.6, 3.6, 3.6, 3.6, 3.6, 4.1, 4.1, 4.1, 4.1, 4.2, 4.2, 4.2. Either restore them or stop claiming a discrepancy.
- `A--Sappa-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 4.1, 5.1, 5.2, 5.3, 5.3, 6.1, 6.2. Either restore them or stop claiming a discrepancy.
- `A--Siswara-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.5%, 2.5%. Either restore them or stop claiming a discrepancy.
- `A--Song-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.2, 6.4.2, 6.4.2. Either restore them or stop claiming a discrepancy.
- `A--Vijayanand-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 3.2, 3.3, 3.3, 3.3. Either restore them or stop claiming a discrepancy.
- `I--Danahy-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 10,000, 2.1, 2.1, 2.1, 2.2, 2.2, 2.2, 3.1. Either restore them or stop claiming a discrepancy.
- `I--Prakoso-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 3.6. Either restore them or stop claiming a discrepancy.
- `I--Rane-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 3.1, 3.5, 3.6, 3.7. Either restore them or stop claiming a discrepancy.
- `I--Yang-2024b` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.1, 2.5, 3.2, 3.2, 3.2, 3.3, 3.3, 3.3. Either restore them or stop claiming a discrepancy.
- `L--Salvador-2024` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 2.2, 2.4, 2.4. Either restore them or stop claiming a discrepancy.
- `A--ZhangEtAl-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 1.1, 4.1, 4.1.2, 4.2.2, 4.2.5, 4.3.5. Either restore them or stop claiming a discrepancy.
- `I--Bai-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.05, 0.059, 5.3, 5.3, 5.3. Either restore them or stop claiming a discrepancy.
- `I--Hajj-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.001, 0.001, 0.001, 0.001, 0.001, 3.1, 3.1, 3.2, 3.2, 3.2, 3.2. Either restore them or stop claiming a discrepancy.
- `I--Sapiri-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 4.2, 4.3, 4.3, 998.789. Either restore them or stop claiming a discrepancy.
- `I--WangLy-2023` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 0.1, 0.1, 3.2.2, 5.2.2, 6.2, 7.1, 7.1, 7.1, 7.2. Either restore them or stop claiming a discrepancy.
- `L--BangkoSentral-2023a` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 5,000, 502,208.75. Either restore them or stop claiming a discrepancy.
- `L--BangkoSentral-2023b` describes a discrepancy in `limitations` but these figures are absent from `effects[]`: 10,000, 27.92, 28.32, 71.11%, 78.5. Either restore them or stop claiming a discrepancy.
- 1 papers have no module assignment yet.
- 45 entries have no DOI in metadata.json.
- 5 entries carry an unverified venue: A--DSouza-2026, L--Abila-2026, L--Francisco-2026, I--Yoganandham-2025, L--Atento-2025.
- 58 entries have no publication type recorded.

## Corpus Composition

| Year | Papers |
| :--- | ---: |
| 2026 | 23 |
| 2025 | 42 |
| 2024 | 20 |
| 2023 | 12 |

| Designation | Papers |
| :--- | ---: |
| algorithm | 50 |
| international | 25 |
| local | 22 |
