---
paper_id: A--Shaha-2025
first_author: Shaha
year: 2025
title: "Enhancing Online Fraud Detection: Leveraging Machine Learning and Behavioral Indicators for Improved Accuracy and Real-Time Detection"
venue: "EPJ Web of Conferences"
doi: 10.1051/epjconf/202532801003
designation: algorithm
status: extracted
modules: [model_performance_evaluation, model_algorithm_integration, model_development, data_collection, system_performance_evaluation]
module_rationale:
  model_performance_evaluation: "Table 1, p. 8, reports Accuracy, Precision, Recall, F1-Score, FPR and ROC-AUC for all six classifiers and ranks LightGBM first on ROC-AUC (0.981)."
  model_algorithm_integration: "Sec. 6, p. 8, describes the proposed 'LightGBM-Based Hybrid Approach' that combines engineered behavioural indicators with a LightGBM classifier inside a two-phase framework."
  model_development: "Sec. 5.1.1–5.1.2, pp. 6–7, give the training preparation workflow: normalization, SMOTE oversampling of the training set, an 80/20 stratified split, PCA and Recursive Feature Elimination."
  data_collection: "Sec. 5.1.1, p. 6, names the single data source — the Kaggle Credit Card Fraud Detection Dataset, 284,807 transactions, 492 fraudulent."
  system_performance_evaluation: "Sec. 7.3 and Table 2, p. 10, measure the deployed-model concern: average prediction time per transaction on an Intel i7 CPU with 16 GB RAM."
---

# A--Shaha-2025 — Extraction Note

## Summary

The paper evaluates six machine learning classifiers — Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), Artificial Neural Network (ANN) and LightGBM — for online credit-card fraud detection on the public Kaggle Credit Card Fraud Detection Dataset, and proposes a LightGBM-based hybrid approach that supplements transactional features with engineered behavioural indicators (transaction-frequency behaviour patterns, device and location consistency frequencies, and user interaction time). Across Accuracy, Precision, Recall, F1-Score, False Positive Rate and ROC-AUC, the proposed LightGBM model reports the best value on every metric in Table 1 (Accuracy 0.976, Precision 0.891, Recall 0.914, F1-Score 0.902, FPR 0.006, ROC-AUC 0.981). A second table reports average prediction time per transaction on an Intel i7 CPU with 16 GB RAM, where LightGBM sits at 0.58 ms — slower than Logistic Regression (0.32 ms) and Decision Tree (0.47 ms) but far faster than SVM (3.12 ms) and ANN (5.78 ms). The paper's argument is that behavioural feature engineering, class-imbalance handling through SMOTE, dimensionality reduction through PCA and Recursive Feature Elimination, and the leaf-wise growth of LightGBM together produce a model that is both accurate and fast enough for real-time deployment in banking, e-commerce and fintech platforms.

The paper is a computational benchmark study, not a fielded system: no live fraud-prevention deployment is described, no human participants are involved, and no statistical test statistic or confidence interval is printed anywhere in the text despite an explicit claim of "statistical significance" in the discussion. Its contribution is the comparative ranking of classifiers plus the framing of behavioural indicators as fraud signals.

## Problem and Motivation

Fraud detection is presented as a critical and growing problem in financial security, driven by the expansion of e-commerce and online financial transactions (Sec. 1, p. 1). The paper's stated motivating gap is not the absence of fraud detection but the deficiency profile of existing approaches: traditional systems are rule-based, applying predefined rules such as flagging a transaction above a certain amount or originating from an unfamiliar location, and therefore suffer from static rules, high false-positive rates, and limited scalability in real-time applications (Sec. 1.3, pp. 2–3). The authors argue these systems "cannot adapt to new and emerging fraud tactics without manual updates" and that false positives lead to customer dissatisfaction and revenue loss.

A second motivating gap is that current machine learning models still face unresolved deficiencies: handling imbalanced datasets, adapting to new fraud schemes, and identifying subtle transactional behaviour that could indicate fraud (Sec. 1, p. 2). The stated scope of the study is therefore twofold (Sec. 2, p. 4): assessing the deficiencies of existing fraud detection models, and identifying key transactional behaviour indicators — transaction frequency and user interaction times among them — that can improve detection accuracy. The paper explicitly frames its contribution as offering "a practical, scalable, and high-accuracy ML approach for real-time fraud prevention systems" (Abstract, p. 1).

