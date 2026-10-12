---
paper_id: I--Simonse-2024
first_author: Simonse
year: 2024
title: "Economic predictors of the subjective experience of financial stress"
venue: "Journal of Behavioral and Experimental Finance"
doi: 10.1016/j.jbef.2024.100933
type: journal article
designation: international
status: extracted
modules: [savings_debt_management, income_expense_management]
module_rationale:
  savings_debt_management: "Sect. 3.3 (Independent Variables) operationalizes buffer savings and the number of debts, and Sect. 4.2 and Sect. 5 report that insufficient buffer savings and more debts predicted financial stress while debt amount did not (Sect. 3.3, p. 6; Table 4, p. 9)."
  income_expense_management: "Sect. 3.3 defines adjusted net income and income volatility (the number of adverse income shocks over twelve months) as predictors, and Sect. 4.2 tests their association with financial stress (Sect. 3.3, pp. 6-7; Table 4, p. 9)."
---

# Economic predictors of the subjective experience of financial stress

`I--Simonse-2024` — Simonse et al. (2024), *Journal of Behavioral and Experimental Finance* \[10.1016/j.jbef.2024.100933]

## Summary

Combining five economic factors — income, buffer savings, debts, income volatility, and employment — predicted financial stress better than income alone in a Dutch household panel (N = 1114). Buffer savings, income, and number of debts predicted financial stress; debt amount and income volatility did not.

The paper takes an integrative approach, entering adjusted income, buffer savings, the number of debts, income volatility, and employment simultaneously in one model of a four-factor financial stress measure (the PIFS). Buffer savings carried the largest relative contribution, followed by employment, number of debts, and income. The number of debts predicted financial stress, but neither debt amount nor debt-to-income ratio did. Income volatility was not associated with financial stress. Employment was negatively associated with financial stress only for households at the lowest income level. The authors conclude that research and policy should look beyond income to savings, number of debts, and unemployment.

## Problem and Motivation

Most research on the economic correlates of financial stress examines only income or one or two predictors in isolation, so the relative contributions of different aspects of a household's economic situation remain unclear, and any isolated association may partly reflect an unmeasured predictor (Sect. 1, p. 2). Savings, debts, income volatility, and employment are also associated with well-being, and their associations with financial stress may be stronger for lower-income households, yet evidence on income interactions is scarce (Sect. 1, p. 2). The study's contribution is an integrative test of the five economic factors together, with income as a moderator, that separates their relative contributions (Sect. 2.3, p. 4).

## Method

**Design.** Cross-sectional survey study analysed with pooled robust MM-regression over 93 multiply-imputed datasets; the authors describe the data as cross-sectional and state no other formal design label (Sect. 3.1, p. 4; Sect. 3.7, p. 7).
**Sample.** N = 1114 respondents (unit of analysis: the individual household respondent) to an April 2018 questionnaire, after removing eight empty surveys; the sample is drawn from Dutch households selected by a Statistics Netherlands probability sample (Sect. 3.1, p. 4).
**Context.** geography: the Netherlands; population: Dutch households; setting: a Centerdata panel questionnaire linked with economic, demographic, and psychological variables, with no intervention and no software system (Sect. 3.1, p. 4).

Procedure as printed:

