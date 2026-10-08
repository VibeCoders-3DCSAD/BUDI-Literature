---
paper_id: I--Yadav-2026
first_author: Yadav
year: 2026
title: "Intelligent Personal Finance Management System for Smart Budgeting and Real-Time Expense Tracking: Design and Development"
venue: "International Scientific Journal of Engineering and Management (ISJEM)"
doi: 10.55041/ISJEM06330

designation: international
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, financial_planning, budgeting, savings_debt_management, income_expense_management, rule_based_classification, linear_programming, model_algorithm_integration, data_collection, model_development, system_development]
module_rationale:
  pfm_apps_overview: "Sec. I.A and Sec. II.A trace PFM tooling from spreadsheets and web banking to mobile trackers, defining the class of applications the paper addresses (pp. 1-2)."
  pfm_apps_features: "Sec. III.A.3 specifies the proposed feature set — real-time expense categorization, smart budgeting, anomaly alerts, personalized recommendations — and Sec. IV names dashboards, goal tracking and nudges (pp. 4-5)."
  pfm_apps_problems: "Sec. I.A, Sec. II.A and Sec. V.A state that current apps offer restricted personalization, fixed budgetary arrangements, passive reporting and no real-time prediction (pp. 1-2, 6)."
  pfm_apps_importance: "Sec. IV and Sec. V.A.1 assert that real-time tracking, AI nudges and adaptive advice would raise budget adherence, savings rates and financial well-being (pp. 5-6)."
  financial_planning: "Sec. I frames the problem as balancing income, expenditure and savings, and Sec. II.B cites optimization-based models that allocate monthly income more efficiently to expense factors (pp. 1, 2-3)."
  budgeting: "Sec. II.B defines smart budgeting as flexible, behaviour-responsive budgets, and Sec. IV.B claims the smart budgeting module improves budget adherence (pp. 2-3, 5-6)."
  savings_debt_management: "Sec. III.A.3 and Sec. IV.C name saving plans, effective savings paths, debt management and goal-progress tracking as system outputs (pp. 4, 5-6)."
  income_expense_management: "Sec. II.C and Sec. III.B.4 describe automatic transaction import plus a detailed, customizable income and expense classification structure with user corrections (pp. 3, 5)."
  rule_based_classification: "Sec. II.C and Sec. II.D.2 describe rule-based transaction classification and rule-coded expert guidance, and Sec. III.C.1 proposes rule-based classifiers as the first expense-categorization step (pp. 3, 5)."
  linear_programming: "Sec. III.C.2 names linear programming among the optimization tools used to calculate budget resources against user objectives (p. 5)."
  model_algorithm_integration: "Sec. III.A.3 assembles the AI and Analytics Engine from four coupled modules, and Sec. III.C.2 chains time-series forecasting into optimization and reinforcement learning (pp. 4, 5)."
  data_collection: "Sec. III.B states that training uses aggregated, anonymized transaction datasets narrowed with user-consented personal data, then tokenized, normalized and imputed (p. 5)."
  model_development: "Sec. III.B and Sec. III.C give the preprocessing steps and the algorithm-selection and training approach for categorization, budgeting/forecasting and anomaly detection (p. 5)."
  system_development: "Sec. III.A specifies a modular microservices architecture with Open Banking/Plaid interfaces, encrypted transport, NoSQL plus relational storage, and a web/mobile UX layer (pp. 3-4)."
---

# I--Yadav-2026

## Summary

The paper proposes the design and development of an **Intelligent Personal Finance Management System (IPFMS)** that combines smart budgeting with real-time expense tracking. It argues that conventional personal finance management (PFM) systems have been poor at offering personalized, actionable advice, leaving users frustrated with financial planning and long-term financial security (Abstract, p. 1). The proposed system is described as integrating artificial intelligence — machine learning and rule-based systems — to analyse financial data, automate expense management and produce predictive budgeting recommendations keyed to individual behaviour and financial goals.

