---
paper_id: A--Thakur-2025
first_author: "Thakur"
year: 2025
title: "Expense Tracker Management System Using Machine Learning"
venue: "Sigma Journal of Engineering and Natural Sciences, 43(4), 1265-1275"
doi: 10.14744/sigma.2025.00119
type: journal-article
designation: algorithm
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, budgeting, income_expense_management, model_algorithm_integration, model_development, system_development, model_performance_evaluation]
module_rationale:
  pfm_apps_overview: "Sec. 4 Web Application Development and Application Description (pp. 6-9) specify what the Expense Tracker Management System is — a Django/PostgreSQL web application with expense and income entry, summaries, categorization and search."
  pfm_apps_features: "Sec. 1 Introduction (p. 2) and Sec. 4 Key Components (p. 7) enumerate the feature set — personalized dashboard, advanced expense categorization, intelligent alerts and notifications, visual reports, predictive analytics and monthly budget forecasts."
  pfm_apps_problems: "Table 1 (pp. 3-4) catalogues the defects of fifteen prior expense tracker applications — manual input, no automation in expense tracking, limited categories, limited data analysis, Android-only availability."
  budgeting: "Sec. 1 (p. 2) and Sec. 4 Key Components (p. 7) describe budget functions of the system: monthly budget forecasting, highlighting potential overspending areas, income and expense limits, and progress bars comparing actual spending against budget limits."
  income_expense_management: "Sec. 2.1 Dataset Description (p. 4) describes the income/expense transaction attributes (Category, Subcategory, Amount, Income/Expense) and Sec. 4 (pp. 7-9) describes expense and income entry, categorization, transaction lists and income/expense summaries."
  model_algorithm_integration: "Sec. 2.2 Ensemble Learning Models (p. 4) defines and Sect. 4 evaluates bagging, boosting, stacking, voting and blending as combined regressors, and Sec. 4 Key Components (p. 7) wires their output into the application's predictive analytics and budget forecasting."
  model_development: "Sec. 3 Proposed Work (pp. 4-5) gives the training and preparation workflow — MinMax normalization, log1p transformation of the amount attribute, TfidfVectorizer (min_df=3), a 70:30 split, hit-and-trial hyperparameter tuning and cross-validation."
  system_development: "Sec. 4 Backend/Frontend Development (pp. 6-7) specifies the implementation stack — Django with built-in authentication and RBAC, PostgreSQL, HTML/CSS/JavaScript, jQuery Ajax, Chart.js, and client-side and server-side validation."
  model_performance_evaluation: "Table 2 (p. 6) reports R-squared, mean absolute error, mean square error and relative absolute error for eight individual and five ensemble regressors, with XGBoost highest among individual models and voting highest overall."
---

# Expense Tracker Management System Using Machine Learning

`A--Thakur-2025` — Thakur (2025), *Sigma Journal of Engineering and Natural Sciences, 43(4), 1265-1275* \[10.14744/sigma.2025.00119]

## Summary

A Django web expense tracker adds machine-learning expense prediction to a public transaction dataset: the voting ensemble regressor attains the highest reported R² (78.11) of thirteen models, and the paper documents the application's dashboards, expense categorization, alerts and budget forecasting.

## Problem and Motivation

Most individuals on fixed incomes need to keep expenditures within budget, yet expense tracking has traditionally been manual, laborious pen-and-paper record keeping. Although many expense tracking apps exist, the paper states that many still rely on manual input systems that are time-consuming and prone to error, and that existing applications offer only basic data analysis. The paper positions predictive analytics — forecasting expenses and monthly budgets from past spending patterns and income trends — as the addition that moves an expense tracker into an "Expense Tracker Management System" (Sec. 1, p. 2).

## Method

