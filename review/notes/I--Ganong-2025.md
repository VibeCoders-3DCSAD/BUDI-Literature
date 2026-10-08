---
paper_id: I--Ganong-2025
first_author: Ganong
year: 2025
title: "Earnings Instability"
venue: "NBER Working Paper Series"
doi: Not reported

designation: international
status: extracted
modules: [income_expense_management, financial_planning, budgeting, savings_debt_management]
module_rationale:
  income_expense_management: "The paper's central object is month-to-month earnings (inflow) volatility and its pass-through to spending (outflow) volatility, documented across Sections 3–7."
  financial_planning: "The paper studies how income instability undermines consumption smoothing and financial stability, with willingness-to-pay estimates for eliminating volatility (Section 6, Table 3)."
  budgeting: "The paper emphasizes that committed monthly obligations—rent, mortgages, car payments—recur at roughly monthly frequencies and make households vulnerable to income fluctuations (Section 2.1, p. 5)."
  savings_debt_management: "The paper measures liquidity via checking account balances and shows that low-liquidity households exhibit a much stronger spending-volatility response to income volatility (Section 6, Table 3, columns 4–5)."
---

## Summary

This paper uses high-frequency administrative data from two sources—a payroll processor (PayrollCompany) covering 2–5 million workers between 2010 and 2023, and bank account records from JPMorganChase Institute (JPMCI)—to document that the majority of U.S. workers experience substantial month-to-month fluctuations in pay even within ongoing employment relationships. The authors document five facts: (1) monthly earnings volatility is large, with pay changing in about 70 percent of months, a median change of 5 percent, and a 75th percentile change of 17 percent; (2) this instability is concentrated among hourly workers, who make up 60 percent of the labor force and experience earnings changes in 91 percent of months with a median absolute change of 9 percent, driven largely by hours fluctuations rather than wage changes; (3) firm-level labor demand fluctuations—measured by month-to-month changes in total firm hours—explain at least half of individual hours volatility; (4) earnings volatility translates into spending volatility, with effects especially large for low-liquidity workers; and (5) workers are more likely to separate from high-volatility jobs, suggesting that volatility is a job disamenity. The authors argue that these findings reveal an important dimension of labor-market inequality not captured by wages alone, since the workers most exposed to pay volatility are also those least able to absorb it.

## Problem and Motivation

Most of the economics literature on earnings risk has focused on annual income dynamics, using either survey data (especially the Panel Study of Income Dynamics) or large administrative datasets such as Social Security records, Census data, tax data, and linked datasets. These large-scale datasets have the power to establish representative patterns and determinants of income changes, but not at high frequencies. In the United States, direct evidence on sub-annual earnings volatility has been built primarily from surveys, including the Survey of Income and Program Participation and detailed financial diaries. These studies directly capture high-frequency fluctuations, but their smaller samples make it harder to identify the forces driving instability and to evaluate how broadly it extends across the labor force. A nascent literature using high-frequency administrative data from outside the United States has also documented substantial monthly earnings volatility. The authors extend this literature using large-scale high-frequency U.S. administrative data from both the firm side (via a payroll processor) and the worker side (via paycheck deposits into Chase bank accounts). The payroll-level data allow measurement of detailed components of individual pay—including hours, wages, and bonuses—for the universe of workers at a given firm. The bank account data enable linking earnings data with spending and liquidity and aggregating jobs into households. Throughout, the authors focus on pay variation within continuing jobs, noting that volatility arising from unemployment and job transitions would only amplify the instability they document.

## Method

**Design.** Empirical study using high-frequency administrative data; the authors state no formal design label.
**Sample.** Baseline PayrollCompany sample of 19,893 firms (a 1 percent random sample of firms), with between 2 and 5 million workers in the data at any point in time; the movers sample includes 20,319 firms and 68,995 moves; the JPMCI spending analysis uses 889,379 job-spell observations; unit of analysis is the worker-month, job spell, or firm-month depending on the analysis.
**Context.** geography: United States; population: U.S. workers, with focus on hourly (60 percent) versus salaried (40 percent) workers; setting: administrative payroll records from an anonymous payroll processor (2010–2023) and bank account data from Chase customers via JPMorganChase Institute (2012–2018).

The paper uses two main datasets. The primary dataset comes from a payroll processor (PayrollCompany) reporting detailed information about employees' paychecks, including regular pay, bonuses, commissions, overtime, and paid leave, as well as gross pre-tax earnings and net earnings after withholding. For a subset of workers, job title, age, gender, number of dependent children from IRS Form W-4, and reason for separation are observed. The second dataset is bank account data from JPMorganChase Institute (JPMCI), which links income with spending and liquidity and allows aggregation of jobs into households. The authors clean the data to remove two sources of monthly pay variation that do not reflect genuine within-job instability: (1) for workers paid weekly or biweekly, total monthly pay fluctuates mechanically with calendar timing, so they normalize total monthly pay by the number of paychecks received in that month and define monthly pay as average pay per paycheck; (2) they exclude the first and last month of each worker's job spell because lower measured pay per paycheck during these months may reflect partial employment rather than true within-job volatility. They also exclude workers whose contract type cannot be reliably classified, dropping workers without a consistently observed positive base wage (11 percent of worker-months) and those whose base wage changes in at least half of the months they are observed (4 percent of worker-months). For computational feasibility, the baseline sample uses a 1 percent random sample of firms, yielding a final sample of 19,893 firms. Despite focusing on small firms, the PayrollCompany data appears representative of the U.S. workforce along several dimensions: distributions of wages, quarterly hours, pay frequency, aggregate seasonality, and monthly hire and separation rates are all similar to administrative benchmarks and BLS data, and both in the sample and in representative benchmarks, 60 percent of workers are hourly and 40 percent are salaried. For the analysis of the sources of hours fluctuations, the authors construct a second sample focused on hourly workers who move between PayrollCompany clients: a random sample of 1,000 firms in which 8 or more such transitions are observed, combined with all other firms directly linked to this set through at least one move by a worker who is on an hourly contract at both origin and destination firms, resulting in a total sample of 20,319 firms and 68,995 moves. In the JPMCI data, the unit of observation is a worker job spell, defined as the string of contiguous months with direct deposits from the same employer; the analysis restricts to job spells with at least 4 full months of employment. Because the terms of job contracts are not observed in the JPMCI data, the authors construct an imputed indicator for whether a job is "pseudo-hourly" or "pseudo-salaried" based on the properties of its pay stream: within each job spell, a worker is classified as pseudo-hourly if pay changes by more than 0.01 percent in at least 70 percent of months and average pay per check is below $2,000. This imputed classification is used only to define subsamples in the JPMCI analysis; it is not used to explain earnings volatility, since the classification is itself based on variation in pay. The main measure of earnings growth is the percent change in pay per paycheck: ∆_{i,t} = (y_{i,t} − y_{i,t−1}) / y_{i,t−1}, where y_{i,t} is average earnings per paycheck in month t for worker i. This variable is winsorized at the 2.5th and 97.5th percentiles of non-zero changes to limit the influence of outliers. When studying heterogeneity across workers, volatility is summarized as Vol_i = Median(|∆_{i,t}|), where the median is taken across all monthly earnings changes for worker i within a job spell. The authors focus primarily on the median absolute change because it captures the typical earnings change faced by a worker and is robust to outliers.

