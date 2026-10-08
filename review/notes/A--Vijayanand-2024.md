---
paper_id: A--Vijayanand-2024
first_author: Vijayanand
year: 2024
title: "Explainable AI - enhanced ensemble learning for financial fraud detection in mobile money transactions"
venue: "Intelligent Decision Technologies"
doi: 10.1177/18724981241289751
designation: algorithm
status: extracted
modules: [data_collection, model_algorithm_integration, model_performance_evaluation, rule_based_classification]
module_rationale:
  data_collection: "Sect 3.1 (p. 56) documents the PaySim synthetic mobile money dataset and its 6,362,620 records, the sole source of development and evaluation data."
  model_algorithm_integration: "Sect 4 and Fig. 5 (pp. 61-62) build a Voting Classifier over XGBoost, LightGBM, Neural Network, Decision Tree and Random Forest, with SHAP layered on top."
  model_performance_evaluation: "Tables 3-9 (pp. 60-62) report accuracy, F1 and ROC AUC under stratified five-fold cross-validation for all six models and the ensemble."
  rule_based_classification: "Sect 3.3.2 (p. 59) specifies the Decision Tree classifier used in the comparison, a branch-and-split if-then partitioner over single attribute values."
---

# A--Vijayanand-2024 — Extraction Note

## Summary

The paper builds an ensemble fraud detector for mobile money transactions by stacking a soft-voting classifier over XGBoost, LightGBM, a Neural Network, a Decision Tree and a Random Forest, then opening the resulting black box with SHAP (SHapley Additive exPlanations). Evaluation is run on the synthetic PaySim dataset of 6,362,620 records, of which 8213 (0.13%) are fraudulent. Six individual models are compared on accuracy, F1 and ROC AUC under stratified five-fold cross-validation, and the Voting Classifier is reported at 99.904% accuracy, an F1 of 0.814 and a ROC AUC of 0.990. SHAP attribute-level analysis is presented as the interpretability contribution, with OldBalanceOrg carrying the largest mean SHAP value (0.065).

## Problem and Motivation

Digital banking has expanded the volume and speed of financial transactions while also expanding the fraud surface. The paper opens with figures it attributes to external sources: ACFE puts worldwide fraud losses at 5% of yearly income; Statista projects global digital payment transactions at US$16.62tn by 2028; cybercrime cost is projected at US$10.5 Trillion annually by 2025; financial institutions are estimated to lose $4.23 for every dollar lost to fraud in 2022; and 70% of financial institutions reported using machine learning for fraud detection as of 2020 (Sect 1, p. 52).

The motivating problem is twofold. First, fraud schemes now use machine learning to evade detection, so static rules and traditional methods lag. Second, the machine learning models that are adopted are usually opaque "black-box" entities, which undermines stakeholder trust and creates regulatory problems where explainability is mandatory. The authors tie this to GDPR- and PSD2-driven accountability and transparency requirements for data processing and decisions (Sect 1, p. 52). Their stated aim is therefore to combine ensemble machine learning with explainable AI so that a fraud detector can be simultaneously accurate and interpretable, and to "provide a safe space for digital finance by bridging the gap between precision and interpretability" (Abstract, p. 52).

The literature survey (Sect 2, pp. 53-54) reviews work on bank fraud, insurance fraud, financial statement fraud and cryptocurrency fraud, and notes that SVM is the most-used data-mining method (23% of uses in one review of 34 methods), followed by Naive Bayes and Random Forest at 15% each. It flags prior calls for ensemble methods, unsupervised and semi-supervised approaches, GAN- and autoencoder-based feature extraction, CNN/LSTM temporal modelling, and the pairing of federated learning with explainable AI as an open direction. The paper positions itself in the last of these gaps: transparency plus accuracy.

## Method

**Design.** Computational model-development and comparative benchmark study on a single synthetic dataset; the authors state no formal design label.
**Sample.** n = 6,362,620 mobile money transactions (PaySim synthetic records: 6,354,407 valid, 8213 fraudulent; 16 flagged), one record per transaction.
**Context.** geography: Not reported for the transaction data (the underlying logs come from a multinational mobile banking provider operating in more than 14 countries; the authors are based in Chennai, India); population: mobile money transactions of types TRANSFER, CASH_OUT, CASH_IN, DEBIT and PAYMENT; setting: Virtual/computational — offline simulation and model comparison on the PaySim dataset; no live payment platform, no human participants.

