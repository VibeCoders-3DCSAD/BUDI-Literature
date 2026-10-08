---
paper_id: A--Bhavana-2025
first_author: Bhavana
year: 2025
title: "AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning"
venue: "International Journal of Advanced Research in Computer Science & Technology (IJARCST)"
doi: 10.15662/IJARCST.2025.0805004
designation: algorithm
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, financial_planning, budgeting, savings_debt_management, income_expense_management, model_algorithm_integration, data_collection, model_development, model_performance_evaluation, system_performance_evaluation, software_quality_evaluation]
module_rationale:
  pfm_apps_overview: "Mint, YNAB and PocketGuard are named as current PFM applications whose form and limits frame the study (Sect. I, p. 1)."
  pfm_apps_features: "the system's feature set — budget planning, goal setting, expenditure optimization, anomaly detection and NLG recommendations — is described in the Abstract and Sect. 3.4."
  pfm_apps_problems: "the Abstract states most personal finance applications remain limited to reactive expense tracking, and Sect. I says they are reactive, rule-based and unable to adapt (p. 1)."
  pfm_apps_importance: "the pilot study reports a 22% savings improvement and 78% literacy improvement, framing software-supported planning as outcome-changing (Abstract, p. 1)."
  financial_planning: "the system allocates income across present and future needs through personalized budget planning, financial goal setting and expenditure optimization (Abstract, p. 1)."
  budgeting: "budget planning is the system's central function, with Contextual Bandits and Reinforcement Learning generating personalized budget recommendations (Sect. 3.4.4, p. 5)."
  savings_debt_management: "savings-to-income and debt-to-income ratios are engineered features and the pilot reports a 22% savings improvement (Sect. 3.3, p. 5; Abstract, p. 1)."
  income_expense_management: "transaction categorisation, expense classification and income/expenditure forecasting are core system functions (Sect. 3.2, p. 4; Sect. I, p. 1)."
  model_algorithm_integration: "the Abstract states the system integrates classification, forecasting, anomaly detection and XAI into one architecture (p. 1)."
  data_collection: "Sect. 3.1 lists transaction data, household expenditure surveys, World Bank/IMF/OECD indicators and the European Credit Card Fraud Dataset as sources (p. 4)."
  model_development: "Sect. 3.4 details the multi-model architecture spanning classification, forecasting, anomaly detection and recommendation models (p. 5)."
  model_performance_evaluation: "Sect. 3.7 reports pilot results for classification accuracy, forecasting MAE, anomaly detection accuracy and recommendation adoption (p. 6)."
  system_performance_evaluation: "recommendation adoption rate and user satisfaction are named as system-level evaluation dimensions (Sect. 3.7, p. 6)."
  software_quality_evaluation: "the System Usability Scale (SUS) is listed as the usability evaluation instrument (Sect. 3.7, p. 6)."
---

# AI-Based Wealth Advisory System using Machine Learning and Predictive Analytics for Personalized Budget Planning — Extraction Note

## Summary

The paper introduces AI Wealth Advisor, an intelligent system for personalized budget planning that integrates classification, forecasting, anomaly detection, and explainable AI (XAI) using machine learning and predictive analytics. The system aims to move personal finance applications beyond reactive expense tracking toward proactive wealth management by delivering transparent, real-time financial guidance through natural language generation (NLG). A pilot study with 100 users reported 95% anomaly detection accuracy, a 22% improvement in savings, and enhanced financial literacy for 78% of participants, alongside 91% F1-score for expense classification, a forecasting error of $43/month per user, and a 41% recommendation adoption rate. The paper describes a six-component methodology — datasets, preprocessing, feature engineering, model development, explainability integration, and evaluation — and positions the system against existing tools such as Mint, YNAB, and PocketGuard. It also addresses privacy, fairness, and trust challenges and outlines future directions including reinforcement learning for adaptive budgeting, generative AI for conversational advisory, and integration into wider financial services. The paper is a conceptual architecture and pilot report with no numbered tables or figures in its own results section; the only table is an unnumbered literature review summary whose rows are largely qualitative.

## Problem and Motivation

