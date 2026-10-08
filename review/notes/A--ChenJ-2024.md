---
paper_id: A--ChenJ-2024
first_author: Chen
year: 2024
title: "A Survey of Time Series Data Forecasting Methods Based on Deep Learning"
venue: "Journal of Basic and Applied Research International"
doi: 10.56557/jobari/2024/v30i69014
designation: algorithm
status: extracted
modules: [model_development, model_performance_evaluation, data_collection, model_algorithm_integration]
module_rationale:
  model_development: "Sec. 3 (pp. 144-150) derives the RNN, LSTM, GRU, Bi-LSTM and Transformer architectures gate by gate, which is the paper's core method exposition."
  model_performance_evaluation: "Table 1 (p. 155) reports MSE and MAE for five models across four datasets, and Sec. 3.6 (p. 151) fixes the evaluation protocol."
  data_collection: "Sec. 2.2 (pp. 143-144) catalogues the ETT, ECL, Traffic, Weather, ILI and TE datasets with their sources, spans and variable counts."
  model_algorithm_integration: "Sec. 3.4 and Sec. 4.1 (pp. 149, 155) treat the stacked LSTM-RNN as a combined architecture and argue for hybrid statistical plus deep learning forecasting."
---

# A--ChenJ-2024 — Extraction Note

## Summary

This is a review article on deep learning methods for time series forecasting, published in the *Journal of Basic and Applied Research International* as Article no. JOBARI.12619. It surveys the common features of time series data, the datasets used in the field, the evaluation metrics applied to forecasting models, and the four families of deep architectures that dominate recent work: recurrent neural networks (RNNs), Long Short-Term Memory (LSTM) networks, Gated Recurrent Units (GRUs), and the Transformer with its self-attention mechanism (Abstract, p. 140; Sec. 3, pp. 144-150). Beyond exposition, the paper runs its own univariate prediction experiment comparing five models — RNN, LSTM, GRU, Transformer and a stacked LSTM-RNN — on four public datasets: ETTm2, Electricity (ECL), Weather and Traffic (Sec. 3.6, p. 151; Table 1, p. 155).

The reported results are mixed across datasets rather than uniformly favouring one architecture. The Transformer records the lowest MSE (3.418) and MAE (1.399) on ETTm2; LSTM records the lowest MAE on Electricity (1.848) and Traffic (0.020); GRU records the lowest MSE on Electricity (19.524) and Traffic (0.00110); and the plain RNN is credited with the best Weather performance (MSE 0.007, MAE 0.060) (Table 1, p. 155). The Transformer's Weather figures — MSE 0.827 and MAE 0.341 — are two orders of magnitude larger than every other model's on that dataset and are reported without comment (Table 1, p. 155). The authors conclude that "in most cases, the combination of the two results in a certain performance improvement" when referring to the LSTM-RNN stack, and that a single fixed model cannot be universally applied because different sample types exhibit distinct distribution patterns (Sec. 3.6 and Sec. 4.1, p. 155).

The paper is a survey rather than a system-building study. It reports no confidence intervals, no significance tests, no repeated runs, no variance, no train/validation/test split sizes, and no hyperparameters beyond the input sequence length, the prediction length and the optimizer (Sec. 3.6, p. 151). Its contribution to this corpus is therefore architectural and metric-related vocabulary: what the four deep architectures are, how they are defined mathematically, which datasets the field uses, and which metrics (MSE, MAE, RMSE, MAPE, SMAPE, R²) are standard (Sec. 2.1, pp. 142-143). The paper contains no household finance data, no Philippine data, and no personal financial management application of any kind; its forecasting framing is generic (finance, healthcare, energy, transportation, meteorology) rather than expense-specific (Sec. 1, p. 141).

## Problem and Motivation

The paper's stated motivation is scale. Time series data "exist widely in domains like finance, healthcare, energy, transportation, and meteorology and are easily accessible," but with the widespread use of sensing devices and advances in data processing, time series "are being generated at an explosive rate" (Sec. 1, p. 141). Traditional machine learning approaches — decision trees, random forests, linear regression — and traditional statistical models such as Support Vector Machines (SVM) and Autoregressive Models (AR) face significant challenges on this data because of temporal dependence, seasonality, non-stationarity and the need for careful feature engineering; AR and SVM in particular require "manual configuration of seasonal and trend components," which limits their efficiency and accuracy on large-scale datasets (Sec. 1, p. 141).

Deep neural networks are proposed as the alternative because they "extract high-level features and identify complex patterns within and across time series with minimal manual effort" and rely on fewer structural assumptions (Sec. 1, p. 141). The paper traces a short history of that shift: Elman's 1990 RNN and its hidden state, the LSTM and GRU variants that address vanishing and exploding gradients, and Vaswani et al.'s 2017 Transformer with self-attention, which "captures long-term dependencies, addressing limitations of traditional RNNs in long-range prediction and parallel computation" (Sec. 1, p. 141).

