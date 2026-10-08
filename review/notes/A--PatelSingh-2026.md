---
paper_id: A--PatelSingh-2026
first_author: Patel
year: 2026
title: "An Intelligent AI-Based Framework for Automated Personal Financial Management"
venue: "International Conference on Multidisciplinary Perspectives in Advanced Computing and Technology (IMPACT 2026), G. B. Pant University of Agriculture and Technology"
doi: Not reported
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, rule_based_classification, model_algorithm_integration, data_collection, system_development, software_quality_evaluation]
module_rationale:
  financial_planning: "The paper frames personal finance management as analysing spending patterns, predicting future expenses and providing recommendations, and treats budgeting and expense prediction as core planning functions (Abstract, p. 774; Sec. 2B Objectives, p. 776)."
  budgeting: "The budgeting module analyses previous spending behaviour to generate personalised budget limits and alerts when thresholds are approached (Sec. 5 Results, p. 779; Table 1, p. 778)."
  savings_debt_management: "The system advises users on better savings habits and lists debt management as a future platform feature (Sec. 5 Results, p. 779; Sec. 6 Conclusion, p. 782)."
  income_expense_management: "The system records and categorises inflows and outflows across UPI, online banking and digital wallets into a unified interface (Sec. 5 Results, p. 779; Table 1, p. 778)."
  pfm_apps_overview: "The literature review characterises early personal finance tools as manual-entry and static-reporting applications (Sec. 3 Literature Review, p. 776)."
  pfm_apps_features: "The paper enumerates dashboards, savings goals, budgeting tools, real-time alerts, reports and expense forecasts as the system's feature set (Abstract, p. 774; Sec. 5 Results, p. 779)."
  pfm_apps_problems: "The introduction and problem statement identify limited intelligence, automation and personalisation, and the absence of predictive insight, as defects of current applications (Sec. 1, p. 774; Sec. 2A, p. 775)."
  pfm_apps_importance: "The Discussion claims the platform enhances the efficiency of personal financial management and improves financial awareness, though no outcome evidence is reported (Sec. 6 Discussion, p. 781)."
  rule_based_classification: "Transactions are categorised by rule-based logic applied to merchant names and transaction descriptions, in combination with ML classification (Table 1, p. 778; Sec. 3, p. 776)."
  model_algorithm_integration: "The system combines rule-based reasoning with machine learning in a single categorisation and insight pipeline (Abstract, p. 774; Sec. 4 Data Processing and AI Integration, p. 777)."
  data_collection: "Financial transaction data is gathered from UPI and banking records through APIs and secure data ingestion, and evaluation uses sample financial datasets (Table 1, p. 778; Sec. 4 Evaluation Approach, p. 778)."
  system_development: "A layered full-stack architecture with frontend, backend, database, AI services and event-driven background processing is described as the implementation approach (Sec. 4 System Design, p. 777)."
  software_quality_evaluation: "The stated evaluation approach covers responsiveness, accuracy of AI-generated insights, reliability of background tasks and general usability, with no instrument named (Sec. 4 Evaluation Approach, p. 778)."
---

# A--PatelSingh-2026 — An Intelligent AI-Based Framework for Automated Personal Financial Management

## Summary

Patel and Singh propose an AI-based personal finance management framework that aggregates scattered financial data from UPI payments, online banking, digital wallets and subscription platforms into a single platform, automatically categorises transactions, generates personalised budgets, issues real-time spending alerts, and produces forecasts and recommendations through interactive dashboards. The paper is a system-architecture and functional-component description rather than an empirical evaluation: it sets out a layered full-stack architecture, a phase-by-phase methodology table, and a qualitative comparison of the proposed system against "traditional financial tools" and "manual / rule-based only" approaches. The claimed advantages are high categorisation accuracy and adaptability, reduced manual effort, multi-source data aggregation, dynamic budgeting, real-time notifications, expense prediction, interactive dashboards, higher user engagement, AI-driven recommendations and better decision support (Table 2, p. 780). None of these advantages is accompanied by a measured value, a sample size, a baseline figure, a confidence interval or a significance test. The paper's conclusion describes the system partly in the future tense and lists direct bank API–UPI gateway integration, deep learning, investment analysis, credit score evaluation, debt management, NLP, blockchain and a cross-platform mobile deployment as work still to come (Sec. 6 Conclusion, pp. 781–782), so the reported "system" is best read as a proposed design whose evaluation has not yet been carried out. For this project's purposes the paper is useful as an articulation of the problem space and of the feature set a PFM application is expected to provide, and as a statement of what current applications lack; it supplies no outcome statistics at all.

