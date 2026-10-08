---
paper_id: L--Reyes-2024
first_author: Reyes
year: 2024
title: "A Comparative Analysis of Machine Learning Models for Predictive Analytics in Finance"
venue: "International Journal of Applied Mathematics and Computing"
doi: 10.62951/ijamc.v1i1.3

designation: local
status: extracted
modules: [model_performance_evaluation]
module_rationale:
  model_performance_evaluation: "Sect. C (p. 16) names accuracy, precision, recall, F1-score, MAE, computational cost and interpretability as the evaluation metrics, and Sect. D (p. 17) reports accuracy and training-time results for linear regression, decision trees, SVM and deep learning."
---

# L--Reyes-2024

## Summary

This is a short comparative-analysis article on machine learning models for financial predictive analytics, written at the University of the Philippines Diliman, Department of Computer Science, and published in the *International Journal of Applied Mathematics and Computing* (Vol. 1, No. 1, January 2024, pp. 14–20). The stated purpose is to compare "various machine learning models in their ability to predict financial trends, with a focus on time-series analysis," and to evaluate those models on accuracy, computational cost and interpretability (Abstract, p. 14). The paper is organised into five lettered sections: A. Introduction; B. Overview of Machine Learning Models; C. Performance Metrics for Model Evaluation; D. Comparative Analysis of Models; E. Guidelines for Model Selection. There is no dedicated data, method, or statistical-analysis section, no table, and no figure anywhere in the article.

The article proceeds in two registers that are not clearly separated. The first is a literature-grounded narrative: Sect. A and Sect. B summarise what prior work is said to have found about linear regression, decision trees, support vector machines and deep learning in finance, and Sect. C summarises the metric vocabulary the field uses. The second is a claim of original empirical work: Sect. D states that "In our study, we implemented linear regression, decision trees, support vector machines, and deep learning models on a dataset comprising historical stock prices and economic indicators" and then reports an average accuracy rate of 92% for deep learning, 89% for SVM, 83% for decision trees and 78% for linear regression, together with training times of 48 hours, around 1 hour, 30 minutes and 15 minutes respectively (Sect. D, p. 17). The dataset itself is never described beyond that single clause: no source, no sample size, no time span, no feature count, no train/test split and no validation procedure is printed anywhere in the paper.

The headline reading the authors draw is a trade-off. Deep learning "consistently outperformed the other models in terms of accuracy," but its computational cost "was substantially higher," and its complexity "rendered [it] less interpretable" (Sect. D, pp. 17–18). Linear regression and decision trees are presented as the interpretable, cheap end of the spectrum, and SVM as the middle case: competitive accuracy at an intermediate training cost. From this the paper derives a set of selection guidelines in Sect. E (pp. 18–19): simpler models for credit scoring and risk assessment where interpretability and regulatory explainability matter; deep learning where accuracy is the primary objective, such as high-frequency trading or market trend analysis; SVM or deep learning where relationships are complex and non-linear; and an explicit caution that as regulation evolves, "the demand for model transparency and explainability is likely to increase" (Sect. E, p. 19).

The paper also foregrounds interpretability as a first-class evaluation criterion rather than an afterthought. It cites Lipton (2016) for the claim that a lack of interpretability in complex models "can hinder trust and acceptance among financial analysts and decision-makers" (Sect. C, p. 17) and it illustrates the point with two unnamed case studies — a hedge fund using deep learning for high-frequency trading that "achieved remarkable returns but faced challenges in explaining their trading strategies to investors," and a bank using decision trees for credit scoring that "was able to provide clear justifications for loan approvals" (Sect. D, p. 18). Neither case study is sourced.

Because the paper is a comparative review of model families rather than a study of a personal financial management system, and because it reports model-performance quantities (accuracy, training time) rather than household financial behaviour, its fit within this project's taxonomy is narrow: it speaks to how model performance is measured and reported. It contains nothing on seasonal expense forecasting, on SARIMA, on rule-based savings-and-debt profiling, on linear programming for budget generation, on inter-quartile-range anomaly detection, on PFM application features, or on software quality evaluation.

