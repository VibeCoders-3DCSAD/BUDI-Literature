---
paper_id: I--Zhao-2025
first_author: Zhao
year: 2025
title: "Wealth-Voyager: Navigating Intelligent Wealth Management with a Multi-Agent Framework"
venue: "Proceedings of the ACM International Conference on AI in Finance (GAIB 2025)"
doi: 10.1145/3766918.3766944

designation: international
status: extracted
modules: [financial_planning, model_algorithm_integration, pfm_apps_problems, pfm_apps_features]
module_rationale:
  financial_planning: "The paper frames wealth management as allocating assets across present and future needs, with retirement planning and SAA/TAA as its core (Abstract; Sect. 4.1)."
  model_algorithm_integration: "Wealth-Voyager integrates four specialised agents and multiple quantitative methods (Monte Carlo, mean-variance, BDI) into a single pipeline (Fig. 1; Sect. 3)."
  pfm_apps_problems: "The paper identifies three limitations of existing advisory systems—lack of behavioral modeling, absent explainability, and static decision logic (Sect. 1; Sect. 2)."
  pfm_apps_features: "Table 3 compares feature sets of Wealth-Voyager against market offerings on real-time adjustment, personalization, and education integration (Table 3, p. 7)."
---

## Summary

Wealth-Voyager is a multi-agent framework for personalised wealth management that combines strategic asset allocation (SAA) with adaptive tactical adjustments. The system orchestrates four specialised agents—AssistHub (behavioural profiling), NewsCrawler (real-time intelligence extraction), AlphaForge (scenario-aware portfolio optimisation), and DualAdvisor (Belief-Desire-Intention grounded role-playing simulation)—under a central LLM-based meta-controller. Its purpose is to address the limitations of traditional advisory models in scalability, cost-efficiency, and objectivity, and the fragmentation of recent AI-driven solutions that focus on isolated tasks. A proof-of-concept case study conducted under live market conditions (April 2 to May 2, 2025) with a single mid-career participant found that the system's adaptive tactical adjustments outperformed a passive baseline, converting a marginal gain into a more substantial return while reducing portfolio volatility. The paper positions Wealth-Voyager as a blueprint for financial co-pilots that integrate quantitative rigour with interactive, cognitively-aware guidance.

## Problem and Motivation

Traditional wealth management frameworks face growing pressure to meet the expectations of a diverse and digitally sophisticated investor base. By 2023, global assets under management had reached USD 1.2 trillion, yet an estimated 320 million potential investors remained underserved by conventional advisory channels. This gap is especially acute in China, where a burgeoning "new middle class" with rising investable assets increasingly seeks technology-enabled financial guidance. The dominance of bank-led fund distribution channels—typically associated with high fees and limited personalisation—further constrains access to tailored services. Beyond structural inefficiencies, behavioural challenges such as speculative trading, early fund redemptions, and limited financial literacy remain widespread, and trust in conventional advisory models is eroded by inadequate transparency and a lack of timely, proactive engagement.

Recent research has focused on LLMs and multi-agent frameworks as promising alternatives, but most implementations exhibit three key limitations. First, the lack of behavioural modeling prevents these systems from accounting for cognitive biases—such as overconfidence or loss aversion—that frequently shape retail investor behaviour. Second, in the absence of interactive explainability, users receive opaque recommendations that undermine trust and reduce engagement. Third, the static nature of their decision logic impedes real-time responsiveness to market events. The paper anchors its framework in asset allocation, which financial literature widely recognises as the cornerstone of long-term portfolio returns, responsible for over 90% of performance variance. This philosophy is implemented through two complementary layers: Strategic Asset Allocation (SAA), which sets the foundational, long-term policy portfolio, and Tactical Asset Allocation (TAA), which enables dynamic, short-term adjustments to that policy.

## Method

