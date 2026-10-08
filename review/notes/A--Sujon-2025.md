---
paper_id: A--Sujon-2025
first_author: Sujon
year: 2025
title: "Accuracy, precision, recall, f1-score, or MCC? empirical evidence from advanced statistics, ML, and XAI for evaluating business predictive models"
venue: "Journal of Big Data"
doi: 10.1186/s40537-025-01313-4
designation: algorithm
status: extracted
modules: [model_performance_evaluation, data_collection, model_development, model_algorithm_integration]
module_rationale:
  model_performance_evaluation: "The paper's central contribution is a statistically rigorous evaluation of five performance metrics (accuracy, precision, recall, F1, MCC) for imbalanced business classification (Abstract, p. 1)."
  data_collection: "The study uses two benchmark datasets: Default of Credit Card Clients (30,000 instances, 23 features) and Telco Customer Churn (7,043 instances, 20+ features) (Sect. Data preparation and preprocessing, p. 6; Sect. Additional dataset, p. 7)."
  model_development: "Five machine learning models (LR, RF, DT, XGB, KNN) are trained with specified hyperparameters and 5-fold stratified cross-validation (Table 4, p. 10; Sect. Stratified 5-fold cross-validation, p. 13)."
  model_algorithm_integration: "A two-stage XAI framework integrates SHAP feature attributions with metric-conditioned threshold analysis to link interpretability to performance metrics (Sect. Explainable AI (XAI) analysis, p. 17)."
---

## Summary

This paper presents a comprehensive, statistically rigorous evaluation of five performance metrics — accuracy, precision, recall, F1-score, and Matthews Correlation Coefficient (MCC) — for imbalanced business classification tasks. Using two benchmark datasets (Default of Credit Card Clients, n = 30,000; Telco Customer Churn, n = 7,043) and five machine learning models (Logistic Regression, Random Forest, Decision Tree, XGBoost, k-Nearest Neighbors), the study incorporates static and dynamic threshold sensitivity analysis, Gaussian noise robustness testing, bootstrap confidence intervals, McNemar's test, Cohen's kappa, and repeated-measures ANOVA. It also introduces a two-stage explainable AI (XAI) framework using SHAP, culminating in 3D metric-conditioned SHAP visualizations that link feature contributions to threshold and metric variation. The authors conclude that F1-score consistently provides the most stable and balanced evaluation across datasets and testing conditions, with MCC offering complementary diagnostic value, while accuracy and precision demonstrate limited robustness under class imbalance.

## Method

**Design.** Comparative benchmark evaluation of five machine learning models across five performance metrics on two imbalanced business datasets, with statistical validation and two-stage XAI; the authors state no formal design label.
**Sample.** n = 30,000 instances (Default of Credit Card Clients dataset) and n = 7,043 instances (Telco Customer Churn dataset); the unit of analysis is a credit card client (first dataset) and a telecom customer (second dataset).
**Context.** geography: Default of Credit Card Clients dataset contains data from a Taiwanese bank's credit card clients; Telco Customer Churn dataset location not reported; population: credit card clients and telecom customers; setting: computational/offline analysis using Python with scikit-learn, XGBoost, and SHAP on a single machine; no live business system was involved.

- Use the "Default of Credit Card Clients" dataset from UCI Machine Learning (30,000 instances, 23 features) with binary target DEFAULT_PAYMENT_NEXT_MONTH (1 = default, 0 = no default).
- Use the Telco Customer Churn dataset from Kaggle (7,043 instances, 20+ features) with binary target Churn (Yes/No), approximately 26.5% churned.
- Standardize all numerical features using z-score normalization.
- Split data into training (80%) and testing (20%) subsets using stratified sampling.
- Select five ML models representing diverse algorithmic paradigms: LR (linear), DT, RF, XGB (tree-based), and KNN (instance-based).
- Train models with specified hyperparameters (Table 4): LR max_iter=1000, solver='lbfgs', penalty='l2', C=1.0; RF n_estimators=100, max_depth=6; DT max_depth=5; XGB n_estimators=100, learning_rate=0.1, max_depth=6, subsample=0.8; KNN n_neighbors=5, weights='uniform'.
- Perform 5-fold stratified cross-validation with scoring metrics [accuracy, precision, recall, f1, mcc].
- Conduct static threshold sensitivity analysis across thresholds 0.1 to 0.9.
- Conduct dynamic threshold sensitivity analysis to find optimal thresholds for each metric.
- Add Gaussian noise (σ = 0.0 to 0.3) to input features and test on noisy data.
- Apply repeated-measures ANOVA with Metric as within factor across five classifiers and nine thresholds.
- Compute bootstrap confidence intervals with N = 1000 resamples at 95% CI.
- Use McNemar's test to compare prediction errors between paired models.
- Use Cohen's kappa to measure agreement between model predictions.
- Implement a cost-sensitive evaluation framework with FP cost = 10 units and FN cost = 100 units, computing Expected Cost of Misclassification (ECM) and Net Profit.
- Apply SHAP analysis to LR model using LinearExplainer, with two stages: conventional SHAP (bar and beeswarm plots) and novel 3D metric-conditioned SHAP analysis linking feature contributions to thresholds and metrics.
- Evaluate four alternative metrics (G-Mean, AUC, Balanced Accuracy, IBA with α=0.1) at fixed threshold 0.5, but exclude them from subsequent robustness, statistical testing, and explainability analysis.

## Software

- Python (version not reported)
- scikit-learn (version not reported)
- XGBoost (version not reported)
- SHAP (version not reported)
- Logistic Regression: max_iter=1000, solver='lbfgs', penalty='l2', C=1.0, random_state=42
- Random Forest: n_estimators=100, max_depth=6, random_state=42
- Decision Tree: max_depth=5, random_state=42
- XGBoost: n_estimators=100, learning_rate=0.1, max_depth=6, subsample=0.8
- k-Nearest Neighbors: n_neighbors=5, weights='uniform', Euclidean distance
- Cross-validation: cv=5, scoring=[accuracy, precision, recall, f1, mcc]
- SHAP: shap.Explainer(model, X_train), explainer(X_test), absolute mean SHAP values per feature
- Bootstrap: 1000 bootstraps
- McNemar's test: exact p-value
- ANOVA: significance level p < 0.05

