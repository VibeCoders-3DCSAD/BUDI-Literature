---
paper_id: A--DeZarza-2024
first_author: de Zarzà
year: 2024
title: "Optimized Financial Planning: Integrating Individual and Cooperative Budgeting Models with LLM Recommendations"
venue: "AI, 5, 91-114"
doi: Not reported
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, linear_programming, model_algorithm_integration]
module_rationale:
  financial_planning: "The paper's stated purpose is to propose novel methodologies for individual and cooperative financial budgeting, aiming to maximize savings through optimization (Abstract, p. 1)."
  budgeting: "Individual and cooperative budget allocation models are constructed, with constraints ensuring expenses do not exceed income (Section 3, pp. 4-5)."
  savings_debt_management: "The objective function for both individual and household models is to maximize savings, and the LLM recommendations allocate specific amounts to savings, debt payments, and emergency funds (Section 3, pp. 4-5)."
  income_expense_management: "The models allocate monthly income across various expense categories such as rent, groceries, utility bills, and entertainment (Section 3, p. 4)."
  linear_programming: "A linear optimization model distributes monthly income across expense categories while maximizing savings, with LLM recommendations serving as bounds (Section 6, p. 13)."
  model_algorithm_integration: "The paper integrates LLM recommendations with econometric optimization models, using LLM outputs as initial feasible solutions or as bounds for the optimization (Abstract, p. 1; Section 3, p. 5)."
---

## Summary

The paper proposes optimization frameworks for individual and cooperative (household) financial budgeting, aiming to maximize savings by allocating monthly income across expense categories. The cooperative model extends the individual model to multiple household members with shared expenses and preference weights. A central innovation is the integration of large language model (LLM) recommendations—specifically OpenAI's GPT-4—as initial feasible solutions or as bounds for the optimization problems. The LLM provides context-aware budget recommendations that are then refined through linear programming. The paper also proposes an extended coevolutionary (EC) theory framework for modeling household financial decision-making as a multi-agent system where LLM recommendations influence agent strategies. A simulation with ten synthetic households compares original savings, LLM-recommended savings, and optimized savings. The paper reports that LLM-recommended solutions produce budget plans that are both economically sound and aligned with financial goals, though no statistical significance tests or real-user evaluations are conducted.

## Problem and Motivation

Financial planning is an indispensable part of modern life, yet the proliferation of expenses and the intricate nature of contemporary economic systems make it overwhelming for many. Traditional methods, while systematic, sometimes fail to accommodate the dynamic nature of financial needs and often lack the ability to personalize recommendations to individual or household-specific priorities (Section 1, p. 1). The paper identifies two primary challenges: first, the need to simplify the intricacies of financial decision-making for non-experts, and second, the need to create an adaptive system resilient to volatile economic dynamics (Section 1, p. 2). The authors motivate their work by the recognition that financial security and literacy are cornerstones of individual autonomy and societal well-being, and they propose an innovative solution that intersects the predictive acuity of LLMs with the foundational constructs of econometrics (Section 1, p. 2). The mathematical core is to optimize a utility function U(I, E) = α log(S) − β ∑ w_o log(E_o), where I is income, S is savings, E represents expenses across n categories, w_o are personalized preference weights, and α, β calibrate the trade-off between savings and expenditures (Equation 1, p. 2).

## Method

**Design.** Computational method-development study with simulation; the authors state no formal design label.

**Sample.** n = 10 synthetic households (unit of analysis: household), plus illustrative individual and household examples.

**Context.** geography: Not reported (the paper uses USD throughout but does not state a country; the authors are affiliated with institutions in Germany, Spain, and Italy); population: individuals and households (illustrative examples use monthly incomes of USD 5000 and USD 4000; synthetic households have incomes ~N(5000, 1000)); setting: virtual/computational simulation using OpenAI GPT-4 (gpt-4-0613) and Python; no live platform or human participants.

