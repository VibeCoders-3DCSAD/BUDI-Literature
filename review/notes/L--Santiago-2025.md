---
paper_id: L--Santiago-2025
first_author: "Santiago"
year: 2025
title: "Budget and Financial Management Information System for Public Elementary Schools: Analytics and Predictive Insights for MOOE Allocation Using Linear Regression"
venue: "International Journal of Advanced Research in Computer Science, 16(3), 128-137"
doi: 10.26483/ijarcs.v16i3.7256
type: journal-article
designation: local
status: extracted
modules: [budgeting, income_expense_management, model_algorithm_integration, model_performance_evaluation, development_methodology, data_collection, system_development, software_quality_evaluation]
module_rationale:
  budgeting: "Sec. I and Sec. V.B develop the Budget Allocation Module for automated MOOE budget creation and next-year allocation, and Fig. 6/Fig. 10 show budget entry and actual-versus-predicted allocation per category."
  income_expense_management: "Sec. V.B and Fig. 7/Fig. 9 document the Expenditure Tracker recording individual expense entries by category, budget, actual spending and percentage used, filtered and updated per project and fiscal year."
  model_algorithm_integration: "Sec. IV.A wires a Python/Scikit-learn linear-regression analytics component into a PHP/MySQL BFMIS through JSON, so predicted MOOE values populate budget, variance-analysis and DepEd-compliant report modules (Table 3)."
  model_performance_evaluation: "Table 4 (p. 134) reports the model's MAE of ₱1,532.75, RMSE of ₱2,126.84 and R² of 0.9281 for MOOE allocation forecasting."
  development_methodology: "Sec. I.B argues Agile as the theoretical framework and Sec. IV.A commits the build to the Agile Development Methodology with planning, designing, building and testing sprints (Fig. 1, Fig. 4)."
  data_collection: "Sec. IV.A specifies the population, purposive sampling, document analysis of Pook Elementary School 2022-2024 MOOE records, structured interviews and an expert-validated TAM survey instrument (Table 1)."
  system_development: "Sec. IV.A names the implementation stack (XAMPP, Apache, MySQL, PHP, Python, Scikit-learn, DomPDF, PhpSpreadsheet, Chart.js, JSON) and Sec. I.C records lack of cloud support as a system limitation."
  software_quality_evaluation: "Sec. IV.B and Sec. V.B evaluate the built system by 37 black-box test cases, compliance testing against ISO/IEC 25010 and ISO 27001, and TAM-based user acceptance testing (Table 2, Table 5)."
---

# Budget and Financial Management Information System for Public Elementary Schools: Analytics and Predictive Insights for MOOE Allocation Using Linear Regression

`L--Santiago-2025` — Santiago (2025), *International Journal of Advanced Research in Computer Science, 16(3), 128-137* \[10.26483/ijarcs.v16i3.7256]

## Summary

A Philippine Budget and Financial Management Information System built on Agile integrates linear-regression analytics into school budgeting for public elementary schools, forecasting next year's MOOE allocation at R² = 0.9281 with MAE of ₱1,532.75 and RMSE of ₱2,126.84.

## Problem and Motivation

Public elementary schools in the Philippines manage Maintenance and Other Operating Expenses (MOOE) without a dedicated financial management system, so manual processes produce errors, inconsistent records, and difficulty tracking expenditures. Those errors compromise transparency, accountability, and compliance with Department of Education financial regulations. The authors position predictive analytics over historical spending patterns as the means of automating budget planning and improving resource utilization.

## Method

