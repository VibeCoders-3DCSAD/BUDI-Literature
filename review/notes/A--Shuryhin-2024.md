---
paper_id: A--Shuryhin-2024
first_author: Shuryhin
year: 2024
title: "Recommendation system for financial decision-making using Artificial intelligence"
venue: "Applied Aspects of Information Technology"
doi: 10.15276/aait.07.2024.24
designation: algorithm
status: extracted
modules: [budgeting, financial_planning, income_expense_management, model_algorithm_integration, model_development, pfm_apps_features, system_development]
module_rationale:
  budgeting: "ARIMA and LSTM models are combined to forecast user budget expenses (Sect. 2.2, p. 4)."
  financial_planning: "The system is framed as supporting financial planning, budgeting, and investing by helping users make rational financial choices (Introduction, p. 1)."
  income_expense_management: "Isolation Forest is applied to detect anomalous user expenses and identify spontaneous or impulsive financial decisions (Sect. 2.1, p. 3)."
  model_algorithm_integration: "The system integrates Isolation Forest, ARIMA, LSTM and an LLM into a single recommendation pipeline (Sect. 2.3, Fig. 3, p. 6)."
  model_development: "The paper details training and preparation workflows for ARIMA, LSTM and Isolation Forest (Sect. 2.1–2.2, pp. 3–4)."
  pfm_apps_features: "The system provides budget forecasting, anomaly detection, personalized financial advice, and alternative spending recommendations (Sect. 4, p. 7)."
  system_development: "The implementation stack includes Python AI modules, Java/Spring budget modules, Spring Cloud Gateway, OAuth 2.0, AWS Glue/SQS/SageMaker, Terraform, and React.js (Sect. 4, pp. 7–9)."
---

## Summary

The paper describes a recommendation system for personal financial decision-making that combines three AI components: Isolation Forest for detecting anomalous expenses, a hybrid ARIMA + LSTM model for budget forecasting, and a large language model (LLaMa 3.1) for generating personalized financial advice. The authors argue that cognitive biases — such as loss aversion and framing effects — lead consumers to irrational spending, and that an AI system can help users make more rational financial choices without manipulating or imposing decisions. The system is built as an event-driven microservices architecture on AWS, with a Python AI module, a Java/Spring budget module, an API Gateway, OAuth 2.0 authentication, and a React.js client. The paper describes the architecture, the mathematical foundations of each model, the integration pipeline, the database entity-relationship model, and the ethical principles that govern the system. No empirical evaluation, user study, or quantitative performance results are reported.

## Problem and Motivation

The modern financial landscape faces ineffective financial management and financial illiteracy among both individual consumers and organizations. Many individuals lack sufficient knowledge to make sound financial decisions, making them vulnerable to aggressive marketing strategies, especially in the context of increasingly sophisticated AI-enhanced marketing techniques that can manipulate consumer behavior and promote irrational expenditures (Introduction, p. 1).

Research in behavioral economics shows that cognitive biases, such as loss aversion or framing effects, significantly impact consumer decision-making, often leading to deviations from rational behavior. This highlights the need for intelligent systems that can help consumers overcome these financial biases and make more informed decisions (Introduction, p. 1).

AI is already demonstrating considerable potential in the financial sector, particularly through its ability to analyze large volumes of data and uncover hidden patterns. Systems that combine cognitive psychology with machine learning algorithms can personalize user experiences and offer recommendations based on an analysis of their behavior and preferences. This enables AI not only to predict consumer behavior but also to provide more accurate recommendations for financial planning, budgeting, and investing (Introduction, p. 1).

The goal of the study is to develop principles for creating financial recommendations using AI models, regardless of user's income levels (Introduction, p. 1).

## Method

