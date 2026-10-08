---
paper_id: A--Ghonaim-2025
first_author: "Ghonaim"
year: 2025
title: "An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network"
venue: "International Journal of Theoretical and Applied Research (IJTAR), 4(2), 840-852"
doi: "Not reported"
type: journal-article
designation: algorithm
status: extracted
modules: [pfm_apps_overview, pfm_apps_features, pfm_apps_problems, budgeting, income_expense_management, savings_debt_management, model_development, data_collection, model_algorithm_integration, system_development, model_performance_evaluation, software_quality_evaluation]
module_rationale:
  pfm_apps_overview: "Sec. 2.3 and 2.4 review 25 named consumer budgeting applications - Wafir, Wise Budget, Wallet, Amwaly, Masareef, Money Lover, Money Manager, GoodBudget, Moneon, Spendee and others - by platform, language and capability, and Table 1 compares them against the proposed app."
  pfm_apps_features: "Sec. 2.5 and Table 1 enumerate the feature set being compared - expense tracking, budgets, debt, reports, alerts, wishlist, retirement planning, multilingual support - and state which existing apps lack them."
  pfm_apps_problems: "Sec. 2.3 and 2.4 record the defects of existing apps directly: Wallet does not provide personalized financial guidance and its analytical features are too simple, Money Manager only records purchases without creating a budget, Buddy gives no alert notifications."
  budgeting: "Sec. 3.1.3 and 3.3.1 specify a per-category monthly budget the user assigns in the My Budget interface, stored in the Budget collection and compared against actual spending, with an alert raised when the budget is exceeded."
  income_expense_management: "Sec. 1 describes expense recording across necessities, loans and discretionary spending with daily and monthly tracking, and Sec. 3.3.1 defines the Transactions collection holding type, amount, date, account and category."
  savings_debt_management: "Abstract and Sec. 5 frame staying out of debt and saving as the budgeting objective, and Sec. 3.3.1 specifies Loan and Debt collections storing counterparty, amount, due date and payment status for tracking due and expected payments."
  model_development: "Sec. 3.1.2 sets out the five-step preprocessing pipeline including risk-label construction, and Sec. 3.1.1 and 4.1 give the BiLSTM architecture and the 70/15/15 split of the training data."
  data_collection: "Sec. 4.1 names the Transactions Fraud Dataset from Kaggle with 1,048,576 transactions and 2,000 users, and Sec. 3.1.2 explains that risk labels were built by the authors because the original dataset had none."
  model_algorithm_integration: "Sec. 3.3.2 and 3.3.1 describe deploying the trained network behind a Flask API so each new transaction is scored and the low/medium/high risk result and its probability are written to the FINANCIAL_RISK_PREDICTION collection and surfaced as an in-app alert."
  system_development: "Sec. 3.2 and 3.3 name the implementation stack - React Native with Expo for the client, Python Flask for the API, Cloud Firestore for storage, Figma for the more than 27 designed interfaces, TensorFlow/Keras and scikit-learn for the model."
  model_performance_evaluation: "Table 2 reports per-class precision, recall, F1-score and support and Table 3 the confusion matrix, with the formulas for each metric printed in Sec. 3.4 and an overall accuracy of 97.45% stated in the Abstract, Sec. 4.2 and Sec. 5."
  software_quality_evaluation: "Sec. 4.3 and Table 4 report nine functional test cases TC-1 to TC-9 covering registration, login, accounts, budgets, transactions and risk alerts, all with status Pass, and Sec. 3.4 lists stability, error rate and data security as quality requirements."
---

# An Intelligent Budget Management Mobile Application Based on a Recurrent Neural Network

`A--Ghonaim-2025` — Ghonaim (2025), *International Journal of Theoretical and Applied Research (IJTAR), 4(2), 840-852* \[doi not recorded in `metadata.json`; printed on p. 1 as `10.21608/IJTAR.2025.427658.1148`]

## Summary

A bilingual Arabic-English budget management mobile app pairs a bidirectional LSTM that classifies each transaction as low, medium or high financial risk with a Firestore backend and React Native client, reaching 97.45% overall accuracy while the monthly per-category budget itself is entered by the user.

## Problem and Motivation