The core of the paper is architectural. The IPFMS is specified as a modular, microservices-based system with four functional layers: a Data Acquisition and Integration Layer (secure connections to banks, card providers and investment platforms through Open Banking frameworks or Plaid); a Data Processing and Storage Layer (cleaning, standardization, deduplication, NoSQL plus relational storage); an AI and Analytics Engine; and a User Interface / User Experience Layer (Sec. III.A, pp. 3-4). The AI and Analytics Engine is itself decomposed into four modules — an Expense Categorization Module, a Smart Budgeting Module, an Anomaly Detection Module, and a Personalized Recommendation Engine (Sec. III.A.3, p. 4).

Algorithm selection is discussed by task rather than by benchmark: rule-based classifiers and supervised models (logistic regression, random forests, lightweight neural networks) for expense categorization; ARIMA, Prophet and LSTMs for income and spending forecasting; linear programming and genetic algorithms to allocate budget resources; reinforcement learning agents for savings-path discovery; and K-Means, DBSCAN and isolation forests for anomaly detection (Sec. III.C, p. 5). No algorithm is implemented, trained or evaluated in the paper.

Section IV is titled "Result" but the paper states plainly that the design and development methodology is the main concern of the paper at this time, and the material that follows is presented as **projected** rather than measured: "the introduction of the suggested Intelligent Personal Finance Management System is likely to have a positive impact on the financial literacy of users, the feeling of control, as well as their overall financial well-being" (Sec. IV, p. 5). Section V discusses implications, technical considerations and ethical/regulatory issues; Section VI concludes and proposes future work on AI integration, larger data sources and stakeholder collaboration. The paper prints **no sample size, no evaluation dataset, no metric, no confidence interval and no p-value** for its own system.

## Problem and Motivation

Personal finance is described as complicated, with most people struggling to balance income, expenditure and savings. Although the array of digital instruments meant to assist in managing finances is increasing, they do not always serve the actual needs of the users, so many fail to fulfil their financial ambitions and are financially stressed (Sec. I, p. 1). The difficulties are aggravated by lack of visibility into spending behaviour, the superiority of manual financial tracking, and the lack of practical, customized advice (Sec. I, p. 1).

The paper's historical account runs from paper ledgers and spreadsheets, through web banking interfaces that made measuring income and expenditure simpler, to mobile applications with expense tracking, financial summaries and easy visualizations (Sec. I.A and Sec. II.A, pp. 1-2). Its complaint is that these improvements did not remove the underlying weakness: most applications remain highly passive, financial planning and interpretation is "almost left to the user" (Sec. II.A, p. 2), and most represent a static image of financial health without prediction, personalization or real-time financial integration (Sec. I.A, p. 1).

The stated motivation for AI is that it allows a move away from straightforward data collection toward systems that read behaviour, predict future demands and facilitate individual financial care (Sec. I.B, p. 2). Two further pressures are named: the desire to make sophisticated financial advice more accessible and cheaper, addressing information asymmetry and misaligned incentives in traditional advising (Sec. I.B, p. 2); and the availability of real-time expense tracking through secure bank and card connections, which makes an instant picture of expenditure behaviour possible (Sec. II.C, p. 3).

## Method

**Design.** The authors state no formal design label. The paper is a system design-and-development proposal: it presents an architecture, a data-processing plan and an algorithm-selection rationale for a system that is described but not built, deployed or evaluated. Section IV, headed "Result", explicitly reports projected rather than measured effects.

**Sample.** Not reported. The paper names no dataset size, no participant count, no number of transactions and no unit of analysis. It states only that "the system is trained with aggregated and anonymized datasets of transactions in the first place, and further narrowed down with user-consented personal data" (Sec. III.B, p. 5), without giving N for either component.

