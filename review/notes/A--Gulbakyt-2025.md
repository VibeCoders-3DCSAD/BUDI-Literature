---
paper_id: A--Gulbakyt-2025
first_author: "Gulbakyt"
year: 2025
title: "Dynamic Model for Budget Allocation in via Multi-Criteria Optimization"
venue: "Journal of Applied Data Sciences, 6(4), 3075-3088"
doi: "Not reported"
type: journal-article
designation: algorithm
status: extracted
modules: [linear_programming, budgeting, financial_planning, model_performance_evaluation, data_collection]
module_rationale:
  linear_programming: "Sec. 3 formulates the district allocation as a quadratic program (Eqs. 1-7) solved by Sequential Quadratic Programming through MATLAB's fmincon, and Sec. 4 benchmarks it against a simplex linear-programming baseline that maximises citizen satisfaction (Table 5)."
  budgeting: "Table 4 reports the numeric budget allocated to each district and activity area, and Eqs. 3, 5-7 impose the budget ceiling, minimum floors and maximum caps the allocation must respect."
  financial_planning: "Eq. 4 combines four competing criteria - citizen satisfaction, strategic priorities, basic needs and urbanization - into one weighted objective for dividing a finite budget, which is the allocation-under-competing-needs problem the module describes."
  model_performance_evaluation: "Table 5 and Table 6 compare the proposed model and the two solvers against level-balance and linear-programming baselines on objective value, convergence, constraint handling and applicability, with Gini 0.223 and standard deviation 5.69% as fairness scores."
  data_collection: "Sec. 3 documents the inputs and their provenance - Bureau of National Statistics figures accessed December 2024 - and states that citizen voting data were synthesised from population counts reduced by approximately 30%."
---

# Dynamic Model for Budget Allocation in via Multi-Criteria Optimization

`A--Gulbakyt-2025` — Gulbakyt (2025), *Journal of Applied Data Sciences, 6(4), 3075-3088* \[doi not recorded in `metadata.json`; printed on p. 1 as `10.47738/jads.v6i4.935`]

## Summary

A multi-criteria quadratic-programming model splits one constrained Almaty regional budget of 42,656,543 thousand tenge across four districts and seven activity areas, solved by SQP to an objective value of 18,519,864.85 thousand tenge and by a Genetic Algorithm to 18,520,000.00 thousand tenge.

## Problem and Motivation

Regional funds in Kazakhstan are distributed by maslikhats, the district representative bodies, and the paper describes that procedure as opaque, low in public participation, and poorly aligned with local priorities. A tight budget forces a trade-off among competing sectors - education, healthcare, transport, infrastructure, digitalization, culture and ecology - so an allocation method is needed that satisfies several partly conflicting goals at once. Participatory budgeting, which folds public opinion into financial choices, is the mechanism the model is built to formalise.

## Method

**Design.** Computational model-development study: a mathematical allocation model is formulated and solved numerically, then compared against a second solver (GA) and against two literature baselines (level-balance and linear programming); the authors state no formal design label.
**Sample.** n = 28 optimisation variables (4 districts x 7 areas of activity) sharing one constrained budget of 42 656 543 thousand tenge; demographic, income and urbanization inputs for the four districts; citizen-vote and strategic-priority inputs synthesised; no human participants.
**Context.** geography: Almaty region, Kazakhstan - Raimbeksky, Karasaysky, Talgarsky and Kegensky districts; population: 55,000 / 230,000 / 190,000 / 45,000 district residents (Table 3, p. 3080); setting: virtual/computational - MATLAB and Python optimisation runs over official statistical inputs, with no maslikhat session, no real ballot, and no implemented policy.