The authors argue that most existing budgeting applications lack Arabic-language support and AI-based forecasting, and that those that do use AI still offer no personal plans fitting the user's budget, no alert when a transaction exceeds the budget, and no retirement plan. Budgeting is presented as a necessity rather than a luxury because living has become costly and economic stresses require people to manage scarce resources. The gap named is comprehensiveness: no single existing application combines tracking, budgeting, alerts, recommendations and multilingual access.

## Method

**Design.** Application design-and-build study with a quantitative model evaluation: a mobile client, a cloud backend and an RNN classifier are specified, implemented and tested, and the classifier is benchmarked on a held-out split of a public transaction dataset; the authors state no formal design label.
**Sample.** n = 1,048,576 transactions from the Kaggle Transactions Fraud Dataset with a users table of 2,000 people, split 70% training / 15% validation / 15% testing; the classification report in Table 2 reports a support total of 1,931,161; no human participants were recruited.
**Context.** geography: Not reported (the application targets Arabic and English speakers and is developed at Al-Azhar University, Cairo, Egypt); population: Not reported (users register with name, email, age and annual income); setting: virtual/computational - a mobile client on React Native/Expo against Cloud Firestore with a Python Flask API, validated by nine functional test cases and by a held-out dataset split, with no field deployment.

- Survey existing budget management work, splitting it into research papers and application papers (Sec. 2, Fig. 1, p. 842).
- Review consumer applications with Arabic interfaces - Wafir, Wise Budget, Wallet, Amwaly, Masareef, Money Lover, Money Manager - and record their features and shortfalls (Sec. 2.3, pp. 843-844).
- Review applications without Arabic interfaces - Mobills, GoodBudget, Moneon, Money Flow, Money Manager, Spendee, PayMaster, 1Money, Buddy - and record the same (Sec. 2.4, p. 844).
- Compare the reviewed applications against the proposed system on features, intelligence and personalisation (Sec. 2.5, Table 1, p. 845).
- Specify the architecture: a bidirectional LSTM with two hidden layers of 128 units, softmax output for three risk classes, ReLU hidden activation, Adam at learning rate 0.001, batch size 64, 50 epochs (Sec. 3.1.1, p. 845).
- Specify the client-server split - React Native with Expo for the client, Cloud Firestore for storage, a separate Python service for AI processing (Sec. 3.1.1, pp. 845-846).
- Preprocess the data in five named steps and construct low/medium/high risk labels by an author-defined scoring method because the Kaggle dataset carries none (Sec. 3.1.2, p. 846).
- Deploy the trained network behind a Flask API so each new transaction is featurised, scored and written to the FINANCIAL_RISK_PREDICTION collection, with income transactions forced to low risk (Sec. 3.3.2, p. 848).
- Evaluate the classifier with precision, recall, F1-score and accuracy on held-out data, reporting a classification report and a confusion matrix (Sec. 3.4 and Sec. 4.2, pp. 848-849).
- Run nine functional test cases over registration, login, accounts, budgets, transactions and risk alerts, all recorded as Pass (Sec. 4.3, Table 4, pp. 849-850).

## Software

- React Native with Expo, client framework (version not reported)
- Python with the Flask framework for the API (version not reported)
- Flask-CORS, for cross-domain communication between app and backend (version not reported)
- TensorFlow, to load and run the trained neural network (version not reported)
- Keras, named alongside TensorFlow for building the RNN (version not reported)
- scikit-learn, for preprocessing and model support utilities (version not reported)
- pandas and NumPy, for data handling (version not reported)
- Firebase Cloud Firestore, cloud database and real-time synchronisation (version not reported)
- Firebase Authentication, email and password sign-in (version not reported)
- Figma, for interface design (version not reported)

## Key Findings