**Context.** geography: India — all three authors are in the Department of CSE, Galgotias University, Greater Noida, India (p. 1); population: Not reported — no user group, income band or demographic is specified for design or evaluation; setting: virtual/computational — a proposed web-and-mobile financial system, described as compliant with PSD2, GDPR and CCPA (Sec. V.B.1, p. 6), with no live deployment, no institutional partner and no field trial reported.

The design proceeds in four parts.

**1. Architecture (Sec. III.A, pp. 3-4).** A modular, domain-based microservices architecture intended to permit independent development, testing and deployment of each component. Four layers are specified:

- *Data Acquisition and Integration Layer* — secured communication with banks, credit card providers and investment hosting platforms, using secure APIs such as Open Banking frameworks or Plaid; all exchanges encrypted in transit and at rest; the layer also collects user-specified financial objectives and individual interests as personalization inputs.
- *Data Processing and Storage Layer* — cleaning, standardization and deduplication of transaction data, then storage in a combination of flexible NoSQL stores and relational storage; user profiles, defined financial goals and past spending records are maintained here.
- *AI and Analytics Engine* — the "core intelligence" of the system, comprising the Expense Categorization Module (SVM, Random Forest, neural networks trained on labelled transactions, improved through continuous user correction), the Smart Budgeting Module (predictive analytics and optimization over past spending habits, income trends, user-defined finance targets and sometimes external economy indicators; reinforcement learning for long-term savings policies in more complex designs), the Anomaly Detection Module (unsupervised clustering and isolation forests, notifying the user on detection), and the Personalized Recommendation Engine (collaborative filtering, content-based recommendation and rule-guided reasoning for financial products, saving plans and investing options).
- *User Interface / User Experience Layer* — web and mobile, with a real-time financial dashboard, customizable budget monitoring tool, goal progress visualization and interactive financial reports.

**2. Data collection and preprocessing (Sec. III.B, p. 5).** Training data are aggregated and anonymized transaction datasets, narrowed with user-consented personal data. Four preprocessing steps are named: tokenization and feature extraction (raw transaction descriptions into numerical features); data normalization and scaling (consistency, reduced training bias); handling missing data (imputation and consistency tests); and a categorization scheme (a detailed, flexible income and expense classification structure supporting both automatic classification and user customization).

**3. Algorithm selection and training (Sec. III.C, p. 5).** The paper states that "the choice of specific algorithms will depend on the nature of the task and the characteristics of the data" and then assigns candidate methods per task. For expense categorization: rule-based classifiers for large transaction volumes, supported by supervised models such as logistic regression, random forests or lightweight neural networks trained on large pre-labelled sets, with active learning to improve the model from user feedback and corrections. For smart budgeting and forecasting: ARIMA, Prophet and LSTMs for time-series forecasting of income and spending trends; optimization tools including linear programming and genetic algorithms to calculate budget resources; and reinforcement learning agents for long-term savings plans and multi-objective optimization. For anomaly detection: unsupervised clustering such as K-Means and DBSCAN, plus isolation forests for high-dimensional financial data.

**4. User experience and interaction design (Sec. III.D, p. 5).** Five design commitments: an intuitive dashboard summarizing financial status, budget status and goal progress; interactive visualizations condensing complex data into applicable insights; actionable insights and nudges (for example a notification when a spending category grows, or help making small transfers into savings); goal setting and tracking (home purchase, retirement, debt pay-off) with progress charts; and a feedback mechanism letting users correct wrongly-classified transactions and rate recommendations, with corrections fed back into retraining.

The paper also lists implementation-facing technical considerations — compliance with PSD2, GDPR and CCPA; encryption, tokenization and multi-factor authentication; periodic model retraining; explainable AI methods to make advice legible to users and financial professionals; and DevOps/CI-CD practice for a multi-model microservices system (Sec. V.B, pp. 6-7) — and ethical concerns: algorithmic bias from small or imbalanced training sets, privacy and trust, accountability for wrong advice, and retention of human oversight with user override (Sec. V.C, p. 7).

## Key Findings

