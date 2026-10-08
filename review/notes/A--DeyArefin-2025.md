---
paper_id: A--DeyArefin-2025
first_author: "Dey"
year: 2025
title: "Developing a Rule-Based System to Recommend Household Budget"
venue: "Journal of Information Systems Engineering and Management"
doi: "Not reported"
type: journal-article
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, rule_based_classification, data_collection, model_development, system_development, model_performance_evaluation]
module_rationale:
  financial_planning: "Sec. 1 Introduction (p. 1) frames the problem as allocating income across competing present and future needs, and Sec. 4.8 (p. 34) closes on helping users allocate resources efficiently while maintaining financial stability."
  budgeting: "Sect. 3.5.3.2 (pp. 15-16) builds the budget estimate and expense estimate rules, Sect. 4.3 (p. 21) gives the income-percentage allocation rules for eight categories, and Sect. 4.6.2 (pp. 31-32) describes the rendered budget breakdown."
  savings_debt_management: "Sect. 3.5.3.2 c (p. 15) allocates a contingency fund, Sect. 4.3 (p. 21) allocates 5-10% to debt payment and 10-20% to savings, and Sect. 3.5.3.2 A and Sect. 4.6.2 f define the cash-in-hand versus debt-payment decision."
  income_expense_management: "Sect. 3.1 (p. 4) defines the eight expense categories, Sect. 3.5.3.2 d (p. 16) tracks user-entered actual spending against allocation, and Table 4.1 (p. 20) stores total income, budget, member count and per-member ages."
  rule_based_classification: "Sect. 3.5.3 (pp. 12-18) defines the system as rules, working memory and an inference engine, states rules R1-R6 on income, budget and expenses, verifies five of them in Table 3.9, and compares the result against KNN and Naive Bayes in Table 4.7."
  data_collection: "Sect. 3.3 Collecting Datasets Description (p. 6) names the free online household budget template, the Kaggle download of 41,545 entries including 520 secondary entries, and primary data obtained from family members."
  model_development: "Sect. 4.5 (pp. 22-23) specifies the modelling target as total savings expenditure over 10 household features, the 80/20 split of 648 and 163 entries, and the randomized split with random_state = 0."
  system_development: "Sect. 4.1 (p. 19) and Sect. 3.4 (p. 6) specify the stack — HTML, CSS, JavaScript, jQuery AJAX on the front end with PHP and MySQL on XAMPP — and Sect. 4.6 (pp. 28-33) describes the login page, input.php and the expense output page."
  model_performance_evaluation: "Table 4.7 (p. 25) reports precision, recall, F1 and accuracy for KNN, Naive Bayes and the rule-based system, and Sect. 4.5.7 (pp. 26-28) adds a confusion matrix and an accuracy curve."
---

# Developing a Rule-Based System to Recommend Household Budget

`A--DeyArefin-2025` — Dey (2025), *Journal of Information Systems Engineering and Management* \[Not reported]

## Summary

A rule-based household budgeting web application allocates monthly income across eight expense categories using predefined percentage and age-group rules, then reports cash in hand or debt payment; evaluated against KNN and Naive Bayes on 811 household records, it reports 90.00% accuracy.

## Problem and Motivation

Many people find budgeting tedious and complex, which the paper links to overspending, insufficient savings and growing debt. The absence of structured financial planning tools leaves households without actionable guidance tailored to their own composition. Existing online platforms such as Nerdwallet, Moneysmart and Money Saving Expert supply budget templates and worksheets that the paper describes as generic and blind to individual family composition (Sec. 1, pp. 1-2).

## Method

**Design.** System design and development study with a comparative classifier experiment (KNN, Naive Bayes, rule-based); the authors state no formal design label.
**Sample.** The paper prints three different dataset sizes: 41,545 Kaggle data entries including 520 secondary entries (Sect. 3.3, p. 6), 1,000 CSV entries imported into MySQL (Sect. 3.3, p. 6), and 811 records actually modelled, split into 648 training and 163 testing entries (Sect. 4.5.2, p. 23; Table 4.9, p. 27); unit: one household record carrying income, budget, member count and per-category expenditure.
**Context.** geography: Bangladesh — Chittagong University of Engineering & Technology, income entered in Bangladeshi Taka (BDT) (Sect. 4.6.2, p. 30); population: households with mean net family income 76813.17 and 1 to 23 members per Table 4.9, p. 27; setting: local XAMPP/MySQL web application on Windows 10 plus offline model training in Jupyter Notebook on an Intel Core i5-7200U with 8 GB RAM (Sect. 4.1, p. 19).

