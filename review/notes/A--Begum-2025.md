---
paper_id: A--Begum-2025
first_author: Begum
year: 2025
title: "Machine Learning in Financial Risk and Behavior Analysis: Predictive Insights on Bankruptcy, Fraud, and Consumer Trends in the USA"
venue: Not reported
doi: Not reported
designation: algorithm
status: extracted
modules: [model_performance_evaluation, model_algorithm_integration, model_development, data_collection, interquartile_range, savings_debt_management, sarima]
module_rationale:
  model_performance_evaluation: "Reports AUC, F1, precision, recall, MAE, RMSE, silhouette and Davies-Bouldin results across bankruptcy, fraud and consumer-behavior pipelines (Sec. 4.1, pp. 13-16)."
  model_algorithm_integration: "Combines a stacking ensemble (XGBoost + Random Forest + GRU), a hybrid ARIMA-LSTM forecast, and multi-model bankruptcy pipelines (Abstract, p. 1; Sec. 2.4, p. 11)."
  model_development: "Describes training pipelines, hyperparameter tuning via grid and Bayesian search, 5-fold cross-validation and early stopping (Sec. 2.4-2.5, pp. 11-12)."
  data_collection: "Specifies six proprietary and public data sources — bank CRM, payment processor, retail BI, SEC EDGAR, Moody's Analytics and a telecom warehouse (Sec. 2.3, p. 5)."
  interquartile_range: "Uses interquartile range analysis alongside z-score thresholds for outlier detection in preprocessing (Sec. 2.3, p. 6)."
  savings_debt_management: "Bankruptcy prediction uses debt-to-equity and current ratio as key predictors, and frames credit risk as a solvency-management problem (Abstract, p. 1; Sec. 2.3, p. 8)."
  sarima: "Uses ARIMA (non-seasonal) for retail sales and consumer-behavior forecasting and evaluates its MAE and RMSE against LSTM (Sec. 4.1, p. 14)."
---

## Summary

A machine-learning framework for United States financial risk and behavior analysis, applied across three parallel pipelines: bankruptcy prediction (Logistic Regression, Random Forest, Gradient Boosting including XGBoost and LightGBM, SVM, Artificial Neural Networks, and LSTM), fraud detection (Isolation Forest, Logistic Regression, Random Forest, XGBoost, a stacking ensemble, and a GRU-based RNN), and consumer behavior trend analysis (K-Means and DBSCAN clustering alongside ARIMA and LSTM time-series forecasting). The study reports that XGBoost (AUC 0.93) and LightGBM (AUC 0.91) lead bankruptcy prediction, that a stacking ensemble achieves the highest fraud-detection F1 (0.89) and precision (0.91), that a GRU-RNN outperforms static models in fraud recall (0.89 vs. 0.81 for XGBoost), and that LSTM beats ARIMA in consumer forecasting on both MAE (2.8 vs. 4.2) and RMSE (3.3 vs. 5.1). K-Means yields a silhouette score of 0.68; DBSCAN yields a Davies-Bouldin index of 0.52. The paper reports no numbered results tables; all findings appear in running prose and in figure captions.

## Problem and Motivation

Traditional financial risk assessment methods struggle with the nonlinear relationships and high-dimensional patterns of modern financial data. The paper argues that machine learning can convert raw financial datasets into actionable insights supporting proactive risk management. Three problem domains are named: bankruptcy prediction for early-warning systems, fraud detection for real-time anomaly identification in transactional streams, and consumer behavior analysis for personalised marketing and retention. The stated motivation is that existing models lack generalisability and interpretability, that data quality and imbalance remain unresolved, that models cannot adapt in real time, and that domain expertise and ethical frameworks are insufficiently integrated (Sec. 2.2, pp. 4-5). A significant internal inconsistency is present: the stated Research Objectives (Sec. 1.3, p. 3) describe a study of "energy sustainability," "energy demand," "greenhouse gas emissions," and "renewable energy solutions," none of which are pursued anywhere in the paper.

## Method

**Design.** Computational method-development study with comparative benchmark evaluation across three parallel ML pipelines (bankruptcy prediction, fraud detection, consumer behavior analysis); the authors state no formal design label.

**Sample.** Not reported as a total. The paper describes six data sources — a regional bank CRM system, a payment-processor risk-analytics division, an international retail chain's BI platform, SEC EDGAR filings, Moody's Analytics databases, and a tier-one telecom provider's data warehouse — without reporting any of their sizes. The only numeric sample statement is that Figure 1 displays debt-to-equity for 500 synthetic firms.

