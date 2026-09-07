# Batch-1 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-1/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-1/` (96 PDFs; 40 algorithm-designated candidates)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet

---

## Method

1. Enumerate the 96 PDFs in `batch-1/` (keys A–B).
2. Pull per-paper best module, tier, and quality from `scores/index.json`.
3. Keep the **algorithm/model-designated** subset: best module in
   `ml_algorithms`, `forecasting`, `anomaly_detection`, `budget_recommendation`,
   or `expense_categorization` → **40 candidates**.
4. **Verify titles against the actual PDFs.** Batch-1 keys *had* titles in the
   manifest — but the same batch-4 pattern holds: stored titles/designations are
   only partly reliable. All titles/years in this doc were re-verified from PDF
   first-page/abstract text via pypdf.
5. Assign proposed stems per `docs/standards/rrl-naming-conventions.md`
   (`A--` algorithm focus, `L--` local Philippine, `I--` international non-algorithm).
   Local classification is based on the **author affiliation in the PDF** (e.g.
   University of Mindanao, MSU-Iligan, Caraga State, UST Manila, UP Cebu), not the
   manifest `designation`/`authors` fields — corrected where they disagree.
6. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline /
   partial fit), or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

**Scope:** algorithm/model papers only, per the requested batch flow (batch-6 → batch-5
→ batch-4 → batch-1).

> **Data-quality note:** the manifest `title`/`designation`/`year` fields for batch-1
> are unreliable in places. Corrections made against the PDFs:
> - `Almonteros et al` is **local Philippine** (Caraga State University, Butuan) —
>   manifest had it as `international-algorithm-specific`.
> - `Alunen et al` is local (University of Santo Tomas, Manila) — confirmed, matches manifest.
> - `Alejandrino et al` (UP Mindanao, Davao), `Apus et al` (MSU–Iligan), `Blancaflor et al`
>   (Mapua University, Manila), `Carillo & Serra` (UP Cebu) all hold their `local` designation.
> Years below use the journal/citation line or PDF creation date as the best signal.

---

## Batch-1 Triage (algorithm-designated candidates)

### Crucial tier (>= 0.45) — 12 papers (all with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Bhavana-2025` | AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning | 2025 | ml_algorithms 0.509 | crucial / 1.50 | **Maintain** |
| `A--Begum-2025` | Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA | 2025 | ml_algorithms 0.508 | crucial / 2.25 | **Maintain** (predominantly credit/fraud risk) |
| `A--Ayari-2026` | Machine Learning Powered Financial Credit Scoring: A Systematic Literature Review | 2026 | ml_algorithms 0.506 | crucial / 2.00 | **Maintain** |
| `L--Alejandrino-2023` | Supervised and Unsupervised Data Mining Approaches in Loan Default Prediction | 2023 | ml_algorithms 0.493 | crucial / 2.25 | **Maintain** (PH, UP Mindanao) |
| `A--Bari-2024` | A Systematic Literature Review of Predictive Models and Analytics in AI-Driven Credit Scoring | 2024 | ml_algorithms 0.483 | crucial / 2.00 | **Maintain** |
| `A--Chandana-2026` | Personal Finance Tracker with AI Based Expense Prediction | 2026 | expense_categorization 0.483 | crucial / 1.75 | **Maintain** |
| `A--Alenazi-2023` | Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking | 2023 | budget_recommendation 0.481 | crucial / 1.75 | **Maintain** |
| `A--Chahar-2026` | Artificial Intelligence Powered Personal Finance Management System | 2026 | expense_categorization 0.478 | crucial / 2.00 | **Maintain** |
| `A--Ahmed-2026` | AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion | 2026 | ml_algorithms 0.466 | crucial / 1.75 | **Maintain** (credit/debt) |
| `A--Bakuwa-2026` | Dynamic Credit Scoring with Machine Learning: Enhancing Financial Inclusion and Risk Management | 2026 | ml_algorithms 0.465 | crucial / 2.00 | **Maintain** (credit/debt) |
| `A--Aldrees-2025` | Behavioral Patterns in Micro-lending: Enhancing Credit Risk Scorecards | 2025 | ml_algorithms 0.460 | crucial / 2.25 | **Maintain** |
| `A--Ao-2025` | A Review of Time Series Prediction Models Based on Deep Learning | 2025 | forecasting 0.454 | crucial / 2.00 | Review (TS review, forecasting) |