- Define eight expense categories — housing, food, medical, education, transportation, debt payment, other expenses, savings — and a four-module architecture of data input, rule application, data processing and output generation (Sect. 3.1-3.2, pp. 4-5).
- Assemble the data from a free online household budget template, a Kaggle download of 41,545 entries including 520 secondary entries, and primary data from family members, importing 1,000 CSV entries into MySQL (Sect. 3.3, p. 6).
- Implement KNN over income, food, medical and other expenditure features using Euclidean distance with k = 3, then majority voting over the nearest neighbours (Sect. 3.5.1, pp. 7-9).
- Implement Naive Bayes classifying household income into Low, Middle and High classes, with a score reported for each of eight expenditure features (Sect. 3.5.2, pp. 9-12).
- Implement the rule-based system as rules, working memory and an inference engine, with Algorithm 1 handling login and Algorithm 2 allocating the household budget (Sect. 3.5.3, pp. 12-14).
- Encode age-group rules comparing income, budget and expenses, and per-age-group food, education and medical allowances from infant through elderly (Sect. 3.5.3.2, pp. 15-18; Table 3.6, p. 16).
- Verify five rules on worked input cases in Table 3.9, and compare KNN, Naive Bayes and the rule-based system across seven qualitative criteria in Table 3.10 (Sect. 3.5.3, p. 18; Sect. 3.5.3, p. 19).
- Apply the allocation percentages: housing 30-35%, food 20-25%, medical and education a minimum of 5%, transport 5%, debt payment 5-10%, savings 10-20%, and the remainder to other expenses (Sect. 4.3 c, p. 21).
- Split the modelling data 80% training (648 entries) and 20% testing (163 entries) with a randomized split at `random_state = 0`, over 10 features X and total savings expenditure as target y, then score accuracy, precision and recall (Sect. 4.5, pp. 22-23).
- Build and describe the web application: a login page with session management, an `input.php` page for income, member ages and budget, and an output page breaking expenses down by category (Sect. 4.6, pp. 28-33).

## Software

- HTML, CSS, JavaScript (front end; versions not reported)
- PHP (back end; version not reported), MySQL (version not reported)
- jQuery and AJAX (versions not reported)
- XAMPP local server (version not reported), phpMyAdmin (version not reported)
- Dreamweaver, Sublime Text (versions not reported)
- Jupyter Notebook for data analysis, visualization and model training (version not reported)
- Python train/test split with `test_size=0.2` and `random_state=0` (library not named)

## Key Findings

