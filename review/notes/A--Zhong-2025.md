---
paper_id: A--Zhong-2025
first_author: "Zhong"
year: 2025
title: "Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features"
venue: "2025 International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS 2025), ACM"
doi: 10.1145/3776759.3776850
type: conference-paper
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation, rule_based_classification, model_development]
module_rationale:
  model_algorithm_integration: "Sect. 3 wires sliding-window statistics, Bayesian change point detection and a weighted Isolation Forest / DBSCAN / Local Outlier Factor ensemble into one pipeline, and Fig. 1 (p. 4) draws the feature-extraction streams that feed the threshold."
  model_performance_evaluation: "Table 4 (p. 7) reports precision, recall, F1-score, false positive rate, processing time and significance for the proposed framework against three detectors, with McNemar's test, a Bonferroni-corrected paired t-test and bootstrap intervals (Sect. 4.3, p. 7)."
  rule_based_classification: "Eq. 1 (p. 3) fixes a deterministic detection boundary tau(t) = mu(t) + alpha x sigma(t) x beta^(t-t0), and Sect. 4.3 (p. 7) names statistical charts, percentiles and rule-based detection systems as the threshold-based systems the framework is tested against."
  model_development: "Sect. 3.2 and 4.1 (pp. 3-5) specify the model-ready workflow: Monte Carlo data generation, temporal interpolation, adaptive filtering, robust scaling, time-index registration, and window statistics for skewness, kurtosis and seasonality (Eqs. 2-5)."
---

# Adaptive Anomaly Detection Threshold for Financial Data Quality Monitoring Based on Time Series Features

`A--Zhong-2025` — Zhong (2025), *2025 International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS 2025), ACM* \[10.1145/3776759.3776850]

## Summary

An adaptive anomaly-detection threshold for bank transaction data quality recalibrates a sliding-window detection boundary from time-series features and Bayesian change point detection, with an Isolation Forest–DBSCAN–Local Outlier Factor ensemble scoring anomalies; on synthetic data it reaches precision 0.847, recall 0.891 and F1 0.868 against a fixed threshold.

## Problem and Motivation

Financial transaction streams evolve, so a threshold set once stops matching the distribution it was calibrated on, and static settings then produce false positives and missed detections (Sec. 1.1, p. 1). Monitoring systems must also separate natural distribution change from genuine anomaly, and supervisory stress-testing regimes such as CCAR and DFAST make accurate anomaly identification a regulatory requirement (Sec. 1.1, p. 1). The operational cost is concrete: excessive false positives during volatility or seasonal shifts force manual review that consumes significant operational resources (Sec. 5.2, p. 8).

## Method

**Design.** Viewpoint paper presenting a computational framework, evaluated on synthetic Monte Carlo transaction data against fixed-threshold, statistical and ML-based baselines; Sect. 5.2 (p. 8) calls the work a Viewpoint paper and no formal design label is stated.
**Sample.** Synthetic Monte Carlo credit-card transactions in three splits: training 2,847,392 transactions over 365 days, validation 356,741 over 45 days, test 445,928 over 60 days; unit = one synthetic transaction, with 48,750, 12,188 and 15,235 customer accounts and 16, 14 and 15 transaction types respectively (Table 3, p. 6).
**Context.** geography: Not reported (no country is named; the transactions are simulated); population: Not applicable (synthetic customer accounts, no human participants); setting: Virtual/computational — offline benchmarking of a data-quality monitoring framework, with no live institution, no user-facing application and no deployment.

