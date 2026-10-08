---
paper_id: A--Bader-2025
first_author: Bader
year: 2025
title: "Bridging AI and Emotion: Enhanced Models for Personal Finance Manager Applications"
venue: "International Journal of Computing and Digital Systems"
doi: 10.12785/ijcds/1571107231
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, income_expense_management, pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, model_algorithm_integration, data_collection, model_development, system_development, model_performance_evaluation, software_quality_evaluation, system_performance_evaluation]
module_rationale:
  financial_planning: "The application provides budgeting, transaction tracking, goal setting and personalized financial advice (Abstract, p. 1; Sect. 3.G, p. 7)."
  budgeting: "The application includes budget creation windows, budget widgets and a budget dashboard (Sect. 3.P, pp. 8-9; Figures 8-10)."
  income_expense_management: "Transaction records are categorised by Merchant Category Code and tracked per user (Sect. 3.B, p. 6; Sect. 3.K, p. 7)."
  pfm_apps_overview: "The paper positions the Financial Advisor Application against existing budgeting apps Mint and YNAB (Sect. 1, p. 1; Sect. 5.D, pp. 16-17)."
  pfm_apps_features: "Dashboards, savings goals, alerts, forecasts and merchant offers are described as the application's feature set (Sect. 3.G, p. 7; Figures 3-11)."
  pfm_apps_problems: "Existing tools 'become mere carriers of simple data transfers' and ignore behaviour and sentiment (Sect. 1.A, p. 2)."
  pfm_apps_importance: "The paper claims its approach 'outperforms conventional budgeting applications' (Sect. 5.C, p. 16)."
  model_algorithm_integration: "Three AI components plus Transformer, TCN and N-BEATS models are combined into one pipeline (Sect. 3.C-E, p. 6; Sect. 3.R, pp. 10-11)."
  data_collection: "The dataset was aggregated from bank transaction logs and Merchant Category Code classification (Sect. 3.J, p. 7)."
  model_development: "Training procedures for the Transformer, TCN, N-BEATS and anomaly detection models are described (Sect. 3.R, pp. 10-11; Sect. 3.S, p. 11)."
  system_development: "The application is built on .NET Core 6 with Python/TensorFlow/Keras AI components and a web/mobile front end (Sect. 1.B, p. 2; Sect. 3.F, p. 7)."
  model_performance_evaluation: "MAPE, RMSE, precision, recall, ROC-AUC, accuracy and F1-score are reported (Sect. 5.A-B, p. 16)."
  software_quality_evaluation: "User satisfaction is measured with self-administered questionnaires and user feedback (Sect. 3.T.6, p. 12)."
  system_performance_evaluation: "Real-time testing in production and user feedback integration are described (Sect. 3.U.4, p. 13)."
---

## Summary

A Financial Advisor Application is developed that combines three AI-driven analytical components — anomaly detection, sentiment analysis and predictive modelling — over users' bank transaction data. The application is built on a .NET Core 6 backend with Python/TensorFlow/Keras models, and it provides budgeting, transaction tracking, goal setting, anomaly alerts and AI-driven merchant recommendations. Anomaly detection is implemented with Isolation Forest, Local Outlier Factor and One-Class SVM; sentiment analysis uses BERT and GPT fine-tuned on financial text and classifies transactions into ten emotional types; predictive modelling compares Transformer, Temporal Convolutional Network (TCN) and N-BEATS architectures. The paper reports 92% anomaly-detection accuracy, 90% precision, 85% recall, an 87.5% F1-score and a 0.93 ROC-AUC, and reports that adding sentiment analysis improved MAPE from 10.5% to 7.8% and reduced prediction error by 25% versus rule-based systems. No sample size, no participant count, no train/test split and no confidence intervals or p-values are reported for any model metric, and most model outcomes are shown only in figures without printed numeric values. The paper does not name a formal study design, does not report the geographic setting of the transaction data, and reports a production deployment without describing its site, users or duration.

## Problem and Motivation

Contemporary financial advisory tools are described as relying on fixed structures that ignore user behaviour, mood and preferences, and as being unable to extract value from unstructured inputs such as transaction descriptions (Sect. 1.A, p. 2). The paper argues that this leads to recommendations that users do not need or cannot handle emotionally, limiting engagement and satisfaction. Existing financial platforms can process structured data but not the unstructured data that stems from user inputs and transaction descriptions (Sect. 1.A, p. 2). The stated objectives are to develop deep learning models for anomaly detection in financial transactions, to create predictive models that analyse historical financial data and user transaction histories, and to incorporate semantic analysis and NLP to understand user sentiment and behaviour for personalised financial advice (Sect. 1.C, p. 3). The paper also states that existing budgeting applications such as Mint and YNAB rely on static rule-based algorithms and do not incorporate sentiment analysis (Sect. 5.C, p. 16).

