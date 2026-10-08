---
paper_id: L--Salvador-2024
first_author: Salvador
year: 2024
title: "Use of Boosting Algorithms in Household-Level Poverty Measurement: A Machine Learning Approach to Predict and Classify Household Wealth Quintiles in the Philippines"
venue: "Not reported"
doi: Not reported

designation: local
status: extracted
modules: [model_development, model_performance_evaluation, data_collection]
module_rationale:
  model_development: "Sec. 2.1-2.5, pp. 2-4 document the full model-preparation workflow - missing-value cleaning, 80/20 stratified partitioning, z-score scaling, SelectFromModel feature selection, SMOTE and hyperparameter tuning - for the five boosting models."
  model_performance_evaluation: "Table 3, p. 6, Table 4, p. 7 and Table 5, p. 7 report accuracy, precision, recall, F1, per-class AUC-ROC, training time, testing time and model size for all five models."
  data_collection: "Sec. 2.1 Data Cleaning, p. 2 documents the 2022 DHS in the Philippines as the sole data source, with 2,099 features from 30,372 households reduced to 396 features and 20,679 households."
---

## Summary

Salvador (2024) compares five gradient-boosting classifiers — Adaptive Boosting (AdaBoost), Cat Boosting (CatBoost), Gradient Boosting Machine (GBM), Light Gradient Boosting Machine (LightGBM), and Extreme Gradient Boosting (XGBoost) — for predicting household wealth quintiles in the Philippines from the 2022 Demographic and Health Survey (DHS). Wealth is framed as a five-class problem (Richest, Richer, Middle, Poorer, Poorest). After cleaning, 20,679 households and 396 features remain; a SelectFromModel procedure reduces these to a final feature set, and SMOTE is applied to the training data for class imbalance. CatBoost attains the best scores across accuracy (0.909333), precision (0.909193), recall (0.909333), and F1 (0.909191); XGBoost, GBM, and LightGBM follow closely, and AdaBoost lags far behind at 0.803917 accuracy. AUC-ROC scores for the four leading models are near-perfect across most classes, while AdaBoost is substantially lower on the Poorest and Poorer classes. The study also reports computational efficacy: AdaBoost trains fastest (4.48 s) but tests slowest (0.23 s), and CatBoost trains slowest (69.29 s) with the largest model (30.50 MB) but tests fastest (0.01 s). The author concludes that machine learning can support poverty prediction and targeted policy interventions, and calls for richer data — GPS, night-light, and similar sources — in future work.

## Problem and Motivation

The paper opens on the scale of global poverty: over 700 million people live in extreme poverty as of 2024, and the lingering effects of COVID-19 may persist in some countries until 2030, placing Sustainable Development Goal 1 at risk (Sec. 1, p. 1). Because policymakers need accurate poverty determinations to target interventions and allocate resources, the paper argues that better measurement is a precondition for effective anti-poverty policy.

The paper distinguishes monetary from non-monetary poverty measurement. The Philippine methodology uses pre-tax income as the household well-being indicator, while other researchers treat poverty as multidimensional, including opportunity, education, and healthcare deficits (Sec. 1, p. 1). Conventional econometric methods are criticized for oversimplifying this multidimensionality by relying on pre-selected features such as income and neglecting non-monetary welfare indicators (Sec. 1, p. 1). Machine learning is positioned as advantageous because it can mitigate multicollinearity, achieve higher accuracy, process data quickly, accommodate large datasets, and perform automatic feature selection that captures nonlinear and obscured relationships (Sec. 1, p. 1).

A specific gap is identified: only a limited number of Philippine poverty studies use machine learning on nationwide DHS data, and those that do (e.g., geospatial studies achieving R² of 0.63 and 0.66, a CBMS study with 13 features, a K-means study with 17 features) do not explore extensive datasets of hundreds of household characteristics (Sec. 1, p. 3). The paper also targets the underutilization of boosting algorithms, noting that XGBoost is the sole boosting algorithm with a 14% usage rate in a recent scoping review on machine learning and poverty prediction (Sec. 1, p. 3). The stated aim is therefore to broaden poverty analysis with an extensive dataset, less restrictive assumptions, and a subset of boosting algorithms.

## Method

