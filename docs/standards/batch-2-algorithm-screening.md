# Batch-2 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-2/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-2/` (96 PDFs; 42 algorithm-designated candidates)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet

---

## Method

1. Enumerate the PDFs in `batch-2/` (keys C–H).
2. Pull per-paper best module, tier, and quality from `scores/index.json`.
3. Keep the **algorithm/model-designated** subset: best module in
   `ml_algorithms`, `forecasting`, `anomaly_detection`, `budget_recommendation`,
   or `expense_categorization` → **42 candidates**.
4. **Verify titles against the actual PDFs.** Same as batch-1/4, manifest titles
   are only partly reliable. Corrections made against the PDFs include:
   - `D. R. et al`: real title is *Robust Learning Under Distribution Shifts for
     Non-Stationary Data Environments* — the manifest title (`AHO-InDNN: ... Fraud
     Detection`) is the model name/alias used inside the paper.
   - `Dhanekula & Munira`: manifest said "Deep Neural Network Architectures...";
     PDF title is *Deep Neural Network Models for Real-Time Financial Forecasting
     and Market Intelligence*.
   - `de Goma et al`: manifest said collaborative-filtering music recommendation;
     PDF title is *Using Item Personality-Based Profiling in Music Recommender Systems*.
5. Assign proposed stems per `docs/standards/rrl-naming-conventions.md`
   (`A--` algorithm focus, `L--` local Philippine, `I--` international non-algorithm).
   Local classification is based on the **author affiliation in the PDF** (MSU–Iligan,
   TUP Manila, Mapua Makati), not the manifest `designation` fields.
6. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline /
   partial fit), or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

**Scope:** algorithm/model papers only, per the requested batch flow (batch-6 → batch-5
→ batch-4 → batch-1 → batch-2).

> **Data-quality note:** batch-2's manifest `title`/`designation`/`year` fields are
> unreliable in places (see corrections above; `Fariha et al` retrievable only with the
> "Advanced" keyword, not its manifest title prefix). Years below use the journal/citation
> line or PDF creation date as the best signal.

---

## Batch-2 Triage (algorithm-designated candidates)

### Crucial tier (>= 0.45) — 8 papers (all with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Fariha-2025` | Advanced Fraud Detection Using Machine Learning Models: Enhancing Financial Transaction Security | 2025 | anomaly_detection 0.563 | crucial / 2.25 | **Maintain** (top score batch-2) |
| `A--Darwish-2025` | Intelligent Approach to Detecting Online Fraudulent Trading with Solution for Imbalanced Data in Fintech Forensics | 2025 | anomaly_detection 0.489 | crucial / 2.25 | Review (fraud) |
| `A--Compagnino-2025` | An Introduction to Machine Learning Methods for Fraud Detection | 2025 | anomaly_detection 0.488 | crucial / 2.00 | Review (fraud survey) |
| `A--DSouza-2026` | A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems | 2026 | forecasting 0.488 | crucial / 2.00 | **Maintain** (PFM ML review) |
| `A--Gulbakyt-2025` | Dynamic Model for Budget Allocation via Multi-Criteria Optimization | 2025 | budget_recommendation 0.486 | crucial / 2.00 | **Maintain** (budget allocation) |
| `A--HoangWiegratz-2023` | Machine Learning Methods in Finance: Recent Applications and Prospects | 2023 | ml_algorithms 0.471 | crucial / 2.25 | **Maintain** (finance ML review) |
| `A--Ghonaim-2025` | Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network | 2025 | budget_recommendation 0.465 | crucial / 2.00 | **Maintain** (RNN budget app) |
| `A--Hossain-2025` | Enhancing Credit Scoring with Multimodal Deep Learning: A Hybrid Neural Network Approach Using Structured and Unstructured Financial Data | 2025 | ml_algorithms 0.454 | crucial / 2.00 | **Maintain** (credit/debt) |

