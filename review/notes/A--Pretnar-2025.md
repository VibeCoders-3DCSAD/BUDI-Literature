---
paper_id: A--Pretnar-2025
first_author: Pretnar
year: 2025
title: "Mental Accounting Through Two-stage Budgeting Under Bounded Rationality"
venue: "Research Square (preprint)"
doi: 10.21203/rs.3.rs-7730348/v1
designation: algorithm
status: extracted
modules: [financial_planning, budgeting, savings_debt_management, income_expense_management, pfm_apps_overview, pfm_apps_problems, pfm_apps_importance, data_collection]
module_rationale:
  financial_planning: "The model is a generalized two-stage budgeting framework in which consumers first allocate income across commodity-group budgets before making individual spending decisions (Sect. 3, pp. 7-9)."
  budgeting: "The paper's central object is budget stickiness, budget re-evaluation, budget updating and budget discipline under cognitive constraints (Sect. 3.2-3.3, pp. 11-18; Sect. 5.2, pp. 28-29)."
  savings_debt_management: "Mental account balances, marginal savings, borrowing limits and counterfactual bankruptcy are modelled and reported outcomes (Sect. 3.1, p. 10; Sect. 5.4, pp. 33-36)."
  income_expense_management: "Expenditure is categorised by MCC into groceries, gasoline, food away from home and other, and weekly aggregates are built from card swipes and income loads (Sect. 4, pp. 20-21)."
  pfm_apps_overview: "Footnote 25 names Mint, Empower, YNAB, EveryDollar, Honeydue and Personal Capital and describes what these apps record and do not record (p. 20)."
  pfm_apps_problems: "The counterfactual discussion argues budgeting-app push notifications can induce more frequent over-spending and bankruptcy for sticky budgeters (Sect. 5.4, p. 36)."
  pfm_apps_importance: "The counterfactual simulates a financial planner or budgeting application constantly nudging weekly budget updates and reports who is better or worse off (Sect. 5.4, pp. 33-36)."
  data_collection: "Estimation uses an anonymized sample of low-income pre-paid debit-card users from a large North American bank, plus U.S. city-average CPI price indices (Sect. 4, pp. 20-22)."
---

## Summary

The paper builds and structurally estimates a generalised two-stage budgeting model in which consumers may be boundedly rational in the way they set and revise category budgets. In classical two-stage budgeting, money is perfectly fungible across commodity-group budgets and first-stage budgets always equal second-stage spending. The authors relax both assumptions by introducing planner/doer selves: a forward-looking planner sets ex-ante budgets, and a myopic doer realises expenditure subject to idiosyncratic preference and price shocks, so that over- or under-spending relative to budget becomes a mental-accounting state variable that feeds back into the next period's budgeting decision. Three behavioural frictions are nested: a sparse-max/narrow-bracketing constraint under which only a random subset of budgets may be re-evaluated in any period; a timing friction under which ex-ante budgets equal ex-post expenditure only on a measure-zero set of shock realisations; and a numeracy constraint under which a candidate budget is accepted only if it differs from the entering budget by more than an exogenous percentage or dollar threshold.

The model is estimated with a hierarchical Metropolis-Hastings within Gibbs MCMC algorithm on weekly, agent-level expenditure data for 2,509 low-income, underbanked pre-paid debit-card users from a large North American bank (71,859 weekly observations). Because only expenditure is observed and not budgets, budget weights, mental accounts and cognitive frictions are inferred as latent time series. The authors report that most consumers are neither fully rational nor fully behavioural: they update some, but not all, budgets each period. Ex-ante, most consumers behave like mental accounters who cut budgets after over-spending and raise them after under-spending; ex-post, a plurality behave like spendthrifts who raise spending regardless of prior over- or under-spending. A counterfactual in which every budget is re-evaluated every week leaves most consumers (68.4% baseline; 68.2% under a $1 numeracy threshold) no better off and makes a small fraction worse off, including a bankruptcy rate that rises from < 1% to 3.3% under the $1 threshold. The authors interpret these results as evidence that cognitive inattentiveness can be disciplining, and that budgeting-app nudges which make budgets easy to change may harm some consumers.

## Problem and Motivation

The paper's starting point is that budgeting is widely promoted as a way for consumers to discipline expenditure, but there is little evidence on how consumers actually use or adhere to budgets in everyday life. Mental accounting theory (Thaler, 1999) posits that consumers tag money for specific purposes, while classical expenditure models assume money is perfectly fungible and freely transferable (Deaton and Muellbauer, 1980a). The paper aims to build a general model of spending and budgeting behaviour that allows individual agents to exhibit varying degrees of bounded rationality, and to estimate it on agent-level expenditure data to quantify how far expenditure patterns reflect mental accounting.