- Dependent variable is the 12-item Psychological Inventory of Financial Scarcity (PIFS): M = 1.96, SD = 1.12, Cronbach's α = .93, with four components — appraisal of insufficient financial resources, appraisal of lack of control, financial worries and rumination, and short-term focus (Sect. 3.2, p. 4; Table 2, p. 6).
- Focal predictors, entered simultaneously: adjusted net income (net monthly household income divided by the square root of household size), buffer savings, number of debts, income volatility, and employment status (Sect. 3.3, pp. 6-7; Sect. 4.2, p. 8).
- Buffer is a dichotomous variable equal to one if liquid assets exceed the threshold € 600 + [monthly income] + € 400 * [household size], following the Nibud Buffer Calculator; liquid savings amount is used in a robustness check (Sect. 3.3, p. 6).
- Debts counted as positive responses to five debt types (personal loans/revolving credit/installment credit; pledged loan; overdue credit-card payments; money borrowed from family, friends, or acquaintances; any other credit, loan, or debt); mortgages and student loans are excluded (Sect. 3.3, p. 6).
- Income volatility is the number of months in the twelve months before measurement in which net income was lower than in the previous month; a robustness check uses the relative size of income shocks (Sect. 3.3, p. 7).
- Employment is a dichotomous variable equal to zero for job seekers after job loss, first-time job seekers, those with (partial) work disability, or unpaid work while retaining unemployment benefit, and one otherwise (Sect. 3.3, p. 7).
- Nine control variables: gender, age, education level, household size, and the five Big Five personality traits (openness, conscientiousness, agreeableness, extraversion, emotional stability) (Sect. 3.4, p. 7).
- Numerical variables standardized before forming interaction terms, yielding standardized coefficients for comparing relative contributions (Sect. 3.5, p. 7).
- Missing data handled by multivariate imputation by chained equations (mice) with random forests; 93 imputed datasets, equivalent to lambda = .05 (Sect. 3.6, p. 7).
- Estimation via the MM-estimator (Yohai, 1987) for robustness to influential observations, using the lmrob function in the R-package robustbase with Koller and Stahel (2017) parameters; 93 regressions pooled with Rubin's (1987) rules (Sect. 3.7, p. 7).
- Models nested: Model 1 economic predictors only; Model 2 adds controls; Model 3 adds interactions of income with savings, debt amount, income volatility, and employment (Sect. 4.2, p. 8; Table 4, p. 9).

## Software

- R; the mice package (Van Buuren and Groothuis-Oudshoorn, 2011) with a random forest imputation mechanism (Sect. 3.6, p. 7).
- R-package robustbase, lmrob function (MM-estimator, Koller and Stahel 2017 parameters) (Sect. 3.7, p. 7).
- Rubin's (1987) rules for pooling the 93 imputations (Sect. 3.7, p. 7).
- Detailed data steps and R-scripts are reported as available in the online supplemental materials (Sect. 3.1, p. 4).

## Key Findings

- num: The model with all five economic factors (R2 = .29) had more explanatory power than a model with income only (R2 = .06) (Sect. 4.3, p. 8).
- num: Buffer savings had the largest relative contribution to explaining financial stress, followed by employment, number of debts, and income (Sect. 4.2, p. 8).
- num: Number of debts predicted financial stress (β = 0.238*** in Model 1), but debt amount and debt-to-income ratio did not (Sect. 4.2, p. 8; Sect. 4.3, p. 8).
- num: Income volatility did not predict financial stress (β = 0.010, p = 0.694 in Model 1) (Table 4, p. 9).
- num: Employment predicted financial stress only at the lowest income level (income two standard deviations below the mean) (Sect. 4.2, p. 8).
- num: Model fit rose from R2 = .29 (Model 1) to R2 = .34 (Model 2), W = 4.90, p < .001, and to R2 = .36/ .35 (Model 3), W = 2.97, p = .019 (Sect. 4.2, p. 8; Table 4, p. 9).
- num: Financial stress correlated with buffer savings (rPB = −.37), income (rS = −.30), number of debts (rS = .25), and employment (rPB = −.18), and very weakly with income volatility (rS = .05) (Sect. 4.1, p. 7).
- num: 41% of savings values were missing, and 550 (49%) respondents had missing values on at least one variable (Sect. 4.1, p. 7).
- num: The results for the four PIFS subscales differed: income had the largest contribution to money shortage, while buffer savings had the largest contribution to lack of control and to financial worries and rumination; short-term focus was primarily influenced by the number of debts (Sect. 4.3, p. 8-9).

## Key Figures and Tables