### Supporting tier (>= 0.30) — 31 papers (28 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Gong-2026` | Research Progress and Trends of Deep Learning in Stock Price Prediction: A Systematic Review from LSTM to Transformer | 2026 | forecasting 0.441 | supporting / 1.75 | Review (stock, not personal) |
| `__Chen & Lin__` | Deep Learning-Based Credit Risk Modeling: Addressing Data Imbalance and Interpretability | — | ml_algorithms 0.439 | supporting / 2.00 | **Skip / carry-over** (no PDF) |
| `A--deZarza-2024` | Optimization of Personal Budgeting with Large Language Models | 2024 | budget_recommendation 0.439 | supporting / 2.75 | **Maintain** (LLM budgeting) |
| `A--George-2023` | Machine Learning for Fraud Detection in Digital Banking: A Systematic Review | 2023 | anomaly_detection 0.438 | supporting / 2.00 | Review (fraud survey) |
| `A--Ciric-2023` | Single and Multiple Separate LSTM Neural Networks for Multiple Output Feature Purchase Prediction | 2023 | forecasting 0.436 | supporting / 2.00 | Review (purchase prediction) |
| `A--HallRasheed-2025` | A Survey of Machine Learning Methods for Time Series Prediction | 2025 | ml_algorithms 0.435 | supporting / 2.75 | Review (survey) |
| `A--Chikoore-2026` | Adaptive Credit Scoring Model With Concept Drift Detection and Adaptation | 2026 | ml_algorithms 0.428 | supporting / 2.00 | **Maintain** (credit/debt) |
| `A--Chowdhury-2025` | A Systematic Review of Demand Forecasting Models for Retail E-Commerce: Enhancing Accuracy in Inventory and Delivery Planning | 2025 | forecasting 0.428 | supporting / 2.00 | Review (e-commerce demand) |
| `A--HanLai-2026` | Temporal Feature Engineering and Threshold Optimization for Early Warning in Healthcare Claims Anomaly Detection | 2026 | anomaly_detection 0.423 | supporting / 2.25 | Review (healthcare claims) |
| `__Chen J. et al__` | A Survey of Time Series Data Forecasting Methods Based on Deep Learning | — | forecasting 0.418 | supporting / 2.00 | **Skip / carry-over** (no PDF) |
| `A--Fathy-2024` | Artificial Intelligence and Predictive Data Analytics to Enhance Risk Assessment and Credit Scoring Mechanisms in Retail Banking | 2024 | ml_algorithms 0.417 | supporting / 2.00 | **Maintain** (credit/debt) |
| `A--Hartomo-2025` | A Novel Weighted Loss TabTransformer Integrating Explainable AI for Imbalanced Credit Risk Datasets | 2025 | ml_algorithms 0.414 | supporting / 2.00 | **Maintain** (credit/XAI) |
| `A--Contreras-2026` | Adaptive Risk Evaluation in FinTech Systems via Reinforcement-Based Continuous Policy Optimization | 2026 | ml_algorithms 0.400 | supporting / 2.00 | Review (RL risk) |
| `A--Hashemi-2024` | A User-Centric Exploration of Axiomatic Explainable AI in Participatory Budgeting | 2024 | budget_recommendation 0.392 | supporting / 1.75 | Review (civic budgeting XAI) |
| `A--Goncu-2026` | Machine Learning for Risk Profiling: An Analysis of Pension Fund Participants | 2026 | ml_algorithms 0.389 | supporting / 4.00 | Review (pension risk) |
| `A--Holmgren-2025` | AI-Augmented Fraud Detection in Cloud Platforms: GRA-Based Risk Ranking with Cybersecurity and Threat Prevention for SAP HANA Healthcare ERP | 2025 | anomaly_detection 0.389 | supporting / 2.00 | Review (cloud infra fraud) |
| `L--Delena-2025` | Predicting Student Retention: A Comparative Study of Machine Learning Approach Utilizing Sociodemographic and Academic Factors | 2025 | ml_algorithms 0.380 | supporting / 2.25 | Review (PH, MSU-Iligan — off-finance) |
| `A--ChenY-2024` | Going Concern and Bankruptcy Prediction under Extreme Class Imbalance | 2024 | ml_algorithms 0.379 | supporting / 2.25 | Review (bankruptcy, business) |
| `A--Dritsas-2025` | Machine Learning in E-Commerce: A Comprehensive Survey of Applications | 2025 | ml_algorithms 0.379 | supporting / 3.00 | Review (e-commerce) |
| `A--Dhanekula-2026` | Deep Neural Network Models for Real-Time Financial Forecasting and Market Intelligence | 2026 | ml_algorithms 0.378 | supporting / 2.25 | Review (market intelligence) |
| `__Chen & Tan__` | LSTM-Based Consumer Behavior Prediction Model Research | — | ml_algorithms 0.371 | supporting / 1.75 | **Skip / carry-over** (no PDF) |
| `A--Duvalla-2025` | Human-AI Collaboration in Customer Behavior Research: Personalizing Financial Services | 2025 | ml_algorithms 0.370 | supporting / 1.75 | Review (customer behavior) |
| `A--Hall-2025` | Machine Learning Time Series Forecasting: A Comprehensive Survey and Stock Market Application | 2025 | ml_algorithms 0.369 | supporting / 2.75 | Review (survey/stock) |
| `A--DR-2026` | Robust Learning Under Distribution Shifts for Non-Stationary Data Environments (AHO-InDNN) | 2026 | ml_algorithms 0.360 | supporting / 2.00 | Review (fraud/concept drift) |
| `A--Heirene-2026` | Predicting Problem Gambling Among Online Sports and Race Bettors: Assessing the Value of Machine Learning Using Behavioural and Self-Reported Data | 2026 | ml_algorithms 0.358 | supporting / 2.25 | Review (gambling) |
| `L--Guban-2025` | WEKA-Based Decision-Tree Model for User Subscription Plan Prediction | 2025 | ml_algorithms 0.349 | supporting / 2.00 | Review (PH, TUP Manila — streaming, off-finance) |
| `A--Hamidi-2024` | An Approach Based on Data Mining and Genetic Algorithm to Optimizing Time Series Clustering for Efficient Segmentation of Customer Behavior | 2024 | expense_categorization 0.345 | supporting / 2.25 | Review (segmentation) |
| `A--ChenX-2025` | Rethinking Time Encoding via Learnable Transformation Functions | 2025 | forecasting 0.332 | supporting / 2.25 | Review (ML method) |
| `A--Essahraui-2025` | Human Behavior Analysis: A Comprehensive Survey on Techniques, Applications | 2025 | ml_algorithms 0.326 | supporting / 2.00 | Review (behavior survey) |
| `L--deGoma-2025` | Using Item Personality-Based Profiling in Music Recommender Systems | 2025 | ml_algorithms 0.317 | supporting / 2.00 | Review (PH, Mapua Makati — music, off-finance) |
| `A--Guido-2023` | A Hyper-Parameter Tuning Approach for Cost-Sensitive Support Vector Machine Classifiers | 2023 | ml_algorithms 0.316 | supporting / 2.25 | Review (method) |