## Method

**Design.** Computational comparative benchmark study with a proposed model; the authors state no formal design label, describing the work instead as "a systematic approach" divided into "two primary phases: (1) evaluation of current fraud detection models, and (2) development of a hybrid detection framework utilizing behavioral insights and a Light Gradient Boosting Machine (LightGBM) model" (Sec. 4, p. 4).

**Sample.** N = 284,807 credit-card transactions (of which 492 are fraudulent), unit of analysis = one credit-card transaction from European cardholders.

**Context.** geography: European cardholders — the dataset is the Kaggle Credit Card Fraud Detection Dataset; no country or city is stated and no Philippine data are used; population: anonymised credit-card transactions described by features V1–V28 (PCA-derived), Time, Amount, and a binary Class label (0 genuine, 1 fraud); setting: virtual/computational — offline model training and evaluation, with runtime benchmarking on a machine with an Intel i7 CPU and 16 GB RAM (Sec. 7.3, p. 10); no live payment platform, no human participants.

The method proceeds through the following steps as printed:

- Conduct a literature review of prevalent fraud detection methodologies — rule-based systems, statistical approaches, and machine learning models including Decision Trees, Random Forests, SVM, Neural Networks and Logistic Regression — to identify persistent challenges such as high false positive rates, limited adaptability, and poor real-time performance (Sec. 4, p. 4).
- Assess existing models on Accuracy, Precision, Recall, F1-Score and False Positive Rate, with the metric definitions printed as equations (Sec. 5, pp. 5–6).
- Document model weaknesses as: high false positive rates, poor adaptability to new fraud schemes, slow real-time processing of high transaction volumes, and limited feature scope with reliance on basic transactional attributes (Sec. 5, p. 6).
- Take the Kaggle Credit Card Fraud Detection Dataset, described as 284,807 transactions from European cardholders with 492 fraudulent transactions, with features V1–V28 derived via PCA plus Time, Amount and the binary Class label (Sec. 5.1.1, p. 6).
- Select the dataset on the grounds that it is publicly available, highly imbalanced (described as ideal for fraud detection benchmarking), and includes transaction timing and monetary features suitable for behavioural pattern extraction (Sec. 5.1.1, p. 6).
- Normalise features with the min–max formula (Sec. 5.1.1, p. 6).
- Apply SMOTE to the training set only, generating synthetic minority-class examples as X_new = X_i + δ · (X_k − X_i), δ ∈ [0,1], where X_i and X_k are two minority-class samples and δ is a random value (Sec. 5.1.1, p. 6).
- Partition the dataset into 80% training and 20% testing sets using stratified sampling to maintain class proportions (Sec. 5.1.1, p. 6).
- Apply PCA for dimensionality reduction on the anonymised variables, capturing maximum variance, mitigating noise and multicollinearity, and improving training efficiency and interpretability, with Z = X · W where X is the feature matrix and W the matrix of principal components (Sec. 5.1.2, p. 7).
- Apply Recursive Feature Elimination to iteratively remove the least important features based on model performance until an optimal subset is reached, reducing overfitting risk and enhancing generalisation (Sec. 5.1.2, p. 7).
- Extract key transactional indicators: a behavioural pattern term defined as the sum of transactions in a time window divided by the time window; device consistency and location consistency frequencies (freq_D and freq_L) tracking how often device or location changes occur; and user interaction time UT = U_end − U_start (Sec. 5.1.2, p. 8).
- Build the proposed model as a Light Gradient Boosting Machine using leaf-wise tree growth, with native categorical feature support, efficient memory usage, and built-in imbalance handling via the parameter scale_pos_weight (Sec. 6, p. 8).
- Implement five baselines for comparison: Logistic Regression, Decision Trees, Random Forest, SVM and ANN (Sec. 6, p. 8).
- Evaluate the models with metrics including ROC-AUC, test for real-time performance with high transaction volumes, and run a comparative analysis of the impact of the key transactional indicators on model performance (Sec. 6, p. 8).
- Report accuracy, precision, recall, F1-score, false positive rate and ROC-AUC for all six classifiers in Table 1 (Sec. 7.1, p. 8).
- Report average prediction time per transaction for all six models in Table 2 (Sec. 7.3, p. 10).