Three questions drive the quantitative strategy: whether consumers use budgets to discipline and constrain expenditure; how the ways in which people use budgets vary; and whether consumers revise all of their budgets or only a subset. The authors also ask what happens to welfare and savings rates when budget rigidities are either enhanced or relaxed. The existing literature is characterised as having investigated consumer behaviour mainly through theory and lab experiments, with only narrow applications to field data, so a structural model estimated on high-frequency field expenditure is presented as a way to push the frontier forward. The setting — low-income, liquidity-constrained, underbanked households using a pre-paid debit card as their dominant liquidity source — is motivated as a natural application because liquidity-constrained households are budget-sensitive and often engage in non-fungible spending on basic necessities such as food.

The paper's stated contribution is both theoretical and empirical: a model environment that nests fungibility frictions from timing constraints, narrow choice bracketing, numeracy constraints on setting optimal budgets, and mental accounting; and a tractable probabilistic inference procedure that recovers latent budgeting and mental-accounting decisions from observed expenditure alone.

## Method

**Design.** Structural econometric model-development and estimation study with counterfactual simulation; the authors state no formal design label. The model is a generalized two-stage budgeting framework with planner/doer timing, estimated by a hierarchical Metropolis-Hastings within Gibbs MCMC algorithm borrowing from endogenous change-point inference techniques.

**Sample.** n = 2,509 customers contributing 71,859 weekly observations (unit of analysis: the customer-week, built from card swipes and income loads); average of approximately 29 weeks per customer, with each consumer profile containing at least 16 consecutive weeks of regular income.

**Context.** geography: United States (anonymized sample from a large North American bank; U.S. city-average CPI series used for prices); population: low-income, underbanked pre-paid debit-card users who use the card as their only banking product, with regular weekly income deposited to the card; setting: computational/structural estimation on enterprise banking transaction data spanning September 2013 to January 2016, with counterfactual simulation of relaxed rationality constraints.

Details of the modelling and estimation procedure:

- Utility is strongly separable over a J-dimensional vector of consumption quantities and unallocated liquidity, with Stone-Geary flow utility allowing zero consumption in a period (Eq. 1, p. 9).
- Expenditure is the inherited budget plus an iid idiosyncratic expenditure shock, so ex-post expenditure deviates from the ex-ante budget and the doer's realised utility is random from the doer's perspective (Eq. 2, p. 10).
- The mental account state variable equals the negative of the previous period's idiosyncratic expenditure shock, so over-spending (a < 0) and under-spending (a > 0) are tracked by category (Eq. 4, p. 12).
- The category budget is a function of income and the mental account balance, with γ_i capturing anchoring to last period's over- or under-spending (Eq. 5, p. 12).
- Budget re-evaluation is Bernoulli with agent- and category-specific probability ψ_ij, independent across categories, producing sparse-max/narrow-bracketing behaviour (Eq. 6, p. 13).
- Candidate optimal budget shares are derived by inverting the first-order conditions of the expected indirect utility problem (Eq. 10, p. 17).
- Numeracy constraints: a candidate budget is accepted under the relative margin if |ϑ* − θ_{t−1}| ≥ ε, and under the absolute margin if ℓ_it |ϑ* − θ_{t−1}| ≥ ε_ℓ (pp. 17-18).
- Six numeracy thresholds are estimated: relative ε ∈ {0, 0.01, 0.05, 0.1} and absolute ε_ℓ ∈ {0.01, 1} (p. 24).
- Additional specifications switch off behavioural features: full anchoring (γ_i = 1), no anchoring (γ_i = 0), constant budget weights (Γ = 0), no budget-updating frictions (Γ = 1), and zero initial mental account balances (p. 24).
- The estimation parameter space contains 4,664,212 parameters, of which 4,598,976 are latent, time-dependent budgeting and mental-accounting variables (p. 23).
- Consumers are type-cast ex-ante and ex-post by the sign of the posterior probability of a budget or expenditure increase conditional on the sign of the previous period's over- or under-saving, yielding four types (budget prioritizers, spending followers, spendthrifts, frugal savers) and 4² = 16 joint types (pp. 29-31).
- The counterfactual forces Γ_ijt = 1 for all i, j, t (equivalently ψ_ij = 1), so every agent updates every budget every week, and compares counterfactual predictive utility with posterior predictive utility (pp. 33-34).

## Key Findings