### Supporting tier (>= 0.30) — 25 papers (23 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Bader-2025` | Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications | 2025 | anomaly_detection 0.442 | supporting / 2.25 | **Maintain** (PFM + emotion) |
| `A--AlLawati-2025` | An Integrated Preprocessing and Drift Detection Approach With Adaptive Windowing for Fraud Detection in Payment Systems | 2025 | ml_algorithms 0.435 | supporting / 2.25 | Review (fraud) |
| `L--Apus-2023` | Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm | 2023 | ml_algorithms 0.433 | supporting / 2.50 | **Maintain** (PH, MSU-Iligan) |
| `A--Cao-2024` | TEMPO: Prompt-Based Generative Pre-Trained Transformer for Time Series Forecasting | 2024 | forecasting 0.433 | supporting / 2.25 | Review (ICLR, forecasting) |
| `A--Agrawal-2025` | Analyzing and Rewarding Credit Card Spending Habits in India: A Machine Learning Approach | 2025 | expense_categorization 0.430 | supporting / 2.25 | **Maintain** (spending habits) |
| `A--Boniol-2024` | Dive into Time-Series Anomaly Detection: A Decade Review | 2024 | anomaly_detection 0.432 | supporting / 2.00 | Review (survey) |
| `__Abd-Ellatif et al__` | ATAD-Net: An Adaptive Deep Learning Framework for Real-Time Financial Anomaly Detection | — | ml_algorithms 0.432 | supporting / 2.25 | **Skip / carry-over** (no PDF) |
| `A--AlRafi-2024` | AI-Driven Fraud Detection Using Self-Supervised Deep Learning for Enhanced Customer Identity Modeling | 2024 | ml_algorithms 0.422 | supporting / 2.00 | Review (fraud) |
| `A--Ashta-2025` | Artificial Intelligence in Microfinance and Financial Inclusion: Applications, Issues, and Future Directions | 2025 | ml_algorithms 0.419 | supporting / 2.00 | Review (microfinance AI) |
| `A--Asemi-2024` | A Model for Investment Type Recommender System Based on the Learning Approaches | 2024 | ml_algorithms 0.414 | supporting / 3.75 | Review (investment) |
| `A--AhmedEtAl-2025` | Real-Time Hybrid Optimization Models for Edge-Based Financial Risk Assessment: Integrating Deep Learning with Adaptive Regression for Low-Latency Decision Making | 2025 | anomaly_detection 0.409 | supporting / 2.25 | Review (fraud/risk) |
| `A--AhmedDey-2023` | Neural Network–Based Customer Retention Forecasting in Mobile Wallet Services Using 200k Historical User Profiles | 2023 | ml_algorithms 0.406 | supporting / 2.25 | Review (retention) |
| `__Abdullahi et al__` | A Systematic Literature Review of Concept Drift Mitigation (in Financial ML) | — | ml_algorithms 0.405 | supporting / 2.00 | **Skip / carry-over** (no PDF) |
| `A--Balbal-2026` | RFM-Net: A Convolutional Neural Network for Customer Segmentation | 2026 | ml_algorithms 0.398 | supporting / 2.25 | Review (segmentation) |
| `A--AoFayek-2023` | Continual Deep Learning for Time Series Modeling | 2023 | forecasting 0.396 | supporting / 2.00 | Review (TS continual learning) |
| `L--Almonteros-2024` | Forecasting Students' Success To Graduate Using Predictive Analytics | 2024 | ml_algorithms 0.393 | supporting / 2.25 | Review (PH, Caraga State — off-finance) |
| `L--Blancaflor-2024` | Exploring Machine Learning for Credit Card Fraud Detection from a Philippine Perspective | 2024 | ml_algorithms 0.392 | supporting / 2.25 | Review (PH, Mapua — fraud) |
| `A--Casolaro-2023` | Deep Learning for Time Series Forecasting: Advances and Open Problems | 2023 | forecasting 0.390 | supporting / 2.00 | Review (survey) |
| `A--Altalhan-2025` | Imbalanced Data Problem in Machine Learning: A Review | 2025 | ml_algorithms 0.389 | supporting / 1.75 | Review (method survey) |
| `L--Alunen-2025` | Comparing Machine Learning Forecasting Models Based on Accuracy (F&B demand) | 2025 | ml_algorithms 0.387 | supporting / 2.00 | Review (PH, UST — off-finance) |
| `A--Charizanis-2025` | Data-Driven Decision Support in SaaS Cloud-Based Service Models | 2025 | ml_algorithms 0.384 | supporting / 2.00 | Review (SaaS DSS) |
| `A--Binzaid-2025` | Intelligent User Behavior Modeling for Customer Centric Fintech | 2025 | ml_algorithms 0.380 | supporting / 2.00 | Review (fintech UX) |
| `A--Adlermann-2024` | A GRA-Enhanced Cloud AI Framework for Petabyte-Scale Multi-Tenant Environments: Multivariate Classification for Credit Card Fraud Detection | 2024 | ml_algorithms 0.349 | supporting / 2.00 | Cull (cloud infra fraud) |
| `A--Andersson-2025` | Insights into the Temporal Dynamics of Identifying Problem Gambling on an Online Casino (ML on account data) | 2025 | ml_algorithms 0.337 | supporting / 4.00 | Review (gambling) |
| `A--Bauer-2023` | Expl(AI)ned: The Impact of Explainable Artificial Intelligence on Users' Information Processing | 2023 | ml_algorithms 0.300 | supporting / 3.50 | Review (XAI/HCI) |