**Design.** Experimental benchmark of regression models with a system implementation; the authors state no formal design label.
**Sample.** Not reported — the paper names the Kaggle "Daily Transactions Dataset" but prints no record count and no user sample (Sec. 2.1, p. 2).
**Context.** geography: India — the dataset's transactions are "recorded in the official currency of India" and the authors are at Manipal University Jaipur; population: Not reported — the dataset is described as "virtual transactions people make every day"; setting: Offline computational benchmarking of a 70:30 train/test split plus a locally implemented Django/PostgreSQL web application shown through screenshots (Sec. 2.1, p. 4; Sec. 4, pp. 6-9).

- Use the "Daily Household Transactions" Kaggle dataset, whose attributes are Date, Mode, Category, Subcategory, Note, Amount, Income/Expense and Currency (Sec. 2.1, pp. 2-4).
- Normalize every feature with MinMax scaling to a range between 0 and 1 (Sec. 3, p. 4).
- Transform the amount attribute with the `log1p` function, the natural logarithm of 1 + x, shown as a distribution in Fig. 1 (Sec. 3, p. 5).
- Vectorize the text fields — Mode, Category, Subcategory, Note, Income/Expense — with `TfidfVectorizer(min_df=3)`, keeping only terms appearing in at least three documents (Sec. 3, p. 5).
- Split the preprocessed dataset 70:30 into training and testing portions (Sec. 3, p. 5).
- Train and evaluate eight individual regressors (XGBoost, random forest, SVM, MLP, KNN, decision tree, extra tree, CatBoost) and five ensemble regressors (bagging, boosting, stacking, voting, blending) (Sec. 2.2, p. 4; Table 2, p. 6).
- Tune key hyperparameters such as XGBoost learning rate and KNN neighbour count by a "Hit and Trial" method, evaluated through cross-validation to prevent overfitting, with best settings validated on the test set (Sec. 4, p. 6).
- Score every model on four regression metrics — R-squared, mean absolute error, mean square error and relative absolute error (Sec. 3, pp. 5-6).
- Implement the Django backend, PostgreSQL database and JavaScript frontend, and describe the resulting application screen by screen with screenshots (Sec. 4, pp. 6-9).

## Software

- Django (Python), version not reported
- PostgreSQL, version not reported
- HTML, CSS, JavaScript
- jQuery (Ajax asynchronous requests; jQuery Validation for client-side validation)
- Chart.js (frontend charting)
- MinMax scaler, `log1p` transformation, `TfidfVectorizer(min_df=3)` — MinMax scaling and data transformation follow Jadhav et al. (2023); library not named
- XGBoost, random forest, SVM, multi-layer perceptron, KNN, decision tree, extra tree, CatBoost (versions not reported)
- Bagging, boosting, stacking, voting and blending ensemble regressors (versions not reported)

## Key Findings

- num: Table 2 (p. 6) gives the voting ensemble regressor the highest R-squared of all thirteen models, 78.11, against 77.89 for the best individual model, XGBoost.
- num: The abstract reports the voting ensemble regressor at "highest R-square value of 78.11% and lowest relative absolute error of 0.6121", while Sec. 4 (p. 6) reports its lowest relative absolute error as 0.1765; Table 2 lists 0.6121 under mean absolute error and 0.1765 under relative absolute error.
- num: The lowest mean absolute error in Table 2 is 0.6107 for extra tree, and the highest is 0.7020 for CatBoost; the voting ensemble regressor records 0.6121.
- num: Mean square error ranges from 0.9399 (XGBoost) to 1.2937 (KNN); bagging and boosting have no mean square error printed.
- num: Relative absolute error is 0.1919 for all eight individual models, then 0.1835 (bagging), 0.1852 (boosting), 0.1939 (stacking), 0.1765 (voting) and 0.1909 (blending).
- num: The preprocessing and evaluation split is 70% training and 30% testing (Sec. 3, p. 5).
- num: The `TfidfVectorizer` is configured with `min_df=3`, retaining only terms appearing in at least three documents (Sec. 3, p. 5).
- num: The paper's stated claimed improvement over prior work is qualitative: advanced analytics and prediction, customizable reporting, user-friendly design and interactive dashboards, against fifteen prior applications in Table 1 (Sec. 4, p. 9).
- The paper argues that because dataset characteristics give the models nearly the same explanatory power, "RAE stands out be the deciding factor in our approach" (Sec. 4, p. 6).

