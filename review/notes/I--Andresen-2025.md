---
paper_id: I--Andresen-2025
first_author: Andresen
year: 2025
title: "Monthly Earnings Volatility and Household Pooling"
venue: "NBER Working Paper Series"
doi: Not reported

designation: international
status: extracted
modules: [income_expense_management, savings_debt_management]
module_rationale:
  income_expense_management: "The paper measures month-to-month changes in monthly earnings and the within-year share of earnings variance (Table 2, Table 3, Figure 2), documenting how volatile the income inflow is at the frequency at which households receive it."
  savings_debt_management: "The paper asks whether households smooth monthly earnings fluctuations through partner pooling versus savings or sorting (Sect. 4, Figure 4, Figure 6) and finds mechanical pooling dominates, bearing on how households buffer income volatility."
---

# Monthly Earnings Volatility and Household Pooling

## Summary

A study of monthly earnings volatility using Norwegian administrative data on the universe of workers from 2015 to 2023. The paper documents that most individual earnings variation is within-year rather than across years, that month-to-month earnings changes are both frequent and large, and that aggregating to the household reduces volatility by 12-35% depending on the measure. Event studies around involuntary job loss and couple formation, together with bounding and decomposition exercises, show that this decline is driven primarily by mechanical pooling rather than marital sorting on volatility or partner labor supply responses to shocks. The authors find no visible partner earnings response to job loss, true household volatility is remarkably similar to random-matching volatility, and the mechanical pooling effect accounts for around 60% of the total decline in the coefficient of variation. The paper contributes to a nascent literature using monthly administrative data and is the first to construct household earnings volatility measures at the monthly level using universe data.

## Problem and Motivation

Labor income volatility and its translation into consumption are key inputs to welfare analysis and safety-net design, but the literature predominantly analyzes volatility at the annual level. Most households earn income at much higher frequencies, so sub-annual fluctuations are missed by annual measures; if households struggle to smooth these higher-frequency fluctuations, there are important welfare and policy implications for the timing of safety-net benefits (Sect. 1, p. 2). The recent rise of gig work, precarious work schedules, and short-term contract work makes within-year volatility all the more important to document. Existing monthly-data studies use payroll processors, single-country tax samples, or men only; none captures volatility across all jobs, non-employment spells, and both partners in a household. The paper fills this gap by using Norwegian administrative records covering the universe of workers from 2015-2023, linked to population registers, to measure individual and household monthly earnings volatility and to decompose why household volatility is lower than individual volatility.

## Method

**Design.** Observational administrative-data panel study with descriptive variance decomposition, event-study analysis, optimal-assignment bounding exercises, and covariance decomposition; the authors state no formal design label.
**Sample.** n = 767,219 individuals (unit of analysis: individual-month, nested in individual-job, individual, and household; 108 months per individual, 2015-2023). Additional subsamples: new couples (n = 13,092 individuals in some rows), stable couples (n = 192,794 couples), and a job-loss subsample.
**Context.** geography: Norway; population: individuals aged 25-66 who are alive, Norwegian residents for the full 2015-2023 period, with wage earnings over 1,000 NOK in at least one month; setting: administrative register data covering the universe of Norwegian workers, linked to annual population registers on residence, cohabitation, and partnership.

The paper proceeds in four empirical steps. First, it describes the data and sample restrictions, documenting the distribution of month-to-month earnings changes and decomposing the within-unit variance of monthly earnings into within-year and across-year components (Sect. 2). Second, it defines three volatility measures and estimates them at the individual-job, individual, and household levels, including and excluding zero-earning months (Sect. 3). Third, it explores three mechanisms behind the lower household volatility: partner insurance (added worker effects), mechanical pooling, and marital sorting (Sect. 4). Fourth, it provides a statistical decomposition of the change in the coefficient of variation upon pooling into pooling and sorting components (Sect. 4.3).

The three volatility measures are:

- CV_i(y_{i,m}): the within-unit coefficient of variation of monthly earnings (standard deviation divided by mean), which handles zero-earning months and is scale-invariant.
- |a_{i,m}|: the mean absolute arc percentage change in monthly earnings, where a_{i,m} = (y_{i,m} - y_{i,m-1}) / ((y_{i,m} + y_{i,m-1})/2).
- SD_i(a_{i,m}): the within-unit standard deviation of arc percentage changes in monthly earnings.

For the job-loss analysis, the authors use a unique Norwegian administrative feature introduced in 2021 that records why an employment spell ended, allowing identification of involuntary job losses and exclusion of voluntary separations (Sect. 4.1). They restrict to individuals employed at the firm for all 12 months prior to job loss, with wage income ≥ 1,000 NOK at least once in the three months prior, who do not return to the same establishment within 12 months, and whose establishment did not experience substantial employment declines before the job loss. For the marital-sorting analysis, they construct random couples by assigning each female from the new-couples subsample a randomly drawn male partner among men who began cohabiting in the same year, and solve optimal assignment problems to bound household volatility under matching patterns that minimize and maximize it (Sect. 4.2).

