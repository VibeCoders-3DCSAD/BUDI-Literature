---
paper_id: A--Hamdare-2025
first_author: Hamdare
year: 2025
title: "Analyzing and Rewarding Credit Card Spending Habits in India: A Machine Learning Approach"
venue: "International Journal of Computational Intelligence Systems, 18, 165"
doi: Not reported
designation: algorithm
status: extracted
modules: [data_collection, income_expense_management, model_development, model_algorithm_integration, model_performance_evaluation]
module_rationale:
  data_collection: "Sect. 3.1–3.2 describe the public Kaggle 'Analyzing Credit Card Spending Habits in India' dataset and the Faker-generated synthetic replacement assembled from GitHub repositories and LLM-suggested attributes (pp. 5–8)."
  income_expense_management: "Expenses are classified into luxury, travel, groceries, EMIs payments and others, and reward points are keyed to expense type (Abstract, p. 1; Table 3, p. 8; Table 6, p. 12)."
  model_development: "K-Means with K=4 over monthly spend, transactions per month, credit utilisation and transaction year/month, after one-hot encoding and correlation-matrix feature selection (Sect. 3.3–3.4, pp. 10–11)."
  model_algorithm_integration: "Fig. 1 chains data exploration, K-Means segmentation and the six-factor reward formula, and the formula is then validated by Linear Regression, XGBoost and Random Forest (Fig. 1, p. 6; Sect. 3.6, p. 12; Sect. 4.4, p. 18)."
  model_performance_evaluation: "Silhouette score and Davies-Bouldin Index for the clustering models and R2, RMSE and MAE for Linear Regression, XGBoost and Random Forest (Sect. 4.1, p. 15; Sect. 4.4, p. 18)."
---

# A--Hamdare-2025 — Analyzing and Rewarding Credit Card Spending Habits in India

## Summary

The paper studies credit-card spending behaviour among Indian cardholders and proposes a personalised reward-point formula in place of the flat, card-type-only reward rule it says issuers currently use. It first examines a public Kaggle dataset ("Analyzing Credit Card Spending Habits in India"), finds it unusable for user-level and temporal analysis because it lacks user identifiers and carries only 2014–2015 dates, and then generates a synthetic replacement with the Python Faker library. On the synthetic data it applies K-Means clustering with K = 4 to segment cardholders into the four card types (Platinum, Gold, Silver, Signature) using monthly spend, transactions per month, credit utilisation and transaction year/month, and compares K-Means against DBSCAN, Hierarchical clustering and Gaussian Mixture Models on silhouette score and the Davies-Bouldin Index. It then defines a six-factor reward-point formula — card-type multiplier (RCT), card promotion date bonus (CPD), expense-type bonus (ET), income-category bonus (IC), number-of-cards penalty (NoC) and attrition-risk bonus (AR) — and validates it by training Linear Regression, XGBoost and Random Forest to predict reward points. The headline result is an R2 of 0.99 for Random Forest and XGBoost, with Random Forest reported as having the lowest RMSE and MAE, and K-Means reported at a silhouette score of 0.42. The paper is written for credit-card issuers and frames its contribution as a data-driven reward-allocation framework for the Indian market; it is not about personal financial management software, household budgeting, or forecasting of consumer expenditure.

## Problem and Motivation

The paper's stated problem is commercial rather than household-financial: credit-card companies in India cannot differentiate their offerings in a competitive market and fail to retain high-value customers because reward programmes are generic. It argues that "the core problem faced by credit card companies in India is differentiating their offerings in a competitive market to retain high-value customers" (Sect. 1, p. 2), and that "current reward programs often fail to incentivize spending among affluent and frequent spenders due to their generic structures, which fail to distinguish between nominal and high-value spenders" (Sect. 1, p. 2).

Three sub-problems are developed in Sect. 2.1. First, lack of personalisation: "currently available rewards systems provide fixed incentives irrespective of individual spending habits, leading to a disconnect between consumer preferences and program benefits" (p. 3). Second, static tiering: tiered structures "are typically static and do not align with individual spending behaviors" (p. 3). Third, rigidity and absent real-time response: "Traditional reward programs also rely on rigid, rule-based systems that do not leverage real-time data to adjust rewards based on evolving consumer behavior" (p. 3).

A seasonal motivation also appears: spending spikes at Diwali, Christmas and New Year, and "during these times, many consumers actively seek cards that offer better benefits for large purchases" (p. 2). The paper later claims support for this from its synthetic monthly trend plot (Sect. 3.2, p. 9). Note that the seasonal argument is an incentive-timing argument, not a forecasting argument: the paper never forecasts a seasonal series.

