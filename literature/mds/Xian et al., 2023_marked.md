---
conversion_metadata:
  converted_at: "2026-10-11T15:13:15Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Xian et al., 2023.pdf"
  source_pdf_sha256: "efab112e682313d6cdf022d9a6dd7bf3461c32bac6aa0bb0704a5bb7bb00b5a4"
  page_count: 9
  markdown_char_count: 43257
---

Xian et al. BMC Infectious Diseases (2023) 23:803 BMC Infectious Diseases
https://doi.org/10.1186/s12879-023-08799-4
RESEARCH Open Access
Comparison of SARIMA model, Holt-winters
model and ETS model in predicting the
incidence of foodborne disease
Xiaobing Xian1†, Liang Wang1†, Xiaohua Wu2†, Xiaoqing Tang2, Xingpeng Zhai1, Rong Yu3, Linhan Qu4 and
Mengliang Ye1*
Abstract
Background According to the World Health Organization, foodborne disease is a significant public health issue. We
will choose the best model to predict foodborne disease by comparison, to provide evidence for government policies
to prevent foodborne illness.
Methods The foodborne disease monthly incidence data from June 2017 to April 2022 were obtained from the
Chongqing Nan’an District Center for Disease Prevention and Control. Data from June 2017 to June 2021 were used to
train the model, and the last 10 months of incidence were used for prediction and validation The incidence was fitted
using the seasonal autoregressive integrated moving average (SARIMA) model, Holt-Winters model and Exponential
Smoothing (ETS) model. Besides, we used MSE, MAE, RMSE to determine which model fits better.
Results During June 2017 to April 2022, the incidence of foodborne disease showed seasonal changes, the months
with the highest incidence are June to November. The optimal model of SARIMA is SARIMA (1,0,0) (1,1,0) . The MSE,
12
MAE, RMSE of the Holt-Winters model are 8.78, 2.33 and 2.96 respectively, which less than those of the SARIMA and
ETS model, and its prediction curve is closer to the true value. The optimal model has good predictive performance.
Conclusion Based on the results, Holt-Winters model produces better prediction accuracy of the model.
Keywords Foodborne Disease, SARIMA model, Holt-Winters model, Exponential smoothing model
Introduction
Foodborne disease (FBD) are a major cause of morbidity
and mortality and a very important public health prob-
†Xiaobing Xian, Liang Wang and Xiaohua Wu contributed equally to lem worldwide. According to the estimation of World
this work.
Health Organization (WHO), 600 million people world-
*Correspondence:
wide fall ill each year due to the consumption of con-
Mengliang Ye
yemengliang@cqmu.edu.cn taminated food, resulting in 420,000 deaths and a loss of
1College of Public Health, Chongqing Medical University, Chongqing, 33 million healthy lives [1, 2]. This equates to 550 disabil-
China
ity-adjusted life years (DALYs). A DALYs can be consid-
2Nan’an District Center for Disease Control and Prevention, Chongqing,
China ered as a loss of health and life for one year [3, 4], WHO
3School of Traditional Chinese Medicine, Chongqing Medical University, FBD Epidemiology Reference Group (FERG) estimated
ChongQing, China
that FBD cause a global loss of 33 million DALYs annu-
4School of The First Clinical College, Chongqing Medical University,
ChongQing, China ally [5], which will have a huge impact on people’s lives
© The Author(s) 2023. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included
in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. The
Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available
in this article, unless otherwise stated in a credit line to the data.

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 2 of 9
and health. These effects are not limited to low-income capabilities of food safety risks, and grasp the baseline of
and high-income countries, such as those in Europe, important FBD.
where 41 to 49 DALYs per 100,000 population can be According to WHO estimates, approximately 2.2 mil-
attributed to FBD [5]. Food insecurity costs $110 billion lion people worldwide die each year due to foodborne or
a year in lost productivity and health care costs among waterborne diarrhea. There are approximately 600 mil-
low-and middle-income countries [6]. As the world’s lion cases of foodborne diseases worldwide each year,
largest developing country, the situation of FBD in China with a death toll of many people, of which 125,000 are
is also not optimistic. An analysis of nearly 2,500 Chinese children under the age of 5 [13]. The Centers for Disease
articles on diseases from 1994 to 2005 revealed 1,082 Control reported that 48 million people in the United
cases of bacterial FBD, if relying solely on these numbers States get sick from FBD each year, with 128,000 hospi-
alone would seriously underestimate the number of FBD talized and 3,000 dying [14]. Nan’an District is one of the
in China, and a national acute gastroenteritis survey esti- main urban areas of Chongqing, which is an area driven
mates that 748 million cases of acute gastroenteritis and by light industry, catering and tourism industry, and also
420 million medical consultations occur in China every with many people who suffer from FBD here. However,
year [7]. Patients with FBD often lack awareness of the due to the low sensitivity of FBD surveillance, there is a
severity of the disease, which may cause them to post- certain gap between the number of cases reported and
pone medical treatment. This delay can easily cover up the actual situation, so it is necessary to choose a better
the outbreak of food safety incidents, which is not con- prediction model for FBD.
ducive to the timely control of disease outbreak. These The autoregressive integrated moving average
health effects have economic implications for affected (ARIMA) model is a widely used time series analysis tool,
people, healthcare systems, food producers and distribu- which is widely used to predict infectious diseases such as
tors [8]. To address these issues, China has begun using malaria, hemorrhagic fevers, hand, foot and mouth dis-
systems such as Pulse Net domestically to track and cor- ease, influenza, COVID -19 and tuberculosis [15]. Addi-
relate food-borne pathogens. tionally, ARIMA-related hybrid models such as Seasonal
FBD ranges from mild self-limiting diseases to life- Autoregressive Integrated Moving Average (SARIMA)
threatening food poisoning [9], and foodborne pollutants was also developed as modeling candidates for future
are abundant. They include viruses and bacteria, para- trend prediction. SARIMA model and Holt-Winters
sites, chemicals, toxins and allergens that cause a wide model are two of the most widely used time series fore-
variety of diseases [5]. In addition, many foodborne haz- casting methods, which are suitable for different types of
ards are transmitted by other means: through water, soil time series models and can reflect time changes as well
or air; by direct contact between people, or between peo- as periodic changes in the original data [16]. Exponential
ple and animals. FBD are becoming a greater challenge Smoothing (ETS) model is also widely used in predicting
due to new and emerging microorganisms and toxins, infectious disease, such as brucellosis and epidemiologi-
the growth of antibiotic resistance, and increasing food cal surveillance [17].
contamination due to new environmental and food pro- Previous studies on FBD mainly focused on analyzing
duction methods [10]. The effort of improving food safety public surveillance data and estimating the actual inci-
and reducing the burden of FBD relies on data from FBD dence rate of FBD in a country or a region, and assess the
monitoring and epidemic investigations to help priori- disease burden caused by various pathogens [18]. How-
tize food safety interventions, policies, and practices [11]. ever, there are few studies that compare the advantages
Recognizing the necessity for global and regional esti- and disadvantages of the three models. This study pro-
mates of FBD to guide public health policy, the WHO poses to establish a SARIMA model, Holt-Winters and
launched the Estimating the Global Burden of FBD Ini- ETS model by the number of monthly incidences and
tiative in 2006. The main aim of the initiative is to get compare the advantages and disadvantages of three dif-
policy makers and some people involved in food safety to ferent models, so as to select the optimal model.
set up appropriate evidence-based regulations, which can
Materials & methods
also improve the capacity of countries to assess their FBD
burden. In addition, since 2011, China has established a Data source
web-based FBD monitoring platform, which has gradu- China’s FBD surveillance platform was established in
ally played a role in the early warning of food safety emer- 2011, which mainly includes: the FBD Outbreaks Sur-
gencies, food safety emergencies, and research on the veillance System, the FBD Surveillance and Reporting
burden brought by FBD [12]. Through these monitoring System, the National Molecular Traceability Network for
platforms, we can timely discover clusters, improve the FBD and other surveillance systems. The China National
early identification, warning, and prevention and control Center for Food Safety Risk Assessment maintains and
manages the platform for data collection and periodic

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 3 of 9
reporting to the National Health Commission [20]. The the Ljung-Box Q test was used to diagnose whether the
data of the FDB and population used in this study were residual error sequence was a white-noise sequence [24].
obtained from Chongqing Nan’an District Center for
Disease Prevention and Control from June 2017 to April Holt-winters model
2022. FBD data were collected from 25 medical institu- The component form of the Holt-Winters model con-
tions for monitoring sites and 14 primary medical insti- sists of four equations, namely the prediction equation
tutions for health emergency response teams in Nan’an and three smoothing equations [25]. The characteristic of
District, and reporting form of the data is the incidence Holt-Winters model is to eliminate some random fluctua-
of cases. We collect continuous monthly data, which tions while correcting seasonal trends. It assigns different
helps input and build the model. Data from June 2017 to weights to data from each period and reasonably predicts
June 2021 were used to train the model, and the last 10 future development trends. The α (level) and β (slope) of
months of incidence were used for prediction and valida- the trend should be between 0 and 1, and when a value
tion. The incidence was fitted using the SARIMA model, close to 0 means that the estimation of current/future
Holt-Winters model and ETS model. time points is based on recent observations [26].
Data processing and analysis ETS model
SPSS 25.0 was used for data preprocessing and descrip- ETS model take the errors, trends, and seasonal com-
tive statistics, the SARIMA, Holt-Winters and ETS mod- ponents of a given time series into consideration, and
els were developed by R 4.1.2. In addition, all the figures evaluates possible alternative models before selecting the
are also made of R 4.1.2. In this study, p < 0.05 was con- best performing model to simulate the data. ETS model
sidered statistically significant. considered comprehensive historical information, it has
three main parameters: error, trend, and seasonal com-
SARIMA model ponent, which can be additive (A), multiplicative (M),
The ARIMA model consists of three parts: autoregres- or none (N). The ETS method includes several detailed
sion order (p), difference order (d), and moving average methods, such as single ETS, double ETS, Holt trend ETS
order (q) [21]. The SARIMA model is a Seasonal ARIMA, (with or without seasonal features), and other methods
which consists by seasonal effect, long-term trend effect, based on various features of the original sequence. The
periodic change and random disturbance. The general optimal model is selected according to the AIC mini-
form of the SARIMA model is (p, d, q) × (P, D, Q) s, p, d mum, the corrected Akaike message criterion (AICc), or
and q are non-negative integers, representing the order the BIC [27]. What’s more, Ljung-Box Q test was used to
of non-seasonal autoregressive (AR) term, non-seasonal diagnose whether the residual sequence is white noise
difference and non-seasonal moving average (MA), sequence.
respectively. P, D and Q are also non-negative integers
indicating the order of seasonal AR term, seasonal dif- Evaluation metrics
ference term and seasonal MA term respectively; S is the In order to evaluate the performance of the SARIMA,
length of the seasonal period [22]. Holt-Winters and ETS model, we tested the fitting values.
Generally speaking, time series modeling methods Several performance indexes, namely, root means square
include the following three steps: model recognition, error (RMSE), mean absolute error (MAE), mean abso-
parameter estimation, and diagnostic checks. Firstly, lute percentage error (MAPE) and means square error
if necessary, perform appropriate differencing on the (MSE) are used to determine the predictive efficiency of
sequence to achieve stationarity and normality. We use the three models [28]. Many researchers have used these
the augmented Dickey Fuller (ADF) unit root test to metrics to assess the accuracy of models, when the MSE,
estimate whether the time series is stationary, if result MAE, and RMSE values of the model are smaller, the fit-
of the ADF test is significant, the sequence is proven to ting degree of the model is better. If all three indicators
be stationary. Secondly, the time dependent structure of a model are lower than another model, then the model
of the transformed data is identified by examining the is more superior. For the measure of these metrics, the
autocorrelation functions (ACF) and partial autocor- smallest value corresponds to the best method. The fol-
relation functions (PACF) of the transformed data [23]. lowing are the calculation methods for some indicators.
Besides, the values of p, d and q, q are finally determined
by considering the smallest Akaike information crite- RMSE= (actual forecast)2 (1/samplesize)
− ×
rion (AIC) and Bayesian information criterion (BIC) val- (cid:31)(cid:30)
ues corresponding to the higher prediction accuracy. At
MAE= (actual forecast) (1/samplesize)
last, in order to test the normality of SARIMA residuals, | − | ×
(cid:31)

