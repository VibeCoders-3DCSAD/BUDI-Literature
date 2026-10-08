---
paper_id: A--Chahar-2026
first_author: Chahar
year: 2026
title: "Artificial Intelligence Powered Personal Finance Management System"
venue: Not reported
doi: Not reported
designation: algorithm
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, budgeting, income_expense_management, savings_debt_management, financial_planning, model_algorithm_integration, model_development, system_development, software_quality_evaluation, model_performance_evaluation]
module_rationale:
  pfm_apps_overview: "Table 1 surveys Mint, YNAB, Digit and Tally with their features and AI techniques (Table 1, p. 3-4)."
  pfm_apps_features: "The proposed assistant offers budgeting, expense tracking, bill reminders, dashboards and conversational queries (Table 1, p. 3-4; Sec. 3.A, p. 5)."
  pfm_apps_problems: "Existing solutions rely on static budgeting and generic guidance and lack true intelligence or adaptive learning (Abstract, p. 1; Intro, p. 2; Sec. 2, p. 3)."
  pfm_apps_importance: "The paper argues AI can bridge financial illiteracy and empowerment and adapt to gig-economy income streams (Intro, p. 2; Sec. 5, p. 8-9)."
  budgeting: "Tailored budget recommendations and adaptive budgets are a core promised output (Abstract, p. 1; Sec. 3.A, p. 5; Sec. 8, p. 11)."
  income_expense_management: "The expense classification engine categorises transactions into categories such as food, transport and utilities (Sec. 3.A, p. 5; Sec. 3.C, p. 6)."
  savings_debt_management: "The system is to provide detailed instructions about debt control and savings alongside budget guidelines (Sec. 4.D, p. 8)."
  financial_planning: "Customised financial planning is named as a primary AI application for personal finance (Sec. 4.D, p. 8)."
  model_algorithm_integration: "The architecture integrates ML expense classification, time-series forecasting, recommendation and NLP into one modular pipeline (Sec. 3.A, p. 5; Abstract, p. 1)."
  model_development: "Random Forest, SVM and LSTM models are trained with TF-IDF and word embeddings plus cross-validation (Sec. 3.C, p. 6)."
  system_development: "React.js, Flask, MongoDB and Firebase form the implementation stack (Sec. 3, p. 7)."
  software_quality_evaluation: "A user survey reports satisfaction ratings for goal-setting, categorisation accuracy and ease of use (Sec. 9, p. 12)."
  model_performance_evaluation: "Accuracy, precision, MAE and F1-score are named as the evaluation metrics for the models (Sec. 6.A, p. 9)."
---

## Summary

The paper proposes an AI-powered personal finance assistant that combines machine learning (ML) and natural language processing (NLP) to deliver dynamic, user-specific financial insights. The assistant is designed to generate tailored budget recommendations, provide financial education aligned with user proficiency, and secure financial data through advanced encryption. The system architecture comprises a data collection and integration module, an expense classification engine, a predictive analytics module, a recommendation system, an NLP interface, and a security and privacy layer. The authors report a preliminary prototype built on React.js, Flask, MongoDB and Firebase, and a user survey returning an overall satisfaction rating of 4.4/5. The paper states that a systematic literature review and preliminary prototype development validate the feasibility of the approach, though no model performance numbers (accuracy, precision, MAE, F1) are printed anywhere in the results section.

## Problem and Motivation

Managing personal finance has become increasingly complex because of evolving income models, diverse investment opportunities, fluctuating markets and changing consumer behaviours. Traditional tools such as spreadsheets and manual budgeting fall short on real-time insight, adaptability and predictive capability, leading to poor savings habits, increased debt and unpreparedness for financial emergencies. The rise of gig-economy workers, freelancers, remote jobs and decentralized finance platforms means users now need tools that adapt to diverse income streams and unconventional portfolios. Existing personal finance solutions rely on static budgeting methods and generic investment guidance, and most current systems lack true intelligence or are limited by static rule-based designs; many do not prioritise user privacy, adaptability or educational value. The paper therefore argues there is a clear opportunity to design an AI-powered system that both assists users in managing their finances and educates and empowers them through intelligent automation and personalised insights.

## Method

**Design.** The paper states no formal design label; it describes itself as combining a systematic literature review and preliminary prototype development (Abstract, p. 1), with a modular system architecture and a user satisfaction survey reported in the conclusion.
**Sample.** Survey respondents (N not reported) rating the prototype; the unit of analysis is the user's rating of specific system features (goal-setting, transaction categorisation, ease of use, overall satisfaction). The literature review surveys prior studies and commercial tools (Mint, YNAB, Digit, Tally) with no formal sampling frame.
**Context.** geography: India (all four authors are affiliated with Sharda University, India and Amity University Noida, India, p. 1); population: personal finance application users (N not reported); setting: Web-based application with React.js frontend, Flask backend, MongoDB database and Firebase authentication, evaluated through a user survey.

