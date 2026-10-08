---
paper_id: A--KaraSenguler-2025
first_author: Kara
year: 2025
title: "A Comparative Analysis of Budget Forecasting Methods: A Systematic Literature Review Covering the 1983-2024 Period"
venue: "Public Budgeting & Finance"
doi: 10.1111/pbaf.70008
designation: algorithm
status: extracted
modules: [budgeting, data_collection, model_performance_evaluation, model_algorithm_integration]
module_rationale:
  budgeting: "The paper systematically reviews methods for forecasting public budgets, a core component of budget creation and fiscal planning (Abstract, p. 1; Sect. 1, p. 1)."
  data_collection: "It analyzes the characteristics of training datasets in the reviewed studies, including time spans, observation counts, and data frequencies (Sect. 4, pp. 9–11, Tables 2–4)."
  model_performance_evaluation: "It examines the evaluation metrics used to assess forecasting performance, notably MAPE, RMSE, and MAE, and critiques the neglect of directional errors (Sect. 4, p. 13; Sect. 5.4, p. 14)."
  model_algorithm_integration: "It discusses the rise of hybrid and ensemble approaches that combine different forecasting models to improve accuracy and robustness (Sect. 5.6, p. 15)."
---

## Summary

This paper is a systematic literature review of comparative budget forecasting methods published between 1983 and 2024. It analyzes 69 peer-reviewed works (abstract) or 68 comparative studies (text), identifying four phases of methodological evolution: basic statistical methods, diversification, machine learning, and deep learning. The review examines geographic distribution, dataset characteristics, evaluation metrics, forecasting horizons, and citation impact. It finds no universally superior method; performance depends on context. The literature is geographically concentrated, with 43% of studies focused on the United States and developing economies underrepresented. Evaluation is dominated by MAPE, RMSE, and MAE, while directional errors are largely neglected. The authors advocate for a pluralistic, context-sensitive approach and further investigation of hybrid and ensemble methods.

## Problem and Motivation

Budget forecasts are strategic instruments of fiscal management, shaping resource allocation, policy credibility, and economic stability. Forecast errors can undermine government programs and lead to policy failure. The existing literature does not provide a homogeneous assessment of forecasting method success because studies vary in datasets, time periods, countries, and model types. A systematic evaluation is needed to guide method selection for policymakers and practitioners. The study responds to a research agenda that identifies “Data and Methods” as a top-tier priority, explicitly calling for research that improves the accuracy of budget and revenue forecasting (McDonald et al. 2024, cited on p. 2). By synthesizing four decades of comparative performance, the review aims to bridge academic inquiry and operational needs.

## Method

**Design.** Systematic literature review with bibliometric-style descriptive statistical analysis, trend analysis, and network analysis; the authors state no formal systematic review protocol label (Sect. 3, p. 3).
**Sample.** n = 69 peer-reviewed works (Abstract, p. 1) / 68 comparative studies (Sect. 4, p. 4); the unit of analysis is a published study that compares multiple forecasting methods and validates forecasts against actual outcomes.
**Context.** geography: international literature, with 43% of studies focused on the United States; other countries include China, Türkiye, Brazil, South Africa, India, and various European countries; population: public budget forecasting studies; setting: academic literature published in peer-reviewed journals, books, book chapters, and scientific conference proceedings from 1983 to 2024.