## Method

**Design.** Applied system-development and model-comparison study; the authors state no formal design label ("This study employs a data-driven approach that integrates machine learning (ML) and artificial intelligence (AI) techniques to provide personalized financial advice based on users' banking transactions", Sect. 3, p. 6).
**Sample.** N not reported; the unit of analysis is the individual bank transaction and the user-level spending time series, with sentiment scored per transaction description (Sect. 3.J, p. 7; Sect. 3.Q, p. 9).
**Context.** geography: Not reported (the authors are affiliated with the Lebanese American University, Beirut, Lebanon, but the geographic origin of the transaction data is not stated); population: Banking customers whose transaction logs, merchant data and account records were aggregated (Sect. 3.J, p. 7); setting: Virtual/computational — a .NET Core 6 web/mobile application with Python/TensorFlow/Keras AI components; model evaluation is offline, with a claimed production deployment but no deployment site described (Sect. 3.F, p. 7; Sect. 3.U, p. 13).

- Aggregate a dataset from bank transaction logs and Merchant Category Code (MCC) classification (Sect. 3.J, p. 7).
- Preprocess transaction descriptions by cleaning punctuation, capitalisation and spelling, and normalise transaction amounts and dates (Sect. 3.Q.1, p. 9).
- Run sentiment analysis on the cleaned transaction descriptions with pre-trained BERT and GPT models fine-tuned on a financial text corpus (Sect. 3.Q.2, p. 9).
- Classify transactions into ten pre-determined emotional types: Outgoing, Sad, Feeling Generous, Shopping, Roadtrip, Adventurous, Health-Focused, Stressed, Culturally Engaged and Tech Enthusiast (Sect. 3.Q.2, p. 10).
- Compile sentiment scores over intervals and combine them with transaction history and account details to enrich user profiles (Sect. 3.Q.3, p. 10).
- Implement anomaly detection with Isolation Forest, Local Outlier Factor and One-Class SVM, selecting features including transaction amount, frequency, time, MCC code and user profile (Sect. 3.S.1-2, p. 11).
- Flag any transaction whose variation from the learned typical pattern is greater than 5% as an outlier (Sect. 3.S.4, p. 11).
- Implement predictive modelling with three architectures: Transformer (multi-head self-attention, feed-forward blocks, layer normalisation and dropout, trained with a learning rate scheduler, Adam optimiser and MSE loss), TCN (dilated convolutions, residual connections and normalisation layers, trained with MSE loss) and N-BEATS (dense layers with ReLU activations and final linear layers outputting trend and seasonality components, trained with learning rate scheduling and early stopping) (Sect. 3.R.1-3, pp. 10-11).
- Add engineered features including user age and gender, account balances and sentiment scores derived from transaction descriptions (Sect. 3.R.4, p. 11).
- Evaluate predictive models with MAPE and accuracy and anomaly models with precision, recall and ROC-AUC (Sect. 3.R.5, p. 11; Sect. 3.S.6, p. 12).
- Use k-fold cross-validation, stratified sampling, grid search and random search for hyperparameter tuning (Sect. 3.U.2-3, p. 13).
- Deploy the models to a production environment and monitor accuracy rate, anomaly-detection rate and user satisfaction index, with periodic retraining (Sect. 3.U.4-6, p. 13).
- Apply a user feedback loop in which users confirm or dispute sentiment categorisations, anomaly flags and recommendations (Sect. 3.Q.5, p. 10; Sect. 3.S.5, p. 11-12).

## Software

- .NET Core 6 (backend integration hub)
- Python (AI features)
- TensorFlow and Keras (deep learning)
- BERT and GPT (pre-trained language models fine-tuned on a financial text corpus)
- Isolation Forest, Local Outlier Factor (LOF), One-Class SVM (anomaly detection)
- Transformer, Temporal Convolutional Network (TCN), N-BEATS (predictive models)
- Adam optimiser, mean squared error loss, learning rate scheduling, early stopping
- Grid search and random search (hyperparameter tuning)
- Front-end application (Web/Mobile) (framework not reported)

