# Batch-5 Algorithm/Model Screening (Budi Intake)

Screening of `Odin-Paper/archived-literature/papers/batch-5/` for papers discussing
**models and algorithms used to improve a user's personal savings and debt** in
intelligent personalized finance management systems.

- **Date:** 2026.09.05
- **Source:** `Odin-Paper/archived-literature/papers/batch-5/` (96 PDFs; 54 algorithm-designated candidates)
- **Primary filter:** `Odin-Literature/scores/index.json` (old 518-paper run) + `scores/report.md`
- **Reference outline:** `Odin-Paper/google-drive/topical-outline/topical-outline.md` (System Models and Algorithms, §3)
- **Status:** screening only — no PDFs copied, converted, summarized, or scored yet

---

## Method

1. Enumerate the 96 PDFs in `batch-5/` (keys S–Y).
2. Pull per-paper best module, tier, and quality from `scores/index.json`
   (old-run scores; batch-5 titles/designations were missing there, so titles were
   recovered from PDF metadata / first-page text via pypdf).
3. Keep the **algorithm/model-designated** subset: best module in
   `ml_algorithms`, `forecasting`, `anomaly_detection`, `budget_recommendation`,
   or `expense_categorization` → **54 candidates** (21 Maintain/Review-worthy,
   remainder cull-tier).
4. Verdict per paper: **Maintain** (recommend intake), **Review** (borderline /
   partial fit), or **Cull / Defer** (low relevance or off-scope).

Tier thresholds: crucial >= 0.45, supporting >= 0.30, cull < 0.30 (per `config/modules.yaml`).

**Scope:** algorithm/model papers only, per the requested flow (batch-6 was done first;
batch-5 is the previous alphabetical batch).

---

## Batch-5 Triage (algorithm-designated candidates)

### Crucial tier (>= 0.45) — 15 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `AI--Vinitha-2026` | AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering | 2026 | forecasting 0.452 | crucial / 1.25 | **Maintain** |
| `AI--SinghU-2025` | A Predictive Framework for Annual Financial Planning using Deep Learning Models | 2025 | forecasting 0.575 | crucial / 1.00 | **Maintain** |
| `A--ThakurJadhav-2025` | Expense Tracker Management System using Machine Learning | 2025 | expense_categorization 0.503 | crucial / 1.25 | **Maintain** |
| `AI--Xiao-2025` | Example-Dependent Cost-Sensitive Learning Based Selective Deep Ensemble for Customer Credit Scoring | 2025 | ml_algorithms 0.463 | crucial / 1.50 | **Maintain** |
| `A--Thundiyil-2024` | Transformer Architectures in Time Series Analysis: A Review | 2024 | forecasting 0.454 | crucial / 1.50 | **Maintain** (methodology) |
| `AI--Sireesha-2026` | AI-Based Personal Finance Manager | 2026 | ml_algorithms 0.543 | crucial / 1.25 | Maintain (PFM w/ AI) |
| `A--Sonkavde-2023` | Forecasting Stock Market Prices using Machine Learning and Deep Learning Models: A Systematic Review | 2023 | ml_algorithms 0.483 | crucial / 1.50 | Maintain (review) |
| `AI--Vijayanand-2025` | Anomaly Detection in Mobile Money Transactions | 2025 | ml_algorithms 0.470 | crucial / 1.50 | Maintain (anomaly) |
| `AI--Veldurthi-2025` | The Role of AI and Machine Learning in Fraud Detection for Financial Services | 2025 | anomaly_detection 0.481 | crucial / 1.50 | Review (fraud survey) |
| `L--Santiago-2025` | Budget and Financial Management Information System for Public Elementary Schools | 2025 | budget_recommendation 0.480 | crucial / 1.25 | Review (PH; linear-regression, school budget) |
| `AI--Shaha-2025` | Enhancing Online Fraud Detection: Leveraging Machine Learning and Behavioral Indicators | 2025 | ml_algorithms 0.475 | crucial / 1.25 | Review (fraud) |
| `AI--Siswara-2024` | Modeling with RNN, Random Forest, and XGBoost for Imbalanced Data: Early Crash Detection in ASEAN-5 Stock Markets | 2024 | ml_algorithms 0.467 | crucial / 1.25 | Review (stock market) |
| `AI--Sankaewtong-2025` | SoK: Advances in Anomaly Detection Techniques for Cryptoasset Transactions | 2025 | anomaly_detection 0.454 | crucial / 1.50 | Review (crypto, tangential) |
| `AI--Scrivano-2025b` | Fraud Detection Pipeline using Machine Learning: Methods, Applications, and Future Directions | 2025 | ml_algorithms 0.453 | crucial / 1.50 | Review (fraud pipeline) |
| `AI--Sappa-2024` | AI Based Portfolio Optimization and Customer Risk Profiling in Fintech Platforms | 2024 | ml_algorithms 0.451 | crucial / 1.50 | Review (portfolio) |