**Design.** System architecture and method-development study; the authors state no formal design label.
**Sample.** Not applicable — no dataset, participants, or evaluation sample is reported; the paper describes system architecture and algorithm design without empirical testing.
**Context.** geography: Not reported (no deployment location stated; authors affiliated with Odesa Polytechnic National University, Ukraine); population: Not applicable (no user population studied or described beyond generic "users" and "consumers"); setting: Virtual/computational — a microservices architecture on AWS with Python AI modules, Java/Spring budget modules, and a React.js client, described but not deployed or evaluated in a live setting.

The paper proceeds in four sections. Section 1 reviews the literature on recommendation systems (RS) generally and financial RS specifically, covering their roles, psychological mechanisms, ethical implications, and the state of the field. Section 2 describes the three AI components used to form financial recommendations. Section 3 discusses the ethical principles the system must satisfy. Section 4 describes the implemented architecture, database model, and software stack.

**Isolation Forest for anomaly detection.** The concept of Isolation Forest was used as the basis for detecting anomalous user expenses, with its core idea being the isolation of anomalies from normal data (Sect. 2.1, p. 3). A binary tree is initially created by randomly selecting features and distributing values. The next step is to determine the anomaly score by calculating the path length from the root of the tree to the terminal node. The shortest paths are considered anomalies. The mathematical basis for calculating the expected path length is given by:

E(h(x)) = c(n) + 2loglog(n−1) − 2(n−1)/n,

where c(n) is the average path length for unsuccessful searches in a binary tree; h(x) is the path length for point x in the isolation tree (the number of edges traversed from the root to the terminal node). The average path length is:

c(n) = 2H(n−1) − (2(n−1)/n),

where H(i) is the harmonic number, calculated as:

H(i) = Σ_{k=1}^{i} 1/k.

The anomaly score for a point is calculated based on the average path length across all trees:

s(x,n) = 2^(−E(h(x))/c(n)),

where s(x,n) ≈ 1 if the point is an anomaly; s(x,n) ≈ 0.5 if the point is normal (Sect. 2.1, p. 3).

**ARIMA model.** To predict user budget expenses, a combination of two models was used: ARIMA (Auto Regressive Integrated Moving Average) and LSTM (Long Short-Term Memory). Both models are designed to work with time series data but have different approaches to solving the problem. ARIMA was used for short-term forecasts, and LSTM for long-term forecasts, allowing for more accurate and stable predictions. The first stage of prediction is data preparation, including data cleaning, handling missing values, and standardizing the data format. The main focus is on removing trends and seasonality from the data series, as these factors can affect the accuracy of the forecast (Sect. 2.2, p. 4).

The ARIMA model consists of three components: AR (AutoRegressive), which models the dependency between an observation and several previous observations; I (Integrated), used to eliminate non-stationarity; and MA (Moving Average), which models the dependency between an observation and the forecast error. Mathematically the ARIMA(p, d, q) is described by:

y_t = c + φ_1 y_{t−1} + φ_2 y_{t−2} + ... + φ_p y_{t−p} + θ_1 ε_{t−1} + θ_2 ε_{t−2} + ... + θ_q ε_{t−q} + ε_t,

where y_t is the value of the series at time t, φ_i are the coefficients of the AR component; θ_j are the coefficients of the MA component; ε_t is the random error term; c is a constant.

The process of building an ARIMA model includes determining the orders p, d, q. The parameter p represents the order of the autoregressive component, i.e., the number of previous values used for forecasting. The parameter d denotes the degree of differencing. The parameter q indicates the order of the moving average component. After determining these parameters, usually selected using the Akaike Information Criterion (AIC) or Bayesian Information Criterion (BIC), the model is trained on the training data and used for short-term forecasting (Sect. 2.2.1, p. 4).

**LSTM model.** For long-term forecasts, the LSTM model is used, which is a type of recurrent neural network (RNN). The LSTM model can capture long-term dependencies in time series data due to its specific architecture, which includes memory cells and mechanisms for forgetting and retaining information. Mathematically, the behavior of a single LSTM block is described by:

f_t = σ(W_f · [h_{t−1}, x_t] + b_f)
i_t = σ(W_i · [h_{t−1}, x_t] + b_i)
C~_t = tanh(W_C · [h_{t−1}, x_t] + b_C)
C_t = f_t * C_{t−1} + i_t * C~_t
o_t = σ(W_o · [h_{t−1}, x_t] + b_o)
h_t = o_t * tanh(C_t)

where f_t is the forget vector, i_t is the input vector, C~_t is the new candidate for the cell state value, C_t is the updated cell state, o_t is the output vector, h_t is the vector of output values from the LSTM block, W_f, W_i, W_C, W_o are weight matrices, and b_f, b_i, b_C, b_o are bias vectors. The LSTM network is trained on historical spending data to create long-term forecasts, taking into account long-term dependencies between observations (Sect. 2.2.2, p. 4).

**Combination of forecasts.** The final step is the combination of forecasts obtained from the ARIMA and LSTM models. A weighted average method is used, where the results of both models are combined to obtain the final expense forecast:

ŷ_t = α · ŷ_t^ARIMA + (1 − α) · ŷ_t^LSTM,

where α is the weight coefficient that determines the influence of each model on the final result. The combination of ARIMA and LSTM allows for consideration of both short-term and long-term trends, enhancing the accuracy of user expense forecasts (Sect. 2.2.3, p. 4).

**LLM for generating financial recommendations.** A large language model (LLM), such as LLaMa 3.1, can be effectively used to generate personalized financial recommendations based on the analysis of previous financial data, spending anomalies, and budget forecasts. To generate personalized recommendations, it is important to ensure high-quality input data. This data includes: historical transaction data of the user; data on detected spending anomalies; budget expenditure forecasts based on ARIMA and LSTM models; and additional parameters, such as the user's financial goals, risk tolerance, and typical spending patterns. The data is transferred to the LLM after preprocessing, which includes normalization, categorization, and extraction of the key features (Sect. 2.3.1, p. 4).

After configuring the LLM, the model can use the available data to create personalized recommendations. The recommendation generation process proceeds as follows: (1) Processing input data — the LLM receives input data, including transaction history, projected expenses, and anomaly information. (2) Context formation — the model defines the context based on the user's current financial status, forecasts, and identified anomalies. (3) Generating recommendations — based on the context, the model generates several options for financial advice, taking into account both the user's short-term and long-term goals. (4) Evaluation of recommendations — each recommendation is evaluated in terms of its alignment with the user's individual characteristics, such as risk level, financial goals, and preferences (Sect. 2.3.2, p. 4).

The generated recommendations are delivered to the user through the system interface as structured suggestions, including explanations and an assessment of the potential consequences of each decision. The user can select one of the suggestions or request additional recommendation if the initial set does not meet their needs. The recommendations are adapted to the user's financial capacity, providing valuable advice for individuals with various income levels, from low to high. Since the analysis, forecasting and advice generation occur within the context of the user's specific financial operations, the system will be beneficial regardless of the user's income level (Sect. 2.3.2, p. 4).

Fig. 1 illustrates an example of a request to the LLM to obtain a personalized financial recommendation. Fig. 2 shows an example of the model's response based on the provided context. Figure 3 demonstrates the interaction of AI components within the financial system. In the initial stage, the system receives input data on the user's financial transactions, which then pass through the data preprocessing module. This module is responsible for data cleaning, normalization, and preparation for further analysis by the models (Sect. 2.3.2, pp. 4–5).

**Ethical principles.** Ethics is an important aspect in designing recommendation systems for supporting financial decisions, as it affects how much users trust the system and how willing they are to accept recommendations as objective and unbiased (Sect. 3, p. 5). In [25], an analysis of ethical issues created by recommendation systems is conducted. The study describes how ethical consequences can arise in a recommendation system: its operations can (negatively) impact the utility for each of its stakeholders and/or violate their rights. Ethical impacts can be immediate (e.g., an inaccurate recommendation leading to reduced utility for the user) or expose relevant parties to future risks (such as the influence of potentially irrelevant or harmful content). The authors of [26] analyze recommendation system technology from the perspective of methods used to address issues in the following areas: privacy, personal data, fairness, transparency, personal identity, and the proper functioning of society (Sect. 3, p. 5).