## Key Findings

- num: The anomaly detection system achieves 92% accuracy, 90% precision, 85% recall and an F1-score of 87.5%, with a ROC-AUC of 0.93 (Sect. 5.A, p. 16).
- num: Conventional financial fraud detection systems typically report precision and recall values in the range of 70–80% (Sect. 5.A, p. 16).
- num: MAPE improved from 10.5% to 7.8% when sentiment analysis was incorporated (Sect. 5.C, p. 16).
- num: RMSE is 0.062 for the Transformer model, 0.074 for the TCN model and 0.057 for the N-BEATS model, with N-BEATS reported as the best performer (Sect. 5.C, p. 16).
- num: Predictive accuracy within a 90% confidence interval achieved 88% alignment with actual user behaviour (Sect. 5.C, p. 16).
- num: Prediction error was reduced by 25% compared to rule-based systems (Sect. 5.C, p. 16).
- num: Table 1 reports 90% anomaly detection precision for the proposed application against 70–80% for traditional banking/fraud detection systems and "Not applicable" for existing budgeting apps; the second precision row reports 85% for the proposed application and 70–80% for traditional systems (Table 1, p. 17).
- num: Table 1 reports MAPE of 7.8% for the proposed application and 10–12% for existing budgeting apps, with "Not applicable" for traditional banking/fraud detection systems (Table 1, p. 17).
- num: Table 1 reports deep learning (Transformer, TCN, N-BEATS) as the proposed forecasting method, against statistical models for traditional systems and rule-based systems for existing budgeting apps (Table 1, p. 17).
- num: Table 1 reports that the proposed application incorporates sentiment analysis, supports real-time adaptability, and is extensible and scalable via the .NET Core 6 framework, while traditional systems are limited and existing budgeting apps are not (Table 1, p. 17).
- The TCN model without sentiment analysis is reported as being "only 5% away from the actual spending" (Sect. 4.A.2, p. 14).
- Section 3.E states that the system "integrates sentiment-aware financial predictions, improving forecasting accuracy by 25" — an incomplete quantity as printed (Sect. 3.E, p. 6).
- The paper's Section 5.E reports that "the TCN model reveals that including sentiment data does not constantly improve the predictive performance", contradicting the general claim that sentiment analysis improves accuracy (Sect. 5.E, p. 17).

## Key Figures and Tables

- Figure 1 (p. 6): Architecture of the application — shows multiple data streams feeding AI analytics that generate personalised financial recommendations.
- Figure 2 (p. 7): MCC dataset — Merchant Category Code classification assigned by Visa and Mastercard.
- Figure 3 (p. 8): The dashboard — visual analytics for spending patterns, anomaly detections and future financial projections.
- Figure 4 (p. 8): Suggestion's box — personalised suggestions presented to the user.
- Figure 5 (p. 8): Merchants box — merchant recommendations and offers.
- Figure 6 (p. 8): Spending behaviour chart — user spending patterns.
- Figure 7 (p. 9): Anomaly transaction — an example of a flagged irregular transaction.
- Figure 8 (p. 9): Budget creation — budget creation window.
- Figure 9 (p. 9): Budget widgets — budget widgets display.
- Figure 10 (p. 9): Budget dashboard — budget dashboard display.
- Figure 11 (p. 9): Goal creation — goal creation interface.
- Figure 12 (p. 14): Scenarios — real-world scenarios demonstrating application capabilities.
- Figure 13 (p. 14): The transformers — Transformer model performance in predicting customer spending without sentiment analysis.
- Figure 14 (p. 14): The TCN — TCN model results without sentiment analysis.
- Figure 15 (p. 15): N-BEATS — N-BEATS model accuracy without sentiment analysis.
- Figure 16 (p. 15): The transformers — Transformer model results with sentiment analysis.
- Figure 17 (p. 15): The TCN — TCN model results with sentiment analysis.
- Figure 18 (p. 16): N-BEATS — N-BEATS model results with sentiment analysis.
- Figure 19 (p. 17): Anomaly detection comparison — comparison of models against anomaly detection.
- Figure 20 (p. 17): Predictive analysis comparison — comparison of models against predictive analysis.
- Table 1 (p. 17): Comparison with existing fintech solutions across anomaly detection precision, financial forecasting method, incorporation of sentiment analysis, MAPE, real-time adaptability, and extensibility and scalability.