A second motivation is architectural fit. CNNs are described as strong at feature extraction but weak on sequences: "CNNs struggle to capture long-range dependencies in time series," and increasing convolutional depth "often remains insufficient for modeling long-term dependencies within sequences" (Sec. 1, p. 141). RNNs handle sequences but degrade over long horizons; Transformers parallelize but, per the Autoformer discussion, sparse attention mechanisms "limit the utilization of information" and self-attention "struggle[s] to capture reliable dependencies" when temporal patterns are complex (Sec. 1, p. 142). The review exists to place these trade-offs side by side.

The paper does not state a research gap in the conventional sense, does not pose a hypothesis, and does not identify an application problem to be solved. Its motivating claim is that the field needs a consolidated comparison of deep architectures under one experimental protocol (Sec. 5, p. 156).

## Method

**Design.** Systematic literature review with an accompanying comparative benchmark experiment on public datasets; the paper is labelled "Review Article" on its first page and states "This paper presents a systematic review of time series forecasting methods based on deep learning" (Sec. 5, p. 156). The authors state no further formal design label, no sampling frame for the literature, and no search strategy.

**Sample.** Five deep learning models (RNN, LSTM, GRU, Transformer, LSTM-RNN) evaluated on four public datasets (ETTm2, Electricity, Traffic, Weather); the unit of analysis is one univariate series per dataset — for ETTm2, Electricity and Weather the first variable was selected, and for Traffic the third variable was selected, "representing the hourly road occupancy rate recorded by a sensor" (Sec. 3.6, p. 151). No human participants were involved.

**Context.** geography: Not reported as a study site; the datasets originate from the State Grid Corporation of China (ETT), California's Department of Transportation (Traffic), the Max Planck Institute for Biogeochemistry meteorological station (Weather), and an unspecified electricity consumption load source for 2012-2014 (Sec. 2.2, pp. 143-144); population: Not applicable, no human participants; setting: Computational — offline benchmark implemented in PyTorch, models trained with the Adam optimizer, input sequence length 24 and prediction length 1, evaluated with MSE and MAE (Sec. 3.6, p. 151).

The method proceeds in five movements:

- Define the evaluation metrics and give each one's formula: MSE, RMSE, MAE, MAPE, SMAPE and R² (Sec. 2.1, pp. 142-143).
- Catalogue the datasets used in the field: ETT, ECL, Traffic, Weather, ILI and TE, with source, period and variable counts for each (Sec. 2.2, pp. 143-144).
- Derive the RNN cell and its update and output equations, then motivate the LSTM and GRU variants as fixes for vanishing and exploding gradients (Sec. 3.1-3.3, pp. 144-149).
- Derive the LSTM gate by gate — forget gate, input gate, cell-state update and output gate — then the GRU's update and reset gates, then the Bi-LSTM's forward/backward concatenation (Sec. 3.2-3.4, pp. 145-149).
- Present the Transformer's encoder-decoder stack, scaled dot-product self-attention, multi-head attention and sinusoidal positional encoding (Sec. 3.5, pp. 150-151).
- Run the comparison: four datasets, five models, one variable each, input length 24, prediction length 1, Adam optimizer, MSE and MAE, PyTorch implementation (Sec. 3.6, p. 151).
- Report the results as prediction-curve figures for each dataset and as a single summary table of MSE and MAE (Figs. 10-13, pp. 152-154; Table 1, p. 155).
- Summarise and set an outlook covering algorithmic improvement, broader application domains, cross-domain fusion with statistics and chaos theory, and real-time prediction as computing power improves (Sec. 4.1-4.2, pp. 155-156).

## Software

- PyTorch — the implementation framework for all models (Sec. 3.6, p. 151)
- Adam optimizer — used to train all models (Sec. 3.6, p. 151)
- No version numbers are reported for PyTorch or for any other tool
- Evaluation metrics implemented: MSE and MAE (Sec. 3.6, p. 151)
- Datasets: ETTm2, Electricity (ECL), Traffic, Weather (Sec. 3.6, p. 151)

## Key Findings