**Design.** Comparative machine-learning benchmark study applying five boosting algorithms to a five-class household wealth classification task; the authors state no formal design label.

**Sample.** n = 20,679 households after cleaning (reduced from 30,372), unit of analysis = household; each household carries a five-class wealth-quintile label (Richest, Richer, Middle, Poorer, Poorest).

**Context.** geography: Philippines; population: households in the 2022 DHS Philippines; setting: computational/offline analysis of survey data in Python, with no fieldwork, no live system, and no human participants.

- Source data: the 2022 DHS in the Philippines, originally 2,099 features from 30,372 households (Sec. 2.1, p. 2).
- Missing-value cleaning: a threshold of 3,050 missing values was assigned because most features had fewer than 3,050 missing values; columns above the threshold were removed and rows with any remaining null values were deleted; some interview-logistics features such as interview date were manually removed (Sec. 2.1, p. 2).
- Result of cleaning: 396 features (from 2,099) and 20,679 households (from 30,372) (Sec. 2.1, p. 2).
- Partitioning: random 80% training / 20% testing split, executed with stratified sampling; a validation set of 10% of the training set was carved out for hyperparameter optimization (Sec. 2.2, p. 3).
- Feature scaling: binary features left unscaled; numerical and ordinal features z-score normalized; the scaler was fit on training data and the same parameters applied to test data to prevent leakage (Sec. 2.3, p. 3).
- Feature selection: `SelectFromModel()` was used as a meta-transformer for each model; the frequency of each feature's selection was tallied and the most frequently chosen features formed the final set (Sec. 2.4, p. 3).
- Multicollinearity: Pearson's correlation coefficient was applied to the selected subset; for pairs with a coefficient of 0.8 or higher, the feature with lower selection frequency was removed (Sec. 2.4, p. 3).
- Class imbalance: SMOTE was employed on the training data (Sec. 2.5, p. 4).
- Hyperparameter tuning: manual trial and error plus grid search on the validation data; the final hyperparameters are in Table 2 (Sec. 2.5, p. 4).
- Models: AdaBoost (learning_rate 0.5, n_estimators 200); CatBoost (depth 4, iterations 300, learning_rate 0.3); GBM (learning_rate 0.3, max_depth 3, n_estimators 300); LightGBM (learning_rate 0.1, n_estimators 200, num_leaves 31); XGBoost (learning_rate 0.3, max_depth 3, n_estimators 300) (Table 2, p. 5).
- Evaluation metrics: accuracy, precision, recall, F1, AUC-ROC, and confusion matrices; computational efficacy measured via training time, testing time, and model size (Sec. 2.6, pp. 5-6).
- Timing and memory measurement used the `time` module and the `memory_profiler` library (Sec. 2.6, p. 6).

## Software

- NumPy 1.25.0
- pandas 1.5.1
- seaborn 0.13.2
- matplotlib 3.6.0
- scipy 1.10.0
- scikit-learn 1.4.2
- lightgbm 4.2.0
- xgboost 1.8.0
- catboost 1.1.0
- memory_profiler 0.61.0

## Key Findings

