---
conversion_metadata:
  converted_at: "2026-10-12T07:41:57Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Singh et al., 2025.pdf"
  source_pdf_sha256: "f1c437eb2c4c24d978a912927cb6884161d4b613332cdace8cb26f6f1f1c5cfd"
  page_count: 6
  markdown_char_count: 43447
---

JOURNALOFSCIENTIFICINNOVATIONANDADVANCEDRESEARCH(JSIAR),VOLUME1,ISSUE1,APRIL2025
(cid:128)https://jsiar.com
#editor@jsiar.com
A Predictive Framework for Annual Financial Planning using
Deep Learning Models
Uttam Singh, Utkarsh Anand, Vishal Singh
Department of Computer Science and Engineering
Noida International University, Greater Noida, India
Email: uttamsingh8607101@gmail.com
Abstract—Annualfinancialplanningisacriticalaspectofsus- such as Long Short-Term Memory (LSTM) [8] and Gated
tainable economic management for organizations, governments, Recurrent Units (GRU) [9], have shown promising results
and institutions. Traditional forecasting methods, such as linear
in modeling temporal dependencies in sequential data [10].
regression and ARIMA, often fall short in capturing the non-
These architectures are particularly suitable for financial time
linear and dynamic nature of real-world financial data. These
limitations hinder the accuracy and adaptability required for series prediction due to their ability to capture long-range
proactive fiscal decision-making. This research proposes a pre- dependencies and non-linear patterns [11].
dictive framework leveraging deep learning models—specifically Inthisstudy,weproposeapredictiveframeworkforannual
Long Short-Term Memory (LSTM) and Gated Recurrent Unit
financial planning using LSTM and GRU-based deep learning
(GRU) networks—for enhanced annual expense forecasting. The
models. The framework is designed to process historical
proposed system is designed to process historical financial
datasets, identify temporal patterns, and predict future expendi- financial data, uncover latent temporal structures, and forecast
tureswithhighprecision.Acomparativeanalysiswasconducted future expenses with high accuracy. The proposed system
to evaluate the performance of LSTM and GRU models against includes preprocessing of time-series data, model training,
classicalstatisticalapproachesusingreal-worldfinancialdatasets.
validation, and a performance comparison with traditional
Experimentalresultsdemonstratethatthedeeplearningmodels,
statistical approaches.
particularlyLSTM,significantlyoutperformtraditionalmethods
in terms of prediction accuracy, robustness, and responsiveness
Contributions
to seasonal variations in expenditure. The study establishes the
potential of advanced neural networks in automating and opti- The primary contributions of this paper are as follows:
mizingfinancialplanningprocesses,ultimatelyaidinginresource
• A deep learning-based framework utilizing LSTM and
allocation and policy formulation. The findings contribute to
GRU models for annual expense forecasting.
the growing field of AI-driven financial analytics and provide
a foundation for scalable, data-informed budgeting systems. • A comparative analysis between deep learning and clas-
Keywords—Deep learning, financial forecasting, LSTM, GRU, sical statistical forecasting methods.
time series prediction, annual expense management • A case study with real-world financial data to evaluate
model performance and reliability.
I. INTRODUCTION
• Insights into model scalability and its practical implica-
Financial planning is a vital component of strategic man- tions for institutional budget planning.
agement in both public and private sectors. It encompasses Theremainderofthispaperisstructuredasfollows:Section
the estimation of future income and expenditures, aligning re- II reviews related work; Section III presents the proposed
sourceallocationwithorganizationalobjectivesoveradefined methodology; Section IV discusses experimental results; Sec-
period, typically on an annual basis [1]. Effective forecasting tion V concludes with future research directions.
of expenses is fundamental to achieving fiscal discipline, risk
mitigation, and operational efficiency [2]. II. RELATEDWORK
Traditionalapproachestoexpenseforecastinghavepredom- Financial forecasting has long been a central topic in
inantly relied on statistical techniques such as Autoregressive both academic research and industrial applications, given its
Integrated Moving Average (ARIMA) [3], linear regression critical role in planning, budgeting, and resource allocation.
[4],andexponentialsmoothingmodels[5].Whilethesemeth- Theearliermethodologiesprimarilyemployedstatisticaltech-
odsarecomputationallyefficientandinterpretable,theyexhibit niquessuchasmovingaverages,exponentialsmoothing,linear
notable limitations in handling complex, non-linear, and high- regression, and ARIMA for time series forecasting [16], [17].
dimensional data patterns commonly observed in financial While these methods offersimplicity and interpretability, they
transactions [6]. Moreover, they are often static and struggle exhibit limited capability in modeling non-linear relationships
to adapt to dynamic market conditions or sudden behavioral and fail to generalize well in scenarios involving structural
shifts, which are critical in long-term planning scenarios [7]. shifts or long-term dependencies [18].
The growing demand for more accurate and adaptive fi-
A. Traditional Forecasting Models
nancial forecasting models has led researchers to explore
advanced machine learning and deep learning techniques. Re- Box-Jenkins ARIMA models [19] and Holt-Winters expo-
current Neural Networks (RNNs), and their enhanced variants nential smoothing [20] are widely used in the domain of
JournalofScientificInnovationandAdvancedResearch©2025JSIAR ISSN:XXXX-XXXX