- Establish inclusion criteria: peer-reviewed articles, books, book chapters, and scientific conference proceedings; studies must compare multiple forecasting methods within the same study; forecasts must be compared with actual outcomes for corresponding periods; exclude single-method studies and non-peer-reviewed reports, technical notes, or institutional assessments.
- Standardize method names: group variants of artificial neural networks under a single ANN category, and consolidate minor variations in model structure or configuration under a single heading.
- Conduct descriptive statistical analysis: frequency of method applications, annual distribution of publications, geographic distribution, metric preferences, and length of forecasting horizons (Sect. 3.1, p. 3).
- Conduct trend analysis: examine temporal changes in method popularity using line graphs to illustrate the evolution of research domains (Sect. 3.2, p. 3).
- Conduct network analysis using Gephi: build method–method, method–year, and method–metric networks; nodes represent methods, years, and metrics; edges denote co-occurrences (Sect. 3.3, p. 4).
- Analyze training dataset characteristics: time span in years, number of observations, and data frequency (Table 2, p. 10).
- Analyze average forecasting horizons by method (Graph 3, p. 12).
- Analyze geographic distribution of studies (Table 3, p. 10).
- Analyze evaluation metric frequency (Table 4, p. 10).
- Analyze the relationship between method diversity and citation counts (Graph 4, p. 13).
- Synthesize findings into a discussion of methodological diversity, benchmarking paradox, data inequality, metric hegemony, academia–practice gap, and hybrid/ensemble approaches (Sect. 5, pp. 14–15).

## Key Findings

- The methodological trajectory of budget forecasting is a four-stage evolution: 1980s basic statistical methods (ARIMA, VAR, regression); subsequent diversification (BVAR, ECM, MIDAS); 2010s machine learning (ANN, SVM); 2020s deep learning and hybrid models (LSTM, XGBoost, PCA-W-KSVR) (Sect. 4, p. 4).
- No single forecasting method is universally superior; optimal choice depends on economic conditions, data quality, institutional structures, and forecast horizon (Abstract, p. 1; Sect. 6, p. 15).
- Geographic concentration is pronounced: the United States accounts for 30 studies (43% per abstract), followed by China (6), panel datasets (6), Türkiye (4), Brazil (2), India (2), South Africa (2), and 17 countries studied once (Table 3, p. 10; Abstract, p. 1).
- Training datasets most commonly span 11–15 years (17 studies); over 60% of studies use datasets covering 6–25 years; 26–50 observations is the most common range (16 studies) (Table 2, p. 10; Sect. 4, p. 10).
- Quarterly data are most common (28 studies), followed by annual (26) and monthly (23); biannual data are rare (1 study) (Table 2, p. 10).
- Evaluation metrics are dominated by MAPE (38 studies), RMSE (36), and MAE (22); directional metrics such as MPE (7), PE (6), MSE (5), and ME (5) are infrequent; two studies report no metric (Table 4, p. 10; Sect. 4, p. 13).
- Average forecasting horizons vary by method: AR (14.3 years), MA (12), MIDAS (9.7), ARIMA (5.5), VAR (5.1), BVAR (4.7), ANN (5.3), and LSTM (3.3) (Graph 3, p. 12; Sect. 4, p. 11).
- Citation impact is highest for studies comparing 3–6 methods (3 methods: 26 citations; 6 methods: 26 citations); single-method studies are rare (3 studies) and have low average citations (7) (Graph 4, p. 13; Sect. 4, p. 14).
- The authors advocate a shift away from seeking a single best model toward a pluralistic, context-sensitive, and potentially hybrid approach (Abstract, p. 1; Sect. 6, p. 15).

## Key Figures and Tables

- Figure 1 (p. 9): Evolution of forecasting methods in budgeting literature over time — illustrates the four-stage methodological evolution from basic statistical models to deep learning and hybrid models.
- Figure 2 (p. 9): Co-occurrence of forecasting methods in comparative budget studies — shows that traditional methods are often compared with next-generation techniques; ARIMA is frequently compared with SARIMA, ANN, or SVM.
- Figure 3 (p. 12): Relationship between methods and performance metrics — RMSE and MAPE are central nodes with strong associations to widely used methods such as ARIMA, ANN, HW, VAR, OFC, COF, and SARIMA.
- Table 1 (pp. 5–8): Literature review of comparative budget forecasting studies — systematically summarizes 68 studies by authors, country, observation type, range years, frequency, observations, methods, best/worst methods, and metrics.
- Table 2 (p. 10): Characteristics of training datasets — period (1–5 years to 50+ years), observation range (1–25 to 1000+), and frequency (quarterly, annual, monthly, biannual).
- Table 3 (p. 10): Country-level distribution of budget forecasting research — USA 30, China 6, Panel 6, Türkiye 4, Bharat 2, Brazil 2, South Africa 2, Others 17.
- Table 4 (p. 10): Number of studies using each evaluation metric — MAPE 38, RMSE 36, MAE 22, MPE 7, PE 6, MSE 5, ME 5, Others 9, None 2.
- Graph 1 (p. 10): Trends in popularity of key forecasting methods over time (best 5) — official forecasts frequently used as benchmarks; ARIMA consistently popular since the 1990s.
- Graph 2 (p. 11): Average training data span by forecasting model (best 10) — ADL and AR have average training periods exceeding 40 years; MIDAS and ARMA can be applied with shorter datasets.
- Graph 3 (p. 12): Average forecasting horizons by method — AR 14.3, MA 12, MIDAS 9.7, ARIMA 5.5, VAR 5.1, BVAR 4.7, ANN 5.3, LSTM 3.3 years.
- Graph 4 (p. 13): Relationship between studies, methods, and citations — studies with 3 methods average 26 citations; studies with 6 methods average 26 citations; single-method studies average 7 citations.