- Figure 1 (p. 3): Conceptual framework → five economic factors predict financial stress, income moderates the other four, and the arrows do not suggest causation.
- Table 1 (p. 5): Operationalizations and descriptive statistics of the model variables → N and % for categorical variables, mean, SD, min and max for numerical variables.
- Table 2 (p. 6): PIFS items and subscales → 12 items across four subscales with alphas of .82, .88, .73, and .79.
- Table 3 (p. 6): Spearman correlations between the four PIFS subscales → inter-subscale correlations between .61 and .78.
- Table 4 (p. 9): Pooled robust regressions for Models 1-3 → standardized β, σ, t and p for the economic predictors, controls, and income interactions.
- Tables S1-S13 (supplemental materials): diagnostics, multicollinearity checks, marginal effects, and robustness and subscale analyses.

## Limitations and Gaps

- The authors acknowledge that the cross-sectional data did not allow causal inferences and call for experiments or quasi-experimental longitudinal studies (Sect. 5.1, p. 10).
- The authors report that they used self-reported economic data and suggest future research could use administrative data instead (Sect. 5.1, p. 10).
- The authors note that the data did not distinguish anticipated income changes from unanticipated ones, which may determine the strength of any association with financial stress (Sect. 5, p. 9).
- The authors state the study is set in the Dutch context and encourage examining the associations in other economic and cultural contexts (Sect. 5.1, p. 10).
- The authors acknowledge that other factors may contribute to financial stress, such as financial literacy, financial attitudes, and self-efficacy, which the model did not include (Sect. 5.1, p. 10).
- The authors explain the absent debt-amount association by noting that higher debts may not increase stress as long as interest and repayment can be paid, measures that were not available in the data (Sect. 5, p. 9).
- [unacknowledged] No confidence interval is reported for any coefficient or correlation; precision is conveyed only by standard errors, and the marginal-effect results are relegated to supplemental Table S6.
- [unacknowledged] The paper reports the Model 3 R2 two ways: the narrative states R2 = .36 (Sect. 4.2, p. 8), while the Table 4 header states R2 = .35 (Table 4, p. 9). Both are recorded in the Statistical Evidence table and are not reconciled here.
- [unacknowledged] Table 1 category counts do not sum to the analytical sample for several variables (Buffer 500, Number of debts 982, Gender 1102), and the employed categories sum to 1115 against a stated N of 1114, so item-level missingness and a one-case discrepancy are not reported in the table.
- [unacknowledged] The significance key in Table 4 labels ** as p < .005 (an unconventional threshold rather than p < .01), and several reported p-values (0.694, 0.484, 0.609, 0.797, 0.097) are not converted to the paper's own star notation.
- [unacknowledged] The missing-data share is large for some variables (41% for savings) and 49% of respondents had a missing value on at least one variable; the imputation assumes missingness at random, which is untested in the main text.

## Definitions

- **Financial stress** — "a psychological construct that reflects a state where pressing financial concerns surpass available resources, endangering well-being" (Sect. 1, p. 1).
- **PIFS (Psychological Inventory of Financial Scarcity)** — the 12-item financial stress measure developed by Van Dijk et al. (2022), with four components, M = 1.96, SD = 1.12, α = .93 (Sect. 3.2, p. 4).
- **Lack of money (subscale 1)** — appraisal of insufficient financial resources; three items, α = .82 (Table 2, p. 6).
- **Lack of control (subscale 2)** — appraisal of inability to deal adequately with the perceived threat; three items, α = .88 (Sect. 3.2, p. 4; Table 2, p. 6).
- **Financial worries and rumination (subscale 3)** — affective response to the perceived threat; three items, α = .73 (Sect. 3.2, p. 4; Table 2, p. 6).
- **Short-term focus (subscale 4)** — cognitive response to the perceived threat; three items, α = .79 (Sect. 3.2, p. 4; Table 2, p. 6).
- **Buffer** — a dichotomous variable equal to one if a household's liquid assets exceed the threshold € 600 + [monthly income] + € 400 * [household size], and zero otherwise (Sect. 3.3, p. 6).
- **Income** — net monthly household income adjusted by dividing by the square root of household size, following OECD (2013) guidelines (Sect. 3.3, p. 6).
- **Income volatility** — the number of months in which net income was lower than in the previous month, calculated over the last twelve months (Sect. 3.3, p. 7; Table 1, p. 5).
- **Number of debts** — the count of positive responses across five types of non-mortgage, non-student loan debt (Sect. 3.3, p. 6).
- **Employment** — a dichotomous variable equal to zero for job seekers after job loss, first-time job seekers, work disability, or unpaid work while retaining unemployment benefit, and one otherwise (Sect. 3.3, p. 7).
- **Prediction** — "the statistical process of estimating the value of one variable based on the values of other variables"; the paper states it does not imply causal relationships (footnote 5, p. 1).

