---
paper_id: A--Olabintan-2026
first_author: Olabintan
year: 2026
title: "FairLend-Africa: An Explainable Machine Learning Framework for Alternative Credit Scoring Using Behavioral Financial Data in Financially Excluded African Communities"
venue: "Not reported"
doi: Not reported
designation: algorithm
status: extracted
modules: [data_collection, model_development, model_algorithm_integration, model_performance_evaluation, system_development]
module_rationale:
  data_collection: "Sect. 4 Dataset Design describes the synthetic data generation approach, feature design rationale and label generation."
  model_development: "Sect. 5 Feature Engineering and Sect. 7.1 Experimental setup describe the ML pipeline and hyperparameter optimization."
  model_algorithm_integration: "Sect. 6 System Architecture combines XGBoost scoring, SHAP explanation and fairness auditing in a three-tier system."
  model_performance_evaluation: "Sect. 7.2 Model performance and Table 3 report accuracy, precision, recall, F1 and ROC-AUC for four configurations."
  system_development: "Sect. 6 System Architecture describes the FastAPI API tier, React dashboard and PostgreSQL logging."
---

## Summary

FairLend-Africa is an explainable machine learning framework for alternative credit scoring that combines XGBoost scoring with SHAP interpretability and systematic fairness auditing, evaluated on a synthetic dataset of 10,000 borrower records generated to reflect African mobile money behavioral patterns. The tuned XGBoost model achieves a held-out test ROC-AUC of 0.7137, but a logistic regression baseline matches it (0.713), suggesting primarily linear structure in the synthetic data. The framework is implemented as a REST API with an interactive dashboard released as open source. The authors frame the contribution as methodological rather than empirical, presenting the framework explicitly as infrastructure for future empirical work rather than as evidence of real-world credit scoring capability.

## Problem and Motivation

Access to formal credit remains constrained for much of the African population due to a lack of conventional credit histories (Abstract, p. 1). Conventional credit scoring systems rely on records of prior formal borrowing, repayment behavior and account standing, and produce either a null score or a rejection by default for individuals who have never held a formal bank account, regardless of actual financial behavior or repayment capacity (Sect. 1, p. 1). Mobile money services generate transaction records that capture income frequency, expenditure patterns, savings behavior and network activity, but their integration into formal credit assessment frameworks remains limited, particularly in contexts where explainability and fairness are simultaneously required (Sect. 1, p. 2). The requirement for explainability in credit decisions is both regulatory and ethical: the European Union's GDPR Article 22 establishes a right to explanation for automated decisions, and equivalent frameworks are emerging in several African jurisdictions (Sect. 2.4, p. 3). Algorithmic fairness in lending has received substantial research attention following evidence that machine learning models can perpetuate or amplify historical discrimination (Sect. 2.5, p. 3).

## Method

**Design.** Computational method-development study with comparative benchmark evaluation against three model configurations (majority class baseline, logistic regression, baseline XGBoost, tuned XGBoost); the authors state no formal design label.
**Sample.** n = 10,000 synthetic borrower records (80% training = 8,000; 20% test = 2,000; one record per borrower).
**Context.** geography: Sub-Saharan Africa (synthetic data designed to reflect African mobile money behavioral patterns); population: synthetic borrowers with mobile money, airtime, savings, credit-history, social, payment and loan-request features; setting: computational/offline — Python scikit-learn pipeline with XGBoost, SHAP and a FastAPI/React/PostgreSQL deployment stack; no real borrower data or live lending platform was involved.

