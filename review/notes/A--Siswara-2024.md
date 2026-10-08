---
paper_id: A--Siswara-2024
first_author: Siswara
year: 2024
title: "Classification Modeling with RNN-based, Random Forest, and XGBoost for Imbalanced Data: A Case of Early Crash Detection in ASEAN-5 Stock Markets"
venue: "Scientific Journal of Informatics"
doi: Not reported
designation: algorithm
status: extracted
modules: []
module_rationale: {}
---

# A--Siswara-2024

## Summary

This paper evaluates the performance of Recurrent Neural Network (RNN) architectures — Simple RNN, Gated Recurrent Units (GRU), and Long Short-Term Memory (LSTM) — against classic machine learning algorithms (Random Forest and XGBoost) for early crash detection in the ASEAN-5 stock markets. The study analyzes daily stock price data from 2010 to 2023 across Indonesia, Malaysia, Singapore, Thailand, and the Philippines. A market crash is defined as the primary stock price index falling below Value at Risk (VaR) thresholds of 5%, 2.5%, and 1%, producing binary classification targets. The study incorporates 213 predictors derived from technical indicators, global markets, commodities, and currency exchange rates; with a time step of 7 (X_{t-1} to X_{t-7}), the total expands to 1,491 predictors per dataset. Class imbalance is addressed with SMOTE-ENN. Models are evaluated using the inverted false alarm rate, hit rate, balanced accuracy, and the precision-recall curve (PRC) score. Results indicate that RNN-based architectures outperform Random Forest and XGBoost across the three VaR scenarios. Among RNN variants, Simple RNN is the most superior, attributed to the datasets' relatively simple characteristics and the model's focus on short-term information. The paper reports an overall hit rate interval of 0%–64% with an average of 21%, and a balanced accuracy of 64% for the best model.

## Problem and Motivation

Early crash detection in financial markets is critical for risk management and investment strategies. Predicting sudden and substantial price drops — known as market crashes — is paramount for investors, financial institutions, and regulators. Crashes are rare, unexpected events like the 2007 subprime mortgage crisis or the 2020 COVID-19 pandemic. Early warning of these events can mitigate potential losses. Deep learning models, particularly RNNs, are well-suited for early crash detection because they excel at predicting patterns in sequential data. A significant research gap exists in predicting substantial and unusual price drops (market crashes) compared to modeling general price movements. Most existing studies focus on predicting whether stock prices will go up or down, a binary trend prediction, rather than detecting crashes. The rarity of market crashes leads to imbalanced target data classes, which this study also addresses. Random Forest and XGBoost are employed for comparative analysis, with XGBoost noted for its robust handling of imbalanced data classes.

## Method

**Design.** Comparative computational modeling study; the authors state no formal design label.
**Sample.** 15 datasets (5 ASEAN-5 countries × 3 VaR scenarios); the unit of analysis is daily stock market index data from 2010–2023.
**Context.** geography: ASEAN-5 (Indonesia, Malaysia, Philippines, Singapore, Thailand); population: daily stock price indices and technical indicators from local and global markets; setting: computational/offline analysis using Python, TensorFlow, Scikit-learn, and XGBoost library on a local machine (12th Gen Intel Core i5-1240P, 16.0 GB DDR5 RAM, Windows 11 Home, Generation 4 SSD).