An AI-powered system must ensure a balance between its ability influence the user and the user's autonomy, promoting more rational financial behavior. One of the ethical advantages of such a system is its ability to help users become aware of their financial habits without judgement, offering the opportunity for an objective analysis of spending and savings, regardless of income level (Sect. 3, p. 5).

An AI-based recommendation system can promote responsible financial behavior by enhancing the user's financial awareness and helping them avoid potentially irrational expenditures. In an aggressive marketing environment, where users are constantly exposed to advertising, an ethically built recommendation system allows users to maintain control over their financial decisions. AI algorithms analyze data to ensure the accuracy and usefulness of recommendations, avoiding manipulation and supporting user's long-term financial goals. This helps users navigate a complex informational landscape where marketing influences often lead to impulsive purchases and irrational spending (Sect. 3, p. 5).

The ethical nature of the system is reinforced by its focus on the user's interests. Instead of evaluating or judging financial behavior, the system provides structured, well-founded advice that helps users better understand their spending patterns, identify potential saving opportunities, and optimize their budget. Importantly, the recommendations are tailored to the user's individual goals and preferences, preserving their independence and autonomy in making financial decisions. The system does not impose specific actions but instead offers a variety of options from which the user can choose that best meet their needs and goals (Sect. 3, p. 7).

**System architecture.** The architecture of the system is built on an event-driven approach with a high-level of module independence. The overall operations principle of the system, which supports core financial operations, integration with banking systems, as well as data cleaning and preparation processes for further AI module analysis, is that each module operates autonomously. For example, the Budget Module remains operations even if the AI module is temporarily unavailable, and vice versa. The AI module is responsible for key functions such as detecting anomalous expenses, forecasting future expenses during budgeting, generating personalized financial advice, and recommending alternative spending options. The Build-Train-Deploy pattern is used to integrate the AI model into the microservices architecture, supported by AWS SageMaker, which automates model training, testing, and deployment [27] (Sect. 4, p. 7).

A database has been developed to store data that provides input information for the recommendation system, with its Entity-Relationship Diagram (ERD) model shown in Fig. 4, illustrating the main entities of the financial platform and the relationships between them. The diagram covers various aspects of the system's operation, including user management, transactions, budgets, financial goals, subscriptions, and categories. Fig. 5 and Fig. 6 provide examples of the screen forms of the developed system (Sect. 4, p. 7).

## Software

- Python (version not reported) — AI Module, using scikit-learn, TensorFlow, and statsmodels
- scikit-learn (version not reported)
- TensorFlow (version not reported)
- statsmodels (version not reported)
- Java with Spring Framework (version not reported) — Budget Module
- Spring Cloud Gateway (version not reported) — API Gateway
- Spring Security with OAuth 2.0 (version not reported) — Authentication Module
- AWS SageMaker (version not reported) — Build-Train-Deploy automation
- AWS Glue (version not reported) — ETL operations, Glue Crawler for schema determination
- AWS SQS (version not reported) — message queuing between microservices
- AWS S3 (version not reported) — data storage
- Terraform (version not reported) — infrastructure automation
- React.js (version not reported) — client side
- LLaMa 3.1 (version not reported) — large language model for recommendation generation
- Isolation Forest (implementation not reported) — anomaly detection
- ARIMA (implementation not reported) — short-term forecasting
- LSTM (implementation not reported) — long-term forecasting

## Key Findings

