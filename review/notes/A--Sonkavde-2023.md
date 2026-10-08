---
paper_id: A--Sonkavde-2023
first_author: Sonkavde
year: 2023
title: "Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications"
venue: "International Journal of Financial Studies"
doi: 10.3390/ijfs11030094
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_development, model_performance_evaluation, data_collection, sarima]
module_rationale:
  model_algorithm_integration: "The paper builds and tests a stacked ensemble 'Random Forest + XG-Boost + LSTM' combining several algorithms into one forecasting pipeline (Sect. 4, pp. 11-12; Table 1, p. 12)."
  model_development: "Table 1, p. 12 and Sect. 4, pp. 11-15 specify the training/testing split, loss function, optimiser, epochs and grid-search tuning used to build the ensemble."
  model_performance_evaluation: "Table 2, p. 15 reports RMSE and R2 for seven models on two stocks, and Table 3, pp. 15-17 reports accuracy, recall, precision, F1, MSE, MAE, RMSE, MAPE and SMAPE."
  data_collection: "The empirical data source is stated explicitly: 'The dataset for implementation was obtained from Yahoo Finance API' (Sect. 4, p. 13)."
  sarima: "Sect. 2.2.1, p. 7 defines ARIMA as a time-series forecasting method and Table 3, p. 16 reports its RMSE 88.05, MAE 65.88 and MAPE 5.73."
---

# A--Sonkavde-2023 — Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models

## Summary

This is a review article on machine-learning and deep-learning forecasting of stock market prices, published in the *International Journal of Financial Studies*. It surveys supervised and unsupervised machine learning, ensemble learning, classical time-series forecasting, and deep learning architectures — linear regression, KNN, SVM, naïve Bayes, logistic regression, ARIMA, FB Prophet, LSTM, GRU, random forest, XG-Boost, E-SVR-RF, XG-Boost + LSTM, and a blending ensemble (LSTM + GRU) — and then adds an empirical component of its own. The authors implement a stacked ensemble "Random Forest + XG-Boost + LSTM" and benchmark it against SVR, MLPR, KNN, random forest, XG-Boost and LSTM on two Indian chemical-sector stocks, TAINIWALCHM and AGROPHOS, drawn from the Yahoo Finance API. Evaluation uses RMSE and R² (Table 2, p. 15). The ensemble reports the best score on both metrics for both stocks — TANIWALCHM RMSE 2.0247 and R² 0.9921; AGROPHOS RMSE 1.2658 and R² 0.9897 (Table 2, p. 15). A second results table, Table 3 (pp. 15–17), aggregates performance figures reported in the prior literature for fourteen algorithm families. The paper concludes that no universal solution exists for stock price forecasting, that ensemble techniques outperform single models, that hyperparameter tuning is a decisive stage, and that AI forecasts should be used only as additional confirmation indicators rather than as the sole basis for trading decisions.

The contribution the authors foreground is unusual for a review: they explicitly state that they did not stop at summarising, but implemented the surveyed models themselves so that a genuine like-for-like comparison could be shown on the same two datasets. The paper also sets out future research directions — stock trend analysis and classification, pattern identification using computer vision, and candlestick chart pattern analysis using computer vision.

## Problem and Motivation

Stock prices are difficult to predict, and the paper frames this as the reason the review exists. Traditional approaches — primary, fundamental and technical analysis — have inherent limitations because they rely on lagging indicators and produce inaccurate predictions (Sect. 1, p. 2). Machine learning and deep learning are presented as an additional approach that can sit alongside technical and fundamental analysis: "Machine learning serves as an additional approach alongside technical and fundamental analysis, with the combination of these tools forming a powerful trading platform" (Sect. 1, p. 2).

The authors motivate the review on volume grounds: although a significant number of review articles on stock price prediction already exist, "due to the boom in artificial intelligence and machine learning, the frequency of publications has increased considerably" (Sect. 1, p. 2). Their stated contributions are threefold: (a) a description of machine learning and deep learning models used in the financial sector; (b) a generic framework for stock price prediction and classification; and (c) implementation of an ensemble model — Random Forest + XG-Boost + LSTM — for forecasting TAINIWALCHM and AGROPHOS stock prices, with a comparative analysis against popular machine learning and deep learning models (Abstract, p. 1).

The problem is thus both methodological and practical: given the proliferation of forecasting algorithms, which ones actually perform, and under what conditions? The paper's answer is that ensembling plus hyperparameter tuning is the practical route, but that the market's evolution erodes any given method's performance over time (Sect. 6, p. 18).

## Method

**Design.** The paper labels itself a "Review" article (p. 1 header) and repeatedly describes itself as "this comprehensive review" (Abstract, p. 1) and "this review article" (Sect. 1, p. 2); the authors state no formal design label for the empirical component, but describe it as an added implementation exercise — "Extra effort is put into implementing the well-known machine learning and deep learning models to understand their nature and performance" (pp. 2–3). The design is therefore a narrative/systematic literature review with an embedded comparative benchmark experiment on two stock price series.

**Sample.** N = Not reported (the paper does not state the number of price records or trading days in either stock series; the empirical material is two stock price series, TAINIWALCHM from 2014–2023 and AGROPHOS from 2018–2023, retrieved from the Yahoo Finance API); unit of analysis = one listed stock's historical price series. Training/testing split is 80% training and 20% testing (Table 1, p. 12).

