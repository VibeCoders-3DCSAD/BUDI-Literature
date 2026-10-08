---
paper_id: A--SinghU-2025
first_author: Singh
year: 2025
title: "A Predictive Framework for Annual Financial Planning using Deep Learning Models"
venue: "Journal of Scientific Innovation and Advanced Research (JSIAR)"
doi: Not reported
designation: algorithm
status: extracted
modules: [financial_planning, data_collection, model_development, model_algorithm_integration, model_performance_evaluation]
module_rationale:
  financial_planning: "The framework is designed to process historical financial data, uncover latent temporal structures, and forecast future expenses with high accuracy (Sec. I, p. 1)."
  data_collection: "financial datasets were collected from publicly available government expenditure portals and enterprise-level budgeting datasets (Sec. IV.A, p. 3)."
  model_development: "Three deep learning architectures were evaluated for this task: RNN, LSTM, GRU (Sec. IV.C, p. 3)."
  model_algorithm_integration: "The architecture of the predictive system comprises multiple interconnected modules that handle data ingestion, preprocessing, model training, prediction, and performance evaluation (Sec. III.A, p. 2)."
  model_performance_evaluation: "The forecasting accuracy is assessed using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE) (Sec. III.C.5, p. 2)."
---

## Summary

The paper proposes a deep learning-based predictive framework for annual financial planning, using Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks to forecast annual organizational expenses. The authors argue that traditional statistical methods — linear regression, ARIMA, and exponential smoothing — cannot capture the non-linear, dynamic nature of real-world financial data, and that deep learning architectures are better suited to modeling long-range temporal dependencies. The framework is described as a pipeline of data ingestion, preprocessing, model training, prediction, and evaluation, implemented in Python with TensorFlow and Keras on Google Colab. Experimental results are reported for three models — RNN, LSTM, and GRU — on a financial dataset; the LSTM model achieves the best reported values on MAE (1872.56), RMSE (2614.32), and MAPE (7.02%), ahead of GRU (1950.45, 2701.25, 7.48%) and RNN (2450.13, 3120.88, 9.85%). The paper concludes that LSTM-based forecasting can support resource allocation and strategic financial planning, while acknowledging dependence on high-quality data and sensitivity to overfitting on smaller datasets.

The paper's stated contributions are: a deep learning-based framework utilizing LSTM and GRU models for annual expense forecasting; a comparative analysis between deep learning and classical statistical forecasting methods; a case study with real-world financial data to evaluate model performance and reliability; and insights into model scalability and its practical implications for institutional budget planning (Sec. I, p. 1). The paper is six pages long and is organized into six sections: Introduction, Related Work, Proposed Framework, Methodology, Results and Discussion, and Conclusion.

## Problem and Motivation

Annual financial planning is a critical task for organizations, governments, and institutions, and accurate expense forecasting underpins fiscal discipline, risk mitigation, and operational efficiency (Sec. I, p. 1). The paper argues that traditional forecasting approaches — ARIMA, linear regression, exponential smoothing — are computationally efficient and interpretable but limited: they fail to model non-linear and high-dimensional data patterns commonly observed in financial transactions, are often static, and struggle to adapt to dynamic market conditions or sudden behavioral shifts that matter for long-term planning (Sec. I, p. 1). The growing demand for more accurate and adaptive models has led researchers to recurrent neural networks and their gated variants, LSTM and GRU, which are argued to be particularly suitable for financial time series because they capture long-range dependencies and non-linear patterns (Sec. I, p. 1).

The paper identifies three gaps in the existing literature: most studies focus on short-term prediction (daily or monthly) with limited work addressing long-term annual forecasting; few comparative frameworks comprehensively evaluate deep learning models against traditional methods in a financial planning context; and the lack of real-world case studies limits the practical relevance and transferability of proposed models (Sec. II.D, p. 2). The study positions itself as addressing these gaps by presenting a deep learning-based framework for annual expense forecasting, evaluating its efficacy using real-world financial data, and benchmarking its performance against classical models (Sec. II.D, p. 2).

