---
paper_id: A--Sappa-2024
first_author: Sappa
year: 2024
title: "AI Based Portfolio Optimization and Customer Risk Profiling in Fintech Platforms"
venue: "Not reported"
doi: Not reported
designation: algorithm
status: extracted
modules: [model_algorithm_integration, data_collection, model_development, system_development, model_performance_evaluation, system_performance_evaluation]
module_rationale:
  model_algorithm_integration: "Abstract describes a dual-engine system that combines reinforcement learning strategies and classification models for user risk profiling."
  data_collection: "Sect. 3.1 describes anonymized user interaction records from a digital investment platform (approximately 20,000 users over a 36-month transaction period)."
  model_development: "Sect. 3.2 and 3.3 describe training of the DQN reinforcement learning agent, XGBoost classifier, K-Means clustering, and MLP."
  system_development: "Sect. 3.2 describes a modular microservices framework managed by Docker and Kubernetes with REST APIs."
  model_performance_evaluation: "Sect. 5 reports Sharpe ratios, F1 scores, AUC, recall, and precision across models."
  system_performance_evaluation: "Sect. 4 describes an elaborate simulation environment to evaluate the deployed system's performance."
---

# AI Based Portfolio Optimization and Customer Risk Profiling in Fintech Platforms

## Summary

The paper proposes and evaluates an AI-based dual-engine system for portfolio optimization and customer risk profiling in FinTech investment platforms. The system combines reinforcement learning (a DQN variant) for dynamic portfolio allocation with supervised classification (XGBoost, MLP) and unsupervised clustering (K-Means) for risk profiling and behavioral segmentation. Using a simulated dataset of approximately 20,000 FinTech users observed over a 36-month transaction period, the study compares AI-driven optimization against traditional mean-variance optimization, rule-based robo-advisory, randomized allocation, and static XGBoost recommendations. The AI models achieve higher Sharpe ratios, better risk classification accuracy, and greater portfolio diversification across customer segments.

## Problem and Motivation

Traditional risk profiling relies on static onboarding questionnaires that are subjective, prone to overestimation during bull markets and underestimation during downturns, and incapable of adapting to changing investor behavior. Classical optimization methods like mean-variance optimization depend on historical data, normal distribution assumptions, and rigid behavioral assumptions, making them ineffective in volatile, non-linear real-world markets. FinTech platforms need smarter, more adaptable methods that can personalize portfolios in real time based on evolving user behavior and market conditions.

The paper argues that AI enables real-time analysis of asset value changes alongside automated rebalancing using behavioral financial engineering, allowing platforms to make client-specific investment decisions at scale (Sect. 1.1). Unlike non-AI integrated systems that depend on structural models and scheduled evaluations, AI systems work continuously and react to new business transactions, sentiment indicators, and market opportunities (Sect. 1.1).

## Method

**Design.** Computational method-development and comparative simulation study; the authors state no formal design label.
**Sample.** n = approximately 20,000 unique users (FinTech platform user records over a 36-month transaction period); unit of analysis is the individual user/investor.
**Context.** geography: Not reported (dataset from a digital investment platform simulating a FinTech environment); population: FinTech platform users with varied demographics, financial preferences, and risk tolerances; setting: Virtual/computational simulation environment with 20,000 simulated investors, multi-asset-class portfolios, and stochastic market conditions.