The paper sets four objectives (Sect. 1, p. 2): segment spending behaviour with K-Means; optimise reward programmes toward luxury and travel; prevent overfitting using synthetic data and regularisation; and improve accuracy with engineered features such as reward points per transaction and spending frequency.

## Method

**Design.** Computational data-analysis and model-development study with a comparative model evaluation; the authors state no formal design label.
**Sample.** Not reported (the paper prints no count of transactions, customers or rows for either the original Kaggle dataset or the synthetic dataset; the unit of analysis is the credit-card transaction, aggregated to the cardholder-month).
**Context.** geography: India (cardholders and market, Sect. 1, p. 1); population: Indian credit-card holders across four card types — Platinum, Gold, Silver and Signature (Sect. 3.4, p. 10); setting: offline computational analysis of a public Kaggle dataset plus a Faker-generated synthetic dataset in Python; no live issuer system, no human participants and no field deployment.

- Obtain the original dataset "Analyzing Credit Card Spending Habits in India" from Kaggle and describe its seven columns: Index, City, Date, Card Type, Exp Type, Gender, Amount (Table 2, p. 6).
- Diagnose the original dataset's defects: the Index field lacks user-specific identifiers, the Date field "contains many missing or outdated values, especially from 2014 to 2015", and monthly amounts lack contextual detail (Sect. 3.1, p. 7).
- Generate a synthetic dataset with the Python Faker library, "defining column names, ranges, and relationships between values", and deliberately correlate attributes such as credit score and attrition risk (Sect. 3.2, pp. 7–8).
- Source candidate attributes by exploring "multiple GitHub repositories and datasets related to credit card transactions", then compile a list, feed it to an LLM to suggest "the most potent ones for our project", and keep those with the highest positive correlation in a correlation matrix (Sect. 3.2, p. 8).
- Expand the schema to sixteen synthetic columns including User ID, Card Promotion Date, Expense Type, Income Category, Number of Cards, Number of Loans, Customer Age, Months Spent with Bank, Risk of Attrition, # Transactions per month, Month of Transaction and Monthly Spending (Table 3, p. 8).
- Clean and transform: convert the Date string field to datetime so that month, year and day can be extracted, and one-hot encode Gender, Card Type and Expense Type (Sect. 3.3, p. 10).
- Cluster with K-Means, plus DBSCAN and GMM for comparison, using monthly spend, transactions per month, credit utilisation/expense category, and year and month of transaction as features; set K = 4 "based on the different card types" (Sect. 3.4, pp. 10–11).
- Evaluate clustering with silhouette score and the Davies-Bouldin Index; state that a silhouette near + 1 is better and that DBI should be below 1 (Sect. 3.4, p. 10).
- Interpret the four resulting clusters as Platinum (high spending, frequent usage, luxury and travel), Gold (moderate, mixed), Silver (lower spending on essentials, lower income) and Signature (routine expenses, minimal variability) (Sect. 3.5, p. 11).
- Define the original-dataset reward formula as Amount Spent Monthly × Points Scored (Based on Card Type) / 500, with base rates Platinum 5, Signature 4, Gold 3, Silver 2 (Table 4, p. 11; Sect. 3.6.1, p. 12).
- Define the synthetic-dataset reward formula as Scored Points × Amount Spent / 500, where Scored Points = [RCT + CPD + ET + IC + NoC + AR] (Sect. 3.6.2, p. 12).
- Parameterise the six factors: RCT from Table 5; CPD unspecified as a value except in the case study (+ 2); ET from Table 6; IC + 1 for high income and 0.5 for middle income; NoC "for every additional card beyond the first, a multiplier of -0.5"; AR + 1.0 for higher attrition risk (Sect. 3.6.2, pp. 12–13).
- Work a single hand-computed case study, Cardholder XYZ, through both formulas to compare outputs (Sect. 4.3, pp. 16–17).
- Train Linear Regression, XGBoost and Random Forest on the synthetic dataset to predict reward points, select the best performer, and report R2 alongside RMSE and MAE (Sect. 4.4, p. 18).
- Present figures for clustering performance, cluster separation, reward-point distribution and cumulative reward-point distribution, and a reward-point comparison (Figs. 4–8, pp. 10–17).

No train/test split, no cross-validation, no random seed, no hyperparameter table and no confidence or significance procedure is reported anywhere in the paper.

## Software

- Python (version not reported)
- Faker library (version not reported) — used for synthetic data generation
- K-Means clustering (implementation and version not reported)
- DBSCAN, Hierarchical clustering and Gaussian Mixture Models (implementations and versions not reported) — used as clustering comparators
- Linear Regression (implementation and version not reported)
- XGBoost (version not reported)
- Random Forest (version not reported)
- LLM used for attribute suggestion (model and version not reported)
- Correlation matrix computation for feature selection (library not reported)