- num: The classifier reached an overall accuracy of 97.45% on held-out data, stated identically in the Abstract, Sect. 4.2 and Sect. 5 (pp. 840, 849, 850).
- num: Table 2 reports precision, recall and F1-score of 0.97 for low risk, 0.97 for medium and 0.98 for high, with a macro average of 0.97, over class support of 588,091 low, 619,864 medium and 723,206 high, totalling 1,931,161 (Table 2, p. 849).
- num: The confusion matrix in Table 3 shows 569,272 low-risk predictions in the row headed Predicted Low, 603,108 medium in the Predicted Medium row and 709,498 high in the Predicted High row, with the largest off-diagonal figure 16,331 (Table 3, p. 849).
- num: The training corpus is the Kaggle Transactions Fraud Dataset with 1,048,576 transactions and 2,000 users, split 70% / 15% / 15% into training, validation and testing, and is modelled with a bidirectional LSTM of two hidden layers of 128 units, a softmax output layer for three classes, ReLU hidden activations, Adam at learning rate 0.001, batch size 64 and 50 epochs (Sec. 4.1, p. 848; Sec. 3.1.1, p. 845).
- num: All nine functional test cases TC-1 to TC-9 - new registration, log in, failed login, add account, add budget, add transaction, and high, medium and low financial alerts - are recorded with status Pass (Table 4, pp. 849-850).
- num: More than 27 interfaces were designed for the application, from registration and login through expense management and financial recommendations (Sec. 3.1.3, p. 846).
- The monthly budget is user-assigned per category rather than derived: the My Budget interface has the user "Enter the month and assign a budget for each category" (Table 4, TC-5, p. 850), and the only automatic computation described is a fallback for the case where no budget has been set, computed from the user's income (Sec. 3.3.2, p. 848).
- The budget amount enters the system in exactly two places - stored in the Budget collection for comparison against actual spending, and used as one indicator in the authors' risk-labelling score (Sec. 3.3.1, p. 847; Sec. 3.1.2, p. 846).
- Risk is set to Low automatically whenever the transaction is income, so the classifier is bypassed for inflows, and sensitivity is described as strongest at the Low and High extremes, with the Medium class "solid, though slightly more variable" (Sec. 3.3.2, p. 848; Sec. 4.2, p. 849).
- The authors describe the model as a foundation for continuous improvement rather than a finished system, and list bank synchronisation, blockchain, generative AI, multi-currency, a web companion and store deployment as future work (Sec. 4.2, p. 849; Sec. 5, pp. 850-851).

## Key Figures and Tables

- Fig. 1 (p. 842): Literature Review Taxonomy → the related-work corpus is split into research papers and application papers, and most of it is applications.
- Fig. 2 (p. 846): Architecture Diagram → the client, Firestore backend and Python AI service are shown as three distinct components.
- Fig. 3 (p. 846): Sign UP and Log in Interfaces → registration and authentication screens.
- Fig. 4 (p. 846): Profile Page Interface → the profile page carries Transactions, Debt/Loan and an Arabic/English language switch.
- Fig. 5 (p. 847): Report interface and Add Account Interface → reporting and account creation screens.
- Fig. 6 (p. 847): My Budget Interface and add a new Budget Interface → the budget is set by the user for a chosen month, per category.
- Table 1 (p. 845): The comparison between the reviewed applications and our proposed application → only the caption survives in the conversion, so the per-feature comparison cells cannot be read.
- Table 2 (p. 849): Classification Report → per-class precision, recall, F1-score, support, macro average and weighted average for the three risk levels.
- Table 3 (p. 849): Confusion Matrix → the predicted-versus-actual counts behind the reported metrics.
- Table 4 (pp. 849-850): Functional Testing → nine test cases with scenario, input steps, expected output, status and actual output, all Pass.

## Limitations and Gaps