The paper reports no empirical findings. The claims it does make are design and projection claims, listed here with locators so they are not mistaken for results.

- The paper's stated contribution is architectural: an IPFMS combining intelligent budgeting with real-time expense tracking, built as a modular microservices architecture with an AI and Analytics Engine of four modules (Sec. III.A, pp. 3-4).
- Section IV reports projected, not measured, effects: "the introduction of the suggested Intelligent Personal Finance Management System is likely to have a positive impact on the financial literacy of users, the feeling of control, as well as their overall financial well-being" (Sec. IV, p. 5).
- The paper claims real-time cost monitoring and simplified graphical interfaces would give users a better and more instant sense of their monetary status, and that automated categorization minimizes the manual nature of transferring personal finances (Sec. IV.A, p. 5).
- It claims the intelligent budgeting module "should enhance the capacity of the users to adhere to financial plans", replacing fixed monthly amounts with dynamic recommendations responsive to real spending performance and fluctuating financial conditions (Sec. IV.B, p. 5).
- It claims predictive capability of the AI engine "enable[s] individuals to estimate the financial needs in the future and possible deficit so as to plan in advance on how to spend or save money" (Sec. IV.B, pp. 5-6).
- It claims the anomaly-detection element "will have an alerting user on the occurrence of any suspicious or possibly fraudulent transactions", enhancing general financial security (Sec. IV.C, p. 6).
- It claims the personalized recommendation engine gives the right solution at the right time for debt management, investment planning and preparation for a major life event (Sec. IV.C, p. 6).
- It projects that adaptive re-tuning of the system over time increases "the probability of positive outcomes in terms of increased rates of savings, reduced levels of debt ratio, and a shift toward long-term financial objectives" (Sec. V.A.1, p. 6).
- It argues existing PFM applications still depend on "restricted personalization, fixed budgetary arrangements, and limited proactive advice", which the IPFMS is aimed at addressing through dynamic budgets, real-time transaction detection and financial forecasting (Sec. V.A, p. 6).
- It flags that deep learning models can provide high predictive accuracy but "may be less transparent, which could be problematic when making financial decisions", motivating integrated explanatory AI methods (Sec. V.B.2, p. 7).
- It warns that AI risk systems trained on small or imbalanced datasets can reinforce existing financial biases and produce unfair or discriminatory suggestions (Sec. V.C, p. 7).
- Future development is said to aim at further AI integration, larger data sources to deepen analytical layers, and collaboration among system developers, financial institutions and end users (Sec. VI, p. 7).

## Key Figures and Tables

The paper contains no numbered tables and no results tables. Its three figures are architecture and conceptual diagrams, not data displays.

- Fig. 1 (p. 2): Architecture of the Intelligent Personal Finance Management (PFM) System → a schematic of the proposed system, not a results plot.
- Fig. 2 (p. 4): Evolution of Personal Finance Management (PFM) Systems → a historical/conceptual progression from manual bookkeeping to AI-assisted PFM, used to motivate the design.
- Fig. 3 (p. 4): System architecture of the proposed Intelligent Personal Finance Management System (IPFMS) → the layered microservices diagram that carries the paper's actual contribution.

There are no evaluation figures, no confusion matrices, no training curves, no usability plots and no comparative charts anywhere in the paper.

## Software

The paper names candidate technologies but reports no versions, configurations, hyperparameters or implementations. Nothing below was built or tested in the paper.

