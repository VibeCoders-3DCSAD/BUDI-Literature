# Literature Review Matrix Validation

- Generated: **2026-09-30T06:53:14.383131+00:00**
- Papers: **93** | extracted: **2** | not extracted: **91**
- Errors: **0** | informational gaps: **5**
- Thresholds: crucial >= 0.45, supporting >= 0.3

Regenerate with `python3 scripts/build_matrix.py --check` (exit 1 on any error).
Rules are defined in `docs/standards/matrix-format.md`.

## Counts

| Check | Count |
| :--- | ---: |
| `malformed_doi` | 0 |
| `metadata_disagreement` | 0 |
| `unmarked` | 0 |
| `unscored` | 0 |
| `duplicate_doi` | 0 |
| `duplicate_title` | 0 |
| `year_mismatch` | 0 |
| `bad_type` | 0 |
| `bad_theme_tags` | 0 |
| `blank_cells` | 0 |
| `effect_conflicts` | 0 |
| `unrecorded_discrepancies` | 0 |
| `extracted` | 2 |
| `not_extracted` | 91 |
| `no_doi` | 42 |
| `unverified_venue` | 5 |
| `no_type` | 76 |

## Errors

None. Every rule passed.

## Informational Gaps

- Same first author and year (zhang|2026): A--ZhangHou-2026, I--ZhangLu-2026 — check for a re-entry.
- Fill-rate verdicts suppressed: only 2 of 93 papers are extracted (need 10).
- 42 entries have no DOI in metadata.json.
- 5 entries carry an unverified venue: A--DSouza-2026, L--Abila-2026, L--Francisco-2026, I--Yoganandham-2025, L--Atento-2025.
- 76 entries have no publication type recorded.

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

| Tier | Papers |
| :--- | ---: |
| crucial | 57 |
| cull | 2 |
| supporting | 34 |
