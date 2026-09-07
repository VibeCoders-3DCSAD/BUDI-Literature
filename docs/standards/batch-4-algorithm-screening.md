# Batch-4 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-4/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-4/` (96 PDFs; 39 algorithm-designated candidates)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet

---

## Method

1. Enumerate the 96 PDFs in `batch-4/` (keys M–S/R).
2. Pull per-paper best module, tier, and quality from `scores/index.json`.
3. Keep the **algorithm/model-designated** subset: best module in
   `ml_algorithms`, `forecasting`, `anomaly_detection`, `budget_recommendation`,
   or `expense_categorization` → **39 candidates**.
4. **Verify titles against the actual PDFs.** Unlike batch-5, batch-4 keys *had*
   titles in the manifest — but spot-checks showed roughly half were unreliable
   (some stored "titles" are venue/conference strings, e.g. `Patel & Singh`'s was
   the IMPACT 2026 conference name; `Reyes et al`'s was wrong too). All titles in
   this doc were re-verified from PDF first-page/abstract text via pypdf.
5. Assign proposed stems per `docs/standards/rrl-naming-conventions.md`
   (`A--` algorithm focus, `L--` local Philippine, `I--` international non-algorithm).
   Local classification is based on the **author affiliation in the PDF** (e.g.
   UP Diliman, Caraga State, Southern Leyte State, UP Los Baños), not the unreliable
   manifest `designation`/`authors` fields.
6. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline /
   partial fit), or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

**Scope:** algorithm/model papers only, per the requested batch flow (batch-6 → batch-5
→ batch-4).

> **Data-quality note:** the manifest `title`/`authors`/`designation`/`year` fields for
> batch-4 are unreliable — several stored titles were conference/journal names and years
> were off by a decade (e.g. `Reyes et al` stored year 2014, actual 2024). Years below use
> the journal/citation line or PDF creation date as the best available signal.

---

## Batch-4 Triage (algorithm-designated candidates)

### Crucial tier (>= 0.45) — 10 papers (8 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--PatelSingh-2026` | An Intelligent AI-Based Framework for Automated Personal Financial Management | 2026 | expense_categorization 0.522 | crucial / 2.00 | **Maintain** |
| `L--Reyes-2024` | A Comparative Analysis of Machine Learning Models for Predictive Analytics in Finance | 2024 | ml_algorithms 0.495 | crucial / 1.50 | **Maintain** (PH, UP Diliman) |
| `A--Rafiaei-2026` | Keyword Matching vs. LLM-Based Classification for Personal Finance Transaction Categorization: A Benchmark Study on Real Canadian Bank Data | 2026 | expense_categorization 0.494 | crucial / 1.75 | **Maintain** |
| `A--Oktana-2025` | Binary Classification for Predicting the Investment Trends of The Younger Generation Based on Machine Learning | 2025 | ml_algorithms 0.488 | crucial / 2.25 | Review (investment) |
| `A--Nagaraj-2025` | A Study on Credit Default Prediction Using Hybrid AI Models Combining Neural Architectures and Econometric Features | 2025 | ml_algorithms 0.481 | crucial / 2.00 | **Maintain** (credit/debt) |
| `A--Peykani-2025` | Evaluation of Cost-Sensitive Learning Models in Forecasting Business Failure of Capital Market Firms | 2025 | ml_algorithms 0.480 | crucial / 2.00 | Review (business failure) |
| `L--Pandiin-2025` | Predictive Modeling for Loan Eligibility Assessment: A Comparative Study of Logistic Regression, Random Forest, and SVM with Detailed Oversampling | 2025 | ml_algorithms 0.473 | crucial / 1.75 | **Maintain** (PH, Caraga State) |
| `__Mohammad__` | Transforming Credit Risk Evaluation in Digital Lending from Black-Box Models to Transparent Decisions | — | ml_algorithms 0.468 | crucial / 2.25 | **Skip / carry-over** (no PDF) |
| `__Mohiuddin__` | Credit Decision Automation in Commercial Banks: A Review of AI and Predictive Analytics in Loan Assessment | — | ml_algorithms 0.462 | crucial / 2.25 | **Skip / carry-over** (no PDF) |
| `A--Nasir-2024` | Data-Driven Decision-Making for Bank Target Marketing Using Supervised Learning Classifiers on Imbalanced Big Data | 2024 | ml_algorithms 0.455 | crucial / 2.00 | Review (bank marketing) |