- Collect daily stock price data from Yahoo Finance for the five largest ASEAN-5 stock markets from 2010 to 2023; data are irregular due to weekday-only trading.
- Define market crash as a binary target variable when the primary stock price index falls below VaR thresholds of 5%, 2.5%, and 1%.
- Form 15 datasets (5 markets × 3 VaR scenarios).
- Construct predictor variables from technical indicators: return, moving average (MA), exponential moving average (EMA), opening-closing price difference, relative strength index (RSI), and moving average convergence divergence (MACD).
- Include global market indicators (DJI, NASDAQ, EURO, JPAN, FAN), commodities (crude oil, gold, bonds), and currency exchange rates relative to the US dollar.
- Expand MA and EMA into lags of 5, 10, 15, 20, 22, 50, and 200 days, resulting in 213 predictors.
- Apply time steps of 7 (X_{t-1} to X_{t-7}), expanding to 1,491 predictors per dataset; the current time point X_t is excluded to enable one-day-ahead prediction.
- Impute missing data with K-Nearest Neighbors (KNN), eliminating variables with >20% missing data.
- Split data into training, validation, and testing using Time Series Cross-Validation (TSCV) with 4 folds; training and validation combined to find optimal hyperparameters, training and testing combined to evaluate final performance.
- Implement Simple RNN, LSTM, and GRU using TensorFlow; Random Forest using Scikit-learn; XGBoost using its library.
- Grid search for hyperparameters: RNN with neuron counts 32/64/128, 1–2 layers, learning rates 0.001/0.01/0.1, up to 50 epochs with early stopping (patience 10 epochs), L1 (1×10^-5) and L2 (1×10^-4) regularization.
- Random Forest: n_estimators 100/200/300, max_depth 10/20/30.
- XGBoost: n_estimators 100/200/300, learning rate 0.01/0.1/0.2, max_depth 3/4/5.
- Run baseline analysis without imbalance handling, then apply SMOTE-ENN to address class imbalance.
- Execute each model on its dataset ten times with regularization strategies to mitigate overfitting.
- Evaluate using inverted false alarm rate, hit rate, balanced accuracy, and AUC-PRC.
- Visualize early crash detection with the best architecture (Simple RNN) for the Indonesian dataset with 1% VaR over 2020–2023.

## Software

- TensorFlow (version not reported) — for Simple RNN, LSTM, and GRU implementation
- Scikit-learn (version not reported) — for Random Forest implementation
- XGBoost library (version not reported)
- Python (version not reported)
- VS Code IDE
- 12th Gen Intel Core i5-1240P processor with 16.0 GB DDR5 RAM
- Windows 11 Home edition
- Generation 4 SSD Storage

## Key Findings

- num: Table 5 reports RNN's average balanced accuracy of 0.626 on the 1% VaR dataset, the highest among all algorithms, with LSTM at 0.600 and GRU at 0.620, compared to RF at 0.488 and XGBoost at 0.512.
- num: On the 2.5% VaR dataset, LSTM has the highest hit rate at 0.366, followed by RNN at 0.362 and GRU at 0.343, while RF achieves only 0.008.
- num: On the 5% VaR dataset, LSTM leads with a hit rate of 0.276, followed by RNN at 0.266 and GRU at 0.260.
- num: XGBoost has the highest false alarm rate on the 1% VaR dataset at 0.987, while RF has the highest on 2.5% and 5% at 0.988 and 0.982 respectively.
- num: The baseline evaluation without SMOTE-ENN showed RNN-based architectures failed to predict crashes (hit rate = 0), with only Random Forest succeeding in the 2.5% VaR scenario.
- num: Overall hit rate interval across all models and datasets is 0%–64%, with an average of 21%.
- num: The conclusion states Simple RNN achieved a balanced accuracy of 64%.
- num: The study compares its hit rate performance to prior work: Chatzis et al. (38%–59%), Moser (45%–71%), Dichtl et al. (9%–50%).
- num: On the Indonesia dataset with 1% VaR, the RNN hit rate did not exceed 50% of total crash incidents.
- num: The paper uses 213 initial predictors expanding to 1,491 after time-step expansion.
- num: SMOTE-ENN is applied to address class imbalance, following Mukhlashin et al. [30].
- The RNN-based architecture is superior because it is well-suited for modeling time dependencies and can handle variable-length sequences in time series data.
- Simple RNN outperforms LSTM and GRU because the datasets may not be overly complex or require extensive processing of long-term historical information.
- On the Thailand dataset with 1% VaR, Random Forest recorded the highest hit rate and balanced accuracy, beating RNN-based models.
- The global financial crisis is the leading cause of crashes in ASEAN-5 stock markets; crashes align with the Chinese Stock Market Crisis (2015–2016), the US Market Sell-Off (2015–2016), and the COVID-19 Pandemic (2020).
- The false alarm rate of RNN-based models is considered within acceptable limits.

## Key Figures and Tables