Xian et al. BMC Infectious Diseases          (2023) 23:803  Page 4 of 9
|     |     |     |     | actu a l f o r cast |     |     |     |
| --- | --- | --- | --- | ------------------- | --- | --- | --- |
MAPE=(1/samplesize) | c−tu | 100% )78.0(01 )91.1(41 )33.2(82 )89.4(06
|     |     |     | ×        | | a a l | | ×        |     | )17.0(8 |
| --- | --- | --- | -------- | --------- | -------- | --- | ------- |
|     |     |     |          | (cid:30)  | (cid:29) |     |         |
|     |     |     | (cid:31) |           |          |     | 21      |
forecast)2
| MSE= | (actual |     |     | (1/samplesize) |     |     |     |
| ---- | ------- | --- | --- | -------------- | --- | --- | --- |
|      |         | −   |     | ×              |     |     |     |
(cid:31)
)83.51(181 )29.21(551 )30.71(502
)30.3(43 )81.4(84
Ethics approval and consent to participate
11
| The  research  | protocols  |     | and  | informed  | consent  forms  |     |     |
| -------------- | ---------- | --- | ---- | --------- | --------------- | --- | --- |
submitted for this project comply with the principles of
)82.51(481
medical ethics and the requirements of the Declaration  )68.9(611
)78.1(12 )13.3(83 )57.7(39
of Helsinki. This study was approved by the Ethics Com-
01
mittee of Nan’an District for center disease control and
prevention, and informed consent was obtain from all the
participant. All the data collection in this study are was in
)16.61(002
accordance to the Law of the People’s Republic of China  )24.6(27 )94.3(04 )10.5(95 )76.7(29
on the Prevention and Treatment of Infectious Diseases.
9
Results
Descriptive statistics
)10.4(54 )29.1(22 )64.6(67 )85.7(19 )27.7(39
Table 1 shows the incidence rate of each month from
| June 2017 to April 2022 based on the average popula- |     |     |     |     |     |     | 8   |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
tion of the Nan’an District. The month with the highest
incidence was November 2021, which reached 17.03 per
)57.9(711
100,000, while the lowest incidence occurred in January  )85.2(92 )29.3(54 )65.7(98 )41.7(68
2019 with 0.08 per 100,000.
7
The analysis of SARIMA model results
This study used the “STL” function to decompose the  )82.01(121
)27.4(35 )66.1(91 )33.9(211 )94.4(45
sequence, Fig. 1 presents seasonal distribution of FBD in
| Nan’an District from June 2017 to April 2022. It can be  |     |     |     |     |     | 2202 ot 7102 ,gniqgnohC ,tcirtsiD na’naN ni ecnedicni DBF fo noitubirtsiD 1 elbaT |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------------------------------------------------------- | --- |
6
clearly seen from the figure that June to November is the
peak period of incidence.
)90.2(42 )84.3(14 )24.6(77 )27.7(39
Only six models passed the residual test and param-
| eter test, the six models were SARIMA (1,0,0) (1,1,0) |          |         |            |          |         | ,   |     |
| ----------------------------------------------------- | -------- | ------- | ---------- | -------- | ------- | --- | --- |
|                                                       |          |         |            |          |         | 12  | 5   |
| SARIMA                                                | (0,0,1)  | (0,1,1) | ,  SARIMA  | (0,0,1)  | (0,1,0) | ,   |     |
|                                                       |          |         | 12         |          |         | 12  |     |
| SARIMA                                                | (0,0,1)  | (1,1,0) | ,  SARIMA  | (0,0,0)  | (0,1,1) | .   |     |
|                                                       |          |         | 12         |          |         | 12  |     |
)71.2(62 )75.2(13 )51.2(62
The AIC values of the five candidate models are listed  )87.0(9 )1.1(31
in Table 2, and we finally confirmed SARIMA (1,0,0)
4
(1,1,0)  model with drift is finally selected as the optimal
| 12  |     |     |     |     |     | )dnasuoht derdnuh/etar ecnedicni( htnoM |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- |
SARIMA model after comparing the AIC values. Besides,
the evaluation criteria for the SARIMA model are dis- )72.1(51 )94.2(03 )37.3(54
)25.0(6 )57.0(9
played in Table 3.
3
| Note:  SARIMA,    |     | Seasonal  | Autoregressive  |              | Integrated  |     |     |
| ----------------- | --- | --------- | --------------- | ------------ | ----------- | --- | --- |
| Moving  Average;  |     | AIC,      | Akaike          | information  | criterion;  |     |     |
BIC, Bayesian information criterion. )66.1(02 )94.1(81
)7.0(8 )15.0(6 )85.0(7
| The analysis of ETS model results |     |     |     |     |     |     | 2   |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ETS programming functions were used to simulate time
series data sets on the incidence of FBD, from which
)85.1(91 )80.1(31
|                                                           |                  |     |      |        | (AIC = 228.24,  |     | )44.0(5 )80.0(1 )52.0(3 |
| --------------------------------------------------------- | ---------------- | --- | ---- | ------ | --------------- | --- | ----------------------- |
| we  found                                                 | an  appropriate  |     | ETS  | model  |                 |     |                         |
| BIC = 256.62). The evaluation criteria for the ETS model  |                  |     |      |        |                 |     | 1                       |
are displayed in Table 3.
raeY 7102 8102 9102 0202 1202 2202

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 5 of 9
Fig. 1 Seasonal distribution of FBD in Nan’an District
Table 2 AIC and BIC values for candidate SARIMA models Table 3 Evaluation indicators of the three models
Candidate Models AIC BIC Evaluation indicators ETS Holt-Winters SARIMA
SARIMA (1,0,0) (1,1,0) with drift 188.83 193.67 MSE 14.45 8.78 17.88
12
SARIMA (0,0,1) (0,1,1) with drift 189.79 194.62 MAE 2.68 2.33 2.75
12
SARIMA (0,0,1) (0,1,0) with drift 189.21 192.43 RMSE 3.80 2.96 4.23
12
SARIMA (0,0,1) (1,1,0) with drift 190.23 195.06 MAPE 29.42 39.29 28.80
12
SARIMA (0,0,0) (0,1,1) with drift 194.49 197.71
12
Best: SARIMA (1,0,0) (1,1,0) 12 with drift the SARIMA and ETS model Table 3. What’s more, the
Holt-Winters model also has better predictive accuracy
The analysis of Holt-winters model results than SARIMA. This may be due to the characteristics
R software automatically selects the model that best fits of each model. In terms of models alone, the SARIMA
the original data. The results showed that Holt-Winters model is more suitable for predicting data with stable
model have good prediction accuracy of the model. changing trends than the Holt-Winters model, while the
Table 3 showed the evaluation index of the Holt-Winters Holt-Winters model is more suitable for predicting data
model. with single changing trends.
Note: MSE, means square error; MAE, mean absolute
Model comparison error; RMSE, root means square error; MAPE, mean
Many scholars have conducted research on disease pre- absolute percentage error; ETS, Exponential Smooth-
diction models. SARIMA model is a model for relatively ing; SARIMA, Seasonal Autoregressive Integrated Mov-
stable time series data. It integrates time trend, seasonal, ing Average.
periodic change, random error and other factors to quan- The forecast results from July 2021 to April 2022
tify the model parameters [29]. However, the Holt-Win- of FBD incidence in Nan ‘an district according to the
ters model has a relatively simple principle, and has a SARIMA (1, 0, 0) (1, 1, 0) model, ETS model and Holt-
12
high prediction accuracy for diseases with periodic regu- Winters model are shown in Table 4. The observed inci-
larity [30]. This method assigns different weights to the dence of SARIMA (1, 0, 0) (1, 1, 0) model in September
12
distance of data on the timeline, which is suitable for pre- and October 2021, the observed incidence of ETS model
dicting individual time series data. We found MSE, MAE, in December 2021 and the observed incidence of Holt-
RMSE of the Holt-Winters model are less than those of Winters model in September, November and December

Xian et al. BMC Infectious Diseases          (2023) 23:803  Page 6 of 9
Table 4 The prediction of SARIMA (1, 0, 0) (1, 1, 0)   model, ETS model and Holt-Winters model
12
Month Incidence SARIMA model(95%CI) ETS model(95%CI) Holt-Winter
model(95%CI)
2021/7/1 7.14 7.11(1.54,12.68) 8.48(-0.04,17) 13.09(12.51,13.67)
2021/8/1 7.72 6.36(0.25,12.47) 7.12(-0.53,14.76) 7.19(6.57,7.81)
2021/9/1 16.61 6.75(0.54,12.97) 8.74(-1.23,18.71) 11.63(10.61,12.65)
2021/10/1 15.28 7.9(1.66,14.14) 8.94(-1.83,19.71) 11.65(10.3,12.99)
2021/11/1 17.03 13.24(7,19.49) 11.86(-3.18,26.9) 15.19(13.03,17.35)
2021/12/1 4.98 2.09(-4.15,8.34) 1.75(-0.58,4.08) 2.46(1.74,3.17)
2022/1/1 1.08 1.33(-4.91,7.58) 0.94(-0.37,2.24) 1.43(0.74,2.12)
2022/2/1 1.49 1.47(-4.78,7.71) 1.15(-0.52,2.81) 2.37(1.18,3.56)
| 2022/3/1 |     | 3.73 | 2.19(-4.05,8.43) |     | 2(-1.02,5.03) |     | 2.4(0.86,3.94) |
| -------- | --- | ---- | ---------------- | --- | ------------- | --- | -------------- |
Table 5 Comparison of prediction results of three models
Month Incidence Holt-Winters forecast SARIMA forecast ETS forecast
Forecast Forecast error (%) Forecast Forecast error (%) Forecast Forecast error (%)
| 2021/7/1  | 7.14  | 13.09 | 83.33  | 7.11 -0.42   |     | 8.48  | 18.77  |
| --------- | ----- | ----- | ------ | ------------ | --- | ----- | ------ |
| 2021/8/1  | 7.72  | 7.19  | -6.87  | 6.36 -17.62  |     | 7.12  | -7.77  |
| 2021/9/1  | 16.61 | 11.63 | -29.98 | 6.75 -59.36  |     | 8.74  | -47.38 |
| 2021/10/1 | 15.28 | 11.65 | -23.76 | 7.9 -48.3    |     | 8.94  | -41.49 |
| 2021/11/1 | 17.03 | 15.19 | -10.8  | 13.24 -22.25 |     | 11.86 | -30.36 |
| 2021/12/1 | 4.98  | 2.46  | -50.6  | 2.09 -58.03  |     | 1.75  | -64.86 |
| 2022/1/1  | 1.08  | 1.43  | 32.41  | 1.33 23.15   |     | 0.94  | -12.96 |
| 2022/2/1  | 1.49  | 2.37  | 59.06  | 1.47 -1.34   |     | 1.15  | -22.82 |
| 2022/3/1  | 3.73  | 2.4   | -35.66 | 2.19 -41.29  |     | 2     | -46.38 |
| 2022/4/1  | 2.15  | 3.45  | 60.47  | 2.5 16.28    |     | 2.17  | 0.93   |
2021 were not within the 95% confidence interval (CI) of  risk of going to hospital, so there are far fewer reported
| the predicted values. |     |     |     | cases of FBD. |     |     |     |
| --------------------- | --- | --- | --- | ------------- | --- | --- | --- |
Note: ETS, Exponential Smoothing; SARIMA, Seasonal  We analyzed the FBD incidence rates and observed a
Autoregressive  Integrated  Moving  Average;  CI,  confi- fluctuating downward trend and seasonal characteris-
dence interval. tics in this study, with the valley is in January to Febru-
In addition, Table 5 shows the comparison of predic- ary, and the incidence is higher from June to November
tion results of three models, in most months of the fore- almost every year. The reasons could be as follows: In the
cast, the forecast error of the Holt-Winters model was  first place, Chinese New Year usually falls in January or
smaller than that of the other two models. Comparing  February, and it is traditionally considered bad luck to
the fitting effects of the three models, it can be seen from  go to the hospital at this time, resulting the reduction of
Fig. 2 that the fitting value of the Holt-Winters model is  reported incidence case [32]. In the second place, higher
closer to the actual value. Therefore, it can be concluded  temperatures in June, July and August make food spoil
that the optimal model is Holt-Winters model. more quickly, which is more likely to cause FBD. Besides,
Note: ETS, Exponential Smoothing; SARIMA, Seasonal  this  phenomenon  may  be  related  to  the  climate  and
Autoregressive Integrated Moving Average. human behaviors [33], as temperatures rise, social activi-
ties and contacts between people tend to increase dur-
Discussion ing the spring and summer months. Thus, the reported
As  can  been  seen  from  the  descriptive  statistics  in  incidence is consistently high during the three months of
Table 1 and the seasonal distribution of FBD in Fig. 1  each year, leading to the widespread epidemics. In addi-
that the number of reported cases from December 2019  tion to this, from Fig. 1 we can see that September to
to April 2020 was at low level. Possibly due to the out- November are also high incidence month of FBD, studies
break of COVID-19, In response to the outbreak of the  have shown that cold weather or wind can affect the inci-
COVID-19 in December 2019, by the end of February,  dence of some diseases [34].
China’s national, provincial and municipal governments  Many  scholars  have  studied  the  disease  prediction
had taken a series of public health interventions to effec- model. Some research shows that the ARIMA model is
tively curb the epidemic [31], such as lockdown mea- suitable for complex interactions between temporal sea-
sures. People are staying at home rather than taking the  sonal effects, long-term trends, and random fluctuations.

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 7 of 9
Fig. 2 Fitting status between the actual incidence of foodborne illness in Chongqing Nan’an District from June 2017 to June 2021 and the predicted
incidence from July 2021 to April 2022. The black line indicates the actual incidence rate, orange, blue, and purple indicate the incidence rates predicted
by the ETS, Holt-Winters, and SARIMA models, and hazy areas indicate the upper and lower ranges of the 95% CI for the predicted incidence rates of
foodborne illness
This model is one of the commonly used time series model has better predictive accuracy than SARIMA and
analysis models for predicting infectious diseases, such ETS models. This may be due to the different character-
as tuberculosis, hand-foot-mouth disease, mumps, influ- istics of each model, as the Holt-Winters model is built
enza etc. [35–38]. What’s more, the “STL” function is using historical data and does not consider the interfer-
used to decompose the series, which can not only display ence of other factors [32]. Therefore, this model has cer-
the trend and seasonal change of the incidence rate series tain reference value for predicting FBD. And through
of FBD, but also calculate the seasonal index of each Fig. 2, we can also clearly see that the fitting curve of the
month, which can intuitively understand its seasonality Holt-Winters model is closer to the true value.
[39]. We use the SARIMA model to perform linear fitting At present, FBD hamper socio-economic development
on the FBD series. By comparing the AIC, BIC values, by placing pressure on health care systems and harm-
SARIMA(1, 0, 0)× (1, 1, 0) is the best model, and the ing national economies, tourism and trade [40]. Despite
12
RMSE and MAPE values of this model are 4.23 and 28.80, significant improvements in medical services and infec-
respectively. Holt-Winters model has high prediction tious disease control capabilities, FBD still remain a
accuracy the periodic regularity disease. Besides, ETS major public health problem in China [41]. Like other
model take comprehensive historical information into countries, FBD characterized by acute gastrointestinal
consideration, it’s also a good method. In order to high- diseases are the largest food safety issue and the most
light the performance accuracy of developed SARIMA, disturbing public health threat related to food in China
ETS, and Holt-Winters models, we divided the FBD time [42, 43]. However, few studies have chosen the optimal
series sample into two parts. The first part of data, June model by comparing the degree of fit of the three mod-
2017 to June 2021, as a training set for in-sample simu- els. The purpose of this study is to select the model with
lated modeling. The rest of 10 month, July 2021 to April the best prediction and fitting performance by compar-
2022, as a testing set. Based on these modellings’ accu- ing several common models, in order to better assist in
racy metrics, it can be seen from the evaluation indica- the rational allocation of medical resources and person-
tors of the three models (Table 3), we found the MSE, nel, and provide clues for the prevention and treatment
MAE, RMSE of the Holt-Winters model are 8.78, 2.33 of this disease from data analysis. Reliable prediction of
and 2.96 respectively. It’s indicated the Holt-Winters FBD helps to better coordinate the relief and intervention

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 8 of 9
Funding
resources of the public health system, and alleviate the This research was funded by the Nan’an District Center for Disease Prevention
pressure on the healthcare system [44]. In addition, the and Control for Study on the Application of Foodborne illness Surveillance
and Early Warning System in Nan’an District. (Grant number: 2021MSXM264)
optimal prediction model of FBD obtained in this study
and Application research of foodborne disease monitoring and early warning
can also be used in other countries and regions to predict system in Nan ‘an District (Grant number: cqmuhx20210010).
and control this disease.
Data Availability
Although we have selected the optimal prediction
The datasets analyzed during the current study are not publicly available
model for FBD by comparing the three, there are still due to the data being investigated and protected by the Chongqing Nan’an
some shortcomings that need to be improved. In this District Center for Disease Prevention and Control, but are available from the
corresponding author on reasonable request.
study, we chose the model with good overall forecasting
effect, but the performance of the three models is various
Declarations
in different months, so the month-specific forecasting
model may need further research and verification in the Ethics approval and consent to participate
future. Besides, the data is not comprehensive enough, The research protocols and informed consent forms submitted for this project
comply with the principles of medical ethics and the requirements of the
and we should consider combining more years of data to
Declaration of Helsinki. This study was approved by the Ethics Committee
make better predictions in future research. of Nan’an District for center disease control and prevention, and informed
consent was obtain from all the participant. All the data collection in this
Conclusions study are was in accordance to the Law of the People’s Republic of China on
the Prevention and Treatment of Infectious Diseases.
We used SARIMA model, Holt-Winters model and ETS
model in predicting the incidence of FBD, from which we Consent for publication
Not applicable.
found the highest incidence was November 2021and the
lowest incidence occurred in January 2019. The incidence Competing interests
of FBD presented obvious seasonal trends in this study. The authors declare no competing interests.
By comparing of prediction results of three models, in
Received: 17 August 2023 / Accepted: 7 November 2023
most months of the forecast, the forecast error of the
Holt-Winters model was smaller than that of the other
two models. When make comparison of the fitting effects
between the three models, the fitting value of the Holt-
Winters model is closer to the actual value. Therefore, it
References
can be concluded that the optimal model is Holt-Winters 1. Organization WH. WHO estimates of the global burden of foodborne Dis-
model, which can provide convenience and new ideas for eases: foodborne Disease burden epidemiology reference group 2007–2015.
World Health Organization; 2015.
related forecasting research in the future.
2. Kirk MD, Pires SM, Black RE, Caipo M, Crump JA, Devleesschauwer B, et al.
World Health Organization Estimates of the Global and Regional Disease
Abbreviations
Burden of 22 foodborne bacterial, Protozoal, and viral Diseases, 2010: A Data
SARIMA Seasonal autoregressive integrated moving average
Synthesis. PLoS Med. 2015;12(12):e1001921.
FBD Foodborne disease
3. Murray CJ. Quantifying the burden of Disease: the technical basis for
ETS model E xponential Smoothing model
disability-adjusted life years. Bull World Health Organ. 1994;72(3):429–45.
WHO World Health Organization
4. Lopez AD, Murray CC. The global burden of Disease, 1990–2020. Nat Med.
ADF Augmented Dickey Fuller
1998;4(11):1241–3.
ACF Autocorrelation functions
5. Havelaar AH, Kirk MD, Torgerson PR, Gibb HJ, Hald T, Lake RJ, et al. World
PACF Partial autocorrelation functions
Health Organization Global Estimates and Regional comparisons of the
AIC Akaike information criterion
Burden of Foodborne Disease in 2010. PLoS Med. 2015;12(12):e1001923.
BIC Bayesian information criterion
6. Jaffee SM, Henson S, Unnevehr LJ, Grace D, Cassou E, editors. The Safe Food
RMSE Root means square error
Imperative: Accelerating Progress in Low- and Middle-Income Countries2018.
MAE Mean absolute error MAE
7. Chen Y, Yan WX, Zhou YJ, Zhen SQ, Zhang RH, Chen J, et al. Burden of self-
MAPE Mean absolute percentage error
reported acute gastrointestinal Illness in China: a population-based survey.
MSE Means square error
BMC Public Health. 2013;13:456.
AR Autoregressive
8. Hussain MA, Dawson CO. Economic impact of Food Safety outbreaks on Food
MA Moving average
businesses. Foods. 2013;2(4):585–9.
9. Lai YH, Chung YA, Wu YC, Fang CT, Chen PJ. Disease burden from foodborne
Acknowledgements
illnesses in Taiwan, 2012–2015. J Formos Med Assoc. 2020;119(9):1372–81.
The authors would like to thank all the participants involved in this project for
10. Switaj TL, Winter KJ, Christensen SR. Diagnosis and management of Food-
their contribution and dedication sincerely.
borne Illness. Am Fam Physician. 2015;92(5):358–65.
11. White AE, Tillman AR, Hedberg C, Bruce BB, Batz M, Seys SA, et al. Foodborne
Authors’ contributions
Illness outbreaks reported to National Surveillance, United States, 2009–2018.
Each author has met the authorship requirements. X.T. and X.W. collected
Emerg Infect Dis. 2022;28(6):1117–27.
the data, X.X. and X.Z. completed data analysis, X.X. and L.W. wrote the
12. Chen L, Sun L, Zhang R, Liao N, Qi X, Chen J. Surveillance for foodborne Dis-
manuscript. R.Y. and L.Q. prepared the figures and tables. All authors have read
ease outbreaks in Zhejiang Province, China, 2015–2020. BMC Public Health.
and agreed to the published version of the manuscript.
2022;22(1):135.
13. Tohma K, Saito M, Pajuelo MJ, Mayta H, Zimic M, Lepore CJ, et al. Viral
intra-host evolution in immunocompetent children contributes to human

Xian et al. BMC Infectious Diseases (2023) 23:803 Page 9 of 9
norovirus diversification at the global scale. Emerg Microbes Infect. 31. Liu Y, Zheng F, Du Z, Li J, Gu J, Jiang M, et al. Evaluation of China’s Hubei
2021;10(1):1717–30. control strategy for COVID-19 epidemic: an observational study. BMC Infect
14. Oliver SP. Foodborne pathogens and Disease Special Issue on the Dis. 2021;21(1):820.
National and International PulseNet Network. Foodborne Pathog Dis. 32. Wang S, Wei F, Li H, Wang Z, Wei P. Comparison of SARIMA model and
2019;16(7):439–40. Holt-Winters model in predicting the incidence of Sjögren’s syndrome. Int J
15. Liu K, Li T, Vongpradith A, Wang F, Peng Y, Wang W, et al. Identification and Rheum Dis. 2022;25(11):1263–9.
prediction of Tuberculosis in Eastern China: analyses from 10-year Population- 33. Wesolowski A, Metcalf CJ, Eagle N, Kombich J, Grenfell BT, Bjørnstad ON, et al.
based Notification Data in Zhejiang Province, China. Sci Rep. 2020;10(1):7425. Quantifying seasonal population fluxes driving rubella transmission dynamics
16. Ma S, Liu Q, Zhang Y. A prediction method of Fire frequency: based on the using mobile phone data. Proc Natl Acad Sci U S A. 2015;112(35):11114–9.
optimization of SARIMA model. PLoS ONE. 2021;16(8):e0255857. 34. Xin L, Zhu Y, Liu J, Fang Y, Xie J. Exposure-lag-response associations between
17. Guan P, Wu W, Huang D. Trends of reported human brucellosis cases in main- extreme environmental conditions and primary Sjögren’s syndrome. Clin
land China from 2007 to 2017: an exponential smoothing time series analysis. Rheumatol. 2022;41(2):523–32.
Environ Health Prev Med. 2018;23(1):23. 35. Mao Q, Zhang K, Yan W, Cheng C. Forecasting the incidence of Tuberculosis
18. Voetsch AC, Van Gilder TJ, Angulo FJ, Farley MM, Shallow S, Marcus R, et al. in China using the seasonal auto-regressive integrated moving average
FoodNet estimate of the burden of Illness caused by nontyphoidal Salmo- (SARIMA) model. J Infect Public Health. 2018;11(5):707–12.
nella Infections in the United States. Clin Infect Dis. 2004;38(Suppl 3):127–34. 36. Tian CW, Wang H, Luo XM. Time-series modelling and forecasting of hand,
19. Hedberg C. Food-related Illness and death in the United States. Emerg Infect foot and mouth Disease cases in China from 2008 to 2018. Epidemiol Infect.
Dis. 1999;5(6):840–2. 2019;147:e82.
20. Scallan E, Mahon BE. Foodborne Diseases Active Surveillance Network (Food- 37. Xu Q, Li R, Liu Y, Luo C, Xu A, Xue F et al. Forecasting the incidence of Mumps
Net) in 2012: a foundation for food safety in the United States. Clin Infect Dis. in Zibo City based on a SARIMA Model. Int J Environ Res Public Health.
2012;54(Suppl 5):381–4. 2017;14(8).
21. Tobias A, Díaz J, Saez M, Alberdi JC. Use of poisson regression and box- 38. Song X, Xiao J, Deng J, Kang Q, Zhang Y, Xu J. Time series analysis of
jenkins models to evaluate the short-term effects of environmental noise Influenza incidence in Chinese provinces from 2004 to 2011. Med (Baltim).
levels on daily emergency admissions in Madrid, Spain. Eur J Epidemiol. 2016;95(26):e3929.
2001;17(8):765–71. 39. Qiu H, Zhao H, Chen Q, Wang Q, Ou R, Ye M. Linear and non-linear combina-
22. Bas MD, Ortiz J, Ballesteros L, Martorell S. Evaluation of a multiple linear tion forecasting model of varicella incidence in Chongqing. Epidemiol Infect.
regression model and SARIMA model in forecasting (7)be air concentrations. 2021;149:e189. https://doi.org/10.1017/S0950268821001813. eCollection
Chemosphere. 2017;177:326–33. 2021.
23. Wang YW, Shen ZZ, Jiang Y. Comparison of ARIMA and GM(1,1) models for 40. Qi X, Alifu X, Chen J, Luo W, Wang J, Yu Y, et al. Descriptive study of food-
prediction of Hepatitis B in China. PLoS ONE. 2018;13(9):e0201987. borne Disease using Disease monitoring data in Zhejiang Province, China,
24. Xia Y, Liao C, Wu D, Liu Y. Dynamic Analysis and Prediction of Food Nitrogen 2016–2020. BMC Public Health. 2022;22(1):1831.
Footprint of Urban and rural residents in Shanghai. Int J Environ Res Public 41. Li W, Pires SM, Liu Z, Ma X, Liang J, Jiang Y, et al. Surveillance of foodborne
Health. 2020;17(5). Disease outbreaks in China, 2003–2017. Food Control. 2020;118:107359.
25. Chatfield C. The Holt-Winters forecasting Procedure. Appl Stat. 42. Chung SS, Wong CK. Regulatory and policy control on food safety in China. J
1978;27:264–79. Epidemiol Community Health. 2013;67(6):476–7.
26. Chatfield C. The Holt-Winters forecasting Procedure. J Royal Stat Soc Ser C: 43. Akhtar S, Sarker MR, Hossain A. Microbiological food safety: a dilemma of
Appl Stat. 2018;27(3):264–79. developing societies. Crit Rev Microbiol. 2014;40(4):348–59.
27. Zeng Q, Li D, Huang G, Xia J, Wang X, Zhang Y, et al. Time series analysis of 44. Thakur M, Ólafsson S, Lee J-S, Hurburgh CRJ. Data mining for recognizing
temporal trends in the Pertussis incidence in Mainland China from 2005 to patterns in foodborne Disease outbreaks. J Food Eng. 2010;97:213–27.
2016. Sci Rep. 2016;6:32367.
28. Hyndman RJ. Another look at Forecast Accuracy Metrics for intermit-
Publisher’s Note
tent demand. Foresight: The International Journal of Applied Forecasting.
2006;4:43–6. Springer Nature remains neutral with regard to jurisdictional claims in
29. Aasim, Singh S, Mohapatra A. Repeated wavelet transform based ARIMA published maps and institutional affiliations.
model for very short-term wind speed forecasting. Renewable Energy. 2019.
30. Chatfield C, Yar M. Holt-Winters forecasting: some practical issues. The Statisti-
cian. 1988;37:129–40.