- num: Table 4.7 (p. 25) reports accuracy of 96.67% for KNN, 93.00% for Naive Bayes and 90.00% for the rule-based system, with precision 0.96, 0.90 and 0.85, recall 0.95, 0.93 and 0.90, and F1 0.95, 0.91 and 0.90 respectively.
- num: The abstract and Sec. 4.8 (p. 34) both state 90% accuracy in budget allocation for the proposed model, matching the 90.00 printed in Table 4.7.
- num: Sect. 4.5.7 (p. 27) states that precision, recall and accuracy average close to 0.95 and that system precision is 0.9, while p. 28 reports accuracy measuring 0.93, 0.96 and 0.90 across different tests.
- num: Table 4.8 (p. 26) prints true positives 647, false negatives 72, false positives 79 and true negatives 13, and the accompanying text refers to "data 810".
- num: Sect. 4.3 c (p. 21) allocates housing 30% of income, or 35% when family members exceed 4; food 20%, or 25% when family members exceed 4; medical and education a minimum of 5%; transport 5%; debt payment 5-10%; savings 10-20%; and the remaining income to other expenses.
- num: Sect. 3.5.3.2 c (p. 15) sets the contingency fund at a fixed or flexible percentage of income, giving 5% of total income as the example.
- num: The modelling data is split 80% training (648 entries) and 20% testing (163 entries), randomized with `random_state = 0`, over 10 features and one target variable (Sect. 4.5.2, pp. 22-23).
- num: Table 4.9 (p. 27) prints 811 records, mean net family income 76813.17 (std 106866.43, min 5000.00, max 1051758.00), mean budget 78683.39, mean family members 4.18 and mean total saving cost 8362.75 over 809 records.
- num: Table 3.5 and Sect. 3.5.2.4 (p. 12) give Other Expenditure the highest feature score, 1.708, and state that it represents 44% of income in the case examined.
- num: The worked scenario in Sect. 4.4 (p. 21) uses income 9,111 BDT with 5 family members and a 9,000 BDT budget, and Table 3.9 (p. 18) verifies rules on incomes of 20000, 16000, 35981 and 55000 against budgets of 15000, 16000, 50000 and 55000.

## Key Figures and Tables

- Fig 3.1 (p. 4): System architecture for the Household Budget Recommendation System → four modules handle input, rules, processing and output.
- Fig 3.2 (p. 7): Processing module detail with family income, members and budget as input and debt payment or cash in hand as output → single arrows mark operation sequence, double arrows mark relationships.
- Table 3.1 (p. 9): Sample values for the K-nearest-neighbour calculation → eleven household rows with distance column.
- Table 3.2 (p. 9): Smallest distance calculation across all attributes with k = 3 → the three closest rows are 18395, 25800 and 30721 at distances 52315.8, 56720.16 and 56768.42.
- Table 3.4 (p. 11): Monthly income range and income class → ten percentile bands from P5000-8000 to P300300-above, labelled Lower, Middle, High and High and rich.
- Table 3.5 (p. 12): Selected features and their scores → eight expenditure features scored, with Other at 1.708 and Education at 1.117 far above the remaining six, which all fall below 0.08.
- Table 3.6 (p. 16): Rules for each age group → infants get cereal only and basic care, children get primary education, teenagers secondary, young adults higher education, and the elderly receive insulin and chronic-condition medicine.
- Rules R1-R6 (pp. 17-18): Income versus budget and budget versus expense decisions → the plan is useful when income covers or exceeds budget, otherwise the user may face debt payment.
- Table 3.9 (p. 18): Rule verification on worked cases → Rule1 outputs cash in hand at income 20000 and budget 15000, Rule4 outputs debt payment at income 35981 and budget 50000, and Rules 2 and 5 output 0 at equal income and budget.
- Table 3.10 (p. 19): Comparison of classification models on ease of implementation, interoperability, accuracy, real-time suitability, scalability and practical usability → the rule-based system is rated easy and high on interoperability and real-time suitability, KNN low on both.
- Table 4.1 (p. 20): Sample input_data rows → each record is one household with total_income, budget_amount, num_members and per-member age and age_group columns.
- Table 4.3 (p. 23) and Table 4.4 (p. 24): X_train and y_train structures → the target is total savings expenditure with length 648 and data type float64.
- Table 4.5 (p. 25) and Table 4.6 (p. 25): X_test and y_test structures → y_test has length 163 and data type float64.
- Table 4.7 (p. 25): Classification report for the three algorithms → KNN leads on accuracy at 96.67%, while the rule-based system leads on neither precision nor recall.
- Table 4.8 (p. 26): Confusion matrix → true positives 647, false negatives 72, false positives 79 and true negatives 13.
- Table 4.9 (pp. 27-28): Data frame description across count, mean, std, min, quartiles and max → two expenditure columns print a count of 810 and the saving column 809 against 811 elsewhere.
- Fig 4.1 (p. 27): Confusion matrix figure for household budget data → the plotted matrix accompanies the Table 4.8 counts.
- Fig 4.2 (p. 28): Accuracy curve for the household budget recommendation system → accuracy is described as very close to 1, measuring 0.93, 0.96 and 0.90 across different tests.
- Fig 4.3 and Fig 4.4 (p. 29): Login page and successful authentication → the login is a PHP session gateway before the input page.
- Fig 4.5 (p. 30): The page of income, family members and budget → dynamic age fields are generated after the member count is supplied.
- Fig 4.6 (p. 33): The expense page → the rendered per-category breakdown and cash-in-hand or debt-payment status.