### Supporting tier (>= 0.30) — 31 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `AI--Sarkar-2026` | A Systematic Review of AI-Driven Credit Risk Assessment Models in Commercial Banking | 2026 | ml_algorithms 0.446 | supporting / 1.50 | **Maintain** (credit/debt) |
| `AI--YangT-2024` | Enhancing Financial Services through Big Data and AI-Driven Customer Insights and Risk Analysis | 2024 | ml_algorithms 0.446 | supporting / 1.25 | Maintain |
| `AI--Song-2025` | Deep Learning-Based Time Series Forecasting | 2025 | forecasting 0.436 | supporting / 1.50 | Maintain (forecasting survey) |
| `A--SanhoshSingh-2025` | Digital Persona Modeling for Context-Aware Financial Decisioning | 2025 | ml_algorithms 0.423 | supporting / 1.25 | Maintain |
| `AI--Sujon-2025` | Accuracy, Precision, Recall, F1-Score, or MCC? Empirical Evidence from Statistics, ML, and XAI for Evaluating Business Predictive Models | 2025 | ml_algorithms 0.416 | supporting / 1.50 | Maintain (metrics) |
| `A--Scrivano-2025a` | Time-Series Forecasting using Deep Learning and Data Mining Models | 2025 | forecasting 0.430 | supporting / 1.25 | Maintain |
| `AI--Yang-2024` | Study of an Adaptive Financial Recommendation Algorithm using Big Data Analysis and User Interest Pattern with Fuzzy K-Means | 2024 | ml_algorithms 0.404 | supporting / 1.25 | Maintain (recommendation) |
| `AI--Schwartz-2025` | Enhancing ML Interpretability for Credit Scoring | 2025 | ml_algorithms 0.413 | supporting / 1.50 | Maintain (credit/XAI) |
| `AI--WangF-2025` | A Survey of Deep Anomaly Detection in Multivariate Time Series: Taxonomy, Applications, and Directions | 2025 | anomaly_detection 0.411 | supporting / 1.50 | Review |
| `AI--Yunita-2025` | Performance Analysis of Neural Network Architectures for Time Series Forecasting: A Comparative Study of RNN, LSTM, GRU, and Hybrid Models | 2025 | forecasting 0.446 | supporting / 1.50 | Maintain |
| `AI--Tjostheim-2025` | Selected Topics in Time Series Forecasting: Statistical Models vs. Machine Learning | 2025 | forecasting 0.435 | supporting / 1.50 | Maintain (review) |
| `AI--Shuryhin-2024` | Recommendation System for Financial Decision-Making using Artificial Intelligence | 2024 | ml_algorithms 0.430 | supporting / 1.25 | Maintain |
| `AI--Yachamaneni-2025` | Credit Card Customer Profiling using Self-Supervised Representation Learning on Multi-Source Financial Data | 2025 | ml_algorithms 0.423 | supporting / 1.25 | Maintain |
| `AI--Vyas-2025` | The Role of Artificial Intelligence in Financial Risk Management, Forecasting, and Global Implementation | 2025 | ml_algorithms 0.421 | supporting / 1.50 | Review |
| `AI--Sandstrom-2024` | AI-Driven Risk-Adaptive Cloud Intelligence for Large-Scale Fraud Detection | 2024 | anomaly_detection 0.417 | supporting / 1.25 | Review (fraud) |
| `AI--Serdan-2025` | Cost-Sensitive Neural Architectures for Handling Class Imbalance in High-Stakes Fraud Detection | 2025 | ml_algorithms 0.415 | supporting / 1.25 | Review (fraud) |
| `I--YildizDemir-2025` | The Impact of Artificial Intelligence on Financial Inclusion: Data-Driven Approaches for Expanding Access to Banking in Underserved Regions | 2025 | ml_algorithms 0.394 | supporting / 1.50 | Review |
| `AI--Yaramolu-2025` | AI-Powered Portfolio Management: Transforming Wealth Management through Intelligent Automation | 2025 | ml_algorithms 0.391 | supporting / 1.25 | Review (portfolio) |
| `AI--Verma-2024` | Counterfactual Explanations and Algorithmic Recourses for Machine Learning: A Review | 2024 | ml_algorithms 0.388 | supporting / 1.50 | Review (XAI) |
| `L--Salvador-2024` | Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines | 2024 | ml_algorithms 0.386 | supporting / 1.25 | **Maintain** (local PH boosting) |
| `AI--Simeonov-2025` | Analysing Community-Level Spending Behaviour Contributing to High Carbon Emissions using Stochastic Block Models | 2025 | expense_categorization 0.377 | supporting / 1.50 | Review (spending/climate) |
| `AI--Stylianou-2025` | Big Data and Consumer Behavior: Macroeconomic Perspective through Supermarket Analytics | 2025 | forecasting 0.373 | supporting / 1.50 | Review |
| `AI--YangR-2025` | Recent Advances in Artificial Intelligence for Management and Financial Technology | 2025 | ml_algorithms 0.365 | supporting / 1.25 | Review |
| `AI--Siddiqui-2025` | STEMS: A Systematic Review of Data-Driven Insights in Financial and Strategic Planning | 2025 | ml_algorithms 0.361 | supporting / 1.50 | Review |
| `AI--Xiang-2023` | Concept Drift Adaptation Methods under the Deep Learning Framework: A Literature Review | 2023 | ml_algorithms 0.361 | supporting / 1.50 | Review |
| `AI--YangZhang-2026` | Offline Conservative RL for Transaction Authorization: Smartly Balancing Fraud Risk and Customer Friction | 2026 | ml_algorithms 0.343 | supporting / 1.25 | Review |
| `AI--Weng-2025` | Deep Embedding Clustering with Adaptive Feature Selection for Banking Customer Segmentation | 2025 | expense_categorization 0.325 | supporting / 1.50 | Review |
| `AI--Sulaiman-2024` | Credit Card Fraud Detection Challenges and Solutions: A Review | 2024 | ml_algorithms 0.310 | supporting / 1.50 | Review (fraud) |
| `AI--Williams-2023` | Anomaly Detection in Multi-Seasonal Time Series Data | 2023 | anomaly_detection 0.301 | supporting / 1.25 | Review |
| `AI--Ullah-2024` | Short-Term Load Forecasting: A Comprehensive Review and Simulation Study with CNN-LSTM Hybrids | 2024 | forecasting 0.437 | supporting / 1.50 | Cull (electricity load) |
| `AI--Silvestre-2026` | Predicting Hotel Booking Cancellations under Disruption | 2026 | ml_algorithms 0.328 | supporting / 1.50 | Cull (hotel/tourism) |

