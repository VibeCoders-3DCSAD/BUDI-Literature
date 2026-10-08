---
paper_id: A--Patra-2026
first_author: Patra
year: 2026
title: "AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation"
venue: "Engineering Research (Rademics Research Institute)"
doi: 10.71443/er.ar16
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, pfm_apps_overview, pfm_apps_features, pfm_apps_problems, pfm_apps_importance, model_algorithm_integration, data_collection, model_development, model_performance_evaluation]
module_rationale:
  financial_planning: "Goal-based financial planning — allocating resources across short-, medium- and long-term life goals — is the paper's stated subject (Abstract, p. 1; Sect. 3 Feasibility Validation Framework, p. 5)."
  budgeting: "Expense distribution and budget allocation are analysed and used to argue that fixed costs limit adjustment flexibility (Sect. 4, Fig. 8 and Table 4, pp. 11-12)."
  savings_debt_management: "Savings variability, negative-savings months and savings-investment allocation are modelled and interpreted for goal feasibility (Sect. 4, Fig. 3 and Table 2, pp. 7-8)."
  income_expense_management: "Monthly income and expense recording, categorisation and cash-flow analysis are the paper's data core (Table 1, p. 6; Table 4, p. 12)."
  pfm_apps_overview: "Robo-advisory and FinTech platforms such as Betterment and Wealthfront are surveyed as the current form of the application class (Sect. 1, p. 2)."
  pfm_apps_features: "The proposed system's feature set — tailored plans, feasibility scores and recommendations — is specified (Abstract, p. 1; Sect. 3 Result Analysis & Output, p. 5)."
  pfm_apps_problems: "Generic risk questionnaires, portfolio-optimisation bias and missing goal-feasibility analysis are named as defects of current applications (Sect. 1 and Sect. 2, p. 2)."
  pfm_apps_importance: "The paper claims benchmarking superiority in accuracy, flexibility and realism over rule-based systems (Conclusion, p. 13)."
  model_algorithm_integration: "A three-layer hybrid architecture pipelines forecasting, reinforcement learning and probabilistic feasibility validation (Sect. 3 Framework Design, p. 3; Fig. 1, p. 3)."
  data_collection: "A dedicated Data Collection & Preprocessing stage describes personal and macroeconomic data sources and cleaning (Sect. 3, p. 4)."
  model_development: "A dedicated AI Model Development stage specifies time-series (LSTM), regression, classification, clustering and RL model construction (Sect. 3, p. 4)."
  model_performance_evaluation: "An Evaluation & Validation stage names accuracy, error and computational time as model-level measures (Sect. 3, p. 5)."
---

# A--Patra-2026 — AI-Driven Goal Based Financial Planning System: A Framework for Contextual Feasibility Validation

## Summary

The paper proposes an artificial-intelligence-powered, goal-based financial planning system with a contextual feasibility-validation layer. The framework is described as a hybrid three-layer architecture — a data layer, an AI layer and a decision layer — that combines personal financial data analysis, machine-learning time-series forecasting (LSTM and regression), reinforcement learning for investment-strategy optimisation, and Monte Carlo probabilistic simulation to estimate the likelihood that a stated financial goal will be met (Abstract, p. 1; Sect. 3 Framework Design, p. 3). The stated output is a tailored financial plan, a feasibility score between 0 and 1, and recommendations such as changing savings levels, changing investment strategy, or changing the goal timeframe (Sect. 3 Result Analysis & Output, p. 5).

The paper reports no experimental evaluation. Everything labelled "results" is descriptive analysis of a single illustrative twelve-month household dataset: monthly income, expenses, savings, investment and a monthly risk score (Tables 1-3, pp. 6-11), an expense-category split (Table 4, p. 12), and a five-variable correlation matrix (Table 5, p. 13). The abstract and conclusion assert that "empirical experiments show that the proposed system increases the accuracy of forecasts, adaptability, and more accurate goal feasibility evaluations than traditional rule-based approaches" (Abstract, p. 1), and that "benchmarking suggested better performance in terms of accuracy, flexibility, and realism than existing rule-based financial systems" (Conclusion, p. 13), but no accuracy value, error value, computational time, baseline score, confidence interval or significance test appears anywhere in the paper. The extraction below records what is printed and flags where the printed evidence does not reach the printed claims.

## Problem and Motivation

The authors argue that conventional financial planning strategies have proved inadequate under growing complexity in financial decision-making and a changing economic environment (Abstract, p. 1). Goal-based financial planning is presented as a shift away from wealth maximisation toward tailoring investment strategies to life goals such as retirement, education and asset acquisition (Sect. 1, p. 1). Drawing on behavioural finance, the paper states that investment decisions are influenced by biases, emotions and risk attitudes, and that people compartmentalise goals and place different weights of importance and risk appetite on each, undermining the homogeneity assumptions of conventional portfolio optimisation (Sect. 1, p. 1).