- The budget is a manual step: the user enters a month and assigns an amount to each category, and the only automatic derivation stated is a fallback computed from the user's income, so nothing in the app optimises or constrains the allocation (Sec. 3.1.3, p. 846; Sec. 3.3.2, p. 848; Table 4 TC-5, p. 850).
- The paper's own future-work list concedes the system is incomplete, naming bank account synchronisation, multi-currency and regional tax support, blockchain integration, generative AI or reinforcement learning, a web companion, store publication and user support as still to be done (Sec. 5, pp. 850-851).
- Evaluation covers only the classifier and functional pass/fail: there is no user study, no usability instrument, no measurement of whether budgets are followed, and no measure of alert usefulness, so the claimed benefit to users is asserted rather than measured (Sec. 4.2-4.3, pp. 849-850).
- The paper itself notes that machine learning struggles to explain why patterns occur, which matters for decision-making - but it raises this about prior work and applies no explanation or interpretability method to its own classifier (Sec. 2.1, p. 842).
- [unacknowledged] No accuracy, precision, recall or F1 value is reported for any baseline model, so the 97.45% figure has nothing to be compared against.
- [unacknowledged] The reported support total of 1,931,161 exceeds the stated dataset size of 1,048,576 transactions, and the paper does not reconcile the two figures.
- [unacknowledged] The risk labels the model is trained on are the authors' own threshold scores over spending relative to income, debt pressure, transaction timing, purchase type and budget exceedance, so the reported metrics measure agreement with that scoring rule rather than with observed financial risk.
- [unacknowledged] Table 1's comparison cells are not recoverable from the conversion, so the paper's central claim of superiority over 25 reviewed applications cannot be checked.
- [unacknowledged] Table 3's cells are out of alignment in the conversion and one figure sits outside the printed block, so the confusion matrix cannot be read off the page without inference.
- [unacknowledged] Sec. 3.2 cites reference [48] for the Python AI components, but the reference list ends at [38].
- [unacknowledged] The application is described as tested against new data and as achieving high potential for practical use, while Sec. 5 lists store publication as a next step, so no deployed system was evaluated.

## Definitions

- **Risk level** — the classifier's three-way output for a transaction, low, medium or high, with a probability attached for each.
- **Risk label construction** — the authors' procedure for creating the low/medium/high labels the original Kaggle dataset lacks, by scoring each transaction on spending relative to income, debt pressure, transaction frequency and timing, purchase type and budget exceedance, then applying simple thresholds.
- **My Budget** — the interface where the user selects a month and assigns a budget amount to each spending category.
- **FINANCIAL_RISK_PREDICTION** — the Firestore collection storing each transaction's predicted risk level and the probability of each.
- **Financial Risk Prediction** — the classification performed on each transaction by the AI model, surfaced immediately in the app.
- **Budget utilisation check** — comparison of actual spending against the amount specified in the Budget collection.
- **Architecture model** — the paper's name for its structure, described as Client-Server with serverless functions or a microservice for AI processing (Sec. 3.1.1, p. 845).
- **Feature-engineering module** — the backend component that converts a user's current-month transactions into the numeric features the trained model expects (Sec. 3.3.2, p. 848).

## Key Equations