## Key Findings

- num: Table 5 reports baseline performance: XGB achieved the highest F1-score (0.380) and MCC (0.287), while LR achieved the highest precision (0.657) but low recall (0.197).
- num: Table 6 (5-fold stratified CV) shows RF achieved the highest mean MCC (0.313) and XGB the highest mean F1-score (0.391).
- num: Table 7 shows static threshold analysis: LR best accuracy 0.800 at threshold 0.5; RF precision 1.000 at threshold 0.9; LR recall 0.924 at threshold 0.1.
- num: Table 8 shows dynamic threshold analysis: RF achieved best precision 1.000 at threshold 0.9; XGB best MCC 0.287 at threshold 0.5; LR best F1 0.428.
- num: Table 9 shows alternative metrics: DT highest G-Mean (0.563) and IBA (0.541); RF best AUC (0.681) and Balanced Accuracy (0.595).
- num: Table 10 shows cost-sensitive evaluation: DT lowest ECM (15,000) and highest Net Profit (-15,000); LR highest ECM (18,130).
- num: Table 12 shows ANOVA descriptive statistics: Accuracy mean 0.716 (CV 0.146); F1 mean 0.296 (CV 0.433); MCC mean 0.183 (CV 0.334); Recall mean 0.323 (CV 0.708).
- num: Repeated-measures ANOVA revealed significant main effect of metric: F(4,176) = 77.62, p < 0.001.
- num: Table 14 shows bootstrap CIs: LR Accuracy CI (0.775, 0.825); DT Accuracy CI (0.672, 0.729); XGB MCC CI (0.208, 0.358).
- num: Table 15 shows McNemar's test: LR vs RF p = 0.00024439, Cohen's kappa 0.546; DT vs XGB p = 3.5484e-22, kappa 0.291.
- num: Table 16 (Telco CV) shows XGB highest F1 (0.562) and LR highest accuracy (0.803) but low recall (0.548).
- num: Table 19 shows Telco McNemar's test: XGB vs KNN p = 0.025, Cohen's kappa 0.595.
- The two-stage SHAP framework links feature importance to metric behavior: repayment history (PAY_0, PAY_3, PAY_5) and billing amounts (BILL_AMT1-3, BILL_AMT5) are most influential for credit default.
- F1-score and MCC emerged as the most stable and balanced metrics for business classification under class imbalance.
- Cost-sensitive evaluation revealed that models with higher recall (e.g., DT) achieved lower overall cost despite lower MCC or precision.

## Key Figures and Tables

- Fig. 1 (p. 6): Proposed research framework for selecting the best metric — shows the multi-faceted analytical framework integrating ML, statistical techniques, and XAI.
- Fig. 2 (p. 7): Class distribution with the imbalanced dataset — demonstrates the imbalanced nature of the Default of Credit Card Clients dataset.
- Fig. 3 (p. 14): Proposed stratified 5-fold cross-validation — illustrates the cross-validation process.
- Fig. 4 (p. 19): Experimental design for selecting the best performance metrics — shows the overall experimental flow.
- Fig. 5 (p. 20): Gaussian distribution of the Default of Credit Card Clients dataset for different features — shows distributions of LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE, PAY_0, PAY_2, PAY_3, BILL_ATM1, BILL_ATM2, BILL_ATM4, BILL_ATM6.
- Fig. 6 (p. 22): Baseline performance evaluation for all models across metrics — bar plots for accuracy, precision, recall, F1, and MCC.
- Fig. 7 (p. 24): Cross-validation mean and standard deviation for all models across metrics — error bar plots.
- Fig. 8 (p. 26): Static threshold sensitivity analysis across different metrics — 3D plots showing threshold-performance relationships.
- Fig. 9 (p. 27): Dynamic threshold sensitivity analysis comparison across metrics — 3D visualizations.
- Fig. 10 (p. 30): Noise robustness testing comparison across metrics for all models — trends under noise levels 0.0 to 0.3.
- Fig. 11 (p. 31): Distribution of evaluation metric scores across five classifiers and nine decision thresholds — boxplots.
- Fig. 12 (p. 33): Bootstrap confidence interval comparison for each metric — visualization of CIs.
- Fig. 13 (p. 34): McNemar's test and Cohen's kappa comparisons — visualization.
- Fig. 14 (p. 35): SHAP-based model interpretability for Logistic Regression — (a) global feature importance, (b) beeswarm plot.
- Fig. 15 (p. 36): SHAP feature impact analysis across thresholds — (a) accuracy, (b) precision, (c) recall, (d) F1, (e) MCC.
- Fig. 16 (p. 39): SHAP feature impact analysis across thresholds with the Telco Customer Churn dataset — (a) accuracy, (b) precision, (c) recall, (d) F1, (e) MCC.
- Table 3 (p. 7): Feature summary and descriptions — lists all features, types, and notes for the Default of Credit Card Clients dataset.
- Table 4 (p. 10): Parameter settings for selected models and techniques — provides hyperparameters and settings for reproducibility.
- Table 5 (p. 21): Baseline model performance for each metric — LR, RF, DT, XGB, KNN across accuracy, precision, recall, F1, MCC.
- Table 6 (p. 23): Results with 5-fold stratified cross-validation — mean and std for each metric across models.
- Table 7 (p. 25): Static threshold sensitivity analysis across different metrics — performance metrics across thresholds 0.1-0.9.
- Table 8 (p. 27): Dynamic threshold sensitivity analysis across different metrics — best metric values and optimal thresholds.
- Table 9 (p. 28): Performance of standard and alternative evaluation metrics across models — F1, MCC, G-Mean, AUC, BA, IBA.
- Table 10 (p. 29): Cost-based evaluation of model performance using confusion matrix analysis — TN, FP, FN, TP, TPR, TNR, FPR, FNR, ECM, Net Profit.
- Table 11 (p. 29): Noise robustness testing across metrics — performance under noise levels 0, 0.1, 0.2, 0.3.
- Table 12 (p. 31): Descriptive statistics and significance tests for evaluation metrics across models and thresholds — mean, std, median, IQR, CV.
- Table 13 (p. 32): Pairwise post-hoc comparisons between metrics using repeated-measures ANOVA — t-stat, p-value, Holm-corrected p.
- Table 14 (p. 32): Bootstrap confidence intervals for performance metrics across models — 95% CIs for each metric and model.
- Table 15 (p. 33): Combined results of McNemar's test and Cohen's kappa for model comparisons — p-values and kappa values.
- Table 16 (p. 37): Cross-validation results for the Telco Customer Churn dataset — accuracy, precision, recall, F1, MCC.
- Table 17 (p. 38): Noise robustness testing across metrics for the Telco Customer Churn dataset — performance under noise levels.
- Table 18 (p. 38): Bootstrap confidence intervals with the Telco Customer Churn dataset — 95% CIs for each metric and model.
- Table 19 (p. 38): Results of McNemar's test and Cohen's kappa for pairwise model comparisons on the Telco Customer Churn dataset — p-values and kappa values.