- Collect financial data via secure API connections to banking institutions or manually uploaded CSV files (Sec. 3.B, p. 6).
- Preprocess raw data by normalisation, missing-value handling, feature extraction, and removal of special characters and stop words from transaction descriptions (Sec. 3.B, p. 6).
- Train several supervised models — Random Forest, Support Vector Machine (SVM) and a deep-learning LSTM network for sequential text analysis — to assign each transaction to a category (Sec. 3.C, p. 6).
- Apply feature engineering on transaction metadata (amount, date, merchant name) and text vectorisation with TF-IDF and word embeddings (Sec. 3.C, p. 6).
- Use cross-validation to select the model with the best accuracy and generalisation (Sec. 3.C, p. 6).
- Implement end-to-end encryption for data in transit and at rest, role-based access control, anonymisation during training, and GDPR compliance (Sec. 3.D, p. 6).
- Build the application with React.js for the frontend UI, Flask for backend and ML operations, MongoDB for database work and Firebase for authentication and real-time functions (Sec. 3, p. 7).
- Add a natural language processing interface for conversational queries and commands (Sec. 3.A, p. 5).
- Build a recommendation system that generates personalised financial advice and budgeting tips based on user behaviour, goals and predictive insights (Sec. 3.A, p. 5).
- Evaluate with a user survey covering goal-setting functionality, correctness of transaction categorisation, convenience of use, and overall satisfaction (Sec. 9, p. 12).

## Software

- React.js (frontend UI; version not reported)
- Flask (backend and ML operations; version not reported)
- MongoDB (database; version not reported)
- Firebase (authentication and real-time functions; version not reported)
- Jinja2 HTML templating (Figure 2 caption, p. 5)
- SQL view for monthly financial summary (Figure 3, p. 6)
- Random Forest (version not reported)
- Support Vector Machine (SVM; version not reported)
- Long Short-Term Memory (LSTM) network (version not reported)
- TF-IDF and word embeddings (version not reported)

## Key Findings

- The paper names Accuracy, Precision, Mean Absolute Error (MAE) and F1-score as the metrics for the models (Sec. 6.A, p. 9) but prints no numeric value for any of them.
- Survey results: goal-setting functionality 4.3/5; correctness of transaction categorisation 4.2/5; convenience of use 4.5/5; overall satisfaction 4.4/5 (Sec. 9, p. 12).
- Several users questioned transaction classification accuracy, particularly for unclear or vendor-specific transactions (Sec. 9, p. 12).
- Recommendations were made to increase the accuracy of spending predictions, especially for variable or non-recurring costs like meals (Sec. 9, p. 12).
- The device performed well for users with stable earnings and predictable expenses, but struggled to offer tailor-made hints for users with relatively fluctuating earnings or abnormal spending patterns (Sec. 6.B, p. 10).
- Accuracy of predictions and suggestions was driven by the quality of input facts; incomplete or misguided transaction records produced less dependable effects (Sec. 6.B, p. 10).
- The system extracts data from three potential sources: manual entry, financial application exports and bank feeds (Sec. 8, p. 11).

## Key Figures and Tables

- Figure 1 (p. 5): Real Time Budget — a screenshot/illustration of the real-time budget view; no underlying data are printed.
- Figure 2 (p. 5): Jinja2 HTML template used in a Flask web application to display and submit user expense data and render an expense chart image from the static directory.
- Figure 3 (p. 6): SQL view definition generating a monthly financial summary per user, calculating total income, expenses and savings using conditional aggregation.
- Figure 4 (p. 7): Data Flow Diagram — User/Institution → Data Input → Data Preprocessing → Feature Extraction → Data Storage → AI Engine → Report Generation → User Interface.
- Figure 5 (p. 8): User engagement growth with the personal finance management system — no numeric data printed.
- Figure 6 (p. 9): Distribution of Expenses across Transaction Types — no numeric data printed.
- Table 1 (p. 3-4): AI-powered finance management tools — Mint (Budgeting, Expense tracking, Bill reminders; Machine Learning, Data Mining; Easy to use, Real-time transaction tracking, Free to use), YNAB (Goal-based budgeting, Expense categorization; Predictive Analytics, Behavioral Modeling; Flexible budgeting, Real-time budget updates), Digit (Automatic saving, Goal setting, Automated transfers; Behavioral Analytics, Automation; Automated saving, Focus on short-term goals), Tally (Credit card management, Debt consolidation; Machine Learning, Predictive Analytics; Automates credit card payments). No quantitative metrics are given for any tool.