## Problem and Motivation

The paper's motivating claim is that the digitisation of financial services — UPI, online banking, digital wallets, e-commerce and subscriptions — has produced "an enormous amount of scattered financial data for an individual" (Abstract, p. 774), and that handling this data manually is inefficient and undermines financial awareness and decision-making. Several specific problems are named: manual tracking "takes a lot of time, is prone to errors, and is often overlooked, resulting in a lack of financial awareness" (Sec. 1, p. 774); current applications "mainly focus on simple expense logging and reporting, offering limited intelligence, automation, and personalisation" (Sec. 1, p. 774); the data "remains highly fragmented across multiple platforms, making it difficult for users to track expenses, manage budgets, and analyse financial behaviour effectively" (Sec. 2A, p. 775); and "most solutions lack automated transaction categorisation, real-time analytics, personalised recommendations, and predictive financial insights" (Sec. 2A, p. 775). The authors locate the consequence in "poor financial awareness, overspending, and inefficient decision-making due to a lack of intelligent financial management tools" (Sec. 2A, p. 775), and identify the affected population as "young professionals and students who often use multiple digital payment platforms but lack structured financial planning" (Sec. 1, p. 774). The literature review reinforces these claims by tracing the trajectory from manual spreadsheet trackers with "high user drop-off rates" (Sec. 3, p. 776), through rule-based categorisation that "was not adaptable and faced difficulty with ambiguous or unseen patterns of transactions" (Sec. 3, p. 776), to machine-learning classifiers that "require a large amount of labelled data and periodic retraining" (Sec. 3, p. 776). The stated gap is "an integrated personal finance management system that incorporates automated data aggregation, intelligent analytics, personalized recommendations, and user-friendly visualization" with scalability and security at "minimum manual effort" (Sec. 3, p. 777). The paper's objectives follow directly: minimise manual expense-tracking effort, aggregate data across payment sources, automate categorisation with rule-based logic and machine learning, provide real-time visual analytics, support budgeting and expense prediction from historical data, deliver personalised recommendations and alerts, and store sensitive information securely (Sec. 2B, pp. 775–776).

## Method

**Design.** The authors state no formal research-design label. The paper describes itself as adopting "a modular full-stack methodology, integrated with artificial intelligence, for automating personal financial management" (Sec. 4, p. 777); its structure is a system-architecture and functional-component description supported by a phase table and two screen-level figures, with no controlled comparison or field trial.
**Sample.** Not reported. The paper reports no N and no unit of analysis; it states only that the system "was tested to assess its effectiveness" (Sec. 5, p. 779) and that evaluation is "based on sample financial datasets" (Sec. 4 Evaluation Approach, p. 778), without naming a dataset, a record count, a participant count, or any sampling frame.
**Context.** geography: India — the authors are affiliated with Galgotias College of Engineering and Technology, Greater Noida, and the paper's motivating payment infrastructure is India's Unified Payments Interface (pp. 774, 775); population: users of digital payment platforms, with the affected group identified as "young professionals and students who often use multiple digital payment platforms but lack structured financial planning" (Sec. 1, p. 774); setting: a proposed full-stack web platform with frontend, backend, relational database, AI services and background processing (Sec. 4, p. 777); no deployment, no live user study and no institutional evaluation is described.

The method proceeds in four stated parts. First, **system design**: "A layered architecture is followed, where the layers include frontend, backend, database, AI services, and background processing," which is said to enable scalability, maintainability and real-time or asynchronous operation (Sec. 4, p. 777). Second, **data processing and AI integration**: "User financial data is then securely collected, validated, and stored in a relational database," and preprocessed transaction data "is fed into an AI model to conduct automated categorization and draw financial insights that are later visualized through dashboards" (Sec. 4, p. 777). Third, **background processing and security**: "Event-driven background workflows run periodic financial reports without affecting the user experience," with authentication, authorisation and rate limiting implemented for privacy and reliability (Sec. 4, pp. 777–778). Fourth, **evaluation approach**: the system "is evaluated for responsiveness, accuracy of AI-generated insights, reliability of background tasks, and general usability based on sample financial datasets" (Sec. 4, p. 778).