## Method

**Design.** Computational method-development study with comparative benchmark evaluation of three deep learning architectures (RNN, LSTM, GRU); the authors state no formal design label.

**Sample.** Not reported: the paper describes financial datasets collected from publicly available government expenditure portals and enterprise-level budgeting datasets, augmented where real data were limited with synthetically generated data using Gaussian and exponential distributions, but never prints a record count, number of series, number of departments, or time span. The unit of analysis is the monthly/annual expense record of an organizational department, categorized by expenditure type and fiscal year.

**Context.** geography: Not reported (the authors are at Noida International University, Greater Noida, India; the datasets are described only as public government expenditure portals and enterprise-level budgeting datasets, with no country stated); population: annual organizational expenses, with features including Department ID and Name, Expenditure Category (operations, salaries, infrastructure), Monthly Spending, Fiscal Year, and Transaction Type (fixed, variable, or one-time); setting: computational/offline — Python with TensorFlow and Keras on a Google Colab GPU environment.

### Procedure as reported

- **Data ingestion.** Collect financial records from spreadsheets, databases, and APIs; features include past annual expenses, budget categories, and temporal indicators such as month and fiscal year (Sec. III.C.1, p. 2).
- **Data preprocessing.** Handle missing values (forward-fill methods and mean substitution depending on temporal context), remove anomalies, apply min-max normalization to scale features between 0 and 1 to assist neural network convergence, and transform to time series (Sec. IV.B, p. 3).
- **Feature engineering.** Create temporal features such as month, quarter, and moving averages; include lag features to provide historical context to the models (Sec. IV.B, p. 3).
- **Time-series formatting.** Structure data as supervised sequences using sliding windows with a lookback period of 12 months (Sec. IV.B, p. 3).
- **Model selection.** Evaluate three architectures: RNN (baseline, simple sequence handling), LSTM (selected for long-term dependencies and avoidance of vanishing gradients), and GRU (selected for lighter structure and computational efficiency while retaining sequential learning capability) (Sec. IV.C, p. 3).
- **Hyperparameter tuning.** Optimize learning rate, batch size, and number of hidden layers using Grid Search; explore dropout rates and number of units per layer using Bayesian Optimization (Sec. IV.C, p. 3).
- **Data split.** Divide data temporally into training (70%), validation (15%), and testing (15%) sets to maintain chronological integrity (Sec. IV.D, p. 3).
- **Training environment.** Implement in Python using TensorFlow and Keras; use Google Colab's GPU environment; employ early stopping and learning rate scheduling to enhance generalization and avoid overfitting (Sec. IV.D, p. 3).
- **Evaluation.** Assess accuracy with Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE), to benchmark against baseline models such as ARIMA and linear regression (Sec. III.C.5, p. 2; Sec. IV.D, p. 3).
- **Deployment claim.** The system is described as scalable and modular, allowing integration with cloud-based services for real-time deployment (Sec. III.D, p. 2).

### Framework modules as described

- **Data Ingestion** — collects financial records from spreadsheets, databases, and APIs (Sec. III.C.1, p. 2).
- **Data Preprocessing** — handles missing values, anomalies, normalization, and time-series transformation, plus feature engineering for seasonal and periodic patterns (Sec. III.C.2, p. 2).
- **Model Selection** — supports multiple deep learning architectures; LSTM and GRU primarily used (Sec. III.C.3, p. 2).
- **Prediction Engine** — takes preprocessed features and feeds them into the trained model to generate yearly financial predictions; supports both point forecasting and interval-based forecasting (Sec. III.C.4, p. 2).
- **Evaluation Metrics** — MAE, RMSE, and MAPE (Sec. III.C.5, p. 2).

## Software

- Python (version not reported)
- TensorFlow (version not reported)
- Keras (version not reported)
- Google Colab GPU environment
- Grid Search (implementation not reported)
- Bayesian Optimization (implementation not reported)
- Early stopping and learning rate scheduling (implementations not reported)

## Key Findings