## Limitations and Gaps

- The headline accuracy belongs to a classification task the paper never defines: the accuracy table (p. 25) gives the rule-based system 90.00% accuracy on a 163-entry test split, while the confusion-matrix table (p. 26) prints true positives 647, false negatives 72, false positives 79 and true negatives 13 — values on the scale of the 811-row dataset rather than the test split — and the confusion-matrix analysis (p. 27) describes precision, recall and accuracy as averaging close to 0.95 (pp. 25-27).
- The dataset size is reported three incompatible ways: 41,545 Kaggle data entries including 520 secondary entries, 1,000 CSV entries imported into MySQL, and 811 records actually modelled as 648 training plus 163 testing entries (pp. 6, 23, 27).
- Accuracy is additionally reported as "0.93, 0.96, and 0.90 across different tests" (p. 28) and as 90% in the abstract (p. 1) and conclusion (p. 34), so no single accuracy figure governs the paper.
- The authors acknowledge that the accuracy of the rules is paramount because "even small deviations can lead to significant issues in budget and expense calculations", and that an infant incorrectly assigned an insulin medical expense would skew the whole allocation (Discussion, pp. 33-34).
- The authors acknowledge that misreading a surplus as a shortfall, or the reverse, yields inappropriate recommendations and may leave the user with unclear or inaccurate advice (Discussion, p. 34).
- The authors acknowledge that rule-based systems "may not be suitable for every situation, particularly those requiring complex classification tasks" (p. 18).
- [unacknowledged] Age-group boundaries are internally inconsistent: the age-band table (p. 16) gives Young Adult 18-25 and Middle-aged 30-50, a second age-band table (p. 22) gives Young Adult 25-30 and Old 50+, and the evaluation (p. 31) gives Young Adult under 25, Middle-aged over 30 and Old over 50 (pp. 16, 22, 31).
- [unacknowledged] Income classes are stated twice with different boundaries: Low, Middle and High at 30,000 and 100,000 thresholds, against the income-class table's ten percentile bands running to "High and rich" above 300,300 (p. 11).
- [unacknowledged] The budget-rule evaluation (p. 33) reverses the polarity of the budget rules it restates: "If the budget exceeds income, the result will be negative, indicating a shortfall", yet "when the budget remains below expenses, the result reflects a positive financial situation" (p. 33).
- [unacknowledged] The allocation percentages (p. 21) are given without any source; no survey, standard or reference supports the 30-35% housing, 20-25% food, 5-10% debt payment or 10-20% savings bands (p. 21).
- [unacknowledged] No confidence interval, per-class metric, cross-validation, significance test or confusion matrix is reported for KNN or Naive Bayes, so only the rule-based row carries any diagnostic detail (pp. 25-26).
- [unacknowledged] In-text citation numbers do not match the reference list: the introduction credits Nerdwallet, Moneysmart and Money Saving Expert to [1]-[3], which the reference list assigns to Debt.org, Delray Credit Counseling and Financial Mentor; Latimaha et al. is cited as [4] but listed as [11]; Sharma et al. as [6] but listed as [14]; Vermont et al. as [5] but listed as [12] (Sec. 1-2, pp. 2-3; refs. 1-6, 11, 12, 14, pp. 34-35).
- [unacknowledged] No user study, usability instrument or quality model is applied to the deployed application, so the paper reports no evidence about whether households follow the recommended budget (pp. 28-33).

## Definitions