For the decomposition of ΔCV_i, the authors use a second-order Taylor approximation around population means of the parameters (μ_M, μ_F, σ_M, σ_F, ρ), which yields terms grouped into a homogeneous benchmark (mechanical pooling if all couples had average parameters and no sorting), within-gender heterogeneity (variance across individuals in earnings levels, risk, and their covariance), and sorting components (assortative matching on levels and risk, cross-moments, correlation dispersion, and covariances with ρ). Variance-covariance estimates are de-biased by subtracting the average within-couple sampling variance-covariance matrix, estimated via bootstrap with 500 repetitions (Sect. 4.3; Appendix C).

## Key Findings

- Around 70% of the within-individual variance of monthly earnings is within-year rather than across years, on average (Sect. 1, p. 2; Abstract, p. 1).
- Within a job spell, 29% of months have no change in earnings, 25% have changes of 23% or more, 36% are increases, and 35% are decreases (Sect. 1, p. 2).
- The mean absolute monthly earnings change within a job is 18%, the standard deviation of monthly changes is 0.286, and the coefficient of variation is 0.290 (Sect. 3.2, p. 17; Table 3, p. 18).
- Including zero-earning months raises the individual CV from 0.377 to 0.676 and the SD of arc changes from 0.296 to 0.427 (Table 3, p. 18).
- For new couples, household volatility declines by 12-35% depending on the measure: mean absolute changes fall from 24% to 21%, the SD of changes falls by 24%, and the CV falls by 35% (Sect. 1, p. 3; Table 3, p. 18).
- Maximum possible household volatility under optimal matching is over three times higher than minimum possible household volatility, and individual volatility is over twice as high as minimum possible household volatility (Sect. 4.2, p. 25).
- True household volatility is remarkably similar to random-matching household volatility, implying marital sorting on volatility does not play an important role; random household CV is roughly 0.25 versus individual CV of roughly 0.4 (Sect. 4.2, p. 25).
- The mechanical pooling effect accounts for around 60% of the total decline in volatility upon pooling (Sect. 4.3, p. 30).
- There is no visible partner employment or earnings response to involuntary job loss, immediately or up to 24 months afterwards (Sect. 4.1, p. 23).
- Individuals who lose their job experience an immediate 50% decline in employment and an immediate 60% drop in monthly earnings; 24 months later, employment recovers only to around 80% and earnings remain around 20% lower (Sect. 4.1, p. 23).
- The authors find positive assortative matching on earnings levels: the correlation of partners' permanent components is 0.20 for new couples and 0.19 for stable couples, and the correlation of monthly components is 0.08 (Sect. 4.2.1, p. 27).
- The paper's evidence emphasizes that earnings volatility is not just an annual phenomenon but a monthly reality for workers and families (Sect. 5, p. 34).

## Key Figures and Tables

- Figure 1 (p. 10): Distribution of months with positive earnings — over 10% of individuals have positive earnings in fewer than half of the 108 months.
- Figure 2 (p. 13): Distributions of month-to-month changes in earnings — Panel (a) compares with vs without zero-earning months; Panel (b) compares individual vs household earnings among couples.
- Figure 3 (p. 23): Labor market outcomes of individuals and partners after job loss — immediate 50% employment decline, no partner response; immediate 60% earnings drop for displaced individuals, no partner earnings response.
- Figure 4 (p. 25): Volatility around couple formation — individual, true household, random household, and min/max household volatility over event time; household volatility always below individual volatility, and true household closely tracks random household.
- Figure 5 (p. 31): Partner correlations of yearly and monthly components of earnings — true couples show positive correlations, random couples near zero, with little change around couple formation.
- Figure 6 (p. 33): E(ΔCV_i) decomposition, before and after couple formation — homogeneous benchmark (mechanical pooling) is substantial, individual heterogeneity accounts for a sizable share, sorting terms sum to approximately zero.
- Table 1 (p. 11): Individual summary statistics — mean age 46, 50% female, 64% have a partner ever, mean monthly earnings 42,108 NOK, N = 767,219.
- Table 2 (p. 15): Variance decomposition of total monthly earnings — within-year share is 0.85 for individual-job, 0.72 for individual excluding zeros, 0.66 for individual including zeros, and 0.66 for household including zeros.
- Table 3 (p. 18): Monthly volatility measures — 21 estimates across individual-job, individual, and household panels, with and without zeros and residualization.
- Table 4 (p. 29): Covariance decomposition of partner earnings — total covariance 187 (new couples, true), 25 (new couples, random), 180 (stable couples, true); permanent share 0.67, -0.19, 0.68 respectively.
- Appendix Table A.1 (p. A2): Selected volatility measures for four illustrative earnings processes.
- Appendix Table A.3 (p. A20): Sample sizes — from 2,523,126 to 767,219 after restrictions.
- Appendix Table A.4 (p. A21): Summary statistics for arc percentage changes across individual-job, individual, and household specifications.
- Appendix Table A.5 (p. A22): Alternative monthly volatility measures (medians and cross-sectional).
- Appendix Table A.6 (p. A22): Variation explained by residualizing earnings — R2 for levels 0.2041 and changes 0.2488 overall, higher for hourly workers.