**Design.** The paper states no formal design label; it is a proof-of-concept case study with a month-long pilot deployment under live market conditions. The authors describe it as a "proof-of-concept case study" (Abstract) and a "month-long pilot study" (Sect. 4).
**Sample.** n = 1 participant (a 45-year-old mid-career professional planning to retire within eight years); the unit of analysis is the individual investor's portfolio, advisory dialogue, and performance outcomes.
**Context.** geography: China (Shenzhen; Chinese A-shares, RMB-denominated assets, Chinese market conditions); population: a single mid-career professional with RMB 3,000,000 initial capital and a retirement objective; setting: sandbox deployment under live market conditions from April 2 to May 2, 2025, with performance data extending to May 9, 2025, coinciding with a period of elevated geopolitical and financial uncertainty marked by a sharp escalation in global trade tensions (tariff shock on April 2, 2025).

The system architecture consists of four core modules. AssistHub is an intelligent customer service module implemented as an agentic workflow on the Dify platform and powered by ChatGPT-4. Through a guided conversational process of context-aware, adaptive testing and interactive calibration, it dynamically handles general inquiries and assists users in articulating their wealth management goals, detailing their current financial status, and completing a personalised risk assessment. It replaces the "static questionnaire" with a guided multi-round dialogue mechanism to build a comprehensive user profile, which serves as a foundational input required by the other specialised modules.

NewsCrawler operates as a dedicated Model Context Protocol (MCP) server responsible for real-time aggregation and processing of market information from a wide array of online sources. It periodically extracts expected return forecasts for major asset classes from research reports published by professional financial institutions, providing AlphaForge with realistic and timely inputs. It also curates and retrieves daily market news tailored to each user's specific profile, including stated investment interests, risk tolerance, and existing portfolio composition, which serves as foundational context for the role-playing dialogues within DualAdvisor.

AlphaForge is the quantitative core, based on modern portfolio theory. Drawing on market expectations (returns, volatilities, and cross-asset correlations) harvested by NewsCrawler and investor-specific constraints produced by AssistHub, it constructs a long-term strategic asset allocation that balances growth, risk, and liquidity. Internally, it employs a constrained mean-variance engine augmented with liquidity caps, draw-down limits, and leverage controls. The solver outputs target weights alongside forward-looking metrics—projected return, volatility, Value-at-Risk, and liquidity coverage—that feed downstream advisory logic. The mathematical specification and optimisation routine are provided in Appendix A.3, which describes a multi-stage optimisation procedure using equal risk contribution initialisation, a closed-form max-Sharpe solution, sequential least squares quadratic programming (SLSQP), and differential evolution.

DualAdvisor utilises a role-playing framework powered by two distinct LLM agents that simulate consultations between a professional investment advisor and the user. The primary purpose is to generate real-time, tactical investment advice. By dynamically modeling advisor-client interactions in response to market events, DualAdvisor provides actionable recommendations that help users make timely portfolio adjustments. The Advisor Agent acts as the rational anchor, interpreting market developments with professional neutrality and proactively detecting behavioural biases reflected in the user's responses. The User Agent serves as a high-fidelity "digital twin" of the user, designed to inject psychologically plausible, and often biased, human behaviour into the simulation. Its purpose is not to be perfectly rational but to realistically model how a specific individual would react to market changes based on their unique financial circumstances, goals, and behavioural tendencies.

The behavioural profile is grounded in the Belief–Desire–Intention (BDI) framework. The User Agent's internal deliberation is modeled using a step-wise prompting mechanism: the LLM is sequentially queried for its beliefs (subjective understanding of the current market), desires (long-term investment goals and emotional inclinations derived from the user profile), and intentions (actionable steps proposed for portfolio adjustment). This chain-of-thought design improves both the logical consistency and interpretability of the simulated decision process. The profile itself quantifies nine behavioural dimensions: loss aversion, news and policy sensitivity, investment experience, real-time emotion, herding tendency, regret aversion, overconfidence, illusion of control, and decision delay. These are categorised into emotional indicators and cognitive indicators.