## Key Equations

- `€ 600 + [monthly income] + € 400 * [household size]` — threshold above which a household is coded as having sufficient buffer (Sect. 3.3, p. 6).
- `(1+m) * VB / VT` — fraction of missing information lambda; m imputed datasets, VB between and VT total variance (Sect. 3.6, p. 7).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Analytical sample after removing eight empty surveys | respondents | 1114 | — | — | Sect. 3.1, p. 4 |
| Empty surveys removed | surveys | 8 | — | — | Sect. 3.1, p. 4 |
| Financial stress (PIFS, 12 items) | mean | 1.96 | — | — | Sect. 3.2, p. 4 |
| Financial stress (PIFS, 12 items) | SD | 1.12 | — | — | Sect. 3.2, p. 4 |
| Financial stress (PIFS, 12 items) | Cronbach's alpha | .93 | — | — | Sect. 3.2, p. 4 |
| PIFS subscale 1 (Lack of money) | Cronbach's alpha | .82 | — | — | Table 2, p. 6 |
| PIFS subscale 2 (Lack of control) | Cronbach's alpha | .88 | — | — | Table 2, p. 6 |
| PIFS subscale 3 (Financial worries and rumination) | Cronbach's alpha | .73 | — | — | Table 2, p. 6 |
| PIFS subscale 4 (Short-term focus) | Cronbach's alpha | .79 | — | — | Table 2, p. 6 |
| PIFS subscale correlations | range | .61 to .78 | — | — | Sect. 3.2, p. 6 |
| Money shortage with lack of control (PIFS subscales) | Spearman rho | .78 | — | — | Table 3, p. 6 |
| Money shortage with financial worries and rumination | Spearman rho | .67 | — | — | Table 3, p. 6 |
| Money shortage with short-term focus | Spearman rho | .70 | — | — | Table 3, p. 6 |
| Lack of control with financial worries and rumination | Spearman rho | .61 | — | — | Table 3, p. 6 |
| Lack of control with short-term focus | Spearman rho | .71 | — | — | Table 3, p. 6 |
| Financial worries and rumination with short-term focus | Spearman rho | .65 | — | — | Table 3, p. 6 |
| Female respondents | share | 55% | — | — | Sect. 4.1, p. 7 |
| Age | range | 18 to 92 | — | — | Sect. 4.1, p. 7 |
| Age | mean (SD) | 53.26 (17.78) | — | — | Sect. 4.1, p. 7 |
| Net monthly income | mean | 2800 euros | — | — | Sect. 4.1, p. 7 |
| Net monthly income | median | 2258 | — | — | Sect. 4.1, p. 7 |
| Net monthly income | SD | 7226 | — | — | Sect. 4.1, p. 7 |
| Missing values, savings | maximum share missing | 41% | — | — | Sect. 4.1, p. 7 |
| Missing values, all variables | total share missing | 9% | — | — | Sect. 4.1, p. 7 |
| Respondents missing at least one variable | respondents | 550 | — | — | Sect. 4.1, p. 7 |
| Respondents missing at least one variable | share | 49% | — | — | Sect. 4.1, p. 7 |
| Financial stress (PIFS) | mean (SD), min, max | 1.96 (1.12), 1.00, 7.00 | — | — | Table 1, p. 5 |
| Net income | mean (SD), min, max | 3048 (1645), 0, 12,114 | — | — | Table 1, p. 5 |
| Adjusted income | mean (SD), min, max | 2051 (916), 0, 6994 | — | — | Table 1, p. 5 |
| Savings (liquid) | mean (SD), min, max | 30,458 (67,978), −8000, 662,957 | — | — | Table 1, p. 5 |
| Debt amount | mean (SD), min, max | 2213.59 (18,100.36), 0, 320,000 | — | — | Table 1, p. 5 |
| Buffer = No | N (%) | 131 (26%) | — | — | Table 1, p. 5 |
| Buffer = Yes | N (%) | 369 (74%) | — | — | Table 1, p. 5 |
| Number of debts = 0 | N (%) | 872 (88.8%) | — | — | Table 1, p. 5 |
| Number of debts = 1 | N (%) | 99 (10.1%) | — | — | Table 1, p. 5 |
| Number of debts = 2 | N (%) | 8 (.8%) | — | — | Table 1, p. 5 |
| Number of debts = 3 | N (%) | 1 (.1%) | — | — | Table 1, p. 5 |
| Number of debts = 5 | N (%) | 2 (.2%) | — | — | Table 1, p. 5 |
| Employed = No | N (%) | 73 (6.5%) | — | — | Table 1, p. 5 |
| Employed = Yes | N (%) | 1042 (93.5%) | — | — | Table 1, p. 5 |
| Income volatility (adverse shocks) = 0 | N (%) | 921 (82.7%) | — | — | Table 1, p. 5 |
| Income volatility (adverse shocks) = 1 | N (%) | 156 (14.0%) | — | — | Table 1, p. 5 |
| Income volatility (adverse shocks) = 2 | N (%) | 28 (2.5%) | — | — | Table 1, p. 5 |
| Income volatility (adverse shocks) = 3 | N (%) | 7 (.6%) | — | — | Table 1, p. 5 |
| Age | mean (SD), min, max | 53.26 (17.78), 18, 92 | — | — | Table 1, p. 5 |
| Household size | mean (SD), min, max | 2.33 (1.25), 1, 9 | — | — | Table 1, p. 5 |
| Financial stress with buffer savings | point-biserial r | −.37 | — | — | Sect. 4.1, p. 7 |
| Financial stress with income | Spearman rho | −.30 | — | — | Sect. 4.1, p. 7 |
| Financial stress with number of debts | Spearman rho | .25 | — | — | Sect. 4.1, p. 7 |
| Financial stress with employment | point-biserial r | −.18 | — | — | Sect. 4.1, p. 7 |
| Financial stress with income volatility | Spearman rho | .05 | — | — | Sect. 4.1, p. 7 |
| Financial stress with age | Spearman rho | −.17 | — | — | Sect. 4.1, p. 7 |
| Financial stress with conscientiousness | Spearman rho | −.20 | — | — | Sect. 4.1, p. 7 |
| Financial stress with emotional stability | Spearman rho | −.20 | — | — | Sect. 4.1, p. 7 |
| Income with buffer | point-biserial r | −.26 | — | — | Sect. 4.1, p. 7 |
| Income with employment | point-biserial r | .17 | — | — | Sect. 4.1, p. 7 |
| Income with number of debts | Spearman rho | −.06 | — | — | Sect. 4.1, p. 7 |
| Income with income volatility | Spearman rho | .08 | — | — | Sect. 4.1, p. 7 |
| Model 1 (base economic predictors) | R2 | .29 | — | — | Sect. 4.2, p. 8 |
| Model 2 (plus control variables) | R2 | .34 | — | — | Sect. 4.2, p. 8 |
| Model 3 (plus interactions), narrative | R2 | .36 | — | — | Sect. 4.2, p. 8 |
| Model 3 (plus interactions), table header | R2 | .35 | — | — | Table 4, p. 9 |
| Model 2 vs Model 1 fit comparison | Wald W | 4.90 | — | <.001 | Sect. 4.2, p. 8 |
| Model 3 vs Model 2 fit comparison | Wald W | 2.97 | — | .019 | Sect. 4.2, p. 8 |
| Income-only model | R2 | .06 | — | — | Sect. 4.3, p. 8 |
| Model including all five economic factors | R2 | .29 | — | — | Sect. 4.3, p. 8 |
| Log financial stress model | R2 | .33 | — | — | Sect. 4.3, p. 8 |
| Liquid savings model (Table S9) | R2 | .29 | — | — | Sect. 4.3, p. 8 |
| Total debt amount model (Table S10) | R2 | .30 | — | — | Sect. 4.3, p. 8 |
| Debt-to-income ratio model (Table S11) | R2 | .30 | — | — | Sect. 4.3, p. 8 |
| Relative size of income shocks model (Table S12) | R2 | .35 | — | — | Sect. 4.3, p. 8 |
| Model 1 income | beta (S.E.) | −0.154*** (0.026) | — | <.001 | Table 4, p. 9 |
| Model 1 buffer | beta (S.E.) | −0.709*** (0.077) | — | <.001 | Table 4, p. 9 |
| Model 1 number of debts | beta (S.E.) | 0.238*** (0.029) | — | <.001 | Table 4, p. 9 |
| Model 1 income volatility | beta (S.E.) | 0.010 (0.025) | — | 0.694 | Table 4, p. 9 |
| Model 1 employed | beta (S.E.) | −0.506*** (0.104) | — | <.001 | Table 4, p. 9 |
| Model 2 income | beta (S.E.) | −0.150*** (0.028) | — | <.001 | Table 4, p. 9 |
| Model 2 buffer | beta (S.E.) | −0.682*** (0.076) | — | <.001 | Table 4, p. 9 |
| Model 2 number of debts | beta (S.E.) | 0.232*** (0.028) | — | <.001 | Table 4, p. 9 |
| Model 2 income volatility | beta (S.E.) | −0.018 (0.025) | — | 0.484 | Table 4, p. 9 |
| Model 2 employed | beta (S.E.) | −0.431*** (0.103) | — | <.001 | Table 4, p. 9 |
| Model 2 age | beta (S.E.) | −0.127*** (0.028) | — | <.001 | Table 4, p. 9 |
| Model 2 gender | beta (S.E.) | −0.137* (0.055) | — | 0.013 | Table 4, p. 9 |
| Model 2 household size | beta (S.E.) | −0.056* (0.026) | — | 0.031 | Table 4, p. 9 |
| Model 3 income | beta (S.E.) | −0.612*** (0.168) | — | <.001 | Table 4, p. 9 |
| Model 3 buffer | beta (S.E.) | −0.653*** (0.077) | — | <.001 | Table 4, p. 9 |
| Model 3 number of debts | beta (S.E.) | 0.224*** (0.030) | — | <.001 | Table 4, p. 9 |
| Model 3 income volatility | beta (S.E.) | −0.013 (0.025) | — | 0.609 | Table 4, p. 9 |
| Model 3 employed | beta (S.E.) | −0.230. (0.138) | — | 0.097 | Table 4, p. 9 |
| Model 3 income × savings | beta (S.E.) | 0.127. (0.076) | — | 0.097 | Table 4, p. 9 |
| Model 3 income × debt amount | beta (S.E.) | −0.009 (0.034) | — | 0.797 | Table 4, p. 9 |
| Model 3 income × income volatility | beta (S.E.) | 0.051. (0.026) | — | 0.05 | Table 4, p. 9 |
| Model 3 income × employed | beta (S.E.) | 0.370* (0.162) | — | 0.023 | Table 4, p. 9 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "We found that the combination of economic factors predicted financial stress better than income alone. Particularly, buffer savings had a large contribution to predicting financial stress." | Abstract, p. 1 | savings_debt_management |
| "The number of debts had a smaller relative contribution to predicting financial stress, whereas we did not find support for debt amount as a predictor of financial stress." | Abstract, p. 1 | savings_debt_management |
| "Employment was negatively associated with financial stress, but only for households with the lowest incomes. We found no support for income volatility predicting financial stress." | Abstract, p. 1 | income_expense_management |
| "Savings may serve as buffers against unexpected expenditures and income shocks, and this could protect against financial stress." | Sect. 2.1, p. 3 | savings_debt_management |
| "We included the amount of household liquid savings in our analyses and excluded other types of wealth, such as real estate and long-term investments." | Sect. 3.3, p. 6 | savings_debt_management |
| "Given that the number of debts is more predictive of financial stress than the total debt amount, we included the number of debts as an independent variable in our analysis." | Sect. 3.3, p. 6 | savings_debt_management |
| "We defined buffer as a dichotomous variable equaling one if a household's liquid assets exceeded a threshold depending on income and household size and zero otherwise." | Sect. 3.3, p. 6 | savings_debt_management |
| "We found that the number of debts, but not debt amounts, predicted financial stress." | Sect. 5, p. 9 | savings_debt_management |
| "This finding suggests a buffer is essential for both lower- and higher-income households to prevent financial stress." | Sect. 5, p. 9 | savings_debt_management |
| "Our results corroborated previous research, indicating that lower-income households are more likely to experience having too few financial resources." | Sect. 5, p. 9 | income_expense_management |
| "We found that employment only predicted financial stress for the lowest-income groups." | Sect. 5, p. 9 | income_expense_management |
| "This study's central message is that income is too narrow to conceptualize one's economic situation to predict financial stress." | Sect. 5.2, p. 10 | income_expense_management |
| "The results showed that less buffer savings, more debts, and unemployment also predicted more financial stress." | Sect. 5.3, p. 11 | savings_debt_management |