The paper develops two optimization models. The individual financial recommendation model maximizes savings S = I − ∑_z E_z subject to E_z ≥ 0, S ≥ 0, and ∑_z E_z ≤ I (Equations 3-6, pp. 4-5). The cooperative financial recommendation model maximizes household savings TS = ∑_o (I_o − ∑_z w_zo E_zo) subject to non-negativity, income, and shared-expense constraints (Equations 7-13, p. 5). LLM recommendations R_z are incorporated by adjusting initial allocations E_z ≈ R_z (Equation 14, p. 5). The paper also proposes a prospective validation framework involving expert review, contextual analysis, risk assessment, and ethical considerations (Section 3.1, p. 6), and a retrieval augmented generation (RAG) approach to mitigate hallucination (Section 3.2, p. 7). A linear optimization model with LLM constraints is formulated where LLM recommendations set upper bounds E_z ≤ E_z^rec and minimum spending requirements set lower bounds E_z ≥ E_z^min (Equations 34-35, p. 13). The EC theory framework models cooperative budgeting as a multi-agent system where each agent o iteratively adjusts expenses E_o(t + 1) = (1 − β C_o,t)(E_o(t) + α ∇U_o(E_o(t), E_−o(t))) + β C_o,t R_o,t, incorporating LLM recommendations R_o,t with confidence C_o,t (Equation 29, p. 13). The simulation generates synthetic financial profiles for ten households with monthly incomes normally distributed around USD 5000 with a standard deviation of USD 1000, and expenses across four categories (rent, groceries, utility bills, entertainment) following normal distributions with category-specific means and variances (Section 7.5, p. 19).

## Software

- OpenAI GPT-4 (model gpt-4-0613) (Section 7.1, p. 14; Section 7.2, p. 16; Section 7.4, p. 18)
- Python (script get_financial_recommendation; script get_cooperative_financial_recommendation) (Section 4, p. 8; Section 5, p. 11)
- Linear programming optimization model (implementation details not reported) (Section 6, p. 13)
- Regular expressions for parsing LLM output (Section 7.5, p. 19)
- Caching mechanism with recommendation_cache (Section 4, p. 8)
- Retry mechanism with exponential backoff (Section 4, p. 8)

## Key Findings

- The LLM (GPT-4) generated individual budget recommendations dividing a $3100 remaining balance into eight categories: emergency fund ($620), retirement savings ($620), debt payments ($465), personal savings/investments ($620), personal spending ($310), health and fitness ($155), education/personal development ($155), and charity ($155) (Section 7.1, p. 14).
- For a two-member household with combined income of $9000, the LLM recommended saving $1800 per month (20% of income) and allocating the remaining $4050 across utilities, healthcare, transportation, recreational expenses, and retirement contributions (Section 7.2, p. 16).
- The LLM's long-term cooperative recommendation for a household with a planned child in 3 years and a retirement horizon of 20 years allocated $500/month to an emergency fund, $300/month to a child fund, $600/month to retirement savings, $1500/month to housing, $650/month to groceries, and approximately $2450/month to daily living and unexpected costs (Section 7.4, p. 18).
- The paper states that the LLM's recommendations "align with traditional financial planning advice" and "the clarity and structure provided by the model can greatly assist users in understanding their financial standing" (Section 7.1, p. 15).
- The simulation results (Figure 2) compare original savings, optimized savings with bounds, and LLM-recommended savings, with the authors stating that "LLMs can effectively contribute to financial decision making, offering insights that align with recognized financial best practices" (Section 7.5, p. 19).
- The EC theory framework is proposed as a way to model cooperative budgeting within households, with agents iteratively adjusting expenses based on utility gradients and LLM recommendations weighted by confidence measures (Section 6, pp. 12-13).
- The paper claims that the integration of AI-driven recommendations with econometric models "paves the way for a new era in financial planning, making it more accessible and effective for a wider audience" (Abstract, p. 1).

## Key Figures and Tables