- Table II reports LSTM with the lowest MAE (1872.56), RMSE (2614.32), and MAPE (7.02%) of the three models; GRU is second (1950.45 / 2701.25 / 7.48%) and RNN is worst (2450.13 / 3120.88 / 9.85%).
- The authors state that LSTM "consistently outperformed both RNN and GRU across all three metrics, indicating superior learning of long-term temporal patterns in expense sequences" (Sec. V.A, p. 4).
- Figure 4 is described as showing LSTM forecasts closely following the true trend of annual spending, with minimal deviation, validating its applicability for long-term financial planning (Sec. V.B, p. 4).
- The paper reports that LSTM and GRU demonstrated strong generalization and stability during training, with dropout layers and early stopping mitigating overfitting, while RNN models suffered from gradient vanishing problems and were less stable during training (Sec. V.C, p. 4).
- Figure 5 is described as showing training and validation loss curves for the LSTM model, indicating convergence without overfitting; the paper states the smooth convergence of validation loss highlights the robustness of the model architecture and preprocessing strategy (Sec. V.C, p. 4).
- The authors claim practical benefits for enterprise financial management: departments can plan budgets more accurately and avoid last-minute deficits or surpluses; financial controllers can simulate multiple forecasting scenarios to assess risk; organizations can reduce dependency on manual spreadsheet models and statistical approximations (Sec. V.D, p. 5).
- The paper claims the LSTM-based framework outperforms traditional statistical methods such as ARIMA and linear regression in accuracy and stability (Abstract, p. 1; Sec. VI, p. 5), although no quantitative results for those baselines are reported anywhere in the paper.
- The paper states that LSTM and GRU models outperform traditional methods in modeling sequential financial patterns due to their gated memory structures, which preserve temporal correlations (Sec. IV.C, p. 3).
- The conclusion states that the benefits of deep learning in financial planning are evident, as these models provide a more nuanced understanding of financial data, especially in capturing long-term dependencies and complex seasonal patterns that traditional methods fail to address (Sec. VI, p. 5).

## Key Figures and Tables

- Figure 1 (p. 3): System Architecture of the Proposed Predictive Framework — high-level design of interconnected modules (data ingestion, preprocessing, model training, prediction, evaluation).
- Figure 2 (p. 3): Flow Diagram — Data Processing and Forecasting Pipeline — raw data collection through annual expense forecasting.
- Figure 3 (p. 4): Workflow of Model Design and Training.
- Figure 4 (p. 4): Comparison of Predicted vs. Actual Expenses using LSTM model — the paper states LSTM forecasts closely follow the true trend, with minimal deviation (Sec. V.B, p. 4); the figure's y-axis runs 40 to 120 (thousands of $) across Jan–Dec.
- Figure 5 (p. 5): Training and Validation Loss per Epoch using LSTM — the paper states the loss curves show smooth convergence of validation loss without overfitting (Sec. V.C, p. 4); the figure's y-axis runs 0 to 1.2 across 1–20 epochs.
- Table I (p. 2): Comparison of Traditional vs. Deep Learning Models in Financial Forecasting — qualitative comparison of Linear Regression, ARIMA, Exponential Smoothing, LSTM, and GRU across "Pattern Capture" (Linear Trends; Seasonal/Trend-Based; Recent Trends; Long-Term Dependencies; Non-Linear Patterns) and "Adaptability" (Low; Medium; Low; High; High). No numeric values.
- Table II (p. 4): Performance Comparison of Deep Learning Models — MAE, RMSE, and MAPE for RNN, LSTM, and GRU. This is the only quantitative results table in the paper.

## Limitations and Gaps