## Definitions

- **MAPE** — Mean Absolute Percentage Error; the average of relative errors, used to assess predictive model performance (Sect. 3.R.5, p. 11).
- **RMSE** — Root Mean Squared Error; reported for the Transformer (0.062), TCN (0.074) and N-BEATS (0.057) models (Sect. 5.C, p. 16).
- **ROC-AUC** — Receiver Operating Characteristic—Area Under Curve; measures how well an anomaly detection model discriminates between normal and abnormal transactions (Sect. 3.S.6, p. 12).
- **MCC** — Merchant Category Code; standardised categories assigned by Visa and Mastercard to classify businesses (Sect. 3.J, p. 7).
- **Isolation Forest** — Anomaly detection algorithm that isolates observations by randomly choosing a feature and a split value; fewer splits indicate an outlier (Sect. 3.S.3, p. 11).
- **LOF** — Local Outlier Factor; estimates the density of a data point relative to its neighbours, where lower density indicates an anomaly (Sect. 3.S.3, p. 11).
- **One-Class SVM** — Anomaly detection algorithm that learns a decision function (hyperplane) separating most data points from the rest (Sect. 3.S.3, p. 11).
- **Transformer** — Deep learning architecture using multi-head self-attention and feed-forward blocks, suited to long-term dependencies in time series (Sect. 3.R.1, p. 10).
- **TCN** — Temporal Convolutional Network; uses causal and dilated convolutions with residual connections for sequence modelling (Sect. 3.R.2, p. 10).
- **N-BEATS** — Neural basis expansion analysis for interpretable time series forecasting; decomposes time-series data into trend and seasonality components (Sect. 3.R.3, p. 10).
- **BERT and GPT** — Pre-trained language models fine-tuned on a financial text corpus for sentiment analysis of transaction descriptions (Sect. 3.Q.2, p. 9).

## Limitations and Gaps