- Figure 1 (p. 571): Illustration of the VaR threshold — shows how the lowest 5% of returns are classified as crashes.
- Figure 2 (p. 572): Recurrent nodes: gated and non-gated variants — illustrates Simple RNN, LSTM, and GRU node architectures.
- Figure 3 (p. 574): A flowchart of the analysis stages — shows the complete methodology from data collection to visualization.
- Figure 4 (p. 576): The crashes that occurred in the ASEAN-5 stock markets under the 2.5% VaR scenario — shows crash occurrence patterns across countries.
- Figure 5 (p. 577): Performance evaluation on datasets with VaR 1% ASEAN-5 based on metrics (a) Hit Rate, (b) Balance accuracy score, (c) PRC score, and (d) False alarm rate — shows improvement after SMOTE-ENN.
- Figure 6 (p. 578): Performance evaluation on datasets with VaR 1% scenario of each country with metrics (a) Hit rate, (b) Balance accuracy score, (c) PRC score, and (d) False alarm rate — shows country-level variation.
- Figure 7 (p. 579): The early crash detection models for the Indonesian dataset with VaR 1% using Simple RNN architectures during 2020–2023 — shows the model successfully identifying crashes during COVID-19 but failing outside crisis periods.
- Table 1 (p. 572): Metrics evaluation — formulas for inverted false alarm rate, hit rate, balanced accuracy, and PRC scores.
- Table 2 (p. 573): Architecture and grid hyperparameters for each model — detailed hyperparameter search space.
- Table 3 (p. 574): Data partition details — 4-fold TSCV with training/validation/testing periods.
- Table 4 (p. 575): Datasets' crash return thresholds based on VaR scenarios — country-specific thresholds.
- Table 5 (p. 577): Average values of each algorithm's/architecture's performances on every dataset — the main results table.

## Limitations and Gaps

- The authors acknowledge that the hit rate performance is still relatively low, with an overall interval of 0%–64% and an average of 21%, requiring better model and architecture development (Results, p. 578).
- The authors acknowledge that the RNN experienced failures in detecting crashes outside the crisis period, indicating limitations in long-term post-crisis predictions (Results, p. 579).
- The authors acknowledge that future researchers need to capture continuous crash predictions (>1 day) (Results, p. 579).
- The authors acknowledge that developing architectures focusing on RNN-based types, such as bidirectional and stacked techniques, is essential to enhance performance (Results, p. 579).
- The authors acknowledge that for each case and each country's different data characteristics, it is necessary to adjust the basic architecture and model individually (Results, p. 579).
- The authors acknowledge that extending the time steps may allow more comprehensive information storage for evaluating LSTM and GRU models (Results, p. 579).
- [unacknowledged] The paper does not report confidence intervals or p-values for any of the performance metrics in Table 5, so the statistical significance of the model comparisons cannot be assessed.
- [unacknowledged] The paper does not report standard deviations or variances across the ten executions of each model, so the stability of the results is unknown.
- [unacknowledged] The paper does not report precision, recall, or F1 scores for the models, only aggregate averages in Table 5.
- [unacknowledged] The paper uses a local machine (Intel i5-1240P, 16 GB RAM) for training, but does not report training time or computational cost.
- [unacknowledged] The paper does not discuss the practical deployment of the model or how predictions would be used in real-time trading.
- [unacknowledged] The paper does not report the number of observations in each dataset or the exact class distribution after SMOTE-ENN.
- [unacknowledged] The paper does not compare against other imbalanced data handling techniques beyond SMOTE-ENN.
- [unacknowledged] The paper does not report the results of the baseline (without SMOTE-ENN) in tabular form, only mentions them in text.
- [unacknowledged] The paper's Table 5 shows that on the 2.5% VaR dataset, Random Forest achieves a false alarm rate of 0.988, which is the highest among all models on that dataset, yet the text states Random Forest shows the highest false alarm rate in the 2.5% and 5% VaR datasets, indicating a better tendency to reduce false crashes — this is a contradiction in interpretation.
- [unacknowledged] The paper states "XGBoost has the highest false alarm rate in the 1% VaR dataset" but Table 5 shows XGBoost at 0.987, GRU at 0.982, RNN at 0.975, and LSTM at 0.973, so XGBoost does have the highest — this is consistent.

## Definitions