Table 1 (p. 778) lays the workflow out as six phases with their tools: Data Collection from UPI and banking records via "APIs, Secure Data Ingestion"; Data Cleaning and Preprocessing for normalisation; Transaction Categorization into categories "like food, travel, bills, etc." using "Rule-Based Logic, ML Classification"; Data Analysis using "Statistical Analysis, Pattern Recognition"; Budget Planning from historical data analysis; and Visualization via dashboard tools. The Results section (Sec. 5, pp. 779–780) then narrates five qualitative findings — automated transaction categories, cost accounting and data integration, budget planning and alerts, predictive insights and recommendations, and user experience and financial awareness — with Table 2 (p. 780) presenting an eight-row qualitative comparison across "Traditional financial tools", "Manual / Rulebased only" and the "Proposed System", and Figures 1 and 2 showing a monthly expense breakdown by category and an income-and-expense dashboard. The Discussion (Sec. 6, p. 781) argues that modularity supports scalability, that background execution protects real-time interaction, and that the system is "constrained by the quality of input data and the reliability of third-party AI services".

## Software

- Full-stack layered web architecture: frontend, backend, relational database, AI services, background processing (Sec. 4, p. 777)
- Relational database for validated transaction data (Sec. 4, p. 777)
- Rule-based logic for transaction categorisation (Table 1, p. 778)
- Machine-learning classification for transaction categorisation (Table 1, p. 778; Sec. 3, p. 776)
- Statistical analysis and pattern recognition for spending-pattern detection (Table 1, p. 778)
- Data visualisation tools for dashboards and charts (Table 1, p. 778)
- Event-driven background workflow engine for periodic reports (Sec. 4, p. 777)
- Authentication, authorisation and rate limiting for data privacy and system reliability (Sec. 4, pp. 777–778)
- Third-party AI services (named only as an external dependency; no vendor or version reported) (Sec. 6, p. 781)
- Frameworks, libraries, language, database product and versions: Not reported

## Key Findings

- The system is claimed to categorise transactions from UPI payments, online banking accounts and digital wallets effectively, with "AI-driven classification and logic rules" said to enhance accuracy over manual procedures and to overcome confusing merchant names (Sec. 5, p. 779).
- The system is claimed to aggregate financial information from multiple platforms "into a unified interface" and to give users real-time access to aggregated expense information, removing the need to manage expenses across several applications and preventing manual entries (Sec. 5, p. 779).
- The budgeting module is claimed to analyse previous spending behaviour to generate personalised budget limits, and alert notifications are said to fire when a predefined threshold is approached or exceeded (Sec. 5, p. 779).
- The predictive component is claimed to offer expenditure trends and forecasts of future expenditure from past expenditure, and recommendations are said to be personalised and to advise on better savings habits (Sec. 5, p. 779).
- Users are described as pleased with "enhanced financial understanding facilitated by engaging graphics and simplified financial statements", and the dashboard is said to make expense allocation easy to comprehend (Sec. 5, p. 780).
- Table 2 (p. 780) asserts the proposed system delivers "High accuracy & adaptability", "Reduced manual efforts", a "Unified financial view", "Improved budget control", "Better overspending control", "Enhanced financial planning", "Improved user understanding", "Increased financial awareness" and "Better financial decisions" — all without an accompanying measured value.
- No quantitative result, sample size, baseline figure, confidence interval, p-value or effect size is reported anywhere in the paper.
- The Conclusion states the system "will incorporate financial information from various sources" and lists deployment "as a cross-platform mobile application and tested at scale with various users" as a future step, indicating that the reported evaluation is prospective rather than completed (Sec. 6 Conclusion, pp. 781–782).

## Key Figures and Tables

- Fig. 1 (p. 779): Monthly Expense Breakdown by Category in this system — a category-level view of monthly spending produced by the system; the paper prints no underlying values or axis figures in the text.
- Fig. 2 (p. 780): Income and Expense Analysis Dashboard Generated by this system — the income-and-expense dashboard; again, no numeric values are reported alongside it.
- Table 1 (p. 778): Methodology — six phases (Data Collection, Data Cleaning/Preprocessing, Transaction Categorization, Data Analysis, Budget Planning, Visualization) mapped to descriptions and tools (APIs/Secure Data Ingestion; Normalization; Rule-Based Logic, ML Classification; Statistical Analysis, Pattern Recognition; Historical Data Analysis; Data Visualisation Tools).
- Table 2 (p. 780): Result Analysis — eight parameters (Transaction Categorization, Expense Tracking, Data Aggregation, Budget Planning, Real-time alerts, Predictive analysis, Data Visualization, User Engagement, Decision Support) compared across Traditional financial tools, Manual / Rulebased only, and the Proposed System, with a "Performance Improvement" column of narrative claims and cited references. Every improvement claim is qualitative; no cell contains a measured value.

