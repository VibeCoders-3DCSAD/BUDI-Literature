# Bucket-Bucket Triage (Budi Intake)

Triage of the 26 candidate PDFs staged in `literature/bucket/bucket-bucket/`
for intake into the Budi corpus. This supersedes the old-scope (Odin) scoring;
every paper here is treated as a **new** candidate for Budi, regardless of
whether an equivalent file was scored under the deprecated 518-paper corpus.

- **Date:** 2026.09.02
- **Bag:** `literature/bucket/bucket-bucket/` (27 PDFs → 26 unique papers)
- **Modules assessed against:** `config/modules.yaml` (17 modules)

---

## Scope and Duplicates

| Note | Detail |
| :--- | :--- |
| In-batch exact duplicate | `67c5107a29142.pdf` ≡ `67c5107a29142 (1).pdf` (identical md5 `b3e93438…`) — **`67c5107a29142 (1).pdf` removed**; `.pdf` kept. |
| Unique candidates | **26** (27 files minus the removed duplicate copy). |

Previously-scored files (`Hovakimyan & Bravo`, `Espelita et-al`, `Santiago`,
`Erno & Grefalde`, `Chen V. et al`) are **revalidated as new** for Budi, not
excluded — the 518-paper corpus belongs to the deprecated Odin scope.

---

## Triage Groups

- **A. Prioritize for Budi intake** — clear topical fit + usable quality signals.
- **B. Defer / needs work** — requires OCR, rename, or is oversized before intake.
- **C. BSP / institutional data** — hold as supporting context, **not** RRL papers.
- **D. Dubious / weak fit** — low topical overlap with the 17 modules.

---

## A. Prioritize for Budi Intake

| Stem (proposed) | Candidate | Identity | Pages | Relevant modules |
| :--- | :--- | :--- | :---: | :--- |
| `L--Sohilauw-2026` | `L--Sohilauw-2026.pdf` (renamed from mis-named `sdsdsad.pdf`) | Income, Saving Behavior, Household Financial Decision-Making (Indonesia, moderated-mediation) | 28 | savings, financial_profile_classification, behavioral_insights |
| `I--Dheepiga-2026` | `8+(1).pdf` | How Financial Literacy Influences Budgeting, Investment, Savings | 14 | financial_literacy, savings, budget_recommendation |
| `L--Prades-2025` | `V5I222.pdf` | Financial Literacy and Propensity Indebtedness, Baao CamSur (PH) | 18 | financial_literacy, debt_management, filipino_context |
| `L--Hambala-2025` | `1204435632.pdf` | Financial Management Practices & Financial Well-Being of HEI Employees (PH) | 17 | financial_wellbeing, financial_literacy, financial_profile_classification |
| `L--Claro-2025` | `ISRGJEBM4852025FT.pdf` | Regressors of Financial Well-Being among LGU Employees, Davao del Norte (PH) | 7 | financial_wellbeing, filipino_context |
| `L--Esperanza-2025` | `document.pdf` | Digital Lending Efficacy on Debt Management of Wage Earners (PH) | 17 | debt_management, digital lending, financial_wellbeing |
| `L--Gula-2026` | `690534-…2614fbb1.pdf` | Causes of Salary Loan Dependency (PH, IJMERI) | 24 | debt_management, filipino_context, behavioral_insights |
| `L--Atento-2025` | `IJHBA+Espelita+et+al.pdf` | Monetary Policy Awareness, Perceptions, Financial Behaviors (PH) | 24 | financial_literacy, financial_wellbeing, filipino_context |
| `L--Erno-2026` | `518-540+(1).pdf` | Behavioral & Psychological Drivers of Sustainable Saving / Financial Resilience (PH) | 23 | savings, behavioral_insights, financial_wellbeing |
| `I--Cumaio-2026` | `jrfm-19-00425.pdf` | Linking Financial Literacy & Behavioural Finance to Saving and Debt (review) | 27 | financial_literacy, savings, debt_management |
| `I--Jumady-2024` | `PUBLISH_EDI+JUMADY.pdf` | Financial Planning → Consumer Debt Management (literacy, self-efficacy) | 29 | debt_management, financial_literacy, budget_recommendation |
| `I--Samli-2025` | `LBIBF_Vol+24(1)_114-129.pdf` | Bibliometric: Financial Behaviour & Debt Management | 15 | debt_management, behavioral_insights |
| `I--Comia-2024` | `1mbmj2024-50-55.pdf` | Socio-Economic Implications of Credit Card Usage | 6 | debt_management, behavioral_insights |
| `I--TuanHa-2025` | `67c5107a29142.pdf` | Self-Control & Saving Behavior among MSME Owners | 13 | savings, behavioral_insights |