## Key Findings

- The abstract states that "the proposed ML model achieved an R2 value of 0.99, demonstrating superior accuracy in optimizing reward point distribution" (Abstract, p. 1).
- Sect. 4.4 reports an R2 of 0.99 "for both the Random Forest and XGBoost models, indicating an almost perfect fit to their respective datasets" (p. 18).
- Random Forest is selected on error metrics, not on R2: "when comparing the models based on performance metrics such as RMSE and MAE, the Random Forest model clearly outperforms both Linear Regression and XGBoost" (Sect. 4.4, p. 18). The RMSE and MAE values themselves are never printed.
- K-Means is reported at a silhouette score of 0.42, "outperforming other clustering techniques (DBSCAN, Hierarchical, GMM)" (Sect. 4.1, p. 15). The corresponding silhouette and DBI values for DBSCAN, Hierarchical and GMM are not printed.
- Cluster separation is described qualitatively: "Visualization in 3D clearly segregates the 4 clusters made based on card type held by customers. Clear separation of Card Types within clusters proves its natural segmentation power" (Sect. 4.1, p. 15).
- Reward points on the five-feature dataset "are restricted to a maximum value of 1000 in synthetic dataset due to the absence of detailed information", while with the additional features "the reward point distribution extends over a broader and more justified range, ranging from 0 to 3500" (Sect. 4.2, p. 16).
- Mean reward points in the synthetic dataset are reported as "approximately 1000" (Sect. 4.4, p. 18).
- The Cardholder XYZ case study produces 400 points under the original formula and 650 points under the synthetic formula for the same 50,000 spend, with Scored Points = [1.5 + 2 + 3 + 1 + −1 + 0] = 6.5 (Sect. 4.3, pp. 16–17).
- The paper claims the synthetic approach yields "Personalization", "Flexibility", "Behavioral Incentives", "Attrition Risk Mitigation" and "Higher Granularity" over the original formula (Sect. 4.3, p. 17).
- The paper states the synthetic dataset "maintains strong predictive performance due to its thoughtful and systematic design" and that it "is inherently superior, as its theoretical framework translates into durable predictive capabilities" (Sect. 4.3, p. 16).
- Market context given: "As of 2024, over 83 million active credit cards are in circulation" in India (Sect. 1, p. 1).
- The conclusion states that "Due to the unavailability of real credit card transaction data and reward point calculation methods, synthetic datasets have been used, and a formula has been developed accordingly" (Sect. 5, p. 18).

## Key Figures and Tables

- Fig. 1 (p. 6): Methodology for calculation of credit score — the step chain from data gathering to reward calculation, with no numeric content.
- Fig. 2 (p. 7): Exploratory data analysis of the original dataset — (a) distribution of transaction amounts, (b) distribution of gender ("female are using card more than male spenders", p. 6), (c) distribution of card type, (d) distribution of expense type.
- Fig. 3 (p. 9): Exploratory data analysis of the synthetic dataset — (a) box plot of spending amount with card type, (b) monthly spending trends across 15 months showing festive-season increases.
- Fig. 4 (p. 10): Performance scores of clustering models — silhouette and DB index for K-Means and DBSCAN, described as "appreciable" but not numerically printed in the text.
- Fig. 5 (p. 14): Cluster-based analysis based on card type — described in the text as a 2D visualization of the K-Means clusters, then described as a 3D visualization segregating four clusters.
- Fig. 6 (p. 14): Distribution of reward points — original vs synthetic, showing the original capped at 1000 and the synthetic extending to 3500.
- Fig. 7 (p. 15): Cumulative distribution of reward points — "underlines the distribution of reward points categorized by spending type" (p. 16).
- Fig. 8 (p. 17): Comparison of reward points — comparative reward points across customers on the synthetic dataset, with mean reward points rising to approximately 1000.
- Table 1 (p. 4): Comparison of previous research, identified gaps and contributions — column headers are rendered as mirror text in the conversion, but the rows name Cheema and Van der Stede [11], Li, Ngai and Hu [12, 13], Gan, Xu & Chen [14], Sadat Akash's "Credit Card Transaction Dataset" [15], Sun and Vasarhelyi [16], Sayjadah et al. [17] and Teng and Lee [18].
- Table 2 (p. 6): Description of attributes in the original dataset — Index, City, Date, Card Type, Exp Type, Gender, Amount.
- Table 3 (p. 8): Description of attributes in the synthetic dataset — sixteen columns from User ID to Monthly Spending (on average).
- Table 4 (p. 11): Base reward points — Platinum 5, Signature 4, Gold 3, Silver 2.
- Table 5 (p. 12): Base multiplier for card types (RCT) — Platinum 2.0, Signature 1.5, Gold 1.0, Silver 0.5.
- Table 6 (p. 12): Expense type bonus (ET) — Travel/Dining + 3.0, Luxury + 2.0, Entertainment + 1.0, Groceries/Bills 0.5, Other Expenses 0.0.