The paper does not print LightGBM hyperparameter values (no learning rate, number of estimators, number of leaves, max depth, or scale_pos_weight value is given), does not name the software environment or programming language, and does not report cross-validation or a held-out validation split beyond the single 80/20 partition.

## Software

- LightGBM (the proposed classifier; version not reported), selected for leaf-wise tree growth, native categorical feature support, efficient memory usage, and built-in imbalance handling via scale_pos_weight (Sec. 6, p. 8).
- Logistic Regression, Decision Tree, Random Forest, Support Vector Machine and Artificial Neural Network as baseline implementations (Sec. 6, p. 8); library and version Not reported.
- SMOTE (Synthetic Minority Oversampling Technique), applied to the training set only (Sec. 5.1.1, p. 6); implementation and version Not reported.
- Principal Component Analysis (PCA), applied to the anonymised variables (Sec. 5.1.2, p. 7); implementation and version Not reported.
- Recursive Feature Elimination (RFE), used for iterative feature removal (Sec. 5.1.2, p. 7); implementation and version Not reported.
- Runtime environment: Intel i7 CPU, 16 GB RAM (Sec. 7.3, p. 10). Operating system and programming language Not reported.

## Key Findings

- num: Table 1 (p. 8) reports the proposed LightGBM model as best on all six metrics: Accuracy 0.976, Precision 0.891, Recall 0.914, F1-Score 0.902, FPR 0.006, ROC-AUC 0.981.
- num: The weakest baseline, Logistic Regression, reports Accuracy 0.948, Precision 0.723, Recall 0.791, F1-Score 0.755, FPR 0.018, ROC-AUC 0.943 (Table 1, p. 8).
- num: Table 2 (p. 10) reports average prediction time per transaction: Logistic Regression 0.32 ms, Decision Tree 0.47 ms, LightGBM 0.58 ms, Random Forest 1.25 ms, SVM 3.12 ms, ANN 5.78 ms.
- num: The evaluation dataset is described as 284,807 transactions from European cardholders, of which 492 are fraudulent (Sec. 5.1.1, p. 6).
- num: The dataset is partitioned 80% training / 20% testing using stratified sampling (Sec. 5.1.1, p. 6).
- num: Sec. 7.4 (p. 10) restates the proposed model's recall as 91.4% and its F1-score as 90.2%, matching the Table 1 values of 0.914 and 0.902.
- The abstract summarises the result as "highest ROC-AUC (0.981), F1-score (0.902), and lowest false positive rate (0.006)" (Abstract, p. 1).
- The paper attributes the LightGBM advantage to leaf-wise tree growth producing faster convergence and better accuracy than level-wise methods (Sec. 6, p. 8).
- The paper claims behavioural attributes significantly enhanced anomaly detection, arguing that capturing temporal, spatial and interaction-based patterns is a promising direction for fraud analytics (Sec. 7.4, p. 10).
- The paper claims statistical significance for the model improvements without printing a test, a test statistic, or a p-value (Sec. 7.4, p. 10).
- The paper concludes that LightGBM is a "highly efficient and scalable solution for real-time fraud detection" (Sec. 8, p. 11).

## Key Figures and Tables

- Fig. 1 (p. 8): "Comparison of results" — a bar chart of model results accompanying Table 1; the paper refers to it as illustrating the trade-off between True Positive Rate and False Positive Rate for each model (Sec. 7.2, p. 8).
- Fig. 2 (p. 10): "ROC Curve Comparison of Fraud Detection Models" — the ROC curves of the six compared models; the paper states LightGBM yielded the highest ROC-AUC value (0.981), "validating its superior discriminative ability" (Sec. 7.2, p. 8).
- Table 1 (p. 8): "Performance Metrics Comparison Across Models" — six models × six metrics (Accuracy, Precision, Recall, F1-Score, FPR, ROC-AUC); LightGBM best on every column.
- Table 2 (p. 10): "Average Prediction Time Per Transaction" — six models against average prediction time in milliseconds; SVM (3.12 ms) and ANN (5.78 ms) are the slowest, Logistic Regression (0.32 ms) the fastest, LightGBM 0.58 ms.
- The paper contains no other numbered tables and no confusion matrix table, despite listing "a confusion matrix" among the metrics used by a cited related work (Sec. 3, p. 4).