## Limitations and Gaps

- The paper names Accuracy, Precision, MAE and F1-score as evaluation metrics (Sec. 6.A, p. 9) but prints no numeric value for any of them anywhere in the results or conclusion; the entire Results and Evaluation section is qualitative.
- The paper reports no sample size for its user survey (Sec. 9, p. 12), and the survey instrument, recruitment and analysis method are not described.
- The paper reports no dataset size, no train/test split, and no per-model breakdown for the Random Forest, SVM and LSTM classifiers (Sec. 3.C, p. 6).
- The paper acknowledges that accuracy of predictions and suggestions was driven by input-fact quality, and that incomplete or misguided transaction records cause less dependable effects (Sec. 6.B, p. 10).
- The authors acknowledge that the device struggled to offer tailor-made hints for users with fluctuating earnings or abnormal spending patterns (Sec. 6.B, p. 10).
- The authors acknowledge that users hesitate to grant trust in AI-driven financial solutions due to fear of errors and system instability (Sec. 7.A, p. 10).
- The authors acknowledge that AI-based personal financial management depends on data quality and accessibility, and that data siloing makes aggregation and analysis more challenging (Sec. 7.B, p. 10).
- The authors acknowledge that AI algorithms can inadvertently perpetuate already present discriminatory practices because they deliver dissimilar results across population segments (Sec. 7.D, p. 11).
- The authors acknowledge regulatory complexity — Know Your Customer provisions, algorithmic bias and model drift — as open challenges (Sec. 7.C, p. 11).
- [unacknowledged] No statistical test, confidence interval, or effect size is reported for the survey ratings; the 4.2-4.5/5 scores have no reported variance or N.
- [unacknowledged] The prototype is described only at the level of a technology stack (React.js, Flask, MongoDB, Firebase) with no code, no repository, no deployment details and no reproducibility artefacts (Sec. 3, p. 7).
- [unacknowledged] No external validation, no held-out test set, no baseline comparison and no ablation of the ML or NLP components are reported.
- [unacknowledged] The paper claims "systematic literature review" (Abstract, p. 1) but reports no search strategy, inclusion criteria or screening counts.
- [unacknowledged] The paper's own text contradicts itself on whether the survey is described in Section 5 or Section 9; the satisfaction numbers appear in both the "Potential impact" and "Conclusion" sections (Sec. 5, p. 8-9; Sec. 9, p. 12).
- [unacknowledged] Several passages are garbled or use non-standard terminology (e.g. "Hourly Problem-Solving Model" in Sec. 7.A, p. 10; "act.js" for React.js in Sec. 3, p. 7), making some claims hard to verify.

## Definitions

