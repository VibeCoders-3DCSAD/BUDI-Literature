---
paper_id: I--Sohilauw-2026
first_author: Sohilauw
year: 2026
title: "Income, Saving Behavior, and Household Financial Decision-Making: A Moderated-Mediation Analysis of Behavioral and Economic Factors in Indonesia"
venue: "Journal of Economics, Entrepreneurship, Management Business and Accounting"
doi: 10.61255/jeemba.v4i4.844

designation: international
status: extracted
modules: [financial_planning, savings_debt_management, income_expense_management, budgeting]
module_rationale:
  financial_planning: "The dependent variable is household financial decision-making (Y₂) and the stated purpose is 'the roles of income and saving behavior in household financial decision-making' (Abstract, p. 1)."
  savings_debt_management: "Saving behavior (X₂) is the dominant predictor, the moderator, and the antecedent of the mediation path, with emergency funds, liquidity buffers and debt management among its measured indicators (Sect. 3, p. 12; Appendix H, p. 28)."
  income_expense_management: "Income (X₁) is measured through income adequacy, stability and price sensitivity, and the paper discusses allocating income across consumption, saving and investment (Sect. 3 Discussion, p. 11; Appendix H, p. 27)."
  budgeting: "Budget discipline is prescribed as the practical lever — 'Structured budgeting practices that prioritize regular saving alongside daily consumption' (Suggestions, p. 15) — and Y12 measures 'Budgeting ability' (Appendix H, p. 28)."
---

# I--Sohilauw-2026 — Income, Saving Behavior, and Household Financial Decision-Making

## Summary

A survey-based moderated-mediation study of 500 economically active working adults in Makassar City, Indonesia, testing how income (X₁) and saving behavior (X₂) shape household financial decision-making (Y₂), with financial risk management (Y₁) as the mediator and saving behavior as the moderator of the income→decision path. Because all items are five-point Likert responses and Shapiro–Wilk tests flag every observed item as non-normal (p < 0.05), the authors abandon covariance-based SEM and use composite scores, ordinary least squares, robust MM regression, nonparametric bootstrapping with 1,000 resamples, and 70/30 hold-out plus five-fold cross-validation. Saving behavior is the strongest predictor of both financial risk management (β = 0.520, p < 0.001) and household financial decision-making (β = 0.604, p < 0.001); income contributes positively but more weakly (β = 0.398, p < 0.001). The income × saving behavior interaction is significant and negative (β = −0.267, p < 0.001), and the moderated model reaches an adjusted R² of 0.628. Mediation through financial risk management is statistically significant for both predictors but carries a negative sign (ACME = −0.111 for saving behavior; ACME = −0.064 for income).

## Problem and Motivation

Household financial decisions are conventionally explained by economic capacity, with income treated as the main determinant of how funds are allocated. The authors argue that in emerging economies this framing misses the social and cultural pressures that make household finance non-optimal in the market sense: culturally embedded expenditures such as Mudik, the Eid al-Fitr homecoming tradition, demand substantial resources within a short period and reflect emotional bonds, family solidarity and social identity, so household financial managers must plan liquidity, follow disciplined budgets and anticipate risk to meet social obligations without undermining long-term well-being (Sect. 1, p. 2). Mudik is used as an illustrative example rather than a measured variable (Sect. 1, p. 2).

Three gaps are named. First, income and saving behavior are usually treated as independent, additive predictors, which assumes that higher economic capacity automatically produces better decisions and overlooks how behavioral discipline governs the use of resources under normative pressure. Second, financial risk management is typically modelled as an end-point outcome rather than as the mechanism that channels disciplined saving into structured decision-making. Third, many empirical studies rely on covariance-based models that prioritise overall fit, which reduces predictive accuracy and weakens estimated relationships when survey data are ordinal or non-normal (Sect. 1, p. 2).

The framework is built on three theories: the Life-Cycle Hypothesis (income as an intertemporal resource guiding consumption and saving), Behavioral Life-Cycle Theory (self-control and mental accounting as enablers of disciplined allocation), and the Theory of Planned Behavior (perceived behavioral control and intention as determinants of structured action under normative pressure) (Sect. 1, p. 3). The claimed contribution is a capacity–discipline interaction framework showing that the marginal effect of income depends on saving discipline, a clarification of financial risk management as mediator, and a demonstration of robust predictive modelling for behavioral financial data (Sect. 1, p. 3).

## Method

