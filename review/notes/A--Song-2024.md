---
paper_id: A--Song-2024
first_author: Song
year: 2024
title: "Deep learning-based time series forecasting"
venue: "Artificial Intelligence Review"
doi: 10.1007/s10462-024-10989-8
designation: algorithm
status: extracted
modules: [model_algorithm_integration, model_performance_evaluation]
module_rationale:
  model_algorithm_integration: "The paper reviews how forecasting models integrate decomposition modules (trend, seasonal, multi-scale, non-stationary) with attention and recurrent architectures, e.g., Autoformer's Auto-Correction module (Sect. 3.1.2, p. 14) and Scaleformer's multi-scale iterative framework (Fig. 10, p. 18)."
  model_performance_evaluation: "Sect. 6 evaluates model performance across five datasets with MAE, MSE, MAPE, and R2 metrics (Tables 5-14, pp. 36-60)."
---

## Summary

This paper is a comprehensive systematic review of deep learning-based time series forecasting models published between 2014 and 2024. It examines the processing logic of forecasting models from two primary perspectives: mining correlations among time steps and mining correlations among variables. The review covers holistic mining approaches (autoencoders, CNNs, TCNs, RNNs, LSTMs, GRUs, Transformers) and targeted information mining approaches that extract trend, seasonal, multi-scale, and non-stationary information through decomposition techniques. It also surveys strategies for reducing the computational cost of attention mechanisms in long-term forecasting, including shortening the input sequence length (Informer, PatchTST, Pyraformer, Triformer) and sparsifying attention (LogTrans, Reformer, Informer, Crossformer). The paper summarizes loss functions used in time series forecasting, distinguishing single-objective loss functions (MAE, MSE, quantile loss) from hybrid loss functions (negative log-likelihood, generative adversarial loss). An extensive experimental section evaluates the reviewed models on multivariate and univariate time series prediction tasks across five datasets from four domains (energy, exchange rate, traffic, disease). Key findings include that DLinear, a simple linear model, achieves competitive or superior accuracy compared to complex models; that complex models often suffer from overfitting and noise interference, as demonstrated by input shuffling and lookback window extension experiments; that simple methods (mean filtering, linear layers) effectively extract trend information while frequency domain methods effectively extract seasonal information; and that patch slicing significantly improves attention efficiency for long-term forecasting. The paper concludes with future research directions including mining time-step dependencies, mining variable relationships, complexity optimization, overfitting mitigation, flexible prediction models, non-stationarity handling, and probabilistic forecasting.

## Problem and Motivation

Time series forecasting is critical for energy consumption, transportation planning, and weather forecasting. Traditional statistical models like ARIMA rely on linear assumptions and struggle with nonlinear correlations in real-world data. Deep learning models have become increasingly important, but their development has been rapid and fragmented across multiple research directions. Existing reviews typically focus on a single model family or a narrow set of applications. This paper aims to provide a comprehensive evaluation of mainstream deep learning forecasting models from multiple perspectives — time-step dependencies, variable correlations, receptive field expansion versus computational cost, and loss functions — and to identify future research directions through systematic experimentation. The authors note that "Fully exploiting these two types of information plays a crucial role in improving the model's capability" (Sect. 1.2, p. 2), referring to time-step dependencies and correlations between temporal variables.

## Method

**Design.** Systematic literature review with comparative benchmark experiments; the authors state no formal design label.

**Sample.** The review covers models published from 2014 to 2024; the experiments evaluate 20+ models on 5 time series datasets (ETTh1, ETTh2, ETTm1, ETTm2, Electricity, Exchange, Traffic, ILI) with input length L=96 (L=36 for ILI) and output lengths O=48, 96, 336 (O=12, 24, 48 for ILI). All experimental results are averaged over five trials with batch size 16.

**Context.** geography: The datasets originate from China (ETT, power transformers), the United States (ILI, influenza patients), California (Traffic, freeway sensors), and international currency markets (Exchange); population: Not applicable — the unit of analysis is time series observations, not human participants; setting: Virtual/computational — offline experiments on real-world time series datasets; no human participants or field deployment.

The review organizes models by their processing logic. For time-step dependencies, it covers holistic mining (Autoencoders, DLinear, CNNs, TCNs, RNNs, LSTMs, GRUs, Transformers) and targeted information mining (trend, seasonal, multi-scale, non-stationary). For variable correlations, it covers TFT's Variable Selection Network, Aliformer's AliAttention, and Crossformer's DAttention. For complexity optimization, it covers sequence-shortening methods (Informer, PatchTST, Pyraformer, Triformer) and attention-sparsifying methods (LogTrans, Reformer, Informer, Crossformer). For loss functions, it covers single-objective (MAE, MSE, quantile loss) and hybrid (negative log-likelihood, GAN-based) approaches.

The experimental section compares model prediction accuracy (Sect. 6.4.1), investigates limitations through input shuffling and lookback window extension (Sect. 6.4.2), assesses trend and season information mining capability on an artificial dataset (Sect. 6.4.3), and evaluates attention modules for Transformer-based models (Sect. 6.4.4).

## Software