## Limitations and Gaps

- The authors acknowledge that both datasets originate from structured tabular domains, and future research should consider a broader range of dataset sizes, structures, and industries to better assess generalizability (Sect. Limitations, p. 42).
- The authors acknowledge that they did not incorporate deep learning architectures, which may yield different patterns in both performance and explainability (Sect. Limitations, p. 42).
- The authors acknowledge that alternative metrics (AUC, G-Mean, Balanced Accuracy, IBA) were analyzed descriptively and were not subjected to the same level of statistical testing or interpretability analysis (Sect. Limitations, p. 42).
- The authors acknowledge that they did not incorporate other domain-specific constraints such as real-time decision thresholds, risk-based optimization, or adaptive cost matrices (Sect. Limitations, p. 42).
- The authors acknowledge that the study focused on classification-based business predictive modeling, and extending the framework to forecasting, optimization, or recommendation remains an open avenue (Sect. Limitations, p. 42).
- [unacknowledged] The paper's claim that F1-score is "the most stable and balanced" metric is complicated by Table 12, which shows F1-score has a higher coefficient of variation (0.433) than MCC (0.334) and Precision (0.340), suggesting MCC may be more stable in relative terms.
- [unacknowledged] The Telco Customer Churn dataset bootstrap confidence interval for LR MCC is (-0.051, 0.050), which includes zero, indicating non-significant MCC; the paper does not flag this anomaly (Table 18, p. 38).
- [unacknowledged] The paper does not report per-class results or the full confusion matrix for the Telco Customer Churn dataset, limiting assessment of minority-class performance.
- [unacknowledged] The cost-sensitive evaluation uses arbitrary cost values (FP = 10 units, FN = 100 units) without deriving them from domain data or sensitivity analysis (Sect. Cost-sensitive evaluation, p. 12).
- [unacknowledged] The paper does not report hyperparameter tuning results or the search space, only the final settings in Table 4, leaving the tuning process unreproducible.
- [unacknowledged] The study uses a fixed random_state (42) but does not report repeated runs for the main models, leaving variance across random seeds unknown (Table 4, p. 10).
- [unacknowledged] Table 15 lists "RD vs DT" which appears to be a typographical error for "RF vs DT"; the paper does not clarify this (Table 15, p. 33).
- [unacknowledged] The text states DT had the highest initial recall (0.403) but Table 5 reports DT recall as 0.404; the discrepancy is small but unreconciled (Sect. Noise robustness testing, p. 29; Table 5, p. 21).
- [unacknowledged] The paper does not report the class imbalance ratio numerically for the Default of Credit Card Clients dataset, only stating it is imbalanced (Fig. 2, p. 7).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline accuracy, LR | accuracy | 0.800 | — | — | Table 5, p. 21 |
| Baseline precision, LR | precision | 0.657 | — | — | Table 5, p. 21 |
| Baseline recall, LR | recall | 0.197 | — | — | Table 5, p. 21 |
| Baseline F1-score, LR | F1-score | 0.303 | — | — | Table 5, p. 21 |
| Baseline MCC, LR | MCC | 0.280 | — | — | Table 5, p. 21 |
| Baseline accuracy, RF | accuracy | 0.787 | — | — | Table 5, p. 21 |
| Baseline precision, RF | precision | 0.541 | — | — | Table 5, p. 21 |
| Baseline recall, RF | recall | 0.238 | — | — | Table 5, p. 21 |
| Baseline F1-score, RF | F1-score | 0.330 | — | — | Table 5, p. 21 |
| Baseline MCC, RF | MCC | 0.253 | — | — | Table 5, p. 21 |
| Baseline accuracy, DT | accuracy | 0.700 | — | — | Table 5, p. 21 |
| Baseline precision, DT | precision | 0.346 | — | — | Table 5, p. 21 |
| Baseline recall, DT | recall | 0.404 | — | — | Table 5, p. 21 |
| Baseline F1-score, DT | F1-score | 0.373 | — | — | Table 5, p. 21 |
| Baseline MCC, DT | MCC | 0.178 | — | — | Table 5, p. 21 |
| Baseline accuracy, XGB | accuracy | 0.790 | — | — | Table 5, p. 21 |
| Baseline precision, XGB | precision | 0.546 | — | — | Table 5, p. 21 |
| Baseline recall, XGB | recall | 0.291 | — | — | Table 5, p. 21 |
| Baseline F1-score, XGB | F1-score | 0.380 | — | — | Table 5, p. 21 |
| Baseline MCC, XGB | MCC | 0.287 | — | — | Table 5, p. 21 |
| Baseline accuracy, KNN | accuracy | 0.772 | — | — | Table 5, p. 21 |
| Baseline precision, KNN | precision | 0.469 | — | — | Table 5, p. 21 |
| Baseline recall, KNN | recall | 0.238 | — | — | Table 5, p. 21 |
| Baseline F1-score, KNN | F1-score | 0.315 | — | — | Table 5, p. 21 |
| Baseline MCC, KNN | MCC | 0.212 | — | — | Table 5, p. 21 |
| Cross-validated mean accuracy, LR | accuracy (mean) | 0.801 | — | — | Table 6, p. 23 |
| Cross-validated std accuracy, LR | accuracy (std) | 0.006 | — | — | Table 6, p. 23 |
| Cross-validated mean precision, LR | precision (mean) | 0.688 | — | — | Table 6, p. 23 |
| Cross-validated std precision, LR | precision (std) | 0.064 | — | — | Table 6, p. 23 |
| Cross-validated mean recall, LR | recall (mean) | 0.188 | — | — | Table 6, p. 23 |
| Cross-validated std recall, LR | recall (std) | 0.021 | — | — | Table 6, p. 23 |
| Cross-validated mean F1, LR | F1 (mean) | 0.294 | — | — | Table 6, p. 23 |
| Cross-validated std F1, LR | F1 (std) | 0.028 | — | — | Table 6, p. 23 |
| Cross-validated mean MCC, LR | MCC (mean) | 0.284 | — | — | Table 6, p. 23 |
| Cross-validated std MCC, LR | MCC (std) | 0.031 | — | — | Table 6, p. 23 |
| Cross-validated mean accuracy, RF | accuracy (mean) | 0.799 | — | — | Table 6, p. 23 |
| Cross-validated std accuracy, RF | accuracy (std) | 0.006 | — | — | Table 6, p. 23 |
| Cross-validated mean precision, RF | precision (mean) | 0.597 | — | — | Table 6, p. 23 |
| Cross-validated std precision, RF | precision (std) | 0.022 | — | — | Table 6, p. 23 |
| Cross-validated mean recall, RF | recall (mean) | 0.288 | — | — | Table 6, p. 23 |
| Cross-validated std recall, RF | recall (std) | 0.029 | — | — | Table 6, p. 23 |
| Cross-validated mean F1, RF | F1 (mean) | 0.388 | — | — | Table 6, p. 23 |
| Cross-validated std F1, RF | F1 (std) | 0.030 | — | — | Table 6, p. 23 |
| Cross-validated mean MCC, RF | MCC (mean) | 0.313 | — | — | Table 6, p. 23 |
| Cross-validated std MCC, RF | MCC (std) | 0.027 | — | — | Table 6, p. 23 |
| Cross-validated mean accuracy, DT | accuracy (mean) | 0.716 | — | — | Table 6, p. 23 |
| Cross-validated std accuracy, DT | accuracy (std) | 0.015 | — | — | Table 6, p. 23 |
| Cross-validated mean precision, DT | precision (mean) | 0.370 | — | — | Table 6, p. 23 |
| Cross-validated std precision, DT | precision (std) | 0.028 | — | — | Table 6, p. 23 |
| Cross-validated mean recall, DT | recall (mean) | 0.399 | — | — | Table 6, p. 23 |
| Cross-validated std recall, DT | recall (std) | 0.035 | — | — | Table 6, p. 23 |
| Cross-validated mean F1, DT | F1 (mean) | 0.384 | — | — | Table 6, p. 23 |
| Cross-validated std F1, DT | F1 (std) | 0.028 | — | — | Table 6, p. 23 |
| Cross-validated mean MCC, DT | MCC (mean) | 0.200 | — | — | Table 6, p. 23 |
| Cross-validated std MCC, DT | MCC (std) | 0.036 | — | — | Table 6, p. 23 |
| Cross-validated mean accuracy, XGB | accuracy (mean) | 0.785 | — | — | Table 6, p. 23 |
| Cross-validated std accuracy, XGB | accuracy (std) | 0.009 | — | — | Table 6, p. 23 |
| Cross-validated mean precision, XGB | precision (mean) | 0.525 | — | — | Table 6, p. 23 |
| Cross-validated std precision, XGB | precision (std) | 0.032 | — | — | Table 6, p. 23 |
| Cross-validated mean recall, XGB | recall (mean) | 0.312 | — | — | Table 6, p. 23 |
| Cross-validated std recall, XGB | recall (std) | 0.030 | — | — | Table 6, p. 23 |
| Cross-validated mean F1, XGB | F1 (mean) | 0.391 | — | — | Table 6, p. 23 |
| Cross-validated std F1, XGB | F1 (std) | 0.028 | — | — | Table 6, p. 23 |
| Cross-validated mean MCC, XGB | MCC (mean) | 0.285 | — | — | Table 6, p. 23 |
| Cross-validated std MCC, XGB | MCC (std) | 0.030 | — | — | Table 6, p. 23 |
| Cross-validated mean accuracy, KNN | accuracy (mean) | 0.779 | — | — | Table 6, p. 23 |
| Cross-validated std accuracy, KNN | accuracy (std) | 0.008 | — | — | Table 6, p. 23 |
| Cross-validated mean precision, KNN | precision (mean) | 0.498 | — | — | Table 6, p. 23 |
| Cross-validated std precision, KNN | precision (std) | 0.033 | — | — | Table 6, p. 23 |
| Cross-validated mean recall, KNN | recall (mean) | 0.267 | — | — | Table 6, p. 23 |
| Cross-validated std recall, KNN | recall (std) | 0.036 | — | — | Table 6, p. 23 |
| Cross-validated mean F1, KNN | F1 (mean) | 0.347 | — | — | Table 6, p. 23 |
| Cross-validated std F1, KNN | F1 (std) | 0.038 | — | — | Table 6, p. 23 |
| Cross-validated mean MCC, KNN | MCC (mean) | 0.245 | — | — | Table 6, p. 23 |
| Cross-validated std MCC, KNN | MCC (std) | 0.038 | — | — | Table 6, p. 23 |
| Static threshold accuracy, LR at threshold 0.5 | accuracy | 0.800 | — | — | Table 7, p. 25 |
| Static threshold precision, LR at threshold 0.5 | precision | 0.657 | — | — | Table 7, p. 25 |
| Static threshold recall, LR at threshold 0.1 | recall | 0.924 | — | — | Table 7, p. 25 |
| Static threshold F1, LR at threshold 0.3 | F1-score | 0.428 | — | — | Table 7, p. 25 |
| Static threshold MCC, LR at threshold 0.3 | MCC | 0.285 | — | — | Table 7, p. 25 |
| Static threshold precision, RF at threshold 0.9 | precision | 1.000 | — | — | Table 7, p. 25 |
| Static threshold recall, RF at threshold 0.1 | recall | 0.857 | — | — | Table 7, p. 25 |
| Static threshold F1, RF at threshold 0.3 | F1-score | 0.451 | — | — | Table 7, p. 25 |
| Static threshold MCC, RF at threshold 0.4 | MCC | 0.279 | — | — | Table 7, p. 25 |
| Static threshold accuracy, XGB at threshold 0.7 | accuracy | 0.795 | — | — | Table 7, p. 25 |
| Static threshold F1, XGB at threshold 0.1 | F1-score | 0.419 | — | — | Table 7, p. 25 |
| Static threshold MCC, XGB at threshold 0.5 | MCC | 0.287 | — | — | Table 7, p. 25 |
| Static threshold accuracy, KNN at threshold 0.7 | accuracy | 0.790 | — | — | Table 7, p. 25 |
| Static threshold precision, KNN at threshold 0.7 | precision | 0.649 | — | — | Table 7, p. 25 |
| Static threshold recall, KNN at threshold 0.1 | recall | 0.709 | — | — | Table 7, p. 25 |
| Dynamic best accuracy, LR | accuracy | 0.800 | — | — | Table 8, p. 27 |
| Dynamic best precision, LR | precision | 0.700 | — | — | Table 8, p. 27 |
| Dynamic best recall, LR | recall | 0.924 | — | — | Table 8, p. 27 |
| Dynamic best F1, LR | F1-score | 0.428 | — | — | Table 8, p. 27 |
| Dynamic best MCC, LR | MCC | 0.285 | — | — | Table 8, p. 27 |
| Dynamic best accuracy, RF | accuracy | 0.787 | — | — | Table 8, p. 27 |
| Dynamic best precision, RF | precision | 1.000 | — | — | Table 8, p. 27 |
| Dynamic best recall, RF | recall | 0.857 | — | — | Table 8, p. 27 |
| Dynamic best F1, RF | F1-score | 0.451 | — | — | Table 8, p. 27 |
| Dynamic best MCC, RF | MCC | 0.307 | — | — | Table 8, p. 27 |
| Dynamic best accuracy, DT | accuracy | 0.700 | — | — | Table 8, p. 27 |
| Dynamic best precision, DT | precision | 0.346 | — | — | Table 8, p. 27 |
| Dynamic best recall, DT | recall | 0.404 | — | — | Table 8, p. 27 |
| Dynamic best F1, DT | F1-score | 0.373 | — | — | Table 8, p. 27 |
| Dynamic best MCC, DT | MCC | 0.178 | — | — | Table 8, p. 27 |
| Dynamic best accuracy, XGB | accuracy | 0.795 | — | — | Table 8, p. 27 |
| Dynamic best precision, XGB | precision | 0.636 | — | — | Table 8, p. 27 |
| Dynamic best recall, XGB | recall | 0.614 | — | — | Table 8, p. 27 |
| Dynamic best F1, XGB | F1-score | 0.419 | — | — | Table 8, p. 27 |
| Dynamic best MCC, XGB | MCC | 0.287 | — | — | Table 8, p. 27 |
| Dynamic best accuracy, KNN | accuracy | 0.790 | — | — | Table 8, p. 27 |
| Dynamic best precision, KNN | precision | 0.649 | — | — | Table 8, p. 27 |
| Dynamic best recall, KNN | recall | 0.709 | — | — | Table 8, p. 27 |
| Dynamic best F1, KNN | F1-score | 0.385 | — | — | Table 8, p. 27 |
| Dynamic best MCC, KNN | MCC | 0.212 | — | — | Table 8, p. 27 |
| Alternative metric G-Mean, RF | G-Mean | 0.486 | — | — | Table 9, p. 28 |
| Alternative metric AUC, RF | AUC | 0.681 | — | — | Table 9, p. 28 |
| Alternative metric BA, RF | Balanced Accuracy | 0.595 | — | — | Table 9, p. 28 |
| Alternative metric IBA, RF | IBA (α=0.1) | 0.452 | — | — | Table 9, p. 28 |
| Alternative metric G-Mean, XGB | G-Mean | 0.472 | — | — | Table 9, p. 28 |
| Alternative metric AUC, XGB | AUC | 0.665 | — | — | Table 9, p. 28 |
| Alternative metric BA, XGB | Balanced Accuracy | 0.581 | — | — | Table 9, p. 28 |
| Alternative metric IBA, XGB | IBA (α=0.1) | 0.440 | — | — | Table 9, p. 28 |
| Alternative metric G-Mean, LR | G-Mean | 0.438 | — | — | Table 9, p. 28 |
| Alternative metric AUC, LR | AUC | 0.653 | — | — | Table 9, p. 28 |
| Alternative metric BA, LR | Balanced Accuracy | 0.584 | — | — | Table 9, p. 28 |
| Alternative metric IBA, LR | IBA (α=0.1) | 0.404 | — | — | Table 9, p. 28 |
| Alternative metric G-Mean, KNN | G-Mean | 0.469 | — | — | Table 9, p. 28 |
| Alternative metric AUC, KNN | AUC | 0.625 | — | — | Table 9, p. 28 |
| Alternative metric BA, KNN | Balanced Accuracy | 0.581 | — | — | Table 9, p. 28 |
| Alternative metric IBA, KNN | IBA (α=0.1) | 0.436 | — | — | Table 9, p. 28 |
| Alternative metric G-Mean, DT | G-Mean | 0.563 | — | — | Table 9, p. 28 |
| Alternative metric AUC, DT | AUC | 0.594 | — | — | Table 9, p. 28 |
| Alternative metric BA, DT | Balanced Accuracy | 0.594 | — | — | Table 9, p. 28 |
| Alternative metric IBA, DT | IBA (α=0.1) | 0.541 | — | — | Table 9, p. 28 |
| Cost-sensitive ECM, LR | ECM | 18130 | — | — | Table 10, p. 29 |
| Cost-sensitive Net Profit, LR | Net Profit | −18130 | — | — | Table 10, p. 29 |
| Cost-sensitive ECM, RF | ECM | 17180 | — | — | Table 10, p. 29 |
| Cost-sensitive Net Profit, RF | Net Profit | −17180 | — | — | Table 10, p. 29 |
| Cost-sensitive ECM, DT | ECM | 15000 | — | — | Table 10, p. 29 |
| Cost-sensitive Net Profit, DT | Net Profit | −15000 | — | — | Table 10, p. 29 |
| Cost-sensitive ECM, XGB | ECM | 17530 | — | — | Table 10, p. 29 |
| Cost-sensitive Net Profit, XGB | Net Profit | −17530 | — | — | Table 10, p. 29 |
| Cost-sensitive ECM, KNN | ECM | 17600 | — | — | Table 10, p. 29 |
| Cost-sensitive Net Profit, KNN | Net Profit | −17600 | — | — | Table 10, p. 29 |
| Cost-sensitive TP, DT | TP | 90 | — | — | Table 10, p. 29 |
| Cost-sensitive FN, DT | FN | 133 | — | — | Table 10, p. 29 |
| Cost-sensitive FP, DT | FP | 170 | — | — | Table 10, p. 29 |
| Cost-sensitive TN, DT | TN | 617 | — | — | Table 10, p. 29 |
| Cost-sensitive TPR, DT | TPR | 0.404 | — | — | Table 10, p. 29 |
| Cost-sensitive TNR, DT | TNR | 0.784 | — | — | Table 10, p. 29 |
| Noise robustness accuracy, LR at noise 0.0 | accuracy | 0.800 | — | — | Table 11, p. 29 |
| Noise robustness accuracy, RF at noise 0.3 | accuracy | 0.803 | — | — | Table 11, p. 29 |
| Noise robustness precision, LR at noise 0.3 | precision | 0.680 | — | — | Table 11, p. 29 |
| Noise robustness precision, RF at noise 0.3 | precision | 0.622 | — | — | Table 11, p. 29 |
| Noise robustness recall, DT at noise 0.0 | recall | 0.404 | — | — | Table 11, p. 29 |
| Noise robustness F1, RF at noise 0.3 | F1-score | 0.380 | — | — | Table 11, p. 29 |
| Noise robustness MCC, RF at noise 0.3 | MCC | 0.317 | — | — | Table 11, p. 29 |
| Noise robustness MCC, LR at noise 0.0 | MCC | 0.280 | — | — | Table 11, p. 29 |
| Descriptive statistics, Accuracy | mean | 0.716 | — | — | Table 12, p. 31 |
| Descriptive statistics, Accuracy | CV | 0.146 | — | — | Table 12, p. 31 |
| Descriptive statistics, MCC | mean | 0.183 | — | — | Table 12, p. 31 |
| Descriptive statistics, MCC | CV | 0.334 | — | — | Table 12, p. 31 |
| Descriptive statistics, Precision | mean | 0.462 | — | — | Table 12, p. 31 |
| Descriptive statistics, Precision | CV | 0.340 | — | — | Table 12, p. 31 |
| Descriptive statistics, F1-score | mean | 0.296 | — | — | Table 12, p. 31 |
| Descriptive statistics, F1-score | CV | 0.433 | — | — | Table 12, p. 31 |
| Descriptive statistics, Recall | mean | 0.323 | — | — | Table 12, p. 31 |
| Descriptive statistics, Recall | CV | 0.708 | — | — | Table 12, p. 31 |
| ANOVA main effect of metric | F(4,176) | 77.62 | — | <0.001 | Sect. ANOVA, p. 30 |
| Post-hoc Accuracy vs MCC | t-statistic | 34.220 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc Accuracy vs Precision | t-statistic | 15.056 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc Accuracy vs F1 | t-statistic | 14.136 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc Accuracy vs Recall | t-statistic | 8.128 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc MCC vs Precision | t-statistic | −11.227 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc MCC vs F1 | t-statistic | 7.302 | — | <0.0001 | Table 13, p. 32 |
| Post-hoc MCC vs Recall | t-statistic | −4.060 | — | 0.0002 | Table 13, p. 32 |
| Post-hoc Precision vs F1 | t-statistic | −4.213 | — | 0.0001 | Table 13, p. 32 |
| Post-hoc Precision vs Recall | t-statistic | 2.544 | — | 0.0145 | Table 13, p. 32 |
| Post-hoc F1 vs Recall | t-statistic | −1.203 | — | 0.2356 | Table 13, p. 32 |
| Bootstrap CI accuracy, LR | 95% CI | (0.775, 0.825) | (0.775, 0.825) | — | Table 14, p. 32 |
| Bootstrap CI precision, LR | 95% CI | (0.530, 0.768) | (0.530, 0.768) | — | Table 14, p. 32 |
| Bootstrap CI recall, LR | 95% CI | (0.148, 0.252) | (0.148, 0.252) | — | Table 14, p. 32 |
| Bootstrap CI F1, LR | 95% CI | (0.234, 0.371) | (0.234, 0.371) | — | Table 14, p. 32 |
| Bootstrap CI MCC, LR | 95% CI | (0.199, 0.355) | (0.199, 0.355) | — | Table 14, p. 32 |
| Bootstrap CI accuracy, DT | 95% CI | (0.672, 0.729) | (0.672, 0.729) | — | Table 14, p. 32 |
| Bootstrap CI recall, DT | 95% CI | (0.341, 0.465) | (0.341, 0.465) | — | Table 14, p. 32 |
| Bootstrap CI MCC, XGB | 95% CI | (0.208, 0.358) | (0.208, 0.358) | — | Table 14, p. 32 |
| Bootstrap CI accuracy, KNN | 95% CI | (0.745, 0.798) | (0.745, 0.798) | — | Table 14, p. 32 |
| McNemar LR vs RF | p-value | 0.00024439 | — | 0.00024439 | Table 15, p. 33 |
| Cohen's kappa LR vs RF | kappa | 0.546 | — | — | Table 15, p. 33 |
| McNemar RD vs DT | p-value | 3.0985E-32 | — | 3.0985E-32 | Table 15, p. 33 |
| Cohen's kappa RD vs DT | kappa | 0.317 | — | — | Table 15, p. 33 |
| McNemar DT vs XGB | p-value | 3.5484E-22 | — | 3.5484E-22 | Table 15, p. 33 |
| Cohen's kappa DT vs XGB | kappa | 0.291 | — | — | Table 15, p. 33 |
| McNemar XGB vs KNN | p-value | 0.63977 | — | 0.63977 | Table 15, p. 33 |
| Cohen's kappa XGB vs KNN | kappa | 0.444 | — | — | Table 15, p. 33 |
| Telco cross-validated accuracy, LR | accuracy | 0.803 | — | — | Table 16, p. 37 |
| Telco cross-validated precision, LR | precision | 0.654 | — | — | Table 16, p. 37 |
| Telco cross-validated recall, LR | recall | 0.548 | — | — | Table 16, p. 37 |
| Telco cross-validated F1, XGB | F1 | 0.562 | — | — | Table 16, p. 37 |
| Telco cross-validated MCC, LR | MCC | 0.470 | — | — | Table 16, p. 37 |
| Telco noise robustness F1, XGB at noise 0.1 | F1-Score | 0.596 | — | — | Table 17, p. 38 |
| Telco noise robustness MCC, LR at noise 0.1 | MCC | 0.482 | — | — | Table 17, p. 38 |
| Telco noise robustness accuracy, LR at noise 0.1 | Accuracy | 0.805 | — | — | Table 17, p. 38 |
| Telco bootstrap CI MCC, LR | 95% CI | (−0.051, 0.050) | (−0.051, 0.050) | — | Table 18, p. 38 |
| Telco bootstrap CI F1, XGB | 95% CI | (0.214, 0.297) | (0.214, 0.297) | — | Table 18, p. 38 |
| Telco bootstrap CI MCC, XGB | 95% CI | (0.228, 0.355) | (0.228, 0.355) | — | Table 18, p. 38 |
| Telco bootstrap CI accuracy, LR | 95% CI | (0.601, 0.645) | (0.601, 0.645) | — | Table 18, p. 38 |
| Telco McNemar LR vs RF | p-value | 0.101 | — | 0.101 | Table 19, p. 38 |
| Telco Cohen's kappa LR vs RF | kappa | 0.669 | — | — | Table 19, p. 38 |
| Telco McNemar RF vs DT | p-value | 0.000 | — | 0.000 | Table 19, p. 38 |
| Telco Cohen's kappa RF vs DT | kappa | 0.527 | — | — | Table 19, p. 38 |
| Telco McNemar DT vs XGB | p-value | 0.058 | — | 0.058 | Table 19, p. 38 |
| Telco Cohen's kappa DT vs XGB | kappa | 0.528 | — | — | Table 19, p. 38 |
| Telco McNemar XGB vs KNN | p-value | 0.025 | — | 0.025 | Table 19, p. 38 |
| Telco Cohen's kappa XGB vs KNN | kappa | 0.595 | — | — | Table 19, p. 38 |
| Default of Credit Card Clients sample size | instances | 30,000 | — | — | Sect. Data preparation and preprocessing, p. 6 |
| Telco Customer Churn sample size | instances | 7,043 | — | — | Sect. Additional dataset, p. 7 |
| Telco Customer Churn churn rate | proportion | 26.5% | — | — | Sect. Additional dataset, p. 7 |
| Training set proportion | proportion | 80% | — | — | Sect. Dataset splitting, p. 8 |
| Testing set proportion | proportion | 20% | — | — | Sect. Dataset splitting, p. 8 |
| Bootstrap resamples | N | 1000 | — | — | Sect. Bootstrap confidence intervals, p. 15 |
| ANOVA thresholds tested | number | 9 | — | — | Sect. Analysis of variance (ANOVA), p. 14 |
| ANOVA classifiers tested | number | 5 | — | — | Sect. Analysis of variance (ANOVA), p. 14 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Imbalanced datasets pose a persistent challenge in business data mining, particularly in high-stakes domains such as financial risk prediction and customer churn analysis, where the minority class often carries disproportionate operational and financial consequences." | Abstract, p. 1 | model_performance_evaluation |
| "Our findings show that the F1-score consistently provides the most stable and balanced evaluation across datasets and testing conditions, with MCC offering complementary diagnostic value." | Abstract, p. 1 | model_performance_evaluation |
| "In contrast, accuracy and precision demonstrate limited robustness under class imbalance." | Abstract, p. 1 | model_performance_evaluation |
| "MCC is ideal for imbalanced datasets as it accounts for true and false classifications of both classes. Unlike Accuracy, it remains reliable even when class distributions are highly skewed" | Sect. Performance metric evaluation, p. 12 | model_performance_evaluation |
| "The F1-Score offers a single metric that balances precision and recall and provides equal importance to both, making it particularly useful for imbalanced datasets." | Sect. Performance metric evaluation, p. 11 | model_performance_evaluation |
| "Recall is vital when false negatives are costly, such as missing a default customer in credit scoring." | Sect. Performance metric evaluation, p. 11 | model_performance_evaluation |
| "DT achieved the lowest ECM (15,000) and thus the highest Net Profit (–15,000), primarily due to its higher recall (0.404) and lower false negative count (133)." | Sect. Cost-sensitive evaluation, p. 28 | model_performance_evaluation |
| "These findings underscore the importance of aligning metric selection not only with data characteristics but also with domain-specific cost structures." | Discussion, p. 42 | model_performance_evaluation |
| "The bootstrap analysis identified LR and XGB as the most stable models across metrics, with consistently narrow CIs." | Sect. Bootstrap confidence intervals, p. 32 | model_performance_evaluation |
| "This is the first study to jointly analyze performance metrics across statistical, algorithmic, and interpretability dimensions" | Sect. Literature review, p. 6 | model_algorithm_integration |
| "We introduce a novel two-stage explainable AI (XAI) framework using SHAP." | Sect. Introduction, p. 2 | model_algorithm_integration |
| "The first stage applies conventional SHAP plots for global and local interpretability, while the second leverages 3D metric-conditioned SHAP visualizations" | Sect. Introduction, p. 2 | model_algorithm_integration |
| "Accuracy and Precision often failed to yield statistically significant differences between models, underscoring their limited discriminatory power in imbalanced settings" | Discussion, p. 41 | model_performance_evaluation |
| "Our results show that Accuracy and Precision are inadequate in imbalanced contexts, as they favor the majority class and underrepresent minority outcomes." | Conclusion, p. 43 | model_performance_evaluation |
| "The dataset used in this study is the 'Default of Credit Card Clients' dataset collected from UCI Machine Learning, available at the URL1, which consists of 30,000 instances and 23 features." | Sect. Data preparation, p. 6 | data_collection |
| "The second dataset employed in this study is the Telco Customer Churn dataset, sourced from Kaggle ... This dataset comprises 7,043 instances and more than 20 features" | Sect. Additional dataset, p. 7 | data_collection |
| "We performed a 5-fold stratified cross-validation analysis across five metrics: Accuracy, Precision, Recall, F1-Score, and MCC." | Sect. Performance with cross validation, p. 22 | model_development |
| "F1-score and MCC emerged as the most stable and balanced metrics for business classification under class imbalance" | Sect. Metric-conditioned SHAP analysis, p. 35 | model_performance_evaluation |