- Generate a synthetic dataset of 10,000 borrower records with 16 raw behavioral features across seven domains: mobile money, airtime, savings, credit history, social, payments and loan request (Table 1, p. 5).
- Generate the binary repayment label via a logistic data generating process with literature-calibrated coefficients: wallet_balance_trend +0.8, prior_loan_repayment_rate +0.9, has_savings_account +0.7, savings_consistency_score +0.6, monthly_txn_count +0.5, airtime_recharge_freq +0.4, bill_payment_regularity +0.3, network_diversity_score +0.2, days_late_avg -0.6, loan_amount_requested_usd -0.4, intercept 0.0 and noise σ=0.3 (Table 2, p. 6).
- Engineer three composite features: transaction intensity = log(1+monthly_txn_count) × log(1+avg_txn_amount_usd), savings commitment ratio = monthly_savings_usd/(avg_txn_amount_usd+1), and airtime stability = airtime_avg_amount/(airtime_recharge_freq+1); add a binary no_prior_loan_flag as the fourth engineered feature (Sect. 5, p. 7).
- Handle missing values (prior_loan_repayment_rate and days_late_avg missing for 5,503 borrowers = 55.03%) via median imputation within the sklearn pipeline after train/test splitting, with the no_prior_loan_flag partially compensating (Sect. 4.4, p. 7).
- Split the dataset 80/20 with stratified sampling: 8,000 training and 2,000 test records (Sect. 7.1, p. 9).
- Train an XGBoost classifier with hyperparameter optimization via RandomizedSearchCV over 30 iterations with 5-fold stratified cross-validation, optimizing ROC-AUC (Sect. 7.1, p. 9).
- Compare four configurations: majority class baseline, logistic regression, baseline XGBoost and tuned XGBoost (Table 3, p. 9).
- Generate post-hoc explanations with SHAP TreeExplainer using a 500-sample training background, reporting mean absolute SHAP values in log-odds space (Sect. 7.3, p. 12; Sect. 7.4, p. 15).
- Audit fairness with three criteria — demographic parity, equal opportunity and predictive parity — using the 80% rule as a disparity threshold (Sect. 8.1, p. 17).
- Evaluate selection rate disparity ratios at four operating thresholds: 0.621 (30% approval), 0.509 (50%), 0.433 (70%) and 0.151 (100%) (Table 6, p. 18).
- Compute Pearson correlations between the five highest-impact behavioral features and demographic group encodings to test for proxy relationships (Sect. 8.3, p. 19).
- Deploy as a three-tier system: Python/scikit-learn/XGBoost model tier with joblib serialization, FastAPI API tier with three endpoints, and React dashboard with three views (Sect. 6, p. 8).

## Software

- Python (version not reported)
- scikit-learn (Pedregosa et al., 2011; version not reported)
- XGBoost (Chen and Guestrin, 2016; version not reported)
- SHAP (Lundberg and Lee, 2017; version not reported)
- FastAPI (version not reported)
- React (version not reported)
- PostgreSQL (version not reported)
- joblib (version not reported)
- RandomizedSearchCV (scikit-learn)
- XGBoost hyperparameters (Table A1, p. 22): learning_rate 0.05, max_depth 4, n_estimators 250, subsample 0.8, colsample_bytree 0.7, min_child_weight 5, scale_pos_weight 3.1

## Key Findings

- num: The tuned XGBoost model achieves a held-out test ROC-AUC of 0.7137, a 5.7 percent relative improvement over the baseline XGBoost (0.675) (Sect. 7.2, p. 10).
- num: Logistic regression matches the tuned XGBoost (ROC-AUC 0.713 vs 0.714), a difference of 0.001 that is within the bootstrap confidence interval width of both models and should not be interpreted as meaningful (Sect. 7.2, p. 9).
- num: The tuned XGBoost achieves lower overall accuracy (0.620) than the baseline XGBoost (0.664) and the majority class baseline (0.755), reflecting the low optimal threshold of 0.151 (Sect. 7.2, p. 10).
- num: Wallet balance trend dominates all other features by a factor of 1.74 times the second-ranked feature (mean |SHAP| 0.3767 vs 0.2162) (Table 4, p. 12; Sect. 7.3, p. 13).
- num: A feature ablation study shows the full 20-feature set and the 16 raw features alone both achieve ROC-AUC 0.714, with ΔAUC = -0.0002 (Sect. 7.3, p. 13; Sect. 9.2, p. 21).
- num: The maximum absolute Pearson correlation between the five highest-impact behavioral features and demographic group encodings is 0.054 (Sect. 8.3, p. 19).
- num: All fairness disparity ratios exceed 0.80, with the most constrained operating point (30% approval) producing the lowest observed ratio of 0.818 (West Africa, regional) (Table 6, p. 18).
- The authors state that the contribution is methodological rather than empirical (Sect. 10, p. 22).
- The system is deployable on free-tier cloud infrastructure (Render or Railway for the API, Vercel for the frontend) without requiring institutional cloud resources (Sect. 6, p. 9).
- SHAP analysis identifies wallet balance trend and savings consistency as dominant signals under the synthetic data generating process (Abstract, p. 1).
- Loan request features (loan_amount_requested_usd, loan_duration_weeks) rank among the lowest-importance features, indicating that the model learned to predict repayment primarily from how borrowers manage money daily rather than from the characteristics of the loan being requested (Sect. 7.3, p. 13).
- The engineered composite features provide no measurable improvement in predictive performance on this dataset (Sect. 7.3, p. 13).

