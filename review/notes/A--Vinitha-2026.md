---
paper_id: A--Vinitha-2026
first_author: Vinitha
year: 2026
title: "AI-Driven Personal Finance Management: Predictive Expense Forecasting and Behavioural Clustering"
venue: "International Journal of Data Science and IoT Management System"
doi: Not reported
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, pfm_apps_overview, pfm_apps_features, pfm_apps_problems, model_algorithm_integration, model_development, system_development, model_performance_evaluation]
module_rationale:
  financial_planning: "The recommendation module computes a surplus between an assumed income and predicted expenses and turns it into a savings or investment suggestion (Sect. 3, p. 464; Fig. 6, p. 466)."
  budgeting: "The system's budget recommendation module generates an investment amount from predicted expenditure so users can allocate income (Sect. 4, Fig. 6, p. 466)."
  savings_debt_management: "The recommendation module explicitly suggests 'potential savings or investment opportunities' from the predicted surplus (Sect. 3, p. 464)."
  income_expense_management: "The core data flow extracts year, month and day from uploaded expenses and clusters expense categories and amounts (Sect. 3, p. 464; Fig. 4, p. 466)."
  pfm_apps_overview: "The paper introduces 'an intelligent financial prediction and analysis platform' and contrasts it with spreadsheets and basic budgeting tools (Abstract, p. 460)."
  pfm_apps_features: "Dashboards, prediction graphs, K-Means clustering views, budget recommendation and VADER feedback classification are described as the system's feature set (Sect. 3, p. 464; Sect. 4, pp. 465-467)."
  pfm_apps_problems: "The paper argues traditional systems 'store transaction data but lack advanced analytical capabilities' and that manual tracking is complex and error-prone (Abstract, p. 460)."
  model_algorithm_integration: "The architecture combines an LSTM forecaster, a K-Means clusterer, a recommendation module and VADER sentiment analysis into one pipeline (Sect. 3, p. 464)."
  model_development: "The training and preparation workflow of the LSTM and K-Means models is described, including sequence reshaping, gates, MSE loss, Adam optimizer and 1000 epochs (Sect. 3.1, p. 465)."
  system_development: "Django, MySQL, a Python backend, Pandas, MinMaxScaler/StandardScaler, Base64 password encoding and SMTP OTP 2FA are specified as the implementation stack (Sect. 3, p. 464)."
  model_performance_evaluation: "The LSTM's expense prediction is evaluated with accuracy 0.9993 (99.93%) and MSE 35.41 (Sect. 4, Fig. 5, p. 466)."
---

# A--Vinitha-2026

## Summary

An AI-driven personal finance management platform, built on the Django web framework with a MySQL relational database, that combines three machine-learning components behind an OTP-authenticated web interface. A Long Short-Term Memory (LSTM) deep-learning model is trained on historical daily expense data to forecast future expenses; K-Means clustering is applied to expense categories and amounts to segment spending behaviour; and VADER sentiment analysis classifies user feedback as positive, negative, or neutral. The system takes a user-uploaded financial dataset (`budget.csv`), extracts year, month and day date features, normalises numerical and categorical data with MinMaxScaler and StandardScaler, and then generates a recommended investment amount from the surplus between an assumed income and the predicted expenses. The paper reports a single evaluation of the LSTM — accuracy 0.9993 (99.93%) and Mean Squared Error 35.41 — and a single worked budget example in which an assumed income of 45,648 units, predicted expenses of 36,987 units and a recommended investment of 8,661 units are shown. No participant count, dataset size, train/test split, baseline comparison, confidence interval, or significance test is reported anywhere in the paper. The paper is a system-description and application paper rather than a controlled evaluation study; the authors state no formal design label. The one acknowledged source of limitations in the paper is a literature-survey discussion of AI adoption in finance generally — regulatory compliance, ethical concerns, workforce transformation, data privacy, algorithmic bias and skill gaps — rather than a reflection on the proposed system itself.

## Problem and Motivation