- CatBoost achieved the highest accuracy at 90.93%, followed by XGBoost at 89.41%, GBM at 89.05%, and LightGBM at 88.52%; AdaBoost had the lowest accuracy at 80.39% (Sec. 3, p. 6).
- Precision ranking was identical: CatBoost 90.92%, XGBoost 89.39%, GBM 89.04%, LightGBM 88.51%, AdaBoost 83.55% (Sec. 3, p. 6).
- Recall ranking was also identical: CatBoost 90.93%, XGBoost 89.41%, GBM 89.05%, LightGBM 88.52%, AdaBoost 80.39% (Sec. 3, p. 6).
- F1 ranking: CatBoost 90.92%, XGBoost 89.40%, GBM 89.04%, LightGBM 88.50%, AdaBoost 80.15% (Sec. 3, p. 6).
- The model ranking was consistent across all four metrics: CatBoost first, then XGBoost, GBM, LightGBM, and AdaBoost; the top four values are described as "remarkably similar," with only AdaBoost significantly lower (Sec. 3, p. 6).
- For the Poorest class, CatBoost, GBM, LightGBM, and XGBoost scored around 0.98 to 0.99, while AdaBoost scored significantly lower at 0.90 (Sec. 3, p. 6).
- For the Poorer class, CatBoost, GBM, LightGBM, and XGBoost all scored 0.99, while AdaBoost scored 0.73 (Sec. 3, p. 6).
- For the Middle class, all models reportedly demonstrated perfect 1.00 performance (Sec. 3, p. 6), though Table 4 prints AdaBoost at 0.99 for this class.
- For the Richer class, CatBoost, GBM, LightGBM, and XGBoost reportedly scored 1.00, while AdaBoost scored 0.79 (Sec. 3, p. 7), though Table 4 prints 0.99 for the four leading models.
- For the Richest class, CatBoost, GBM, LightGBM, and XGBoost reportedly scored 1.00 and AdaBoost 0.99 (Sec. 3, p. 7), though Table 4 prints AdaBoost at 1.00.
- AdaBoost's confusion matrix shows true Poorest instances misclassified as Poorer and some as Richer; Poorer instances misclassified as Poorest or Middle; and Richer instances misclassified as Poorer or Richest (Sec. 3, pp. 6-7).
- Computational efficacy: AdaBoost had the shortest training time (~4.48 s) but longest testing time (0.23 s); CatBoost had the longest training time (69.29 s) and largest model size (30.50 MB) but fastest testing (0.01 s); GBM had 16.81 s training, 0.02 s testing, 15.80 MB model; LightGBM had 2.17 s training, 0.07 s testing, 2.50 MB; XGBoost had 2.58 s training, 0.03 s testing, 3.10 MB (Sec. 3, p. 7).
- The discussion concludes CatBoost is the top performer overall, XGBoost, GBM, and LightGBM follow closely, and AdaBoost is efficient in training but weaker in all performance metrics (Sec. 4, p. 7).
- LightGBM and XGBoost are singled out as the best balance of high performance and computational efficiency and therefore as strong practical candidates (Sec. 4, p. 7).

## Key Figures and Tables

- Figure 1 (p. 2): Distribution of missing values across features, with a blue line at the 3,050 threshold used to drop columns.
- Table 1 (pp. 3-4): Description of the selected features — 36 rows covering drinking-water source, toilet facility, household assets (television, refrigerator, bicycle, motorcycle/scooter, car/truck, telephone, watch, computer, bank account, washing machine, air conditioner, gas range, microwave, audio component, cable services, mobile telephone, mobile-phone financial transactions, induction stove, DVD player), housing materials, cookstove and cooking fuel, light source, tenure status, place of residence, time to water source, number of sleeping rooms, 4Ps beneficiary status, and handwashing place.
- Table 2 (p. 5): Hyperparameters for the five gradient-boosting algorithms.
- Table 3 (p. 6): Performance evaluation metrics (accuracy, precision, recall, F1) for the five models.
- Table 4 (p. 7): AUC-ROC scores per wealth class (Poorest, Poorer, Middle, Richer, Richest) for each model.
- Table 5 (p. 7): Computational efficacy metrics (training time, testing time, model size) for each model.
- Figure 2 (p. 8): Confusion matrices for AdaBoost (Fig 2.1), CatBoost (Fig 2.2), GBM (Fig 2.3), LightGBM (Fig 2.4), and XGBoost (Fig 2.5).

## Limitations and Gaps