- Figure 1 (p. 9): Flowchart illustrating the financial planning methodology with LLM integration — the process starts with data collection, followed by analysis, integration of LLM insights, recommendation, implementation, and iterative review with monitoring to adjust the plan.
- Figure 2 (p. 20): Comparative analysis of household savings across three scenarios — Original Savings (savings from synthetic dataset without optimization), Optimized Savings with Bounds (savings after linear optimization with minimum essential expenditures), and LLM Recommended Savings (aggregate of savings categories suggested by the LLM including emergency fund, retirement savings, and non-retirement savings).
- Figure 3 (p. 21): Sequence diagram of the LLM financial recommender system illustrating the interaction between the user, LLM system, API interface, optimization model, and database.
- Table 1 (p. 22): Comparative analysis of traditional and proposed LLM-integrated models across six criteria — Personalization (Low vs. High), Adaptability to Market Changes (Limited vs. Enhanced), Scalability (Moderate vs. High), User Accessibility (Variable vs. Improved), Real-time Data Integration (Limited vs. Enhanced), and Long-term Financial Planning (Moderate vs. Superior).

## Limitations and Gaps

- The paper acknowledges that "when artificial neural networks (ANNs), including DL and LLMs, are trained through supervised learning, they employ a learning rule that iteratively converges toward an equilibrium... their operational mechanics do not inherently encapsulate an internal representation of the nonlinear relationships between training exemplars" (Section 1, p. 2).
- The authors acknowledge the "potential limitations and inherent risks of AI, such as errors and hallucinations, and the strategies that can be implemented to mitigate these issues, such as rigorous validation processes, the constant monitoring of AI outputs, and the incorporation of fail-safes and human oversight" (Section 1, p. 2).
- The paper acknowledges that "LLM recommendations, like budget suggestions, come with inherent uncertainties" and proposes a confidence measure C_o,t associated with each recommendation (Section 6, p. 13).
- The authors state that future work may involve "Expansion of Utility Functions... Model Robustness... Integration with Real-time Data... Human-in-the-loop Mechanism... Ethical Considerations... Scalability to Larger Cooperative Entities" (Section 8, pp. 22-23).
- The paper states that the Python script can be augmented by "Incorporating feedback mechanisms where household members can adjust recommendations based on changing financial scenarios," "Integrating data from financial institutions in real-time," and "Introducing functionalities to handle more complex financial situations, such as investments, loans, and mortgages" (Section 5, p. 12).
- [unacknowledged] The paper reports no statistical significance tests, confidence intervals, or effect sizes for any of its claims about LLM recommendation quality or the simulation results.
- [unacknowledged] The simulation uses only synthetic data with 10 households and does not validate the LLM recommendations against real household financial data or outcomes.
- [unacknowledged] The paper proposes a RAG approach and a validation framework but provides no empirical implementation or evaluation of either.
- [unacknowledged] The EC theory is presented as a mathematical framework but no simulation or experiment is conducted to test its predictions or compare them against alternatives.
- [unacknowledged] The paper does not report any measure of LLM recommendation accuracy, error rate, or comparison against ground-truth optimal allocations.
- [unacknowledged] The qualitative comparison in Table 1 rates the proposed model as "High," "Enhanced," "Superior," etc. on six criteria, but no measurement or operationalization of these criteria is provided.

## Definitions

- **LLM** — Large Language Model, specifically OpenAI's GPT-4 (gpt-4-0613) in this paper.
- **EC theory** — Extended coevolutionary theory, a framework for modeling multi-agent systems where agents adapt strategies over time and can incorporate external insights such as LLM recommendations.
- **RAG** — Retrieval Augmented Generation, a methodology for grounding LLM outputs in verifiable data by querying a curated dataset prior to generation.
- **Individual financial recommendation model** — An optimization framework maximizing savings S = I − ∑_z E_z subject to non-negativity and income constraints.
- **Cooperative financial recommendation model** — An extension of the individual model to households, maximizing TS = ∑_o (I_o − ∑_z w_zo E_zo) with preference weights w_zo and shared-expense constraints.
- **Utility function U(I, E)** — U(I, E) = α log(S) − β ∑_{o=1}^n w_o log(E_o), where α and β calibrate the trade-off between savings and expenditures (Equation 1, p. 2).
- **E_min** — Vector of minimum expenses ensuring essential spending requirements.
- **E_LLM** — Vector of LLM-recommended expenses.
- **Consumption smoothing** — A life-cycle model principle aiming to allocate resources to maintain a consistent standard of living throughout one's life.
- **Life-cycle model** — A model that simulates various stages of an individual's life from early career to retirement to prepare for financial needs and challenges.