### Cull tier (< 0.30) — 8 papers

| Proposed stem | Full title | Year | Best module / score | Tier / quality | Verdict |
| :--- | :--- | :---: | :--- | :---: | :---: |
| `AI--Salminen-2023` | How Can Algorithms Help in Segmenting Users and Customers? A Systematic Review and Research Agenda for Algorithmic Customer Segmentation | 2023 | ml_algorithms 0.294 | cull / 1.50 | Cull (carry-over in bucket) |
| `AI--Wani-2024` | Comprehensive Analysis of Clustering Algorithms: Exploring Limitations and Innovative Solutions | 2024 | anomaly_detection 0.291 | cull / 1.50 | Cull |
| `AI--WangY-2023` | New Developments in Sequential Change Point Detection for Time Series and Spatio-Temporal Analysis | 2023 | anomaly_detection 0.277 | cull / 1.50 | Cull |
| `AI--YuanHernandez-2023` | User Cold Start Problem in Recommendation Systems: A Systematic Review | 2023 | expense_categorization 0.277 | cull / 1.50 | Cull |
| `AI--Singh-2023` | Directive Explanations for Actionable Explainability in Machine Learning | 2023 | ml_algorithms 0.264 | cull / 1.50 | Cull |
| `AI--YilmazDemirhan-2023` | Weighted Kappa Measures for Ordinal Multi-Class Classification Performance | 2023 | expense_categorization 0.253 | cull / 1.50 | Cull |
| `AI--Vasileiou` | *(agent scheduling, explainability)* | — | budget_recommendation 0.180 | cull / 1.25 | Cull |

