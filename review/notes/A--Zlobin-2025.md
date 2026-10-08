---
paper_id: A--Zlobin-2025
first_author: Zlobin
year: 2025
title: "Systematic Review of Deep and Machine Learning for Financial Modeling"
venue: "Technical Sciences and Technologies (Технічні науки та технології)"
doi: 10.25140/2411-5363-2025-1(39)-184-195
designation: algorithm
status: extracted
modules: [model_performance_evaluation, model_algorithm_integration, pfm_apps_features, pfm_apps_importance, budgeting]
module_rationale:
  model_performance_evaluation: "The whole paper is a comparative performance review of ML/DL models across financial tasks, built around Table 1 and Table 2 and metric-by-metric results (Tables 1–2, pp. 189, 192)."
  model_algorithm_integration: "It reviews hybrid pipelines that combine models — BS-ANN, CNN-AdaBoost, GRU-CA — and reports their combined performance (p. 188–191)."
  pfm_apps_features: "It describes MyFinanceAI's feature set — predictive budgeting, automated bill management, expense forecasting — and their measured usefulness (p. 189)."
  pfm_apps_importance: "It reports that AI personal-finance tools changed outcomes: monthly savings up 22%, financial literacy scores up 40% (p. 189)."
  budgeting: "The MyFinanceAI predictive budgeting module is explicitly described as using autoregressive integrated moving average and LSTM models to forecast expenses (p. 189)."
---

## Summary

This is a systematic review of machine learning (ML) and deep learning (DL) applied to financial modelling, organised around two task families: classification problems (credit scoring, fraud detection, customer segmentation) and regression problems (stock price prediction, option pricing, volatility forecasting, anomaly detection). The paper states that 41 papers were analysed. It surveys traditional models (logistic regression, decision trees, support vector machines, random forests) alongside deep architectures (deep belief networks, convolutional neural networks, long short-term memory networks, graph convolutional networks) and hybrid constructions (BS-ANN, CNN-AdaBoost, GRU-CA). Its headline quantitative claims are that XGBoost is the strongest credit-scoring model across the metrics reviewed, that random forest and XGBoost reach 99.6%–99.9% accuracy in fraud detection, that LSTM reaches 93% accuracy in Vietnamese stock-price trend prediction, that a Black-Scholes-ANN hybrid reduces option-pricing error and increases stability, and that a GRU-CA hybrid reduces anomaly-detection RMSE from 13.28 to 9.74 on S&P 500 data. A short section reviews AI personalization in personal finance (MyFinanceAI, chatbots, recommendation models), where the paper reports savings, retention, and literacy gains. The paper closes by naming explainable AI, federated learning, and quantum computing as future directions, and by listing interpretability, data quality, concept drift, and fairness/regulatory compliance as unresolved challenges. The review has no stated search protocol, screening procedure, or quality appraisal, and the two comparative tables are poorly aligned in the source, so several of its comparative claims cannot be reconstructed from the printed material.

## Problem and Motivation