- **VaR (Value at Risk)** — A statistical measure of the level of financial risk over a specific time frame; in this paper, the 5%, 2.5%, and 1% thresholds define the lowest return percentiles considered market crashes.
- **Market crash** — An anomaly or significant price decline that falls outside an investor's risk tolerance; operationalized as the primary stock price index falling below a specified VaR threshold.
- **SMOTE-ENN** — Synthetic Minority Over-sampling Technique combined with Edited Nearest Neighbors; an oversampling method that adds samples to the minority class and a cleaning technique that removes ambiguous or overlapping samples.
- **TSCV (Time Series Cross-Validation)** — A validation method for time series data using sequential folds; training and validation data are combined to find optimal hyperparameters, while training and testing data are combined to evaluate final performance.
- **PRC (Precision-Recall Curve)** — A curve assessing the trade-off between precision and recall, particularly for the minority class; the area under the PRC (AUC-PRC) provides a single measure of overall model performance.
- **Hit rate** — The proportion of correctly predicted crashes among all actual crashes; TP/(TP+FN).
- **Balanced accuracy** — The average of sensitivity and specificity; 1/2 (TP/(TP+FN) + TN/(TN+FP)).
- **False alarm rate** — The frequency of incorrect market crash predictions; in this study, the false alarm rate is inverted (1 − FP/(FP+TN)) to facilitate interpretation.
- **Simple RNN** — The basic architecture of RNNs where each hidden layer is interconnected; often encounters gradient vanishing.
- **LSTM (Long Short-Term Memory)** — An RNN variant that uses a memory cell and three gates (input, output, forget) to preserve long-term information.
- **GRU (Gated Recurrent Unit)** — An RNN variant that merges several LSTM gates into one or two gates, making it more computationally efficient.
- **TSCV K-fold** — The paper uses 4 folds: K=1 (train 2010–2011, validate 2012–2013), K=2 (train 2010–2013, validate 2014–2015), K=3 (train 2010–2015, validate 2016–2019), K=4 (train 2010–2019, validate/test 2020–2023).

## Key Equations