## Limitations and Gaps

- The authors acknowledge that "limitations such as dataset representativeness and model generalizability must be addressed in future work" and that a comparative analysis with state-of-the-art fraud detection methods in real-world financial systems is still needed to validate the approach (Sec. 8, p. 11).
- The authors acknowledge dataset biases as a practical implementation challenge that the research "addressed," but no bias measurement, fairness metric, or per-group result is reported anywhere in the paper (Sec. 8, p. 11).
- [unacknowledged] The paper claims that "the statistical significance of the model improvements reinforces the reliability of findings," yet no significance test, test statistic, p-value, confidence interval, or variance estimate is printed anywhere (Sec. 7.4, p. 10). The claim is unverifiable from the paper's own evidence.
- [unacknowledged] No ablation, no feature-importance ranking, and no before/after comparison is reported for the behavioural indicators. The claim that behavioural attributes "significantly enhanced the model's ability to detect anomalies" (Sec. 7.4, p. 10) is not supported by any table in the paper.
- [unacknowledged] The behavioural indicators the paper defines — behavioural pattern (transactions per time window), device consistency frequency, location consistency frequency, and user interaction time — cannot be computed from the stated dataset features. The Kaggle dataset's inputs are V1–V28 (PCA-anonymised), Time, Amount and Class (Sec. 5.1.1, p. 6); the paper never states where device, location or interaction-time data came from, nor how they were joined to the transactions.
- [unacknowledged] The paper is described as a "hybrid detection framework," but no hybrid architecture is specified beyond the use of LightGBM; there is no ensemble, no stacking, and no second model combined with it.
- [unacknowledged] Table 2's model names and values are printed out of alignment in the source table; the mapping of the four leading values (0.32, 0.47, 1.25, 3.12) to the first four named models is not printed explicitly and has been inferred only from row order.
- [unacknowledged] No LightGBM hyperparameters, no software environment, no random seed, and no cross-validation scheme are reported, so the reported metrics cannot be reproduced.
- [unacknowledged] The dataset is a single European cardholder dataset from a 2015 publication (Dal Pozzolo et al., cited as reference 1); the paper reports no external validation, no second dataset, and no temporal split, so the generalisability claim in Sec. 8 rests on one dataset.
- [unacknowledged] The FPR of 0.006 is reported on a 20% test partition of a dataset with a 492-in-284,807 fraud rate, but the paper reports no confusion matrix, no absolute counts of true positives, false positives, true negatives or false negatives, and no precision–recall curve, so the operating point behind the FPR is unstated.
- [unacknowledged] The paper claims real-time viability from a per-transaction latency benchmark on an Intel i7 CPU with 16 GB RAM but reports no throughput, no memory footprint, and no test under concurrent load.
- [unacknowledged] Section numbering is inconsistent — "5. Evaluation of Current Fraud Detection Techniques" contains "5.1.2. Feature Engineering and Extraction" before "5.1 Identifying and Extracting Key Transactional Behavior Indicators," and "4. Model Testing and Evaluation" appears inside Section 6 (pp. 6–8) — which complicates precise citation of the preprocessing steps.
- [unacknowledged] No comparison is drawn to any published fraud-detection benchmark on the same dataset, so the reported superiority is internal to the six models implemented here.
- [unacknowledged] The study reports no cost analysis, no false-positive operational burden, and no human review workflow, despite framing false positives as the core business problem in Sec. 1.3.

## Definitions