## Limitations and Gaps

- The authors acknowledge that no real transaction data were available: "Due to the unavailability of real credit card transaction data and reward point calculation methods, synthetic datasets have been used, and a formula has been developed accordingly" (Sect. 5, p. 18).
- The authors acknowledge that the reward multipliers are invented: "Since banks and credit card companies do not publicly disclose their actual multipliers for calculating reward points, these values are subjective and intended to provide a reasonable approximation" (Sect. 3.6.2, p. 13), and "The specific values are suggestive and not meant to be taken as a standard" (p. 13).
- The authors acknowledge the original dataset's obsolescence: the Date field contains "many missing or outdated values, especially from 2014 to 2015 which is quite obsolete as well" (Sect. 3.1, p. 7).
- The authors acknowledge that the framework could be extended: "Expanding the model with demographic attributes could refine customer segmentation, allowing for deeper personalization" (Sect. 5, p. 19).
- [unacknowledged] The Data availability statement says "No datasets were generated or analysed during the current study" (p. 19), which directly contradicts Sect. 3.2, which describes generating a synthetic dataset with the Faker library, and contradicts the abstract's claim that "The usage of original and synthetic datasets ensured scalability and adaptability across different financial domains" (p. 1). Both statements are left standing in the paper.
- [unacknowledged] No sample size is reported anywhere. Neither the number of rows in the original Kaggle dataset nor the number of synthetic records is printed, so no reported metric can be sized or replicated.
- [unacknowledged] The reported R2 of 0.99 is presented as evidence that the formula is accurate, but the models were trained to reproduce reward points that the formula itself computes; the paper concedes that "The model gave information about everyone's transactions and credit card type but not our specific formula or multipliers" (Sect. 5, p. 18). A near-perfect fit to a deterministic target the authors defined is not independent validation, and the paper does not treat it as a limitation.
- [unacknowledged] RMSE and MAE are described as the deciding metrics ("the Random Forest model clearly outperforms... achieves the lowest RMSE and MAE values", Sect. 4.4, p. 18) but no RMSE or MAE value is printed for any of the three models.
- [unacknowledged] No train/test split, cross-validation, confidence interval, standard error or significance test is reported for any model, and no per-fold or per-seed variance is given.
- [unacknowledged] The clustering comparison is claimed but not evidenced numerically: K-Means is said to have "outperformed other clustering techniques (DBSCAN, Hierarchical, GMM)" at a silhouette of 0.42 (Sect. 4.1, p. 15), yet no comparator score is printed and Fig. 4's values are never stated in the text.
- [unacknowledged] The expense-type bonuses contradict themselves. Table 6 (p. 12) prints Travel/Dining + 3.0 and Luxury + 2.0, while the surrounding text prints "travel and dining have a bonus factor of + 2.0, luxury has + 1.5, entertainment has + 1.0, and groceries and bills have + 0.5" (Sect. 3.6.2, p. 13). The two lists disagree on two of five categories and the paper never flags or reconciles the difference.
- [unacknowledged] The modelling target is described inconsistently. Sect. 4.4 says Random Forest is "the most accurate and reliable model for predicting customer credit scores" (p. 18), while the rest of the paper says the models predict reward points. No credit-score model is specified or evaluated.
- [unacknowledged] Feature selection is reported as a correlation-matrix procedure, but no matrix, threshold, retained-variable list or dropped-variable list is printed, so the synthetic schema in Table 3 cannot be tied to the selection step.
- [unacknowledged] The synthetic data were generated with the Faker library after attribute names were suggested by an unnamed LLM, and the paper never states the generative distributions, the seed, or the correlation structure, so the synthetic dataset cannot be reconstructed.
- [unacknowledged] The citation for the source dataset is inconsistent: the text attributes "Sadat Akash's 'Credit Card Transaction Dataset' [15]" (Sect. 2, p. 3), while reference [15] is Ho, Tien, Wu and Singh (2021) and the Kaggle dataset is reference [22] (Sadat, 2024). The reference list and the in-text citation do not match.
- [unacknowledged] The paper is an analysis of Indian credit-card reward economics, not of personal financial management or household expenditure forecasting. Nothing in it addresses income allocation, budgeting, savings, debt repayment, expense-tracker applications, or seasonal expense forecasting for a household, so it cannot support claims about those constructs.
- [unacknowledged] Fig. 5 is described as a 2D visualization and then as a 3D visualization of the same clustering in the same paragraph (Sect. 4.1, p. 15).
- [unacknowledged] No external validity evidence is offered: no issuer supplied data, no A/B or holdout test of the reward formula, and no measure of customer response to the proposed reward allocation.