- Collect anonymized user interaction records including transaction logs, portfolios, demographics, financial preferences, historical returns, trading activity, and self-assessed risk tolerance (Sect. 3.1).
- Filter for active users who completed at least three rebalancing activities or two investment cycles (Sect. 3.1).
- Impute missing data via KNN for demographic data and forward-fill for time-series gaps; encode categorical features; standardize numeric features with Z-score normalization (Sect. 3.1).
- Design a DQN-variant reinforcement learning agent with a three-layer neural network; state features include portfolio weights, asset returns, volatility scores, and temporal market signals; actions are discrete allocation changes (e.g., +10% equities, −5% bonds); rewards are Sharpe ratio improvements penalized for turnover and risk breaches (Sect. 3.2).
- Train the RL agent in synthetic market environments with over 10,000 starting capital, user-specified goals, and risk profiles (Sect. 3.2).
- Use XGBoost models as starting policy precursors for the RL agent (Sect. 3.2).
- Implement event-driven rebalancing triggered by market shocks, behavior deviations, or asset performance breaches (Sect. 3.2).
- Deploy the system on a modular microservices framework managed by Docker and Kubernetes with REST APIs (Sect. 3.2).
- Apply K-Means clustering with silhouette-based optimization to place users into five risk clusters: Conservative, Moderate, Balanced, Aggressive, and Speculative (Sect. 3.3).
- Train an XGBoost classifier on behavioral and demographic data for supervised risk classification; use SHAP values for feature importance (Sect. 3.3).
- Train a supplementary MLP classifier to capture non-linear dependencies and provide probability distributions for borderline users (Sect. 3.3).
- Validate classification outputs against user activity in simulated volatile scenarios (Sect. 3.3).
- Simulate 20,000 investors over 36 months with daily portfolio updates and monthly or weekly reviews (Sect. 4.1).
- Apply portfolio constraints: max 60% per asset class, min 2 asset classes, min 5% cash/liquid ETFs, 0.3% transaction fee, monthly rebalancing limits, VaR and max drawdown filters (Sect. 4.2).
- Compare against four baselines: MVO, rule-based allocation, randomized allocation with filtering, and XGBoost-based static recommendation (Sect. 4.3).
- Evaluate with stratified analysis by user type, investment goal, and market cycle (Sect. 4.3).
- Record outcomes: returns, volatility, Sharpe ratio, maximum drawdown, transaction fees, turnover, retention rate, override frequency, and average rebalances (Sect. 4.3).

## Software

- Python (version not reported)
- TensorFlow (version not reported)
- PyTorch (version not reported)
- Ray RLlib (version not reported)
- MLflow (version not reported)
- PostgreSQL (version not reported)
- Docker (version not reported)
- Kubernetes (version not reported)
- Pandas, Scikit-learn, TensorFlow Data Pipelines (Sect. 3.1)
- NVIDIA T4 GPUs (for RL training)
- Intel Xeon CPU units (for inference)
- REST APIs (for microservices)

## Key Findings

- The reinforcement learning agent achieved the highest Sharpe ratio of 1.45, compared to 1.28 for XGBoost static, 1.05 for rule-based, and 0.92 for mean-variance optimization (Sect. 5.1, Figure 7).
- The XGBoost risk classifier was reported as the best-performing model with an F1 score of 0.86, AUC of 0.91, recall of 0.89, and precision of 0.84 according to the text (Sect. 5.2).
- Neural networks scored an F1 of 0.84 and AUC of 0.89 according to the text (Sect. 5.2).
- Logistic regression and autoencoders performed more poorly with F1 scores of 0.72 and 0.65, respectively, according to the text (Sect. 5.2).
- AI-based models consistently produced portfolios with lower Herfindahl-Hirschman Index (HHI) values, indicating greater diversification than mean-variance or rule-based optimizers (Sect. 5.3).
- The reinforcement learning agent dynamically shifted allocations to less volatile assets during market declines, resulting in more conservative portfolios while retaining upside potential during recovery (Sect. 5.3).
- Younger investors aged 25-40 leaned toward aggressive portfolios with average returns ranging from 7.5% to 8.1%; older investors above 55 years shifted toward conservative portfolios with returns of 3.8% to 4.4%; balanced portfolios averaged close to 6% across all age groups (Sect. 6.1, Figure 10).
- The system achieved an optimal level of interpretability and adaptiveness by combining parallel XGBoost models as starting policy precursors to the RL agent (Sect. 3.2).
- The five risk clusters identified were Conservative, Moderate, Balanced, Aggressive, and Speculative, with the majority of customers in the Moderate and Balanced categories (Sect. 5.3, Figure 5).
- The classification outputs were validated against user activity in simulated volatile scenarios to ensure predicted risk profiles matched user actions (Sect. 3.3).
- The assessment was stratified by user type, investment goal, and market cycle (bull, bear, recovery, sideways) to evaluate model robustness (Sect. 4.3).
- Performance monitoring capabilities evaluated inference latency, drift, error percentage, and other parameters during execution in real-time (Sect. 4.1).

## Key Figures and Tables