**Context.** geography: India (Tainwala Chemicals and Plastics (India) Ltd., Mumbai — TAINIWALCHM; Agro Phos (India) Ltd., Indore — AGROPHOS), both described as belonging to the chemical industry market sector; population: two listed chemical-sector stocks on Indian exchanges, with the literature review additionally covering European (5767 companies, Ballings et al. 2015), Chinese and US stock studies; setting: computational/offline — models implemented in Python using Keras, TensorFlow and sklearn, trained on Yahoo Finance historical price data, with no live trading, no portfolio deployment and no human participants.

The empirical procedure as printed:

- Retrieve historical price data for both stocks from the Yahoo Finance API (Sect. 4, p. 13).
- Preprocess: remove redundancies and null values, then perform feature selection over open, close, adj close and volume (Sect. 3, p. 11).
- Split the data 80% training / 20% testing (Table 1, p. 12).
- Train seven models: SVR, MLPR, KNN, random forest, XG-Boost, LSTM, and the stacked ensemble Random Forest + XG-Boost + LSTM (Table 2, p. 15).
- Configure the ensemble with MSE loss, Adam optimiser, maximum 50 epochs, LSTM layers 2, dropout rate 0.2, dense layer 25 units, batch size 32, and grid search for hyperparameter tuning (Table 1, p. 12).
- Configure random forest over number of estimators [50, 100, 200], maximum depth [3, 5, 7] and maximum features ['sqrt', 'log2'], with grid search (Table 1, p. 12).
- Configure XG-Boost over maximum depth [3, 4, 5], learning rate [0.1, 0.01, 0.001] and number of estimators [50, 100, 150, 500, 1000], with grid search (Table 1, p. 12).
- Evaluate every model with RMSE and R² (Sect. 4, pp. 12–13).
- Present results graphically as forecast-vs-actual panels for each model on each stock (Figures 7 and 8, pp. 13–14) and numerically in Table 2 (p. 15).
- Separately, compile Table 3 (pp. 15–17) from prior studies, listing each algorithm's gap analysis and its performance evaluation as reported by the original authors.

## Software

- Python (version not reported) — "We implemented all of these algorithms using Python programming language" (Sect. 4, p. 12).
- Keras (version not reported).
- TensorFlow (version not reported).
- sklearn (version not reported).
- Grid search for hyperparameter tuning of all three ensemble components (Table 1, p. 12).
- Optimizer: Adam (Table 1, p. 12).
- Loss function: MSE (Table 1, p. 12).
- Maximum epochs: 50 (Table 1, p. 12).
- LSTM configuration: 2 layers, dropout rate 0.2, dense layer 25 units, batch size 32 (Table 1, p. 12).
- Random forest configuration: number of estimators [50, 100, 200], maximum depth [3, 5, 7], maximum features ['sqrt', 'log2'] (Table 1, p. 12).
- XG-Boost configuration: maximum depth [3, 4, 5], learning rate [0.1, 0.01, 0.001], number of estimators [50, 100, 150, 500, 1000] (Table 1, p. 12).
- PyStan — noted as the implementation library for FB Prophet (Sect. 2.2.2, p. 7), not used in the authors' own experiment.

## Key Findings

- The ensemble Random Forest + XG-Boost + LSTM reported the best performance of the seven models on both stocks on both metrics: TANIWALCHM RMSE 2.0247 and R² 0.9921; AGROPHOS RMSE 1.2658 and R² 0.9897 (Table 2, p. 15).
- Random forest reported by far the worst RMSE of the seven models on both stocks — 87.8839 for TANIWALCHM and 98.5633 for AGROPHOS — while simultaneously reporting a high R² (0.9818 and 0.9428 respectively) (Table 2, p. 15). The authors do not comment on this.
- XG-Boost is the strongest single non-ensemble model on RMSE for both stocks: 2.0686 (TANIWALCHM) and 1.7618 (AGROPHOS) (Table 2, p. 15).
- LSTM is the weakest of the deep/single models on RMSE for both stocks: 5.6241 (TANIWALCHM) and 5.2494 (AGROPHOS) (Table 2, p. 15).
- KNN's R² collapses on AGROPHOS to 0.7262, against 0.9311 on TANIWALCHM, while its RMSE is similar across the two (4.4249 vs 4.7877) (Table 2, p. 15).
- The paper states directly that the ensemble was best: "The analysis results in Table 2 indicate that the ensemble algorithm demonstrated the best performance compared to other distinct algorithms'." (Sect. 4, p. 15).
- Hyperparameter tuning is presented as decisive: "the modification of hyperparameters is a crucial stage in the process of stock forecasting as it can maximize the performance of machine learning models" (Sect. 4, p. 15).
- In the aggregated prior-literature table, random forest reports accuracy 80.7, recall 78.3, precision 75.2 and F1 Score 76.7% (0.77) (Table 3, p. 17).
- In the same table, Gaussian naïve Bayes reports accuracy 84, F1 Score 62.44% (0.62), specificity 0.70 and AUC 0.90 (Table 3, p. 16).
- Logistic regression reports accuracy 78.6, recall 76.6, precision 77.8 and F1 Score 77.1% (0.77) (Table 3, p. 16).
- ARIMA reports RMSE 88.05, MAE 65.88 and MAPE 5.73, and RMSE 6.41 when combined with sentiment analysis (Table 3, p. 16).
- FB Prophet reports RMSE 93 (Table 3, p. 16).
- LSTM reports, without sentiment analysis, MAE 48.47, RMSE 55.993 and R-squared 0.867, and with news-sentiment analysis, MAE 17.689, RMSE 23.070 and R-squared 0.867 (Table 3, p. 16).
- GRU reports, without sentiment analysis, MAE 42.8, RMSE 47.31 and R-squared 0.879, and with sentiment analysis, MAE 24.472, RMSE 29.153 and R-squared 0.967 (Table 3, p. 16).
- The paper reports that XG-Boost outperformed ARIMA and LSTM in a prior study (Sect. 2, p. 3), and that adding multimodal data raised accuracy "of up to 18.6% to 89.93% points" in Ren et al. (2019) (Sect. 2, p. 4).
- Khan et al. (2020) achieved 80–98% accuracy using Pyspark, MLlib, linear regression and random forest (Sect. 2, p. 3).
- The paper's overall conclusion is that no algorithm is universally best: "even today, there is no universal solution to accurately predict the stock price or trend of the market" (Sect. 7, p. 19).
- Ensemble techniques are recommended: "researchers should keep exploring new avenues to solve price action problems using ensemble techniques" (Sect. 7, p. 19).
- Models are positioned as decision support only: "Traders and investment advisors can use machine learning and deep learning models as additional confirmation indicators to support their decisions, and decisions should not rely only on AI-based price forecasting methods" (Sect. 7, p. 19).