## Problem and Motivation

The paper's motivation is stated at the level of the analyst's dilemma rather than a household or institutional problem. Predictive analytics "has emerged as a critical tool for decision-making" in finance, and with machine learning, analysts "now have access to sophisticated models that can analyze vast amounts of data to predict market trends, assess risks, and optimize investment strategies" (Sect. A, p. 14). The problem the paper sets itself is a trade-off: "A significant challenge in financial modeling is the trade-off between accuracy and interpretability. While complex models like deep learning often yield higher accuracy, their black-box nature makes it difficult for analysts to derive actionable insights. Conversely, simpler models may provide clearer interpretations but at the cost of predictive power" (Sect. A, p. 14). The paper presents itself as addressing that dilemma "by providing a structured comparison of these models, helping practitioners make informed decisions based on their specific needs and constraints" (Sect. A, p. 14).

Two further motivations are pressed into service. The first is commercial scale, via a McKinsey citation: companies that leverage advanced analytics are said to be 23 times more likely to acquire customers, 6 times more likely to retain them and 19 times more likely to be profitable (Sect. A, p. 14). The second is the operational constraint of real-time finance: financial institutions "are increasingly seeking models that balance accuracy with computational efficiency, particularly in high-frequency trading environments," per a Deloitte (2021) citation (Sect. C, p. 17). Time-series data is named as the domain's prevalent data type — "stock prices, interest rates, and economic indicators" — and its complexity is said to "necessitate robust modeling techniques that can capture underlying patterns and trends" (Sect. A, p. 14).

## Method

**Design.** Comparative model-comparison study across four model families on financial time-series data, with a literature-grounded metric framework; the authors state no formal design label.
**Sample.** Not reported — the paper states only that "a dataset comprising historical stock prices and economic indicators" was used (Sect. D, p. 17); no N, no number of series, no number of observations, no time span and no unit of analysis is printed.
**Context.** geography: Not reported; the only institutional affiliation given is the University of the Philippines Diliman, Department of Computer Science (p. 14), which is not stated as the data setting; population: Not reported; setting: computational/offline comparison of four model families — linear regression, decision trees, support vector machines and deep learning — on historical stock prices and economic indicators, with training times quoted "on a standard GPU" for deep learning (Sect. D, p. 17).

Procedure as described in the paper:

- Compare four model families: linear regression, decision trees, support vector machines (SVM), and deep learning (Abstract, p. 14; Sect. D, p. 17).
- Evaluate each on three criteria: accuracy, computational cost, and interpretability (Abstract, p. 14).
- Define the metric vocabulary first, in Sect. C: accuracy, precision, recall, F1-score and mean absolute error (MAE), plus computational cost and interpretability (Sect. C, pp. 16–17).
- Implement the four families "on a dataset comprising historical stock prices and economic indicators" (Sect. D, p. 17).
- Report accuracy per family: deep learning average 92%, SVM 89%, decision trees 83%, linear regression 78% (Sect. D, p. 17).
- Report training time per family: deep learning averaging 48 hours on a standard GPU; SVM averaging around 1 hour; decision trees 30 minutes; linear regression 15 minutes (Sect. D, p. 17).
- Treat interpretability qualitatively rather than numerically, via the decision-path visualisation of decision trees and the black-box characterisation of deep learning (Sect. D, pp. 17–18).
- Illustrate practical consequences with two unsourced case studies — a hedge fund and a bank (Sect. D, p. 18).
- Derive selection guidelines in Sect. E by matching model family to application, data structure, organisational capability and regulatory expectation (Sect. E, pp. 18–19).

The paper does not state a sampling procedure, a train/test split, a cross-validation scheme, a hyperparameter search, a software stack, a random seed, or any statistical test. The only named hardware detail is "a standard GPU" in the deep learning training-time sentence (Sect. D, p. 17).

## Key Findings