**Context.** geography: United States (data sources and stated market focus); population: publicly traded US firms (bankruptcy), credit-card transactions (fraud), retail customers (sales), bank and telecom customers (churn); setting: Virtual/computational — offline model training in Python with scikit-learn, XGBoost, LightGBM, TensorFlow/Keras and statsmodels; no live deployment, no human participants.

- Train three pipelines on 80:20 stratified splits with 5-fold cross-validation for hyperparameter tuning.
- For bankruptcy, train six model families: Logistic Regression (L1/L2 penalty tuned over a logarithmic grid), Random Forest, Gradient Boosting (XGBoost and LightGBM variants), SVM (RBF kernel with tuned gamma and C), a three-layer feed-forward neural network with dropout and batch normalization, and an LSTM ingesting historical financial ratios as sequences.
- Calibrate final predictions using Platt scaling or isotonic regression.
- For fraud, train an Isolation Forest unsupervised alongside Logistic Regression, Random Forest and XGBoost, with SMOTE-balanced samples and class-weighted loss functions; blend the supervised predictions through a stacking ensemble with a logistic-regression meta-learner; add a GRU-based RNN on ordered transaction sequences per account.
- For consumer behavior, segment customers with K-Means (k chosen by silhouette analysis and elbow method) and DBSCAN (ε and min_samples chosen by k-distance plots), then forecast aggregated metrics with ARIMA (orders chosen by AIC minimisation) and LSTM, combining forecasts via simple averaging.
- Apply SMOTE for class imbalance, and PCA or Recursive Feature Elimination for dimensionality reduction where needed.
- Compute feature importance scores for tree-based methods and SHAP values for black-box models to validate predictive attributes against domain knowledge.
- Use MLflow for pipeline versioning and log validation scores, confusion matrices, ROC curves, precision-recall curves and residual plots.

## Software

- Python (version not reported)
- scikit-learn (version not reported)
- XGBoost (version not reported)
- LightGBM (version not reported)
- TensorFlow/Keras (version not reported)
- statsmodels (version not reported)
- MLflow (version not reported)

## Key Findings

- Bankruptcy prediction: XGBoost (AUC 0.93) and LightGBM (0.91) lead; LSTM (0.92) and ANN (0.89) follow; Logistic Regression (0.76) lags; LSTM converges faster and to a lower loss than the ANN.
- Fraud detection: Stacking Ensemble achieves the highest F1 (0.89) and precision (0.91); GRU-RNN recall is 0.89 versus 0.81 for XGBoost; Isolation Forest precision is 0.65.
- Consumer behavior forecasting: LSTM achieves lower MAE (2.8 vs. 4.2) and lower RMSE (3.3 vs. 5.1) than ARIMA; ARIMA residuals reach ±4 during volatile sales periods.
- Consumer segmentation: K-Means silhouette score is 0.68; DBSCAN Davies-Bouldin index is 0.52 and is sensitive to ε tuning (ε=1.2 identifies organic clusters and noise effectively).
- The fraud dataset exhibits roughly 2% fraud labels, described as typical of real credit-card data.
- Bankrupt firms show higher Debt/Equity (mean ~1.5 vs. ~0.5 for healthy firms) and Current Ratio clustering around 1.0 (vs. 2.5 for healthy firms); ROA and Profit Margin distributions are left-skewed for bankrupt firms.
- Debt/Equity and Profit Margin are negatively correlated at -0.4; Current Ratio and ROA are weakly correlated at 0.2.
- Bankruptcy status has weak correlations (<0.1) with all numeric metrics, motivating nonlinear modelling.
- The paper reports the LSTM-ARIMA hybrid as the best consumer-forecasting configuration in the discussion (Sec. 4.2, p. 16), though the results section reports the two models separately.

## Key Figures and Tables

The paper contains **no numbered tables**. All results are reported in prose or figure captions. Figures are referenced but the conversion does not render their contents; the descriptions below rest on the paper's own in-text captions and the surrounding prose.