### Supporting tier (>= 0.30) — 27 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Ng-2026` | AI-BAAM: AI-Driven Bank Statement Analytics as Alternative Data for Malaysian MSME Credit Scoring | 2026 | ml_algorithms 0.427 | supporting / 2.25 | **Maintain** (credit, alt-data) |
| `A--Patra-2026` | AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation | 2026 | ml_algorithms 0.427 | supporting / 2.50 | **Maintain** (goal-based savings) |
| `A--Pretnar-2025` | Mental Accounting Through Two-Stage Budgeting Under Bounded Rationality | 2025 | budget_recommendation 0.426 | supporting / 1.50 | **Maintain** (budgeting) |
| `A--Olabintan-2026` | FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data | 2026 | ml_algorithms 0.424 | supporting / 2.25 | **Maintain** (credit/XAI) |
| `A--Pratama-2024` | User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation | 2024 | expense_categorization 0.405 | supporting / 1.50 | **Maintain** (transaction profiling) |
| `A--Nie-2024` | A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges | 2024 | ml_algorithms 0.394 | supporting / 2.25 | **Maintain** (survey) |
| `A--Pagliaro-2025` | Artificial Intelligence vs. Efficient Markets: A Critical Reassessment of Predictive Models in the Big Data Era | 2025 | ml_algorithms 0.446 | supporting / 2.00 | Review |
| `A--Oliveira-2026` | Neural Networks for Real-Time Financial Fraud Detection | 2026 | ml_algorithms 0.421 | supporting / 1.50 | Review (fraud) |
| `A--Munira-2025` | Artificial Intelligence in Financial Customer Relationship Management: A Systematic Review of AI-Driven Strategies in Banking and FinTech | 2025 | ml_algorithms 0.420 | supporting / 2.25 | Review |
| `A--Polytarchos-2025` | Credit Card Fraud Detection Through Deep Learning and Real-Time Data Streams: A Comparison and New Directions | 2025 | anomaly_detection 0.417 | supporting / 1.75 | Review (fraud) |
| `A--Papanastassiou-2025` | A Reinforcement Learning Framework for Fraud Detection in Highly Imbalanced Financial Data | 2025 | ml_algorithms 0.414 | supporting / 2.25 | Review (fraud/RL) |
| `A--Qawasmeh-2025` | Beyond Firewall: Leveraging Machine Learning for Real-Time Insider Threats Identification and User Profiling | 2025 | ml_algorithms 0.411 | supporting / 2.25 | Review (security) |
| `L--RamAgoylo-2025` | Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach | 2025 | ml_algorithms 0.411 | supporting / 1.75 | Review (students, off-finance) |
| `A--Saeedian-2025` | A Comparative Review of Electricity Load Forecasting Methods Across Temporal Horizons | 2025 | forecasting 0.411 | supporting / 1.75 | Cull (electricity load) |
| `A--Paz-2026` | Interpretable Binary Classification Under Constraints for Financial Compliance Modeling | 2026 | ml_algorithms 0.408 | supporting / 2.25 | Review (compliance) |
| `A--Saghafi-2025` | Impact of Categorization Autonomy on Effective Use and Adoption Intentions | 2025 | expense_categorization 0.405 | supporting / 1.50 | Review (HCI) |
| `A--Odufisan-2025` | Harnessing Artificial Intelligence and Machine Learning for Fraud Detection and Prevention in Nigeria | 2025 | ml_algorithms 0.400 | supporting / 2.00 | Review (fraud) |
| `A--Moury-2026` | Machine Learning-Based Transaction Risk Scoring Models for Financial Compliance Monitoring in Foreign Exchange Operations | 2026 | anomaly_detection 0.392 | supporting / 2.00 | Review |
| `A--Ramagiri-2025` | Tuning AML Detection Rules: A Quantitative Approach to Reducing False Positives | 2025 | anomaly_detection 0.382 | supporting / 2.25 | Review (AML/fraud) |
| `A--Quan-2025` | A Strategic Analysis of AI-Driven Customer Relationship Management Systems in Enhancing Personalization and Retention in Financial Institutions | 2025 | ml_algorithms 0.380 | supporting / 1.75 | Review (CRM) |
| `A--Patterson-2026` | Concept Drift Monitoring and Continual Learning in Production AI Systems: An Empirical Cost–Benefit Comparison of Detection Methods and Adaptation Strategies | 2026 | ml_algorithms 0.378 | supporting / 1.50 | Review (concept drift) |
| `A--Pereira-2025` | A Comparison of Approaches for Handling Concept Drifts in Data Processed with Machine Learning | 2025 | ml_algorithms 0.378 | supporting / 1.75 | Review (concept drift) |
| `A--Prashanth-2025` | Adaptive Buffering Strategies for Incremental Learning Under Concept Drift in Lifestyle Disease Modeling | 2025 | ml_algorithms 0.358 | supporting / 2.00 | Cull (health/lifestyle disease) |
| `A--Pisal-2025` | An Integrated TOPSIS and ARAS Method Multi-Criteria Decision-Making Approach for Optimizing Investment Portfolios using Goal Programming and Genetic Algorithm Model | 2025 | budget_recommendation 0.346 | supporting / 2.25 | Cull (investment) |
| `A--Sahraoui-2025` | Targeting Social Assistance Beneficiaries Using Machine Learning: A Poverty Probability-Based Approach | 2025 | ml_algorithms 0.344 | supporting / 2.00 | Review (poverty targeting) |
| `A--Nooji-2025` | Hybrid Clustering Meets Behavior Analytics: Adaptive Consumer Segmentation for E-Commerce Success | 2025 | anomaly_detection 0.336 | supporting / 2.00 | Cull (e-commerce) |
| `A--Sabiri-2025` | Hybrid Quality-Based Recommender Systems: A Systematic Literature Review | 2025 | ml_algorithms 0.301 | supporting / 2.00 | Review |