- **Rule-based system** — "a logical framework that uses predefined rules and facts to solve problems and assist in decision-making", recommending budgets from income, family member count and transactions (Sect. 3.5.3, p. 12).
- **Rules** — "Logical conditions and actions for budget recommendations" (Sect. 3.5.3.1, p. 13).
- **Working Memory** — stores "facts, user inputs, and intermediate results" (Sect. 3.5.3.1, p. 13).
- **Inference Engine** — "Matches rules against facts to draw conclusions", comparing income, budget and expenses against predefined rules (Sect. 3.5.3.1, p. 13).
- **ABALANCE (Available Balance)** — `INCOME – COST`, positive when savings are available and negative when expenses exceed income (Sect. 3.5.3.2 B, p. 16).
- **Cash in hand** — the output status when income meets or exceeds budget, that is when total expenses are less than income (Sect. 3.5.3.2 A, p. 16; Sect. 4.6.2 f, p. 32).
- **Debt Payment** — the output status when the allocated amount exceeds income, prompting debt repayment recommendations (Sect. 3.5.3.2 A, p. 16; Sect. 4.6.2 f, p. 32).
- **Income class** — the paper's classification of monthly family income into Low at or below 30,000, Middle at 30,001-100,000 and High above 100,000 (Sect. 3.5.2.2, p. 11).
- **Age group** — the paper's expense profile partition: Infant, Child, Teenager, Young Adult, Middle-aged and Old (Sect. 3.5.3.2 b, p. 15; Sect. 4.6.2 d, p. 31).
- **Contingency Fund** — a fixed or flexible percentage of total income, given as 5%, tracking unexpected expenses such as urgent repairs and medical emergencies (Sect. 3.5.3.2 c, p. 15).

## Key Equations