## B. Defer / Needs Work

| Draft stem | Candidate | Reason for deferral |
| :--- | :--- | :--- |
| `I--Tun-2025` | `Shwe Zin Tun (EMBF-53).pdf` | 85-page Myanmar MBA thesis on student saving behavior; strong topical fit (savings) but verbose — summarize selectively or extract the study design + findings. |
| `?--Journal38` | `no-38_research-and-education-journal-volume-38*.pdf` | 121-page **scanned image PDF** with no extractable text. Requires OCR before any relevance/quality assessment. Defer until OCR'd. |
| `L--Santiago-2025` | `MBA_financial-awareness-and-work-adaptability_Santiago-FINAL.pdf` | 194-page thesis (financial awareness / work adaptability, PH). Relevant but oversized; extract the core instrument + findings, or split. |
| `I--Hovakimyan-2024` | `Hovakimyan & Bravo.pdf` | Concept Drift Detection systematic review — algorithm/ML relevance only; keep for the classifier/forecast modules, not for finance behavior. |

## C. BSP / Institutional Data (context, not RRL papers)

| Candidate | Identity | Use |
| :--- | :--- | :--- |
| `AnnRep_2025.pdf` | Bangko Sentral ng Pilipinas **Annual Report 2025** (142 pp) | Institutional context for `filipino_context` / regulator stance; not a citable RRL paper by itself. |
| `FIP_1Sem2018.pdf` | BSP Financial Inclusion Program, 1H2018 | Data/advocacy context for financial inclusion; cite as a BSP source, not an RRL item. |
| `FIDashboard_4Q2023.pdf` | BSP Financial Inclusion Dashboard (2022/2023 Q4) | Indicator data for `filipino_context`; use as a data source. |
| `LTP_1qtr2026.pdf` | BSP Monetary Policy Report, 1Q 2026 (72 pp) | Current monetary-policy/economic context for `filipino_context`; regulator data, not an RRL paper. |
| `REDP_2023.pdf` | BSP Report on Regional Economic Developments (2023, 69 pp) | Regional-economic context for `filipino_context`; regulator data, not an RRL paper. |

## D. Dubious / Weak Fit

| Draft stem | Candidate | Assessment |
| :--- | :--- | :--- |
| `I--Chen-2023` | `Chen V. et al.pdf` | Human-AI decision-making / explainability. Tangential to the finance modules; low direct fit — cull unless the explainability angle is kept. |
| `?--Yessenov-2026` | `Зарубежный.pdf` | Financial competency & management skills of tertiary students (Kazakhstan). Moderate literacy fit; consider only if the student-literacy angle is needed. |
| `?--ImprovingPerf-2025` | `Improving_financial_performance_through.pdf` | Corporate/institutional financial performance — **not** personal finance; weak fit for a personal-finance app RRL. |
| `?--GanKay-2025` | `kelphick,+5.1+Gan+Kay.pdf` | Household savings determinants (U.S.). Moderate savings fit but non-PH context; low priority. |

---

## Recommended Next Steps

1. **Resolve the ordering issue** the team flagged: the four studied papers in
   `literature/bucket/` (`Salminen`, `Salvador`, `Yuttama`, `Zambrano`) should
   move into `literature/papers/` for conversion, and the `bucket-bucket/`
   candidates should promote to `bucket/`. This matches the intended
   bucket → papers → conversions flow.
2. ~~Drop the in-batch duplicate copy of `67c5107a29142.pdf`~~ — **done** (`67c5107a29142 (1).pdf` removed).
3. ~~Rename `sdsdsad.pdf`~~ — **done** (`L--Sohilauw-2026.pdf`).
4. **Prioritize Group A** for the next intake batch; **defer Group B** until OCR
   / selective extraction is done; keep **Group C** in a data/context folder;
   **cull Group D** unless a specific angle is defended.
