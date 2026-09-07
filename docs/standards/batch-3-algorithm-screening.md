# Batch-3 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-3/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-3/` (96 PDFs; 55 algorithm-designated candidates; 53 with PDF)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet
- **This is the last batch** — batches 6, 5, 4, 1, 2 docs already exist in `docs/standards/`

---

## Method

1. Enumerate the PDFs in `batch-3/` (keys I–M + two no-PDF carry-overs).
2. Pull per-paper best module, tier, and quality from `scores/index.json`.
3. Keep the **algorithm/model-designated** subset: best module in
   `ml_algorithms`, `forecasting`, `anomaly_detection`, `budget_recommendation`,
   or `expense_categorization` → **55 candidates** (53 PDFs + 2 missing).
4. **Verify titles against the actual PDFs.** Batch-3 manifest titles were
   unreliable — re-verified every title from PDF first-page/abstract text via pypdf.
   Notable corrections: `Lockwood et al`'s stored title ("Designing for Financial
   Literacy…") was wrong — the paper is *Machine Learning Approaches for Credit
   Default Prediction in Emerging Economies*; `Kashif & Naseer` stored title was
   truncated. Years taken from the journal/citation line or PDF creation date.
5. Assign proposed stems per `docs/standards/rrl-naming-conventions.md`
   (`A--` algorithm focus, `L--` local Philippine, `I--` international non-algorithm).
   Local classification is based on the **author affiliation in the PDF** (e.g.
   Mapua University Makati, University of Southeastern Philippines), not the
   unreliable manifest `designation` field — `Mariano & Monreal` was stored as
   international but is **local (`L--`)**, Mapua.
6. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline /
   partial fit), or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

**Scope:** algorithm/model papers only, per the requested batch flow (batch-6 → batch-5
→ batch-4 → batch-1 → batch-2 → batch-3).

> **Data-quality note:** the manifest `title`/`authors`/`designation`/`year` fields for
> batch 1–4 are unreliable. Years below use the journal/citation line or PDF creation
> date as the best available signal.
>
> **Cross-batch finding:** `Kowsar M. et al-2023` is the **same paper** flagged as
> no-PDF `Mohiuddin et al` in the batch-4 screening (0.462, *Credit Decision Automation
> in Commercial Banks: A Review of AI and Predictive Analytics in Loan Assessment*) —
> the batch-3 PDF recovers that batch-4 carry-over. The related `Mohammad et al` (0.468,
> batch-4 carry-over) remains no-PDF.

---

## Batch-3 Triage (algorithm-designated candidates)

### Crucial tier (>= 0.45) — 12 papers (11 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--KashifNaseer-2025` | Comprehensive Analysis of Fraud Detection and Prevention Systems for Accuracy and Efficacy | 2025 | anomaly_detection 0.499 | crucial / 2.00 | Review (fraud) |
| `A--Khan-2025` | Model-Agnostic Explainable Artificial Intelligence Methods in Finance: A Systematic Review, Recent Developments, Limitations, Challenges and Future Directions | 2025 | ml_algorithms 0.485 | crucial / 2.00 | **Maintain** |
| `A--LuongXie-2026` | Explainable Ensemble Machine Learning for Financial Transaction Fraud Detection | 2026 | ml_algorithms 0.483 | crucial / 2.25 | Review (fraud) |
| `__Huang A. et al__` | Dynamic Calibration of Decision Thresholds for Financial Anomaly Detection | — | anomaly_detection 0.481 | crucial / 3.25 | **Skip / carry-over** (no PDF) |
| `A--Kontopoulou-2023` | ARIMA vs. Machine Learning Approaches for Time Series Forecasting in Data-Driven Networks | 2023 | forecasting 0.476 | crucial / 2.00 | Review (methodology) |
| `A--LuYifei-2025` | A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting | 2025 | budget_recommendation 0.474 | crucial / 2.25 | **Maintain** (budget) |
| `A--Jayaprakashnarayan-2026` | AI-Enabled NLP Framework for Automated Expense Management and Financial Transactions | 2026 | expense_categorization 0.470 | crucial / 3.25 | **Maintain** (expense) |
| `A--KaraSenguler-2025` | A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review | 2025 | forecasting 0.466 | crucial / 2.00 | **Maintain** (budget forecast) |
| `A--Judijanto-2024` | Early Warning Systems for Financial Distress: A Machine Learning Approach | 2024 | ml_algorithms 0.465 | crucial / 2.00 | Review (corporate distress) |
| `A--Kowsar-2023` | Credit Decision Automation in Commercial Banks: A Review of AI and Predictive Analytics in Loan Assessment | 2023 | ml_algorithms 0.462 | crucial / 2.00 | **Maintain** (credit; = batch-4 `Mohiuddin` PDF) |
| `A--LiChen-2025` | Dynamic Quantification Anti-Fraud Machine Learning Model for Real-Time Transaction Monitoring | 2025 | anomaly_detection 0.456 | crucial / 2.25 | Review (fraud) |
| `A--Krstev-2023` | An Overview of Forecasting Methods for Monthly Electricity Consumption | 2023 | forecasting 0.453 | crucial / 2.00 | Cull (electricity) |

