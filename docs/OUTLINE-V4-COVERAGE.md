# Outline V4 Coverage Analysis

Generated 2026-09-26 by re-scoring the 91-paper corpus against `config/modules.yaml`
after it was realigned to Topical Outline V4 (`GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`).

Thresholds: crucial >= 0.45, supporting >= 0.30.

How many corpus papers clear each threshold for each required leaf. This is the first
measurement of whether the corpus can actually support the current outline, rather than a
judgement about it.

| Module | Outline V4 leaf | Crucial | Supporting | Best match |
|---|---|---:|---:|---|
| `agile_methodology` | Agile lifecycle + Kanban **0** | 0 | 1 | `L--Santiago-2025` (0.401) |
| `system_evaluation` | System Evaluation (SUS + ISO/IEC 25010) **0** | 0 | 1 | `L--Santiago-2025` (0.358) |
| `seasonal_expense_forecasting` | Seasonal Expense Forecasting **0** | 0 | 9 | `I--Ganong-2025` (0.429) |
| `forecasting` | SARIMA forecasting | 3 | 19 | `A--SinghU-2025` (0.492) |
| `budget_recommendation` | Budget Creation / constraint optimization | 3 | 20 | `A--Gulbakyt-2025` (0.493) |
| `financial_profile_classification` | Saver/Borrower Profile Classification | 3 | 61 | `L--Francisco-2026` (0.487) |
| `filipino_context` | Philippine financial problems in planning | 4 | 19 | `L--Atento-2025` (0.493) |
| `pfms_systems` | Personal Financial Management Application | 6 | 33 | `I--Yadav-2026` (0.524) |
| `performance_indicators` | Performance Analysis indicators | 6 | 49 | `I--Yadav-2026` (0.495) |
| `anomaly_detection` | Unusual Expense Detection | 7 | 21 | `A--Zhong-2025` (0.534) |
| `financial_planning` | Financial Planning (now the central concept) | 7 | 42 | `I--Yeo-2023` (0.554) |
| `ml_algorithms` | Models and algorithms (general) | 14 | 36 | `A--Sireesha-2026` (0.539) |

## Leaves the corpus cannot support at all

3 of 12 required leaves have **zero** papers at crucial tier:

- **Agile lifecycle + Kanban** (`agile_methodology`) — 1 supporting, best match `L--Santiago-2025` at 0.401, below the 0.45 floor.
- **System Evaluation (SUS + ISO/IEC 25010)** (`system_evaluation`) — 1 supporting, best match `L--Santiago-2025` at 0.358, below the 0.45 floor.
- **Seasonal Expense Forecasting** (`seasonal_expense_forecasting`) — 9 supporting, best match `I--Ganong-2025` at 0.429, below the 0.45 floor.

Three of these are hard requirements of the outline, and the gaps are not academic:

| Gap | Why it is a problem |
|---|---|
| **Seasonal Expense Forecasting** | This is the thesis's core technical claim. The chapter leans on Dasmariñas et al. (2024) for it seven times, and that paper is not in the corpus at all. The adviser's standard for a core algorithm is six to seven sources. |
| **Agile lifecycle and Kanban** | Outline V4 names both explicitly under Methodology. The single supporting paper is a budget system paper, not a methodology source. The chapter's Kanban paragraph currently has no citation at all. |
| **System Evaluation (SUS, ISO/IEC 25010)** | Outline V4 names both explicitly. One supporting paper. The chapter discusses the ISO quality model and the SUS instrument across four paragraphs with no methodology source behind either. |

## Consequences for the intake list

The intake list agreed on 2026-09-21 (Tjostheim, Rafiei, Hovakimyan & Bravo, Schwartz, BSP
CFIS 2025, Khashadourian & Harrison, Fenig & Petersen, Asebedo 2025) was derived against
Outline V3. Outline V4 removed the savings and debt product subtypes, TAM/UTAUT, and the SVM
classifier, so several of those eight now serve a leaf the outline no longer contains. They are
re-ranked in `docs/NEW-SCOPE-SOURCES.md`.

Reordering the intake by this analysis puts the three zero-coverage leaves first, ahead of the
topic gaps those eight were chosen for.