## Key Figures and Tables

- Table 1 (p. 5): Raw behavioral features — 16 features across 7 domains (Mobile money, Airtime, Savings, Credit history, Social, Payments, Loan request).
- Figure 1 (p. 5): Feature distributions by repayment outcome — overlapping histograms show visible separation between repayers (green) and defaulters (red) across key behavioral features.
- Table 2 (p. 6): Data generating process coefficients — wallet_balance_trend +0.8, prior_loan_repayment_rate +0.9, has_savings_account +0.7, savings_consistency_score +0.6, monthly_txn_count +0.5, airtime_recharge_freq +0.4, bill_payment_regularity +0.3, network_diversity_score +0.2, days_late_avg -0.6, loan_amount_requested_usd -0.4, intercept 0.0, noise σ=0.3.
- Figure 2 (p. 6): Class distribution of the repayment label — 7,553 repayers (75.53%) and 2,447 defaulters (24.47%).
- Figure 3 (p. 8): Pearson correlation matrix across all features and the repayment label.
- Table 3 (p. 9): Model comparison test set performance (95% bootstrap CI, n=1000) — four configurations with accuracy, precision, recall, F1, ROC-AUC and threshold.
- Figure 4 (p. 11): ROC curve on held-out test set (n=2,000) — tuned XGBoost AUC = 0.7137.
- Figure 5 (p. 11): Confusion matrix on held-out test set.
- Figure 6 (p. 12): Performance comparison across three model configurations.
- Table 4 (p. 12): Top 5 features by mean absolute SHAP value — wallet_balance_trend 0.3767, savings_consistency_score 0.2162, monthly_savings_usd 0.1255, has_savings_account 0.0554, txn_intensity 0.0348.
- Figure 7 (p. 13): Global feature importance measured by mean absolute SHAP value across all 2,000 test borrowers.
- Figure 8 (p. 14): SHAP beeswarm plot.
- Figure 9 (p. 15): SHAP dependence plots for the four highest-importance features.
- Figure 10a/b/c (pp. 15-16): Local SHAP explanations — high-confidence repayer, high-confidence defaulter, borderline borrower.
- Table 5 (p. 17): Fairness disparity ratios by demographic group — selection rate, TPR and precision for seven groups.
- Table 6 (p. 18): Selection rate disparity ratios across operating thresholds — threshold, approval rate, region disparity, gender disparity and worst group.
- Figure 11 (p. 19): Demographic parity analysis.
- Figure 12 (p. 19): Equal opportunity analysis.
- Figure 13 (p. 20): ROC-AUC by demographic group.
- Table A1 (p. 22): Optimized XGBoost hyperparameters.

## Limitations and Gaps