## Key Findings

- Monthly earnings volatility is substantial: in about 70 percent of months, workers' pay differs from the prior month; the median monthly change is 5 percent; and in one quarter of months the change is at least 17 percent (Section 3, p. 8–9, Table 1).
- Earnings volatility is concentrated among hourly workers: hourly workers experience earnings changes in 91 percent of months, with a median absolute change of 9 percent and a 75th percentile of 21 percent, driven largely by hours fluctuations rather than wage changes (Section 4, p. 12–13, Table 1, Panel C).
- Salaried workers' pay is far more stable: the median absolute change is zero and the 75th percentile is only 5 percent; when salaried pay does change, it usually reflects one-time payments such as bonuses, commissions, or raises (Section 4, p. 13, Table 1).
- Firms exhibit substantial month-to-month fluctuations in total hours: the median absolute percent change in total hours worked by continuing workers is 3.4 percent and the 75th percentile is 7.3 percent (Section 5.1.1, p. 19, Figure 6).
- Fluctuations in total firm hours can explain a substantial share of individual volatility: the median value of individual volatility is 9.0 percent while the counterfactual volatility absent changes in total firm hours is 3.9 percent, suggesting that almost 60 percent of individual volatility for the typical worker arises from fluctuations in total firm hours (Section 5.1.2, p. 20–21).
- Using a movers design, moving from a bottom-decile to a sixth-decile firm causes individual volatility to rise by 8.1 percentage points; average individual volatility for a worker at a sixth-decile firm is 14.1 percent, implying that around 60 percent of that individual volatility is caused by the firm (Section 5.2.2, p. 22–23, Figure 7).
- Earnings volatility translates into spending volatility: the OLS coefficient of 0.260 implies that when the median monthly percent change in income increases by 10 percentage points, the median monthly percent change in spending increases by 2.6 percentage points (Section 6, p. 25, Table 3, column 1).
- Low-liquidity households exhibit a much stronger relationship between income volatility and spending volatility than high-liquidity households (Section 6, p. 28, Table 3, columns 4–5).
- Workers in volatile jobs separate at higher rates: moving from a job with constant earnings to one with median hourly worker volatility (11.9 percent) raises the separation hazard by 40 percent (1.40 = exp[2.85 × 0.119]) (Section 7, p. 30, Table 4, column 1).
- The authors compute willingness-to-pay estimates: for spending volatility, the estimates imply a willingness to pay for the median hourly worker of five to nine percent; for separations, an hourly worker with median volatility would give up around 10 percent of wages to eliminate it (Section 6, p. 28; Section 7, p. 30–31).

## Key Figures and Tables

- Figure 1 (p. 10): Within-job earnings and wage volatility — cumulative distribution function (panel a) and histogram (panel b) show that total earnings changes are an order of magnitude larger than changes in base wages; base wages only change in 10 percent of months while earnings change in 70 percent of months.
- Figure 2 (p. 12): Earnings risk in monthly data versus models calibrated to annual data — models substantially understate the frequency of large month-to-month earnings changes; the 75th percentile of the absolute percent change in earnings is between 0 and 8 percent in the models compared with 17 percent in the data.
- Figure 3 (p. 13): The persistence of monthly earnings changes — the variance ratio is much closer to white noise than to a random walk, indicating that a large share of month-to-month earnings changes are fairly transitory; estimating an AR(1) process yields a coefficient of 0.53, implying little persistence at annual horizons (0.53^12 = 0.0005).
- Figure 4 (p. 14): Earnings volatility for hourly and salaried workers — frequent earnings fluctuations are the norm for hourly workers but relatively rare for salaried workers.
- Figure 5 (p. 17): Pay volatility by occupation and industry — occupations that are usually salaried have median monthly earnings changes close to zero while occupations that are usually hourly have median monthly earnings changes of around 10 percent; the pattern largely reflects contract type rather than occupation itself.
- Figure 6 (p. 19): Firm total-hours volatility — the blue bars show total-hours growth including hires and separations; the orange bars show total hours worked by continuing workers, with a median absolute percent change of 3.4 percent and a 75th percentile of 7.3 percent.
- Figure 7 (p. 22): Firm causal effects by decile estimated from movers designs — the orange bar shows the firm effect relative to decile 1; the green bar captures differential selection of workers; the blue bar represents the intercept.
- Figure 8 (p. 24): Relationship between firm total-hours volatility and individual worker volatility — the left panel shows relationships in levels for all workers; the right panel measures changes for workers who move between firms.
- Figure 9 (p. 29): Relationship between separation rates and volatility — a binscatter showing the positive relationship between firm volatility and firm separation rates; for firms that record quits, the relationship between total separations and volatility is closely mirrored by the relationship between quits and volatility.
- Table 1 (p. 9): Summary statistics of earnings changes — baseline all workers total earnings: share ∆≠0 = 0.69, median |∆| = 0.05, 75th p |∆| = 0.17, std dev = 0.25, skewness = 1.80, kurtosis = 6.46; base wage: share ∆≠0 = 0.10, median |∆| = 0.00, 75th p = 0.00, std dev = 0.03.
- Table 2 (p. 16): Heterogeneity by contract type and wage level — all Q1: share salaried 15%, share ∆≠0 0.82, median 0.11, 75th p 0.28, std dev 0.30; all Q4: share salaried 81%, share ∆≠0 0.47, median 0.00, 75th p 0.12, std dev 0.28; hourly Q1: 0% salaried, 0.93, 0.11, 0.25, 0.29; salaried Q4: 100% salaried, 0.41, 0.00, 0.17, 0.35.
- Table 3 (p. 26): The effect of income volatility on consumption volatility — OLS coefficient 0.260*** (0.003); IV(2) 0.256*** (0.010); IV(3) 0.152*** (0.012); IV(4) 0.346*** (0.012); IV(5) 0.263*** (0.022); implied WTP 8.77%, 8.65%, 5.05%.
- Table 4 (p. 30): The effect of income volatility on separation rates — Med|%∆Yij| coefficients 2.85*** (0.057), 2.94*** (0.150), 2.85*** (0.204), 3.25*** (0.188), 3.09*** (0.291), 2.72*** (0.251), 2.72*** (0.238); implied WTP ranges from 9.2% to 10.7%.
- Table A-10 (p. 35): AKM variance decompositions — baseline: num movers 20319, mean vol 0.14, median vol 0.11, SD vol 0.11, SD firm FE 0.048, SD worker FE 0.048, ratio 1.00, cov 0.00050.
- Table A-13 (p. 36): Earnings risk in monthly data versus models calibrated to annual data — monthly data: P90-P10 |∆| = 0.45, share |∆|>1% = 0.64, share |∆|>20% = 0.22, 50th percentile = 0.05, 75th percentile = 0.17, 90th percentile = 0.39, std dev = 0.25, kurtosis = 6.46.