## Definitions

- **Personal finance management system** — the paper's object of design: a platform that aggregates financial data from multiple sources, automatically categorises transactions, and delivers insights through interactive dashboards and analytics (Sec. 1, p. 775).
- **Transaction categorisation** — the automatic classification of transactions into categories "like food, travel, bills, etc." by rule-based logic and machine-learning classification (Table 1, p. 778).
- **Rule-based logic** — deterministic classification built from merchant names, transaction descriptions and predefined keywords; the paper notes it "was not adaptable and faced difficulty with ambiguous or unseen patterns of transactions" (Sec. 3, p. 776).
- **Predictive insights** — expenditure trends and forecasts of future expenditure derived from past expenditure (Sec. 5, p. 779).
- **Personalised budget** — a spending limit generated from the user's historical spending behaviour rather than a static ceiling (Sec. 5, p. 779; Table 1, p. 778).
- **Real-time alerts** — notifications issued when spending approaches or exceeds a predefined threshold (Sec. 5, p. 779).
- **Layered architecture** — the system's structure of frontend, backend, database, AI services and background processing layers (Sec. 4, p. 777).
- **Background processing** — event-driven workflows that run periodic financial reports without affecting the user experience (Sec. 4, p. 777).
- **UPI** — Unified Payments Interface, the Indian digital payment rail named as a primary data source and as a target for future bank API integration (Abstract, p. 774; Sec. 6 Conclusion, p. 782).

## Limitations and Gaps

- [unacknowledged] The paper reports **no outcome statistics of any kind**. Section 5 (pp. 779–780) and Table 2 (p. 780) present only narrative descriptors — "High accuracy & adaptability", "Reduced manual efforts", "Unified financial view" — with no accuracy figure, no error rate, no baseline number, no confidence interval and no p-value; Figures 1 and 2 are presented without accompanying values.
- [unacknowledged] The paper reports **no sample**. Neither the number of transactions, the number of records, the number of users, nor the identity of the "sample financial datasets" used for evaluation is stated (Sec. 4 Evaluation Approach, p. 778; Sec. 5, p. 779). The claim that the system "was tested" cannot be assessed without it.
- [unacknowledged] The comparison in Table 2 (p. 780) is against "Traditional financial tools" and "Manual / Rulebased only" as unnamed categories, not against identified systems, and the "Performance Improvement" column contains assertions rather than measurements, so no claim of superiority is supported.
- [unacknowledged] The stated evaluation covers "responsiveness, accuracy of AI-generated insights, reliability of background tasks, and general usability" (Sec. 4, p. 778), but no instrument, scale, protocol or result is reported for any of the four; no usability questionnaire, no SUS score and no ISO/IEC 25010 mapping appears.
- [unacknowledged] The paper's tense contradicts its own results claims. Section 5 reports the system's performance in the past tense ("The system performed effectively", p. 779) while the Conclusion describes the system in the future tense — "the emerging system will incorporate financial information from various sources" — and lists deployment and large-scale user testing as future work (Sec. 6 Conclusion, pp. 781–782). The evaluation therefore appears prospective, not completed.
- [unacknowledged] The system is described as relying on "third-party AI services" (Sec. 6, p. 781) whose identity, version and behaviour are not reported, so the categorisation and forecasting components are not reproducible.
- [unacknowledged] The paper states no model, no feature set, no training procedure, no labelled dataset and no retraining policy for its machine-learning component, although the literature review itself notes that ML classifiers "require a large amount of labelled data and periodic retraining" (Sec. 3, p. 776).
- [unacknowledged] The reference list does not support several of the citations it is attached to — reference [1], cited throughout for personal finance management claims, is Grass and Lynch (1982), a printing-resources cost workshop (References, p. 782) — so the paper's evidential base for its background claims is unreliable.
- [acknowledged] The authors state the system "offers meaningful AI-driven insights, but it is constrained by the quality of input data and the reliability of third-party AI services" (Sec. 6 Discussion, p. 781).
- [acknowledged] The authors list future work rather than reporting it: direct bank API–UPI gateway integration for real-time transaction synchronisation without manual uploads; deep learning for expense-forecasting accuracy and financial recommendations; investment analysis, credit score evaluation and debt management features; natural language processing for financial-assistant queries; blockchain and enhanced encryption for data security; and cross-platform mobile deployment tested at scale with various users (Sec. 6 Conclusion, pp. 781–782).
- [unacknowledged] No privacy mechanism is evaluated. The paper asserts that authentication, authorisation and rate limiting ensure data privacy and system reliability (Sec. 4, pp. 777–778) but reports no threat model, no privacy analysis and no security test.
- [unacknowledged] The literature review's limitation claims — high user drop-off in manual tools, non-adaptability of rule-based categorisation, labelled-data requirements of ML classifiers — are stated without reported effect sizes, sample sizes or citations that the reference list verifies.