- Generate simulated Monte Carlo credit-card transactions carrying commodity, workday or seasonal occasion attributes and injected anomalies: sudden increase gaps, atypical geography, non-seasonal timing, and deviations from everyday trading categories (Sect. 4.1, p. 5).
- Mask the generated records and preprocess them: temporal interpolation for missing values, adaptive filtering to separate measurement noise from legitimate variance, robust scaling, and registration of a consistent time index across data sources (Sect. 4.1, p. 5).
- Extract time-series features over a sliding window: moving-average level, standard deviation, skewness and kurtosis, computed over multiple horizons (Sect. 3.2, Eqs. 2-5, p. 3).
- Decompose the transaction series into trend, seasonal and residual components using seasonal decomposition, exponential smoothing and trend analysis, in parallel processing streams (Sect. 3.2, pp. 3-4).
- Segment the series with Bayesian change point detection detectors used together with information-theoretic criteria and evidence for detected change, so major pattern shifts trigger threshold adjustment (Sect. 3.1, p. 3).
- Compute the adaptive threshold from the window mean, the sensitivity factor and the decay factor, so the boundary moves without manual recalibration (Sect. 3.1, Eq. 1 and Table 1, p. 3).
- Score anomalies with an ensemble of Isolation Forest, DBSCAN clustering and Local Outlier Factor, combined by weights proportional to each algorithm's area under the ROC curve (Sect. 3.3, Eqs. 6-7, p. 4).
- Adapt DBSCAN's neighbourhood radius to the 90th percentile of k-nearest-neighbour distances inside each window, holding min_samples fixed at 10 (Sec. 3.3, Eq. 8, p. 5).
- Evaluate with precision, recall, F1-score and false positive rate under temporal cross-validation and sliding-window validation, with bootstrap resampling for confidence intervals (Sect. 4.2, p. 6).
- Benchmark against fixed-threshold, statistical and ML-based detectors on identical datasets and inspection criteria, with factorial sensitivity analysis; results are mean ± standard deviation over 10 independent runs (Sect. 4.3 and Table 4 note, p. 7).

## Software

- Isolation Forest (library and version Not reported; n_estimators=200, contamination=auto)
- DBSCAN (library and version Not reported; eps=adaptive, min_samples=10)
- Local Outlier Factor (library and version Not reported; n_neighbors=20, contamination=0.1)
- Grid Search CV, Silhouette Analysis and Bayesian Optimization, named as the tuning method for each ensemble member (Table 2, p. 5)
- Intel Xeon E5-2680 v4 @ 2.40GHz with 32GB RAM, the benchmark platform for the processing-time column (Table 4 note, p. 7)
- No programming language, package or version is named anywhere in the paper.

## Key Findings

- num: Table 4 (p. 7) gives the proposed framework precision 0.847 ± 0.023, recall 0.891 ± 0.016, F1-score 0.868 ± 0.015 and FPR 0.076 ± 0.004, at 21.5 ± 2.3 ms per 1000 transactions, p < 0.001.
- num: The fixed-threshold baseline is precision 0.724 ± 0.031, recall 0.831 ± 0.024, F1 0.774 ± 0.022 and FPR 0.142 ± 0.008, at 12.3 ± 1.4 ms per 1000 transactions, with no significance value printed.
- num: The statistical baseline is precision 0.789 ± 0.028, recall 0.856 ± 0.021, F1 0.821 ± 0.019 and FPR 0.098 ± 0.006, at 18.7 ± 2.1 ms, p < 0.01.
- num: The ML-based baseline is precision 0.812 ± 0.025, recall 0.873 ± 0.018, F1 0.841 ± 0.017 and FPR 0.089 ± 0.005, at 24.1 ± 2.8 ms in the page-aware extraction of Table 4 and 24.8 ± 2.8 ms in the full-text pass, p < 0.001.
- num: The proposed framework cuts false positive rate by 46.5% and raises F1 accuracy by 12.1% against the fixed-threshold comparison (Sec. 5.1, p. 8).
- num: Memory usage analysis reports resource requirements 23 percent lower than conventional threshold methods (Sec. 5.1, p. 8).
- num: Table 1 defaults are window size 1000 (range 500-5000), sensitivity factor 0.15 (0.05-0.30), decay factor 0.95 (0.80-0.99) and change point threshold 0.01 (0.001-0.05), the last set by cross-validation on synthetic financial data (p. 3).
- num: Table 3 anomaly rates are 2.14 ± 0.08% in training, 2.31 ± 0.12% in validation and 1.97 ± 0.09% in test, so the splits are strongly imbalanced toward normal transactions (p. 6).
- num: Average daily volume is 7,801 ± 342 (training), 7,927 ± 289 (validation) and 7,432 ± 401 (test), with peak volumes of 12,847, 11,203 and 10,891 (Table 3, p. 6).
- num: The abstract reports the headline gain as 46.5% under the name "false favorable rates", while Sect. 5.1 (p. 8) and the conclusion (p. 9) report the same figure as a false positive rate reduction; the term in the abstract is never defined.
- Processing time grows in proportion to business volume without sacrificing detection accuracy, and the framework is stated to be stable across customer segments and transaction types (Sec. 5.1, p. 8).
- The paper states that trading volume and patterns vary predictably at year-end and holiday periods, which static systems wrongly flag as anomalies (Sec. 5.2, p. 8).