- The authors acknowledge that generalisation across diverse financial behaviours is untested and that future work should explore adaptability across different user demographics and financial habits (Sect. 5.F, p. 18).
- The authors acknowledge that deep learning models require significant computational resources and that model pruning and edge AI deployment will be explored to improve efficiency (Sect. 5.F, p. 18).
- The authors acknowledge that user trust and adoption remain a critical factor and that future studies will examine user perception, trust-building and human-AI interaction (Sect. 5.F, p. 18).
- The authors acknowledge that scalability is a challenge: efficiency and responsiveness in handling large-scale, real-world financial data streams require further investigation (Sect. 6, p. 18).
- The authors acknowledge that the models primarily rely on structured and semi-structured data and that extending them to unstructured data such as textual descriptions or social media sentiment remains a critical area for development (Sect. 6, p. 18).
- The authors acknowledge that deployment raises data privacy, security vulnerability and financial-regulation compliance issues that must be addressed rigorously (Sect. 6, p. 18).
- The authors acknowledge that the TCN model shows that including sentiment data does not constantly improve predictive performance (Sect. 5.E, p. 17).
- [unacknowledged] No sample size, participant count, transaction count, train/test split or dataset size is reported anywhere in the paper, so the scale of the evidence base cannot be assessed.
- [unacknowledged] No confidence intervals or p-values are reported for any model metric; the only interval statement is a 90% confidence interval attached to an 88% alignment value, with no interval bounds printed (Sect. 5.C, p. 16).
- [unacknowledged] Most results are presented only in figures (Fig. 13-18) without printed numeric values; the only numeric model-outcome summary in the results narrative is the single bullet list in Sect. 5.C (p. 16).
- [unacknowledged] The paper claims deployment in a production environment (Sect. 3.U.4, p. 13) but reports no deployment site, no user count, no deployment duration and no live-system measurements.
- [unacknowledged] Table 1 labels two rows "Anomaly Detection Precision", the second of which carries the value 85% that the narrative treats as recall (Sect. 5.A, p. 16; Table 1, p. 17), so the table's metric labels are internally ambiguous.
- [unacknowledged] Sect. 3.E prints "improving forecasting accuracy by 25" as an incomplete quantity (p. 6), while Sect. 5.C renders the same 25 as "reduction in prediction error by 25%" (p. 16); the two framings are not reconciled.
- [unacknowledged] The MAPE improvement is reported from a baseline of 10.5% (Sect. 5.C, p. 16), while Table 1 gives existing budgeting apps a MAPE range of 10–12% (Table 1, p. 17); the baseline is not stated consistently.
- [unacknowledged] The sentiment classifier is described as assigning ten emotional types, but no inter-rater reliability, validation accuracy or error rate for the sentiment classification is reported (Sect. 3.Q.2, p. 10).
- [unacknowledged] The paper reports no demographic breakdown of the users whose transactions were analysed and no information on how consent or data governance was handled.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Anomaly detection system, proposed application | accuracy | 92% | — | — | Sect. 5.A, p. 16 |
| Anomaly detection system, proposed application | precision | 90% | — | — | Sect. 5.A, p. 16 |
| Anomaly detection system, proposed application | recall | 85% | — | — | Sect. 5.A, p. 16 |
| Anomaly detection system, proposed application | F1-score | 87.5% | — | — | Sect. 5.A, p. 16 |
| Anomaly detection system, proposed application | ROC-AUC | 0.93 | — | — | Sect. 5.A, p. 16 |
| Conventional financial fraud detection systems | precision and recall range | 70–80% | — | — | Sect. 5.A, p. 16 |
| Anomaly detection precision, proposed application (Table 1) | precision | 90% | — | — | Table 1, p. 17 |
| Anomaly detection precision, traditional banking/fraud detection systems (Table 1) | precision | 70–80% | — | — | Table 1, p. 17 |
| Anomaly detection precision, existing budgeting apps (Table 1) | precision | Not applicable | — | — | Table 1, p. 17 |
| Anomaly detection recall (row labelled precision in the table), proposed application (Table 1) | recall | 85% | — | — | Table 1, p. 17 |
| Anomaly detection recall (row labelled precision in the table), traditional banking/fraud detection systems (Table 1) | recall | 70–80% | — | — | Table 1, p. 17 |
| Anomaly detection recall (row labelled precision in the table), existing budgeting apps (Table 1) | recall | Not applicable | — | — | Table 1, p. 17 |
| Financial forecasting method, proposed application (Table 1) | method class | Deep Learning (Transformer, TCN, N-BEATS) | — | — | Table 1, p. 17 |
| Financial forecasting method, traditional banking/fraud detection systems (Table 1) | method class | Statistical Models | — | — | Table 1, p. 17 |
| Financial forecasting method, existing budgeting apps (Table 1) | method class | Rule-Based Systems | — | — | Table 1, p. 17 |
| Incorporation of sentiment analysis, proposed application (Table 1) | sentiment analysis inclusion | Yes | — | — | Table 1, p. 17 |
| Incorporation of sentiment analysis, traditional banking/fraud detection systems (Table 1) | sentiment analysis inclusion | No | — | — | Table 1, p. 17 |
| Incorporation of sentiment analysis, existing budgeting apps (Table 1) | sentiment analysis inclusion | No | — | — | Table 1, p. 17 |
| MAPE prediction error, proposed application (Table 1) | MAPE | 7.8% | — | — | Table 1, p. 17 |
| MAPE prediction error, traditional banking/fraud detection systems (Table 1) | MAPE | Not applicable | — | — | Table 1, p. 17 |
| MAPE prediction error, existing budgeting apps (Table 1) | MAPE | 10–12% | — | — | Table 1, p. 17 |
| Real-time adaptability, proposed application (Table 1) | real-time adaptability | Yes | — | — | Table 1, p. 17 |
| Real-time adaptability, traditional banking/fraud detection systems (Table 1) | real-time adaptability | Limited | — | — | Table 1, p. 17 |
| Real-time adaptability, existing budgeting apps (Table 1) | real-time adaptability | No | — | — | Table 1, p. 17 |
| Extensibility and scalability, proposed application (Table 1) | extensibility and scalability | Yes (via .NET Core 6 framework) | — | — | Table 1, p. 17 |
| Extensibility and scalability, traditional banking/fraud detection systems (Table 1) | extensibility and scalability | Limited | — | — | Table 1, p. 17 |
| Extensibility and scalability, existing budgeting apps (Table 1) | extensibility and scalability | No | — | — | Table 1, p. 17 |
| MAPE before sentiment analysis | MAPE | 10.5% | — | — | Sect. 5.C, p. 16 |
| MAPE after sentiment analysis | MAPE | 7.8% | — | — | Sect. 5.C, p. 16 |
| RMSE, Transformer model | RMSE | 0.062 | — | — | Sect. 5.C, p. 16 |
| RMSE, TCN model | RMSE | 0.074 | — | — | Sect. 5.C, p. 16 |
| RMSE, N-BEATS model | RMSE | 0.057 | — | — | Sect. 5.C, p. 16 |
| Predictive accuracy alignment with actual user behaviour | alignment | 88% | 90% confidence interval (as printed) | — | Sect. 5.C, p. 16 |
| Reduction in prediction error versus rule-based systems | prediction error reduction | 25% | — | — | Sect. 5.C, p. 16 |
| Forecasting accuracy improvement from sentiment-aware predictions | accuracy improvement | 25 | — | — | Sect. 3.E, p. 6 |
| TCN model MAPE without sentiment analysis | MAPE | 5% | — | — | Sect. 4.A.2, p. 14 |
| Real-time anomaly detection significance threshold | variation threshold | 5% | — | — | Sect. 3.S.4, p. 11 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The Financial Advisor Application is a perfect example of the synergy of highly developed IT solutions and profound financial knowledge in the constantly evolving field of fintech." | Sect. 1, p. 1 | pfm_apps_overview |
| "The application combines different aspects of financial management, including budgeting, transaction tracking, and goal setting" | Abstract, p. 1 | pfm_apps_features |
| "Unlike traditional instruments that work independently of one another, this platform offers a global picture of a person's financial status and provides recommendations and solutions." | Sect. 1, p. 1 | pfm_apps_overview |
| "Most contemporary approaches to managing financial and accounting activity are based on fixed structures that ignore essential data, such as general user behavior and attitude needed to define what kind of recommendations the administrators should give." | Sect. 1.A, p. 2 | pfm_apps_problems |
| "Today's financial platforms can process structured data effectively, they cannot extract as much value as from the unstructured data that stems from inputs about the users and descriptions of the transactions" | Sect. 1.A, p. 2 | pfm_apps_problems |
| "The core of the system architecture consists of three AI-driven analytical components, which process the input data and extract meaningful financial insights" | Sect. 3.C, p. 6 | model_algorithm_integration |
| "Techniques such as Isolation Forests, One-Class SVM, and Autoencoders are used to identify fraudulent transactions, unauthorized spending, or financial distress signals" | Sect. 3.C, p. 6 | model_algorithm_integration |
| "The system also integrates sentiment-aware financial predictions, improving forecasting accuracy by 25" | Sect. 3.E, p. 6 | model_algorithm_integration |
| "The experimental results demonstrate the robustness of our anomaly detection system, achieving an accuracy of 92%, with a precision of 90%, recall of 85%, and an F1-score of 87.5%." | Sect. 5.A, p. 16 | model_performance_evaluation |
| "The ROC-AUC score of 0.93 indicates a strong ability to distinguish between normal and fraudulent transactions." | Sect. 5.A, p. 16 | model_performance_evaluation |
| "Mean Absolute Percentage Error (MAPE) improved from 10.5% to 7.8% when sentiment analysis was incorporated." | Sect. 5.C, p. 16 | model_performance_evaluation |
| "Our approach outperforms conventional budgeting applications, which primarily rely on static rule-based algorithms (e.g., Mint, YNAB)." | Sect. 5.C, p. 16 | pfm_apps_importance |
| "The reduction in prediction error by 25% compared to rule-based systems highlights the transformative impact of AI-driven financial forecasting in personal finance management." | Sect. 5.C, p. 16 | pfm_apps_importance |
| "Notably, the TCN model reveals that including sentiment data does not constantly improve the predictive performance" | Sect. 5.E, p. 17 | model_performance_evaluation |
| "The dataset was aggregated from bank transaction logs, which were processed and analyzed to extract meaningful insights." | Sect. 3.J, p. 7 | data_collection |
| "This work involves leveraging the features of NET Core 6 to design an extremely robust and highly scalable application." | Sect. 1.B, p. 2 | system_development |
| "The application gives users a summary of the financial situation, combining the data from several accounts and the asset summary, liability, expenditure, and savings plan." | Sect. 2.A, p. 3 | financial_planning |
| "Deep learning models require significant computational resources. Future optimizations, including model pruning and edge AI deployment, will be explored to improve efficiency." | Sect. 5.F, p. 18 | model_development |