- Ingest the PaySim synthetic transaction log and drop rows with missing values in the target variable `isFraud` (Sect 3.1, p. 56; Sect 3.2, p. 58).
- Profile the data visually: a pie chart of transaction-type shares, a bar chart of total value by type, and a bar chart of fraudulent-incidence by type (Figs. 2-4, pp. 57-58).
- Rectify disparities in origin and destination balances after each transaction, and examine transactions with amounts less than or equal to zero as candidate anomalies (Sect 3.1, p. 58).
- Feature-engineer from the 11 original columns (`step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `oldbalanceDest`, `newbalanceDest`, `isFraud`, `isFlaggedFraud`), then remove `step`, `type`, `nameOrig`, `nameDest`, `error_orig`, `error_dest` and `isFlaggedFraud` (Sect 3.2, p. 58).
- Standardise `amount`, `oldbalanceOrg`, `oldbalanceDest`, `newbalanceOrig` and `newbalanceDest` to the 0-to-1 range with StandardScaler (Sect 3.2, p. 58).
- Split with `train_test_split` at a 20% test size, preserving stratification, and verify the resulting dimensions (Sect 3.2, p. 58).
- Train and compare six classifiers — Logistic Regression, Decision Tree, Random Forest, XGBoost, LightGBM and Neural Network — on accuracy, F1, confusion matrix and ROC AUC (Sect 3.3, p. 59; Table 6, p. 61).
- Validate with stratified K-Fold cross-validation and compare models statistically with Friedman's test plus a Nemenyi post-hoc pairwise test (Sect 3.3.6, p. 60; Table 7, p. 61).
- Build a meta-classifier Voting Classifier that merges the base models' outputs, using soft voting over class pseudo-probabilities to pick the most likely class (Sect 4, p. 61; Fig. 5, p. 62).
- Interpret the resulting model with SHAP, treated as a "feature attribution method" that assigns per-attribute importance values to each prediction, and report mean SHAP values per attribute (Sect 5, pp. 62-63; Table 10, p. 63).

## Software

- PaySim — financial mobile money simulator used to generate the dataset; version Not reported (Sect 3.1, p. 56)
- StandardScaler — feature scaling; version Not reported (Sect 3.2, p. 58)
- XGBoost — Extreme Gradient Boosting implementation; version Not reported (Sect 3.3.4, p. 59)
- LightGBM — histogram-based gradient boosting framework; version Not reported (Sect 3.3.5, p. 60)
- SHAP — SHapley Additive exPlanations, used as the explainability layer; version Not reported (Sect 5, p. 62)
- Voting Classifier — soft-voting meta-classifier over the base learners; version Not reported (Sect 4, p. 61)

## Key Findings

- The Voting Classifier ensemble reports 99.904% accuracy, an F1 of 0.814 and a ROC AUC of 0.990 (Table 9, p. 62).
- The Decision Tree is the strongest single model on accuracy and F1: 99.937% accuracy, F1 0.893 and ROC AUC 0.943 (Table 6, p. 61). Its accuracy is higher than the ensemble's 99.904%.
- Random Forest has the highest ROC AUC of any model at 0.996, above the ensemble's 0.990 (Table 6, p. 61; Table 9, p. 62).
- LightGBM is the weakest model on every averaged metric: 99.753% accuracy, F1 0.507 and ROC AUC 0.641 (Table 6, p. 61).
- Accuracy is uniformly high (99.75%-99.94%) while F1 varies widely (0.507-0.893), so the headline accuracy figure is largely a reflection of the 0.13% positive rate (Tables 3-6, pp. 60-61).
- Friedman's test yields p = 0.000139, below the 0.05 significance level, so the models differ significantly; Nemenyi pairwise comparisons localise the significant differences to Logistic Regression, Decision Trees, Random Forest and LightGBM (Sect 3.3.6, p. 60; Table 7, p. 61).
- SHAP ranks OldBalanceOrg (0.065) as the most influential attribute, followed by NewBalanceOrg (0.055), Amount (0.04), NewBlanceDest (0.03) and OldBalanceDest (0.03) (Table 10, p. 63).
- The dataset is severely imbalanced: 6,354,407 valid transactions (99.87%) against 8213 fraudulent transactions (0.13%), with all 16 flagged transactions belonging to the TRANSFER type (Sect 3.1, p. 56).

## Key Figures and Tables

- Fig. 1 (p. 56): Architecture of the proposed methodology — dataset ingestion, preprocessing, feature engineering, model training and SHAP explanation form one pipeline.
- Fig. 2 (p. 57): Pie chart of ratio of transaction types — Transfer transactions 19%, Cash Out transactions 81%.
- Fig. 3 (p. 57): Total amount transacted in each transaction type — Cash Out 394,412,995,224; Transfer 485,291,987,263.
- Fig. 4 (p. 58): Fraudulent transactions types — cash out and transfer; Cash Out 223,750 instances, Transfer 532,909 instances.
- Fig. 5 (p. 62): Proposed ensemble model — the Voting Classifier sits over XGBoost, LightGBM, Neural Network, Decision Tree and Random Forest.
- Fig. 6 (p. 62): Process of explainable AI — application domain and requirements determine input data, the prediction approach, and the XAI methods and explanation interface.
- Fig. 7 (p. 63): Mean SHAP value — average impact of each attribute on model output, OldBalanceOrg highest.
- Fig. 8 (p. 64): SHAP value and feature value — the distribution of SHAP values against attribute magnitude.
- Table 1 (p. 55): Comparative analysis of various research works (rendered as a rotated/garbled character-level grid in the source conversion) — prior work spans ML and deep learning algorithms for financial fraud detection.
- Table 2 (p. 59): Detailed information of the dataset attributes — 11 attributes with descriptions and dtypes (`step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `oldbalanceDest`, `newbalanceDest`, `isFraud`, `isFlaggedFraud`).
- Table 3 (p. 60): Cross-validation results on accuracy (%) for six models across five folds.
- Table 4 (p. 60): Cross-validation results on F1 scores for six models across five folds.
- Table 5 (p. 60): Cross-validation results on ROC AUC scores for six models across five folds.
- Table 6 (p. 61): Performance metrics of classification machine learning models — averaged accuracy, F1 and ROC AUC per model.
- Table 7 (p. 61): Nemenyi post-hoc test results — a 6×6 symmetric p-value matrix with 0-5 row and column indices; the model names behind the indices are not printed.
- Table 8 (p. 61): Cross-validation results of the ensemble learning classifier — accuracy, F1 and ROC AUC across five folds.
- Table 9 (p. 62): Performance measure of the ensemble learning classifier — 99.904% accuracy, 0.814 F1, 0.990 ROC AUC.
- Table 10 (p. 63): Average impact of attributes on model output — mean SHAP values for the five retained continuous attributes.