The paper opens with a broad framing of financial forecasting as a decision-support capability relevant to governance, wholesale and retail trade, production scheduling, sales planning and inventory control, where consumer preferences fluctuate and demand shows pronounced seasonality (Sect. 1, p. 460). It narrows to personal financial management with a two-part problem statement. First, users struggle to predict future expenses because spending habits carry non-linear trends, seasonal variations and irregular large payments that traditional methods fail to capture. Second, users need to understand how and why money is spent beyond simple category totals — identifying underlying spending patterns, detecting anomalies, and linking qualitative financial feelings to quantitative expense data (Sect. 1.1, p. 461). The motivation for the system is stated as the failure of existing tools: spreadsheets and basic budgeting tools can store transaction data but lack advanced analytical capabilities, so accurate prediction of future expenses is difficult and financial decisions are inefficient (Abstract, p. 460). Manual financial tracking is described as complex, time-consuming and prone to errors as digital transactions and expenditure categories multiply. The proposed response is an intelligent platform that provides automated financial insights, personalised recommendations and enhanced decision-making support by combining predictive modelling, clustering, sentiment evaluation and secure authentication in one system (Abstract, p. 460).

## Method

**Design.** System-development and application paper with a single offline model-evaluation component; the authors state no formal design label. The paper presents a proposed system architecture, then reports results through screenshots of the running system rather than through a controlled study.
**Sample.** Not reported (the paper states no N — no user count, no transaction count, no dataset size. The only sample-like object named is a user-uploaded file, `budget.csv`, and the unit of analysis is a daily expense record in that file).
**Context.** geography: India (author affiliation is the Department of Computer Science and Engineering, Kommuri Pratap Reddy Institute of Technology, Ghanpur, Ghatkesar, 501301, Telangana, India; no study locale is otherwise stated); population: individual personal-finance users who upload their own daily-expense dataset (no demographic is described); setting: a Django web application with a MySQL database and a Python-based backend, presented and illustrated through screenshots of the running system, with no field deployment, no participant study, no live user data and no organisational setting described.

The system is described as a structured three-layer architecture: a MySQL database for secure storage and user management, a Python-based backend for preprocessing and ML computations, and an interactive web interface (Sect. 3, p. 464). The implementation steps the paper states are:

- Users register and authenticate through a multi-level mechanism that combines Base64-based password encoding with OTP-based two-factor authentication delivered by SMTP, intended to safeguard user accounts and sensitive financial information (Sect. 3, p. 464).
- Once authenticated, a user uploads a financial dataset (`budget.csv`), which is processed with Pandas; date features — year, month and day — are extracted (Sect. 3, p. 464).
- Numerical and categorical data are normalised using MinMaxScaler and StandardScaler to prepare them for the ML models (Sect. 3, p. 464).
- K-Means clustering is applied to expense categories and amounts to group similar spending behaviours and let users visualise their financial habits (Sect. 3, p. 464).
- The LSTM model is trained on historical daily expense data to learn sequential patterns and generate future expense predictions, with performance evaluated using metrics such as score and MSE (Sect. 3, p. 464).
- Raw time features (year, month, day) and total expenses are scaled, and input features are reshaped into 3D sequences in `[samples, timesteps, features]` format required by the LSTM (Sect. 3.1, p. 465).
- Each input sequence passes through the gates sequentially: the Forget Gate multiplies the old cell state by a sigmoid output between 0 and 1 to decide what to discard; the Input Gate determines new information to add using sigmoid for filtering and tanh for candidate values; the Cell State is updated by forgetting old information and adding new information; the Output Gate determines the final hidden state from the new cell state (Sect. 3.1, p. 465).
- After the sequence is processed, the output from the final LSTM layer feeds into a dense layer that produces the single-day expense forecast (Sect. 3.1, p. 465).
- Backpropagation calculates prediction error using the Mean Squared Error loss function, and weights are adjusted with the Adam optimizer (Sect. 3.1, p. 465).
- Steps two through four are repeated over multiple epochs — 1000 in the code — to minimise loss and optimise model performance (Sect. 3.1, p. 465).
- Predicted values feed a recommendation module where a practical surplus is computed by comparing estimated expenses with a generated income approximation, allowing the system to suggest potential savings or investment opportunities (Sect. 3, p. 464).
- A qualitative feedback mechanism lets users submit feedback that VADER analyses as positive, negative or neutral; analysed sentiment results are stored in the database to support ongoing improvement and adaptive system behaviour (Sect. 3, p. 464).