- Figure 1 (p. 7): Bankruptcy Indicator Distributions — debt-to-equity across 500 synthetic firms; heavy right skew.
- Figure 2 (p. 7): Correlation matrix for key financial metrics — net income mildly negatively correlated with debt-to-equity; current ratio and net income near zero; bankruptcy status <0.1 with all numeric metrics.
- Figure 3 (p. 7): Class Imbalance in Fraud Labels — approximately 2% fraud.
- Figure 4 (p. 8): Distribution of Key Financial Ratios — bankrupt vs. healthy Debt/Equity, Current Ratio, ROA, Profit Margin.
- Figure 5 (p. 9): Correlation Matrix of Financial Features — Debt/Equity vs. Profit Margin -0.4; Current Ratio vs. ROA 0.2.
- Figure 6 (p. 9): Transaction Amount Distribution by Class — fraudulent transactions skew larger.
- Figure 7 (p. 10): Transaction Amount Characteristics — heavy-tailed distribution; most under $100, occasional transactions above $500.
- Figure 8 (p. 10): Retail Sales Time Series — monthly retail sales over five years; upward trend with month-to-month volatility.
- Figure 9 (p. 11): Customer Churn by Contract Type — month-to-month contracts have the highest churn rate.
- Figure 10 (p. 14): Bankruptcy Prediction: AUC Comparison and Learning Curves.
- Figure 11 (p. 14): Fraud Detection: Precision-F1 Comparison and GRU Recall.
- Figure 12 (p. 15): Consumer Behavior Forecasting: ARIMA vs. LSTM Error Metrics.
- Figure 13 (p. 15): Clustering Evaluation: Silhouette Analysis and DBSCAN Sensitivity.
- Figure 14 (p. 16): Clustering Evaluation: K-Means vs. DBSCAN Visual Comparison.

## Limitations and Gaps