- Deep learning models "consistently outperformed the other models in terms of accuracy, achieving an average accuracy rate of 92%" (Sect. D, p. 17).
- Linear regression reached 78% accuracy and decision trees 83% accuracy in the same comparison (Sect. D, p. 17).
- SVM was "competitive, with an accuracy of 89%," but with longer training times than the two simpler models (Sect. D, p. 17).
- Training cost was dramatically asymmetric: 48 hours on a standard GPU for deep learning, versus 15 minutes for linear regression, 30 minutes for decision trees and around 1 hour for SVM (Sect. D, p. 17).
- Interpretability ran the other way: "While deep learning models provided superior accuracy, their complexity rendered them less interpretable" (Sect. D, p. 18).
- Decision trees were singled out for interpretability because they "offered clear visualizations of decision paths, enabling analysts to trace how input variables influenced predictions" (Sect. D, p. 18).
- The paper's guideline conclusion is that linear regression and decision trees suit applications "where interpretability and computational efficiency are paramount," such as credit scoring or risk assessment, while deep learning suits applications where "accuracy is the primary objective, particularly in high-frequency trading or market trend analysis" (Sect. E, p. 18).
- SVM and deep learning are recommended for "datasets with complex, non-linear relationships, such as those often found in financial markets," while linear regression "remains a robust and interpretable option" for more straightforward linear relationships (Sect. E, pp. 18–19).
- Regulatory pressure is expected to increase demand for transparency, pushing institutions toward model-agnostic interpretability methods for complex models (Sect. E, p. 19).
- From cited prior work: Chen et al. (2019) is reported as finding SVM at 87% against 75% for linear regression in stock market trend prediction (Sect. A, p. 15); Kourentzes et al. (2014) as finding SVM at 85% against 75% for linear regression in financial time-series forecasting (Sect. B, p. 15); and Fischer and Krauss (2018) as finding LSTM networks at 90% accuracy in predicting stock price movements (Sect. B, p. 16).
- From cited prior work: Tsai and Wu (2008) is reported as finding that linear regression "yielded satisfactory results in stock price predictions but struggled with high-dimensional datasets" (Sect. B, p. 15), and Zhang et al. (2019) as finding that decision trees "provided clear insights" but that "their predictive accuracy was often lower than that of more complex models, such as ensemble methods" (Sect. B, p. 15).

## Definitions

- **Accuracy** — "the ratio of correctly predicted instances to the total instances"; a fundamental metric that "may not be sufficient on its own, especially in the context of financial data where class imbalance can occur (e.g., predicting defaults in loan applications)" (Sect. C, p. 16).
- **Precision and recall** — metrics the paper says are "essential for assessing the effectiveness of models in scenarios where false positives and false negatives have different implications," citing Saito and Rehmsmeier (2015) (Sect. C, p. 16).
- **F1-score** — listed among the common metrics for evaluating machine learning models in finance; not defined further (Sect. C, p. 16).
- **Mean absolute error (MAE)** — a metric that "quantifies the average magnitude of errors in a set of predictions, without considering their direction," said to be favoured in time-series analysis for giving "a clear indication of the average error in predictions" (Sect. C, p. 16).
- **Linear regression** — "one of the simplest forms of predictive modeling," establishing "a linear relationship between dependent and independent variables"; limited in handling non-linear relationships and multicollinearity (Sect. B, p. 15).
- **Decision trees** — models that "work by recursively splitting data into subsets based on feature values, leading to a tree-like model of decisions"; valued for interpretability, prone to overfitting "especially in the presence of noise in the data" (Sect. B, p. 15).
- **Support Vector Machines (SVM)** — models that "work by finding the optimal hyperplane that separates different classes in the dataset," effective in high-dimensional spaces and able to handle non-linear relationships "through the use of kernel functions" (Sect. B, p. 15).
- **Deep learning** — neural-network models, including recurrent neural networks (RNNs) and long short-term memory (LSTM) networks, "specifically designed to handle sequential data, making them well-suited for time-series analysis in finance" (Sect. B, p. 16).
- **Computational cost** — "the time and resources required to train and deploy models," which "can significantly impact their usability in real-time financial applications" (Sect. C, p. 16).
- **Interpretability** — the property that lets stakeholders obtain "clear explanations for predictions"; linear regression and decision trees are described as generally more interpretable than deep learning models, "which are often seen as black boxes" (Sect. C, p. 17).