### Cull tier (< 0.30) — 3 papers (1 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `__Chen V. et al__` | Understanding the Role of Human Intuition on Reliance in Human-AI Decision Making | — | ml_algorithms 0.281 | cull / 2.50 | **Skip / carry-over** (no PDF; cull) |
| `A--Fei-2023` | Impact of Mental Representation on Consumer Behaviors: Implications for Mental Budgeting and Prediction Algorithm Preferences | 2023 | budget_recommendation 0.266 | cull / 2.00 | Cull (0.266; dissertation, mental budgeting — note for contextual) |
| `A--Hassan-2024` | GCZRec: Generative Collaborative Zero-Shot Framework for Cold Start News Recommendation | 2024 | ml_algorithms 0.262 | cull / 2.00 | Cull (0.262; news rec, off-scope) |

### No-sourcing candidates (PDF unavailable)

| Index key | Status |
| :--- | :--- |
| `Chen & Lin` | **Skip / carry-over flag** — no PDF found in batch-2 dir, bucket, or other batches (supporting, 0.439) |
| `Chen J. et al` | **Skip / carry-over flag** — no PDF found (supporting, 0.418) |
| `Chen & Tan` | **Skip / carry-over flag** — no PDF found (supporting, 0.371) |
| `Chen V. et al` | **Skip / carry-over flag** — no PDF found (cull, 0.281) |