- The system combines Isolation Forest for anomaly detection, ARIMA + LSTM for budget forecasting, and an LLM (LLaMa 3.1) for generating personalized financial recommendations (Abstract, p. 1; Sect. 2.3, p. 4).
- ARIMA was used for short-term forecasts, and LSTM for long-term forecasts, allowing for more accurate and stable predictions (Sect. 2.2, p. 4).
- The final expense forecast is a weighted average of the ARIMA and LSTM forecasts, with weight coefficient α determining the influence of each model (Sect. 2.2.3, p. 4).
- The LLM receives transaction history, projected expenses, anomaly information, and additional parameters (financial goals, risk tolerance, spending patterns), and generates recommendations in a four-stage process: processing input data, context formation, generating recommendations, and evaluation of recommendations (Sect. 2.3.2, p. 4).
- The generated recommendations are adapted to the user's financial capacity and are claimed to be beneficial regardless of the user's income level (Sect. 2.3.2, p. 4).
- The ethical framework rests on confidentiality, fairness, transparency, and user autonomy; the system does not impose specific actions but offers a variety of options (Sect. 3, p. 7).
- The architecture is event-driven with module independence; the Budget Module continues to operate if the AI Module is unavailable, and vice versa (Sect. 4, p. 7).
- The system is claimed to ensure high accuracy through the combination of various AI models, completeness by training on user's transactions, and privacy and security by adhering to OAuth 2 standards and OWASP Top 10 principles (Conclusions, p. 9).
- No empirical evaluation, user study, or quantitative performance measurement of any component is reported anywhere in the paper.

## Key Figures and Tables

- Fig. 1 (p. 6): Diagram of the request implementation to the LLM for obtaining a personalized financial recommendation → shows the request structure sent to the LLM; no numerical data.
- Fig. 2 (p. 6): Example of the model's response based on the provided context → shows a sample LLM response; no numerical data.
- Fig. 3 (p. 7): Diagram of the interaction of AI components within the system → shows input data passing through preprocessing, then through the AI models; no numerical data.
- Fig. 4 (p. 8): ERD for the recommendation system → shows entities for user management, transactions, budgets, financial goals, subscriptions, and categories; no numerical data.
- Fig. 5 (p. 8): Main page → screen capture of the developed system; no numerical data.
- Fig. 6 (p. 8): Use of AI models for anomaly detection → screen capture of the anomaly detection interface; no numerical data.
- No numbered tables appear in the paper.

## Limitations and Gaps

- The paper reports no empirical evaluation of the system or its components: no accuracy, precision, recall, RMSE, MAE, F1, or user study results appear anywhere in the text, figures, or conclusions. [unacknowledged]
- No dataset is described — the paper does not state what transaction data was used, how much data, from how many users, or from what source. [unacknowledged]
- The claim that "the system ensures high accuracy" (Conclusions, p. 9) is unsupported by any reported accuracy measurement. [unacknowledged]
- The LLM component (LLaMa 3.1) is described but not tested; no examples of generated recommendations are analysed or evaluated. [unacknowledged]
- The choice of α (the ARIMA/LSTM weight coefficient) is not specified, and no method for selecting or validating it is given. [unacknowledged]
- The paper does not report how anomaly thresholds are set for Isolation Forest's s(x,n) score. [unacknowledged]
- No comparison to baseline or existing financial recommendation systems is performed. [unacknowledged]
- The ethical principles (confidentiality, fairness, transparency, user autonomy) are stated but not operationalised or tested. [unacknowledged]
- The authors acknowledge that prior work [11] found a limit of development for financial recommendation systems and that further expenditure on promotion can only be justified by economic impact — but they do not report any economic impact assessment of their own system. [acknowledged]
- The system's architecture is described but no deployment or field test is reported. [unacknowledged]
- The paper cites [13] as concluding that a salary-management recommendation system is useful only when a person has high income, but the authors do not reconcile this with their own claim that the system benefits all income levels. [unacknowledged]

## Definitions