- **LightGBM** — Light Gradient Boosting Machine, a gradient boosting decision tree implementation that employs leaf-wise tree growth, with native categorical feature support, efficient memory usage, and built-in imbalance handling via the parameter scale_pos_weight (Sec. 6, p. 8).
- **Behavioural Patterns (BP)** — Defined as the sum of transactions in a time window divided by the time window (Sec. 5.1.2, p. 8).
- **Device and Location Consistency** — The frequency of device or location changes, tracked as freq_D and freq_L (Sec. 5.1.2, p. 8).
- **User Interaction Time (UT)** — UT = U_end − U_start (Sec. 5.1.2, p. 8).
- **SMOTE** — Synthetic Minority Oversampling Technique, used to generate synthetic examples for the minority (fraudulent) class from the training set (Sec. 5.1.1, p. 6).
- **Recursive Feature Elimination (RFE)** — Iterative removal of the least important features based on model performance until an optimal feature subset is achieved (Sec. 5.1.2, p. 7).
- **False Positive Rate (FPR)** — FPR = FP / (FP + TN) (Sec. 5, p. 6).
- **Class label** — Binary target variable Class, where 0 indicates genuine and 1 indicates fraud (Sec. 5.1.1, p. 6).

## Key Equations

- Accuracy: `A = (TP + TN) / (TP + TN + FP + FN)` — where TP, TN, FP and FN represent True Positives, True Negatives, False Positives and False Negatives respectively (Sec. 5, pp. 5–6).
- Precision: `P = TP / (TP + FP)` (Sec. 5, p. 6).
- Recall: `R = TP / (TP + FN)` (Sec. 5, p. 6).
- F1-Score: `F1 = 2 · (P · R) / (P + R)` (Sec. 5, p. 6).
- False Positive Rate: `FPR = FP / (FP + TN)` (Sec. 5, p. 6).
- Min–max normalization: `X_norm = (X − X_min) / (X_max − X_min)`, where X was a feature and X_min and X_max were its minimum and maximum values respectively (Sec. 5.1.1, p. 6).
- SMOTE synthetic sample: `X_new = X_i + δ · (X_k − X_i), δ ∈ [0,1]`, where X_i and X_k were two samples from the minority class and δ was a random value (Sec. 5.1.1, p. 6).
- PCA projection: `Z = X · W`, where X was the feature matrix and W was the matrix of principal components (Sec. 5.1.2, p. 7).
- Behavioural pattern: `BP = Sum of Transactions in Time Window / Time Window` (Sec. 5.1.2, p. 8).
- User interaction time: `UT = U_end − U_start` (Sec. 5.1.2, p. 8).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fraud detection accuracy, Logistic Regression baseline | accuracy | 0.948 | — | — | Table 1, p. 8 |
| Fraud detection precision, Logistic Regression baseline | precision | 0.723 | — | — | Table 1, p. 8 |
| Fraud detection recall, Logistic Regression baseline | recall | 0.791 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, Logistic Regression baseline | F1-score | 0.755 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, Logistic Regression baseline | FPR | 0.018 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, Logistic Regression baseline | ROC-AUC | 0.943 | — | — | Table 1, p. 8 |
| Fraud detection accuracy, Decision Tree baseline | accuracy | 0.951 | — | — | Table 1, p. 8 |
| Fraud detection precision, Decision Tree baseline | precision | 0.759 | — | — | Table 1, p. 8 |
| Fraud detection recall, Decision Tree baseline | recall | 0.803 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, Decision Tree baseline | F1-score | 0.780 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, Decision Tree baseline | FPR | 0.015 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, Decision Tree baseline | ROC-AUC | 0.949 | — | — | Table 1, p. 8 |
| Fraud detection accuracy, Random Forest baseline | accuracy | 0.967 | — | — | Table 1, p. 8 |
| Fraud detection precision, Random Forest baseline | precision | 0.842 | — | — | Table 1, p. 8 |
| Fraud detection recall, Random Forest baseline | recall | 0.873 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, Random Forest baseline | F1-score | 0.857 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, Random Forest baseline | FPR | 0.010 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, Random Forest baseline | ROC-AUC | 0.970 | — | — | Table 1, p. 8 |
| Fraud detection accuracy, SVM baseline | accuracy | 0.958 | — | — | Table 1, p. 8 |
| Fraud detection precision, SVM baseline | precision | 0.802 | — | — | Table 1, p. 8 |
| Fraud detection recall, SVM baseline | recall | 0.812 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, SVM baseline | F1-score | 0.807 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, SVM baseline | FPR | 0.013 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, SVM baseline | ROC-AUC | 0.958 | — | — | Table 1, p. 8 |
| Fraud detection accuracy, ANN baseline | accuracy | 0.963 | — | — | Table 1, p. 8 |
| Fraud detection precision, ANN baseline | precision | 0.827 | — | — | Table 1, p. 8 |
| Fraud detection recall, ANN baseline | recall | 0.849 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, ANN baseline | F1-score | 0.838 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, ANN baseline | FPR | 0.011 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, ANN baseline | ROC-AUC | 0.965 | — | — | Table 1, p. 8 |
| Fraud detection accuracy, proposed LightGBM | accuracy | 0.976 | — | — | Table 1, p. 8 |
| Fraud detection precision, proposed LightGBM | precision | 0.891 | — | — | Table 1, p. 8 |
| Fraud detection recall, proposed LightGBM | recall | 0.914 | — | — | Table 1, p. 8 |
| Fraud detection F1-score, proposed LightGBM | F1-score | 0.902 | — | — | Table 1, p. 8 |
| Fraud detection false positive rate, proposed LightGBM | FPR | 0.006 | — | — | Table 1, p. 8 |
| Fraud detection ROC-AUC, proposed LightGBM | ROC-AUC | 0.981 | — | — | Table 1, p. 8 |
| Average prediction time per transaction, Logistic Regression | milliseconds | 0.32 | — | — | Table 2, p. 10 |
| Average prediction time per transaction, Decision Tree | milliseconds | 0.47 | — | — | Table 2, p. 10 |
| Average prediction time per transaction, Random Forest | milliseconds | 1.25 | — | — | Table 2, p. 10 |
| Average prediction time per transaction, SVM | milliseconds | 3.12 | — | — | Table 2, p. 10 |
| Average prediction time per transaction, ANN | milliseconds | 5.78 | — | — | Table 2, p. 10 |
| Average prediction time per transaction, LightGBM | milliseconds | 0.58 | — | — | Table 2, p. 10 |
| Recall restated in the discussion for the proposed LightGBM model | recall | 91.4% | — | — | Sec. 7.4, p. 10 |
| F1-score restated in the discussion for the proposed LightGBM model | F1-score | 90.2% | — | — | Sec. 7.4, p. 10 |
| Highest ROC-AUC reported in the abstract for the proposed model | ROC-AUC | 0.981 | — | — | Abstract, p. 1 |
| F1-score reported in the abstract for the proposed model | F1-score | 0.902 | — | — | Abstract, p. 1 |
| Lowest false positive rate reported in the abstract for the proposed model | FPR | 0.006 | — | — | Abstract, p. 1 |
| Total transactions in the evaluation dataset | transactions | 284,807 | — | — | Sec. 5.1.1, p. 6 |
| Fraudulent transactions in the evaluation dataset | transactions | 492 | — | — | Sec. 5.1.1, p. 6 |
| Training partition of the dataset | share of dataset | 80% | — | — | Sec. 5.1.1, p. 6 |
| Testing partition of the dataset | share of dataset | 20% | — | — | Sec. 5.1.1, p. 6 |
| Anonymised PCA-derived input features in the dataset | features | V1–V28 | — | — | Sec. 5.1.1, p. 6 |
| Machine used for the runtime benchmark | CPU and RAM | Intel i7 CPU, 16 GB RAM | — | — | Sec. 7.3, p. 10 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "LightGBM, the proposed model, outperformed other methods, achieving the highest ROC-AUC (0.981), F1-score (0.902), and lowest false positive rate (0.006)." | Abstract, p. 1 | model_performance_evaluation |
| "The dataset used in this study is the Kaggle Credit Card Fraud Detection Dataset [1], which contains 284,807 transactions from European cardholders." | Sec. 5.1.1, p. 6 | data_collection |
| "Among these, 492 transactions are fraudulent, making the dataset highly imbalanced." | Sec. 5.1.1, p. 6 | data_collection |
| "The core model of this study is a Light Gradient Boosting Machine (LightGBM) [3], selected for its high performance in handling large-scale, imbalanced data." | Sec. 6, p. 8 | model_algorithm_integration |
| "It employs leaf-wise tree growth, resulting in faster convergence and better accuracy compared to level-wise methods." | Sec. 6, p. 8 | model_algorithm_integration |
| "Recursive Feature Elimination (RFE) was used to iteratively remove features based on their importance until the optimal set was achieved." | Sec. 5.1.2, p. 7 | model_development |
| "The contribution of behavioral attributes significantly enhanced the model's ability to detect anomalies." | Sec. 7.4, p. 10 | model_algorithm_integration |
| "The statistical significance of the model improvements reinforces the reliability of findings, ensuring the model's superiority is not by chance." | Sec. 7.4, p. 10 | model_performance_evaluation |
| "LightGBM maintained a strong balance between low latency (0.58 ms) and high predictive accuracy, making it well-suited for deployment in real-time fraud detection systems." | Sec. 7.3, p. 10 | system_performance_evaluation |
| "Given its low computational cost and strong performance, LightGBM is ideal for high-volume transactional environments such as banking, e-commerce, and fintech platforms." | Sec. 7.4, p. 10 | system_performance_evaluation |
| "Traditional fraud detection methods, such as rule-based systems, rely heavily on predefined rules and patterns, making them rigid and unable to adapt to the ever-evolving tactics of fraudsters." | Sec. 1.1, p. 2 | rule_based_classification |
| "While this study provides a strong foundation for ML-based fraud detection, limitations such as dataset representativeness and model generalizability must be addressed in future work." | Sec. 8, p. 11 | data_collection |
| "The Synthetic Minority Oversampling Technique (SMOTE) [2] was applied to the training set to generate synthetic examples for the minority (fraudulent) class" | Sec. 5.1.1, p. 6 | model_development |
| "A runtime analysis was conducted to assess the efficiency of each model." | Sec. 7.3, p. 10 | system_performance_evaluation |

