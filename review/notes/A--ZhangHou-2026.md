---
paper_id: A--ZhangHou-2026
first_author: Zhang
year: 2026
title: "Consumer Behavior Data Mining and Analysis Using Machine Learning Algorithms"
venue: "Procedia Computer Science"
doi: Not reported
designation: algorithm
status: extracted
modules: [data_collection, model_development, model_performance_evaluation, rule_based_classification]
module_rationale:
  data_collection: "Sect. 3.1 names the single data source — the public UCI 'Online Retail' dataset, its date range and its fields — as the basis for all experiments."
  model_development: "Sect. 3.2–3.3 describe cleaning, label construction, the 28 RFM-based features and grid-search with 5-fold cross-validation that prepare the four models."
  model_performance_evaluation: "Table 1 reports accuracy, precision, recall, F1 and AUC for each of the four models on a held-out test set, and Table 2 reports their training and prediction times."
  rule_based_classification: "Sect. 3.3 and Eq. 3 define the compared classifiers, including the tree models whose nodes are split by Gini-selected if-then rules."
---

## Summary

This paper compares four machine-learning classifiers — logistic regression, support vector machine (SVM), random forest (labelled "SF" or "Stochastic Forest" in the tables) and XGBoost — on one binary task: predicting whether a customer will make another purchase inside a fixed future window. The data are the public UCI "Online Retail" dataset, described as recording all cross-border transactions of an online retail company from 1 December 2020 to 9 December 2021 across fields such as InvoiceNo, StockCode, Quantity, InvoiceDate, UnitPrice, Customer ID and Country. Every customer is represented by 28 numerical features in four families: RFM core features, behavioural breadth and depth, consumption patterns, and time patterns. The forecast window runs from 1 November to 9 December 2021; a customer with at least one purchase in that window is a positive case, and all data before 1 November 2021 supply the features. The dataset is split 7:3 by Customer ID into training and test sets, each model is tuned by grid search with 5-fold cross-validation, and performance is reported on accuracy, precision, recall, F1 score and AUC. XGBoost leads on all five indicators (accuracy 0.876, precision 0.781, recall 0.602, F1 0.680, AUC 0.872), logistic regression is fastest to train (0.8 s) and SVM slowest (125.3 s), and recency of the most recent purchase is the top-ranked feature in every model. The paper reports no confidence intervals, no significance tests, and never states its sample size.

## Problem and Motivation

E-commerce, mobile internet and IoT technologies have recorded browsing, searching, clicking, buying and evaluating behaviour on digital platforms, producing "a huge, diverse and real-time big data resource" (Sect. 1, p. 2). The paper argues this marks a paradigm shift for consumer-behaviour research, away from causal inference on sampling surveys and toward correlation mining and predictive analysis on full data. Traditional statistical tools such as linear regression and analysis of variance are presented as inadequate for these high-dimensional, nonlinear, complex data forms, whereas machine learning "automatically learns patterns and rules from data through algorithms" and is already used for customer churn prediction, marketing response modelling and credit scoring.

The stated gap is comparative rather than methodological: the paper says existing research has proven the value of machine learning in consumer-behaviour analysis and has moved from linear models and kernel methods to deep learning and ensemble learning, but that the four chosen algorithms have not been placed under "the same data and evaluation system" so that "the root causes of their performance differences" can be discussed (Sect. 2, p. 3). The study therefore sets out to run "rigorous controlled experiments" that evaluate logistic regression, SVM, random forest and XGBoost under one feature-engineering and evaluation framework, and to add engineering-practice indicators — training efficiency and feature importance — to the accuracy comparison so that practitioners get "a clear and comprehensive algorithm performance map and selection decision reference" (Sect. 1, p. 2). A secondary motivation is the trade-off the abstract names between accuracy, efficiency and interpretability: ensemble learning is expected to win on accuracy, logistic regression is expected to retain "the best explicability," and the paper promises selection guidance rather than a single winner.

