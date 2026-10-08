---
paper_id: I--Yang-2024b
first_author: Yang
year: 2024
title: "Enhancing Financial Services Through Big Data and AI-Driven Customer Insights and Risk Analysis"
venue: "Journal of Knowledge Learning and Science Technology"
doi: 10.60087/jklst.vol3.n3.p53-62

designation: international
status: extracted
modules: [model_algorithm_integration, model_development, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "The paper integrates big data, AI, face recognition, knowledge graphs and XGBoost for financial risk analysis and customer insights (Sect. 1, p. 53; Sect. 2.3, pp. 55-57)."
  model_development: "Describes building an XGBoost-based profit model with hyperparameter search and variable selection across submodels (Sect. 3.2, pp. 58-59)."
  model_performance_evaluation: "Evaluates model performance via out-of-sample MSE, classification error and AUC with 5x cross-validation (Sect. 3.2, p. 59; Sect. 3.3, p. 59)."
---

# I--Yang-2024b

## Summary

The article discusses the integration of big data and artificial intelligence (AI) technologies in the financial sector, focusing on supervised learning for pricing models to enhance customer identification and targeting. The authors construct a six-component customer feature system — customer attributes, debit card transactions, credit card installments, loan applications, trend characteristics, and product-page visit behavior — and propose using AI to profile customers, boost consumption, improve price management, and support risk management and loan approval decisions (Abstract, p. 53; Sect. 1, pp. 53-54). The paper reviews financial risk monitoring technology, machine learning in bank credit, and risk-control solutions based on big data and machine learning, including face recognition, data forgery identification, and gang fraud analysis (Sect. 2.1-2.5, pp. 54-57). It then reports a customer churn prediction model applied to bank account data — drawing a sample of 150,000 loans originated in 2012 and tracked until December 2015 — and models account-level profit using Extreme Gradient Boosting (XGBoost) with hyperparameter search and variable selection (Sect. 3, pp. 57-59). The paper reports that revenue and total profit models have poor forecasting performance but good ranking performance, and that the hump-shaped relationship between profit components and risk is retained between predicted and actual curves (Sect. 3.3, p. 59). It concludes by advocating for further application of AI and big data to improve risk forecasting accuracy and efficiency in financial services (Sect. 4, pp. 59-60).

## Problem and Motivation

With the wide application of big data and artificial intelligence technology across all walks of life, data have grown explosively and information has flooded the financial field. Customers' transaction behaviors, product ownership information, and marketing activity participation have built a huge database of information, laying the foundation for digital applications (Sect. 1, p. 53). Compared with traditional measurement methods and statistical models, machine learning has significant advantages in processing massive data and discovering potential laws; the authors therefore choose supervised learning as the basis of an artificial intelligence pricing model, aiming to realize man-machine decision-making for accurately identifying customers and effectively reaching the target (Sect. 1, p. 53).

Financial risk — the risk generated in financial activities — refers to any potential threat that may lead to financial losses for businesses or institutions, and can be categorized into market risk, credit risk, liquidity risk, operational risk, and legal risk (Sect. 2.1, p. 54). Financial risk monitoring plays a crucial role in today's economic system, not only maintaining financial system stability but also protecting investor interests, ensuring market confidence, enhancing market efficiency, and improving financial regulatory frameworks (Sect. 2.1, p. 54). However, financial risk monitoring faces challenges including handling large and complex financial data, adapting to rapidly changing market environments, technological innovations, preventing financial fraud risks and security threats, and addressing challenges posed by globalization and diversified risks (Sect. 2.1, p. 54).

In the context of digital transformation, the accelerated pace of financial technology innovation and the widespread application of new technologies in the financial field have introduced new dimensions of risk, leading to new characteristics of financial risks; financial regulation and risk prevention therefore face greater challenges, requiring urgent research on the application of new technologies such as artificial intelligence and big data in financial risk monitoring and reasonable predictions and arrangements for future applications (Sect. 2.1, p. 54).

While the customer's level of risk is an important factor for institutions to consider, lenders are primarily interested in maximizing profits; risk and profit are not necessarily monotonously correlated. For example, a credit card revolving customer may have a small possibility of default but need to pay a lot of financial fees; if they pay off the balance each cycle, no fees accumulate (Sect. 2.2, p. 55). The difference between risk models and the profit motive of lenders has been noted in papers such as Finlay (2008), but models predicting account-level profits are still relatively rare in the industry due to data limitations and the potential complexity of the models (Sect. 2.2, p. 55).

## Method

**Design.** The authors state no formal design label. The paper is a computational method-development and review study that builds an AI-based pricing and profit model for financial services and reviews related work in financial risk monitoring and machine learning in credit risk modeling (Sect. 3, pp. 57-59).

**Sample.** n = 150,000 loans originated in 2012 and tracked until December 2015; the unit of analysis is the bank account / loan account (Sect. 3, p. 57).

**Context.** geography: Not reported (multiple datasets are used and bank-level anonymity is preserved); population: Bank accounts classified into three portfolio types — high liquidity (Spender), high finance charge (Revolver), or neither (Middle); setting: Computational/virtual, using XGBoost on bank account data with no live deployment described (Sect. 3, p. 57).

The paper develops a customer feature system and an AI-based pricing model through the following steps:

- Dig into customer information and, combined with business experience, build six characteristic systems: customer attributes, debit card transactions, credit card installments, loan applications, trend characteristics, and visit behavior to product pages (Sect. 1, p. 53).
- Focus debit card and credit card transaction characteristics on transaction frequency, consumption amount, and credit overdraft of customers in different time windows; trend features focus on consumption characteristics of individuals in the past month and the borrowing ratio (Sect. 1, pp. 53-54).
- Use artificial intelligence to achieve an accurate portrait of customers, stimulate consumption potential, and enhance the leverage of price management, providing financial institutions with more effective risk management and loan approval decision support (Sect. 1, p. 54).
- Review financial risk monitoring technology, categorizing financial risk into market, credit, liquidity, operational, and legal risk, and noting that traditional techniques rely heavily on expert experience and traditional statistical models but may perform poorly in fast-changing market environments (Sect. 2.1, p. 54).
- Review machine learning in bank credit, noting that automated underwriting and account management systems have become commonplace over the past two decades and that banks automate creditworthiness evaluation using data extracted from external credit department data and internal account management data to predict the probability of a "bad" customer (Sect. 2.2, p. 55).
- Present risk-control solutions based on big data and machine learning technology, including face recognition technology (Sect. 2.3.1, pp. 55-56), identification of data forgery using relationship graphs (Sect. 2.4, pp. 56-57), and analysis of gang fraud using knowledge graphs, community discovery algorithms (LOUVAIN, LPA, SLPA) and label propagation algorithms (Sect. 2.5, p. 57).
- Draw a sample of bank accounts from multiple datasets, analyze 150,000 loans originated in 2012 and tracked until December 2015, divide accounts into "integrated loan portfolios," and classify banks as high liquidity, high finance charge, or neither (Sect. 3, p. 57).
- Run a multi-class classification problem to predict whether an account belongs to high liquidity, high finance charge, or neither category, with the critical value of the score determining the structure of the overall credit portfolio (Sect. 3, p. 57).
- Model behavioral subcomponents of profit — monthly balance, monthly repayment percentage, monthly tendency to pay late, and monthly tendency to write off — and aggregate these models across time at the account level (Sect. 3.2, p. 58).
- Use "Extreme Gradient Boosting" (XGBoost) as the actual model algorithm, testing driver model structure at different levels of granularity and determining that the approach with the best model performance was at a relatively aggregated level (Sect. 3.2, p. 58).
- Model revenue, default probabilities, and default loss rates at the account level for optimal model performance, but choose to model revenue drivers separately due to interpretation difficulty, with almost insignificant decline in out-of-sample model performance (Sect. 3.2, p. 58).
- For each submodel, use a range of hyperparameter search and variable selection techniques to improve performance and interpretability and reduce potential overfitting; carry out grid search to adjust tree depth and learning rate hyperparameters; control the number of trees with 5x cross validation and early stop functions for AUC (Sect. 3.2, p. 59).
- Limit the learning rate to a relatively small range (between 0.001 and 0.01) because of the high risk of overfitting; the number of trees is also high, reaching into the thousands (Sect. 3.2, p. 59).
- Select the best hyperparameters according to the out-of-sample mean square error of the regression submodel and the out-of-sample classification error of the default probability model, then find the first 30 variables of each submodel according to XGBoost; re-estimate all submodels on these constrained feature spaces through another complete hyperparameter search (Sect. 3.2, p. 59).

## Key Findings

- The paper reports that the forecasting performance of the revenue model and total profit model is poor, but the ranking performance is better (Sect. 3.3, p. 59).
- Without richer account performance data, it is difficult to accurately estimate the net present value of customers to issuers; the model has difficulty capturing changes in experiential profits within the risk range and cannot capture increases in experiential profit changes within the higher risk range (Sect. 3.3, p. 59).
- The model still does a good job of separating more profitable customers from less profitable customers, and the hump-shaped relationship between the profit component and risk is retained between the predicted curve and the actual curve (Sect. 3.3, p. 59).
- The average profitability of the portfolio obtained by ranking by this score is significantly higher than the average profitability when the risk score is used alone (Sect. 3.3, p. 59).
- The hump shape of the curve is most pronounced in the turnover portion, where the credit portfolios of spenders and intermediaries are more closely related to risk (Sect. 3.1, p. 58).
- Across all portfolios, the profit quartile spread across risk ranges increases with the level of risk, indicating the potential challenge of capturing all changes in profits in high-risk areas (Sect. 3.1, p. 58).
- It is more important for institutions with such credit portfolios to understand risk-independent profits; at the same time, doing so is more challenging because of its non-monotonic relationship with risk (Sect. 3.1, p. 58).
- Six feature systems are constructed, including customer attributes, debit and credit card transactions, loan applications, trend characteristics, and product page visit behavior; artificial intelligence technology is used for data processing and feature construction to achieve an accurate portrait of customers (Sect. 4, p. 59).

## Key Figures and Tables

- Figure 1 (p. 56): Principle of machine learning face recognition technology — deep learning (deep neural networks) automatically summarizes face features most suitable for computer understanding and differentiation after learning and training on tens of millions or even billions of level face databases; features extracted from different photos of the same person are very close in feature space, and different people are far apart.
- Figure 2 (p. 57): Experimental data — referenced as showing a comparison of loan portfolios by typical credit sector attributes; spending banks tend to consist of wealthier, higher credit quality, and more creditworthy borrowers than weekly transition banks (Sect. 3, p. 57).
- Table 1 (referenced at Sect. 3.2, p. 59): Results of hyperparameter searches — the paper states "The results of these searches are shown in Table 1," but the table's numeric content is not reproduced in the extracted text.
- Figure 1 (referenced at Sect. 3, p. 57): Comparison of loan portfolios by typical credit sector attributes — shows that spending banks tend to consist of wealthier, higher credit quality, and more creditworthy borrowers than weekly transition banks.

## Limitations and Gaps

- The paper references "Table 1" for the results of hyperparameter searches but the table's numeric content is not reproduced in the available text; the search results cannot be verified from the extraction (Sect. 3.2, p. 59).
- The paper reports no outcome statistics — no accuracy, precision, recall, F1, AUC value, MSE value, or classification error figure is printed anywhere in the text. The results are described only qualitatively: "forecasting performance ... is poor, but the ranking performance is better" (Sect. 3.3, p. 59).
- [unacknowledged] The paper's Section 3 heading reads "CUSTOMER CHURN PREDICTION MODEL IN TELECOM INDUSTRY" but the content describes a bank credit portfolio model, not a telecom churn model; the heading does not match the content (Sect. 3, p. 57).
- [unacknowledged] The paper reports that revenue and total profit models have poor forecasting performance, yet also reports that the model "does a good job of separating more profitable customers from less profitable customers" and that ranking by this score yields significantly higher average profitability than risk score alone; these claims are in tension and no quantitative evidence is provided to reconcile them (Sect. 3.3, p. 59).
- [unacknowledged] The paper provides no statistical significance tests, no confidence intervals, and no cross-validation performance metrics for any model reported (Sect. 3.2-3.3, pp. 58-59).
- [unacknowledged] The 150,000 loans originated in 2012 and tracked until December 2015 are described as drawn from "multiple datasets" but no dataset names, sources, or access details are reported; the sample's provenance is unverifiable (Sect. 3, p. 57).
- [unacknowledged] The paper's review sections (Sect. 2.1-2.5) are not tied to the empirical Section 3; the face recognition, data forgery, and gang fraud material is presented as background and is not tested or evaluated in the reported model.
- [unacknowledged] The paper reports no hyperparameter values actually selected — no optimal tree depth, no optimal learning rate, no optimal number of trees — only the ranges searched and the top 30 variables per submodel (Sect. 3.2, p. 59).
- [unacknowledged] The paper's acknowledgement section thanks authors of unrelated papers on patient disease risk, AI face recognition, and GPU computing, but none of these contributions are integrated into the reported method or evaluation.

## Definitions

- **Big data** — The paper does not formally define this term; it is used throughout to refer to the large-scale data generated by customer transaction behaviors, product ownership information, and marketing activity participation (Sect. 1, p. 53).
- **Artificial intelligence (AI)** — Used in the paper to refer to supervised learning and machine learning methods applied to financial services, particularly for pricing models and customer identification (Sect. 1, p. 53).
- **Financial risk** — The risk generated in financial activities; any potential threat that may lead to financial losses for businesses or institutions (Sect. 2.1, p. 54).
- **Market risk** — Fluctuations in financial market prices, which may arise from changes in interest rates, stock prices, and other factors (Sect. 2.1, p. 54).
- **Credit risk** — Potential losses due to borrowers or counterparties failing to fulfill their contractual obligations (Sect. 2.1, p. 54).
- **Operational risk** — Errors and losses caused by internal processes, systems, or human factors (Sect. 2.1, p. 54).
- **Liquidity risk** — Losses incurred when assets cannot be effectively bought or sold within a specific period (Sect. 2.1, p. 54).
- **Legal risk** — Potential legal disputes and regulatory changes in financial activities (Sect. 2.1, p. 54).
- **High liquidity banks (Spender, Spender)** — One of three bank portfolio categories; spending banks tend to consist of wealthier, higher credit quality, and more creditworthy borrowers (Sect. 3, p. 57).
- **High finance charge banks (Revolver, Revolver)** — One of three bank portfolio categories; credit card revolving customers who may have a small possibility of default but need to pay a lot of financial fees (Sect. 2.2, p. 55; Sect. 3, p. 57).
- **Middle banks (Middle, Middle)** — One of three bank portfolio categories; neither high liquidity nor high finance charge (Sect. 3, p. 57).
- **XGBoost (Extreme Gradient Boosting)** — The actual model algorithm used for estimation in the profit model (Sect. 3.2, p. 58).

## Key Equations

Not reported. The paper describes models conceptually but prints no equations.

## Statistical Evidence

The paper reports no outcome statistics — no accuracy, precision, recall, F1, AUC, MSE, or classification error values are printed. The following rows record the quantities that are reported, all of which are design or method parameters rather than findings.

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Loan sample analyzed | count | 150,000 | — | — | Sect. 3, p. 57 |
| Loan origination year | year | 2012 | — | — | Sect. 3, p. 57 |
| Loan tracking end date | date | December 2015 | — | — | Sect. 3, p. 57 |
| Customer feature systems constructed | count | 6 | — | — | Sect. 1, p. 53 |
| Bank portfolio categories in classification | count | 3 | — | — | Sect. 3, p. 57 |
| Multi-class classification output classes | count | 3 | — | — | Sect. 3, p. 57 |
| Face database size for recognition training | image count | tens of millions or even billions | — | — | Sect. 2.3.1, p. 56 |
| XGBoost learning rate range | rate | 0.001–0.01 | — | — | Sect. 3.2, p. 59 |
| Cross-validation folds for tree number control | count | 5 | — | — | Sect. 3.2, p. 59 |
| Top variables selected per submodel | count | 30 | — | — | Sect. 3.2, p. 59 |
| Number of trees in XGBoost model | count | thousands | — | — | Sect. 3.2, p. 59 |
| Trend feature lookback window | period | past month | — | — | Sect. 1, p. 54 |
| Debit and credit card transaction time windows | periods | different time Windows | — | — | Sect. 1, p. 53 |
| Face recognition training database level | scale | tens of millions or even billions | — | — | Sect. 2.3.1, p. 56 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "With the wide application of big data and artificial intelligence technology in all walks of life, we have witnessed the explosive growth of data and the flood of information." | Sect. 1, p. 53 | model_algorithm_integration |
| "we first dig into customer information, and combined with business experience to build six characteristic system." | Sect. 1, p. 53 | model_development |
| "our goal is to use artificial intelligence to achieve an accurate portrait of customers, so as to stimulate the consumption potential of customers and enhance the leverage of price management." | Sect. 1, p. 54 | model_algorithm_integration |
| "Financial risk, the risk generated in financial activities, refers to any potential threat that may lead to financial losses for businesses or institutions." | Sect. 2.1, p. 54 | model_algorithm_integration |
| "Effective risk monitoring techniques can alert potential financial risks, prevent major economic impacts, optimize resource allocation for financial institutions, and enhance overall market operational efficiency" | Sect. 2.1, p. 54 | model_performance_evaluation |
| "The actual model algorithm used for the estimation is 'Extreme Gradient Boosting', also known as XgBoost." | Sect. 3.2, p. 58 | model_development |
| "Because of the high risk of overfitting of this sample, the learning rate was limited to a relatively small range (between 0.001 and 0.01)" | Sect. 3.2, p. 59 | model_development |
| "This paper selects the best hyperparameters according to the out-of-sample mean square error of the regression submodel and the out-of-sample classification error of the default probability model" | Sect. 3.2, p. 59 | model_performance_evaluation |
| "the model still does a good job of separating more profitable customers from less profitable customers" | Sect. 3.3, p. 59 | model_performance_evaluation |
| "The foundation of machine learning is built on structured databases." | Sect. 1, p. 53 | model_development |
| "By leveraging AI, financial institutions aim to accurately profile customers, boost consumption, and improve price management" | Abstract, p. 53 | model_algorithm_integration |
| "In the context of digital transformation, the accelerated pace of financial technology innovation and the widespread application of new technologies in the financial field have introduced new dimensions of risk" | Sect. 2.1, p. 54 | model_algorithm_integration |
| "However, with the advent of machine learning methods in credit risk modeling, financial institutions have come to rely on models to estimate increasingly complex relationships" | Sect. 2.2, p. 55 | model_development |
| "This paper draws a sample of bank accounts from multiple datasets and analyses 150,000 loans originated in 2012, tracking them until December 2015." | Sect. 3, p. 57 | model_development |

## Remember This

- The paper proposes a six-feature customer system for AI-driven pricing and risk analysis in financial services, covering customer attributes, debit/credit card transactions, loan applications, trend characteristics, and product page visits.
- It reviews financial risk monitoring, machine learning in bank credit, face recognition, data forgery detection, and gang fraud analysis.
- It reports a bank portfolio model using XGBoost on 150,000 loans originated in 2012 and tracked until December 2015.
- No outcome statistics — no accuracy, F1, AUC, or error values — are printed; results are described only qualitatively.
- The model's forecasting performance for revenue and total profit is described as poor, but ranking performance is described as better; the hump-shaped relationship between profit and risk is retained.
- The paper's Section 3 heading incorrectly labels the model as a "CUSTOMER CHURN PREDICTION MODEL IN TELECOM INDUSTRY" while the content is about bank credit portfolios.

## Cited Works

- Thomas (2000) (context) — Automated underwriting and account management systems predict the probability of a "bad" customer using external credit department data and internal account management data. [p. 55]
- Finlay (2008) (methodology) — Compares linear and machine learning-style approaches in neural network algorithms, demonstrating that a continuous financial behavior model is superior to a binary model of customer default; also notes the difference between risk models and lender profit motive. [p. 55]
- Finlay (2010) (methodology) — Extends comparison of linear and machine learning-style approaches in neural network algorithms. [p. 55]
- Fitzpatrick and Mues (2021) (methodology) — Extends a set of algorithms for predicting profitability in the context of P2P lending. [p. 55]
- Verbraken et al. (2014) (methodology) — Points out that profit-based modeling allows the calculation of an optimal profit-based threshold that would otherwise not fully approximate the average profit using default scores and segment levels. [p. 55]
- Shi, Y., Yuan, J., Yang, P., Wang, Y., & Chen, Z. (context) — Implementing Intelligent Predictive Models for Patient Disease Risk in Cloud Data Warehousing; acknowledged as inspiration for the present article. [p. 60]
- Li, Huixiang, et al. (2024) (context) — "AI Face Recognition and Processing Technology Based on GPU Computing," Journal of Theory and Practice of Engineering Science 4.05: 9-16; acknowledged as inspiration for the present article. [p. 60]
- Zhan, Xiaoan, et al. (2024) (context) — "Aspect category sentiment analysis based on multiple attention mechanisms and pre-trained models," Applied and Computational Engineering 71: 21-26. [p. 60]
- Xu, J., et al. (2024) (context) — "Practical Applications of Advanced Cloud Services and Generative AI Systems in Medical Image Analysis," arXiv preprint arXiv:2403.17549. [p. 61]
- Huang, J., et al. (context) — "Implementation of Seamless Assistance with Google Assistant Leveraging Cloud Computing." [p. 61]
- Liang, Penghao, et al. (2024) (context) — "Automating the Training and Deployment of Models in MLOps by Integrating Systems with Machine Learning," arXiv preprint arXiv:2405.09819. [p. 61]
- Zhan, Tong, et al. (2024) (context) — "Optimization Techniques for Sentiment Analysis Based on LLM (GPT-3)," arXiv preprint arXiv:2405.09770. [p. 61]
- Zhang, Y., et al. (2024) (context) — "Application of Machine Learning Optimization in Cloud Computing Resource Scheduling and Management," arXiv preprint arXiv:2402.17216. [p. 61]
- Gong, Y., et al. (2024) (context) — "Dynamic Resource Allocation for Virtual Machine Migration Optimization using Machine Learning," arXiv preprint arXiv:2403.13619. [p. 61]
- Chen, B., et al. (2018) (context) — "Structure of the DNA-binding domain of human myelin-gene regulatory factor reveals its potential protein-DNA recognition mode," Journal of Structural Biology 203(2): 170-178. [p. 61]
- Lei, Han, et al. (2024) (context) — "Automated Lane Change Behavior Prediction and Environmental Perception Based on SLAM Technology," arXiv preprint arXiv:2404.04492. [p. 61]
- Fan, C., et al. (context) — "Integrating Artificial Intelligence with SLAM Technology for Robotic Navigation and Localization in Unknown Environments." [p. 61]
- Ding, W., et al. (context) — "Immediate Traffic Flow Monitoring and Management Based on Multimodal Data in Cloud Computing." [p. 61]
- Wang, Y., et al. (2024) (context) — "The Intelligent Prediction and Assessment of Financial Information Risk in the Cloud Computing Model," arXiv preprint arXiv:2404.09322. [p. 61]
- Zhou, Y., et al. (2024) (context) — "RNA Secondary Structure Prediction Using Transformer-Based Deep Learning Models," arXiv preprint arXiv:2405.06655. [p. 61]
- Liu, Beichang, et al. (context) — "Precise Positioning and Prediction System for Autonomous Driving Based on Generative Artificial Intelligence." [p. 61]
- Wang, B., et al. (context) — "Predictive Optimization of DDoS Attack Mitigation in Distributed Systems using Machine Learning." [p. 61]
- Cui, Z., et al. (context) — "Precision Gene Editing Using Deep Learning: A Case Study of the CRISPR-Cas9 Editor." [p. 61]
- Li, Hanzhe, et al. (2024) (context) — "Driving Intelligent IoT Monitoring and Control through Cloud Computing and Machine Learning," arXiv preprint arXiv:2403.18100. [p. 62]
- Tian, J., et al. (context) — "Intelligent Medical Detection and Diagnosis Assisted by Deep Learning." [p. 62]
- Qi, Y., et al. (2024) (context) — "Leveraging Federated Learning and Edge Computing for Recommendation Systems within Cloud Computing Networks," arXiv preprint arXiv:2403.03165. [p. 62]
- He, Z., et al. (context) — "Application of K-means Clustering Based on Artificial Intelligence in Gene Statistics of Biological Information Engineering." [p. 62]
- Zhou, Y., et al. (2023) (context) — "Semantic Wireframe Detection." [p. 62]
- Qi, Yaqian, et al. (2024) (context) — "Application of AI-based Data Analysis and Processing Technology in Process Industry," Journal of Computer Technology and Applied Mathematics 1(1): 54-62. [p. 62]
- Tian, J., et al. (2024) (context) — "Deep Learning Algorithms Based on Computer Vision Technology and Large-Scale Image Data," Journal of Computer Technology and Applied Mathematics 1(1): 109-115. [p. 62]
- Wang, X., et al. (2024) (context) — "Short-Term Passenger Flow Prediction for Urban Rail Transit Based on Machine Learning," Journal of Computer Technology and Applied Mathematics 1(1): 63-69. [p. 62]
- Feng, Y., et al. (2024) (context) — "Application of Machine Learning Decision Tree Algorithm Based on Big Data in Intelligent Procurement." [p. 62]
- Tian, Jingxiao, et al. (context) — "Intelligent Medical Detection and Diagnosis Assisted by Deep Learning." [p. 62]

```text
CLAIM AUDIT
1. [NOT SUPPORTED] The Philippine evidence summarized in Chapter I places these findings in context. Savings buffers are thin and expenditures track income closely (Bangko Sentral ng Pilipinas [BSP], 2026b; Financial Sector Forum [FSCC], 2024), and income level and saving behavior predict financial resilience among Filipinos (Bunyi, 2024). — The paper does not mention the Philippines, savings buffers, income level, saving behavior, or Filipino financial resilience. It is about AI and big data in financial services, credit risk modeling, and bank portfolio classification using XGBoost (Sect. 1-4, pp. 53-60). None of the cited claims appear in the paper.
```