## Limitations and Gaps

- The authors acknowledge that monthly earnings are pre-tax and do not capture after-tax differences from the tax system or withholding, though they do capture end-of-year bonuses and June holiday pay (Sect. 2.1, p. 7).
- The authors acknowledge that keeping earnings in nominal terms means volatility measures do not pick up discrete changes in real earnings from inflation adjustments; they note that the literature has not coalesced on this issue (Sect. 2.1, p. 7, footnote 7).
- The authors acknowledge that residency data is available only at the annual level, so within-year moves abroad may still be picked up (Sect. 2.1, p. 8, footnote 8).
- The authors acknowledge that the job-loss sample split into those with and without a new job or UI benefits is endogenous, so those results are only suggestive (Sect. 4.1, p. 24).
- The authors acknowledge that positively correlated shocks between partners could attenuate any potential partner response, though they would then expect to see a decrease in partner employment, which they do not observe (Sect. 4.1, p. 24).
- The authors acknowledge that the correlation of annual components cannot be identified due to a weak identification issue when annual shocks are small relative to permanent heterogeneity (Sect. 4.2.1, p. 28, footnote 37).
- The authors acknowledge that the analysis of consequences of monthly volatility on consumption and welfare is beyond the scope of the paper (Sect. 1, p. 6).
- The authors acknowledge that the sample restriction to couples where both have positive labor income at some point means female labor force participation is higher than in the total Norwegian population (Sect. 4.1, p. 22, footnote 29).
- [unacknowledged] The paper reports a discrepancy in the share of months with positive earnings: Table 1 reports "Mean share of months with non-zero earnings 0.86" (Table 1, p. 11), while Sect. 3.3 states "individuals have positive earnings for 81% of months" (Sect. 3.3, p. 21); the two figures are not reconciled.
- [unacknowledged] The paper is entirely Norway-specific: no evidence is provided on the Philippines, lower-income settings, or settings with different paycheck frequencies, so external validity to the project's context is untested.
- [unacknowledged] The paper does not study personal financial management apps, software, or any of the algorithms (SARIMA, rule-based classification, linear programming, IQR) that the project's taxonomy covers.
- [unacknowledged] The paper does not examine how households actually smooth monthly volatility through savings, transfers, or consumption adjustment; it only rules out partner labor supply and marital sorting as mechanisms, leaving the savings/consumption channel unmeasured.
- [unacknowledged] The annual-variance decomposition assumes observations are i.i.d. and bias-corrects for sampling variance; more conservative inference allowing for serial dependence would decrease precision and, if anything, increase the within-year share (Sect. 2.3, p. 14, footnote 17).

## Definitions

- **Arc percentage change (a_{i,m})** — (y_{i,m} - y_{i,m-1}) / ((y_{i,m} + y_{i,m-1})/2), with a_{i,m} = 0 when both months have zero earnings (Sect. 2.2, p. 12).
- **Coefficient of variation (CV_i)** — the ratio of the standard deviation of monthly earnings to mean earnings for unit i; unit i is an individual-job, individual, or household (Sect. 3.1, p. 15).
- **Within-year variance share** — the share of total within-unit variance of monthly earnings that is within years rather than across years (Sect. 2.3, p. 14).
- **New couples subsample** — different-sex couples observed entering cohabitation during the sample period, not previously partnered, cohabiting at least three years, both observed at least two years prior, with a balanced panel for event years -2 to 2 (Sect. 2.1, p. 9).
- **Stable couples** — couples observed cohabiting together for the full sample period 2015-2023 (Table 4 note, p. 29).
- **Job loss subsample** — individuals who experienced an involuntary job loss between 2021-2022 and had a partner in the year they lost their job (Sect. 2.1, p. 9).
- **Random couples** — constructed by assigning each female from the new-couples subsample a randomly drawn male partner among men who began cohabiting in the same year (Sect. 2.1, p. 9).
- **Mechanical pooling** — the reduction in volatility from averaging earnings across partners, independent of who matches with whom (Sect. 4.2, p. 25).
- **Assortative matching (sorting)** — the extent to which partners' earnings processes are positively or negatively correlated, which can attenuate or amplify the pooling effect (Sect. 4, p. 22).
- **Added worker effect (partner insurance)** — the endogenous change in one partner's labor supply in response to the other partner's earnings shock (Sect. 4, p. 22).

## Key Equations