## Method

**Design.** Comparative benchmark experiment over four machine-learning classification algorithms on one public transactional dataset; the authors state no formal design label.
**Sample.** N not reported (the paper never prints the number of transactions, invoices, or customers in the dataset, nor the sizes of the training and test sets); the unit of analysis is the customer, represented by one 28-feature vector built from that customer's historical transactions, with Customer ID as the split key.
**Context.** geography: Not reported for the customer population; the dataset is the public UCI "Online Retail" set and the company is described only as an online retailer whose transactions are cross-border; population: customers of that single online retail company with at least one transaction between 1 December 2020 and 9 December 2021; setting: computational and offline — a single Intel Core i7-12700H machine with 16GB DDR4 memory running Python 3.9, with no human participants, no field deployment and no live system.

- Use the publicly available "Online Retail" dataset from the UCI machine-learning repository, recording all cross-border transactions of one online retail company from 1 December 2020 to 9 December 2021 with fields InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, Customer ID and Country (Sect. 3.1).
- Clean the data by deleting duplicate records, excluding records with an empty Customer ID because they cannot be associated with an individual, and removing records unrelated to purchase prediction or representing abnormal behaviour — return records whose invoice numbers start with 'C' and entries with negative Quantity (Sect. 3.2.1).
- Define the label as binary: customers with at least one purchase between 1 November and 9 December 2021 are positive samples (y=1), all others negative (y=0); all history from 1 December 2020 to 31 October 2021 builds the features (Sect. 3.2.1).
- Split the dataset randomly 7:3 into a training set and an independent test set by Customer ID, so that all records of one customer fall in exactly one side and evaluation is not inflated by data leakage (Sect. 3.2.1).
- Build 28 numerical features per customer in four families: RFM core features; behavioural breadth and depth (unique products purchased, unique product categories visited, average products per invoice); consumption pattern features (average order value, standard deviation of order value, average unit price, standard deviation of unit price, proportion of discounted goods purchased); and time pattern features (average purchase interval days, standard deviation of purchase interval days, proportion of weekend purchases, distribution across morning, afternoon and evening on weekdays) (Sect. 3.2.2).
- Standardise all features before training (Sect. 3.3).
- Optimise key hyperparameters of each model on the training set with grid search combined with 5-fold cross-validation — the regularisation coefficient C for logistic regression and SVM, the number and maximum depth of trees for random forests, and the learning rate and maximum tree depth for XGBoost (Sect. 3.3).
- Select four algorithms for comparison: logistic regression as the linear benchmark; SVM with a radial basis kernel; random forest as a Bagging representative using Gini-based splits; and XGBoost as a Boosting representative with a regularised additive objective (Sect. 3.3).
- Evaluate the tuned models on the independent test set that was never used for training or tuning, using accuracy, precision, recall, F1 score and AUC (Sect. 4.1).
- Record training time (including cross-validation tuning) and test-set prediction time for each model in the same hardware environment (Sect. 4.1).
- Analyse feature importance per model — normalised absolute coefficients for logistic regression, impurity (or information gain) reduction for the tree models — and report the top three features per model (Sect. 4.1).

## Software

- Python 3.9 (Sect. 3.1)
- Pandas 1.4.2 (Sect. 3.1)
- NumPy 1.22.3 (Sect. 3.1)
- Scikit-learn 1.0.2 (Sect. 3.1)
- XGBoost 1.5.0 (Sect. 3.1)
- Matplotlib (version not reported) and Seaborn (version not reported) for visualisation (Sect. 3.1)
- Hardware: Intel Core i7-12700H processor with 16GB DDR4 memory (Sect. 3.1)
- Data source: UCI machine-learning repository "Online Retail" dataset (Sect. 3.1)

## Key Findings