### No-sourcing candidates (PDF unavailable)

| Index key | Status |
| :--- | :--- |
| `Samuel` | **Skip / carry-over flag** — no PDF found in batch-5 dir, bucket, or other batches |
| `Sanchez` | **Skip / carry-over flag** — no PDF found in batch-5 dir, bucket, or other batches |

---

## Algorithm/Model-Designated Papers (Budi Candidates) — detail

### Crucial tier (top priority for intake)

1. **Singh U. et al. (2025)** — *A Predictive Framework for Annual Financial Planning using Deep Learning Models*
   - **Best module:** forecasting 0.575 (crucial) — top score in the whole batch-5 set.
   - **Why it fits:** deep-learning framework returning annual financial/spending forecasts — a
     direct forecasting-model paper for personal financial planning (§3.2/§3.3). Unknown (US-institution)
     origin, journal-only, quality 1.00 (no full score in index).
   - **Source:** `Singh U. et al.pdf`.

2. **Sireesha et al. (2026)** — *AI-Based Personal Finance Manager*
   - **Best module:** ml_algorithms 0.543 (crucial).
   - **Why it fits:** an AI personal-finance-manager system — directly a PFM with ML features (§2.4.1).
   - **Source:** `Sireesha et al.pdf`.

3. **Thakur & Jadhav (2025)** — *Expense Tracker Management System using Machine Learning*
   - **Best module:** expense_categorization 0.503 (crucial).
   - **Why it fits:** expense tracker + ML (compares MLP, XGBoost, SVM, bagging/boosting ensembles;
     XGBoost best). Directly supports expense categorization module and §2.4/§3.
   - **Source:** `Thakur & Jadhav.pdf`.

4. **Xiao et al. (2025)** — *Example-Dependent Cost-Sensitive Learning Based Selective Deep Ensemble for Customer Credit Scoring*
   - **Best module:** ml_algorithms 0.463 (crucial); quality 1.50 (Scientific Reports).
   - **Why it fits:** cost-sensitive deep ensemble for credit scoring — a debt/credit model paper
     (§2.4.4 / debt management). Methodologically strong.
   - **Source:** `Xiao et al.pdf`.

5. **Thundiyil et al. (2024)** — *Transformer Architectures in Time Series Analysis: A Review*
   - **Best module:** forecasting 0.454 (crucial); quality 1.50.
   - **Why it fits:** transformer-models review — modern forecasting backbone for spending forecasts (§3.2).
   - **Source:** `Thundiyil et al.pdf`.

6. **Sonkavde et al. (2023)** — *Forecasting Stock Market Prices using Machine Learning and Deep Learning Models: A Systematic Review*
   - **Best module:** ml_algorithms 0.483 (crucial); quality 1.50.
   - **Why it fits:** ML/DL forecasting survey; useful as §3 method foundation (though stock market, not
     personal spending). Review-type.
   - **Source:** `Sonkavde et al.pdf`.

7. **Vijayanand & Smrithy (2025)** — *Anomaly Detection in Mobile Money Transactions*
   - **Best module:** ml_algorithms 0.470 (crucial); quality 1.50.
   - **Why it fits:** anomaly detection on financial transactions — §3 anomaly-detection module,
     close to the fraud/overspending sibling.
   - **Source:** `Vijayanand & Smrithy.pdf`.

### Supporting tier (promising, needs RRL verdict)

8. **Sarkar (2026)** — *A Systematic Review of AI-Driven Credit Risk Assessment Models in Commercial Banking*
   - **Best module:** ml_algorithms 0.446 (supporting); quality 1.50.
   - **Why it fits:** credit-risk assessment review — debt-management angle (§2.4.4 / debt_management).
   - **Source:** `Sarkar.pdf`.

9. **Song et al. (2025)** — *Deep Learning-Based Time Series Forecasting* (Artificial Intelligence Review)
   - **Best module:** forecasting 0.436 (supporting); quality 1.50.
   - **Why it fits:** comprehensive DL time-series forecasting review — §3 forecasting foundation.
   - **Source:** `Song et al.pdf`.