- Gather input data: strategic priorities, demographic statistics, and outcomes of simulated citizen voting (Sec. 3, Fig. 1, p. 3077).
- Set the district budget total B as the sum of all district allocations and derive minimum and maximum boundaries from population, urbanization and regional profitability (Eqs. 2, 3, 5, pp. 3077-3078).
- Build a weighted objective function over four criteria - citizen satisfaction (0.2), strategic priorities (0.2), basic needs (0.3) and urbanization (0.3) (Eq. 4, p. 3078; weights p. 3080).
- Impose constraints: a total-budget equality, inequality limits on allocated amounts, and a lower and upper bound on every allocation variable (Eqs. 6-7, pp. 3078-3079).
- Solve the resulting quadratic program with Sequential Quadratic Programming through MATLAB's fmincon solver (Sec. 3, p. 3077; Fig. 4, p. 3082).
- Compare the allocation against the level-balance model and a simplex linear-programming model that maximises citizen satisfaction (Sec. 4, p. 3083; Table 5, p. 3084).
- Score the resulting allocation with fairness measures: standard deviation, coefficient of variation and Gini coefficient (Sec. 4, p. 3081).
- Record fmincon termination diagnostics and the objective-function convergence trajectory (Figs. 4-5, pp. 3082-3083).
- Re-solve the same multi-criteria problem with a Genetic Algorithm in Python using DEAP - population 200, 500 generations, 80% crossover, 5% mutation, penalised fitness (Sec. 4, p. 3084).
- Tabulate SQP against GA on objective value, convergence, accuracy, constraint handling, advantages, disadvantages and applicability (Table 6, p. 3085).

## Software

- MATLAB `fmincon` solver, Sequential Quadratic Programming method (version not reported)
- Python (version not reported)
- DEAP, the Genetic Algorithm library used for the GA implementation (version not reported)
- Python SciPy `scipy.optimize.minimize` with `method='SLSQP'`, named as an open-source equivalent of the MATLAB solver (version not reported)
- Pymoo, recommended for future work to improve constraint handling (version not reported)

## Key Findings

- num: SQP converged in 100 iterations with an objective function value of 18,519,864.85 thousand tenge and the GA reached 18,520,000.00 thousand tenge after 500 generations; the 135.15 thousand tenge gap is stated as 0.0007% of the budget and treated as confirmation that both methods are reliable (Abstract, p. 3075; Table 6, p. 3085; Sec. 4, p. 3086).
- num: Healthcare received 22.05% and transport 21.11% of the allocation, while education received 7.03% and ecology 6.99%; infrastructure received 11.26% (Sec. 4, pp. 3081, 3084).
- num: Fairness was scored with a standard deviation of sectoral shares of 5.69%, a coefficient of variation of 0.398 and a Gini coefficient of 0.223 (Abstract, p. 3075; Sec. 4, p. 3081).
- num: fmincon terminated at Func-count 128 and Fval -1.654620e+07 with First-order optimality 7.016e-01, leaving a residual constraint violation of approximately 865,100 tenge, which the paper puts at approximately 0.47% of the total budget, after the objective rose from roughly 16.5 million to 18.52 million tenge within the initial iteration and stabilised (Sec. 4, Fig. 4, p. 3082; Sec. 4, pp. 3082-3083).
- num: The criterion weights are citizen satisfaction 0.2, strategic priorities 0.2, basic needs 0.3 and urbanization 0.3, set by expert judgment (Sec. 3, p. 3080).
- num: Strategic priority multipliers ranged from 1.0 to 2.1 across activity areas and districts (Table 2, p. 3079; Sec. 3, p. 3080).
- num: In the solver comparison, GA allocated 300,000.00 thousand tenge to education in Raimbeksky against SQP's 296,622.18 thousand tenge, a difference the paper lists among minor allocation discrepancies (Sec. 5 Conclusion, p. 3086).
- Table 5 rates the proposed multi-criteria model higher than the level-balance and linear-programming baselines on financing of all categories, balance between criteria and transparency, while the level-balance model is rated only "Partly" on taking citizen opinion into account (Table 5, p. 3084).
- Table 6 contrasts SQP as deterministic, fast and high-accuracy but liable to a local minimum, with GA as stochastic, slower but robust to local minima and suited to uncertainty (Table 6, p. 3085).
- No quantitative accuracy metric is computed against real allocations; the paper states RMSE and MAE could not be calculated and names "prediction error and budget deviation" as the metrics a future data request would enable (Sec. 4, p. 3084).

## Key Figures and Tables