**Design.** Quantitative explanatory design using a composite-based, prediction-oriented analytical strategy; the authors state the label explicitly ("This study employs a quantitative explanatory design", Sect. 2, p. 3) and describe the approach as "a predictive composite modeling approach combining robust MM estimation and cross-validated regression" (Abstract, p. 1). No other formal design label (e.g., cross-sectional survey, quasi-experimental) is stated.
**Sample.** N = 500 working individuals; the unit of analysis is the individual economically active adult who earns income and is directly involved in managing household finances, with behaviours measured treated as reflecting household-level financial decision processes (Sect. 2, p. 4).
**Context.** geography: Makassar City, Indonesia; population: economically active working adults who are income earners within their households, including native residents and migrants who live and work in the city, some of whom maintain socio-economic ties and financial obligations to places of origin outside Makassar; setting: a structured questionnaire administered directly to respondents, with five-point Likert items, analysed in RStudio with Microsoft Excel used for coding, missing-value checking and dataset formatting (Sect. 2, pp. 4, 7).

Procedure, in the paper's own order:

- Assess internal consistency with Cronbach's alpha, then extend to inter-item correlation analysis to detect negative or very low correlations and items that weaken construct homogeneity (Sect. 2, p. 5).
- Purify constructs at the correlational level rather than by factor loadings, reducing measurement noise before structural estimation (Sect. 2, p. 5).
- Operationalise each construct as a composite index equal to the mean of its retained indicators, X_k = (1 / p_k) Σ x_ik, where p_k is the number of retained items (Sect. 2, p. 5).
- Estimate the first-stage mediation model Y₁ = α₀ + α₁X₁ + α₂X₂ + ϵ; the main structural model Y₂ = β₀ + β₁X₁ + β₂X₂ + β₃Y₁ + u; and the moderation model Y₂ = β₀ + β₁X₁ + β₂X₂ + β₃(X₁ × X₂) + β₄Y₁ + u (Sect. 2, p. 5).
- Compute indirect effects as IE = α × β and test them with nonparametric bootstrapping (1,000 resamples) and bootstrap confidence intervals rather than a normality assumption (Sect. 2, p. 6; Sect. 3, p. 9).
- Re-estimate the main structural model with robust MM regression, chosen for its high breakdown point and strong efficiency under heteroskedasticity and influential observations (Sect. 2, p. 6).
- Evaluate generalisability with a 70/30 hold-out split and k-fold cross-validation, reporting RMSE and MAE (Sect. 2, p. 6; Sect. 3, p. 10).
- Report Shapiro–Wilk normality diagnostics for all 20 observed items, VIF/tolerance, univariate outlier screening at |Z| > 3, CFA fit indices, a composite-level Pearson correlation matrix, and the full structural estimation tables in Appendices B–G (pp. 23–27).

Retained-measure notes that affect interpretation:

- The outcome construct Y₂ was initially five items with α = 0.565; items Y23, Y24 and Y25 were removed for weak or negative inter-item correlations, leaving Y21 and Y22 with α = 0.822 (Sect. 3, p. 8; Table C1 and C2, p. 24).
- The retained Y₂ indicators are described by the authors as capturing "the normative–emotional dimension of household financial decision-making" rather than the full multidimensional construct (Sect. 3, p. 8).
- CFA for X₁ and X₂ produced poor global fit (CFI = 0.651; TLI = 0.538; RMSEA = 0.241), which is the stated reason for switching to composite scores in the regression analyses (Table C3, pp. 24–25).

## Software

- RStudio (version not reported) — all regression, mediation and moderation analysis (Sect. 2, p. 7).
- Microsoft Excel (version not reported) — data preparation, variable coding, missing-value checking, dataset formatting (Sect. 2, p. 7).
- Robust MM regression estimators (Maronna et al., 2018; Yohai, 1987) (Sect. 2, p. 6).
- Nonparametric bootstrapping with 1,000 resamples, following Preacher and Hayes (2008) (Sect. 2, p. 6; Sect. 3, p. 9).
- Five-point Likert questionnaire instrument; no survey platform, sampling software, or code repository is reported.

## Key Findings