## Definitions

- **RCT** — Base multiplier for reward points determined by card type: Platinum 2.0, Signature 1.5, Gold 1.0, Silver 0.5 (Table 5, p. 12).
- **CPD** — Card Promotion Date bonus, an additive term in Scored Points; its general value is not tabulated, only the case-study value + 2 (Sect. 3.6.2, p. 12; Sect. 4.3, p. 16).
- **ET** — Expense Type bonus, higher for discretionary categories (Table 6, p. 12).
- **IC** — Income Category bonus: 1 for high income, 0.5 for middle income (Sect. 3.6.2, p. 13).
- **NoC** — Penalty for additional cards, "a multiplier of -0.5" for every card beyond the first, intended "to encourage consolidation" (Sect. 3.6.2, p. 13).
- **AR** — Attrition Risk bonus, "+ 1.0 points to incentivize loyalty" for customers with higher attrition risk (Sect. 3.6.2, p. 13).
- **Scored Points** — The summed six-factor value `[RCT + CPD + ET + IC + NoC + AR]` that scales the monthly amount spent (Sect. 3.6.2, p. 12).
- **Silhouette score** — A clustering validity index ranging from −1 to +1, where "values near 1 are considered better as this indicates how well each of data points is clustered" (Sect. 3.4, p. 10).
- **Davies-Bouldin Index (DBI)** — A validation index for the optimal number of clusters that "should be less than 1"; "A lower value of DB index suggests compactness and minimal overlap between clusters" (Sect. 3.4, p. 10).
- **Risk of Attrition** — A synthetic flag "indicating whether the customer is likely to leave the bank" (Table 3, p. 8).
- **Original dataset** — "Analyzing Credit Card Spending Habits in India", the public Kaggle dataset with seven columns (Table 2, p. 6; reference 22, p. 20).
- **Synthetic dataset** — The Faker-generated sixteen-column replacement built to support user-level and contextual reward calculation (Table 3, p. 8).

## Key Equations