- num: The baseline model yields an average of 2.48 budget updates per week; the $1-threshold model yields 2.11; relative thresholds yield 1.45 (ε = 0.01), 0.89 (ε = 0.05) and 0.75 (ε = 0.1) (Sect. 5.2, p. 28).
- num: With a $1 threshold, full rationality (k = J = 4) is observed only 10% of the time, and just over 80% of consumer-week combinations exhibit some degree of bounded rationality even with no numeracy constraints (Sect. 5.2, p. 28).
- num: Raising the numeracy threshold from zero to $1 reduces updates by about 0.34 per week; relative thresholds reduce updates by 0.95 (ε = 0.01), 1.54 (ε = 0.05) and 1.69 (ε = 0.1) (Sect. 5.2, p. 29).
- num: Total budget updates fall 14.9% with the $1 threshold, 41.8% with ε = 0.01, 64% with ε = 0.05 and 70% with ε = 0.1 (Sect. 5.2, p. 29).
- num: Ex-ante, 82.6% (baseline) and 78.7% ($1 threshold) of consumers are type (i) budget prioritizers; ex-post, only 11.0% (baseline) and 10.4% ($1) are type (i), while 42.5% (baseline) and 46.8% ($1) are type (iii) spendthrifts (Table 3, p. 32).
- num: The largest joint type is ex-ante type (i) with ex-post type (iii): 0.375 (baseline) and 0.382 ($1 threshold) (Table 4, p. 33).
- num: For 68.4% of consumers (baseline) and 68.2% ($1 threshold), weekly budget updates for every category do not lead to welfare improvements relative to the posterior predictive baseline (Sect. 5.4, p. 34).
- num: The bankruptcy rate is < 1% in the baseline model and 3.3% under the $1 threshold; bankrupt consumers average 1.25 updates per week versus 2.48 (baseline) and 2.11 ($1) across the whole sample (Sect. 5.4, pp. 34-35).
- num: Differences between bankrupt consumers and all others are significant at the 1% level in both models (Sect. 5.4, p. 35).
- num: The median consumer earns $460.05 per week after taxes ($23,922.60 per year nominal); 96.8% of the sample fall below 2015 median U.S. household income of $56,516 (Sect. 4, p. 21).
- num: 7.8%, 18.3%, 30.8% and 51.4% of the sample fall below the 2015 poverty thresholds for one-, two-, three- and four-person households headed by someone under 65 (Sect. 4, p. 22).
- Consumers exhibit rich heterogeneity in the degree to which budgeting appears boundedly rational; pure mental accounting and perfect fungibility are opposing extreme cases of a fungibility continuum.
- Most consumers are neither fully rational (updating all budgets every period) nor fully behavioural (never updating any budget); they update some, but not all, budgets each period.
- The best-fitting specification is the fully parameterized $1-threshold model, which achieves the largest information gain over the baseline relative to any other fully parameterized model.
- Counterfactually relaxing rationality makes some consumers financially worse off, and the most rationally constrained consumers are most vulnerable to adverse outcomes from interventions designed to increase financial attentiveness.

## Key Figures and Tables

- Fig. 1 (p. 19): Directed graph of within-period timing — re-evaluation shocks realised, candidate budgets computed and numeracy-evaluated, expenditure shocks realised, spending occurs, mental accounts updated, move to t + 1 → budgets are set before shocks and revised only when both margins are satisfied.
- Fig. 2 (p. 25): Actual weekly spending for the median-income agent (black) with baseline predicted means (red, 95% regions in pink) and $1-threshold predicted means (blue, 95% regions in light blue) → both models predict the series almost identically.
- Fig. 3 (p. 28): Posterior density (panel a) and marginal posterior probability mass function (panel b) of the number of budget changes per period under different numeracy thresholds → few consumers update all budgets every period.
- Fig. 4 (p. 35): Density of estimated budget updates conditional on counterfactual type (Better Off, Worse Off Not Bankrupt, Worse Off Bankrupt) for baseline and $1 threshold → bankrupt consumers have lower budget-update counts.
- Table 1 (p. 22): Summary statistics over agent-level means — median income $460.052, median balances $204.734, median groceries $34.715, median auto/gas $48.430, median food away $51.965, median other $283.406; I = 2,509, total consumer weeks 71,859.
- Table 2 (p. 27): Posterior summary statistics for baseline and $1-threshold models — e.g. borrowing limit 5,311.618 in both; long-run expenditure shares 0.106, 0.146, 0.150, 0.598 in both; ψ_ij between 0.515 and 0.667; large posterior standard deviations on several likelihood and mental-account parameters in the $1-threshold model.
- Table 3 (p. 32): Marginal distributions of ex-ante and ex-post types — ex-ante type (i) dominates; ex-post plurality is type (iii).
- Table 4 (p. 33): Joint distributions of ex-ante and ex-post types — the modal cell is ex-ante type (i) with ex-post type (iii).

## Limitations and Gaps