**Design.** Descriptive-developmental research design (the paper's own label, Sec. IV.A, p. 131): a descriptive analysis of current MOOE practice plus a developmental design-and-implementation study of the BFMIS.
**Sample.** A purposive sample of at least 30 participants — school heads, financial officers and DepEd auditors from selected public elementary schools under Laguna's Schools Division Office; the exact realised count is Not reported. The predictive model is fitted to Pook Elementary School 2022–2024 MOOE records.
**Context.** geography: Philippines — public elementary schools under Laguna's Schools Division Office, Laguna; population: school heads, financial officers and DepEd auditors responsible for school financial management; setting: institutional school budgeting in a DepEd knowledge-management web system, plus black-box and TAM acceptance testing with IT professionals as testers.

- Adopt the descriptive-developmental design: the descriptive part analyses current MOOE practice in public elementary schools, the developmental part designs and implements BFMIS with AI-driven linear regression (Sec. IV.A, p. 131).
- Draw the population from school heads, financial officers and DepEd auditors under Laguna's Schools Division Office, taking a purposive sample of at least 30 participants directly involved in financial management (Sec. IV.A, p. 131).
- Combine document analysis of Pook Elementary School 2022–2024 MOOE records, structured interviews with administrators and financial officers, and a TAM-based survey (Sec. IV.A, p. 131).
- Validate the TAM questionnaire with information systems experts, then analyse survey data with descriptive statistics — frequencies, percentages, means and standard deviations (Sec. IV.A, p. 131).
- Test the AI component's accuracy in forecasting MOOE allocation by regression analysis, reporting MAE, RMSE and R² score (Sec. IV.A and Sec. V.B, pp. 131, 134).
- Build the system on the Agile Development Methodology, each sprint covering planning, designing, building and testing, prioritising compliance, accuracy and predictive analytics (Sec. IV.A, p. 131; Fig. 4).
- Implement on XAMPP with PHP and MySQL for entry and storage, Python with Scikit-learn for predictive analytics, JSON for exchange, and DomPDF and PhpSpreadsheet for reporting (Sec. IV.A, pp. 131–132).
- Run black-box testing using equivalence partitioning across the system modules, following the 3–5 test case guideline of Pressman and Maxim (2014) (Sec. V.B, p. 132; Table 2).
- Run usability testing, ISO compliance testing against ISO/IEC 25010 and ISO 27001, and TAM-based User Acceptance Testing with administrators, financial officers and auditors (Sec. IV.B, p. 132).
- Produce a five-phase implementation plan from June 2025 to December 2026 covering pilot rollout, training, stakeholder roles, risk management and DepEd platform integration (Sec. V.B, p. 135; Fig. 11).

## Software

- XAMPP (version not reported) — local server environment providing Apache, MySQL and PHP
- PHP (version not reported) — dynamic web pages, user authentication, budget and expense tracking
- MySQL (version not reported) — relational database for MOOE data
- Python (version not reported) — predictive analytics
- Scikit-learn (version not reported) — built and validated the regression models
- DomPDF (version not reported) — PDF report generation
- PhpSpreadsheet (version not reported) — Excel report export
- Chart.js (version not reported) — budget visualisation module
- JSON — data exchange between the Python analytics and the PHP front end

## Key Findings

- num: Table 4 reports the linear regression model's MAE of ₱1,532.75, RMSE of ₱2,126.84 and R² score of 0.9281 for MOOE allocation forecasting; the narrative states the same fit as an R² value of 92.81% of variance explained.
- num: Predicted next-cycle MOOE increases were reported at +9.83% for Electricity and +66.67% for Fidelity Bond, with ICT Program predictions showing minimal variance (Sec. V.B, p. 134).
- num: Black-box testing comprised 37 test cases (TC001–TC037) across nine modules, against a per-module guideline of 3–5 cases (Table 2, p. 132).
- num: One tester reported four failures — UI responsiveness (TC010), missing field validation (TC012), incorrect feedback for over-budget entries (TC017), and display issues at zero budget (TC020) (Sec. V.B, p. 135).
- num: Table 5 reports weighted means of 4.62 for System Quality, 4.61 for Ease of Use, 4.51 for Perceived Usefulness, 4.51 for System Features and Functionality, and 4.51 for User Satisfaction and Acceptance.
- num: Sec. VI.A instead summarises the same five areas as System Quality (4.47), Ease of Use (4.46), Usefulness (4.37), Features (4.37) and Satisfaction (4.37) on a 5-point scale.
- num: Standard deviations across all user acceptance categories ranged from 0.47 to 0.62, indicating consistent agreement among respondents (Sec. V.B, p. 135).
- num: The highest-rated user acceptance criterion was secure user role and password protection (Mean = 4.70), and the dashboard-clarity item was rated 4.67 (Sec. V.B, p. 135).
- num: The expense report covers MOOE categories from January 1 to May 15, 2025, with 100% spending in the Graduation Program indicating full budget use (Sec. V.B, p. 133).
- num: The questionnaire instrument was validated by experts with a validity mean of Not reported and validated against ISO/IEC 25010 (software quality) and ISO 27001 (security).

## Key Figures and Tables

- Fig. 1 (p. 129): Agile Software Development Cycle → iterative delivery with continuous stakeholder review and automated validation at every stage.
- Fig. 2 (p. 129): Conceptual Framework of the BFMIS as an Input-Process-Output model → linear regression sits in the Process phase; reports and predictive insights are the Output.
- Fig. 3 (p. 130): Black Box Testing Model → behaviour is validated from inputs and expected outputs without examining internal code.
- Fig. 4 (p. 132): Agile Software Development Methodology Model → each sprint plans, designs, builds and tests prioritising compliance, accuracy and predictive analytics.
- Fig. 5 (p. 133): BFMIS Dashboard → live financial status, summary reports and audit logs.
- Fig. 6 (p. 133): BFMIS Add Budget Page → structured MOOE entry by category, amount and fiscal year.
- Fig. 7 (p. 133): View Expense Entries Page → recorded expenses by project and fiscal year with percentage used and remarks.
- Fig. 8 (p. 133): MOOE Prediction Page → linear regression compares predicted (green) and actual (blue) values to recommend allocations.
- Fig. 9 (p. 133): Budget and Expense Report Page → allocated budget, total expenses and % utilization per MOOE category.
- Fig. 10 (p. 134): Actual vs. Predicted MOOE Allocations per Category → the largest predicted increases fall on Electricity and Fidelity Bond.
- Fig. 11 (p. 135): BFMIS Phased Implementation Plan → five phases from June 2025 to December 2026, ending in DepEd BEIS and EMIS integration.
- Table 1 (p. 131): Sample TAM Questionnaire Structure → five criteria (quality factors, ease of use, usefulness, features, satisfaction) on a 1–5 Likert scale.
- Table 2 (p. 132): Black Box Test Case Table → nine modules and their test case IDs and counts, benchmarked against the 3–5 rule.
- Table 3 (p. 134): Core Features of the Developed BFMIS → four modules (budget allocation, AI prediction, expenditure tracker, automated reporting) with technologies and beneficiaries.
- Table 4 (p. 134): Regression Model Performance → MAE ₱1,532.75, RMSE ₱2,126.84 and R² 0.9281 for the linear regression model.
- Table 5 (p. 135): Summary of Evaluation Results → five dimensions with their highest-rated criterion, mean and weighted mean.
- Table 6 (p. 136): Risk Mitigation Strategies → five identified risks (resistance to change, low digital literacy, data privacy, prediction discrepancies, device incompatibility) with mitigations.

## Limitations and Gaps

- The predictive component depends entirely on the accuracy of the data entered, and the authors themselves record dependency on accurate data input as a scope limitation while carrying "budget inaccuracies or prediction discrepancies" as a live implementation risk mitigated only by continuous model validation and manual override options (Sec. I.C, p. 129; Table 6, p. 136).
- Reported user-acceptance scores are internally inconsistent between the results table and the summary. Table 5 (p. 135) gives dimension means of 4.70 (System Quality), 4.63 (Ease of Use), 4.67 (Perceived Usefulness), 4.67 (System Features) and 4.53 (User Satisfaction), while Sec. VI.A (p. 136) gives System Quality (4.47), Ease of Use (4.46), Usefulness (4.37), Features (4.37) and Satisfaction (4.37). Neither set is reconciled anywhere in the paper.
- Black-box outcomes are internally inconsistent: Sec. V.B (p. 135) records four failures reported by a single tester, whereas Sec. VI.A (p. 136) states that all 37 test cases were passed successfully.
- [unacknowledged] The narrative attributes the per-category actual-versus-predicted comparison (Electricity +9.83%, Fidelity Bond +66.67%) to Table 4, but the printed Table 4 is the regression-metric table, so the per-category figures are not locatable in any printed table.
- [unacknowledged] The regression evaluation reports MAE, RMSE and R² only. No baseline or alternative model is fitted, no out-of-sample or holdout protocol is described, no confidence interval or significance test is printed, and no seasonality, trend or interval estimate appears anywhere in the paper.
- [unacknowledged] Table 2's six listed modules account for 28 test cases while three further modules of 3 cases each carry the total to 37; the six-module table alone does not sum to the reported total.
- [unacknowledged] The ISO/IEC 25010 and ISO 27001 compliance checks are stated as procedure (Sec. IV.B, p. 132) but no characteristic-level result, score or conformance statement is printed for either standard.
- [unacknowledged] The study is a single-system development study on one school's three fiscal years of records with no comparison system, no household or personal-finance setting, and no cost or adoption outcome data.
- The authors acknowledge four specific black-box defects — UI responsiveness (TC010), missing field validation (TC012), incorrect feedback for over-budget entries (TC017), and display issues when the budget is zero (TC020) — despite concluding the system has no major bugs or crashes (Sec. V.B, p. 135).
- The pilot implementation, DepEd BEIS and EMIS integration, and the twelve-month impact assessment are recommendations for future work rather than completed evaluations (Sec. VI.C, p. 136).

## Definitions

- **BFMIS** — Budget and Financial Management Information System, the paper's developed system, functioning as a Knowledge Management System integrated with AI.
- **MOOE** — Maintenance and Other Operating Expenses, the government-allocated funds covering basic expenses such as utilities and minor repairs, mandated under DepEd Orders No. 13, s. 2016 and No. 122, s. 2017.
- **APP** — Annual Procurement Plan, mandated under RA 9184, consolidating procurement needs within the approved budget.
- **AIP** — Annual Implementation Plan, mandated under DepEd Order No. 44, s. 2015, translating long-term goals into yearly programs, budgets and timelines.
- **TAM** — Technology Acceptance Model, originally from Davis (1989) and extended by Venkatesh and Davis (2000), offering a framework for understanding user adoption from perceived usefulness and perceived ease of use.
- **Linear regression** — A predictive analytics tool that forecasts outcomes such as budget needs from historical data by estimating a best-fit linear equation to reveal trends and relationships.
- **Black box testing** — Evaluating a system's behaviour from inputs and expected outputs without considering internal code, used with equivalence partitioning to validate functionality, security and role-based access.
- **% Utilization** — Expenses divided by the budget, offering a quick view of financial efficiency and helping identify over- or under-utilized funds.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MOOE allocation forecasting accuracy, proposed BFMIS linear regression | R2 score | 0.9281 | — | — | Table 4, p. 134 |
| MOOE allocation forecasting accuracy as stated in the narrative | R2 value | 92.81% | — | — | Sec. 5.B Results and Discussion, p. 134 |
| MOOE allocation forecasting error, proposed BFMIS linear regression | MAE | ₱1,532.75 | — | — | Table 4, p. 134 |
| MOOE allocation forecasting error, proposed BFMIS linear regression | RMSE | ₱2,126.84 | — | — | Table 4, p. 134 |
| MOOE allocation forecasting, headline model figures restated | R2, MAE and RMSE | R2 = 0.9281, MAE = ₱1,532.75, RMSE = ₱2,126.84 | — | — | Sec. 6.A Summary, p. 136 |
| Predicted MOOE change, Electricity category | predicted increase | +9.83% | — | — | Sec. 5.B, Fig. 10 discussion, p. 134 |
| Predicted MOOE change, Fidelity Bond category | predicted increase | +66.67% | — | — | Sec. 5.B, Fig. 10 discussion, p. 134 |
| Budget utilization in the expense report, Graduation Program | percent utilization | 100% | — | — | Sec. 5.B, Fig. 9 discussion, p. 133 |
| Black-box coverage across all tested modules | test cases | 37 | — | — | Table 2, p. 132 |
| Black-box test cases, Login Functionality | test cases | 5 | — | — | Table 2, p. 132 |
| Black-box test cases, Role-Based Access Control | test cases | 3 | — | — | Table 2, p. 132 |
| Black-box test cases, Dashboard Overview | test cases | 5 | — | — | Table 2, p. 132 |
| Black-box test cases, Budget Management | test cases | 6 | — | — | Table 2, p. 132 |
| Black-box test cases, Expense Management | test cases | 6 | — | — | Table 2, p. 132 |
| Black-box test cases, Report Generation | test cases | 3 | — | — | Table 2, p. 132 |
| Black-box test cases, Prediction Module, User Management and Security Testing | test cases | 3, 3, 3 | — | — | Table 2 continuation, p. 132 |
| Black-box failures reported by one tester | failed test cases | 4 | — | — | Sec. 5.B, p. 135 |
| User acceptance, System Quality dimension | mean rating | 4.70 | — | — | Table 5, p. 135 |
| User acceptance, System Quality dimension | weighted mean rating | 4.62 | — | — | Table 5, p. 135 |
| User acceptance, Ease of Use dimension | mean rating | 4.63 | — | — | Table 5, p. 135 |
| User acceptance, Ease of Use dimension | weighted mean rating | 4.61 | — | — | Table 5, p. 135 |
| User acceptance, Perceived Usefulness dimension | mean rating | 4.67 | — | — | Table 5, p. 135 |
| User acceptance, Perceived Usefulness dimension | weighted mean rating | 4.51 | — | — | Table 5, p. 135 |
| User acceptance, System Features and Functionality dimension | mean rating | 4.67 | — | — | Table 5, p. 135 |
| User acceptance, System Features and Functionality dimension | weighted mean rating | 4.51 | — | — | Table 5, p. 135 |
| User acceptance, User Satisfaction and Acceptance dimension | mean rating | 4.53 | — | — | Table 5, p. 135 |
| User acceptance, User Satisfaction and Acceptance dimension | weighted mean rating | 4.51 | — | — | Table 5, p. 135 |
| User acceptance across the five key areas as summarised | mean rating by dimension | System Quality 4.47, Ease of Use 4.46, Usefulness 4.37, Features 4.37, Satisfaction 4.37 | — | — | Sec. 6.A Summary, p. 136 |
| Dispersion of user acceptance ratings across all categories | standard deviation | 0.47 to 0.62 | — | — | Sec. 5.B, p. 135 |
| User acceptance sample | participants | at least 30 | — | — | Sec. 4.A Research Design, p. 131 |
| Regression training data window | MOOE record years | 2022–2024 | — | — | Sec. 4.A Research Design, p. 131 |
| Implementation rollout window | planned phases | June 2025 to December 2026 | — | — | Sec. 5.B, Fig. 11, p. 135 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The system integrates Artificial Intelligence (AI) and linear regression analytics to automate budget planning, optimize the allocation of Maintenance and Other Operating Expenses (MOOE), and enhance financial reporting." | Abstract, p. 128 | budgeting |
| "Using Agile methodology, the system was designed with a user-centered approach and developed through iterative cycles involving continuous stakeholder feedback." | Abstract, p. 128 | development_methodology |
| "The system underwent black-box testing and was evaluated against ISO/IEC 25010 (software quality) and ISO 27001 (information security) standards." | Abstract, p. 128 | software_quality_evaluation |
| "Results showed that BFMIS significantly improved accuracy in budget forecasting, enhanced accountability through audit trails and real-time dashboards, and facilitated informed financial decision-making." | Abstract, p. 128 | budgeting |
| "This study employed a descriptive-developmental research design." | Sec. 4.A Research Design, p. 131 | development_methodology |
| "A purposive sample of at least 30 participants directly involved in financial management was selected." | Sec. 4.A Research Design, p. 131 | data_collection |
| "Documents from Pook Elementary School (2022–2024 MOOE records) were gathered and cleaned for system testing." | Sec. 4.A Research Design, p. 131 | data_collection |
| "The system development followed Fig. 4 Agile Development Methodology, chosen for its iterative, flexible approach suited to the dynamic financial management needs of public schools" | Sec. 4.A Project Design, p. 131 | development_methodology |
| "Black box testing evaluates a system’s behavior based on inputs and expected outputs without considering internal code, making it ideal for validating functionality, security, and role-based access in financial systems" | Sec. 3.G Black Box Testing, p. 130 | software_quality_evaluation |
| "Surveys, based on the Technology Acceptance Model (TAM), were conducted during user acceptance testing to evaluate system usability, features, and user attitudes toward the BFMIS." | Sec. 4.A Research Design, p. 131 | software_quality_evaluation |
| "To evaluate the model’s reliability, the following regression metrics such as Mean Absolute Error (MAE), Root Mean Square Error (RMSE) and R² Score were computed." | Sec. 5.B Results and Discussion, p. 134 | model_performance_evaluation |
| "The results presented in Table 4 shows that the model maintains high predictive accuracy, with an R² value of 92.81%, indicating that most of the variance in the target budget can be explained by historical data." | Sec. 5.B Results and Discussion, p. 134 | model_performance_evaluation |
| "AI-Powered Prediction Module, developed in Python using Scikit-learn, it uses linear regression to forecast future budget needs, enabling proactive and strategic planning" | Sec. 5.B Results and Discussion, p. 134 | model_algorithm_integration |
| "Python was used for predictive analytics, applying linear regression for budget forecasting. Scikit-learn built and validated the regression models." | Sec. 4.A Project Design, p. 131 | model_algorithm_integration |
| "XAMPP provides a local server environment with Apache, MySQL, and PHP for development and testing." | Sec. 4.A Project Design, p. 131 | system_development |
| "limitations include dependency on accurate data input, lack of cloud support, basic security, and manual updates for policy changes." | Sec. 1.C Scope and Limitations, p. 129 | system_development |
| "It displays key details like category, budget, actual spending, percentage used, and remarks." | Sec. 5.B Results and Discussion, p. 133 | income_expense_management |
| "The report includes columns for School Year, Category, Allocated Budget, Total Expenses, and % Utilization." | Sec. 5.B Results and Discussion, p. 133 | income_expense_management |
| "The % Utilization metric—calculated by dividing expenses by the budget—offers a quick view of financial efficiency, helping identify over- or under-utilized funds." | Sec. 5.B Results and Discussion, p. 133 | income_expense_management |
| "Continuous model validation and override options" | Table 6 Risk Mitigation Strategies, p. 136 | model_performance_evaluation |

## Remember This

- BFMIS is a Philippine public-school budget system built on Agile with linear-regression MOOE forecasting.
- The only forecasting metrics reported are MAE ₱1,532.75, RMSE ₱2,126.84 and R² 0.9281.
- The paper contains no SARIMA, no SMAPE, no MDA and no prediction intervals.
- Table 5 user-acceptance means conflict with the five figures given in the summary.
- Evaluation is 37 black-box test cases, ISO/IEC 25010 and ISO 27001 compliance, and TAM acceptance.

## Cited Works

- Venkatesh, V.; Davis, F. D. (2000) (methodology) — Extended TAM with social influence and cognitive factors, showing user acceptance evolves with experience. [Sec. 3.H, p. 130]
- Davis, F. D. (1989) (methodology) — Original TAM, defining perceived usefulness, perceived ease of use and user acceptance of information technology. [Sec. 3.H, p. 131]
- Delima, A.; Tejero, M. (2022) (finding) — Perceived usefulness and ease of use significantly impact satisfaction among school financial managers. [Sec. 3.H, p. 131]
- Sun, L.; Li, J. (2023) (methodology) — Applied black box testing to a Family Financial Management System to verify user authentication and data integrity. [Sec. 3.G, p. 130]
- Pressman, R. S.; Maxim, B. R. (2014) (methodology) — Black box testing from a user's perspective detects functional errors and input issues; recommends multiple test cases per module. [Sec. 3.G, p. 130]
- Byol, A.; Foygel, V. (2023) (finding) — Positive perceptions driven by intuitive dashboards and secure features increase long-term adoption in sensitive financial systems. [Sec. 3.H, p. 131]
- Widanaputra, A.; Santosa, D.; Aisyah, N. (2022) (baseline) — Linear regression is effective for educational budget forecasting, enabling data-driven and proactive financial planning. [Sec. 5.B, p. 134]
- Roustaei, M. (2024) (baseline) — Linear regression is effective at identifying patterns, especially with limited data. [Sec. 3.F, p. 130]
- Wasserbacher, M.; Spindler, M. (2022) (context) — Digital financial systems and data analytics strengthen the use of regression models for financial planning and analysis. [Sec. 3.F, p. 130]
- Faheem, M.; Abdullah, R.; Zhang, Y. (2024) (context) — AI lets financial analysts incorporate social media sentiment and macroeconomic indicators to generate real-time, adaptable insights. [Sec. 3.E, p. 130]
- Amado, R.; Dela Cruz, N.; Villanueva, P. (2025) (finding) — Involving parents and teachers in budgeting leads to better resource use and alignment with school needs. [Sec. 3.A, p. 130]
- Beronibla, C. (2024) (context) — Transparency through inclusive budgeting and monitoring systems, with regular audits to maintain financial integrity. [Sec. 3.A, p. 130]
- Gaspar, R.; De Luna, A.; Borja, K. (2022) (finding) — Proper use of MOOE contributes to daily operations, teacher development and student welfare. [Sec. 3.B, p. 130]
- Almazan, J. (2023) (critique) — Schools often face shortages in covering even basic needs, prompting calls for increased budget support and school-head capacity building. [Sec. 3.B, p. 130]
- Caballero, S.; Torres, L.; Ramos, J. (2020) (methodology) — Misalignment detection highlights discrepancies between planned and predicted spending for timely adjustments. [Sec. 5.B, p. 133]

---

Conversion: [`L--Santiago-2025_marked.md`](../../literature/paper-markdowns/L--Santiago-2025_marked.md)