- The paper reports no software implementation for the review itself.
- Models were trained and evaluated using code available at https://github.com/TCCofWANG/Deep-Learning-based-Time-Series-Forecasting (Abstract, p. 1).
- Hyperparameters for all deep learning models were set according to optimal configurations in their respective papers or source code (Sect. 6.4.1, p. 48).
- Experiments used batch size 16 for main experiments (Sect. 6.4.1, p. 48) and batch size 8 for attention module comparisons (Sect. 6.4.4, p. 52).
- For univariate prediction, ARIMA served as the baseline; for multivariate prediction, VAR served as the baseline (Sect. 6.4.1, p. 48).
- Simple time split validation was used for all datasets except Exchange, where sliding window validation with window size one-tenth of dataset length was applied (Sect. 6.4.1, p. 48).

## Key Findings

- DLinear, a simple linear layer model, achieves competitive or superior accuracy compared to complex models across the vast majority of datasets. On ETTh1 with prediction length 336, DLinear outperforms PatchTST in MAE by 3.13% and Fedformer in MAPE by 2.24%, and improves R2 by 14.87% compared to PatchTST (Sect. 6.4.1, p. 48).
- Crossformer, which captures variable correlations, shows a distinct accuracy advantage on the Electricity dataset (321 variables), improving MSE by 10.93% and MAPE by 17.70% over NS-Transformer for prediction length 48 (Sect. 6.4.1, p. 48).
- PatchTST demonstrates suitability for datasets with pronounced long-term periodicity and trends, improving MSE by 27.30% and R2 by 17.49% over NS-Transformer on the ILI dataset for prediction length 48 (Sect. 6.4.1, p. 49).
- NS-Transformer performs better in univariate than multivariate settings; on ILI long-term prediction, it improves MAE by 9.54%, MSE by 25.32%, and R2 by 46.47% over PatchTST (Sect. 6.4.1, p. 49).
- In input shuffling experiments, PatchTST shows the most notable decline in prediction accuracy after shuffling across ETTh1, ILI, and Exchange datasets, while complex models like Autoformer, TDformer, and others show minimal impact or even slight improvements (Sect. 6.4.2, p. 50).
- In lookback window extension experiments, complex models including ETSformer, TDformer, and Autoformer achieve highest accuracy only with the shortest input and decline as input lengthens; PatchTST is the only model with optimal accuracy for the longest input on both datasets (Sect. 6.4.2, p. 51).
- On the artificial dataset, Fedformer achieves the best trend term prediction, improving MAE by 3.14% and MSE by 6.18% over TDformer, and 26.24% and 48.43% over DLinear (Sect. 6.4.3, p. 51).
- For season term prediction, Fedformer improves MAE by 26.65% and MSE by 43.07% over TDformer, and 29.17% in MAE and 44.17% in MSE over ETSformer (Sect. 6.4.3, p. 52).
- Patch Attention in PatchTST significantly improves prediction capability, with 17.95% and 30.06% improvements in MAE and MSE on ETTh1, and 85.27% improvement in MSE on Exchange compared to vanilla Attention (Sect. 6.4.4, p. 53).
- Reformer demonstrates superior prediction performance with low time complexity, reducing test time by 10.14% compared to LogTrans, and improving MAE by 14.03% and MSE by 18.42% on ETTh1 (Sect. 6.4.4, p. 53).
- PatchTST exhibits memory occupation 10.93% lower than LogTrans for prediction length 336, with MAE improvement of 28.83% and MSE improvement of 42.09% (Sect. 6.4.4, p. 53).
- Pyraformer exhibits memory occupation 3.00% lower than LogTrans for prediction length 336, with MAE improvement of 4.10% and MSE improvement of 4.27% (Sect. 6.4.4, p. 54).

## Key Figures and Tables