### Cull tier (< 0.30) — 3 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `L--CarilloSerra-2025` | Optimized Nonlinear Grey Bernoulli Model for Nowcasting the Philippine Gross Domestic Product | 2025 | forecasting 0.295 | cull / 3.00 | Cull (0.295; PH nowcasting — note for contextual use) |
| `A--AnesAbreu-2025` | Adaptive Cluster-Based Normalization for Robust TOPSIS in Multi-Criteria Decision Making | 2025 | budget_recommendation 0.272 | cull / 2.25 | Cull (0.272; MCDM normalization, off-scope) |
| `A--Cau-2026` | Exploring the Impact of Explainable AI and Cognitive Capabilities on Users' Decision Making | 2026 | ml_algorithms 0.267 | cull / 3.00 | Cull (0.267; XAI off-scope) |

Only 3 papers landed strictly below 0.30; the cull bucket is small because batch-1's
algorithm-designated set skews strongly toward direct finance/credit/forecasting topics.

### No-sourcing candidates (PDF unavailable)

| Index key | Status |
| :--- | :--- |
| `Abd-Ellatif et al` | **Skip / carry-over flag** — no PDF found in batch-1 dir, bucket, or other batches (supporting, 0.432) |
| `Abdullahi et al` | **Skip / carry-over flag** — no PDF found in batch-1 dir, bucket, or other batches (supporting, 0.405) |

---

## Algorithm/Model-Designated Papers (Budi Candidates) — detail

### Crucial tier (top priority for intake)

1. **Bhavana et al. (2025)** — *AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning*
   - **Best module:** ml_algorithms 0.509 (crucial) — top score in batch-1; quality 1.50.
   - **Why it fits:** AI wealth-advisory + personalized budget planning via ML/predictive
     analytics — a direct savings/budgeting §3 fit for an intelligent PFM app.
   - **Source:** `Bhavana et al.pdf` (Surana College, Bengaluru, India).

2. **Begum (2025)** — *Machine Learning in Financial Risk and Behavior Analysis: Bankruptcy, Fraud, and Consumer Trends in the USA*
   - **Best module:** ml_algorithms 0.508 (crucial); quality 2.25.
   - **Why it fits:** ML framework predicting bankruptcy/fraud/consumer-trend behavior —
     a behavior-analysis evidence paper relevant to spending/financial-health early warning
     (§2.4.4 / §3).
   - **Source:** `Begum.pdf` (Trine University, USA).

3. **Ayari et al. (2026)** — *Machine Learning Powered Financial Credit Scoring: A Systematic Literature Review*
   - **Best module:** ml_algorithms 0.506 (crucial); quality 2.00.
   - **Why it fits:** systematic review of ML credit-scoring models — debt/credit scoring
     methodology (§2.4.4.2 / §3).
   - **Source:** `Ayari et al.pdf` (Artificial Intelligence Review 59:13).

4. **Alejandrino et al. (2023)** — *Supervised and Unsupervised Data Mining Approaches in Loan Default Prediction*
   - **Best module:** ml_algorithms 0.493 (crucial); quality 2.25.
   - **Why it fits:** loan-default prediction comparing supervised/unsupervised approaches
     from **University of Mindanao, Philippines** — local PH debt/credit classifier evidence
     (§2.4.4.2 / debt_management).
   - **Source:** `Alejandrino et al.pdf` (IJECE, University of Mindanao Davao).