## Remember This

- The proposed model is LightGBM inside a two-phase evaluation-then-development framework; the paper gives no architecture beyond the classifier plus engineered behavioural features.
- Six classifiers are compared on the Kaggle Credit Card Fraud Detection Dataset (284,807 transactions, 492 fraudulent, European cardholders).
- LightGBM is reported best on all six metrics in Table 1 (Accuracy 0.976, Precision 0.891, Recall 0.914, F1 0.902, FPR 0.006, ROC-AUC 0.981).
- Table 2 gives average prediction time per transaction: LightGBM 0.58 ms, against 5.78 ms for ANN and 3.12 ms for SVM.
- The paper claims statistical significance without printing a test, a p-value, or a confidence interval anywhere.
- Behavioural indicators (BP, device/location consistency frequency, user interaction time) are defined but cannot be computed from the PCA-anonymised dataset features the paper names, and no ablation isolates their contribution.
- Preprocessing: min–max normalization, SMOTE on the training set, 80/20 stratified split, PCA, RFE.

## Cited Works

- Dal Pozzolo, O. Caelen, Y. Le Borgne, S. Waterschoot, G. Bontempi (2015) (methodology) — Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy, IEEE Transactions on Neural Networks and Learning Systems; the source of the Kaggle dataset used in all experiments. [p. 11]
- Chawla, Bowyer, Hall, Kegelmeyer (2002) (methodology) — SMOTE: Synthetic Minority Over-sampling Technique, Journal of Artificial Intelligence Research 16, pp. 321–357; the oversampling method applied to the training set. [p. 11]
- Ke, Meng, Finley, Wang, Chen, et al. (2017) (methodology) — LightGBM: A Highly Efficient Gradient Boosting Decision Tree, Advances in Neural Information Processing Systems; the proposed model's reference implementation. [p. 11]
- Alatawi, M. N. (2024) (context) — Detection of fraud in IoT-based credit-card collected dataset using machine learning, Machine Learning with Applications; reports improved accuracy, precision, recall and F1 with RF, GBM and MLP. [p. 4]
- Kapadiya, Ramoliya, Gohil, Patel, Gupta, Tanwar, Rodrigues (2024) (context) — Blockchain-assisted healthcare insurance fraud detection framework using ensemble learning, Computers and Electrical Engineering 122; compares ensemble learning with traditional ML algorithms on recall, accuracy, precision, ROC, F1 and confusion matrix. [pp. 4, 11–12]
- Lu, Bhar, Sarkar, Noorwali, Othman (2024) (context) — Enhancing real-time intrusion detection and secure key distribution using a multi-model machine learning approach, Internet of Things 28; uses Max–Min normalization on UNSW-NB15 and CICIoT2023 and PCA for dimensionality reduction. [pp. 4, 12]
- Prasad, Chowdary, Bavitha, Mounisha, Reethika (2023) (baseline) — A Comparison Study of Fraud Detection in Usage of Credit Cards using Machine Learning, ICOEI 2023, pp. 1204–1209. [pp. 4, 12]
- Aggarwal, Sarangi, Sahoo (2023) (baseline) — Credit Card Fraud Detection: Analyzing the Performance of Four Machine Learning Models, ICDT 2023, pp. 650–654. [pp. 4, 12]
- Fiore et al. (2019) (context) — Investigated GANs to enhance classification efficiency in credit-card fraud detection, Information Sciences; GANs as a supplementary dataset-enhancement tool. [p. 4]
- Zhang et al. (2018) (context) — Proposed a CNN-based model for detecting fraudulent activity in online financial transactions. [p. 4]
- Suhas Jain, Rakesh, Pranavi, Bale (2021) (context) — A Novel Approach in Credit Card Fraud Detection System Using Machine Learning Techniques, FABS 2021, pp. 1–5. [p. 12]
- Chaquet-Ulldemolins, Moral-Rubio, Muñoz-Romero (2022) (context) — On the black-box challenge for fraud detection using machine learning (II): nonlinear analysis through interpretable autoencoders, Appl. Sci. 12, 3856. [p. 12]
- Hilal, Gadsden, Yawney (2021) (context) — Financial fraud: a review of anomaly detection techniques and recent advances, Expert Systems with Applications 193. [p. 12]
- Ashtiani, Raahemi (2021) (context) — Intelligent fraud detection in financial statements using machine learning and data mining: a systematic literature review, IEEE Access 10, 72504–72525. [p. 12]
- Al-Hashedi, Magalingam (2021) (context) — Financial fraud detection applying data mining techniques: a comprehensive review from 2009 to 2019, Computer Science Review 40. [p. 12]
- Jayaraman, Alshehri, Kumar, Abugabah, Samant, Mohamed (2023) (context) — Secure biomedical document protection framework to ensure privacy through blockchain, Big Data 11(6), 437–451. [p. 12]
- Rao, Jayaraman (2023) (context) — A Novel Quantum Identity Authentication protocol without entanglement and preserving pre-shared key information, Quantum Information Processing, Springer 22, Article No. 92. [p. 12]
- Faisal, Nahar, Sultana, Mintoo (2024) (context) — Fraud Detection In Banking Leveraging AI To Identify And Prevent Fraudulent Activities In Real-Time, Journal of Machine Learning, Data Engineering and Data Science 1(01), 181–197. [p. 12]
- Oluwole (2024) (context) — 4 African countries with highest scam losses in 2024, Business Insider Africa. [p. 12]
- Sharma, Mehta, Sharma (2024) (context) — Role of artificial intelligence and machine learning in fraud detection and prevention, in Risks and Challenges of AI-Driven Finance: Bias, Ethics, and Security, IGI Global, pp. 90–120. [p. 12]
- Theodorakopoulos, Theodoropoulou, Stamatiou (2024) (context) — A state-of-the-art review in big data management engineering: real-life case studies, challenges, and future research directions, Eng 5(3), 1266–1297. [p. 12]
- Takyar (2024) (context) — Financial fraud detection using machine learning models, LeewayHertz. [p. 12]