## Key Figures and Tables

- Table 1 (pp. 3-4): state-of-the-art description of fifteen expense tracking, income and expense tracker applications with their focus, dataset, parameters and limitations → every listed prior system is limited by manual entry, absent automation, limited analysis or single-platform availability.
- Table 2 (p. 6): R-squared, mean absolute error, mean square error and relative absolute error for eight individual and five ensemble models → voting leads on R-squared and relative absolute error; extra tree leads on mean absolute error; bagging and boosting have no mean square error.
- Figure 1 (p. 5): distribution of `log(1+amount)` after data transformation → justifies applying `log1p` to the amount attribute.
- Figure 2 (p. 7): login page → Django built-in authentication with `@login_required` authorization decorators.
- Figure 3 (p. 7): expense summary with category breakdown, monthly trend line charts and transaction list → spending is presented per category and per period.
- Figure 4 (p. 8): income summary by source with charts and comparison of actual against projected income targets → income is tracked alongside expenses.
- Figure 5 (p. 8): expense entry form → expenses are entered manually through a form or API endpoint with validation.
- Figure 6 (p. 9): income entry form with recurring-entry marking → future income entries can be automated once flagged recurring.
- Figure 7 (p. 9): expense categorization as shopping, food, rent and other → categories are predefined plus user-created custom ones.
- Figure 8 (p. 10): search and filtering → the described debt tracking module is reached through keyword search, attribute filters and sorting.

## Limitations and Gaps

- The headline error figure contradicts itself: the abstract (pp. 1) and the conclusion (pp. 10) both state a "lowest relative absolute error of 0.6121" for the voting ensemble regressor, while Sec. 4 (pp. 6) states 0.1765 and Table 2 lists 0.6121 as the voting model's *mean absolute error* and 0.1765 as its relative absolute error.
- The paper reports no record count, no number of users, no number of users represented and no dataset characteristics beyond the attribute list; the dataset is stated only as the Kaggle "Daily Transactions Dataset" (p. 2).
- [unacknowledged] The forecasting claim is not evaluated as forecasting: the split is a single 70:30 random ratio with no temporal holdout, no forecast horizon, and no comparison of a predicted expense against a realised later expense (Sec. 3, pp. 5).
- [unacknowledged] No confidence interval, standard deviation, per-fold result or significance test is reported for any model in Table 2, and relative absolute error is an identical 0.1919 for all eight individual models (Table 2, pp. 6).
- [unacknowledged] Table 2 leaves mean square error blank for bagging and boosting, so no mean square error comparison covers the ensemble group (Table 2, pp. 6).
- [unacknowledged] The application's claimed benefits over prior work — improved budgeting, financial planning and financial awareness — are asserted without any user study, usability instrument or outcome measurement, so no benefit claim is supported by data (Sec. 4 Application Benefits, pp. 9; Sec. 5, pp. 10).
- [unacknowledged] Savings and debt appear only as display surfaces: a savings overview reporting a total and a search/filter screen described as a debt tracking system, with no savings goal, debt balance, repayment strategy or alert evaluation (Sec. 4, pp. 7, 9).
- [unacknowledged] The paper describes the entry path as manual in several places while the introduction claims automation that eliminates manual data entry, and no automated capture mechanism (bank sync, receipt scanning) is described as built rather than as future work (Sec. 1, pp. 2; Sec. 4, pp. 8; Sec. 5, pp. 10).
- The authors state that future work will develop a dataset capturing "distinct and meaningful patterns, leading to better performance and more reliable predictions", which acknowledges the present dataset limits prediction quality (Sec. 5, pp. 10).