- The results are explicitly model-dependent: because only expenditure is observed and budgets, mental accounts and cognitive frictions are latent, the quantitative conclusions depend on the parametric structure of the model (Sect. 1, p. 4; Sect. 5, p. 23).
- The authors acknowledge that restricting the analysis to pre-paid debit-card users limits inferences to a small subset of the population, namely the underbanked with limited access to other banking products (Sect. 4, p. 21).
- The authors acknowledge that the fourth expenditure category, which collects all remaining expenditure, includes both classifiable transactions outside the two-digit codes and cash withdrawals, so some possibly classifiable expenditure may be mis-categorized and cannot be reconciled without strong assumptions (footnote 27, p. 21).
- The authors acknowledge that preference shocks and price shocks cannot be separately identified because prices and quantities are not observed (Sect. 3.1, p. 11).
- The authors acknowledge that household size is not observed in the dataset, so poverty-threshold comparisons cannot be made at the household level (footnote 31, p. 22).
- The authors acknowledge that the literature contains no widely agreed-upon definition of what exactly constitutes mental accounting (Sect. 2.3, p. 5).
- The authors acknowledge that posterior variability in mental-account balance means and likelihood variances is large and is to be expected given the spikiness of the weekly series and the absence of explicit budgeting data (Sect. 5.1, p. 26).
- [unacknowledged] The headline counterfactual result — a rise in bankruptcy from < 1% to 3.3% under the $1 threshold — is a model-simulated classification; bankruptcy is never observed in the data, and no external validation of the classification is reported.
- [unacknowledged] Tables 3 and 4 report type shares without standard errors, credible intervals or posterior probabilities, so the precision of the marginal and joint distributions is unknown and the differences between baseline and $1-threshold shares are not tested.
- [unacknowledged] No out-of-sample or held-out validation is reported, and the estimated model is not benchmarked against alternative forecasting specifications on held-out expenditure data.
- [unacknowledged] Several parameter estimates in the $1-threshold model are extreme — for example τ_i2 has mean 2.18 × 10^21 with posterior S.D. 1.09 × 10^23 and τ_i4 has mean 1.29 × 10^18 with S.D. 6.44 × 10^19 (Table 2, p. 27) — which suggests non-convergence or weakly identified variance priors, yet the paper does not discuss these values or report convergence diagnostics in the main text.
- [unacknowledged] The four expenditure categories are exogenously defined by two-digit MCC codes, and the "other" bucket carries by far the largest share (long-run share 0.598, Table 2), so category-level inference for the three named categories rests on a minority of expenditure.
- [unacknowledged] The sample is drawn from a single large North American bank over September 2013 to January 2016, so the findings have no established external validity beyond that institution, period or country.
- [unacknowledged] The counterfactual compares counterfactual predictive utility with posterior predictive utility rather than with actual utility, so the welfare interpretation is relative to the model's own predictions (footnote 42, p. 34).
- [unacknowledged] The paper does not report the proportion of the sample that is fully rational versus fully behavioural under each specification as a single headline share; the reported figures are distributions across categories and thresholds, and no formal test of differences across numeracy thresholds is given for the type shares.

## Definitions

- **Two-stage budgeting** — the theory that consumers first allocate expenditure shares to broad commodity categories and then make individual spending decisions within them (Sect. 2.1, p. 3).
- **Planner / doer** — the two "selves" of the consumer: a forward-looking planner who sets ex-ante budgets subject to cognitive constraints, and a myopic doer who realises expenditure subject to shocks (Sect. 3, pp. 8-9).
- **Mental account (a_ijt)** — a state variable equal to the negative of the previous period's idiosyncratic expenditure shock for category j; a_ijt < 0 indicates over-spending and a_ijt > 0 indicates under-spending relative to budget (Eq. 4, p. 12).
- **Budget (ω_ijt)** — the category j budget in period t, a function of income and the mental account balance (Eq. 5, p. 12).
- **Quasi-share (θ_ijt)** — the share of income the consumer intends to spend on category j; it need not be interior to the unit interval and is the object the planner controls (Sect. 3.2, pp. 12-13).
- **γ_i** — the anchoring parameter capturing how much the mental account balance influences the budget; γ_i → 1 increases anchoring and γ_i = 0 removes it (Sect. 3.2, p. 12).
- **ψ_ij** — the probability that a consumer re-evaluates the budget-weighting variable for category j in the first stage of a period (Eq. 6, p. 13).
- **Γ_ijt (underlined and un-underlined)** — the indicator for the extensive-margin re-evaluation draw and, without underline, the indicator for a re-evaluation that also satisfies the numeracy constraint; Γ ≤ Γ always (pp. 14-18).
- **k_it** — the total number of budget updates the agent implements in a period, bounded above by J (p. 14).
- **Numeracy constraint (ε, ε_ℓ)** — the minimum relative or absolute difference between a candidate budget and the entering budget required for a budget update to be accepted (pp. 17-18).
- **Personal mental accounting equilibrium** — the decision-theoretic equilibrium in which, each period, budgets satisfy the sparse-max problem and numeracy constraints, budgets imply expected expenditure, expenditure satisfies the shock criterion, marginal savings follows, mental accounts update, and bank balances evolve (Definition, pp. 19-20).
- **Budget prioritizers** — consumers who cut expected (or realised) spending after over-spending and raise it after under-spending; type (i) (p. 30).
- **Spending followers** — consumers who raise expected (or realised) spending after over-spending and cut it after under-spending; type (ii) (pp. 30-31).
- **Spendthrifts** — consumers who raise expected (or realised) spending after both over- and under-spending; type (iii) (p. 31).
- **Frugal savers** — consumers who cut expected (or realised) spending after both over- and under-spending; type (iv) (p. 31).
- **MCC** — Visa merchant category classification codes; the first two digits define the expenditure categories used in the study (Sect. 4, p. 20).