The dialogue flow progresses through four phases: Rational Initialization (the Advisor Agent synthesises daily market news through the lens of the user's profile), Behavioural Response (the User Agent generates its initial BDI response), Cognitive Debiasing (the Advisor Agent critiques the response and identifies irrational patterns), and Iterative Consensus (the agents engage in iterative dialogue until a consensus is reached, governed by either a specific agreement phrase or a predefined maximum of ten rounds). The entire interaction culminates in a Daily Investment Briefing, a structured report that summarises the dialogue, providing a market overview, the Advisor Agent's tailored interpretation, concrete portfolio adjustment suggestions, and key areas of focus for the near future.

## Software

- Dify platform (version not reported) — used to implement AssistHub as an agentic workflow.
- ChatGPT-4 (GPT-4) — the underlying LLM powering AssistHub and the DualAdvisor agents.
- Model Context Protocol (MCP) server (version not reported) — used by NewsCrawler for real-time aggregation of market information.
- Monte Carlo simulation (custom implementation) — used for probabilistic outcome estimation and re-sampling loops.
- Constrained mean-variance optimisation engine with liquidity caps, draw-down limits, and leverage controls — implemented in AlphaForge.
- SLSQP (Sequential Least Squares Quadratic Programming) — used for local optimisation.
- Differential Evolution — used for global repair in the multi-stage optimisation procedure.
- Equal Risk Contribution (ERC) initialisation — used to initialise the optimisation.

## Key Findings

- num: The adaptive tactical adjustments outperformed a passive baseline by +1.62 pp during a period of elevated macro uncertainty (Sect. 5, p. 7).
- num: The strategic allocations improved the user's risk-return trade-off by +2.81 pp annualized return and −8.66 pp volatility (Sect. 5, p. 7).
- num: Anchoring alone increased the annual return from 3.72% to 6.53% while nearly halving annualised volatility from 18.08% to 9.42% (Table 2a, p. 7).
- num: The Tactical strategy delivered a cumulative return of 1.86% over the evaluation period, against 0.24% for the Anchored strategy, with annual volatility reduced to 12.10% (Table 2b, p. 7).
- num: Following the tariff-induced shock (Apr 02–Apr 09), the tactical approach reduced losses (−2.56% vs. −2.79%) (Sect. 4.3, p. 6; Fig. 2, p. 7).
- num: In the rebound phase (Apr 09–Apr 23), the tactical approach captured greater upside (3.24% vs. 2.16%) (Sect. 4.3, p. 6; Fig. 2, p. 7).
- num: During Apr 30–May 07, tactical returns remained higher (1.15% vs. 0.68%) (Sect. 4.3, p. 6; Fig. 2, p. 7).
- The AI-optimised allocation reduced the REITs concentration from 20% to 6.0%, increased A-shares from 30% to 35.3%, increased bonds from 35% to 41.1%, and increased gold from 15% to 17.6% (Table 1, p. 6).
- The system inferred latent preferences and applied a structured, investment-bank-style workflow to revise the portfolio, improving diversification and more closely aligning with the user's implicit risk profile (Sect. 4.1, p. 5).
- Qualitative feedback indicated that the dual-agent simulation enhances user trust and self-awareness by exposing cognitive biases in an explainable dialogue (Sect. 5, p. 7).
- Users reported that Wealth-Voyager's ability to explain investment logic in plain language and adapt to their evolving preferences significantly improved their engagement and understanding of portfolio management (Sect. 4.4, p. 6).
- The comparison with mainstream platforms (Ant Fortune, JD Xiaobei, Ping An Butler) reveals that while current platforms fulfil baseline advisory requirements, they remain limited in responsiveness and personalization depth (Sect. 4.4, p. 6).

## Key Figures and Tables

- Fig. 1 (p. 4): The architecture of the proposed Wealth-Voyager framework — illustrates the integration of AssistHub, NewsCrawler, AlphaForge, and DualAdvisor with core tools including an intelligent customer assistant, a news crawler, and portfolio optimisation models.
- Fig. 2 (p. 7): Segment-level returns for passive and tactical portfolios (April 2–May 9, 2025) — shows the tariff-induced shock (Apr 02–Apr 09), rebound phase (Apr 09–Apr 23), subsequent intervals including Apr 30–May 07 (1.15% vs. 0.68%), and mild pullbacks (May 07–May 09).
- Table 1 (p. 6): Comparison between user-declared baseline profile and AI-optimised allocation — shows initial capital RMB 3,000,000, target RMB 4,500,000+, risk tolerance N/A vs Medium (max loss 20%), strategic asset mix A-shares 30%/Bonds 35%/Gold 15%/REITs 20% vs A-shares 35.3%/Bonds 41.1%/Gold 17.6%/REITs 6.0%, expected return N/A vs 6.53%, expected volatility N/A vs 9.42%.
- Table 2 (p. 7): Performance comparison across user-declared, anchored, and tactical portfolio strategies — (a) Original vs. Anchored: annual return 3.72% vs 6.53%, annual volatility 18.08% vs 9.42%; (b) Anchored vs. Tactical: cumulative return 0.24% vs 1.86%, annual volatility 13.70% vs 12.10%.
- Table 3 (p. 7): Capability comparison between Wealth-Voyager and representative market offerings — Wealth-Voyager supports all five features (diverse asset-class support, interactive interface, real-time dynamic adjustment, personalized customization, financial education integration), while Ant Fortune, JD Xiaobei, and Ping An Butler support only the first two and lack the latter three.
- Table 4 (p. 9): Default Personality Mapping M — maps investment purpose (retirement, child_education, house_purchase, wealth_growth) to nine-dimensional behavioural vectors.

## Limitations and Gaps

- The authors acknowledge that the prototype was evaluated on a single user and a limited asset universe, and that its performance is contingent on the underlying LLM (Sect. 5, p. 7).
- The authors acknowledge that future work will prioritise a multi-faceted evaluation, including larger, longitudinal studies with a diverse cohort of users to statistically validate the system's adaptability across different behavioural profiles (Sect. 5, p. 7).
- The authors acknowledge the need to expand the asset universe and test the framework under varied market regimes to assess its resilience (Sect. 5, p. 7).
- The authors acknowledge the need for systematic benchmarking against state-of-the-art systems to highlight the advantages of the behaviour-aware approach (Sect. 5, p. 7).
- The authors acknowledge that further work is needed to explore reinforcement learning to refine the negotiation dynamics within DualAdvisor and to investigate domain-specific models to improve performance and reduce inference costs (Sect. 5, p. 7).
- [unacknowledged] The study reports no significance tests, confidence intervals, or variance estimates for any of the performance comparisons in Table 2 or Figure 2; all comparisons rest on a single participant's portfolio over a one-month period.
- [unacknowledged] The comparison with market solutions (Table 3) is based on a six-week co-development deployment with "a group of novice and intermediate investors" whose number is not reported; the feedback informing the design differentiators is not quantified.
- [unacknowledged] The expected return (6.53%) and volatility (9.42%) in Table 1 are forward-looking projections from AlphaForge, not realised outcomes, yet they are presented alongside realised returns in Table 2 without distinguishing projection from realisation.
- [unacknowledged] The paper provides no ablation study to isolate which module (AssistHub, NewsCrawler, AlphaForge, or DualAdvisor) contributes to the reported performance gains, so the incremental value of each component remains unestablished.
- [unacknowledged] The baseline "Original" portfolio in Table 2a uses user-declared weights while the "Anchored" and "Tactical" portfolios use AI-optimised weights, so the comparison confounds behavioural anchoring with quantitative optimisation.
- [unacknowledged] The paper reports that "the system was fully deployed in a sandbox environment" (Sect. 4), which may not reflect live production constraints such as latency, data availability, or execution frictions.
- [unacknowledged] The paper does not report the number of dialogue rounds actually taken to reach consensus in the DualAdvisor simulation, nor the frequency of reaching the predefined maximum of ten rounds.
- [unacknowledged] The performance comparison period (April 2 to May 9, 2025) is short and coincides with a single, specific market event (the tariff shock and subsequent recovery), so the results may not generalise to other market regimes.

## Definitions

- **Wealth-Voyager** — A behaviour-aware, multi-agent financial advisory framework coordinated by a central LLM-based meta-controller.
- **SAA (Strategic Asset Allocation)** — The foundational, long-term policy portfolio that sets the strategic asset mix.
- **TAA (Tactical Asset Allocation)** — Dynamic, short-term adjustments to the SAA policy in response to real-time market events.
- **AssistHub** — An intelligent customer service module implemented on the Dify platform and powered by ChatGPT-4, used for behavioural profiling through guided multi-round dialogue.
- **NewsCrawler** — A dedicated Model Context Protocol (MCP) server responsible for real-time aggregation and processing of market information from online sources.
- **AlphaForge** — The quantitative core of Wealth-Voyager, a constrained mean-variance engine augmented with liquidity caps, draw-down limits, and leverage controls.
- **DualAdvisor** — A role-playing module powered by two LLM agents that simulate consultations between a professional investment advisor and the user, grounded in a Belief-Desire-Intention framework.
- **BDI (Belief-Desire-Intention)** — A framework for rational agency that sequentially models the agent's beliefs (subjective understanding of the current market), desires (long-term investment goals and emotional inclinations), and intentions (actionable steps proposed for portfolio adjustment).
- **A-shares** — RMB-denominated equities on mainland Chinese exchanges.
- **REITs** — Real-estate investment trusts.
- **CVaR (Conditional Value at Risk)** — A risk measure used in portfolio optimisation.
- **Monte Carlo simulation (MCS)** — A probabilistic method for estimating outcomes through repeated random sampling.
- **Daily Investment Briefing** — The final user-facing deliverable that summarises the dialogue, providing a market overview, the Advisor Agent's tailored interpretation, concrete portfolio adjustment suggestions, and key areas of focus.

## Key Equations

- `L(w) = −Sharpe(w) + λ IlliqPenalty(w)` — The objective function for the multi-stage optimisation procedure in AlphaForge, combining negative Sharpe ratio with an illiquidity penalty (Appendix A.3, Algorithm 3).
- The optimisation procedure uses: `w(0) ← ERC_Init(Σ)` (equal risk contribution initialisation), `w_MS ← closed-form max-Sharpe solution`, `w★ ← SLSQP(L, w(0), b_i, constraints)` (local optimisation), and `w⋄ ← DifferentialEvolution(L, b_i, constraints)` (global repair) (Appendix A.3, Algorithm 3).
- The Monte-Carlo-driven meta-agent loop: `c ← c0; best_c ← c0; best_p ← 0`; for `r ← 1 to R`: `p ← MonteCarloSim(c)`; if `p > best_p` then `best_c ← c; best_p ← p`; if `p ≥ τ` then break; `c ← LLM_Adjust(c, allowed_params)` (Appendix A.1, Algorithm 1).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Initial capital, user-declared | amount | RMB 3,000,000 | — | — | Table 1, p. 6 |
| Initial capital, AI-optimised | amount | RMB 3,000,000 | — | — | Table 1, p. 6 |
| Target amount, user-declared | target | RMB 4,500,000+ | — | — | Table 1, p. 6 |
| Target amount, AI-optimised | target | RMB 4,500,000+ | — | — | Table 1, p. 6 |
| Expected return, AI-optimised | expected return | 6.53% | — | — | Table 1, p. 6 |
| Expected volatility, AI-optimised | expected volatility | 9.42% | — | — | Table 1, p. 6 |
| Strategic asset mix, user-declared | allocation | A-shares 30%, Bonds 35%, Gold 15%, REITs 20% | — | — | Table 1, p. 6 |
| Strategic asset mix, AI-optimised | allocation | A-shares 35.3%, Bonds 41.1%, Gold 17.6%, REITs 6.0% | — | — | Table 1, p. 6 |
| Risk tolerance, AI-optimised | risk tolerance | Medium (max loss 20%) | — | — | Table 1, p. 6 |
| Tariff shock segment return (Apr 02–Apr 09), tactical | segment return | -2.56% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Tariff shock segment return (Apr 02–Apr 09), passive | segment return | -2.79% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Rebound phase segment return (Apr 09–Apr 23), tactical | segment return | 3.24% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Rebound phase segment return (Apr 09–Apr 23), passive | segment return | 2.16% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Apr 30–May 07 segment return, tactical | segment return | 1.15% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Apr 30–May 07 segment return, passive | segment return | 0.68% | — | — | Sect. 4.3, p. 6; Fig. 2, p. 7 |
| Annual return, Original portfolio | annual return | 3.72% | — | — | Table 2a, p. 7 |
| Annual volatility, Original portfolio | annual volatility | 18.08% | — | — | Table 2a, p. 7 |
| Annual return, Anchored portfolio | annual return | 6.53% | — | — | Table 2a, p. 7 |
| Annual volatility, Anchored portfolio | annual volatility | 9.42% | — | — | Table 2a, p. 7 |
| Cumulative return, Anchored portfolio | cumulative return | 0.24% | — | — | Table 2b, p. 7 |
| Annual volatility, Anchored portfolio (2b) | annual volatility | 13.70% | — | — | Table 2b, p. 7 |
| Cumulative return, Tactical portfolio | cumulative return | 1.86% | — | — | Table 2b, p. 7 |
| Annual volatility, Tactical portfolio | annual volatility | 12.10% | — | — | Table 2b, p. 7 |
| Adaptive advice improvement over passive baseline | percentage point improvement | +1.62 pp | — | — | Sect. 5, p. 7 |
| Annualized return improvement, strategic allocations | annualized return improvement | +2.81 pp | — | — | Sect. 5, p. 7 |
| Volatility reduction, strategic allocations | volatility reduction | −8.66 pp | — | — | Sect. 5, p. 7 |
| Real-time dynamic adjustment, Wealth-Voyager | capability | ✓ | — | — | Table 3, p. 7 |
| Real-time dynamic adjustment, Ant Fortune | capability | ✗ | — | — | Table 3, p. 7 |
| Real-time dynamic adjustment, JD Xiaobei | capability | ✗ | — | — | Table 3, p. 7 |
| Real-time dynamic adjustment, Ping An Butler | capability | ✗ | — | — | Table 3, p. 7 |
| Personalized customization, Wealth-Voyager | capability | ✓ | — | — | Table 3, p. 7 |
| Personalized customization, Ant Fortune | capability | ✗ | — | — | Table 3, p. 7 |
| Personalized customization, JD Xiaobei | capability | ✗ | — | — | Table 3, p. 7 |
| Personalized customization, Ping An Butler | capability | ✗ | — | — | Table 3, p. 7 |
| Financial education integration, Wealth-Voyager | capability | ✓ | — | — | Table 3, p. 7 |
| Financial education integration, Ant Fortune | capability | ✗ | — | — | Table 3, p. 7 |
| Financial education integration, JD Xiaobei | capability | ✗ | — | — | Table 3, p. 7 |
| Financial education integration, Ping An Butler | capability | ✗ | — | — | Table 3, p. 7 |
| Diverse asset-class support, all four platforms | capability | ✓ | — | — | Table 3, p. 7 |
| Interactive interface, all four platforms | capability | ✓ | — | — | Table 3, p. 7 |
| Real-world deployment period | weeks | 6 | — | — | Sect. 4.4, p. 6 |
| Pilot study period | date range | April 2 to May 2, 2025 | — | — | Sect. 4, p. 5 |
| Performance evaluation period | date range | April 2 to May 9, 2025 | — | — | Sect. 4.3, p. 6 |
| Participant age | years | 45 | — | — | Sect. 4.1, p. 5 |
| Participant retirement horizon | years | 8 | — | — | Sect. 4.1, p. 5 |
| Initial REITs concentration | allocation | 20% | — | — | Sect. 4.1, p. 5 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Rising demand for hyper-personalized wealth management is increasingly unmet by traditional advisory models, which suffer from limitations in scalability, cost-efficiency, and objectivity." | Abstract, p. 1 | pfm_apps_problems |
| "we introduce Wealth-Voyager, a multi-agent framework that synergizes strategic asset allocation with adaptive tactical adjustments." | Abstract, p. 1 | model_algorithm_integration |
| "The system's adaptive tactical adjustments outperformed a passive baseline, converting a marginal gain into a more substantial return while reducing portfolio volatility." | Abstract, p. 1 | financial_planning |
| "the lack of behavioral modeling prevents these systems from accounting for cognitive biases—such as overconfidence or loss aversion—that frequently shape retail investor behavior." | Sect. 1, p. 2 | pfm_apps_problems |
| "We anchor our framework in asset allocation, which financial literature widely recognizes as the cornerstone of long-term portfolio returns, responsible for over 90% of performance variance" | Sect. 1, p. 2 | financial_planning |
| "DualAdvisor, a novel Belief-Desire-Intention (BDI) grounded role-playing simulation that interactively manages user-specific behavioral biases in response to real-time events." | Abstract, p. 1 | model_algorithm_integration |
| "AssistHub replaces the 'static questionnaire' with a guided multi-round dialogue mechanism to comprehensive user profile." | Sect. 3.2, p. 3 | financial_planning |
| "the recorded conversation acts as a 'behavioral mirror' for investor education, enabling users to observe how professional reasoning can mitigate their own cognitive distortions" | Sect. 3.3.1, p. 4 | pfm_apps_features |
| "Our validation, while promising, has several limitations: the prototype was evaluated on a single user and a limited asset universe, and its performance is contingent on the underlying LLM." | Sect. 5, p. 7 | pfm_apps_problems |
| "Users reported that Wealth-Voyager's ability to explain investment logic in plain language and adapt to their evolving preferences significantly improved their engagement and understanding of portfolio management." | Sect. 4.4, p. 6 | pfm_apps_features |
| "Recent industry analyses highlight the growing adoption of AI-driven wealth-management systems in China, notably: Ant Group's Ant Fortune, JD Digits' JD Xiaobei, and Ping An's Intelligent Wealth Butler." | Sect. 4.4, p. 6 | pfm_apps_problems |
| "By 2023, global assets under management (AUM) had reached USD 1.2 trillion, yet an estimated 320 million potential investors remained underserved by conventional advisory channels." | Sect. 1, p. 1 | financial_planning |
| "The structured yet flexible nature of the SAA-TAA framework makes it an ideal domain for an advisory system that must also address the critical gaps in behavioral modeling and real-time adaptiveness." | Sect. 1, p. 2 | model_algorithm_integration |
| "This dual-agent design fulfills two complementary objectives. Firstly, it generates personalized, bias-aware investment guidance by anticipatorily modeling the user's likely emotional reactions." | Sect. 3.3.1, p. 4 | pfm_apps_features |
| "Users reported that Wealth-Voyager's ability to explain investment logic in plain language and adapt to their evolving preferences significantly improved their engagement and understanding of portfolio management." | Sect. 4.4, p. 6 | pfm_apps_features |

## Remember This

- Wealth-Voyager is a multi-agent framework combining SAA with TAA, orchestrated by four specialised agents under an LLM meta-controller.
- The proof-of-concept case study (n = 1) ran April 2 to May 2, 2025, under live market conditions coinciding with a tariff shock.
- Adaptive tactical adjustments outperformed a passive baseline by +1.62 pp; strategic allocations improved annualized return by +2.81 pp and reduced volatility by −8.66 pp.
- Anchoring alone raised annual return from 3.72% to 6.53% and cut volatility from 18.08% to 9.42%; Tactical added cumulative return of 1.86% vs 0.24% for Anchored.
- The AI-optimised allocation reduced REITs from 20% to 6.0% and increased A-shares from 30% to 35.3%, bonds from 35% to 41.1%, and gold from 15% to 17.6%.
- DualAdvisor uses a BDI-grounded role-playing simulation with an Advisor Agent and a User Agent (digital twin) to surface and debias cognitive biases.
- The paper acknowledges the single-user, single-period, single-asset-universe limitation and calls for larger longitudinal studies.
- Table 3 shows Wealth-Voyager uniquely supports real-time dynamic adjustment, personalized customization, and financial education integration among compared platforms.

## Cited Works

- Achiam, J. et al. (2023) — GPT-4 technical report. arXiv:2303.08774. [p. 3]
- Ant Group (n.d.) — Ant Fortune. https://www.antfortune.com/. [p. 6]
- Barnwal, K. (2023) — User Friendly Portfolio Optimisation Using Monte Carlo Simulation. Medium. [p. 3]
- Bodie, Z. (1995) — Investments. Book. [p. 2]
- Brinson, G. P., Hood, L. R., and Beebower, G. L. (1986) — Determinants of Portfolio Performance. Financial Analysts Journal 42(4), 39–44. [p. 2]
- Chandra, A., Kumar, A., and Bala, S. (2025) — Cognitive Biases and Robo-Advisory Adoption: Experimental Evidence. Journal of Behavioral and Experimental Finance 37, 100742. [p. 3]
- Dong, X., Stratopoulos, T., and Wang, C. (2024) — Large Language Models for Financial and Investment Management. The Journal of Portfolio Management 51(2), 211–230. [p. 2]
- Eichler, K. S. and Schwab, E. (2024) — Evaluating Robo-Advisors through Behavioral Finance. Frontiers in Behavioral Economics 3, 1489159. [p. 3]
- Financial Edge Training (2024) — Portfolio Optimisation Explained: Mean–Variance, CVaR and Beyond. [p. 3]
- Guo, T. et al. (2025) — MASS: Multi-Agent Simulation Scaling for Portfolio Construction. arXiv:2505.10278. [p. 2]
- Huang, Z. and Tanaka, F. (2022) — MSPM: A modularized and scalable multi-agent reinforcement learning-based system for financial portfolio management. Plos one 17(2), e0263689. [p. 2]
- Ibbotson, R. G. and Kaplan, P. D. (2000) — Does Asset Allocation Policy Explain 40, 90, or 100 Percent of Performance? Financial Analysts Journal 56(1), 26–33. [p. 2]
- CFA Institute (2022) — Enhancing Investors' Trust: 2022 CFA Institute Investor Trust Study. [p. 1]
- International Monetary Institute (2024) — China Wealth Management Competency Evaluation Report (2023). [p. 1]
- JD Digits (n.d.) — JD Xiaobei. https://jr.jd.com/. [p. 6]
- Lakkaraju, K. et al. (2023) — Can LLMs Be Good Financial Advisors? An Initial Study in Personal Finance Decision Making. Proc. ICAPS FinPlan Workshop. [p. 2]
- Leatherwood, A. and Matta, V. (2025) — Building AI Applications with Dify.ai: A Hands-On Workshop. [p. 3]
- Lee, J. et al. (2020) — MAPS: Multi-agent reinforcement learning-based portfolio management system. arXiv:2007.05402. [p. 2]
- Li, G. et al. (2023) — Camel: Communicative agents for "mind" exploration of large language model society. Advances in Neural Information Processing Systems 36, 51991–52008. [p. 4]
- Li, Z., Tam, V., and Yeung, K. L. (2024) — Developing a multi-agent and self-adaptive framework with deep reinforcement learning for dynamic portfolio risk management. arXiv:2402.00515. [p. 2]
- Liu, X.-Y. et al. (2023) — FinGPT: Democratizing Internet-Scale Data for Financial Large Language Models. arXiv:2307.10485. [p. 2]
- Model Context Protocol Initiative (2024) — Introduction to the Model Context Protocol. [p. 3]
- Ping An Group (n.d.) — Intelligent Wealth Butler. https://group.pingan.com/. [p. 6]
- Pompian, M. (2016) — Risk profiling through a behavioral finance lens. CFA Institute Research Foundation. [p. 4]
- Statista Research Department (2023) — Global wealth-management market size, 2019–2023. [p. 1]
- Takayanagi, T. et al. (2025) — Are Generative AI Agents Effective Personalized Financial Advisors? Proc. SIGIR 2025. arXiv:2504.05862. [p. 3]
- Wu, S. et al. (2023) — BloombergGPT: A Large Language Model for Finance. arXiv:2303.17564. [p. 2]
- Xiao, Y. et al. (2024) — TradingAgents: Multi-Agents LLM Financial Trading Framework. arXiv:2412.20138. [p. 2]
- Yu, Y. et al. (2024) — Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making. Advances in Neural Information Processing Systems 37, 137010–137045. [p. 2]