- Fig. 1 (p. 2): Process of time series forecasting — historical sequence Xt−L:t is mapped to future sequence Xt:t+O by model φ(·).
- Fig. 2 (p. 8): Dilated causal convolution — dilating the convolution kernel expands the receptive field without increasing kernel size.
- Fig. 3 (p. 8): Structure of LSTM — input gate, forget gate, output gate, and cell state regulate information flow.
- Fig. 4 (p. 10): Structure of Transformer — encoder-decoder architecture with self-attention mechanism.
- Fig. 5 (p. 11): Patch slice — input time series segmented into fixed-length patches using sliding window.
- Fig. 6 (p. 14): Recurrent-skip network — connections between t-th and (t−p)-th time steps capture seasonal information.
- Fig. 7 (p. 15): Auto-Correction in Autoformer — time-delay similarity used to weight and aggregate delayed sequences.
- Fig. 8 (p. 15): FEA in Fedformer — Fourier transform, frequency component selection, attention, inverse Fourier transform.
- Fig. 9 (p. 17): Season Stack in N-BEATS — Fourier period coding and Fourier series for seasonal term prediction.
- Fig. 10 (p. 18): Structure of Scaleformer — multi-scale iterative framework with downsampling and upsampling.
- Fig. 11 (p. 19): Pyramid structure in Pyraformer — different layers represent different time scales.
- Fig. 12 (p. 19): Triformer — node size indicates granularity of time scale.
- Fig. 13 (p. 20): VSN structure in TFT and GRN module.
- Fig. 14 (p. 20): AliAttention in Aliformer — fusion of attention graphs from different variables.
- Fig. 15 (p. 21): LogSparse Self-Attention — connecting lines indicate similarity computation requirements.
- Fig. 16 (p. 21): LSH Attention — different colors indicate different hash groups.
- Fig. 17 (p. 35): Validation split of datasets — simple time split and sliding window validation.
- Fig. 18 (p. 46): Prediction results for trend term on artificial dataset.
- Fig. 19 (p. 46): Prediction results for season term on artificial dataset.
- Fig. 20 (p. 54): Inference time — vertical axis represents inference time for whole test dataset.
- Fig. 21 (p. 54): Maximum memory occupation during training — horizontal axis represents prediction length.
- Table 1 (p. 10): Deep learning time series prediction models using time series decomposition.
- Table 2 (p. 20): Space complexity of different Attention modules.
- Table 3 (p. 21): Commonly used time series datasets.
- Table 4 (p. 34): Summary of all models in experimental section.
- Table 5 (pp. 36-39): Partial results of multivariate time series forecasting experiment.
- Table 6 (pp. 40-43): Partial results of univariate time series forecasting experiment.
- Table 7 (p. 44): Comparison of prediction results before and after shuffling input sequence.
- Table 8 (p. 45): Prediction results across different lookback window lengths.
- Table 9 (p. 46): Prediction of trend and season terms on artificial dataset.
- Table 10 (p. 47): Comparison of prediction results among different Attention modules.
- Table 11 (p. 47): Time series prediction results of models based on Attention.
- Table 12 (p. 47): Maximum memory occupation in MB during training.
- Table 13 (pp. 57-58): Multivariate time series forecasting results (complete).
- Table 14 (pp. 59-60): Univariate time series forecasting results (complete).

## Limitations and Gaps

- The authors acknowledge that existing complex models have limited proficiency in effectively capturing the sequential order of time series, as demonstrated by input shuffling experiments where complex models show minimal accuracy decline (Sect. 6.4.2, p. 50).
- The authors acknowledge that complex models suffer from overfitting and noise interference, as demonstrated by lookback window extension experiments where accuracy declines with longer inputs (Sect. 6.4.2, p. 51).
- The authors acknowledge that attention mechanisms optimized for complexity often face information loss, potentially impacting prediction performance (Sect. 7, p. 55).
- The authors note that current models are constrained by fixed input and output sequence lengths, requiring redesign and retraining if prediction length or position changes (Sect. 7, p. 56).
- The authors state that research on modeling changes in statistical properties of time series is still in its early stages (Sect. 7, p. 56).
- [unacknowledged] The review covers only models published between 2014 and 2024; earlier foundational work is excluded by design.
- [unacknowledged] The experiments use a single random seed configuration per model (though results are averaged over five trials), and no per-fold variance or confidence intervals are reported for the main comparison tables.
- [unacknowledged] The artificial dataset experiment uses a single set of parameter values (β0 = −0.2, β1 = L, A1 = A2 = 0.15, f1 = 1/10, f2 = 1/13), so generalizability of trend/season findings to other generating processes is untested.
- [unacknowledged] The ILI dataset is very small (966 samples, 7 features), and the paper does not discuss how this affects statistical power or result stability.
- [unacknowledged] The paper reports no statistical significance tests for the main comparison tables (Tables 5 and 6), so whether observed differences between models are reliable is unclear.
- [unacknowledged] The attention module comparison (Table 10) adjusts hidden layer dimensions to equalize space complexity, which may artificially disadvantage modules whose architecture assumes larger hidden dimensions (FA, DAttention).
- [unacknowledged] No ablation study isolates the contribution of individual components (e.g., decomposition, attention, normalization) within each model.

## Definitions

- **Time-step dependencies** — The interrelations among time step vectors xt ∈ RD within a time series.
- **Correlations among variables** — The relationships between different univariate time series vi⊤ ∈ RL within a multivariate time series.
- **Trend information** — The discernible persistence and regularity of fluctuations between consecutive time steps within a defined scope.
- **Seasonal information** — Periodic behavior within the data, indicating correlations between time steps separated by fixed intervals.
- **Multi-scale information** — Temporal dependencies of a time series at different scales (e.g., hourly, daily, weekly, monthly).
- **Non-stationary information** — Variations in the statistical characteristics of a time series over time, typically manifested through shifts in mean and standard deviation.
- **Dilated causal convolution (DCC)** — Convolution with gaps in the kernel that expands the receptive field without increasing kernel size, with temporal causality ensuring output at time t depends only on inputs up to t.
- **Auto-Correction** — Autoformer's module that assesses time-delay similarity among input sequences to characterize periodicity.
- **FEA (Frequency Enhanced Attention)** — Fedformer's module that applies attention to frequency components after Fourier transform.
- **ESA (Exponential Smoothing Attention)** — ETSformer's module integrating exponential weighted averaging into attention.
- **PAM (Pyramidal Attention Module)** — Pyraformer's module that computes attention within neighboring nodes across pyramid layers.
- **RevIN** — Reversible Instance Normalization, a method that normalizes input sequences and denormalizes predictions to handle distribution shift.
- **VSN (Variable Selection Network)** — TFT's module that filters variables using GRN and weighted averaging.
- **DAttention** — Crossformer's module applying attention directly to variables by transposing input dimensions.
- **ProbSparse Self-Attention** — Informer's mechanism that selectively retains Top-U query vectors based on a scoring function.
- **LSH Attention** — Reformer's mechanism that maps time steps into a hash space and computes attention only within hash groups.