- Saving behavior (X₂) is the strongest predictor of household financial decision-making, β = 0.604, p < 0.001 (Table 1, p. 10), and of financial risk management, β = 0.520, p < 0.001 (Table 1, p. 10).
- Income (X₁) positively predicts household financial decision-making, β = 0.398, p < 0.001 (Table 1, p. 10), and financial risk management, β = 0.301, p < 0.001 (Sect. 3 Discussion, p. 11).
- The income × saving behavior interaction is significant and negative, β = −0.267, p < 0.001, and is read as income's marginal effect shrinking as saving discipline rises (Sect. 3, p. 9; Table 1, p. 10).
- The baseline OLS model explains R² = 0.538 of household financial decision-making; the moderated robust MM model raises adjusted R² to 0.628 (Sect. 3, pp. 8–9).
- Effect sizes are large for saving behavior (f² = 0.524), medium for income (f² = 0.201), small for financial risk management (f² = 0.056) and small for the interaction (f² = 0.074) (Sect. 3, p. 9).
- Mediation through financial risk management is statistically significant for saving behavior (ACME = −0.111, 95% CI −0.148 to −0.074, p < 0.001) and for income (ACME = −0.064, 95% CI −0.097 to −0.036, p < 0.001); both indirect effects are negative, which the authors attribute to a negative estimated path from financial risk management to decision-making (Table E3, p. 26; Sect. 3, pp. 9, 13).
- Predictive validation is reported as low overfitting risk: hold-out RMSE = 0.715, five-fold mean RMSE = 0.680, mean MAE = 0.570, Durbin–Watson = 2.11 with p > 0.05, while Breusch–Pagan = 38.37 with p < 0.001 flags heteroskedasticity (Sect. 3, p. 10; Table F, p. 27).
- All five stated hypotheses are reported as supported (Table 1, p. 10).
- Practical recommendations are behavioural rather than income-raising: strengthen saving discipline, integrate risk management (emergency funds, liquidity, contingency plans), and offer structured saving instruments such as automatic savings accounts and commitment-based programmes (Suggestions, pp. 15–16).
- The paper frames its novelty as the dual role of saving behavior as both dominant predictor and moderator, and as evidence that "higher income alone does not guarantee better financial decisions without disciplined saving behavior" (Sect. 3 Novelty, p. 10).

## Key Figures and Tables

- Figure 1 (p. 7): Conceptual framework — Income (X₁) and Saving Behaviour (X₂) feed Household Financial Decision Making (Y₂), with Financial Risk Management (Y₁) as the mediating box; the figure is printed with a caption typo ("Conteptual Framework (2025)") and a garbled layout in the source.
- Figure A1 (p. 26): Interaction effects, referenced in the text as illustrating the moderation result but not accompanied by any printed values.
- Figure A2 (p. 26): Mediation results, referenced in the text as illustrating the mediation result but not accompanied by any printed values.
- Table 1 (p. 10): Hypothesis Result — five hypotheses, all "Supported", with statistics β = 0.398, β = 0.604, β = 0.520, ACME = −0.111 and β = −0.267, each at p < 0.001.
- Table A1 (p. 23): Means, standard deviations and ranges of the 20 indicators, plus pooled ranges for Y11–Y15 and Y21–Y25.
- Table B1 (p. 23): Shapiro–Wilk normality tests for all 20 items, every one "Not normal" with p < 0.001.
- Table B2 (p. 24): VIF (1.32 for both X₁ and X₂) and tolerance (0.758), interpreted as no multicollinearity.
- Table B3 (p. 24): Univariate outlier screening — 500 observations per composite, zero outliers at |Z| > 3 for all four constructs.
- Table C1 (p. 24): Internal consistency — 0.759, 0.835, 0.814 for X₁, X₂, Y₁ and 0.822 for the two-item Y₂.
- Table C2 (p. 24): Inter-item correlation matrix for Y₂, showing the 0.71 Y21–Y22 correlation that justifies retaining only those two items.
- Table C3 (pp. 24–25): CFA fit for X₁ and X₂ — CFI 0.651, TLI 0.538, RMSEA 0.241, all "Poor fit".
- Table D (p. 25): Composite-level Pearson correlations, 0.41 to 0.67.
- Table E1 (p. 25): Baseline OLS models for Y₁ and Y₂_clean with coefficients, R², adjusted R², F-statistic and observations.
- Table E2 (p. 25): Full moderation model under robust MM with β values and Cohen's f² effect sizes.
- Table E3 (p. 26): Mediation analysis with ACME, 95% CI, ADE, total effect, proportion mediated and p-value for both predictors.
- Table E4 (pp. 26–27): Model comparison summary — baseline 0.54, full moderation 0.63, sensitivity (no interaction) 0.54.
- Table F (p. 27): Robustness and predictive validation — Breusch–Pagan, Durbin–Watson, hold-out RMSE, cross-validated mean RMSE and mean MAE.
- Table G (p. 27): Sensitivity analysis under three alternative specifications, all reported as substantively unchanged.
- Appendix H (pp. 27–28): Operational definitions of all 20 indicators and their source citations.

## Limitations and Gaps

Acknowledged by the authors:

- Cross-sectional data limit the ability to establish causal relationships among income, saving behavior, financial risk management and household financial decision-making; longitudinal studies are recommended (Limitations, p. 16).
- Contextual factors — cultural norms, extended family obligations, traditions such as mudik — shape spending priorities, saving patterns and risk management and may limit generalisability beyond Makassar City (Limitations, p. 16).
- The study is confined to a specific geographic and socio-economic setting; variations in regional economic conditions, income distribution, financial literacy and access to financial institutions may change household financial behavior elsewhere (Limitations, p. 16).
- The retained Y₂ indicators capture only the normative–emotional dimension of household financial decision-making, not the full multidimensional construct (Sect. 3, p. 8).