- `Precision = TruePositives / (TruePositives + FalsePositives)` — share of predicted-positive cases that are truly positive.
- `Recall = TruePositives / (TruePositives + FalseNegatives)` — share of truly positive cases the model finds.
- `F1 = 2 x (Precision x Recall) / (Precision + Recall)` — harmonic mean of precision and recall.
- `Accuracy = Correct Predictions / Total Predictions` — proportion of correct predictions overall.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Transaction risk classification, proposed RNN overall | accuracy | 97.45% | — | — | Abstract, p. 840 |
| Transaction risk classification, proposed RNN overall | accuracy | 97.45% | — | — | Sec. 4.2 Prediction Model Results, p. 849 |
| Transaction risk classification, proposed RNN overall | accuracy | 97.45% | — | — | Sec. 5 Conclusion, p. 850 |
| Transaction risk classification, proposed RNN overall | F1 measures per risk category | higher than 0.97 | — | — | Abstract, p. 840 |
| Transaction risk classification, low risk class | precision | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, medium risk class | precision | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, high risk class | precision | 0.98 | — | — | Table 2, p. 849 |
| Transaction risk classification, proposed RNN | macro average precision | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, low risk class | recall | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, medium risk class | recall | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, high risk class | recall | 0.98 | — | — | Table 2, p. 849 |
| Transaction risk classification, low risk class | F1-score | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, medium risk class | F1-score | 0.97 | — | — | Table 2, p. 849 |
| Transaction risk classification, high risk class | F1-score | 0.98 | — | — | Table 2, p. 849 |
| Transaction risk classification, low risk class | support | 588,091 | — | — | Table 2, p. 849 |
| Transaction risk classification, medium risk class | support | 619,864 | — | — | Table 2, p. 849 |
| Transaction risk classification, high risk class | support | 723,206 | — | — | Table 2, p. 849 |
| Transaction risk classification, all classes | support total | 1,931,161 | — | — | Table 2, p. 849 |
| Confusion matrix, Predicted Low row as printed | predicted counts against Actual Low, Medium, High | 569,272; 7,300; 11,519 | — | — | Table 3, p. 849 |
| Confusion matrix, Predicted Medium row as printed | predicted counts against Actual Low, Medium, High | 16,331; 603,108; 425 | — | — | Table 3, p. 849 |
| Confusion matrix, Predicted High row as printed | predicted counts against Actual Low, Medium, High | 2,112; 709,498; 11,596 | — | — | Table 3, p. 849 |
| Confusion matrix, largest off-diagonal entry as printed | misclassified count | 16,331 | — | — | Table 3, p. 849 |
| Model training corpus | transactions | 1,048,576 | — | — | Sec. 4.1 Dataset Description, p. 848 |
| Model training corpus | users in the users table | 2,000 | — | — | Sec. 4.1 Dataset Description, p. 848 |
| Dataset partitioning | training / validation / testing split | 70% / 15% / 15% | — | — | Sec. 4.1 Dataset Description, p. 848 |
| Bidirectional LSTM architecture | hidden layers | two hidden layers | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM architecture | units per hidden layer | 128 | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM architecture | output layer | fully connected with softmax activation for 3-class classification | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM architecture | hidden activation function | RELU | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM training | optimizer | Adam | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM training | learning rate | 0.001 | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM training | batch size | 64 | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Bidirectional LSTM training | epochs | 50 | — | — | Sec. 3.1.1 Architecture Model, p. 845 |
| Functional testing of the proposed application | test cases executed | 9 test cases, TC-1 to TC-9 | — | — | Table 4, pp. 849-850 |
| Functional testing of the proposed application | test cases passed | all recorded Pass | — | — | Sec. 4.3 Application Testing Case, p. 850 |
| Interface design | interfaces designed | more than 27 | — | — | Sec. 3.1.3 Interface Design, p. 846 |
| Application scale | journal article page range | 840-852 | — | — | p. 1 header, p. 840 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "A lot of budgeting applications lacked Arabic language support and AI-based forecasting capabilities." | Abstract, p. 840 | pfm_apps_problems |
| "The application was tested on new data; it reached an overall accuracy of 97.45%." | Abstract, p. 840 | model_performance_evaluation |
| "they do not offer personal plans and purchase recommendations that fit the user's budget, nor do they provide the user with an alert when the transaction exceeds the budget" | Sec. 1 Introduction, p. 841 | pfm_apps_problems |
| "It provides multiple services, including recording expenditures across categories such as necessities, loans, and discretionary spending within a monthly adjustable budget." | Sec. 1 Introduction, p. 841 | budgeting |
| "However, the app requires time-consuming manual entries and does not provide personalized financial guidance." | Sec. 2.3 Applications with Arabic Interfaces, p. 843 | pfm_apps_problems |
| "the money manager application only provides the ability to record his/her purchases in an orderly manner without creating a budget" | Sec. 2.3 Applications with Arabic Interfaces, p. 843 | pfm_apps_problems |
| "our application integrates advanced AI techniques, specifically an RNN to predict financial risk and provide personalized plans" | Sec. 2.5 Budget Mobile Applications Comparison, p. 844 | model_algorithm_integration |
| "Because the original Kaggle dataset did not include risk labels, we created them through a clear and replicable scoring method." | Sec. 3.1.2 Data Preprocessing, p. 846 | data_collection |
| "Budget: This collection stores the budget amount for each category, such as food, entertainment, and transportation etc." | Sec. 3.3.1 Backend Development, p. 847 | budgeting |
| "The data is later used by comparing the actual spending against the amount specified." | Sec. 3.3.1 Backend Development, p. 847 | budgeting |
| "It then collects all the users' recent transactions for the current month and tries to find a monthly budget. If no budget has been set before, the system automatically calculates one based on the user's income." | Sec. 3.3.2 Model Integration, p. 848 | budgeting |
| "If the transaction is an income, the risk is always set to Low automatically." | Sec. 3.3.2 Model Integration, p. 848 | model_algorithm_integration |
| "Its sensitivity to medium-risk patterns is solid, though slightly more variable, reflecting the nuanced nature of such behaviors." | Sec. 4.2 Prediction Model Results, p. 849 | model_performance_evaluation |
| "The prediction model's outcomes show a real technical victory, but they also represent a significant human step toward empowering consumers to make better financial decisions." | Sec. 4.2 Prediction Model Results, p. 849 | software_quality_evaluation |
| "The application passed all these tests without errors, which indicates the stability of the application and its ease of use." | Sec. 4.3 Application Testing Case, p. 849 | software_quality_evaluation |
| "Advanced AI techniques, such as generative AI or reinforcement learning, can improve personalization and forecasting accuracy." | Sec. 5 Conclusion, recommendations and future work, p. 850 | model_development |
| "Bank account synchronization would allow real-time financial data import, reducing manual entry." | Sec. 5 Conclusion, recommendations and future work, p. 850 | system_development |
| "Data Security: (Implicit Requirement) Is user data stored and handled securely within Firestore and during API interactions?" | Sec. 3.4 Model Performance, p. 848 | software_quality_evaluation |