## Key Equations

- `u_i(q_it, z_it) = Σ_{j=1}^{J} α_ij ln(q_ijt + 1) + α_{i,J+1} ln(z_it)` — Eq. 1, p. 9: strongly separable Stone-Geary utility over consumption quantities and unallocated liquidity.
- `x_ijt = ω_ijt + ζ_ijt` — Eq. 2, p. 10: realised expenditure equals the inherited budget plus an iid idiosyncratic expenditure shock.
- `v_it(ζ_it; p_t, ω_it, ℓ_it, b_it) = Σ α_ij ln((ω_ijt + ζ_ijt)/p_jt + 1) + α_{i,J+1} ln(ℓ_it − Σ[ω_ijt + ζ_ijt] + m_i + r_t b_it)` — Eq. 3, p. 11: realised indirect utility.
- `a_ijt = ω_ij,t−1 − x_ij,t−1 = −ζ_ij,t−1` — Eq. 4, p. 12: the mental account law of motion.
- `ω_ijt = θ_ijt ℓ_it + γ_i a_ijt` — Eq. 5, p. 12: the budgeting function.
- `Γ_ijt ~ Bernoulli(ψ_ij)` — Eq. 6, p. 13: the budget re-evaluation indicator.
- `ϑ*_it = argmax_{ϑ_it} E^ζ_it v_it(ϑ_it; θ_it \ ϑ_it, ζ_it)` — Eq. 8, p. 16: the planner's sparse-max candidate budget problem.
- Eq. 10, p. 17: the inverted analytic expression for the optimal candidate budget share ϑ*_iyt as a function of the other candidate shares, income, mental account balances, shocks, prices, borrowing limit and balances.
- Eqs. 11-12, p. 30: posterior conditional probabilities used to classify consumers as ex-ante and ex-post types based on the sign of the change in budgets or expenditure conditional on the sign of a_{i,J+1,t}.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Weeks observed per customer, median agent-level average | weeks | 25 | — | — | Table 1, p. 22 |
| Weeks observed per customer, mean agent-level average | weeks | 28.640 | — | — | Table 1, p. 22 |
| Income, median agent-level average | dollars | 460.052 | — | — | Table 1, p. 22 |
| Income, mean agent-level average | dollars | 510.732 | — | — | Table 1, p. 22 |
| Balances, median agent-level average | dollars | 204.734 | — | — | Table 1, p. 22 |
| Balances, mean agent-level average | dollars | 500.744 | — | — | Table 1, p. 22 |
| Groceries expenditure, median agent-level average | dollars | 34.715 | — | — | Table 1, p. 22 |
| Groceries expenditure, mean agent-level average | dollars | 42.018 | — | — | Table 1, p. 22 |
| Auto/Gas expenditure, median agent-level average | dollars | 48.430 | — | — | Table 1, p. 22 |
| Food Away expenditure, median agent-level average | dollars | 51.965 | — | — | Table 1, p. 22 |
| Other expenditure, median agent-level average | dollars | 283.406 | — | — | Table 1, p. 22 |
| Median consumer annual income in nominal dollars | dollars | 23,922.60 | — | — | Sect. 4, p. 21 |
| Share of sample below 2015 median U.S. household income | share | 96.8% | — | — | Sect. 4, p. 21 |
| Share of sample below one-person 2015 poverty threshold | share | 7.8% | — | — | Sect. 4, p. 22 |
| Share of sample below two-person 2015 poverty threshold | share | 18.3% | — | — | Sect. 4, p. 22 |
| Share of sample below three-person 2015 poverty threshold | share | 30.8% | — | — | Sect. 4, p. 22 |
| Share of sample below four-person 2015 poverty threshold | share | 51.4% | — | — | Sect. 4, p. 22 |
| Number of consumers | customers | 2,509 | — | — | Sect. 4, p. 21 |
| Total consumer weeks | observations | 71,859 | — | — | Sect. 4, p. 21 |
| Average weeks per customer | weeks | approximately 29 | — | — | Sect. 4, p. 21 |
| Borrowing limit, baseline model | parameter | 5,311.618 | — | — | Table 2, p. 27 |
| Borrowing limit, $1-threshold model | parameter | 5,311.618 | — | — | Table 2, p. 27 |
| Long-run expenditure share groceries, both models | share | 0.106 | — | — | Table 2, p. 27 |
| Long-run expenditure share auto/gasoline, both models | share | 0.146 | — | — | Table 2, p. 27 |
| Long-run expenditure share food away, both models | share | 0.150 | — | — | Table 2, p. 27 |
| Long-run expenditure share other, both models | share | 0.598 | — | — | Table 2, p. 27 |
| Liquidity preference α_i,J+1, baseline model | parameter | 12.178 | — | — | Table 2, p. 27 |
| Liquidity preference α_i,J+1, $1-threshold model | parameter | 11.488 | — | — | Table 2, p. 27 |
| Probability of budget update groceries ψ_i1, baseline model | probability | 0.667 | — | — | Table 2, p. 27 |
| Probability of budget update groceries ψ_i1, $1-threshold model | probability | 0.545 | — | — | Table 2, p. 27 |
| Probability of budget update auto/gasoline ψ_i2, baseline model | probability | 0.644 | — | — | Table 2, p. 27 |
| Probability of budget update auto/gasoline ψ_i2, $1-threshold model | probability | 0.545 | — | — | Table 2, p. 27 |
| Probability of budget update food away ψ_i3, baseline model | probability | 0.590 | — | — | Table 2, p. 27 |
| Probability of budget update food away ψ_i3, $1-threshold model | probability | 0.517 | — | — | Table 2, p. 27 |
| Probability of budget update other ψ_i4, baseline model | probability | 0.536 | — | — | Table 2, p. 27 |
| Probability of budget update other ψ_i4, $1-threshold model | probability | 0.515 | — | — | Table 2, p. 27 |
| Budgeted share of income groceries θ_i1, baseline model | share | 0.204 | — | — | Table 2, p. 27 |
| Budgeted share of income groceries θ_i1, $1-threshold model | share | 0.114 | — | — | Table 2, p. 27 |
| Budgeted share of income other θ_i4, baseline model | share | 2.188 | — | — | Table 2, p. 27 |
| Budgeted share of income other θ_i4, $1-threshold model | share | 0.708 | — | — | Table 2, p. 27 |
| Realised budget-update indicator groceries Γ_i1, baseline model | probability | 0.694 | — | — | Table 2, p. 27 |
| Realised budget-update indicator groceries Γ_i1, $1-threshold model | probability | 0.566 | — | — | Table 2, p. 27 |
| Mental account balance other a_i4, baseline model | dollars | -158.191 | — | — | Table 2, p. 27 |
| Mental account balance other a_i4, $1-threshold model | dollars | 211.587 | — | — | Table 2, p. 27 |
| Global mean of µ_α_i,J+1, baseline model | parameter | 14.844 | — | — | Table 2, p. 27 |
| Global mean of µ_α_i,J+1, $1-threshold model | parameter | 13.074 | — | — | Table 2, p. 27 |
| Global S.D. of µ_α_i,J+1, baseline model | parameter | 0.501 | — | — | Table 2, p. 27 |
| Global S.D. of µ_α_i,J+1, $1-threshold model | parameter | 3.512 | — | — | Table 2, p. 27 |
| Parameter-space dimension of preferred model | parameters | 4,664,212 | — | — | Sect. 5, p. 23 |
| Latent time-dependent budgeting and mental-accounting parameters | parameters | 4,598,976 | — | — | Sect. 5, p. 23 |
| Budget updates per week, baseline model | updates/week | 2.48 | — | — | Sect. 5.2, p. 28 |
| Budget updates per week, absolute threshold ε_ℓ = 0.01 | updates/week | 2.51 | — | — | Sect. 5.2, p. 28 |
| Budget updates per week, $1-threshold model | updates/week | 2.11 | — | — | Sect. 5.2, p. 28 |
| Budget updates per week, relative threshold ε = 0.01 | updates/week | 1.45 | — | — | Sect. 5.2, p. 28 |
| Budget updates per week, relative threshold ε = 0.05 | updates/week | 0.89 | — | — | Sect. 5.2, p. 28 |
| Budget updates per week, relative threshold ε = 0.1 | updates/week | 0.75 | — | — | Sect. 5.2, p. 28 |
| Full rationality (k = J = 4) frequency, $1 threshold | share of consumer-weeks | 10% | — | — | Sect. 5.2, p. 28 |
| Bounded rationality prevalence with no numeracy constraints | share of consumer-weeks | just over 80% | — | — | Sect. 5.2, p. 28 |
| Reduction in weekly updates from $1 threshold | updates/week | 0.34 | — | — | Sect. 5.2, p. 29 |
| Reduction in weekly updates at ε = 0.01 | updates/week | 0.95 | — | — | Sect. 5.2, p. 29 |
| Reduction in weekly updates at ε = 0.05 | updates/week | 1.54 | — | — | Sect. 5.2, p. 29 |
| Reduction in weekly updates at ε = 0.1 | updates/week | 1.69 | — | — | Sect. 5.2, p. 29 |
| Drop in total budget updates, $1 threshold | percent | 14.9% | — | — | Sect. 5.2, p. 29 |
| Drop in total budget updates, ε = 0.01 | percent | 41.8% | — | — | Sect. 5.2, p. 29 |
| Drop in total budget updates, ε = 0.05 | percent | 64% | — | — | Sect. 5.2, p. 29 |
| Drop in total budget updates, ε = 0.1 | percent | 70% | — | — | Sect. 5.2, p. 29 |
| Ex-ante type (i) budget prioritizers, baseline | share | 0.826 | — | — | Table 3, p. 32 |
| Ex-ante type (i) budget prioritizers, $1-threshold | share | 0.787 | — | — | Table 3, p. 32 |
| Ex-ante type (ii) spending followers, baseline | share | 0.042 | — | — | Table 3, p. 32 |
| Ex-ante type (ii) spending followers, $1-threshold | share | 0.057 | — | — | Table 3, p. 32 |
| Ex-ante type (iii) spendthrifts, baseline | share | 0.075 | — | — | Table 3, p. 32 |
| Ex-ante type (iii) spendthrifts, $1-threshold | share | 0.096 | — | — | Table 3, p. 32 |
| Ex-ante type (iv) frugal savers, baseline | share | 0.058 | — | — | Table 3, p. 32 |
| Ex-ante type (iv) frugal savers, $1-threshold | share | 0.060 | — | — | Table 3, p. 32 |
| Ex-post type (i) spending prioritizers, baseline | share | 0.110 | — | — | Table 3, p. 32 |
| Ex-post type (i) spending prioritizers, $1-threshold | share | 0.104 | — | — | Table 3, p. 32 |
| Ex-post type (ii) spending followers, baseline | share | 0.305 | — | — | Table 3, p. 32 |
| Ex-post type (ii) spending followers, $1-threshold | share | 0.318 | — | — | Table 3, p. 32 |
| Ex-post type (iii) spendthrifts, baseline | share | 0.425 | — | — | Table 3, p. 32 |
| Ex-post type (iii) spendthrifts, $1-threshold | share | 0.468 | — | — | Table 3, p. 32 |
| Ex-post type (iv) frugal savers, baseline | share | 0.160 | — | — | Table 3, p. 32 |
| Ex-post type (iv) frugal savers, $1-threshold | share | 0.110 | — | — | Table 3, p. 32 |
| Joint ex-ante (i) / ex-post (i), baseline | share | 0.102 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (ii), baseline | share | 0.220 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (iii), baseline | share | 0.375 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (iv), baseline | share | 0.128 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (i), $1-threshold | share | 0.093 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (ii), $1-threshold | share | 0.223 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (iii), $1-threshold | share | 0.382 | — | — | Table 4, p. 33 |
| Joint ex-ante (i) / ex-post (iv), $1-threshold | share | 0.089 | — | — | Table 4, p. 33 |
| Share with no welfare improvement from weekly full budget updates, baseline | share | 68.4% | — | — | Sect. 5.4, p. 34 |
| Share with no welfare improvement from weekly full budget updates, $1-threshold | share | 68.2% | — | — | Sect. 5.4, p. 34 |
| Share with lower overall utility under relaxed constraints | share | >65% | — | — | Sect. 5.4, p. 34 |
| Bankruptcy rate, baseline model | share | < 1% | — | — | Sect. 5.4, p. 34 |
| Bankruptcy rate, $1-threshold model | share | 3.3% | — | — | Sect. 5.4, p. 34 |
| Bankrupt consumers' average weekly budget updates | updates/week | 1.25 | — | — | Sect. 5.4, p. 35 |
| Difference between bankrupt and other consumers' behavioural profiles (both models) | significance level | significant at the 1% level | — | 1% level | Sect. 5.4, p. 35 |
| Median-income consumer mean weekly grocery expenditure | dollars | 60.67 | — | — | Fig. 2, p. 25 |
| Median-income consumer mean weekly auto/gasoline expenditure | dollars | 32.50 | — | — | Fig. 2, p. 25 |
| Median-income consumer mean weekly food-away expenditure | dollars | 21.98 | — | — | Fig. 2, p. 25 |
| Median-income consumer mean weekly other expenditure | dollars | 357.00 | — | — | Fig. 2, p. 25 |
| Median-income consumer average weekly card balance after spending | dollars | 115.21 | — | — | Fig. 2, p. 25 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "We propose a model that generalizes two-stage budgeting to incorporate frictions which induce budgetary stickiness and mental accounting behavior." | Abstract, p. 1 | budgeting |
| "Inattention limits the fungibility of money across mental accounts, leading to boundedly rational behavior." | Abstract, p. 1 | budgeting |
| "Financial attentiveness is cognitively costly, so consumers might re-assess only a subset of spending budgets every period." | Abstract, p. 1 | budgeting |
| "Attentiveness constraints can have a disciplinary effect on finances: relaxing constraints leads some consumers to over-spend and become financially worse off." | Abstract, p. 1 | pfm_apps_importance |
| "Our quantitative results indicate that consumer decision-making is neither fully rational nor fully irrational, but rather budgeting behavior falls along a rationality continuum." | Sect. 1, p. 1 | budgeting |
| "In our model, mental accounting is just a book-keeping mechanism which may inform budget responsiveness" | Sect. 2.3, p. 5 | income_expense_management |
| "Expenditure is categorized by 4-digit Visa merchant category classification codes (MCC)." | Sect. 4, p. 20 | income_expense_management |
| "Financial-planning and budgeting apps (e.g., Mint, Empower, YNAB (You Need a Budget), EveryDollar, Honeydue, and Personal Capital) record budgeting goals, sometimes by category" | Footnote 25, p. 20 | pfm_apps_overview |
| "users opt in to using such apps, meaning that conclusions drawn from their data are likely plagued by selection bias." | Footnote 25, p. 20 | pfm_apps_problems |
| "we have a total of I = 2,509 customers with a total of 71,859 weekly observations" | Sect. 4, p. 21 | data_collection |
| "The median consumer in our sample earns $460.05 per week after taxes, which aggregates to $23,922.60 per year in nominal dollars." | Sect. 4, p. 21 | financial_planning |
| "restricting the analysis to pre-paid debit card users limits inferences to only a small subset of the population, namely the underbanked with limited access to other banking products" | Sect. 4, p. 21 | data_collection |
| "In the baseline model consumers make an average of 2.48 budget updates every week." | Sect. 5.2, p. 28 | budgeting |
| "With a $1 threshold (teal), full rationality (kit = J = 4) is observed only 10% of the time." | Sect. 5.2, p. 28 | budgeting |
| "Even without allowing for numeracy constraints, just over 80% of consumer-week combinations exhibit some degree of bounded rationality providing strong evidence for the presence of financial-attentiveness frictions." | Sect. 5.2, p. 28 | budgeting |
| "Ex-ante, most consumers (> 75%) are type (i) consumers and thus exhibit aggregate budgeting behavior consistent with what mental accounting theory would predict." | Sect. 5.3.1, p. 32 | budgeting |
| "a plurality of consumers appear to be spend thrifts (iii), who are more likely to increase spending regardless of whether they previously over- or under-spent." | Sect. 5.3.1, p. 32 | savings_debt_management |
| "In the baseline model < 1% of all consumers go bankrupt, while this number jumps to 3.3% when the $1 threshold is imposed." | Sect. 5.4, p. 34 | savings_debt_management |
| "The push notifications, presumably designed to nudge consumers toward financial discipline, could thus have the opposite effect by making the pain of over-expenditure overly salient." | Sect. 5.4, p. 36 | pfm_apps_problems |
| "Our results thus provide evidence that consumers who use sticky budgets as rules of thumb to regulate spending patterns are most vulnerable to adverse outcomes when such budgets can be easily changed." | Sect. 5.4, p. 36 | pfm_apps_problems |
| "Future work should consider using data from financial-planning apps where budgeting and attentiveness, like say through app log-ins, can be explicitly measured in order to validate our latent inferences." | Sect. 6, p. 37 | pfm_apps_importance |