Not acknowledged by the authors:

- [unacknowledged] The effect of saving behavior on household financial decision-making is printed as β = 0.604 (Table 1, p. 10), β = 0.66 (Table E2, p. 25) and β ≈ 0.69 standardized (Sect. 3 Discussion, p. 12). Three values for the same claim are never reconciled, and only the 0.604 value carries a p-value.
- [unacknowledged] The moderation section states that "The model's adjusted R² increased from 0.538 to 0.628" (p. 13), but 0.538 is the baseline R² and the baseline adjusted R² is 0.535 (Table E1, p. 25); Table E4 rounds the same quantities to 0.54 and 0.63. The paper treats R² and adjusted R² as interchangeable in that sentence.
- [unacknowledged] The abstract states "The model explains 62.8% of the variance in household financial decision-making" without indicating that 0.628 is the adjusted R² of the moderated model and that the unadjusted R² is not reported for that model.
- [unacknowledged] The mediation is described as "partial mediation" and as evidence that disciplined saving improves outcomes through risk management, yet both ACMEs are negative and the paper never explains how a negative indirect effect supports the stated H3 direction, nor what a negative "proportion mediated" (−0.193 and −0.226) means.
- [unacknowledged] The CFA for X₁ and X₂ shows poor fit on every reported index (CFI 0.651, TLI 0.538, RMSEA 0.241) yet the constructs are carried into regression as composites; no discriminant validity evidence beyond the correlation matrix is offered.
- [unacknowledged] The measurement model for the outcome is thin: three of five Y₂ items were dropped after seeing the data, leaving a two-item outcome whose alpha (0.822) is reported only for the purified set, while the unreported initial alpha of 0.565 is disclosed but never used for sensitivity.
- [unacknowledged] Income is measured only as Likert-scale perceptions (adequacy of current income, employment and income stability, price sensitivity, sustainability of income sources, access to seasonal additional income; Appendix H, p. 27). No monetary income figure, bracket, or objective income record appears, so "income" in the model is perceived income adequacy, not actual income.
- [unacknowledged] No sampling method is described: there is no sampling frame, recruitment procedure, response rate, or comparison of respondents with non-respondents (Sect. 2, pp. 4, 7). "Checking for missing values" is mentioned for Excel but no missing-data count or treatment is reported.
- [unacknowledged] No demographic profile of the 500 respondents is reported anywhere — no age, sex, education, occupation, household size or income distribution — although these are the natural moderators for the paper's own cultural argument.
- [unacknowledged] The unit of analysis is the individual while all claims are about households; the paper asserts that measured behaviours "reflect household-level financial decision-making processes" (Sect. 2, p. 4) without any household-level validation or dyadic data.
- [unacknowledged] Mudik is introduced as the motivating cultural mechanism but is never operationalised or measured, so the cultural-pressure argument is asserted, not tested; the paper itself notes it is "used as an illustrative example" only (Sect. 1, p. 2).
- [unacknowledged] Table 1 reports no confidence intervals and no exact p-values (only p < 0.001); the only interval estimates in the paper are the two bootstrap CIs in Table E3.
- [unacknowledged] Breusch–Pagan = 38.37 with p < 0.001 confirms heteroskedasticity in the OLS specification, yet no heteroskedasticity-robust standard errors or re-specified variance model are reported for the structural coefficients.
- [unacknowledged] No sensitivity analysis is reported for the mediation, only for the moderation (Table G, p. 27), and Table G reports no numbers — only qualitative statements that "coefficient signs remain consistent" and "results remain substantively unchanged".

## Definitions

- **Income (X₁)** — measured with five indicators: current income level, employment status and income stability, sensitivity to prices and costs, sustainability of income sources, and access to seasonal additional income (Appendix H, p. 27).
- **Saving behavior (X₂)** — measured with five indicators: saving goals (short- and long-term), financial literacy in saving decisions, cultural values in saving habits, social pressure in saving, and adaptive saving behaviour under economic risk (Appendix H, pp. 27–28).
- **Financial risk management (Y₁)** — measured with five indicators: availability of emergency funds, budgeting ability, debt management, financial risk management during travel, and response to macroeconomic conditions (Appendix H, p. 28).
- **Household financial decision-making (Y₂)** — initially five indicators (emotional motivation to reunite, cultural obligation and traditional values, rational cost–benefit decision-making, financial readiness, accessibility of transportation and infrastructure); purified to the two retained items Y21 and Y22 (Appendix H, p. 28; Sect. 3, p. 8).
- **Y₂_clean** — the refined two-item construct used as the dependent variable in all structural models (Sect. 3, p. 8).
- **Composite score** — the mean of a construct's purified indicators, X_k = (1 / p_k) Σ x_ik (Sect. 2, p. 5).
- **Robust MM estimation** — regression estimation combining a high breakdown point with strong efficiency, used to resist heteroskedasticity and influential observations (Sect. 2, p. 6).
- **ACME / ADE** — Average Causal Mediation Effect (indirect effect) and Average Direct Effect from the bootstrap mediation procedure (Table E3 notes, p. 26).
- **Mudik** — the Eid al-Fitr homecoming tradition in Indonesia, used in this paper as an illustration of culturally embedded expenditure pressure rather than as a measured variable (Sect. 1, p. 2).