Financial literacy is a key determinant of economic well-being, shaping individuals' ability to plan, save, invest, and navigate increasingly complex financial ecosystems. However, the Global Financial Literacy Survey (GFLEC, 2023) reported that more than 60% of adults worldwide lack understanding of fundamental concepts such as compound interest, inflation, and risk diversification (Sect. I, p. 1). These deficiencies often result in unsustainable indebtedness, poor retirement planning, and heightened susceptibility to fraud, with consequences particularly severe in emerging economies where access to financial education is limited (Sect. I, p. 1).

Traditional financial management tools such as spreadsheets and ledger systems provide basic record-keeping but lack predictive and adaptive capabilities (Sect. I, p. 1). Modern budgeting applications like Mint, YNAB, and PocketGuard improve automation and visualization but remain primarily reactive, rule-based, and unable to adapt to dynamic financial behaviors (Sect. I, p. 1). Meanwhile, AI and machine learning have demonstrated transformative applications in financial services — fraud detection, risk scoring, and portfolio optimization — but most AI-driven tools remain enterprise-focused, leaving a significant gap in personalized, consumer-centric financial advisory solutions (Sect. I, p. 1).

The paper addresses this gap by proposing AI Wealth Advisor, designed to be predictive, personalized, and interpretable. The system integrates predictive analytics for income and expenditure forecasting, anomaly detection for fraud prevention, XAI for transparency, and NLG for delivering insights in user-friendly language (Sect. I, p. 1). The stated contribution is a novel AI-driven architecture for personal finance, validated through pilot studies, while also addressing challenges of bias, privacy, and user adoption (Sect. I, p. 2).

## Method

**Design.** System architecture and pilot evaluation study; the authors state no formal design label. The methodology is structured into six major components: datasets, preprocessing, feature engineering, model development, explainability integration, and evaluation (Sect. III, p. 4).

**Sample.** n = 100 users (pilot testing); unit of analysis is the individual user (Sect. 3.7, p. 6). The paper reports no demographic breakdown, recruitment method, or study duration for these 100 users.

**Context.** geography: Not reported explicitly; the paper cites U.S. Consumer Expenditure Survey, India's National Sample Survey, European Credit Card Fraud Dataset, World Bank, IMF, and OECD data sources (Sect. 3.1, p. 4); population: individual users of a personal finance advisory system; setting: virtual/computational — the paper describes a system architecture and pilot testing but no live deployment or institutional setting is stated.

The system's methodology proceeds through the following steps:

- Collect transaction data (income deposits, debit and credit card purchases, recurring bill payments, subscription charges) through secure banking APIs enabled by Open Banking/PSD2, complemented by household expenditure surveys (U.S. Consumer Expenditure Survey, India's National Sample Survey) and macroeconomic indicators (inflation rates, employment levels, interest rates, stock indices) from the World Bank, IMF, and OECD (Sect. 3.1, p. 4).
- Use specialized datasets such as the European Credit Card Fraud Dataset for anomaly detection, noting that fraudulent activity typically constitutes less than 1% of all transactions, requiring resampling strategies and algorithms such as Autoencoders and Isolation Forests (Sect. 3.1, p. 4).
- Preprocess raw data through cleaning (duplicate and erroneous entry removal), normalization (currency standardization), categorization (merchant codes and NLP for expense classification into housing, transport, food, healthcare), anonymization (PII stripping for GDPR and CCPA compliance), and imputation (mean substitution, KNN imputation) (Sect. 3.2, p. 4).
- Engineer features including financial ratios (savings-to-income, debt-to-income, liquidity), behavioral patterns (average transaction frequency, spending spikes, seasonality trends), derived indicators (credit utilization rate, financial stress index, monthly net cash flow), and temporal features (day-of-week and month-of-year indicators) (Sect. 3.3, p. 5).
- Develop a multi-model architecture: classification models (XGBoost, Random Forests, BERT-based NLP) for expense categorization; forecasting models (ARIMA, Prophet, LSTM, Transformers) for expenditure prediction; anomaly detection models (Isolation Forests, Autoencoders, GAN-based detectors) for fraud flagging; and a recommendation engine (Contextual Bandits, Reinforcement Learning) for personalized budget and savings advice (Sect. 3.4, p. 5).
- Integrate explainability through SHAP values for feature importance, LIME for model-agnostic interpretability, and rule-based summaries for non-technical users (Sect. 3.5, p. 5).
- Apply security and privacy safeguards: AES-256 encryption at rest, TLS 1.3 in transit, differential privacy, federated learning, and role-based access controls (Sect. 3.6, p. 5).
- Evaluate across classification (accuracy, precision, recall, F1-score), forecasting (MAE, RMSE, R²), anomaly detection (AUC, precision-recall AUC), recommendations (adoption rate, user satisfaction), and usability (SUS) (Sect. 3.7, p. 6).
- Address ethical considerations through fairness-aware algorithms, transparency reports, and consent management (Sect. 3.8, p. 6).

## Software

- XGBoost (version not reported) — classification of structured data (Sect. 3.4.1, p. 5).
- Random Forests (version not reported) — classification of structured data (Sect. 3.4.1, p. 5).
- BERT-based NLP models (version not reported) — classification of unstructured transaction descriptions (Sect. 3.4.1, p. 5).
- ARIMA (version not reported) — short-term linear forecasting (Sect. 3.4.2, p. 5).
- Prophet (Meta) (version not reported) — seasonality-adjusted trend forecasting (Sect. 3.4.2, p. 5).
- LSTM Networks (version not reported) — long-term non-linear forecasting (Sect. 3.4.2, p. 5).
- Transformers (version not reported) — capturing global sequential dependencies (Sect. 3.4.2, p. 5).
- Isolation Forests (version not reported) — outlier detection (Sect. 3.4.3, p. 5).
- Autoencoders (version not reported) — reconstructing transaction patterns (Sect. 3.4.3, p. 5).
- GAN-based anomaly detectors (version not reported) — adversarial detection (Sect. 3.4.3, p. 5).
- Contextual Bandits (version not reported) — adaptive recommendation suggestions (Sect. 3.4.4, p. 5).
- Reinforcement Learning (version not reported) — dynamically adjusting recommendations (Sect. 3.4.4, p. 5).
- SHAP (version not reported) — feature importance explanations (Sect. 3.5, p. 5).
- LIME (version not reported) — model-agnostic interpretability (Sect. 3.5, p. 5).
- AES-256 (version not reported) — data-at-rest encryption (Sect. 3.6, p. 5).
- TLS 1.3 (version not reported) — data-in-transit encryption (Sect. 3.6, p. 5).
- Differential Privacy (version not reported) — controlled noise for user data protection (Sect. 3.6, p. 5).
- Federated Learning (version not reported) — on-device training without centralizing raw data (Sect. 3.6, p. 5).

No implementation language, framework, database, or deployment platform is reported. No model hyperparameters, training data sizes, or validation procedures are given.

## Key Findings

- The pilot study reports anomaly detection accuracy of 95% (Abstract, p. 1; Sect. 3.7, p. 6).
- The pilot study reports a 22% improvement in savings (Abstract, p. 1).
- The pilot study reports enhanced financial literacy for 78% of participants (Abstract, p. 1).
- The pilot study reports expense classification accuracy of 91% F1-score (Sect. 3.7, p. 6).
- The pilot study reports a forecasting error of MAE $43/month per user (Sect. 3.7, p. 6).
- The pilot study reports a recommendation adoption rate of 41% (Sect. 3.7, p. 6).
- The paper cites Mohammed et al. (2021) as achieving 96% fraud detection accuracy and reducing false positives by 12% using Autoencoders with Isolation Forest on European bank transaction logs (Sect. II, p. 2; Table row 1, p. 2).
- The paper cites Zhang et al. (2022) as reducing mean absolute error by 18% using a hybrid ARIMA and Gradient Boosted Decision Trees model on Chinese household expenditure survey data (Sect. II, p. 2; Table row 3, p. 2).
- The paper cites Li et al. (2021) as increasing user engagement by 25% and reducing redundant suggestions using contextual bandits (Sect. II, p. 2; Table row 7, p. 3).
- The paper states that fraudulent activity typically constitutes less than 1% of all transactions (Sect. 3.1, p. 4).
- The paper states that more than 60% of adults worldwide lack understanding of compound interest, inflation, and risk diversification (Sect. I, p. 1).
- The system integrates classification, forecasting, anomaly detection, XAI, and NLG into a single architecture (Abstract, p. 1).
- The paper acknowledges challenges of data privacy, algorithmic bias, and scalability across diverse financial ecosystems (Sect. IV, p. 6).
- The paper identifies future directions: reinforcement learning for adaptive budgeting, generative AI for conversational advisory, and integration into wider financial services (Sect. IV, p. 6).

## Key Figures and Tables

The paper contains no numbered figures and no numbered tables in its own results section. The only table is an unnumbered literature review table spanning pages 2–3, with column headers "No. | Paper Title | Author Name | Key Points | Remark." It has 15 rows. Three rows report specific quantitative results: row 1 (Mohammed et al., 2021 — 96% fraud detection accuracy, 12% false positive reduction), row 3 (Zhang et al., 2022 — 18% MAE reduction), and row 7 (Li et al., 2021 — 25% user engagement increase). The remaining 12 rows contain no numbers.

The paper's own results (Sect. 3.7, p. 6) are presented as a bulleted list, not a table or figure. No visual analytics, workflow diagram, architecture diagram, or screenshot appears in the paper, despite the Abstract stating the report is "supported by visual analytics" (p. 1).

- Table (unnumbered), pp. 2–3: Literature review summary — 15 rows spanning fraud detection, forecasting, advisory, explainability, privacy, fairness, and adoption; only 3 rows report quantitative results. → The table establishes the paper's positioning but provides no comparative benchmark for AI Wealth Advisor itself.
- Abstract, p. 1: Pilot study headline results — 95% anomaly detection accuracy, 22% savings improvement, 78% financial literacy improvement. → These three numbers do not reappear in the body except for anomaly detection accuracy.
- Sect. 3.7, p. 6: Pilot testing results — 91% F1-score expense classification, $43/month/user MAE, 95% anomaly detection accuracy, 41% recommendation adoption rate. → These four numbers constitute the paper's entire empirical results section.

## Limitations and Gaps

- The authors acknowledge that "Challenges include data privacy, algorithmic bias, and scalability across diverse financial ecosystems" (Sect. IV, p. 6).
- The authors acknowledge that "privacy restrictions limit access to real financial records, creating a strong need for synthetic and augmented datasets" (Sect. 3.1, p. 4).
- The authors acknowledge that the paper is a conceptual architecture validated only through a pilot study; no large-scale deployment or longitudinal evaluation is reported.
- [unacknowledged] The paper reports no confidence intervals, no p-values, no standard deviations, and no per-user variance for any of its six pilot results.
- [unacknowledged] The pilot study's methodology is not described: no recruitment procedure, no study duration, no measurement instrument, and no demographic breakdown of the 100 users is given.
- [unacknowledged] The abstract's claims of a "22% improvement in savings" and "enhanced financial literacy for 78% of participants" (p. 1) do not appear anywhere in the body text, leaving their derivation unreproducible.
- [unacknowledged] The paper lists five evaluation dimensions — classification, forecasting, anomaly detection, recommendations, and usability (Sect. 3.7, p. 6) — but reports only four results; no usability (SUS) score is reported despite SUS being named as the instrument.
- [unacknowledged] The paper lists accuracy, precision, recall, and F1-score for classification; MAE, RMSE, and R² for forecasting; AUC and precision-recall AUC for anomaly detection; and adoption rate and user satisfaction for recommendations (Sect. 3.7, p. 6). It reports only F1-score (91%), MAE ($43/month/user), accuracy (95%), and adoption rate (41%). Precision, recall, RMSE, R², AUC, PR-AUC, and user satisfaction are absent.
- [unacknowledged] The paper's own results section (Sect. 3.7, p. 6) is four bullet points. No table, figure, or per-model comparison is provided, so the multi-model architecture's relative performance cannot be assessed.
- [unacknowledged] The paper does not report which model or combination of models produced the reported pilot results, nor the training data size, hyperparameters, or validation strategy for any model.
- [unacknowledged] The paper describes a "multi-model architecture" (Sect. 3.4, p. 5) but provides no ablation study, no baseline comparison of its own, and no statistical test of whether the reported results are significant.
- [unacknowledged] The paper claims "Natural Language Generation (NLG)" translates analytics into "simple, actionable recommendations" (Abstract, p. 1) but the only example of NLG output is a rule-based summary in Sect. 3.5 (p. 5); no NLG model, evaluation, or user comprehension test is reported.
- [unacknowledged] The paper claims XAI integration via SHAP and LIME (Sect. 3.5, p. 5) but reports no interpretability evaluation, no user trust measurement, and no comparison of XAI methods.
- [unacknowledged] The paper reports "Expense classification accuracy = 91% F1-score" (Sect. 3.7, p. 6), conflating accuracy and F1-score, which are distinct metrics; the reported metric is ambiguous.
- [unacknowledged] The paper reports "Forecasting error = MAE of $43/month per user" (Sect. 3.7, p. 6) but does not report the scale of user expenditure, making the magnitude of the error uninterpretable.
- [unacknowledged] The paper reports "Anomaly detection accuracy = 95%" (Sect. 3.7, p. 6) but does not report the class balance of the anomaly detection task, the dataset used, or whether the 95% is on a held-out test set.
- [unacknowledged] The paper states that "fraudulent activity typically constitutes less than 1% of all transactions" (Sect. 3.1, p. 4) but does not report the actual dataset size or the number of fraudulent transactions used in evaluation.
- [unacknowledged] The paper's literature review table (pp. 2–3) has 15 rows, but 12 of them report no quantitative results, so the table cannot support the paper's claim that it reviews "diverse applications and methodological innovations that enhance operational efficiency, accuracy, and trustworthiness" (Sect. II, p. 2).
- [unacknowledged] The paper's reference list contains 15 entries, but several citations in the text (e.g., [3] for Mint, YNAB, PocketGuard; [4]; [18]; [19]) do not map cleanly to the listed references, and some listed references are not cited in the text.
- [unacknowledged] The paper states that the system "has the potential to become a scalable financial companion for individuals worldwide" (Sect. IV, p. 6) but reports no scalability testing, no load testing, and no deployment evaluation.
- [unacknowledged] No ethics approval, informed consent procedure, or data protection review is reported for the 100-user pilot study, despite the paper's own ethical considerations section (Sect. 3.8, p. 6) requiring consent management.
- [unacknowledged] The paper's title and abstract describe an "AI-Based Wealth Advisory System" but the system described is a personal finance and budgeting tool; no investment advisory, portfolio management, or wealth accumulation functionality is implemented or evaluated.
- [unacknowledged] The paper claims "supported by visual analytics" in the Abstract (p. 1) but contains no figures, charts, or visual outputs of any kind.

## Definitions

- **AI Wealth Advisor** — The paper's proposed intelligent system for personalized budget planning, financial goal setting, and expenditure optimization using machine learning and predictive analytics (Abstract, p. 1).
- **Anomaly detection** — Identification of fraudulent or unusual spending behavior using Isolation Forests, Autoencoders, and GAN-based detectors (Sect. 3.4.3, p. 5).
- **Cold-start problem** — The situation where new users with limited transaction history are supported through generalized expenditure patterns from household surveys (Sect. 3.1, p. 4).
- **Contextual Bandits** — An adaptive recommendation approach used for personalized budget and savings suggestions (Sect. 3.4.4, p. 5).
- **Explainable AI (XAI)** — Integration of SHAP values, LIME, and rule-based summaries to provide transparency in model predictions (Sect. 3.5, p. 5).
- **Federated Learning** — Training on user devices without centralizing raw data (Sect. 3.6, p. 5).
- **Financial stress index** — A derived indicator engineered from transaction data (Sect. 3.3, p. 5).
- **MAE (Mean Absolute Error)** — Forecasting evaluation metric reported as $43/month per user in the pilot study (Sect. 3.7, p. 6).
- **Natural Language Generation (NLG)** — The component that translates complex analytics into simple, actionable recommendations (Abstract, p. 1).
- **Open Banking (PSD2)** — The framework enabling secure banking APIs for transaction data access (Sect. 3.1, p. 4).
- **Pilot study** — Testing with 100 users that produced the paper's six reported empirical results (Sect. 3.7, p. 6).
- **System Usability Scale (SUS)** — The usability evaluation instrument listed but not reported (Sect. 3.7, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Anomaly detection accuracy, pilot study | accuracy | 95% | — | — | Abstract, p. 1; Sect. 3.7, p. 6 |
| Savings improvement, pilot study | improvement | 22% | — | — | Abstract, p. 1 |
| Financial literacy improvement, pilot study | proportion of participants | 78% | — | — | Abstract, p. 1 |
| Expense classification accuracy, pilot study | F1-score | 91% | — | — | Sect. 3.7, p. 6 |
| Forecasting error, pilot study | MAE | $43/month per user | — | — | Sect. 3.7, p. 6 |
| Recommendation adoption rate, pilot study | adoption rate | 41% | — | — | Sect. 3.7, p. 6 |
| Pilot testing sample size | users | 100 | — | — | Sect. 3.7, p. 6 |
| Fraud detection accuracy, Mohammed et al. (2021) | accuracy | 96% | — | — | Sect. II, p. 2; Table row 1, p. 2 |
| False positive reduction, Mohammed et al. (2021) | reduction | 12% | — | — | Sect. II, p. 2; Table row 1, p. 2 |
| Mean absolute error reduction, Zhang et al. (2022) | MAE reduction | 18% | — | — | Sect. II, p. 2; Table row 3, p. 2 |
| User engagement increase, Li et al. (2021) | engagement increase | 25% | — | — | Sect. II, p. 2; Table row 7, p. 3 |
| Adults lacking financial understanding, GFLEC (2023) | proportion | more than 60% | — | — | Sect. I, p. 1 |
| Fraud rate in transaction datasets | proportion | less than 1% | — | — | Sect. 3.1, p. 4 |
| Grocery expense deviation example | deviation | 38% | — | — | Sect. 3.5, p. 5 |
| Anomaly probability example | probability | 0.92 | — | — | Sect. 3.5, p. 5 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "most personal finance applications remain limited, focusing primarily on reactive expense tracking rather than proactive wealth management" | Abstract, p. 1 | pfm_apps_problems |
| "This paper introduces AI Wealth Advisor, an intelligent system designed to deliver personalized budget planning, financial goal setting, and expenditure optimization using machine learning and predictive analytics." | Abstract, p. 1 | pfm_apps_features |
| "A pilot study showed promising results: anomaly detection accuracy of 95%, a 22% improvement in savings, and enhanced financial literacy for 78% of participants." | Abstract, p. 1 | pfm_apps_importance |
| "Modern budgeting applications like Mint, YNAB, and PocketGuard [3] improve automation and visualization but remain primarily reactive, rule-based, and unable to adapt to dynamic financial behaviors" | Sect. I, p. 1 | pfm_apps_problems |
| "more than 60% of adults worldwide lack understanding of fundamental concepts such as compound interest, inflation, and risk diversification" | Sect. I, p. 1 | financial_planning |
| "The system integrates classification, forecasting, anomaly detection, and explainable AI (XAI) to provide transparent, real-time financial guidance." | Abstract, p. 1 | model_algorithm_integration |
| "Personalized budget and savings recommendations use: Contextual Bandits [13] for adaptive suggestions. Reinforcement Learning [14] to dynamically adjust recommendations based on user feedback." | Sect. 3.4.4, p. 5 | budgeting |
| "Financial Ratios: Savings-to-income, debt-to-income, and liquidity ratios." | Sect. 3.3, p. 5 | savings_debt_management |
| "These records, often accessed through secure banking APIs enabled by frameworks like Open Banking (PSD2 in Europe), provide time-stamped, user-specific information that allows models to detect spending patterns, forecast future expenditures, and flag unusual behavior." | Sect. 3.1, p. 4 | data_collection |
| "The methodology is structured into six major components: datasets, preprocessing, feature engineering, model development, explainability integration, and evaluation." | Sect. III, p. 4 | model_development |
| "Usability: System Usability Scale (SUS) score [19]." | Sect. 3.7, p. 6 | software_quality_evaluation |
| "For example, instead of 'anomaly detected with probability 0.92,' the system explains: 'Your grocery expenses this week were 38% higher than your usual pattern, likely due to festival-related purchases.'" | Sect. 3.5, p. 5 | model_algorithm_integration |
| "Traditional financial management tools, such as spreadsheets and ledger systems, provide basic record-keeping but lack predictive and adaptive capabilities." | Sect. I, p. 1 | pfm_apps_overview |
| "Pilot testing with 100 users demonstrated: Expense classification accuracy = 91% F1-score. Forecasting error = MAE of $43/month per user. Anomaly detection accuracy = 95%. Recommendation adoption rate = 41%." | Sect. 3.7, p. 6 | model_performance_evaluation |
| "Recommendations: Adoption rate (% of suggestions followed), User Satisfaction (survey-based)." | Sect. 3.7, p. 6 | system_performance_evaluation |

## Remember This

- AI Wealth Advisor is a personal finance and budgeting system that integrates classification, forecasting, anomaly detection, XAI, and NLG.
- The pilot study with 100 users reported 95% anomaly detection accuracy, 22% savings improvement, 78% financial literacy improvement, 91% F1-score expense classification, $43/month/user MAE, and 41% recommendation adoption rate.
- The abstract's 22% savings improvement and 78% financial literacy improvement do not appear in the body text.
- The paper's own results section is four bullet points with no table, no figure, no confidence interval, and no p-value.
- The paper describes a multi-model architecture but reports no per-model performance, no ablation, and no baseline comparison.
- The literature review table has 15 rows but only 3 report quantitative results (Mohammed et al. 96%/12%, Zhang et al. 18%, Li et al. 25%).
- SUS is listed as the usability instrument but no SUS score is reported.
- The paper acknowledges privacy, bias, and scalability challenges but does not test any of them.

## Cited Works

- Mohammed, A., et al. (2021) (baseline) — Autoencoders with Isolation Forest on European bank transaction logs achieved 96% fraud detection accuracy and reduced false positives by 12%. [p. 2]
- Carcillo, F., et al. (2019) (context) — Ensemble learning for anomaly detection in imbalanced credit card data, balancing precision-recall trade-offs for real-time monitoring. [p. 2]
- Zhang, G., et al. (2022) (baseline) — Hybrid ARIMA and neural network model for time series forecasting; reduced household expenditure MAE by 18%. [p. 2]
- Makridakis, S., et al. (2018) (context) — LSTM and RNN architectures outperformed traditional econometric methods and captured seasonal patterns. [p. 2]
- Yang, X., et al. (2023) (context) — NLP-driven financial assistants improved accessibility for low-literacy users and increased financial confidence. [p. 2]
- Bauman, M., et al. (2023) (context) — Deep reinforcement learning for goal-based investing under regime-switching outperformed static asset allocation. [p. 2]
- Li, L., et al. (2021) (methodology) — Contextual bandit approach to personalized recommendation increased user engagement by 25% and reduced redundant suggestions. [p. 2]
- Priya, S., et al. (2024) (context) — XAI frameworks improve interpretability and mitigate compliance risks in AI-driven finance. [p. 2]
- Ribeiro, M. T., et al. (2016) (methodology) — LIME model-agnostic explainability provided transparency in black-box models and enabled validation of credit scoring systems. [p. 2]
- Kury, P., et al. (2025) (context) — Generative AI agents enabled personalized financial advisory but raised transparency and hallucination concerns. [p. 2]
- Abadi, M., et al. (2016) (methodology) — Differential privacy in machine learning preserved data privacy in sensitive financial datasets. [p. 2]
- Barocas, S., et al. (2019) (context) — Fairness and machine learning identified biases in lending algorithms and proposed fairness-aware ML methods. [p. 2]
- Lundberg, S., & Lee, S.-I. (2017) (methodology) — SHAP provided consistent feature attributions and enhanced model interpretability for finance regulators. [p. 3]
- Davis, F. D., et al. (1989) (context) — Technology Adoption Model explained why users accept or reject AI tools and highlighted the importance of simplicity. [p. 3]
- Goodfellow, I., et al. (2016) (context) — Deep learning principles underpinned modern financial forecasting models. [p. 3]
- Global Financial Literacy Survey (GFLEC, 2023) (context) — Reported that more than 60% of adults worldwide lack understanding of fundamental financial concepts. [p. 1]