- `Reward Points (Old dataset) = Amount Spent Monthly ∗ Points Scored (Based on Card Type) / 500` — the original, card-type-only reward rule (Sect. 3.6.1, p. 12).
- `Reward Points (Synthetic Dataset) = Scored Points ∗ Amount Spent / 500` — the proposed reward rule (Sect. 3.6.2, p. 12).
- `Scored Points = [RCT + CPD + ET + IC + NoC + AR]` — the six-factor score that multiplies into the reward formula (Sect. 3.6.2, p. 12).
- Case-study substitution: `Scored Points = [1.5 + 2 + 3 + 1 + −1 + 0] = 6.5` and `Reward Points (Synthetic Dataset) = 6.5 ∗ 50000 / 500 = 650 points` (Sect. 4.3, p. 17).
- Case-study original substitution: `Reward Points (Synthetic Dataset) = 4 ∗ 50000 / 500 = 400 points` (Sect. 4.3, p. 16) — note the paper labels this original-dataset computation with the synthetic-dataset equation name.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Proposed ML model (abstract claim) | R2 | 0.99 | — | — | Abstract, p. 1 |
| Reward point prediction, Random Forest | R2 | 0.99 | — | — | Sect. 4.4, p. 18 |
| Reward point prediction, XGBoost | R2 | 0.99 | — | — | Sect. 4.4, p. 18 |
| Clustering of card types, K-Means | silhouette score | 0.42 | — | — | Sect. 4.1, p. 15 |
| Reward point distribution, original (five-feature) dataset | maximum value | 1000 | — | — | Sect. 4.2, p. 16 |
| Reward point distribution, synthetic dataset | range | 0 to 3500 | — | — | Sect. 4.2, p. 16 |
| Mean reward points, synthetic dataset | mean | approximately 1000 | — | — | Sect. 4.4, p. 18 |
| Cardholder XYZ reward points, original formula | reward points | 400 points | — | — | Sect. 4.3, p. 16 |
| Cardholder XYZ reward points, synthetic formula | reward points | 650 points | — | — | Sect. 4.3, p. 17 |
| Cardholder XYZ scored points, synthetic formula | scored points | 6.5 | — | — | Sect. 4.3, p. 17 |
| Base reward points, Platinum | base reward rate | 5 points | — | — | Table 4, p. 11 |
| Base reward points, Signature | base reward rate | 4 points | — | — | Table 4, p. 11 |
| Base reward points, Gold | base reward rate | 3 points | — | — | Table 4, p. 11 |
| Base reward points, Silver | base reward rate | 2 points | — | — | Table 4, p. 11 |
| Base multiplier RCT, Platinum | base multiplier | 2.0 | — | — | Table 5, p. 12 |
| Base multiplier RCT, Signature | base multiplier | 1.5 | — | — | Table 5, p. 12 |
| Base multiplier RCT, Gold | base multiplier | 1.0 | — | — | Table 5, p. 12 |
| Base multiplier RCT, Silver | base multiplier | 0.5 | — | — | Table 5, p. 12 |
| Expense type bonus ET, Travel/Dining (tabulated) | bonus points | + 3.0 | — | — | Table 6, p. 12 |
| Expense type bonus ET, Luxury (tabulated) | bonus points | + 2.0 | — | — | Table 6, p. 12 |
| Expense type bonus ET, Entertainment (tabulated) | bonus points | + 1.0 | — | — | Table 6, p. 12 |
| Expense type bonus ET, Groceries/Bills (tabulated) | bonus points | 0.5 | — | — | Table 6, p. 12 |
| Expense type bonus ET, Other Expenses (tabulated) | bonus points | 0.0 | — | — | Table 6, p. 12 |
| Expense type bonus, Travel/Dining (stated in running text) | bonus factor | + 2.0 | — | — | Sect. 3.6.2, p. 13 |
| Expense type bonus, Luxury (stated in running text) | bonus factor | + 1.5 | — | — | Sect. 3.6.2, p. 13 |
| Expense type bonus, Entertainment (stated in running text) | bonus factor | + 1.0 | — | — | Sect. 3.6.2, p. 13 |
| Expense type bonus, Groceries/Bills (stated in running text) | bonus factor | + 0.5 | — | — | Sect. 3.6.2, p. 13 |
| Income category bonus IC, high income | bonus | 1 | — | — | Sect. 3.6.2, p. 13 |
| Income category bonus IC, middle income | bonus | 0.5 | — | — | Sect. 3.6.2, p. 13 |
| Number of cards penalty NoC, per additional card beyond the first | multiplier | -0.5 | — | — | Sect. 3.6.2, p. 13 |
| Number of cards penalty NoC, Cardholder XYZ holds 3 cards | multiplier | − 1 | — | — | Sect. 4.3, p. 16 |
| Attrition risk bonus AR, higher attrition risk | bonus points | + 1.0 | — | — | Sect. 3.6.2, p. 13 |
| Active credit cards in circulation in India as of 2024 | count | over 83 million | — | — | Sect. 1, p. 1 |
| Synthetic monthly spending trend window | months | 15 months | — | — | Sect. 3.2, p. 9 |
| Cardholder XYZ monthly spending on card | amount | 50,000 | — | — | Sect. 4.3, p. 16 |
| Clustering partition | number of clusters | 4 | — | — | Sect. 3.4, p. 11 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "The proposed ML model achieved an R2 value of 0.99, demonstrating superior accuracy in optimizing reward point distribution." | Abstract, p. 1 | model_performance_evaluation |
| "Besides this, this study focuses on categories as luxury, travel, groceries, EMIs payments, and others and employs ML methods, using K-Means clustering to segment users based on card types (Silver, Gold, Platinum, and Signature)." | Abstract, p. 1 | income_expense_management |
| "Traditional reward programs also rely on rigid, rule-based systems that do not leverage real-time data to adjust rewards based on evolving consumer behavior." | Sect. 2.1, p. 3 | rule_based_classification |
| "To generate synthetic credit card data, the Faker library in Python was used, defining column names, ranges, and relationships between values." | Sect. 3.2, p. 7 | data_collection |
| "Figure 3b highlights the monthly spending trends across 15 months. It can be inferred that during festive seasons as Diwali, Christmas, and Holi, the spending by credit card users shows an increasing trend" | Sect. 3.2, p. 9 | income_expense_management |
| "The inclusion of the Income Category allows for a better understanding of the customer's spending power, which is critical for customizing reward offers." | Sect. 3.2, p. 8 | income_expense_management |
| "The goal is to encourage spending on discretionary expenses like travel, luxury shopping, and dining by providing higher reward points, while discouraging spending on necessities like groceries and bills." | Sect. 3.6.2, p. 13 | income_expense_management |
| "The specific values are suggestive and not meant to be taken as a standard. Banks can adjust the factors to allocate reward points differently based on spending categories." | Sect. 3.6.2, p. 13 | model_development |
| "K-Means achieved a score of 0.42, outperforming other clustering techniques (DBSCAN, Hierarchical, GMM)." | Sect. 4.1, p. 15 | model_performance_evaluation |
| "Clear separation of Card Types within clusters proves its natural segmentation power." | Sect. 4.1, p. 15 | model_performance_evaluation |
| "The analysis in Fig. 6 indicates that, with only five features as in the original dataset, the reward points are restricted to a maximum value of 1000 in synthetic dataset due to the absence of detailed information." | Sect. 4.2, p. 16 | data_collection |
| "However, in the synthetic dataset, including the additional features outlined in Table 3, the reward point distribution extends over a broader and more justified range, ranging from 0 to 3500." | Sect. 4.2, p. 16 | model_development |
| "The model performance results demonstrate a highly impressive R2 value of 0.99 for both the Random Forest and XGBoost models, indicating an almost perfect fit to their respective datasets." | Sect. 4.4, p. 18 | model_performance_evaluation |
| "Specifically, the Random Forest model achieves the lowest RMSE and MAE values, making it the most accurate and reliable model for predicting customer credit scores." | Sect. 4.4, p. 18 | model_performance_evaluation |
| "Due to the unavailability of real credit card transaction data and reward point calculation methods, synthetic datasets have been used, and a formula has been developed accordingly." | Sect. 5, p. 18 | data_collection |
| "The model gave information about everyone's transactions and credit card type but not our specific formula or multipliers." | Sect. 5, p. 18 | model_algorithm_integration |
| "No datasets were generated or analysed during the current study." | Data availability, p. 19 | data_collection |
| "The core problem faced by credit card companies in India is differentiating their offerings in a competitive market to retain high-value customers." | Sect. 1, p. 2 | pfm_apps_problems |