### Cull tier (< 0.30) — 2 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `L--Onsay-2024` | When Machine Learning Meets Econometrics: Can It Build a Better Measure to Predict Multidimensional Poverty and Examine Unmeasurable Economic Conditions? | 2024 | ml_algorithms 0.286 | cull / 2.00 | Cull (0.286; PH poverty — note for contextual use) |
| `A--Qu-2024` | Budgeted Embedding Table for Recommender Systems | 2024 | budget_recommendation 0.245 | cull / 1.75 | Cull (embeddings, off-scope) |

### No-sourcing candidates (PDF unavailable)

| Index key | Status |
| :--- | :--- |
| `Mohammad et al` | **Skip / carry-over flag** — no PDF found in batch-4 dir, bucket, or other batches (crucial, 0.468) |
| `Mohiuddin et al` | **Skip / carry-over flag** — no PDF found in batch-4 dir, bucket, or other batches (crucial, 0.462) |

---

## Algorithm/Model-Designated Papers (Budi Candidates) — detail

### Crucial tier (top priority for intake)

1. **Patel & Singh (2026)** — *An Intelligent AI-Based Framework for Automated Personal Financial Management*
   - **Best module:** expense_categorization 0.522 (crucial) — top in batch-4; quality 2.00.
   - **Why it fits:** an automated personal-financial-management framework (expense categorization
     driven) — a direct §2.4/§3 fit for an intelligent PFM app. Stored manifest title was the
     conference name (IMPACT 2026); real title verified from page 1.
   - **Source:** `Patel & Singh.pdf` (Galgotias College, India).