## Key Figures and Tables

- Figure 1 (p. 4): Time Series Feature Extraction Pipeline Architecture — parallel streams over time dependencies, statistical properties and frequency-domain patterns feed threshold computation → the detection boundary is conditioned on features rather than fixed.
- Figure 2 (p. 6): Multidimensional Performance Evaluation Framework — detection accuracy, computational efficiency and system robustness with significance testing built in → evaluation is not precision alone; latency and robustness are treated as first-class outcomes.
- Figure 3 (p. 7): Algorithm Performance Comparison Across Multiple Dimensions — visual comparison of the four methods → the proposed framework leads on precision, recall, F1-score and false positive rate reduction against all baselines.
- Table 1 (p. 3): Adaptive Threshold Algorithm Parameters — window size, sensitivity factor, decay factor and change point threshold with defaults and ranges → four tunable parameters are printed with search ranges, but the search itself is described only as cross-validation on synthetic data.
- Table 2 (p. 5): Unsupervised Learning Algorithm Configuration — parameters, optimization method and performance metric per algorithm → each ensemble member is tuned against a different criterion (AUC-ROC, cluster validity, precision-recall).
- Table 3 (p. 6): Dataset Characteristics and Statistics — totals, anomaly rate, temporal span, accounts, transaction types and daily volumes per split → the evaluation data is synthetic and 1.97-2.31% anomalous, so accuracy would be uninformative and is not reported.
- Table 4 (p. 7): Comparative Analysis Results Summary — precision, recall, F1-score, FPR, processing time and p-value for four methods → the proposed framework is best on all four detection metrics, and the fixed threshold is the fastest.

## Limitations and Gaps

- Every reported result is measured on synthetic Monte Carlo transactions; the authors state this "introduces limitations regarding generalization to real-world financial systems" and ask for validation on anonymised real transaction data (p. 9, with the same point made at p. 5).
- The framework does not handle entirely unexpected behaviour: where the market is abnormal and behaviour was not anticipated, the authors state the approach does not handle it well (p. 9).
- The comparison is confined to one synthetic dataset and one split design; although Sect. 4.3 (p. 7) says factorial sensitivity analysis across data conditions was performed, no sensitivity result is printed for any condition.
- Accuracy is never reported even though the anomaly rate is 2.14 ± 0.08%, 2.31 ± 0.12% and 1.97 ± 0.09% across the three splits, so no overall correctness rate can be reconstructed (Table 3, p. 6).
- Table 4 prints mean ± standard deviation over 10 independent runs with bootstrap n = 1000, but no confidence-interval bounds and no effect sizes are given, although the text states the framework pairs statistical testing with effect size measurement (pp. 7-8).
- The two conversion passes of the same table disagree on one printed value: the ML-based processing time is 24.1 ± 2.8 ms in the page-aware extraction and 24.8 ± 2.8 ms in the full-text pass; both are kept as rows and neither is a winner (Table 4, p. 7).
- [unacknowledged] The abstract attaches the 46.5% figure to "false favorable rates", a term the paper never defines, while Sect. 5.1 and the conclusion attach the identical figure to false positive rates (p. 1 against pp. 8-9).
- [unacknowledged] The tuning behind the Table 1 defaults is described only as cross-validation on synthetic financial data; no search space, objective function or winning configuration is reported (p. 3).
- [unacknowledged] The domain is bank transaction data quality for supervisory reporting; the paper contains no household spending series, no personal finance application and no end user, so nothing in it measures whether a person acts on an alert (p. 8).
- [unacknowledged] Precision and recall rest on a test set with a 1.97 ± 0.09% anomaly rate, yet no class-wise breakdown, confusion matrix or detection-count figure is printed, so the number of anomalous records behind those estimates cannot be established (pp. 6-7).

## Definitions