10. **Salvador (2024)** — *Use of Boosting Algorithms in Household-Level Poverty Measurement* (Philippines)
    - **Best module:** ml_algorithms 0.386 (supporting); quality 1.25.
    - **Why it fits:** **local Philippine** boosting/classification of household wealth quintiles —
    relevant to financial classification §2.4.4 / `L--` designation. CatBoost-based. Already staged in `literature/bucket/`.
    - **Source:** `literature/bucket/Salvador, 2024.pdf` (carry-over).

11. **Sujon et al. (2025)** — *Accuracy, Precision, Recall, F1, or MCC? ... for Evaluating Business Predictive Models*
    - **Best module:** ml_algorithms 0.416 (supporting); quality 1.50 (Journal of Big Data).
    - **Why it fits:** metric selection under class imbalance for financial model evaluation — supports §3.4 evaluation.
    - **Source:** `Sujon et al.pdf`.

12. **Yang (2024)** — *Adaptive Financial Recommendation Algorithm ... Fuzzy K-Means*
    - **Best module:** ml_algorithms 0.404 (supporting).
    - **Why it fits:** financial recommendation algorithm (fuzzy K-means clustering) — recommendation feature (§2.4.4).
    - **Source:** `Yang.pdf`.

13. **Schwartz et al. (2025)** — *Enhancing ML Interpretability for Credit Scoring*
    - **Best module:** ml_algorithms 0.413 (supporting); quality 1.50 (arXiv preprint).
    - **Why it fits:** interpretability/XAI for credit scoring — explainability + debt angle (§3.4).
    - **Source:** `Schwartz et al.pdf`.

14. **Yunita et al. (2025)** — *Performance Analysis of Neural Network Architectures for Time Series
    Forecasting: RNN, LSTM, GRU, and Hybrid Models* (MethodsX)
    - **Best module:** forecasting 0.446 (supporting); quality 1.50.
    - **Why it fits:** head-to-head RNN/LSTM/GRU forecasting comparison — direct §3.2 forecasting evidence.
    - **Source:** `Yunita et al.pdf`.

15. **Tjostheim (2025)** — *Selected Topics in Time Series Forecasting: Statistical Models vs. Machine
    Learning* (review)
    - **Best module:** forecasting 0.435 (supporting); quality 1.50.
    - **Why it fits:** statistical-vs-ML forecasting review — model-selection guidance for §3.2.
    - **Source:** `Tjostheim.pdf`.

16. **Shuryhin & Zinovatna (2024)** — *Recommendation System for Financial Decision-Making using AI*
    - **Best module:** ml_algorithms 0.430 (supporting); quality 1.25.
    - **Why it fits:** personal financial-advice recommendation using Isolation Forest + ARIMA/LSTM —
      a strong recommendation/forecasting hybrid for §2.4.4.2.
    - **Source:** `Shuryhin & Zinovatna.pdf`.

17. **Yachamaneni et al. (2025)** — *Credit Card Customer Profiling using Self-Supervised Representation
    Learning on Multi-Source Financial Data*
    - **Best module:** ml_algorithms 0.423 (supporting); quality 1.25.
    - **Why it fits:** self-supervised profiling of financial data — feature-learning approach relevant
      to spending profiling/segmentation (§3.2).
    - **Source:** `Yachamaneni et al.pdf`.

18. **Yang T. et al. (2024)** — *Enhancing Financial Services through Big Data and AI-Driven Customer
    Insights and Risk Analysis*
    - **Best module:** ml_algorithms 0.446 (supporting); quality 1.25.
    - **Why it fits:** customer insights + risk analysis via AI on financial data — broad §2.4/§3 context.
    - **Source:** `Yang T. et al.pdf`.

19. **Wang F. et al. (2025)** — *A Survey of Deep Anomaly Detection in Multivariate Time Series:
    Taxonomy, Applications, and Directions*
    - **Best module:** anomaly_detection 0.411 (supporting); quality 1.50.
    - **Why it fits:** deep anomaly-detection taxonomy — methodology backbone for the anomaly module (§3.2/§3.3),
      generally applicable to financial time series.
    - **Source:** `Wang F. et al.pdf`.

### Review / borderline