- `D(a,n) = √(Σᵢ (aᵢ − nᵢ)²)` — Euclidean distance between an input point and a training point.
- `P(A|B) = P(B|A)P(A) / P(B)` — posterior of an income class given expenditure features.
- `ABALANCE = INCOME − COST` — available balance; positive means savings available.
- `Precision = TP / (TP + FP)` — share of positive predictions that are correct.
- `Recall = TP / (TP + FN)` — share of actual positives the system captures.
- `Accuracy = (TP + TN) / (TP + TN + FP + FN)` — proportion of all predictions that are correct.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Household budget classification, KNN | precision | 0.96 | — | — | Table 4.7, p. 25 |
| Household budget classification, KNN | recall | 0.95 | — | — | Table 4.7, p. 25 |
| Household budget classification, KNN | F1 score | 0.95 | — | — | Table 4.7, p. 25 |
| Household budget classification, KNN | accuracy | 96.67% | — | — | Table 4.7, p. 25 |
| Household budget classification, Naive Bayes | precision | 0.90 | — | — | Table 4.7, p. 25 |
| Household budget classification, Naive Bayes | recall | 0.93 | — | — | Table 4.7, p. 25 |
| Household budget classification, Naive Bayes | F1 score | 0.91 | — | — | Table 4.7, p. 25 |
| Household budget classification, Naive Bayes | accuracy | 93.00% | — | — | Table 4.7, p. 25 |
| Household budget classification, Rule-Based System | precision | 0.85 | — | — | Table 4.7, p. 25 |
| Household budget classification, Rule-Based System | recall | 0.90 | — | — | Table 4.7, p. 25 |
| Household budget classification, Rule-Based System | F1 score | 0.90 | — | — | Table 4.7, p. 25 |
| Household budget classification, Rule-Based System | accuracy | 90.00% | — | — | Table 4.7, p. 25 |
| Budget allocation of the proposed rule-based model | accuracy | 90% | — | — | Abstract, p. 1 |
| Budget allocation of the proposed rule-based system | accuracy rate | 90% | — | — | Sec. 4.8 Conclusion, p. 34 |
| Household budget recommendation system precision | precision | 0.9 | — | — | Sect. 4.5.7 Confusion Matrix Analysis, p. 27 |
| Household budget recommendation system, average of precision, recall and accuracy | mean metric value | close to 0.95 | — | — | Sect. 4.5.7 Confusion Matrix Analysis, p. 27 |
| Household budget recommendation system accuracy across different tests | accuracy | 0.93, 0.96, and 0.90 | — | — | Sect. 4.5.7 Confusion Matrix Analysis, p. 28 |
| Household budget confusion matrix, rule-based prediction | true positives | 647 | — | — | Table 4.8, p. 26 |
| Household budget confusion matrix, rule-based prediction | false negatives | 72 | — | — | Table 4.8, p. 26 |
| Household budget confusion matrix, rule-based prediction | false positives | 79 | — | — | Table 4.8, p. 26 |
| Household budget confusion matrix, rule-based prediction | true negatives | 13 | — | — | Table 4.8, p. 26 |
| Dataset used for classification evaluation | records | 811.00 | — | — | Table 4.9, p. 27 |
| Net family income in the evaluation dataset | mean | 76813.17 | — | — | Table 4.9, p. 27 |
| Net family income in the evaluation dataset | standard deviation | 106866.43 | — | — | Table 4.9, p. 27 |
| Net family income in the evaluation dataset | minimum | 5000.00 | — | — | Table 4.9, p. 27 |
| Net family income in the evaluation dataset | maximum | 1051758.00 | — | — | Table 4.9, p. 27 |
| Budget in the evaluation dataset | mean | 78683.39 | — | — | Table 4.9, p. 27 |
| Family members in the evaluation dataset | mean | 4.18 | — | — | Table 4.9, p. 27 |
| Total saving cost in the evaluation dataset | mean | 8362.75 | — | — | Table 4.9, p. 28 |
| Training split for model building | entries | 648 | — | — | Sec. 4.5.2 Data Structure and Splitting, p. 23 |
| Testing split for model performance | entries | 163 | — | — | Sec. 4.5.2 Data Structure and Splitting, p. 23 |
| Training and testing partition of the dataset | split | 80% training / 20% testing | — | — | Sec. 4.5 Model Training, p. 22 |
| Dataset downloaded from Kaggle | data entries | 41,545 | — | — | Sec. 3.3 Collecting Datasets Description, p. 6 |
| Secondary data entries within the download | entries | 520 | — | — | Sec. 3.3 Collecting Datasets Description, p. 6 |
| CSV entries imported into the MySQL database | entries | 1,000 | — | — | Sec. 3.3 Collecting Datasets Description, p. 6 |
| Other Expenditure feature score in the Naive Bayes model | feature score | 1.708 | — | — | Table 3.5, p. 12 |
| Education Expenditure feature score in the Naive Bayes model | feature score | 1.117 | — | — | Table 3.5, p. 12 |
| Other Expenditure share of household income | share of income | 44% | — | — | Sect. 3.5.2.4 Feature Scores and Interpretation, p. 12 |
| Family income classification, stated classes | class boundaries | Low ≤ 30,000; Middle 30,001 - 100,000; High > 100,000 | — | — | Sect. 3.5.2.2 Data Transformation, p. 11 |
| Family income classification, tabulated percentile bands | band boundaries | P5000-8000 to P300300-above | — | — | Table 3.4, p. 11 |
| Housing allocation, family members greater than 4 | allocation percentage of income | 35% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Housing allocation, four or fewer family members | allocation percentage of income | 30% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Food allocation, family members greater than 4 | allocation percentage of income | 25% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Food allocation, four or fewer family members | allocation percentage of income | 20% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Debt payment allocation | allocation percentage of income | 5-10% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Savings allocation | allocation percentage of income | 10-20% | — | — | Sec. 4.3 c Rules for Budget Allocation, p. 21 |
| Contingency fund allocation | percentage of total income | 5% | — | — | Sect. 3.5.3.2 c Estimate Contingency Expenses, p. 15 |
| Worked sample scenario household | income | 9,111 BDT | — | — | Sec. 4.4 Sample Scenario, p. 21 |
| Worked sample scenario household | budget | 9,000 BDT | — | — | Sec. 4.4 Sample Scenario, p. 21 |
| Worked sample scenario household | family members | 5 | — | — | Sec. 4.4 Sample Scenario, p. 21 |
| Rule verification, Rule 1 | income and budget | income = 20000, budget = 15000 | — | — | Table 3.9 Rule Verification, p. 18 |
| Rule verification, Rule 4 | income and budget | income = 35981, budget = 50000 | — | — | Table 3.9 Rule Verification, p. 18 |
| KNN nearest-neighbour working example | distance to nearest training row | 52315.80 | — | — | Table 3.2 Smallest Distance Calculation, p. 9 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This paper introduces a rule-based system that optimizes expenses by considering family size, age distribution, income, and overall budget." | Abstract, p. 1 | rule_based_classification |
| "Experimental results show that the proposed model achieves 90% accuracy in budget allocation, ensuring financial sustainability and preventing overspending." | Abstract, p. 1 | model_performance_evaluation |
| "A rule-based system is a logical framework that uses predefined rules and facts to solve problems and assist in decision-making." | Sect. 3.5.3 Rule-Based System, p. 12 | rule_based_classification |
| "Rules: Logical conditions and actions for budget recommendations." | Sect. 3.5.3.1 Components, p. 13 | rule_based_classification |
| "Inference Engine: Matches rules against facts to draw conclusions." | Sect. 3.5.3.1 Components, p. 13 | rule_based_classification |
| "We can categorize Family Income into classes, for example: Low Income (L): 30,000, Middle Income (M): 30,001 - 100,000, High Income (H): > 100,000." | Sect. 3.5.2.2 Data Transformation, p. 11 | rule_based_classification |
| "If Family Members > 4: Housing = 35% of income. Otherwise: Housing = 30% of income." | Sec. 4.3 c Rules for Budget Allocation, p. 21 | rule_based_classification |
| "The accuracy of these rules is paramount, as even small deviations can lead to significant issues in budget and expense calculations, ultimately affecting the reliability of the recommendations." | Sect. 4.7 Discussion, p. 33 | rule_based_classification |
| "After comparing the Naive Bayes and K-Nearest Neighbors (KNN) algorithms with the Rule-Based System, we conclude that the Rule-Based System is the most appropriate choice for managing household budgets." | Sect. 3.5.3 Rule-Based System, p. 18 | model_performance_evaluation |
| "While KNN achieves the highest accuracy (96.67%), it requires significant computational resources and extensive training data." | Sect. 4.5.5 Model Performance, p. 25 | model_performance_evaluation |
| "Among these, Other Expenditure has the highest score (1.708), making it the most important predictor of income class." | Sect. 3.5.2.4 Feature Scores, p. 12 | income_expense_management |
| "The datasets were split into: Training Set: 80% (648 entries) to build the model. Testing Set: 20% (163 entries) to evaluate model performance." | Sect. 4.5.2 Data Structure and Splitting, p. 23 | model_development |
| "We downloaded a datasets containing 41,545 data entries from Kaggle, including 520 secondary data entries, along with additional primary data obtained from family members." | Sec. 3.3 Collecting Datasets Description, p. 6 | data_collection |
| "Many people find budgeting tedious and complex, often leading to overspending, insufficient savings, and increased debt." | Sec. I Introduction, p. 1 | financial_planning |
| "This study introduces a structured household budget system that dynamically categorizes expenses based on income, family size, and age groups." | Sec. 4.8 Conclusion, p. 34 | financial_planning |
| "Unlike traditional budgeting tools, our system dynamically distributes income across essential categories—such as housing, food, medical care, education, and savings—using predefined rules." | Abstract, p. 1 | budgeting |
| "Budget is Adequate: When the allocated amount is more than or equal to income." | Sect. 3.5.3.2 A Budget Estimate Rule, p. 16 | budgeting |
| "In some cases, the input page may display identical budgets for all family members." | Sect. 4.6.3 Implementation Summary, p. 33 | budgeting |
| "Allocate a fixed or flexible percentage of income to the Contingency Fund (e.g., 5% of total income)." | Sect. 3.5.3.2 c Estimate Contingency Expenses, p. 15 | savings_debt_management |
| "It calculates whether the user's financial situation is positive (savings available) or negative (expenses exceeding income)." | Sect. 3.5.3.2 B Expense Estimate, p. 16 | savings_debt_management |
| "When the budget exceeds income, the result will be negative, indicating a shortfall." | Sect. 4.6.3 Implementation Summary, p. 33 | savings_debt_management |
| "The system categorizes expenses into distinct areas, including housing, food, medical care, education, transportation, debt payments, and savings, ensuring comprehensive coverage of household needs." | Sec. I Introduction, p. 1 | income_expense_management |
| "Users input the actual spending amounts for each category." | Sect. 3.5.3.2 d Track Expenses, p. 16 | income_expense_management |
| "The system was implemented using a combination of front-end technologies (HTML, CSS, JavaScript) and back-end tools (PHP, MySQL)." | Sec. IV Implementation and Experimental Results, p. 19 | system_development |