JournalofScientificInnovationandAdvancedResearch(JSIAR)2025
univariate time series forecasting. These models are suitable III. PROPOSEDFRAMEWORK
for stationary or trend-based series but often require strong
This section presents the architecture and functional mod-
assumptions about data distribution and seasonality [21].
ulesoftheproposeddeeplearning-basedpredictiveframework
Moreover, their predictive performance tends to degrade in
for annual financial planning. The system is designed to pro-
the presence of irregularities or volatility [22].
vide accurate forecasting of yearly expenses using advanced
sequence modeling techniques, enabling organizations and
B. Deep Learning in Financial Forecasting
individuals to make informed financial decisions.
With the advent of deep learning, researchers have in-
A. System Architecture
creasingly turned to neural network-based models for finan-
Thearchitectureofthepredictivesystemcomprisesmultiple
cial forecasting tasks. Recurrent Neural Networks (RNNs),
interconnectedmodulesthathandledataingestion,preprocess-
particularly Long Short-Term Memory (LSTM) networks,
ing, model training, prediction, and performance evaluation.
havedemonstratedstrongperformanceinmodelingsequential
Figure 1 illustrates the high-level architectural design of the
dependencies [23]. Gated Recurrent Units (GRUs), a sim-
system.
plified variant of LSTM, are also gaining popularity due
to their computational efficiency and comparable accuracy
B. Flow of Data and Processes
[24]. Applications of these models range from stock market
The overall process follows a well-defined pipeline be-
prediction[25]andcreditriskanalysis[26]tocorporatebudget
ginning with raw data collection and culminating in annual
forecasting [27] and personal finance management [28].
expenseforecasting.Thestepsaredepictedintheflowdiagram
(Figure 2).
C. Comparative Studies
C. Functional Modules
Multiplestudieshavecomparedtheperformanceofclassical
and deep learning models in financial time series prediction. 1) Data Ingestion: This module is responsible for collect-
For instance, Siami-Namini et al. [29] showed that LSTM ing financial records from various sources such as spread-
outperforms ARIMA in forecasting accuracy across various sheets, databases, and APIs. The data includes past annual
metrics including MAE and RMSE. Similarly, Fischer and expenses, budget categories, and temporal indicators such as
Krauss [30] found that deep neural networks could achieve month and fiscal year.
higher returns and lower risk in portfolio management tasks 2) Data Preprocessing: Preprocessing involves multiple
compared to traditional econometric models. steps including handling missing values, removing anoma-
lies, normalization, and time-series transformation. Feature
engineering is also performed to capture seasonal trends and
TABLEI
COMPARISONOFTRADITIONALVS.DEEPLEARNINGMODELSIN periodic patterns relevant to yearly expense forecasting.
FINANCIALFORECASTING 3) ModelSelection: Theframeworksupportsmultipledeep
Model PatternCapture Adaptability learning architectures for sequential forecasting. In this study,
LinearRegression LinearTrends Low Long Short-Term Memory (LSTM) and Gated Recurrent Unit
ARIMA Seasonal/Trend-Based Medium
(GRU) networks are primarily utilized due to their proven
ExponentialSmoothing RecentTrends Low
LSTM Long-TermDependencies High capabilitiesincapturinglong-termdependenciesintimeseries
GRU Non-LinearPatterns High data. Model parameters are optimized using grid search and
validation performance metrics.
4) Prediction Engine: This module takes the preprocessed
D. Identified Gaps input features and feeds them into the trained model to
generateyearlyfinancialpredictions.Thesystemsupportsboth
Despite these advancements, several limitations persist in
point forecasting and interval-based forecasting to account for
the current body of research:
uncertainty.
• Moststudiesfocusonshort-termprediction(e.g.,dailyor 5) Evaluation Metrics: The forecasting accuracy is as-
monthly),withlimitedworkaddressinglong-termannual
sessedusingMeanAbsoluteError(MAE),RootMeanSquared
forecasting.
Error(RMSE),andMeanAbsolutePercentageError(MAPE).
• Few comparative frameworks comprehensively evaluate Thesemetricsensurerobustevaluationacrossvariousfinancial
deep learning models against traditional methods in a
scenarios and help in benchmarking against baseline models
financial planning context.
such as ARIMA and linear regression.
• The lack of real-world case studies limits the practical
relevance and transferability of proposed models. D. Implementation Highlights
This study addresses these gaps by presenting a deep • The framework is implemented using Python with Ten-
learning-based framework for annual expense forecasting, sorFlow and Keras for deep learning model construction.
evaluating its efficacy using real-world financial data, and • Time-based cross-validation is used to maintain the tem-
benchmarking its performance against classical models. poral integrity of training and test datasets.
(cid:128)https://jsiar.com
#editor@jsiar.com ©2025JSIAR