## Definitions

- **Expense Tracker Management System** — the paper's term for an expense tracker that places heightened emphasis on expense management specifically, in contrast to the earlier "Income and Expense Tracker" (Abstract, p. 1).
- **R-squared (R2) value** — "the coefficient of determination", measuring the proportion of the variance in the dependent variable that is predictable from the independent variables; higher (closer to 1) indicates better model fit (Sec. 3, Eq. 1, p. 5).
- **Mean absolute error (MAE)** — "the average magnitude of errors between predicted and actual values"; lower indicates better performance (Sec. 3, Eq. 2, p. 5).
- **Mean square error (MSE)** — "the average of the squares of the errors", that is the average squared difference between actual and predicted values (Sec. 3, Eq. 3, p. 5).
- **Relative absolute error (RAE)** — total absolute error expressed "as a proportion of the total absolute error of a simple predictor, such as the mean of the actual values", a normalized measure of prediction accuracy (Sec. 3, Eq. 4, p. 5).
- **Ensemble learning** — "a technique in machine learning where we combine the predictions of several different models to make a stronger and more accurate model than any individual model" (Sec. 2.2, p. 4).
- **Blending** — stacking that uses a holdout set, taken from the training set, to generate predictions for the meta-model's training set (Sec. 2.2, p. 4).
- **Stacking** — training multiple base models then using a meta-model to combine their predictions, treating base-model predictions as additional features (Sec. 2.2, p. 4).

## Key Equations