- num: The Transformer achieved the lowest ETTm2 error, with MSE 3.418 and MAE 1.399 against MSE 3.459/MAE 1.404 for RNN, 3.480/1.414 for LSTM, 3.454/1.402 for GRU and 3.454/1.404 for LSTM-RNN (Table 1, p. 155).
- num: LSTM achieved the lowest MAE on Electricity (1.848) and on Traffic (0.020); GRU achieved the lowest MSE on Electricity (19.524) and on Traffic (0.00110) (Table 1, p. 155).
- num: RNN is credited with the best Weather performance, with MSE 0.007 and MAE 0.060, tying GRU and LSTM-RNN at MSE 0.007 (Table 1, p. 155).
- num: The Transformer's Weather errors (MSE 0.827, MAE 0.341) are far above every other model's on that dataset, where all four alternatives report MSE 0.007 or 0.008 (Table 1, p. 155).
- num: On Electricity, RNN (21.603) and LSTM-RNN (21.583) have the largest MSE, while GRU (19.524), Transformer (19.541) and LSTM (19.821) cluster lower (Table 1, p. 155).
- num: On Traffic, all five models fall within MSE 0.00110-0.00125 and MAE 0.020-0.021 — a spread of roughly 14% in MSE and 5% in MAE (Table 1, p. 155).
- num: The ETT dataset contains 1,051,200 data points, split into subsets at 15-minute and 1-hour sampling intervals containing 69,680 and 17,420 data points respectively (Sec. 2.2.1, p. 143).
- num: The ETT subsets have seven features each — the oil-temperature target plus six power load features (Sec. 2.2.1, p. 143).
- num: The Weather dataset records 21 meteorological indicators every 10 minutes from 2020 to 2021 (Sec. 2.2.4, p. 144).
- num: The TE chemical process dataset comprises 41 measured variables (XMEAS (1)-XMEAS (41)) and 12 manipulated variables (XMV (1)-XMV (12)), for 53 observed variables, and simulates 21 fault types across 6 categories (Sec. 2.2.6, p. 144).
- num: The ILI dataset records the weekly ratio of influenza-like-illness patients to total patients from 2002 to 2021 (Sec. 2.2.5, p. 144).
- num: All models used input sequence length 24 and prediction length 1 (Sec. 3.6, p. 151).
- The authors' overall conclusion is that the combination of an RNN and an LSTM "in most cases" yields a certain performance improvement, and that the LSTM-RNN outperforms the standard RNN and the ordinary LSTM on ETTm2 and Weather (Sec. 3.6, p. 155).
- The authors conclude that "a single fixed model cannot be universally applied," which is why the field has turned to hybrid methods that combine traditional statistical models with deep learning (Sec. 4.1, p. 155).
- The paper identifies interpretability and data hunger as the standing costs of deep models: they rely on fewer structural assumptions, "making them more challenging to interpret and often requiring larger training datasets to learn accurate models" (Sec. 4.1, p. 155).
- The outlook predicts that Transformers and graph neural networks will handle time-series data better, that cross-domain fusion with statistics and chaos theory will improve generalization and robustness, and that real-time prediction will become possible as computing power improves (Sec. 4.2, pp. 155-156).

## Key Figures and Tables

- Fig. 1 (p. 144): RNN structure diagram — output o_t, hidden state h_t, previous hidden state h_{t−1} and current input x_t, with activation functions f1 and f2 and weight matrices W, U, V → establishes the recurrence that all later variants modify.
- Fig. 2 (p. 145): LSTM structure diagram — forget gate, input gate, cell state and output gate → the four-component decomposition the paper then derives.
- Fig. 3 (p. 146): Forgetting gate structure diagram → illustrates the element-wise multiplication of the sigmoid vector with the previous cell state C_{t−1}.
- Fig. 4 (p. 146): Input door structure diagram → the sigmoid gate plus tanh candidate vector that decides what enters the cell state.
- Fig. 5 (p. 147): Update cell structure diagram → the combination of the forgotten and newly added information into the new cell state C_t.
- Fig. 6 (p. 147): Output gate structure diagram → the gate that filters the cell state into the hidden output h_t.
- Fig. 7 (p. 148): GRU structure diagram → the update and reset gates that replace LSTM's separate memory cell.
- Fig. 8 (p. 149): Bi-LSTM structure diagram → forward and backward LSTM layers whose outputs are summed element-wise.
- Fig. 9 (p. 150): Transformer architecture diagram → the encoder-decoder stack with multi-head self-attention and position-wise feedforward sub-layers.
- Figs. 10(a)-(e) (pp. 152-153): Prediction curves on ETTm2 for RNN, LSTM, GRU, Transformer and LSTM-RNN — blue is actual, red is predicted → the visual companion to the ETTm2 column of Table 1.
- Figs. 11(a)-(e) (pp. 153-154): Prediction curves on the ECL dataset for the same five models → companion to the Electricity column of Table 1.
- Figs. 12(a)-(e) (pp. 153-154): Prediction curves on the Weather dataset → visually the Transformer panel is the outlier, matching its anomalous Table 1 values.
- Figs. 13(a)-(e) (p. 154): Prediction curves on the Traffic dataset → companion to the Traffic column of Table 1.
- Table 1 (p. 155): Comparison of univariate prediction performance — MSE and MAE for five models across ETTm2, Electricity, Weather and Traffic → the paper's only results table and the entire quantitative basis of its comparison.

## Limitations and Gaps

