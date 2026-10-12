---
conversion_metadata:
  converted_at: "2026-10-12T07:26:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "J. Chen et al., 2024.pdf"
  source_pdf_sha256: "725092e0974a288381e986c5bd74b591656212b3d831c684569f6faff0aeac8d"
  page_count: 18
  markdown_char_count: 81194
---

Journal of Basic and Applied Research International
Volume 30, Issue 6, Page 140-157, 2024; Article no.JOBARI.12619
ISSN: 2395-3438 (P), ISSN: 2395-3446 (O)
A Survey of Time Series Data
Forecasting Methods Based on Deep
Learning
Jiahui Chen a, Tao Chen a, Yishui Wang a
and Lidong Wang a*
a School of Engineering, Hangzhou Normal University, 310018, Hangzhou, Zhejiang, China.
Authors’ contributions
This work was carried out in collaboration among all authors. Authors JC and TC designed the study,
performed the statistical analysis and wrote the first draft of the manuscript. Authors YW and LW
managed the analyses of the study. Author LW managed the literature searches. All authors read and
approved the final manuscript.
Article Information
DOI: https://doi.org/10.56557/jobari/2024/v30i69014
Open Peer Review History:
This journal follows the Advanced Open Peer Review policy. Identity of the Reviewers, Editor(s) and additional Reviewers,
peer review comments, different versions of the manuscript, comments of the editors, etc are available here:
https://prh.ikprress.org/review-history/12619
Received: 17/10/2024
Accepted: 20/12/2024
Review Article
Published: 27/12/2024
ABSTRACT
Time Series Forecasting (TSF) involves predicting future values and trends of data at specific points
or periods by analyzing historical patterns, such as trends and seasonality. With the advent of IoT
sensors, traditional machine learning approaches struggle to handle massive time series datasets.
Recently, deep learning algorithms, exemplified by convolutional neural networks (CNNs), recurrent
neural networks (RNNs), and Transformer models, have made significant progress in time series
forecasting tasks. This paper reviews the common features of time series data, relevant datasets,
and evaluation metrics for models. It also conducts experimental comparisons of various forecasting
algorithms, focusing on time and algorithmic architectures. This paper conducts prediction
experiments on several deep learning models using the ETT dataset and presents the final results.
_____________________________________________________________________________________________________
*Corresponding author: E-mail: wld@hznu.edu.cn;
Cite as: Chen, Jiahui, Tao Chen, Yishui Wang, and Lidong Wang. 2024. “A Survey of Time Series Data Forecasting Methods
Based on Deep Learning”. Journal of Basic and Applied Research International 30 (6):140-57.
https://doi.org/10.56557/jobari/2024/v30i69014.

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

We evaluate model performance using metrics like Mean Absolute Error (MAE) and Mean Squared
Error (MSE). We highlight the strengths and weaknesses of deep learning-based TSF methods.
Major deep learning-based time series forecasting methods are introduced and compared. Finally,
challenges and future research directions in applying deep learning to time series forecasting are
discussed.

Keywords:  Deep learning; time series forecasting; recurrent neural networks; gated recurrent units;
transformer model.

1. INTRODUCTION  Convolutional Neural Networks (CNNs), as one
of the most representative network architectures

Time  series  data  exist  widely  in  domains  like  in  deep  learning  (Shaowei  et  al.,  2023),  hold
|     |     |     |     |     |     |     | broad  | application  |     | prospects  | in  | this  | field.  |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ---------- | --- | ----- | ------- |
finance, healthcare, energy, transportation, and
|     |     |     |     |     |     |     | Compared  |     | to  traditional  |     | methods,  |     | CNNs  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------- | --- | --------- | --- | ----- |
meteorology and are easily accessible. However,
with the widespread use of sensing devices and  demonstrate  superior  capabilities  in  feature
advancements  in  data  processing,  time  series  extraction and information mining. While CNNs
are highly effective for processing image data,
data are being generated at an explosive rate.
Analyzing  these  data  is  crucial  for  extracting  they face limitations when applied to time series
valuable  information,  such  as  weather  data,  such  as  sequences,  speech,  and  text.
Specifically, CNNs struggle to capture long-range
| predictions,  |     | traffic  | flow  | forecasts,  |     | financial  |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ----- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
dependencies in time series. Although increasing
| analysis,  | flu  | trend  | monitoring,  |     |     | medical  |     |     |     |     |     |     |     |
| ---------- | ---- | ------ | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
responses, and system workload management  the depth of convolutional layers can expand the
|     |     |     |     |     |     |     | receptive  | field,  | it  often  | remains  | insufficient  |     | for  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---------- | -------- | ------------- | --- | ---- |
(Eslin & Agon, 2012).
|     |     |     |     |     |     |     | modeling  | long-term  |     | dependencies  |     |     | within  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------------- | --- | --- | ------- |

Time  Series  Forecasting  is  a  critical  tool  for  sequences.  In  1990, Jeffrey  Elman introduced
|     |     |     |     |     |     |     | the  foundational  |     | concept  |     | and  | structure  | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --- | ---- | ---------- | --- |
making predictions based on historical data that
Recurrent Neural Networks (RNNs) in his paper
| is  collected  |     | over  time.  | By  | leveraging  |     | various  |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
statistical  and  machine  learning  models,  Finding  Structure  in  Time.  Elman's  model
|     |     |     |     |     |     |     | introduced  | the  | concept  | of  | a  hidden  | layer  | (or  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | -------- | --- | ---------- | ------ | ---- |
businesses and researchers can predict future
|     |     |     |     |     |     |     | internal  | state),  | which  | stores  | information  |     | about  |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ------- | ------------ | --- | ------ |
events, trends, and behaviors in areas ranging
previous elements in a sequence and uses it to
| from  finance  |     | to  weather  |     | forecasting.  |     | While  |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
traditional  machine  learning  methods  (like  predict  the  next  element.  This  breakthrough
opened the door for RNN applications in natural
| decision  | trees,  | random  |     | forests,  | and  | linear  |     |     |     |     |     |     |     |
| --------- | ------- | ------- | --- | --------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
language processing, time series analysis, and
| regression)  |     | can  be  | applied  | to  | time  | series  |     |     |     |     |     |     |     |
| ------------ | --- | -------- | -------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
forecasting, they face significant challenges due  other domains. Subsequently, RNNs evolved to
|     |     |     |     |     |     |     | address  | issues  | like  | vanishing  | and  | exploding  |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----- | ---------- | ---- | ---------- | --- |
to the unique nature of time series data, including
gradients in long-sequence processing through
| temporal  | dependence,  |     |     | seasonality,  |     | non- |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
stationarity,  and  the  need  for  careful  feature  variants  such  as  Long  Short-Term  Memory
|               |     |                |          |           |        |            | (LSTM)       | networks   | and            | Gated        | Recurrent          |      | Units  |
| ------------- | --- | -------------- | -------- | --------- | ------ | ---------- | ------------ | ---------- | -------------- | ------------ | ------------------ | ---- | ------ |
| engineering.  |     | These          | methods  |           | often  | require    |              |            |                |              |                    |      |        |
|               |     |                |          |           |        |            | (GRU).       | In  2017,  | Vaswani        |              | et  al.  proposed  |      | the    |
| substantial   |     | preprocessing  |          |           | and    | feature    |              |            |                |              |                    |      |        |
|               |     |                |          |           |        |            | Transformer  |            | architecture,  | introducing  |                    | the  | self-  |
| engineering   |     | to  capture    | the      | temporal  |        | patterns.  |              |            |                |              |                    |      |        |
Specifically, traditional statistical models, such as  attention  mechanism—a  key  innovation  that
|                 |         |         |           |        |        |                           | enables     | exceptional  |     |        | performance         |     | in                 |
| --------------- | ------- | ------- | --------- | ------ | ------ | ------------------------- | ----------- | ------------ | --- | ------ | ------------------- | --- | ------------------ |
| Support         | Vector  |         | Machines  |        | (SVM)  | and                       |             |              |     |        |                     |     |                    |
|                 |         |         |           |        |        |                           | processing  | sequence     |     | data.  | The  Transformer's  |     |                    |
| Autoregressive  |         | Models  |           | (AR),  |        | require                   |             |              |     |        |                     |     |                    |
manual  configuration  of  seasonal  and  trend  self-attention  mechanism  captures  long-term
|             |         |           |           |        |             |      | dependencies,  |       | addressing  |             | limitations  |     | of   |
| ----------- | ------- | --------- | --------- | ------ | ----------- | ---- | -------------- | ----- | ----------- | ----------- | ------------ | --- | ---- |
| components  |         | (Gers     | et  al.,  | 2000;  | Durbin      | &    |                |       |             |             |              |     |      |
|             |         |           |           |        |             |      | traditional    | RNNs  | in          | long-range  | prediction   |     | and  |
| Koopman,    | 2012),  | limiting  |           | their  | efficiency  | and  |                |       |             |             |              |     |      |
accuracy  with  large-scale  datasets.  Deep                 parallel computation. As a result, Transformers
have achieved remarkable performance in time
| neural  | networks  | (DNNs)  |     | offer  | an  alternative                |     |     |     |     |     |     |     |     |
| ------- | --------- | ------- | --- | ------ | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
series forecasting tasks.
| due  to  | their  | ability  | to  | extract  |     | high-level                 |     |     |     |     |     |     |     |
| -------- | ------ | -------- | --- | -------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |

features and identify complex patterns within and
|     |     |     |     |     |     |     | In  modern  | domains,  |     | time  | series  | forecasting  |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | ----- | ------- | ------------ | --- |
across time series with minimal manual effort.
|     |     |     |     |     |     |     | methods  | are  | already  | well-established.  |     |     | For  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | ------------------ | --- | --- | ---- |
However, DNNs require extensive training data
instance, Facebook's visual interactive network
| due  to  | their  | reliance  | on  | fewer  |     | structural  |     |     |     |     |     |     |     |
| -------- | ------ | --------- | --- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
(VIN) employs bidirectional LSTM to effectively
assumptions.
capture temporal information in videos (Michael

141

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

et  al.,  2024).  Chinese  researchers  have  also  effectively enhancing SOTA model performance.
achieved  significant  results  in  tasks  such  as  In 2023, Zhang et al.  proposed a multi-scale
image  captioning  and  video  classification.  For  pyramid  Transformer  model  called  MTPNet
example,  the  Chinese  Academy  of  Sciences  (Zhang  et  al.,  2024).  The  use  of  multi-layer
proposed the spatio-temporal attention network  Transformer structures with different scales has
(STAN),  which  uses  bidirectional  GRU  to  solved the problem of time dependent modeling
enhance video classification accuracy (Hanen et  for fixed or constrained scales. Some studies,
al., 2024). Photovoltaics (PV), one of the most  such  as  the  BERT  model,  adopt  learnable
promising  renewable  energy  sources,  requires  position  encodings  to  learn  positional
accurate power forecasting to ensure the safe  embeddings from time series through  training.
operation  and  economic  integration  of  PV  For  instance,  Jin  et  al.,  (2021)  proposed  the
systems in smart grids. Mohamed Abdel-Nasser  TrafficBERT  model  for  traffic  flow  prediction.
et al. proposed an LSTM-RNN-based method for  Additionally, Li et al., (2019) replaced traditional
predicting PV system output power, providing a  position  encodings  with  learnable  position
useful tool for smart grid planning and control  embeddings in the LogSparse Transformer. In
(Abdel-Nasser & Mahmoud, 2019; Qiang et al.,  2021,  Wu  et  al.,  (2021)  introduced  the
2020). Qiang Cui et al. introduced a Multi-View  Autoformer  model,  which  is  a  self-correlation
Recurrent Neural Network (MV-RNN) model to  decomposition  Transformer  for  long-term
handle  sequence  recommendations  and  cold- forecasting.  Although  sparse  attention
start  issues.  By  integrating  visual  and  textual  mechanisms  address  the  quadratic  complexity
information,  MV-RNN  mitigates  cold-start  issue,  they  limit  the  utilization  of  information.
problems,  dynamically  captures  user  interests,  Furthermore,  due  to  the  complex  temporal
generates personalized ranking lists, addresses  patterns  in  long-term  predictions,  self-attention
missing modality issues, and alleviates cold-start  mechanisms  struggle  to  capture  reliable
challenges (Qiang et al., 2020). Shaowei Pan et  dependencies.  Therefore,  Autoformer  was
al. proposed a hybrid model (CNN-LSTM-SA),  designed  with  a  deep  decomposition
combining  Convolutional  Neural  Networks  architecture,  which  integrates  time  series
(CNNs),  LSTM  networks,  and  self-attention  decomposition into the Transformer model for the
mechanisms (SA). This model achieved optimal  first  time. This  architecture  includes  sequence
performance in capturing fundamental trends and  decomposition  units,  self-correlation
predicting specific values for oil well production  mechanisms,  and  corresponding  encoder-
(Shaowei et al., 2023). In the field of speech  decoder components.
| recognition,  | RNNs         |     | and  their      | variants  |     | have  |                |     |          |     |      |
| ------------- | ------------ | --- | --------------- | --------- | --- | ----- | -------------- | --- | -------- | --- | ---- |
| achieved      | significant  |     | breakthroughs.  |           |     | For   |                |     |          |     |      |
|               |              |     |                 |           |     |       | 2  EVALUATION  |     | METRICS  |     | AND  |
example, Microsoft's deep neural network (DNN)  DATASETS  FOR  TIME  SERIES
| combined  | with  | LSTM  | demonstrated  |     | excellent  |     |     |     |     |     |     |
| --------- | ----- | ----- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
FORECASTING
performance in speech recognition competitions.