- **Adaptive threshold tau(t)** — the detection boundary recomputed each period from the current window's mean and standard deviation, weighted toward history by the decay factor (Eq. 1, p. 3).
- **Window size (W)** — number of observations in the sliding window; default 1000, range 500-5000 (Table 1, p. 3).
- **Sensitivity factor (alpha)** — dimensionless ratio controlling threshold strictness; default 0.15, range 0.05-0.30 (Table 1, p. 3).
- **Decay factor (beta)** — historical weight decay rate with 0 < beta < 1, reducing the influence of historical information; default 0.95 (Table 1, p. 3).
- **Change point threshold (gamma)** — the statistical significance level for pattern shifts, set by cross-validation on synthetic financial data; default 0.01 (Table 1, p. 3).
- **Ensemble anomaly score S(x)** — weighted sum of the normalized scores of Isolation Forest, DBSCAN and Local Outlier Factor, with weights summing to one (Eq. 6, p. 4).
- **Dynamic weight w_j(t)** — algorithm j's share of the ensemble score, proportional to its area under the ROC curve at time t on recent validation data (Eq. 7, p. 4).
- **Anomaly rate** — the percentage of transactions in a split carrying an anomalous label; 2.14 ± 0.08% in the training split (Table 3, p. 6).
- **False positive rate (FPR)** — the proportion of normal transactions incorrectly flagged as anomalies, FP/(FP+TN) (Eq. 12, p. 6).
- **Sliding window validation** — evaluation that respects the temporal ordering of transactions while still reporting performance across periods and data types (Sect. 4.2, p. 6).
- **Financial data quality monitoring** — automated, end-to-end validation of transaction data for governance and supervisory stress testing, motivated by CCAR and DFAST (Sect. 2.3, p. 2).
- **Adaptive batch- and cross-customer calibration** — DBSCAN clustering of transactions by proximity and volume into behavioural groupings that establish thresholds (Sect. 3.3, p. 4).
- **Cluster validity** — the DBSCAN tuning metric named in Table 2 alongside silhouette analysis as its optimization method (p. 5).

## Key Equations