Fraud-focused surveys (Veldurthi, Shaha, Sandstrom, Serdan, Sulaiman, Scrivano-2025b, Wang F.) —
relevant to the anomaly-detection sibling as a shared module, but they target bank/card fraud rather
than personal-overspending detection. Portfolio/risk papers (Sappa, Yaramolu, Yang R., YangZhang) —
investment-oriented, tangential to savings/debt. Stock-market (Siswara) and hotel/tourism (Silvestre)
papers are off the personal-finance scope and are culled. Others (Ullah load forecasting) are culled
as electric-power, not personal-finance.

### Cull / defer

Ullah (CNN-LSTM electricity load), Silvestre (hotel cancellations), plus the < 0.30 cull-tier set —
off-scope for personal savings/debt finance despite algorithm keywords.

---

## Topical Outline Mapping ($3 System Models and Algorithms)

| Paper | Topical outline node | Notes |
| :--- | :--- | :--- |
| Singh U. et al 2025 | §3.3 forecasting | Annual deep-learning financial planning |
| Sireesha et al 2026 | §2.4.1 / §3 | AI PFM system |
| Thakur & Jadhav 2025 | §2.4.4.1 / §3 classification, expense | XGBoost expense tracker |
| Xiao et al 2025 | §2.4.4.2 / §3, credit | Cost-sensitive deep ensemble credit scoring |
| Thundiyil et al 2024 | §3.2 forecasting | Transformer time-series review |
| Sonkavde et al 2023 | §3.2/§3.3, forecasting | ML/DL forecasting survey |
| Vijayanand & Smrithy 2025 | §3.3 anomaly | Mobile-money anomaly detection |
| Sarkar 2026 | §2.4.4.2 / §3, credit risk | Credit-risk review (debt) |
| Song et al 2025 | §3.2 forecasting | DL time-series forecasting review |
| Salvador 2024 | §2.4.4.1 / §3 classification (L--) | PH boosting, household wealth classification |
| Santiago 2025 | §2.4.4.2 / §3, budget (L--) | PH school-MOOE budget with linear regression |
| Sujon et al 2025 | §3.4 evaluation | Metric selection, class imbalance |
| Sanhosh & Singh 2025 | §2.4.4 / §3 | Digital persona / context-aware financial decisioning |
| Yang 2024 | §2.4.4.2 / §3, recommendation | Fuzzy K-means financial recommendation |
| Schwartz et al 2025 | §3.4 evaluation / §2.4.4.2 | XAI for credit scoring |
| Yunita et al 2025 | §3.2 forecasting | RNN/LSTM/GRU comparison |
| Tjostheim 2025 | §3.2 forecasting | Statistical vs. ML forecasting review |
| Shuryhin & Zinovatna 2024 | §2.4.4.2 / §3, recommendation | Isolation Forest + ARIMA/LSTM financial advice |
| Yachamaneni et al 2025 | §3.2 profiling | Self-supervised customer profiling |
| Yang T. et al 2024 | §2.4.1 / §3 | Customer insights + risk analysis |
| Wang F. et al 2025 | §3.2/§3.3 anomaly | Deep anomaly detection taxonomy |

The remaining papers map mostly to fraud detection (shared anomaly sibling), portfolio/investment,
or off-scope domains (stock, hotel, electricity) outside the personal savings/debt algorithm focus.

---

## Recommended Next Steps

1. **Confirm verdicts** for the "Review" papers — researcher decision, especially the
   fraud-family (keep as anomaly-sibling evidence?), the portfolio/investment cluster,
   and the two local `L--` PH papers (Santiago, Salvador).
2. **Intake the Maintain set** per `docs/standards/rrl-workflow.md` (batch-7 runbook):
   copy to `literature/bucket/` → `fetch_pdfs.py` → `prepare_pdf.py` → rename with the
   proposed stems → summarize `_summarized.json` → `embed.py` + `score.py`.
3. **Survive-note carry-overs:** Salminen/Salvador PDFs are already staged in `literature/bucket/`;
   treat as carry-over, not re-screen. **Samuel/Sanchez** have no recoverable PDF in this workspace —
   flag for the researcher to re-fetch from the Drive source before inclusion.
4. **Re-score** once the intake lands — batch-5 old-run best_module/best_score values were computed
   from the deprecated 518-paper corpus and will be replaced by the batch-7 run.