- `a_{i,m} = (y_{i,m} - y_{i,m-1}) / ((y_{i,m} + y_{i,m-1})/2)` — Arc percentage change in monthly earnings; a_{i,m} = 0 when both months are zero (Sect. 2.2, p. 12).
- `y^J_{i,m} = α^J_i + π^J_{i,t(m)} + θ^J_{i,m}` — Three-component earnings model for partner J ∈ (M, F): permanent term α, annual term π, monthly term θ (Sect. 4.2.1, p. 28).
- `Cov(y^M_{i,m}, y^F_{i,m}) = Cov(α^M_i, α^F_i) + Cov(π^M_i, π^F_i) + Cov(θ^M_i, θ^F_i)` — Covariance decomposition of partner earnings into permanent, annual, and monthly components (Sect. 4.2.1, p. 28).
- `ΔVar_i = -0.25(σ^2_{Mi} + σ^2_{Fi}) + 0.5 ρ_i σ_{Mi} σ_{Fi}` — Change in variance upon pooling: first term is the pooling effect, second is the assortative matching effect (Sect. 4.3, p. 31).
- `ΔCV_i = (√(σ^2_{Mi} + σ^2_{Fi} + 2ρ_i σ_{Mi} σ_{Fi}) / (μ_{Mi} + μ_{Fi})) - (1/2)(σ_{Mi}/μ_{Mi} + σ_{Fi}/μ_{Fi})` — Change in coefficient of variation upon pooling (Sect. 4.3, p. 32).
- `ρ*_i = ((1 + m_i)^2/4)(1 + k_i/m_i)^2 - (1 + k^2_i) / (2k_i)` — Condition for when a couple sees reduced volatility upon pooling, where m_i = μ_{Fi}/μ_{Mi} and k_i = σ_{Fi}/σ_{Mi} (Appendix C, p. A9).
- `CV(y_{i,m}) = √((1-π)(μ^2 + σ^2) - (1-π)^2 μ^2) / ((1-π)μ)` — Coefficient of variation including zero-earning periods, where π is the probability of zero earnings (Appendix B, p. A6).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Within-individual variance that is within-year rather than across years | share | 70% | — | — | Abstract, p. 1; Sect. 1, p. 2 |
| Month-to-month earnings change within a job: no change | share of months | 29% | — | — | Sect. 1, p. 2 |
| Month-to-month earnings change within a job: change of 23% or more | share of months | 25% | — | — | Sect. 1, p. 2 |
| Month-to-month earnings change within a job: increase | share of months | 36% | — | — | Sect. 1, p. 2 |
| Month-to-month earnings change within a job: decrease | share of months | 35% | — | — | Sect. 1, p. 2 |
| Mean absolute arc percentage change in monthly earnings within a job | mean absolute arc percentage change | 18% | — | — | Sect. 1, p. 2; Sect. 3.2, p. 17 |
| Standard deviation of arc percentage changes in earnings within a job | standard deviation | 29% | — | — | Sect. 1, p. 2 |
| Within-individual coefficient of variation of monthly earnings | coefficient of variation | 0.29 | — | — | Sect. 1, p. 2 |
| New couples, individual mean absolute change | mean absolute arc percentage change | 24% | — | — | Sect. 1, p. 3 |
| New couples, household mean absolute change | mean absolute arc percentage change | 21% | — | — | Sect. 1, p. 3 |
| New couples, decline in mean absolute changes upon pooling | decline | 12% | — | — | Abstract, p. 1; Sect. 1, p. 3 |
| New couples, decline in standard deviation of change upon pooling | decline | 24% | — | — | Sect. 1, p. 3 |
| New couples, decline in CV upon pooling | decline | 35% | — | — | Sect. 1, p. 3 |
| Mean age of sample | age | 46 | — | — | Table 1, p. 11 |
| Share female | share | 0.50 | — | — | Table 1, p. 11 |
| Share with a partner ever | share | 0.64 | — | — | Table 1, p. 11 |
| Share of months with partner, conditional on ever | share | 0.90 | — | — | Table 1, p. 11 |
| Individual-average monthly earnings: mean | NOK | 42,108 | — | — | Table 1, p. 11 |
| Individual-average monthly earnings: standard deviation | NOK | 23,372 | — | — | Table 1, p. 11 |
| Individual-average monthly earnings: 5th percentile | NOK | 2,717 | — | — | Table 1, p. 11 |
| Individual-average monthly earnings: median | NOK | 41,547 | — | — | Table 1, p. 11 |
| Individual-average monthly earnings: 95th percentile | NOK | 84,392 | — | — | Table 1, p. 11 |
| Mean number of employers over sample period | employers | 3 | — | — | Table 1, p. 11 |
| Median number of employers over sample period | employers | 2 | — | — | Table 1, p. 11 |
| Share with only one employer over sample period | share | 0.34 | — | — | Table 1, p. 11 |
| Mean share of months with non-zero earnings | share | 0.86 | — | — | Table 1, p. 11 |
| Share with earnings from salaried work ever | share | 0.91 | — | — | Table 1, p. 11 |
| Share of months with salaried job, conditional on ever | share | 0.76 | — | — | Table 1, p. 11 |
| Share with earnings from hourly work ever | share | 0.71 | — | — | Table 1, p. 11 |
| Share of months with hourly job, conditional on ever | share | 0.32 | — | — | Table 1, p. 11 |
| Number of individuals | individuals | 767,219 | — | — | Table 1, p. 11 |
| Individual-job, excluding zeros: total variance | 1,000s NOK | 355,461 | — | — | Table 2, p. 15 |
| Individual-job, excluding zeros: share within-year | share | 0.85 | — | — | Table 2, p. 15 |
| Individual-job, excluding zeros: share across years | share | 0.15 | — | — | Table 2, p. 15 |
| Individual, excluding zeros: total variance | 1,000s NOK | 429,343 | — | — | Table 2, p. 15 |
| Individual, excluding zeros: share within-year | share | 0.72 | — | — | Table 2, p. 15 |
| Individual, excluding zeros: share across years | share | 0.28 | — | — | Table 2, p. 15 |
| Individual, including zeros: total variance | 1,000s NOK | 445,001 | — | — | Table 2, p. 15 |
| Individual, including zeros: share within-year | share | 0.66 | — | — | Table 2, p. 15 |
| Individual, including zeros: share across years | share | 0.34 | — | — | Table 2, p. 15 |
| Household, including zeros: total variance | 1,000s NOK | 323,452 | — | — | Table 2, p. 15 |
| Household, including zeros: share within-year | share | 0.66 | — | — | Table 2, p. 15 |
| Household, including zeros: share across years | share | 0.34 | — | — | Table 2, p. 15 |
| Individual-job, excluding zeros: CV | coefficient of variation | 0.290 | — | — | Table 3, p. 18 |
| Individual-job, excluding zeros: mean absolute arc percentage change | mean absolute arc percentage change | 0.178 | — | — | Table 3, p. 18 |
| Individual-job, excluding zeros: SD arc percentage change | standard deviation | 0.286 | — | — | Table 3, p. 18 |
| Individual-job, excluding zeros, residualized: CV | coefficient of variation | 0.280 | — | — | Table 3, p. 18 |
| Individual-job, excluding zeros, residualized: mean absolute arc percentage change | mean absolute arc percentage change | 0.186 | — | — | Table 3, p. 18 |
| Individual-job, excluding zeros, residualized: SD arc percentage change | standard deviation | 0.293 | — | — | Table 3, p. 18 |
| Individual, excluding zeros: CV | coefficient of variation | 0.377 | — | — | Table 3, p. 18 |
| Individual, excluding zeros: mean absolute arc percentage change | mean absolute arc percentage change | 0.184 | — | — | Table 3, p. 18 |
| Individual, excluding zeros: SD arc percentage change | standard deviation | 0.296 | — | — | Table 3, p. 18 |
| Individual, including zeros: CV | coefficient of variation | 0.676 | — | — | Table 3, p. 18 |
| Individual, including zeros: mean absolute arc percentage change | mean absolute arc percentage change | 0.229 | — | — | Table 3, p. 18 |
| Individual, including zeros: SD arc percentage change | standard deviation | 0.427 | — | — | Table 3, p. 18 |
| Individual, including zeros, new couples: CV | coefficient of variation | 0.515 | — | — | Table 3, p. 18 |
| Individual, including zeros, new couples: mean absolute arc percentage change | mean absolute arc percentage change | 0.240 | — | — | Table 3, p. 18 |
| Individual, including zeros, new couples: SD arc percentage change | standard deviation | 0.435 | — | — | Table 3, p. 18 |
| Household, including zeros: CV | coefficient of variation | 0.552 | — | — | Table 3, p. 18 |
| Household, including zeros: mean absolute arc percentage change | mean absolute arc percentage change | 0.218 | — | — | Table 3, p. 18 |
| Household, including zeros: SD arc percentage change | standard deviation | 0.377 | — | — | Table 3, p. 18 |
| Household, including zeros, new couples: CV | coefficient of variation | 0.337 | — | — | Table 3, p. 18 |
| Household, including zeros, new couples: mean absolute arc percentage change | mean absolute arc percentage change | 0.210 | — | — | Table 3, p. 18 |
| Household, including zeros, new couples: SD arc percentage change | standard deviation | 0.332 | — | — | Table 3, p. 18 |
| Partial R2 for residualizing earnings levels on firm-by-month and individual-firm FE | R2 | 0.2041 | — | — | Sect. 3.2, p. 17; Appendix Table A.6, p. A22 |
| Partial R2 for residualizing earnings changes on firm-by-month FE | R2 | 0.2488 | — | — | Sect. 3.2, p. 17; Appendix Table A.6, p. A22 |
| Share of months with positive earnings, individuals | share | 81% | — | — | Sect. 3.3, p. 21 |
| Including zero-earning months, average absolute month-to-month change in earnings | mean absolute arc percentage change | 23% | — | — | Sect. 3.3, p. 21 |
| Including zero-earning months, average SD of month-to-month changes in earnings | standard deviation | 43% | — | — | Sect. 3.3, p. 21 |
| Job loss: immediate decline in employment in month after job loss | decline | 50% | — | — | Sect. 4.1, p. 23 |
| Job loss: employment recovery by 12 months | share | 80% | — | — | Sect. 4.1, p. 23 |
| Job loss: peak UI benefit receipt three months after job loss | share | 20% | — | — | Sect. 4.1, p. 23 |
| Job loss: UI benefit receipt 24 months after job loss | share | <10% | — | — | Sect. 4.1, p. 23 |
| Job loss: share with neither new job nor UI benefits 24 months after | share | 15% | — | — | Sect. 4.1, p. 23 |
| Job loss: immediate drop in monthly earnings relative to month prior | decline | 60% | — | — | Sect. 4.1, p. 23 |
| Job loss: earnings 24 months after relative to pre-job-loss | decline | 20% | — | — | Sect. 4.1, p. 23 |
| Maximum possible household volatility relative to minimum possible | ratio | over 3 times higher | — | — | Sect. 4.2, p. 25 |
| Individual volatility relative to minimum possible household volatility | ratio | over 2 times higher | — | — | Sect. 4.2, p. 25 |
| Random household CV vs individual CV | coefficient of variation | 0.25 vs 0.4 | — | — | Sect. 4.2, p. 25 |
| New couples, true couples: total covariance | covariance in millions of NOK^2 | 187 | — | — | Table 4, p. 29 |
| New couples, true couples: share permanent component | share | 0.67 | — | — | Table 4, p. 29 |
| New couples, true couples: share yearly component | share | 0.19 | — | — | Table 4, p. 29 |
| New couples, true couples: share monthly component | share | 0.14 | — | — | Table 4, p. 29 |
| New couples, true couples: N couples | couples | 6,546 | — | — | Table 4, p. 29 |
| New couples, true couples: N monthly observations | monthly observations | 705,702 | — | — | Table 4, p. 29 |
| New couples, random couples: total covariance | covariance in millions of NOK^2 | 25 | — | — | Table 4, p. 29 |
| New couples, random couples: share permanent component | share | -0.19 | — | — | Table 4, p. 29 |
| New couples, random couples: share yearly component | share | 0.83 | — | — | Table 4, p. 29 |
| New couples, random couples: share monthly component | share | 0.36 | — | — | Table 4, p. 29 |
| Stable couples, true couples: total covariance | covariance in millions of NOK^2 | 180 | — | — | Table 4, p. 29 |
| Stable couples, true couples: share permanent component | share | 0.68 | — | — | Table 4, p. 29 |
| Stable couples, true couples: share yearly component | share | 0.18 | — | — | Table 4, p. 29 |
| Stable couples, true couples: share monthly component | share | 0.14 | — | — | Table 4, p. 29 |
| Stable couples, true couples: N couples | couples | 192,794 | — | — | Table 4, p. 29 |
| Stable couples, true couples: N monthly observations | monthly observations | 20,821,752 | — | — | Table 4, p. 29 |
| Correlation of partners' permanent components, new couples | correlation | 0.20 | — | — | Sect. 4.2.1, p. 27 |
| Correlation of partners' permanent components, stable couples | correlation | 0.19 | — | — | Sect. 4.2.1, p. 27 |
| Correlation of partners' permanent components, Hyslop (2001) | correlation | 0.57 | — | — | Sect. 4.2.1, p. 27 |
| Correlation of partners' monthly components | correlation | 0.08 | — | — | Sect. 4.2.1, p. 27 |
| Mechanical pooling effect as share of total decline in volatility | share | around 60% | — | — | Sect. 4.3, p. 30 |
| Illustrative process y1: CV | coefficient of variation | 0.21 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y1: mean absolute arc change | mean absolute arc percentage change | 0.02 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y1: SD arc change | standard deviation | 0.09 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y2: CV | coefficient of variation | 0.21 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y2: mean absolute arc change | mean absolute arc percentage change | 0.40 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y2: SD arc change | standard deviation | 0.41 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y3: CV | coefficient of variation | 0.39 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y3: mean absolute arc change | mean absolute arc percentage change | 0.40 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y3: SD arc change | standard deviation | 0.57 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y4: CV | coefficient of variation | 0.29 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y4: mean absolute arc change | mean absolute arc percentage change | 0.05 | — | — | Appendix Table A.1, p. A2 |
| Illustrative process y4: SD arc change | standard deviation | 0.00 | — | — | Appendix Table A.1, p. A2 |
| Sample size after restriction: alive & working age | individuals | 2,523,126 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: Norwegian resident full period | individuals | 2,000,762 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: never missing employer info | individuals | 1,994,547 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: never negative wage income | individuals | 1,709,871 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: never income from self-employment | individuals | 1,278,785 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: trim top/bottom 1% | individuals | 1,243,332 | — | — | Appendix Table A.3, p. A20 |
| Sample size after restriction: drop if partner dropped | individuals | 767,219 | — | — | Appendix Table A.3, p. A20 |
| Individual-job, all: share of months with non-zero arc change | share | 0.71 | — | — | Appendix Table A.4, p. A21 |
| Individual-job, all: mean absolute arc change | mean absolute arc percentage change | 0.19 | — | — | Appendix Table A.4, p. A21 |
| Individual-job, salaried: mean absolute arc change | mean absolute arc percentage change | 0.14 | — | — | Appendix Table A.4, p. A21 |
| Individual-job, hourly: mean absolute arc change | mean absolute arc percentage change | 0.40 | — | — | Appendix Table A.4, p. A21 |
| Individual, including zeros: share of months with non-zero arc change | share | 0.65 | — | — | Appendix Table A.4, p. A21 |
| Household, including zeros: share of months with non-zero arc change | share | 0.76 | — | — | Appendix Table A.4, p. A21 |
| Medians, individual-job excluding zeros: CV | median coefficient of variation | 0.239 | — | — | Appendix Table A.5, p. A22 |
| Medians, individual including zeros: CV | median coefficient of variation | 0.371 | — | — | Appendix Table A.5, p. A22 |
| Medians, household including zeros, new couples: CV | median coefficient of variation | 0.265 | — | — | Appendix Table A.5, p. A22 |
| Cross-sectional, individual including zeros: CV | cross-sectional coefficient of variation | 0.746 | — | — | Appendix Table A.5, p. A22 |
| Cross-sectional, household including zeros, new couples: CV | cross-sectional coefficient of variation | 0.524 | — | — | Appendix Table A.5, p. A22 |
| R2 for residualizing levels, all workers | R2 | 0.2041 | — | — | Appendix Table A.6, p. A22 |
| R2 for residualizing changes, all workers | R2 | 0.2488 | — | — | Appendix Table A.6, p. A22 |
| R2 for residualizing levels, hourly workers | R2 | 0.3624 | — | — | Appendix Table A.6, p. A22 |
| R2 for residualizing changes, hourly workers | R2 | 0.4336 | — | — | Appendix Table A.6, p. A22 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This paper examines monthly earnings volatility and its transmission to household earnings volatility using Norwegian data on the universe of monthly pay histories." | Abstract, p. 1 | income_expense_management |
| "We document substantial month-to-month earnings changes: within a job, while over one-quarter of months have no earnings changes, another quarter have at least a 23% change." | Abstract, p. 1 | income_expense_management |
| "Accounting for multiple jobs and non-employment increases volatility, while aggregating to households reduces volatility by 12-35%." | Abstract, p. 1 | savings_debt_management |
| "Event studies around job loss and couple formation, along with decomposition and bounding exercises, show that most of this decline reflects pooling effects rather than sorting or responses to shocks." | Abstract, p. 1 | savings_debt_management |
| "on average, around 70% of the within-individual variance is within-year rather than across years, suggesting that annual earnings measures are insufficient for capturing the full extent of earnings volatility." | Sect. 1, p. 2 | income_expense_management |
| "Within a job spell, we document that 29% of months have no change in earnings from one month to the next, while 25% have changes of 23% or more" | Sect. 1, p. 2 | income_expense_management |
| "We find an average CV of 0.29, which implies that, on average, the standard deviation in earnings within an individual is 29% of the individual's mean earnings." | Sect. 1, p. 2 | income_expense_management |
| "Overall, our results suggest that partners, on average, do not insure one another's labor supply shocks (as measured by job loss) by increasing – or even changing at all – their labor supply." | Sect. 4.1, p. 23 | savings_debt_management |
| "the mechanical effect stemming from pooling earnings is an important driver of the reduced volatility for couples" | Sect. 4.2, p. 25 | savings_debt_management |
| "Taken together, these results suggest that household-level insurance operates primarily through pooling, rather than through who marries whom or through behavioral responses to shocks." | Sect. 5, p. 34 | savings_debt_management |
| "Our final sample consists of 767,219 individuals." | Sect. 2.1, p. 7 | income_expense_management |
| "Norway is a small, high-income economy with a total labor force of around 3 million people, where employees account for 95 percent of workers, unemployment is low, and female labor force participation is high." | Sect. 2, p. 6 | income_expense_management |
| "More broadly, our evidence emphasizes that earnings volatility is not just an annual phenomenon but a monthly reality for workers and families" | Sect. 5, p. 34 | income_expense_management |
| "random household volatility is substantially lower than individual volatility" | Sect. 4.2, p. 25 | savings_debt_management |
| "maximum possible household volatility is over three times higher than minimum possible household volatility" | Sect. 4.2, p. 25 | savings_debt_management |
| "If such higher frequency earnings fluctuations are easily smoothed through mechanisms such as savings or high-frequency transfers (e.g., safety net programs or informal insurance from family and friends), then it is no surprise that individuals do not necessarily choose partners or labor supply with monthly volatility in mind." | Sect. 1, p. 4 | savings_debt_management |
| "variability in monthly income causes financial hardship and other adverse outcomes for some families, particularly low-income families" | Sect. 1, p. 5 | savings_debt_management |
| "an examination of the consequences of monthly volatility on consumption and welfare is beyond the scope of this paper" | Sect. 1, p. 5 | savings_debt_management |