## Key Equations

- `it = σ(Wxixt + Whiht−1 + bi)` — LSTM input gate (Eq. 1, p. 9).
- `ft = σ(Wxfxt + Whfht−1 + bf)` — LSTM forget gate (Eq. 1, p. 9).
- `ct = ft ⊙ ct−1 + it ⊙ ~ct` — LSTM cell state update (Eq. 3, p. 9).
- `ht = ot ⊙ tanh(ct)` — LSTM hidden state output (Eq. 3, p. 9).
- `Q = WQ⊤X, K = WK⊤X, V = WV⊤X` — Transformer query, key, value projections (Eq. 4, p. 9).
- `A = Q⊤K, O = V Softmax(A/√Dk)` — Scaled dot-product attention (Eq. 5, p. 9).
- `yt = Σi=0^{k−1} Wi xt−k+i + b` — LSTnet trend term prediction (Eq. 6, p. 12).
- `θ = XW + B, XT = Σi=0^h θi ti` — N-BEATS Trend Stack polynomial fitting (Eq. 7, p. 12).
- `Ôt = αOt + (1−α)Ôt−1` — ETSformer exponential smoothing attention (Eq. 8, p. 13).
- `Xp = Patch(X), Qp = XpWQ + bQ` — PatchTST patch embedding (Eq. 9, p. 13).
- `Ap = Qp Kp⊤, Op = Vp Softmax(Ap/√Dk)` — PatchTST attention (Eq. 10, p. 13).
- `RX(τ) = lim_{L→∞} (1/L) Σ_{t=1}^L xt xt−τ` — Autoformer auto-correlation (Eq. 11, p. 14).
- `Auto-Correlation(X) = Σ_{i=1}^k Roll(X, τi) R̂X(τi)` — Autoformer auto-correlation aggregation (Eq. 13, p. 15).
- `Õ = Atten(Q̃, K̃, Ṽ), YS = F−1(Padding(Õ))` — Fedformer FEA processing (Eq. 15, p. 16).
- `YS = Σ_{i=0}^{⌊h/2+1⌋} θi cos(2πitt) + θi+⌊h/2⌋ sin(2πitt)` — N-BEATS season term prediction (Eq. 17, p. 17).
- `μi = (1/(n+m))(Σ_{t=1}^m Pi,t + Σ_{t=1}^n Ui,t)` — Scaleformer cross-scale normalization (Eq. 18, p. 18).
- `y = Σ_{i∈N(s)l} exp(qki⊤/√dK) vi / Σ_{i∈N(s)l} exp(qki⊤/√dK)` — Pyraformer PAM attention (Eq. 23, p. 22).
- `m = (1/L) Σ_{j=1}^L Xj, v = (1/L) Σ_{j=1}^L (Xj − m)²` — RevIN mean and variance (Eq. 25, p. 23).
- `X̂ = γ((X − m)/√(v + ε)) + β` — RevIN normalization (Eq. 25, p. 23).
- `Ŷ = √(v + ε)((Y − β)/γ) + m` — RevIN denormalization (Eq. 26, p. 23).
- `Â = v Q̂⊤ K̂ + 1m⊤K̂` — NS-Transformer De-stationary Attention (Eq. 27, p. 23).
- `log τ = MLP(v, X), Δ = MLP(m, X)` — NS-Transformer non-stationary information learning (Eq. 28, p. 24).
- `MAE(Y, Ŷ) = (1/(O×D)) Σ_{i=1}^O Σ_{j=1}^D |yi,j − ŷi,j|` — Mean Absolute Error (Eq. 41, p. 29).
- `MSE(Y, Ŷ) = (1/(O×D)) Σ_{i=1}^O Σ_{j=1}^D (yi,j − ŷi,j)²` — Mean Squared Error (Eq. 42, p. 29).
- `L = q ∗ max(0, Y − Ŷ) + (1−q) ∗ max(0, Ŷ − Y)` — Quantile loss (Eq. 43, p. 30).
- `θ* = argmin_θ Σ_{i=1}^O −log P(yi|θ)` — Negative log-likelihood (Eq. 44, p. 31).
- `min_G max_D V(D,G) = Ex∼pdata(x)[log D(x)] + Ez∼pz(z)[log(1−D(G(z)))]` — GAN loss (Eq. 45, p. 31).
- `GeneratorLoss = Pρ(YO, Ŷ) + λE[log(1−D(Yfake))]` — AST generator loss (Eq. 47, p. 32).
- `DiscriminatorLoss = E[−log D(Yreal) − log(1−D(Yfake))]` — AST discriminator loss (Eq. 48, p. 32).

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Multivariate forecasting, Fedformer, ETTh1, Short | MAE | 0.4566 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ETTh1, Short | MSE | 0.4189 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ETTh1, Short | MAPE | 68.28% | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ETTh1, Short | R2 | 0.4847 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, Exchange, Short | MAE | 0.1629 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, Exchange, Short | MSE | 0.0509 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, Exchange, Short | MAPE | 2.22% | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, Exchange, Short | R2 | 0.7904 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ILI, Short | MAE | 0.6483 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ILI, Short | MSE | 0.9915 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ILI, Short | MAPE | 45.38% | — | — | Table 5, p. 36 |
| Multivariate forecasting, Fedformer, ILI, Short | R2 | 0.4547 | — | — | Table 5, p. 36 |
| Multivariate forecasting, ETSformer, ETTh1, Short | MAE | 0.5026 | — | — | Table 5, p. 36 |
| Multivariate forecasting, ETSformer, ETTh1, Short | MSE | 0.5423 | — | — | Table 5, p. 36 |
| Multivariate forecasting, ETSformer, ETTh1, Short | MAPE | 68.63% | — | — | Table 5, p. 36 |
| Multivariate forecasting, ETSformer, ETTh1, Short | R2 | 0.4134 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Crossformer, ETTh1, Short | MAE | 0.4132 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Crossformer, ETTh1, Short | MSE | 0.3788 | — | — | Table 5, p. 36 |
| Multivariate forecasting, Crossformer, ETTh1, Short | MAPE | 62.44% | — | — | Table 5, p. 36 |
| Multivariate forecasting, Crossformer, ETTh1, Short | R2 | 0.5584 | — | — | Table 5, p. 36 |
| Multivariate forecasting, DLinear, ETTh1, Short | MAE | 0.3979 | — | — | Table 5, p. 36 |
| Multivariate forecasting, DLinear, ETTh1, Short | MSE | 0.3663 | — | — | Table 5, p. 36 |
| Multivariate forecasting, DLinear, ETTh1, Short | MAPE | 66.14% | — | — | Table 5, p. 36 |
| Multivariate forecasting, DLinear, ETTh1, Short | R2 | 0.5768 | — | — | Table 5, p. 36 |
| Multivariate forecasting, PatchTST, ETTh1, Short | MAE | 0.4008 | — | — | Table 5, p. 36 |
| Multivariate forecasting, PatchTST, ETTh1, Short | MSE | 0.3674 | — | — | Table 5, p. 36 |
| Multivariate forecasting, PatchTST, ETTh1, Short | MAPE | 65.62% | — | — | Table 5, p. 36 |
| Multivariate forecasting, PatchTST, ETTh1, Short | R2 | 0.5749 | — | — | Table 5, p. 36 |
| Multivariate forecasting, N-BEATS, ETTh1, Short | MAE | 0.4579 | — | — | Table 5, p. 37 |
| Multivariate forecasting, N-BEATS, ETTh1, Short | MSE | 0.4353 | — | — | Table 5, p. 37 |
| Multivariate forecasting, N-BEATS, ETTh1, Short | MAPE | 61.44% | — | — | Table 5, p. 37 |
| Multivariate forecasting, N-BEATS, ETTh1, Short | R2 | 0.5110 | — | — | Table 5, p. 37 |
| Multivariate forecasting, Autoformer, ETTh1, Short | MAE | 0.5041 | — | — | Table 5, p. 37 |
| Multivariate forecasting, Autoformer, ETTh1, Short | MSE | 0.4961 | — | — | Table 5, p. 37 |
| Multivariate forecasting, Autoformer, ETTh1, Short | MAPE | 68.67% | — | — | Table 5, p. 37 |
| Multivariate forecasting, Autoformer, ETTh1, Short | R2 | 0.4155 | — | — | Table 5, p. 37 |
| Multivariate forecasting, NS-Transformer, ETTh1, Short | MAE | 0.4306 | — | — | Table 5, p. 37 |
| Multivariate forecasting, NS-Transformer, ETTh1, Short | MSE | 0.4197 | — | — | Table 5, p. 37 |
| Multivariate forecasting, NS-Transformer, ETTh1, Short | MAPE | 70.07% | — | — | Table 5, p. 37 |
| Multivariate forecasting, NS-Transformer, ETTh1, Short | R2 | 0.5293 | — | — | Table 5, p. 37 |
| Input shuffling, DLinear, ETTh1, Original | MAE | 0.4317 | — | — | Table 7, p. 44 |
| Input shuffling, DLinear, ETTh1, Shuffled | MAE | 0.6655 | — | — | Table 7, p. 44 |
| Input shuffling, DLinear, ETTh1, Drop | MAE drop | 54.16% | — | — | Table 7, p. 44 |
| Input shuffling, PatchTST, ETTh1, Original | MAE | 0.4070 | — | — | Table 7, p. 44 |
| Input shuffling, PatchTST, ETTh1, Shuffled | MAE | 0.7860 | — | — | Table 7, p. 44 |
| Input shuffling, PatchTST, ETTh1, Drop | MAE drop | 93.12% | — | — | Table 7, p. 44 |
| Input shuffling, Crossformer, ETTh1, Original | MAE | 0.4454 | — | — | Table 7, p. 44 |
| Input shuffling, Crossformer, ETTh1, Shuffled | MAE | 0.7744 | — | — | Table 7, p. 44 |
| Input shuffling, Crossformer, ETTh1, Drop | MAE drop | 73.84% | — | — | Table 7, p. 44 |
| Lookback window, DLinear, ETTh1, 48 | MAE | 0.4389 | — | — | Table 8, p. 45 |
| Lookback window, DLinear, ETTh1, 96 | MAE | 0.4317 | — | — | Table 8, p. 45 |
| Lookback window, DLinear, ETTh1, 192 | MAE | 0.4301 | — | — | Table 8, p. 45 |
| Lookback window, PatchTST, ETTh1, 48 | MAE | 0.4434 | — | — | Table 8, p. 45 |
| Lookback window, PatchTST, ETTh1, 96 | MAE | 0.4323 | — | — | Table 8, p. 45 |
| Lookback window, PatchTST, ETTh1, 192 | MAE | 0.4289 | — | — | Table 8, p. 45 |
| Artificial dataset, DLinear, Original Sequence | MAE | 0.0145 | — | — | Table 9, p. 46 |
| Artificial dataset, DLinear, Original Sequence | MSE | 0.0003 | — | — | Table 9, p. 46 |
| Artificial dataset, DLinear, Trend Term | MAE | 0.1456 | — | — | Table 9, p. 46 |
| Artificial dataset, DLinear, Trend Term | MSE | 0.0351 | — | — | Table 9, p. 46 |
| Artificial dataset, DLinear, Season Term | MAE | 0.1500 | — | — | Table 9, p. 46 |
| Artificial dataset, DLinear, Season Term | MSE | 0.0351 | — | — | Table 9, p. 46 |
| Artificial dataset, Fedformer, Trend Term | MAE | 0.1074 | — | — | Table 9, p. 46 |
| Artificial dataset, Fedformer, Trend Term | MSE | 0.0181 | — | — | Table 9, p. 46 |
| Artificial dataset, Fedformer, Season Term | MAE | 0.0823 | — | — | Table 9, p. 46 |
| Artificial dataset, Fedformer, Season Term | MSE | 0.0115 | — | — | Table 9, p. 46 |
| Attention module comparison, Auto-Correction, ETTh1 | MAE | 0.5160 | — | — | Table 10, p. 47 |
| Attention module comparison, Auto-Correction, ETTh1 | MSE | 0.5331 | — | — | Table 10, p. 47 |
| Attention module comparison, Patch Attention, ETTh1 | MAE | 0.4357 | — | — | Table 10, p. 47 |
| Attention module comparison, Patch Attention, ETTh1 | MSE | 0.4015 | — | — | Table 10, p. 47 |
| Attention module comparison, Attention (vanilla), ETTh1 | MAE | 0.5310 | — | — | Table 10, p. 47 |
| Attention module comparison, Attention (vanilla), ETTh1 | MSE | 0.5741 | — | — | Table 10, p. 47 |
| Attention-based models, PatchTST, ETTh1, O=48 | MAE | 0.3932 | — | — | Table 11, p. 47 |
| Attention-based models, PatchTST, ETTh1, O=48 | MSE | 0.3506 | — | — | Table 11, p. 47 |
| Attention-based models, Reformer, ETTh1, O=48 | MAE | 0.4986 | — | — | Table 11, p. 47 |
| Attention-based models, Reformer, ETTh1, O=48 | MSE | 0.4984 | — | — | Table 11, p. 47 |
| Attention-based models, Transformer, ETTh1, O=48 | MAE | 0.4745 | — | — | Table 11, p. 47 |
| Attention-based models, Transformer, ETTh1, O=48 | MSE | 0.4491 | — | — | Table 11, p. 47 |
| Memory occupation, Logtrans, O=336 | MB | 1799 | — | — | Table 12, p. 47 |
| Memory occupation, PatchTST, O=336 | MB | 1602 | — | — | Table 12, p. 47 |
| Memory occupation, Pyraformer, O=336 | MB | 1745 | — | — | Table 12, p. 47 |
| DLinear ETTh1 MAE improvement over PatchTST, O=336 | improvement | 3.13% | — | — | Sect. 6.4.1, p. 48 |
| DLinear ETTh1 MAPE improvement over Fedformer, O=336 | improvement | 2.24% | — | — | Sect. 6.4.1, p. 48 |
| DLinear ETTh1 R2 improvement over PatchTST, O=336 | improvement | 14.87% | — | — | Sect. 6.4.1, p. 48 |
| Crossformer Electricity MSE improvement over NS-Transformer, O=48 | improvement | 10.93% | — | — | Sect. 6.4.1, p. 48 |
| Crossformer Electricity MAPE improvement over NS-Transformer, O=48 | improvement | 17.70% | — | — | Sect. 6.4.1, p. 48 |
| PatchTST ILI MSE improvement over NS-Transformer, O=48 | improvement | 27.30% | — | — | Sect. 6.4.1, p. 49 |
| PatchTST ILI R2 improvement over NS-Transformer, O=48 | improvement | 17.49% | — | — | Sect. 6.4.1, p. 49 |
| PatchTST Traffic MAE improvement over NS-Transformer, O=336 | improvement | 11.46% | — | — | Sect. 6.4.1, p. 49 |
| NS-Transformer ILI long-term MAE improvement over PatchTST | improvement | 9.54% | — | — | Sect. 6.4.1, p. 49 |
| NS-Transformer ILI long-term MSE improvement over PatchTST | improvement | 25.32% | — | — | Sect. 6.4.1, p. 49 |
| NS-Transformer ILI long-term R2 improvement over PatchTST | improvement | 46.47% | — | — | Sect. 6.4.1, p. 49 |
| Fedformer trend term MAE improvement over TDformer | improvement | 3.14% | — | — | Sect. 6.4.3, p. 51 |
| Fedformer trend term MSE improvement over TDformer | improvement | 6.18% | — | — | Sect. 6.4.3, p. 51 |
| Fedformer trend term MAE improvement over DLinear | improvement | 26.24% | — | — | Sect. 6.4.3, p. 51 |
| Fedformer trend term MSE improvement over DLinear | improvement | 48.43% | — | — | Sect. 6.4.3, p. 51 |
| Fedformer season term MAE improvement over TDformer | improvement | 26.65% | — | — | Sect. 6.4.3, p. 52 |
| Fedformer season term MSE improvement over TDformer | improvement | 43.07% | — | — | Sect. 6.4.3, p. 52 |
| Fedformer season term MAE improvement over ETSformer | improvement | 29.17% | — | — | Sect. 6.4.3, p. 52 |
| Fedformer season term MSE improvement over ETSformer | improvement | 44.17% | — | — | Sect. 6.4.3, p. 52 |
| Patch Attention ETTh1 MAE improvement over vanilla Attention | improvement | 17.95% | — | — | Sect. 6.4.4, p. 53 |
| Patch Attention ETTh1 MSE improvement over vanilla Attention | improvement | 30.06% | — | — | Sect. 6.4.4, p. 53 |
| Patch Attention Exchange MSE improvement over vanilla Attention | improvement | 85.27% | — | — | Sect. 6.4.4, p. 53 |
| Reformer test time reduction compared to LogTrans | reduction | 10.14% | — | — | Sect. 6.4.4, p. 53 |
| Reformer ETTh1 MAE improvement over LogTrans | improvement | 14.03% | — | — | Sect. 6.4.4, p. 53 |
| Reformer ETTh1 MSE improvement over LogTrans | improvement | 18.42% | — | — | Sect. 6.4.4, p. 53 |
| PatchTST memory reduction compared to LogTrans, O=336 | reduction | 10.93% | — | — | Sect. 6.4.4, p. 53 |
| PatchTST ETTh1 MAE improvement over LogTrans, O=336 | improvement | 28.83% | — | — | Sect. 6.4.4, p. 53 |
| PatchTST ETTh1 MSE improvement over LogTrans, O=336 | improvement | 42.09% | — | — | Sect. 6.4.4, p. 53 |
| Pyraformer memory reduction compared to LogTrans, O=336 | reduction | 3.00% | — | — | Sect. 6.4.4, p. 54 |
| Pyraformer ETTh1 MAE improvement over LogTrans, O=336 | improvement | 4.10% | — | — | Sect. 6.4.4, p. 54 |
| Pyraformer ETTh1 MSE improvement over LogTrans, O=336 | improvement | 4.27% | — | — | Sect. 6.4.4, p. 54 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "With the advancement of deep learning algorithms and the growing availability of computational power, deep learning-based forecasting methods have gained significant importance in the domain of time series forecasting." | Abstract, p. 1 | model_algorithm_integration |
| "Fully exploiting these two types of information plays a crucial role in improving the model's capability." | Sect. 1.2, p. 2 | model_algorithm_integration |
| "The Transformer model does not make good use of time series order information." | Sect. 1.2, p. 3 | model_algorithm_integration |
| "To reduce the complexity of time series forecasting and capture these temporal patterns, some models have introduced time series decomposition techniques." | Sect. 1.2, p. 3 | model_algorithm_integration |
| "CNN models are constrained by their limited receptive field, hindering their ability to effectively capture long-term time series data." | Sect. 1.2, p. 4 | model_performance_evaluation |
| "DLinear outperforms the suboptimal model PatchTST in terms of MAE and Fedformer in terms of MAPE for the ETTh1 dataset." | Sect. 6.4.1, p. 48 | model_performance_evaluation |
| "Complex models like Autoformer, TDformer, and others demonstrate minimal impact on their prediction accuracy or even show slight improvements after input shuffling." | Sect. 6.4.2, p. 50 | model_performance_evaluation |
| "Fedformer, TDformer, and DLinear all use simple trend information extraction methods, such as mean filtering and linear layers. This indicates that simple techniques can effectively extract trend information." | Sect. 6.4.3, p. 51 | model_algorithm_integration |
| "Patch Attention in PatchTST significantly improves the prediction capability of the Attention mechanism." | Sect. 6.4.4, p. 53 | model_performance_evaluation |
| "The benefits of complexity optimization through patch slicing become more apparent as the length of the input time series increases." | Sect. 6.4.4, p. 55 | model_algorithm_integration |
| "Existing complex models often suffer from overfitting and noise interference, leading to prediction performance that is sometimes inferior to simpler models." | Sect. 7, p. 55 | model_performance_evaluation |
| "Exploring seasonal information in the frequency domain remains a promising direction for future research." | Sect. 7, p. 55 | model_algorithm_integration |
| "Effectively utilizing these relationships remains an important research direction." | Sect. 7, p. 55 | model_algorithm_integration |
| "Optimizing the computational cost of the Attention mechanism without sacrificing prediction accuracy remains a key area for further exploration and research." | Sect. 7, p. 55 | model_algorithm_integration |
| "There is a critical need to develop time series prediction models that can adapt to flexible prediction scenarios, accommodating changes in prediction length and position without requiring extensive redesign or retraining." | Sect. 7, p. 56 | model_algorithm_integration |
| "The non-stationarity of time series, particularly the differences in statistical characteristics between the training and test sets, can often impact the model's predictive accuracy." | Sect. 7, p. 56 | model_performance_evaluation |