## Remember This

- The paper evaluates five performance metrics (accuracy, precision, recall, F1, MCC) for imbalanced business classification using two datasets (Default of Credit Card Clients, n=30,000; Telco Customer Churn, n=7,043) and five ML models (LR, RF, DT, XGB, KNN).
- F1-score is concluded to be the most stable and balanced metric, with MCC offering complementary diagnostic value, while accuracy and precision are inadequate under class imbalance.
- A two-stage XAI framework using SHAP is introduced, with 3D metric-conditioned SHAP visualizations linking feature contributions to thresholds and metrics.
- Statistical validation includes repeated-measures ANOVA (F(4,176) = 77.62, p < 0.001), bootstrap CIs (1000 resamples), McNemar's test, and Cohen's kappa.
- Cost-sensitive evaluation (FP cost=10, FN cost=100) shows DT achieves lowest ECM (15,000) due to higher recall (0.404).
- The paper acknowledges limitations including structured tabular datasets only, no deep learning, and alternative metrics analyzed only descriptively.
- [unacknowledged] F1-score has a higher coefficient of variation (0.433) than MCC (0.334) in Table 12, complicating the claim of F1 being most stable.
- [unacknowledged] The Telco LR MCC bootstrap CI (-0.051, 0.050) includes zero, indicating non-significant MCC, which the paper does not flag.