## Limitations and Gaps

- The authors acknowledge pronounced geographic concentration, with the United States dominating and developing economies substantially underrepresented, which limits the generalizability of findings (Sect. 5.3, p. 14; Sect. 6, p. 15).
- The authors acknowledge the near-absolute dominance of MAPE, RMSE, and MAE in performance evaluation, which neglects the direction of errors and asymmetric policy costs (Sect. 5.4, p. 14; Sect. 6, p. 15).
- The authors acknowledge data constraints: many models are built on 11–15 years of data, posing overfitting risks for data-hungry methods such as deep learning (Sect. 5.3, p. 14).
- The authors acknowledge an academia–practice gap: complex state-of-the-art models are often opaque “black boxes” for policymakers, while simpler models offer transparency and accountability (Sect. 5.5, p. 15).
- The authors acknowledge that the limited number of panel studies (6) means the literature has not fully developed a comparative perspective capable of providing generalizable cross-country insights (Sect. 4, p. 13).
- [unacknowledged] The paper contradicts itself on the sample size: the Abstract states 69 peer-reviewed works, while Sect. 4 states 68 comparative studies; no reconciliation is provided.
- [unacknowledged] No formal search strategy, inclusion/exclusion flow diagram, or quality appraisal of included studies is reported; the review is not registered and no inter-rater reliability is reported.
- [unacknowledged] Table 1 is presented in a rotated, partially garbled format in the source, making independent verification of per-study entries difficult.
- [unacknowledged] The review does not conduct a meta-analysis or quantitative synthesis of effect sizes; it reports frequencies and descriptive trends only.
- [unacknowledged] The network analysis using Gephi is described but no network statistics (e.g., centrality, modularity) are reported to support the visual claims.
- [unacknowledged] The paper does not report the exact search string, databases queried, or date of search, limiting reproducibility.

## Definitions