- num: XGBoost records the best value on all five reported indicators: accuracy 0.876, precision 0.781, recall 0.602, F1 score 0.680 and AUC 0.872 (Table 1, p. 4).
- num: Random forest ("SF") is second on all five indicators: accuracy 0.862, precision 0.758, recall 0.570, F1 0.651 and AUC 0.853 (Table 1, p. 4).
- num: Logistic regression has the lowest recall of the four models, 0.468, against 0.512 for SVM, 0.570 for random forest and 0.602 for XGBoost (Table 1, p. 4).
- num: Logistic regression is the fastest model to train (0.8 s) and to predict with (0.02 s); SVM is by far the slowest to train (125.3 s) and to predict (18.7 s) (Table 2, p. 5).
- num: Random forest trains in 15.2 s and predicts in 0.35 s, while XGBoost trains in 9.5 s and predicts in 0.08 s — the paper reads this as XGBoost being more training-efficient than random forest (Table 2, p. 5).
- num: The dataset is described as all cross-border transactions of one online retail company from 1 December 2020 to 9 December 2021 (Sect. 3.1, p. 3).
- num: Features are 28 numerical values per customer in four categories, standardised before training (Sect. 3.2.2, p. 3).
- num: The train/test split is 7:3 by Customer ID and hyperparameter tuning uses grid search with 5-fold cross-validation (Sect. 3.2.1, Sect. 3.3, p. 3–4).
- num: The forecast window is 1 November to 9 December 2021, with all earlier data (1 December 2020 to 31 October 2021) used to construct features (Sect. 3.2.1, p. 3).
- "Recent purchase time" (Recency) is the single top-ranked predictor across all models, which the paper reads as data-driven confirmation of the R component of the RFM framework (Sect. 4.1–4.2, pp. 5–6).
- The paper concludes that XGBoost gives the best balance of accuracy and efficiency, random forest gives stable and robust accuracy, and logistic regression keeps irreplaceable value through interpretability and computational efficiency (Sect. 5, p. 6).
- SVM's cost is attributed to its dependence on kernel and penalty-parameter choice and to a time complexity that becomes "the main bottleneck in large-scale data" (Sect. 4.2, pp. 5–6).

## Key Figures and Tables

- Table 1 (p. 4): Comprehensive comparison of prediction performance of different machine-learning models — accuracy, precision, recall, F1 score and AUC for logistic regression (0.834, 0.701, 0.468, 0.562, 0.792), SVM (0.848, 0.732, 0.512, 0.602, 0.821), SF (0.862, 0.758, 0.570, 0.651, 0.853) and XGBoost (0.876, 0.781, 0.602, 0.680, 0.872) → XGBoost leads on every indicator and the ranking of models is identical across all five metrics.
- Table 2 (p. 5): Comparison of model training and prediction efficiency in seconds — training time 0.8 (logistic regression), 125.3 (SVM), 15.2 (SF), 9.5 (XGBoost); prediction time on the test set 0.02, 18.7, 0.35, 0.08 in the same model order → the accuracy winner is not the slowest model, and the model with the best accuracy also trains faster than random forest.
- Table 3 (p. 5): Model feature importance ranking (top 3) — logistic regression by normalised absolute coefficient: Recency, Monetary, frequency; SF by impurity reduction: Recency, frequency, Monetary; XGBoost by impurity reduction: Recency, frequency, average order value → recency ranks first everywhere, and XGBoost additionally surfaces the derived "average order value" feature.
- No figures are present in the paper; all reported results are tabular.
- [unacknowledged] Table 3's column boundaries are partially garbled in the available extraction, so the exact membership of the SF and XGBoost top-three lists (in particular whether Monetary or average order value occupies the third XGBoost slot) cannot be fully reconstructed, and the text's statement that all three RFM indicators "consistently rank high" does not settle the ordering.

## Limitations and Gaps