## Key Equations

- `X_k = (1 / p_k) Σ_(i=1)^(p_k) x_ik` — composite construct score as the mean of retained indicators (Sect. 2, p. 5).
- `Y₁ = α₀ + α₁ X₁ + α₂ X₂ + ϵ` — first-stage mediation model, predictors to financial risk management (Sect. 2, p. 5).
- `Y₂ = β₀ + β₁ X₁ + β₂ X₂ + β₃ Y₁ + u` — main structural model for household financial decision-making (Sect. 2, p. 5).
- `Y₂ = β₀ + β₁ X₁ + β₂ X₂ + β₃ (X₁ × X₂) + β₄ Y₁ + u` — moderation model adding the income × saving behavior interaction (Sect. 2, p. 5).
- `IE = α × β` — indirect effect as the product of the predictor-to-mediator and mediator-to-outcome paths (Sect. 2, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Income (X₁) construct | Cronbach's alpha | 0.759 | — | — | Sect. 3, p. 8; Table C1, p. 24 |
| Saving behavior (X₂) construct | Cronbach's alpha | 0.835 | — | — | Sect. 3, p. 8; Table C1, p. 24 |
| Financial risk management (Y₁) construct | Cronbach's alpha | 0.814 | — | — | Sect. 3, p. 8; Table C1, p. 24 |
| Household financial decision-making (Y₂), initial five-item specification | Cronbach's alpha | 0.565 | — | — | Sect. 3, p. 8; Table C1, p. 24 |
| Household financial decision-making (Y₂_clean), two retained items | Cronbach's alpha | 0.822 | — | — | Sect. 3, p. 8; Table C1, p. 24 |
| First-stage mediation model, financial risk management (Y₁) | R² | 0.515 | — | — | Sect. 3, p. 8; Table E1, p. 25 |
| First-stage mediation model, financial risk management (Y₁) | adjusted R² | 0.513 | — | — | Table E1, p. 25 |
| First-stage mediation model, financial risk management (Y₁) | F-statistic | 264.2*** | — | — | Table E1, p. 25 |
| First-stage mediation model, income (X₁) | coefficient | 0.301*** | — | — | Table E1, p. 25 |
| First-stage mediation model, saving behavior (X₂) | coefficient | 0.520*** | — | — | Table E1, p. 25 |
| Baseline OLS structural model, household financial decision-making (Y₂_clean) | R² | 0.538 | — | — | Sect. 3, p. 9; Table E1, p. 25 |
| Baseline OLS structural model, household financial decision-making (Y₂_clean) | adjusted R² | 0.535 | — | — | Table E1, p. 25 |
| Baseline OLS structural model, household financial decision-making (Y₂_clean) | F-statistic | 192.1*** | — | — | Table E1, p. 25 |
| Baseline OLS structural model, income (X₁) | coefficient | 0.398*** | — | — | Table E1, p. 25 |
| Baseline OLS structural model, saving behavior (X₂) | coefficient | 0.604*** | — | — | Table E1, p. 25 |
| Baseline OLS structural model, financial risk management (Y₁) | coefficient | -0.214*** | — | — | Table E1, p. 25 |
| Moderated structural model (robust MM), income × saving behavior | β | -0.267 | — | <0.001 | Sect. 3, p. 9; Table E2, p. 25 |
| Moderated structural model (robust MM), income (X₁) | β | 0.433 | — | — | Table E2, p. 25 |
| Moderated structural model (robust MM), saving behavior (X₂) | β | 0.66 | — | — | Table E2, p. 25 |
| Moderated structural model (robust MM), financial risk management (Y₁) | β | -0.25 | — | — | Table E2, p. 25 |
| Moderated structural model (robust MM) | adjusted R² | 0.628 | — | — | Sect. 3, p. 9; Table E2, p. 25 |
| Effect size, income (X₁) | Cohen's f² | 0.201 | — | — | Sect. 3, p. 9; Table E2, p. 25 |
| Effect size, saving behavior (X₂) | Cohen's f² | 0.524 | — | — | Sect. 3, p. 9; Table E2, p. 25 |
| Effect size, income × saving behavior (X₁ × X₂) | Cohen's f² | 0.074 | — | — | Sect. 3, p. 9; Table E2, p. 25 |
| Effect size, financial risk management (Y₁) | Cohen's f² | 0.056 | — | — | Sect. 3, p. 9; Table E2, p. 25 |
| H1 income (X₁) → household financial decision-making (Y₂) | β | 0.398 | — | <0.001 | Table 1, p. 10 |
| H2a saving behavior (X₂) → household financial decision-making (Y₂) | β | 0.604 | — | <0.001 | Table 1, p. 10 |
| H2b saving behavior (X₂) → financial risk management (Y₁) | β | 0.520 | — | <0.001 | Table 1, p. 10 |
| H3 financial risk management mediates saving behavior → Y₂ | ACME | -0.111 | — | <0.001 | Table 1, p. 10 |
| H4 saving behavior moderates income → Y₂ | β | -0.267 | — | <0.001 | Table 1, p. 10 |
| Income (X₁) → financial risk management (Y₁), discussion text | β | 0.301 | — | <0.001 | Sect. 3 Discussion, p. 11 |
| Saving behavior (X₂) → household financial decision-making (Y₂), standardized coefficient, discussion text | β | ≈ 0.69 | — | — | Sect. 3 Discussion, p. 12 |
| Mediation X₁ → Y₁ → Y₂ | ACME (indirect effect) | -0.064 | -0.097 to -0.036 | <0.001 | Table E3, p. 26 |
| Mediation X₁ → Y₁ → Y₂ | ADE (direct effect) | 0.398 | — | — | Table E3, p. 26 |
| Mediation X₁ → Y₁ → Y₂ | total effect | 0.334 | — | — | Table E3, p. 26 |
| Mediation X₁ → Y₁ → Y₂ | proportion mediated | -0.193 | — | — | Table E3, p. 26 |
| Mediation X₂ → Y₁ → Y₂ | ACME (indirect effect) | -0.111 | -0.148 to -0.074 | <0.001 | Table E3, p. 26 |
| Mediation X₂ → Y₁ → Y₂ | ADE (direct effect) | 0.604 | — | — | Table E3, p. 26 |
| Mediation X₂ → Y₁ → Y₂ | total effect | 0.492 | — | — | Table E3, p. 26 |
| Mediation X₂ → Y₁ → Y₂ | proportion mediated | -0.226 | — | — | Table E3, p. 26 |
| Residual autocorrelation | Durbin–Watson statistic | 2.11 | — | >0.05 | Sect. 3, p. 10; Table F, p. 27 |
| Heteroskedasticity | Breusch–Pagan statistic | 38.37 | — | <0.001 | Table F, p. 27 |
| Hold-out validation (70/30) | RMSE | 0.715 | — | — | Sect. 3, p. 10; Table F, p. 27 |
| Five-fold cross-validation | mean RMSE | 0.680 | — | — | Sect. 3, p. 10; Table F, p. 27 |
| Five-fold cross-validation | mean MAE | 0.570 | — | — | Sect. 3, p. 10; Table F, p. 27 |
| Multicollinearity, income (X₁) | VIF | 1.32 | — | — | Table B2, p. 24 |
| Multicollinearity, saving behavior (X₂) | VIF | 1.32 | — | — | Table B2, p. 24 |
| Multicollinearity, income (X₁) and saving behavior (X₂) | tolerance | 0.758 | — | — | Table B2, p. 24 |
| CFA global fit for constructs X₁ and X₂ | CFI | 0.651 | — | — | Table C3, p. 24 |
| CFA global fit for constructs X₁ and X₂ | TLI | 0.538 | — | — | Table C3, p. 24 |
| CFA global fit for constructs X₁ and X₂ | RMSEA | 0.241 | — | — | Table C3, p. 25 |
| Composite correlation, income (X₁) – saving behavior (X₂) | Pearson r | 0.49 | — | — | Table D, p. 25 |
| Composite correlation, income (X₁) – financial risk management (Y₁) | Pearson r | 0.56 | — | — | Table D, p. 25 |
| Composite correlation, income (X₁) – Y₂_clean | Pearson r | 0.58 | — | — | Table D, p. 25 |
| Composite correlation, saving behavior (X₂) – financial risk management (Y₁) | Pearson r | 0.67 | — | — | Table D, p. 25 |
| Composite correlation, saving behavior (X₂) – Y₂_clean | Pearson r | 0.66 | — | — | Table D, p. 25 |
| Composite correlation, financial risk management (Y₁) – Y₂_clean | Pearson r | 0.41 | — | — | Table D, p. 25 |
| Inter-item correlation, Y21 – Y22 (retained outcome items) | Pearson r | 0.71 | — | — | Table C2, p. 24 |
| Model comparison, baseline (OLS) | R² | 0.54 | — | — | Table E4, p. 26 |
| Model comparison, full moderation | R² | 0.63 | — | — | Table E4, p. 27 |
| Model comparison, sensitivity (no interaction) | R² | 0.54 | — | — | Table E4, p. 27 |
| Sample size | N | 500 | — | — | Sect. 2, p. 4 |
| Outliers detected on all four composites (\|Z\| > 3) | count | 0 | — | — | Table B3, p. 24 |
| Income (X₁) composite | mean | 4.24 | — | — | Table B3, p. 24 |
| Saving behavior (X₂) composite | mean | 3.83 | — | — | Table B3, p. 24 |
| Financial risk management (Y₁) composite | mean | 4.15 | — | — | Table B3, p. 24 |
| Household financial decision-making (Y₂) composite | mean | 4.07 | — | — | Table B3, p. 24 |
| Normality of all 20 observed items | Shapiro–Wilk W | 0.92–0.97 | — | <0.001 | Table B1, p. 23 |
| Indicator X11 (current income level) | mean | 4.32 | — | — | Table A1, p. 23 |
| Indicator X11 (current income level) | SD | 0.74 | — | — | Table A1, p. 23 |
| Indicator X24 (social pressure in saving) | mean | 3.48 | — | — | Table A1, p. 23 |
| Indicator X25 (adaptive saving behaviour under economic risk) | mean | 4.39 | — | — | Table A1, p. 23 |

Note on significance markers: Table E1 and Table E2 print asterisks (`***`) rather than numeric p-values; the asterisks are reproduced in the Value cell exactly as printed and no p-value is entered in the `p` column.

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This study examines the roles of income and saving behavior in household financial decision-making, with financial risk management as an intervening factor." | Abstract, p. 1 | financial_planning |
| "The results show that saving behavior has a strong positive effect on household financial decision-making and financial risk management." | Abstract, p. 1 | savings_debt_management |
| "The model explains 62.8% of the variance in household financial decision-making." | Abstract, p. 1 | financial_planning |
| "The findings suggest that strengthening saving behavior and financial risk management is more effective than relying on income alone." | Abstract, p. 1 | savings_debt_management |
| "Culturally embedded expenditures, such as Mudik, the Eid al-Fitr homecoming tradition in Indonesia, illustrate this dynamic." | Sect. 1, p. 2 | income_expense_management |
| "Individuals responsible for household finances must therefore carefully plan liquidity, follow disciplined budgets, and anticipate potential risks to meet these social obligations without undermining long-term financial well-being." | Sect. 1, p. 2 | budgeting |
| "The data were collected through a structured survey in Makassar City, Indonesia, involving 500 working individuals who were economically active at the time of data collection." | Sect. 2, p. 4 | financial_planning |
| "Therefore, the empirical results reported in this study should be interpreted as reflecting this normative–emotional dimension rather than the full multidimensional construct of household financial decision-making." | Sect. 3, p. 8 | financial_planning |
| "Income represents available financial resources, while saving behavior determines how effectively those resources are utilized." | Sect. 3 Novelty, p. 10 | financial_planning |
| "Higher income expands the financial capacity available for planning, saving, and managing expenditures, thereby supporting better household financial decisions." | Sect. 3 Discussion, p. 11 | income_expense_management |
| "Income also positively influences financial risk management (Y₁) (β = 0.301, p < 0.001), although the magnitude of this effect is smaller than that of saving behavior." | Sect. 3 Discussion, p. 11 | income_expense_management |
| "Saving behavior (X₂) has a strong and statistically significant effect on household financial decision-making (Y₂), with a regression coefficient of β = 0.604 (p < 0.001)." | Sect. 3 Discussion, p. 12 | savings_debt_management |
| "By accumulating precautionary savings and maintaining liquidity buffers, households are better positioned to stabilize their financial conditions and manage financial risks more effectively." | Sect. 3 Discussion, p. 12 | savings_debt_management |
| "In cultural contexts such as Indonesia, where social and family obligations are strong, disciplined saving is particularly important." | Sect. 3 Discussion, p. 12 | savings_debt_management |
| "When saving discipline is strong, the marginal impact of income becomes weaker because disciplined financial management reduces reliance on income alone in shaping financial decisions." | Sect. 3 Discussion, p. 13 | financial_planning |
| "Structured budgeting practices that prioritize regular saving alongside daily consumption can improve the quality of financial decision-making." | Sect. 4 Suggestions, p. 15 | budgeting |
| "This includes maintaining emergency funds, managing liquidity, and preparing contingency plans for potential financial disruptions." | Sect. 4 Suggestions, p. 15 | savings_debt_management |
| "The use of cross sectional data limits the ability to establish causal relationships among income, saving behavior, financial risk management, and household financial decision making." | Sect. 4 Limitations, p. 16 | financial_planning |

## Remember This

- A 500-respondent survey in Makassar City, Indonesia, modelled as a moderated mediation: income and saving behavior → household financial decision-making, with financial risk management as mediator and saving behavior as moderator of the income path.
- Saving behavior dominates: β = 0.604 on decision-making and β = 0.520 on financial risk management, both p < 0.001.
- The interaction is negative (β = −0.267, p < 0.001) and is read as income mattering less when saving discipline is high; adjusted R² rises to 0.628 in the moderated robust MM model.
- Both indirect effects are negative (ACME = −0.111 for saving behavior, −0.064 for income) yet are reported as support for the mediation hypothesis.
- Saving behavior's effect is printed three different ways (0.604, 0.66, ≈ 0.69) with no reconciliation, and the baseline R²/adjusted R² are conflated in the moderation paragraph.

## Cited Works

- Thaler, R. H.; Shefrin, H. M. (1981) (theory) — An economic theory of self-control; the behavioral life-cycle foundation for disciplined saving, mental accounting and self-control. [p. 3]
- Friedman, M. (1957) (theory) — The permanent income hypothesis; income as an intertemporal resource guiding consumption and saving. [p. 3]
- Modigliani, F.; Brumberg, R. (1954) (theory) — Utility analysis and the consumption function; the life-cycle framing of consumption and saving. [p. 3]
- Ajzen, I. (1991) (theory) — The theory of planned behavior; perceived behavioral control and intention under normative pressure. [p. 3]
- Maronna, R. A.; Martin, R. D.; Yohai, V. J.; Salibián-Barrera, M. (2018) (methodology) — Robust statistics reference underpinning the MM estimator used for the structural model. [p. 6]
- Yohai, V. J. (1987) (methodology) — High breakdown-point, high-efficiency robust regression estimates; the MM estimator source. [p. 6]
- Preacher, K. J.; Hayes, A. F. (2008) (methodology) — Asymptotic and resampling strategies for assessing indirect effects; the bootstrap mediation procedure used. [p. 6]
- Rhemtulla, M.; Brosseau-Liard, P. É.; Savalei, V. (2012) (methodology) — When categorical variables can be treated as continuous; justification for handling non-normal Likert data. [p. 4]
- Cronbach, L. J. (1951) (methodology) — Coefficient alpha and the internal structure of tests; the reliability statistic used for construct purification. [p. 5]
- Shmueli, G.; Sarstedt, M.; Hair, J. F.; Cheah, J.-H.; Ting, H.; Vaithilingam, S.; Ringle, C. M. (2019) (methodology) — Predictive model assessment in PLS-SEM; the prediction-oriented rather than covariance-oriented stance. [p. 3]
- Hair, J.; Hult, G. T. M.; Ringle, C.; Sarstedt, M. (2019) (methodology) — Primer on PLS-SEM; cited for robustness and prediction-oriented estimation. [p. 3]
- Norman, G. (2010) (methodology) — Likert scales, levels of measurement and the "laws" of statistics; cited to defend parametric treatment of ordinal items. [p. 4]
- Kachepa, P.; Mumtaz, M. Z. (2023) (context) — What factors influence household financial decisions in Malawi; comparative evidence that income stability shapes saving and risk management. [p. 11]
- Gomes, F.; Haliassos, M.; Ramadorai, T. (2021) (context) — Household finance review; liquidity constraints and household responsibilities redirect resources to short-term needs. [p. 12]
- Ali, M. S.; Marwat, I. U. K. (2021) (context) — Financial literacy and saving behavior of private sector employees; self-efficacy as mediator between literacy and saving. [p. 11]
- Godase, R.; P, J.; Supriya, M. L. (2024) (context) — Financial planning propensity in working adults; media influence on planning behaviour. [p. 2]
- Warmath, D.; Elizabeth O'Connor, G.; Wong, N.; Newmeyer, C. (2022) (context) — Social psychological factors in vulnerability to financial hardship. [p. 2]
- Mannell, K.; Boyle, E.; Kennedy, J.; Holcombe-James, I. (2025) (context) — How low-income families experience and negotiate digital dis/connections. [p. 2]
- Bandi, V.; Dagadu, S.; Dal, V.; Rautela, G.; Kale, M. N. (2025) (context) — Optimum finance: personal finance management using LLM; the only cited work touching personal financial management software. [p. 11]