The identified gap is twofold. First, existing robo-advisory and FinTech platforms, while convenient and cost-effective, "frequently rely on generic risk assessment questionnaires, which fail to account for the nuanced preferences of users and changes in financial circumstances", and "tend to prioritize portfolio optimization over assessing the achievability of financial goals" (Sect. 1, p. 2). This produces a gap between investment returns and goal achievement. Second, the research-gap section states that current solutions "focus primarily on portfolio management and forecasting but lack dynamic financial goal feasibility analysis", underuse behavioural factors and real-time contextual information, and rarely integrate machine learning and/or reinforcement learning models with feasibility analysis (Sect. 2, p. 2). The authors conclude that "an intelligent, context-sensitive system that harmonizes behavioral factors, real-time financial data analytics, and adaptive decision-making was needed to enhance the feasibility of achieving goals" (Sect. 2, p. 2).

Motivation for the forecasting component comes from the observation that statistical models such as ARIMA cannot cope with non-linear and non-stationary data, leading to deep-learning approaches such as LSTM (Sect. 1, p. 2). Motivation for the reinforcement-learning component comes from the claim that RL models "learn and adapt strategies over time, making them well-adapted to dynamic financial environments", though the paper itself notes that "issues related to reward function design, convergence, and volatility create difficulties in applying these models in practice" (Sect. 1, p. 2). Motivation for the feasibility component is that existing validation approaches "typically involve deterministic assumptions about income growth, inflation, and investment returns, which do not account for uncertainties", whereas Monte Carlo simulation can quantify the chances of achieving goals under different market scenarios (Sect. 1, p. 2).

## Method