- The authors acknowledge that logistic regression's "strong assumption of linearly separable data" does not hold on complex behavioural data, which they give as the reason for its lowest recall of 0.468 (Sect. 4.2, p. 5).
- The authors acknowledge that SVM performance "is highly dependent on the selection of kernel function and penalty parameter C, resulting in high optimization costs" (Sect. 4.2, p. 5).
- The authors acknowledge that SVM's training time "far exceeds other models, and its time complexity becomes the main bottleneck in large-scale data, with poor scalability" (Sect. 4.2, pp. 5–6).
- The authors acknowledge, in the abstract's framing, that no model wins on every criterion: the study is presented as guidance for "the trade-off between accuracy, efficiency and interpretability" (Abstract, p. 1).
- [unacknowledged] The paper never reports a sample size — not the number of transactions, not the number of customers, not the size of the training or test set — so the precision of every estimate in Table 1 and the effective N behind the 7:3 split are unknown.
- [unacknowledged] No confidence interval, standard error, p-value or cross-validation variance is printed anywhere; the comparison between, for example, accuracy 0.862 (SF) and 0.876 (XGBoost) rests on single point estimates with no test of whether the gap is larger than run-to-run noise.
- [unacknowledged] The grid-search hyperparameter values actually selected are never printed — only the search strategy (grid search with 5-fold cross-validation) and the names of the tuned parameters — so the reported results are not reproducible from the paper.
- [unacknowledged] Class balance is not reported: the proportion of positive labels in the 1 November – 9 December 2021 forecast window is never given, leaving precision (0.701–0.781) and recall (0.468–0.602) without the base rate needed to interpret them.
- [unacknowledged] The paper states that 28 numerical features were constructed in four categories, but the four categories enumerate only about fifteen named features (3 RFM + 3 behavioural + 5 consumption + roughly 4 time-pattern), so the remaining features are not identified.
- [unacknowledged] Only one dataset, one forecast window and one split ratio are used; there is no repeated splitting, no alternative prediction horizon, and no external or temporal validation beyond the single 7:3 by-Customer-ID split.
- [unacknowledged] The efficiency comparison rests on single measurements in one hardware environment with no repetition, yet the paper describes XGBoost's training efficiency advantage over random forest as "significantly higher" without a statistical test (Sect. 4.2, p. 6).
- [unacknowledged] No confusion matrix, ROC curve, per-class breakdown or calibration analysis is reported, so the source of the recall gap between logistic regression and XGBoost cannot be inspected.
- [unacknowledged] The label definition uses "such as the following month" for the fixed prediction window and then fixes 1 November – 9 December 2021, a 39-day window that is neither a calendar month nor a uniform period, and the paper does not discuss this choice (Sect. 3.2.1, p. 3).
- [unacknowledged] The paper contains no limitations section, no future-work statement and no discussion of how the four-model ranking might transfer to other retailers, countries or time periods.
- [unacknowledged] The text of Sect. 4.1 defines "Accuracy" twice in a row — once as "the proportion of correct overall classification" and once as "the proportion of customers predicted by the model to actually make a purchase" — while precision is the column that the second definition describes, leaving the reported precision column's stated definition ambiguous in the prose (Sect. 4.1, p. 4).

## Definitions

- **RFM model** — Recency, Frequency, Monetary value framework; its three core indicators supply the first feature family and rank high in every model's importance list.
- **Recency (R)** — time of the customer's most recent purchase; described as the primary predictor in all four models and the top-ranked feature in Table 3.
- **SF / Stochastic Forest** — the label used in Tables 1 and 2 and in the abstract for the random forest model (Sect. 4.1).
- **XGBoost** — Boosting ensemble method fitting an additive model of decision trees with a loss function plus a regularisation term; the best-performing model on all five indicators.
- **AUC** — area under the ROC curve; "the closer it is to 1, the better," measuring the model's ability to rank positive samples above negative samples (Sect. 4.1).
- **F1 score** — the harmonic mean of precision and recall, used for comprehensive evaluation (Sect. 4.1).
- **Gini coefficient** — impurity measure used to select the optimal splitting feature when growing a single decision tree (Eq. 3, Sect. 3.3).
- **Online Retail dataset** — the public UCI machine-learning repository dataset used for all experiments, described as cross-border transactions of one online retail company from 1 December 2020 to 9 December 2021.
- **Forecast period** — 1 November to 9 December 2021; customers with at least one purchase in it are positive samples (y=1), all others negative (y=0).
- **Data leakage (as used here)** — the inflation of evaluation results that the by-Customer-ID 7:3 split is designed to prevent by keeping all of one customer's data on one side of the split.