- The paper's feature-selection account is internally inconsistent: Sec. 2.4 states that "This process resulted in the selection of 66 features deemed most relevant for predicting poverty," then immediately states that "From the original 36 features initially selected via SelectFromModel(), the final count remained the same" (Sec. 2.4, p. 3). Both figures are printed; the actual selected-feature count is ambiguous.
- Table 4's printed AUC-ROC values disagree with the narrative in Sec. 3 for several classes — the narrative claims all models reach 1.00 for Middle and that the four leading models reach 1.00 for Richer, while Table 4 prints AdaBoost at 0.99 for Middle and the four leading models at 0.99 for Richer; the narrative also claims AdaBoost scores 0.99 for Richest while Table 4 prints 1.00 (Table 4, p. 7 vs. Sec. 3, pp. 6-7). Both values are kept in the evidence table rather than reconciled.
- [unacknowledged] The paper reports no confidence intervals, no standard errors, no cross-validation folds, and no significance tests; every model metric is a single point estimate on one 20% test split (Sec. 3, pp. 6-7).
- [unacknowledged] No per-model confusion-matrix cell counts are printed; Figure 2 is described only qualitatively, so precision, recall, and per-class error structure cannot be reconstructed (Sec. 3, pp. 6-7).
- [unacknowledged] The 2022 DHS wealth index used as the label is itself a constructed asset-based index; the paper does not report how the five quintile classes were derived from the DHS wealth variable, nor does it show the class distribution before and after SMOTE (Sec. 2.5, p. 4).
- [unacknowledged] The paper reports no temporal validation, no geographic hold-out, and no external dataset; all results are in-sample to one survey wave (Sec. 2.2, p. 3).
- [unacknowledged] Table 1 is described as the selected-feature list, but a number of listed rows (e.g., "Time to get to water source", "Number of rooms used for sleeping") are numerical features with no printed range or distribution, so the feature set cannot be fully re-implemented from the paper (Table 1, pp. 3-4).
- The authors acknowledge reliance on DHS data and state that "the limitations in this study, such as the reliance on DHS data and the need for further validation using alternative datasets or methodologies must be acknowledged" (Sec. 4, p. 8).
- The authors acknowledge that incorporating more complex information — GPS data, night-light data, and other advanced metrics — is necessary to improve precision, and that combining GPS with survey data could enhance classification accuracy (Sec. 4, p. 8).
- The authors note that CatBoost required the longest training time and the largest model size, while AdaBoost had the shortest training time but longest testing time (Sec. 3, p. 7; Sec. 4, p. 7).
- The paper does not report any policy-evaluation or causal result; feature selection is said only to "indirectly suggest" areas for policy focus, and the paper calls for future research to model explicitly how changes in those features affect predicted poverty classes (Sec. 4, p. 7).

## Definitions

- **Boosting algorithm** — an ensemble method that combines weak learners sequentially to improve predictive performance; five variants are compared here (Sec. 2.5, p. 4).
- **Wealth quintile classes** — the five-class target: Richest, Richer, Middle, Poorer, Poorest (Sec. 3, p. 6).
- **DHS** — Demographic and Health Survey; the 2022 Philippines wave is the sole data source (Sec. 2.1, p. 2).
- **SMOTE** — Synthetic Minority Over-sampling Technique, applied to the training data to handle class imbalance (Sec. 2.5, p. 4).
- **SelectFromModel** — a scikit-learn meta-transformer for feature selection compatible with estimators that expose feature importance (Sec. 2.4, p. 3).
- **AUC-ROC** — Area Under the Receiver Operating Characteristic Curve; ranges from 0 to 1, with 1 indicating perfect class separation and 0.5 random guessing (Sec. 2.6, p. 5).
- **4Ps** — Pantawid Pamilyang Pilipino Program, a Philippine conditional cash-transfer programme included among the features (Table 1, p. 4).

## Key Equations