## Remember This

- The paper develops a Financial Advisor Application combining anomaly detection, sentiment analysis and predictive modelling over bank transaction data.
- Anomaly detection uses Isolation Forest, LOF and One-Class SVM; sentiment analysis uses fine-tuned BERT and GPT over ten emotional transaction types.
- Predictive modelling compares Transformer, TCN and N-BEATS; N-BEATS reports the best RMSE at 0.057.
- The paper reports 92% anomaly-detection accuracy, 90% precision, 85% recall, an 87.5% F1-score and a 0.93 ROC-AUC, but prints no CI or p-value for any of them.
- MAPE is reported to improve from 10.5% to 7.8% with sentiment analysis, and prediction error is reported reduced by 25% versus rule-based systems.
- No sample size, participant count or dataset size is reported anywhere in the paper.
- Section 5.E contradicts the paper's general claim by reporting that sentiment data does not constantly improve TCN predictive performance.

## Cited Works

- Zaki, M. J.; Meira Jr, W. (2014) (methodology) — Data mining and analysis: fundamental concepts and algorithms. [p. 18]
- Goodfellow, I.; Bengio, Y.; Courville, A. (2016) (methodology) — Deep learning. [p. 18]
- Chollet, F. (2017) (methodology) — Deep learning with Python. [p. 18]
- Heaton, J.; Polson, N.; Witte, J. (2017) (methodology) — Deep learning for finance: deep portfolios. [p. 18]
- Nelson, D. M.; Pereira, A. C.; de Oliveira, R. A. (2017) (methodology) — Stock market's price movement prediction with LSTM neural networks. [p. 18]
- Rezaei, M.; Sani, M. R. F.; Homayouni, S. M. (2020) (context) — Deep learning-based stock market prediction. [p. 18]
- Esteva, A.; Kuprel, B.; Novoa, R. A.; Ko, J.; Swetter, S. M.; Blau, H. M.; Thrun, S. (2017) (context) — Dermatologist-level classification of skin cancer with deep neural networks. [p. 18]
- Agrawal, A.; Gans, J. S.; Goldfarb, A. (2018) (context) — Prediction machines: the simple economics of artificial intelligence. [p. 18]
- Bollen, J.; Mao, H.; Zeng, X. (2011) (methodology) — Twitter's mood predicts the stock market. [p. 18]
- Kumar, V.; Shah, D. (2004) (context) — Building and sustaining profitable customer loyalty for the 21st century. [p. 18]
- Rasp, S.; Dueben, P. D.; Scher, S.; Weyn, J. A.; Mouatadid, S.; Thuerey, N. (2020) (methodology) — Weatherbench: a benchmark dataset for data-driven weather forecasting. [p. 18]
- Carbonneau, R.; Laframboise, K.; Vahidov, R. (2008) (methodology) — Application of machine learning techniques for supply chain demand forecasting. [p. 18]
- Young, T.; Hazarika, D.; Poria, S.; Cambria, E. (2018) (context) — Recent trends in deep learning-based natural language processing. [p. 18]
- Sun, K. (2023) (baseline) — Fine-tuned BERT models for sentiment analysis in financial marketplaces. [p. 19]
- Patel, S.; Kumar, R. (2022) (context) — Predictive analytics for budget planning in fintech. [p. 19]
- Lee, J. (2023) (baseline) — AI-driven fraud detection in digital payments. [p. 19]
- Ramachandran, V. (2024) (context) — Blockchain-enhanced AI for transparent financial systems. [p. 19]
- Chen, Y. (2024) (context) — Sentiment analysis in mobile banking: enhancing user experience through AI. [p. 19]
- Gupta, R. (2023) (context) — Integrating sentiment analysis with transaction data for merchant recommendations. [p. 19]
- Iqbal, H. (2022) (baseline) — Combining TCN and N-BEATS models for financial forecasting. [p. 19]
- Johnson, P. (2024) (context) — Knowledge graphs and sentiment analysis for decision support in fintech. [p. 19]
- Sharma, T. (2023) (context) — Challenges in deploying AI in fintech: a scalability perspective. [p. 19]
- Chandola, V.; Banerjee, A.; Kumar, V. (2009) (methodology) — Anomaly detection: a survey. [p. 19]
- El Abaji, M.; Haraty, R. A. (2025) (context) — Enhancing bitcoin forecast accuracy by integrating AI, sentiment analysis, and financial models. [p. 19]
- Haraty, R. A.; Sobeh, S. (2024) (context) — Unveiling insights from unstructured wealth: a comparative analysis of clustering techniques on blockchain cryptocurrency data. [p. 19]