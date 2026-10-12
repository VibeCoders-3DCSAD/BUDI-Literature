---
paper_id: I--Hamid-2023
first_author: Hamid
year: 2023
title: "Determinants of financial resilience: insights from an emerging economy"
venue: "Journal of Social and Economic Development, 25, 479-499"
doi: 10.1007/s40847-023-00239-y
type: journal article
designation: international
status: extracted
modules: [savings_debt_management, financial_planning]
module_rationale:
  savings_debt_management: "the paper measures and models the 'financial cushion' component (Resil 3, ability to withstand financial shock) and re-estimates resilience using five savings-ratio categories (Sect. Data and methodology, p. 483; Table 2, p. 485; Table 5, pp. 494–495)"
  financial_planning: "one of the five resilience components is 'having a financial planning' (Resil 5, actively saving and holding future financial goals), reported in Table 2 and regressed in Table 4 column 6 (Sect. Data and methodology, p. 483; Table 4, p. 491)"
---

# Determinants of financial resilience: insights from an emerging economy

`I--Hamid-2023` — Hamid, Loke and Chin (2023), *Journal of Social and Economic Development, 25, 479-499* [doi:10.1007/s40847-023-00239-y]

## Summary

Using 3,394 Malaysian adults from the 2018 OECD (INFE) Financial Literacy Survey, financial knowledge and financial inclusion predict financial resilience. Ordered logit models show higher knowledge and more bank accounts and financial products raise resilience, which also varies with age, income, education, ethnicity and region.

The paper measures resilience as five OECD components — keeping control of money, taking care of expenditures, having a financial cushion, handling financial shortfall or stress, and having financial planning — and estimates their determinants separately from a total resilience score. Higher financial knowledge is positive and significant for total resilience and for all five components, while holding no bank account or a single bank account lowers resilience relative to several bank accounts. An alternative model using the savings ratio reproduces the financial knowledge and product-holding results.

## Problem and Motivation

The 2018 OECD survey of 125,787 adults in twenty-six countries shows almost a third have savings lasting only a week and almost half are concerned about meeting everyday living expenses (p. 479). Malaysia's household debt to GDP of 93.4 percent in 2020 is the highest in the region, and household savings are low relative to OECD countries, so many households are exposed to adverse shocks (p. 480). The paper argues that studying financial resilience from an emerging-economy perspective can supply a different perspective on the topic (p. 480).

## Method

**Design.** Ordered logit (ordered logistic regression) on cross-sectional survey data; the authors give no formal design label beyond stating that "cross-sectional analysis is mostly used in studying individuals' financial resilience" (p. 483).
**Sample.** Abstract reports a sample of 3395 individuals across Malaysia (p. 479), the Data section reports a total of 3,394 individuals participated (p. 483), and the ordered logit regressions use 3,300 observations (Table 4, p. 491); the alternative savings model uses 2,352 observations (Table 5, p. 494). Unit = individual survey respondent.
**Context.** geography: Malaysia, nationwide covering the East and West of Malaysia; population: adults from age 24 and less to 60 and above, 50.8% male and 49.2% female, majority Malay (57.45%), majority secondary education (71.03%), majority low income (51.49%); setting: 2018 OECD (INFE) Financial Literacy Survey data provided by Bank Negara Malaysia, with no intervention, no software system and no experimental manipulation.

Procedure as printed:

- Financial resilience is measured by five components proposed by OECD (2020): keeping control of money (Resil 1, three questions, score 3–11), taking care of expenditures (Resil 2, two questions, 2–10), having a financial cushion (Resil 3, two questions, 2–7), handling financial shortfall or stress (Resil 4, three questions, 3–13) and having a financial planning (Resil 5, three questions, 3–12) (pp. 483–484; Table 1).
- Total Resilience is based on 13 questions with raw range 13 to 53; each component score is divided by its total and multiplied by 53, and the five weighted scores are added with an equal weight of 0.2 (pp. 483–484).
- Each weighted component score ranges from 2.12 to 10.6 and is classified low (2.12–4.95), medium (4.96–7.79) or high (7.8–10.6); Total Resilience (13.22 to 53) is classified low (13.22–26.48), medium (26.49–39.75) or high (39.76–53) (p. 486).
- Financial knowledge is measured with seven questions on time value of money, interest paid on a loan, simple interest, compound interest, risk and return, inflation and risk diversification, scored 0 to 7; low 0–2, moderate 3–4, high 5–7 (p. 486).
- Financial inclusion is measured by bank product/service use (no bank account, single bank account, several bank accounts; several banks is the reference group) and level of financial product holding across deposit, loan, credit or debit card, insurance or takaful, investment and retirement products; low is two products or less, moderate three or four, high five to six (pp. 486–487).
- Socio-demographic controls are gender, age (six categories, 24 and less as reference), education (four categories, university as reference), income (four categories, RM1500 and less as reference), ethnicity (Malays as reference), marital status (married as reference), dependents (supporting oneself as reference), region (centre Peninsula Malaysia as reference) and urbanisation (city centre as reference) (p. 487).
- Ordered logit is estimated with robust standard errors; the latent variable is y* = β′x + ε with two thresholds μ1 and μ2 estimated by maximum likelihood (Eqs. 1–7, pp. 487–488).
- An alternative resilience measure uses five savings-ratio categories of current earnings saved — less than 5 percent, 5 to 10 percent, 10 to 20 percent, 20 to 35 percent, 35 to 50 percent and above 50 percent — estimated by ordered logit (p. 486; Table 5).

## Software

- Not reported. (The reference list cites Cameron and Trivedi 2010, *Microeconometrics using stata*, but the paper does not state which software it used.)

## Key Findings

- num: high financial knowledge raises Total Resilience with coefficient 1.086*** (S.E. 0.100) and moderate knowledge 0.583*** (0.094), relative to low knowledge (Table 4, p. 491).
- num: compared with several bank accounts, no bank account lowers Total Resilience by −1.272*** (0.144) and a single bank account by −0.508*** (0.080) (Table 4, p. 491).
- num: high product holdings are positive for Total Resilience at 0.292*** (0.108), while moderate product holdings are not significant at 0.081 (0.086) (Table 4, p. 491).
- num: being male is associated with lower Total Resilience at −0.123* (0.069); higher age (60 and above 0.660***, 0.227) and higher income (high income 0.791***, 0.169) are associated with greater resilience (Table 4, p. 491).
- num: living in East Malaysia (0.819***, 0.132) or East Peninsula Malaysia (0.602***, 0.137) is associated with higher Total Resilience than the centre of Peninsula Malaysia (Table 4, p. 492).
- num: in the savings model, high financial knowledge is 0.505*** (0.116) and high product holdings 0.379*** (0.112); middle income is 1.064*** (0.209) and high income 1.459*** (0.221) (Table 5, pp. 494–495).
- num: 25.37 percent of respondents fall in the low Total Resilience category, 51.09 percent medium and 23.54 percent high (Table 2, p. 485).
- num: for the financial-cushion component (Resil 3), 44.81 percent of respondents are weak and only 4.33 percent good at it (Table 2, p. 485).
- num: for financial planning (Resil 5), 51.97 percent of respondents are good, 25.04 percent moderate and 22.98 percent weak (Table 2, p. 485).

## Key Figures and Tables

- Figure 1 (p. 482): Conceptual framework — economic resource factors (financial literacy, financial inclusion, socio-demographics) are shown feeding into financial resilience.
- Table 1 (pp. 484–485): Survey questions, answer scales and scores for the five components of financial resilience (13 questions).
- Table 2 (p. 485): Distribution of respondents across low, medium and high categories for Total Resilience and each of the five components.
- Table 3 (pp. 489–490): Financial knowledge, financial inclusion and socio-demographic variables by Total Resilience category.
- Table 4 (pp. 491–492): Ordered logit regressions on the determinants of Total Resilience and the five components, N = 3,300.
- Table 5 (pp. 494–495): Ordered logit regression using the savings ratio as an alternative financial resilience measure, N = 2,352.