- The authors acknowledge that deep models "rely on fewer structural assumptions, making them more challenging to interpret and often requiring larger training datasets to learn accurate models" (Sec. 4.1, p. 155).
- The authors acknowledge that traditional statistical modelling requires independent modelling of time series data in modern predictive applications, which "significantly increases labor and computational costs" (Sec. 4.1, p. 155).
- The authors acknowledge that different sample types exhibit distinct distribution patterns and therefore "a single fixed model cannot be universally applied, necessitating the use of multiple regression algorithms" (Sec. 4.1, p. 155).
- The authors state as an outlook item, not as a completed result, that real-time prediction will become possible only as computing power continues to improve (Sec. 4.2, p. 156).
- [unacknowledged] Table 1 is titled "Comparison of univariate prediction performance of four deep learning models" but lists five models (RNN, LSTM, GRU, Transformer, LSTM-RNN), and Figs. 10-13 are captioned "four models" while each contains five panels (a)-(e) (Table 1, p. 155; Figs. 10-13, pp. 152-154).
- [unacknowledged] The Abstract states the paper "conducts prediction experiments on several deep learning models using the ETT dataset," but the results in Table 1 cover ETTm2, Electricity, Weather and Traffic — four datasets, only one of which is ETT (Abstract, p. 140; Table 1, p. 155).
- [unacknowledged] ILI and TE are described at length in Sec. 2.2 (pp. 144) with their variable counts and fault types, but no result for either appears anywhere in the paper; the exclusion is justified only by the generic phrase "insufficient periodicity, seasonality, or data volume" with no diagnostic reported (Sec. 3.6, p. 151).
- [unacknowledged] No confidence interval, standard error, p-value, effect size or significance test accompanies any of the 40 MSE and MAE values in Table 1; the paper does not state how many runs produced each number (Table 1, p. 155).
- [unacknowledged] No variance, standard deviation or per-fold result is reported, so differences as small as MSE 3.418 versus 3.454 on ETTm2 cannot be assessed for stability (Table 1, p. 155).
- [unacknowledged] The Transformer's Weather values (MSE 0.827, MAE 0.341) are roughly 100 times larger than every other model's on the same dataset (MSE 0.007-0.008, MAE 0.060-0.066); the paper reports them without explanation, without flagging them as anomalous, and without excluding them from its conclusion that the Transformer performs best overall on ETTm2 (Table 1, p. 155).
- [unacknowledged] The claim that the RNN "achieved the best performance on the Weather dataset, with minimum MAE and MSE values" is only partly supported by Table 1: GRU and LSTM-RNN also report MSE 0.007 for Weather, so RNN does not hold the minimum MSE alone (Sec. 3.6, p. 155; Table 1, p. 155).
- [unacknowledged] Hyperparameters, epoch counts, learning rate, batch size, train/validation/test split proportions and random seeds are all unreported; only the optimizer, input length and prediction length are stated, so the benchmark is not reproducible (Sec. 3.6, p. 151).
- [unacknowledged] No non-deep-learning baseline is run. AR and SVM are named as the traditional alternatives in Sec. 1 (p. 141) but never appear in Table 1, so the paper's implicit claim that deep models are superior is not tested on its own data.
- [unacknowledged] The variable selected for prediction differs per dataset — the first variable for ETTm2, Electricity and Weather, the third for Traffic — and the paper does not report whether results are sensitive to that choice (Sec. 3.6, p. 151).
- [unacknowledged] Table 1's ETTm2 column contains no result for the LSTM-RNN's stated advantage in the accompanying text beyond the same MSE as GRU (3.454), so the qualitative claim of "a certain performance improvement" rests on two MAE values (1.404 versus 1.414 for LSTM) (Table 1, p. 155).
- [unacknowledged] The paper contains no household finance data, no personal financial management data, no expense or budgeting series, and no Philippine data; its only finance connection is a one-clause mention of stock price prediction and risk management in the outlook (Sec. 4.2, p. 156).
- [unacknowledged] The reference list duplicates one entry verbatim — Shaowei, P., Bo, Y., Shukai, W., et al. (2023), "Oil well production prediction based on CNN-LSTM model with self-attention mechanism," *Energy*, 284 — appearing twice (References, p. 157).
- [unacknowledged] Section numbering is inconsistent with content: Sec. 3 is titled "Time Series Prediction Model Based on Deep Learning" but Sec. 3.6 is the experimental comparison, and Secs. 4.1 and 4.2 appear as "Summary" and "Outlook" under the heading "Summary and Outlook" (Sec. 3-4, pp. 144-156).

## Definitions