- Figure 1 (p. 3077): Conceptual framework of the dynamic budget allocation model → inputs feed a GA/SQP multi-criteria framework, and the result is scored for fairness.
- Figure 2 (p. 3081): Budget allocation result → the optimised B(i,j) values, showing the budget spread relatively evenly across districts while respecting the constraints.
- Figure 3 (p. 3082): Feasible budget allocation region for Healthcare and Transport with actual district-level results → all four district optima fall inside the region permitted by the minimum, maximum and total-budget constraints.
- Figure 4 (p. 3082): Optimization process - output parameters of the algorithm → the fmincon termination block from which the convergence claims are read.
- Figure 5 (p. 3083): Convergence of the objective function value during SQP optimization → a fast initial rise followed by a stabilisation phase.
- Figure 6 (p. 3085): Distribution of the budget by districts and regions, obtained using GA → the GA solution closely resembles the SQP solution but spreads other categories more uniformly.
- Table 1 (p. 3079): Distributed votes of citizens → 28 synthetic vote counts over the seven activity areas; these are the citizen-satisfaction inputs.
- Table 2 (p. 3079-3080): Unique strategic priorities → per-district priority multipliers from 1.0 to 2.1 feeding the strategic-priority criterion.
- Table 3 (p. 3080): Demographic data, profitability and quality of regions → population, annual income and urbanization coefficient per district, from the Bureau of National Statistics.
- Table 4 (p. 3081): Numerical results (thousands tenge) → the optimised allocation amounts, with the column alignment ambiguous in the conversion.
- Table 5 (p. 3084): Comparative analysis of models → level balance vs linear programming vs multi-criteria on four qualitative criteria.
- Table 6 (p. 3085): Comparative Characteristics of SQP and GA methods → the two solvers on seven characteristics including objective value, convergence and constraint handling.

## Limitations and Gaps

- The paper reports no quantitative validation of its allocation at all: RMSE and MAE could not be computed because detailed disaggregated budget data were unavailable, and government-reported allocations are typically aggregated, so the named accuracy metrics - prediction error and budget deviation - are proposed rather than measured (Sec. 4, p. 3084).
- The solver leaves a non-zero constraint violation of approximately 865,100 tenge at the final iteration, which the authors attribute to the model's nonlinear, multidimensional structure and describe as a trade-off between strict feasibility and utility within the iteration limit (Sec. 4, p. 3083).
- The four criterion weights were fixed by expert judgment and the authors state they lack grounding in formal sensitivity analysis, with systematic sensitivity testing and multi-scenario analysis deferred to future work (Sec. 3, p. 3080).
- The authors state that although strategic priority multipliers varied from 1.0 to 2.1, their specific quantitative influence on allocation was not distinctly isolated in the study (Sec. 3, p. 3080).
- The authors state the model remains at the conceptual phase, that pilot testing has been requested but not answered, and that conclusions about real-world applicability should be considered preliminary pending validation in a policy implementation context (Sec. 5, p. 3086).
- The authors identify ethical concerns: combining publicly available demographic data with subjective weights risks transparency and perceived equity, and AI-guided decisions may meet public scepticism or political opposition (Sec. 5, p. 3086).
- [unacknowledged] Citizen voting data are synthetic, generated by reducing population counts by approximately 30%, so the citizen-satisfaction criterion - one of the four weighted terms - is not grounded in any observed preference.
- [unacknowledged] The objective function value is reported three times with two different figures: 18,519,864.85 thousand tenge in the Abstract, Table 4 and Sec. 5, but 18,482 thousand tenge in the Sec. 4 baseline-comparison paragraph.
- [unacknowledged] SQP convergence is stated as "100 iterations" in the Abstract, "under 100 iterations" in Sec. 4 and "within 100 iterations" in Sec. 5, so the iteration count is given three ways without reconciliation.
- [unacknowledged] Table 4's printed cells repeat four values across seven category columns and do not resolve to a single row per district, so the per-district allocation amounts cannot be reconstructed from the table.
- [unacknowledged] The conclusion's figure and table cross-references are inconsistent with the numbering used earlier: it attributes SQP convergence to Figure 2 and GA allocation patterns to Figure 3, whereas Figures 2 and 3 are the allocation result and the feasible region, and Figures 5 and 6 carry convergence and GA distribution.

## Definitions