- Rule-based classifiers (version not reported) — first-pass expense categorization (Sec. III.C.1, p. 5)
- Logistic regression, random forests, lightweight neural networks (versions not reported) — supervised expense categorization (Sec. III.C.1, p. 5)
- Support Vector Machines, Random Forest models, neural networks (versions not reported) — Expense Categorization Module (Sec. III.A.3, p. 4)
- ARIMA, Prophet, LSTM neural networks (versions not reported) — income and spending forecasting (Sec. III.C.2, p. 5)
- Linear programming and genetic algorithms (versions not reported) — budget-resource calculation (Sec. III.C.2, p. 5)
- Reinforcement learning agents (version not reported) — long-term savings-policy discovery (Sec. III.C.2, p. 5; Sec. IV.B, p. 6)
- K-Means, DBSCAN, isolation forests (versions not reported) — anomaly detection (Sec. III.C.3, p. 5)
- Collaborative filtering and content-based recommendation (versions not reported) — Personalized Recommendation Engine (Sec. III.A.3, p. 4)
- Open Banking frameworks / Plaid (version not reported) — transaction data acquisition (Sec. III.A.1, p. 4)
- NoSQL plus relational data storage (products not reported) — Data Processing and Storage Layer (Sec. III.A.2, p. 4)
- Microservices architecture with DevOps and CI/CD pipelines (tools not reported) — deployment and maintainability (Sec. III.A, p. 3; Sec. V.B.3, p. 7)
- Encryption, tokenization, multi-factor authentication (products not reported) — security controls (Sec. V.B.1, p. 6)

## Definitions

- **IPFMS (Intelligent Personal Finance Management System)** — the paper's proposed system, integrating AI for intelligent budgeting and real-time expense tracking; also written IPFM in the abstract (Abstract, p. 1).
- **Smart budgeting** — budgeting that replaces strict spending constraints with flexible, customizable systems that react to user behaviour and money management, in contrast to fixed, manually created budgets (Sec. II.B, p. 2).
- **Real-time expense tracking** — the capability, normally delivered through secure connections to banks and credit cards, of automatically importing transaction information so the user has an instant picture of expenditure behaviour (Sec. II.C, p. 3).
- **AI and Analytics Engine** — the "core intelligence" of the system, comprising the Expense Categorization Module, Smart Budgeting Module, Anomaly Detection Module and Personalized Recommendation Engine (Sec. III.A.3, p. 4).
- **Expense Categorization Module** — uses SVM, Random Forest and neural networks on labelled transactions to classify expenses in real time, improving with user corrections (Sec. III.A.3, p. 4).
- **Smart Budgeting Module** — uses predictive analytics and optimization over past spending habits, income trends, user-defined finance targets and sometimes external economy indicators to produce individual budget recommendations (Sec. III.A.3, p. 4).
- **Anomaly Detection Module** — uses unsupervised clustering and isolation forests to identify irregular spending patterns and possible fraud, and notifies the user (Sec. III.A.3, p. 4).
- **Personalized Recommendation Engine** — uses collaborative filtering, content-based recommendation and rule-guided reasoning to recommend financial products, saving plans and investing options aligned to the user's profile and objectives (Sec. III.A.3, p. 4).
- **Financial well-being** — as quoted from the Consumer Financial Protection Bureau: the capacity to fulfil present and future budgetary requirements, confidence in a future, and the liberty to decide freely in life (Sec. I, p. 1).

## Limitations and Gaps