## Definitions

- **Earnings instability** — month-to-month fluctuations in pay even within ongoing employment relationships; the paper's central object of study.
- **Pay per paycheck** — average earnings per paycheck in a given month, used to abstract from pay-schedule-driven fluctuations for workers paid weekly or biweekly.
- **Base wage** — the pre-populated value each pay period for regular pay for salaried workers or the hourly wage rate for hourly workers; changes in base wages are rare (10 percent of months) while total earnings change in 70 percent of months.
- **Pseudo-hourly** — imputed classification in the JPMCI data: a worker is classified as pseudo-hourly if pay changes by more than 0.01 percent in at least 70 percent of months and average pay per check is below $2,000.
- **Pseudo-salaried** — imputed classification in the JPMCI data: a worker who does not meet the pseudo-hourly criteria.
- **Necessary share** — the share of worker hours changes that are not offset by other workers in the firm changing hours in the opposite direction; measures the extent to which individual changes are "necessary" to achieve the net change in firm hours.
- **Total firm hours** — the total number of hours worked by all employees at a firm in a given month; fluctuations are interpreted as reflecting shifts in labor demand by firms.
- **Vol_i** — individual-level volatility, defined as Median(|∆_{i,t}|), the median absolute percent change in pay per paycheck across all monthly changes for worker i within a job spell.
- **Variance ratio** — Var(log y_{t+k} − log y_t) / (k · Var(log y_{t+1} − log y_t)); equals one for a random walk and converges to zero for white noise.

## Key Equations

- `∆_{i,t} = (y_{i,t} − y_{i,t−1}) / y_{i,t−1}` — Earnings growth: percent change in pay per paycheck (Equation 1, p. 8).
- `∆H^{firm}_{j,t} ≡ Σ_{i∈j} ∆h_{i,j,t}` — Net change in total firm hours (Equation 2, p. 20).
- `∆H^{gross}_{j,t} ≡ Σ_{i∈j} |∆h_{i,j,t}|` — Gross sum of individual hours changes (Equation 3, p. 20).
- `Necessary share_{j,t} ≡ |∆H^{firm}_{j,t}| / ∆H^{gross}_{j,t}` — Share of worker hours changes necessary to achieve the observed change in total firm hours (Equation 4, p. 20).
- `Vol_{i,j} = µ + α_i + ψ_{k(j)} + ε_{ij}` — Two-way fixed effects specification with movers (AKM), where ψ_{k(j)} is the effect of firm j's group (Equation 5, p. 21).
- `Vol^c_{i,j} = α + β Vol^y_{i,j} + u_{i,j}` — Cross-sectional relationship between spending volatility and income volatility (Equation 6, p. 25).
- `Vol^c_{i,j} = α + β \hat{Vol}^y_{i,j} + u_{i,j}` — Second-stage IV regression (Equation 7, p. 26).
- `Vol^y_{i,j} = κ + π Vol^y_{j(i)} + e_{i,j}` — First-stage regression instrumenting individual income volatility with firm-level average volatility (Equation 8, p. 26).
- `log y_{i,j,t} − log y_{i,j,t−1} = β X_{i,j,t} + ε_{i,j,t}` — Regression for predictable annual variation (Equation 9, p. 49).
- `∆\tilde{h}_{i,t}(x)` — Counterfactual change in monthly hours for worker i under a counterfactual change in total firm hours equal to x (Equation 10, p. 53).
- `Willingness to Pay = (1/2) γ σ_c^2 = (1/2) γ β_σ σ_y^2` — Standard welfare calculation based on Lucas (1987) (Equation 11, p. 61).

## Limitations and Gaps