---

## Algorithm/Model-Designated Papers (Budi Candidates) — detail

### Crucial tier (top priority for intake)

1. **Fariha et al. (2025)** — *Advanced Fraud Detection Using Machine Learning Models: Enhancing Financial Transaction Security*
   - **Best module:** anomaly_detection 0.563 (crucial) — highest score in batch-2; quality 2.25.
   - **Why it fits:** ML fraud-detection framework for financial transaction security — the
     strongest anomaly/financial-health evidence in this batch (§2.4.4.4 / §3).
   - **Source:** `Fariha et al.pdf` (Univ. Bridgeport et al; Int J Accounting & Economics Studies).

2. **D'Souza et al. (2026)** — *A Comprehensive Review of Machine Learning Techniques for Intelligent Personal Finance Management Systems*
   - **Best module:** forecasting 0.488 (crucial); quality 2.00 (P.E.S Modern College of Engineering, Pune, India).
   - **Why it fits:** a review dedicated to **ML techniques for intelligent PFM systems** —
     a direct §2.4/§3 fit (personal finance management scope).
   - **Source:** `D'Souza et al.pdf`.

3. **Gulbakyt et al. (2025)** — *Dynamic Model for Budget Allocation via Multi-Criteria Optimization*
   - **Best module:** budget_recommendation 0.486 (crucial); quality 2.00.
   - **Why it fits:** dynamic budget-allocation via multi-criteria optimization — a direct
     budget-recommendation algorithm paper (§2.4.4.2 / budgeting / §3).
   - **Source:** `Gulbakyt et al.pdf` (J. Applied Data Sciences).

4. **Hoang & Wiegratz (2023)** — *Machine Learning Methods in Finance: Recent Applications and Prospects*
   - **Best module:** ml_algorithms 0.471 (crucial); quality 2.25 (Karlsruhe Institute of Technology; EFM).
   - **Why it fits:** survey of ML methods in finance — methodological context spanning
     classification/forecasting/anomaly applications (§2.4.4 / §3).
   - **Source:** `Hoang & Wiegratz.pdf`.

5. **Ghonaim & El-Sharawy (2025)** — *Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network*
   - **Best module:** budget_recommendation 0.465 (crucial); quality 2.00 (Al-Azhar University, Cairo).
   - **Why it fits:** an RNN-based **budget-management mobile application** — direct
     budget-tracking/forecasting system evidence (§2.4.4.2 / budgeting / §3).
   - **Source:** `Ghonaim & El-Sharawy.pdf`.

6. **Hossain et al. (2025)** — *Enhancing Credit Scoring with Multimodal Deep Learning (Structured + Unstructured Data)*
   - **Best module:** ml_algorithms 0.454 (crucial); quality 2.00 (Westcliff University et al).
   - **Why it fits:** multimodal deep-learning credit scoring — debt/credit classification
     (§2.4.4.2 / debt_management).
   - **Source:** `Hossain et al.pdf`.

### Supporting tier (promising, needs RRL verdict)

7. **de Zarza et al. (2024)** — *Optimization of Personal Budgeting with Large Language Models*
   - **Best module:** budget_recommendation 0.439 (supporting); quality 2.75 (MDPI AI).
   - **Why it fits:** LLM-driven personal-budgeting optimization — direct §3 evidence for
     LLM-based budgeting/recommendation features (note an earlier PDF name variant
     "Optimized Financial Planning..." exists; verified title per MDPI citation).
8. **Chikoore et al. (2026)** — *Adaptive Credit Scoring Model With Concept Drift Detection and Adaptation* (IEEE Access)
   - **Best module:** ml_algorithms 0.428 (supporting); quality 2.00.
   - **Why it fits:** concept-drift-aware credit scoring — debt + drift robustness
     (§2.4.4.2 / §3).
9. **Fathy (2024)** — *AI and Predictive Data Analytics to Enhance Risk Assessment and Credit Scoring in Retail Banking*
   - **Best module:** ml_algorithms 0.417 (supporting); quality 2.00 (Nile University).
   - **Why it fits:** credit scoring / risk-assessment with AI — debt dimension (§2.4.4.2).