- The paper reports no evaluation of any kind for its own system. Section IV is headed "Result" but presents only projected effects ("is likely to have", "should enhance", "will have an alerting user"); no metric, baseline, dataset, user test or deployment is reported (Sec. IV, pp. 5-6).
- No sample size, dataset name, transaction count or participant count is given anywhere. Data collection is described only in the abstract as "aggregated and anonymized datasets of transactions" narrowed with "user-consented personal data", with no N and no source (Sec. III.B, p. 5).
- The authors acknowledge that AI in personal finance raises significant ethical and legal issues "that should be scrutinized in detail", naming algorithmic bias, privacy and trust, accountability for wrong advice, and human oversight (Sec. V.C, p. 7).
- The authors acknowledge that modern deep learning models may be less transparent, "which could be problematic when making financial decisions", and that explanatory AI methods are needed for trust (Sec. V.B.2, p. 7).
- The authors acknowledge that managing a system with several AI models adds complexity despite microservices scalability, requiring mature DevOps and CI/CD practice (Sec. V.B.3, p. 7).
- The authors acknowledge that significant technical and ethical issues remain, "especially with regard to issues of data protection, algorithmic fairness, as well as regulatory congruence" (Sec. VI, p. 7).
- [unacknowledged] Algorithm selection is left entirely open. The paper lists several candidate methods per task (e.g. logistic regression, random forests and lightweight neural networks for categorization) and states only that "the choice of specific algorithms will depend on the nature of the task and the characteristics of the data" (Sec. III.C, p. 5), so no reproducible model specification exists.
- [unacknowledged] No architecture is instantiated. Every technology is named without product, version or configuration — Open Banking or Plaid, NoSQL plus relational storage, encryption, tokenization, multi-factor authentication, DevOps and CI/CD pipelines (Sec. III.A and Sec. V.B, pp. 3-7) — so the design cannot be reproduced or assessed.
- [unacknowledged] The paper is a design proposal with no implementation, no deployment and no user study, yet Sections IV and V are written in the register of expected benefit ("Sustainable finance", "would encourage healthier financial habits", "would allow people to make more effective choices"), which reads as finding language without findings (Sec. V.A.1, p. 6; Sec. IV.D, p. 6).
- [unacknowledged] No Philippine data, population or setting is involved, and no geographic scope for the intended users is stated beyond the authors' Indian affiliation, so transferability to a Philippine household-finance context is untested.
- [unacknowledged] The literature review is largely non-systematic: references are single-conference and single-journal items cited in blocks ([1], [2], [5], [7], [9]) without comparison tables or extracted evidence, and Section II.D reports that Random Forest and SVM "will exhibit different levels of performance in different types of financial behavioral trends" (p. 3) without reporting any such comparison.
- [unacknowledged] Section I.B and Section I.C are near-duplicate text — both open with the claim that AI, specifically machine learning and deep learning, is becoming a more significant factor across industries with financial services among the most actively developing — so the introduction contains two overlapping subsections making the same argument (Sec. I.B and I.C, p. 2).
- [unacknowledged] The reference list carries 14 items but several are cited only as generic support for broad statements about privacy, ethics and robo-advising ([6], [7]), and no reference is used to justify a numeric or comparative claim.

## Statistical Evidence