## Remember This

- The model generalises two-stage budgeting with planner/doer timing, mental accounting, sparse-max budget re-evaluation and numeracy thresholds.
- Estimation uses 2,509 low-income pre-paid debit-card users and 71,859 weekly observations from a large North American bank, with CPI price indices.
- Consumers update some but not all budgets each period; baseline average 2.48 updates per week versus 2.11 under the $1 threshold and 0.75 under ε = 0.1.
- Ex-ante most consumers are budget prioritizers (0.826 baseline), but ex-post the plurality are spendthrifts (0.425 baseline; 0.468 under $1).
- Counterfactually forcing weekly budget updates leaves 68.4% (baseline) / 68.2% ($1) no better off and raises simulated bankruptcy from < 1% to 3.3%.
- The paper directly implicates budgeting apps: push notifications that make budgets easy to change may induce over-spending among sticky budgeters.

## Cited Works

- Thaler, R. (1985) (theory) — Mental accounting and consumer choice, the book-keeping mechanism the paper imports into its budgeting model. [pp. 5-6]
- Thaler, R. (1999) (theory) — Mental accounting matters, cited as positing that consumers tag money for specific purposes. [p. 1]
- Deaton, A.; Muellbauer, J. (1980a) (theory) — Classical two-stage budgeting with perfect fungibility, the framework the paper relaxes. [pp. 1, 3, 5, 7]
- Shefrin, H.; Thaler, R. (1981) (theory) — Planner/doer self-control model that motivates the paper's two-selves structure. [pp. 5, 7, 9]
- Gabaix, X. (2014) (theory) — Sparse-max model of bounded rationality, the basis for the paper's sparse budget re-evaluation. [pp. 3, 5, 13]
- Ko˝szegi, B.; Matˇejka, F. (2020) (theory