The paper does not describe a train/test split, a validation procedure, a cross-validation scheme, a baseline model, a hyperparameter search, or a sampling strategy for either the LSTM or the K-Means model.

## Software

- Django web framework (version not reported)
- MySQL relational database (version not reported)
- Python-based backend (version not reported)
- Pandas (version not reported), used for date-feature extraction
- MinMaxScaler (version not reported), used for numerical normalisation
- StandardScaler (version not reported), used for categorical/numerical normalisation
- K-Means clustering (implementation and k not reported)
- LSTM (implementation and library not reported; trained for 1000 epochs; Adam optimizer; MSE loss)
- VADER — Valence Aware Dictionary and Sentiment Reasoner (version not reported)
- SMTP for email-based OTP delivery (version not reported)
- Base64 password encoding (implementation not reported)
- Base64-based password encoding and OTP 2FA are presented as the security mechanism (Sect. 3, p. 464)

## Key Findings

- The LSTM model's expense-prediction performance is reported as Accuracy 0.9993 (99.93%) and Mean Squared Error 35.41 (Sect. 4, Fig. 5, p. 466).
- The paper states that a graphical comparison between predicted expenses and actual test expenses "demonstrates how closely the predicted values follow the actual financial expense patterns" (Sect. 4, p. 466).
- In the worked budget-recommendation example, an assumed income of 45,648 units combined with predicted expenses of 36,987 units yields a recommended investment amount of 8,661 units (Sect. 4, Fig. 6, p. 466).
- K-Means clustering groups transaction records into clusters based on similarities in spending categories and expense amounts, and each cluster is described as representing a distinct pattern of financial activity (Sect. 4, p. 465).
- VADER sentiment analysis is demonstrated on one submitted feedback example and classifies it as Neutral (Sect. 4, Fig. 7, p. 467).
- The conclusion states that "Performance metrics such as MSE and R² score validate the accuracy and reliability of the predictions", but no R² value is printed anywhere in the paper (Sect. 5, p. 467).
- The paper reports no baseline comparison — no ARIMA, SARIMA, exponential smoothing or alternative clustering result is given, even though the literature survey cites a comparison of ARIMA, SARIMA and LSTM models (reference [5], Sect. 2, p. 463).

## Key Figures and Tables

- Fig. 1 (p. 460): Finance Management — a conceptual illustration of financial management as the framing for the paper; no data.
- Fig. 2 (p. 464): Proposed System architecture — the three-layer Django/MySQL/Python architecture; no quantitative content.
- Fig. 3 (p. 465): Internal Workflow of LSTM — the forget, input and output gates and the cell-state update; no quantitative content.
- Fig. 4 (p. 466): K-means clustering for personal finance — clusters of transaction records by spending category and amount; the figure is described but no cluster count, centroid value, inertia or silhouette statistic is printed.
- Fig. 5 (p. 466): LSTM Model Evaluation Screen — reports Accuracy 0.9993 (99.93%) and Mean Squared Error 35.41, and shows a graphical comparison of predicted expenses against actual test expenses.
- Fig. 6 (p. 466): Recommend budget Screen — the worked example: assumed income 45,648 units, predicted expenses 36,987 units, recommended investment 8,661 units.
- Fig. 7 (p. 467): Predicting Feedback Screen — a submitted feedback example classified by VADER as Neutral.

The paper contains no numbered tables. There is therefore no results table to represent, and the Statistical Evidence section below reports every quantity the paper does print.

## Limitations and Gaps