## Limitations and Gaps

- [unacknowledged] The empirical claim at the centre of the paper — that "we implemented" four model families on a dataset of historical stock prices and economic indicators (Sect. D, p. 17) — is unsupported by any description of that dataset. No source, sample size, period, feature set, unit of analysis, train/test split or validation procedure appears anywhere in the article, so the reported 92%/89%/83%/78% accuracies cannot be checked, reproduced or compared against anything.
- [unacknowledged] No statistical apparatus accompanies the results. There is no confidence interval, no significance test, no variance across folds or seeds, and no per-model precision, recall, F1-score or MAE value, even though Sect. C names precision, recall, F1-score and MAE as the metrics the field uses (Sect. C, pp. 16–17). The paper defines metrics it then does not report.
- [unacknowledged] The cited accuracies and the paper's own accuracies are not reconciled. Chen et al. (2019) is reported at 87% for SVM and 75% for linear regression (Sect. A, p. 15); Kourentzes et al. (2014) at 85% for SVM and 75% for linear regression (Sect. B, p. 15); the paper's own comparison puts SVM at 89% and linear regression at 78% (Sect. D, p. 17). The paper never comments on the divergence, which matters because two cited studies agree on 75% for linear regression while the paper's own figure is 78%.
- [unacknowledged] Two of the three evaluation criteria are never operationalised. Computational cost is reported only as wall-clock training time on "a standard GPU" of unstated make, with no inference latency, memory footprint or energy figure (Sect. D, p. 17). Interpretability is discussed only in prose, with no measurement instrument, and is never converted into a comparable score (Sect. D, pp. 17–18).
- [unacknowledged] The two case studies used to make the interpretability argument — the hedge fund that achieved "remarkable returns but faced challenges in explaining their trading strategies to investors" and the bank that used decision trees for credit scoring — are presented without any citation, institution, date or data (Sect. D, p. 18). They read as illustration rather than evidence, but they are not labelled as such.
- [unacknowledged] The dataset is described as historical stock prices and economic indicators (Sect. D, p. 17), which is equity-market data, but the guidelines the paper draws are extended to credit scoring, loan approval, risk management and compliance scenarios (Sect. E, p. 18) — domains with different data structures, label semantics and regulatory regimes. No transfer of evidence between the two is argued.
- [unacknowledged] The reference list (pp. 19–20) is printed as a list of titles and venue-years with no author names, and the in-text citations (Chen et al., Tsai and Wu, Zhang et al., Kourentzes et al., Fischer and Krauss, Saito and Rehmsmeier, McKinsey, Deloitte, Lipton) cannot be matched to entries in it unambiguously. Several in-text citations have no corresponding entry identifiable by title.
- [unacknowledged] The claim that companies using advanced analytics are "23 times more likely to acquire customers, 6 times more likely to retain customers, and 19 times more likely to be profitable" is attributed only to "a report by McKinsey" (Sect. A, p. 14), with no title, year or locator, and is used to motivate a methods comparison it does not directly support.
- [unacknowledged] The paper gives no software, library, framework or implementation detail for any of the four model families, so no part of the comparison is reproducible as printed.
- [unacknowledged] The paper's own framing is time-series forecasting (Abstract, p. 14), but the reported accuracy metric is a classification-style accuracy with no statement of forecast horizon, target variable, or whether the task is level forecasting, direction prediction or classification. The metric and the task do not clearly match.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Companies leveraging advanced analytics — customer acquisition, cited to McKinsey (2020) | relative likelihood | 23 times more likely | — | — | Sect. A Introduction, p. 14 |
| Companies leveraging advanced analytics — customer retention, cited to McKinsey (2020) | relative likelihood | 6 times more likely | — | — | Sect. A Introduction, p. 14 |
| Companies leveraging advanced analytics — profitability, cited to McKinsey (2020) | relative likelihood | 19 times more likely | — | — | Sect. A Introduction, p. 14 |
| Stock market trend prediction, SVM, cited to Chen et al. (2019) | accuracy | 87% | — | — | Sect. A Introduction, p. 15 |
| Stock market trend prediction, linear regression, cited to Chen et al. (2019) | accuracy | 75% | — | — | Sect. A Introduction, p. 15 |
| Financial time-series forecasting, SVM, cited to Kourentzes et al. (2014) | accuracy | 85% | — | — | Sect. B Overview of Machine Learning Models, p. 15 |
| Financial time-series forecasting, linear regression, cited to Kourentzes et al. (2014) | accuracy | 75% | — | — | Sect. B Overview of Machine Learning Models, p. 15 |
| Stock price movement prediction, LSTM networks, cited to Fischer and Krauss (2018) | accuracy | 90% | — | — | Sect. B Overview of Machine Learning Models, p. 16 |
| Own comparison, deep learning models | average accuracy rate | 92% | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, SVM | accuracy | 89% | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, decision trees | accuracy | 83% | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, linear regression | accuracy | 78% | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, deep learning models | training time | 48 hours | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, SVM | training time | around 1 hour | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, decision trees | training time | 30 minutes | — | — | Sect. D Comparative Analysis of Models, p. 17 |
| Own comparison, linear regression | training time | 15 minutes | — | — | Sect. D Comparative Analysis of Models, p. 17 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This paper compares various machine learning models in their ability to predict financial trends, with a focus on time-series analysis." | Abstract, p. 14 | model_performance_evaluation |
| "Our results reveal that deep learning models offer superior accuracy but are less interpretable, while simpler models, though less accurate, provide better insight into the underlying data." | Abstract, p. 14 | model_performance_evaluation |
| "A significant challenge in financial modeling is the trade-off between accuracy and interpretability." | Sect. A Introduction, p. 14 | model_performance_evaluation |
| "A study by Chen et al. (2019) demonstrated that SVM outperformed traditional models in predicting stock market trends, achieving an accuracy rate of 87% compared to 75% for linear regression." | Sect. A Introduction, p. 15 | model_performance_evaluation |
| "Research by Fischer and Krauss (2018) showed that LSTM networks achieved an accuracy rate of 90% in predicting stock price movements, significantly outperforming traditional models." | Sect. B Overview of Machine Learning Models, p. 16 | model_performance_evaluation |
| "Accuracy, defined as the ratio of correctly predicted instances to the total instances, is a fundamental metric but may not be sufficient on its own, especially in the context of financial data where class imbalance can occur" | Sect. C Performance Metrics for Model Evaluation, p. 16 | model_performance_evaluation |
| "In our study, we implemented linear regression, decision trees, support vector machines, and deep learning models on a dataset comprising historical stock prices and economic indicators." | Sect. D Comparative Analysis of Models, p. 17 | model_performance_evaluation |
| "The results indicated that deep learning models consistently outperformed the other models in terms of accuracy, achieving an average accuracy rate of 92%." | Sect. D Comparative Analysis of Models, p. 17 | model_performance_evaluation |
| "The performance of SVMs was found to be competitive, with an accuracy of 89%, but they also exhibited longer training times than linear regression and decision trees, averaging around 1 hour." | Sect. D Comparative Analysis of Models, p. 17 | model_performance_evaluation |
| "However, the computational cost of deep learning models was substantially higher, with training times averaging 48 hours on a standard GPU, compared to just 15 minutes for linear regression and 30 minutes for decision trees." | Sect. D Comparative Analysis of Models, p. 17 | model_performance_evaluation |
| "While deep learning models provided superior accuracy, their complexity rendered them less interpretable." | Sect. D Comparative Analysis of Models, p. 18 | model_performance_evaluation |
| "When accuracy is the primary objective, particularly in high-frequency trading or market trend analysis, deep learning models may be the preferred choice." | Sect. E Guidelines for Model Selection, p. 18 | model_performance_evaluation |