- **Isolation Forest** — An anomaly detection model that isolates anomalies by randomly selecting features and splitting values; anomalies have shorter path lengths in the resulting binary trees (Sect. 2.1, p. 3).
- **ARIMA** — Auto Regressive Integrated Moving Average, a time-series forecasting model with autoregressive, differencing, and moving-average components (Sect. 2.2.1, p. 4).
- **LSTM** — Long Short-Term Memory, a type of recurrent neural network with memory cells and forget/input gates capable of capturing long-term dependencies (Sect. 2.2.2, p. 4).
- **LLM** — Large language model; the paper uses LLaMa 3.1 as an example (Sect. 2.3, p. 4).
- **RS** — Recommendation system (Sect. 1, p. 2).
- **Anomaly score (s(x,n))** — A score between 0 and 1 where values close to 1 indicate an anomaly and values close to 0.5 indicate a normal point (Sect. 2.1, p. 3).
- **ERD** — Entity-Relationship Diagram, used to model the database entities and their relationships (Sect. 4, p. 7).
- **OAuth 2.0** — An authorization framework used for controlling access to protected resources via tokens (Sect. 4, p. 8).
- **Build-Train-Deploy pattern** — A pattern used to integrate the AI model into the microservices architecture, supported by AWS SageMaker (Sect. 4, p. 7).
- **OWASP Top 10** — A list of the most critical web application security risks, referenced as a security principle (Conclusions, p. 9).

## Key Equations

- `E(h(x)) = c(n) + 2loglog(n−1) − 2(n−1)/n` — Expected path length in an isolation tree.
- `c(n) = 2H(n−1) − (2(n−1)/n)` — Average path length for unsuccessful searches in a binary tree.
- `H(i) = Σ_{k=1}^{i} 1/k` — Harmonic number.
- `s(x,n) = 2^(−E(h(x))/c(n))` — Anomaly score; ≈1 for an anomaly, ≈0.5 for a normal point.
- `y_t = c + φ_1 y_{t−1} + φ_2 y_{t−2} + ... + φ_p y_{t−p} + θ_1 ε_{t−1} + θ_2 ε_{t−2} + ... + θ_q ε_{t−q} + ε_t` — ARIMA(p, d, q) model.
- `f_t = σ(W_f · [h_{t−1}, x_t] + b_f)` — LSTM forget gate.
- `i_t = σ(W_i · [h_{t−1}, x_t] + b_i)` — LSTM input gate.
- `C~_t = tanh(W_C · [h_{t−1}, x_t] + b_C)` — LSTM new candidate cell state.
- `C_t = f_t * C_{t−1} + i_t * C~_t` — LSTM updated cell state.
- `o_t = σ(W_o · [h_{t−1}, x_t] + b_o)` — LSTM output gate.
- `h_t = o_t * tanh(C_t)` — LSTM output vector.
- `ŷ_t = α · ŷ_t^ARIMA + (1 − α) · ŷ_t^LSTM` — Combined ARIMA + LSTM forecast.

## Statistical Evidence