- The Research Objectives section (Sec. 1.3, p. 3) is entirely about energy sustainability, energy demand prediction, greenhouse gas emissions and renewable energy — none of which are studied anywhere else in the paper. The stated objectives do not match the reported work. [unacknowledged]
- The paper claims data from six named proprietary and public sources (bank CRM, payment processor, retail BI, SEC EDGAR, Moody's, telecom warehouse) but Figure 1 describes "500 synthetic firms" (Sec. 2.3, p. 6), and no dataset size is reported for any of the six sources. Whether the reported results rest on real or synthetic data is unclear from the text. [unacknowledged]
- The results section reports no numbered tables and no confusion matrices, ROC curves, precision-recall curves or residual plots, despite the methodology stating that all of these are logged. Figures 10-14 are referenced but their numeric contents are not recoverable from the prose. [unacknowledged]
- No confidence intervals and no p-values are reported for any outcome, despite the methodology stating that hyperparameter tuning and validation were systematic (Sec. 2.5, pp. 12-13). All Statistical Evidence rows therefore carry `—` for CI and p.
- Random Forest, SVM, LightGBM and XGBoost are named in the bankruptcy pipeline, but only XGBoost, LightGBM, LSTM, ANN and Logistic Regression AUCs are reported. Random Forest and SVM bankruptcy results are absent. [unacknowledged]
- ARIMA and LSTM forecasts are reported separately in Sec. 4.1 but the discussion (Sec. 4.2, p. 16) reports "the LSTM-ARIMA model excelled" — a hybrid whose standalone results are not given in the results section. [unacknowledged]
- Hyperparameter values are not reported despite grid search and Bayesian optimisation being described; the actual selected values for tree depth, learning rate, regularisation terms, layer sizes, lookback windows and batch sizes are absent. [unacknowledged]
- The paper describes consumer-behavior analysis across telecom churn, banking churn and social-media sentiment in the literature review, but the results section reports only clustering (K-Means, DBSCAN) and forecasting (ARIMA, LSTM). Customer churn prediction results are not reported for any model. [unacknowledged]
- SMOTE and PCA are described in methodology (Sec. 2.3, p. 6) but no ablation, no comparison against no-SMOTE, and no PCA variance-explained value is reported, so their effect on results is unevidenced. [unacknowledged]
- The authors acknowledge that models relied on static pre-collected datasets that "may not reflect rapidly changing market dynamics or consumer behaviors" and that real-world deployment would require continuous retraining and monitoring (Sec. 4.2, p. 17).
- The authors acknowledge that future work should incorporate macroeconomic indicators, social media signals and unstructured text such as financial news or transaction narratives (Sec. 4.2, p. 17).
- The authors acknowledge the need to explore automated feature engineering and advanced hyperparameter optimisation to further improve performance (Sec. 4.2, p. 17).
- The authors acknowledge that ensuring fairness, accountability and responsible data use is crucial as predictive models become more pervasive, and that most current research focuses on accuracy and efficiency with limited emphasis on ethical deployment frameworks (Sec. 2.2, p. 5).
- Two references (Sizan et al., 2025 [17] and [18]) are cited repeatedly in the introduction and literature review and appear to be the same research group; the relationship between those papers and the present study is not made explicit. [unacknowledged]

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bankruptcy prediction, XGBoost | AUC | 0.93 | — | — | Sec. 4.1, p. 13 |
| Bankruptcy prediction, LightGBM | AUC | 0.91 | — | — | Sec. 4.1, p. 13 |
| Bankruptcy prediction, LSTM | AUC | 0.92 | — | — | Sec. 4.1, p. 13 |
| Bankruptcy prediction, ANN | AUC | 0.89 | — | — | Sec. 4.1, p. 13 |
| Bankruptcy prediction, Logistic Regression | AUC | 0.76 | — | — | Sec. 4.1, p. 13 |
| Fraud detection, Stacking Ensemble | F1 | 0.89 | — | — | Sec. 4.1, p. 14 |
| Fraud detection, Stacking Ensemble | precision | 0.91 | — | — | Sec. 4.1, p. 14 |
| Fraud detection, GRU-RNN | recall | 0.89 | — | — | Sec. 4.1, p. 14 |
| Fraud detection, XGBoost | recall | 0.81 | — | — | Sec. 4.1, p. 14 |
| Fraud detection, Isolation Forest | precision | 0.65 | — | — | Sec. 4.1, p. 14 |
| Consumer behavior forecasting, LSTM | MAE | 2.8 | — | — | Sec. 4.1, p. 14 |
| Consumer behavior forecasting, ARIMA | MAE | 4.2 | — | — | Sec. 4.1, p. 14 |
| Consumer behavior forecasting, LSTM | RMSE | 3.3 | — | — | Sec. 4.1, p. 14 |
| Consumer behavior forecasting, ARIMA | RMSE | 5.1 | — | — | Sec. 4.1, p. 14 |
| Consumer behavior forecasting, ARIMA residuals during volatile sales periods | residual range | ±4 | — | — | Sec. 4.1, p. 15 |
| Consumer segmentation, K-Means | silhouette score | 0.68 | — | — | Sec. 4.1, p. 15 |
| Consumer segmentation, DBSCAN | Davies-Bouldin index | 0.52 | — | — | Sec. 4.1, p. 15 |
| Fraud class distribution | fraud rate | about 2% | — | — | Sec. 2.3, p. 6 |
| Bankruptcy EDA, bankrupt firms | Debt/Equity mean | ~1.5 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, healthy firms | Debt/Equity mean | ~0.5 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, bankrupt firms | Current Ratio cluster | around 1.0 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, healthy firms | Current Ratio mean | 2.5 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, Debt/Equity vs. Profit Margin | correlation | -0.4 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, Current Ratio vs. ROA | correlation | 0.2 | — | — | Sec. 2.3, p. 8 |
| Bankruptcy EDA, bankruptcy status vs. numeric metrics | correlation | <0.1 | — | — | Sec. 2.3, p. 6 |
| Bankruptcy EDA, synthetic firms sample | N | 500 | — | — | Sec. 2.3, p. 6 |
| Data split | train:test ratio | 80:20 | — | — | Sec. 2.3, p. 6 |
| Cross-validation | folds | 5 | — | — | Sec. 2.4, p. 11 |
| Early stopping patience for neural networks and LSTM | epochs | 10 | — | — | Sec. 2.5, p. 12 |
| DBSCAN parameter at which organic clusters and noise are identified | ε | 1.2 | — | — | Sec. 4.1, p. 15 |
| Transaction amount distribution | typical threshold | under $100 | — | — | Sec. 2.3, p. 9 |
| Transaction amount distribution, occasional large transactions | upper tail | past $500 | — | — | Sec. 2.3, p. 9 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This research proposes a machine learning-based framework to analyze and predict financial risk factors, with a specific focus on bankruptcy prediction, fraud detection, and consumer behavior trends." | Abstract, p. 1 | model_algorithm_integration |
| "To predict bankruptcy, the study employs six different models—Logistic Regression, Random Forest, Gradient Boosting (including XGBoost and LightGBM), Support Vector Machines (SVM), Artificial Neural Networks, and Long Short-Term Memory (LSTM) networks." | Abstract, p. 1 | model_development |
| "For fraud detection, the research integrates unsupervised techniques such as Isolation Forest alongside supervised classifiers like Logistic Regression, Random Forest, and XGBoost." | Abstract, p. 1 | model_algorithm_integration |
| "To understand consumer behavior trends, the study utilizes K-Means and DBSCAN clustering for behavioral segmentation, along with time-series models like ARIMA and LSTM to forecast financial activities and preferences." | Abstract, p. 1 | model_algorithm_integration |
| "To tackle challenges such as data imbalance, particularly in fraud detection and bankruptcy prediction, the Synthetic Minority Over-sampling Technique (SMOTE) is implemented." | Abstract, p. 1 | data_collection |
| "Outliers were detected using a combination of z-score thresholds and interquartile range analysis, with winsorization or log-transformations mitigating their undue influence." | Sec. 2.3 Data Preprocessing, p. 6 | interquartile_range |
| "In terms of AUC Scores for bankruptcy prediction, XGBoost (0.93) and LightGBM (0.91) dominate due to their gradient-boosting architectures, which effectively model nonlinear interactions in financial ratios (e.g., Debt/Equity, ROA)." | Sec. 4.1, p. 13 | model_performance_evaluation |
| "Logistic Regression (0.76) lags, constrained by its linear assumptions." | Sec. 4.1, p. 13 | model_performance_evaluation |
| "In Fraud Detection, Stacking Ensemble model achieves the highest F1 (0.89) and precision (0.91) by combining XGBoost, Random Forest, and GRU predictions." | Sec. 4.1, p. 14 | model_algorithm_integration |
| "GRU-RNN model outperforms static models in recall (0.89 vs. 0.81 for XGBoost), excelling at detecting sequential fraud patterns such as multi-transaction scams." | Sec. 4.1, p. 14 | model_performance_evaluation |
| "Isolation Forest suffers from low precision (0.65) due to false positives, validating its role as a supplementary anomaly detector rather than a standalone solution." | Sec. 4.1, p. 14 | model_performance_evaluation |
| "LSTM achieves lower MAE (2.8 vs. 4.2) and RMSE (3.3 vs. 5.1) by modeling nonlinear trends (e.g., holiday spikes) and long-term dependencies in transactional data." | Sec. 4.1, p. 14 | model_performance_evaluation |
| "ARIMA, although effective for linear, stationary data, struggled with volatile or seasonal fluctuations evident in retail sales." | Sec. 4.1, p. 14 | sarima |
| "K-Means achieves a higher silhouette score (0.68) confirming well-separated clusters (e.g., low vs. high spenders), enabling actionable marketing strategies." | Sec. 4.1, p. 15 | model_performance_evaluation |
| "DBSCAN on the other hand achieves a lower Davies-Bouldin score (0.52) reflects better cluster separation than K-Means, but performance heavily depends on ε tuning." | Sec. 4.1, p. 15 | model_performance_evaluation |
| "The first plot (Figure 1) displays the distribution of the debt-to-equity ratio among 500 synthetic firms." | Sec. 2.3, p. 6 | data_collection |
| "The class distribution plot (Figure 3) illustrates that only about 2% of transactions are labeled as fraud—typical of real credit-card datasets—revealing a severe class imbalance." | Sec. 2.3, p. 6 | data_collection |
| "Bankrupt firms exhibit higher Debt/Equity ratios (mean ~1.5) compared to healthy firms (mean ~0.5), indicating overleveraging." | Sec. 2.3, p. 8 | savings_debt_management |
| "The primary objective of this research is to investigate how artificial intelligence and machine learning can be harnessed to promote energy sustainability by forecasting, analyzing, and optimizing consumption patterns." | Sec. 1.3 Research Objectives, p. 3 | model_algorithm_integration |
| "Nonetheless, the study reveals several limitations that should be addressed in future research. Firstly, the models relied on static, pre-collected datasets, which may not reflect rapidly changing market dynamics or consumer behaviors." | Sec. 4.2, p. 17 | model_development |

## Definitions

- **SMOTE** — Synthetic Minority Over-sampling Technique; used to address class imbalance in fraud and churn tasks without information loss (Sec. 2.3, p. 6).
- **PCA** — Principal Component Analysis; used alongside Recursive Feature Elimination for dimensionality reduction (Sec. 2.3, p. 6).
- **RFE** — Recursive Feature Elimination; paired with PCA for feature-set streamlining (Sec. 2.3, p. 6).
- **AUC** — Area Under the (ROC) Curve; the primary bankruptcy-prediction metric (Sec. 4.1, p. 13).
- **AUC-PR** — Area under the precision-recall curve; used in fraud detection due to class skew (Sec. 2.5, p. 13).
- **Platt scaling** — A probability calibration method used alongside isotonic regression on bankruptcy model outputs (Sec. 2.4, p. 11).
- **GRU** — Gated Recurrent Unit; used in the fraud-detection RNN for sequential transaction modelling (Sec. 2.4, p. 12).
- **Isolation Forest** — An unsupervised anomaly-detection method used as a fraud-detection baseline (Sec. 2.4, p. 11).
- **DBSCAN** — Density-Based Spatial Clustering of Applications with Noise; used for consumer segmentation with ε and min_samples tuned via k-distance plots (Sec. 2.4, p. 12).
- **SHAP** — SHapley Additive exPlanations; used for black-box model feature attribution (Sec. 2.4, p. 12).
- **MLflow** — Model-versioning tool used to log validation scores, confusion matrices, ROC curves, precision-recall curves and residual plots (Sec. 2.5, p. 13).

## Remember This

- The paper covers three ML pipelines — bankruptcy prediction, fraud detection, consumer behavior analysis — applied to US financial data.
- Bankruptcy prediction is led by XGBoost (AUC 0.93); fraud detection is led by a stacking ensemble (F1 0.89, precision 0.91); consumer forecasting is led by LSTM (MAE 2.8, RMSE 3.3).
- The research objectives section describes energy sustainability, which the paper never studies — a substantial internal inconsistency.
- Figure 1 describes 500 synthetic firms, while Sec. 2.3 describes six proprietary real-world sources; the actual data basis of the results is unclear.
- No numbered results tables exist; all numeric results are reported in prose or figure captions, with no confidence intervals and no p-values.

## Cited Works

- Al Montaser et al. (2025) — Sentiment analysis of social media for consumer behavior and business trends in the USA; cited for behavioral-pattern extraction from social media (context). [2]
- Brown & Liu (2023) — ML techniques for anomaly detection in financial transactions (methodology). [3]
- Chakraborty & Amam (2024) — Explainable AI in financial decision-making: trust, transparency, accountability (context). [4]
- Chen et al. (2024) — Deep learning for retail sales forecasting; cited for domain-informed feature engineering in retail forecasting (context). [5]
- Chen & Guestrin (2016) — XGBoost: a scalable tree boosting system; cited as the origin of tree-based ensemble strength in financial prediction (methodology). [6]
- Davis & Porter (2024) — Ensemble learning methods for financial risk prediction (context). [7]
- Farooq et al. (2025) — Predicting e-commerce customer satisfaction using machine learning (context). [8]
- Hyndman & Athanasopoulos (2018) — Forecasting: Principles and Practice; cited for combining statistical and deep-learning forecasting (methodology). [9]
- Idris et al. (2025) — Hybrid ML framework for fraud detection in e-commerce transactions (baseline). [10]
- Karim et al. (2017) — LSTM Fully Convolutional Networks for time-series classification (methodology). [11]
- Liu et al. (2008) — Isolation Forest; cited for the observation that anomaly detection tends toward high precision but fails to capture all fraudulent cases (methodology). [12]
- Liu et al. (2023) — Hybrid fraud detection using ensemble deep learning models (context). [13]
- Mohaimin et al. (2025) — Predictive analytics for telecom customer churn in the US market (context). [14]
- Rana et al. (2025) — AI-driven predictive modelling for banking customer churn in the US financial sector (context). [15]
- Roy et al. (2023) — Comprehensive study on ML techniques for churn prediction across domains (context). [16]
- Sizan et al. (2025a) — Bankruptcy prediction for US businesses using machine learning (context, cited repeatedly). [17]
- Sizan et al. (2025b) — Advanced ML approaches for credit card fraud detection in the USA (context, cited repeatedly). [18]
- Zarei et al. (2024) — Social media opinion mining: techniques and business applications (context). [19]
- Zhang et al. (2023) — Machine learning for customer credit risk prediction: a comparative study (context). [20]
- Zhou et al. (2020) — Machine learning on big data: opportunities and challenges; cited for the importance of nonlinear models in financial risk prediction (methodology). [21]