- `Inverted False Alarm Rate = 1 − FP/(FP+TN)` — Table 1, Eq. (1), p. 572
- `Hit Rate = TP/(TP+FN)` — Table 1, Eq. (2), p. 572
- `Balanced Accuracy = 1/2 (TP/(TP+FN) + TN/(TN+FP))` — Table 1, Eq. (3), p. 572
- `Recall = TP/(TP+FN)` — Table 1, Eq. (4), p. 572
- `Precision = TP/(TP+FP)` — Table 1, Eq. (5), p. 572

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Crash detection, Dataset 1% VaR, RNN | False alarm rate | 0.975 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RNN | Hit rate | 0.278 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RNN | Balanced accuracy | 0.626 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RNN | PRC score | 0.072 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, LSTM | False alarm rate | 0.973 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, LSTM | Hit rate | 0.226 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, LSTM | Balanced accuracy | 0.600 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, LSTM | PRC score | 0.058 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, GRU | False alarm rate | 0.982 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, GRU | Hit rate | 0.257 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, GRU | Balanced accuracy | 0.620 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, GRU | PRC score | 0.068 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RF | False alarm rate | 0.850 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RF | Hit rate | 0.126 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RF | Balanced accuracy | 0.488 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, RF | PRC score | 0.015 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, XGBoost | False alarm rate | 0.987 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, XGBoost | Hit rate | 0.038 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, XGBoost | Balanced accuracy | 0.512 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 1% VaR, XGBoost | PRC score | 0.016 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RNN | False alarm rate | 0.853 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RNN | Hit rate | 0.362 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RNN | Balanced accuracy | 0.608 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RNN | PRC score | 0.066 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, LSTM | False alarm rate | 0.834 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, LSTM | Hit rate | 0.366 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, LSTM | Balanced accuracy | 0.600 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, LSTM | PRC score | 0.067 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, GRU | False alarm rate | 0.846 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, GRU | Hit rate | 0.343 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, GRU | Balanced accuracy | 0.594 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, GRU | PRC score | 0.067 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RF | False alarm rate | 0.988 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RF | Hit rate | 0.008 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RF | Balanced accuracy | 0.498 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, RF | PRC score | 0.028 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, XGBoost | False alarm rate | 0.971 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, XGBoost | Hit rate | 0.108 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, XGBoost | Balanced accuracy | 0.539 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 2.5% VaR, XGBoost | PRC score | 0.040 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RNN | False alarm rate | 0.885 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RNN | Hit rate | 0.266 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RNN | Balanced accuracy | 0.575 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RNN | PRC score | 0.074 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, LSTM | False alarm rate | 0.867 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, LSTM | Hit rate | 0.276 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, LSTM | Balanced accuracy | 0.571 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, LSTM | PRC score | 0.067 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, GRU | False alarm rate | 0.902 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, GRU | Hit rate | 0.260 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, GRU | Balanced accuracy | 0.581 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, GRU | PRC score | 0.072 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RF | False alarm rate | 0.982 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RF | Hit rate | 0.064 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RF | Balanced accuracy | 0.523 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, RF | PRC score | 0.059 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, XGBoost | False alarm rate | 0.943 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, XGBoost | Hit rate | 0.149 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, XGBoost | Balanced accuracy | 0.546 | — | — | Table 5, p. 577 |
| Crash detection, Dataset 5% VaR, XGBoost | PRC score | 0.062 | — | — | Table 5, p. 577 |
| Indonesia VaR 5% crash return threshold | Return threshold | -1.62% | — | — | Table 4, p. 575 |
| Indonesia VaR 2.5% crash return threshold | Return threshold | -2.24% | — | — | Table 4, p. 575 |
| Indonesia VaR 1% crash return threshold | Return threshold | -3.13% | — | — | Table 4, p. 575 |
| Malaysia VaR 5% crash return threshold | Return threshold | -1.06% | — | — | Table 4, p. 575 |
| Malaysia VaR 2.5% crash return threshold | Return threshold | -1.36% | — | — | Table 4, p. 575 |
| Malaysia VaR 1% crash return threshold | Return threshold | -1.85% | — | — | Table 4, p. 575 |
| Philippines VaR 5% crash return threshold | Return threshold | -1.70% | — | — | Table 4, p. 575 |
| Philippines VaR 2.5% crash return threshold | Return threshold | -2.25% | — | — | Table 4, p. 575 |
| Philippines VaR 1% crash return threshold | Return threshold | -3.02% | — | — | Table 4, p. 575 |
| Singapore VaR 5% crash return threshold | Return threshold | -1.28% | — | — | Table 4, p. 575 |
| Singapore VaR 2.5% crash return threshold | Return threshold | -1.58% | — | — | Table 4, p. 575 |
| Singapore VaR 1% crash return threshold | Return threshold | -2.22% | — | — | Table 4, p. 575 |
| Thailand VaR 5% crash return threshold | Return threshold | -1.47% | — | — | Table 4, p. 575 |
| Thailand VaR 2.5% crash return threshold | Return threshold | -1.95% | — | — | Table 4, p. 575 |
| Thailand VaR 1% crash return threshold | Return threshold | -2.78% | — | — | Table 4, p. 575 |
| Initial predictor count | Count | 213 | — | — | Methods, p. 571 |
| Total predictor count after time-step expansion | Count | 1,491 | — | — | Methods, p. 571 |
| Time step setting | Time steps | 7 | — | — | Methods, p. 571 |
| Overall hit rate interval across all models | Hit rate | 0%–64% | — | — | Results, p. 578 |
| Overall average hit rate across all models | Hit rate | 21% | — | — | Results, p. 578 |
| Balanced accuracy of Simple RNN (conclusion) | Balanced accuracy | 64% | — | — | Conclusion, p. 579 |
| Baseline RNN hit rate without SMOTE-ENN | Hit rate | 0 | — | — | Results, p. 576 |
| Chatzis et al. hit rate interval | Hit rate | 38%–59% | — | — | Results, p. 578 |
| Moser hit rate interval | Hit rate | 45%–71% | — | — | Results, p. 578 |
| Dichtl et al. hit rate interval | Hit rate | 9%–50% | — | — | Results, p. 578 |
| Indonesia RNN hit rate (visualization) | Hit rate | did not exceed 50% | — | — | Results, p. 579 |
| KNN imputation maximum data generation | Percent of data | 20% | — | — | Methods, p. 574 |
| Maximum training epochs | Epochs | 50 | — | — | Methods, p. 573 |
| Early stopping patience | Epochs | 10 | — | — | Methods, p. 573 |
| L1 regularization coefficient | Coefficient | 1×10^-5 | — | — | Table 2, p. 573 |
| L2 regularization coefficient | Coefficient | 1×10^-4 | — | — | Table 2, p. 573 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This research aims to evaluate the performance of several Recurrent Neural Network (RNN) architectures, including Simple RNN, Gated Recurrent Units (GRU), and Long Short-Term Memory (LSTM), compared to classic algorithms such as Random Forest and XGBoost" | Abstract, p. 569 | model_performance_evaluation |
| "The results indicate that all RNN-based architectures outperform Random Forest and XGBoost." | Abstract, p. 569 | model_performance_evaluation |
| "Among the various RNN architectures, Simple RNN is the most superior, primarily due to its simple data characteristics and focus on short-term information." | Abstract, p. 569 | model_performance_evaluation |
| "The study examines imbalanced data, which is expected due to the rarity of market crashes." | Abstract, p. 569 | model_development |
| "A market crash is the target variable when the primary stock price indices fall below the Value at Risk (VaR) thresholds of 5%, 2.5%, and 1%." | Abstract, p. 569 | data_collection |
| "The study incorporates 213 predictors with their respective lags (5, 10, 15, 22, 50, 200) and uses a time step of 7, expanding the total number of predictors to 1,491." | Abstract, p. 569 | model_development |
| "The challenge of data imbalance is addressed with SMOTE-ENN." | Abstract, p. 569 | model_development |
| "Model performance is evaluated using the false alarm rate, hit rate, balanced accuracy, and the precision-recall curve (PRC) score." | Abstract, p. 569 | model_performance_evaluation |
| "The baseline evaluation revealed that the RNN-based architecture failed to predict stock market crashes (hit rate = 0)." | Results, p. 576 | model_performance_evaluation |
| "The RNN-based architectures (RNN, LSTM, and GRU) demonstrated higher hit rate, balanced accuracy, and PRC scores compared to Random Forest and XGBoost." | Results, p. 577 | model_performance_evaluation |
| "Overall, the performance of the hit rate metric in this study is in the interval of 0%–64%, with an average of 21%." | Results, p. 578 | model_performance_evaluation |
| "The model achieved commendable accuracy metrics, including a balanced accuracy of 64%, and demonstrated a strong capacity to detect significant market downturns, even under the challenging conditions of imbalanced data." | Conclusion, p. 579 | model_performance_evaluation |
| "The RNN experienced several failures in detecting crashes outside the crisis period, indicating limitations in long-term post-crisis predictions." | Results, p. 579 | model_performance_evaluation |
| "Developing an architecture focusing on RNN-based types, such as bidirectional and stacked techniques, is essential to enhance performance." | Results, p. 579 | model_development |
| "Future researchers need to capture continuous crash predictions (>1 day)." | Results, p. 579 | model_development |
| "RNN-based models are more effective than tree-based models in capturing time dynamics." | Results, p. 578 | model_performance_evaluation |
| "This finding suggests that the datasets used in the research might not be overly complex or not require extensive processing of long-term historical information, aligning with the basic capabilities of Simple RNN that prioritize short-term memory." | Results, p. 578 | model_performance_evaluation |
| "On the Thailand dataset with 1% VaR, Random Forest recorded the highest hit rate and balanced accuracy, beating RNN-based." | Results, p. 578 | model_performance_evaluation |
| "The global financial crisis is the leading cause of crashes in the ASEAN-5 stock markets." | Results, p. 575 | data_collection |
| "The use of SMOTE-ENN has been demonstrated to be effective, as evidenced by the research of Mukhlashin et al. [30]." | Methods, p. 573 | model_development |