2. **Reyes et al. (2024)** — *A Comparative Analysis of Machine Learning Models for Predictive Analytics in Finance*
   - **Best module:** ml_algorithms 0.495 (crucial); quality 1.50.
   - **Why it fits:** compares ML models for financial predictive analytics from **UP Diliman**
     (Dept. of Computer Science) — a local Philippine classifier-comparison paper for financial
     prediction (§2.4.4 / §3). Stored title ("Spending Pattern Analysis...") was wrong; verified.
   - **Source:** `Reyes et al.pdf`.

3. **Rafiaei (2026)** — *Keyword Matching vs. LLM-Based Classification for Personal Finance Transaction Categorization*
   - **Best module:** expense_categorization 0.494 (crucial); quality 1.75.
   - **Why it fits:** benchmark of LLM vs. keyword-rule categorization of personal-finance
     transactions on real bank data — a direct expense-categorization evidence paper (§2.4.4.1/§3).
   - **Source:** `Rafiaei.pdf`.

4. **Nagaraj (2025)** — *A Study on Credit Default Prediction Using Hybrid AI Models Combining Neural Architectures and Econometric Features*
   - **Best module:** ml_algorithms 0.481 (crucial); quality 2.00 (Visa Inc.).
   - **Why it fits:** hybrid neural + econometric credit-default prediction — debt-management angle
     (§2.4.4.2 / debt_management).
   - **Source:** `Nagaraj.pdf`.

5. **Pandiin & Matias (2025)** — *Predictive Modeling for Loan Eligibility Assessment: LR vs RF vs SVM with Detailed Oversampling*
   - **Best module:** ml_algorithms 0.473 (crucial); quality 1.75.
   - **Why it fits:** loan-eligibility classification from **Caraga State University (Philippines)** —
     a local debt/credit classifier paper (§2.4.4.2 / debt_management). Stored title had a stray
     "Paper-" prefix; verified.
   - **Source:** `Pandiin & Matias.pdf`.

### Supporting tier (promising, needs RRL verdict)

6. **Ng et al. (2026)** — *AI-BAAM: AI-Driven Bank Statement Analytics as Alternative Data for Malaysian MSME Credit Scoring* (ICLR 2026)
   - **Best module:** ml_algorithms 0.427 (supporting); quality 2.25.
   - **Why it fits:** bank-account-analytics → credit scoring using alternative transaction data —
     a transaction-analysis-to-credit pipeline that generalizes well to personal PFM (§3.2).
7. **Patra et al. (2026)** — *AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation*
   - **Best module:** ml_algorithms 0.427 (supporting); quality 2.50 (KIIT, India).
   - **Why it fits:** goal-based financial planning with contextual feasibility — direct savings/goal
     support (§2.4.4.2 / savings).
8. **Pretnar et al. (2025)** — *Mental Accounting Through Two-Stage Budgeting Under Bounded Rationality*
   - **Best module:** budget_recommendation 0.426 (supporting); quality 1.50.
   - **Why it fits:** two-stage budgeting / mental accounting — behavioral budgeting model relevant
     to budget-recommendation design (§2.4.4.2 / budgeting).
9. **Olabintan (2026)** — *FairLend-Africa: An Explainable ML Framework for Alternative Credit Scoring Using Behavioral Financial Data*
   - **Best module:** ml_algorithms 0.424 (supporting); quality 2.25 (Nigeria).
   - **Why it fits:** XAI credit scoring on behavioral financial data — explainability + credit/debt
     (§3.4 + §2.4.4.2).