## Key Equations

- `U(I, E) = α log(S) − β ∑_{o=1}^n w_o log(E_o)` — Utility function encapsulating financial health, where I is income, S is savings, E represents expenses across n categories, w_o are personalized preference weights, and α, β calibrate the trade-off (Equation 1, p. 2).
- `max_x {U(x) : x ∈ F, G(x) ≤ 0, H(x) = 0}` — General optimization framework where x represents financial decision variables, U is the utility function, F defines the feasible set, G represents inequality constraints, and H captures equality constraints (Equation 2, p. 3).
- `Maximize S = I − ∑_z E_z` — Individual model objective function maximizing savings after covering necessary expenses (Equation 3, p. 4).
- `Maximize TS = ∑_o (I_o − ∑_z E_zo)` — Cooperative model objective function maximizing total household savings (Equation 7, p. 5).
- `Maximize TS = ∑_o (I_o − ∑_z w_zo E_zo)` — Cooperative model with preference weights w_zo representing the importance of expense category z for member o (Equation 12, p. 5).
- `E_rent, combined ≤ E_rent,1 + E_rent,2` — Collaborative constraint for shared expenses such as rent (Equation 13, p. 5).
- `E_z ≈ R_z ∀z` — Adjustment of initial financial allocations based on LLM recommendation R_z (Equation 14, p. 5).
- `Maximize U(S, E, C) = f(S) − g(E, C)` — Utility function dependent on savings S, expenses E, and context vector C, where f(S) quantifies utility from savings and g(E, C) is a penalty function (Equation 15, p. 6).
- `Maximize U(S, E, C) subject to E_min ≤ E ≤ E_LLM, S + ∑ E ≤ I, S, E ≥ 0` — Optimization problem with LLM recommendations as bounds (Equations 16-19, p. 6).
- `RAG(E, D) → E_LLM` — RAG process with expenses E and retrieved data D mapping to LLM-recommended expenses (Equation 20, p. 7).
- `max_x U(x, θ) subject to x ∈ F(Ψ), G(x, Φ) ≤ 0, H(x, Λ) = 0` — Utility function enhanced by LLM insights θ, feasible region influenced by external data Ψ, constraints parameterized by Φ and Λ (Equation 21, p. 8).
- `∀r ∈ R, ∃t ∈ T : C(r, t) → Valid Recommendation` — Constraint satisfaction problem for verification mechanism where generated recommendations R must satisfy conditions C based on truths T from financial database D (Equation 22, p. 10).
- `max_P U(P) s.t. Q(R|P) is maximized` — Prompt optimization problem maximizing utility U of prompt P with respect to quality Q of recommendation R (Equation 23, p. 10).
- `∆x(t + 1) = F(x(t), x(t − 1), ..., x(0))` — Change in strategy vector at time t + 1 as a nonlinear function of strategy vectors at all previous time steps (Equation 24, p. 11).
- `x(t + 1) = x(t) + γ(R − x(t)) + ∆x(t + 1)` — EC model update with γ representing the rate of integration of LLM recommendations R (Equation 25, p. 11).
- `B_H = ∑_{o=1}^n (I_o − E_o)` — Collective budget of household H consisting of n members (Equation 26, p. 12).
- `E_o(t + 1) = E_o(t) + α∇U_o(E_o(t), E_−o(t))` — Agent o iteratively adjusts expenses based on utility gradient with learning rate α (Equation 27, p. 12).
- `E_o(t + 1) = (1 − β)(E_o(t) + α∇U_o(E_o(t), E_−o(t))) + βR_o,t` — Agent expense update incorporating LLM recommendation R_o,t with influence rate β (Equation 28, p. 12).
- `E_o(t + 1) = (1 − βC_o,t)(E_o(t) + α∇U_o(E_o(t), E_−o(t))) + βC_o,tR_o,t` — Expense update with confidence measure C_o,t associated with LLM recommendation (Equation 29, p. 13).
- `Maximize S = I − ∑_z E_z` — Linear optimization model objective function (Equation 30, p. 13).
- `E_z ≥ E_z^min` — Minimum spending constraint (Equation 34, p. 13).
- `E_z ≤ E_z^rec` — LLM-recommended spending constraint (Equation 35, p. 13).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Individual example: monthly income | USD | 5000 | — | — | Section 4, p. 8 |
| Individual example: rent | USD | 1200 | — | — | Section 4, p. 8 |
| Individual example: groceries | USD | 400 | — | — | Section 4, p. 8 |
| Individual example: utilities | USD | 200 | — | — | Section 4, p. 8 |
| Individual example: entertainment | USD | 100 | — | — | Section 4, p. 8 |
| Individual example: total monthly spending | USD | 1900 | — | — | Section 4, p. 8 |
| Individual example: remaining balance | USD | 3100 | — | — | Section 4, p. 8 |
| LLM individual recommendation: emergency fund | USD | 620 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: retirement savings | USD | 620 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: debt payments | USD | 465 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: personal savings/investments | USD | 620 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: personal spending | USD | 310 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: health and fitness | USD | 155 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: education/personal development | USD | 155 | — | — | Section 7.1, p. 14 |
| LLM individual recommendation: charity | USD | 155 | — | — | Section 7.1, p. 14 |
| Household example: Member 1 income | USD | 5000 | — | — | Section 5, p. 11 |
| Household example: Member 1 rent | USD | 800 | — | — | Section 5, p. 11 |
| Household example: Member 1 groceries | USD | 300 | — | — | Section 5, p. 11 |
| Household example: Member 2 income | USD | 4000 | — | — | Section 5, p. 11 |
| Household example: Member 2 rent | USD | 700 | — | — | Section 5, p. 11 |
| Household example: Member 2 groceries | USD | 350 | — | — | Section 5, p. 11 |
| Household example: combined monthly income | USD | 9000 | — | — | Section 7.2, p. 16 |
| Household example: combined rent | USD | 1500 | — | — | Section 7.2, p. 16 |
| Household example: rent as percentage of income | % | 16.67 | — | — | Section 7.2, p. 16 |
| Household example: combined groceries | USD | 650 | — | — | Section 7.2, p. 16 |
| Household example: groceries as percentage of income | % | 7.2 | — | — | Section 7.2, p. 16 |
| Household example: recommended savings | USD | 1800 | — | — | Section 7.2, p. 16 |
| Household example: remaining after rent, groceries, savings | USD | 4050 | — | — | Section 7.2, p. 16 |
| Household example: emergency fund target range | USD | 10,800–21,600 | — | — | Section 7.2, p. 16 |
| Long-term example: emergency fund | USD/month | 500 | — | — | Section 7.4, p. 18 |
| Long-term example: child fund | USD/month | 300 | — | — | Section 7.4, p. 18 |
| Long-term example: retirement savings | USD/month | 600 | — | — | Section 7.4, p. 18 |
| Long-term example: housing | USD/month | 1,500 | — | — | Section 7.4, p. 18 |
| Long-term example: groceries | USD/month | 650 | — | — | Section 7.4, p. 18 |
| Long-term example: daily living and unexpected costs | USD/month | 2450 | — | — | Section 7.4, p. 18 |
| Long-term example: basic monthly expenses | USD | 2150 | — | — | Section 7.4, p. 18 |
| Synthetic households: number | households | 10 | — | — | Section 7.5, p. 19 |
| Synthetic households: mean monthly income | USD | 5000 | — | — | Section 7.5, p. 19 |
| Synthetic households: income standard deviation | USD | 1000 | — | — | Section 7.5, p. 19 |
| LLM recommendation: rent | % of income | 24 | — | — | Figure 2, p. 20 |
| LLM recommendation: groceries | % of income | 8 | — | — | Figure 2, p. 20 |
| LLM recommendation: utility bills | % of income | 4 | — | — | Figure 2, p. 20 |
| LLM recommendation: entertainment | % of income | 2 | — | — | Figure 2, p. 20 |
| LLM recommendation: emergency fund | % of income | 20 | — | — | Figure 2, p. 20 |
| LLM recommendation: retirement savings | % of income | 15 | — | — | Figure 2, p. 20 |
| LLM recommendation: non-retirement savings | % of income | 10 | — | — | Figure 2, p. 20 |
| LLM recommendation: debts | % of income | 8.5 | — | — | Figure 2, p. 20 |
| LLM recommendation: personal spending | % of income | 8.5 | — | — | Figure 2, p. 20 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "We firstly propose an optimization framework for individual budget allocation, aiming to maximize savings by efficiently distributing monthly income among various expense categories." | Abstract, p. 1 | financial_planning |
| "A notable innovation in our approach is the integration of recommendations from a large language model (LLM)." | Abstract, p. 1 | model_algorithm_integration |
| "Our primary goal is to find the best allocation of an individual's monthly income across various expense categories while maximizing their potential savings." | Section 3, p. 4 | budgeting |
| "In a household setting, our aim is to optimize combined budget allocation for all members. We ensure that each member's preferences and necessities are accommodated." | Section 3, p. 5 | budgeting |
| "The true innovation of our approach lies in blending traditional optimization techniques with AI-driven insights." | Section 3, p. 5 | model_algorithm_integration |
| "Given a recommendation R_z from the LLM for an expense category z, we can adjust our initial financial allocations." | Section 3, p. 5 | model_algorithm_integration |
| "The approach leverages the capabilities of OpenAI's GPT-4 model to analyze a user's financial data and provide a bespoke recommendation based on that data." | Section 4, p. 8 | model_algorithm_integration |
| "Cooperative budgeting emerges as an imperative when multiple individuals, such as partners or roommates, decide to combine their financial resources and manage expenses collectively." | Section 5, p. 11 | budgeting |
| "Financial planning, at its core, is not just about budgeting for the next month or year: it is about laying a foundation for the entire life-cycle." | Section 7.3, p. 16 | financial_planning |
| "The transition from traditional optimization approaches to the use of the extended coevolutionary (EC) theory presents an innovative direction for the domain of financial planning." | Section 8, p. 22 | financial_planning |
| "The findings suggest that LLMs can effectively contribute to financial decision making, offering insights that align with recognized financial best practices." | Section 7.5, p. 19 | model_algorithm_integration |
| "Long-term models bring foresight to financial decision making. By analyzing long-term implications of current financial data, these models offer recommendations that are not just about immediate benefit but also cater to future financial health." | Section 7.3, p. 16 | financial_planning |

## Remember This

- The paper proposes individual and cooperative (household) budgeting optimization models that maximize savings by allocating income across expense categories, with LLM (GPT-4) recommendations integrated as initial feasible solutions or optimization bounds.
- The cooperative model introduces preference weights w_zo and shared-expense constraints to accommodate multiple household members' needs.
- The paper also proposes an extended coevolutionary (EC) theory framework for modeling household financial decision-making as a multi-agent system where LLM recommendations influence agent strategies.
- A simulation with ten synthetic households compares original savings, LLM-recommended savings, and optimized savings, but no statistical significance tests are reported.
- The paper claims LLM recommendations align with traditional financial planning advice, but no ground-truth comparison, real-user evaluation, or accuracy metric is provided.
- The paper acknowledges AI risks such as hallucinations and proposes RAG and expert validation as mitigations, but neither is empirically implemented or tested.