- **Time Series Forecasting (TSF)** — "predicting future values and trends of data at specific points or periods by analyzing historical patterns, such as trends and seasonality" (Abstract, p. 140).
- **MSE (Mean Squared Error)** — the average squared difference between predicted and actual values, reflecting overall error between predictions and outcomes (Sec. 2.1, p. 142).
- **RMSE (Root Mean Squared Error)** — the square root of MSE, assigning higher weights to larger errors and emphasizing stability of predictions (Sec. 2.1, p. 143).
- **MAE (Mean Absolute Error)** — the mean absolute difference between predicted and actual values, reducing the influence of outliers (Sec. 2.1, p. 143).
- **MAPE (Mean Absolute Percentage Error)** — considers the relative magnitude of actual values, avoiding the cancellation effect of positive and negative errors (Sec. 2.1, p. 143).
- **SMAPE (Symmetric Mean Absolute Percentage Error)** — a modification of MAPE that avoids excessively large values when actual values are very small (Sec. 2.1, p. 143).
- **R² (Coefficient of Determination)** — also known as goodness of fit, divides explained variance by total variance to measure the proportion of variance in the dependent variable explained by the independent variables (Sec. 2.1, p. 143).
- **RNN** — a network of input layer, hidden layer and output layer where the hidden layer's output depends on both the current input and the hidden state from the previous timestep (Sec. 3.1, p. 144).
- **LSTM** — a specialized RNN architecture proposed by Hochreiter and Schmidhuber in 1997, designed to overcome gradient vanishing and exploding, with forget gate, input gate, cell state and output gate (Sec. 3.2, p. 145).
- **Forget gate** — reads the previous output h_{t−1} and current input x_t, applies a sigmoid transformation, and outputs a vector whose values from 0 to 1 decide retention or discard of cell-state information (Sec. 3.2.1, p. 145).
- **Input gate** — a sigmoid layer that determines which values will be updated to the cellular state, paired with a tanh layer that generates candidate cell states (Sec. 3.2.2, p. 146).
- **Output gate** — the gate that, with a sigmoid transformation of h_{t−1} and x_t, filters the cell state into the hidden output h_t (Sec. 3.2.3, p. 147).
- **GRU** — a simplified variant of LSTM that retains the gating mechanisms (update and reset gates) to control information flow while omitting the separate memory cell, with fewer parameters and higher computational efficiency (Sec. 3.3, p. 148).
- **Update gate** — determines how much of the previous timestep's hidden state should be retained in the current hidden state, outputting values between 0 and 1 (Sec. 3.3.1, p. 148).
- **Reset gate** — determines the extent to which the previous hidden state influences the computation of the candidate hidden state; near 0 means most previous information is ignored (Sec. 3.3.2, p. 148).
- **Bi-LSTM** — an improved LSTM combining two LSTMs, one processing the sequence forward and one backward, whose concatenated outputs provide the complete hidden representation (Sec. 3.4, p. 149).
- **Transformer** — a deep learning architecture first proposed by Vaswani et al. in 2017, employing a self-attention-based encoder-decoder structure and excelling at long-range dependencies and parallel computation (Sec. 3.5, p. 150).
- **Self-attention** — the core concept of the Transformer; it considers all positions in the input sequence simultaneously and assigns varying attention weights to different parts of the input to capture semantic relationships (Sec. 3.5.1, p. 150).
- **Multi-head attention** — combining multiple scaled dot-product attention mechanisms in parallel to integrate information from different attention heads (Sec. 3.5.2, p. 151).
- **Positional encoding** — sine and cosine functions at different frequencies added to input embeddings so the model can capture relative or absolute token position despite not relying on recursion or convolution (Sec. 3.5.3, p. 151).
- **ETT** — the dataset provided by the State Grid Corporation of China, minute-level transformer oil temperatures from two counties in one province, 2016-2018, split into ETTm1, ETTm2, ETTh1 and ETTh2 (Sec. 2.2.1, p. 143).
- **ECL (Electricity Consuming Load)** — electricity consumption load dataset from 2012-2014 (Sec. 2.2.2, p. 143).
- **Traffic** — dataset from California's Department of Transportation, 2015-2016 (Sec. 2.2.3, p. 144).
- **Weather** — 21 meteorological indicators including air pressure, temperature and humidity, collected every 10 minutes from 2020 to 2021 by the Max Planck Institute for Biogeochemistry meteorological station (Sec. 2.2.4, p. 144).
- **ILI** — influenza dataset from the US Centers for Disease Control and Prevention, the weekly ratio of influenza-like-illness patients to total patients, 2002-2021 (Sec. 2.2.5, p. 144).
- **TE (Tennessee Eastman)** — a representative chemical process consisting of a gas-liquid separator, circulating compressor, stripper, condenser and reactor, simulating 21 fault types across 6 categories with 53 observed variables (Sec. 2.2.6, p. 144).

## Key Equations