- Figure 1 (p. 2): Distribution of Customer Risk Appetite Across FinTech Users — shows the distribution of risk appetite across the user base.
- Figure 2 (p. 5): Comparison of Mean-Variance vs AI-Based Optimization Returns — visualizes the return advantage of AI-based optimization over MVO.
- Figure 3 (p. 6): Feature Importance in Customer Risk Classification Models — ranks features used in risk classification.
- Figure 4 (p. 8): Convergence of Portfolio Reward Function Over Iterations — shows RL agent training convergence.
- Figure 5 (p. 9): Number of Customers in Each Risk Profile Cluster — distribution of users across five risk clusters.
- Figure 6 (p. 12): Allocation Weights vs Risk Profile Segment — asset allocation by risk profile.
- Figure 7 (p. 14): Sharpe Ratio Trend Across Optimizers — MVO 0.92, rule-based 1.05, XGBoost 1.28, RL 1.45.
- Figure 8 (p. 15): Confusion Matrix Visualization for Risk Classifier — classification outcomes for risk categories.
- Figure 9 (p. 17): Model-Wise Return Percentages Across Portfolios — return percentages by model.
- Figure 10 (p. 19): Risk Profile Score vs Return Curve Across Age Segments — returns by age and risk profile.
- Table 1 (p. 3): Overview of Portfolio Types and Risk Strategies Offered in FinTech Platforms — lists portfolio types (Income, Growth, Balanced, Aggressive Growth, Thematic) with risk levels, target audiences, and key assets.
- Table 2 (p. 7): Summary of Literature on AI in Portfolio Analytics — summarizes five studies with AI techniques and key contributions.
- Table 3 (p. 10): Model Architectures, Features, and Output Descriptions — describes XGBoost, K-Means, RL agent, and MLP models.
- Table 4 (p. 12): Dataset Split, Evaluation Metrics, and Portfolio Return Thresholds — 70/15/15 split; metrics; return thresholds.
- Table 5 (p. 15): Performance Summary Across Metrics (F1 Score, AUC, Recall, Precision) — classification model performance.

## Limitations and Gaps

- The study is a simulation-based evaluation using synthetic and anonymized data; no live FinTech platform, real money, or human participants were involved (Sect. 4.1). [unacknowledged]
- The dataset is described as anonymized user interaction records from "a digital investment platform that simulates a FinTech environment," blurring the line between real and synthetic data; the source and representativeness of the 20,000 users are not specified (Sect. 3.1). [unacknowledged]
- Table 5's reported values are internally inconsistent with the text: the text states XGBoost achieved an F1 score of 0.86 and neural networks an F1 of 0.84, while the table appears to show XGBoost F1 of 0.84 and neural network F1 of 0.65 (Sect. 5.2, Table 5). [unacknowledged]
- No confidence intervals, p-values, or significance tests are reported for any performance comparison (Sect. 5). [unacknowledged]
- The paper does not report standard deviations, per-fold variance, or exact sample sizes for the performance metrics (Sect. 5). [unacknowledged]
- The authors acknowledge that some would propose AI, especially deep learning, is opaque, and explainability remains an issue (Sect. 6.1).
- The authors note that dangers of model drift, non-interpretable decision pathways, and biased training data can greatly affect systems, requiring periodic backtesting, human-in-the-loop validation, and fairness audits (Sect. 6.2).
- The paper does not report the exact number of users in each risk cluster, only that Moderate and Balanced were predominant (Sect. 5.3, Figure 5). [unacknowledged]
- The paper does not report quantitative diversification metrics (HHI values) despite describing HHI as a measure (Sect. 5.3). [unacknowledged]
- The paper does not report the exact performance of the XGBoost-based static portfolio recommendation baseline beyond its Sharpe ratio of 1.28 (Sect. 5.1). [unacknowledged]

## Definitions