## Cited Works

- Japkowicz, N. (2013) (context) — Assessment metrics for imbalanced learning; foundational work on metric inadequacy under imbalance. [p. 3]
- Ferri, C.; Hernández-Orallo, J.; Modroiu, R. (2009) (context) — Experimental comparison of performance measures for classification; recommends F1 and MCC. [p. 3]
- Boughorbel, S.; Jarray, F.; El-Anbari, M. (2017) (methodology) — Optimal classifier for imbalanced data using MCC; advocates MCC for binary classification. [p. 2]
- Chicco, D.; Jurman, G. (2020) (methodology) — Advantages of MCC over F1 and accuracy in binary classification evaluation. [p. 12]
- Kubat, M. (1997) (context) — One-sided selection for imbalanced training sets. [p. 3]
- Diallo, R.; Edalo, C.; Awe, O.O. (2024) (context) — Machine learning evaluation of imbalanced health data; confirms MCC and F1 stability. [p. 3]
- Öztürk, M.M. (2017) (context) — Metrics for class imbalance in software defect prediction; finds MCC and G-Mean more robust than accuracy. [p. 4]
- Cruz Huayanay, A.; Bazán, J.L.; Russo, C.M. (2025) (context) — Performance of evaluation metrics for classification in imbalanced data; simulation comparison of twelve metrics. [p. 4]
- Wong, T-T.; Chung, P-C. (2025) (context) — Consistency analysis on four evaluation metrics for classifying imbalanced data; theoretical consistency analysis. [p. 4]
- Jiménez-Navarro, M.; Troncoso-García, A.; et al. (2024) (context) — Explainable deep learning with embedded feature selection for electricity demand forecasting. [p. 4]
- Troncoso-Garcia, A.R.; Martinez-Ballesteros, M.; et al. (2025) (context) — Metric based on association rules to assess feature-attribution explainability for time series. [p. 4]
- Troncoso-García, A.; Martínez-Ballesteros, M.; et al. (2022) (context) — Explainable machine learning for sleep apnea prediction using SHAP. [p. 4]
- Kadir, M.A.; Mosavi, A.; Sonntag, D. (2023) (context) — Evaluation metrics for XAI: review, taxonomy, and practical applications. [p. 4]
- Yeh, I-C.; Lien, C-h. (2009) (methodology) — Default of Credit Card Clients dataset from UCI Machine Learning Repository. [p. 20]
- Mahmud Sujon, K.; Binti Hassan, R.; et al. (2024) (methodology) — When to use standardization and normalization: empirical evidence from ML models and XAI. [p. 8]
- Szeghalmy, S.; Fazekas, A. (2023) (methodology) — Comparative study of stratified cross-validation in imbalanced learning. [p. 13]
- Pembury Smith, M.Q.; Ruxton, G.D. (2020) (methodology) — Effective use of the McNemar test. [p. 15]
- Aguirre-Urreta, M.I.; Rönkkö, M. (2018) (methodology) — Statistical inference with PLSc using bootstrap confidence intervals. [p. 15]
- Więckowska, B.; Kubiak, K.B.; et al. (2022) (methodology) — Cohen's kappa coefficient as a measure to assess classification improvement. [p. 15]
- Chen, T.; Guestrin, C. (2016) (methodology) — XGBoost: A scalable tree boosting system. [p. 9]
- Halder, R.K.; Uddin, M.N.; et al. (2024) (methodology) — Enhancing k-nearest neighbor algorithm: comprehensive review. [p. 9]
- Alsulmi, M. (2022) (context) — Rank-based portfolio stock selection. [p. 12]
- Alsubaie, Y.; El Hindi, K.; Alsalman, H. (2019) (context) — Cost-sensitive prediction of stock price direction. [p. 12]
- Foody, G.M. (2023) (context) — Challenges in real-world use of classification accuracy metrics. [p. 41]
- Tang, J.; Li, Y.; et al. (2024) (context) — Robust two-stage instance-level cost-sensitive learning for class imbalance. [p. 41]
- Owusu-Adjei, M.; Hayfron-Acquah, J.B.; et al. (2023) (context) — Imbalanced class distribution and performance evaluation metrics in healthcare systems. [p. 41]
- Wardhani, N.W.S.; Rochayani, M.Y.; et al. (2019) (context) — Cross-validation metrics for evaluating classification performance on imbalanced data. [p. 41]
- Mokhtari, K.E.; Higdon, B.P.; Başar, A. (2019) (context) — Interpreting financial time series with SHAP values. [p. 41]