- **AI-Powered Personal Finance Management System** — the paper's proposed modular assistant that integrates ML, NLP and data analytics for personal finance.
- **Expense Classification Engine** — a module that applies ML models to categorise transactions automatically into predefined categories (e.g. food, transport, utilities).
- **Predictive Analytics Module** — a time-series forecasting component that predicts future expenses and income flows for proactive financial planning.
- **Recommendation System** — a component that generates personalised financial advice and budgeting tips based on user behaviour, goals and predictive insights.
- **Natural Language Processing Interface** — a conversational interface allowing users to interact with the system through queries and commands.
- **Security and Privacy Layer** — a component implementing encryption, anonymisation and access control to protect sensitive user data.
- **TF-IDF** — a text vectorisation technique used to represent transaction descriptions as features for the classification models.
- **ARIMA** — a time-series forecasting method cited in the literature review as applied to predict future expenses or cash flow trends.
- **LSTM** — Long Short-Term Memory network; used both as a deep-learning classifier for sequential text analysis and as a time-series forecasting model.
- **Robo-advisors** — AI-powered services that deliver retail investors access to professional wealth management at affordable cost (Sec. 5, p. 8-9).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Goal-setting functionality, user survey | satisfaction rating (out of 5) | 4.3/5 | — | — | Sec. 9, p. 12 |
| Correctness of transaction categorisation, user survey | satisfaction rating (out of 5) | 4.2/5 | — | — | Sec. 9, p. 12 |
| Convenience of use, user survey | satisfaction rating (out of 5) | 4.5/5 | — | — | Sec. 9, p. 12 |
| Overall satisfaction, user survey | satisfaction rating (out of 5) | 4.4/5 | — | — | Sec. 9, p. 12 |
| Expense classification, proposed system | accuracy | Not reported | — | — | Sec. 6.A, p. 9 |
| Expense classification, proposed system | precision | Not reported | — | — | Sec. 6.A, p. 9 |
| Spending prediction, proposed system | mean absolute error (MAE) | Not reported | — | — | Sec. 6.A, p. 9 |
| Budget allocation optimisation, proposed system | F1-score | Not reported | — | — | Sec. 6.A, p. 9 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The rising complexity of financial systems, combined with limited financial literacy and inadequate budgeting tools, poses significant challenges for individuals in managing personal finances effectively." | Abstract, p. 1 | pfm_apps_problems |
| "Existing personal finance solutions often rely on static budgeting methods and offer generic investment guidance, lacking adaptability and personalization." | Abstract, p. 1 | pfm_apps_problems |
| "The assistant is designed to generate tailored budget recommendations, provide financial education aligned with user proficiency levels, and ensure secure financial data handling through advanced encryption protocols." | Abstract, p. 1 | budgeting |
| "Despite the existence of several financial management tools, most current systems lack true intelligence or are limited by static rule-based designs." | Intro, p. 2 | pfm_apps_problems |
| "AI can bridge the gap between financial illiteracy and financial empowerment by automating complex tasks such as categorizing expenses, forecasting budgets, analyzing credit scores, and even detecting anomalies that may indicate fraud or identity theft." | Intro, p. 2 | pfm_apps_importance |
| "This table 1 summarizes the technical aspects of several prominent AI-powered personal finance management tools. It highlights their key features, AI techniques, strengths, and limitations." | Sec. 2, p. 3 | pfm_apps_overview |
| "The classification engine employs supervised machine learning algorithms to assign each transaction to appropriate categories." | Sec. 3.C, p. 6 | income_expense_management |
| "Initially, a labeled dataset of transactions is used to train several models such as Random Forest, Support Vector Machine (SVM), and a deep learning-based Long Short-Term Memory (LSTM) network for sequential text analysis." | Sec. 3.C, p. 6 | model_development |
| "Given the sensitivity of financial data, the system incorporates robust security mechanisms" | Sec. 3.D, p. 6 | model_algorithm_integration |
| "Real-time financial data analysis through AI algorithms operates on large data sets to provide customers with valuable insights into their expenditure habits and investment returns and progress toward financial targets." | Sec. 4.B, p. 8 | pfm_apps_features |
| "Customized financial planning emerges from AI-powered personal finance tools through assessing what users prefer and demand." | Sec. 4.D, p. 8 | financial_planning |
| "The systems will provide detailed instructions about debt control and savings together with budget guidelines." | Sec. 4.D, p. 8 | savings_debt_management |
| "High satisfaction was shown by the survey results, with favorable comments given to important areas including goal-setting functionality (4.3/5), correctness of transaction categorization (4.2/5), and convenience of use (average score of 4.5/5)." | Sec. 9, p. 12 | software_quality_evaluation |
| "The accuracy of transaction classification was questioned by a few users, particularly when dealing with unclear or vendor-specific transactions." | Sec. 9, p. 12 | software_quality_evaluation |
| "The device accomplished well for users with stable earnings and predictable expenses, however, struggled to offer tailor-made hints for users with relatively fluctuating earnings or abnormal spending patterns." | Sec. 6.B, p. 10 | model_performance_evaluation |
| "Records first-class: The accuracy of predictions and suggestions was motivated via the exceptional of input facts." | Sec. 6.B, p. 10 | model_performance_evaluation |
| "People find it hard to grant trust in AI-driven financial solutions and hence hinder widespread adoption." | Sec. 7.A, p. 10 | pfm_apps_problems |
| "AI algorithms can inadvertently perpetuate already present discriminatory practices because these algorithms deliver dissimilar results across population segments." | Sec. 7.D, p. 11 | pfm_apps_problems |

## Remember This

- The paper proposes an AI-powered personal finance assistant combining ML expense classification, time-series forecasting, a recommendation engine, and an NLP interface.
- Implementation stack: React.js frontend, Flask backend, MongoDB database, Firebase authentication.
- The only numeric outcomes reported are user survey ratings: goal-setting 4.3/5, transaction categorisation 4.2/5, ease of use 4.5/5, overall satisfaction 4.4/5 (Sec. 9, p. 12).
- Accuracy, Precision, MAE and F1-score are named as evaluation metrics (Sec. 6.A, p. 9) but no value is printed for any of them.
- Table 1 surveys Mint, YNAB, Digit and Tally with features and AI techniques but no quantitative metrics.
- The paper acknowledges data quality, model adaptability to irregular income, user trust, and algorithmic bias as open challenges (Sec. 6.B, p. 10; Sec. 7, p. 10-11).