## Key Equations

- `P(y = 1 ∣ x) = 1 / (1 + e^(−(w^T x + b)))` — logistic regression mapping a linear combination of features to a probability through the sigmoid function; x is the feature vector and w and b are weights and bias (Eq. 1, Sect. 3.3).
- `f(x) = sign(Σ_{i=1}^{n} α_i y_i K(x_i, x) + b)` — SVM decision function, with α_i the Lagrange multiplier and K(·,·) the kernel function (this study uses a radial basis kernel) (Eq. 2, Sect. 3.3).
- `Gini(D) = 1 − Σ_{k=1}^{K} (p_k)^2` — Gini coefficient used to choose the optimal splitting feature and minimise node "impurity"; D is the current node sample set, K the number of categories and p_k the proportion of samples in the k-th category (Eq. 3, Sect. 3.3).
- `L^(t) = Σ_{i=1}^{n} l(y_i, ŷ_i^(t−1) + f_t(x_i)) + Ω(f_t)` — XGBoost objective combining a loss function l and a regularisation term Ω(f_t) controlling the complexity of the t-th tree; optimised through second-order Taylor expansion approximation (Eq. 4, Sect. 3.3).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Purchase prediction, logistic regression | accuracy | 0.834 | — | — | Table 1, p. 4 |
| Purchase prediction, logistic regression | precision | 0.701 | — | — | Table 1, p. 4 |
| Purchase prediction, logistic regression | recall | 0.468 | — | — | Table 1, p. 4 |
| Purchase prediction, logistic regression | F1 score | 0.562 | — | — | Table 1, p. 4 |
| Purchase prediction, logistic regression | AUC | 0.792 | — | — | Table 1, p. 4 |
| Purchase prediction, SVM | accuracy | 0.848 | — | — | Table 1, p. 4 |
| Purchase prediction, SVM | precision | 0.732 | — | — | Table 1, p. 4 |
| Purchase prediction, SVM | recall | 0.512 | — | — | Table 1, p. 4 |
| Purchase prediction, SVM | F1 score | 0.602 | — | — | Table 1, p. 4 |
| Purchase prediction, SVM | AUC | 0.821 | — | — | Table 1, p. 4 |
| Purchase prediction, random forest (SF) | accuracy | 0.862 | — | — | Table 1, p. 4 |
| Purchase prediction, random forest (SF) | precision | 0.758 | — | — | Table 1, p. 4 |
| Purchase prediction, random forest (SF) | recall | 0.570 | — | — | Table 1, p. 4 |
| Purchase prediction, random forest (SF) | F1 score | 0.651 | — | — | Table 1, p. 4 |
| Purchase prediction, random forest (SF) | AUC | 0.853 | — | — | Table 1, p. 4 |
| Purchase prediction, XGBoost | accuracy | 0.876 | — | — | Table 1, p. 4 |
| Purchase prediction, XGBoost | precision | 0.781 | — | — | Table 1, p. 4 |
| Purchase prediction, XGBoost | recall | 0.602 | — | — | Table 1, p. 4 |
| Purchase prediction, XGBoost | F1 score | 0.680 | — | — | Table 1, p. 4 |
| Purchase prediction, XGBoost | AUC | 0.872 | — | — | Table 1, p. 4 |
| Model training time, logistic regression | seconds | 0.8 | — | — | Table 2, p. 5 |
| Test-set prediction time, logistic regression | seconds | 0.02 | — | — | Table 2, p. 5 |
| Model training time, SVM | seconds | 125.3 | — | — | Table 2, p. 5 |
| Test-set prediction time, SVM | seconds | 18.7 | — | — | Table 2, p. 5 |
| Model training time, random forest (SF) | seconds | 15.2 | — | — | Table 2, p. 5 |
| Test-set prediction time, random forest (SF) | seconds | 0.35 | — | — | Table 2, p. 5 |
| Model training time, XGBoost | seconds | 9.5 | — | — | Table 2, p. 5 |
| Test-set prediction time, XGBoost | seconds | 0.08 | — | — | Table 2, p. 5 |
| Top-3 predictors, logistic regression (by normalised absolute coefficient) | rank order of features | Recency; Monetary; frequency | — | — | Table 3, p. 5 |
| Top-3 predictors, random forest (SF) (by impurity reduction) | rank order of features | Recency; frequency; Monetary | — | — | Table 3, p. 5 |
| Top-3 predictors, XGBoost (by impurity reduction) | rank order of features | Recency; frequency; average order value | — | — | Table 3, p. 5 |
| XGBoost result restated in the conclusion | F1 score | 0.680 | — | — | Sect. 5 Conclusion, p. 6 |
| XGBoost result restated in the conclusion | AUC | 0.872 | — | — | Sect. 5 Conclusion, p. 6 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study aims to systematically explore and compare the effectiveness of different machine learning algorithms in consumer behavior data mining and analysis." | Abstract, p. 1 | model_performance_evaluation |
| "Focusing on the core task of "prediction of customers' future purchase intention", the research selects four typical algorithms, including logical regression, support vector machine, random forest and XGboost" | Abstract, p. 1 | rule_based_classification |
| "The analysis shows that XGboost algorithm performs best in accuracy, F1 score, AUC and other key indicators, showing a strong ability to deal with complex nonlinear relationships" | Abstract, p. 1 | model_performance_evaluation |
| "This study not only verifies the superiority of ensemble learning in consumer behavior prediction, but also provides empirical basis and selection guidance for enterprises in the trade-off between accuracy, efficiency and interpretability." | Abstract, p. 1 | model_performance_evaluation |
| "This marks a profound transformation of the research paradigm of consumer behavior from causal inference based on sampling survey to correlation mining and predictive analysis based on full data [1]." | Sect. 1 Introduction, p. 2 | data_collection |
| "In view of this, this study aims to empirically compare and deeply analyze four mainstream machine learning algorithms through a rigorous and reproducible data science process." | Sect. 1 Introduction, p. 2 | model_development |
| "This study used the publicly available "Online Retail" dataset from the UCI machine learning repository." | Sect. 3.1, p. 3 | data_collection |
| "The hardware environment for the experiment is an Intel Core i7-12700H processor with 16GB DDR4 memory." | Sect. 3.1, p. 3 | model_development |
| "Based on the customer's historical transaction records, four categories of 28 numerical features were constructed for each customer" | Sect. 3.2.2, p. 3 | model_development |
| "This partitioning ensures that all data from the same client will only appear in one of the training or testing sets, effectively avoiding the problem of model evaluation results being inflated due to data leakage." | Sect. 3.2.1, p. 3 | model_development |
| "When a single decision tree is growing, the Gini coefficient is often used to select the optimal splitting feature to minimize the "impurity" of nodes." | Sect. 3.3, p. 4 | rule_based_classification |
| "Use grid search combined with 5-fold cross validation to optimize key hyperparameters for each model on the training set" | Sect. 3.3, p. 4 | model_development |
| "As can be seen from the table, XGBoost leads in all indicators." | Sect. 4.1, p. 4 | model_performance_evaluation |
| "Logistic regression has the fastest speed, SVM is the slowest, and Random Forest and XGBoost are in between." | Sect. 4.1, p. 5 | model_performance_evaluation |
| "Although the model principles are different, "recent purchase time" is unanimously considered as the primary predictor, verifying the core position of R (proximity) in the RFM framework." | Sect. 4.1, p. 5 | model_development |
| "The training time of SVM far exceeds other models, and its time complexity becomes the main bottleneck in large-scale data, with poor scalability." | Sect. 4.2, p. 6 | model_performance_evaluation |
| "Random forests exhibit excellent accuracy and robustness, while logistic regression holds irreplaceable value in specific scenarios due to its outstanding interpretability and computational efficiency." | Sect. 5 Conclusion, p. 6 | model_performance_evaluation |