## Remember This

- The RNN classifies transaction risk; it does not allocate the budget.
- The monthly per-category budget is typed in by the user, with income-based fallback only.
- Accuracy is 97.45%; precision, recall and F1 are 0.97-0.98 across the three risk classes.
- Trained on the Kaggle Transactions Fraud Dataset: 1,048,576 transactions, 2,000 users.
- Risk labels are the authors' own threshold scores, not observed ground truth.

## Cited Works

- Sonjaya, Y. (2024) (context) — Evolution of budgeting practices from traditional hierarchical top-down instructions to technology-supported planning and prediction [p. 841]
- Bai, R. (2023) (finding) — Financial literacy, mental budgeting and self-control mediate the impact of investment decision making on financial wellbeing [p. 841]
- Bohora, A. (2023) (baseline) — Money Alignment tool analyses current financial industry practice to expose spending patterns and support reduced spending [p. 842]
- Valle-Cruz, D.; Fernandez-Cortez, V.; Gil-Garcia, J. R. (2022) (methodology) — Hybrid multilayer perceptron and multi-objective genetic algorithm applied to public budget allocation and its effect on inflation, GDP and inequality [p. 842]
- Hellwig, K.-P. (2021) (baseline) — Random forest, gradient boosted trees and elastic net for predicting fiscal crises, validated out-of-sample and by data pooling [p. 842]
- Wasserbacher, H.; Spindler, M. (2021) (critique) — Machine learning finds patterns in financial data but struggles to explain why they occur, which matters for decisions [p. 842]
- Hansun, S.; Young, J. C. (2021) (baseline) — LSTM forecasting of LQ45 financial sector indices, lowest MAPE for BBCA and BMRI [p. 842]
- Balathas, M.; Ganeshalingam, S.; Segar, A.; Vallaven, Y.; Siriwardana, S. (2022) (baseline) — Money Empire extracts transaction details from banking SMS alerts and expenses from invoices to automate personal finance management [p. 842]
- Saputra, K. D.; Setiawan, K.; Suryani, D.; Purnama, Y. (2019) (baseline) — Manage on Money uses Google Cloud Vision API and One Signal API in a mobile personal finance application [p. 842]
- Stefanov, T.; Stefanova, M.; Varbanova, S.; Temelkov, S. (2024) (baseline) — Personal finance Android application with budget tracking validated by beta testing including users with visual impairments [p. 842]
- Wong, C. K.; Mohb Salleh, M. N. (2023) (baseline) — CashSave budgeting application passed 78% of test cases but its history tracking failed in some cases [p. 842]
- Pandey, A.; Tripathi, A.; Chauhan, M. (2024) (baseline) — Student-targeted expense management Android application built with the Waterfall Model, noted as lacking adaptability [p. 842]
- Talasila, S. D. (2024) (finding) — MyFinanceAI combines deep networks and reinforcement learning, reporting 40% more recommendation accuracy, 43% less financial stress and 22% higher monthly savings [p. 843]
- Hochreiter, S.; Schmidhuber, J. (1997) (methodology) — Long Short-Term Memory architecture that addresses vanishing gradient problems in recurrent networks [p. 851]
- ComputingVictor (2024) (methodology) — Financial Transactions Dataset on Kaggle supplying 1,048,576 transactions and 2,000 users for model training [p. 852]

---

Conversion: [`A--Ghonaim-2025_marked.md`](../../literature/paper-markdowns/A--Ghonaim-2025_marked.md)