- The paper reports only one evaluation quantity for the LSTM model (accuracy 0.9993 / 99.93% and MSE 35.41) and no evaluation at all for the K-Means clustering or the VADER sentiment component beyond a single illustrated example (Fig. 4, Fig. 5, Fig. 7, pp. 466-467).
- [unacknowledged] No sample size, user count, transaction count, date range or currency is stated for the dataset (`budget.csv`) on which the models were trained, so the reported accuracy and MSE cannot be contextualised or reproduced.
- [unacknowledged] No train/test split, validation procedure, hold-out protocol or cross-validation scheme is described; the accuracy of 0.9993 and MSE of 35.41 are reported without any statement of how the evaluation set was constructed.
- [unacknowledged] The accuracy metric is not defined: the paper does not say whether 0.9993 is classification accuracy, regression score, or some other quantity, and it reports this accuracy alongside a non-trivial MSE of 35.41 without reconciling the two.
- [unacknowledged] The conclusion names an R² score as validating the predictions, but no R² value appears anywhere in the paper (Sect. 5, p. 467).
- [unacknowledged] No baseline model is compared. Reference [5] in the literature survey reports a comparison of ARIMA, SARIMA and LSTM for time-series forecasting, but the paper's own evaluation does not benchmark its LSTM against any of these.
- [unacknowledged] The 45,648 / 36,987 / 8,661 budget example is a single worked example presented in a screenshot; the unit is never defined (currency is not stated), the income is "assumed" rather than measured, and no population-level distribution of recommended investment amounts is reported.
- [unacknowledged] The K-Means clustering output is described only in prose and shown as a figure; no number of clusters, centroid values, within-cluster variance, or cluster-selection method is reported.
- [unacknowledged] VADER sentiment analysis is demonstrated on a single feedback item classified as Neutral; no accuracy, agreement or validation of the sentiment classifier is reported.
- [unacknowledged] The paper reports no software-quality evaluation — no System Usability Scale, no ISO/IEC 25010 assessment, no user study, no task-completion data, and no deployed-system evaluation of whether users follow the recommended plans.
- [unacknowledged] Base64 encoding is described as part of the security mechanism for passwords (Sect. 3, p. 464); Base64 is an encoding scheme rather than a hashing or encryption scheme, so the protection it provides is not established in the paper.
- [unacknowledged] The abstract's framing of "behavioural clustering" is not operationalised as a distinct algorithm; the clustering component is K-Means on expense categories and amounts, and no behavioural theory or behavioural variable is defined.
- The literature survey cites acknowledged challenges of AI adoption in finance generally — regulatory compliance, ethical concerns, workforce transformation, data privacy, algorithmic bias, implementation costs and skill gaps (Sect. 2, pp. 462-463) — but the paper does not apply any of these to its own system, and it acknowledges no limitation of its own design, data or evaluation in the conclusion.

## Definitions