## Remember This

- Eight fixed expense categories with percentage-of-income allocation rules drive the whole recommendation.
- Rules compare income against budget and budget against expense, returning cash in hand or debt payment.
- Accuracy of 90.00% for the rule-based system trails KNN at 96.67% and Naive Bayes at 93.00%.
- Dataset size is reported as 41,545, as 1,000, and as 811 modelled records.
- Allocation bands (housing 30-35%, food 20-25%, debt 5-10%, savings 10-20%) are given without a source.

## Cited Works

- Latimaha, R.; Bahari, Z.; Ismail, N. A. (2017) (critique) — OLS analysis of basic needs budgets for middle-income earners in three high-cost Malaysian cities found shortfalls and lacked real-time adjustment. [Sec. 2.1, p. 2; ref. 11, p. 35]
- Vermont Legislative Joint Fiscal Office (2019) (critique) — Basic needs budgets and livable wage for urban and rural Vermont, excluding clothing, telecommunications and personal care. [Sec. 2.2, p. 2; ref. 12, p. 35]
- Sharma, S. (2016) (critique) — Ideal monthly expenses of a Nepali family split into lower, middle and upper classes, limited by unpredictable expenses. [Sec. 2.3, pp. 2-3; ref. 14, p. 35]
- A'Hearn, B.; Amendola, N.; Vecchi, G. (2016) (finding) — US study of 5,000 households, 1968-1972, found dual earners managed food budgets less efficiently because of the opportunity cost of time. [Sec. B Related Work, p. 3; ref. 7, p. 35]
- Dominick, S. R.; Widmar, N. O.; Acharya, L.; Bir, C. (2018) (methodology) — Best-worst analysis of the relative importance of household budget categories. [ref. 5, p. 34]
- Apus, J. O.; Mantalaba, K. D. V.; Mackno, A. J. B.; Bokingkito, P. B., Jr. (n.d.) (baseline) — Predicting Filipino household income using a Naïve Bayes classification algorithm. [ref. 22, p. 35]
- Althnian, A. (2021) (baseline) — Design of a rule-based personal finance management system based on financial well-being. [ref. 23, p. 35]
- Bekaroo, G.; Sunhaloo, S. (2007) (context) — Intelligent online budget tracker. [ref. 13, p. 35]
- Yadav, S.; Malhotra, R.; Tripathi, J. (2016) (context) — Smart expense management model for smart homes. [ref. 16, p. 35]
- Saunders, P. (1998) (finding) — Household budgets and income distribution over the longer term, evidence for Australia. [ref. 17, p. 35]
- Galperti, S. (2017) (methodology) — A theory of personal budgeting. [ref. 18, p. 35]
- Noll, H.-H. (2007) (finding) — Household consumption, household incomes and living standards. [ref. 15, p. 35]
- Bumpass, R.; Sweet, L. (2019) (methodology) — Household budget analysis techniques. [ref. 26, p. 35]
- Saunders, P.; Galperti, S. (2022) (methodology) — Smart financial planning models. [ref. 27, p. 35]
- Debt.org (n.d.) (baseline) — Labelled in the introduction as Nerdwallet; cited for generic budget templates that ignore family composition, while reference [1] is Debt.org. [Sec. 1, p. 2; ref. 1, p. 34]

---

Conversion: [`A--DeyArefin-2025_marked.md`](../../literature/paper-markdowns/A--DeyArefin-2025_marked.md)