Not reported. Section IV ("Result") presents only projected effects in modal language ("is likely to have a positive impact", "should enhance the capacity of the users to adhere to financial plans", "will have an alerting user"), Section V adds no numbers, and the paper prints no sample size, no dataset size, no metric, no confidence interval, no p-value and no test statistic anywhere in the body; the only numerals in the document are bibliographic and publishing artifacts (ISSN 2583-6129, Volume 05 Issue 04, Impact Factor 8.072 in the running footer, DOI 10.55041/ISJEM06330, and the 14 reference entries). There are no numbered tables in the paper and its three figures are architecture/concept diagrams, not data displays.

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Although the array of digital instruments meant to assist in managing finances is increasing, they do not always serve the actual needs of the users." | Sec. I Introduction, p. 1 | pfm_apps_problems |
| "Conventional Personal Finance Management Systems have been poor in offering personalized and actionable advice, which has left many people frustrated with financial planning and the attainment of long-term financial security." | Abstract, p. 1 | pfm_apps_problems |
| "Most of these applications are however limited and still represent a static image of financial health, and do not offer much support in depicting financial optimization through prediction, personalization, or real-time financial integration." | Sec. I.A, p. 1 | pfm_apps_problems |
| "Majority of the systems remained highly passive in their approach and the financial planning and interpretation was almost left to the user" | Sec. II.A, p. 2 | pfm_apps_problems |
| "Instead of using strict spending constraints, intelligent budgeting emphasizes developing flexible and custom budgeting systems that react to user behavior in terms of their money management" | Sec. II.B, p. 2 | budgeting |
| "This feature is normally done by having secure connections with financial powerhouses, including banks and credit cards, so that the transaction information is automatically imported" | Sec. II.C, p. 3 | income_expense_management |
| "Whereas many platforms initiate rule-based classification (to make the system manage common patterns of transactions), more complex systems are based on machine learning models that are refined with corrections made by users" | Sec. II.C, p. 3 | rule_based_classification |
| "This module uses supported machine learning methods, including Support Vector Machines, Random Forest models and neural networks, based on labeled dataset of transactions to automatically classify expenses on a real-time basis." | Sec. III.A.3, p. 4 | pfm_apps_features |
| "This component relies on predictive analytics and optimization methods to come up with individual budget recommendations." | Sec. III.A.3, p. 4 | pfm_apps_features |
| "The system is trained with aggregated and anonymized datasets of transactions in the first place, and further narrowed down with user-consented personal data to facilitate individualized recommendations." | Sec. III.B, p. 5 | data_collection |
| "Models like ARIMA, Prophet, and neural networks like LSTMs can be used to forecast future income and spending trends based on the time-series forecasting techniques." | Sec. III.C.2, p. 5 | pfm_apps_features |
| "These trends justify optimization tools, including linear programming and genetic algorithms, to calculate budget resources which can be used to meet user objectives and anticipated financial performance." | Sec. III.C.2, p. 5 | linear_programming |
| "The users would be in a higher position to make timely decisions instead of looking back on monthly reports, which would suit their budgets and financial targets." | Sec. V.A.1, p. 6 | pfm_apps_importance |
| "In order to secure sensitive financial data, the system will include powerful encryption tools, tokenization procedures and multi-factor authentication services." | Sec. V.B.1, p. 6 | system_development |
| "Risk AI systems that have been trained on small or imbalanced datasets can be used to strengthen the current financial biases, therefore, leading to unfair advice or even discriminatory suggestions." | Sec. V.C, p. 7 | pfm_apps_problems |
| "The proposed IPFMS is expected to simplify the financial planning process, enhance financial literacy, and improve financial well-being through offering individualized, proactive, and constantly adaptive guidance that can help with the financial planning." | Sec. VI Conclusion, p. 7 | pfm_apps_importance |

## Remember This

- The paper designs an IPFMS — a modular, microservices PFM system with an AI and Analytics Engine of four modules (categorization, smart budgeting, anomaly detection, recommendation) — but builds and evaluates nothing.
- Section IV is headed "Result" and reports no results: every effect is stated as projected ("is likely to have", "should enhance", "will have an alerting user").
- There is no sample size, no dataset name, no metric, no CI and no p-value anywhere in the paper. The Statistical Evidence section is correctly empty.
- Algorithm selection is explicitly deferred: "the choice of specific algorithms will depend on the nature of the task and the characteristics of the data" (Sec. III.C, p. 5).
- Candidate methods named, none implemented: SVM / Random Forest / neural networks for categorization; ARIMA / Prophet / LSTM for forecasting; linear programming and genetic algorithms for budget allocation; reinforcement learning for savings paths; K-Means / DBSCAN / isolation forests for anomalies.
- Security and compliance are named (PSD2, GDPR, CCPA; encryption, tokenization, MFA) but no product, version or configuration is given.
- The paper's own literature review concedes that current PFM applications remain passive and lack prediction, personalization and real-time integration — the gap the design claims to fill.
- Sections I.B and I.C are substantially duplicated text making the same argument about AI in financial planning.

## Cited Works