### Supporting tier (>= 0.30) — 42 papers (41 with PDF)

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Kalideen-2025` | Detection of Fraudulent Transaction Issues in the Payment Card Industry Using Intelligent Models | 2025 | anomaly_detection 0.449 | supporting / 1.75 | Review (fraud) |
| `A--Karthikeyan-2026` | A High-Recall Cost-Sensitive Machine Learning Framework for Real-Time Online Banking Transaction Fraud Detection | 2026 | anomaly_detection 0.449 | supporting / 2.00 | Review (fraud; venue unverified) |
| `L--LaspinasMurcia-2024` | Machine Learning Approaches in Classifying Income Levels | 2024 | ml_algorithms 0.440 | supporting / 2.00 | **Maintain** (L--, income) |
| `A--MaP-2023` | Review of Family-Level Short-Term Load Forecasting and Its Application in Smart Grids | 2023 | forecasting 0.439 | supporting / 2.25 | Cull (electricity) |
| `A--Malave-2026` | Transforming Financial Documents into Credit Decisions Using Explainable AI | 2026 | ml_algorithms 0.439 | supporting / 2.25 | **Maintain** (credit + XAI) |
| `A--Mienye-2026` | Deep Learning for Credit Risk Prediction: A Survey of Major Modeling Techniques | 2026 | ml_algorithms 0.439 | supporting / 2.00 | **Maintain** (credit survey) |
| `A--Mamun-2025` | Advancements in Machine Learning for Customer Retention: A Systematic Review | 2025 | ml_algorithms 0.436 | supporting / 2.25 | Review (churn) |
| `A--KimJ-2025` | A Comprehensive Survey of Deep Learning for Time Series Forecasting: Architectures and Applications | 2025 | forecasting 0.433 | supporting / 2.25 | Review (generic TS survey) |
| `A--IslamA-2026` | Benchmarking Machine Learning Models for Real-Time Fraud Detection in Financial Services | 2026 | ml_algorithms 0.431 | supporting / 2.25 | Review (fraud) |
| `A--Imani-2025` | Customer Churn Prediction: A Systematic Review of Recent Advances and Trends | 2025 | ml_algorithms 0.424 | supporting / 2.00 | Review (churn) |
| `A--Lou-2026` | Predicting Customer Buying Habits Using Convolutional Neural Network | 2026 | ml_algorithms 0.416 | supporting / 3.75 | Review (e-commerce) |
| `A--Kuna-2025` | AI-Driven Behavioral Risk Profiling in Digital Lending Platforms: A Critical Review | 2025 | ml_algorithms 0.413 | supporting / 1.75 | Review (lending) |
| `A--JapinyeAdedugbe-2025` | Explainable AI for Credit Scoring with SHAP-Calibrated Ensembles: A Multinational Assessment | 2025 | ml_algorithms 0.412 | supporting / 2.25 | **Maintain** (credit + XAI) |
| `A--Liu-2025` | Deep Feature Extraction Method for Automatic Classification and Processing of Accounting Information | 2025 | expense_categorization 0.407 | supporting / 2.25 | Review (accounting entries) |
| `A--Lockwood-2026` | Machine Learning Approaches for Credit Default Prediction in Emerging Economies | 2026 | ml_algorithms 0.407 | supporting / 1.75 | **Maintain** (credit; manifest title was wrong) |
| `A--MartinJ-2025` | A Novel Financial Performance Metric to Minimize Misclassification Cost in Credit Assessment | 2025 | ml_algorithms 0.407 | supporting / 2.25 | Review (metric) |
| `A--LiY-2025` | Machine Learning-Based Identification of Anomalous Trading Behavior Patterns | 2025 | anomaly_detection 0.403 | supporting / 2.25 | Review (trading) |
| `A--LiLi-2025` | Exploring Factors Involved in Loan Approval Decision: Deep Insights from Borrowing Records | 2025 | ml_algorithms 0.402 | supporting / 2.25 | Review (loan factors) |
| `A--LeibikerTalmon-2023` | A Recommendation System for Participatory Budgeting | 2023 | budget_recommendation 0.395 | supporting / 2.00 | Review (civic budgeting) |
| `A--John-2025` | Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explainability Strategies | 2025 | ml_algorithms 0.393 | supporting / 2.25 | **Maintain** (credit + XAI + drift) |
| `A--LiJ-2026` | Research on Personalized Asset Allocation Using AI Agents in Robo-Advisory | 2026 | ml_algorithms 0.393 | supporting / 2.00 | Review (investment) |
| `L--MarianoMonreal-2025` | Predict, Optimize, Deliver: Demand Forecasting and Resource Optimization for a Market Research Firm | 2025 | forecasting 0.384 | supporting / 2.00 | Review (L--, off-finance demand forecast) |
| `__Hovakimyan & Bravo__` | Evolving Strategies in Machine Learning: A Systematic Review of Concept Drift Handling | — | ml_algorithms 0.380 | supporting / 2.25 | **Skip / carry-over** (no PDF) |
| `A--IslamM-2025` | AI-Driven Fraud Detection and Prevention Using Human Behavior Analysis | 2025 | anomaly_detection 0.380 | supporting / 2.00 | Review (fraud) |
| `A--Ibrahim-2025` | An Equity-Aware Recommender System for University Admissions | 2025 | budget_recommendation 0.379 | supporting / 4.25 | Cull (admissions, off-scope) |
| `A--KrichenMihoub-2025` | Long Short-Term Memory Networks: A Comprehensive Survey of Architectures and Applications | 2025 | forecasting 0.376 | supporting / 2.00 | Review (generic LSTM survey) |
| `A--Mehta-2025` | Clustering and Similarity Learning in Financial Markets: A Tutorial for the Practitioners | 2025 | anomaly_detection 0.372 | supporting / 2.25 | Review (markets) |
| `A--LeeJ-2023` | Comparing Deep Learning and Classical Regression Approaches for Predicting Healthcare Expenditure and Spending: A Systematic Review | 2023 | ml_algorithms 0.368 | supporting / 2.25 | Cull (healthcare) |
| `A--KimK-2025` | RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification | 2025 | expense_categorization 0.366 | supporting / 2.25 | Review (customer segments) |
| `A--LiGautam-2025` | Segmented Confidence Sequences and Multi-Scale Adaptive Confidence for Anomaly Detection | 2025 | anomaly_detection 0.357 | supporting / 2.00 | Review (methodology) |
| `A--Jouini-2026` | Drift-Driven Collaborative Learning for Non-Stationary Time Series: A COVID-Data Study | 2026 | ml_algorithms 0.354 | supporting / 2.25 | Cull (COVID, off-scope) |
| `A--KhanSadaoui-2026` | Learner-Based Concept Drift Detection: Analysis and Evaluation | 2026 | ml_algorithms 0.350 | supporting / 2.00 | Review (methodology) |
| `A--Jiang-2026` | A Dynamic Framework for Causal User Profiling and Treatment Segmentation | 2026 | ml_algorithms 0.348 | supporting / 2.25 | Review (methodology) |
| `A--Jafarigol-2025` | A Review of Machine Learning Techniques in Imbalanced Data and Future Research Directions | 2025 | ml_algorithms 0.346 | supporting / 2.25 | Review (methodology) |
| `A--Mienye-2024` | Recurrent Neural Networks: A Comprehensive Review of Architectures and Applications | 2024 | forecasting 0.336 | supporting / 2.00 | Review (generic RNN survey) |
| `A--KavyaSumathi-2024` | Staying Ahead of Phishers: A Review of Recent Advances in Phishing Detection | 2024 | ml_algorithms 0.324 | supporting / 2.00 | Cull (security) |
| `A--LiC-2026` | BIRCH-AE: A Hierarchical Ensemble Framework for Scalable E-Commerce User Behavior Analysis | 2026 | expense_categorization 0.320 | supporting / 2.25 | Review (e-commerce) |
| `A--Kaya-2026` | Explainable Artificial Intelligence (XAI): Concepts, Applications, Challenges, and Future Perspectives | 2026 | ml_algorithms 0.316 | supporting / 2.00 | Review (generic XAI survey) |
| `A--LiEtAl-2025` | LLM-Based Personalized Portfolio Recommender: Integrating Large Language Models and Reinforcement Learning | 2025 | ml_algorithms 0.313 | supporting / 2.00 | Review (investment) |
| `A--Lombardo-2026` | Cost-Sensitive Evaluation for Binary Classifiers | 2026 | ml_algorithms 0.309 | supporting / 2.25 | Review (metrics) |
| `A--LingWeiling-2025` | Enhancing Segmentation: A Comparative Study of Clustering Methods | 2025 | expense_categorization 0.304 | supporting / 2.25 | Review (methodology) |
| `A--LienRajasekharan-2024` | Automatic Standard Building Category Classification from Smart Meter Data: A Supervised Learning Approach | 2024 | expense_categorization 0.303 | supporting / 2.00 | Cull (buildings/energy) |

### Cull tier (< 0.30) — 1 paper

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `A--Kozakova-2025` | Smart Finance Management System Based on Artificial Intelligence Technology | 2025 | ml_algorithms 0.277 | cull / 2.00 | Cull (0.277) |

### No-sourcing candidates (PDF unavailable)

| Index key | Status |
| :--- | :--- |
| `Huang A. et al` | **Skip / carry-over flag** — no PDF found in batch-3 dir, bucket, or other batches (crucial, 0.481, anomaly_detection, quality 3.25) |
| `Hovakimyan & Bravo` | **Skip / carry-over flag** — no PDF found in batch-3 dir, bucket, or other batches (supporting, 0.380, ml_algorithms, quality 2.25) |

---

## Algorithm/Model-Designated Papers (Budi Candidates) — detail

### Crucial tier (top priority for intake)

1. **Khan et al. (2025)** — *Model-Agnostic Explainable Artificial Intelligence Methods in Finance: A Systematic Review* (Artificial Intelligence Review 58:232)
   - **Best module:** ml_algorithms 0.485 (crucial) — top-scoring non-fraud paper in batch-3; quality 2.00.
   - **Why it fits:** systematic review of model-agnostic XAI methods across the whole
     finance stack (credit, fraud, forecasting) — supports the explainability layer of
     BUDI (§3.4) and pairs with batch-2's D'Souza PFM-ML review.
   - **Source:** `Khan et al.pdf`.

2. **Lu, Yifei et al. (2025)** — *A Constrained, Data-Driven Budgeting Framework Integrating Macro Demand Forecasting* (J. Tech. Informatics 4(3), Dec 2025)
   - **Best module:** budget_recommendation 0.474 (crucial); quality 2.25.
   - **Why it fits:** a budgeting framework that constrains forecasting outputs into an
     actionable allocation — the clearest budget-module model paper in batch-3 (§3.
     budget_recommendation).
   - **Source:** `Lu, Yifei et al.pdf`.

3. **Jayaprakashnarayan et al. (2026)** — *AI-Enabled NLP Framework for Automated Expense Management and Financial Transactions* (IJEETR)
   - **Best module:** expense_categorization 0.470 (crucial); quality 3.25.
   - **Why it fits:** NLP-driven automation of expense capture/categorization — direct
     expense-categorization evidence (§2.4.4.1 / §3); highest quality score in the crucial tier.
   - **Source:** `Jayaprakashnarayan et al.pdf`.

4. **Kara & Senguler (2025)** — *A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review* (Public Budgeting & Finance)
   - **Best module:** forecasting 0.466 (crucial); quality 2.00.
   - **Why it fits:** SLR comparing budget-forecasting methods — directly supports the
     forecasting/budget modules for income prediction (§3.3).
   - **Source:** `Kara & Senguler.pdf`.

5. **Kowsar M. et al. (2023)** — *Credit Decision Automation in Commercial Banks: A Review of AI and Predictive Analytics in Loan Assessment* (Am. J. Interdisciplinary Studies 4(4))
   - **Best module:** ml_algorithms 0.462 (crucial); quality 2.00.
   - **Why it fits:** credit/loan-assessment automation review — debt-management evidence
     (§2.4.4.2). **This is the recovered PDF for batch-4's no-PDF `Mohiuddin et al`
     carry-over (same title, 0.462).**
   - **Source:** `Kowsar M. et al-2023.pdf`.

### Supporting tier (promising, needs RRL verdict)

6. **Laspinas & Murcia (2024)** — *Machine Learning Approaches in Classifying Income Levels* (TWIST)
   - **Best module:** ml_algorithms 0.440 (supporting); quality 2.00.
   - **Why it fits:** income-level classification from **University of Southeastern
     Philippines – Mintal + University of Mindanao** — a local income-classifier paper
     (`L--`) that mirrors batch-1's `Apus et al` for budget/income profiling (§3.2).
7. **Malave et al. (2026)** — *Transforming Financial Documents into Credit Decisions Using Explainable AI*
   - **Best module:** ml_algorithms 0.439 (supporting); quality 2.25.
   - **Why it fits:** document OCR → explainable credit decision — alternative-data credit
     pipeline (§3.2 / §3.4), pairs with batch-4's `Ng et al` AI-BAAM.
8. **Mienye et al. (2026)** — *Deep Learning for Credit Risk Prediction: A Survey of Major Modeling Techniques* (Information 17:395)
   - **Best module:** ml_algorithms 0.439 (supporting); quality 2.00.
   - **Why it fits:** credit-risk DL survey (§2.4.4.2), complements the older `Mienye-2024`
     RNN survey still in the supporting tier.
9. **Japinye & Adedugbe (2025)** — *Explainable AI for Credit Scoring with SHAP-Calibrated Ensembles: A Multinational Assessment*
   - **Best module:** ml_algorithms 0.412 (supporting); quality 2.25.
   - **Why it fits:** SHAP-calibrated ensemble credit scoring — explainability + debt model
     in one paper (§3.4 + §2.4.4.2).
10. **Lockwood et al. (2026)** — *Machine Learning Approaches for Credit Default Prediction in Emerging Economies*
    - **Best module:** ml_algorithms 0.407 (supporting); quality 1.75.
    - **Why it fits:** credit-default prediction explicitly for **emerging economies** —
    directly relevant to Filipino debt context (§2.4.4.2). **Stored manifest title was
    the wrong paper** ("Designing for Financial Literacy…"); verified title above.
    - **Source:** `Lockwood et al.pdf`.
11. **John (2025)** — *Fair and Explainable Credit-Scoring under Concept Drift: Adaptive Explainability Strategies*
    - **Best module:** ml_algorithms 0.393 (supporting); quality 2.25.
    - **Why it fits:** fairness + explainability + concept drift in credit scoring — a rare
      three-way fit for BUDI's accuracy/explainability requirements (§3.4 + §2.4.4.2).

### Review / borderline

Fraud/anomaly family (Kashif & Naseer, Luong & Xie, Li & Chen, Kalideen, Karthikeyan,
Islam A., Islam M.) — shared-module evidence for the anomaly-detection sibling, but they
target bank/card fraud rather than personal-overspending detection. Corporate/business
distress (Judijanto) — ML early-warning for firms, tangential to personal debt.
Forecasting methodology reviews (Kontopoulou, Kim J., Krichen & Mihoub, Mienye-2024) —
useful method comparisons but application-agnostic. Concept-drift/imbalance methodology
(Khan & Sadaoui, Jafarigol, Jiang, Li & Gautam, Lombardo, Ling & Weiling) — ML methodology
only. Churn/CRM (Mamun, Imani), e-commerce (Lou, Li C., Kim K.), trading (Li Y., Mehta),
investment/robo (Li J., Li & Li, Li et al), civic budgeting (Leibiker & Talmon), lending
(Kuna), accounting entries (Liu), metrics (Martin J.) — partial fit for §3/§2.4 context
only. `L--MarianoMonreal-2025` is a **local Mapua paper** (stored as international) but its
demand-forecasting application is a market-research use case, not personal finance — off-
scope for savings/debt; noted so it is not lost from the local-paper inventory.

### Cull / defer

Krstev (monthly electricity consumption), Ma P. (family-level *electricity* load
forecasting), Ibrahim (university-admissions recommender), Lee J. (healthcare expenditure —
also named to "(2023)" in citation line), Jouini (COVID time series), Kavya & Sumathi
(phishing/security), Lien & Rajasekharan (building-category classification from smart
meters), Kozakova & Endeva (generic "smart finance" system, 0.277) — off-scope for
personal savings/debt finance despite algorithm keywords.

---

## Topical Outline Mapping (§3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Khan et al 2025 | §3.4 explainability | Model-agnostic XAI review in finance |
| Lu, Yifei et al 2025 | §2.4.4.2 / §3, budget | Constrained data-driven budgeting framework |
| Jayaprakashnarayan et al 2026 | §2.4.4.1 / §3, expense | NLP automated expense management |
| Kara & Senguler 2025 | §3.3 forecasting / budget | Budget-forecasting SLR |
| Kowsar M. et al 2023 | §2.4.4.2 / §3, credit | Credit-decision automation review (= `Mohiuddin`) |
| Laspinas & Murcia 2024 | §3.2 classification (L--) | ML income-level classification, PH |
| Malave et al 2026 | §3.2 / §3.4 credit | Document OCR + XAI credit decisions |
| Mienye et al 2026 | §2.4.4.2 / §3, credit | Deep-learning credit-risk survey |
| Japinye & Adedugbe 2025 | §3.4 + §2.4.4.2 | SHAP-calibrated credit scoring |
| Lockwood et al 2026 | §2.4.4.2 / §3, credit | Credit-default prediction, emerging economies |
| John 2025 | §3.4 + §2.4.4.2 | Fair XAI credit scoring under concept drift |

The remaining papers map mostly to fraud/anomaly (shared anomaly sibling), churn/CRM,
e-commerce, trading/investment, or off-scope domains (electricity, healthcare, COVID,
university admissions, security) outside the personal savings/debt algorithm focus.

---

## Recommended Next Steps

1. **Confirm verdicts** for the "Review" papers — researcher decision, especially the
   fraud/anomaly family, the forecasting-methodology surveys (Kontopoulou, Kim J.,
   Krichen & Mihoub, Mienye-2024), and the two local `L--` papers (Laspinas & Murcia,
   Mariano & Monreal).
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   proposed stems → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Survive-note carry-overs:** `Huang A. et al` (crucial, 0.481, anomaly, q3.25) and
   `Hovakimyan & Bravo` (supporting, 0.380, ml, q2.25) have no recoverable PDF in this
   workspace — flag for the researcher to re-fetch from the Drive source before inclusion.
4. **Re-resolve batch-4 carry-over** `Mohiuddin et al` via `Kowsar M. et al-2023` (same
   paper — now has a PDF). `Mohammad et al` (batch-4) remains no-PDF.
5. **Re-score** once the intake lands — batch-3 old-run best_module/best_score values were
   computed from the deprecated 518-paper corpus and will be replaced by the batch-7 run.

---

## Screening Complete (all batches)

| Batch | Candidates | Maintain | Review | Cull | No-PDF carry-over | Doc |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| batch-6 | 14 | — | — | — | — | `batch-6-algorithm-screening.md` |
| batch-5 | 54 | — | — | — | Samuel, Sanchez | `batch-5-algorithm-screening.md` |
| batch-4 | 39 | 11 | — | 2 | Mohammad, Mohiuddin | `batch-4-algorithm-screening.md` |
| batch-1 | 40 | — | — | 3 | Abd-Ellatif, Abdullahi | `batch-1-algorithm-screening.md` |
| batch-2 | 42 | — | — | 3 | Chen & Lin, Chen J., Chen & Tan, Chen V. | `batch-2-algorithm-screening.md` |
| batch-3 | 55 | 11 | — | 8 | Huang A., Hovakimyan & Bravo | **this doc** |