- The authors acknowledge the dataset is synthetic and cannot capture the full complexity of real mobile money data, including temporal dynamics, seasonal patterns and network effects; validation on real transaction data from a partner institution remains necessary (Sect. 9.2, p. 21).
- The authors acknowledge the feature set is constructed from literature-informed assumptions rather than empirical feature selection from real behavioral data; relative feature importance may differ substantially across populations, geographies and mobile money platforms (Sect. 9.2, p. 21).
- The authors acknowledge the fairness analysis is constrained by the synthetic data's designed independence between demographics and behavior; real-world fairness properties cannot be inferred from this analysis (Sect. 9.2, p. 21).
- The authors acknowledge the system has not been evaluated for temporal stability; a production system would require ongoing monitoring and retraining (Sect. 9.2, p. 21).
- The authors acknowledge the near-identical performance of logistic regression (ROC-AUC: 0.713) and tuned XGBoost (ROC-AUC: 0.714) suggests primarily linear structure in the synthetic dataset, limiting the external validity of the SHAP non-linearity analysis (Sect. 9.2, p. 21).
- The authors acknowledge the engineered composite features provided no measurable improvement over the 16 raw features in the ablation study (ΔAUC = -0.0002) (Sect. 9.2, p. 21).
- The authors acknowledge SHAP explanations can be manipulated to conceal systematic bias while producing plausible-looking explanations (Slack et al., 2020); SHAP explanations should be treated as decision-support tools subject to auditing rather than as definitive proofs of model behavior (Sect. 9.2, p. 21).
- The authors acknowledge TreeExplainer assumes feature independence when computing conditional expectations; in the presence of correlated features, SHAP values may distribute credit erroneously across correlated predictors (Sect. 9.2, p. 21).
- The authors acknowledge median imputation assumes Missing At Random (MAR), which is technically inconsistent with the MNAR mechanism identified for prior loan history features; median imputation on MNAR data likely biases coefficient estimates toward zero, attenuating the predictive contribution of prior loan history features (Sect. 4.4, p. 7).
- [unacknowledged] The paper reports a tuned XGBoost ROC-AUC of 0.7137 in the Abstract and in the text of Sect. 7.2, but Table 3 prints 0.714; the text also says the tuned model achieves 0.714 and logistic regression 0.713. These are the same value to three decimal places but the fourth decimal (0.7137) appears only in the Abstract and text, not in the table.
- [unacknowledged] The near-universal selection rate at the optimal threshold (0.151) means the fairness analysis is evaluating a near-trivial condition; the authors themselves note "When all borrowers are approved, demographic parity is automatically satisfied" (Sect. 7.2, p. 10), but the reported fairness results in Table 5 are all 1.000 for selection rate and TPR, which limits their informativeness.
- [unacknowledged] The tuned XGBoost's accuracy (0.620) is below the majority class baseline (0.755) and below the baseline XGBoost (0.664); the authors attribute this to the low threshold but do not explore institution-specific cost ratios, noting only that "Practitioners should recalibrate this threshold using institution-specific cost ratios before deployment" (Sect. 7.2, p. 10).
- [unacknowledged] No precision, recall or F1 confidence intervals are reported for the logistic regression and baseline XGBoost, with the note stating they are "omitted for brevity" (Table 3, p. 9).
- [unacknowledged] The paper does not report per-group ROC-AUC values, only stating that all groups exceed the random baseline (0.5) and demonstrate consistent discrimination ability (Figure 13, p. 20).
- [unacknowledged] The paper evaluates only three fairness criteria and notes that satisfying all simultaneously is mathematically impossible when base rates differ across groups (Chouldechova, 2017), but the synthetic data's designed demographic-behavioral independence means base rates do not differ, so the impossibility theorem is not exercised.
- [unacknowledged] The paper does not report calibration metrics for the tuned XGBoost, despite noting that "uncalibrated tree-based ensembles often generate biased probability distributions compared to generalized linear models" (Sect. 7.2, p. 9).

## Definitions

- **FairLend-Africa** — The paper's proposed explainable machine learning framework for alternative credit scoring, combining XGBoost scoring with SHAP interpretability and systematic fairness auditing.
- **Alternative credit scoring** — Credit assessment using behavioral financial data (mobile money transactions, airtime patterns, savings consistency) instead of conventional bureau-based credit histories.
- **SHAP (SHapley Additive exPlanations)** — A unified framework for model explanation grounded in cooperative game theory; SHAP values satisfy local accuracy, missingness and consistency axioms.
- **XGBoost** — Gradient boosted tree classifier used as the primary prediction model.
- **Demographic parity** — Equal positive prediction rates across groups, assessed via selection rate disparity ratios.
- **Equal opportunity** — Equal true positive rates across groups, ensuring that creditworthy borrowers have equal probability of approval regardless of demographic membership.
- **Predictive parity** — Equal precision across groups, ensuring that approved borrowers in each group have equal likelihood of actually repaying.
- **80 percent rule** — A disparity threshold below 0.80 is considered a meaningful fairness violation; adopted from the United States Equal Credit Opportunity Act as an international baseline indicator.
- **MNAR (Missing Not At Random)** — Missingness mechanism where the absence of a value is itself informative, as with prior_loan_repayment_rate and days_late_avg for first-time borrowers.
- **txn_intensity** — Engineered composite feature defined as log(1+monthly_txn_count) × log(1+avg_txn_amount_usd).
- **savings_commitment_ratio** — Engineered composite feature defined as monthly_savings_usd / (avg_txn_amount_usd + 1).
- **airtime_stability** — Engineered composite feature defined as airtime_avg_amount / (airtime_recharge_freq + 1).
- **no_prior_loan_flag** — Binary missingness indicator added as the fourth engineered feature, preserving structural information in the missingness pattern for borrowers with no prior loan history.
- **SHAP base rate** — The model's expected value under the SHAP background distribution (500-sample training background used for TreeExplainer), which differs from the empirical repayment rate of 75.53%.

## Key Equations