## Remember This

- This is a comprehensive review of deep learning time series forecasting models from 2014 to 2024, covering time-step dependencies, variable correlations, complexity optimization, and loss functions.
- DLinear, a simple linear layer model, achieves competitive or superior accuracy compared to complex models across most datasets, suggesting existing complex models may have limited capability in effectively capturing and utilizing time-step information.
- Complex models suffer from overfitting and noise interference, as demonstrated by input shuffling experiments (complex models show minimal accuracy decline) and lookback window extension experiments (accuracy declines with longer inputs).
- Simple methods (mean filtering, linear layers) effectively extract trend information, while frequency domain methods effectively extract seasonal information; Fedformer achieves the best performance on both trend and season term prediction on the artificial dataset.
- Patch slicing significantly improves attention efficiency for long-term forecasting, with benefits becoming more pronounced as input length increases.
- The paper identifies future directions including mining time-step dependencies, mining variable relationships, complexity optimization, overfitting mitigation, flexible prediction models, non-stationarity handling, and probabilistic forecasting.

## Cited Works

- Zhang (2003) — ARIMA model for time series forecasting. [p. 2]
- Ariyo et al. (2014) — Stock price prediction using ARIMA. [p. 2]
- Contreras et al. (2003) — ARIMA models for electricity price prediction. [p. 2]
- Lv et al. (2014) — Autoencoder and Stacked Autoencoders for traffic flow prediction. [p. 2]
- Gudelek et al. (2017) — CNN for stock trading trend detection. [p. 2]
- Bai et al. (2018) — Temporal Convolutional Network (TCN) for sequence modeling. [p. 2]
- Shi et al. (2015) — Convolutional LSTM network for precipitation nowcasting. [p. 3]
- Dey and Salem (2017) — Gated Recurrent Unit (GRU) neural networks. [p. 3]
- Salinas et al. (2020) — DeepAR for probabilistic forecasting. [p. 5]
- Lai et al. (2018) — LSTnet for long- and short-term temporal patterns. [p. 3]
- Vaswani et al. (2017) — Transformer architecture with attention mechanism. [p. 3]
- Devlin et al. (2018) — BERT for natural language understanding. [p. 3]
- Dosovitskiy et al. (2020) — Vision Transformer for image recognition. [p. 3]
- Wu et al. (2021) — Autoformer with decomposition and auto-correlation. [p. 3]
- Li et al. (2019) — LogTrans with LogSparse Self-Attention. [p. 4]
- Zhou et al. (2021) — Informer with ProbSparse Self-Attention. [p. 4]
- Kitaev et al. (2020) — Reformer with LSH Attention. [p. 4]
- Zhou et al. (2022) — Fedformer with frequency enhanced attention. [p. 4]
- Oreshkin et al. (2019) — N-BEATS with interpretable time series forecasting. [p. 4]
- Woo et al. (2022) — ETSformer with exponential smoothing attention. [p. 4]
- Nie et al. (2022) — PatchTST with patch-based attention. [p. 4]
- Zhang and Yan (2022) — Crossformer with cross-dimension dependency. [p. 4]
- Lim et al. (2021) — Temporal Fusion Transformers (TFT). [p. 4]
- Qi et al. (2021) — Aliformer for sales forecasting. [p. 4]
- Liu et al. (2021) — Pyraformer with pyramidal attention. [p. 4]
- Shabani et al. (2022) — Scaleformer with multi-scale iterative framework. [p. 4]
- Kim et al. (2021) — RevIN for distribution shift. [p. 4]
- Liu et al. (2022) — NS-Transformer with De-stationary Attention. [p. 4]
- Cirstea et al. (2022) — Triformer with triangular attention. [p. 4]
- Lin et al. (2021) — SSDNet with state space model and negative log-likelihood. [p. 5]
- Wu et al. (2020) — AST with adversarial sparse transformer. [p. 5]
- Goodfellow et al. (2014) — Generative Adversarial Networks. [p. 5]
- Zhang et al. (2022) — TDformer with first de-trend then attend. [p. 5]
- Yun et al. (2019) — DLinear with linear layer forecasting. [p. 5]