5. **Bari et al. (2024)** — *A Systematic Literature Review of Predictive Models and Analytics in AI-Driven Credit Scoring*
   - **Best module:** ml_algorithms 0.483 (crucial); quality 2.00.
   - **Why it fits:** credit-scoring predictive-models SLR — complements Ayari et al; debt
     dimension (§2.4.4.2 / §3).
   - **Source:** `Bari et al.pdf` (Lamar University; JMLDEDS).

6. **Chandana et al. (2026)** — *Personal Finance Tracker with AI Based Expense Prediction*
   - **Best module:** expense_categorization 0.483 (crucial); quality 1.75.
   - **Why it fits:** personal-finance tracker with AI expense prediction — direct expense-
     categorization / PFM tracker evidence (§2.4.4.1 / §3).
   - **Source:** `Chandana et al.pdf` (Sri Indu College, Hyderabad, India).

7. **Alenazi & Sas (2023)** — *Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking*
   - **Best module:** budget_recommendation 0.481 (crucial); quality 1.75.
   - **Why it fits:** mental-accounting-based evaluation of budgeting apps — budgeting-
     behavior design evidence (§2.4.4.2 / budgeting / §3).
   - **Source:** `Alenazi & Sas.pdf` (Lancaster University, UK; BCS HCI 2023).

8. **Chahar et al. (2026)** — *Artificial Intelligence Powered Personal Finance Management System*
   - **Best module:** expense_categorization 0.478 (crucial); quality 2.00.
   - **Why it fits:** AI-powered PFM system — a direct system-design paper for expense
     categorization / transaction workflows (§2.4.4.1 / §3).
   - **Source:** `Chahar et al.pdf` (SSCSE, India).

9. **Ahmed (2026)** — *AI-Driven Credit Risk Assessment in Fintech Lending: Implications for Financial Inclusion*
   - **Best module:** ml_algorithms 0.466 (crucial); quality 1.75.
   - **Why it fits:** credit-risk assessment in fintech lending — debt default prediction
     (§2.4.4.2 / debt_management).
   - **Source:** `Ahmed.pdf` (AIJBM).

10. **Bakuwa & Jimu (2026)** — *Dynamic Credit Scoring with Machine Learning: Enhancing Financial Inclusion and Risk Management*
    - **Best module:** ml_algorithms 0.465 (crucial); quality 2.00.
    - **Why it fits:** dynamic ML credit-scoring for financial inclusion — debt/credit scoring
      (§2.4.4.2 / §3).
    - **Source:** `Bakuwa & Jimu.pdf` (Afriresearch).

11. **Aldrees et al. (2025)** — *Behavioral Patterns in Micro-lending: Enhancing Credit Risk Scorecards*
    - **Best module:** ml_algorithms 0.460 (crucial); quality 2.25.
    - **Why it fits:** behavioral micro-lending credit risk scorecards — credit/debt + behavior
      (§2.4.4.2 / §3 / behavior).
    - **Source:** `Aldrees et al.pdf` (IJ Comput Intell Syst 2025).

### Supporting tier (promising, needs RRL verdict)

12. **Bader & Haraty (2025)** — *Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications*
    - **Best module:** anomaly_detection 0.442 (supporting); quality 2.25 (Lebanese American University).
    - **Why it fits:** emotion-enhanced models for personal finance manager apps — directly
      relevant to personalized PFM (emotion/behavioral dimension, §2.4.4.4 / §3).
13. **Apus et al. (2023)** — *Predicting the Filipino Household Income Using Naive Bayes Classification Algorithm*
    - **Best module:** ml_algorithms 0.433 (supporting); quality 2.50.
    - **Why it fits:** predicting **Filipino household income** with Naive Bayes from
      **MSU–Iligan Institute of Technology** — local PH income/affordability classifier,
      ideal for PH-context savings/budget recommendations (§2.4.4.2 / §3).
14. **Agrawal et al. (2025)** — *Analyzing and Rewarding Credit Card Spending Habits in India: A Machine Learning Approach*
    - **Best module:** expense_categorization 0.430 (supporting); quality 2.25.
    - **Why it fits:** ML on credit-card spending habits for reward/promotion targeting —
      spending-pattern analytics transferable to expense categorization (§2.4.4.1 / §3).

### Review / borderline

- **Fraud/compliance family:** Al Lawati et al, Al Rafi, Ahmed et al (edge risk), Blancaflor
  et al — relevant to the anomaly-detection sibling as shared-module evidence, but target
  bank/card fraud rather than personal overspending detection. `Blancaflor et al` is **local PH
  (Mapua University)** — note for shared anomaly context.