## Cited Works

- "Quicken: One place to manage your money and your life | Quicken." [1] — cited as an early static PFM tool without advanced analytics or predictive modelling. [p. 2]
- L. Zhang, W.-D. Zhou, T.-T. Su, and L.-C. Jiao, "Decision tree support vector machine," Int. J. Artif. Intell. Tools, vol. 16, no. 01, pp. 1–15, Feb. 2007. [2] — cited for ML classifiers (decision trees, SVM, neural networks) applied to transaction categorisation. [p. 3]
- S. Siami-Namini, N. Tavakoli, and A. Siami Namin, "A Comparison of ARIMA and LSTM in Forecasting Time Series," ICMLA, Dec. 2018, pp. 1394–1401. [3] — cited for time-series forecasting of expenses and cash flow. [p. 3]
- J. Luef, C. Ohrfandl, D. Sacharidis, and H. Werthner, "A recommender system for investing in early-stage enterprises," SAC, Mar. 2020, pp. 1453–1460. [4] — cited for collaborative filtering and content-based recommendation in personal finance. [p. 3, 8, 10]
- Prof. Vijaykumar S, Shriya R, and Vibha M, "Empowering Financial Peace through Chatbot Guidance," IJARSCT, Feb. 2024, pp. 509–516. [5] — cited for NLP chatbots and virtual assistants in financial applications. [p. 3]
- "Web-based Design of Financial Apps: Case of Kosan 54 - ProQuest." [6] — cited for a PHP/MySQL online application combining billing, auditing, budgeting and planning. [p. 4]
- A. Ahmed, C. Mohammed, A. Ahmad, and M. Abdulrazzaq, "Design and Implementation of a Responsive Web-based System for Controlling the Financial Budget of Universities," J. Technol. Inform. JoTI, vol. 5, no. 1, pp. 1–7, July 2023. [7] — cited for a responsive university budget administration system. [p. 4]
- A. Molina-García, A. J. Cisneros-Ruiz, M. D. López-Subires, and J. Diéguez-Soto, "How does financial literacy influence undergraduates' risk-taking propensity?," Int. J. Manag. Educ., vol. 21, no. 3, p. 100840, Nov. 2023. [8] — cited for the negative correlation between risk tolerance and literacy. [p. 4, 8]
- J. P. Rath and S. Patra, "Financial Literacy In India – A New Way Forward," ComFin Res., vol. 11, no. 2, pp. 20–27, Apr. 2023. [9] — cited on the importance of literacy in navigating Indian financial systems. [p. 4]
- V. S. Dube and P. K. Asthana, "Financial knowledge, attitude and behaviour components of financial literacy: a study of Indian higher education students," Int. J. Indian Cult. Bus. Manag., vol. 28, no. 1, pp. 124–143, Jan. 2023. [10] — cited on knowledge, ability and behavioural deficits in Indian students. [p. 4]
- L. Cao, "AI in Finance: Challenges, Techniques and Opportunities," arXiv:2107.09051, July 2021. [11] — cited for a survey of AI strategies and analytics/learning approaches in finance. [p. 4]
- A. J. Warchlewska, A. Janc, and R. Iwański, "Personal Finances in the Era of Modern Technological Solutions," J. Finance Financ. Law, vol. 1, no. 29, pp. 155–174, Mar. 2021. [12] — cited on consumer acceptability of AI finance tools and demographic differences. [p. 4]
- S. Galperti, "A theory of personal budgeting," Theor. Econ., vol. 14, no. 1, pp. 173–210, 2019. [13] — cited on theoretic connections between consumption-saving biases and budgeting, and on predictive analytics. [p. 4, 8]
- G. Paliwal, A. Kumar, K. P. Sharma, D. Bhargava, and V. M. Shrimal, "Transformative impact of explainable artificial intelligence: bridging complexity and trust," Discov. Artif. Intell., vol. 5, no. 1, p. 51, May 2025. [14] — cited on trust and explainability as barriers to AI adoption. [p. 10]
- W. Ruan, M. Xu, W. Fang, L. Wang, L. Wang, and W. Han, "Private, Efficient, and Accurate: Protecting Models Trained by Multi-party Learning with Differential Privacy," IEEE S&P, May 2023, pp. 1926–1943. [15] — cited on privacy-preserving machine learning. [p. 11]