- `R² = 1 − SS_res / SS_tot` — coefficient of determination: explained variance over total variance.
- `MAE = (1/n) Σ |y_i − ŷ_i|` — average magnitude of prediction error.
- `MSE = (1/n) Σ (y_i − ŷ_i)²` — average squared prediction error.
- `RAE = Σ|y_i − ŷ_i| / Σ|y_i − ȳ|` — total absolute error relative to a mean-only predictor.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Expense prediction, XGBoost (individual) | R-squared (R2) | 77.89 | — | — | Table 2, p. 6 |
| Expense prediction, XGBoost (individual) | mean absolute error | 0.6324 | — | — | Table 2, p. 6 |
| Expense prediction, XGBoost (individual) | mean square error | 0.9399 | — | — | Table 2, p. 6 |
| Expense prediction, XGBoost (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, random forest (individual) | R-squared (R2) | 77.02 | — | — | Table 2, p. 6 |
| Expense prediction, random forest (individual) | mean absolute error | 0.6150 | — | — | Table 2, p. 6 |
| Expense prediction, random forest (individual) | mean square error | 0.9773 | — | — | Table 2, p. 6 |
| Expense prediction, random forest (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, SVM (individual) | R-squared (R2) | 72.41 | — | — | Table 2, p. 6 |
| Expense prediction, SVM (individual) | mean absolute error | 0.6943 | — | — | Table 2, p. 6 |
| Expense prediction, SVM (individual) | mean square error | 1.1734 | — | — | Table 2, p. 6 |
| Expense prediction, SVM (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, MLP (individual) | R-squared (R2) | 74.81 | — | — | Table 2, p. 6 |
| Expense prediction, MLP (individual) | mean absolute error | 0.6439 | — | — | Table 2, p. 6 |
| Expense prediction, MLP (individual) | mean square error | 1.0716 | — | — | Table 2, p. 6 |
| Expense prediction, MLP (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, KNN (individual) | R-squared (R2) | 69.58 | — | — | Table 2, p. 6 |
| Expense prediction, KNN (individual) | mean absolute error | 0.6956 | — | — | Table 2, p. 6 |
| Expense prediction, KNN (individual) | mean square error | 1.2937 | — | — | Table 2, p. 6 |
| Expense prediction, KNN (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, decision tree (individual) | R-squared (R2) | 70.89 | — | — | Table 2, p. 6 |
| Expense prediction, decision tree (individual) | mean absolute error | 0.6701 | — | — | Table 2, p. 6 |
| Expense prediction, decision tree (individual) | mean square error | 1.2378 | — | — | Table 2, p. 6 |
| Expense prediction, decision tree (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, extra tree (individual) | R-squared (R2) | 75.68 | — | — | Table 2, p. 6 |
| Expense prediction, extra tree (individual) | mean absolute error | 0.6107 | — | — | Table 2, p. 6 |
| Expense prediction, extra tree (individual) | mean square error | 1.0344 | — | — | Table 2, p. 6 |
| Expense prediction, extra tree (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, CatBoost (individual) | R-squared (R2) | 76.02 | — | — | Table 2, p. 6 |
| Expense prediction, CatBoost (individual) | mean absolute error | 0.7020 | — | — | Table 2, p. 6 |
| Expense prediction, CatBoost (individual) | mean square error | 1.0199 | — | — | Table 2, p. 6 |
| Expense prediction, CatBoost (individual) | relative absolute error | 0.1919 | — | — | Table 2, p. 6 |
| Expense prediction, bagging (ensemble) | R-squared (R2) | 76.34 | — | — | Table 2, p. 6 |
| Expense prediction, bagging (ensemble) | mean absolute error | 0.6217 | — | — | Table 2, p. 6 |
| Expense prediction, bagging (ensemble) | mean square error | Not reported | — | — | Table 2, p. 6 |
| Expense prediction, bagging (ensemble) | relative absolute error | 0.1835 | — | — | Table 2, p. 6 |
| Expense prediction, boosting (ensemble) | R-squared (R2) | 75.89 | — | — | Table 2, p. 6 |
| Expense prediction, boosting (ensemble) | mean absolute error | 0.6208 | — | — | Table 2, p. 6 |
| Expense prediction, boosting (ensemble) | mean square error | Not reported | — | — | Table 2, p. 6 |
| Expense prediction, boosting (ensemble) | relative absolute error | 0.1852 | — | — | Table 2, p. 6 |
| Expense prediction, stacking (ensemble) | R-squared (R2) | 73.56 | — | — | Table 2, p. 6 |
| Expense prediction, stacking (ensemble) | mean absolute error | 0.6613 | — | — | Table 2, p. 6 |
| Expense prediction, stacking (ensemble) | mean square error | 1.0604 | — | — | Table 2, p. 6 |
| Expense prediction, stacking (ensemble) | relative absolute error | 0.1939 | — | — | Table 2, p. 6 |
| Expense prediction, voting (ensemble) | R-squared (R2) | 78.11 | — | — | Table 2, p. 6 |
| Expense prediction, voting (ensemble) | mean absolute error | 0.6121 | — | — | Table 2, p. 6 |
| Expense prediction, voting (ensemble) | mean square error | 0.9648 | — | — | Table 2, p. 6 |
| Expense prediction, voting (ensemble) | relative absolute error | 0.1765 | — | — | Table 2, p. 6 |
| Expense prediction, blending (ensemble) | R-squared (R2) | 74.37 | — | — | Table 2, p. 6 |
| Expense prediction, blending (ensemble) | mean absolute error | 0.6731 | — | — | Table 2, p. 6 |
| Expense prediction, blending (ensemble) | mean square error | 1.0439 | — | — | Table 2, p. 6 |
| Expense prediction, blending (ensemble) | relative absolute error | 0.1909 | — | — | Table 2, p. 6 |
| Best individual model, XGBoost, R-squared stated in the results text | R-squared (R2) | 77.89 | — | — | Sec. 4 Results and Discussion, p. 6 |
| Lowest relative absolute error claimed for the voting ensemble regressor | relative absolute error | 0.6121 | — | — | Abstract, p. 1 |
| Lowest relative absolute error claimed for the voting ensemble regressor | relative absolute error | 0.6121 | — | — | Sec. 5 Conclusion, p. 10 |
| Training and testing partition of the dataset | train/test ratio | 70:30 | — | — | Sec. 3 Proposed Work, p. 5 |
| TF-IDF document-frequency floor for retained terms | min_df | 3 | — | — | Sec. 3 Proposed Work, p. 5 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Extreme Boost (XGBoost) outperforms other individual models with highest R-square value and voting ensemble regressor outperforms ensemble techniques with highest R-square value of 78.11% and lowest relative absolute error of 0.6121." | Abstract, p. 1 | model_performance_evaluation |
| "XGBoost technique outperforms other individual machine learning models with a highest r-square value of 77.89, while Voting Ensemble Regressor outperforms individual models and other ensemble approaches with highest r-square value of 78.11 and lowest relative absolute error of 0.1765." | Sec. 4 Results and Discussion, p. 6 | model_performance_evaluation |
| "Despite the availability of expense tracking apps, many still rely on manual input systems, which can be time-consuming and prone to error." | Sec. 1 Introduction, p. 2 | pfm_apps_problems |
| "Our system leverages machine learning for advanced analytics and precise expense predictions, offering users a deeper understanding of their financial patterns." | Sec. 4 Application Benefits, p. 9 | pfm_apps_features |
| "Furthermore, our system incorporates predictive analytics capabilities, allowing users to forecast their monthly budgets with precision." | Sec. 1 Introduction, p. 2 | budgeting |
| "Users can also see their top expenses, compare their actual spending against budget limits with progress bars, and view predictive analytics for future expenses." | Sec. 4 Application Description, p. 7 | budgeting |
| "Budget Forecasting: Offer monthly budget forecasts and highlight potential overspending areas." | Sec. 4 Key Components, p. 7 | pfm_apps_features |
| "Our application outperforms other applications from the state-of-the-art discussed in the literature." | Sec. 4 Application Benefits, p. 9 | pfm_apps_overview |
| "The dataset attributes are as follows. Date: The date and time of the transaction; Mode: The payment method used for the transaction." | Sec. 2.1 Dataset Description, pp. 2-3 | income_expense_management |
| "Users can assign categories to their expenses either manually or through automated rules." | Sec. 4 Application Description, p. 9 | income_expense_management |
| "Ensemble learning is a technique in machine learning where we combine the predictions of several different models to make a stronger and more accurate model than any individual model." | Sec. 2.2 Ensemble Learning Models, p. 4 | model_algorithm_integration |
| "The first step is normalization using MinMax scaling technique which scales each feature to a given range, between 0 and 1." | Sec. 3 Proposed Work, p. 4 | model_development |
| "After successful preprocessing, the dataset is divided into the ratio of 70:30, where 70% is used for training and 30% is used for testing purposes." | Sec. 3 Proposed Work, p. 5 | model_development |
| "The parameter tuning process for the selected machine learning models involves identifying key hyperparameters such as learning rate for XGBoost or number of neighbors for KNN, by using Hit and Trial method." | Sec. 4 Results and Discussion, p. 6 | model_development |
| "Django's Built-in Authentication: Implement role-based access control (RBAC) using Django's authentication system." | Sec. 4 Backend Development, p. 6 | system_development |
| "Visual Reports: Generate visual reports using JavaScript charting libraries like Chart.js." | Sec. 4 Key Components, p. 7 | system_development |
| "Since there is no more difference in the r-square value of models because of characteristics of the dataset, as the distribution of the variables and the nature of their relationships, explaining the same amount of variance." | Sec. 4 Results and Discussion, p. 6 | model_performance_evaluation |
| "We also aim in developing a dataset for expense tracker system to ensure that the dataset captures distinct and meaningful patterns, leading to better performance and more reliable predictions." | Sec. 5 Conclusion, p. 10 | model_performance_evaluation |

## Remember This

- Thirteen regressors are compared on one Kaggle daily-transactions dataset; voting leads at R² 78.11.
- The abstract and conclusion mislabel the voting model's MAE 0.6121 as its relative absolute error; Sec. 4 gives 0.1765.
- Preprocessing is MinMax scaling, log1p on amount, and TF-IDF with min_df=3, then a 70:30 split.
- No record count, user sample, confidence interval or significance test is reported anywhere in the paper.
- The web application is Django with PostgreSQL, Chart.js and jQuery; expense entry remains manual.

## Cited Works

- Jadhav, N. J.; Chakor, R. V.; Gun-jal, T. M.; Pawar, D. D. (2022) (baseline) — Expense tracker records category, date and amount; limited by manual input for adding expenses. [Table 1, p. 3]
- Masendu, T. R.; Tripathi, A. M. (2022) (baseline) — Daily expense tracker with expense history, analytics and PDF reports; Android-only and dependent on internet for updates. [Table 1, p. 3]
- Thomas, P.; Lekshmi; Mahalekshmi (2020) (baseline) — Expense tracker with email verification, analysis and prediction; not suitable for complex data analysis, only simple daily expenses. [Table 1, p. 3]
- Cabañero, R. A. (2023) (baseline) — CodeIgniter expense management system covering expense tracking, income records and budget planning; relies on user-entered data. [Table 1, p. 3]
- Johri, E.; Desai, P.; Soni, P.; Jain, H.; Sanganeria, N. (2023) (baseline) — AI-based expense monitoring application whose recommendations depend heavily on the accuracy of user-provided data and thresholds. [Table 1, p. 3]
- Thakare, R.; Thakare, N.; Sangtani, R.; Bondre, S.; Manekar, A. (2023) (baseline) — Expense tracker application using Naïve Bayes to detect bank messages from Firebase; manual expenses entry, no automation. [Table 1, p. 3]
- Laishram, C. (2023) (baseline) — Flutter expenses tracker app comprising expense entry and monthly budget setting; Android-only with manual entry. [Table 1, p. 3]
- Thanapal, P.; Patel, M. Y.; Raj, T. L.; Kumar, J. S. (2015) (baseline) — Income and expense tracker adding income, expense, category and file export; Android-only and manual entry. [Table 1, p. 3]
- Saravade, P. S.; Molak, P. R.; Jadhav, B. S.; Khare, K. P.; Lokare, S. M. (2023) (baseline) — Income and expense daily tracker system with registration, income/expense views, email verification and analysis; depends on manual data entry. [Table 1, p. 3]
- Daily Transactions Dataset, Kaggle (2024) (methodology) — Kaggle dataset prasad22/daily-transactions-dataset, accessed 21 July 2025, supplies the transaction records used for training and testing. [Sec. 2.1, p. 2; ref. 16, p. 11]
- Jadhav, A.; Dhaulakhandi, D.; Shandilya, S. K.; Malviya, L.; Mewada, A. (2023) (methodology) — Data transformation as a preprocessing stage in machine learning regression problems, cited for the MinMax scaling step. [ref. 21, p. 11]
- Mienye, I. D.; Sun, Y. (2022) (context) — Survey of ensemble learning covering concepts, algorithms, applications and prospects, cited to motivate bagging, boosting, stacking, voting and blending. [ref. 19, p. 11]
- Aldave, R.; Dussault, J. P. (2014) (methodology) — Systematic ensemble learning for regression, cited as the ensemble-learning reference. [ref. 18, p. 11]
- Doan, T.; Kalita, J. (2015) (context) — Selecting machine learning algorithms using regression models, cited for machine learning's expanding application potential. [ref. 17, p. 11]
- Odegua, R. (2019) (methodology) — Empirical study of bagging, boosting and stacking ensemble techniques, cited for improved overall ensemble performance. [ref. 20, p. 11]

---

Conversion: [`A--Thakur-2025_marked.md`](../../literature/paper-markdowns/A--Thakur-2025_marked.md)