- **Forecasting/methodology:** Cao et al (TEMPO, ICLR 2024), Peng-era TS reviews (Ao et al 2025,
  Casolaro 2023), Ao & Fayek (continual DL) — strong forecasting evidence but methodology-oriented;
  decide via forecasting sibling scope.
- **Segmentation/marketing:** Balbal & Birant (RFM-Net), Ahmed & Dey (wallet retention),
  Charizanis (SaaS DSS), Binzaid (fintech UX) — customer analytics tangential to savings/debt.
- **Off-domain local PH:** Almonteros et al (Caraga State — students' graduation, not finance),
  Alunen et al (UST — F&B demand forecasting) — hold as local-context notes only.
- **Investment/other finance:** Asemi (investment recommender), Ashta (microfinance AI review),
  Andersson (gambling behavior), Bauer (XAI/HCI) — partial fit for §3/§2.4 context only.
- `Cao et al`/`Ao et al`: TEMPO and the TS review pair are strong forecasting references; keep
  on Review pending the forecasting sibling's §3 need (their 0.43/0.45 scores favor inclusion).

### Cull / defer

- `Adlermann` (cloud/petabyte infra + credit-card fraud) — infrastructure-heavy, off-scope for
  personal savings/debt algorithms.
- `Anes & Abreu` (TOPSIS multi-criteria normalization, 0.272) — MCDM methodology, off-scope.
- `Carillo & Serra` (PH GDP nowcasting, < 0.30) — UP Cebu; keep as possible contextual note
  for forecasting/PH economic context despite cull tier.
- `Cau & Spano` (XAI + cognitive capabilities, < 0.30) — off-scope.

---

## Topical Outline Mapping (§3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Bhavana et al 2025 | §2.4.4.2 / §3, savings + budgeting | AI wealth advisory + budget planning |
| Begum 2025 | §2.4.4 / §3, behavior | Financial risk & behavior analysis |
| Ayari et al 2026 | §2.4.4.2 / §3, credit | Credit scoring SLR |
| Alejandrino et al 2023 | §2.4.4.2 / §3, loan (L--) | Loan-default data mining, PH |
| Bari et al 2024 | §2.4.4.2 / §3, credit | AI credit-scoring SLR |
| Chandana et al 2026 | §2.4.4.1 / §3, expense | PFM tracker + AI expense prediction |
| Alenazi & Sas 2023 | §2.4.4.2 budgeting | Budgeting-app evaluation (mental accounting) |
| Chahar et al 2026 | §2.4.4.1 / §3, expense | AI-powered PFM system |
| Ahmed 2026 | §2.4.4.2 / §3, credit | Fintech credit risk |
| Bakuwa & Jimu 2026 | §2.4.4.2 / §3, credit | Dynamic credit scoring |
| Aldrees et al 2025 | §2.4.4.2 / §3, credit + behavior | Behavioral micro-lending risk |
| Bader & Haraty 2025 | §2.4.4.4 / §3, emotion | Emotion-enhanced PFM models |
| Apus et al 2023 | §2.4.4.2 / §3, income (L--) | Filipino household income, Naive Bayes |
| Agrawal et al 2025 | §2.4.4.1 / §3, spending | Credit-card spending analytics |

Remaining papers map mostly to fraud/compliance (shared anomaly sibling), forecasting
methodology (Ao, Cao, Casolaro, Ao & Fayek), segmentation/marketing, or off-scope domains
(education, F&B, cloud infra, gambling) outside the personal savings/debt algorithm focus.

---

## Recommended Next Steps

1. **Confirm verdicts** for the "Review" papers — researcher decision, especially the
   forecasting-methodology pair (Ao et al, Cao et al — high scores suggest inclusion), the
   fraud family (esp. local PH `Blancaflor et al`), and the two borderline local `L--`
   papers (Almonteros et al, Alunen et al — off-domain but PH-relevant).
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   proposed stems → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Survive-note carry-overs:** `Abd-Ellatif et al` (supporting, 0.432) and
   `Abdullahi et al` (supporting, 0.405) have no recoverable PDF in this workspace — flag
   for the researcher to re-fetch from the Drive source before inclusion.
4. **Re-score** once the intake lands — batch-1 old-run best_module/best_score values were
   computed from the deprecated 518-paper corpus and will be replaced by the batch-7 run.