## Statistical Evidence

Not reported. The Results section (Sec. 5, pp. 779–780) and Table 2 (p. 780) report only qualitative descriptors ("High accuracy & adaptability", "Reduced manual efforts", "Unified financial view") with no numeric value, confidence interval, p-value or effect size printed anywhere in the paper; the two figures (Figs. 1 and 2, pp. 779–780) are reproduced without accompanying statistics, and the Methodology and Evaluation Approach sections (Sec. 4, pp. 777–778) state what will be evaluated without reporting a sample, an instrument or a result.

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The system aggregates financial information from multiple sources and automatically classifies transactions into categories." | Abstract, p. 774 | pfm_apps_features |
| "It utilises rule-based reasoning and machine learning algorithms to identify spending habits, forecast future expenditures, and provide financial recommendations to users." | Abstract, p. 774 | model_algorithm_integration |
| "Current personal finance applications mainly focus on simple expense logging and reporting, offering limited intelligence, automation, and personalisation" | Sec. 1 Introduction, p. 774 | pfm_apps_problems |
| "Most solutions lack automated transaction categorisation, real-time analytics, personalised recommendations, and predictive financial insights" | Sec. 2A Problem Statement, p. 775 | pfm_apps_problems |
| "Most people depend on manual methods or basic finance apps to manage their expenses and budgets" | Sec. 1 Introduction, p. 774 | income_expense_management |
| "Good financial management involves not just recording transactions but also analysing spending patterns, predicting future expenses, and providing useful recommendations" | Sec. 1 Introduction, p. 774 | financial_planning |
| "Traditional personal finance management tools relied heavily on manual data entry and static reporting mechanisms" | Sec. 3 Literature Review, p. 776 | pfm_apps_overview |
| "simple static budget limits cannot capture the heterogeneity in user spending behaviours" | Sec. 3 Literature Review, p. 776 | budgeting |
| "Transactions are automatically classified into categories like food, travel, bills, etc." | Table 1, p. 778 | rule_based_classification |
| "A layered architecture is followed, where the layers include frontend, backend, database, AI services, and background processing" | Sec. 4 System Design, p. 777 | system_development |
| "User financial data is then securely collected, validated, and stored in a relational database." | Sec. 4 Data Processing and AI Integration, p. 777 | data_collection |
| "The system is evaluated for responsiveness, accuracy of AI-generated insights, reliability of background tasks, and general usability based on sample financial datasets" | Sec. 4 Evaluation Approach, p. 778 | software_quality_evaluation |
| "The system offered relevant insights such as expenditure trends and forecasts for future expenditures based on past expenditures" | Sec. 5 Results, p. 779 | pfm_apps_features |
| "The recommendations were personalized, and people were advised on how to make better savings habits" | Sec. 5 Results, p. 779 | savings_debt_management |
| "The proposed AI-enabled personal finance management platform proves that integrating AI with modern full-stack web technologies significantly enhances the efficiency of personal financial management" | Sec. 6 Discussion, p. 781 | pfm_apps_importance |
| "This system offers meaningful AI-driven insights, but it is constrained by the quality of input data and the reliability of third-party AI services" | Sec. 6 Discussion, p. 781 | pfm_apps_problems |
| "Although it is an all-encompassing solution for personal finance management, there are some areas where it can be improved." | Sec. 6 Conclusion, p. 782 | pfm_apps_problems |
| "Lastly, to assess system performance and effectiveness, it can be deployed as a cross-platform mobile application and tested at scale with various users." | Sec. 6 Conclusion, p. 782 | software_quality_evaluation |