10. **Hartomo et al. (2025)** — *A Novel Weighted Loss TabTransformer Integrating XAI for Imbalanced Credit Risk Datasets* (IEEE Access)
    - **Best module:** ml_algorithms 0.414 (supporting); quality 2.00.
    - **Why it fits:** XAI + transformer credit-risk classification under imbalance —
      credit/debt + explainability (§3.4 + §2.4.4.2).

### Review / borderline

- **Fraud/anomaly sibling:** Darwish, Compagnino, George, Holmgren, D. R. et al (AHO-InDNN),
  Han & Lai (healthcare claims) — relevant to the anomaly-detection sibling as shared-module
  evidence, but target bank/card/healthcare fraud rather than personal overspending detection.
- **Forecasting methodology / surveys:** Gong, Ciric, Hall & Rasheed, Chowdhury, Chen J.,
  Hall, Chen X. — methodological or stock/e-commerce-demand forecasting, tangential to
  personal-savings forecasting.
- **Credit/bankruptcy (business-facing):** Chen Y. (bankruptcy under imbalance), Contreras
  (FinTech RL risk), Goncu (pension risk) — credit-adjacent but business/investment oriented.
- **Behavior/marketing:** Duvalla, Hamidi, Essahraui — customer-behavior ML, not
  savings/debt-specific.
- **Off-domain local PH:** Delena et al (MSU-Iligan — student retention), Guban et al
  (TUP Manila — streaming subscription), de Goma et al (Mapua Makati — music recommender) —
  hold as local-context notes only.

### Cull / defer

- `Fei` (mental-budgeting dissertation, < 0.30) — mental-budgeting link noted for contextual
  background despite low score.
- `Hassan et al` (GCZRec, news recommendation) and `Chen V. et al` (human-AI reliance, no PDF)
  — off-scope/low relevance.

---

## Topical Outline Mapping (§3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Fariha et al 2025 | §2.4.4.4 / §3, anomaly | ML fraud/anomaly detection for financial transactions |
| D'Souza et al 2026 | §2.4.1 / §3, PFM | ML techniques for intelligent PFM systems (review) |
| Gulbakyt et al 2025 | §2.4.4.2 / §3, budgeting | Multi-criteria budget allocation |
| Hoang & Wiegratz 2023 | §2.4.4 / §3 | ML methods in finance (survey) |
| Ghonaim & El-Sharawy 2025 | §2.4.4.2 / §3, budgeting | RNN budget-management app |
| Hossain et al 2025 | §2.4.4.2 / §3, credit | Multimodal deep-learning credit scoring |
| de Zarza et al 2024 | §2.4.4.2 / §3, budgeting | LLM personal-budgeting optimization |
| Chikoore et al 2026 | §2.4.4.2 / §3, credit | Drift-adaptive credit scoring |
| Fathy 2024 | §2.4.4.2 / §3, credit | AI credit scoring (retail banking) |
| Hartomo et al 2025 | §2.4.4.2 / §3, credit + XAI | TabTransformer credit-risk with XAI |

Remaining papers map mostly to fraud/compliance (shared anomaly sibling), methodology
surveys, market/pension/bankruptcy, customer-behavior marketing, or off-scope domains
(music, streaming, healthcare claims, news).

---

## Recommended Next Steps

1. **Confirm verdicts** for the "Review" papers — researcher decision, especially the
   fraud/anomaly family (Darwish, Compagnino, George, Holmgren, D. R.), the forecasting-
   methodology surveys (Gong, Ciric, Hall & Rasheed, Hall), and the borderline local `L--`
   papers (Delena, Guban, de Goma — all off-domain but PH-relevant).
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   proposed stems → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Survive-note carry-overs:** `Chen & Lin` (0.439), `Chen J. et al` (0.418), `Chen & Tan`
   (0.371), and `Chen V. et al` (0.281) have no recoverable PDF in this workspace — flag for
   the researcher to re-fetch from the Drive source before inclusion.
4. **Re-score** once the intake lands — batch-2 old-run best_module/best_score values were
   computed from the deprecated 518-paper corpus and will be replaced by the batch-7 run.