Financial institutions now hold datasets that traditional analytical methods struggle to process effectively. ML and DL models analyse these large volumes of data with improved predictive accuracy and more informed decision-making. The paper identifies three practical domains where this matters: credit scoring (DL models improve assessment of borrowers' creditworthiness and reduce default rates), fraud detection (ML algorithms improve identification of fraudulent activities by analysing transaction patterns and anomalies), and market forecasting (DL techniques improve accuracy of predicting market trends). The urgency is framed by three trends — explainable AI, federated learning, and quantum computing — which the paper says address data privacy, model interpretability, and computational limitations, respectively. Prior reviews are acknowledged [4–7], covering ML/DL in financial applications, DL in economics, ML in business and finance, and DL for financial time series forecasting. Despite those reviews, the paper says challenges remain: data imbalance, model transparency, and the need for evaluation metrics. The "uninvestigated parts" it names are model interpretability (many models are "black boxes" whose decision-making is hard to understand, which reduces trust and slows adoption in regulated finance), data quality (noise, missing values, imbalanced classes, restricted access to proprietary data), and concept drift (dynamic market conditions make historical models outdated and reduce predictive accuracy). The stated research objective is to systemize existing knowledge, evaluate the efficacy of different ML and DL models, and identify gaps in the current literature to guide future research.

## Method

**Design.** Systematic review (the paper's own label; the abstract calls it a "systematic review", p. 184). No formal review protocol is stated — there is no PRISMA flow, no search string, no database list, no inclusion/exclusion criteria, no screening procedure, and no risk-of-bias or quality appraisal.
**Sample.** N = 41 papers reviewed (the abstract and conclusion both state "A total of 41 papers were analysed"); the unit of analysis is the published paper/study, not a human participant.
**Context.** geography: Not reported (the reviewed literature is international; no country or region is stated as the scope of the review, though individual reviewed studies cover the U.S., Vietnam, Korea, China, and Germany); population: Not applicable (the unit of analysis is published papers, not people); setting: Desk-based synthesis of English-language ML/DL financial-modelling literature, spanning credit scoring, fraud detection, customer segmentation, stock price prediction, option pricing, volatility forecasting, and anomaly detection.

The review's own workflow, as printed:

- Group the literature into two task families: classification problems (credit scoring, fraud detection, customer segmentation) and regression problems (stock price prediction, volatility forecasting, option pricing, anomaly detection).
- For classification, review traditional ML first (decision trees, SVMs, logistic regression), then DL architectures (DBN, CNN, LSTM, autoencoders), then hybrid constructions (CNN-AdaBoost, GCN).
- For regression, review traditional approaches (linear regression, PCA-linear regression, Black-Scholes, binomial tree, Monte Carlo) against ML/DL approaches (LSTM, XGBoost, random forest, MLP, GRU, GRU-CA).
- Assemble two comparative tables: Table 1 for classification applications, Table 2 for option pricing and anomaly detection.
- Assess models on performance metrics (AUC, accuracy, F1, precision, recall, RMSE, standard deviation), interpretability, and trade-offs between accuracy, computational complexity, and generalizability.
- Treat credit scoring, fraud detection, AI personalization, stock price prediction, option pricing, and anomaly detection as separate evidence clusters, each with its own cited studies.
- Close by listing challenges (data quality, ethics, integration with traditional financial frameworks) and future directions (explainable AI, federated learning, quantum computing).

## Key Findings

- In credit scoring, the review reports that the study of Gunnarsson et al. [19] over 10 retail credit-scoring datasets found XGBoost consistently outperformed all other models on AUC, Brier score, partial Gini, and expected maximum profit, and that deep neural networks did not significantly outperform shallower ML models while being considerably more computationally expensive. The review's own conclusion nonetheless states that "DL models such as DBN and CNNs showed good performance over traditional ML models like logistic regression and decision trees", which is in tension with the [19] finding.
- Fairness in credit scoring is quantified: reducing fairness violations below a 0.2 separation-metric threshold cost approximately 4.91% in profit, while perfect fairness would cost over a 35% drop in profitability, making it financially unfeasible for lenders [15].
- SHAP values were the most effective explanation method in a 2D-CNN credit-scoring framework, raising classification accuracy to 99% and 100% in test cases [18].
- In fraud detection, an ensemble-feature-selection random forest reached an ROC score of 95.83%, accuracy of 99.6%, F1 of 99.6%, and precision of 100% [21]; a separate random forest on SMOTE-balanced data reached 99.9% accuracy [22].
- A CNN fraud detector reached AUC of 87.64% on the European dataset and 70.56% on the German dataset, reduced cost of failure by nearly 30%, and beat random forest and SVM by 5–10% AUC [24].
- A CNN-AdaBoost hybrid reached 96.35% accuracy in electricity-theft detection, beating logistic regression (84.05%), decision trees (90.05%), random forest (90.98%), and SVM (90.88%) [25].
- A GCN reached 94.5% fraud-detection accuracy, beating CNN (93%), random forest (85%), logistic regression (82%), and SVM (84%), with recall of 83.3% against a 70% traditional-model average [26].
- In AI personalization, payment recommendations raised engagement by 27%, retention by 15%, and conversion by 20% [28]; MyFinanceAI reported 85% of users with reduced stress, 43% decrease in anxiety scores, 22% increase in monthly savings ($317 per user per month), 92% avoiding late fees ($185 saved per user), 30% better expense-forecasting accuracy, and 40% higher literacy scores [29].
- In regression, LSTM reached 93% accuracy in Vietnamese stock-price trend prediction [32]; a BS-ANN hybrid had the lowest standard deviation among tested option-pricing models [36]; Black-Scholes and the binomial tree had the lowest RMSE across timeframes (0.650 weekly, 0.641 monthly, 0.385 for 50-day maturities), while ML models had much higher RMSE (XGBoost 6.307, random forest 5.097, MLP 21.351 weekly) but higher simulated profitability [37].
- In anomaly detection, a GRU-CA hybrid reduced RMSE from 13.28, 13.27, and 13.29 (GRU alone) to 9.76, 9.78, and 9.74 on S&P 500 data [40].
- The paper's conclusion states that in option pricing, hybrid models such as BS-ANN outperformed traditional pricing methods by reducing mispricing errors and improving stability, while Monte Carlo simulations provided comparable results but were computationally expensive and impractical for real-time application.

## Key Figures and Tables

- Table 1 (p. 189), "Comparative analysis of ML and DL models in financial applications", lists ten rows: Decision Trees & SVM [8-9], Neural networks [13], Deep Belief Networks (DBN) [17], Convolutional neural networks (CNN) [24], Long short-term memory (LSTM) [29], Random forest (RF) [20-22], XGBoost [19], Graph convolutional networks (GCN) [26], AI Personalization [28-30], and Hybrid CNN-AdaBoost [25]. The table's two middle columns are labelled "Findings" and "Metrics and performance", but in the source extraction the performance values and the findings text are transposed relative to their headers, so column membership cannot be relied on.
- Table 2 (p. 192), "Comparative analysis of ML and DL in option pricing and anomaly detection", lists nine rows: Linear Regression [31, 33, 34], LSTM [32], Black-Scholes-ANN Hybrid (BS-ANN) [36], Monte Carlo Simulation [37], XGBoost & Random Forest (RF) [37], GRU-CA Hybrid [40], Gaussian Mixture Model (GMM) [41], Clustering-Based Models (BIRCH, DenStream, CluStream) [41], and Nearest-Neighbor Models (k-NN, LOF, iLOF) [41]. The "Findings" and "Metrics" columns describe the models qualitatively and quantitatively but the table omits any comparative baseline values for the anomaly-detection rows.
- No figures are printed in the paper. The only visual elements are Table 1 (p. 189) and Table 2 (p. 192).
- The paper's two tables are not reproduced with consistent column semantics in the source, so any downstream use of Table 1's "Metrics and performance" column should be checked against the narrative text on pp. 186–189.

## Definitions

- **ML (machine learning)** — Algorithms that learn from data to improve predictive accuracy in financial modelling, in contrast to traditional statistical methods.
- **DL (deep learning)** — Neural-network models with multiple layers that process unstructured data (text, images) for complex financial tasks such as sentiment analysis of news for stock-price prediction.
- **DBN (deep belief network)** — A deep generative architecture reviewed for credit scoring, reported to achieve higher accuracy than shallower networks [17].
- **CNN (convolutional neural network)** — A deep architecture reviewed for fraud detection (AUC 87.64% European, 70.56% German) and credit scoring (2D-CNN with SHAP explanations) [18, 24].
- **LSTM (long short-term memory)** — A recurrent architecture reviewed for capturing temporal dependencies in stock-price data and for expense forecasting [29, 32].
- **GCN (graph convolutional network)** — A deep architecture that learns node-level and edge-level features on graph-structured user data for fraud and insider-threat detection [26].
- **XGBoost (extreme gradient boosting)** — A gradient-boosted tree ensemble described as the best-performing credit-scoring model across AUC, Brier score, partial Gini, and expected maximum profit [19].
- **BS-ANN (Black-Scholes–Artificial Neural Network)** — A hybrid option-pricing model combining the Black-Scholes-Merton formulation with an ANN; reported to have the lowest standard deviation among tested models [36].
- **GRU-CA (gated recurrent unit with contextual attention)** — A hybrid anomaly-detection model combining a GRU with an attention module; reported to reduce RMSE from 13.28 to 9.74 on S&P 500 data [40].
- **GMM (Gaussian Mixture Model)** — A statistical anomaly-detection method that assigns an anomaly score based on the probability of data deviating from an estimated distribution; limited adaptability to evolving streams [41].
- **SMOTE (synthetic minority over-sampling technique)** — An oversampling method used to address class imbalance in fraud and electricity-theft datasets [22, 25].
- **AUC** — Area under the receiver operating characteristic curve, the primary metric in the reviewed credit-scoring and fraud-detection comparisons.
- **RMSE** — Root mean square error, the primary metric in the reviewed option-pricing and anomaly-detection comparisons.
- **SHAP** — A feature-attribution explanation method reported as the most effective in the reviewed 2D-CNN credit-scoring framework [18].
- **Concept drift** — The paper's term for the phenomenon in which market conditions change over time and models trained on historical data become outdated, reducing predictive accuracy.
- **Explainable AI, federated learning, quantum computing** — The three future directions the paper names for financial modelling.

## Limitations and Gaps

- The paper states that many ML and DL models operate as "black boxes" and that this lack of transparency reduces trust and slows adoption in financial institutions where interpretability is used for regulatory compliance and risk management (p. 185). It names this as a central uninvestigated part.
- The paper states that financial datasets often contain noise, missing values, or imbalanced classes, that this can introduce biases in model training, and that access to high-quality proprietary financial data is frequently restricted (p. 185).
- The paper states that concept drift is still a major limitation in financial modelling: market conditions are dynamic, statistical properties change over time, and models trained on historical data may become outdated (p. 185).
- The paper acknowledges fairness and regulatory compliance as remaining concerns for widespread adoption of DL credit scoring (Conclusion, p. 192): "challenges such as fairness in credit decision-making and regulatory compliance remain concerns for widespread adoption."
- The paper acknowledges that Monte Carlo option-pricing simulations were "computationally expensive, limiting their real-time application" (Conclusion, p. 193).
- [unacknowledged] The review claims to be "systematic" but reports no search strategy, no database list, no inclusion or exclusion criteria, no screening or full-text selection procedure, no PRISMA flow, and no quality appraisal. The 41-paper count cannot be independently verified from the printed material, and several references are cited as background rather than analysed.
- [unacknowledged] The abstract claims coverage of "algorithmic trading", "transformer-based models for sentiment analysis", and "portfolio optimization" (p. 184), but the body contains no section on algorithmic trading, no discussion of transformer-based models, and only incidental mentions of sentiment analysis and portfolio optimization. The stated coverage over-reaches what is delivered.
- [unacknowledged] The review's own conclusion contradicts a finding it reports from reference [19]. The review states at p. 187 that [19] concluded "DL is not the most suitable approach for credit scoring, and XGBoost should be preferred for optimal classification performance", and that deep networks "do not significantly outperform shallower ML models and are considerably more computationally expensive". The conclusion at p. 192 nevertheless states that "DL models such as DBN and CNNs showed good performance over traditional ML models like logistic regression and decision trees." Both statements are retained here without reconciliation.
- [unacknowledged] Table 1 lists "AI Personalization" and "Hybrid CNN-AdaBoost" alongside model families (DBN, CNN, LSTM, RF, XGBoost, GCN) as if they were models. AI personalization is an application category, not a model, so the table's category scheme is inconsistent.
- [unacknowledged] Table 1's "Findings" and "Metrics and performance" columns are transposed relative to their headers in the source, and Table 2's "Findings" and "Metrics" columns overlap. Downstream extraction from these tables is error-prone.
- [unacknowledged] No per-study effect sizes, confidence intervals, or significance tests are reported for any of the reviewed results. The review reproduces point values without uncertainty information, so none of its comparative claims can be statistically assessed.
- [unacknowledged] The review does not state how studies were weighted, whether any were excluded for quality reasons, or whether the 41 papers were selected from a larger pool. The reader cannot tell whether the review is exhaustive or illustrative.
- [unacknowledged] The LSTM row in Table 1 is filed under "improved expense forecasting accuracy by 30%" with a citation to [29] (MyFinanceAI), while in the regression section LSTM is discussed for stock-price prediction [32]. The two uses are not reconciled, and the row conflates a PFM expense-forecasting result with a stock-price forecasting architecture.
- [unacknowledged] The paper's claims about AI personalization (27% engagement, 15% retention, 20% conversion, 40% literacy) come from vendor-style case studies [28–30] with no described sampling frame, control group, or statistical test. Their evidentiary status is much weaker than the paper's presentation implies.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| World adult population lacking access to banking services | share | nearly one-third | — | — | p. 186, citing [14] |
| Total outstanding retail credit in the U.S. in 2020 | USD | $4,161 billion | — | — | p. 186, citing [15] |
| Profit loss from reducing credit-scoring fairness violations below a 0.2 separation-metric threshold | profit loss | approximately 4.91% | — | — | p. 186, citing [15] |
| Profitability drop from achieving perfect fairness in credit scoring | profit drop | over 35% | — | — | p. 186, citing [15] |
| SHAP-based 2D-CNN credit-scoring classification accuracy | accuracy | 99% and 100% | — | — | p. 186, citing [18] |
| Retail credit-scoring datasets used by Gunnarsson et al. | datasets | 10 | — | — | p. 187, citing [19] |
| Performance metrics used by Gunnarsson et al. | metrics | 4 | — | — | p. 187, citing [19] |
| Random forest fraud detection with ensemble feature selection | ROC score | 95.83% | — | — | p. 187, citing [21] |
| Random forest fraud detection with ensemble feature selection | accuracy | 99.6% | — | — | p. 187, citing [21] |
| Random forest fraud detection with ensemble feature selection | F1-score | 99.6% | — | — | p. 187, citing [21] |
| Random forest fraud detection with ensemble feature selection | precision | 100% | — | — | p. 187, citing [21] |
| Random forest credit-card fraud model, training set | rows | 1.3 million | — | — | p. 187, citing [22] |
| Random forest credit-card fraud model, test set | rows | 550,000 | — | — | p. 187, citing [22] |
| Random forest credit-card fraud model on SMOTE-balanced data | accuracy | 99.9% | — | — | p. 187, citing [22] |
| CNN fraud detection on European dataset | AUC | 87.64% | — | — | p. 187, citing [24] |
| CNN fraud detection on German dataset | AUC | 70.56% | — | — | p. 187, citing [24] |
| CNN fraud detection, cost of failure | reduction | nearly 30% | — | — | p. 187, citing [24] |
| CNN fraud detection advantage over random forest and SVM | AUC margin | 5-10% | — | — | p. 187, citing [24] |
| Fraudulent share of total transactions in fraud datasets | share | less than 1% | — | — | p. 187, citing [24] |
| State Grid Corporation of China electricity-theft dataset | observations | 42,372 | — | — | p. 188, citing [25] |
| State Grid Corporation of China electricity-theft dataset, fraudulent records | records | 3,579 | — | — | p. 188, citing [25] |
| CNN-AdaBoost electricity-theft detection | accuracy | 96.35% | — | — | p. 188, citing [25] |
| Logistic regression electricity-theft detection | accuracy | 84.05% | — | — | p. 188, citing [25] |
| Decision trees electricity-theft detection | accuracy | 90.05% | — | — | p. 188, citing [25] |
| Random forest electricity-theft detection | accuracy | 90.98% | — | — | p. 188, citing [25] |
| Support vector machines electricity-theft detection | accuracy | 90.88% | — | — | p. 188, citing [25] |
| CNN-AdaBoost electricity-theft detection | RMSE | 0.2880 | — | — | p. 188, citing [25] |
| CNN-AdaBoost electricity-theft detection | F1-score | 95.60 | — | — | p. 188, citing [25] |
| CMU CERT v4.2 insider-threat dataset | users | 1,000 | — | — | p. 188, citing [26] |
| CMU CERT v4.2 insider-threat dataset | months of activity | 16 | — | — | p. 188, citing [26] |
| GCN fraud detection | accuracy | 94.5% | — | — | p. 188, citing [26] |
| CNN fraud detection (GCN comparison) | accuracy | 93% | — | — | p. 188, citing [26] |
| Random forest fraud detection (GCN comparison) | accuracy | 85% | — | — | p. 188, citing [26] |
| Logistic regression fraud detection (GCN comparison) | accuracy | 82% | — | — | p. 188, citing [26] |
| Support vector machines fraud detection (GCN comparison) | accuracy | 84% | — | — | p. 188, citing [26] |
| GCN fraud detection | recall rate | 83.3% | — | — | p. 188, citing [26] |
| Traditional models fraud detection, average | recall rate | 70% | — | — | p. 188, citing [26] |
| AI personalized payment recommendations | engagement increase | 27% | — | — | p. 188, citing [28] |
| Fintech AI personalization | customer retention rise | 15% | — | — | p. 188, citing [28] |
| Fintech AI personalization | conversion-rate boost | 20% | — | — | p. 188, citing [28] |
| MyFinanceAI pilot study | users | 1,000 | — | — | p. 189, citing [29] |
| MyFinanceAI pilot study | duration | 6 months | — | — | p. 189, citing [29] |
| MyFinanceAI users reporting reduced financial stress | share | 85% | — | — | p. 189, citing [29] |
| MyFinanceAI financial anxiety scale decrease | decrease | 43% | — | — | p. 189, citing [29] |
| MyFinanceAI monthly savings increase | increase | 22% | — | — | p. 189, citing [29] |
| MyFinanceAI additional savings per user per month | USD | $317 | — | — | p. 189, citing [29] |
| MyFinanceAI users avoiding late fees | share | 92% | — | — | p. 189, citing [29] |
| MyFinanceAI average saving from avoiding late fees per user | USD | $185 | — | — | p. 189, citing [29] |
| MyFinanceAI predictive budgeting expense-forecasting improvement | accuracy improvement | 30% | — | — | p. 189, citing [29] |
| MyFinanceAI financial literacy score increase | increase | 40% | — | — | p. 189, citing [29] |
| AI personalization in financial institutions | customer engagement increase | 20% | — | — | p. 189, citing [30] |
| AI personalization in financial institutions | customer retention rise | 15% | — | — | p. 189, citing [30] |
| AI chatbots and virtual assistants, customer wait times | reduction | up to 35% | — | — | p. 189, citing [30] |
| AI chatbots, customer response times | improvement | 18% | — | — | p. 189, citing [30] |
| AI chatbots, bank operational costs | reduction | 25% | — | — | p. 189, citing [30] |
| LSTM Vietnamese stock-price trend prediction | accuracy | 93% | — | — | p. 190, citing [32] |
| Linear regression Google stock-price study | historical data | 14 years | — | — | p. 190, citing [33] |
| Black-Scholes and binomial tree option pricing, weekly predictions | RMSE | 0.650 | — | — | p. 190, citing [37] |
| Black-Scholes and binomial tree option pricing, monthly predictions | RMSE | 0.641 | — | — | p. 190, citing [37] |
| Black-Scholes and binomial tree option pricing, 50-day maturities | RMSE | 0.385 | — | — | p. 190, citing [37] |
| Monte Carlo simulation with variance reduction | RMSE range | 0.485-0.686 | — | — | p. 190, citing [37] |
| XGBoost option pricing, weekly predictions | RMSE | 6.307 | — | — | p. 190, citing [37] |
| Random forest option pricing, weekly predictions | RMSE | 5.097 | — | — | p. 190, citing [37] |
| MLP option pricing, weekly predictions | RMSE | 21.351 | — | — | p. 190, citing [37] |
| GRU anomaly detection, across prediction horizons | RMSE | 13.28, 13.27, and 13.29 | — | — | p. 191, citing [40] |
| GRU-CA anomaly detection, across prediction horizons | RMSE | 9.76, 9.78, and 9.74 | — | — | p. 191, citing [40] |
| S&P 500 anomaly-detection experiment, training share | share | 70% | — | — | p. 191, citing [40] |
| S&P 500 anomaly-detection experiment, testing share | share | 30% | — | — | p. 191, citing [40] |
| Table 1, Decision Trees & SVM, credit scoring and fraud detection | qualitative finding | improved accuracy over statistical methods | — | — | Table 1, p. 189 |
| Table 1, Neural networks, credit scoring | qualitative finding | improved default prediction; outperformed logistic regression | — | — | Table 1, p. 189 |
| Table 1, DBN, credit scoring | qualitative finding | higher accuracy than shallow networks | — | — | Table 1, p. 189 |
| Table 1, CNN, fraud detection | AUC | 87.64% | — | — | Table 1, p. 189 |
| Table 1, CNN, fraud detection, cost of failure | reduction | 30% | — | — | Table 1, p. 189 |
| Table 1, LSTM, expense forecasting | accuracy improvement | 30% | — | — | Table 1, p. 189 |
| Table 1, Random forest, fraud detection | accuracy | 99.6% | — | — | Table 1, p. 189 |
| Table 1, Random forest, fraud detection | precision | 100% | — | — | Table 1, p. 189 |
| Table 1, XGBoost, credit scoring | qualitative finding | outperformed all models; highest accuracy and efficiency | — | — | Table 1, p. 189 |
| Table 1, GCN, fraud detection vs CNN | accuracy | 94.5% vs. 93% | — | — | Table 1, p. 189 |
| Table 1, GCN, fraud detection recall improvement | recall improvement | 10% | — | — | Table 1, p. 189 |
| Table 1, AI Personalization, retention | retention boost | 15% | — | — | Table 1, p. 189 |
| Table 1, AI Personalization, engagement | engagement boost | 27% | — | — | Table 1, p. 189 |
| Table 1, AI Personalization, conversion | conversion boost | 20% | — | — | Table 1, p. 189 |
| Table 1, Hybrid CNN-AdaBoost, electricity-theft detection | accuracy | 96.35% | — | — | Table 1, p. 189 |
| Table 2, Linear Regression, Google stock price | qualitative finding | high confidence in trend forecasting; struggles with nonlinear trends | — | — | Table 2, p. 192 |
| Table 2, LSTM, Vietnamese stock prices | accuracy | 93% | — | — | Table 2, p. 192 |
| Table 2, BS-ANN, European option pricing | qualitative finding | lowest pricing error and standard deviation among tested models | — | — | Table 2, p. 192 |
| Table 2, Monte Carlo Simulation, option pricing | RMSE range | 0.485-0.686 | — | — | Table 2, p. 192 |
| Table 2, XGBoost, option pricing | RMSE | 6.307 | — | — | Table 2, p. 192 |
| Table 2, Random Forest, option pricing | RMSE | 5.097 | — | — | Table 2, p. 192 |
| Table 2, GRU-CA, S&P 500 anomaly detection | RMSE reduction | from 13.28 to 9.74 | — | — | Table 2, p. 192 |
| Table 2, GMM, anomaly detection | qualitative finding | requires strong prior knowledge of data distribution | — | — | Table 2, p. 192 |
| Table 2, Clustering-Based Models, anomaly detection | qualitative finding | reduces computational overhead in evolving datasets | — | — | Table 2, p. 192 |
| Table 2, Nearest-Neighbor Models, anomaly detection | qualitative finding | high precision but memory-intensive | — | — | Table 2, p. 192 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "A total of 41 papers were analysed to identify trends, methodologies, and research gaps in this domain." | Abstract, p. 184 | model_performance_evaluation |
| "Many ML and DL models operate as "black boxes", difficult to understand their decision-making processes." | p. 185 | model_performance_evaluation |
| "The problem of concept drift is still a major limitation in financial modelling." | p. 185 | model_performance_evaluation |
| "The results show that XGBoost consistently outperforms all other models, achieving the highest ranking across all performance measures." | p. 187 | model_performance_evaluation |
| "The paper concludes that DL is not the most suitable approach for credit scoring, and XGBoost should be preferred for optimal classification performance due to its superior accuracy and efficiency" | p. 187 | model_performance_evaluation |
| "The random forest model achieves an accuracy of 99.6%, with an F1-score of 99.6% and precision of 100%" | p. 187 | model_performance_evaluation |
| "Experimental results show that the CNN-AdaBoost model achieves a classification accuracy of 96.35%" | p. 188 | model_algorithm_integration |
| "GCN achieves a fraud detection accuracy of 94.5%, outperforming CNN (93%), random forest (85%), logistic regression (82%), and support vector machines (84%)." | p. 188 | model_algorithm_integration |
| "MyFinanceAI system integrates DNNs and reinforcement learning to provide personalized financial recommendations based on real transaction data, spending habits, and financial goals." | p. 188 | pfm_apps_features |
| "The predictive budgeting module uses autoregressive integrated moving average and LSTM models, improving expense forecasting accuracy by 30% compared to traditional regression models." | p. 189 | budgeting |
| "Additionally, monthly savings increased by 22%, translating to an average additional savings of $317 per user per month." | p. 189 | pfm_apps_importance |
| "In stock price prediction, traditional linear regression models performed well for short-term forecasting but struggled with market complexities." | Conclusion, p. 192 | model_performance_evaluation |
| "In option pricing, hybrid models such as BS-ANN outperformed traditional pricing methods by reducing mispricing errors and improving stability." | Conclusion, p. 193 | model_algorithm_integration |
| "Future research directions should focus on explainable AI methods to improve model transparency, federated learning to improve data privacy in financial applications, and quantum computing to address computational limitations in high-dimensional modelling tasks." | Conclusion, p. 193 | model_performance_evaluation |
| "The paper also identifies challenges, including data quality, ethical concerns, models, and the integration of ML/DL with traditional financial frameworks." | Abstract, p. 184 | model_performance_evaluation |

## Remember This

- This is a 41-paper systematic review of ML/DL in finance, split into classification tasks (credit scoring, fraud detection, customer segmentation) and regression tasks (stock price prediction, option pricing, volatility forecasting, anomaly detection).
- The paper's strongest comparative claim is that XGBoost is the best credit-scoring model across AUC, Brier score, partial Gini, and expected maximum profit — and that DL does not significantly beat shallower models in credit scoring [19].
- Fraud detection results cluster at 99.6%–99.9% accuracy for random forest and 94.5% for GCN; CNN fraud AUC is 87.64% (European) and 70.56% (German).
- In stock-price prediction, LSTM reaches 93% accuracy; in option pricing, Black-Scholes and the binomial tree have the lowest RMSE (0.650 weekly, 0.385 for 50-day maturities) while XGBoost and random forest are less accurate but more profitable in simulation.
- The AI personalization section (MyFinanceAI, chatbots, recommendation models) reports savings, retention, engagement, and literacy gains, but these come from case-study sources with no stated sampling frame or significance testing.
- The paper names explainable AI, federated learning, and quantum computing as future directions; interpretability, data quality, concept drift, and fairness are its named challenges.
- The review has no search protocol, no screening procedure, no quality appraisal, and its two tables are misaligned in the source; its abstract also claims coverage of algorithmic trading, transformers, and portfolio optimization that the body does not deliver.

## Cited Works

- Amoako, E. K. W.; Boateng, V.; Ajay, O.; Adukpo, T. K.; Mensah, N. (2025) (context) — Systematic review of ML/DL in anti-money-laundering strategies in the U.S. financial industry, cited as one of the fraud-detection anchors. [ref. 1]
- Rajendran, S.; John, A. A.; Suhas, B.; Sahana, B. (2023) (context) — Role of ML and DL in detecting fraudulent transactions, cited for transaction-pattern fraud detection. [ref. 2]
- Mienye, E.; Jere, N.; Obaido, G.; Mienye, I. D.; Aruleba, K. (2024) (context) — Survey of DL applications and techniques in finance, cited for fraud-detection model effectiveness. [ref. 3]
- Nazareth, N.; Ramana Reddy, Y. Y. (2023) (context) — Literature review of financial applications of machine learning. [ref. 4]
- Zheng, Y.; Xu, Z.; Xiao, A. (2023) (context) — Systematic and critical review of deep learning in economics. [ref. 5]
- Sezer, O. B.; Gudelek, M. U.; Ozbayoglu, A. M. (2020) (context) — Systematic literature review of deep learning for financial time-series forecasting, 2005–2019. [ref. 6]
- Shi, S.; Tse, R.; Luo, W.; D'Addona, S.; Pau, G. (2022) (context) — Systemic review of machine-learning-driven credit risk. [ref. 7]
- Sahin, Y.; Duman, E. (2011) (methodology) — Detecting credit card fraud by decision trees and support vector machines; one of the earliest classification anchors in the review. [ref. 8]
- Huang, C.-L.; Chen, M.-C.; Wang, C.-J. (2007) (methodology) — Credit scoring with a data-mining approach based on support vector machines. [ref. 9]
- Peivandizadeh, A.; Hatami, S.; Nakhjavani, A.; Khoshsima, L.; Qazani, M. R. C.; Haleem, M.; Alizadehsani, R. (2024) (methodology) — Stock market prediction with transductive LSTM and social-media sentiment analysis. [ref. 10]
- Khalil, F.; Pipa, G. (2021) (context) — Whether deep learning and NLP are transcending financial forecasting, examined through news analytics. [ref. 11]
- Liu, C.; Arulappan, A.; Naha, R.; Mahanti, A.; Kamruzzaman, J.; Ra, I.-H. (2024) (context) — Large language models and sentiment analysis in financial markets: review, datasets, and case study. [ref. 12]
- Hang, V.; Sivakulasingam, S.; Wang, H.; Wong, S. T.; Ganatra, M. A.; Luo, J. (2024) (methodology) — Credit-risk prediction with ML and DL on credit-card customers, cited for neural-network default prediction. [ref. 13]
- Kumar, A.; Sharma, S.; Mahdavi, M. (2021) (context) — ML technologies for digital credit scoring in rural finance; the source of the "one-third of adults lack banking access" figure. [ref. 14]
- Kozodoi, N.; Jacob, J.; Lessmann, S. (2021) (methodology) — Fairness in credit scoring: assessment, implementation, and profit implications; source of the 4.91% and 35% fairness–profit figures. [ref. 15]
- Albanesi, S.; Vamossy, D. F. (2019) (methodology) — Predicting consumer default with a deep-learning approach, cited for DL outperforming standard credit-scoring models. [ref. 16]
- Hayashi, Y. (2022) (methodology) — Emerging trends in deep learning for credit scoring; source of the DBN-better-than-shallow finding. [ref. 17]
- Dastile, X.; Celik, T. (2021) (methodology) — Making deep-learning-based predictions for credit scoring explainable; source of the 2D-CNN and SHAP results. [ref. 18]
- Gunnarsson, B. R.; Vanden Broucke, S.; Baesens, B.; Óskarsdóttir, M.; Lemahieu, W. (2021) (methodology) — Deep learning for credit scoring: Do or don't?; the source of the XGBoost-best and DL-not-significantly-better findings, and of the internal tension with the review's own conclusion. [ref. 19]
- Afriyie, J. K.; Tawiah, K.; Pels, W. A.; Addai-Henne, S.; Dwamena, H. A.; Owiredu, E. O.; Ayeh, S. A.; Eshun, J. (2023) (methodology) — Supervised ML for detecting and predicting credit-card fraud. [ref. 20]
- Akazue, M. I.; Debekeme, I. A.; Edje, A. E.; Asuai, C.; Osame, U. J. (2023) (methodology) — Ensemble feature selection to enhance random-forest fraud detection; source of the 95.83% ROC, 99.6% accuracy, 99.6% F1, and 100% precision figures. [ref. 21]
- Mihali, S.-I.; Niță, Ș.-L. (2024) (methodology) — Credit-card fraud detection based on a random forest model; source of the 99.9% accuracy and 1.3M/550K row counts. [ref. 22]
- Chen, Y.; Zhao, C.; Xu, Y.; Nie, C. (2025) (context) — Year-over-year developments in financial fraud detection via deep learning. [ref. 23]
- Raghavan, P.; Gayar, N. E. (2019) (methodology) — Fraud detection using ML and DL; source of the CNN AUC figures (87.64%, 70.56%), the 30% cost-of-failure reduction, and the 5–10% AUC margin. [ref. 24]
- Nirmal, S.; Patil, P.; Kumar, J. R. R. (2024) (methodology) — CNN-AdaBoost hybrid for electricity-theft detection; source of the 96.35% accuracy, RMSE 0.2880, and F1 95.60 figures. [ref. 25]
- Jiang, J.; Chen, J.; Gu, T.; Choo, K.-K. R.; Liu, C.; Yu, M.; Huang, W.; Mohapatra, P. (2019) (methodology) — Anomaly detection with graph convolutional networks for insider threat and fraud; source of the 94.5% GCN accuracy and 83.3% recall figures. [ref. 26]
- Kanaparthi, V. (2024) (context) — AI-based personalization and trust in digital finance. [ref. 27]
- Abba, S. (2022) (methodology) — AI in fintech: personalized payment recommendations; source of the 27% engagement, 15% retention, and 20% conversion figures. [ref. 28]
- Talasila, S. D. (2024) (methodology) — AI-driven personal finance management (MyFinanceAI); source of the 85% stress-reduction, 43% anxiety-decrease, 22% savings, $317, 92%, $185, 30%, and 40% figures, and the source of the predictive-budgeting ARIMA/LSTM description. [ref. 29]
- Bhuiyan, M. S. (2024) (methodology) — Role of AI-enhanced personalization in customer experiences; source of the 20% engagement, 15% retention, 35% wait-time, 18% response-time, and 25% operational-cost figures. [ref. 30]
- Soni, P.; Tewari, Y.; Krishnan, D. (2022) (methodology) — ML approaches in stock-price prediction: systematic review. [ref. 31]
- Phuoc, T.; Anh, P. T. K.; Tam, P. H.; Nguyen, C. V. (2024) (methodology) — Applying ML algorithms to predict stock-price trends in Vietnam; source of the 93% LSTM accuracy figure. [ref. 32]
- Pahwa, K.; Agarwal, N. (2019) (methodology) — Stock market analysis using supervised ML; source of the 14-year Google stock-price application. [ref. 33]
- Misra, M.; Yadav, A. P.; Kaur, H. (2018) (methodology) — Stock market prediction using ML algorithms; source of the PCA-linear-regression improvement. [ref. 34]
- Chowdhury, R.; Mahdy, M. R. C.; Alam, T. N.; Al Quaderi, G. D.; Arifur Rahman, M. (2020) (methodology) — Predicting frontier-market stock prices with ML and a modified Black-Scholes option-pricing model. [ref. 35]
- Shahvaroughi Farahani, M.; Babaei, S.; Esfahani, A. (2024) (methodology) — "Black-Scholes-Artificial Neural Network": a novel option-pricing model; source of the BS-ANN lowest-standard-deviation finding. [ref. 36]
- Kim, S.; Kim, J.; Song, J. (2024) (methodology) — Option pricing and profitability: ML, Black-Scholes, and Monte Carlo compared on KOSPI200; source of the 0.650/0.641/0.385, 0.485–0.686, 6.307, 5.097, and 21.351 RMSE figures. [ref. 37]
- Stanković, Z. Z.; Rajic, M. N.; Božić, Z.; Milosavljević, P.; Păcurar, A.; Borzan, C.; Păcurar, R.; Sabău, E. (2024) (context) — Volatility dynamics of European power-market prices during COVID-19; cited in the volatility-forecasting paragraph. [ref. 38]
- Li, X.; Li, Y.; Liu, X. Y.; Wang, C. D. (2019) (context) — Risk management via anomaly circumvent: mnemonic deep learning for midterm stock prediction; cited in the volatility-forecasting paragraph. [ref. 39]
- Wang, B.; Dong, Y.; Yao, J.; Qin, H.; Wang, J. (2024) (methodology) — Anomaly detection and risk assessment in financial markets using deep neural networks; source of the GRU and GRU-CA RMSE figures (13.28/13.27/13.29 versus 9.76/9.78/9.74) and the 70/30 S&P 500 split. [ref. 40]
- Salehi, M.; Rashidi, L. (2018) (methodology) — Survey on anomaly detection in evolving data; source of the GMM, clustering-based (BIRCH, CluStream, DenStream, DStream), and nearest-neighbor (k-NN, LOF, iLOF) categorisation. [ref. 41]