- **LSTM (Long Short-Term Memory)** — A specialised Recurrent Neural Network designed to overcome the vanishing-gradient problem and learn long-term dependencies in time-series forecasting; its memory cell is regulated by a Forget Gate, an Input Gate and an Output Gate (Sect. 3.1, p. 464).
- **Forget Gate** — Multiplies the old cell state by a sigmoid output between 0 and 1 to decide what information to discard (Sect. 3.1, p. 465).
- **Input Gate** — Determines new information to add to the cell state, using sigmoid for filtering and tanh for creating candidate values (Sect. 3.1, p. 465).
- **Output Gate** — Determines the final hidden-state output based on the new cell state (Sect. 3.1, p. 465).
- **K-Means clustering** — An algorithm applied to expense categories and amounts to group similar spending behaviours into clusters (Sect. 3, p. 464).
- **VADER (Valence Aware Dictionary and Sentiment Reasoner)** — A sentiment-analysis tool used to classify user feedback as positive, negative or neutral (Abstract, p. 460).
- **OTP (One-Time Password)** — A one-time code delivered by email through SMTP as a second authentication factor (Abstract, p. 460; Sect. 3, p. 464).
- **SMTP (Simple Mail Transfer Protocol)** — The protocol used to send the OTP email (Abstract, p. 460).
- **MinMaxScaler / StandardScaler** — The two normalisation tools used to prepare numerical and categorical data for the ML models (Sect. 3, p. 464).
- **MSE (Mean Squared Error)** — The loss function used to calculate prediction error during LSTM backpropagation; also reported as an evaluation metric with value 35.41 (Sect. 3.1, p. 465; Sect. 4, Fig. 5, p. 466).
- **R² score** — Named in the conclusion as a validation metric for the predictions, but no value is printed (Sect. 5, p. 467).
- **budget.csv** — The financial dataset a user uploads for processing by the system (Sect. 3, p. 464).
- **2FA (Two-Factor Authentication)** — The multi-level authentication mechanism combining password encoding with an OTP (Sect. 3, p. 464).
- **Practical surplus** — The quantity computed by comparing estimated expenses against a generated income approximation, used to suggest savings or investment (Sect. 3, p. 464).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LSTM expense prediction accuracy, fraction form as printed | accuracy | 0.9993 | — | — | Sect. 4, Fig. 5, p. 466 |
| LSTM expense prediction accuracy, percent form as printed | accuracy | 99.93% | — | — | Sect. 4, Fig. 5, p. 466 |
| LSTM expense prediction error | Mean Squared Error | 35.41 | — | — | Sect. 4, Fig. 5, p. 466 |
| Budget recommendation, assumed income in worked example | income | 45,648 units | — | — | Sect. 4, Fig. 6, p. 466 |
| Budget recommendation, predicted expenses in worked example | predicted expenses | 36,987 units | — | — | Sect. 4, Fig. 6, p. 466 |
| Budget recommendation, recommended investment amount in worked example | recommended investment amount | 8,661 units | — | — | Sect. 4, Fig. 6, p. 466 |
| LSTM training configuration | epochs | 1000 | — | — | Sect. 3.1, p. 465 |
| Feedback sentiment classification, displayed example | sentiment class | Neutral | — | — | Sect. 4, Fig. 7, p. 467 |
| AI-in-finance publication trend reported from cited work [14] | annual growth rate | 13.34% | — | — | Sect. 2 Literature Survey, p. 463 |

The paper reports these quantities and no others. There is no baseline comparison, no per-cluster statistic, no confidence interval, no p-value, no variance measure and no effect size anywhere in the paper. The results section is composed of four figures (Fig. 4 through Fig. 7), of which only Fig. 5 and Fig. 6 contain numbers. This is a genuine sparse-reporting case rather than an extraction that stopped early: the paper's evaluation content is fully captured above.

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "A Long Short-Term Memory (LSTM) deep learning model is utilized to analyze historical financial data and predict future expenses by capturing temporal patterns and trends." | Abstract, p. 460 | model_development |
| "Additionally, K-Means clustering is applied to group expenses into different categories, enabling users to better understand their spending behavior and identify financial patterns." | Abstract, p. 460 | income_expense_management |
| "The system further integrates sentiment analysis using VADER (Valence Aware Dictionary and Sentiment Reasoner) to evaluate user feedback and classify it as positive, negative, or neutral, supporting continuous system improvement." | Abstract, p. 460 | pfm_apps_features |
| "The model performance is measured using evaluation metrics including Accuracy of 0.9993 (99.93%) and Mean Squared Error of 35.41." | Sect. 4, p. 466 | model_performance_evaluation |
| "For example, if the system assumes an income of 45,648 units and predicted expenses of 36,987 units, the recommended investment amount is calculated as 8,661 units." | Sect. 4, Fig. 6, p. 466 | financial_planning |
| "In the displayed example, the system identifies the feedback sentiment as Neutral." | Sect. 4, Fig. 7, p. 467 | pfm_apps_features |
| "The central challenge in personal financial management is transforming voluminous, raw transaction data into accurate, actionable, and personalized insights regarding future financial status." | Sect. 1.1, p. 461 | financial_planning |
| "Traditional financial management systems, such as spreadsheets and basic budgeting tools, allow users to store transaction data but lack advanced analytical capabilities, making accurate prediction of future expenses difficult and leading to inefficient financial decisions." | Abstract, p. 460 | pfm_apps_problems |
| "This gating mechanism allows the LSTM to remember patterns that occurred months ago (like annual fees or seasonal spending) and integrate them effectively into the current day's expense prediction" | Sect. 3.1, p. 465 | model_development |
| "Performance metrics such as MSE and R² score validate the accuracy and reliability of the predictions." | Sect. 5 Conclusion, p. 467 | model_performance_evaluation |
| "The system is developed using the Django web framework and extends beyond conventional financial tracking by integrating predictive modeling and behavioral analysis to enhance financial awareness and decision-making." | Sect. 3, p. 463 | system_development |
| "The system follows a structured three-layer architecture consisting of a MySQL database for secure storage and user management, a Python-based backend responsible for preprocessing and ML computations, and an interactive web interface that facilitates seamless user interaction." | Sect. 3, p. 464 | system_development |