- `Accuracy = (TP + TN) / (TP + TN + FP + FN)` — proportion of correctly predicted instances (Eq. 1, p. 5).
- `Precision = TP / (TP + FP)` — proportion of correctly predicted positives among predicted positives (Eq. 2, p. 5).
- `Recall = TP / (TP + FN)` — proportion of correctly predicted positives among actual positives (Eq. 3, p. 5).
- `F1 Score = 2 × (Precision × Recall) / (Precision + Recall)` — harmonic mean of precision and recall (Eq. 4, p. 5).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Source dataset, original households | households | 30,372 | — | — | Sec. 2.1, p. 2 |
| Source dataset, original features | features | 2,099 | — | — | Sec. 2.1, p. 2 |
| Missing-value threshold applied to columns | missing values | 3,050 | — | — | Sec. 2.1, p. 2 |
| Cleaned dataset, features retained | features | 396 | — | — | Sec. 2.1, p. 2 |
| Cleaned dataset, households retained | households | 20,679 | — | — | Sec. 2.1, p. 2 |
| Selected features after SelectFromModel (first statement) | features | 66 | — | — | Sec. 2.4, p. 3 |
| Selected features after SelectFromModel (second statement) | features | 36 | — | — | Sec. 2.4, p. 3 |
| Multicollinearity removal threshold | Pearson correlation coefficient | 0.8 | — | — | Sec. 2.4, p. 3 |
| Training / testing split | share of cleaned dataset | 80% / 20% | — | — | Sec. 2.2, p. 3 |
| Validation set | share of training set | 10% | — | — | Sec. 2.2, p. 3 |
| AdaBoost accuracy | accuracy | 0.803917 | — | — | Table 3, p. 6 |
| AdaBoost precision | precision | 0.835551 | — | — | Table 3, p. 6 |
| AdaBoost recall | recall | 0.803917 | — | — | Table 3, p. 6 |
| AdaBoost F1 | F1 score | 0.801523 | — | — | Table 3, p. 6 |
| CatBoost accuracy | accuracy | 0.909333 | — | — | Table 3, p. 6 |
| CatBoost precision | precision | 0.909193 | — | — | Table 3, p. 6 |
| CatBoost recall | recall | 0.909333 | — | — | Table 3, p. 6 |
| CatBoost F1 | F1 score | 0.909191 | — | — | Table 3, p. 6 |
| GBM accuracy | accuracy | 0.890474 | — | — | Table 3, p. 6 |
| GBM precision | precision | 0.890362 | — | — | Table 3, p. 6 |
| GBM recall | recall | 0.890474 | — | — | Table 3, p. 6 |
| GBM F1 | F1 score | 0.890353 | — | — | Table 3, p. 6 |
| LightGBM accuracy | accuracy | 0.885155 | — | — | Table 3, p. 6 |
| LightGBM precision | precision | 0.885137 | — | — | Table 3, p. 6 |
| LightGBM recall | recall | 0.885155 | — | — | Table 3, p. 6 |
| LightGBM F1 | F1 score | 0.884996 | — | — | Table 3, p. 6 |
| XGBoost accuracy | accuracy | 0.894101 | — | — | Table 3, p. 6 |
| XGBoost precision | precision | 0.893919 | — | — | Table 3, p. 6 |
| XGBoost recall | recall | 0.894101 | — | — | Table 3, p. 6 |
| XGBoost F1 | F1 score | 0.893981 | — | — | Table 3, p. 6 |
| AUC-ROC Poorest, AdaBoost | AUC-ROC | 0.90 | — | — | Table 4, p. 7 |
| AUC-ROC Poorest, CatBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Poorest, GBM | AUC-ROC | 0.98 | — | — | Table 4, p. 7 |
| AUC-ROC Poorest, LightGBM | AUC-ROC | 0.98 | — | — | Table 4, p. 7 |
| AUC-ROC Poorest, XGBoost | AUC-ROC | 0.98 | — | — | Table 4, p. 7 |
| AUC-ROC Poorer, AdaBoost | AUC-ROC | 0.73 | — | — | Table 4, p. 7 |
| AUC-ROC Poorer, CatBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Poorer, GBM | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Poorer, LightGBM | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Poorer, XGBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Middle, AdaBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Middle, CatBoost | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Middle, GBM | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Middle, LightGBM | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Middle, XGBoost | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Richer, AdaBoost | AUC-ROC | 0.79 | — | — | Table 4, p. 7 |
| AUC-ROC Richer, CatBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Richer, GBM | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Richer, LightGBM | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Richer, XGBoost | AUC-ROC | 0.99 | — | — | Table 4, p. 7 |
| AUC-ROC Richest, AdaBoost | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Richest, CatBoost | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Richest, GBM | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Richest, LightGBM | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AUC-ROC Richest, XGBoost | AUC-ROC | 1.00 | — | — | Table 4, p. 7 |
| AdaBoost training time | seconds | 4.48 | — | — | Table 5, p. 7 |
| AdaBoost testing time | seconds | 0.23 | — | — | Table 5, p. 7 |
| AdaBoost model size | MB | 1.20 | — | — | Table 5, p. 7 |
| CatBoost training time | seconds | 69.29 | — | — | Table 5, p. 7 |
| CatBoost testing time | seconds | 0.01 | — | — | Table 5, p. 7 |
| CatBoost model size | MB | 30.50 | — | — | Table 5, p. 7 |
| GBM training time | seconds | 16.81 | — | — | Table 5, p. 7 |
| GBM testing time | seconds | 0.02 | — | — | Table 5, p. 7 |
| GBM model size | MB | 15.80 | — | — | Table 5, p. 7 |
| LightGBM training time | seconds | 2.17 | — | — | Table 5, p. 7 |
| LightGBM testing time | seconds | 0.07 | — | — | Table 5, p. 7 |
| LightGBM model size | MB | 2.50 | — | — | Table 5, p. 7 |
| XGBoost training time | seconds | 2.58 | — | — | Table 5, p. 7 |
| XGBoost testing time | seconds | 0.03 | — | — | Table 5, p. 7 |
| XGBoost model size | MB | 3.10 | — | — | Table 5, p. 7 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "CatBoost achieved the highest accuracy (90.93%) and overall performance metrics, followed by XGBoost, GBM, and LightGBM. AdaBoost had the lowest performance." | Highlights, p. 1 | model_performance_evaluation |
| "This study assessed the effectiveness of machine learning models in predicting poverty levels in the Philippines using five boosting algorithms" | Abstract, p. 2 | model_performance_evaluation |
| "CatBoost emerged as the superior model and achieved the highest scores across accuracy, precision, recall, and F1-score at 91%, while XGBoost and GBM followed closely with 89% and 88% respectively." | Abstract, p. 2 | model_performance_evaluation |
| "These results indicate that machine learning can aid in poverty prediction and in the development of targeted policy interventions." | Abstract, p. 2 | data_collection |
| "The data for this study was obtained from the 2022 DHS in the Philippines." | Sec. 2.1 Data Cleaning, p. 2 | data_collection |
| "The original dataset consisted of 2,099 features collected from 30,372 households." | Sec. 2.1 Data Cleaning, p. 2 | data_collection |
| "After this step, the dataset was reduced to 396 features from 2,099 features, and 20,679 households from 30,372 households." | Sec. 2.1 Data Cleaning, p. 2 | data_collection |
| "This process resulted in the selection of 66 features deemed most relevant for predicting poverty." | Sec. 2.4 Feature Selection, p. 3 | model_development |
| "From the original 36 features initially selected via SelectFromModel(), the final count remained the same, as there is minimal to no multicollinearity among them." | Sec. 2.4 Feature Selection, p. 3 | model_development |
| "To handle class imbalance, the Synthetic Minority Over-sampling Technique (SMOTE) was employed on the training data." | Sec. 2.5 Machine Learning Models, p. 4 | model_development |
| "Wealth classification was approached as a five-class problem (Richest, Richer, Middle, Poorer, Poorest)." | Sec. 3 Results, p. 6 | model_development |
| "CatBoost was first, followed by XGBoost, GBM, LightGBM, and AdaBoost in that order." | Sec. 3 Results, p. 6 | model_performance_evaluation |
| "AdaBoost stands out with the shortest training time at approximately 4.48 seconds, making it the quickest model to train. However, it takes the longest time for testing at 0.23 seconds." | Sec. 3 Results, p. 7 | model_performance_evaluation |
| "CatBoost, while having the longest training time of 69.29 seconds and the largest model size at 30.50 MB, demonstrates exceptional efficiency during testing, taking only 0.01 seconds." | Sec. 3 Results, p. 7 | model_performance_evaluation |
| "Overall, CatBoost emerged as the top performer across all metrics, followed closely by XGBoost, GBM, and LightGBM." | Sec. 4 Discussion, p. 7 | model_performance_evaluation |
| "LightGBM and XGBoost demonstrated a good balance of high performance and computational efficiency, thus are strong candidates for practical applications." | Sec. 4 Discussion, p. 7 | model_performance_evaluation |
| "Combining GPS data with survey data, for instance, could significantly enhance the accuracy of poverty level classification in the Philippines." | Sec. 4 Discussion, p. 8 | data_collection |
| "This study demonstrated the effectiveness of machine learning boosting algorithms, particularly CatBoost, in predicting household poverty levels in the Philippines." | Sec. 5 Conclusion, p. 9 | model_performance_evaluation |