- The paper acknowledges that the framework depends on high-quality, clean, and complete datasets, and that incomplete or noisy financial data may hinder model performance (Sec. VI, p. 5).
- The paper acknowledges that while the focus has been on annual expenses, the model's performance may vary with different financial domains or forecasting time horizons (e.g., monthly or quarterly) (Sec. VI, p. 5).
- The paper acknowledges that the models could be sensitive to overfitting if not carefully tuned, particularly in smaller datasets (Sec. VI, p. 5).
- [unacknowledged] No confidence intervals, p-values, significance tests, or per-fold variance are reported anywhere in the paper; Table II gives single point estimates with no uncertainty.
- [unacknowledged] The abstract and conclusion claim the deep learning models were compared against classical statistical approaches (ARIMA, linear regression), but no quantitative results for any traditional baseline are reported — Table II compares only RNN, LSTM, and GRU. Table I is a qualitative comparison only. The claim of outperforming ARIMA and linear regression is therefore unsupported by the paper's own printed evidence.
- [unacknowledged] The dataset is never quantified: no record count, no number of series, no number of departments, no time span, and no train/validation/test sample sizes are printed.
- [unacknowledged] Hyperparameters are not fully specified: the number of hidden layers, number of units per layer, dropout rates, learning rate, and batch size are described as "optimized" or "explored" but no final values are printed, making the experiments unreproducible.
- [unacknowledged] No ablation, no sensitivity analysis, and no comparison of the effect of the individual preprocessing steps (normalization, lag features, temporal features, lookback window length) on performance is reported.
- [unacknowledged] The figures (Figure 4, Figure 5) print no data values, so the visual claims of forecasts "closely follow" the true trend and loss curves showing "smooth convergence" cannot be independently checked from the text.
- [unacknowledged] The paper does not state which country's government expenditure portals supplied the data, nor whether the dataset is public and reusable; the described dataset is a mix of real and synthetic data but the proportions are not reported.
- [unacknowledged] No statistical comparison between LSTM and GRU is performed, even though their reported MAPE values (7.02% vs 7.48%) are close; the claim that LSTM "consistently outperformed" is not tested for significance.
- [unacknowledged] The paper reports three models but the Related Work frames the contribution as comparing against traditional statistical approaches; the actual baseline set is narrower than the framing.
- [unacknowledged] The paper does not report the number of experimental runs, random seeds, or hardware details beyond "Google Colab's GPU environment," so reproducibility is limited.
- [unacknowledged] The paper reports no computational cost, training time, or inference time, despite claiming scalability as a contribution.

## Definitions