- **Dual-engine system** — An AI architecture combining reinforcement learning strategies and classification models for user risk profiling (Abstract).
- **DQN variant** — A deep Q-network reinforcement learning agent with a three-layer neural network used for portfolio optimization (Sect. 3.2).
- **Risk clusters** — Five user segments identified by K-Means clustering: Conservative, Moderate, Balanced, Aggressive, and Speculative (Sect. 3.3).
- **SHAP values** — Shapley additive explanations used to interpret feature importance in the XGBoost risk classifier (Sect. 3.3).
- **Herfindahl-Hirschman Index (HHI)** — A measure of portfolio concentration calculated as the sum of squared asset weights; lower values indicate greater diversification (Sect. 5.3).
- **Event-driven rebalancing** — Portfolio rebalancing triggered by market shocks, deviations in user behavior, or asset performance breaches rather than fixed schedules (Sect. 3.2).
- **Mean-Variance Optimization (MVO)** — Classical portfolio optimization technique that minimizes risk for a target return or maximizes return for a given risk level (Sect. 4.3).
- **Behavioral scores** — Numeric values between 0 and 1 derived from clickstream data or session logs, including responses to risk messages, speed of investment decisions, and dropping high-risk portfolios (Sect. 3.1).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Sharpe ratio, Mean-Variance Optimization | Sharpe ratio | 0.92 | — | — | Sect. 5.1, p. 13 |
| Sharpe ratio, Rule-based model | Sharpe ratio | 1.05 | — | — | Sect. 5.1, p. 13 |
| Sharpe ratio, XGBoost static model | Sharpe ratio | 1.28 | — | — | Sect. 5.1, p. 13 |
| Sharpe ratio, Reinforcement learning agent | Sharpe ratio | 1.45 | — | — | Sect. 5.1, p. 13 |
| F1 Score, XGBoost (text claim) | F1 Score | 0.86 | — | — | Sect. 5.2, p. 15 |
| AUC, XGBoost (text claim) | AUC | 0.91 | — | — | Sect. 5.2, p. 15 |
| Recall, XGBoost (text claim) | Recall | 0.89 | — | — | Sect. 5.2, p. 15 |
| Precision, XGBoost (text claim) | Precision | 0.84 | — | — | Sect. 5.2, p. 15 |
| F1 Score, Neural Network (text claim) | F1 Score | 0.84 | — | — | Sect. 5.2, p. 15 |
| AUC, Neural Network (text claim) | AUC | 0.89 | — | — | Sect. 5.2, p. 15 |
| F1 Score, Logistic Regression (text claim) | F1 Score | 0.72 | — | — | Sect. 5.2, p. 15 |
| F1 Score, Autoencoder (text claim) | F1 Score | 0.65 | — | — | Sect. 5.2, p. 15 |
| F1 Score, Logistic Regression (Table 5) | F1 Score | 0.72 | — | — | Table 5, p. 15 |
| F1 Score, Random Forest (Table 5) | F1 Score | 0.86 | — | — | Table 5, p. 15 |
| F1 Score, XGBoost (Table 5) | F1 Score | 0.84 | — | — | Table 5, p. 15 |
| F1 Score, Neural Network (Table 5) | F1 Score | 0.65 | — | — | Table 5, p. 15 |
| F1 Score, Autoencoder (Table 5) | F1 Score | 0.78 | — | — | Table 5, p. 15 |
| Training data split | Proportion | 70% | — | — | Table 4, p. 12 |
| Validation data split | Proportion | 15% | — | — | Table 4, p. 12 |
| Testing data split | Proportion | 15% | — | — | Table 4, p. 12 |
| Return threshold, acceptable | Annual return | >7% | — | — | Table 4, p. 12 |
| Return threshold, preferred | Annual return | >8% | — | — | Table 4, p. 12 |
| Return threshold, exceptional | Annual return | >10% | — | — | Table 4, p. 12 |
| Aggressive portfolio returns, ages 25-40 | Average return | 7.5% to 8.1% | — | — | Sect. 6.1, p. 18 |
| Conservative portfolio returns, ages 55+ | Average return | 3.8% to 4.4% | — | — | Sect. 6.1, p. 18 |
| Balanced portfolio returns, all age groups | Average return | close to 6% | — | — | Sect. 6.1, p. 18 |
| Sample size | Unique users | approximately 20,000 | — | — | Sect. 3.1, p. 7 |
| Simulation period | Months | 36 | — | — | Sect. 3.1, p. 7 |
| Maximum allocation per asset class | Proportion | 60% | — | — | Sect. 4.2, p. 11 |
| Minimum asset classes per strategy | Count | 2 | — | — | Sect. 4.2, p. 11 |
| Minimum cash/liquid ETF allocation | Proportion | 5% | — | — | Sect. 4.2, p. 11 |
| Transaction fee | Fee | 0.3% | — | — | Sect. 4.2, p. 11 |
| Simulated investors | Count | 20,000 | — | — | Sect. 4.1, p. 10 |
| Starting capital for training episodes | Currency amount | over 10,000 | — | — | Sect. 3.2, p. 8 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "This research proposes an AI-based approach to improve portfolio optimization and customer risk profiling in FinTech investment platforms." | Abstract, p. 1 | model_algorithm_integration |
| "We created and tested a dual-engine system that combines reinforcement learning strategies and classification models for user risk profiling" | Abstract, p. 1 | model_algorithm_integration |
| "The analysis reveals performance enhancements in return-to-risk ratio, accuracy of risk classification, and level of diversification across customer segments." | Abstract, p. 1 | model_performance_evaluation |
| "AI enables this transformation with its ability to provide personalized portfolio recommendations, adaptive risk assessment and real-time tailoring of portfolios using various ML models" | Sect. 1.1, p. 1 | model_algorithm_integration |
| "These fixed profiles are then utilized to pigeonhole the investors into pre-defined portfolios without any further checking or modification." | Sect. 1.2, p. 3 | rule_based_classification |
| "The goal of this research is to create, implement, and assess an AI-based system tailored for two functions: customer risk profiling and portfolio optimization in digital investment platforms." | Sect. 1.3, p. 3 | model_algorithm_integration |
| "The system integrates predictive modeling and optimization algorithms to build portfolios to market standards, while also monitoring user behavior to behaviorally update user profiles and risk levels." | Sect. 1.3, p. 3 | model_algorithm_integration |
| "Unlike classical models, AI models can incorporate market trends, investor activity, and changing correlations with assets." | Sect. 5.1, p. 13 | model_algorithm_integration |
| "The best results were achieved through employing a reinforcement learning agent that was able to devise a policy for allocating assets which optimally adjusted during the investment period and maximally constrained risk exposure." | Sect. 5.1, p. 13 | model_algorithm_integration |
| "AI models not only enhanced returns on risk adjusted based frameworks, but also dynamically responded to customer and market changes in real-time." | Sect. 7, p. 20 | model_algorithm_integration |
| "Strong precision and recall rates of risk classifiers facilitated accurate construction of tailored portfolios, thus improving personalization." | Sect. 7, p. 20 | model_performance_evaluation |
| "With silhouette-based optimization for determining cluster count, K-means was utilized for clustering." | Sect. 3.3, p. 9 | model_development |