Not reported. The paper contains no results tables, no performance metrics, no accuracy values, no error measures, and no quantitative evaluation of the ARIMA, LSTM, Isolation Forest, or LLM components; the six figures are architecture diagrams and screen captures, not results. The only numerical quantities in the paper are the mathematical definitions in Sect. 2.1–2.2 and the statement that e-commerce accounts for "17% of all reviewed studies" in the literature review (Sect. 1, p. 2), which is a summary of cited work [3, 4] rather than an outcome of this study.

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The rapid expansion of artificial intelligence (AI) in consumer markets presents challenges, particularly in how cognitive biases influence financial decision-making." | Abstract, p. 1 | financial_planning |
| "Techniques include using Isolation Forest for identifying atypical financial actions and a combination of ARIMA and LSTM models for budget forecasting." | Abstract, p. 1 | model_algorithm_integration |
| "The research also considers integrating these models with large language models (LLMs) to generate personalized recommendations." | Abstract, p. 1 | model_algorithm_integration |
| "Special attention is paid to the ethical aspects of the system, which include ensuring confidentiality, fairness and transparency, as well as the importance of supporting user autonomy in making financial decisions." | Abstract, p. 1 | pfm_apps_features |
| "The goal of this study is to develop principles for creating financial recommendations using AI models, regardless of user's income levels." | Introduction, p. 1 | financial_planning |
| "The concept of Isolation Forest was used as the basis for detecting anomalous user expenses, with its core idea being the isolation of anomalies from normal data." | Sect. 2.1, p. 3 | income_expense_management |
| "To predict user budget expenses, a combination of two models was used: ARIMA (Auto Regressive Integrated Moving Average) and LSTM (Long Short-Term Memory)." | Sect. 2.2, p. 4 | budgeting |
| "A large language model (LLM), such as LLaMa 3.1, can be effectively used to generate personalized financial recommendations based on the analysis of previous financial data, spending anomalies, and budget forecasts." | Sect. 2.3, p. 4 | model_algorithm_integration |
| "An AI-powered system must ensure a balance between its ability influence the user and the user's autonomy, promoting more rational financial behavior." | Sect. 3, p. 5 | financial_planning |
| "The system does not impose specific actions but instead offers a variety of options from which the user can choose that best meet their needs and goals." | Sect. 3, p. 7 | pfm_apps_features |
| "The architecture of the system is built on an event-driven approach with a high-level of module independence." | Sect. 4, p. 7 | system_development |
| "The AI Module is implemented in Python using libraries like scikit-learn, TensorFlow, and statsmodels." | Sect. 4, p. 7 | system_development |
| "The system ensures high accuracy through the combination of various AI models (ARIMA and LSTM for forecasting, Isolation Forest for anomaly detection, and LLM for generating advice)" | Conclusions, p. 9 | model_algorithm_integration |
| "Consumers often prefer human interaction in fields characterized by high consumer involvement, such as healthcare and financial services, over computer-generated advice." | Sect. 1, p. 3 | pfm_apps_problems |
| "Privacy and security are important issue for recommendation systems." | Sect. 1, p. 3 | pfm_apps_features |
| "The system promotes responsible financial behavior by helping to avoid impulsive spending and increasing financial awareness without manipulation or imposing specific decisions." | Abstract, p. 1 | financial_planning |

## Remember This

- The paper describes a financial recommendation system combining Isolation Forest (anomaly detection), ARIMA + LSTM (budget forecasting), and LLaMa 3.1 (advice generation) into a single pipeline.
- ARIMA is used for short-term forecasts and LSTM for long-term forecasts, combined via a weighted average with weight α.
- The system is an event-driven microservices architecture on AWS with a Python AI module, Java/Spring budget module, Spring Cloud Gateway, OAuth 2.0, AWS Glue, AWS SQS, Terraform, and React.js.
- No empirical evaluation of any kind is reported — no accuracy, no RMSE, no user study, no dataset description.
- The ethical framework rests on confidentiality, fairness, transparency, and user autonomy, but these are stated as principles rather than tested properties.
- The paper claims the system benefits users at all income levels, but cites prior work [13] finding that a salary-management recommendation system is useful only for high-income individuals, without reconciling the contradiction.

## Cited Works