- **LSTM (Long Short-Term Memory)** — A recurrent neural network architecture selected for its capability to handle long-term dependencies and avoid vanishing gradient problems (Sec. IV.C, p. 3).
- **GRU (Gated Recurrent Unit)** — A simplified variant of LSTM considered for its lighter structure and computational efficiency while retaining sequential learning capability (Sec. IV.C, p. 3).
- **RNN (Recurrent Neural Network)** — Used as a baseline due to its simplicity in handling sequences (Sec. IV.C, p. 3).
- **ARIMA (Autoregressive Integrated Moving Average)** — A classical statistical forecasting method that the paper positions as a traditional baseline (Sec. I, p. 1).
- **MAE (Mean Absolute Error)** — One of the three evaluation metrics (Sec. III.C.5, p. 2).
- **RMSE (Root Mean Squared Error)** — One of the three evaluation metrics (Sec. III.C.5, p. 2).
- **MAPE (Mean Absolute Percentage Error)** — One of the three evaluation metrics (Sec. III.C.5, p. 2).
- **Lookback period** — The number of prior time steps used as model input; set to 12 months in this study (Sec. IV.B, p. 3).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Annual expense forecasting, RNN model | MAE | 2450.13 | — | — | Table II, p. 4 |
| Annual expense forecasting, RNN model | RMSE | 3120.88 | — | — | Table II, p. 4 |
| Annual expense forecasting, RNN model | MAPE (%) | 9.85 | — | — | Table II, p. 4 |
| Annual expense forecasting, LSTM model | MAE | 1872.56 | — | — | Table II, p. 4 |
| Annual expense forecasting, LSTM model | RMSE | 2614.32 | — | — | Table II, p. 4 |
| Annual expense forecasting, LSTM model | MAPE (%) | 7.02 | — | — | Table II, p. 4 |
| Annual expense forecasting, GRU model | MAE | 1950.45 | — | — | Table II, p. 4 |
| Annual expense forecasting, GRU model | RMSE | 2701.25 | — | — | Table II, p. 4 |
| Annual expense forecasting, GRU model | MAPE (%) | 7.48 | — | — | Table II, p. 4 |
| Model input window (design parameter) | lookback period | 12 months | — | — | Sec. IV.B, p. 3 |
| Data split (design parameter) | training set proportion | 70% | — | — | Sec. IV.D, p. 3 |
| Data split (design parameter) | validation set proportion | 15% | — | — | Sec. IV.D, p. 3 |
| Data split (design parameter) | test set proportion | 15% | — | — | Sec. IV.D, p. 3 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Annual financial planning is a critical aspect of sustainable economic management for organizations, governments, and institutions." | Abstract, p. 1 | financial_planning |
| "Traditional forecasting methods, such as linear regression and ARIMA, often fall short in capturing the non-linear and dynamic nature of real-world financial data." | Abstract, p. 1 | model_algorithm_integration |
| "This research proposes a predictive framework leveraging deep learning models—specifically Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks—for enhanced annual expense forecasting." | Abstract, p. 1 | model_algorithm_integration |
| "Experimental results demonstrate that the deep learning models, particularly LSTM, significantly outperform traditional methods in terms of prediction accuracy, robustness, and responsiveness to seasonal variations in expenditure." | Abstract, p. 1 | model_performance_evaluation |
| "Moreover, they are often static and struggle to adapt to dynamic market conditions or sudden behavioral shifts, which are critical in long-term planning scenarios." | Sec. I, p. 1 | financial_planning |
| "These architectures are particularly suitable for financial time series prediction due to their ability to capture long-range dependencies and non-linear patterns." | Sec. I, p. 1 | model_algorithm_integration |
| "The datasets were divided into training (70%), validation (15%), and testing (15%) sets using a temporal split to maintain chronological integrity." | Sec. IV.D, p. 3 | model_development |
| "As evident, the LSTM model consistently outperformed both RNN and GRU across all three metrics, indicating superior learning of long-term temporal patterns in expense sequences." | Sec. V.A, p. 4 | model_performance_evaluation |
| "The LSTM forecasts closely follow the true trend of annual spending, with minimal deviation, validating its applicability for long-term financial planning." | Sec. V.B, p. 4 | model_performance_evaluation |
| "The LSTM and GRU models demonstrated strong generalization and stability during training. The use of dropout layers and early stopping effectively mitigated overfitting." | Sec. V.C, p. 4 | model_development |
| "RNN models, in contrast, suffered from gradient vanishing problems and were less stable during training." | Sec. V.C, p. 4 | model_development |
| "The current framework is dependent on high-quality, clean, and complete datasets. Incomplete or noisy financial data may hinder model performance." | Sec. VI, p. 5 | data_collection |
| "The models could be sensitive to overfitting if not carefully tuned, particularly in smaller datasets." | Sec. VI, p. 5 | model_development |
| "Exploring hybrid models that combine deep learning with classical statistical techniques (e.g., ARIMA + LSTM) to improve robustness and performance." | Sec. VI, p. 5 | model_algorithm_integration |

## Remember This

- The paper proposes an LSTM/GRU deep learning framework for annual expense forecasting.
- Table II reports LSTM (MAE 1872.56, RMSE 2614.32, MAPE 7.02%) ahead of GRU (1950.45 / 2701.25 / 7.48%) and RNN (2450.13 / 3120.88 / 9.85%).
- No confidence intervals, p-values, or significance tests are reported for any result.
- The paper claims comparison against ARIMA and linear regression but reports no quantitative baseline results anywhere.
- Dataset size, country of data origin, and final hyperparameter values are not reported.
- The framework is a five-module pipeline (ingestion, preprocessing, model selection, prediction engine, evaluation) implemented in Python with TensorFlow and Keras on Google Colab.