- `MSE(y, ŷ) = (1/n) Σ (y_i − ŷ_i)²` — Eq. 1, p. 142.
- `RMSE(y, ŷ) = √((1/n) Σ (y_i − ŷ_i)²)` — Eq. 2, p. 143.
- `MAE(y, ŷ) = (1/n) Σ |y_i − ŷ_i|` — Eq. 3, p. 143.
- `MAPE(y, ŷ) = (100%/n) Σ |y_i − ŷ_i| / |y_i|` — Eq. 4, p. 143.
- `SMAPE(y, ŷ) = (100%/n) Σ |y_i − ŷ_i| / ((|y_i| + |ŷ_i|)/2)` — Eq. 5, p. 143.
- `R²(y, ŷ) = 1 − (Σ(y_i − ŷ_i)²) / (Σ(y_i − ȳ)²)` — Eq. 6, p. 143.
- `h_t = f₁(U x_t + W h_{t−1} + b)` — RNN hidden state, Eq. 7, p. 144.
- `o_t = f₂(V h_t + c)` — RNN output, Eq. 8, p. 144.
- `f_t = σ(W_f [h_{t−1}, x_t] + b_f)` — LSTM forget gate, Eq. 9, p. 146.
- `i_t = σ(W_i [h_{t−1}, x_t] + b_i)` — LSTM input gate, Eq. 10, p. 147.
- `C̃_t = tanh(W_c [h_{t−1}, x_t] + b_c)` — candidate cell state, Eq. 11, p. 147.
- `o_t = σ(W_0 [h_{t−1}, x_t] + b_0)` — LSTM output gate, Eq. 12, p. 147.
- `h_t = o_t * tanh(C_t)` — LSTM hidden output, Eq. 13, p. 148.
- `z_t = σ(W_z [h_{t−1}, x_t] + b_z)` — GRU update gate, Eq. 14, p. 148.
- `r_t = σ(W_r [h_{t−1}, x_t] + b_r)` — GRU reset gate, Eq. 15, p. 148.
- `h̃_t = tanh(W[r_t h_{t−1}, x_t] + b)` — GRU candidate hidden state, Eq. 16, p. 149.
- `h_t = (1 − z_t) * h_{t−1} + z_t * h̃_t` — GRU current hidden state, Eq. 17, p. 149.
- `h_t = h_t^f ⊕ h_t^b` — Bi-LSTM combined output, Eq. 18, p. 149.
- `Attention(Q, K, V) = softmax(QK^T / √d_k) V` — scaled dot-product self-attention, Eq. 19, p. 150.
- `PE(t)_i = sin(t / 10000^{2k/d}) for i = 2k; cos(t / 10000^{2k/d}) for i = 2k+1` — sinusoidal positional encoding, Eq. 20, p. 151.

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ETTm2 univariate forecasting, RNN model | MSE | 3.459 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, RNN model | MAE | 1.404 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, LSTM model | MSE | 3.480 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, LSTM model | MAE | 1.414 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, GRU model | MSE | 3.454 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, GRU model | MAE | 1.402 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, Transformer model | MSE | 3.418 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, Transformer model | MAE | 1.399 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, LSTM-RNN model | MSE | 3.454 | — | — | Table 1, p. 155 |
| ETTm2 univariate forecasting, LSTM-RNN model | MAE | 1.404 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, RNN model | MSE | 21.603 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, RNN model | MAE | 2.014 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, LSTM model | MSE | 19.821 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, LSTM model | MAE | 1.848 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, GRU model | MSE | 19.524 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, GRU model | MAE | 1.889 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, Transformer model | MSE | 19.541 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, Transformer model | MAE | 2.025 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, LSTM-RNN model | MSE | 21.583 | — | — | Table 1, p. 155 |
| Electricity univariate forecasting, LSTM-RNN model | MAE | 1.941 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, RNN model | MSE | 0.007 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, RNN model | MAE | 0.060 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, LSTM model | MSE | 0.008 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, LSTM model | MAE | 0.066 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, GRU model | MSE | 0.007 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, GRU model | MAE | 0.062 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, Transformer model | MSE | 0.827 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, Transformer model | MAE | 0.341 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, LSTM-RNN model | MSE | 0.007 | — | — | Table 1, p. 155 |
| Weather univariate forecasting, LSTM-RNN model | MAE | 0.062 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, RNN model | MSE | 0.00112 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, RNN model | MAE | 0.021 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, LSTM model | MSE | 0.00120 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, LSTM model | MAE | 0.020 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, GRU model | MSE | 0.00110 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, GRU model | MAE | 0.021 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, Transformer model | MSE | 0.00122 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, Transformer model | MAE | 0.021 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, LSTM-RNN model | MSE | 0.00125 | — | — | Table 1, p. 155 |
| Traffic univariate forecasting, LSTM-RNN model | MAE | 0.021 | — | — | Table 1, p. 155 |
| ETT dataset size | data points | 1,051,200 | — | — | Sec. 2.2.1, p. 143 |
| ETT subset size at 15-minute and 1-hour sampling intervals | data points | 69,680 and 17,420 | — | — | Sec. 2.2.1, p. 143 |
| ETT per-datapoint feature count | features | seven | — | — | Sec. 2.2.1, p. 143 |
| TE chemical process observed variables | variables | 53 | — | — | Sec. 2.2.6, p. 144 |
| TE chemical process measured variables | variables | 41 | — | — | Sec. 2.2.6, p. 144 |
| TE chemical process manipulated variables | variables | 12 | — | — | Sec. 2.2.6, p. 144 |
| TE simulated fault types | fault types | 21 | — | — | Sec. 2.2.6, p. 144 |
| TE fault categories | fault types | 6 | — | — | Sec. 2.2.6, p. 144 |
| Weather dataset meteorological indicators | indicators | 21 | — | — | Sec. 2.2.4, p. 144 |
| Model input sequence length used in all experiments | timesteps | 24 | — | — | Sec. 3.6, p. 151 |
| Model prediction length used in all experiments | timesteps | 1 | — | — | Sec. 3.6, p. 151 |
| Number of datasets used in the comparative experiment | datasets | 4 | — | — | Sec. 3.6, p. 151 |
| Number of models compared in Table 1 | models | 5 | — | — | Table 1, p. 155 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Time Series Forecasting (TSF) involves predicting future values and trends of data at specific points or periods by analyzing historical patterns, such as trends and seasonality." | Abstract, p. 140 | model_development |
| "With the advent of IoT sensors, traditional machine learning approaches struggle to handle massive time series datasets." | Abstract, p. 140 | model_development |
| "Recently, deep learning algorithms, exemplified by convolutional neural networks (CNNs), recurrent neural networks (RNNs), and Transformer models, have made significant progress in time series forecasting tasks." | Abstract, p. 140 | model_development |
| "This paper reviews the common features of time series data, relevant datasets, and evaluation metrics for models." | Abstract, p. 140 | data_collection |
| "This paper conducts prediction experiments on several deep learning models using the ETT dataset and presents the final results." | Abstract, p. 140 | data_collection |
| "Evaluation metrics are tools used to assess and analyze the performance of time series forecasting models, serving as key criteria for measuring model performance." | Sec. 2.1, p. 142 | model_performance_evaluation |
| "Except for R², all the evaluation metrics mentioned above are better when their values are smaller." | Sec. 2.1, p. 143 | model_performance_evaluation |
| "The ETT dataset, provided by the State Grid Corporation of China, consists of minute-level recordings of transformer oil temperatures from two counties in the same province during 2016–2018." | Sec. 2.2.1, p. 143 | data_collection |
| "Each dataset contains 1,051,200 data points." | Sec. 2.2.1, p. 143 | data_collection |
| "Although RNNs are effective for processing sequential data, they suffer from issues like vanishing and exploding gradients." | Sec. 3.1, p. 144 | model_development |
| "GRU is a simplified variant of LSTM that retains the gating mechanisms (update and reset gates) to control the flow of information while omitting the separate memory cell." | Sec. 3.3, p. 148 | model_development |
| "This study conducted experiments using the ETTm2, Electricity, Traffic, and Weather datasets. Other datasets were excluded due to insufficient periodicity, seasonality, or data volume." | Sec. 3.6, p. 151 | data_collection |
| "To ensure consistency, all models used an input sequence length of 24 and a prediction length of 1." | Sec. 3.6, p. 151 | model_development |
| "All models were trained using the Adam optimizer, with MSE (Mean Squared Error) and MAE (Mean Absolute Error) as evaluation metrics. PyTorch was used for implementation." | Sec. 3.6, p. 151 | model_performance_evaluation |
| "the Transformer model achieved the best performance on the ETTm2 dataset, with minimum MAE and MSE values" | Sec. 3.6, p. 155 | model_performance_evaluation |
| "The LSTM model achieved the minimum MAE on the Electricity and Traffic datasets, i.e. the minimum tie error." | Sec. 3.6, p. 155 | model_performance_evaluation |
| "The GRU model achieved the minimum mean square error (MSE) on the Electricity and Traffic datasets." | Sec. 3.6, p. 155 | model_performance_evaluation |
| "The RNN model achieved the best performance on the Weather dataset, with minimum MAE and MSE values." | Sec. 3.6, p. 155 | model_performance_evaluation |
| "The LSTM-RNN model generally outperforms the standard RNN and also shows better results than the ordinary LSTM model on the ETTm2 and Weather datasets." | Sec. 3.6, p. 155 | model_algorithm_integration |
| "Additionally, since different sample types exhibit distinct distribution patterns, a single fixed model cannot be universally applied, necessitating the use of multiple regression algorithms." | Sec. 4.1, p. 155 | model_performance_evaluation |
| "However, these models rely on fewer structural assumptions, making them more challenging to interpret and often requiring larger training datasets to learn accurate models." | Sec. 4.1, p. 155 | model_development |
| "This paper presents a systematic review of time series forecasting methods based on deep learning." | Sec. 5, p. 156 | model_development |