| Domestic  | companies  |       | such     | as  iFLYTEK  |            | and  |                  |          |      |       |         |
| --------- | ---------- | ----- | -------- | ------------ | ---------- | ---- | ---------------- | -------- | ---- | ----- | ------- |
|           |            |       |          |              |            |      | 2.1  Evaluation  | Metrics  | for  | Time  | Series  |
| Sogou     | have       | also  | adopted  |              | RNN-based  |      |                  |          |      |       |         |
Forecasting
| technologies                                        |     | to  improve  |     | speech  | recognition  |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ------------ | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
| accuracy (Fang et al., 2021). In hydrological time  |     |              |     |         |              |     |     |     |     |     |     |
Evaluation metrics are tools used to assess and
| series  | forecasting,  |     | Muhammad  | Waqas  |     | et  al.  |     |     |     |     |     |
| ------- | ------------- | --- | --------- | ------ | --- | -------- | --- | --- | --- | --- | --- |
demonstrated  the  effectiveness  of  RNNs  and  analyze  the  performance  of  time  series
LSTMs in modeling nonlinear and time-varying  forecasting models, serving as key criteria for
|     |     |     |     |     |     |     | measuring  | model  | performance.  |     | Common  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------- | --- | ------- |
hydrological systems, making them a research
hotspot  (Waqas  &  Humphries,  2024.  The  evaluation  metrics  for  time  series  forecasting
| Transformer's self-attention mechanism excels in  |     |     |     |     |     |     | include:  |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |

| capturing  | long-range  |     | dependencies,  |     |     | offering  |     |     |     |     |     |
| ---------- | ----------- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
superior  temporal  modeling  capabilities  and  Mean Squared Error (MSE): This measures the
advantages in handling time series data (Wen et  average  squared  difference  between  predicted
al., 2023). Liu et al. proposed a de-stationary  and  actual  values,  reflecting  the  overall  error
framework to address over-stabilization issues in  between the predictions and actual outcomes. It
processing raw time series data (Liu et al., 2022).  is calculated as follows:
| Additionally,  | Liu     | et         | al.  recently  | introduced  |       | an      |            |      |           |     |               |
| -------------- | ------- | ---------- | -------------- | ----------- | ----- | ------- | ---------- | ---- | --------- | --- | ------------- |
| inverted       | input   | approach   | that           | reassigns   |       | roles   |            | 1 n  |           |     |               |
|                |         |            |                |             |       |         | MSE（y,yˆ）= | (y  | − yˆ )2   |     |               |
| between        | the     | attention  |                | module      | and   | the     |            |      |           |     |          (1)  |
|                |         |            |                |             |       |         |            | ni=1 | i i       |     |               |
| feedforward    | neural  |            | network        | (Liu  et    | al.,  | 2024),  |            |      |           |     |               |

142

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Root Mean Squared Error (RMSE): This is the
|     |     |     |     |     |     | Except  | for  R | 2 ,  all  | the  | evaluation  |     | metrics  |
| --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ---- | ----------- | --- | -------- |
square root of MSE, assigning higher weights to  mentioned above are better when their values
larger errors and emphasizing the stability of the
|     |     |     |     |     |     | are  smaller.  |     | The  choice  |     | of  evaluation  |     | metric  |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | --------------- | --- | ------- |
prediction results. It is calculated as follows:
depends on the specific situation. Typically, a
|     |     |     |     |     |     | combination  |     | of  multiple  |     | metrics  | is  | used  to  |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | -------- | --- | --------- |
1 ni= comprehensively  analyze  the  model,
|     |     | （ ） |     | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
R M S E y , ˆy = ( y − ˆy ) enabling deeper insights. Due to the differences
|     |     |     | i   | i   | (2)  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
n 1            in  the  characteristics  and  application

|     |     |     |     |     |     | focus  | of  Recurrent  |     | Neural  | Network  |     | (RNN)  |
| --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ------- | -------- | --- | ------ |
Mean Absolute Error (MAE): This represents  models  and  Transformer  models  when
the mean absolute difference between predicted  handling time series data, researchers prioritize
and  actual  values,  reducing  the  influence  of  different  metrics  when  evaluating  algorithm
| outliers. It is calculated as follows:  |         |              |          |     |      | performance.                                     |     |            |               |     |     |           |
| --------------------------------------- | ------- | ------------ | -------- | --- | ---- | ------------------------------------------------ | --- | ---------- | ------------- | --- | --- | --------- |
|                                         |         |              |          |     |      |                                                  |     |            |               |     |     |           |
|                                         |         | 1 ni=       |          |     |      | RNN models, with their memory capability, excel  |     |            |               |     |     |           |
|                                         | M A E （ | y , ˆy ） = ( | | y − ˆy | |)  |      |                                                  |     |            |               |     |     |           |
|                                         |         |              |          |     | (3)  | at  capturing                                    |     | long-term  | dependencies  |     |     | in  time  |
|                                         |         | n            | i        | i   |      |                                                  |     |            |               |     |     |           |
1                  series.  Consequently,  evaluation  metrics  for

RNNs often emphasize the ability to model the
Mean Absolute Percentage Error (MAPE): This
|     |     |     |     |     |     | overall  | structure  | of  | the  | time  | series  | and  |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---- | ----- | ------- | ---- |
metric considers the relative magnitude of the  adaptability to various tasks. Researchers may
actual values, avoiding the cancellation effect of  use  a  diverse  range  of  evaluation  metrics  to
positive and negative errors. It is calculated as
|           |     |     |     |     |     | thoroughly   | assess  | the    | performance     |        | of           | these  |
| --------- | --- | --- | --- | --- | --- | ------------ | ------- | ------ | --------------- | ------ | ------------ | ------ |
| follows:  |     |     |     |     |     | algorithms.  | On      | the    | other           | hand,  | Transformer  |        |
|           |     |     |     |     |     | models,      | with    | their  | self-attention  |        | mechanism    |        |
1 0 0 % ni= y − ˆy allowing  for  parallel  computation,  are  more
M A P E （ y , ˆy ） = i i efficient  and  focus  heavily  on  predictive
(4)
|     |     | n   | 1 y |     |           | accuracy. As such, researchers commonly use  |     |           |         |      |      |        |
| --- | --- | --- | --- | --- | --------- | -------------------------------------------- | --- | --------- | ------- | ---- | ---- | ------ |
|     |     |     | i   |     |           |                                              |     |           |         |      |      |        |
|     |     |     |     |     |           | MAE  (Mean                                   |     | Absolute  | Error)  | and  | MSE  | (Mean  |
Squared Error) to measure the performance of
| Symmetric  |     | Mean  Absolute  |     | Percentage             |     |     |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Transformers.
Error (SMAPE): This is a modification of MAPE

that avoids excessively large values when the
| actual values are very small. It is calculated as  |     |     |     |     |     | 2.2 Datasets  |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| follows:                                           |     |     |     |     |     |               |     |     |     |     |     |     |
|                                                    |     |     |     |     |     | 2.2.1 ETT     |     |     |     |     |     |     |

|     |     | 1 0 0 % n | y − | ˆy  |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | （   | ˆy ）       | i   | i   | (5) |     |     |     |     |     |     |     |
S M A P E y , = The  ETT  dataset,  provided  by  the  State  Grid
|     |     | n （ | y + | | ˆy ）| / 2 |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
i= 1 i i              Corporation  of  China,  consists  of  minute-level
|     |     |     |     |     |     | recordings of transformer oil temperatures from  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Coefficient  of  Determination  (R²):  Also                 two counties in the same province during 2016–
known  as  the  goodness  of  fit,  this  metric                2018.  Each  dataset  contains  1,051,200  data
divides  the  explained  variance  by  the                     points.  To  explore  long-term  prediction
total  variance  to  measure  the  proportion  of  granularity,  the  dataset  was  divided  into
variance in the dependent variable explained by  subsets  based  on  sampling  intervals  of  15
the  independent  variables.  It  is  calculated  as  minutes and 1 hour, resulting in four subsets:
| follows:  |     |      |     |     |     | ETTm1,                                          | ETTm2,  | ETTh1,      |        | and  | ETTh2.    | These  |
| --------- | --- | ---- | --- | --- | --- | ----------------------------------------------- | ------- | ----------- | ------ | ---- | --------- | ------ |
|           |     |      |     |     |     | subsets contain 69,680 and 17,420 data points,  |         |             |        |      |           |        |
|           |     |      |     |     |     | respectively.                                   |         | Each  data  | point  |      | includes  | seven  |
|           |     | 1 n | 2   |     |     |                                                 |         |             |        |      |           |        |
( y − ˆy )i features,  comprising  the  target  variable  (oil
|     |             | n1 i          |     | M S E |     |               |     |           |        |     |        |       |
| --- | ----------- | ------------- | --- | ----- | --- | ------------- | --- | --------- | ------ | --- | ------ | ----- |
|     | R 2（ y , ˆy | ） = 1 − i=1n | = 1 | −     |     |               |     |           |        |     |        |       |
|     |             |               |     |       | (6) | temperature)  |     | and  six  | types  | of  | power  | load  |
2 V a r
|     |     | ( y − | y )i |     |     | features.  |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
n i
|     |     | i=1 |     |          |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

|                                             |     |     |     |     | y   | 2.2.2 ECL  |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| In the formulas (1) to (6) mentioned above, |     |     |     |     | is  |            |     |     |     |     |     |     |

| the true value, yˆ |     |  is the predicted value, y is the  |     |     |     |                    |     |            |     |         |              |     |
| ------------------ | --- | ---------------------------------- | --- | --- | --- | ------------------ | --- | ---------- | --- | ------- | ------------ | --- |
|                    |     |                                    |     |     |     | ECL  (Electricity  |     | Consuming  |     | Load):  | Electricity  |     |
y
mean of  , and Var is the variance.  Consumption Load dataset from 2012–2014.

143

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

2.2.3 Traffic  including  constant  position,  sticking,  step,
|     |     |     |     | random  variable,  | slow  | drift,  and  | five  unknown  |
| --- | --- | --- | --- | ------------------ | ----- | ------------ | -------------- |
Traffic:  Traffic  dataset  from  California's  faults. The variable parameters of this process
Department of Transportation (2015–2016).  include  41  measured  variables  (XMEAS  (1)  -
|     |     |     |     | XMEAS  (41))  | and  12  | manipulated  | variables  |
| --- | --- | --- | --- | ------------- | -------- | ------------ | ---------- |
2.2.4 Weather  (XMV (1) - XMV (12)), for a total of 53 observed
|                                                |     |     |     | variables.  |     |     |     |
| ---------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- |
| Weather: The weather dataset, provided by the  |     |     |     |             |     |     |     |
meteorological station of the Max Planck Institute  3  TIME  SERIES  PREDICTION  MODEL
for Biogeochemistry, records 21 meteorological
BASED ON DEEP LEARNING
indicators such as air pressure, temperature, and

humidity collected every 10 minutes from 2020 to
3.1 RNN
2021.

The RNN model consists of the following three
2.2.5 ILI
main components:

| ILI:  The  | influenza  | dataset,  | provided  by  the  |            |                   |        |            |
| ---------- | ---------- | --------- | ------------------ | ---------- | ----------------- | ------ | ---------- |
|            |            |           |                    | (1) Input  | Layer:  Receives  | input  | data  and  |
Centers for Disease Control and Prevention in
passes it to the hidden layer. The input
the United States, records the ratio of influenza
like  disease  patients  to  the  total  number  of  includes  not  only  static  data  but  also
historical information from the sequence.
patients per week from 2002 to 2021.
|     |     |     |     | (2) Hidden Layer: The core  |     | component that  |     |
| --- | --- | --- | --- | --------------------------- | --- | --------------- | --- |

|     |     |     |     | captures  | temporal  | dependencies.  | The  |
| --- | --- | --- | --- | --------- | --------- | -------------- | ---- |
2.2.6 TE
|     |     |     |     | output of the hidden layer depends on both  |     |     |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
Tennessee  Eastman  (TE)  is  a  representative  the current input and the hidden state from
the previous timestep.
| chemical  | process  | proposed  | by  an  American  |     |     |     |     |
| --------- | -------- | --------- | ----------------- | --- | --- | --- | --- |
chemical  company,  consisting  of  a  gas-liquid  (3) Output  Layer:  Generates  the  final
separator, a circulating compressor, a stripper, a  prediction  based  on  the  output  of  the
| condenser,                                     | a  reactor,  | and  other  | components.  | hidden layer.  |     |     |     |
| ---------------------------------------------- | ------------ | ----------- | ------------ | -------------- | --- | --- | --- |
| The TE chemical process can simulate 21 types  |              |             |              |                |     |     |     |
of  faults  in  industrial  production  processes.  The  structure  of  the  RNN  is  illustrated  in  the
| These  faults  | are  | mainly  divided  | into  6  types,  | diagram below:  |     |     |     |
| -------------- | ---- | ---------------- | ---------------- | --------------- | --- | --- | --- |

Fig. 1. RNN structure diagram

144

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

| The  | diagram  | shows  |     | the  basic  | structure  | of  an  |                                               |     |     |     |     |     |
| ---- | -------- | ------ | --- | ----------- | ---------- | ------- | --------------------------------------------- | --- | --- | --- | --- | --- |
|      |          |        |     |             |            |         | output layer then generates the final output  |     |     |     |     | o   |
t
o
RNN, where t represents the output information,  using  another  weight  matrix  and  activation
function.
| h   | represents  | the  | hidden  |     | layer  output  | at  the  |     |     |     |     |     |     |
| --- | ----------- | ---- | ------- | --- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
t

| current timestep,  |     |     | h  represents the hidden layer  |     |     |     |           |            |            |      |             |     |
| ------------------ | --- | --- | ------------------------------- | --- | --- | --- | --------- | ---------- | ---------- | ---- | ----------- | --- |
|                    |     |     | t− 1                            |     |     |     | Although  | RNNs  are  | effective  | for  | processing  |     |
output  from  the  previous  timestep,  and  x   sequential  data,  they  suffer  from  issues  like
t
|                                          |     |     |     |     |     |         | vanishing  | and  exploding  | gradients.  |     | For  | long  |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------- | ---------- | --------------- | ----------- | --- | ---- | ----- |
| represents the current input. Functions  |     |     |     |     |     | f  and  |            |                 |             |     |      |       |
1
|     |                   |     |             |     |        |       | sequences,                                         | the  gradients  |     | may  become  |     | very  |
| --- | ----------------- | --- | ----------- | --- | ------ | ----- | -------------------------------------------------- | --------------- | --- | ------------ | --- | ----- |
| f   |  are  activation  |     | functions,  |     | while  | , ,   |                                                    |                 |     |              |     |       |
|     | 2                 |     |             |     |        | W U V | small (vanish) or excessively large (explode) due  |                 |     |              |     |       |
represent  weight  matrices.  RNNs  work  by  to  repeated  multiplication.  To  address  these
continuously cycling the same neuron over time.
problems, variants of RNNs, such as Long Short-
The calculation for the current timestep is given
|      |     |     |     |     |     |     | Term  Memory                                 | (LSTM)  | networks  |     | and  | Gated  |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | ------- | --------- | --- | ---- | ------ |
| by:  |     |     |     |     |     |     | Recurrent Units (GRU), have been developed.  |         |           |     |      |        |

|     |     |         |       |       |     |          (7)  |                                    |     |     |     |     |     |
| --- | --- | ------- | ----- | ----- | --- | ------------- | ---------------------------------- | --- | --- | --- | --- | --- |
|     | h = | f ( U x | + W h | + b ) |     |               | 3.2 Long Short-Term Memory (LSTM)  |     |     |     |     |     |
|     | t   | 1 t     | t−    | 1     |     |               |                                    |     |     |     |     |     |

o = f ( V h + c )                                      (8)  LSTM  is  a  specialized  RNN  architecture
|     | t   | 2 t |     |     |     |     | proposed  | by  Hochreiter  | and  | Schmidhuber  |     | in  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ---- | ------------ | --- | --- |

1997. It was designed to overcome the gradient
| The  | working  |     | principle  | of  | RNNs  | can  be  |     |     |     |     |     |     |
| ---- | -------- | --- | ---------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
vanishing and exploding problems encountered
| summarized  |     | in  | the  following  |     | steps:  | At  each  |               |       |       |           |     |       |
| ----------- | --- | --- | --------------- | --- | ------- | --------- | ------------- | ----- | ----- | --------- | --- | ----- |
|             |     |     |                 |     |         |           | in  standard  | RNNs  | when  | handling  |     | long  |
x
|                                            |     |     |     |     |     |         | sequences.  | The  core  | of  | an  LSTM  |     | is  its  |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------- | ----------- | ---------- | --- | --------- | --- | -------- |
| timestep, the RNN unit receives the input  |     |     |     |     |     | t  for  |             |            |     |           |     |          |
sophisticated gating mechanism, which controls
h
| the current timestep and the hidden state  |     |     |     |     |     | t−  | 1   |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the flow of information in and out of the unit. A
from the previous timestep. Based on these, the
|     |     |     |     |     |     |     | typical  LSTM  | unit  | comprises  | the  | following  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ---------- | ---- | ---------- | --- |
hidden layer computes a new state h  using a  components: forget gate, input gate, cell state,
t
nonlinear function (such as Tanh or ReLU). The  and output gate. Below is its structure diagram:

Fig. 2. LSTM structure diagram

3.2.1 Forget Gate

In an LSTM, the first step is determining which information should be filtered out from the cell state by
the forget gate. This operation is achieved through the forget gate's structure. The forget gate reads
the previous output h  and the current input x , applies a Sigmoid nonlinear transformation, and
|     |     |     | t−  | 1   |     |     | t   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
outputs a vector ft . Each value in this vector ranges from 0 to 1, where 1 indicates complete retention
and 0 indicates complete discard. This vector is then multiplied element-wise with the cell stateC
t-1
.For example, in a language model, the cell state may encode the gender information of the subject in
the current sentence, ensuring the correct pronoun is selected. When a new subject is identified, the
forget gate removes the prior subject's gender information to make room for the new information.

145

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Fig. 3. Forgetting gate structure diagram

The mathematical formula for the forget gate is  (1) Input  Gate  activation  function.  This  is  a
| as follows:  |     |     |     | layer  composed  | of  a  | sigmoid  activation  |
| ------------ | --- | --- | --- | ---------------- | ------ | -------------------- |

function that determines which values will
f =  ( W [ h , x ] + b )             (9)  be updated to the cellular state. This layer
| t   | f t− 1 t | f   |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
outputs a vector between 0 and 1, where

each element corresponds to the updated
| here (        | )and ( b ) are the weight matrix and bias  |           |          |                                                |     |     |
| ------------- | ------------------------------------------ | --------- | -------- | ---------------------------------------------- | --- | --- |
| W             | f                                          |           |          |                                                |     |     |
|               | f                                          |           |          | weight of the corresponding element in the     |     |     |
| vector, (     | ) is the previous hidden state,(           |           | ) is     |                                                |     |     |
|               | h                                          |           | x        | candidate cell state.                          |     |     |
|               | t−1                                        |           | t        |                                                |     |     |
|               |                                            |          |          | (2) Generation of candidate cell states. This  |     |     |
| the  current  | input,  and                                |  is  the  | Sigmoid  |                                                |     |     |
activation function.  layer, formed by a tanh activation function,
|     |     |     |     | creates  | a  vector  of  | potential  new  |
| --- | --- | --- | --- | -------- | -------------- | --------------- |
3.2.2 Input gate  information containing values that might be

integrated into the current cell state. This
| The  information  | update  | mechanism  | in  Long  |     |     |     |
| ----------------- | ------- | ---------- | --------- | --- | --- | --- |
newly generated vector is then multiplied
Short-Term Memory (LSTM) networks involves  element-wise  by  the  output  of  the  input
the following two steps to determine how new  gate to determine the actual values added
information is stored in the cell state:
to the cell state.

|     | .   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

Fig. 4. Input door structure diagram

146

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

The mathematical expressions for these two steps are as follows:

|     | i =  ( W [i | h , x ] + b )    |     |     |     |                (10)  |
| --- | ------------ | ---------------- | --- | --- | --- | -------------------- |
|     | t            | t− 1 t i         |     |     |     |                      |

~C
|     | = ta n h ( | W [ h , x ] + b )   |     |     |     |     (11)  |
| --- | ---------- | ------------------- | --- | --- | --- | --------- |
|     | t          | c t− 1 t c          |     |     |     |           |

W b )，( W )and（ ） are the parameter matrices and bias vectors, (
| here ( | i )and ( i | c b |     |     |     | h ) is the hidden  |
| ------ | ---------- | --- | --- | --- | --- | ------------------ |
|        |            | c   |     |     |     | t−1                |
|        |            | x   |     |    |     |                    |
state from the previous timestep, ( ) is the current input,  and tanh are activation functions.
t

The next step updates the cell state C  by combining the information to be forgotten and the newly
t
added information:

Fig. 5. Update cell structure diagram

LSTM cells need to multiply the previous state  C with f , discard the information that needs to be
t-1 t
~
| discarded, and then add i |     | C . This is the new output state |     | C .  |     |     |
| ------------------------- | --- | --------------------------------- | --- | ---- | --- | --- |
|                           |     | t t                               |     | t    |     |     |

3.2.3 Output gate

Fig. 6. Output Gate Structure Diagram

The mathematical formula for the output gate is as follows:

|     | o =(W | [h ,x ]+b )  |     |     |     |     (12)  |
| --- | ------ | ------------ | --- | --- | --- | --------- |
|     | t 0    | t−1 t 0      |     |     |     |           |

147

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

|     | h = | o  t a n h ( C | )     |     |     |     |     |     | (13)  |
| --- | --- | --------------- | ----- | --- | --- | --- | --- | --- | ----- |
|     | t   | t t             |       |     |     |     |     |     |       |

here (W )and (b ) are the parameter matrices and bias vectors, (h ) is the previous timestep's
|     | 0   | 0   |     |     |     |     | t−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hidden state, (x ) is the current input, and    is the sigmoid activation function.
t

3.3 Gated Recurrent Units (GRU)

GRU is a simplified variant of LSTM that retains the gating mechanisms (update and reset gates) to
control the flow of information while omitting the separate memory cell. GRUs have fewer parameters
than  LSTMs,  resulting  in  higher  computational  efficiency  and,  in  some  cases,  similar  or  better
performance. The core components of GRU include:

Fig. 7. GRU structure diagram

3.3.1 Update gate  to  1,  more  past  information  is  retained.  The
|                                             |             |         |        |         |     | formula is:  |                   |         |              |
| ------------------------------------------- | ----------- | ------- | ------ | ------- | --- | ------------ | ----------------- | ------- | ------------ |
| The update gate determines how much of the  |             |         |        |         |     |              |                   |         |              |
| previous                                    | timestep's  | hidden  | state  | should  | be  |              |                   |         |              |
|                                             |             |         |        |         |     | r =          |  ( W [ h , x ] + | b )     |        (15)  |
|                                             |             |         |        |         |     | t            | t t− 1 t          | t       |              |
retained in the current hidden state. It outputs

values between 0 and 1, where higher values
here (W
indicate greater retention of past information and  r )and(b ) are the parameter matrices and
r
| lower values suggest reliance on current input.  |     |     |     |     |     | bias vectors.  |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |

The formula is:
|     |     |     |     |     |     | At  each  | time  step,  the  | GRU  unit  processes  |     |
| --- | --- | --- | --- | --- | --- | --------- | ----------------- | --------------------- | --- |
information through the following steps:
|     | z =  | ( W [ h , x ] | + b )    |      (14)  |     |     |     |     |     |
| --- | ----- | ------------- | -------- | ---------- | --- | --- | --- | --- | --- |
|     | t     | z t− 1 t      | z        |            |     |     |     |     |     |

(1) Calculate update and reset gates
here (W
|     | z ) and (b | ) are the parameter matrices  |     |     |     |     |     |     |     |
| --- | ---------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
z
and bias  vectors,( h ) is the previous  hidden  According  to  the  above  formula,  calculate  the
t−1
x ) is the current input, and  is the  update gates ( z ) and ( r ) respectively, and the
| state, ( | t   |     |     |     |     |     | t   | t   |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sigmoid activation function.  outputs of these gates will control the update of
|                   |     |     |     |     |     | hidden states and the degree of preservation of  |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
| 3.3.2 Reset gate  |     |     |     |     |     | historical information.                          |     |     |     |
|                   |     |     |     |     |     |                                                  |     |     |     |
The reset gate determines the extent to which  (2) Calculate candidate hidden states
| the  | previous  | hidden  | state  influences  |     | the  |     |     |     |     |
| ---- | --------- | ------- | ------------------ | --- | ---- | --- | --- | --- | --- |

computation of the candidate hidden state. When  GRU uses reset gates to control the degree of
the reset gate output is close to 0, most of the  dependence  on  previously  hidden  states  and
previous information is ignored; when it is close
calculate candidate hidden states.

148

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
The calculation formula for candidate hidden
states is:
~
h = tanh( W[rh ,x ]+b) (16)
t t t−1 t
Among them, (
149
r
t
 h
t− 1
) represents combining
the hidden state of the previous time step ( h
t− 1
)
with the reset gate (
r
t ) to control its degree of
influence, and ( W ) and ( b ) are the parameter
matrix and bias.
(3) Update Hidden State
z
The final step is to use the update gate ( t) to
calculate the current hidden state ( h
t
):
h
t
= (1 − z
t
)  h
t− 1
+ z
t

~h
t
3.4 Bi-LSTM Model
The Bi-LSTM (Bidirectional Long Short-Term
Memory) network is an improved version of the
LSTM network. It combines two LSTMs: one
processes the sequence from the beginning to
the end, while the other processes it in reverse,
from the end to the beginning. This architecture
excels in several tasks compared to standard
LSTM networks. Bi-LSTM is a time-recurrent
neural network that stacks forward and backward
LSTM layers together. The output is determined
by the hidden states of these two LSTM layers.
Bi-LSTM combines the traditional forward and
backward time sequences, leveraging LSTM's
sensitivity to sequence order to construct a
bidirectional network. The concatenated vector of
outputs from the forward and backward
processes provides the complete hidden
representation of Bi-LSTM, as shown below:
(17)
Here, (1−z)h controls the retention of past
t t−1 ~
information, and z h introduces new
t t
information. This formula ensures that the current
hidden state incorporates both historical and new
information effectively.
h
t
= h ft  h bt (18)
Here, h ft is the output from the forward LSTM
layer, and h bt is the output from the backward
LSTM layer. These outputs are combined using
element-wise summation. The internal structure
of Bi-LSTM cells is identical to that of standard
LSTMs and is thus not elaborated further.
Fig. 8. Bi LSTM Structure Diagram

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

is composed of stacked identical layers. Each
3.5 Transformer Model
|     |     |     |     | decoder  | layer  adds  | a  third  | sub-layer,  |     | which  |
| --- | --- | --- | --- | -------- | ------------ | --------- | ----------- | --- | ------ |
The Transformer is a deep learning architecture  performs multi-head attention over the encoder's
primarily used for natural language processing  output. Residual connections and normalization
| (NLP)  | and  other  | sequence-to-sequence      la   y e  r s      are  |     |     |          |           |             |     |      |
| ------ | ----------- | ------------------------------------------------- | --- | --- | -------- | --------- | ----------- | --- | ---- |
|        |             |                                                   |     |     | applied  | to  each  | sub-layer.  |     | The  |
tasks. It was first proposed by Vaswani et al.      f o  ll o  w   i n  g  is  the  architecture  diagram  of
| in  2017.    | The           | key  innovation  | of  the      T  r a  n  s  former.  |     |     |     |     |     |     |
| ------------ | ------------- | ---------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
| Transformer  | architecture  | is  the          | self-attention                      |     |     |     |     |     |     |

mechanism,  which  allows  it  to  excel  in  3.5.1 Self-Attention mechanism
| processing  | sequential  | data.  The  | Transformer  |     |     |     |     |     |     |
| ----------- | ----------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- |
employs a self-attention-based encoder-decoder  The self-attention mechanism is the core concept
|     |     |     |     | of  the  Transformer.  |     | It  enables  | the  | model  | to  |
| --- | --- | --- | --- | ---------------------- | --- | ------------ | ---- | ------ | --- |
structure.
|     |     |     |     | consider  | all  positions  | in  | the  input  | sequence  |     |
| --- | --- | --- | --- | --------- | --------------- | --- | ----------- | --------- | --- |

(1)  Encoder:  Composed  of  stacked  identical  simultaneously, unlike recurrent or convolutional
layers,  each  layer  includes  two  sub-layers:  a  neural networks that process sequentially. The
multi-head  self-attention  mechanism  and  a  self-attention  mechanism  assigns  varying
position-wise  fully  connected  feedforward  attention weights to different parts of the input
network.  Normalization  layers  and  residual  sequence,  thereby  capturing  semantic
connections are applied to the input and output  relationships more effectively. The mathematical
of the multi-head self-attention module.  expression for self-attention is as follows:
|                                                |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (2) Decoder: The decoder generates the output  |     |     |     |     |     |     | T   |     |     |
|                                                |     |     |     |     |     |     | Q K |     |     |
sequence using the representation produced by  A tte n tio n ( Q ,K ,V ) = s o ftm a x ( )V         (19)
| the encoder. Similar to the encoder, the decoder  |     |     |     |     |     |     | d   |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k

Fig. 9. Transformer architecture diagram

150

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
Firstly, extract the query vector (
151
Q ), key vector
( K ), and value vector ( V ) from the embedded
vector. Next, determine a score for each vector:
the score is equal toQ•K. Score normalization
(division d
k
) is used for gradient stability. Next,
use the softmax activation function to process
the scores. The weighted score of each input
vector is obtained by taking the softmax dot
product value. Sum up to produce the final result.
3.5.2 Multi-head attention mechanism
The Transformer model employs a multi-head
self-attention mechanism to enhance its ability to
capture dependencies among elements in a
sequence. The core principle of the attention
mechanism is that each token in a sequence can
aggregate information from other tokens,
enabling the model to better understand
contextual relationships. This is achieved by
mapping a query, a set of key-value pairs, and
an output (each represented as vectors) into an
attention function. The output is computed as a
weighted sum of the values, where the weights
are determined by a compatibility function
between the query and the corresponding keys.
Multi-head attention is equivalent to combining
multiple scaled dot-product attention
mechanisms. It effectively parallelizes the
processing of the query ( Q ), key (K ), and value
( V
Here,
) vectors, resulting in a final output that
integrates information from different attention
heads.
3.5.3 Positional encoding
Since the Transformer model does not rely on
recursion or convolution, it requires a method
to capture the relative or absolute position of
tokens within a sequence to effectively utilize
sequential order. Positional encoding is
introduced at the input level of the encoder and
decoder stacks. These positional encodings are
added to the input embeddings, sharing the
same dimensional space. They are calculated
using sine and cosine functions at different
frequencies as follows:
  t 

sin ,i =2k
 100002k/d 
PE(t) = (20)
i
  t  cos ,i =2k+1
  100002k/d 
t is the position in the sequence, d is the
vector dimension, and k is the natural number
used for indexing. By mapping each position to a
unique frequency using sine and cosine
functions, and converting the frequency into an
element in the embedding vector using the
corresponding sine and cosine functions, the
model can capture the position information when
processing the input sequence.
3.6 Comparison of Deep Learning Models
Datasets: This study conducted experiments
using the ETTm2, Electricity, Traffic, and
Weather datasets. Other datasets were excluded
due to insufficient periodicity, seasonality, or data
volume.
Experiment Details: To ensure consistency, all
models used an input sequence length of 24 and
a prediction length of 1. For the ETTm2,
Electricity, and Weather datasets, the first
variable was selected for prediction, representing
the high-useful load of an electric transformer oil
temperature, a user's hourly electricity
consumption, and atmospheric pressure,
respectively. For the Traffic dataset, the third
variable was selected, representing the hourly
road occupancy rate recorded by a sensor. All
models were trained using the Adam optimizer,
with MSE (Mean Squared Error) and MAE (Mean
Absolute Error) as evaluation metrics. PyTorch
was used for implementation.
Fig. 10 shows the prediction curves of four
models on the ETTm2 dataset, where the
horizontal axis represents the dataset, the
vertical axis represents the numerical size, the
blue curve represents the actual data value, and
the red curve represents the predicted value.
Fig. 11 The prediction curves of four models on
the ECL dataset, where the horizontal axis
represents the dataset, the vertical axis
represents the numerical size, the blue curve
represents the actual data value, and the red
curve represents the predicted value.
Fig. 12 The prediction curves of four models on
the Weather dataset, where the horizontal axis
represents the number of test sets, the vertical
axis represents the numerical size, the blue
curve represents the actual data value, and the
red curve represents the predicted value.

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
(a) RNN model (b) LSTM model
(c) GRU model (d) Transformer model
(e) LSTM-RNN model
Fig. 10. The prediction curves of four models on the ETTm2 dataset
(a) RNN model (b) LSTM model
152

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
(c) GRU model (d) Transformer model
(e) LSTM-RNN model
Fig. 11. The prediction curves of four models on the ECL dataset
(a) RNN model (b) LSTM model
(c) GRU model (d) Transformer model
153

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
(e) LSTM-RNN model
Fig. 12. The prediction curves of four models on the Weather dataset
(a) RNN model (b) LSTM model
(c) GRU model (d) Transformer model
(e) LSTM-RNN model
Fig. 13. The prediction curves of four models on the Traffic dataset
154

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

Table 1. Comparison of univariate prediction performance of four deep learning models

Model  Evaluating indicator   ETTm2  Electricity  Weather  Traffic
| RNN          | MSE  |     | 3.459  |     | 21.603  |     | 0.007  |     | 0.00112  |     |
| ------------ | ---- | --- | ------ | --- | ------- | --- | ------ | --- | -------- | --- |
|              | MAE  |     | 1.404  |     | 2.014   |     | 0.060  |     | 0.021    |     |
| LSTM         | MSE  |     | 3.480  |     | 19.821  |     | 0.008  |     | 0.00120  |     |
|              | MAE  |     | 1.414  |     | 1.848   |     | 0.066  |     | 0.020    |     |
| GRU          | MSE  |     | 3.454  |     | 19.524  |     | 0.007  |     | 0.00110  |     |
|              | MAE  |     | 1.402  |     | 1.889   |     | 0.062  |     | 0.021    |     |
| Transformer  | MSE  |     | 3.418  |     | 19.541  |     | 0.827  |     | 0.00122  |     |
|              | MAE  |     | 1.399  |     | 2.025   |     | 0.341  |     | 0.021    |     |
| LSTM-RNN     | MSE  |     | 3.454  |     | 21.583  |     | 0.007  |     | 0.00125  |     |
|              | MAE  |     | 1.404  |     | 1.941   |     | 0.062  |     | 0.021    |     |

Fig. 13 The prediction curves of four models on  learning  techniques  can  accurately  identify
the  Traffic  dataset,  where  the  horizontal  axis  complex patterns within and across time series
represents the number of test sets, the vertical  with  relatively  lower  human  resource
axis  represents  the  numerical  size,  the  blue  requirements.  However,  these  models  rely  on
curve represents the actual data value, and the  fewer structural assumptions, making them more
red curve represents the predicted value.  challenging to interpret and often requiring larger
|     |     |     |     | training  |     | datasets  | to  learn  | accurate  |     | models.  |
| --- | --- | --- | --- | --------- | --- | --------- | ---------- | --------- | --- | -------- |
We compare and analyze the performance of the  Additionally, since different sample types exhibit
four deep learning models mentioned above (as  distinct distribution patterns, a single fixed model
shown in Table 1).
cannot be universally applied, necessitating the
|     |     |     |     | use of multiple regression algorithms. This has  |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
The experimental data of various models listed in
|     |     |     |     | led  | to  | innovative  | forecasting  |     | methods  | that  |
| --- | --- | --- | --- | ---- | --- | ----------- | ------------ | --- | -------- | ----- |
Table 1 were analyzed and summarized in depth,
combine traditional statistical models with deep
and the conclusion is as follows: the Transformer
|                  |            |              |          | learning.      |     | These      | hybrid  | approaches        |     | have      |
| ---------------- | ---------- | ------------ | -------- | -------------- | --- | ---------- | ------- | ----------------- | --- | --------- |
| model  achieved  | the  best  | performance  | on  the  |                |     |            |         |                   |     |           |
|                  |            |              |          | significantly  |     | addressed  |         | the  limitations  |     | of  both  |
ETTm2 dataset, with minimum MAE and MSE
techniques. In recent years, many deep neural
values. The LSTM model achieved the minimum
|     |     |     |     | network  |     | models  | for  time  | series  | analysis  | have  |
| --- | --- | --- | --- | -------- | --- | ------- | ---------- | ------- | --------- | ----- |
MAE on the Electricity and Traffic datasets, i.e.
been proposed. These methods not only enable
the minimum tie error. The GRU model achieved  models  to  automatically  extract  features  and
the minimum mean square error (MSE) on the
learn complex temporal patterns but also apply
Electricity and Traffic datasets. The RNN model
assumptions like temporal smoothing, enhancing
achieved the best performance on the Weather
|     |     |     |     | model  | interpretability.  |     | As  | research  | on  | neural  |
| --- | --- | --- | --- | ------ | ------------------ | --- | --- | --------- | --- | ------- |
dataset, with minimum MAE and MSE values.
|     |     |     |     | network  |     | technologies  | continues  |     | to  | advance,  |
| --- | --- | --- | --- | -------- | --- | ------------- | ---------- | --- | --- | --------- |
The LSTM-RNN model generally outperforms the
deep  learning has become one of the hottest
standard RNN and also shows better results than
research topics in machine vision. Based on a
| the ordinary  | LSTM model on the ETTm2 and  |     |     |     |     |     |     |     |     |     |
| ------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
review of literature on time series forecasting and
Weather datasets. Overall, in most cases, the
deep learning, this paper primarily explores four
| combination  | of  the  two  | results  | in  a  certain  |     |     |     |     |     |     |     |
| ------------ | ------------- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
deep learning models for time series forecasting.
| performance improvement.  |     |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

4.2 Outlook
4. SUMMARY AND OUTLOOK

4.1 Summary  Deep learning has achieved significant results in
the field of time series prediction, and the future

Although  traditional  statistical  modeling  prospects  are  even  more  exciting.  With  the
techniques  incorporate  structural  assumptions  continuous advancement of technology, we have
into models, making them easier to understand,  reason to believe that deep learning will play a
they often require independent modeling of time  more  important  role  in  temporal  prediction,
series  data  in  modern  predictive  applications.  bringing  revolutionary  changes  to  various
| This approach significantly increases labor and     |     |     |     | industries.  |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| computational costs. Therefore, it is necessary to  |     |     |     |              |     |     |     |     |     |     |
find  more  efficient  techniques  capable  of  Firstly, at the algorithmic level, deep learning will
simultaneously  handling  varying  degrees  of  be further optimized and improved. At present,
relationships among two or more variables. Deep  models such as RNN, LSTM, and GRU have

155

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619

achieved good results in time series prediction.  (ChatGPT,  COPILOT,  etc)  and  text-to-image
In the future, new deep learning models such as  generators  have  been  used  during  writing  or
Transformers  and  graph  neural  networks  are  editing of this manuscript.
| expected  | to  | better  | handle  | time-series  |     | data,  |     |     |     |     |     |     |     |
| --------- | --- | ------- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
COMPETING INTERESTS
improve prediction accuracy and stability.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Secondly, at the application level, deep learning  Authors  have  declared  that  no  competing
| will play an important role in more fields. For  |     |     |     |     |     |     | interests exist.  |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
example, in the financial field, deep learning can

| be  used                                            | for  | stock  | price  |     | prediction,  | risk  | REFERENCES  |     |     |     |     |     |     |
| --------------------------------------------------- | ---- | ------ | ------ | --- | ------------ | ----- | ----------- | --- | --- | --- | --- | --- | --- |
| management, etc; In the field of energy, it can be  |      |        |        |     |              |       |             |     |     |     |     |     |     |
used  for  power  load  forecasting,  new  energy  Abdel-Nasser,  M.,  &  Mahmoud,  K.  (2019).
generation  forecasting,  etc;  In  the  field  of  Accurate  photovoltaic  power  forecasting
transportation,  it  can  be  used  for  traffic  flow  models  using  deep  LSTM-RNN.  Neural
prediction, flight delay prediction, etc. With the  Computing and Applications, 31(7), 2727-
| continuous accumulation of data, the application  |     |     |     |     |     |     |     | 2740.  |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
of  deep  learning  in  time  series  prediction  will  Durbin, J., & Koopman, S. J. (2012). Time series
become more widespread.  analysis by state space methods (2nd ed.).
|     |     |     |     |     |     |     |     | OUP Oxford.  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
In addition, cross domain fusion of deep learning
Eslin, G. P., & Agon, C. (2012). Time-series data
in  temporal  prediction  will  also  become  a  mining. ACM Computing Surveys (CSUR),
| development  |     | trend.  | For  | example,  | combining  |     |     | 45(1), 1-34.  |     |     |     |     |     |
| ------------ | --- | ------- | ---- | --------- | ---------- | --- | --- | ------------- | --- | --- | --- | --- | --- |
deep learning with statistics, chaos theory, etc. is
|           |             |     |              |     |                 |     | Fang, W., Chen,  |           |     | Y., et     | al. (2021).  | Survey           | on  |
| --------- | ----------- | --- | ------------ | --- | --------------- | --- | ---------------- | --------- | --- | ---------- | ------------ | ---------------- | --- |
| expected  | to further  |     | improve the  |     | generalization  |     |                  |           |     |            |              |                  |     |
|           |             |     |              |     |                 |     |                  | research  | of  | RNN-based  |              | spatio-temporal  |     |
ability and robustness of prediction models. At  sequence prediction algorithms. Journal on
the same time, by combining domain knowledge,
Big Data, 3(3), 97-110.
deep learning can achieve finer grained temporal
Gers, F. A., Schmidhuber, J., & Cummin, S. F.
prediction, providing decision-makers with more  (2000).  Learning  to  forget:  Continual
targeted recommendations.  prediction with LSTM. Neural Computation,

12(10), 2451-2471.
| Finally,  | with  | the  continuous  |     |     | improvement  | of  |     |     |     |     |     |     |     |
| --------- | ----- | ---------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Hanen, B., Ali, A. B., & Riadh, I. F. (2024). A Bi-
computing power, the real-time performance of
|                 |     |               |     |             |     |           |     | GRU-based          |     | encoder–decoder  |         | framework     |     |
| --------------- | --- | ------------- | --- | ----------- | --- | --------- | --- | ------------------ | --- | ---------------- | ------- | ------------- | --- |
| deep  learning  |     | in  temporal  |     | prediction  |     | will  be  |     |                    |     |                  |         |               |     |
|                 |     |               |     |             |     |           |     | for  multivariate  |     | time             | series  | forecasting.  |     |
guaranteed. In the future, real-time prediction will
Soft Computing, 28(9-10), 6775-6786.
become possible, providing more accurate and
Jin, K. H., Wi, J. A., Lee, E. J., et al. (2021).
real-time decision support for various industries.
TrafficBERT: Pre-trained model with large-

|     |     |     |     |     |     |     |     | scale  | data  | for  | long-range  | traffic  | flow  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---- | ----------- | -------- | ----- |
5. CONCLUSION
|     |     |     |     |     |     |     |     | forecasting.  |     | Expert  |     | Systems  | with  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | -------- | ----- |

Applications, 186, 115738.
This paper presents a systematic review of time
series  forecasting  methods  based  on  deep  Li,  S.  Y.,  Jin,  X.  Y.,  Xuan,  Y.,  et  al.  (2019).
|            |            |             |     |      |              |     |     | Enhancing  |     | the  locality  | and  | breaking  | the  |
| ---------- | ---------- | ----------- | --- | ---- | ------------ | --- | --- | ---------- | --- | -------------- | ---- | --------- | ---- |
| learning.  | It  first  | introduces  |     | the  | background,  |     |     |            |     |                |      |           |      |
memory bottleneck of Transformer on time
significance, and various methods of time series
forecasting. Then, it provides a detailed overview  series  forecasting.  In  Proceedings  of
NeurIPS 2019, 5244-5254.
of representative deep learning models in this
|          |            |     |       |        |       |      | Liu,  | Y.,  Hu,  | T.,  | Zhang,  | H.,  | et  al.  | (2024).  |
| -------- | ---------- | --- | ----- | ------ | ----- | ---- | ----- | --------- | ---- | ------- | ---- | -------- | -------- |
| domain,  | including  |     | RNN,  | LSTM,  | GRU,  | and  |       |           |      |         |      |          |          |
Transformer models. Subsequently, it conducts  ITransformer:  Inverted  transformers  are
|              |             |     |              |     |     |         |     | effective    | for  | time  | series  | forecasting.   | In  |
| ------------ | ----------- | --- | ------------ | --- | --- | ------- | --- | ------------ | ---- | ----- | ------- | -------------- | --- |
| comparative  | prediction  |     | experiments  |     | on  | public  |     |              |      |       |         |                |     |
|              |             |     |              |     |     |         |     | Proceedings  |      | of    | the     | International  |     |
datasets and evaluates the performance of these
Conference on Learning Representations
| models.     | Finally,  | it    | explores  |     | future    | research  |     |               |     |     |     |     |     |
| ----------- | --------- | ----- | --------- | --- | --------- | --------- | --- | ------------- | --- | --- | --- | --- | --- |
| directions  | for       | deep  | learning  |     | in  time  | series    |     | (ICLR 2024).  |     |     |     |     |     |
Liu, Y., Wu, H. X., Wang, J. M., et al. (2022).
forecasting, offering valuable insights for further
Non-stationary transformers: Exploring the
advancements in this field.
|     |     |     |     |     |     |     |     | stationarity  |     | in  time  | series  | forecasting.  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------- | ------------- | --- |
DISCLAIMER (ARTIFICIAL INTELLIGENCE)  Advances  in  Neural  Information
Processing Systems, 35, 9881-9893.

Author(s) hereby declare that NO generative AI
Michael, E. N., Bansal, C. R., Ismail, A. A. A., et
technologies such as Large Language Models  al.  (2024).  A  cohesive  structure  of  Bi-

156

Chen et al.; J. Basic Appl. Res. Int., vol. 30, no. 6, pp. 140-157, 2024; Article no.JOBARI.12619
directional long-short-term memory in Neural Information Processing Systems,
(BiLSTM)-GRU for predicting hourly solar 30, 5998-6008.
radiation. Renewable Energy, 222, Waqas, M., & Humphries, W. U. (2024). A critical
119943-. review of RNN and LSTM variants in
Qiang, C., Shu, W., Qiang, L., et al. (2020). MV- hydrological time series predictions.
RNN: A Multi-View Recurrent M e t hodsX, 13102946-102946.
Neural Network for Sequential Wen, Q. S., Zhou, T., Zhang, C. L., et al. (2023).
Recommendation. IEEE Transactions on Transformers in time series: A survey. In
Knowledge and Data Engineering, 32(2), Proceedings of the International Joint
317-331. Conference on Artificial Intelligence (IJCAI
Shaowei, P., Bo, Y., Shukai, W., et al. (2023). Oil 2023), 6778-6786.
well production prediction based on CNN- Wu, H. X., Xu, J. H., Wang, J. M., et al. (2021).
LSTM model with self-attention Autoformer: Decomposition transformers
mechanism. Energy, 284. with auto-correlation for long-term series
Shaowei, P., Bo, Y., Shukai, W., et al. (2023). Oil forecasting. In Proceedings of NeurIPS
well production prediction based on CNN- 2021, 34, 22419-22430.
LSTM model with self-attention Zhang, Y. F., Wu, R., Dascalu, S. M., et al.
mechanism. Energy, 284. (2024). Multi-scale transformer pyramid
Vaswani, A., Shazeer, N., Parmar, N., et al. networks for multivariate time series
(2017). Attention is all you need. Advances forecasting. IEEE Access, 14731-14741.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of the publisher and/or the editor(s). This publisher and/or the editor(s) disclaim responsibility for
any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
_________________________________________________________________________________
© Copyright (2024): Author(s). The licensee is the journal publisher. This is an Open Access article distributed under the terms
of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0), which permits unrestricted use,
distribution, and reproduction in any medium, provided the original work is properly cited.
Peer-review history:
The peer review history for this paper can be accessed here:
https://prh.ikprress.org/review-history/12619
157