- The authors acknowledge that although they find that fluctuations in firm total hours are an important driver of pay instability, their payroll data do not reveal why firms vary their hours so much from month to month; understanding why firms move their total hours requires detailed information on firm sales, production, and inventories (Section 8, p. 32).
- The authors acknowledge that firms may differ not only in total-hours fluctuations but also in their scheduling practices, and that understanding the contribution of scheduling practices to pay and hours volatility requires detailed data on workers' schedules beyond what is used in the paper (Section 8, p. 32–33).
- The authors acknowledge that their estimates capture individual workers' preferences in partial equilibrium, holding fixed the set of jobs; a central question for future work is whether, in general equilibrium, eliminating instability (e.g., through regulation) might lead to the existence of fewer low-wage and hourly jobs (Section 8, p. 33).
- The authors acknowledge that they cannot fully separate earnings volatility from other unobserved attributes of high-volatility jobs; they interpret the evidence as showing that monthly earnings instability is part of a broader bundle of undesirable attributes associated with low-quality hourly jobs (Section 1, p. 4; Section 7, p. 32).
- The authors acknowledge that a causal interpretation of the total-hours volatility regression requires not only the exogenous mobility assumption but also the additional assumption that firm total-hours volatility is uncorrelated with other residual firm attributes that independently affect worker volatility (Section 5.2.3, p. 25).
- The authors acknowledge that their willingness-to-pay estimates should be interpreted cautiously because they require strong parametric assumptions and because the underlying relationship need not isolate the value workers place on fluctuating income alone, but may reflect the broader disamenity of job volatility (Section 7, p. 30–31).
- The authors acknowledge that even after data-cleaning steps, some of what they measure as earnings volatility may reflect residual measurement error rather than genuine instability; however, they note that if volatility simply reflected measurement error, it should not systematically affect spending volatility or quit behavior (Section 2.1, p. 6–7).
- The authors acknowledge that identification of the AKM movers design requires the exogenous mobility assumption, which could be violated if changes in workers' idiosyncratic volatility cause them to switch to firms with different volatility or if the realization of the match-specific component affects which matches are formed; they provide event-study diagnostics and argue that selection on match formation is likely to bias toward finding smaller causal effects of firms (Appendix D.3, p. 54–56).
- [unacknowledged] The paper uses a 1 percent random sample of firms, which yields 19,893 firms but may not be fully representative of all U.S. firms; the authors note that most PayrollCompany clients are small firms with a median firm size of 18 employees (Section 2.1, p. 5).
- [unacknowledged] The JPMCI data capture only income from direct deposits into Chase bank accounts, so jobs not paid via direct deposit or paid into non-Chase accounts are not observed; the authors note this limitation when discussing why they cannot measure firm total-hours volatility in the Chase data (Appendix E, p. 59).
- [unacknowledged] The paper's analysis focuses on within-job pay variation and excludes volatility arising from job transitions and unemployment; the authors note this is a conservative choice that would only amplify the instability documented (Section 2.1, p. 5).
- [unacknowledged] The paper does not report the exact number of workers in the baseline sample, only the number of firms (19,893) and the range of workers (2–5 million at any point in time); the unit of analysis varies across analyses (Section 2.1, p. 6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline total earnings, share of months with pay change | Share ∆≠0 | 0.69 | — | — | Table 1, p. 9 |
| Baseline total earnings, median absolute change | Median \|∆\| | 0.05 | — | — | Table 1, p. 9 |
| Baseline total earnings, 75th percentile absolute change | 75th p \|∆\| | 0.17 | — | — | Table 1, p. 9 |
| Baseline total earnings, standard deviation of change | Std. dev. | 0.25 | — | — | Table 1, p. 9 |
| Baseline total earnings, skewness of change | Skewness | 1.80 | — | — | Table 1, p. 9 |
| Baseline total earnings, kurtosis of change | Kurtosis | 6.46 | — | — | Table 1, p. 9 |
| Baseline base wage, share of months with wage change | Share ∆≠0 | 0.10 | — | — | Table 1, p. 9 |
| Baseline base wage, median absolute change | Median \|∆\| | 0.00 | — | — | Table 1, p. 9 |
| Baseline base wage, 75th percentile absolute change | 75th p \|∆\| | 0.00 | — | — | Table 1, p. 9 |
| Baseline base wage, standard deviation of change | Std. dev. | 0.03 | — | — | Table 1, p. 9 |
| Baseline base wage, skewness of change | Skewness | 4.75 | — | — | Table 1, p. 9 |
| Baseline base wage, kurtosis of change | Kurtosis | 65.99 | — | — | Table 1, p. 9 |
| Quarterly earnings, share of quarters with pay change | Share ∆≠0 | 0.80 | — | — | Table 1, p. 9 |
| Quarterly earnings, median absolute change | Median \|∆\| | 0.06 | — | — | Table 1, p. 9 |
| Quarterly earnings, 75th percentile absolute change | 75th p \|∆\| | 0.16 | — | — | Table 1, p. 9 |
| Quarterly earnings, standard deviation of change | Std. dev. | 0.20 | — | — | Table 1, p. 9 |
| Net earnings (PayrollCompany), share of months with change | Share ∆≠0 | 0.76 | — | — | Table 1, p. 9 |
| Net earnings (PayrollCompany), median absolute change | Median \|∆\| | 0.05 | — | — | Table 1, p. 9 |
| Net earnings (JPMCI), share of months with change | Share ∆≠0 | 0.79 | — | — | Table 1, p. 9 |
| Net earnings (JPMCI), median absolute change | Median \|∆\| | 0.05 | — | — | Table 1, p. 9 |
| Hourly total earnings, share of months with pay change | Share ∆≠0 | 0.91 | — | — | Table 1, p. 9 |
| Hourly total earnings, median absolute change | Median \|∆\| | 0.09 | — | — | Table 1, p. 9 |
| Hourly total earnings, 75th percentile absolute change | 75th p \|∆\| | 0.21 | — | — | Table 1, p. 9 |
| Hourly total earnings, standard deviation of change | Std. dev. | 0.26 | — | — | Table 1, p. 9 |
| Hourly base wage, share of months with wage change | Share ∆≠0 | 0.12 | — | — | Table 1, p. 9 |
| Hourly base wage, median absolute change | Median \|∆\| | 0.00 | — | — | Table 1, p. 9 |
| Hourly hours, share of months with hours change | Share ∆≠0 | 0.90 | — | — | Table 1, p. 9 |
| Hourly hours, median absolute change | Median \|∆\| | 0.07 | — | — | Table 1, p. 9 |
| Hourly hours, 75th percentile absolute change | 75th p \|∆\| | 0.19 | — | — | Table 1, p. 9 |
| Salaried total earnings, share of months with pay change | Share ∆≠0 | 0.34 | — | — | Table 1, p. 9 |
| Salaried total earnings, median absolute change | Median \|∆\| | 0.00 | — | — | Table 1, p. 9 |
| Salaried total earnings, 75th percentile absolute change | 75th p \|∆\| | 0.05 | — | — | Table 1, p. 9 |
| Salaried total earnings, standard deviation of change | Std. dev. | 0.23 | — | — | Table 1, p. 9 |
| Salaried base wage, share of months with wage change | Share ∆≠0 | 0.07 | — | — | Table 1, p. 9 |
| Salaried base wage, median absolute change | Median \|∆\| | 0.00 | — | — | Table 1, p. 9 |
| Full-time hourly total earnings, share of months with change | Share ∆≠0 | 0.90 | — | — | Table 1, p. 9 |
| Full-time hourly total earnings, median absolute change | Median \|∆\| | 0.07 | — | — | Table 1, p. 9 |
| Full-time hourly total earnings, 75th percentile absolute change | 75th p \|∆\| | 0.16 | — | — | Table 1, p. 9 |
| Prime-age hourly total earnings, share of months with change | Share ∆≠0 | 0.93 | — | — | Table 1, p. 9 |
| Prime-age hourly total earnings, median absolute change | Median \|∆\| | 0.09 | — | — | Table 1, p. 9 |
| No-overtime hourly total earnings, share of months with change | Share ∆≠0 | 0.86 | — | — | Table 1, p. 9 |
| No-overtime hourly total earnings, median absolute change | Median \|∆\| | 0.09 | — | — | Table 1, p. 9 |
| All workers Q1 (lowest pay), share salaried | Share salaried | 15% | — | — | Table 2, p. 16 |
| All workers Q1 (lowest pay), median absolute change | Median \|∆\| | 0.11 | — | — | Table 2, p. 16 |
| All workers Q4 (highest pay), share salaried | Share salaried | 81% | — | — | Table 2, p. 16 |
| All workers Q4 (highest pay), median absolute change | Median \|∆\| | 0.00 | — | — | Table 2, p. 16 |
| Hourly workers Q1 (lowest wage), share salaried | Share salaried | 0% | — | — | Table 2, p. 16 |
| Hourly workers Q1 (lowest wage), median absolute change | Median \|∆\| | 0.11 | — | — | Table 2, p. 16 |
| Hourly workers Q4 (highest wage), share salaried | Share salaried | 0% | — | — | Table 2, p. 16 |
| Hourly workers Q4 (highest wage), median absolute change | Median \|∆\| | 0.07 | — | — | Table 2, p. 16 |
| Salaried workers Q1 (lowest pay), share salaried | Share salaried | 100% | — | — | Table 2, p. 16 |
| Salaried workers Q1 (lowest pay), median absolute change | Median \|∆\| | 0.00 | — | — | Table 2, p. 16 |
| Salaried workers Q4 (highest pay), share salaried | Share salaried | 100% | — | — | Table 2, p. 16 |
| Salaried workers Q4 (highest pay), median absolute change | Median \|∆\| | 0.00 | — | — | Table 2, p. 16 |
| Firm total-hours volatility, median absolute percent change | Median \|∆\| | 3.4% | — | — | Section 5.1.1, p. 19 |
| Firm total-hours volatility, 75th percentile | 75th p \|∆\| | 7.3% | — | — | Section 5.1.1, p. 19 |
| Necessary share of worker hours changes | Necessary share | 42% | — | — | Section 5.1.2, p. 20 |
| Median individual volatility (all workers) | Median Vol | 9.0% | — | — | Section 5.1.2, p. 21 |
| Counterfactual individual volatility absent firm total-hours changes | Median Vol(0) | 3.9% | — | — | Section 5.1.2, p. 21 |
| Movers design: bottom-decile to sixth-decile firm | Change in individual volatility | 8.1 pp | — | — | Section 5.2.2, p. 23 |
| Average individual volatility at sixth-decile firm | Mean Vol | 14.1% | — | — | Section 5.2.2, p. 23 |
| Coefficient relating firm total-hours volatility to individual pay volatility | Coefficient | 1.07 | — | — | Section 5.2.3, p. 24 |
| Decline in individual pay volatility from median to zero firm total-hours volatility | Percentage point decline | 5.3 pp | — | — | Section 5.2.3, p. 24 |
| Decline in hours volatility from counterfactual exercise | Percentage point decline | 5.1 pp | — | — | Section 5.2.3, p. 24 |
| One-standard-deviation increase in firm total-hours volatility | Increase in individual pay volatility | 0.043 | — | — | Section 5.2.3, p. 24 |
| One-standard-deviation increase in firm-group effect | Increase in individual pay volatility | 0.050 | — | — | Section 5.2.3, p. 24 |
| Spending volatility OLS coefficient on income volatility | Coefficient | 0.260 | — | *** | Table 3, column 1, p. 26 |
| Spending volatility IV coefficient (firm-level instrument) | Coefficient | 0.256 | — | *** | Table 3, column 2, p. 26 |
| Spending volatility IV coefficient with worker fixed effects | Coefficient | 0.152 | — | *** | Table 3, column 3, p. 26 |
| Spending volatility IV coefficient, high checking interaction | Coefficient | −0.162 | — | *** | Table 3, column 4, p. 26 |
| Spending volatility IV coefficient, high checking interaction with income quintile FEs | Coefficient | −0.127 | — | *** | Table 3, column 5, p. 26 |
| Implied WTP to eliminate spending variance, OLS | WTP | 8.77% | — | — | Table 3, column 1, p. 26 |
| Implied WTP to eliminate spending variance, IV | WTP | 8.65% | — | — | Table 3, column 2, p. 26 |
| Implied WTP to eliminate spending variance, IV with worker FEs | WTP | 5.05% | — | — | Table 3, column 3, p. 26 |
| Separation hazard coefficient on individual volatility (simplest) | Coefficient | 2.85 | — | *** | Table 4, column 1, p. 30 |
| Separation hazard coefficient on individual volatility (IV) | Coefficient | 2.94 | — | *** | Table 4, column 2, p. 30 |
| Separation hazard coefficient on individual volatility (IV with controls) | Coefficient | 2.85 | — | *** | Table 4, column 3, p. 30 |
| Separation hazard coefficient on individual volatility (movers) | Coefficient | 3.25 | — | *** | Table 4, column 4, p. 30 |
| Separation hazard coefficient on individual volatility (full-time) | Coefficient | 3.09 | — | *** | Table 4, column 5, p. 30 |
| Separation hazard coefficient on individual volatility (large firms) | Coefficient | 2.72 | — | *** | Table 4, column 6, p. 30 |
| Separation hazard coefficient on individual volatility (exclude last quarter) | Coefficient | 2.72 | — | *** | Table 4, column 7, p. 30 |
| Implied WTP to eliminate volatility from separations, simplest | WTP | 9.6% | — | — | Table 4, column 1, p. 30 |
| Implied WTP to eliminate volatility from separations, IV | WTP | 9.8% | — | — | Table 4, column 2, p. 30 |
| Implied WTP to eliminate volatility from separations, IV with controls | WTP | 9.6% | — | — | Table 4, column 3, p. 30 |
| Implied WTP to eliminate volatility from separations, movers | WTP | 10.7% | — | — | Table 4, column 4, p. 30 |
| Implied WTP to eliminate volatility from separations, full-time | WTP | 10.2% | — | — | Table 4, column 5, p. 30 |
| Implied WTP to eliminate volatility from separations, large firms | WTP | 9.2% | — | — | Table 4, column 6, p. 30 |
| Implied WTP to eliminate volatility from separations, exclude last quarter | WTP | 9.2% | — | — | Table 4, column 7, p. 30 |
| Separation hazard coefficient on firm volatility, hourly workers | Coefficient | 3.01 | — | *** | Table A-12, p. 37 |
| Separation hazard coefficient on firm volatility, salaried workers | Coefficient | 1.30 | — | *** | Table A-12, p. 37 |
| AKM variance decomposition, SD of firm fixed effects (baseline) | SD firm FE | 0.048 | — | — | Table A-10, p. 35 |
| AKM variance decomposition, SD of worker fixed effects (baseline) | SD worker FE | 0.048 | — | — | Table A-10, p. 35 |
| AKM variance decomposition, ratio of SD firm FE to SD worker FE (baseline) | Ratio | 1.00 | — | — | Table A-10, p. 35 |
| AKM variance decomposition, covariance of firm and worker FE (baseline) | Cov(firm FE, worker FE) | 0.00050 | — | — | Table A-10, p. 35 |
| Robustness: spending volatility coefficient, non-work spending | Coefficient | 0.371 | — | *** | Table A-11, column 2, p. 36 |
| Robustness: spending volatility coefficient, other nondurable spending | Coefficient | 0.235 | — | *** | Table A-11, column 3, p. 36 |
| Robustness: spending volatility coefficient, total spending | Coefficient | 0.265 | — | *** | Table A-11, column 4, p. 36 |
| Robustness: spending volatility coefficient, quarterly frequency | Coefficient | 0.315 | — | *** | Table A-11, column 5, p. 36 |
| Robustness: spending volatility coefficient, monthly income and quarterly spending | Coefficient | 0.240 | — | *** | Table A-11, column 6, p. 36 |
| Robustness: spending volatility coefficient, two-job households | Coefficient | 0.341 | — | *** | Table A-11, column 7, p. 36 |
| Robustness: spending volatility coefficient, firms with at least 50 workers | Coefficient | 0.260 | — | *** | Table A-11, column 8, p. 36 |
| Monthly data: P90 − P10 of absolute log earnings changes | P90 − P10 \|∆\| | 0.45 | — | — | Table A-13, p. 36 |
| Monthly data: share of earnings changes exceeding 1% | Share \|∆\| > 1% | 0.64 | — | — | Table A-13, p. 36 |
| Monthly data: share of earnings changes exceeding 20% | Share \|∆\| > 20% | 0.22 | — | — | Table A-13, p. 36 |
| Monthly data: 50th percentile absolute log earnings change | 50th percentile \|∆\| | 0.05 | — | — | Table A-13, p. 36 |
| Monthly data: 75th percentile absolute log earnings change | 75th percentile \|∆\| | 0.17 | — | — | Table A-13, p. 36 |
| Monthly data: 90th percentile absolute log earnings change | 90th percentile \|∆\| | 0.39 | — | — | Table A-13, p. 36 |
| Monthly data: standard deviation of log earnings changes | Std. dev. | 0.25 | — | — | Table A-13, p. 36 |
| Monthly data: kurtosis of log earnings changes | Kurtosis | 6.46 | — | — | Table A-13, p. 36 |
| Monthly data: Crow-Siddiqui kurtosis | Crow-Siddiqui kurtosis | 14.07 | — | — | Table A-13, p. 36 |
| KMV model: standard deviation of log earnings changes | Std. dev. | 0.17 | — | — | Table A-13, p. 36 |
| KV model: standard deviation of log earnings changes | Std. dev. | 0.30 | — | — | Table A-13, p. 36 |
| MLM model: standard deviation of log earnings changes | Std. dev. | 0.06 | — | — | Table A-13, p. 36 |
| CHT model: standard deviation of log earnings changes | Std. dev. | 0.07 | — | — | Table A-13, p. 36 |
| Unpaid leave: observed median absolute earnings change | Median \|∆\| | 0.06 | — | — | Table A-14, p. 37 |
| Unpaid leave: counterfactual median absolute earnings change after removing unpaid leave | Median \|∆\| | 0.05 | — | — | Table A-14, p. 37 |
| Unpaid leave: observed 75th percentile absolute earnings change | 75th percentile \|∆\| | 0.15 | — | — | Table A-14, p. 37 |
| Unpaid leave: counterfactual 75th percentile after removing unpaid leave | 75th percentile \|∆\| | 0.13 | — | — | Table A-14, p. 37 |
| Share of months where absolute dollar change in income exceeds 50% of median checking account balance | Share | 40% | — | — | Section 3, p. 10–11 |
| Share of months where absolute dollar change in income exceeds median checking account balance | Share | One-fourth | — | — | Section 3, p. 10–11 |
| Pseudo-hourly workers: months where earnings change exceeds half median checking account balance | Share | 47% | — | — | Section 4, p. 13 |
| Pseudo-salaried workers: months where earnings change exceeds half median checking account balance | Share | 33% | — | — | Section 4, p. 13 |
| Pseudo-hourly workers: months where earnings change exceeds entire median checking account balance | Share | 28% | — | — | Section 4, p. 13 |
| Pseudo-salaried workers: months where earnings change exceeds entire median checking account balance | Share | 18% | — | — | Section 4, p. 13 |
| Contract type in PayrollCompany: hourly share | Share hourly | 60% | — | — | Table A-1, p. 30 |
| Contract type in PayrollCompany: salaried share | Share salaried | 40% | — | — | Table A-1, p. 30 |
| Contract type in PayrollCompany: bonus recipients | Share bonus | 35% | — | — | Table A-1, p. 30 |
| Contract type in PayrollCompany: no bonus | Share no bonus | 65% | — | — | Table A-1, p. 30 |
| JPMCI job-level earnings volatility (no condition), standard deviation | Std. dev. | 0.24 | — | — | Table A-3, p. 31 |
| JPMCI job-level earnings volatility (no condition), share ∆≠0 | Share ∆≠0 | 0.79 | — | — | Table A-3, p. 31 |
| JPMCI household-level earnings volatility (no condition), standard deviation | Std. dev. | 0.22 | — | — | Table A-3, p. 31 |
| JPMCI household-level earnings volatility (no condition), share ∆≠0 | Share ∆≠0 | 0.80 | — | — | Table A-3, p. 31 |
| Lagged median: full-time hourly total earnings, share ∆≠0 | Share ∆≠0 | 0.90 | — | — | Table A-4, p. 31 |
| Lagged median: full-time hourly total earnings, median absolute change | Median \|∆\| | 0.06 | — | — | Table A-4, p. 31 |
| Seasonality of earnings changes: hourly workers R² (firm-by-month FEs) | R² | 0.09 | — | — | Table A-5, p. 31 |
| Seasonality of earnings changes: hourly workers R² (12-month lags) | R² | 0.03 | — | — | Table A-5, p. 31 |
| Seasonality of earnings changes: salaried workers with bonus R² (firm-by-month FEs) | R² | 0.33 | — | — | Table A-5, p. 31 |
| Seasonality of earnings changes: salaried workers with bonus R² (12-month lags) | R² | 0.24 | — | — | Table A-5, p. 31 |
| Age heterogeneity: workers under 25, median absolute change | Median \|∆\| | 0.12 | — | — | Table A-7, p. 32 |
| Age heterogeneity: workers 55+, median absolute change | Median \|∆\| | 0.02 | — | — | Table A-7, p. 32 |
| Gender/children: men with children, median absolute change | Median \|∆\| | 0.05 | — | — | Table A-8, p. 33 |
| Industry heterogeneity: Accommodation and Food Services, median absolute change | Median \|∆\| | 0.10 | — | — | Table A-9, p. 34 |
| Occupation heterogeneity: Host, median absolute change | Median \|∆\| | 0.19 | — | — | Table A-9, p. 34 |
| Occupation heterogeneity: Accountant, median absolute change | Median \|∆\| | 0.01 | — | — | Table A-9, p. 34 |
| AR(1) coefficient matching variance ratio | Coefficient | 0.53 | — | — | Section 3, p. 13 |
| Implied persistence at annual horizon from AR(1) | 0.53^12 | 0.0005 | — | — | Section 3, p. 13 |
| Separation hazard increase from moving to median volatility job | Increase | 40% | — | — | Section 7, p. 30 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "In about three quarters of months, workers' pay differs from the prior month." | Section 3, p. 4 | income_expense_management |
| "The median month has a change of 5 percent, and in one quarter of months the change in pay is at least 17 percent." | Section 3, p. 4 | income_expense_management |
| "This earnings instability is pervasive, but it has been masked in past analysis of annual data." | Abstract, p. 2 | income_expense_management |
| "The vast majority of this earnings volatility is driven by fluctuations in hours rather than wages." | Section 4, p. 4 | income_expense_management |
| "This is because earnings instability arises in large part from firm-driven fluctuations in hours." | Abstract, p. 2 | income_expense_management |
| "The effects are especially large for workers with low liquidity, consistent with the presence of binding budget constraints." | Section 6, p. 3 | savings_debt_management |
| "Hourly workers are more likely to quit high-volatility jobs, suggesting that high volatility is a disamenity." | Section 7, p. 3 | financial_planning |
| "Because hourly workers also tend to have lower incomes and less liquidity, this means that the workers most exposed to pay volatility are on average the ones least able to absorb it." | Section 4, p. 4 | savings_debt_management |
| "The concentration of earnings instability among low-wage hourly workers is consistent with a long tradition in labor economics linking job instability to job quality." | Section 4, p. 4 | financial_planning |
| "Taken together, these final two facts show that high-frequency earnings instability has meaningful consequences for households and workers." | Section 1, p. 5 | financial_planning |
| "Firms may have some scope to insure workers against earnings changes (e.g., salaried workers receive the same base pay each month), but in many production settings they have less scope to smooth labor input itself." | Section 1, p. 4 | income_expense_management |
| "In forty percent of months, workers have an absolute dollar change in income that exceeds 50 percent of their median checking account balance, and in one-fourth of months the absolute change exceeds the median balance." | Section 3, p. 10–11 | savings_debt_management |
| "The median value of volatility V oli(∆H firm t ) is 9.0 percent while the median value of V oli(0) is 3.9 percent." | Appendix D.2, p. 52 | income_expense_management |
| "Moving from a bottom-decile to a sixth-decile firm causes individual volatility to rise by 8.1 percentage points." | Section 5.2.2, p. 25 | income_expense_management |
| "The estimate in column 1 of Table 3, β̂ = 0.260, implies that when the median monthly percent change in income increases by 10 percentage points, the median monthly percent change in spending increases by 2.6 percentage points." | Section 6, p. 25 | budgeting |
| "These patterns are not specific to the PayrollCompany data. Monthly income volatility within jobs in the JPMCI data is nearly identical to that in the PayrollCompany." | Section 3, p. 9 | income_expense_management |
| "The reason hourly workers face substantial pay volatility is that they face large changes in hours that pass through directly into earnings." | Section 4, p. 13 | income_expense_management |
| "If differences in total-hours fluctuations explain most of the differences in pay volatility across firms, then this leaves little role for other cross-firm differences such as scheduling practices." | Section 5.2.3, p. 24–25 | financial_planning |
| "This earnings instability is a meaningful source of economic risk: we provide evidence that it increases consumption volatility and leads to greater job separations." | Abstract, p. 2 | financial_planning |
| "These findings suggest that short-term earnings risk is a significant feature of the labor market and that this risk falls disproportionately on the most financially fragile workers." | Abstract, p. 2 | savings_debt_management |

## Remember This

- The paper documents five facts about earnings instability: (1) monthly earnings volatility is substantial (pay changes in ~70% of months, median change 5%, 75th percentile 17%); (2) volatility is concentrated among hourly workers (91% of months have pay changes, median 9%, 75th percentile 21%) and driven by hours fluctuations rather than wage changes; (3) firm-level labor demand fluctuations explain at least half of individual hours volatility; (4) earnings volatility translates into spending volatility, especially for low-liquidity workers; and (5) workers are more likely to separate from high-volatility jobs.
- Hourly workers make up 60% of the labor force and tend to have lower income and less liquidity than salaried workers, meaning the workers most exposed to pay volatility are also those least able to absorb it.
- Firms have substantial month-to-month fluctuations in total hours worked by continuing workers (median absolute change 3.4%, 75th percentile 7.3%), and these fluctuations can explain almost 60% of individual volatility for the typical worker.
- The movers design shows that moving from a bottom-decile to a sixth-decile firm causes individual volatility to rise by 8.1 percentage points, and around 60% of the individual volatility at a sixth-decile firm is caused by the firm.
- Earnings volatility passes through to spending volatility: when the median monthly percent change in income increases by 10 percentage points, the median monthly percent change in spending increases by 2.6 percentage points.
- Workers in volatile jobs separate at higher rates: moving from a job with constant earnings to one with median hourly worker volatility raises the separation hazard by 40%.
- The authors compute willingness-to-pay estimates: 5–9% of income to eliminate spending volatility and around 10% of wages to eliminate earnings volatility from separations.
- Models of income dynamics calibrated only to annual data substantially understate the frequency of large monthly earnings changes and imply much more persistence than is observed in the data.
- The paper's findings connect to dual labor market theory and the literature on job amenities and total compensation, suggesting that pay volatility is an important dimension of labor-market inequality not captured by wages alone.

## Cited Works

- Abowd, J. M. and McKinney, K. L. (2024) — Mixed-effects methods for search and matching research; administrative data source. [p. 34]
- Abowd, J. M., Kramarz, F., and Margolis, D. N. (1999) — AKM two-way fixed effects model for matched employer-employee data; methodological foundation for the movers design. [p. 21]
- Andresen, M. E., Kostøl, A. R., Milton, R. T., Mommaerts, C., and Wallossek, L. (2025) — Monthly earnings volatility and household pooling in Norwegian administrative data; comparison for household smoothing. [p. 11]
- Bania, N. and Leete, L. (2009) — Monthly household income volatility in the U.S., 1991/92 vs. 2002/03 using SIPP; prior survey evidence. [p. 1]
- Bassier, I., Dube, A., and Naidu, S. (2022) — Monopsony in movers; source of separation elasticity to wages. [p. 21]
- Bergman, A., David, G., and Song, H. (2023) — Schedule volatility as a driver of voluntary employee turnover in retail and home health; quasi-experimental evidence. [p. 4]
- Blundell, R., Bollinger, C. R., Hokayem, C., and Ziliak, J. P. (2025) — Interpreting cohort profiles of life cycle earnings volatility; annual earnings volatility for less-educated Black men. [p. 3]
- Bonhomme, S., Lamadon, T., and Manresa, E. (2019) — Distributional framework for matched employer-employee data; methodology for grouping firms. [p. 21]
- Borovičková, K. and Shimer, R. (2024) — Assortative matching and wages: the role of selection; critique of AKM diagnostics. [p. 22]
- Brewer, M., Cominetti, N., and Jenkins, S. P. (2025) — What do we know about income and earnings volatility?; review. [p. 2]
- Caplin, A., Gregory, V., Lee, E., Leth-Petersen, S., and Sæverud, J. (2023) — Subjective earnings risk; survey-based literature. [p. 1]
- Card, D., Cardoso, A. R., and Kline, P. (2016) — Bargaining, sorting, and the gender wage gap; event-study diagnostic in AKM context. [p. 34]
- Chetty, R. and Szeidl, A. (2007) — Consumption commitments and risk preferences; motivation for focusing on monthly variation. [p. 5]
- Crawley, E., Holm, M. B., and Tretvoll, H. (2026) — A parsimonious model of idiosyncratic income; benchmark model calibrated to annual data. [p. 4]
- Davis, S. J. and Haltiwanger, J. (1992) — Gross job creation, gross job destruction, and employment reallocation; source of the excess reallocation statistic. [p. 3]
- Doeringer, P. B. and Piore, M. J. (1971) — Internal labor markets and manpower analysis; dual labor market theory. [p. 2]
- Druedahl, J., Graber, M., and Jørgensen, T. H. (2023) — High frequency income dynamics; non-U.S. administrative evidence. [p. 2]
- Dube, A., Naidu, S., and Reich, A. D. (2022) — Power and dignity in the low-wage labor market; full-time position as most sought-after amenity. [p. 32]
- Ehrenreich, B. (2001) — Nickel and Dimed; qualitative account of instability among peripheral low-wage workers. [p. 3]
- Farkas, H. (2025) — The economic incidence of schedule unpredictability in hourly work; weather-driven demand fluctuations passed onto workers' schedules. [p. 19]
- Farrell, D. and Greig, F. (2015) — Weathering Volatility; JPMCI prior work on income and expense volatility. [p. 7]
- Farrell, D., Greig, F., and Yu, C. (2019) — Weathering Volatility 2.0; JPMCI prior work. [p. 7]
- Ganong, P. and Noel, P. (2019) — Consumer spending during unemployment; work and non-work spending definitions. [p. 28]
- Ganong, P., Jones, D., Noel, P. J., Greig, F. E., Farrell, D., and Wheat, C. (2025) — Liquid wealth and consumption smoothing of typical labor income shocks; JPMCI sample and spending measure. [p. 7]
- Gottschalk, P. and Moffitt, R. (1994) — The growth of earnings instability in the U.S. labor market; PSID evidence. [p. 1]
- Grigsby, J., Hurst, E., and Yildirmaz, A. (2021) — Aggregate nominal wage adjustments; administrative payroll data evidence on wage rigidity. [p. 9]
- Gronberg, T. and Reed, W. (1994) — Estimating workers' marginal willingness to pay for job attributes using duration data; WTP methodology for separations. [p. 30]
- Guiso, L., Pistaferri, L., and Schivardi, F. (2005) — Insurance within the firm; limited pass-through of transitory firm shocks into annual earnings in Italy. [p. 4]
- Guvenen, F., Ozkan, S., and Song, J. (2014) — The nature of countercyclical income risk; administrative Social Security records. [p. 1]
- Haider, S. J. (2001) — Earnings instability and earnings inequality of males in the United States: 1967–1991; PSID evidence. [p. 1]
- Hannagan, A. and Morduch, J. (2015) — Income gains and month-to-month income volatility; US Financial Diaries evidence. [p. 1]
- Hart, O. and Holmström, B. (1987) — The theory of contracts; implicit contracts literature. [p. 4]
- Humlum, A., Rasmussen, M., and Rose, E. K. (2025) — Firm premia and match effects in pay vs. amenities; job amenities literature. [p. 3]
- Johnson, D. S., Parker, J. A., and Souleles, N. S. (2006) — Household expenditure and the income tax rebates of 2001; spending responses to transitory income changes. [p. 4]
- Kaplan, G. and Violante, G. L. (2022) — The marginal propensity to consume in heterogeneous agent models; benchmark model calibrated to annual data. [p. 4]
- Kaplan, G., Moll, B., and Violante, G. L. (2018) — Monetary policy according to HANK; benchmark model calibrated to annual data. [p. 4]
- Kesavan, S. and Kuhnen, C. M. (2017) — Demand fluctuations, precarious incomes, and employee turnover; quasi-experimental evidence. [p. 4]
- Kline, P. (2024) — Firm wage effects; leave-out estimation guidance. [p. 16]
- Kline, P., Saggio, R., and Sølvsten, M. (2020) — Leave-out estimation of variance components; correction for sampling bias in variance decompositions. [p. 16]
- Lachowska, M., Mas, A., and Woodbury, S. A. (2022) — How reliable are administrative reports of paid work hours?; validation of hours data. [p. 23]
- Lachowska, M., Mas, A., Saggio, R., and Woodbury, S. A. (2026) — Work hours mismatch; evidence that most workers would prefer to work more hours than their employer offers. [p. 3]
- Lamadon, T., Mogstad, M., and Setzler, B. (2022) — Imperfect competition, compensating differentials, and rent sharing in the US labor market; separation elasticity to wages. [p. 30]
- Lambert, S. J., Henly, J. R., and Kim, J. (2019) — Precarious work schedules as a source of economic insecurity and institutional distrust; survey evidence. [p. 4]
- Lemieux, T., MacLeod, W. B., and Parent, D. (2009) — Performance pay and wage inequality; bonus-driven volatility for high earners. [p. 4]
- Lucas, R. E. Jr. (1987) — Models of Business Cycles; welfare calculation framework. [p. 28]
- MacLeod, W. B. and Parent, D. (1999) — Job characteristics and the form of compensation; implicit contracts literature. [p. 4]
- Maestas, N., Mullen, K. J., Powell, D., von Wachter, T., and Wenger, J. B. (2023) — The value of working conditions in the United States; job amenities literature. [p. 3]
- Mas, A. (2025) — Non-wage amenities; recent review. [p. 3]
- Mas, A. and Pallais, A. (2017) — Valuing alternative work arrangements; job amenities literature. [p. 3]
- Maxted, P., Laibson, D., and Moll, B. (2025) — Present bias amplifies the household balance-sheet channels of macroeconomic policy; benchmark model calibrated to annual data. [p. 4]
- Meghir, C. and Pistaferri, L. (2004) — Income variance dynamics and heterogeneity; PSID evidence. [p. 1]
- Moffitt, R. A. and Gottschalk, P. (2012) — Trends in the transitory variance of male earnings; persistent versus transitory income changes. [p. 4]
- Moffitt, R. and Zhang, S. (2018) — Income volatility and the PSID; overview of PSID studies. [p. 1]
- Moffitt, R., Abowd, J., Bollinger, C., Carr, M., Hokayem, C., McKinney, K., Wiemers, E., Zhang, S., and Ziliak, J. (2022) — Reconciling trends in U.S. male earnings volatility; linked datasets. [p. 1]
- Morduch, J. and Schneider, R. (2017) — The Financial Diaries; detailed financial diaries evidence on month-to-month instability. [p. 1]
- Myers, C. A. and Shultz, G. P. (1951) — The Dynamics of a Labor Market; earlier work on labor market segmentation. [p. 2]
- Pickens, J. and Sojourner, A. (2026) — Effects of Fair Workweek Laws on labor market outcomes; policy discussion. [p. 33]
- Prendergast, C. (2002) — The tenuous trade-off between risk and incentives; implicit contracts literature. [p. 4]
- Pruitt, S. and Turner, N. (2020) — Earnings risk in the household; tax data evidence. [p. 1]
- Rebitzer, J. B. and Taylor, L. J. (1991) — A model of dual labor markets when product demand is uncertain; dual labor market theory. [p. 2]
- Reynolds, L. G. (1951) — The Structure of Labor Markets; earlier work on labor market segmentation. [p. 2]
- Schneider, D. and Harknett, K. (2019) — Consequences of routine work-schedule instability for worker health and well-being; survey evidence on schedule instability. [p. 4]
- Schoefer, B. (2025) — Eurosclerosis at 40; European labor market institutions and adjustment costs. [p. 33]
- Sorkin, I. (2018) — Ranking firms using revealed preference; job amenities literature. [p. 3]
- Zhang, C. Y., Sussman, A. B., Wang-Ly, N., and Lyu, J. K. (2022) — How consumers budget; household budgeting at monthly horizon. [p. 5]
- Ziliak, J. P., Hardy, B., and Bollinger, C. (2011) — Earnings volatility in America: evidence from matched CPS; linked datasets. [p. 1]