## Remember This

- The paper is a system-architecture and feature description of an AI-based PFM framework; it reports no outcome statistics, no sample and no statistical test.
- Its evaluation claim rests entirely on a qualitative Table 2 (p. 780) comparing the proposed system against unnamed "Traditional financial tools" and "Manual / Rulebased only".
- The stated evaluation dimensions are responsiveness, accuracy of AI-generated insights, reliability of background tasks and general usability — none is instrumented or reported (Sec. 4, p. 778).
- The Conclusion is written prospectively and lists bank API integration, deep learning, investment analysis, credit score, debt management, NLP, blockchain and mobile deployment as future work (pp. 781–782), indicating the evaluation is not yet done.
- Its usable contribution to this project is the problem framing and the feature list — aggregation, categorisation, budgeting, alerts, forecasting, dashboards — not evidence about any of them.

## Cited Works

- Grass, M.; Lynch, P. A. (1982) (context) — Printing Resources Management Information Systems Cost and Financial Workshop proceedings; cited throughout for personal finance management claims. [p. 782]
- Naik, S. L.; Kumar, G. R.; Kiran, A.; Ganesh, D.; Madgi, M. (2024) (methodology) — Exploration of automatic expense tracking systems; cited for rule-based logic and ML classification of transactions. [p. 782]
- Stefanov, T.; Stefanova, M.; Varbanova, S.; Temelkov, S. (2024) (context) — Personal finance management application published in TEM Journal 13(3), 2066. [p. 782]
- Fernández, A. (2019) (context) — Artificial intelligence in financial services, Banco de España. [p. 782]
- Harshitha, G. M.; Kumar, P.; Rakshitha, M. (2025) (methodology) — AI-driven financial insights for personal budget planning and future expense prediction; cited for budgeting and expense prediction. [p. 782]
- Zhang, S. (2025) (methodology) — Big-data-driven financial analysis and decision support system design, Informatica 49(11); cited for pattern recognition and real-time analytics. [p. 782]
- Hastie, T.; Tibshirani, R.; Friedman, J. (2017) (methodology) — The Elements of Statistical Learning, 2nd ed.; cited for machine-learning classification. [p. 782]
- Goodfellow, I.; Bengio, Y.; Courville, A. (2016) (methodology) — Deep learning, MIT Press; cited for AI in financial decision-making. [p. 782]
- Kapoor, S.; Prosad, J. M. (2017) (context) — Behavioural finance review, Procedia Computer Science 122, 50–54. [p. 783]
- Laudon, K. C.; Laudon, J. P. (2004) (context) — Management information systems: managing the digital firm. [p. 783]
- Russell, S.; Norvig, P. (1995) (context) — Artificial intelligence: a modern approach. [p. 783]
- Du, C. (2024) (methodology) — Intelligent financial management system based on data mining technology, Procedia Computer Science 243, 1079–1088. [p. 783]
- Mombeuil, C. (2020) (context) — Factors affecting renewed adoption of mobile wallets, Journal of Retailing and Consumer Services 55, 102127. [p. 783]
- Makridakis, S.; Spiliotis, E.; Assimakopoulos, V. (2018) (methodology) — Statistical and machine learning forecasting methods, PLoS ONE 13(3), e0194889; cited for time-series expense forecasting. [p. 783]
- Sutton, R. S.; Barto, A. G. (1998) (context) — Reinforcement learning: an introduction; cited for data privacy and explainability concerns. [p. 783]
- Ahmed, S. (2025) (context) — Implementation of advanced encryption techniques to protect sensitive financial data; cited for security and rate limiting. [p. 783]
- Vermani, R.; Arora, N. (2025) (context) — Role of Unified Payments Interface (UPI) in digital inclusion. [p. 783]
- Hand, D. J. (2007) (methodology) — Principles of data mining, Drug Safety 30(7), 621–622; cited for data cleaning and normalisation. [p. 783]
- Han, J.; Kamber, M.; Pei, J. (2012) (methodology) — Data mining: concepts and techniques; cited for ambiguous transaction patterns and third-party AI reliability. [p. 783]
- Whitetaker, K. (2025) (context) — Role of big data analytics in behavioural finance: consumer spending and saving, SSRN 5413835. [p. 783]