## Key Figures and Tables

- Fig. 1 (p. 5): Stock forecasting algorithm — a taxonomy diagram of the algorithms considered in the review, mapping which algorithms are used for stock market prediction across the surveyed research papers.
- Fig. 2 (p. 8): LSTM structure — the cell diagram showing input, forget and output gates, each using the sigmoid activation function.
- Fig. 3 (p. 9): GRU structure — the two-gate (update and reset) diagram contrasting with the three-gate LSTM cell.
- Fig. 4 (p. 10): Random forest — the ensemble-of-decision-trees process, with the four generic steps (pick N random records; build a decision tree on N inputs; pick the number of trees; predict per tree).
- Fig. 5 (p. 10): XG-Boost algorithm — the sequential weak-learner (decision-tree) boosting process with per-iteration gradient-driven weight updates.
- Fig. 6 (p. 11): Workflow of basic ML model — the seven-step generic pipeline from data loading through preprocessing, feature selection, 75/25 train-test split, training, evaluation and hyperparameter fine-tuning.
- Fig. 7 (p. 13): TANIWALCHM stock price forecasting — seven panels, (a) SVR, (b) MLPR, (c) KNN, (d) random forest, (e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM — showing forecast against actual price for the 2014–2023 series.
- Fig. 8 (p. 14): AGROPHOS stock price forecasting — the same seven-panel structure for the AGROPHOS series.
- Table 1 (p. 12): Ensemble model parameter configuration — model type (stacked ensemble), libraries (Keras, TensorFlow, sklearn), algorithms (Random Forest + XG-Boost + LSTM), 80%/20% training/testing split, MSE loss, Adam optimiser, 50 maximum epochs, and the three per-algorithm grid-search configurations.
- Table 2 (p. 15): RMSE and R² scores of algorithms — seven algorithms × two stocks × two metrics; the ensemble is best on RMSE and R² for both stocks.
- Table 3 (pp. 15–17): Summary of existing stock prediction and forecasting algorithms with performance analysis — fourteen algorithm entries (linear regression, SVM, KNN, Gaussian naïve Bayes, logistic regression, ARIMA, FB Prophet, GRU, LSTM, random forest, XG-Boost, E-SVR-RF, XG-Boost + LSTM, blending ensemble LSTM + GRU), each with a gap analysis and a performance evaluation drawn from the cited source.

## Limitations and Gaps

Acknowledged by the authors:

- The authors state that machine learning or deep learning models alone are not sufficient, and that ensemble techniques are capable of providing superior performance (Sect. 5, p. 17).
- The authors state that merely developing a model is not enough and that emphasis should also be placed on hyperparameter tuning (Sect. 5, p. 18).
- The authors state that the stock market evolves over time, so "the approaches developed for handling specific problems will see low performance sooner or later even though their performance is found to be appreciated initially" (Sect. 6, p. 18).
- The authors state that there is no universal solution to accurately predicting stock price or trend, and that AI-based models can fail if not trained efficiently with fresh data (Sect. 7, p. 19).
- The authors state that decisions should not rely only on AI-based price forecasting methods (Sect. 7, p. 19).

[unacknowledged] findings:

- Table 2 reports random forest RMSE of 87.8839 (TANIWALCHM) and 98.5633 (AGROPHOS) against 1.5074–5.6241 for every other model on the same data, while simultaneously reporting random forest R² of 0.9818 and 0.9428 — an internally inconsistent pairing that the paper neither flags nor explains (Table 2, p. 15).
- Table 3 reports E-SVR-RF as having "MAPE = 1.335, MAE = 0.1537, RMSE = 0.0188, and MAE = 0.0485" — the MAE label appears twice with two different values, so the metric set cannot be reconstructed (Table 3, p. 17).
- The paper contradicts itself on the blending ensemble (LSTM + GRU): the running text reports "the lowest RMSE value of 186.32, a precision of 60%, and an F1-score of 66.47" (Sect. 2, p. 4), while Table 3 reports "MSE = 186.32, MPA = 99.65, precision = 60%, Recall = 75%, F1-Score = 66.67%" (Table 3, p. 17). Both numbers are kept in the Statistical Evidence table with their distinct locators; the metric (RMSE vs MSE) and the F1 value (66.47 vs 66.67) differ between the two locations.
- The text describing Figure 8 (AGROPHOS) reads "we have considered the dataset for TAINIWALCHM from the year 2018 to the year 2023" (Sect. 4, p. 14) — the sentence names the wrong stock, so the AGROPHOS sample window is stated under a mislabel.
- The number of price records, trading days or observations in either stock series is never reported, so the effective sample size of the empirical comparison is unknown.
- No confidence interval, standard error, p-value or significance test is reported anywhere for the authors' own Table 2 results, despite these being the paper's headline empirical contribution.
- No train/test split in absolute record counts is given, and no per-fold or repeated-run variance is reported, so the stability of the RMSE and R² values in Table 2 cannot be assessed.
- Table 3 aggregates numbers produced by different studies on different datasets, instruments and time windows, using different metrics — the review presents them in one table without any normalisation, so cross-row comparison is not like-for-like.
- Despite being titled a "systematic review", the paper reports no search strategy, no databases searched, no inclusion/exclusion criteria and no screening or PRISMA-style flow, so the literature selection cannot be reproduced or assessed for bias.
- The paper reports "80–98% accuracy" for Khan et al. (2020) without naming the model or metric variant, and no denominator or dataset description accompanies the figure.
- The empirical evaluation is limited to two stocks in one sector (chemicals) in one country (India), so no claim about generalisation to other sectors or markets is supported by the authors' own results.
- The paper reports only RMSE and R² for its own experiment, with no directional-accuracy, precision, recall or F1 measure, so the comparison against the classification-based rows in Table 3 is not on a common metric.
- No statistical test of the difference between the ensemble and the best single model (XG-Boost) is reported, so the claim that the ensemble "demonstrated the best performance" rests on unsmoothed point estimates (Table 2, p. 15).
- Section 3 specifies a 75%/25% train-test split in the generic pipeline (p. 11) while Table 1 specifies 80%/20% for the actual experiment (p. 12); the paper does not reconcile the two.

## Definitions

- **Linear regression** — a model that simulates the linear relationship between dependent and independent variables and produces a best-fit line, drawn so that the sum of squared differences between each data point and the line is as small as possible (Sect. 2.1.1, p. 5).
- **KNN (K-Nearest Neighbor)** — a classification and regression technique described as a "lazy learner" because it does not need a long learning period; it requires only the value of K and the Euclidean distance (Sect. 2.1.2, p. 6).
- **SVM (Support Vector Machine)** — supervised learning used to categorise aspects using a separator; data are mapped to a high-dimensional feature space and grouped by their location relative to the optimal hyperplane (Sect. 2.1.3, p. 6).
- **Naïve Bayes** — a classification algorithm in which a combination of probabilities summing the frequencies and value combinations is taken from a dataset; its basic concept is that attribute values are independent in the presence of an output value (Sect. 2.1.4, p. 6).
- **Logistic regression** — a supervised method that groups independent factors into two or more mutually exclusive groups using logistic-curve variables and forecasts the likelihood of equities that perform well (Sect. 2.1.5, p. 7).
- **ARIMA** — a time-series forecasting algorithm comprising three steps — identify, estimate, diagnose — combining autoregression (AR) and moving average (MA) (Sect. 2.2.1, p. 7).
- **FB Prophet** — a time-series forecasting library developed by Facebook, described as better suited to data with null values, decomposing a series into linear trend, seasonal patterns, holiday effects and white-noise error (Sect. 2.2.2, p. 7).
- **LSTM (Long Short-Term Memory)** — an advanced model of recurrent neural networks comprising three gates (input, forget, output), all using the sigmoid activation function, able to handle lengthy sequences by remembering the data sequence (Sect. 2.3.1, p. 8).
- **GRU (Gated Recurrent Neural Network)** — an RNN-based model with only two gates (reset and update), computationally efficient and faster to train than LSTM while capturing long-term dependencies (Sect. 2.3.2, pp. 8–9).
- **Random forest** — a supervised ensemble-learning method derived from the decision-tree concept that creates several decision trees to provide results, working for both classification and regression (Sect. 2.4.1, p. 9).
- **XG-Boost** — an ensembled machine learning algorithm combining weak learners such as decision trees in a sequential model that considers the gradient for each iteration so that weights are updated per decision-tree iteration (Sect. 2.4.2, p. 10).
- **E-SVR-RF** — ensemble support vector regression with random forest, following the bagging method, combining a support vector regressor and random forest by weighted average (Sect. 2.4.3, p. 10).
- **Stacking vs blending** — cooperative and competitive classifier algorithms use stacking and blending; bagging and boosting techniques are used to reduce variance and bias (Sect. 2, p. 3).
- **RMSE / R² / MAE / MSE / MAPE / SMAPE** — the regression evaluation metrics reported throughout; RMSE and MAPE are named in Sect. 1 (p. 2) as the preferred metrics for regression or price forecasting models.

## Key Equations

- `O = Sx + K` — linear regression, where O is the output, Sx the slope and K a constant (Equation 1, p. 5).
- `D(hi, pr) = sqrt( Σ(l=1..n) (Pr − hi)² )` — Euclidean distance in KNN, where Pr is the predicted value and hi the data value (Equation 2, p. 6).
- `P(H|U) = (P(U|H) · P(H)) / P(U)` — Bayes posterior probability, where U is unknown class data and H the hypothesis (Equation 3, p. 6).
- `P(Ai = a1 | B = bi) = (1 / sqrt(2π€)) e^(−(ai − µij)² / 2€4ij)` — naïve Bayes as used in stock prediction, where µ is the mean and € the standard deviation (Equation 4, p. 6).
- `Zit = β1 + β2EPSit + β2PBit + β2ROEit + β2CRit + β2DEit + β2salesit + Vit` — logistic regression maximum likelihood for classifying stock performance (Equation 5, p. 7).
- `y'(t) = k + βp ∗ ωD y'(t−1) + · · · + βp ∗ ωD y'(t−p) + θ1 ∗ ε(t−1) + · · · + θq ∗ ε(ti−q) + εti` — ARIMA, where p is the autoregressive degree, D the degree of differencing and q the moving-average degree (Equation 6, p. 7).
- `Yt = l(t) + sp(t) + v(t) + εt , yt = g(t) + s(t) + h(t) + εn` — FB Prophet, where l(t) is the linear trend, sp(t) seasonal patterns, v(t) holiday effects and εn white-noise error (Equation 7, p. 7).
- `iga = σ(Wip [ht−1, Xc] + bi)` — LSTM input gate (Equation 8, p. 8).
- `fga = σ(Wfg [ht−1, Xc] + bf)` — LSTM forget gate (Equation 9, p. 8).
- `Opg = σ(Wop [ht−1, Xc] + bo)` — LSTM output gate (Equation 10, p. 8).
- `Z[t] = σ(W(z)xt + U(z)ht−1)` — GRU update gate (Equation 11, p. 9).
- `r[t] = σ(W(r)xt + U(r)ht−1)` — GRU reset gate (Equation 12, p. 9).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TANIWALCHM stock price forecasting, SVR | RMSE | 4.525 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, SVR | R2 | 0.9279 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, MLPR | RMSE | 2.5893 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, MLPR | R2 | 0.9611 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, KNN | RMSE | 4.4249 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, KNN | R2 | 0.9311 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, LSTM | RMSE | 5.6241 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, LSTM | R2 | 0.8867 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, random forest | RMSE | 87.8839 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, random forest | R2 | 0.9818 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, XG-Boost | RMSE | 2.0686 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, XG-Boost | R2 | 0.9842 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, ensemble Random Forest + XG-Boost + LSTM | RMSE | 2.0247 | — | — | Table 2, p. 15 |
| TANIWALCHM stock price forecasting, ensemble Random Forest + XG-Boost + LSTM | R2 | 0.9921 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, SVR | RMSE | 1.5074 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, SVR | R2 | 0.9432 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, MLPR | RMSE | 2.4764 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, MLPR | R2 | 0.9472 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, KNN | RMSE | 4.7877 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, KNN | R2 | 0.7262 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, LSTM | RMSE | 5.2494 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, LSTM | R2 | 0.8809 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, random forest | RMSE | 98.5633 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, random forest | R2 | 0.9428 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, XG-Boost | RMSE | 1.7618 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, XG-Boost | R2 | 0.9379 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, ensemble Random Forest + XG-Boost + LSTM | RMSE | 1.2658 | — | — | Table 2, p. 15 |
| AGROPHOS stock price forecasting, ensemble Random Forest + XG-Boost + LSTM | R2 | 0.9897 | — | — | Table 2, p. 15 |
| Linear regression, prior study (Gururaj et al. 2019) | RMSE | 3.22 | — | — | Table 3, p. 15 |
| Linear regression, prior study (Gururaj et al. 2019) | MAE | 2.53 | — | — | Table 3, p. 15 |
| Linear regression, prior study (Gururaj et al. 2019) | MSE | 10.37 | — | — | Table 3, p. 15 |
| Linear regression, prior study (Gururaj et al. 2019) | R-squared | 0.73 | — | — | Table 3, p. 15 |
| Support vector machine classification, prior study | accuracy | 68.2 | — | — | Table 3, p. 15 |
| Support vector machine classification, prior study | recall | 65.2 | — | — | Table 3, p. 15 |
| Support vector machine classification, prior study | precision | 64.2 | — | — | Table 3, p. 15 |
| Support vector machine classification, prior study | F1-Score | 64.9% (0.65) | — | — | Table 3, p. 15 |
| Support vector regression (SVR), prior study | SMAPE | 5.59 | — | — | Table 3, p. 15 |
| Support vector regression (SVR), prior study | R-squared | 1.69 | — | — | Table 3, p. 15 |
| Support vector regression (SVR), prior study | RMSE | 43.36 | — | — | Table 3, p. 15 |
| K-nearest neighbor classification, prior study | accuracy | 65.2 | — | — | Table 3, p. 15 |
| K-nearest neighbor classification, prior study | recall | 63.6 | — | — | Table 3, p. 15 |
| K-nearest neighbor classification, prior study | precision | 64.8 | — | — | Table 3, p. 15 |
| K-nearest neighbor classification, prior study | F1 Score | 64.1% (0.64) | — | — | Table 3, p. 15 |
| KNN regressor, prior study | SMAPE | 14.32 | — | — | Table 3, p. 15 |
| KNN regressor, prior study | R-squared | −2.42 | — | — | Table 3, p. 15 |
| KNN regressor, prior study | RMSE | 56.44 | — | — | Table 3, p. 15 |
| Gaussian naïve Bayes, prior study (Bansal et al. 2022) | accuracy | 84 | — | — | Table 3, p. 16 |
| Gaussian naïve Bayes, prior study (Bansal et al. 2022) | F1 Score | 62.44% (0.62) | — | — | Table 3, p. 16 |
| Gaussian naïve Bayes, prior study (Bansal et al. 2022) | specificity | 0.70 | — | — | Table 3, p. 16 |
| Gaussian naïve Bayes, prior study (Bansal et al. 2022) | AUC | 0.90 | — | — | Table 3, p. 16 |
| Logistic regression, prior study | accuracy | 78.6 | — | — | Table 3, p. 16 |
| Logistic regression, prior study | recall | 76.6 | — | — | Table 3, p. 16 |
| Logistic regression, prior study | precision | 77.8 | — | — | Table 3, p. 16 |
| Logistic regression, prior study | F1 Score | 77.1% (0.77) | — | — | Table 3, p. 16 |
| ARIMA, prior study (Kedar 2021) | RMSE | 88.05 | — | — | Table 3, p. 16 |
| ARIMA, prior study (Kedar 2021) | MAE | 65.88 | — | — | Table 3, p. 16 |
| ARIMA, prior study (Kedar 2021) | MAPE | 5.73 | — | — | Table 3, p. 16 |
| ARIMA with sentiment analysis, prior study (Kedar 2021) | RMSE | 6.41 | — | — | Table 3, p. 16 |
| FB Prophet, prior study (Suresh et al. 2022; Kaninde et al. 2022) | RMSE | 93 | — | — | Table 3, p. 16 |
| GRU without sentiment analysis, prior study (Shahi et al. 2020) | MAE | 42.8 | — | — | Table 3, p. 16 |
| GRU without sentiment analysis, prior study (Shahi et al. 2020) | RMSE | 47.31 | — | — | Table 3, p. 16 |
| GRU without sentiment analysis, prior study (Shahi et al. 2020) | R-squared | 0.879 | — | — | Table 3, p. 16 |
| GRU with sentiment analysis, prior study (Shahi et al. 2020) | MAE | 24.472 | — | — | Table 3, p. 16 |
| GRU with sentiment analysis, prior study (Shahi et al. 2020) | RMSE | 29.153 | — | — | Table 3, p. 16 |
| GRU with sentiment analysis, prior study (Shahi et al. 2020) | R-squared | 0.967 | — | — | Table 3, p. 16 |
| LSTM without sentiment analysis, prior study (Shahi et al. 2020) | MAE | 48.47 | — | — | Table 3, p. 16 |
| LSTM without sentiment analysis, prior study (Shahi et al. 2020) | RMSE | 55.993 | — | — | Table 3, p. 16 |
| LSTM without sentiment analysis, prior study (Shahi et al. 2020) | R-squared | 0.867 | — | — | Table 3, p. 16 |
| LSTM with sentiment analysis, prior study (Shahi et al. 2020) | MAE | 17.689 | — | — | Table 3, p. 16 |
| LSTM with sentiment analysis, prior study (Shahi et al. 2020) | RMSE | 23.070 | — | — | Table 3, p. 16 |
| LSTM with sentiment analysis, prior study (Shahi et al. 2020) | R-squared | 0.867 | — | — | Table 3, p. 16 |
| Random forest, prior study (Pathak and Pathak 2020; Polamuri et al. 2019) | accuracy | 80.7 | — | — | Table 3, p. 17 |
| Random forest, prior study (Pathak and Pathak 2020; Polamuri et al. 2019) | recall | 78.3 | — | — | Table 3, p. 17 |
| Random forest, prior study (Pathak and Pathak 2020; Polamuri et al. 2019) | precision | 75.2 | — | — | Table 3, p. 17 |
| Random forest, prior study (Pathak and Pathak 2020; Polamuri et al. 2019) | F1 Score | 76.7% (0.77) | — | — | Table 3, p. 17 |
| XG-Boost, prior study (Zhu and He 2022) | MSE | 360.0 | — | — | Table 3, p. 17 |
| E-SVR-RF, prior study (Xu et al. 2020) | MAPE | 1.335 | — | — | Table 3, p. 17 |
| E-SVR-RF, prior study (Xu et al. 2020) | MAE | 0.1537 | — | — | Table 3, p. 17 |
| E-SVR-RF, prior study (Xu et al. 2020) | RMSE | 0.0188 | — | — | Table 3, p. 17 |
| E-SVR-RF, prior study (Xu et al. 2020) | MAE (second value printed under the same label) | 0.0485 | — | — | Table 3, p. 17 |
| XG-Boost + LSTM, prior study (Vuong et al. 2022) | MSE | 3.465 | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study (Li and Pan 2021) | MSE | 186.32 | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study (Li and Pan 2021) | MPA | 99.65 | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study (Li and Pan 2021) | precision | 60% | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study (Li and Pan 2021) | Recall | 75% | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study (Li and Pan 2021) | F1-Score | 66.67% | — | — | Table 3, p. 17 |
| Blending ensemble (LSTM + GRU), prior study, as reported in the running text (Li and Pan 2021) | RMSE | 186.32 | — | — | Sect. 2, p. 4 |
| Blending ensemble (LSTM + GRU), prior study, as reported in the running text (Li and Pan 2021) | precision | 60% | — | — | Sect. 2, p. 4 |
| Blending ensemble (LSTM + GRU), prior study, as reported in the running text (Li and Pan 2021) | F1-score | 66.47 | — | — | Sect. 2, p. 4 |
| Khan et al. (2020) stock prediction using Pyspark, MLlib, linear regression and random forest | accuracy | 80–98% | — | — | Sect. 2, p. 3 |
| Multimodal (price + news text) forecasting, prior study (Ren et al. 2019) | accuracy increase | 18.6% to 89.93% points | — | — | Sect. 2, p. 4 |
| Comparative evaluation of classifiers on European companies, prior study (Ballings et al. 2015) | number of companies compared | 5767 | — | — | Sect. 2, p. 3 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Extra effort is put into implementing the well-known machine learning and deep learning models to understand their nature and performance." | Sect. 1, pp. 2-3 | model_development |
| "The dataset for implementation was obtained from Yahoo Finance API, and we considered the dataset for TAINIWALCHM from the year 2014 to the year 2023." | Sect. 4, p. 13 | data_collection |
| "Gradient boosting is a top choice algorithm for classification and regression predictive modeling projects because it often achieves the best performance, but it takes lot of time to converge to the solution." | Sect. 4, p. 12 | model_algorithm_integration |
| "In order to achieve the best performance in stock price forecasting, the LSTM is combined in this model due to its capability of storing past information." | Sect. 4, p. 12 | model_algorithm_integration |
| "The analysis results in Table 2 indicate that the ensemble algorithm demonstrated the best performance compared to other distinct algorithms'." | Sect. 4, p. 15 | model_performance_evaluation |
| "From this study and experimental analysis, we observed that the modification of hyperparameters is a crucial stage in the process of stock forecasting as it can maximize the performance of machine learning models." | Sect. 4, p. 15 | model_development |
| "ARIMA can be considered because it is a unique model with significant coefficients and passes all the diagnostic tests" | Table 3, p. 16 | sarima |
| "The result without sentiment analysis are MAE = 48.47, RMSE = 55.993, and R-squared = 0.867" | Table 3, p. 16 | model_performance_evaluation |
| "This is one of the most used ML algorithms for stock forecasting, and when used along with sentiment analysis, it shows better results than without sentiment analysis." | Table 3, p. 16 | model_performance_evaluation |
| "XG-Boost is sensitive to hyperparameters and will not work as well on large datasets as random forest" | Table 3, p. 17 | model_performance_evaluation |
| "The model's use of a huge number of trees slows it down, which is a drawback" | Table 3, p. 17 | model_performance_evaluation |
| "Despite the existence of several popular methods for stock price forecasting, even today, there is no universal solution to accurately predict the stock price or trend of the market." | Sect. 7, p. 19 | model_performance_evaluation |
| "There is still a possibility that AI-based models can also fail if they are not trained efficiently with fresh data." | Sect. 7, p. 19 | model_development |
| "Traders and investment advisors can use machine learning and deep learning models as additional confirmation indicators to support their decisions, and decisions should not rely only on AI-based price forecasting methods." | Sect. 7, p. 19 | model_algorithm_integration |
| "It is said that the stock market evolves over a period of time, and hence, the approaches developed for handling specific problems will see low performance sooner or later" | Sect. 6, p. 18 | model_performance_evaluation |

## Remember This

- This is a review article with an embedded benchmark: seven models — SVR, MLPR, KNN, LSTM, random forest, XG-Boost and a stacked Random Forest + XG-Boost + LSTM ensemble — compared on two Indian chemical-sector stocks.
- The ensemble reports the best RMSE and R² on both stocks: TANIWALCHM 2.0247 / 0.9921; AGROPHOS 1.2658 / 0.9897 (Table 2, p. 15).
- Random forest reports RMSE 87.8839 (TANIWALCHM) and 98.5633 (AGROPHOS) against 1.5–5.6 for every other model, while its R² stays high at 0.9818 and 0.9428 — an unflagged internal inconsistency (Table 2, p. 15).
- The paper contradicts itself on the LSTM + GRU blending ensemble: RMSE 186.32 with F1 66.47 in the text (p. 4) versus MSE 186.32 with F1 66.67 in Table 3 (p. 17).
- Table 3 aggregates fourteen algorithm families' reported metrics from prior studies on heterogeneous datasets — it is a literature summary, not a controlled comparison.
- The paper reports no confidence intervals, no p-values and no significance tests anywhere.
- The dataset windows are stated as TAINIWALCHM 2014–2023 and AGROPHOS 2018–2023, but the AGROPHOS sentence names the wrong stock; the number of price records is never reported.
- Headline conclusion: ensemble plus hyperparameter tuning beats single models, but there is no universal solution and AI forecasts should serve only as confirmation indicators.

## Cited Works

- Gururaj, V.; Shriya, V. R.; Ashwini, K. (2019) (baseline) — Linear regression and SVM applied to stock market prediction; supplies the linear regression row in Table 3 with RMSE 3.22, MAE 2.53, MSE 10.37 and R-squared 0.73. [p. 15]
- Pathak, A.; Pathak, S. (2020) (baseline) — Study of machine learning algorithms for stock market prediction; supplies SVM, KNN, logistic regression and random forest rows in Table 3. [pp. 15–17]
- Grigoryan, H. (2017) (baseline) — Support vector machines with variable selection for stock market trend prediction; source of the SVM and SVR rows. [p. 15]
- Tanuwijaya, J.; Hansun, S. (2019) (baseline) — KNN regression on the LQ45 stock index; source of the KNN regressor metrics. [p. 15]
- Venkat, P. (2022) (baseline) — K-nearest neighbor algorithm for stock market trend prediction; source of KNN regressor SMAPE, R-squared and RMSE. [p. 15]
- Setiani, I.; Tentua, M. N.; Oyama, S. (2020) (baseline) — Naïve Bayes prediction of banking stock prices. [p. 16]
- Ampomah, E. K.; Nyame, G.; Qin, Z.; Addo, P. C.; Gyamfi, E. O.; Gyan, M. (2021) (baseline) — Gaussian naïve Bayes machine learning for stock market prediction; supplies the GNB accuracy and F1 rows. [p. 16]
- Bansal, M.; Goyal, A.; Choudhary, A. (2022) (baseline) — High-accuracy stock market prediction with machine learning; source of accuracy 84, F1 62.44%, specificity 0.70 and AUC 0.90. [p. 16]
- Ali, S. S.; Mubeen, M.; Hussain, A. (2018) (baseline) — Logistic regression for stock performance on the Pakistan Stock Exchange; supplies the logistic regression row. [p. 16]
- Mashadihasanli, T. (2022) (baseline) — ARIMA applied to the Istanbul stock market; the paper's justification that ARIMA "passes all the diagnostic tests". [p. 16]
- Kedar, S. V. (2021) (baseline) — Twitter sentiment analysis combined with ARIMA; source of ARIMA RMSE 88.05, MAE 65.88, MAPE 5.73 and the sentiment RMSE 6.41. [p. 16]
- Suresh, N.; Priya, B.; Lakshmi, G. (2022) (baseline) — Historical analysis and forecasting of the stock market using FB Prophet; source of the FB Prophet RMSE 93. [p. 16]
- Kaninde, S.; Mahajan, M.; Janghale, A.; Joshi, B. (2022) (baseline) — Stock price prediction using Facebook Prophet. [p. 16]
- Shahi, T. B.; Shrestha, A.; Neupane, A.; Guo, W. (2020) (baseline) — Comparative study of deep learning for stock price forecasting; source of the GRU and LSTM with/without sentiment metric sets. [p. 16]
- Pramod, B. S.; Pm, M. S. (2021) (baseline) — Stock price prediction using LSTM; cited for LSTM memory and weight adjustment. [p. 16]
- Mukherjee, S.; Sadhukhan, B.; Sarkar, N.; Roy, D.; De, S. (2021) (baseline) — Stock market prediction using deep learning algorithms; cited for LSTM error stability. [p. 16]
- Polamuri, S. R.; Srinivas, K.; Mohan, A. K. (2019) (baseline) — Stock market prices prediction using random forest and extra tree regression; source of the random forest metrics. [p. 17]
- Zhu, Z.; He, K. (2022) (baseline) — Prediction of Amazon's stock price with ARIMA, XGBoost and LSTM; source of the XG-Boost MSE 360.0 and the finding that XG-Boost outperformed ARIMA and LSTM. [pp. 3, 17]
- Xu, Y.; Yang, C.; Peng, S.; Nojima, Y. (2020) (baseline) — Hybrid two-stage financial stock forecasting with clustering and ensemble learning; source of the E-SVR-RF metrics. [p. 17]
- Vuong, P. H.; Dat, T. T.; Mai, T. K.; Uyen, P. H. (2022) (baseline) — Stock-price forecasting based on XGBoost and LSTM; source of the XG-Boost + LSTM MSE 3.465. [p. 17]
- Li, Y.; Pan, Y. (2021) (baseline) — Novel ensemble deep learning model for stock prediction based on prices and news; source of the blending ensemble LSTM + GRU metrics, which are reported inconsistently between text and table. [pp. 4, 17]
- Ballings, M.; Van den Poel, D.; Hespeels, N.; Gryp, R. (2015) (context) — Evaluation of multiple classifiers for stock price direction prediction on 5767 European companies; random forest found best, followed by SVM. [p. 3]
- Khan, W.; Ghazanfar, M. A.; Azam, M. A.; Karami, A.; Alyoubi, K. H.; Alfakeeh, A. S. (2020) (context) — Stock market prediction using machine learning classifiers, social media and news; reported 80–98% accuracy. [p. 3]
- Ren, R.; Wu, D. D.; Liu, T. (2019) (context) — Forecasting stock market movement direction using sentiment analysis and SVM; reported accuracy increase of up to 18.6% to 89.93% points with multimodal data. [p. 4]
- Di Persio, L.; Honchar, O. (2017) (methodology) — Recurrent neural networks for forecasting Google assets; source of the RNN/LSTM/GRU comparison and the GRU input-output description. [pp. 3, 9]
- Zhang, Z.; et al. — Not applicable (the reference list does not contain a Zhang et al. entry; omitted).
- Lim, K.-P.; Brooks, R. (2011) (context) — Survey of the evolution of stock market efficiency over time; cited for the claim that the stock market evolves and methods degrade. [p. 18]
- Barra, S.; Carta, S. M.; Corriga, A.; Podda, A. S.; Reforgiato Recupero, D. (2020) (methodology) — Deep learning and time-series-to-image encoding for financial forecasting; cited in the pattern-identification future direction. [p. 18]
- Cagliero, L.; Fior, J.; Garza, P. (2023) (methodology) — Shortlisting machine learning-based stock trading recommendations using candlestick pattern recognition. [p. 18]
- Jiang, W. (2021) (context) — Applications of deep learning in stock market prediction: recent progress; cited in the trend-analysis future direction. [p. 18]
- Nikou, M.; Mansourfar, G.; Bagherzadeh, J. (2019) (baseline) — Stock price prediction using deep learning compared with machine learning algorithms. [p. 18]
- Obthong, M.; Tantisantiwong, N.; Jeamwatthanachai, W.; Wills, G. (2020) (context) — Survey on machine learning for stock price prediction: algorithms and techniques. [p. 1]