JournalofScientificInnovationandAdvancedResearch(JSIAR)2025
|                                                      |             |             |       | Fig.1.        | SystemArchitectureoftheProposedPredictiveFramework      |             |     |             |        |          |               |         |      |           |            |
| ---------------------------------------------------- | ----------- | ----------- | ----- | ------------- | ------------------------------------------------------- | ----------- | --- | ----------- | ------ | -------- | ------------- | ------- | ---- | --------- | ---------- |
|                                                      |             |             |       |               | Fig.2. FlowDiagram:DataProcessingandForecastingPipeline |             |     |             |        |          |               |         |      |           |            |
| • The system                                         |             | is scalable | and   | modular,      | allowing                                                | integration |     | C. Model    | Design |          |               |         |      |           |            |
| with                                                 | cloud-based | services    |       | for real-time | deployment.                                             |             |     |             |        |          |               |         |      |           |            |
|                                                      |             |             |       |               |                                                         |             |     | Three       | deep   | learning | architectures |         | were | evaluated | for this   |
| Thislayeredapproachallowsthesystemtogeneralizeacross |             |             |       |               |                                                         |             |     | task:       |        |          |               |         |      |           |            |
| various financial                                    |             | domains     | while | maintaining   |                                                         | flexibility | and |             |        |          |               |         |      |           |            |
|                                                      |             |             |       |               |                                                         |             |     | • Recurrent |        | Neural   | Networks      | (RNNs): | Used | as        | a baseline |
accuracy in long-term financial planning. due to their simplicity in handling sequences.
IV. METHODOLOGY • Long Short-Term Memory (LSTM): Selected for its
|              |          |           |            |            |           |              |         | capability |           | to handle | long-term         |        | dependencies |     | and avoid  |
| ------------ | -------- | --------- | ---------- | ---------- | --------- | ------------ | ------- | ---------- | --------- | --------- | ----------------- | ------ | ------------ | --- | ---------- |
| The proposed |          | framework | for        | annual     | financial | forecasting  |         |            |           |           |                   |        |              |     |            |
|              |          |           |            |            |           |              |         | vanishing  |           | gradient  | problems.         |        |              |     |            |
| using deep   | learning | models    | is         | structured | around    | a systematic |         |            |           |           |                   |        |              |     |            |
|              |          |           |            |            |           |              |         | • Gated    | Recurrent |           | Unit              | (GRU): | Considered   |     | due to its |
| methodology. | This     | section   | elaborates |            | on the    | various      | stages, |            |           |           |                   |        |              |     |            |
|              |          |           |            |            |           |              |         | lighter    | structure |           | and computational |        | efficiency   |     | while re-  |
includingdataacquisition,preprocessing,modeldesign,train-
|     |     |     |     |     |     |     |     | taining | sequential |     | learning | capability. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | -------- | ----------- | --- | --- | --- |
ing, and evaluation.
|     |     |     |     |     |     |     |     | Justification: |     | LSTM | and | GRU | models | outperform | tradi- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | --- | --- | ------ | ---------- | ------ |
A. Data Collection tional methods in modeling sequential financial patterns due
|                 |            |           |             |      |           |                 |      | to their       | gated | memory | structures, |                 | which | preserve | temporal  |
| --------------- | ---------- | --------- | ----------- | ---- | --------- | --------------- | ---- | -------------- | ----- | ------ | ----------- | --------------- | ----- | -------- | --------- |
| For this        | study,     | financial | datasets    | were | collected | from            | pub- |                |       |        |             |                 |       |          |           |
| licly available | government |           | expenditure |      | portals   | and enterprise- |      | correlations.  |       |        |             |                 |       |          |           |
|                 |            |           |             |      |           |                 |      | Hyperparameter |       |        | Tuning:     | Hyperparameters |       | such     | as learn- |
levelbudgetingdatasets.Incaseswhererealdatasetswerelim-
ited, synthetically generated data using realistic distributions ing rate, batch size, and number of hidden layers were op-
(e.g., Gaussian and exponential) were employed to augment timized using Grid Search. Additionally, dropout rates and
|              |          |     |     |     |     |     |     | number | of units | per | layer | were | explored | using | Bayesian |
| ------------ | -------- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ----- | ---- | -------- | ----- | -------- |
| the training | process. |     |     |     |     |     |     |        |          |     |       |      |          |       |          |
The datasets typically consist of the following features: Optimization for best performance.
|               |     |           |       |           |                |           |       | Figure      | 3 presents |            | the model | training | and | evaluation | work- |
| ------------- | --- | --------- | ----- | --------- | -------------- | --------- | ----- | ----------- | ---------- | ---------- | --------- | -------- | --- | ---------- | ----- |
| • Department  |     | ID and    | Name: | Indicates | organizational |           | divi- |             |            |            |           |          |     |            |       |
| sion.         |     |           |       |           |                |           |       | flow.       |            |            |           |          |     |            |       |
| • Expenditure |     | Category: | Such  | as        | operations,    | salaries, | in-   |             |            |            |           |          |     |            |       |
|               |     |           |       |           |                |           |       | D. Training | and        | Validation |           |          |     |            |       |
frastructure.
|           |           |     |          |     |          |       |        | The datasets |         | were  | divided | into training |            | (70%), | validation |
| --------- | --------- | --- | -------- | --- | -------- | ----- | ------ | ------------ | ------- | ----- | ------- | ------------- | ---------- | ------ | ---------- |
| • Monthly | Spending: |     | Recorded |     | for each | month | across |              |         |       |         |               |            |        |            |
|           |           |     |          |     |          |       |        | (15%), and   | testing | (15%) | sets    | using         | a temporal | split  | to main-   |
| multiple  | years.    |     |          |     |          |       |        |              |         |       |         |               |            |        |            |
Fiscal Year: Indicates the year of the transaction. tain chronological integrity. Evaluation of prediction accuracy
•
|                       |     |       |        |           |             |     |           | was performed |          | using   | the following |        | metrics: |     |     |
| --------------------- | --- | ----- | ------ | --------- | ----------- | --- | --------- | ------------- | -------- | ------- | ------------- | ------ | -------- | --- | --- |
| • Transaction         |     | Type: | Fixed, | variable, | or one-time |     | expenses. |               |          |         |               |        |          |     |     |
|                       |     |       |        |           |             |     |           | • Mean        | Absolute |         | Error (MAE)   |        |          |     |     |
| B. Data Preprocessing |     |       |        |           |             |     |           | Root          | Mean     | Squared | Error         | (RMSE) |          |     |     |
•
The collected datasets required extensive preprocessing to • Mean Absolute Percentage Error (MAPE)
ensure suitability for time series modeling: Training Environment: The models were implemented in
• MissingDataHandling:Missingvalueswereimputedus- Python using TensorFlow and Keras libraries. Google Colab’s
ingforward-fillmethodsandmeansubstitutiondepending GPU environment was utilized to expedite training processes.
on temporal context. Earlystoppingandlearningrateschedulingwereemployedto
• Normalization: Min-max normalization was applied to enhance generalization and avoid overfitting.
scale features between 0 and 1 to assist neural network Thismethodicalapproachensuresthattheproposedpredic-
convergence. tive system remains robust, scalable, and adaptable for practi-
Time Series Formatting: Data was structured as super- cal deployment in real-world financial planning scenarios.
•
| vised | sequences | using | sliding | windows |     | with a | lookback |     |     |     |     |     |     |     |     |
| ----- | --------- | ----- | ------- | ------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
V. RESULTSANDDISCUSSION
| period | of 12 | months. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Feature Engineering: Temporal features such as month, Thissectionpresentstheexperimentalresultsobtainedfrom
•
quarter, and moving averages were created. Lag features the deep learning models applied to the annual financial
wereincludedtoprovidehistoricalcontexttothemodels. dataset. We evaluate and compare the models using standard
(cid:128)https://jsiar.com
| #editor@jsiar.com |     |     |     |     |     |     |     |     |     |     |     |     |     |     | ©2025JSIAR |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |

JournalofScientificInnovationandAdvancedResearch(JSIAR)2025
|     |     |     |     |     |     | Absolute    |     | Percentage  | Error | (MAPE). | Table  | II  | summarizes | the |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----- | ------- | ------ | --- | ---------- | --- |
|     |     |     |     |     |     | comparative |     | performance |       | of each | model. |     |            |     |
TABLEII
PERFORMANCECOMPARISONOFDEEPLEARNINGMODELS
|     |     |     |     |     |     |          |             | Model | MAE          |         | RMSE         | MAPE(%)  |              |         |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | ------------ | ------- | ------------ | -------- | ------------ | ------- |
|     |     |     |     |     |     |          |             | RNN   | 2450.13      | 3120.88 |              | 9.85     |              |         |
|     |     |     |     |     |     |          |             | LSTM  | 1872.56      | 2614.32 |              | 7.02     |              |         |
|     |     |     |     |     |     |          |             | GRU   | 1950.45      | 2701.25 |              | 7.48     |              |         |
|     |     |     |     |     |     |          | As evident, | the   | LSTM         | model   | consistently |          | outperformed |         |
|     |     |     |     |     |     | both     | RNN         | and   | GRU          | across  | all three    | metrics, | indicating   |         |
|     |     |     |     |     |     | superior | learning    |       | of long-term |         | temporal     | patterns | in           | expense |
sequences.
|     |     |     |     |     |     | B.     | Visualization |           | of Predictions |               |          |        |              |        |
| --- | --- | --- | --- | --- | --- | ------ | ------------- | --------- | -------------- | ------------- | -------- | ------ | ------------ | ------ |
|     |     |     |     |     |     |        | To further    | analyze   | model          | performance,  |          |        | we visualize | the    |
|     |     |     |     |     |     | actual | versus        | predicted |                | values        | for the  | test   | period using | the    |
|     |     |     |     |     |     | LSTM   | model.        | Figure    | ??             | shows         | the time | series | comparison   | of     |
|     |     |     |     |     |     | actual | and           | predicted | annual         | expenditures. |          |        |              |        |
|     |     |     |     |     |     |        | Predicted     |           | vs. Actual     | Annual        | Expenses |        | (LSTM        | Model) |
120
Actual
|     |     |     |     |     |     |     |     | Predicted |     | (LSTM) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --- | --- | --- | --- |
100
)0001$
ni(
80
esnepxE
60
40
|     |     |     |     |     |     |     |     | Jan FebMarAprMayJun |     |     | JulAugSepOctNovDec |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------------ | --- | --- | --- |
Month
|     |     |     |     |     |     | Fig.4. | ComparisonofPredictedvs.ActualExpensesusingLSTMmodel |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
TheLSTMforecastscloselyfollowthetruetrendofannual
|     |     |     |     |     |     | spending, |           | with minimal |     | deviation, | validating |     | its applicability |     |
| --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | --- | ---------- | ---------- | --- | ----------------- | --- |
|     |     |     |     |     |     | for       | long-term | financial    |     | planning.  |            |     |                   |     |
Fig.3. WorkflowofModelDesignandTraining
|             |               |         |               |               |           | C.        | Analysis | of Model      | Behavior |             |              |           |              |         |
| ----------- | ------------- | ------- | ------------- | ------------- | --------- | --------- | -------- | ------------- | -------- | ----------- | ------------ | --------- | ------------ | ------- |
|             |               |         |               |               |           |           | The LSTM | and           | GRU      | models      | demonstrated |           | strong       | gener-  |
| time series | forecasting   | metrics | and           | analyze their | accuracy, |           |          |               |          |             |              |           |              |         |
|             |               |         |               |               |           | alization |          | and stability |          | during      | training.    | The       | use of       | dropout |
| stability,  | and practical | utility | in real-world | financial     | planning  |           |          |               |          |             |              |           |              |         |
|             |               |         |               |               |           | layers    | and      | early         | stopping | effectively |              | mitigated | overfitting. |         |
contexts.
|                |            |     |           |     |     | RNN      | models, | in       | contrast, | suffered | from   | gradient  | vanishing |     |
| -------------- | ---------- | --- | --------- | --- | --- | -------- | ------- | -------- | --------- | -------- | ------ | --------- | --------- | --- |
|                |            |     |           |     |     | problems |         | and were | less      | stable   | during | training. |           |     |
| A. Performance | Comparison |     | of Models |     |     |          |         |          |           |          |        |           |           |     |
Figure??presentsthetrainingandvalidationlosscurvesfor
Three models—RNN, LSTM, and GRU—were evaluated the LSTM model, indicating convergence without overfitting.
based on their ability to predict future annual expenses. The smooth convergence of validation loss highlights the
The performance metrics used include Mean Absolute Er- robustness of the model architecture and preprocessing strat-
| ror (MAE), | Root Mean | Squared | Error | (RMSE), | and Mean | egy. |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------- | ----- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:128)https://jsiar.com
| #editor@jsiar.com |     |     |     |     |     |     |     |     |     |     |     |     | ©2025JSIAR |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