## Remember This

- Financial stress has four components: money shortage, lack of control, financial worries and rumination, and short-term focus.
- Buffer savings had the largest relative contribution; income, number of debts, and employment also predicted financial stress.
- Number of debts predicted financial stress, but debt amount and debt-to-income ratio did not.
- Income volatility did not predict financial stress; employment predicted it only at the lowest income level.
- Cross-sectional self-report data, so associations are not causal; no confidence intervals are reported.

## Cited Works

- Van Dijk et al. (2022) (methodology) — provided the 12-item PIFS measure and the paper's definition of financial stress [p. 4]
- Mullainathan and Shafir (2013) (context) — financial stress arises in financially challenging circumstances and describes the "slack" households experience [pp. 1, 10]
- Ruberton et al. (2016) (finding) — a financial buffer contributes to financial well-being; minimal savings matter more than wealth above sufficiency [p. 4]
- Ariely et al. (2009); Ong et al. (2019) (finding) — the number of debts is more predictive of financial stress than the total debt amount [pp. 3, 4]
- Prelec and Loewenstein (1998) (finding) — people keep each loan in a separate mental account, so each debt's first dollars create the most mental load [p. 3]
- Tay et al. (2017) (finding) — debt affects well-being through financial well-being and a strain on financial resources, and the debt-stress link may be stronger for lower-income households [pp. 3-4]
- Gennetian and Shafir (2015) (critique) — prior evidence that income volatility increases financial stress, which this study did not reproduce [p. 9]
- Yohai (1987) (methodology) — the MM-estimator used for robust regression [p. 7]
- Meng and Rubin (1982) (methodology) — the adapted Wald statistic used to compare multiply-imputed model fits [p. 8]
- Von Hippel (2020) (methodology) — guidance used to set the number of imputations at 93 [p. 7]
- Goldberg (1992) (methodology) — the Big Five personality index used for the control variables [p. 4]
- Brüggen et al. (2017) (context) — definition of financial well-being contrasted with financial stress [p. 1]
- Xiao and Kim (2022) (finding) — debt delinquency is associated with financial stress [p. 3]
- Cook and Sadeghein (2018) (context) — households with financial stress may underestimate the cost of borrowing and overborrow [p. 3]
- Lusardi and Mitchell (2014); Dare et al. (2021) (context) — financial literacy, attitudes, and self-efficacy as factors the paper did not include [p. 9]

---
Conversion: [`Simonse et al., 2024_marked.md`](../../literature/mds/Simonse et al., 2024_marked.md)