## Remember This

- Monthly earnings volatility is high: within a job, 29% of months have no change and 25% have changes of 23% or more; the average within-job CV is 0.29.
- Around 70% of within-individual variance is within-year, so annual data understates the volatility households face.
- Aggregating to the household reduces volatility by 12-35% depending on the measure (CV, SD of arc changes, mean absolute arc changes).
- The decline is driven by mechanical pooling, not marital sorting on volatility or partner labor supply responses; the pooling effect accounts for around 60% of the CV decline.
- Partners show no employment or earnings response to involuntary job loss, immediately or up to 24 months later.
- The paper reports a discrepancy between the 81% share of months with positive earnings in Sect. 3.3 and the 0.86 mean share in Table 1.
- The study is Norway-specific, uses administrative data, and does not address PFM apps, savings behavior, or consumption smoothing.

## Cited Works

- Ganong, P.; Noel, P.; Patterson, C.; Vavra, J.; Weinberg, A. (2025) — Earnings Instability, NBER Working Paper 34227; US payroll data comparison. [p. 12]
- Brewer, M.; Cominetti, N.; Jenkins, S. P. (2025) — "What Do We Know About Income and Earnings Volatility?", Review of Income and Wealth; UK monthly tax data comparison. [p. 12]
- Druedahl, J.; Graber, M.; Jørgensen, T. H. (2025) — High Frequency Income Dynamics; Danish administrative data. [p. 12]
- Hyslop, D. R. (2001) — "Rising U.S. Earnings Inequality and Family Labor Supply", American Economic Review; reports permanent correlation 0.57. [p. 27]
- Meghir, C.; Pistaferri, L. (2004) — "Income Variance Dynamics and Heterogeneity", Econometrica. [p. 6]
- Gottschalk, P.; Moffitt, R. (1994) — "The Growth of Earnings Instability in the U.S. Labor Market", Brookings Papers on Economic Activity. [p. 6]
- Guvenen, F.; Karahan, F.; Ozkan, S.; Song, J. (2021) — "What Do Data on Millions of U.S. Workers Reveal About Lifecycle Earnings Dynamics?", Econometrica. [p. 6]
- Pruitt, S.; Turner, N. (2020) — "Earnings Risk in the Household", American Economic Review: Insights. [p. 6]
- Altonji, J. G.; Vidangos, I. (2013) — "Modeling Earnings Dynamics", Econometrica. [p. 6]
- Larrimore, J.; Lloro, A.; Merchant, Z.; Merry, E. A.; Shaalan, F.; Siwicki, J.; Zabek, M. (2025) — "Economic Well-Being of US Households in 2024", Federal Reserve Board. [p. 5]
- Cullen, J. B.; Gruber, J. (2000) — "Does unemployment insurance crowd out spousal labor supply?", Journal of Labor Economics. [p. 6]
- Stephens, M. Jr. (2002) — "Worker Displacement and the Added Worker Effect", Journal of Labor Economics. [p. 6]
- Halla, M.; Schmieder, J.; Weber, A. (2020) — "Job Displacement, Family Dynamics, and Spousal Labor Supply", American Economic Journal: Applied Economics. [p. 6]
- De Nardi, M.; Fella, G.; Paz-Pardo, G. (2020) — "Nonlinear Household Earnings Dynamics, Self-Insurance, and Welfare", Journal of the European Economic Association. [p. 6]
- Greenwood, J.; Guner, N.; Kocharkov, G.; Santos, C. (2014) — "Marry your like: Assortative mating and income inequality", American Economic Review. [p. 6]
- Eika, L.; Mogstad, M.; Zafar, B. (2019) — "Educational Assortative Mating and Household Income Inequality", Journal of Political Economy. [p. 6]
- Chiappori, P.-A.; Costa-Dias, M.; Meghir, C.; Zhang, H. (2025) — "Changes in Marital Sorting: Theory and Evidence from the US", Journal of Political Economy. [p. 6]
- Shore, S. H. (2015) — "The co-movement of couples incomes", Review of Economics of the Household. [p. 6]
- Hryshko, D.; Juhn, C.; McCue, K. (2017) — "Trends in earnings inequality and earnings instability among US couples", Labour Economics. [p. 6]
- OECD (2025) — "Employment and unemployment by five-year age group and sex - indicators". [p. 22]
- Kleven, H.; Landais, C.; Leite-Mariante, G. (2024) — "The child penalty atlas", Review of Economic Studies. [p. 25]
- Autor, D.; Kostøl, A.; Mogstad, M.; Setzler, B. (2019) — "Disability benefits, consumption insurance, and household labor supply", American Economic Review. [p. 24]
- Fadlon, I.; Nielsen, T. H. (2021) — "Family labor supply responses to severe health shocks", American Economic Journal: Applied Economics. [p. 24]
- Persson, P. (2020) — "Social insurance and the marriage market", Journal of Political Economy. [p. 24]
- Lachowska, M.; Mas, A.; Saggio, R.; Woodbury, S. A. (2022) — "Wage Posting or Wage Bargaining? A Test Using Dual Jobholders", Journal of Labor Economics. [p. 19]