## Remember This

- The paper proposes a dual-engine AI system combining RL for portfolio optimization and XGBoost/MLP for risk profiling.
- AI models achieved higher Sharpe ratios (RL: 1.45) than traditional methods (MVO: 0.92).
- The XGBoost risk classifier achieved the best performance with an F1 score of 0.86, AUC of 0.91, recall of 0.89, and precision of 0.84 according to the text.
- The system was evaluated on approximately 20,000 users over 36 months in a simulated FinTech environment.
- AI models dynamically adjusted portfolios in response to market conditions and user behavior.
- The five risk clusters are Conservative, Moderate, Balanced, Aggressive, and Speculative.
- Younger investors aged 25-40 with aggressive portfolios earned 7.5% to 8.1% returns; older investors aged 55+ with conservative portfolios earned 3.8% to 4.4%.
- Table 5's values are inconsistent with the text claims for XGBoost and neural network F1 scores.

## Cited Works

- Sironi, P. (2016) — FinTech innovation: from robo-advisors to goal based investing and gamification. [p. 1]
- Arner, D. W., Barberis, J., Buckley, R. P. (2017) — FinTech and RegTech: impact on regulators and banks. [p. 1]
- Gomber, P., et al. (2018) — On the fintech revolution. [p. 1]
- Treleaven, P., Batrinca, B. (2017) — Algorithmic regulation. [p. 1]
- D'Acunto, F., Prabhala, N., Rossi, A. (2018) — The promises and pitfalls of Robo-advising. [p. 2]
- Statman, M. (2019) — Behavioral finance: The second generation. [p. 2]
- Sharpe, W. F. (1994) — The sharpe ratio. [p. 2]
- Cordell, D. M. (2001) — RiskPACK: How to evaluate risk tolerance. [p. 3]
- Sharpe, W. F. (1964) — Capital asset prices. [p. 4]
- Stoilov, T., Stoilova, K., Vladimirov, M. (2020) — Modified Black-Litterman model. [p. 4]
- Moro, S., Cortez, P., Rita, P. (2014) — Data-driven approach to predict bank telemarketing success. [p. 5]
- Greff, K., et al. (2016) — LSTM: A search space odyssey. [p. 5]
- Mashrur, A., et al. (2020) — Machine learning for financial risk management. [p. 5]
- Liu, X.-Y., et al. (2022) — FinRL-Meta. [p. 6]
- May, K. (2022) — Forecast Based Portfolio Optimisation Using XGBoost. [p. 6]
- Krauss, C., Do, X. A., Huck, N. (2017) — Deep neural networks, gradient-boosted trees, random forests. [p. 6]
- Cerrada, M., et al. (2022) — AutoML for feature selection and model tuning. [p. 7]
- Jiang, M., et al. (2020) — An improved Stacking framework for stock index prediction. [p. 7]