## Definitions

- **Financial resilience** — measured by five components: keeping control of money, taking care of expenditures, having a financial cushion, handling financial shortfall or stress, and having financial planning (p. 483).
- **Total Resilience** — equal-weighted sum of the five standardised component scores, range 13.22 to 53, classified low, medium or high (p. 486).
- **Financial knowledge** — seven-question score, range 0 to 7, grouped low (0–2), moderate (3–4) and high (5–7) (p. 486).
- **Financial inclusion** — bank product and service usage combined with level of financial product holding (pp. 486–487).
- **Financial cushion (Resil 3)** — the ability to withstand financial shock, measured by two questions (p. 483).
- **Financial planning (Resil 5)** — actively saving and holding short- or long-term financial goals, measured by three questions (p. 483).

## Key Equations

- `y* = β′x + ε` — latent financial resilience as a function of explanatory variables (Eq. 1).
- `y = 0 (low), if y* < μ1` — observed resilience category from threshold variables (Eq. 2).
- `Pr(y = 0) = φ(−β′x)` — cumulative normal probability of the low resilience category (Eq. 5).

## Limitations and Gaps

- The study is cross-sectional, so it cannot observe how an individual recovers from a shock over time; the authors state that longitudinal data are required to capture the individuals' financial condition when the shock happens but are time consuming and costly (p. 483).
- The authors acknowledge that the assumption that each of the five resilience components contributes equally to financial resilience "may not necessarily be the case" (footnote 2, p. 484).
- The 2018 OECD survey conducted in Malaysia did not include the fraud-awareness question that OECD's conceptualisation of financial resilience otherwise includes (footnote 1, p. 480).
- [unacknowledged] Sample counts conflict: the abstract reports 3395 individuals, the Data section reports 3,394 participants, and the regressions use 3,300 observations; the paper does not explain the differences (Abstract, p. 479; p. 483; Table 4, p. 491).
- [unacknowledged] The savings model (Table 5) uses 2,352 observations against 3,300 in the main models; the paper does not state or explain the loss of observations (Table 5, p. 494).
- [unacknowledged] Only coefficients and robust standard errors are reported; no confidence intervals, marginal effects, log-likelihood, pseudo R² or proportional-odds test is given (Tables 4–5, pp. 491–495).
- [unacknowledged] No software, estimation command, sampling weight or survey-design adjustment is reported despite the analysis resting on a complex nationwide survey (pp. 486–488).
- [unacknowledged] No reliability or validity statistic (for example Cronbach alpha) is reported for the financial resilience index or the financial knowledge scale (pp. 483–486).
- [unacknowledged] The low, medium and high resilience cut-offs are arbitrary equal thirds of the observed weighted range rather than theoretically defined thresholds, and the equal-interval assumption is not justified (p. 486).
- [unacknowledged] The financial knowledge score allows an "I don't know" option and awards 1 per correct answer, but no adjustment for guessing or multiple-choice scoring is described (p. 486).
- [unacknowledged] The paper's language implies direction and comparison ("raises the probability", "more resilient") that a cross-sectional ordered logit cannot establish causally; no causal identification strategy is offered (pp. 483, 493).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Participants, abstract | individuals | 3395 | — | — | Abstract, p. 479 |
| Participants, Data section | individuals | 3,394 | — | — | p. 483 |
| Total Resilience ordered logit | observations | 3300 | — | — | Table 4, p. 491 |
| Savings model (alternative resilience measure) | observations | 2352 | — | — | Table 5, p. 494 |
| Total Resilience, low | respondents (%) | 861 (25.37) | — | — | Table 2, p. 485 |
| Total Resilience, medium | respondents (%) | 1734 (51.09) | — | — | Table 2, p. 485 |
| Total Resilience, high | respondents (%) | 799 (23.54) | — | — | Table 2, p. 485 |
| Resil 1 (keeping control of money), low | respondents (%) | 637 (18.77) | — | — | Table 2, p. 485 |
| Resil 1, medium | respondents (%) | 1429 (42.1) | — | — | Table 2, p. 485 |
| Resil 1, high | respondents (%) | 1328 (39.13) | — | — | Table 2, p. 485 |
| Resil 2 (taking care of expenditure), low | respondents (%) | 532 (15.67) | — | — | Table 2, p. 485 |
| Resil 2, medium | respondents (%) | 1160 (34.18) | — | — | Table 2, p. 485 |
| Resil 2, high | respondents (%) | 1702 (50.15) | — | — | Table 2, p. 485 |
| Resil 3 (financial cushion), low | respondents (%) | 1521 (44.81) | — | — | Table 2, p. 485 |
| Resil 3, medium | respondents (%) | 1726 (50.85) | — | — | Table 2, p. 485 |
| Resil 3, high | respondents (%) | 147 (4.33) | — | — | Table 2, p. 485 |
| Resil 4 (financial stress), low | respondents (%) | 370 (10.9) | — | — | Table 2, p. 485 |
| Resil 4, medium | respondents (%) | 1775 (52.3) | — | — | Table 2, p. 485 |
| Resil 4, high | respondents (%) | 1249 (36.8) | — | — | Table 2, p. 485 |
| Resil 5 (financial planning), low | respondents (%) | 780 (22.98) | — | — | Table 2, p. 485 |
| Resil 5, medium | respondents (%) | 850 (25.04) | — | — | Table 2, p. 485 |
| Resil 5, high | respondents (%) | 1764 (51.97) | — | — | Table 2, p. 485 |
| Financial knowledge, low | share | 25.55% | — | — | Table 3, p. 489 |
| Financial knowledge, moderate | share | 36.56% | — | — | Table 3, p. 489 |
| Financial knowledge, high | share | 37.89% | — | — | Table 3, p. 489 |
| No bank account | share | 10.58% | — | — | Table 3, p. 489 |
| Single bank account | share | 52.5% | — | — | Table 3, p. 489 |
| Several bank accounts | share | 36.92% | — | — | Table 3, p. 489 |
| Less products holding | share | 49.85% | — | — | Table 3, p. 489 |
| Moderate products holding | share | 30.47% | — | — | Table 3, p. 489 |
| High products holding | share | 19.68% | — | — | Table 3, p. 489 |
| Financial knowledge high, Total Resilience | coefficient (robust S.E.) | 1.086*** (0.100) | — | <0.01 | Table 4, p. 491 |
| Financial knowledge moderate, Total Resilience | coefficient (robust S.E.) | 0.583*** (0.094) | — | <0.01 | Table 4, p. 491 |
| No bank account, Total Resilience | coefficient (robust S.E.) | −1.272*** (0.144) | — | <0.01 | Table 4, p. 491 |
| Single bank account, Total Resilience | coefficient (robust S.E.) | −0.508*** (0.080) | — | <0.01 | Table 4, p. 491 |
| Moderate product holdings, Total Resilience | coefficient (robust S.E.) | 0.081 (0.086) | — | — | Table 4, p. 491 |
| High product holdings, Total Resilience | coefficient (robust S.E.) | 0.292*** (0.108) | — | <0.01 | Table 4, p. 491 |
| Gender (male), Total Resilience | coefficient (robust S.E.) | −0.123* (0.069) | — | <0.1 | Table 4, p. 491 |
| Age 60 and above, Total Resilience | coefficient (robust S.E.) | 0.660*** (0.227) | — | <0.01 | Table 4, p. 491 |
| Low income, Total Resilience | coefficient (robust S.E.) | 0.392*** (0.133) | — | <0.01 | Table 4, p. 491 |
| Middle income, Total Resilience | coefficient (robust S.E.) | 0.531*** (0.146) | — | <0.01 | Table 4, p. 491 |
| High income, Total Resilience | coefficient (robust S.E.) | 0.791*** (0.169) | — | <0.01 | Table 4, p. 491 |
| Secondary education, Total Resilience | coefficient (robust S.E.) | −0.549*** (0.108) | — | <0.01 | Table 4, p. 491 |
| Other ethnic, Total Resilience | coefficient (robust S.E.) | −0.425*** (0.146) | — | <0.01 | Table 4, p. 491 |
| East Peninsula Malaysia, Total Resilience | coefficient (robust S.E.) | 0.602*** (0.137) | — | <0.01 | Table 4, p. 492 |
| East Malaysia, Total Resilience | coefficient (robust S.E.) | 0.819*** (0.132) | — | <0.01 | Table 4, p. 492 |
| Financial knowledge high, Resil 1 | coefficient (robust S.E.) | 0.428*** (0.094) | — | <0.01 | Table 4, p. 491 |
| Financial knowledge high, Resil 2 | coefficient (robust S.E.) | 0.368*** (0.098) | — | <0.01 | Table 4, p. 491 |
| Financial knowledge moderate, Resil 3 | coefficient (robust S.E.) | 0.244** (0.100) | — | <0.05 | Table 4, p. 491 |
| Financial knowledge high, Resil 4 | coefficient (robust S.E.) | 0.325*** (0.100) | — | <0.01 | Table 4, p. 491 |
| Financial knowledge moderate, Resil 5 | coefficient (robust S.E.) | 0.664*** (0.097) | — | <0.01 | Table 4, p. 491 |
| Financial knowledge high, Resil 5 | coefficient (robust S.E.) | 0.746*** (0.100) | — | <0.01 | Table 4, p. 491 |
| High product holdings, Resil 1 | coefficient (robust S.E.) | 0.263** (0.107) | — | <0.05 | Table 4, p. 491 |
| No bank account, Resil 1 | coefficient (robust S.E.) | −1.223*** (0.145) | — | <0.01 | Table 4, p. 491 |
| No bank account, Resil 5 | coefficient (robust S.E.) | −0.895*** (0.137) | — | <0.01 | Table 4, p. 491 |
| Chinese, Resil 3 | coefficient (robust S.E.) | 0.319*** (0.089) | — | <0.01 | Table 4, p. 492 |
| Chinese, Resil 5 | coefficient (robust S.E.) | −0.276*** (0.083) | — | <0.01 | Table 4, p. 492 |
| Financial knowledge moderate, savings ratio | coefficient (robust S.E.) | 0.220** (0.111) | — | <0.05 | Table 5, p. 494 |
| Financial knowledge high, savings ratio | coefficient (robust S.E.) | 0.505*** (0.116) | — | <0.01 | Table 5, p. 494 |
| Moderate product holdings, savings ratio | coefficient (robust S.E.) | 0.281*** (0.095) | — | <0.01 | Table 5, p. 494 |
| High product holdings, savings ratio | coefficient (robust S.E.) | 0.379*** (0.112) | — | <0.01 | Table 5, p. 494 |
| Middle income, savings ratio | coefficient (robust S.E.) | 1.064*** (0.209) | — | <0.01 | Table 5, p. 495 |
| High income, savings ratio | coefficient (robust S.E.) | 1.459*** (0.221) | — | <0.01 | Table 5, p. 495 |
| Secondary education, savings ratio | coefficient (robust S.E.) | −0.231** (0.105) | — | <0.05 | Table 5, p. 495 |
| Other ethnic, savings ratio | coefficient (robust S.E.) | −0.711*** (0.188) | — | <0.01 | Table 5, p. 495 |
| North Peninsula Malaysia, savings ratio | coefficient (robust S.E.) | −0.427*** (0.121) | — | <0.01 | Table 5, p. 495 |
| South Peninsula Malaysia, savings ratio | coefficient (robust S.E.) | −0.383*** (0.118) | — | <0.01 | Table 5, p. 495 |
| East Malaysia, savings ratio | coefficient (robust S.E.) | 0.766*** (0.128) | — | <0.01 | Table 5, p. 495 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The Organisation for Economic Co-operation and Development Financial Literacy Survey of 2018 response is used to study the impact of financial knowledge, financial inclusion, and socio-demographic characteristics on financial resilience." | Abstract, p. 479 | data_collection |
| "The third component (Resil 3) is related to having financial cushion, taking into consideration elements connected to the ability in withstanding financial shock." | p. 483 | savings_debt_management |
| "The last component (Resil 5) is related to having a financial planning includes elements linked to actively saving and having financial goals in the future." | p. 483 | financial_planning |
| "A total of 3,394 individuals participated in the study." | p. 483 | data_collection |
| "The survey was conducted nationwide, covering the East and West of Malaysia." | p. 483 | data_collection |
| "The survey included questions on financial literacy which incorporates financial knowledge, behaviour, and attitudes." | p. 483 | data_collection |
| "Additional analysis is done by using an alternative measure of financial resilience. Access to savings has been used by Mcknight and Rucci (2020) to study resilience." | p. 486 | savings_debt_management |
| "In assessing adequacy of saving, respondents were asked how much of their current earnings do they save." | p. 486 | savings_debt_management |
| "It is also observed that in comparison with living in the centre of peninsula Malaysia, living in the rest of the regions lower the probability of having financial cushion." | p. 493 | savings_debt_management |
| "This suggests that higher financial knowledge facilitates individuals in managing their finances and handling financial shortfall and stress." | p. 496 | savings_debt_management |
| "This includes elements related to keeping control of money, taking care of expenditure, having financial cushion, handling financial shortfall and stress, and having a financial planning." | p. 496 | financial_planning |
| "Overall, it is found that higher final knowledge increases the probability of being financially resilient." | p. 496 | financial_planning |