## Remember This

- The paper presents a Django + MySQL personal finance application built around three ML components: LSTM expense forecasting, K-Means spending-behaviour clustering and VADER feedback sentiment.
- The only reported model result is LSTM accuracy 0.9993 (99.93%) and MSE 35.41, with no sample size, no train/test split, no validation procedure and no baseline.
- The only reported budget example is a worked example — assumed income 45,648 units, predicted expenses 36,987 units, recommended investment 8,661 units — and the unit is never defined.
- K-Means and VADER are demonstrated only through single illustrative figures, not evaluated quantitatively.
- The conclusion names an R² score as validating the predictions but no R² value is printed.
- The paper is an Indian institutional system-development paper with no field deployment, no participants and no user study.

## Cited Works

- Ramezanian, M.; Haghdoost, A.A.; Mehrolhassani, M.H.; Abolhallaje, M.; Dehnavieh, R.; Najafi, B.; Fazaeli, A.A. (2019) (context) — ARIMA model used to forecast health expenditures in Iran (2016-2020). [p. 467]
- Rubio, L.; Gutiérrez-Rodríguez, A.J.; Forero, M.G. (2021) (context) — EBITDA index prediction using exponential smoothing and ARIMA. [p. 467]
- Zhang, P.; Joshi, M.; Lingras, P. (2011) (context) — Stability and seasonality analysis for optimal inventory prediction models. [p. 467]
- Amirkhanov, I.V.; Puzynina, T.P.; Puzynin, I.V.; Sarhadov, I.; Pavlušová, E.; Pavluš, M. (2011) (context) — Numerical simulation of heat and moisture transfer subject to phase transition. [pp. 467-468]
- Sirisha, U.M.; Belavagi, M.C.; Attigeri, G. (2022) (methodology) — Profit prediction comparing ARIMA, SARIMA and LSTM models in time-series forecasting. [p. 468]
- Shiyyab, F.S.; Alzoubi, A.B.; Obidat, Q.M.; Alshurafat, H. (2023) (context) — AI disclosure index and its relationship with financial performance. [p. 461]
- Yaseen, H.; Al-Amarneh, A. (2025) (context) — Trust, transparency and fairness in AI-driven fraud detection adoption in banking in the UAE and Qatar. [p. 461]
- El Hajj, M.; Hammoud, J. (2023) (context) — AI and ML influence on financial markets across trading, risk management and operations. [p. 461]
- Aleksandrova, A.; Ninova, V.; Zhelev, Z. (2023) (context) — Survey of AI implementation in finance, cyber insurance and financial controlling. [p. 462]
- Yang, Q.; Lee, Y.-C. (2024) (context) — GenAI adoption in financial advisory services through service-dominant logic and AIDUA. [p. 462]
- Shaban, O.S.; Omoush, A. (2025) (context) — AI-driven financial transparency and corporate governance with evidence from Jordan. [p. 462]
- Artene, A.E.; Domil, A.E.; Ivascu, L. (2024) (context) — Integrating AI-driven financial reporting systems into business decision-making. [p. 462]
- Mhlanga, D. (2020) (context) — Impact of AI on digital financial inclusion. [p. 462]
- Bayakhmetova, A.; Rudenko, L.; Krylova, L.; Suleimenova, B.; Niyazbekova, S.; Nurpeisova, A. (year not reported) (context) — Bibliometric analysis of AI in financial behaviour; reports a 13.34% annual growth rate in publications. [p. 463]
- Liu, L.X.; Sun, Z.; Xu, K.; Chen, C. (2024) (context) — ChatGPT-4o financial reasoning capabilities and challenges. [p. 463]