## Remember This

- The paper is a review article, not a system paper: it surveys RNN, LSTM, GRU, Bi-LSTM and Transformer architectures and runs one comparative benchmark.
- The benchmark compares five models (RNN, LSTM, GRU, Transformer, LSTM-RNN) on four datasets (ETTm2, Electricity, Weather, Traffic) with input length 24, prediction length 1, Adam optimizer and PyTorch.
- Table 1 (p. 155) is the only results table; it reports MSE and MAE for every model-dataset combination, with no CI and no p-value anywhere.
- The Transformer wins ETTm2 (MSE 3.418, MAE 1.399); LSTM wins MAE on Electricity and Traffic; GRU wins MSE on Electricity and Traffic; RNN is credited with the best Weather result.
- The Transformer's Weather values (MSE 0.827, MAE 0.341) are two orders of magnitude worse than every other model's and are reported without explanation.
- Table 1's caption says "four deep learning models" but five are listed, and Figs. 10-13 are captioned "four models" while showing five panels each.
- The Abstract says the experiments use "the ETT dataset" but results cover four datasets, and ILI and TE are described but never evaluated.
- The paper reports no train/test split, no hyperparameters beyond optimizer and sequence length, no seed and no repeated runs, so nothing in Table 1 is reproducible from the text.
- Relevance to personal financial management is indirect: it supplies architecture and metric vocabulary for forecasting, not household finance findings.