## Remember This

- Cross-sectional ordered logit study of 3,394 (abstract) to 3,300 (regression) Malaysian adults from the 2018 OECD survey.
- Higher financial knowledge and financial inclusion raise the probability of being financially resilient.
- Only 23.54 percent of respondents are highly resilient; 44.81 percent are weak at having a financial cushion.
- Savings as an alternative resilience measure confirms financial knowledge and product holdings matter.
- Causal claims are unsupported; sample counts differ across abstract, data section and regressions.

## Cited Works

- Lusardi, Schneider and Tufano (2011) (finding) — define financial resilience as the ability to raise emergency funds; find lower resilience among younger generations. [p. 481]
- Modigliani and Brumberg (1954) (context) — Life-Cycle Hypothesis: savings let individuals face temporary income falls or unexpected expenses. [p. 481]
- Salignac et al. (2019) (context) — four-factor framework linking financial resilience to economic resources, products, knowledge and social capital. [p. 481]
- Kass-Hanna et al. (2021) (finding) — higher financial literacy is linked to more saving and better emergency preparedness. [p. 481]
- Lusardi et al. (2021) (finding) — higher financial literacy is linked to better planning, less debt constraint and more saving. [p. 481]
- Belayeth Hussain et al. (2019) (finding) — greater resilience observed among bank account holders compared with non-account holders. [p. 482]
- Lyons and Kass-Hanna (2021) (finding) — greater financial inclusion is linked to lower financial vulnerability. [p. 482]
- Cihak et al. (2016) (finding) — greater financial product holdings can contribute to financial stability. [p. 496]
- Mcknight and Rucci (2020) (methodology) — use access to savings as an indicator to assess financial resilience. [p. 486]
- Cameron and Trivedi (2010) (methodology) — justify ordered logit when a dependent variable has naturally ordered categories. [p. 487]
- Daud et al. (2019) (finding) — find no significant difference in the financial vulnerability of Malaysian men and women. [p. 496]
- Goyal et al. (2021) (context) — individuals with higher income and education have more resources and awareness to prepare for shocks. [p. 497]
- Salignac et al. (2021) (finding) — regional differences in Indonesia, with those in Bali more resilient than those in Central Java. [p. 497]
- Abdullah Yusof (2019) (finding) — observed ethnic disparity in financial fragility in Malaysia. [p. 497]
- World Bank (2019) (context) — reports high unaffordability among low- and middle-income Malaysian households and low savings. [p. 480]

---
Conversion: [`Hamid et al., 2023_marked.md`](../../literature/mds/Hamid et al., 2023_marked.md)