- `tau(t) = mu(t) + alpha x sigma(t) x beta^(t-t0)` — adaptive detection threshold from window mean, sensitivity and decay.
- `MA(t) = (1/W) x sum of x_i over the window` — moving-average level; summation bounds are garbled in the conversion (Eq. 2, p. 3).
- `sigma(t) = sqrt[(1/W) x sum of (x_i - MA(t))^2]` — window standard deviation about the moving average (Eq. 3, p. 3).
- `gamma1(t) = E[(X - mu)^3] / sigma^3` — skewness of the transaction distribution over the window (Eq. 4, p. 3).
- `gamma2(t) = E[(X - mu)^4] / sigma^4` — kurtosis of the transaction distribution over the window (Eq. 5, p. 3).
- `S(x) = sum over j=1..M of w_j x s_j(x)` — ensemble anomaly score with M = 3 and weights summing to one (Eq. 6, p. 4).
- `w_j(t) = AUC_ROC_j(t) / sum over k of AUC_ROC_k(t)` — reliability-proportional ensemble weight (Eq. 7, p. 4).
- `epsilon(i) = Percentile90(D_k(W_i))` — DBSCAN radius from the 90th percentile of k-nearest-neighbour distances (Eq. 8, p. 5).
- `Precision = TP/(TP + FP)` — correctly identified anomalies among all flagged transactions (Eq. 9, p. 6).
- `Recall = TP/(TP + FN)` — actual anomalies successfully detected (Eq. 10, p. 6).
- `F1 = 2 x (Precision x Recall)/(Precision + Recall)` — harmonic mean balancing precision and recall (Eq. 11, p. 6).
- `FPR = FP/(FP + TN)` — normal transactions incorrectly flagged as anomalies (Eq. 12, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Anomaly detection, proposed adaptive threshold framework | precision | 0.847 ± 0.023 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, proposed adaptive threshold framework | recall | 0.891 ± 0.016 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, proposed adaptive threshold framework | F1-score | 0.868 ± 0.015 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, proposed adaptive threshold framework | false positive rate | 0.076 ± 0.004 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, proposed adaptive threshold framework | processing time (ms per 1000 transactions) | 21.5 ± 2.3 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, fixed-threshold baseline | precision | 0.724 ± 0.031 | — | — | Table 4, p. 7 |
| Anomaly detection, fixed-threshold baseline | recall | 0.831 ± 0.024 | — | — | Table 4, p. 7 |
| Anomaly detection, fixed-threshold baseline | F1-score | 0.774 ± 0.022 | — | — | Table 4, p. 7 |
| Anomaly detection, fixed-threshold baseline | false positive rate | 0.142 ± 0.008 | — | — | Table 4, p. 7 |
| Anomaly detection, fixed-threshold baseline | processing time (ms per 1000 transactions) | 12.3 ± 1.4 | — | — | Table 4, p. 7 |
| Anomaly detection, statistical baseline | precision | 0.789 ± 0.028 | — | p < 0.01* | Table 4, p. 7 |
| Anomaly detection, statistical baseline | recall | 0.856 ± 0.021 | — | p < 0.01* | Table 4, p. 7 |
| Anomaly detection, statistical baseline | F1-score | 0.821 ± 0.019 | — | p < 0.01* | Table 4, p. 7 |
| Anomaly detection, statistical baseline | false positive rate | 0.098 ± 0.006 | — | p < 0.01* | Table 4, p. 7 |
| Anomaly detection, statistical baseline | processing time (ms per 1000 transactions) | 18.7 ± 2.1 | — | p < 0.01* | Table 4, p. 7 |
| Anomaly detection, ML-based baseline | precision | 0.812 ± 0.025 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, ML-based baseline | recall | 0.873 ± 0.018 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, ML-based baseline | F1-score | 0.841 ± 0.017 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, ML-based baseline | false positive rate | 0.089 ± 0.005 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, ML-based baseline, page-aware extraction of the table | processing time (ms per 1000 transactions) | 24.1 ± 2.8 | — | p < 0.001 | Table 4, p. 7 |
| Anomaly detection, ML-based baseline, full-text pass of the table | processing time (ms per 1000 transactions) | 24.8 ± 2.8 | — | p < 0.001 | Table 4, p. 7 |
| False positive rate reduction, proposed framework against fixed threshold | false positive rate reduction | 46.5% | — | — | Sec. 5.1, p. 8 |
| F1-score improvement, proposed framework against fixed threshold | F1 accuracy improvement | 12.1% | — | — | Sec. 5.1, p. 8 |
| False positive rate reduction, proposed framework against fixed threshold | false positive rate reduction, termed "false favorable rates" in the text | 46.5% | — | — | Abstract, p. 1 |
| False positive rate reduction, proposed framework against fixed threshold | false positive rate reduction | 46.5% | — | — | Sec. 6 Conclusion, p. 9 |
| Memory footprint against conventional threshold methods | memory reduction | 23 percent | — | — | Sec. 5.1, p. 8 |
| Synthetic dataset, training split | total transactions | 2,847,392 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | total transactions | 356,741 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | total transactions | 445,928 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | anomaly rate | 2.14 ± 0.08 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | anomaly rate | 2.31 ± 0.12 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | anomaly rate | 1.97 ± 0.09 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | temporal span (days) | 365 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | temporal span (days) | 45 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | temporal span (days) | 60 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | customer accounts | 48,750 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | customer accounts | 12,188 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | customer accounts | 15,235 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | transaction types | 16 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | transaction types | 14 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | transaction types | 15 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | average daily volume | 7,801 ± 342 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | average daily volume | 7,927 ± 289 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | average daily volume | 7,432 ± 401 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | peak daily volume | 12,847 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | peak daily volume | 11,203 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | peak daily volume | 10,891 | — | — | Table 3, p. 6 |
| Synthetic dataset, training split | minimum daily volume | 4,231 | — | — | Table 3, p. 6 |
| Synthetic dataset, validation split | minimum daily volume | 4,892 | — | — | Table 3, p. 6 |
| Synthetic dataset, test split | minimum daily volume | 4,567 | — | — | Table 3, p. 6 |
| Adaptive threshold configuration, default value | window size W | 1000 | — | — | Table 1, p. 3 |
| Adaptive threshold configuration, default value | sensitivity factor alpha | 0.15 | — | — | Table 1, p. 3 |
| Adaptive threshold configuration, default value | decay factor beta | 0.95 | — | — | Table 1, p. 3 |
| Adaptive threshold configuration, default value | change point threshold gamma | 0.01 | — | — | Table 1, p. 3 |
| Isolation Forest configuration | n_estimators | 200 | — | — | Table 2, p. 5 |
| Isolation Forest configuration | contamination | auto | — | — | Table 2, p. 5 |
| DBSCAN configuration | min_samples | 10 | — | — | Table 2, p. 5 |
| DBSCAN adaptive selection of eps | percentile of k-nearest-neighbour distances | Percentile90 | — | — | Eq. 8, p. 5 |
| Local Outlier Factor configuration | n_neighbors | 20 | — | — | Table 2, p. 5 |
| Local Outlier Factor configuration | contamination | 0.1 | — | — | Table 2, p. 5 |
| Reproducibility of the comparative analysis | independent runs | 10 | — | — | Table 4 note, p. 7 |
| Confidence interval estimation for the comparative analysis | bootstrap resamples | n=1000 | — | — | Table 4 note, p. 7 |
| Benchmark platform for the processing-time column | processor and memory | Intel Xeon E5-2680 v4 @ 2.40GHz with 32GB RAM | — | — | Table 4 note, p. 7 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "traditional static threshold-based anomaly detection systems exhibit significant limitations in adapting to distributional shifts, leading to elevated false positives and compromised detection accuracy" | Abstract, p. 1 | rule_based_classification |
| "We propose a dynamic threshold adjustment framework that leverages time series feature extraction combined with unsupervised learning techniques to calibrate detection thresholds based on evolving data characteristics automatically." | Abstract, p. 1 | model_algorithm_integration |
| "Our methodology integrates sliding window statistical analysis with Bayesian change point detection algorithms to identify significant pattern shifts." | Abstract, p. 1 | model_algorithm_integration |
| "At the same time, ensemble approaches combining Isolation Forest, DBSCAN clustering, and Local Outlier Factor provide robust anomaly scoring mechanisms." | Abstract, p. 1 | model_algorithm_integration |
| "Threshold-based recognition fails to adapt to dynamic transaction patterns, which leads to high false positives and missed detections." | Sec. 1.1, p. 1 | rule_based_classification |
| "Static threshold settings do not adapt to genuine differences in purchasing policies, seasonal buying, or evolving customer preferences, leading to many false alarms, increased operational costs, and reduced system efficiency" | Sec. 1.2, p. 1 | rule_based_classification |
| "Our algorithm uses sliding window statistical analysis to calculate both global and local parameters for threshold adjustment." | Sec. 3.1, p. 3 | rule_based_classification |
| "The integration framework you designed serves not only to balance weights between the different unsupervised algorithms but to provide seamless coordination among them within a real-time processing scenario." | Sec. 3.3, p. 4 | model_algorithm_integration |
| "Before we go on, remember that handling missing data points in a data preprocessing task of such magnitude is just one step." | Sec. 4.1, p. 5 | model_development |
| "Our synthetic data approximates statistical properties of real transactions through parametric modeling, but may not fully represent the long-tail distributions and rare event combinations present in actual financial systems." | Sec. 4.1.1, p. 5 | model_development |
| "The use of synthetic data was necessitated by privacy regulations and proprietary constraints preventing access to real financial transaction data." | Sec. 4.1.1, p. 5 | model_development |
| "Introducing a tradeoff between detection sensitivity and operating efficiency is its defining characteristic" | Sec. 4.2, p. 6 | model_performance_evaluation |
| "Results represent mean ± standard deviation over 10 independent runs." | Table 4 note, p. 7 | model_performance_evaluation |
| "Statistical significance was determined using McNemar's test for model comparison and a 5x2-fold cross-validation paired t-test with Bonferroni correction for multiple comparisons." | Table 4 note, p. 7 | model_performance_evaluation |
| "Non-parametric bootstrap resampling (n=1000) was applied to estimate confidence intervals for performance metrics." | Table 4 note, p. 7 | model_performance_evaluation |
| "Figure 3 provides a visual comparison of algorithm performance across multiple evaluation dimensions, demonstrating the proposed framework's superiority in precision, recall, F1-score, and false positive rate reduction compared to baseline methods." | Sec. 4.3, p. 7 | model_performance_evaluation |
| "Traditional static threshold systems often generate excessive false positives during periods of market volatility or seasonal transaction pattern changes, forcing manual review that consumes significant operational resources." | Sec. 5.2, p. 8 | rule_based_classification |
| "The framework's unsupervised learning approach allows it to be used in federated environments, where labeled training data can be scarce or absent." | Sec. 5.2.2, p. 8 | model_algorithm_integration |
| "The problem with the proposed adaptive threshold algorithm is that if the market is abnormal and entirely unexpected behaviour should occur in the markets, then this approach does not handle it well." | Sec. 5.3, p. 9 | model_performance_evaluation |
| "Validation on anonymized real-world datasets from financial institutions would provide crucial evidence of the framework's operational effectiveness and identify additional edge cases requiring algorithmic refinement." | Sec. 5.3, p. 9 | model_performance_evaluation |

## Remember This

- The framework recalibrates a sliding-window threshold and adds an Isolation Forest, DBSCAN and Local Outlier Factor ensemble for scoring.
- On synthetic data it reaches precision 0.847, recall 0.891 and F1 0.868, with false positive rate down 46.5% from a fixed threshold.
- Table 4 compares four detectors; McNemar's test, a Bonferroni-corrected paired t-test and bootstrap n=1000 supply significance.
- All results come from simulated Monte Carlo transactions, and the authors ask for anonymised real-data validation.
- The domain is bank transaction data quality, not household budgeting or user-facing alerting.

## Cited Works

- Iqbal, A.; Amin, R.; Alsubaei, F. S.; Alzahrani, A. (2024) (context) — deep ensemble models for anomaly detection in multivariate time series data, credited in the acknowledgments with deepening the author's grasp of ensemble detection. [Acknowledgments, p. 9; ref. 1]
- Asmar, M.; Aqel, B. Y. (2023) (context) — analysis of credit card anomaly detection from a process and techniques perspective, cited for the static-threshold failure that outdates efficiency gains. [Sec. 1.1, p. 1; ref. 2]
- Liu, H. (2025) (context) — multi-variable time-series anomaly detection for intelligent operation and maintenance, cited for the validation demands of supervisory stress testing. [Sec. 1.1, p. 1; ref. 3]
- Jain, J.S.; Sapra, A.; Gupta, A.; Dagar, L.; Niranjan, V. (2025) (baseline) — performance analysis of machine learning and deep learning models for credit card anomaly detection, cited for the false alarms static settings produce. [Sec. 1.2, p. 1; ref. 4]
- Chen, Z.; Wang, S.; Yan, D.; Li, Y. (2023) (methodology) — reinforcement learning with LSTM for a bank credit card anomaly detection system, cited for wise calibration of thresholds on temporal patterns. [Sec. 1.2, p. 2; ref. 5]
- Ida, S. J.; Balasubadra, K. (2024) (methodology) — LSTM sequential analysis with early stopping for credit card anomaly detection, cited for automatic parameter tuning. [Sec. 1.3, p. 2; ref. 6]
- Chen, Y.; Zhao, C.; Xu, Y.; Nie, C. (2025) (context) — systematic review of year-over-year deep learning developments in financial anomaly detection, cited for tuning under changing data characteristics. [Sec. 1.3, p. 2; ref. 7]
- Sathe, R.; Shinde, S. (2024) (context) — a deep learning framework for effective anomaly detection in time series data, cited for the perceptual aspects of behaviour. [Sec. 1.3, p. 2; ref. 8]
- Cui, Y.; Han, X.; Chen, J.; Zhang, X.; Yang, J.; Zhang, X. (2025) (context) — FraudGNN-RL, a graph neural network with reinforcement learning for adaptive financial anomaly detection, cited as prior art. [Sec. 2.1, p. 2; ref. 9]
- Suganthi, V.; Jebathangam, J. (2024) (context) — GRU networks for credit card anomaly detection, cited for adaptivity achieved in reinforcement-learning approaches. [Sec. 2.1, p. 2; ref. 10]
- Tang, Y.; Liu, Z. (2024) (context) — credit card anomaly detection based on SDT and federated learning, cited for sequence analysis in dynamic financial systems. [Sec. 2.3, p. 3; ref. 11]
- Chidambaranathan, P.; MuthuPriya, V. (2024) (methodology) — risk prediction in financial transactions using IoT big data analytics, cited for dynamic optimisation of Isolation Forest parameters. [Sec. 3.3, p. 4; ref. 12]
- Xie, Y.; Zhou, M.; Liu, G.; Wei, L.; Zhu, H.; De Meo, P. (2025) (context) — a transactional-behaviour-based hierarchical gated network for credit card anomaly detection, cited for sensitivity to unconventional behaviour. [Sec. 3.2, p. 4; ref. 13]
- Meng, C. C.; Lim, K. M.; Lee, C. P.; Lim, J. Y. (2023) (baseline) — TabNet for credit card anomaly detection, cited as an interpretable architecture with performance no worse than the state of the art. [Sec. 4.1, p. 5; ref. 14]
- Alamri, M. A.; Ykhlef, M. A. (2023) (methodology) — a machine learning framework for detecting credit card anomalies, cited for temporal cross-validation that respects temporal orderings. [Sec. 4.2, p. 6; ref. 15]

---

Conversion: [`A--Zhong-2025_marked.md`](../../literature/paper-markdowns/A--Zhong-2025_marked.md)