- Lu, J.; Zhang, Q.; Zhang, G. (2020) (context) — Theoretical studies for recommendation systems, with applications, prototypes, and real examples. [p. 1]
- Verma, P.; Sharma, S. (2020) (context) — AI-based recommendation system providing personalized recommendations and feedback. [p. 2]
- Roy, D.; Dutta, M. (2022) (context) — Systematic review and research perspective on recommender systems; notes e-commerce accounts for 17% of reviewed studies. [p. 2]
- Hodovychenko, M. A.; Gorbatenko, A. A. (2023) (context) — Recommender systems models, challenges, and opportunities. [p. 2]
- He, X.; Liu, Q.; Jung, S. (2024) (context) — Impact of recommendation system on user satisfaction; psychological reactance. [p. 2]
- Deschênes, M. (2020) (context) — Recommender systems to support learners' agency; predicting how a user will rate a resource. [p. 2]
- Reiter-Gavish, L.; Qadan, M.; Yagil, J. (2021) (context) — Financial advice followership; more experienced investors less likely to use recommendations. [p. 2]
- Schepen, A.; Burger, M. J. (2022) (context) — Professional financial advice and subjective well-being; stronger for households with income growth. [p. 2]
- Fieberg, C.; Hornuf, L.; Streich, D. (2023) (context) — Using GPT-4 for financial advice; offers investment portfolios reflecting risk tolerance and stability preference. [p. 2]
- Sharaf, M.; Hemdan, E. E. D.; El-Sayed, A. et al. (2022) (context) — Survey on recommendation systems for financial services; banking, stocks, insurance. [p. 2]
- Zatevakhina, A.; Dedyukhina, N.; Klioutchnikov, O. (2019) (context) — Recommender systems as foundation of an intelligent financial platform; notes a limit of development has been reached. [p. 2]
- Zibriczky, D. (2016) (context) — Recommender systems meet finance; personalized recommendations on spending opportunities based on credit card usage and geolocation. [p. 2]
- Kanaujia, P. K. M.; Behera, N.; Pandey, M.; Rautaray, S. S. (2016) (context) — Recommendation system for salary management; concludes useful when a person has high income. [p. 2]
- Li, T.; Song, J. (2024) (context) — Deep learning-powered financial product recommendation; Transformers, transfer learning, GNN. [p. 2]
- Ayemowa, M. O.; Ibrahim, R.; Khan, M. M. (2024) (context) — Analysis of recommender systems using generative AI; GANs as predominant technique. [p. 2]
- Yue, X. (2024) (context) — Application of AI technology in personalized recommendation system for financial services; LSTM + LDA. [p. 2]
- Jannach, D.; Pu, P.; Ricci, F.; Zanker, M. (2021) (context) — Recommender systems past, present, future; evaluate diversity and novelty, not only accuracy. [p. 2]
- Chua, A. Y. K.; Pal, A.; Banerjee, S. (2023) (context) — AI-enabled investment advice; acceptance as function of attitudes, trust, perceived accuracy, uncertainty. [p. 3]
- Longoni, C.; Bonezzi, A.; Morewedge, C. K. (2019) (context) — Resistance to medical artificial intelligence; consumers prefer human interaction in high-involvement fields. [p. 3]
- Zhang, L.; Pentina, I.; Fan, Y. (2021) (context) — Comparing perceptions of human vs robo-advisor in financial services. [p. 3]
- Bonelli, M. I.; Döngül, E. S. (2023) (context) — Robo-advisors in financial services; NLP integration for chatbots. [p. 3]
- Zhang, Q.; Lu, J.; Jin, Y. (2020) (context) — Artificial intelligence in recommender systems; users find it difficult to trust systems due to opacity and privacy concerns. [p. 3]
- del Valle, J. I.; Lara, F. (2024) (context) — AI-powered recommender systems and preservation of personal autonomy. [p. 3]
- Christman, J. (2020) (context) — Autonomy in moral and political philosophy; definition of human autonomy. [p. 3]
- Milano, S.; Taddeo, M.; Floridi, L. (2020) (context) — Recommender systems and their ethical challenges; ethical impacts immediate or future. [p. 5]
- Karakolis, E.; Oikonomidis, P. F.; Askounis, D. (2022) (context) — Identifying and addressing ethical challenges in recommender systems; privacy, personal data, fairness, transparency, identity, society. [p. 5]
- Shuryhin, K. A.; Zinovatna, S. L. (2024) (methodology) — Architecture of the financial manager system using AI technologies; Build-Train-Deploy pattern with AWS SageMaker. [p. 7]