10. **Pratama & Putri (2024)** — *User Profiling Based on Financial Transaction Patterns: A Clustering Approach for User Segmentation*
    - **Best module:** expense_categorization 0.405 (supporting); quality 1.50.
    - **Why it fits:** clustering on transaction patterns for user segmentation — direct expense/
      behavioral-profiling evidence (§2.4.4.1 / §3). **Stored title was wrong** ("Financial Literacy...");
      verified title is transaction-pattern user profiling.
11. **Nie et al. (2024)** — *A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges*
    - **Best module:** ml_algorithms 0.394 (supporting); quality 2.25 (arXiv 2406.11903).
    - **Why it fits:** comprehensive LLM-for-finance survey — context for LLM-based categorization /
      explanation features (§2.4.4 / §3).

### Review / borderline

Fraud/compliance-family (Oliveira, Polytarchos, Papanastassiou, Odufisan, Moury, Ramagiri) —
relevant to the anomaly-detection sibling as shared-module evidence, but they target bank/card/AML
fraud rather than personal-overspending detection. Investment/portfolio (Oktana, Pisal, Pagliaro) —
investment-oriented, tangential to savings/debt. Concept-drift methodology (Patterson, Pereira) and
security (Qawasmeh) — ML methodology, not finance-specific. HCI/adoption (Saghafi), CRM (Munira,
Quan), compliance (Paz), poverty targeting (Sahraoui) — partial fit for §3/§2.4 context only.
`Ram & Agoylo` is a local PH classifier but on *student lifestyle*, not finance — off-scope.

### Cull / defer

Saeedian (electricity load forecasting), Prashanth (lifestyle disease),
Nooji (e-commerce segmentation), Qu (embedding tables) — off-scope for personal savings/debt
finance despite algorithm keywords. `Onsay & Rabajante` (PH, < 0.30) — multidimensional-poverty
prediction; note as possible contextual background despite cull tier.

---

## Topical Outline Mapping ($3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Patel & Singh 2026 | §2.4.1 / §3, expense | AI personal-financial-management framework |
| Reyes et al 2024 | §3.2 classification (L--) | ML model comparison for financial prediction |
| Rafiaei 2026 | §2.4.4.1 / §3, categorization | LLM vs keyword transaction categorization |
| Nagaraj 2025 | §2.4.4.2 / §3, credit | Hybrid credit-default prediction |
| Pandiin & Matias 2025 | §2.4.4.2 / §3, loan (L--) | Loan-eligibility classifiers, PH |
| Ng et al 2026 | §3.2 profiling / credit | Bank-statement alt-data credit scoring |
| Patra et al 2026 | §2.4.4.2 / §3, savings | Goal-based financial planning |
| Pretnar et al 2025 | §2.4.4.2 budgeting | Mental accounting, two-stage budgeting |
| Olabintan 2026 | §3.4 + §2.4.4.2 | XAI alternative credit scoring |
| Pratama & Putri 2024 | §2.4.4.1 / §3 clustering | Transaction-pattern user segmentation |
| Nie et al 2024 | §2.4.4 / §3 | LLM-for-finance survey |

The remaining papers map mostly to fraud/compliance (shared anomaly sibling), investment/portfolio,
or off-scope domains (electricity, health, e-commerce, security) outside the personal savings/debt
algorithm focus.

---

## Recommended Next Steps

1. **Confirm verdicts** for the "Review" papers — researcher decision, especially the
   fraud/compliance family, the concept-drift methodology pair (Patterson, Pereira), and the
   two borderline local `L--` papers (Ram & Agoylo, Onsay & Rabajante).
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   proposed stems → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Survive-note carry-overs:** `Mohammad et al` and `Mohiuddin et al` (both crucial,
   0.468 / 0.462) have no recoverable PDF in this workspace — flag for the researcher to
   re-fetch from the Drive source before inclusion.
4. **Re-score** once the intake lands — batch-4 old-run best_module/best_score values were
   computed from the deprecated 518-paper corpus and will be replaced by the batch-7 run.