- Stefanov, T.; Stefanova, M.; Varbanova, S.; et al. (2024) (context) — Personal finance management application; cited for manual digital record-keeping, mobile expense tracking and financial summaries. [p. 1, p. 2]
- Althnian, A. (2021) (methodology) — Design of a rule-based personal finance management system based on financial well-being; cited for rule-based design and for restricted personalization in current applications. [p. 1, p. 6]
- Bunnell, L.; Osei-Bryson, K.-M.; Yoon, V. (2020) (context) — FinPathlight, a multiagent recommender framework to increase consumer financial capability; cited in the reference list but not discussed in the body. [p. 7]
- Kit, B. C. C.; Ghani, N. F. A. (2023) (methodology) — Designing an expert system for personal financial management; cited for rule-coded expert guidance and for reducing financial stress. [p. 3, p. 6]
- de Zarzà, I.; de Curtò, J.; Roig, G.; et al. (2023) (methodology) — Optimized financial planning integrating individual and cooperative budgeting models with LLM recommendations; cited for optimization-based budget planning and LLM-assisted budget drafting. [p. 2, p. 3, p. 6]
- Feng, R.; Li, H.; Liu, M. (2023) (context) — Robo-advisors beyond automation: principles and roadmap for AI-driven financial planning; cited for AI-enabled behavioural reading and accountability problems. [p. 2, p. 7]
- Pal, A.; Gopi, S.; Lee, K. M. (2023) (context) — Fintech agents: technologies and theories; cited for privacy, ethics, fairness and explainability concerns in AI financial systems. [p. 2, p. 3, p. 6, p. 7]
- Dey, S.; Arefin, M. S. (2025) (methodology) — Developing a rule-based system to recommend household budget; cited for automatic expense identification and spending-pattern prediction. [p. 2]
- Shah, A.; Raj, P.; Kumar, P.; et al. (2020) (methodology) — FinAID: a financial advisor application using AI; cited for automated transaction import, automated categorization and model selection across user groups. [p. 3]
- Tolani, K.; Shukla, J. V.; Mohare, R.; et al. (2025) (methodology) — Machine learning analysis of financial behavior: Gen Y and Gen Z preferences; cited for reinforcement-learning savings strategies. [p. 3]
- Phadale, K. S. (2024) (methodology) — BudgetBliss: predictive budget planning using neural networks and socioeconomic factors; cited for neural-network predictive budget planning. [p. 3]
- Avacharmal, R.; Balakrishnan, A. V.; Ranjan, P.; et al. (2024) (methodology) — Leveraging reinforcement learning for advanced financial planning and personalization in economic forecasting and savings strategies; cited for reinforcement learning, savings outcomes and ontology-based multi-agent recommenders. [p. 3, p. 6]
- Mohammed, S.; Bealer, R.; Cohen, J. (2021) (context) — Vanguard reinforcement learning for financial goal planning; listed in the reference list but not discussed in the body. [p. 8]
- Theerthala, A. (2025) (context) — Synthesizing behaviorally-grounded reasoning chains: a data-generation framework for personal finance LLMs; listed in the reference list but not discussed in the body. [p. 8]

```text
CLAIM AUDIT
1. [PARTIAL] Digital tools now organize a user's income, transactions, expenses, savings goals, and debt obligations in one place, and analytical components can use that information to estimate future expenses and help users allocate their funds (Yadav et al., 2026; D'Souza et al., 2026).
Locator: The paper describes these as design intentions of a system that was never built or tested, not as an established present-tense property of digital tools. What it does say: the proposed IPFMS "is able to aggregate real-time financial transaction data to provide a real-time snapshot of financial conditions" (Abstract, p. 1); its Data Processing and Storage Layer maintains "User profiles, defined financial goals as well as past spending records" (Sec. III.A.2, p. 4); the Personalized Recommendation Engine covers "debt management, investment planning and how to prepare to a big event in life" (Sec. IV.C, p. 6); and predictive capability "enable[s] individuals to estimate the financial needs in the future and possible deficit so as to plan in advance on how to spend or save money" (Sec. IV.B, pp. 5-6). However the paper's own review says existing tools do not do this — "Most of these applications are however limited and still represent a static image of financial health, and do not offer much support in depicting financial optimization through prediction, personalization, or real-time financial integration" (Sec. I.A, p. 1) — and every capability is stated in projected rather than demonstrated form, with no implementation, deployment or evaluation reported.
```