- **AA (Area of Activity)** — one of the seven sectors the budget is split across: education, healthcare, transport, infrastructure, digitalization, culture, ecology.
- **Maslikhat** — district representative body whose members are elected by the population of administrative-territorial units for 5 years and which largely allocates public monies across activity areas.
- **Multi-criteria optimization** — finding a solution that concurrently meets multiple, sometimes conflicting, criteria.
- **Quadratic programming** — an optimisation method in which the objective function is quadratic and the constraints are linear.
- **Sequential Quadratic Programming (SQP)** — the algorithm used here; supports linear and non-linear constraints, permits variable boundaries and constraint matrices, and approximates the target function at each iteration.
- **CU (urbanization coefficient)** — the standard ratio of urban population to total population in the region, used as a weighted factor reflecting degree of urban development.
- **Bmin, Bmax** — the minimum and maximum budget boundaries per district and activity area, derived from population, urbanization and regional profitability.
- **Level balance model** — a baseline that divides funds among regions and activity areas by predetermined thresholds, guaranteeing proportionately greater funding to more crucial areas and the bare minimum to each category.
- **Feasible region** — all budget combinations for the selected sectors that satisfy the minimum, maximum and total-budget constraints simultaneously.
- **Participatory budgeting** — a strategy that integrates public opinion into financial choices and increases equity and transparency in resource allocation.

## Key Equations