## Cited Works

- Vaswani, A., Shazeer, N., Parmar, N., et al. (2017) (methodology) — "Attention is all you need," the origin of the Transformer and self-attention architecture. [p. 150, p. 157]
- Hochreiter and Schmidhuber (1997) (methodology) — credited as the proposers of LSTM, designed to overcome gradient vanishing and exploding in long sequences. [p. 145]
- Elman, J. (1990) (methodology) — introduced the foundational concept and structure of RNNs and the hidden state in "Finding Structure in Time." [p. 141]
- Wu, H. X., Xu, J. H., Wang, J. M., et al. (2021) (methodology) — Autoformer, a self-correlation decomposition Transformer for long-term forecasting that integrates time series decomposition into the Transformer. [p. 142, p. 157]
- Liu, Y., Wu, H. X., Wang, J. M., et al. (2022) (methodology) — Non-stationary Transformers, a de-stationary framework addressing over-stabilization when processing raw time series. [p. 142, p. 156]
- Liu, Y., Hu, T., Zhang, H., et al. (2024) (methodology) — ITransformer, an inverted input approach reassigning roles between the attention module and the feedforward network. [p. 142, p. 156]
- Zhang, Y. F., Wu, R., Dascalu, S. M., et al. (2024) (methodology) — MTPNet, a multi-scale pyramid Transformer addressing time-dependent modelling at fixed or constrained scales. [p. 142, p. 157]
- Jin, K. H., Wi, J. A., Lee, E. J., et al. (2021) (context) — TrafficBERT, a pre-trained model with large-scale data for long-range traffic flow forecasting. [p. 142, p. 156]
- Li, S. Y., Jin, X. Y., Xuan, Y., et al. (2019) (methodology) — LogSparse Transformer replacing traditional position encodings with learnable position embeddings. [p. 142, p. 156]
- Wen, Q. S., Zhou, T., Zhang, C. L., et al. (2023) (context) — "Transformers in time series: A survey," cited for the Transformer's self-attention advantages on time series. [p. 142, p. 157]
- Abdel-Nasser, M., & Mahmoud, K. (2019) (context) — deep LSTM-RNN photovoltaic power forecasting, cited as a smart-grid planning tool. [p. 142, p. 156]
- Qiang, C., Shu, W., Qiang, L., et al. (2020) (methodology) — MV-RNN, a Multi-View Recurrent Neural Network for sequential recommendation and cold-start mitigation. [p. 142, p. 157]
- Shaowei, P., Bo, Y., Shukai, W., et al. (2023) (methodology) — a CNN-LSTM-SA hybrid model for oil well production prediction; listed twice in the reference list. [p. 142, p. 157]
- Hanen, B., Ali, A. B., & Riadh, I. F. (2024) (context) — a Bi-GRU encoder-decoder framework for multivariate time series forecasting, cited alongside STAN. [p. 142, p. 156]
- Fang, W., Chen, Y., et al. (2021) (context) — a survey of RNN-based spatio-temporal sequence prediction algorithms, cited for speech recognition adoption. [p. 142, p. 156]
- Waqas, M., & Humphries, W. U. (2024) (context) — a critical review of RNN and LSTM variants in hydrological time series prediction. [p. 142, p. 157]
- Michael, E. N., Bansal, C. R., Ismail, A. A. A., et al. (2024) (context) — a BiLSTM-GRU structure for predicting hourly solar radiation, cited for Facebook's VIN use of bidirectional LSTM. [p. 141, p. 156]
- Gers, F. A., Schmidhuber, J., & Cummin, S. F. (2000) (context) — "Learning to forget: Continual prediction with LSTM," cited for the manual configuration burden of traditional statistical models. [p. 141, p. 156]
- Durbin, J., & Koopman, S. J. (2012) (context) — "Time series analysis by state space methods," cited alongside Gers et al. for AR/SVM limitations. [p. 141, p. 156]
- Eslin, G. P., & Agon, C. (2012) (context) — "Time-series data mining," cited for the breadth of application domains for time series analysis. [p. 141, p. 156]