- **ARIMA** — Auto-Regressive Integrated Moving Average, a classical time-series forecasting model.
- **BVAR** — Bayesian Vector Autoregression, a multivariate model with Bayesian priors.
- **ECM** — Error Correction Model, used for cointegrated time series.
- **MIDAS** — Mixed Data Sampling, a regression approach for frequency mismatch.
- **ANN** — Artificial Neural Network, a machine learning model.
- **SVM** — Support Vector Machine, a machine learning model.
- **LSTM** — Long Short-Term Memory, a deep learning recurrent neural network.
- **XGBoost** — Extreme Gradient Boosting, an ensemble tree method.
- **MAPE** — Mean Absolute Percentage Error, a scale-independent accuracy metric.
- **RMSE** — Root Mean Squared Error, a scale-dependent accuracy metric.
- **MAE** — Mean Absolute Error, a scale-dependent accuracy metric.
- **MPE** — Mean Percentage Error, a directional error metric.
- **OFC** — Official Forecasts, used as a benchmark.
- **RW** — Random Walk, a naïve benchmark.
- **COF** — Combination of Forecasts, a method that combines multiple forecasts.
- **SARIMA** — Seasonal Auto-Regressive Integrated Moving Average, a seasonal extension of ARIMA.
- **PCA-W-KSVR** — Principal Component Analysis combined with Wavelet and Kernel Support Vector Regression, a hybrid model.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Peer-reviewed works analyzed, abstract | count | 69 | — | — | Abstract, p. 1 |
| Comparative studies analyzed, text | count | 68 | — | — | Sect. 4, p. 4 |
| Studies focused on United States | percentage | 43% | — | — | Abstract, p. 1 |
| Training dataset period 1–5 years | studies (N) | 4 | — | — | Table 2, p. 10 |
| Training dataset period 6–10 years | studies (N) | 13 | — | — | Table 2, p. 10 |
| Training dataset period 11–15 years | studies (N) | 17 | — | — | Table 2, p. 10 |
| Training dataset period 16–20 years | studies (N) | 10 | — | — | Table 2, p. 10 |
| Training dataset period 21–25 years | studies (N) | 9 | — | — | Table 2, p. 10 |
| Training dataset period 26–30 years | studies (N) | 2 | — | — | Table 2, p. 10 |
| Training dataset period 31–35 years | studies (N) | 7 | — | — | Table 2, p. 10 |
| Training dataset period 35–50 years | studies (N) | 4 | — | — | Table 2, p. 10 |
| Training dataset period 50+ years | studies (N) | 3 | — | — | Table 2, p. 10 |
| Observation range 1–25 | studies (N) | 8 | — | — | Table 2, p. 10 |
| Observation range 26–50 | studies (N) | 16 | — | — | Table 2, p. 10 |
| Observation range 51–75 | studies (N) | 10 | — | — | Table 2, p. 10 |
| Observation range 76–100 | studies (N) | 6 | — | — | Table 2, p. 10 |
| Observation range 101–150 | studies (N) | 12 | — | — | Table 2, p. 10 |
| Observation range 151–250 | studies (N) | 7 | — | — | Table 2, p. 10 |
| Observation range 251–400 | studies (N) | 3 | — | — | Table 2, p. 10 |
| Observation range 401–1000 | studies (N) | 4 | — | — | Table 2, p. 10 |
| Observation range 1000+ | studies (N) | 3 | — | — | Table 2, p. 10 |
| Data frequency: Quarterly | studies (N) | 28 | — | — | Table 2, p. 10 |
| Data frequency: Annual | studies (N) | 26 | — | — | Table 2, p. 10 |
| Data frequency: Monthly | studies (N) | 23 | — | — | Table 2, p. 10 |
| Data frequency: Biannual | studies (N) | 1 | — | — | Table 2, p. 10 |
| Country distribution: USA | studies (N) | 30 | — | — | Table 3, p. 10 |
| Country distribution: China | studies (N) | 6 | — | — | Table 3, p. 10 |
| Country distribution: Panel | studies (N) | 6 | — | — | Table 3, p. 10 |
| Country distribution: Türkiye | studies (N) | 4 | — | — | Table 3, p. 10 |
| Country distribution: Bharat | studies (N) | 2 | — | — | Table 3, p. 10 |
| Country distribution: Brazil | studies (N) | 2 | — | — | Table 3, p. 10 |
| Country distribution: South Africa | studies (N) | 2 | — | — | Table 3, p. 10 |
| Country distribution: Others | studies (N) | 17 | — | — | Table 3, p. 10 |
| Metric: MAPE | studies (N) | 38 | — | — | Table 4, p. 10 |
| Metric: RMSE | studies (N) | 36 | — | — | Table 4, p. 10 |
| Metric: MAE | studies (N) | 22 | — | — | Table 4, p. 10 |
| Metric: MPE | studies (N) | 7 | — | — | Table 4, p. 10 |
| Metric: PE | studies (N) | 6 | — | — | Table 4, p. 10 |
| Metric: MSE | studies (N) | 5 | — | — | Table 4, p. 10 |
| Metric: ME | studies (N) | 5 | — | — | Table 4, p. 10 |
| Metric: Others | studies (N) | 9 | — | — | Table 4, p. 10 |
| Metric: None | studies (N) | 2 | — | — | Table 4, p. 10 |
| Average forecasting horizon: AR | years | 14.3 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: MA | years | 12 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: MIDAS | years | 9.7 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: ARIMA | years | 5.5 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: VAR | years | 5.1 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: BVAR | years | 4.7 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: ANN | years | 5.3 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Average forecasting horizon: LSTM | years | 3.3 | — | — | Graph 3, p. 12; Sect. 4, p. 11 |
| Studies comparing 2 methods | cases | 18 | — | — | Sect. 4, p. 14; Graph 4 |
| Studies comparing 3 methods | cases | 15 | — | — | Sect. 4, p. 14; Graph 4 |
| Studies comparing 4 methods | cases | 14 | — | — | Sect. 4, p. 14; Graph 4 |
| Average citations for studies with 3 methods | citations | 26 | — | — | Sect. 4, p. 14; Graph 4 |
| Average citations for studies with 6 methods | citations | 26 | — | — | Sect. 4, p. 14; Graph 4 |
| Studies employing only a single method | studies | 3 | — | — | Sect. 4, p. 14; Graph 4 |
| Average citations for single-method studies | citations | 7 | — | — | Sect. 4, p. 14; Graph 4 |
| Studies relying on datasets covering 6–25 years | percentage | over 60% | — | — | Sect. 4, p. 10 |
| Studies using datasets of 31 years or more | studies | 14 | — | — | Sect. 4, p. 11 |
| Studies with only 1–25 observations | studies | 8 | — | — | Sect. 4, p. 11 |
| Studies with more than 100 observations | studies | 28 | — | — | Sect. 4, p. 11 |
| Of those, studies with 150 or more observations | studies | 16 | — | — | Sect. 4, p. 11 |
| Studies using quarterly data | studies | 28 | — | — | Sect. 4, p. 11; Table 2 |
| Studies using annual data | studies | 26 | — | — | Sect. 4, p. 11; Table 2 |
| Studies using monthly data | studies | 23 | — | — | Sect. 4, p. 11; Table 2 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study systematically analyzes 69 peer‐reviewed works comparing budget forecasting methods." | Abstract, p. 1 | budgeting |
| "Geographically, 43% of studies focus on the United States, while developing economies remain underrepresented." | Abstract, p. 1 | data_collection |
| "In evaluation, MAPE, RMSE, and MAE dominate, with directional errors largely neglected." | Abstract, p. 1 | model_performance_evaluation |
| "Findings show that optimal method choice depends on context, supporting a pluralistic, context‐sensitive approach rather than universal reliance on a single forecasting method." | Abstract, p. 1 | budgeting |
| "The dataset constructed in this study encompasses the academic literature in which budget forecasting methods have been comparatively evaluated." | Sect. 2, p. 3 | data_collection |
| "The most frequently used evaluation criteria are MAPE (38 studies), RMSE (36 studies), and MAE (22 studies)." | Sect. 4, p. 13 | model_performance_evaluation |
| "The near‐absolute dominance of MAPE, RMSE, and MAE as performance metrics provides a common language for comparison but also poses a potential pitfall: the tyranny of averages." | Sect. 5.4, p. 14 | model_performance_evaluation |
| "The emergence of hybrid models points, albeit modestly, toward a promising direction for the field." | Sect. 5.6, p. 15 | model_algorithm_integration |

## Remember This

- The paper is a systematic review of 69 (abstract) or 68 (text) comparative budget forecasting studies from 1983–2024.
- It identifies four methodological phases: basic statistical, diversification, machine learning, and deep learning.
- No single method is universally best; context determines performance.
- Geographic concentration is severe: 43% of studies focus on the United States; developing economies are underrepresented.
- MAPE, RMSE, and MAE dominate evaluation, while directional errors are neglected.
- Average forecasting horizons are longest for AR (14.3 years) and MA (12 years), shortest for LSTM (3.3 years).
- The authors advocate for pluralistic, context-sensitive, and hybrid/ensemble approaches.