- `B = sum_i sum_j B(i,j)` — total district budget is the sum of all per-district, per-area allocations.
- `min (1/2 x^T Q x + c^T x), s.t. Aeq x = beq, Aineq x <= bineq` — the quadratic program the allocation solves.
- `Bmin(i,j) <= B(i,j) <= Bmax(i,j)` — per-variable budget floor and ceiling.
- `Objective = max( alpha * sum V(i,j)/max(V) * B(i,j) + beta * sum W(i,j)/max(W) * B(i,j) + gamma * sum 1(B(i,j) >= Bmin(i,j)) + delta * sum U(i)/max(U) * B(i,j) )` — the four-criterion weighted objective.
- `Bmin(i) = kpop * Population(i) + kurban * Urbanization(i) + kincome * Income(i)` — minimum budget boundary from population, urbanization and profitability.
- `Bmax(i) = alpha * Bmin(i)` — maximum boundary as an increase factor on the minimum.
- `Aeq * Bvec = Total budget; Aineq * Bvec <= bineq` — budget equality and inequality constraints.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Constrained regional budget distributed by the model | total budget | 42 656 543 thousand tenge | — | — | Abstract, p. 3075 |
| Allocation of the constrained regional budget | objective function value, SQP | 18,519,864.85 thousand tenge | — | — | Abstract, p. 3075 |
| Allocation of the constrained regional budget | objective function value, GA | 18,520,000.00 thousand tenge | — | — | Abstract, p. 3075 |
| Agreement between the two solvers | objective value difference | 135.15 thousand tenge | — | — | Abstract, p. 3075 |
| Agreement between the two solvers | difference as share of total budget | 0.0007% | — | — | Abstract, p. 3075 |
| Agreement between the two solvers | objective value difference | 135.15 thousand tenge | — | — | Sec. 4, p. 3086 |
| SQP solution process | iterations to convergence | 100 iterations | — | — | Abstract, p. 3075 |
| SQP solution process | iterations to convergence | under 100 iterations | — | — | Sec. 4, p. 3085 |
| GA solution process | generations to convergence | 500 generations | — | — | Abstract, p. 3075 |
| Sectoral shares of the optimised allocation | healthcare share | 22.05% | — | — | Sec. 4, p. 3081 |
| Sectoral shares of the optimised allocation | transport share | 21.11% | — | — | Sec. 4, p. 3081 |
| Sectoral shares of the optimised allocation | education share | 7.03% | — | — | Sec. 4, p. 3081 |
| Sectoral shares of the optimised allocation | ecology share | 6.99% | — | — | Sec. 4, p. 3081 |
| Sectoral shares of the optimised allocation | infrastructure share | 11.26% | — | — | Sec. 4, p. 3084 |
| Fairness of sectoral budget shares | standard deviation | 5.69% | — | — | Sec. 4, p. 3081 |
| Fairness of sectoral budget shares | coefficient of variation | 0.398 | — | — | Sec. 4, p. 3081 |
| Fairness of sectoral budget shares | Gini coefficient | 0.223 | — | — | Sec. 4, p. 3081 |
| fmincon termination diagnostics | Func-count | 128 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | Fval | -1.654620e+07 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | Feasibility (residual constraint violation) | 8.651e+05 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | Step Length | 1.435e-11 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | Norm of Step | 2.707e-06 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | First-order optimality (gradient value) | 7.016e-01 | — | — | Sec. 4, Fig. 4, p. 3082 |
| fmincon termination diagnostics | gradient norm restated in the conclusion | 0.7016 | — | — | Sec. 4, p. 3082 |
| fmincon termination diagnostics | gradient norm restated in the conclusion | 0.7016 | — | — | Sec. 5 Conclusion, p. 3086 |
| Residual infeasibility at the final iteration | constraint violation in tenge | approximately 865,100 ₸ | — | — | Sec. 4, p. 3083 |
| Residual infeasibility at the final iteration | share of total budget | ≈ 0.47% | — | — | Sec. 4, p. 3083 |
| Objective function trajectory | value at the start of optimisation | roughly 16.5 million tenge | — | — | Sec. 4, p. 3082 |
| Objective function trajectory | value after the initial iteration | 18.52 million tenge | — | — | Sec. 4, p. 3082 |
| Criterion weights in the objective function | citizen satisfaction weight | 0.2 | — | — | Sec. 3, p. 3080 |
| Criterion weights in the objective function | strategic priority weight | 0.2 | — | — | Sec. 3, p. 3080 |
| Criterion weights in the objective function | basic needs weight | 0.3 | — | — | Sec. 3, p. 3080 |
| Criterion weights in the objective function | urbanization weight | 0.3 | — | — | Sec. 3, p. 3080 |
| Strategic priority multipliers across districts and activity areas | multiplier range | 1.0 to 2.1 | — | — | Sec. 3, p. 3080 |
| Strategic priority multiplier, Talgarsky education | multiplier value | 1.3 | — | — | Sec. 4, p. 3081 |
| District populations | Raimbeksky, Karasaysky, Talgarsky, Kegensky | 55,000; 230,000; 190,000; 45,000 | — | — | Table 3, p. 3080 |
| District average annual income | Raimbeksky, Karasaysky, Talgarsky, Kegensky | 280,000; 350,000; 310,000; 260,000 thousand tenge | — | — | Table 3, p. 3080 |
| District urbanization coefficient CU | Raimbeksky, Karasaysky, Talgarsky, Kegensky | 24.5; 65.3; 60.8; 20.1 | — | — | Table 3, p. 3080 |
| District populations accessed from the Bureau of National Statistics | access date for stat.gov.kz | December 2024 | — | — | Sec. 3, p. 3080 |
| Synthetic citizen voting data | population reduction factor used to generate votes | approximately 30% | — | — | Sec. 3, p. 3079 |
| Synthetic citizen votes, Table 1 printed row 1 | vote counts across the seven activity areas | 1121; 5000; 3400; 2800; 3500; 3200; 4100 | — | — | Table 1, p. 3079 |
| Synthetic citizen votes, Table 1 printed row 2 | vote counts across the seven activity areas | 3700; 4200; 7100; 5300; 5900; 2700; 2800 | — | — | Table 1, p. 3079 |
| Synthetic citizen votes, Table 1 printed row 3 | vote counts across the seven activity areas | 5300; 4300; 6800; 4500; 6700; 800; 1500 | — | — | Table 1, p. 3079 |
| Synthetic citizen votes, Table 1 printed row 4 | vote counts across the seven activity areas | 6300; 3300; 6400; 5400; 2200; 4900; 2900 | — | — | Table 1, p. 3079 |
| Strategic priority multipliers, Table 2 printed row 1 | multiplier values across the seven activity areas | 1.1; 1.2; 1.3; 2.1; 1.8; 1.7; 1.2 | — | — | Table 2, p. 3079 |
| Strategic priority multipliers, Table 2 Kegensky district | multiplier values across the seven activity areas | 1.0; 1.5; 1.4; 1.3; 1.3; 1.2; 1.4 | — | — | Table 2, p. 3080 |
| Optimised allocation amounts reported in Table 4 | allocation amounts as printed, column alignment ambiguous | 296622.18; 2947763.44; 2904838.10; 3082251.69; 3266538.43; 2307597.61; 223033.64 | — | — | Table 4, p. 3081 |
| Optimised allocation amounts reported in Table 4 | total objective function value | 18519864.85 thousand tenge | — | — | Table 4, p. 3081 |
| Multi-criteria optimisation in the baseline-comparison paragraph | objective function value | 18,482 thousand tenge | — | — | Sec. 4, p. 3084 |
| Level-balance baseline, ecology in Talgarsky district | allocated amount | 3,253 thousand tenge | — | — | Sec. 4, p. 3083 |
| Level-balance baseline, technology in Karasaysky district | allocated amount | 1,801 thousand tenge | — | — | Sec. 4, p. 3083 |
| Linear-programming baseline, healthcare in Karasaysky district | allocated amount | 1,741 thousand tenge | — | — | Sec. 4, p. 3083 |
| Genetic Algorithm configuration | population size | 200 | — | — | Sec. 4, p. 3084 |
| Genetic Algorithm configuration | crossover rate | 80% | — | — | Sec. 4, p. 3084 |
| Genetic Algorithm configuration | mutation rate | 5% | — | — | Sec. 4, p. 3084 |
| SQP versus GA, education allocation in Raimbeksky district | GA allocation | 300,000.00 thousand tenge | — | — | Sec. 5 Conclusion, p. 3086 |
| SQP versus GA, education allocation in Raimbeksky district | SQP allocation | 296,622.18 thousand tenge | — | — | Sec. 5 Conclusion, p. 3086 |
| Evaluation coverage | quantitative accuracy metrics computed against real allocations | None; RMSE and MAE not computable and prediction error and budget deviation deferred | — | — | Sec. 4, p. 3084 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This research introduces a dynamic multi-criteria optimization framework for fair budget distribution across four districts in Kazakhstan's Almaty region." | Abstract, p. 3075 | linear_programming |
| "The minimal difference of 135.15 thousand tenge (0.0007% of the budget) underscores the reliability of both methods." | Abstract, p. 3075 | linear_programming |
| "Finding a solution that concurrently meets multiple (sometimes conflicting) criteria is the goal of multi-criteria optimization." | Sec. 2 Theoretical Basis, p. 3076 | financial_planning |
| "This approach was adopted in the absence of actual participatory budgeting records. The model is designed to simulate citizen preferences in a representative manner, serving as a proof-of-concept." | Sec. 3 Methodology, p. 3079 | data_collection |
| "These values are normalized and scaled based on their relative importance in the model, as determined by the assigned weights." | Sec. 3 Methodology, p. 3080 | financial_planning |
| "While these coefficients align with practical priorities, they lack grounding in formal sensitivity analysis." | Sec. 3 Methodology, p. 3080 | financial_planning |
| "Although strategic priority multipliers varied from 1.0 to 2.1 across activity areas and districts, their specific quantitative influence on budget allocation was not distinctly isolated in this study." | Sec. 3 Methodology, p. 3080 | model_performance_evaluation |
| "The standard deviation of the distribution was 5.69%, and the coefficient of variation stood at 0.398, suggesting moderate variability across sectors." | Sec. 4 Results and Discussion, p. 3081 | model_performance_evaluation |
| "Nevertheless, the absence of objective function optimization restricts the efficient use of resources." | Sec. 4 Results and Discussion, p. 3083 | linear_programming |
| "During the optimization process, the solver identified a non-zero constraint violation at the final iteration, approximately 865,100 ₸" | Sec. 4 Results and Discussion, p. 3083 | linear_programming |
| "a quantitative assessment using performance metrics (e.g., RMSE, MAE) could not be performed due to the lack of detailed, disaggregated budget data" | Sec. 4 Results and Discussion, p. 3084 | model_performance_evaluation |
| "Government-reported allocations are typically aggregated, hindering direct alignment with the model's framework." | Sec. 4 Results and Discussion, p. 3084 | data_collection |
| "enabling the calculation of accuracy metrics such as prediction error and budget deviation" | Sec. 4 Results and Discussion, p. 3084 | model_performance_evaluation |
| "All categories received funding, with healthcare accounting for 22.05% and transport for 21.11% securing the largest shares" | Sec. 4 Results and Discussion, p. 3084 | budgeting |
| "GA is excellent at examining trade-offs between goals and demonstrates resilience in situations involving a lot of uncertainty." | Sec. 4 Results and Discussion, p. 3085 | linear_programming |
| "although the proposed model exhibits significant potential for practical use, especially in participatory and multi-criteria regional budget allocation, it remains at the conceptual phase" | Sec. 5 Conclusion, p. 3086 | financial_planning |