**Design.** Framework-development and conceptual system-design study with descriptive analysis of a single illustrative twelve-month financial dataset; the authors label the section "Research methodology" but state no formal design label (Sect. 3, p. 3).
**Sample.** n = 12 monthly observations of one household's income, expenses, savings, investment and risk score (unit of analysis: month); no participant sample, no train/test split, and no model evaluation dataset is reported (Table 1, p. 6; Table 2, p. 8; Table 3, p. 11).
**Context.** geography: Not reported (the authors are affiliated with KIIT Deemed to be University, Bhubaneshwar, Odisha, India, but the paper states no study geography) (p. 1); population: Not reported (a single illustrative household's monthly finances) (Tables 1-3, pp. 6-11); setting: computational/conceptual — a proposed system and its equations, with no implemented software, no deployed system and no human participants (Sect. 3, pp. 3-5).

- Formulate goal-centred financial planning as a dynamic framework in which planning is based on the attainment of goals such as retirement income, education funding and wealth building, rather than wealth maximisation (Sect. 3 Problem Formulation, p. 3).
- Identify and organise financial factors — income, expenses, savings, liabilities, risk aversion, consumption patterns and external economic parameters — as interrelated elements in a multi-dimensional decision-making environment (Sect. 3, p. 3).
- Formulate the feasibility problem as an optimisation problem over time horizon, initial resources, financial markets and personal constraints, with uncertainty in income and market prices modelled (Sect. 3, p. 3).
- Design a hybrid three-layer architecture: a data layer (user financial data plus macroeconomic data), an AI layer (adaptive models) and a decision layer (actionable insights translated into advice) (Sect. 3 Framework Design, p. 3).
- Establish a data pipeline converting collected financial data into structured formats, passing transformed data to the AI layer for simultaneous predictions, classifications and optimisations, then to the decision layer for recommendations, feasibility assessments and insights (Sect. 3, p. 4).
- Collect user-specific income, expenditure, savings, investment and debt data plus macroeconomic inflation, interest-rate and market-index data; preprocess for missing values, outliers, format standardisation, normalisation and temporal conversion (Sect. 3 Data Collection & Preprocessing, p. 4).
- Structure time-based income and expense data as time series, aggregate transactional data, and apply segmentation algorithms to segment financial activities (Sect. 3, p. 4).
- Extract features encompassing cash-flow patterns, savings ratios, spending habits and inferred risk measures (Sect. 3, p. 4).
- Build time-series models (LSTM networks) to predict income, expenses and savings, and regression models to model relationships between financial variables (Sect. 3 AI Model Development, p. 4).
- Apply classification techniques to classify users by financial profile, spending habits and estimated risk attitudes, and clustering algorithms to discover user clusters with similar financial profiles (Sect. 3, p. 4).
- Develop a reinforcement-learning agent that engages with financial simulations and learns from rewards and penalties defined by goal progress, risk control and financial stability (Sect. 3, p. 4; Eq. 5, p. 10).
- Define goals as short-, medium- and long-term with their own priorities, time constraints and budgetary needs, and link planning strategies to time-bound goals and risk factors (Sect. 3 Feasibility Validation Framework, p. 5).
- Test the influence of uncertainty with Monte Carlo simulations varying income growth, spending variability, inflation and returns, producing a distribution of possible outcomes rather than a single deterministic projection (Sect. 3, p. 5).
- Assess the probability of achieving each goal from the simulated distribution of final wealth relative to the target (Eq. 8, p. 10), and periodically update the simulation with the latest data or financial circumstances (Sect. 3, p. 5).
- Evaluate at both model and system level using accuracy, error and computational time; benchmark against conventional planning approaches based on static forecasts and rule-based decision-making heuristics (Sect. 3 Evaluation & Validation, p. 5).
- Validate feasibility results for consistency with actual financial scenarios, run sensitivity testing on input variables, and assess recommendation validity against improved outcomes and user preferences (Sect. 3, p. 5).
- Produce financial plans with feasibility scores, prioritised goals, and suggestions on savings levels, investment strategies and goal timeframes (Sect. 3 Result Analysis & Output, p. 5).

## Key Findings

- The monthly income series is volatile: the paper reports income as low as approximately 41,000 and as high as 78,000 across the twelve months, with peaks in the third and seventh months and lower values in the second, tenth and eleventh months (Sect. 4, p. 6; Fig. 4, p. 7).
- In some months expenses are close to or exceed income; the paper names the second and third months, with month 2 recording savings of −17000 (Sect. 4, p. 6; Table 1, p. 6).
- Savings peak around the seventh month (51000) and turn negative in the second month (−17000), which the authors read as evidence of volatile financial circumstances requiring adaptive models (Sect. 4, pp. 6-7; Fig. 3, p. 7).
- Investment does not track savings: in month 2, with savings of −17000, investment is still 21000, which the authors attribute to prior savings, other funding sources or pre-set investment plans, and flag as a liquidity risk (Sect. 4, p. 8; Table 2, p. 8).
- Risk scores rise from 2.1 in month 1 to a peak of 9.0 in month 9, then drop sharply to 2.8 in month 10 and 4.2 in month 12; the authors read the rise as growing confidence and the fall as a return to conservatism (Sect. 4, pp. 10-11; Table 3, p. 11).
- Expense allocation is dominated by rent at 40%, followed by food at 25%, others at 20% and transport at 15%; the paper concludes that the high fixed-expense share limits flexibility for savings and investment (Sect. 4, pp. 11-12; Table 4, p. 12).
- The correlation matrix reports income–savings at 0.70 and expenses–savings at −0.60, which the authors read as evidence that income drives surplus and that expense control protects financial stability (Sect. 4, pp. 12-13; Table 5, p. 13).
- Income–investment correlation is reported as 0.45 in the table; the text describes it as "moderate positive" on p. 12 and as "weak positive" on p. 13 (Table 5, p. 13; Sect. 4, pp. 12-13).
- The risk-score row is reported as −0.20 with income, 0.15 with expenses, −0.25 with savings and 0.35 with investment, while the narrative says risk score has "moderate relationships with investment and income" (Sect. 4, p. 12; Table 5, p. 13).
- The conclusion asserts that the AI approach captured financial trends and enhanced forecasts for income, expenses and savings, that reinforcement learning allowed continuous adaptation of investment strategies, and that Monte Carlo simulation modelled goal-achievement probability — all without a printed metric (Conclusion, p. 13).
- The conclusion asserts that benchmarking "suggested better performance in terms of accuracy, flexibility, and realism than existing rule-based financial systems" (Conclusion, p. 13).
- The conclusion states that the system provided feasibility scores and specific recommendations for decision support, enhancing financial planning and decision-making (Conclusion, p. 13).
- The data availability statement says only that "All data utilized in this study have been incorporated into the manuscript" — the monthly figures are printed in Tables 1-3, but no source, collection instrument or generation procedure is named (Data Availability Statement, p. 14).

## Key Figures and Tables

- Fig. 1 (p. 3): Research methodology flowchart → the seven-stage pipeline from problem formulation through framework design, data collection and preprocessing, AI model development, feasibility validation, evaluation and validation, to result analysis and output.
- Fig. 2 (p. 6): Monthly income–expense dynamics → the income curve peaks around the third and seventh months while the expenditure curve is more diverse; the gap is read as the need for continuous monitoring.
- Fig. 3 (p. 7): Monthly savings variability → savings swing between −17000 and 51000 across the year, with the peak at month 7; the switching signs are read as evidence of volatile financial circumstances.
- Fig. 4 (p. 7): Monthly income distribution and cash-flow variability → higher values in months 3 and 7, lower in months 2, 10 and 11; interpreted as non-stable income streams that planning must accommodate.
- Fig. 5 (p. 8): Savings–investment allocation patterns → savings vary widely while investment stays relatively high and stable; investment continues in low-savings months, which the paper calls a liquidity risk.
- Fig. 6 (p. 9): Income distribution and frequency-based financial stability → income spans mid-to-high levels with clustering around particular ranges and outliers at the top, interpreted as bonuses, incentives or market conditions.
- Fig. 7 (p. 10): Risk score distribution and investor behaviour profiling → values concentrate in the lower and middle ranges, with shifts over time read as dynamic risk tolerance.
- Fig. 8 (p. 11): Expense distribution and budget allocation → the pie chart corresponds to Table 4 (rent 40%, food 25%, others 20%, transport 15%) and is used to argue that fixed costs crowd out savings.
- Fig. 9 (p. 12): Correlation matrix heatmap → warm colours for positive and cool for negative associations; income–savings positive, expenses–savings negative, risk score weakly associated with savings.
- Table 1 (p. 6): Monthly income and expense data for twelve months, with a derived savings column (income − expenses). Income ranges from 41000 to 78000; savings range from −17000 to 51000.
- Table 2 (p. 8): Savings and investment allocation for twelve months. Investment ranges from 12000 to 46000 and does not move with savings.
- Table 3 (p. 11): Monthly risk score, ranging from 1.5 (month 2) to 9.0 (month 9), with a discontinuity between month 9 and month 10.
- Table 4 (p. 12): Expense distribution by category — Rent 40%, Food 25%, Transport 15%, Others 20%.
- Table 5 (p. 13): Correlation between financial variables — a five-by-five matrix over Income, Expenses, Savings, Risk Score and Investment; diagonals are 1.00.

## Limitations and Gaps

- The paper claims "empirical experiments" (Abstract, p. 1) and "benchmarking" (Conclusion, p. 13) but reports no experiment: no model was trained, no baseline was run, and no comparison table exists anywhere in the paper. [unacknowledged]
- No accuracy, error, computational-time, precision, recall, F1, RMSE or MAPE value is printed, even though Sect. 3 Evaluation & Validation states that "performance measures such as accuracy, error, and computational time were used to assess the accuracy of prediction models and classification algorithms" (Sect. 3, p. 5). [unacknowledged]
- No confidence interval, p-value, significance test, effect size or variance estimate appears anywhere in the paper; the only inferential apparatus is qualitative description. [unacknowledged]
- The paper reports no participant sample, no user study and no usability evaluation; no SUS, ISO/IEC 25010 or comparable instrument is mentioned. Claims about personalisation and recommendation usefulness are therefore untested. [unacknowledged]
- The evaluation dataset is twelve rows of an unnamed single household's monthly finances with no stated source, collection instrument, currency or generation procedure (Tables 1-3, pp. 6-11; Data Availability Statement, p. 14). [unacknowledged]
- No train/test split, cross-validation or held-out evaluation is described for any of the LSTM, regression, classification, clustering or reinforcement-learning components. [unacknowledged]
- No implementation stack is reported: no language, framework, library, version, hardware or repository. The system is a design, not a built artefact. [unacknowledged]
- The paper contradicts itself on the income–investment correlation: the same value of 0.45 is described as "moderate positive correlations" on p. 12 and as a "weak positive correlation" on p. 13 (Table 5, p. 13; Sect. 4, pp. 12-13). Both statements are recorded here rather than reconciled.
- The narrative on the risk-score row contradicts Table 5: the text says the risk score shows "moderate relationships with investment and income" (p. 12), while the table prints −0.20 for risk score with income and 0.35 with investment (Table 5, p. 13).
- The paper acknowledges that "issues related to reward function design, convergence, and volatility create difficulties in applying these models in practice" (Sect. 1, p. 2), but does not say how the proposed RL agent addresses any of them.
- The paper acknowledges that "issues such as data variability, privacy, and lack of behavioral considerations remain" in personal financial data analytics (Sect. 1, p. 2), without specifying a mitigation in the proposed framework.
- Several numbered equations are malformed as printed — for example the regularised loss is typeset as `L(θ)= 1/n Σ(Y_i − Ŷ_i)^2 + ‖λ‖‖θ‖2` (Eq. 10, p. 10) and Eq. 5 is typeset with the reward symbol R_t detached from the summation — leaving the objective ambiguous. [unacknowledged]
- The system is presented as an integrated whole, but the paper gives no integration test, no pipeline timing, and no demonstration that the forecast output is actually consumed by the reinforcement-learning agent or the feasibility score. [unacknowledged]
- The cited literature is frequently off-domain: reference [25] is on AI-driven drug discovery, [26] and [31] on smart buildings, and [32] on supply-chain aggregate planning, yet they are cited for claims about context-sensitive financial systems (References, pp. 14-15). This weakens the stated grounding of the framework. [unacknowledged]
- The paper's own bibliographic apparatus is internally inconsistent: running heads read "2025, Vol 02. Issue 02" while the article history gives "Accepted: 18 December 2025" and the citation line gives "Engineering Research 1.1(2025):1-2" (pp. 1, 2, 16). [unacknowledged]
- The paper states that goals are categorised as short-, medium- and long-term and assessed in context (Sect. 3, p. 5), but no goal, timeframe, target amount or feasibility score is ever instantiated or reported. [unacknowledged]
- The abstract states the system "increases the accuracy of forecasts, adaptability, and more accurate goal feasibility evaluations than traditional rule-based approaches" (Abstract, p. 1), but no rule-based baseline is defined, run or measured. [unacknowledged]

## Definitions

- **Goal-based financial planning** — a planning paradigm that tailors investment strategies to life goals such as retirement, education and asset acquisition, rather than maximising wealth (Sect. 1, p. 1).
- **Context-aware system** — an AI system that considers dynamic multidimensional factors such as economic changes, time, user activities and events rather than static inputs (Sect. 1, p. 2).
- **Feasibility score (F_t)** — a normalised score between 0 and 1 for the achievability of a financial goal, combining wealth progress, savings capacity, risk level and market conditions through a sigmoid function (Eq. 6, p. 10).
- **Financial state vector (X_t)** — the multidimensional vector [I_t, E_t, S_t, R_t, B_t, M_t] combining income, expenses, savings, risk profile, behavioural factors and market conditions (Eq. 2, p. 9).
- **Contextual adjustment (C_t)** — the term subtracted in the savings equation to account for inflation impact and unexpected events (Eq. 1, p. 9).
- **Wealth evolution (W_{t+1})** — wealth at the next period as current wealth plus savings plus investment allocation times return rate (Eq. 3, p. 10).
- **Investment policy (A_t = π(X_t))** — allocation determined by a policy function dependent on savings, risk tolerance and market conditions, with weights λ1, λ2, λ3 (Eq. 9, p. 10).
- **Risk score** — a monthly scalar in Table 3 interpreted as the level of risk tolerance, ranging from 1.5 to 9.0 over the illustrative year (Table 3, p. 11).
- **Monte Carlo feasibility validation** — repeated simulation with varying return rates drawn from stochastic distributions to produce a probability of goal attainment (Eq. 7 and Eq. 8, p. 10).
- **Rule-based decision-making heuristics** — the conventional comparator approach described as relying on static growth assumptions and deterministic calculations (Sect. 3 Evaluation & Validation, p. 5).

## Key Equations

- `S_t = I_t − E_t − C_t` — savings at time t as income minus expenses minus contextual adjustments such as inflation and unexpected events (Eq. 1, p. 9).
- `X_t = [I_t, E_t, S_t, R_t, B_t, M_t]` — the financial state vector combining financial, behavioural and contextual variables (Eq. 2, p. 9).
- `W_{t+1} = W_t + S_t + A_t · r_t` — wealth evolution from savings and investment returns (Eq. 3, p. 10).
- `Ŷ_{t+1} = f_θ(X_t)` — future financial variables predicted by a trained ML model such as LSTM (Eq. 4, p. 10).
- `max_π E[Σ_{t=0}^{T} γ^t R_t (reward)]` — the reinforcement-learning objective of maximising cumulative discounted reward over time (Eq. 5, p. 10).
- `F_t = σ(α W_t/G + βS_t + γR_t + δM_t)` — feasibility of a goal as a sigmoid-normalised score in [0, 1] (Eq. 6, p. 10).
- `W_{t+1}^{(i)} = W_t + S_t + A_t · r_t^{(i)}` — scenario wealth paths generated by varying the return rate (Eq. 7, p. 10).
- `P(G) = (1/N) Σ_{i=1}^{N} I(W_T^{(i)} ≥ G)` — probability of goal attainment as the proportion of simulated scenarios reaching the target (Eq. 8, p. 10).
- `A_t = π(X_t) = λ1 S_t + λ2 R_t + λ3 M_t` — investment allocation policy as a weighted function of savings, risk tolerance and market conditions (Eq. 9, p. 10).
- `L(θ) = (1/n) Σ (Y_i − Ŷ_i)^2 + ‖λ‖‖θ‖2` — regularised loss used to train predictive models, as printed (Eq. 10, p. 10).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Month 1 income, expenses, savings | PHP (income / expenses / savings) | 56000 / 25000 / 31000 | — | — | Table 1, p. 6 |
| Month 2 income, expenses, savings | PHP (income / expenses / savings) | 41000 / 58000 / -17000 | — | — | Table 1, p. 6 |
| Month 3 income, expenses, savings | PHP (income / expenses / savings) | 78000 / 59000 / 19000 | — | — | Table 1, p. 6 |
| Month 4 income, expenses, savings | PHP (income / expenses / savings) | 51000 / 37000 / 14000 | — | — | Table 1, p. 6 |
| Month 5 income, expenses, savings | PHP (income / expenses / savings) | 46000 / 40000 / 6000 | — | — | Table 1, p. 6 |
| Month 6 income, expenses, savings | PHP (income / expenses / savings) | 57000 / 49000 / 8000 | — | — | Table 1, p. 6 |
| Month 7 income, expenses, savings | PHP (income / expenses / savings) | 77000 / 26000 / 51000 | — | — | Table 1, p. 6 |
| Month 8 income, expenses, savings | PHP (income / expenses / savings) | 62000 / 47000 / 15000 | — | — | Table 1, p. 6 |
| Month 9 income, expenses, savings | PHP (income / expenses / savings) | 56000 / 46000 / 10000 | — | — | Table 1, p. 6 |
| Month 10 income, expenses, savings | PHP (income / expenses / savings) | 42000 / 39000 / 3000 | — | — | Table 1, p. 6 |
| Month 11 income, expenses, savings | PHP (income / expenses / savings) | 41000 / 38000 / 3000 | — | — | Table 1, p. 6 |
| Month 12 income, expenses, savings | PHP (income / expenses / savings) | 43000 / 23000 / 20000 | — | — | Table 1, p. 6 |
| Month 1 savings and investment | PHP (savings / investment) | 31000 / 18000 | — | — | Table 2, p. 8 |
| Month 2 savings and investment | PHP (savings / investment) | -17000 / 21000 | — | — | Table 2, p. 8 |
| Month 3 savings and investment | PHP (savings / investment) | 19000 / 34000 | — | — | Table 2, p. 8 |
| Month 4 savings and investment | PHP (savings / investment) | 14000 / 13000 | — | — | Table 2, p. 8 |
| Month 5 savings and investment | PHP (savings / investment) | 6000 / 33000 | — | — | Table 2, p. 8 |
| Month 6 savings and investment | PHP (savings / investment) | 8000 / 27000 | — | — | Table 2, p. 8 |
| Month 7 savings and investment | PHP (savings / investment) | 51000 / 25000 | — | — | Table 2, p. 8 |
| Month 8 savings and investment | PHP (savings / investment) | 15000 / 46000 | — | — | Table 2, p. 8 |
| Month 9 savings and investment | PHP (savings / investment) | 10000 / 36000 | — | — | Table 2, p. 8 |
| Month 10 savings and investment | PHP (savings / investment) | 3000 / 12000 | — | — | Table 2, p. 8 |
| Month 11 savings and investment | PHP (savings / investment) | 3000 / 14000 | — | — | Table 2, p. 8 |
| Month 12 savings and investment | PHP (savings / investment) | 20000 / 34000 | — | — | Table 2, p. 8 |
| Month 1 risk score | risk score | 2.1 | — | — | Table 3, p. 11 |
| Month 2 risk score | risk score | 1.5 | — | — | Table 3, p. 11 |
| Month 3 risk score | risk score | 3.8 | — | — | Table 3, p. 11 |
| Month 4 risk score | risk score | 4.5 | — | — | Table 3, p. 11 |
| Month 5 risk score | risk score | 5.2 | — | — | Table 3, p. 11 |
| Month 6 risk score | risk score | 6.0 | — | — | Table 3, p. 11 |
| Month 7 risk score | risk score | 7.5 | — | — | Table 3, p. 11 |
| Month 8 risk score | risk score | 8.2 | — | — | Table 3, p. 11 |
| Month 9 risk score | risk score | 9.0 | — | — | Table 3, p. 11 |
| Month 10 risk score | risk score | 2.8 | — | — | Table 3, p. 11 |
| Month 11 risk score | risk score | 3.5 | — | — | Table 3, p. 11 |
| Month 12 risk score | risk score | 4.2 | — | — | Table 3, p. 11 |
| Rent share of monthly expenditure | % | 40 | — | — | Table 4, p. 12 |
| Food share of monthly expenditure | % | 25 | — | — | Table 4, p. 12 |
| Transport share of monthly expenditure | % | 15 | — | — | Table 4, p. 12 |
| Others share of monthly expenditure | % | 20 | — | — | Table 4, p. 12 |
| Correlation, income and expenses | correlation coefficient | 0.25 | — | — | Table 5, p. 13 |
| Correlation, income and savings | correlation coefficient | 0.70 | — | — | Table 5, p. 13 |
| Correlation, income and risk score | correlation coefficient | -0.20 | — | — | Table 5, p. 13 |
| Correlation, income and investment | correlation coefficient | 0.45 | — | — | Table 5, p. 13 |
| Correlation, expenses and savings | correlation coefficient | -0.60 | — | — | Table 5, p. 13 |
| Correlation, expenses and risk score | correlation coefficient | 0.15 | — | — | Table 5, p. 13 |
| Correlation, expenses and investment | correlation coefficient | 0.30 | — | — | Table 5, p. 13 |
| Correlation, savings and risk score | correlation coefficient | -0.25 | — | — | Table 5, p. 13 |
| Correlation, savings and investment | correlation coefficient | 0.20 | — | — | Table 5, p. 13 |
| Correlation, risk score and investment | correlation coefficient | 0.35 | — | — | Table 5, p. 13 |
| Monthly income range across the twelve-month dataset | PHP | approximately 41,000 to 78,000 | — | — | Sect. 4, p. 6 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "In the wake of growing complexity in financial decision-making and the ever-changing economic environment, conventional financial planning strategies have proven inadequate." | Abstract, p. 1 | financial_planning |
| "The tool offers tailored financial plans, feasibility measures, and recommendations to help make more realistic and informed decisions." | Abstract, p. 1 | pfm_apps_features |
| "Empirical experiments show that the proposed system increases the accuracy of forecasts, adaptability, and more accurate goal feasibility evaluations than traditional rule-based approaches." | Abstract, p. 1 | pfm_apps_importance |
| "The tend to prioritize portfolio optimization over assessing the achievability of financial goals." | Sect. 1, p. 2 | pfm_apps_problems |
| "Though robo-advisors provide benefits such as convenience, cost-effectiveness, and user-friendliness, frequently rely on generic risk assessment questionnaires, which fail to account for the nuanced preferences of users and changes in financial circumstances." | Sect. 1, p. 2 | pfm_apps_overview |
| "An intelligent, context-sensitive system that harmonizes behavioral factors, real-time financial data analytics, and adaptive decision-making was needed to enhance the feasibility of achieving goals." | Sect. 2 Research gap, p. 2 | financial_planning |
| "A hybrid AI architecture was envisaged, which involved three main layers: the data layer, the AI (artificial intelligence) layer, and the decision layer" | Sect. 3 Framework Design, p. 3 | model_algorithm_integration |
| "our system was benchmarked against conventional financial planning approaches, which are based on static forecasts and rule-based decision-making heuristics" | Sect. 3 Evaluation & Validation, p. 5 | rule_based_classification |
| "In order to test the influence of uncertainty on financial performance, the model was tested using Monte Carlo simulations." | Sect. 3 Feasibility Validation Framework, p. 5 | model_algorithm_integration |
| "Time-series models like LSTM are able to learn and predict future income trends from past data." | Sect. 4, p. 8 | model_development |
| "Savings at the time were modeled not only as the difference between income and expenses but also adjusted for contextual factors such as inflation, emergencies, or economic shocks." | Sect. 4, p. 9 | savings_debt_management |
| "The probability of achieving a financial goal was computed as the proportion of simulated scenarios where final wealth exceeded the target." | Sect. 4, p. 10 | model_algorithm_integration |
| "The highest proportion of expenditure (40%) was allocated to rent, which means that housing was the biggest expense." | Sect. 4, p. 11 | income_expense_management |
| "An increase in the proportion of income allocated to fixed expenses result in a decrease in the surplus available for savings and investment." | Sect. 4, p. 12 | budgeting |
| "There are moderate positive correlations between income and investment, indicating that higher incomes allow for more investment." | Sect. 4, p. 12 | income_expense_management |
| "A high positive correlation was noticed between income and savings, implying that increased income was correlated with increased surplus." | Sect. 4, p. 13 | savings_debt_management |
| "Machine learning techniques efficiently captured financial trends and enhanced forecasts for income, expenses, and savings." | Conclusion, p. 13 | model_development |
| "Benchmarking suggested better performance in terms of accuracy, flexibility, and realism than existing rule-based financial systems." | Conclusion, p. 13 | pfm_apps_importance |
| "The system provided feasibility scores and specific recommendations for decision support, enhancing financial planning and decision-making." | Conclusion, p. 13 | pfm_apps_features |
| "All data utilized in this study have been incorporated into the manuscript." | Data Availability Statement, p. 14 | data_collection |

## Remember This

- The paper proposes, but does not build or test, an AI goal-based financial planning system combining LSTM forecasting, reinforcement learning and Monte Carlo feasibility validation in a three-layer architecture.
- Every quantitative result in the paper is descriptive: twelve months of one illustrative household's income, expenses, savings, investment and risk score, plus an expense-category split and a five-variable correlation matrix.
- The abstract and conclusion claim "empirical experiments" and "benchmarking" superiority over rule-based systems, but no accuracy, error, computational-time, CI or p-value is printed anywhere.
- The correlation narrative contradicts the printed matrix twice: income–investment (0.45) is called both "moderate positive" and "weak positive", and the risk-score row (−0.20 with income) is described as showing moderate relationships with income.
- The paper's own cited literature is frequently off-domain (drug discovery, smart buildings, supply chains), which weakens its claimed grounding.

## Cited Works

- [1] Addy, W. A. et al. (2024) (context) — review of transforming financial planning with AI-driven analysis. [p. 14]
- [2] Abdellatef, A. (2025) (context) — how AI is redefining the future of financial planning and analysis. [p. 14]
- [3] Gadam, H. & Upadhyay, A. (2023) (context) — AI-driven financial planning: a study on predictive modelling. [p. 14]
- [4] Omoruyi, N. (2025) (methodology) — advanced computational methods for financial planning and analysis risk assessment. [p. 14]
- [5] Mlybari, E. A. & Elgohary, H. A. (2025) (context) — AI-driven value management in construction. [p. 14]
- [6] OJO, O. et al. (2025) (context) — AI-driven decision-making in financial management. [p. 14]
- [7] Cortez, A. M. (2025) (methodology) — AI-driven predictive analytics, uncertainty quantification and robust model validation for financial forecasting. [p. 14]
- [8] Hesami, S. (2025) (context) — navigating the AI-driven transformation of personal finance. [p. 14]
- [9] Talasila, S. D. (2024) (context) — AI-driven personal finance and budgeting management. [p. 14]
- [10] Sholapurapu, P. K. (2024) (context) — AI-based financial risk assessment tools in project planning and execution. [p. 14]
- [11] Duong, C. D. (2025) (context) — AI-enabled drivers and entrepreneurial feasibility. [p. 14]
- [12] Bessa, G. & Barbosa, B. (2025) (methodology) — integrating AI into scenario analysis for strategic planning under economic uncertainty. [p. 14]
- [13] Sharma, A. et al. (2025) (context) — optimising retirement income adequacy with AI-based personalised financial planning systems. [p. 14]
- [14] Thiyagarajan, V. (2024) (methodology) — AI-driven forecasting and scenario planning in a planning-and-budgeting cloud service. [p. 14]
- [15] Rainy, T. A. et al. (2023) (context) — systematic review of AI-enhanced decision support tools in information systems. [p. 14]
- [16] Celestin, M. et al. (2025) (context) — AI-driven risk forecasting theory. [p. 14]
- [17] Bukovski, K. et al. (2025) (context) — AI and open finance for holistic financial health and smart future planning. [p. 14]
- [18] Sepanosian, T. et al. (2024) (methodology) — scaling AI adoption in finance: modelling framework and implementation study. [p. 14]
- [19] Saleela, D. et al. (2025) (context) — feasibility study for an AI-driven decision support system for personalised housing adaptations. [p. 14]
- [20] Ashiedu, B. I. et al. (2023) (context) — designing financial intelligence systems for real-time decision-making in African corporates. [p. 14]
- [21] Ahirrao, Y. S. et al. (2025) (context) — AI-powered financial strategy through predictive analytics. [p. 15]
- [22] Tanim, S. H. & Ahmad, M. S. (2025) (context) — AI-driven strategic decision-making in IT project management. [p. 15]
- [23] Rong, C. (2024) (context) — AI-driven decision framework for sustainable entrepreneurship in vocational colleges. [p. 15]
- [24] Ayankoya, M. B. et al. (2025) (context) — data-driven financial optimisation for SMEs. [p. 15]
- [25] Talib, A. M. et al. (2025) (context) — critical success factors in AI-driven drug discovery using AHP. [p. 15]
- [26] Sadri, H. (2025) (context) — AI-driven integration of digital twins and blockchain for smart building management. [p. 15]
- [27] Ahmed, A. et al. (2025) (context) — AI-driven innovations in modern banking, risk management and ATM forecasting. [p. 15]
- [28] Mahamad, S. et al. (2025) (methodology) — architecting an AI-driven decision support system for online learning and assessment. [p. 15]
- [29] Ayodeji, D. C. et al. (2022) (methodology) — operationalising analytics to improve strategic planning: a business intelligence case study in digital finance. [p. 15]
- [30] Faqihi, A. & Miah, S. J. (2023) (context) — artificial-intelligence-driven talent management system: risks and options. [p. 15]
- [31] Arun, M. et al. (2025) (context) — economic, policy, social and regulatory aspects of AI-driven smart buildings. [p. 15]
- [32] Hossain, M. S. et al. (2025) (context) — AI-driven aggregate planning for sustainable supply chains. [p. 15]
- [33] Artene, A. E. et al. (2024) (context) — integrating AI-driven decision-making in financial reporting systems. [p. 15]
- [34] Arshad, N. et al. (2025) (methodology) — framework for intelligent, scalable and performance-optimised software development. [p. 15]
- [35] J. Nair, A. et al. (2025) (context) — AI-enabled FinTech for innovative sustainability in digital accounting and finance. [p. 15]
- [36] Chukwuma-Eke, E. C. et al. (2022) (methodology) — conceptual framework for financial optimisation and budget management in large-scale energy projects. [p. 15]
- [37] Grabocka, E. & Ndoka, E. (2025) (context) — AI-driven innovation within the ICT sector. [p. 15]
- [38] Yang, H. et al. (2025) (methodology) — FinRobot: generative business process AI agents for enterprise resource planning in finance. [p. 15]
- [39] Jahid, M. S. R. (2025) (context) — AI-driven optimisation and risk modelling in strategic economic zone development. [p. 15]
- [40] De Zarzà, I. et al. (2023) (methodology) — optimised financial planning integrating individual and cooperative budgeting models with LLM recommendations. [p. 15]