## Remember This

- The paper is a four-way classification benchmark on one public transactional dataset: logistic regression, SVM, random forest ("SF") and XGBoost, predicting repeat purchase in a fixed future window.
- XGBoost wins on all five reported indicators; its scores are accuracy 0.876, precision 0.781, recall 0.602, F1 0.680 and AUC 0.872 (Table 1, p. 4).
- Logistic regression has the lowest recall, 0.468, and the fastest times (0.8 s training, 0.02 s prediction); SVM is the slowest (125.3 s training, 18.7 s prediction) (Tables 1 and 2).
- Recency is the top-ranked predictor in every model, which the authors read as data-driven confirmation of the R in RFM (Sect. 4.1, p. 5).
- No sample size, no confidence interval, no p-value and no selected hyperparameter value is ever printed; every comparison is a single point estimate.

## Cited Works

- Li L. (2023) (context) — Data mining and machine learning analysis of e-commerce customers' shopping behaviour. [ref. 1, p. 6]
- Akram N., Aravindhan K., Sujatha K., et al. (2025) (context) — Consumer behaviour prediction using machine-learning algorithms, in a volume on psychology, social innovation and machine-learning applications. [ref. 2, p. 6]
- Lin J. (2025) (context) — Machine learning for predicting consumer behaviour and precision marketing; cited as the source of the Apriori milestone in association-rule mining. [ref. 3, p. 2]
- Ebrahimi P., Basirat M., Yousefi A., et al. (2022) (context) — Social-network marketing and consumer purchase behaviour combining SEM with unsupervised machine learning; cited for the FP-growth algorithm. [ref. 4, p. 2]
- Mohan L., Devarajan M., Alotoum F. J., et al. (2025) (context) — Data analytics for predicting consumer behaviour with machine learning and association-rule mining; cited for sequential pattern mining. [ref. 5, p. 2]
- Chaubey G., Gavhane P. R., Bisen D., et al. (2023) (context) — Customer purchasing-behaviour prediction with classification techniques; cited for K-means clustering and its variants. [ref. 6, p. 2]
- Li H. (2025) (context) — Social-media data mining and online consumer-behaviour analysis; cited for support vector machines in customer classification and sentiment analysis. [ref. 7, p. 2]
- Bhoyar S., Bhoyar P., Shah M. A. (2023) (context) — Machine-learning predictive approach to evaluating consumer behaviour; cited for random forest in churn prediction and credit-risk assessment. [ref. 8, p. 2]
- Abdul Aziz M., Mustakim N. A., Abdul Rahman S. (2024) (context) — Decision tree and rule-based classification for predicting online purchase behaviour in Malaysia; cited for gradient boosting and XGBoost. [ref. 9, p. 2]
- Zvarikova K., Machova V., Nica E. (2022) (context) — Cognitive AI algorithms, movement and behaviour tracking, and customer identification in metaverse commerce; cited alongside ref. 9 for gradient boosting. [ref. 10, p. 2]
- GhorbanTanhaei H., Boozary P., Sheykhan S., et al. (2024) (context) — Predictive analytics in customer behaviour for anticipating trends and preferences; cited for LSTM and its variants on behavioural sequences. [ref. 11, p. 2]
- Xu Z., Zhu G., Metawa N., et al. (2022) (context) — Machine-learning customer brand-equity analysis for marketing behaviour evaluation; cited for deep reinforcement learning in sequential decision-making. [ref. 12, p. 2]