## Remember This

- One Almaty regional budget is split across four districts and seven activity areas by a weighted quadratic program.
- SQP reached objective 18,519,864.85 thousand tenge; GA reached 18,520,000.00 after 500 generations.
- The paper names "budget deviation" and "prediction error" as accuracy metrics but computes neither.
- Aggregation of government-reported allocations is the stated reason no quantitative validation was possible.
- Weights 0.2, 0.2, 0.3, 0.3 come from expert judgment, not sensitivity analysis.

## Cited Works

- Gulbakyt, S.; Abdualiyev, A. (2024) (methodology) — Mathematical model for distributing financial resources using linear programming on the simplex method plus a level-balancing approach [p. 3076]
- Mazelis, L.; Krasko, A.; Krasova, E. (2021) (methodology) — Dynamic model maximising financial resource distribution for human capital growth in Primorsky Krai over multi-period interdependence [p. 3076]
- Sigala, M.; Beer, A.; Hodgson, L.; O'Connor, A. (2019) (context) — Big-data process and quality-criteria framework for measuring the impact of tourism economic development programmes [p. 3087]
- Bartocci, L.; Grossi, G.; Mauro, S.; Ebdon, C. (2023) (context) — Systematic literature review of participatory budgeting, its journey and future research directions [p. 3086]
- Hershkowitz, D.; Kahng, A.; Peters, D.; Procaccia, A. (2021) (context) — District-fair participatory budgeting as a fairness condition over accepted projects [p. 3087]
- Beikverdi, M.; Tehrani, G. N.; Shahanaghi, K. (2024) (methodology) — Bi-level model for district-fair participatory budgeting solved by decomposition methods [p. 3087]
- Zhang, W.; Xiao, M.; Gen, M.; Geng, H.; Wang, X.; Deng, M.; Zhang, G. (2024) (context) — Survey of multi-objective evolutionary algorithms enhanced with machine learning for scheduling problems [p. 3087]
- Ma, Y.; Gao, X.; Liu, C.; Li, J. (2024) (methodology) — Improved SQP and SLSQP algorithms for feasible path-based process optimisation [p. 3087]
- Rey, S.; Endriss, U.; de Haan, R. (2025) (methodology) — Framework for participatory budgeting with additional constraints, including project quotas for low-income areas [p. 3088]
- Schugurensky, D.; Mook, L. (2024) (context) — Participatory budgeting and local development: impacts, challenges and prospects [p. 3088]
- Baffo, I.; Leonardi, M.; D'Alberti, V.; Petrillo, A. (2024) (methodology) — SEESIM multi-criteria decision model for optimising sustainable public investment across economic, environmental and social goals [p. 3088]
- Abraham, R.; Samad, M. E.; Bakhach, A. M.; El-Chaarani, H.; Sardouk, A.; Nemar, S. E.; Jaber, D. (2022) (finding) — Genetic algorithm optimising random-forest model parameters increased stock-price prediction accuracy [p. 3087]
- Erdoğdu, A.; Dayi, F.; Yildiz, F.; Yanik, A.; Ganji, F. (2025) (methodology) — Hybrid of genetic algorithms with fuzzy rules to optimise the cost-time-quality ratio in agriculture [p. 3087]
- Orito, Y.; Takeda, M.; Yamamoto, H. (2009) (finding) — Index fund optimisation with a genetic algorithm and scatter-diagram coefficients of determination outperformed traditional techniques [p. 3087]
- Salami, A.; Afshar-Nadjafi, B.; Amiri, M. (2023) (baseline) — Two-stage genetic-algorithm optimisation for healthcare facility location-allocation, cited for SQP's accuracy under well-defined constraints [p. 3088]

---

Conversion: [`A--Gulbakyt-2025_marked.md`](../../literature/paper-markdowns/A--Gulbakyt-2025_marked.md)