## Remember This

- The paper is a five-section comparative review — Introduction, Model Overview, Metrics, Comparative Analysis, Guidelines — with no data section, no table, no figure and no statistical test.
- Its own empirical claim is that four model families were implemented on "a dataset comprising historical stock prices and economic indicators" (p. 17); the dataset is never described further, so the result is not reproducible.
- Reported own-comparison accuracies: deep learning 92%, SVM 89%, decision trees 83%, linear regression 78% (p. 17).
- Reported own-comparison training times: deep learning 48 hours, SVM around 1 hour, decision trees 30 minutes, linear regression 15 minutes (p. 17).
- The paper defines precision, recall, F1-score and MAE in Sect. C and then reports none of them; only accuracy and training time appear in Sect. D.
- The paper's conclusion is a selection heuristic: simple models where interpretability and regulatory explainability dominate, deep learning where accuracy dominates.

## Cited Works

- Chen et al. (2019) (context) — SVM outperformed traditional models in predicting stock market trends, achieving 87% against 75% for linear regression. [p. 15]
- Tsai, S.-H.; Wu, C.-C. (2008) (context) — Linear regression yielded satisfactory results in stock price predictions but struggled with high-dimensional datasets. [p. 15]
- Zhang et al. (2019) (context) — Decision trees provided clear insights but their predictive accuracy was often lower than that of more complex models such as ensemble methods; also cited for the claim that MAE is often favoured in time-series analysis. [pp. 15, 16]
- Kourentzes et al. (2014) (context) — SVMs outperformed linear regression in forecasting financial time series, achieving 85% against 75%. [p. 15]
- Fischer, T.; Krauss, C. (2018) (context) — LSTM networks achieved 90% accuracy in predicting stock price movements, significantly outperforming traditional models. [p. 16]
- Saito, T.; Rehmsmeier, M. (2015) (methodology) — Precision and recall are essential for assessing model effectiveness where false positives and false negatives have different implications. [p. 16]
- McKinsey (2020) (context) — Companies that leverage advanced analytics are 23 times more likely to acquire customers, 6 times more likely to retain customers and 19 times more likely to be profitable. [p. 14]
- Deloitte (2021) (context) — Financial institutions are increasingly seeking models that balance accuracy with computational efficiency, particularly in high-frequency trading environments. [p. 17]
- Lipton, Z. C. (2016) (context) — The lack of interpretability in complex models can hinder trust and acceptance among financial analysts and decision-makers. [p. 17]
- Reference list (pp. 19–20) — Printed as titles with venue-year only, without author names: "A Comparative Analysis of Regression and Neural Network Models in Financial Forecasting"; "A Comparative Study of Supervised and Unsupervised Learning Techniques for Financial Data Analysis"; "A Review of Machine Learning Models in Risk Management and Credit Scoring"; "Applications of Support Vector Machines and Neural Networks in Finance"; "Comparative Analysis of ML Algorithms for Financial Time-Series Prediction"; "Decision Trees, Random Forests, and Gradient Boosting for Financial Forecasting"; "Deep Learning vs. Traditional Models in Predicting Financial Distress"; "Evaluating Machine Learning Techniques for Forecasting Stock Returns"; "Evaluating the Effectiveness of Ensemble Learning Models for Portfolio Optimization"; "Machine Learning Approaches for Predicting Corporate Bankruptcy"; "Machine Learning in High-Frequency Trading: A Comparative Approach"; "Machine Learning Models for Stock Price Prediction: A Comparative Study"; "Predictive Analytics in Financial Markets: Comparing Traditional and Deep Learning Models"; "Predictive Modeling in Finance: A Comparison of ML Models for Market Volatility"; "Time-Series Forecasting for Financial Applications: Comparing ML and Statistical Models."