- `txn_intensity = log(1 + monthly_txn_count) × log(1 + avg_txn_amount_usd)` — Transaction intensity composite feature.
- `savings_commitment_ratio = monthly_savings_usd / (avg_txn_amount_usd + 1)` — Savings commitment ratio composite feature.
- `airtime_stability = airtime_avg_amount / (airtime_recharge_freq + 1)` — Airtime stability composite feature.
- `f(x_i) = ∅_0 + Σ_{j=1}^{p} ∅_{ij}` — SHAP explanation decomposition, where ∅_0 is the base rate and ∅_{ij} is the contribution of feature j (Sect. 3, p. 4).
- The data generating process is a logistic function with coefficients from Table 2 and noise ε ~ N(0, 0.3) added to the log-odds before applying the sigmoid (Table 2, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Tuned XGBoost ROC-AUC on held-out test set | ROC-AUC | 0.7137 | — | — | Abstract, p. 1 |
| Tuned XGBoost ROC-AUC on held-out test set | ROC-AUC | 0.714 | [0.688, 0.739] | — | Table 3, p. 9 |
| Logistic regression ROC-AUC on held-out test set | ROC-AUC | 0.713 | [0.688, 0.738] | — | Table 3, p. 9 |
| Baseline XGBoost ROC-AUC on held-out test set | ROC-AUC | 0.675 | — | — | Table 3, p. 9 |
| Majority class baseline ROC-AUC | ROC-AUC | 0.500 | — | — | Table 3, p. 9 |
| Majority class baseline accuracy | accuracy | 0.755 | — | — | Table 3, p. 9 |
| Logistic regression accuracy | accuracy | 0.760 | — | — | Table 3, p. 9 |
| Baseline XGBoost accuracy | accuracy | 0.664 | — | — | Table 3, p. 9 |
| Tuned XGBoost accuracy | accuracy | 0.620 | — | — | Table 3, p. 9 |
| Logistic regression precision | precision | 0.770 | — | — | Table 3, p. 9 |
| Baseline XGBoost precision | precision | 0.824 | — | — | Table 3, p. 9 |
| Tuned XGBoost precision | precision | 0.862 | [0.841, 0.883] | — | Table 3, p. 9 |
| Logistic regression recall | recall | 0.960 | — | — | Table 3, p. 9 |
| Baseline XGBoost recall | recall | 0.706 | — | — | Table 3, p. 9 |
| Tuned XGBoost recall | recall | 0.600 | [0.574, 0.625] | — | Table 3, p. 9 |
| Logistic regression F1 | F1 | 0.860 | — | — | Table 3, p. 9 |
| Baseline XGBoost F1 | F1 | 0.760 | — | — | Table 3, p. 9 |
| Tuned XGBoost F1 | F1 | 0.707 | [0.686, 0.727] | — | Table 3, p. 9 |
| Optimal classification threshold for tuned XGBoost | threshold | 0.151 | — | — | Table 3, p. 9; Sect. 7.2, p. 10 |
| Relative improvement of tuned XGBoost over baseline XGBoost | relative improvement | 5.7% | — | — | Sect. 7.2, p. 10 |
| Dataset size | records | 10,000 | — | — | Sect. 4.5, p. 7 |
| Repayers in dataset | proportion | 75.53% | — | — | Fig. 2, p. 6 |
| Defaulters in dataset | proportion | 24.47% | — | — | Fig. 2, p. 6 |
| Repayers in dataset | count | 7,553 | — | — | Fig. 2, p. 6 |
| Defaulters in dataset | count | 2,447 | — | — | Fig. 2, p. 6 |
| Missing prior loan history | proportion | 55.03% | — | — | Sect. 4.4, p. 7 |
| Missing prior loan history | count | 5,503 | — | — | Sect. 4.4, p. 7 |
| Training records | records | 8,000 | — | — | Sect. 7.1, p. 9 |
| Test records | records | 2,000 | — | — | Sect. 7.1, p. 9 |
| Wallet balance trend mean absolute SHAP value | mean \|SHAP\| | 0.3767 | — | — | Table 4, p. 12 |
| Savings consistency score mean absolute SHAP value | mean \|SHAP\| | 0.2162 | — | — | Table 4, p. 12 |
| Monthly savings USD mean absolute SHAP value | mean \|SHAP\| | 0.1255 | — | — | Table 4, p. 12 |
| Has savings account mean absolute SHAP value | mean \|SHAP\| | 0.0554 | — | — | Table 4, p. 12 |
| txn_intensity mean absolute SHAP value | mean \|SHAP\| | 0.0348 | — | — | Table 4, p. 12 |
| Wallet balance trend dominance over second-ranked feature | ratio | 1.74 | — | — | Sect. 7.3, p. 13 |
| Feature ablation, full 20-feature set | ROC-AUC | 0.714 | — | — | Sect. 7.3, p. 13 |
| Feature ablation, 16 raw features alone | ROC-AUC | 0.714 | — | — | Sect. 7.3, p. 13 |
| Feature ablation delta | ΔAUC | -0.0002 | — | — | Sect. 9.2, p. 21 |
| Maximum absolute correlation between top features and demographic encodings | Pearson correlation | 0.054 | — | — | Sect. 8.3, p. 19 |
| West Africa selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| East Africa selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| Southern Africa selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| Central Africa selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| Female selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| Male selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| Prefer not to say selection rate disparity | selection rate | 1.000 | — | — | Table 5, p. 17 |
| West Africa TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| East Africa TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| Southern Africa TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| Central Africa TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| Female TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| Male TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| Prefer not to say TPR | TPR | 1.000 | — | — | Table 5, p. 17 |
| West Africa precision | precision | 0.990 | — | — | Table 5, p. 17 |
| East Africa precision | precision | 0.959 | — | — | Table 5, p. 17 |
| Southern Africa precision | precision | 1.000 | — | — | Table 5, p. 17 |
| Central Africa precision | precision | 0.989 | — | — | Table 5, p. 17 |
| Female precision | precision | 1.000 | — | — | Table 5, p. 17 |
| Male precision | precision | 0.977 | — | — | Table 5, p. 17 |
| Prefer not to say precision | precision | 0.989 | — | — | Table 5, p. 17 |
| Threshold 0.621, 30% approval, region disparity | disparity ratio | 0.818 | — | — | Table 6, p. 18 |
| Threshold 0.621, 30% approval, gender disparity | disparity ratio | 0.932 | — | — | Table 6, p. 18 |
| Threshold 0.509, 50% approval, region disparity | disparity ratio | 0.811 | — | — | Table 6, p. 18 |
| Threshold 0.509, 50% approval, gender disparity | disparity ratio | 0.947 | — | — | Table 6, p. 18 |
| Threshold 0.433, 70% approval, region disparity | disparity ratio | 0.903 | — | — | Table 6, p. 18 |
| Threshold 0.433, 70% approval, gender disparity | disparity ratio | 0.978 | — | — | Table 6, p. 18 |
| Threshold 0.151, 100% approval, region disparity | disparity ratio | 1.000 | — | — | Table 6, p. 18 |
| Threshold 0.151, 100% approval, gender disparity | disparity ratio | 1.000 | — | — | Table 6, p. 18 |
| SHAP base rate | base rate | 0.64 | — | — | Sect. 7.4, p. 15 |
| SHAP background sample size | samples | 500 | — | — | Sect. 7.4, p. 15 |
| Hyperparameter optimization iterations | iterations | 30 | — | — | Sect. 7.1, p. 9 |
| Hyperparameter optimization cross-validation folds | folds | 5 | — | — | Sect. 7.1, p. 9 |
| Wallet balance trend DGP coefficient | coefficient | +0.8 | — | — | Table 2, p. 6 |
| prior_loan_repayment_rate DGP coefficient | coefficient | +0.9 | — | — | Table 2, p. 6 |
| has_savings_account DGP coefficient | coefficient | +0.7 | — | — | Table 2, p. 6 |
| savings_consistency_score DGP coefficient | coefficient | +0.6 | — | — | Table 2, p. 6 |
| monthly_txn_count DGP coefficient | coefficient | +0.5 | — | — | Table 2, p. 6 |
| airtime_recharge_freq DGP coefficient | coefficient | +0.4 | — | — | Table 2, p. 6 |
| bill_payment_regularity DGP coefficient | coefficient | +0.3 | — | — | Table 2, p. 6 |
| network_diversity_score DGP coefficient | coefficient | +0.2 | — | — | Table 2, p. 6 |
| days_late_avg DGP coefficient | coefficient | -0.6 | — | — | Table 2, p. 6 |
| loan_amount_requested_usd DGP coefficient | coefficient | -0.4 | — | — | Table 2, p. 6 |
| Intercept DGP coefficient | coefficient | 0.0 | — | — | Table 2, p. 6 |
| Noise term σ | standard deviation | 0.3 | — | — | Table 2, p. 6 |
| learning_rate | hyperparameter | 0.05 | — | — | Table A1, p. 22 |
| max_depth | hyperparameter | 4 | — | — | Table A1, p. 22 |
| n_estimators | hyperparameter | 250 | — | — | Table A1, p. 22 |
| subsample | hyperparameter | 0.8 | — | — | Table A1, p. 22 |
| colsample_bytree | hyperparameter | 0.7 | — | — | Table A1, p. 22 |
| min_child_weight | hyperparameter | 5 | — | — | Table A1, p. 22 |
| scale_pos_weight | hyperparameter | 3.1 | — | — | Table A1, p. 22 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "We present FairLend-Africa, an explainable machine learning framework combining XGBoost scoring with SHAP interpretability and systematic fairness auditing." | Abstract, p. 1 | model_algorithm_integration |
| "Using a synthetic dataset of 10,000 borrower records, the system achieves a held-out test ROC-AUC of 0.7137." | Abstract, p. 1 | model_performance_evaluation |
| "A logistic regression baseline matches the XGBoost performance, suggesting primarily linear structures in the synthetic data and motivating validation on real-world datasets where non-linear interactions may emerge." | Abstract, p. 1 | model_performance_evaluation |
| "This paper is a methodological demonstration rather than an empirical study of real African borrower behavior." | Sect. 1, p. 2 | data_collection |
| "All results predictive performance, feature importance rankings, and fairness audit outcomes are properties of the synthetic data generating process and the proposed framework applied to it." | Sect. 1, p. 2 | data_collection |
| "The dataset was split into 80 percent training (8,000 records) and 20 percent test (2,000 records) using stratified sampling to preserve the class ratio." | Sect. 7.1, p. 9 | model_development |
| "The tuned model achieves a ROC-AUC of 0.7137, representing a 5.7 percent relative improvement over the baseline." | Sect. 7.2, p. 10 | model_performance_evaluation |
| "The low optimal threshold of 0.151 reflects the class imbalance correction applied during tuning rather than an explicit cost-benefit specification." | Sect. 7.2, p. 10 | model_development |
| "wallet_balance_trend dominates all other features by a factor of 1.74 times the second-ranked feature, confirming the theoretical expectation that balance trajectory is the strongest behavioral creditworthiness signal." | Sect. 7.3, p. 13 | model_development |
| "The engineered composite features (transaction intensity, savings commitment ratio, airtime stability) provided no measurable improvement over the 16 raw features in the ablation study (ΔAUC = -0.0002)." | Sect. 9.2, p. 21 | model_development |
| "All disparity ratios exceed 0.80 across all groups and all criteria." | Sect. 8.2, p. 17 | model_performance_evaluation |
| "The maximum absolute correlation observed was 0.054 across all feature-group pairs, indicating no meaningful proxy relationships." | Sect. 8.3, p. 19 | model_performance_evaluation |
| "The synthetic data generating process explicitly constructed demographic attributes to be uncorrelated with behavioral features a condition that may not hold in real-world data." | Sect. 8.4, p. 20 | data_collection |
| "The system is deployable on free-tier cloud infrastructure (Render or Railway for the API, Vercel for the frontend) without requiring institutional cloud resources." | Sect. 6, p. 9 | system_development |
| "The contribution of this work is methodological rather than empirical: we demonstrate that the combination of alternative behavioral data, gradient boosted trees, post-hoc explainability, and structured fairness auditing can be implemented as a coherent, reproducible, and deployable system." | Sect. 10, p. 22 | model_algorithm_integration |
| "TreeExplainer provides exact Shapley values relative to the tree ensemble's output, it assumes feature independence when computing conditional expectations." | Sect. 9.2, p. 21 | model_algorithm_integration |

## Remember This

- FairLend-Africa combines XGBoost scoring, SHAP interpretability and fairness auditing for alternative credit scoring on African mobile money behavioral data.
- Evaluation uses a synthetic dataset of 10,000 borrower records (80/20 split: 8,000 training, 2,000 test) and achieves a held-out test ROC-AUC of 0.7137.
- Logistic regression (0.713) matches tuned XGBoost (0.714), suggesting primarily linear structure in the synthetic data.
- The tuned XGBoost's accuracy (0.620) is below both the baseline XGBoost (0.664) and the majority class baseline (0.755), reflecting the low optimal threshold of 0.151.
- Wallet balance trend is the dominant SHAP feature (mean |SHAP| 0.3767), 1.74× the second-ranked feature.
- The engineered composite features provide no measurable improvement over the 16 raw features (ΔAUC = -0.0002).
- All fairness disparity ratios exceed 0.80, but this is partly because the tuned threshold approves nearly all borrowers.
- The paper explicitly frames the contribution as methodological rather than empirical; no real borrower data or live lending platform was involved.

## Cited Works

- Demirgüç-Kunt, A., Klapper, L., Singer, D., and Ansar, S. (2022) (context) — The Global Findex Database 2021, World Bank; 1.4 billion adults unbanked, Sub-Saharan Africa disproportionately represented. [p. 1]
- GSMA (2023) (context) — The State of Mobile Money in Sub-Saharan Africa; mobile money systems generate transaction records. [p. 1]
- Björkegren, D. and Grissen, D. (2018) (baseline) — Mobile phone metadata predicts loan repayment in Rwanda, AUC approximately 0.70. [p. 2, p. 3]
- Suri, T. and Jack, W. (2016) (context) — M-Pesa adoption welfare effects in Kenya. [p. 2, p. 3]
- Khandani, A. E., Kim, A. J., and Lo, A. W. (2010) (baseline) — Consumer transaction data credit scores with AUC 0.68–0.72. [p. 3]
- Agarwal, S., Amromin, G., Ben-David, I., Chomsisengphet, S., and Evanoff, D. D. (2020) (context) — Fintech lending in India improved inclusion for thin-file borrowers. [p. 3]
- Lauer, K. and Lyman, T. (2015) (context) — Digital financial inclusion; transaction frequency and regularity as actionable behavioral signals. [p. 3]
- Baesens, B., Van Gestel, T., Viaene, S., Stepanova, M., Suykens, J., and Vanthienen, J. (2003) (baseline) — Benchmarking classification algorithms for credit scoring. [p. 3]
- Chen, T. and Guestrin, C. (2016) (methodology) — XGBoost scalable tree boosting system. [p. 3]
- Lundberg, S. M. and Lee, S. I. (2017) (methodology) — SHAP unified framework for model explanation. [p. 3]
- Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., and Lee, S. I. (2020) (methodology) — Explainable AI for trees. [p. 3]
- Ribeiro, M. T., Singh, S., and Guestrin, C. (2016) (context) — LIME local explanation method. [p. 3]
- Slack, D., Hilgard, S., Jia, E., Singh, S., and Lakkaraju, H. (2020) (context) — Fooling LIME and SHAP: adversarial attacks on post hoc explanation methods. [p. 3]
- Barocas, S. and Hardt, M. (2017) (context) — Fairness in machine learning. [p. 3]
- Chouldechova, A. (2017) (context) — Impossibility theorem. [p. 3]
- Fuster, A., Goldsmith-Pinkham, P., Ramadorai, T., and Walther, A. (2022) (context) — Predictably unequal? Effects of ML on credit markets. [p. 3]
- Kozodoi, N., Jacob, J., and Lessmann, S. (2022) (context) — Fairness in credit scoring. [p. 4]
- Blattner, L. and Nelson, S. (2021) (context) — How Costly is Noise? Data and Disparate Algorithms in Consumer Credit. [p. 4]
- Jordon, J., Szpruch, L., Houssiau, F., Bottarelli, M., Cherubin, G., Maple, C., Cohen, S. N., and Weller, A. (2022) (methodology) — Synthetic data what, why and how? [p. 4]
- Ledgerwood, J. (1999) (context) — Microfinance Handbook. [p. 2]
- Totolo, E. (2018) (context) — Kenya's Digital Credit Revolution: Five Years On. [p. 2]
- Chiteli, N. (2013) (context) — Agent banking operations as competitive strategy. [p. 2]
- Greenleaf, G. (2021) (context) — Global Data Privacy Laws 2021. [p. 4]
- Dwork, C., Hardt, M., Pitassi, T., Reingold, O., and Zemel, R. (2012) (methodology) — Fairness through awareness. [p. 17]
- Hardt, M., Price, E., and Srebro, N. (2016) (methodology) — Equality of opportunity in supervised learning. [p. 17]
- Corbett-Davies, S., Pierson, E., Feller, A., Goel, S., and Huq, A. (2017) (context) — Algorithmic decision making and the cost of fairness. [p. 18]
- Kusner, M. J., Loftus, J., Russell, C., and Silva, R. (2017) (context) — Counterfactual fairness. [p. 21]
- Niculescu-Mizil, A. and Caruana, R. (2005) (context) — Predicting good probabilities with supervised learning. [p. 9]
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., and others (2011) (methodology) — Scikit-learn: Machine learning in Python. [p. 8]
- van Buuren, S. (2018) (methodology) — Flexible Imputation of Missing Data. [p. 7]
- Zhang, Y. and Long, J. (2021) (context) — Fairness-aware learning with missing attributes. [p. 18]