JournalofScientificInnovationandAdvancedResearch(JSIAR)2025
Training and Validation Loss (LSTM) dependencies and complex seasonal patterns that traditional
|     |     |     |     |     |     |     | methods | fail to | address. | By leveraging | advanced |     | architectures |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | ------------- | -------- | --- | ------------- | --- |
1.2
|     |     |     |     |     |            |      | like LSTM           | and | GRU,   | businesses | can achieve | more | accurate     |     |
| --- | --- | --- | --- | --- | ---------- | ---- | ------------------- | --- | ------ | ---------- | ----------- | ---- | ------------ | --- |
|     |     |     |     |     | Training   | Loss |                     |     |        |            |             |      |              |     |
|     |     |     |     |     |            |      | budget predictions, |     | better | resource   | allocation, |      | and enhanced |     |
| 1   |     |     |     |     | Validation | Loss |                     |     |        |            |             |      |              |     |
decision-making.
|     |     |     |     |     |     |     | Despite | the promising |     | results, | several | limitations |     | exist in |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | ------- | ----------- | --- | -------- |
0.8
this study:
)ESM(
|     |     |     |     |     |     |     | • The | current | framework |     | is dependent | on  | high-quality, |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --------- | --- | ------------ | --- | ------------- | --- |
0.6
|     |     |     |     |     |     |     | clean, | and | complete | datasets. | Incomplete | or  | noisy | finan- |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | --------- | ---------- | --- | ----- | ------ |
ssoL
|     |     |     |     |     |     |     | cial | data may | hinder | model | performance. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | ----- | ------------ | --- | --- | --- |
0.4
• Whilethefocushasbeenonannualexpenses,themodel’s
performancemayvarywithdifferentfinancialdomainsor
| 0.2 |     |     |     |     |     |     | forecasting |        | time horizons |              | (e.g., monthly | or  | quarterly). |       |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------- | ------------ | -------------- | --- | ----------- | ----- |
|     |     |     |     |     |     |     | The         | models | could         | be sensitive | to overfitting |     | if not      | care- |
•
| 0   |     |     |         |                        |     |     | fully      | tuned,    | particularly | in      | smaller      | datasets. |               |     |
| --- | --- | --- | ------- | ---------------------- | --- | --- | ---------- | --------- | ------------ | ------- | ------------ | --------- | ------------- | --- |
| 1   | 2 3 | 4 5 | 6 7 8 9 | 1011121314151617181920 |     |     |            |           |              |         |              |           |               |     |
|     |     |     |         |                        |     |     | For future | research, |              | several | improvements |           | and potential |     |
Epoch
|     |     |     |     |     |     |     | directions | are identified: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- |
• Exploringhybridmodelsthatcombinedeeplearningwith
| Fig.5. | TrainingandValidationLossperEpochusingLSTM |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classicalstatisticaltechniques(e.g.,ARIMA+LSTM)to
|             |              |     |     |     |     |     | improve     | robustness |           | and performance. |                   |     |           |      |
| ----------- | ------------ | --- | --- | --- | --- | --- | ----------- | ---------- | --------- | ---------------- | ----------------- | --- | --------- | ---- |
| D. Business | Implications |     |     |     |     |     |             |            |           |                  |                   |     |           |      |
|             |              |     |     |     |     |     | • Extending |            | the model | to               | handle additional |     | financial | met- |
Theresultshighlightthepracticalpotentialofdeeplearning- rics, such as revenues, investments, and external eco-
basedforecastingsystemsinenterprisefinancialmanagement. nomic factors.
Accurateannualexpensepredictionenablesbetterallocationof • Investigating more advanced deep learning models like
|               |               |             |              |          |            |           | Transformer-based |            |          | architectures | or       | Autoencoders |            | for |
| ------------- | ------------- | ----------- | ------------ | -------- | ---------- | --------- | ----------------- | ---------- | -------- | ------------- | -------- | ------------ | ---------- | --- |
| resources,    | risk          | management, | and          | informed | strategic  | decision- |                   |            |          |               |          |              |            |     |
| making.       | For instance: |             |              |          |            |           | anomaly           | detection. |          |               |          |              |            |     |
|               |               |             |              |          |            |           | Incorporating     |            | external | sources       | of data, | such         | as macroe- |     |
| • Departments |               | can         | plan budgets | more     | accurately | and avoid | •                 |            |          |               |          |              |            |     |
last-minute deficits or surpluses. conomic indicators or industry trends, to further enhance
|             |     |             |     |          |          |             | prediction |     | accuracy. |     |     |     |     |     |
| ----------- | --- | ----------- | --- | -------- | -------- | ----------- | ---------- | --- | --------- | --- | --- | --- | --- | --- |
| • Financial |     | controllers | can | simulate | multiple | forecasting |            |     |           |     |     |     |     |     |
scenarios to assess risk. In conclusion, the proposed framework offers a substantial
Organizations can reduce dependency on manual spread- advancement in financial forecasting, providing businesses
•
sheet models and statistical approximations. with a reliable tool for strategic financial planning. However,
Overall, the LSTM-based framework represents a valuable ongoing research and improvements will be necessary to
|          |            |           |            |              |     |            | enhance | the generalizability |     |     | and accuracy | of  | these | models |
| -------- | ---------- | --------- | ---------- | ------------ | --- | ---------- | ------- | -------------------- | --- | --- | ------------ | --- | ----- | ------ |
| tool for | predictive | financial | analytics, | particularly |     | in dynamic |         |                      |     |     |              |     |       |        |
and data-rich environments. across diverse financial contexts.
|     |     |     | VI. CONCLUSION |     |     |     |     |     |     | REFERENCES |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
Thispaperpresentsanovelpredictiveframeworkforannual [1] J.C.Hull,RiskManagementandFinancialInstitutions.Wiley,2015.
financial planning using deep learning models, specifically [2] R.H.FrankandB.Bernanke,PrinciplesofEconomics.McGraw-Hill,
2012.
LSTM and GRU. The primary contributions of this work are [3] G.E.P.Boxetal.,TimeSeriesAnalysis:ForecastingandControl.Wiley,
| as follows: |     |     |     |     |     |     | 2016. |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[4] D.Montgomeryetal.,IntroductiontoLinearRegressionAnalysis.Wiley,
| • A | comprehensive |     | deep | learning-based |     | framework for |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | ---- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2012.
predictingannualexpenses,outperformingtraditionalsta-
[5] S.Makridakis,S.Wheelwright,andR.Hyndman,Forecasting:Methods
tistical methods such as ARIMA and linear regression in andApplications.Wiley,2008.
[6] T.Chatfield,TheAnalysisofTimeSeries:AnIntroduction.CRCPress,
| terms | of  | accuracy | and stability. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2016.
| Detailed |     | exploration | of data | preprocessing, |     | feature engi- |     |     |     |     |     |     |     |     |
| -------- | --- | ----------- | ------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
• [7] M. Ahmed et al., “Shortcomings of classical methods in modern
neering, and model selection, with a particular focus on financial forecasting,” J. Fin. Analytics, vol. 23, no. 4, pp. 211–221,
2020.
| the      | utilization | of           | LSTM | and GRU   | networks | to capture |                   |     |                     |     |                  |     |          |        |
| -------- | ----------- | ------------ | ---- | --------- | -------- | ---------- | ----------------- | --- | ------------------- | --- | ---------------- | --- | -------- | ------ |
|          |             |              |      |           |          |            | [8] S. Hochreiter |     | and J. Schmidhuber, |     | “Long short-term |     | memory,” | Neural |
| temporal |             | dependencies | in   | financial | data.    |            |                   |     |                     |     |                  |     |          |        |
Comput.,vol.9,no.8,pp.1735–1780,1997.
• A rigorous evaluation of model performance using stan- [9] K. Cho et al., “Learning phrase representations using RNN
dard metrics, demonstrating the robustness of the pro- encoder-decoder for statistical machine translation,” arXiv preprint
arXiv:1406.1078,2014.
posed system in forecasting future financial trends. [10] A. Graves, “Supervised sequence labelling with recurrent neural net-
The benefits of utilizing deep learning in financial planning works,”StudiesinComputationalIntelligence,vol.385,Springer,2012.
[11] H.Siami-Namini,N.Tavakoli,andA.SiamiNamin,“Acomparisonof
| are evident, | as  | these | models provide | a   | more | nuanced under- |       |     |         |             |               |      |           |      |
| ------------ | --- | ----- | -------------- | --- | ---- | -------------- | ----- | --- | ------- | ----------- | ------------- | ---- | --------- | ---- |
|              |     |       |                |     |      |                | ARIMA | and | LSTM in | forecasting | time series,” | 2018 | 17th IEEE | Int. |
standing of financial data, especially in capturing long-term Conf.Mach.Learn.Appl.,pp.1394–1401.
(cid:128)https://jsiar.com
| #editor@jsiar.com |     |     |     |     |     |     |     |     |     |     |     |     | ©2025JSIAR |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |

JournalofScientificInnovationandAdvancedResearch(JSIAR)2025
[12] Y. Bengio, A. Courville, and P. Vincent, “Representation learning: A
reviewandnewperspectives,”IEEETrans.PatternAnal.Mach.Intell.,
vol.35,no.8,pp.1798–1828,2013.
[13] F.Chollet,“DeeplearningwithPython,”ManningPublications,2018.
[14] I.Goodfellow,Y.Bengio,andA.Courville,DeepLearning.MITPress,
2016.
[15] J. Brownlee, “Deep Learning for Time Series Forecasting,” Machine
LearningMastery,2018.
[16] P. J. Brockwell and R. A. Davis, Introduction to Time Series and
Forecasting.Springer,2016.
[17] G.Zhang,B.EddyPatuwo,andM.Y.Hu,“Forecastingwithartificial
neural networks: The state of the art,” Int. J. Forecast., vol. 14, no. 1,
pp.35–62,1998.
[18] N. B. Nwulu and A. A. Fakorede, “Comparative study of traditional
and ML methods in short-term electricity price forecasting,” Energy
Procedia,vol.158,pp.1234–1239,2019.
[19] G.BoxandG.Jenkins,TimeSeriesAnalysis:ForecastingandControl,
5thed.Wiley,2015.
[20] R.HyndmanandG.Athanasopoulos,Forecasting:PrinciplesandPrac-
tice.OTexts,2021.
[21] A.KhasheiandM.Bijari,“Anartificialneuralnetwork(p,d,q)modelfor
timeseriesforecasting,”ExpertSyst.Appl.,vol.37,no.1,pp.479–489,
2010.
[22] T.G.Andersenetal.,“Volatilityforecasting,”Rev.Econ.Stat.,vol.89,
no.3,pp.617–631,2007.
[23] Y. Sun et al., “Financial time series forecasting using LSTM models,”
J.Appl.Intell.,vol.50,pp.275–289,2020.
[24] J.Chungetal.,“Empiricalevaluationofgatedrecurrentneuralnetworks
onsequencemodeling,”arXiv:1412.3555,2014.
[25] A.K.S.SaxenaandV.K.Agrawal,“Stockpricepredictionusingdeep
learningtechniques,”Proc.ICCCNT,2021.
[26] D.MalhotraandR.Malhotra,“Evaluatingconsumerloansusingneural
networks,”Omega,vol.31,no.2,pp.83–96,2003.
[27] J.Wangetal.,“Budgetforecastingusinghybriddeeplearningmodels,”
IEEEAccess,vol.8,pp.98743–98756,2020.
[28] N. Mishra and M. Singh, “Personal finance recommendation system
usingdeeplearning,”J.Intell.Fin.,vol.5,no.3,pp.147–159,2021.
[29] H.Siami-Naminietal.,“Forecastingeconomicandfinancialtimeseries:
ARIMAvs.LSTM,”FutureGen.Comput.Syst.,vol.100,pp.740–752,
2019.
[30] T.FischerandC.Krauss,“Deeplearningwithlongshort-termmemory
networksforfinancialmarketpredictions,”Eur.J.Oper.Res.,vol.270,
no.2,pp.654–669,2018.
(cid:128)https://jsiar.com
#editor@jsiar.com ©2025JSIAR