## Definitions

- **Voting Classifier** — Meta-classifier that merges prediction models from different or comparable machine learning datasets by majority vote or soft voting; the paper uses soft voting, which averages the base models' class pseudo-probabilities (Sect 4, p. 61).
- **SHAP (SHapley Additive exPlanations)** — A feature attribution method, analogous to a game-theory approach, that assigns each attribute an importance value for an individual prediction; it is model-agnostic and provides both local and global explanations (Sect 5, p. 63).
- **Mean SHAP value** — The average impact of an attribute on model output, reported in Table 10 (p. 63).
- **PaySim** — A simulator that generates synthetic mobile money transactions from a subset of real transactions extracted from a provider's monthly financial data (Sect 3.1, p. 56).
- **`isFraud`** — Binary indicator (1 or 0) marking transactions carried out by fraudulent agents in the simulation (Table 2, p. 59).
- **`isFlaggedFraud`** — Signal that suggests an attempt to send more than $200,000 in a single transaction (Table 2, p. 59).
- **`step`** — A real-world time measure where one step is equivalent to one hour (Table 2, p. 59).
- **Financial fraud (paper's definition)** — Acting to "intentionally and knowingly deceive the victim by misrepresenting, concealing, or omitting facts about promised goods, services, or other benefits and consequences that are nonexistent, unnecessary, never intended to be provided, or deliberately distorted for the purpose of monetary gain" (Sect 3, p. 54).
- **Mobile money** — Monetary services and transactions that may be carried out via a mobile device, such as a phone or tablet, without necessarily connecting to a bank account (Sect 3, p. 54).
- **Explainable AI (XAI)** — Term coined by DARPA in 2016 to address the need for transparency in AI systems and to counter the "black box" nature of machine learning (Sect 5, p. 62).
- **STRATIFIED K-FOLD cross-validation** — The resampling scheme used to assess reliability and robustness of the experiments (Sect 3.3.6, p. 60).

## Key Equations

- `S(x) = 1 ÷ (1 + e^(−x))` — the nonlinear sigmoidal function applied to a linear combination of features in Logistic Regression (Equation 1, Sect 3.3.1, p. 59).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Background: worldwide fraud losses as share of yearly income (cited to ACFE) | share of yearly income | 5% | — | — | Sect 1, p. 52 |
| Background: projected global digital payment transactions by 2028 (cited to Statista) | value | US$16.62tn | — | — | Sect 1, p. 52 |
| Background: projected annual cybercrime cost by 2025 | value | US$10.5 Trillion | — | — | Sect 1, p. 52 |
| Background: estimated loss per dollar lost to fraud in 2022 | loss ratio | $4.23 | — | — | Sect 1, p. 52 |
| Background: financial institutions reporting machine learning use for fraud detection as of 2020 | share of institutions | 70% | — | — | Sect 1, p. 52 |
| Dataset composition, total records | records | 6,362,620 | — | — | Sect 3.1, p. 56 |
| Dataset composition, valid transactions | records and share | 6,354,407 (99.87%) | — | — | Sect 3.1, p. 56 |
| Dataset composition, fraudulent transactions | records and share | 8213 (0.13%) | — | — | Sect 3.1, p. 56 |
| Dataset composition, flagged transactions | records | 16 | — | — | Sect 3.1, p. 56 |
| Flagged transaction amount range | local currency | 353,874.22 to 10,000,000.0 | — | — | Sect 3.1, p. 56 |
| Transaction type share, Transfer | share | 19% | — | — | Fig. 2, p. 57 |
| Transaction type share, Cash Out | share | 81% | — | — | Fig. 2, p. 57 |
| Total amount transacted, Cash Out | total amount | 394,412,995,224 | — | — | Fig. 3, p. 57 |
| Total amount transacted, Transfer | total amount | 485,291,987,263 | — | — | Fig. 3, p. 57 |
| Fraudulent-incidence by type, Cash Out (as labelled in the paper) | instances | 223,750 | — | — | Fig. 4, p. 58 |
| Fraudulent-incidence by type, Transfer (as labelled in the paper) | instances | 532,909 | — | — | Fig. 4, p. 58 |
| Cross-validated accuracy, Logistic Regression (folds 1-5) | accuracy (%) | 99.82, 99.83, 99.81, 99.82, 99.83 | — | — | Table 3, p. 60 |
| Cross-validated accuracy, Decision Tree (folds 1-5) | accuracy (%) | 99.94, 99.93, 99.94, 99.93, 99.94 | — | — | Table 3, p. 60 |
| Cross-validated accuracy, Random Forest (folds 1-5) | accuracy (%) | 99.92, 99.92, 99.92, 99.93, 99.92 | — | — | Table 3, p. 60 |
| Cross-validated accuracy, XGBoost (folds 1-5) | accuracy (%) | 99.91, 99.90, 99.91, 99.90, 99.92 | — | — | Table 3, p. 60 |
| Cross-validated accuracy, LightGBM (folds 1-5) | accuracy (%) | 99.75, 99.75, 99.75, 99.76, 99.76 | — | — | Table 3, p. 60 |
| Cross-validated accuracy, Neural Network (folds 1-5) | accuracy (%) | 99.86, 99.85, 99.85, 99.87, 99.85 | — | — | Table 3, p. 60 |
| Cross-validated F1, Logistic Regression (folds 1-5) | F1 score | 0.60, 0.62, 0.61, 0.60, 0.60 | — | — | Table 4, p. 60 |
| Cross-validated F1, Decision Tree (folds 1-5) | F1 score | 0.89, 0.90, 0.89, 0.90, 0.89 | — | — | Table 4, p. 60 |
| Cross-validated F1, Random Forest (folds 1-5) | F1 score | 0.86, 0.85, 0.85, 0.85, 0.86 | — | — | Table 4, p. 60 |
| Cross-validated F1, XGBoost (folds 1-5) | F1 score | 0.83, 0.83, 0.82, 0.83, 0.83 | — | — | Table 4, p. 60 |
| Cross-validated F1, LightGBM (folds 1-5) | F1 score | 0.51, 0.50, 0.51, 0.50, 0.50 | — | — | Table 4, p. 60 |
| Cross-validated F1, Neural Network (folds 1-5) | F1 score | 0.68, 0.68, 0.69, 0.68, 0.68 | — | — | Table 4, p. 60 |
| Cross-validated ROC AUC, Logistic Regression (folds 1-5) | ROC AUC | 0.98, 0.98, 0.97, 0.98, 0.98 | — | — | Table 5, p. 60 |
| Cross-validated ROC AUC, Decision Tree (folds 1-5) | ROC AUC | 0.94, 0.94, 0.94, 0.94, 0.94 | — | — | Table 5, p. 60 |
| Cross-validated ROC AUC, Random Forest (folds 1-5) | ROC AUC | 0.99, 0.99, 0.99, 0.99, 0.99 | — | — | Table 5, p. 60 |
| Cross-validated ROC AUC, XGBoost (folds 1-5) | ROC AUC | 0.99, 0.99, 0.99, 0.99, 0.99 | — | — | Table 5, p. 60 |
| Cross-validated ROC AUC, LightGBM (folds 1-5) | ROC AUC | 0.64, 0.64, 0.64, 0.64, 0.65 | — | — | Table 5, p. 60 |
| Cross-validated ROC AUC, Neural Network (folds 1-5) | ROC AUC | 0.98, 0.98, 0.98, 0.98, 0.98 | — | — | Table 5, p. 60 |
| Logistic Regression, averaged performance | accuracy (%) | 99.826 | — | — | Table 6, p. 61 |
| Logistic Regression, averaged performance | F1 score | 0.606 | — | — | Table 6, p. 61 |
| Logistic Regression, averaged performance | ROC AUC | 0.978 | — | — | Table 6, p. 61 |
| Decision Tree, averaged performance | accuracy (%) | 99.937 | — | — | Table 6, p. 61 |
| Decision Tree, averaged performance | F1 score | 0.893 | — | — | Table 6, p. 61 |
| Decision Tree, averaged performance | ROC AUC | 0.943 | — | — | Table 6, p. 61 |
| Random Forest, averaged performance | accuracy (%) | 99.922 | — | — | Table 6, p. 61 |
| Random Forest, averaged performance | F1 score | 0.855 | — | — | Table 6, p. 61 |
| Random Forest, averaged performance | ROC AUC | 0.996 | — | — | Table 6, p. 61 |
| XGBoost, averaged performance | accuracy (%) | 99.908 | — | — | Table 6, p. 61 |
| XGBoost, averaged performance | F1 score | 0.829 | — | — | Table 6, p. 61 |
| XGBoost, averaged performance | ROC AUC | 0.990 | — | — | Table 6, p. 61 |
| LightGBM, averaged performance | accuracy (%) | 99.753 | — | — | Table 6, p. 61 |
| LightGBM, averaged performance | F1 score | 0.507 | — | — | Table 6, p. 61 |
| LightGBM, averaged performance | ROC AUC | 0.641 | — | — | Table 6, p. 61 |
| Neural Network, averaged performance | accuracy (%) | 99.855 | — | — | Table 6, p. 61 |
| Neural Network, averaged performance | F1 score | 0.682 | — | — | Table 6, p. 61 |
| Neural Network, averaged performance | ROC AUC | 0.983 | — | — | Table 6, p. 61 |
| Nemenyi post-hoc, row 0 vs column 1 | p-value | 0.009434 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 0 vs column 2 | p-value | 0.114066 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 0 vs column 3 | p-value | 0.532706 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 0 vs column 4 | p-value | 0.900000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 0 vs column 5 | p-value | 0.900000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 1 vs column 2 | p-value | 0.900000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 1 vs column 3 | p-value | 0.532706 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 1 vs column 4 | p-value | 0.001000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 1 vs column 5 | p-value | 0.114066 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 2 vs column 3 | p-value | 0.900000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 2 vs column 4 | p-value | 0.009434 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 2 vs column 5 | p-value | 0.532706 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 3 vs column 4 | p-value | 0.114066 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 3 vs column 5 | p-value | 0.900000 | — | — | Table 7, p. 61 |
| Nemenyi post-hoc, row 4 vs column 5 | p-value | 0.532706 | — | — | Table 7, p. 61 |
| Overall model comparison, Friedman's test | p-value | 0.000139 | — | — | Sect 3.3.6, p. 60 |
| Ensemble Voting Classifier, cross-validated accuracy (folds 1-5) | accuracy (%) | 99.90, 99.91, 99.90, 99.90, 99.92 | — | — | Table 8, p. 61 |
| Ensemble Voting Classifier, cross-validated F1 (folds 1-5) | F1 score | 0.81, 0.82, 0.81, 0.81, 0.82 | — | — | Table 8, p. 61 |
| Ensemble Voting Classifier, cross-validated ROC AUC (folds 1-5) | ROC AUC | 0.99, 0.99, 0.99, 0.99, 0.99 | — | — | Table 8, p. 61 |
| Ensemble Voting Classifier, averaged performance | accuracy (%) | 99.904 | — | — | Table 9, p. 62 |
| Ensemble Voting Classifier, averaged performance | F1 score | 0.814 | — | — | Table 9, p. 62 |
| Ensemble Voting Classifier, averaged performance | ROC AUC | 0.990 | — | — | Table 9, p. 62 |
| SHAP mean impact, OldBalanceOrg | mean SHAP value | 0.065 | — | — | Table 10, p. 63 |
| SHAP mean impact, NewBalanceOrg | mean SHAP value | 0.055 | — | — | Table 10, p. 63 |
| SHAP mean impact, Amount | mean SHAP value | 0.04 | — | — | Table 10, p. 63 |
| SHAP mean impact, NewBlanceDest | mean SHAP value | 0.03 | — | — | Table 10, p. 63 |
| SHAP mean impact, OldBalanceDest | mean SHAP value | 0.03 | — | — | Table 10, p. 63 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The usefulness of an Ensemble Learning Model with a Voting Classifier is shown by its evaluation of different machine learning models, which achieves an excellent accuracy of 99.904%." | Abstract, p. 52 | model_algorithm_integration |
| "This research combines the power of explainable AI with ensemble machine learning to create financial fraud detection models that perform well in accuracy and offer stakeholders interpretable insights." | Sect 1, p. 53 | model_algorithm_integration |
| "Traditional machine learning models frequently function as opaque, or "black-box," entities, making it challenging for stakeholders to understand the logic underlying the models forecasts." | Sect 1, p. 53 | model_algorithm_integration |
| "With this dataset, we want to address a knowledge vacuum in publicly available financial services datasets, with a focus on mobile money transactions as a relatively young industry." | Sect 3.1, p. 56 | data_collection |
| "The dataset encompasses a comprehensive 6,362,620 records, of which 6,354,407 are valid transactions, constituting 99.87%, and 8213 are fraudulent transactions, amounting to 0.13%." | Sect 3.1, p. 56 | data_collection |
| "Among the flagged transactions, totaling 16, all fall under the "TRANSFER" type and are marked as fraudulent." | Sect 3.1, p. 56 | data_collection |
| "To ensure uniformity, continuous values within the columns "amount," "oldbalanceOrg," "oldbalanceDest," "newbalanceOrig," and "newbalanceDest" are standardized to fall within the 0 to 1 range using the StandardScaler." | Sect 3.2, p. 58 | data_collection |
| "Thirdly, there is a connection to a branch from the root node in each subset. With each branch completed, the algorithm repeatedly continues the process." | Sect 3.3.2, p. 59 | rule_based_classification |
| "A stratified K-Fold cross validation was performed to ensure the reliability and robustness of the experiments." | Sect 3.3.6, p. 60 | model_performance_evaluation |
| "Additionally, Friedman's statistical test is used to compare the performance of different models. The resulting p-value is 0.000139 which is significantly less than the significance level 0.05" | Sect 3.3.6, p. 60 | model_performance_evaluation |
| "A number of classifiers—including XGBoost, LightBGM, Neural Networks, Decision Tree Classifier, and Random Forest Classifier—are part of this ensemble." | Sect 4, p. 61 | model_algorithm_integration |
| "To choose the most likely class, soft voting averages the base models' class pseudo-probabilities." | Sect 4, p. 61 | model_algorithm_integration |
| "The voting classifier outperforms the other baseline models because to its ability to incorporate the predictions of many ML and DL models." | Sect 4, p. 61 | model_algorithm_integration |
| "Remarkably, the OldBalanceOrg attribute takes precedence with the highest mean SHAP value of 0.065, signifying its discernibly stronger impact on the model's predictive outcomes." | Sect 5, p. 63 | model_algorithm_integration |
| "An F1 Score of 0.893, a ROC AUC Score of 0.943, and a maximum accuracy of 99.937 percent distinguish the Decision Tree model as the best performer among the models that were evaluated." | Sect 6, p. 63 | model_performance_evaluation |
| "With a 99.904% accuracy rate, an F1 Score of 0.814, and a remarkable ROC AUC Score of 0.990, the Ensemble Learning Model—implemented via a Voting Classifier—demonstrates itself as a strong solution." | Sect 6, p. 64 | model_performance_evaluation |

## Limitations and Gaps

- The paper claims the Voting Classifier "outperforms the other baseline models" (Sect 4, p. 61), but Table 6 (p. 61) reports the Decision Tree at 99.937% accuracy and 0.893 F1 and the Random Forest at 0.996 ROC AUC, all above the ensemble's 99.904%, 0.814 and 0.990 (Table 9, p. 62). Both sets of numbers are kept as printed; the paper does not reconcile them.
- The paper states it analyses "six well-known machine learning models" and then lists only five — Neural Network, XGBoost, Decision Tree, Random Forest and Logistic Regression — omitting LightGBM from the list even though LightGBM appears in every results table (Sect 3.3, p. 59).
- Figure 4 (p. 58) is captioned "Fraudulent transactions types" and gives Cash Out 223,750 and Transfer 532,909 instances, which cannot be reconciled with the 8213 fraudulent transactions reported in Sect 3.1 (p. 56); the paper does not explain the discrepancy.
- Table 7 (p. 61) labels its rows and columns only as 0 through 5, and the paper never states which model each index denotes, so the pairwise comparisons cannot be attributed to named models.
- Table 6 (p. 61) prints LightGBM between XGBoost and Neural Network, but the running text at Sect 3.3 (p. 59) and Sect 4 (p. 61) varies in how it lists the six classifiers; the reader cannot confirm the intended ordering.
- [unacknowledged] All reported results come from a single synthetic PaySim dataset. No external dataset, no live payment platform and no real transaction data are used, so external validity is untested.
- [unacknowledged] No confidence interval, standard deviation, or fold-level dispersion statistic is reported for any headline accuracy, F1 or ROC AUC figure. Tables 3-5 give fold values but no variance summary.
- [unacknowledged] Accuracy is reported on a dataset with a 0.13% positive rate, where a trivial all-negative classifier would score about 99.87%. The paper reports accuracy as the headline metric throughout and does not discuss this base-rate problem, though its own F1 values (0.507-0.893) show the models differ sharply on the minority class.
- [unacknowledged] The paper does not report which model the SHAP analysis was computed on, nor which sample of records the SHAP values come from.
- [unacknowledged] No random seed, no library version, and no code or data artefact is reported, so none of the results are reproducible from the text.
- [unacknowledged] The paper does not report a confusion matrix, precision or recall for any model, despite listing the confusion matrix among the planned performance indicators (Sect 3.3, p. 59).
- [unacknowledged] The `train_test_split` is described as stratified at a 20% test size (Sect 3.2, p. 58), but the absolute sizes of the training and test sets are not printed even though the text says the final dimensions were verified.
- [unacknowledged] The Nemenyi results are interpreted as showing that "Logistic Regression, Decision Trees, Random Forest, LightGBM have performance differences that are statistically significant" (p. 61), but with unlabelled indices this attribution cannot be checked.
- The authors acknowledge no financial support for the research, authorship or publication of the article (p. 64). They declare no competing interests (p. 65).

## Remember This

- The paper stacks a soft-voting classifier over XGBoost, LightGBM, Neural Network, Decision Tree and Random Forest, then explains it with SHAP.
- All evidence comes from one synthetic PaySim dataset of 6,362,620 mobile money transactions with 8213 frauds (0.13%).
- The ensemble reports 99.904% accuracy, 0.814 F1 and 0.990 ROC AUC — but the Decision Tree alone reports 99.937% accuracy and 0.893 F1, and Random Forest reports 0.996 ROC AUC, so the ensemble is not the best model on every metric the paper prints.
- OldBalanceOrg carries the largest mean SHAP value (0.065), followed by NewBalanceOrg (0.055) and Amount (0.04).
- Friedman's test p = 0.000139 supports the claim that the models differ; the Nemenyi matrix is printed with 0-5 indices and no model labels.

## Cited Works

- Ali, A.; Abd Razak, S.; Othman, S. H.; et al. (2022) (review) — systematic literature review of machine learning for financial fraud detection; recommends ensemble methods, unsupervised clustering, and text-mining techniques such as Word2Vec, Doc2Vec and BERT. [Sect 2, p. 53]
- Al-Hashedi, K. G.; Magalingam, P. (2021) (review) — review of 75 publications, 2009-2019; classifies fraud into bank, insurance, financial statement and cryptocurrency fraud; SVM is the most-used of 34 data-mining methods at 23%. [Sect 2, p. 53]
- Wickramanayake, B.; Geeganage, D. K.; Ouyang, C.; et al. (2020) (review) — survey of 45 papers on online card payment fraud detection using data-mining methods. [Sect 2, p. 53]
- Liu, Z.; Ye, R.; Ye, R. (2021) (methodology) — interpretable machine learning for financial statement fraud; identifies SMOTE as the best oversampling algorithm and Adaptive Lasso as the top feature selector. [Sect 2, p. 53]
- Hilal, W.; Gadsden, S. A.; Yawney, J. (2022) (review) — reviews anomaly detection for financial fraud with emphasis on unsupervised and semi-supervised learning, GANs and autoencoders. [Sect 2, p. 53]
- Mittal, S.; Tyagi, S. (2020) (review) — examines security concerns in online credit card use over 25 years, and the shortage of standard algorithms and benchmark datasets. [Sect 2, p. 53]
- Sadgali, I.; Sael, N.; Benabbou, F. (2019) (methodology) — evaluates machine learning techniques with emphasis on hybrid methods for detecting financial fraud types; highlights SVMs in instantaneous transactional fraud detection. [Sect 2, pp. 53-54]
- Alghofaili, Y.; Albattah, A.; Rassam, M. A. (2020) (baseline) — LSTM-based financial fraud detection model reporting 99.95% accuracy on a genuine credit card fraud dataset in under a minute. [Sect 2, p. 54]
- Alarfaj, F. K.; Malik, I.; Khan, H. U.; et al. (2022) (baseline) — enhanced deep learning algorithms for credit card fraud detection, reporting an F1 of 85.71%, precision of 93.1% and AUC of 98.0% on the European card benchmark dataset. [Sect 2, p. 54]
- Ileberi, E.; Sun, Y.; Wang, Z. (2021) (baseline) — ET-AdaBoost with Decision Trees, Random Forest, Extra Trees, XGBoost, Logistic Regression and SVM; reports 99.98% accuracy and an MCC of 0.99. [Sect 2, p. 54]
- Esenogho, E.; Mienye, I. D.; Swart, T. G.; et al. (2022) (baseline) — ensemble classifier with an LSTM base learner in AdaBoost and SMOTE-ENN hybrid resampling; reports specificity 0.998 and sensitivity 0.996. [Sect 2, p. 54]
- Alfaiz, N. S.; Fati, S. M. (2022) (baseline) — AllKNN-CatBoost for credit card fraud during the COVID-19 online-purchase spike; reports AUC 97.94%, recall 95.91% and F1 87.30% against sixty-six other models. [Sect 2, p. 54]
- Awosika, T.; Shukla, R. M.; Pranggono, B. (2023) (methodology) — combines explainable AI with federated learning for financial fraud detection, arguing that SHAP supports accountability, user trust and regulatory compliance. [Sect 2, p. 54]
- Lopez-Rojas, E. A.; Elmir, A.; Axelsson, S. (2016) (methodology) — PaySim, the financial mobile money simulator used to generate this paper's dataset. [Sect 3.1, p. 56; ref. 29, p. 65]
- Saranya, A.; Subhashini, R. (2023) (methodology) — systematic review of Explainable Artificial Intelligence models and applications, cited for the XAI process and the input-data/prediction-approach/explanation-interface chain. [Sect 5, p. 62]
- Hall, P.; Gill, N. (2019) (context) — the claim that machine learning models cannot be understood or trusted unless they are interpretable. [Sect 1, p. 52]
- Muna, R. K.; Hossain, M. I.; Alam, M. G. R.; et al. (2023) (context) — explainable-AI demystification of machine learning models for massive IoT attack detection in smart cities. [Sect 3, p. 55]
- Loh, H. W.; Ooi, C. P.; Seoni, S.; et al. (2022) (methodology) — systematic review of explainable AI in healthcare, cited for the Shapley-value axioms of efficiency, symmetry, dummy and additivity. [Sect 5, p. 63]
- Van den Broeck, G.; Lykov, A.; Schleich, M.; et al. (2022) (methodology) — tractability of SHAP explanations, cited for treating SHAP as a feature-attribution method. [Sect 5, p. 63]