## Remember This

- The paper is a credit-card reward-optimisation study for Indian issuers, not a personal financial management or household-budgeting study.
- Its pipeline is K-Means segmentation by card type plus a hand-specified six-factor reward formula, validated by Linear Regression, XGBoost and Random Forest.
- The headline number is an R2 of 0.99 for Random Forest and XGBoost; K-Means is reported at a silhouette score of 0.42.
- RMSE and MAE decide the model choice in the text, but no RMSE or MAE value is printed.
- No sample size is reported for either the original Kaggle dataset or the synthetic dataset.
- The R2 of 0.99 validates a formula the authors wrote against a target the same formula produced, and the paper's own Data availability statement says no datasets were generated.
- Table 6 and the running text disagree on the expense-type bonuses (Travel/Dining + 3.0 vs + 2.0; Luxury + 2.0 vs + 1.5); both are printed and neither is reconciled.
- No CI, p-value, train/test split or cross-validation appears anywhere in the paper.

## Cited Works

- Cheema, A.; Van der Stede, W. (2019) (context) — Case study of consumer spending habits and reward programmes; said to lack dynamic adaptation to shifts in spending patterns. [Sect. 2, p. 2; reference 11, p. 20]
- Li, T.; Ngai, E.; Hu, Y. (2021) (context) — Review of ML in financial services covering K-Means, Random Forest and Gradient Boosting for consumer prediction and segmentation; described as static. [Sect. 2, p. 2; reference 12, p. 20]
- Ngai, E.; Hu, Y.; Wong, Y.H.; Chen, J. (2022) (context) — Comprehensive review of AI and financial services. [Sect. 2, p. 2; reference 13, p. 20]
- Gan, Y.; Xu, Z.; Chen, L. (2021) (context) — XGBoost and LightGBM ensemble models for predicting consumer behaviour in high-value categories; said to overfit on high-dimensional data. [Sect. 2, p. 3; reference 14, p. 20]
- Sadat, A. (2024) (data source) — "Credit Card Spending Habits in India" Kaggle dataset, the paper's original data source. [Sect. 2, p. 3 (cited as [15]); reference 22, p. 20]
- Ho, H.; Tien, K.M.T.; Wu, A.; Singh, S. (2021) (context) — Sequence analysis approach to segmenting credit card customers; this is reference [15], which the text incorrectly attaches to Sadat's dataset. [Sect. 2, p. 3; reference 15, p. 20]
- Sun, T.; Vasarhelyi, M.A. (2018) (context) — Deep neural networks for predicting credit card delinquencies; high accuracy for risk assessment but no focus on reward-eligible spending. [Sect. 2, p. 3; reference 16, p. 20]
- Sayjadah, Y.; Hashem, I.A.T.; Alotaibi, F.; Kasmiran, K.A. (2018) (context) — Credit card default prediction using machine learning techniques. [Sect. 2, p. 3; reference 17, p. 20]
- Teng, H.W.; Lee, M. (2019) (context) — Five alternative ML methods including decision trees and SVMs for credit card default; said to generalise poorly to high-value spending segments. [Sect. 2, p. 3; reference 18, p. 20]
- Wu, J.; Zhao, X.; Yuan, H. et al. (2023) (context) — CDGAT graph attention network for credit card defaulter prediction. [Sect. 1, p. 1; reference 1, p. 19]
- Ho, A.T.; Morin, L.; Paarsch, H.J.; Huynh, K.P. (2022) (context) — Intervention analysis of credit-card usage during the coronavirus pandemic. [Sect. 1, p. 1; reference 2, p. 19]
- Krivorotov, G. (2023) (context) — ML-based profit modelling for credit card underwriting and credit risk. [Sect. 1, p. 1; reference 3, p. 19]
- Chang, V.; Sivakulasingam, S.; Wang, H.; Wong, S.T.; Ganatra, M.A.; Luo, J. (2024) (context) — Credit risk prediction with machine learning and deep learning on credit card customers. [Sect. 1, p. 1; reference 4, p. 19]
- Patel, P.; Chauhan, S.; Gupta, S.; Gupta, T.; Agrawal, R. (2024) (context) — Ensemble SMOTEfied-GAN for automobile insurance fraud detection. [Sect. 1, p. 1; reference 5, p. 20]
- deHaan, E.; Kim, J.; Lourie, B.; Zhu, C. (2024) (context) — Buy now pay (pain?) later. [Sect. 1, p. 1; reference 6, p. 20]
- Bello, O.A. (2023) (context) — Machine learning algorithms for credit risk assessment, economic and financial analysis. [Sect. 1, p. 1; reference 7, p. 20]
- Dal Colle, L. (2022) (context) — Phygital customer journey intervention. [Sect. 1, p. 1; reference 8, p. 20]
- Xu, D.; Zhang, X.; Hu, J.; Chen, J. (2020) (context) — Ensemble credit scoring with extreme learning machine and generalised fuzzy soft sets. [Sect. 1, p. 1; reference 9, p. 20]
- Tripathi, D.; Edla, D.R.; Cheruku, R.; Kuppili, V. (2019) (context) — Hybrid credit scoring with ensemble feature selection and multilayer ensemble classification. [Sect. 1, p. 1; reference 10, p. 20]
- Altman, E. (2022) (methodology) — Synthesizing credit card transactions. [Sect. 3.1, p. 5; reference 21, p. 20]
- Gkikas, D.; Theodoridis, P. (2022) (context) — AI in consumer behaviour. [Sect. 3.2, p. 9; reference 23, p. 20]
- Yahaya, S.N.; Bakar, M.H. (2020) (methodology) — Critical factors influencing consumer spending by credit card, cited for one-hot encoding. [Sect. 3.3, p. 10; reference 24, p. 20]
- Aniceto, M.C.; Barboza, F.; Kimura, H. (2020) (methodology) — Machine learning predictivity applied to consumer creditworthiness, cited alongside DBSCAN and GMM. [Sect. 3.4, p. 10; reference 25, p. 20]
- Aluri, A.; Price, B.S.; McIntyre, N.H. (2019) (context) — Machine learning to cocreate value through dynamic customer engagement in a brand loyalty programme, cited for clustering use cases. [Sect. 3.4, p. 11; reference 26, p. 20]
- Nasir, M.; Ezeife, C.I.; Gidado, A. (2021) (context) — E-commerce product recommendation with semantic context and sequential purchase history. [Sect. 3.5, p. 11; reference 27, p. 20]
- Rane, N. (2023) (context) — Enhancing customer loyalty through AI, IoT and big data. [Sect. 3.5, p. 11; reference 28, p. 20]
- Kasaian, K.; Murthi, B.P.S.; Steffes, E. (2022) (methodology) — Effects of teaser rates on new credit card customers' spending and borrowing, cited for silhouette-score validity. [Sect. 4.1, p. 15; reference 29, p. 20]
- Zarkesh, B. (2023) (context) — Master's thesis on AI-driven pricing and customer loyalty/churn in banking. [Sect. 4.2, p. 15; reference 30, p. 20]
- Chen, Y.; Lin, C.; Zhao, Y.; Xie, X.; Zhang, M. (2022) (methodology) — Modelling evolving user preferences for sequential recommendation with credit card transactions, arXiv preprint. [Sect. 4.2, p. 15; reference 31, p. 20]
- Mittal, S.; Tyagi, S. (2019) (context) — Performance evaluation of ML algorithms for credit card fraud detection. [Sect. 2, p. 3; reference 19, p. 20]
- Makki, S.; Assaghir, Z.; Taher, Y.; Haque, R.; Hacid, M.; Zeineddine, H. (2019) (context) — Experimental study with imbalanced classification approaches for credit card fraud detection. [Sect. 2, p. 3; reference 20, p. 20]