## Remember This

- The paper benchmarks five boosting algorithms (AdaBoost, CatBoost, GBM, LightGBM, XGBoost) on 2022 DHS Philippines data for a five-class household wealth prediction task.
- CatBoost is the top performer on accuracy (0.909333), precision (0.909193), recall (0.909333) and F1 (0.909191); AdaBoost is last on all four (0.803917 / 0.835551 / 0.803917 / 0.801523).
- The four leading models are within roughly two accuracy points of one another; only AdaBoost separates clearly.
- Computational trade-off: AdaBoost trains fastest (4.48 s) but tests slowest (0.23 s); CatBoost trains slowest (69.29 s) with the largest model (30.50 MB) but tests fastest (0.01 s).
- The paper's own feature-count statements disagree (66 vs 36), and Table 4 disagrees with the Sec. 3 narrative for Middle, Richer, and Richest AUC-ROC cells.
- No confidence intervals, no significance tests, no cross-validation folds, and no per-cell confusion-matrix counts are reported.

## Cited Works

- [1] World Bank (2024) — Poverty overview: development news, research, data; source for the 700 million extreme-poverty figure. [p. 1]
- [2] Shulla, Voigt, Cibian, Scandone, Martinez, Nelkovski, Salehi (2021) — Effects of COVID-19 on the Sustainable Development Goals; source for the pandemic's lingering effects. [p. 1]
- [3] Riegner (2016) — Implementing the data revolution for the post-2015 SDGs; source for the claim that accurate poverty determination is paramount. [p. 1]
- [4] Grindle (2004) — Good enough governance: poverty reduction and reform in developing countries; source for the risk that policy falls short without accurate data. [p. 1]
- [5] Decerf (2023) — A preference-based theory unifying monetary and non-monetary poverty measurement; source for the two-category poverty measurement framing. [p. 1]
- [6] Albert (2023) — Analysis on poverty lines and counting the poor; source for the Philippine pre-tax income methodology. [p. 1]
- [7] Briones, Lopez, Elumbre, Angangco (2021) — Income, consumption, and poverty measurement in the Philippines; source for the Philippine methodology. [p. 1]
- [8] Alkire, Roche, Ballon, Foster, Santos, Seth (2015) — Multidimensional poverty measurement and analysis; source for the multidimensional view of poverty. [p. 1]
- [9] Watson, Whelan, Maître, Williams (2017) — Non-monetary indicators and multiple dimensions; source for the critique of conventional poverty measures. [p. 1]
- [10] Shobana, Umamaheswari (2021) — Forecasting by machine learning techniques and econometrics: a review; source for machine-learning advantages over econometric methods. [p. 1]
- [11] Li, Cheng, Wang, Morstatter, Trevino, Tang, Liu (2017) — Feature selection: a data perspective; source for feature selection and the excessive-features efficiency concern. [pp. 1, 3]
- [12] Tingzon, Orden, Go, Sy, Sekara, Weber, Kim (2019) — Mapping poverty in the Philippines using machine learning, satellite imagery, and crowd-sourced geospatial information (R² 0.63). [p. 3]
- [13] Ledesma, Garonita, Flores, Tingzon, Dalisay (2020) — Interpretable poverty mapping using social media data, satellite images, and geospatial information (R² 0.66). [p. 3]
- [14] Talingdan (2019) — Performance comparison of different classification algorithms for household poverty classification (CBMS, 13 features, Naive Bayes best). [p. 3]
- [15] Repollo, Aurelius, Robielos (2021) — Applying clustering algorithm on poverty analysis in a community in the Philippines (K-means, 17 features). [p. 3]
- [16] Li, Yu, Échevin, Fan (2022) — Is poverty predictable with machine learning? A study of DHS data from Kyrgyzstan; source for the underutilization of boosting in poverty prediction. [p. 3]
- [17] Usmanova, Aziz, Rakhmonov, Osamy (2022) — Utilities of artificial intelligence in poverty prediction: a review; source for the 14% XGBoost usage rate. [p. 3]
- [18] Bentéjac, Csörgő, Martínez-Muñoz (2021) — A comparative analysis of gradient boosting algorithms; source for the expansion of the boosting family. [p. 3]