## Remember This

- The paper compares RNN-based architectures (Simple RNN, GRU, LSTM) against Random Forest and XGBoost for early crash detection in ASEAN-5 stock markets.
- The study uses 15 datasets (5 countries × 3 VaR scenarios) with daily data from 2010 to 2023.
- 213 initial predictors expand to 1,491 with a time step of 7.
- SMOTE-ENN is used to address class imbalance.
- RNN-based architectures outperform Random Forest and XGBoost across all three VaR scenarios.
- Simple RNN is the most superior RNN variant, with a balanced accuracy of 0.626 on the 1% VaR dataset.
- The baseline without SMOTE-ENN showed RNN hit rate = 0.
- Overall hit rate interval is 0%–64%, with an average of 21%.
- The conclusion states Simple RNN achieved a balanced accuracy of 64%.
- On the Thailand dataset with 1% VaR, Random Forest beat RNN-based models.

## Cited Works

- Chatzis, S. P.; Siakoulis, V.; Petropoulos, A.; Stavroulakis, E.; Vlachogiannakis, N. (2018) (benchmark) — Uses neural networks and support vector machines with daily data from 39 countries for stock market-focused research; deep neural networks significantly enhance classification accuracy. [p. 570]
- Moser, R. (2018) (benchmark) — Examined RNN-LSTM models alongside classic machine learning; simpler models can be more effective than complex ones in various scenarios. [p. 570]
- Dichtl, H.; Drobetz, W.; Otto, T. (2023) (benchmark) — Demonstrated that support vector machines are particularly effective in predicting stock market crashes in the Eurozone; hit rate interval 9%–50%. [p. 570]
- Bluwstein, K.; Buckmann, M.; Joseph, A.; Kapadia, S.; Şimşek, Ö. (2023) (context) — Used machine learning to predict recessions; explored financial market rather than specifically targeting the stock market. [p. 570]
- Tölö, E. (2020) (context) — Used RNNs to detect financial crises focusing on a broad range of macroeconomic factors. [p. 570]
- Li, C.; Qian, G. (2022) (context) — Stock price prediction using a frequency decomposition based GRU Transformer neural network. [p. 570]
- Jin, Z.; Yang, Y.; Liu, Y. (2020) (context) — Stock closing price prediction based on sentiment analysis and LSTM. [p. 570]
- Zhao, J.; Zeng, D.; Liang, S.; Kang, H.; Liu, Q. (2021) (context) — Prediction model for stock price trend based on recurrent neural network. [p. 570]
- Mukhlashin, P. A. R.; Fitrianto, A.; Soleh, A. M.; Muhamad, W. Z. A. W. (2023) (methodology) — Ensemble learning with imbalanced data handling in the early detection of capital markets; SMOTE-ENN demonstrated effective. [p. 573]
- Giot, P.; Laurent, S. (2003) (methodology) — Value-at-risk for long and short trading positions. [p. 572]
- Mensi, W.; Ur Rehman, M.; Maitra, D.; Hamed Al-Yahyaee, K.; Sensoy, A. (2020) (context) — Bitcoin co-movement and risk sharing with Sukuk and world and regional Islamic stock markets. [p. 572]
- Zhang, S. (2012) (methodology) — Nearest neighbor selection for iteratively kNN imputation. [p. 574]
- Deng, A. (2023) (methodology) — Time series cross validation: a theoretical result and finite sample performance. [p. 574]
- Jozefowicz, R.; Zaremba, W.; Sutskever, I. (2015) (methodology) — An empirical exploration of Recurrent Network architectures. [p. 572]
- Shewalkar, A.; nyavanandi, D.; Ludwig, S. A. (2019) (methodology) — Performance Evaluation of Deep neural networks Applied to Speech Recognition: RNN, LSTM and GRU. [p. 572]
- Williams, V.; Argyriou, V. (2019) (methodology) — Development of PPTNet a Neural Network for the Rapid Prototyping of Pulsed Plasma Thrusters. [p. 572]
- Zhang, D.; Qian, L.; Mao, B.; Huang, C.; Huang, B.; Si, Y. (2018) (methodology) — A Data-Driven Design for Fault Detection of Wind Turbines Using Random Forests and XGboost. [p. 572]
- Bentéjac, C.; Csörgő, A.; Martínez-Muñoz, G. (2021) (methodology) — A comparative analysis of gradient boosting algorithms. [p. 572]
- Mdegela, L.; Mannens, E.; De Bock, Y.; Leo, J.; Luhanga, E. (2023) (methodology) — Navigating the Kikuletwa River Levels with Deep Learning: An LSTM-Based Approach to Forecasting. [p. 573]
- Zhang, C.; Bengio, S.; Hardt, M.; Recht, B.; Vinyals, O. (2021) (methodology) — Understanding deep learning (still) requires rethinking generalization. [p. 573]
- Anbaee Farimani, S.; Vafaei Jahan, M.; Milani Fard, A.; Tabbakh, S. R. K. (2022) (methodology) — Investigating the informativeness of technical indicators and news sentiment in financial market price prediction. [p. 574]
- Qu, L.; Zhang, M.; Li, Z.; Li, W. (2020) (context) — Temporal Backtracking and Multistep Delay of Traffic Speed Series Prediction. [p. 578]
- Weerakody, P. B.; Wong, K. W.; Wang, G.; Ela, W. (2021) (context) — A review of irregular time series data handling with gated recurrent neural networks. [p. 578]
- Mou, L.; Ghamisi, P.; Zhu, X. X. (2017) (context) — Deep Recurrent Neural Networks for Hyperspectral Image Classification. [p. 578]
- Sherstinsky, A. (2020) (methodology) — Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) network. [p. 578]
- Liu, C.; Zhang, Y.; Sun, J.; Cui, Z.; Wang, K. (2022) (context) — Stacked bidirectional LSTM RNN to evaluate the remaining useful life of supercapacitor. [p. 579]
- Gao, S. et al. (2020) (context) — Short-term runoff prediction with GRU and LSTM networks without requiring time step optimization during sample generation. [p. 579]
- Yuan, Z.; Wang, Y.; Sun, C. (2017) (context) — Construction schedule early warning from the perspective of probability and visualization. [p. 579]
- Cai, Y.; Zhang, N.; Zhang, S. (2023) (context) — GRU and LSTM Based Adaptive Prediction Model of Crude Oil Prices: Post-Covid-19 and Russian Ukraine War. [p. 579]
- Wang, C.; Deng, C.; Wang, S. (2020) (methodology) — Imbalance-XGBoost: leveraging weighted and focal losses for binary label-imbalanced classification with XGBoost. [p. 570]
- Xing, K.; Yang, X. (2019) (context) — How to detect crashes before they burst: Evidence from Chinese stock market. [p. 569]
- Huang, Y.; Kou, G.; Peng, Y. (2017) (context) — Nonlinear manifold learning for early warnings in financial markets. [p. 569]
- Smith, M. F.; Sinha, I.; Lancioni, R.; Forman, H. (1999) (context) — Role of Market Turbulence in Shaping Pricing Strategy. [p. 569]
- Casas, I. (2020) (context) — Networks, Neural. [p. 569]
- DiPietro, R.; Hager, G. D. (2020) (context) — Deep learning: RNNs and LSTM. [p. 569]
- Brownlee, J. (2018) (methodology) — How to Develop LSTM Models for Time Series Forecasting. [p. 569]
- Zhu, R.; Tu, X.; Huang, J. X. (2020) (context) — Deep learning on information retrieval and its applications. [p. 569]
- Ahmadzadeh, E.; Kim, H.; Jeong, O.; Kim, N.; Moon, I. (2022) (methodology) — A Deep Bidirectional LSTM-GRU Network Model for Automated Ciphertext Classification. [p. 570]
- Koors, A.; Page, B. (2012) (methodology) — Transfer and Generalisation of Financial Risk Metrics to Discrete Event Simulation. [p. 571]
- Kyureghian, G.; Capps, O.; Nayga, R. M. (2011) (methodology) — A Missing Variable Imputation Methodology with an Empirical Application. [p. 574]
- Awang Pona, K. Z.; K, K. P. (2021) (methodology) — Hyperparameter Tuning of Deep learning Models in Keras. [p. 574]
- Marcham, F. (1929) (methodology) — Tensorflow: Large-scale Machine Learning on Heterogeneous Distributed Systems. [p. 574]
- Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V.; Thirion, B. (2011) (methodology) — Scikit-learn: Machine Learning in Python. [p. 574]
- Yahoo Finance (methodology) — Data source for all stock market datasets. [p. 570]