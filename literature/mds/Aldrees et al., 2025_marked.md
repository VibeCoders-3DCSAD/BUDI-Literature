---
conversion_metadata:
  converted_at: "2026-10-12T07:08:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Aldrees et al., 2025.pdf"
  source_pdf_sha256: "f08c53280250f7eb617a09ac7e0b6b0d86934740521257a1200dcbab11521f72"
  page_count: 24
  markdown_char_count: 95634
---

Int J Comput Intell Syst (2025) 18:60
RESEARCH ARTICLE
Behavioral Patterns in Micro‑lending: Enhancing
Credit Risk Assessment with Collaborative Filtering
and Federated Learning
Asma Aldrees1 · Sana Shahab2 · Ashit Kumar Dutta3 · Waseem Ahmad4 · Mohd Anjum5
Received: 22 January 2025 / Accepted: 18 February 2025
© The Author(s) 2025
Abstract
Credit risk assessment uses finance-based behavioural patterns for micro-lending purposes and organizations.
The repayment behaviour and credit stability patterns are analyzed across varying repayment tenures and financed
amounts. Due to limited borrower data and fluctuating financial patterns, micro-lending platforms have substan-
tial hurdles when it comes to effectively evaluating credit risk. This article introduces a Collaborative Filtering
Method using Lending Pattern Analysis (CFM-LPA). The proposed method is enhanced through collaborative
federated learning, enabling the analysis of these patterns. This approach evaluates the return rate, credit limit,
and consumer response behaviours. Federated learning processes one or more of these factors to assess diverse
lending patterns. Based on these evaluations, the behavioural factor is updated for each return period, influencing
the credit risk for subsequent return periods and supporting the financial stability of micro-lending operations.
The model is trained individually on the identified factors, allowing the behavioural factor to be filtered. New
credit risks are identified using this filtered factor from the previous return period. These insights help define
new behavioural patterns for the specified credit limit. The proposed method enhances risk detection accuracy
by 14.03% and improves return rate analysis by 13.28% across financed amounts. The above abstract is also
graphically presented.
Graphical Abstract
Keywords Behavior pattern · Collaborative filtering · Credit risk · Federated learning · Micro-lending
Int J Comput Intell Syst (2025) 18:60 https://doi.org/10.1007/s44196-025-00776-w
Vol.:(0123456789)

60 Page 2 of 24 https://doi.org/10.1007/s44196-025-00776-w
1 Introduction
Credit risk assessment is a must in every micro-lending organization. The actual credit risks are assessed using
finance-based behavioural patterns in micro-lending organizations. The behavioural patterns provide stability,
interest rate, and return capacity [1]. A unique credit risk assessment strategy is used in micro-lending organiza-
tions. The assessment strategy uses logistics functions to determine the financial risks that may occur after lend-
ing small funds or loans [2, 3]. The exact severity level of the risks is calculated to produce feasible information
for assessment services. The strategy predicts the successful finding of factors minimizing financial crises or
risk rates in money lending services [4]. A credit risk analysis technique is also used to analyze the risk ratio for
micro-lending services. The analysis technique evaluates the potential risk factors that cause credit risks to the
services [5]. The technique identifies the interest rate and predicts the credit risks based on financial stabilities.
The analysis technique provides the possibility of risks, which reduces the computational complexity of lending.
The technique improves the performance and efficiency of assessment services [6].
Behavioural patterns are analyzed and evaluated, which produces an effective dataset for credit risk predic-
tion in lending applications. The patterns provide details such as financial status, credit details, interest rates,
and the impact of micro-lending on customers [7]. A behavioural pattern analysis approach predicts credit risks
in micro-lending services. The analysis approach evaluates the impact of loan borrowers’ financial status and
consistency while paying the debts [8]. The approach identifies the difference between the behavioural patterns
and produces feasible data for detection processes. The analysis approach elevates the accuracy rate of credit risk
detection and enhances the efficiency range of the lending systems. A tracing detection method is used in lending
systems for credit risk prediction [9, 10]. The detection method uses software to analyze the behavioural pattern
of the borrower and lender’s activity on online platforms. The method provides empirical features to calculate
the credit risks as per severity. The method also reduces the computational cost during detection, enhancing the
systems’ performance. The detection method minimizes the latency range and provides optimal user lending
services [11, 12].
Machine learning (ML) methods are used in micro-lending systems for credit risk analysis services. ML meth-
ods improve the detection services’ precision and accuracy [13]. A credit risk assessment using an ML algorithm
is used in micro- and macro-lending applications. The assessment model addresses the common issues that cause
application credit risks [14]. The model uses a linear learning analysis method to analyze the overheads and factors
of the systems. The assessment model also investigates the actual cause of risks using ML, which minimizes the
energy consumption range of the systems [15, 16]. The assessment model maximizes the credit risk prediction
and reduces the financial risk factors while lending money to borrowers [17]. A random forest algorithm-based
credit risk analysis technique is also used in lending applications. The random forest algorithm analyses the
dynamic and systemic credit features to evaluate the actual stages of risks [18]. The analysis technique provides
a feasible solution to solve the issues from the applications. It also provides companion strategies to reduce risk
rates from the systems. The algorithm reduces micro-lending services’ fault and credit risk ratio [19]. The role of
consumer behaviour decides the credit risk and further lending in small-scale financial services. This customer/
consumer behaviour is defined by various factors that influence credit return policies. A precise credit level/ risk
level decision will be made based on the fluctuating influencing factors. Motivated by this factor, the proposed
credit risk analysis method is designed and discussed.
1.1 Research Gap
Data shortage, borrower variety, and privacy issues contribute to micro-lending platforms’ ongoing struggles with
proper credit risk assessment. Due to security concerns and a lack of flexibility for changing financial patterns,
traditional credit scoring algorithms often depend on centralized data collecting. Moreover, micro-lending situ-
ations often do not have access to the large amounts of labelled data needed by current machine learning-based
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w Page 3 of 24 60
methods, resulting in less-than-ideal risk projections. However, this research is not fit for decentralized financial
ecosystems since they do not adequately include privacy-preserving approaches in behavioural analysis for credit
evaluation. Accurate credit risk assessment must be achieved in micro-lending situations while protecting user
data’s privacy and security.
1.2 Objectives
This research focuses on the Collaborative Filtering Method utilizing Lending Pattern Analysis (CFM-LPA), an
attempt to improve micro-lending credit risk assessment via the integration of federated learning and collabora-
tive filtering. The main goal is to guarantee data privacy via decentralized learning and increase the accuracy
of credit risk prediction by using borrower behaviour patterns. A scalable and adaptable model that can capture
shifting financial habits is also one of the article’s goals, which aims to improve lending practices. More informed
lending choices in micro-lending contexts may be supported by this research’s robust, privacy-preserving, and
data-driven methodology, which addresses the constraints of existing credit scoring methods.
The article makes the following contributions:
1. Introducing and discussing a novel credit risk analysis method supported by federated learning and collabora-
tive learning techniques.
2. Exploring the role of various factors influencing financial stability provides insights into their combined
impact through comprehensive analysis.
3. A data-driven approach can be defined to verify the self-analytical factors of the proposed method.
4. A comparative analysis will be presented to evaluate and validate the efficiency of the proposed method.
The rest of the paper is prearranged as follows: Sect. 2 presents the related works, section suggests the CFM-
LPA model, Sect. 4 deliberates the results and discussion and Sect. 5 concludes the research paper.
2 Related Works
Zhuang et al. [20] created the GAN-LightGBM model to analyze credit risk in financial technology. The method
employs Generative Adversarial Networks (GAN) to address data imbalance and a Light Gradient Boosting
Machine (LightGBM) to estimate credit risk. The strategy improves model performance by creating realistic
synthetic data and increasing forecast accuracy. The approach provides extensive credit risk assessment capabili-
ties for financial applications. Aruleba et al. [21] used ensemble classifiers using SMOTE-ENN. The approach
combines Random Forest, Adaptive Boosting, and XGBoost classifiers with Synthetic Minority Over-sampling
Technique-Edited Nearest Neighbour (SMOTE-ENN) to increase model interpretability and alleviate class imbal-
ance. The method incorporates Shapley Additive Explanations for feature importance analysis. The strategy
improves model transparency and ensures a reliable credit risk assessment.
Yang et al. [22] presented a multi-stage ensemble model. The technique extracts relevant aspects by combin-
ing behavioural and non-financial data. To solve class imbalance, the method uses bagging-based oversampling.
The strategy increases small and medium enterprises’ credit risk prediction and management tactics. Gamba-
Santamaria et al. [23] used intrinsic estimators with penalized regression. The technique separates loan risk
into payment capacity and bank risk components. The strategy addresses multicollinearity and results in more
accurate credit risk analysis. The strategy helps policymakers comprehend systemic financial risks better, which
provides deeper insights.
Haitao et al. [24] designed an integrated supply chain management system. The strategy improves real-time data
sharing between suppliers, dealers, and customers, which leads to better credit risk management. The technique
boosts operational efficiency and decision-making capabilities. The strategy promotes better risk management
Int J Comput Intell Syst (2025) 18:60

60 Page 4 of 24 https://doi.org/10.1007/s44196-025-00776-w
on e-commerce platforms. Wang et al. [25] used Nonlinear Least Squares Support Vector Machine to develop a
specialized index system for credit risk classification in online supply chains. The approach improves analytical
precision and overall generalization performance. The strategy outperforms existing credit risk models in terms
of risk classification. The method improves online credit risk evaluation processes.
Rao et al. [26] used Particle Swarm Optimisation to fine-tune eXtreme Gradient Boosting hyperparameters to
improve auto loan credit risk assessment. The strategy optimizes parameter choices to increase model accuracy
and efficiency. The strategy lowers computational expenses while improving prediction performance. The strategy
greatly improves auto loan credit risk prediction.
Shetabi [27] suggested an evolving ensemble feature technique. The technique uses numerous algorithms to
assess credit risks dynamically. The technique improves predictive accuracy and computational efficiency. The
technique adjusts to changing risk factors in the financial technology industry. Xia et al. [28] used ML algorithms
for classification and risk prediction to manage risk on online loan platforms. The technique examines platform
activity to identify harmful behaviours and execute preventive actions. The method enhances the security and
management of online lending systems. The strategy improves risk identification and mitigation strategies.
Sinkey Jr. et al. [29] statistically analyzed risk factors. The technique examines the factors influencing loan
losses and banks’ risk management practices. The approach helps to understand the economic implications of
lending behaviour. The technique offers useful information for enhancing financial strategies in the banking indus-
try. Li et al. [30] focused on loan profit forecast. The method combines financial and non-financial information
to provide a thorough risk analysis. The strategy improves prediction accuracy and enables risk management for
small and medium enterprises loans. The strategy offers actionable insights on reducing small business credit
risks.
Wang et al. [31] used ensemble learning approaches to enhance their forecasts for student loan default. The
approach uses many classifiers to increase prediction resilience and accuracy. The method corrects the class
imbalance and improves prediction performance. The strategy provides insight into educational initiatives and
improves loan default risk management. Zhang et al. [32] created a visual early warning system to detect credit
risks associated with college net loans. The approach analyses several danger indicators in real-time to generate
early warnings. The strategy eliminates dangerous loans by timely interventions. The strategy improves debt
management and student safety at educational institutions.
Liu et al. [33] investigated risk management solutions for bank mortgage loans to improve home loan risk
management. The strategy improves decision-making by combining financial analysis and prediction models. The
strategy improves home loan risk management by identifying significant risk elements. The method establishes
a reliable framework for evaluating mortgage loan risks. Carannante et al. [34] proposed a climate risk-sharing
approach. The technique uses climatic risk indicators to determine loan viability. The strategy decreases exposure
to climate-related risks in the tourism business. The strategy promotes strong financial systems for both borrowers
and lenders. Liu et al. [35] investigated loan securitizations and risk-sharing systems to reduce revenue volatil-
ity for small enterprises. The strategy incorporates income insurance to reduce income volatility. The strategy
improves financial stability in small business-dependent areas. The strategy promotes total financial security in
the small business sector. Table 1 shows the summary of existing models.
Microlending services rely on heterogeneous patterns classified under services and consumer behaviours. The
conventional methods rely on return rate and customer history for further lending and validation. ML-based solu-
tions rely on the statistical computation of return rate to increase the credit level and thereby infer the reduction
rates. However, this is feasible for a large financial service, whereas in a low-interest-rated financial service, the
different patterns (customer return and lending) impact credit risks differently. These include delayed response
or failed returns across increasing scheduled tenures. This article proposes a pattern-converted behaviour factor
assessment method using federated learning to address these diverse issues. This method validates financial and
customer factors to identify filtered risks in lending credits. Traditional machine learning models and ensemble
approaches comprise the bulk of the existing literature on micro-lending credit risk assessment; however, these
methods often depend on centralized data sources, which might lead to privacy problems. A lack of complete
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
|                                    |                                   |                                            |                                          |                                           |                                       |                                          |                                                                                | Page 5 of 24                            |    60                                 |
| ---------------------------------- | --------------------------------- | ------------------------------------------ | ---------------------------------------- | ----------------------------------------- | ------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------- | ------------------------------------- |
|                                    |                                   |  rof stesatad laicnanfi evisnetxe seriuqeR |  evitisnes dna evisnetni yllanoitatupmoC |                                           |                                       |  ytilibaliava eht no sdneped ecnamrofreP |                                                                                |                                         |                                       |
|                                    |                                   |                                            | -nanfi gnoma noitargetni hgih seriuqeR   |  elitalov ylhgih ni ssenevitceffe detimiL |                                       |                                          |  ycarucca eht no sdneped ssenevitceffE  egagtrom lacirotsih evisnetxe seriuqeR |  decudni-etamilc etagitim ylluf ton yaM | -aluger dna ytixelpmoc noitatnemelpmI |
|                                    |                                   |                                            |                                          |  ot tpada ot setadpu tneuqerf seriuqeR    | -upinam lairasrevda htiw elggurts yaM |                                          |                                                                                |                                         |                                       |
|  syawla ton yam atad detareneg-NAG |                                   |  tnereffid ot llew ezilareneg ton yaM      |                                          |                                           |  laicnanfi gnigreme erutpac ton yaM   |  rof ytilibaterpretni detimil evah yaM   |                                                                                |                                         |                                       |
|                                    |  ot eud evisnepxe yllanoitatupmoC |                                            | sniahc ylppus dna snoitutitsni laic      |                                           |                                       |                                          |                                                                                |                                         |                                       |
seitixelpmoc dlrow-laer erutpac
noitceles retemaraprepyh ot
sledom elbmesne elpitlum
atad laicnanfi esrevid fo
|     |     |     |     | stnemnorivne cimonoce | smroftalp naol fo noital | gnidnel latigid ni sksir |     |     |     |
| --- | --- | --- | --- | --------------------- | ------------------------ | ------------------------ | --- | --- | --- |
srotacidni gninraw fo
|     |     | smetsysoce laicnanfi |     | srotcaf ksir gnignahc |     |     |     |     |     |
| --- | --- | -------------------- | --- | --------------------- | --- | --- | --- | --- | --- |
snoitamitse esicerp
skcohs cimonoce
|     |     |     |     |     |     |     |     | gniniart rof atad | segnellahc yrot |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --------------- |
srekamycilop
snoitatimiL
|     |                                                                           |  sevorpmi ,ytiraenillocitlum sesserddA |                                     |     |  noitagitim ksir dna ytiruces secnahnE |                                      |                                          |                                        |     |
| --- | ------------------------------------------------------------------------- | -------------------------------------- | ----------------------------------- | --- | -------------------------------------- | ------------------------------------ | ---------------------------------------- | -------------------------------------- | --- |
|     | -ropmi erutaef rof PAHS setaroprocnI ycnerapsnart serusne ,sisylana ecnat |                                        | -arepo dna gnikam-noisiced sevorpmI |     | -knab otni sthgisni cimonoce sedivorP  |  secnahne ,ecnalabmi ssalc sesserddA |  retteb rof stnemele ksir yek sefiitnedI | -rob rof smetsys laicnanfi snehtgnertS |     |
tnemeganam tbed evitcaorp selbanE
|  ,atad citehtnys citsilaer setareneG |     |  laicnanfi-non dna laroivaheb sesU |  dna noisicerp lacitylana secnahnE | -itpo ,tsoc lanoitatupmoc secudeR  dna ycarucca evitciderp sevorpmI |     |  dna ycarucca noitciderp sevorpmI |     |     |     |
| ------------------------------------ | --- | ---------------------------------- | ---------------------------------- | ------------------------------------------------------------------- | --- | --------------------------------- | --- | --- | --- |
ytilibailer noitciderp secnahne  dna ytilitalov emocni secudeR
noisneherpmoc ksir cimetsys
|     |     | tnemssessa retteb rof atad |     | ycneicffie lanoitatupmoc |     |     |     |     |     |
| --- | --- | -------------------------- | --- | ------------------------ | --- | --- | --- | --- | --- |
tnemeganam ksir tiderc
sretemaraprepyh sezim
srednel dna srewor
|     |     |     |                   |     |     | seigetarts ksir gni |                 |                 | ytiruces secnahne |
| --- | --- | --- | ----------------- | --- | --- | ------------------- | --------------- | --------------- | ----------------- |
|     |     |     | ycneicffie lanoit |     |     |                     | tnemeganam ksir | gnikam-noisiced |                   |
noitazilareneg
| egatnavdA |                                       |     |                                                                              |                                        | seigetarts                                                                     |                                      |                                         |                                      |                                         |
| --------- | ------------------------------------- | --- | ---------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------ | --------------------------------------- | ------------------------------------ | --------------------------------------- |
|           |                                       |     |                                                                              | -ciderp ksir tiderc naol otua secnahnE |  enilno ni sroivaheb lufmrah sefiitnedI  sessol naol fo gnidnatsrednu sevorpmI | snaol EMS rof sisylana ksir secnahnE | sgninraw ksir tiderc emit-laer sedivorP |                                      |                                         |
|           |  dna ytilibaterpretni ledom sesaercnI |     |  rof gnirahs atad emit-laer secnahnE  ni noitacfiissalc ksir tiderc sevorpmI |                                        |                                                                                |  fo ycarucca dna ecneiliser sevorpmI | tnemssessa ksir naol emoh secnahnE      |  detaler-etamilc ot erusopxe secudeR |  llams rof ytilibats laicnanfi sevorpmI |
-eganam ksir tiderc EMS secnahnE
 tnemyap otni ksir naol setarapeS
 ksir tiderc stsujda yllacimanyD
 noitciderp ksir tiderc sevorpmI
ecnalabmi ssalc setaivella
tnemeganam ksir tiderc
ksir knab dna yticapac
sniahc ylppus enilno
secitcarp ksir dna
sksir laicnanfi
snoitciderp
sessenisub
ycarucca
sledom
| stluseR |     | tnem |     |     | snaol |     |     |     |     |
| ------- | --- | ---- | --- | --- | ----- | --- | --- | --- | --- |
noit
-serger dezilanep + srotamitse cisnirtnI
|     |  ,tsooBadA ,FR( srefiissalc elbmesnE |     |  tnemeganam niahc ylppus detargetnI -ceV troppuS serauqS tsaeL raenilnoN |                                     |                                      |                                     |                                      |     |  rof gnirahs-ksir + noitazitiruces naoL |
| --- | ------------------------------------ | --- | ------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------ | ----------------------------------- | ------------------------------------ | --- | --------------------------------------- |
|     |                                      |     |                                                                          | noitceles erutaef elbmesne gnivlovE |  enilno rof sledom noitacfiissalc LM |  naol tneduts rof gninrael elbmesnE | -uts rof metsys gninraw ylrae lausiV |     |                                         |
-gab + ledom elbmesne egats-itluM
|  atad rof NAG( MBGthgiL-NAG  ksir rof MBGthgiL + gnicnalab |     |     |     |     | srotcaf ksir fo sisylana lacitsitatS |                                 |  tnemeganam ksir egagtrom knaB |                               |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | ------------------------------------ | ------------------------------- | ------------------------------ | ----------------------------- | --- |
|                                                            |     |     |     |     |                                      | -nanfi( gnitsacerof tfiorp naoL |                                | hcaorppa gnirahs-ksir etamilC |     |
NNE-ETOMS + )tsooBGX
gnilpmasrevo desab-gnig
|     |     |     |     | tsooBGX dezimitpo-OSP |     | )atad laicnanfi-non + laic |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | -------------------------- | --- | --- | --- |
noitciderp tluafed
| sledom gnitsixe eht fo yrammuS  |     |     |     |             |              |     | sksir naol tned |     |     |
| ------------------------------- | --- | --- | --- | ----------- | ------------ | --- | --------------- | --- | --- |
|                                 |     |     |     | enihcaM rot | ksir gnidnel |     |                 |     |     |
)noitamitse
sledom
| dohteM |     |     | metsys |     |     |     |     |     | sEMS |
| ------ | --- | --- | ------ | --- | --- | --- | --- | --- | ---- |
nois
]32[ .la te airamatnaS-abmaG
]43[ .la te etnannaraC
]92[ .la te .rJ yekniS
| ]02[ .la te gnauhZ | ]12[ .la te abelurA |                  |                                     |                 |                 |                  |                   |     |                 |
| ------------------ | ------------------- | ---------------- | ----------------------------------- | --------------- | --------------- | ---------------- | ----------------- | --- | --------------- |
|                    |                     |                  | ]42[ .la te oatiaH ]52[ .la te gnaW |                 |                 | ]13[ .la te gnaW | ]23[ .la te gnahZ |     |                 |
|                    |                     | ]22[ .la te gnaY |                                     | ]62[ .la te oaR |                 |                  |                   |     |                 |
|                    |                     |                  |                                     |                 | ]82[ .la te aiX |                  | ]33[ .la te uiL   |     | ]53[ .la te uiL |
|                    |                     |                  |                                     | ]72[ ibatehS    |                 | ]03[ .la te iL   |                   |     |                 |
 1 elbaT )s(rohtuA
Int J Comput Intell Syst           (2025) 18:60

60 Page 6 of 24 https://doi.org/10.1007/s44196-025-00776-w
integration of borrower behavioural patterns limits the forecasting accuracy of techniques like GAN-LightGBM
and SMOTE-ENN, which address data imbalance and feature selection. In addition, the difficulties of data frag-
mentation among financial institutions are mostly ignored in most research, resulting in inadequate risk evalu-
ations and incomplete borrower profiles. Research on the combination of federated learning with collaborative
filtering for customized credit risk prediction is still in its early stages, but it provides a privacy-preserving option.
Furthermore, there are significant inequalities in accountability and long-term dependability caused by the fact
that current models seldom ever deal with problems such as model drift, adversarial robustness, and demographic
biases in loan choices. Improving risk detection while guaranteeing data privacy and transparency is the goal of
the proposed CFM-LPA paradigm, which employs federated learning and collaborative filtering to fill these gaps.
3 Data Description
Credit risk analysis data from [36] is used to validate the proposed method using fuzzy optimization. The data
is classified under 12 features utilizing personal and loan-related information. The status and history of the data
provided are used to analyze the behaviour factor. The behaviour factor computation process uses the return rate,
prompt return, and credit limit. Thus, the data used to evaluate the proposed method is described in Fig. 1.
The data are split into three blocks: initial input (return + Response) and behaviour pattern. For this purpose
the above-referenced data with the following feature values is used: the age ranges between (20 and 45), income
(4 K to 2039 K), ownership (rented, own, mortgage, employment tenure (1 to 31 yrs), loan purpose (personal,
education, venture, medical, home needs), loan grade (A to D), loan amount (0.5 K to 35 K), interest rate (5.42
to 23.22), loan status (0-nil, 1-pending) per cent of loan income (0 to 0.83), the credit history (2 to 30 years). The
above data are provided for 32,581 record sets as collected from the dataset. The notable parameters: credit his-
tory, grade, status, and income % decide the behaviour patterns of the consumers. This pattern detection finalizes
the credit risk under different lending periods (Refer to Fig. 1).
4 Proposed Collaborative Filtering Method Using Filtering Pattern for Credit Risk
Analysis
Credit risk assessment is one of the most important aspects of the sustainability and profitability of micro-
lending organizations. In micro-lending, understanding the financial behaviour of borrowers is critical to
minimize defaults and optimize credit distribution. This incorporates a Collaborative Filtering Method (CFM)
to enhance credit risk assessment using Lending Pattern (LP) analysis. The critical factors, including return
Fig. 1 Data used for evaluation
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
|     |     |     |     |     |     |     |     |     |     |     |     | Page 7 of 24  |    60  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ |
rates, credit limits, and consumer response behaviours, were evaluated through collaborative federated learn-
ing. The federated approach allows for the decentralized analysis of lending patterns in a manner that ensures
data privacy and security requirements in any financial system. The CFM analyzes such factors over suc-
cessive repayment periods, identifies behaviour trends, and refines its credit risk assessment. This approach
offers strong credit stability prediction and limit optimization to ensure the financial stability of micro-lending
|     |     |     |     |     | M (t) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
organizations. The following equation  L  measures the micro-lending factors that help to monitor and
predict the risk in the environment at a time.
|     |     | (t) | =   | +Br | ×   | ×E   | +B  |      | +C   | × 1+B | (t+1) |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---- | ---- | ----- | ----- | --- | --- |
|     |     | M   | C   |     | I   |      |     |      |      |       |       | .   | (1) |
|     |     | L   |     | lm  | C   | rate | con | fact | risk |       | fact  |     |     |
|     |     |     | (   |     | ((  |      | )   | )    |      | ) (   |       | )   |     |
To predict the risk in micro-lending, it is important to monitor and analyze factors that lead to environmental
C
risk. The credit limit is denoted as  lm which is provided to the borrower with a particular limit. It helps to meas-
ure how the credit is extended to the borrower over time. A high credit limit may indicate a financial risk and
affect the behavioural pattern. The borrower’s credit score is represented as Br C and  B fact measures the behaviour
|     |     |     |     |     |     |     |     |     |     | I   | ×E  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factor of the borrower. It helps to identify the external risk factors. The term  rate con  measures the combined
analysis of interest rates and economic conditions such as inflation with variations in credit rate. The credit risk
|                |     |     |     |     |     |     |     |     |     | (   |     | )       |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
| is denoted as  | C   |     |     |     |     |     |     |     |     |     |     | B (t+1) |     |
risk which monitors the risk factors during the credit period. The term  fact  measures the
behaviour factor for the next time to predict the upcoming environmental credit risk. This helps monitor the
micro-lending organization to adapt to changing financial conditions and mitigate financial risk. The return rate
R
| is measured as  |     | rate in the equation below. |     |     |     |      |     |     |     |     |     |     |     |
| --------------- | --- | --------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |                             |     | R   | = R | +exp | C   | ×Br | +M  | (t) |     |     |     |
amt−tot
|     |     |     |     | rate | amt     |       |     | lm    | C    | L   |     |     |     |
| --- | --- | --- | --- | ---- | ------- | ----- | --- | ----- | ---- | --- | --- | --- | --- |
|     |     |     |     |      | wh�ereR | � >   | C ∀ | amt−E |      |     |     |     |     |
|     |     |     |     |      |         | ra te | lm� |       | �con | ⎫.  |     |     | (2) |
t
|     |     |     |     |         |     |      |        | C      | ×I       | ⎪   |     |     |     |
| --- | --- | --- | --- | ------- | --- | ---- | ------ | ------ | -------- | --- | --- | --- | --- |
|     |     |     |     | R       | =   | B    | ×�     | risk   | rate,i � |     |     |     |     |
|     |     |     |     | amt−tot |     |      | fact,i | 1−(1+I | )t       | ⎪   |     |     |     |
|     |     |     |     |         |     | i=1� |        |        | rate,i   |     |     |     |     |
|     |     |     |     |         |     |      |        | �      | ��       | ⎬   |     |     |     |
|     |     |     |     |         |     | ∑    |        |        |          | ⎪   |     |     |     |
|     |     |     |     |         |     | R    |        |        |          | ⎪   |     |     |     |
Here, the total return amount is denoted as  amt−tot and the total amount co nsidered for micro-lending is rep-
⎭
R
resented as amt . The term  amt−tot  computes the ratio of the amount to be returned by the borrower over the
amt
amount they borrowed. It (is evalu)ated by analyzing the borrower’s credit limit and behaviour factor. When
| R > C | ∀ amt−E |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rate lm con  indicates that the return rate exceeds the credit limit, which ensures a possibility of risk.
The total am ount is moni tored for each month  i  to  t  to avoid complications in lending. The term  C ×I rate,i helps
|     | (   |     | )   |     |     |     |     |     |     |     |     | risk |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
t
to adjust the credit risk based on  B fact,i and  1+I  balance the interest rate over time. This helps to monitor
rate,i
both credit risk and the overall amount needed to be returned by the borrower to ensure an accurate return rate
|     |     |     |     |     | (   |     | )   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C
in the micro-lending process. The following equation  lm measures the credit limit.
C
|     |     |     |     | C = | B    | ×Br  | + 1+C |      | ×   | risk |     |     |     |
| --- | --- | --- | --- | --- | ---- | ---- | ----- | ---- | --- | ---- | --- | --- | --- |
|     |     |     |     | lm  | fact | risk |       | hist |     | E    |     |     |     |
con
|     |     |     |     |     |     | 0 ≤ | B r ≤   | 1   | �   | �   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | �   |     | � risk� |     | �   | ⎫.  |     |     |     |
|     |     |     |     |     | t   |     |         |     |     |     |     |     | (3) |
⎪
|     |     |     |     | Br   | =   | amt+ | Br  | −C   | ×E  |       |     |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- | ----- | --- | --- | --- |
|     |     |     |     | risk |     |      | C   | hist |     | con ⎪ |     |     |     |
|     |     |     |     |      | i=1 |      |     |      |     | ⎬     |     |     |     |
|     |     |     |     |      | ∑�  |      | �   |      | ��  | ⎪     |     |     |     |
In the above equation, the borrower risk during lending is denoted as Br ⎪
⎭k which monitors the risk from the
ris
C
borrower’s side. The term  1+C  measures the influence of credit history and the term  risk  defines the
|     |     |     |     | hist |     |     |     |     |     |     |     | E   |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
con
environmental factors that c(ause cred)it risk. It evaluates the borrower factor after considering( the c)redit history.
If 0 ≤ Br ≤ 1 is true; it normalizes the borrower risk, avoiding deviations in behaviour patterns. The term
risk
Br −C  measures the variations between behavioural patterns and credit history to evaluate the borrower’s
| C   | hist |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
payment details. The relation between the return rate and the credit limit is diagrammatically presented in Fig. 2.
| (   | )   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Int J Comput Intell Syst           (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
   60   Page 8 of 24
Fig. 2   Illustration of return rate and credit limit relation
The relationship between return rate and  C lm is presented using Fig. 2 representations. If  R = E ×t  then
|     |     |     |     |     |     |     |     |     |     | rate con |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
Br = good, and the rate of return with the score is high. This type of customer exhibits go
|     |     |     |     |     |     |     |     |     |     | od behaviour pa | tterns  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- |
| c   |     |     |     |     |     |     |     |     |     | (               | )       |
without change in repayment. The “loan status = 0” retention in the appropriate tenure reduces the credit risk for the
customers. The improper return rate is verified under single/multiple tenures to estimate the high risk/ limit reduction
≤ ≤
across various (progressive) tenures. The condition (0  Br 1)  verifies the need for normalization to check if
risk
| R   |     |     |     |     |     |     | Br −C |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
rate is feasible. This relationship is exploited further to validate the  c hist  across various tenures (Fig. 2). The
suggested CFM-LPA model’s collaborative filtering method uses past lending trends to evaluate borrowers’ similar
|     |     |     |     |     |     |     | (   | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
features and, by extension, their credit risk. Utilizing a combination of user- and item-based filtering algorithms, it
generates risk ratings by analyzing lending behaviour, repayment history, and financial transactions. This is made
easier using the federated learning architecture, allowing decentralized model training across several banks without
exposing sensitive information. This improves generalizability across varied datasets while also preserving privacy.
With the use of tools like Federated Averaging (FedAvg), the federated model may improve risk assessment models
and reduce data silo problems by aggregating local changes. Further optimization is necessary to address non-IID
data distributions, communication costs, and model drift. This will guarantee scalable and resilient performance in
real-world financial applications. Based on this factor, the analysis of Br
risk is presented in Fig. 3.
Credit risk assessment incorporates risk factors such as default rate, repayment, and credit history. It is moni-
tored with credit limit over the borrowers at a time. The obtained credit risk assessment score is updated using
federated learning with LPs from different scenarios. The proposed method ensures high credit risk assessment
| C (t+1) | = Len | +log | Br  | ×C  | × 1+Len |     |     |     |     |     |     |
| ------- | ----- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
risk adjust C hist pat  which accurately monitors the financial instability. For
example, a borrower with a high debt and consistent payments shows high credit risk. A borrower with a stable return
|     | (   |     | (   |     | )) ( | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
rate and timely repayments has a lower credit risk score. This high credit risk helps to identify the borrowers with
increasing risks in their tenure (Fig. 3). It measures the organization’s credit policy and risk toward the credit amount.
This adjusts the credit limit based on the borrower’s lending capacity to ensure fair lending decisions. The patterns
for return and credit stability are analyzed under different repay tenures, and the sum finance which is expressed as
| R U  | C     | U      |                         |     |     |     |     |     |     |     |     |
| ---- | ----- | ------ | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|      |  and  |        |  in the equation below. |     |     |     |     |     |     |     |     |
| rate | repay | stable | repay                   |     |     |     |     |     |     |     |     |
| (    | )     | (      | )                       |     | t   |     |     | Br  |     |     |     |
C
|     |     | R   | U          | =    | B ×R   | + 1−Dr |                                                  | +   | ×C  | ,   |     |
| --- | --- | --- | ---------- | ---- | ------ | ------ | ------------------------------------------------ | --- | --- | --- | --- |
|     |     |     | rate repay |      | fact,i | rate   | i                                                | amt | lm  |     | (4) |
|     |     |     |            |      | i=1    |        |                                                  | (   | )   |     |     |
|     |     |     | (          | ) ∑( |        | ) (    | )                                                |     |     |     |     |
|     |     |     |            |      |        |        | Int J Comput Intell Syst           (2025) 18:60  |     |     |     |     |

https://doi.org/10.1007/s44196-025-00776-w
|     |     |     |     |     |     |     |     |     |     |     |     | Page 9 of 24  |    60  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ |
Fig. 3   Credit risk analysis
|     |        |       |     | t    |     | amt×I |       | C   | +C      |     |         |     |     |
| --- | ------ | ----- | --- | ---- | --- | ----- | ----- | --- | ------- | --- | ------- | --- | --- |
|     |        |       |     |      |     |       | rate  |     | lm risk |     |         |     |     |
|     | C      | U     | =   | 1+Dr |     | ×     |       | ×   |         | × R | −Br     | .   |     |
|     | stable | repay |     |      | i   | 1+E   |       |     | C       |     | amt−tot | C   | (5) |
|     |        |       |     | i=1  |     | (     | con ) | (   | hist    | )   |         |     |     |
|     |        | (     | )   | ∑(   | )   |       |       |     |         | (   |         | )   |     |
|     |        |       |     |      |     | U     |       |     | B       | ×R  |         |     |     |
The different repayment tenure is denoted as  repay in which the term   measures the behaviour
|     |     |     |     |     |     |     |     |     |     | fact,i | rate |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | --- |
i
factor with the return rate for the period   to monitor the accurate repayment amount. The default payment by
|     |     |     |     |     |     |     |     |     | (    |     | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |     |     |     | Dr  |     |     | 1−Dr |     |     |     |     |
the borrower for each month is denoted as  i in which the term  i  measures the impact of default
|     |     |     |     |     |     |     |     |     |     |     | ≤   | ≤   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
payment on the overall lending process. The behaviour patterns we re adjus ted as 0 C 1 for consistent
|     |     |     |     |     |     |     |     |     | (   | )   |     | lm  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
borrower lending over the entire repayment tenure. The financial reliability of the borrower is considered in
a m t× I
the credit stability. A high inflation with instability in credit occurs when  E ≥ 0 . The term  rate  esti-
|     |     |     |     |     |     |     |     |     |     | con |     | 1 + E |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
con
|     |     |     |     |     |     |     |     |     |     |     |     | (   | )   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mates the overall amount that needs to be repaid by the borrower. The return rate analyzes how effectively
the amount is repaid over the given tenure, and credit stability measures the borrower’s financial stability
under different repayment conditions. This helps to analyze the variations in repayment in the micro-lending
|     |     |     |     |     | H (t) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
environment. The following equation  res  measures the response rate.
|     | H   | (t) = | R    | +C  | × R  | U +C  |        | U     | ×    | 1−Dr | + 1+E | .   |     |
| --- | --- | ----- | ---- | --- | ---- | ----- | ------ | ----- | ---- | ---- | ----- | --- | --- |
|     | res |       | rate | lm  | rate | repay | stable | repay |      | i    |       | con | (6) |
|     |     |       | (    | )   | (    | ( )   |        | (     | )) ( | )    | (     | )   |     |
The influence of return rate and credit stability measures the borrower’s behaviour to the credit response.
| R   | U   | +C  |     | U   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The term   measures the combined relationship of the return rate with the credit
|     | rate | repay | stable | repay |     |     |     |     |     |     |     |     |     |
| --- | ---- | ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rate. It measures how much of the loan amount is repaid over the tenure and how much is credited to the
| (   | (   | )   |     | (   | ))  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | R   |     |     |     |     |     |     | C   |     |     |     |     |
borrower. A high  rate ensure accurate repayment behaviour and a high  stable indicate high potential risk and
stable behaviour. The term  1−Dr  measures the impact of default rate in which a high Dr i reduce the default
i
E
from the borrower side. A h igh  con)  increases the risk of environmental factors that reduce the response in the
(
Int J Comput Intell Syst           (2025) 18:60

60 Page 10 of 24 https://doi.org/10.1007/s44196-025-00776-w
lending process. This helps to predict the borrower’s loan repayment and performance to be adjusted for the
borrower’s specific behaviour. The behaviour pattern detection process is presented in Algorithm 1.
Algorithm 1 Behavior Pattern Detection
A CFM using an LP helps to analyze the credit risk, which is discussed in the following sections.
4.1 Collaborative Filtering
The historical data of multiple borrowers were evaluated using the CFM and LP to analyze patterns of repayment
behaviour and predict future loan performance. It monitors repayment history, credit limits, return rates, and
borrower behaviour in different segments to analyze the similarities between borrowers. The identified patterns
were used to classify and predict new borrowers’ credit and repayment defaults. LP analysis mainly identifies the
consistent traits of borrowing behaviour, such as timely repayments, the proportion of loans repaid, and financial
stability indicators. CFM enhances lending decisions through federated learning without exchanging borrower-
specific data directly to maintain privacy. The system filters relevant behaviour factors to predict the borrower’s
future repayment behaviour and determine the associated credit risk. The borrower’s profile was updated every
repayment period to change behaviours for accurate credit risk assessments and better lending decisions in suc-
cessive cycles. The following equation Len pat measures the process of LPs for credit risk.
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
|     |     |     |     |     |     |     | Page 11 of 24  |    60  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ |
Fig. 4   Lending pattern analysis
t
amt×C
|         |     | Len =      |        | risk +  | 1−Dr     |     |     |     |
| ------- | --- | ---------- | ------ | ------- | -------- | --- | --- | --- |
|         |     | pat        | 1−(1+I | )       | i        |     |     |     |
|         |     | i=1        |        | rate    |          |     |     |     |
|         |     | adjust∑=�R |        | ×C�     |          |     | .   | (7) |
|         |     | Len        |        |         | +�H (t)� |     |     |     |
|         |     |            | rate   | lm      | res      |     | ⎫   |     |
| C (t+1) | =   | Len +log   | Br     | ×C      | × 1+Len  | +E  | ⎪   |     |
| risk    |     | adjust     | �      | C h�ist |          | pat | con |     |
⎬
|     | �   | amt×C | �   |     | �� � | �   | ⎪   |     |
| --- | --- | ----- | --- | --- | ---- | --- | --- | --- |
In the above equation, the term  risk  measures the repayment of individual b⎭orrowers using interest
|     |     | 1−(1+I ) |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- |
rate
rates. This is adjusted using the def(ault rate to) avoid fault predictions. The formulation of Len adjust evaluates the
adjusted LPs to improve the prediction for new borrowers based on the previous response. It ensures privacy
|     |     | C   | (t+1) |     |     |     | (t+1) |     |
| --- | --- | --- | ----- | --- | --- | --- | ----- | --- |
during lending between borrowers. The term  risk  measures the credit risk for time   to monitor the
next risk period during lending. This combines the adjusted and actual LP with credit history to ensure accurate
prediction. Federated learning continuously updates this LP to ensure that the new borrower is assessed based on
the current LPs and economic conditions. LP analysis is presented in Fig. 4.
The variations in risk factors may lead to high risk in the micro-lending platform. These variations were moni-
tored and analyzed using pattern analysis. The proposed method, which ensures consistent repayment, ensures
high pattern analysis. This high value indicates strong patterns that align with borrowers’ financial stability and
consistent behaviour. Incorporating federated learning aggregates data across varying lending scenarios with pri-
vacy to analyze the patterns. A borrower with a stable pattern of repayments for every month indicates a smooth
Int J Comput Intell Syst           (2025) 18:60

60 Page 12 of 24 https://doi.org/10.1007/s44196-025-00776-w
lending process without risk. A borrower with irregular repayment and behaviour patterns leads to abnormal
patterns and indicates a potential risk during lending. This high pattern analysis enhances the understanding of
borrower behaviour over time (Fig. 4). The filtering process is described in Algorithm 2.
Algorithm 2 Filtering Process
4.2 Role of Federated Learning
Federated learning is incorporated to learn the pattern variations for multiple lenders and borrowers. In the LP
credit risk assessment, federated learning ensures the data privacy of various micro-lending entities. Federated
learning evaluates the risk that drives return rates, credit limits, and repayment behaviour among diverse micro-
lenders. The system excludes sensitive information related to the borrowers to conform to the LP on data pri-
vacy. It generalized patterns in lending to avoid the risk based on high-risk detection. The historical credit rate is
constantly updated to capture temporal shifts in borrower behaviour and financial risk. A decentralized method
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
|     |     |     |     |     |     |     |     |     |     |     | Page 13 of 24  |     |    60  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ |
improves the quality of risk-based lending predictions without affecting borrowers’ confidentiality. Federated
learning analyzes a minimum of one or all of the above factors to verify different LPs, which is termed as Len (t)
fed
in the equation below.
t
|     |     |     |     |      |       | C   | U            | +Br   |     |      |       |     |     |
| --- | --- | --- | --- | ---- | ----- | --- | ------------ | ----- | --- | ---- | ----- | --- | --- |
|     |     |     |     |      |       |     | stable repay |       | C   |      |       |     |     |
| Len | (t) | =   | Len | ×C   | (t+1) | ×   |              |       |     | + 1+ | Dr ×E | .   | (8) |
|     | fed |     | pat | risk |       |     | (1+I         |       |     |      | i     | con |     |
|     |     |     |     |      |       | (   |              | rat)e | )   |      |       |     |     |
i=1
|     |     | ∑(  |     |     | )   |     |     |     |     | (   | (   | ))    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
|     |     |     |     |     |     |     | (   | )   |     |     | ×C  | (t+1) |     |
The actual lending data are processed into an LP for each borrower based on  Len  to enhance
|     |     |     |     |              |      |     |     |     |     |     | pat risk |     |     |
| --- | --- | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | -------- | --- | --- |
|     |     |     | C   | (U           | )+Br |     |     |     |     |     |          |     |     |
|     |     |     |     | stable repay | C    |     |     |     |     |     |          |     |     |
the lending prediction. The term  (1+I )  monitors the relative importan(ce of the stable repay)ment credit
rate
based on the borrower. It analyz(es the environm)ental conditions that affect the borrower’s behaviour. The term
1+ Dr ×E  measures the influence of default rates and environmental conditions that affect the overall LP.
i con
This helps monitor the borrower’s repayment credit during the entire micro-lending process. It identifies the
( ( ))
fluctuations that affect the repayment behaviour in the lending process. The following equation Ft (t)
bh  formulates
the behaviour pattern over time.
|     |     |     | Ft    | =   | U R   | ×C   | −Dr(t)+H |     |     | (t) |     |     |     |
| --- | --- | --- | ----- | --- | ----- | ---- | -------- | --- | --- | --- | --- | --- | --- |
|     |     |     | bh-in |     | repay | rate | stable   |     | res |     |     |     |     |
|     |     |     |       |     | �     |      | �        |     |     |     |     |     |     |
⎫
|     |     |     |        | U     | = a m t due | ×amt× | R     | ×C   |     | ⎪.    |     |     |     |
| --- | --- | --- | ------ | ----- | ----------- | ----- | ----- | ---- | --- | ----- | --- | --- | --- |
|     |     |     |        | repay |             |       |       | rate | lm  |       |     |     | (9) |
|     |     |     |        |       | a m t       |       |       |      |     |       |     |     |     |
|     |     |     |        |       | paid        |       |       |      |     | ⎪     |     |     |     |
|     |     |     |        |       | �           | �     |       |      |     |       |     |     |     |
|     |     |     |        |       |             |       | �     |      | �   | ⎪     |     |     |     |
|     |     |     | Ft (t) | = Len | (t)×Ft      |       | × 1+E |      | ∀U  | ⎬     |     |     |     |
|     |     |     | bh     |       | fed         | bh-in |       | con  |     | repay |     |     |     |
⎪
|     |     |     |     | �   |     |     | � � |     | �   | ⎪   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Here, the term Ft ⎪
bh−in measures the initial behaviour pattern to monitor the rep ⎭ ayment consistency. It captures
the borrower’s ability to meet the repayment rate consistently in the lending process. The repayment is measured
by evaluating the due amount over the paid amount by the borrower, which is represented as amt due and amt paid .
U
It helps to reduce the behaviour pattern when there is a high default rate in the market. A high  repay indicates the
|     |     |     |     |     |     |     |     |     |     |     |     | Len (t)×Ft |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
borrower’s credit inefficiency, and a low repayment rate indicates a high return rate. The term  fed bh-in
combines federated lending with the initial behaviour factor to balance the risk factors. The lender can assess
|     |     |     |     |     |     |     |     |     |     |     | (   |     | )   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the credit risk according to the initial behavioural factor. Financial adaptability captures income fluctuations and
spending behaviours; loan purpose categorizes lending patterns (e.g., business vs. personal use) to identify risk
profiles; repayment consistency tracks timely and late payments to assess reliability; loan frequency indicates a
borrower’s dependency on micro-loans; peer influence analyzes how similar borrowers impact creditworthiness;
and financial adaptability tracks repayment consistency. By including these parameters in collaborative filtering,
the system can estimate credit risk based on previous patterns by mapping borrowers with similar lending hab-
its. Federated learning allows pattern detection among several lenders without sacrificing privacy by allowing
decentralized institutions to communicate updated models instead of raw data safely. This Ft (t)∀U
|     |     |     |     |     |     |     |     |     |     |     |     | bh repay ensures  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
the model’s adaptability to enhance the borrower even during environmental conditions. The following equation
C
period models the credit period in the lending process.
|     |     |        |        |      |       | amt   |          |      |          |          | Dr     |     |      |
| --- | --- | ------ | ------ | ---- | ----- | ----- | -------- | ---- | -------- | -------- | ------ | --- | ---- |
|     | C   | =      | Br     | +C   | × 1+  |       |          | +log | 1+I      | +        | i ,    |     |      |
|     |     | period | C      | hist |       |       |          |      |          | rate     |        |     | (10) |
|     |     |        |        |      |       | amt   |          |      |          |          | E      |     |      |
|     |     |        |        |      | (     | (     | mon))    |      |          |          | ( con) |     |      |
|     |     |        | (      |      | )     |       |          |      | (        | )        |        |     |      |
|     |     |        |        |      |       | +C    | ≥ 𝜑andDr |      | ≤ 𝜑      |          |        |     |      |
|     |     |        |        |      | if Br |       |          |      | maxC     |          |        |     |      |
|     |     |        |        |      | C     | hist  |          | i    |          | t period |        |     |      |
|     |     | f      | C      | =    |       |       |          |      |          |          | .      |     | (11) |
|     |     |        | period |      | if Br | +C    | < 𝜑andDr |      | > 𝜑 minC |          |        |     |      |
|     |     |        |        | {    | ( C   | hist) |          | i    |          | period   |        |     |      |
t
|     |     | (   |     | )   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | (   |     | )   |     |     |     |     |     |     |
Int J Comput Intell Syst           (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
   60   Page 14 of 24
Fig. 5   Behaviour factor estimation using federated learning
The amount to be paid monthly by the borrower is denoted as amt
mon which is measured over the total
|     |     |     |     |     |     | 1+  | amt |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
amount that is lent to the borrower. The term   monitors the loan tenure to the borrower and its
amt
mon
|     |     |     | 1+I |     | (   | (   | ) ) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
influence on the risk. The term  rate  mea sures  the int er est needed to repay during the tenure. Borrowers
with poor credit and historical scores will have low credit periods. Borrowers with high credit and historical
|     |     |     | (   |     | )   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | E   |     |     |     | Dr  |     |     |
scores will have high credit periods. A high  con reduce the credit period with a high  i should be reduced
to minimize the risk. The computation of  f C  evaluates when the credit period becomes maximum and
period
𝜑, which predicts the credit
minimum in the lending process. It is monitored over a predefined threshold
|     |     |       |          |     | (   | )   |     |     |     |     |     |
| --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Br +C | ≥ 𝜑andDr |     | ≤ 𝜑 |     |     |     |     |     |     |
period. When  C hist i  then the credit period is considered as maximum, and
| Br +C | 𝜑an | dDr 𝜑 |     |     |     |     |     |     |     |     | B (t) |
| ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
C hist i  ind icates the minimum credit period based on the LP. The following equation  fact
|     | (   |     | )   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
measures the behavior pattern based on the change in the credit period.
| �   | �   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ⟨   | ⟩   |     |     |     |     |     |     |     |     |     |
t
O
|     |     | B   | (t) = | C   | ×Ft | (t) | ×   | i   | × Br −Dr . |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | ---------- | --- | --- |
(12)
|     |     |     | fact |     | period | bh  |     | 1+I    | C i |     |     |
| --- | --- | --- | ---- | --- | ------ | --- | --- | ------ | --- | --- | --- |
|     |     |     |      | i=1 |        |     | (   | rate ) |     |     |     |
|     |     |     | ∑(   |     |        |     | )   |        | ( ) |     |     |
|     | C   | ×Ft | (t)  |     |        |     | (   | )      |     |     |     |
The term  period bh  captures the repayment based on the behaviour pattern to ensure consistency.
|     |     |     |  according to m |     | inC |     | ≤ C | ≤ m axC |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | ------- | --- | --- | --- |
The credit pe riod is adjusted period period period which helps assess the borrower’s
|     | (   |     | )   |     | t   |     |     | t   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
repayment. The liability is denoted as  O i which reduces the behaviour factor and indicates the high financial
O
risk in the lending process. The term  i  computes the liability over the influence of interest rate to
(1+I )
rate
( Br −)Dr
enhance the behavioural factor. The term   C i  evaluates the difference between the borrower credit and
default rate to analyze the change in environmental conditions. The behaviour factor estimation using the
|     |     |     |     |     | (   | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
federated learning process is depicted in Fig. 5.
The learning process for behaviour factor assessment is depicted in Fig. 5. This learning process inputs
Len ∀t  provided amt = R rate is increasing over the tenure. Therefore, amt paid is directly proportional to R
| pat |     | paid |     |     |     |     |     |     |     |     | rate  |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
1
for  t  such that  U 𝛼  is true. This is the linear case for  B (t)  computation without  Br −Dr  is used
|     |     | repay am | t   |     |     |     |     | fact |     | c   | i   |
| --- | --- | -------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
due
|     | (   |     | )   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
( )
|     |     |     |     |     |     |     |     | Int J Comput Intell Syst           (2025) 18:60  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |

https://doi.org/10.1007/s44196-025-00776-w Page 15 of 24 60
Fig. 6 Behaviour factor analysis
to identify multiple behavior patterns under R rate and Ft bh-in inputs. However, there is an alternate case for vali-
dating f C period under Br c +C hist ≥ 𝜓 and verifying Dr i ≤ 𝜓 . This condition verification is used for
max t C peri(od and m ) in t C perio(d under B fac)t . The combinations of Br c ,C hist are used to detect Ft bh (t) for U repay under
B
new patterns detected. In Fig. 6, fact is an analysis of diffe ( rent varia ) nts.
In micro-lending, a borrower’s behaviour over time is analyzed based on the credit period. The proposed
method indicates a high behaviour factor value, reflecting positive financial behaviour. The repayment patterns
with financial adaptability Ft bh (t)∀U repay were analyzed based on the economic conditions to avoid risk during
lending. Federated learning ensures fairness and accuracy throughout the entire process. A low behaviour factor
occurs when a borrower has missed payments and engages in irregular financial activity. A high behaviour factor
occurs when a borrower timely repays their amount and consistent economic market. This ensures the borrower’s
financial health and adaptability, contributing to positive lending decisions (Fig. 6). The federated learning pro-
cess is described in Algorithm 3.
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
   60   Page 16 of 24
Algorithm 3   Federated Learning Process
This helps to measure the borrower’s factors even during high default rates and liabilities in the lending process.
A
The risk filtering is expressed as  risk in the following equation.
|      | t C    | ×C          | C      | ×U         |        |     |       |     |      |
| ---- | ------ | ----------- | ------ | ---------- | ------ | --- | ----- | --- | ---- |
|      |        | risk stable |        | risk repay |        |     |       |     |      |
| A    | =      |             | −      |            | + R ×C | +   | Dr ×E | .   |      |
| risk | I      | −maxC       | I      | −minC      | rate   | lm  | i     | con | (13) |
|      | ( rate | period)     | ( rate | period)    |        |     |       |     |      |
|      | i=1    | t           |        | t          |        |     |       |     |      |
|      | ∑      |             |        |            | (      | )   | (     | )   |      |
C ×C
Here, the term  risk stable  identifies the maximum risk factors based on the maximum credit period with
|     | I −maxC |        |     |     |     |     |     |     |     |
| --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | rate    | period |     |     |     |     |     |     |     |
|     | ( t     | )      |     |     |     |     |     |     |     |
×U
|     |     | C risk repay |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
credit stability. The term   measures the minimum risk factors based on the minimum credit period
|     | I      | −minC      |     |     |     |     |     |     |     |
| --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
|     | ( rate | t period ) |     |     |     |     |     |     |     |
with repayment rate. The difference between maximum and minimum credit periods was analyzed to filter the
risk factor. Non-risk factors highlighted the risk occurrence factors to obtain accurate risk factors in the lending
  Int J Comput Intell Syst           (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
Page 17 of 24     60
Fig. 7   Filtering ratio analysis
process. New credit risks are identified using this filtered factor from the previous return period. This filtering
process helps to make decisions in the micro-lending environment. The following equation risk (t)  detects the
detect
risk.
1
|     | risk | (t) | = Br | +C  | +C × | ×   | B −C | +E . |
| --- | ---- | --- | ---- | --- | ---- | --- | ---- | ---- |
(14)
|     |     | detect |     | C hist | lm A |       | fact period | con |
| --- | --- | ------ | --- | ------ | ---- | ----- | ----------- | --- |
|     |     |        |     |        | (    | risk) |             |     |
|     |     |        | (   |        | )    |       | (           | )   |
The borrower credits with history and credit limit were analyzed to predict the external economic risk that was
not evaluated during the lending process. The term risk (t) ∝ 1
|     |     |     |     |     | detect |     |  indicates that an increase in accurate  |     |
| --- | --- | --- | --- | --- | ------ | --- | ---------------------------------------- | --- |
A risk
−C
filtering decreases the risk. The term  B  normalizes the (behav)iour pattern by differentiating the credit
|     |     |     |     | fact           | period  |     |     |     |
| --- | --- | --- | --- | -------------- | ------- | --- | --- | --- |
|     |     |     |     | bility. When r | isk (t) | > A |     |     |
period to monitor the financial insta detect risk indicates high risk based on the risk filter
|     |     |     | (   |     | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
process. This helps to address the borrower’s ability to manage the risk and evaluate the lender to modify the
borrowing amount during the micro-lending process. These identifications define new behavioural patterns for
the selected credit limit. The filtering ratio is analyzed as presented in Fig. 7.
The proportion of risk factors to non-risk factors with borrowers was monitored to filter the risk. A high
t
|     |     |       | ×           |     | C × U       |     |     |     |
| --- | --- | ----- | ----------- | --- | ----------- | --- | --- | --- |
| A   | =   | C ris | k C s table | −   | ris k repay |     |     |     |
filtering ratio  risk  indicates a larger proportion of risks being detected
|     |      | I rate − | m a x C period | I   | rate − m in C period |     |     |     |
| --- | ---- | -------- | -------------- | --- | -------------------- | --- | --- | --- |
|     | i=1� |          | t              | � � | t �                  |     |     |     |
∑
Int J Comput Intell Syst           (2025) 18:60

60 Page 18 of 24 https://doi.org/10.1007/s44196-025-00776-w
and filtered effectively by the proposed method. It ensures the effectiveness of the CFM in separating risk-
prone borrowers from low-risk. For example, a borrower with a high filtering ratio and poor repayment
behaviour will have high leverage in lending. Meanwhile, a borrower with consistent repayments and a low
filtering ratio will have low leverage in lending. This proposed method continuously refines its analysis
through federated learning to prioritize actionable risks from the obtained risk factors. A high filtering ratio
enhances precision in isolating risky behaviours and ensures a robust assessment (Fig. 7). The risk detection
process is explained in Algorithm 4.
Algorithm 4 Risk Detection Process
The potential for bias in credit scoring algorithms may be reduced using several methods. Methods for
pre-processing data, such as re-sampling (for instance, reweighting underrepresented groups) and SMOTE
(for example, synthetic data production), may help achieve class distribution parity. Model training may be
adjusted to eliminate inequalities using in-processing approaches such as adversarial debiasing or fairness-
aware loss functions. Adjustments to thresholds and re-ranking procedures are examples of post-processing
solutions that guarantee fairness in final decision-making without changing the underlying model. Decentral-
ized fairness-aware optimization approaches and individualized model changes are necessary to minimize
systemic biases, particularly in federated learning contexts.
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w Page 19 of 24 60
Fig. 8 New risk detection
5 Results and Discussion
The results for two new risk and return rate metrics are discussed in this part. The results are analyzed using the
WEKA tool by analyzing the raw input data formatted for credit risk analysis. In this results part, the existing
SMOTE-ENN (referenced in [21]), Light GBM-GAN (referenced in [20]), and FEEM-VO (Referenced in [22])
methods are considered for comparative analysis. The X-variants are: tenure (2 to 20 yrs.), interest rate (5 to
23), amt(K) (5 to 35), and C lm (A to D) considered. The comparative analysis results are graphically presented in
Figs. 8 and 9 for the above metrics.
To enhance the reliability of the findings, this research incorporates 95% confidence intervals (for
instance, ± 2.1% for accuracy) and statistical significance tests such as a paired t-test (p < 0.05) and Wilcoxon
signed-rank test. For reliability, information on hyperparameter adjustment is additionally required. Applying
Bayesian Optimization across a fivefold cross-validation setup, the following parameters were optimized for
the XGBoost model used for credit risk assessment: number of boosting rounds = 500, learning_rate = 0.05,
max_depth = 6, subsample = 0.8, fraction of features used per tree = 0.7, and L2 regularization lambda = 1.2.
One possible source of bias in the dataset is the difference between Group A (the majority) and Group B (the
minority). Group A has an average credit score of 720, an acceptance rate of 85% for loans, and a default rate
of 5%. In contrast, Group B has a lower approval rate of 65%, an average score of 680, and a slightly higher
default rate of 7%. One way to address these biases is by using fairness-aware techniques. These techniques
Int J Comput Intell Syst (2025) 18:60

60 Page 20 of 24 https://doi.org/10.1007/s44196-025-00776-w
Fig. 9 Return rate analysis
include reweighting training data to ensure underrepresented groups are balanced, using equalized odds con-
straints to ensure risk-equivalent applicants have consistent approval rates, and using explainability methods
like SHAP or LIME to find biased feature contributions and adjust them. Table 2 shows the experimental setup.
The occurrence of newly identified risks with time-based on borrower specification is analyzed using the
proposed method. The proposed method ensures fewer values, which indicates a minimal emergence of new
risks. Federated learning continuously updates the models based on previously unseen risks identified based
on credit history. The accurate filtering and pattern analysis reduce the emergence of new risks and ensure
the stability of the credit assessment in micro-lending. If a borrower with variation in financial behaviour
stabilizes their repayment patterns, there will be a high possibility of new risk. A borrower with predictable
and stable financial behaviour will have a low occurrence of new risk (Fig. 8).
The return rate in micro-lending represents the proportion of borrowers repaying loans on time. The proposed
CFM with LP analysis improves the return rate compared to existing methods. The existing methods often fail
to adapt borrower behaviours based on economic conditions. It leads to lower and unstable return rates dur-
ing economic downturns. The proposed method continuously updates borrower credit patterns using federated
learning to monitor repayment behaviours during unstable economic conditions and R rate > C lm ∀ amt−E con
indicates the possibility of risk. This helps to identify where the return rate declines during market fluctuations
( )
and environmental factors. It maintains stability to enhance risk filtering and improves repayment outcomes in a
micro-lending environment (Fig. 9). Table 3 shows the comparative analysis.
As data distributions vary over time, a phenomenon known as model drift occurs, and the prediction perfor-
mance continues to decline. The problem is much more severe in federated networks when clients’ data is distrib-
uted differently, making global model updates less effective. Adaptive federated optimization methods like FedAvg
with momentum, FedProx (which regularizes local model updates), and drift-aware aggregation procedures are
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w
Page 21 of 24     60
Table 2   Experimental
|     | Component |     |     |     | Details |
| --- | --------- | --- | --- | --- | ------- |
setup
|     | GPU |     |     |     | NVIDIA A100 (80 GB  |
| --- | --- | --- | --- | --- | ------------------- |
VRAM)
|     | CPU                  |     |     |     | 64-core AMD EPYC 7742 |
| --- | -------------------- | --- | --- | --- | --------------------- |
|     | RAM                  |     |     |     | 128 GB                |
|     | Storage              |     |     |     | 2T B                  |
|     | Network              |     |     |     | 10 Gbps Ethernet      |
|     | Operating system     |     |     |     | Windows 11            |
|     | Programming language |     |     |     | Python 3.9            |
|     | Bias mitigation      |     |     |     | AIF360, Fairlearn     |
|     | Learning rate        |     |     |     | 0.01                  |
|     | Max depth            |     |     |     | 10                    |
|     | Number of estimators |     |     |     | 500                   |
Table 3   Comparative analysis
Model New risk detec- Return rate  Tenure (yrs)  Interest rate  Amount (K) Limit categories (A, B, C, D)
|     | tion (%) | analysis (%) | (X-axis) | (%) |     |
| --- | -------- | ------------ | -------- | --- | --- |
SMOTE-ENN [21] 80.12 0.81 10 12 15 A: 78, B: 80, C: 82, D: 84
LightGBM-GAN [20] 86.45 0.88 15 15 20 A: 82, B: 85, C: 88, D: 90
| FEEM-VO [22] | 90.32 | 0.92 | 20  | 18 25 | A: 86, B: 89, C: 91, D: 93 |
| ------------ | ----- | ---- | --- | ----- | -------------------------- |
CFM-LPA (proposed) 95.21 0.97 25 21 30 A: 90, B: 93, C: 95, D: 96
necessary to combat drift. Concept drift detection approaches, such as adaptive windowing (ADWIN) or Kol-
mogorov–Smirnov tests, may be used to monitor model performance continuously. This allows for timely model
upgrades to be triggered to retain accuracy. One adversarial attack is model poisoning, in which malicious clients
insert biased gradients into a federated learning system. Another type is inference attacks, in which attackers try to
retrieve private data from shared model updates. Defending against poisoning attacks may be done via defensive
measures like Byzantine-resilient aggregation (like Krum or median-based filtering). To avoid inference attacks
without compromising model usefulness, utilize differential privacy strategies like secure multi-party comput-
ing (MPC) or local perturbation (e.g., Gaussian noise addition). Further improvements to federated learning
framework security and trust may be achieved via robust encryption methods and consensus mechanisms based
on blockchain technology.
6   Conclusion
The proposed CFM with LP analysis is transformative in credit risk assessment for micro-lending. The method
integrates federated learning and behavioural analysis to understand borrowers’ repayment trends and credit
stability. The continuous evaluation of return rates with credit limits and consumer responses predicts the risk
assessment with the financial behaviours of the borrowers. This approach improves the accuracy of credit risk
models that protect data. The filtering and utilization of behavioural factors from previous return periods allow
micro-lending organizations to adjust their approach according to the dynamics of the borrowers. It helps to
avoid risks and enhance sustained growth in the micro-lending platform. The proposed method reduces default
rates and ensures stronger financial systems with high-risk detection in the micro-lending. The proposed method
improves the risk detection analysis by 14.82% and return rate analysis by 13.63% for the different interest rates.
H However, the model’s reliance on collaborative filtering may introduce biases if the available lending data is
Int J Comput Intell Syst           (2025) 18:60

60 Page 22 of 24 https://doi.org/10.1007/s44196-025-00776-w
sparse or imbalanced, potentially leading to inaccurate risk predictions for new or underrepresented borrowers.
Federated learning ensures data privacy; it requires significant computational resources and robust synchroniza-
tion across multiple lending institutions, which may pose scalability challenges. Future studies will improve the
model’s scalability through efficient communication protocols in federated learning, help reduce computational
overhead and incorporate real-time financial indicators and alternative credit data sources, such as social and
transactional behaviour, to improve adaptability to dynamic lending environments.
Acknowledgements This research was supported by the Princess Nourah bint Abdulrahman University Researchers Sup-
porting Project number (PNURSP2025R259), Princess Nourah bint Abdulrahman University, Riyadh, Saudi Arabia.
Author Contributions Asma Aldrees: methodology, validation, formal analysis, resources, writing—review and editing,
visualization, funding acquisition Sana Shahab: conceptualization, methodology, software, data curation, writing—original
draft, writing—review and editing, visualization, funding acquisition. Ashit Kumar Dutta: methodology, resources, writ-
ing—review and editing, visualization, funding acquisition Waseem Ahmad: conceptualization, methodology, resources,
writing—original draft, writing—review and editing Mohd Anjum: conceptualization, methodology, software, writing—
original draft, writing—review and editing.
Funding This work was supported by the Researchers Supporting Project Number (UM-DSR-IG-2023–07) Almaarefa
University, Riyadh, Saudi Arabia.
Data Availability Data is open accessible through the link: https://w ww.k aggle.c om/d atase ts/l aotse/c redit-r isk-d atase t.
Declarations
Conflict of Interest The authors declare no competing interests.
Informed Consent Not applicable.
Institutional Review Board Statement Not applicable.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Interna-
tional License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party material in this article are included in the article’s
Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://c reat
ivecom mons.o rg/l icens es/b y-n c-n d/4.0 /.
References
1. Aiello, M.A., Angelico, C.: Climate change and credit risk: the effect of carbon tax on Italian banks’ business loan default
rates. J. Policy Model. 45(1), 187–201 (2023)
2. Dömötör, B., Illés, F., Ölvedi, T.: Peer-to-peer lending: legal loan sharking or altruistic investment? analyzing platform
investments from a credit risk perspective. J. Int. Financ. Markets. Inst. Money 86, 101801 (2023)
3. Kaya, O.: The impact of late payments on SMEs’ access to finance: evidence from credit rationing and loan terms. Econ.
Model. 141, 106896 (2024)
4. Chan, S.H.: An exploratory study of using micro-credit to encourage the setting up of small businesses in the rural sector
of Malaysia. Asian Bus. Manag.Manag. 4, 455–479 (2005)
5. Enimu, S., Eyo, E.O., Ajah, E.A.: Determinants of loan repayment among agricultural microcredit finance group mem-
bers in Delta state, Nigeria. Financ. Innov. 3, 1–12 (2017)
6. Dorfleitner, G., Oswald, E.M., Zhang, R.: From credit risk to social impact: on the funding determinants in interest-free
peer-to-peer lending. J. Bus. Ethics 170, 375–400 (2021)
Int J Comput Intell Syst (2025) 18:60

https://doi.org/10.1007/s44196-025-00776-w Page 23 of 24 60
7. Daniels, K., Ramirez, G.G.: Information, credit risk, lender specialization and loan pricing: evidence from the DIP
financing market. J. Financ. Serv. Res. 34, 35–59 (2008)
8. Meressa, H.A.: Micro-and small-scale enterprises’ financing preference in line with POH and access to credit:
empirical evidence from entrepreneurs in Ethiopia. J. Innov. Entrepreneurship 11(1), 54 (2022)
9. Shrieves, R.E., Dahl, D.: Regulation, recession, and bank lending behavior: the 1990 credit crunch. J. Financ. Serv.
Res. 9(1), 5–30 (1995)
10. Blanco-Oliver, A., Samaniego, A., Palacin-Sanchez, M.J.: How do loan officer-borrower gender-driven behavioural
differences impact on the microfinance lending market? Borsa Istanb. Rev. 24(3), 435–448 (2024)
11. Hu, B., Hu, Y.P.: Pricing models for small and micro loan portfolio insurance. Int. Rev. Financ. Anal.Financ. Anal.
96, 103552 (2024)
12. Chu, L., Mathieu, R., Robb, S., Zhang, P.: Bank capitalization and lending behavior after the introduction of the
basle accord. Rev. Quant. Financ. Acc.Financ. Acc. 28, 147–162 (2007)
13. Andersson, P.: P1198: Software for tracing decision behavior in lending to small businesses. Behav. Res. Methods
Instrum. Comput.. Res. Methods Instrum. Comput. 33, 234–242 (2001)
14. Barboza, G., Trejos, S.: Micro credit in Chiapas, México: poverty reduction through group lending. J. Bus. Ethics
88, 283–299 (2009)
15. Yang, F., Ye, X., Huang, W., Zhao, X.: The impacts on informal financing strategy of small and micro enterprises
by interest rate risks and public health emergencies. Int. Entrepreneurship Manag. J. 19(4), 1673–1705 (2023)
16. Wu, S., Dong, M., Tan, S., Dong, Y.: Who is lending to small and micro family business in China: evidence from
CHFS data. Small Bus. Econ. 63(3), 1225–1247 (2024)
17. Zhao, Y.: Investigation of the application of machine learning algorithms in credit risk assessment of medium and
micro enterprises. IEEE Access (2024). https://d oi.o rg/1 0.1 109/A CCESS.2 024.3 47755 6
18. Liu, Y., Baals, L.J., Osterrieder, J., Hadji-Misheva, B.: Leveraging network topology for credit risk assessment in
P2P lending: a comparative study under the lens of machine learning. Expert Syst. Appl. 252, 124100 (2024)
19. Qian, Y., Wang, F., Zhang, M., Zhong, N.: Political uncertainty, bank loans, and corporate behavior: new investiga-
tion with machine learning. Pac. Basin Financ. J.Financ. J. 87, 102480 (2024)
20. Zhuang, Y., Wei, H.: Design of a personal credit risk prediction model and legal prevention of financial risks. IEEE
Access (2024). https://d oi.o rg/1 0.1 109/A CCESS.2 024.3 46619 2
21. Aruleba, I., Sun, Y.: Effective credit risk prediction using ensemble classifiers with model explanation. IEEE Access
(2024). https://d oi.o rg/1 0.1 109/A CCESS.2 024.3 44530 8
22. Yang, D., Xiao, B.: Feature enhanced ensemble modeling with voting optimization for credit risk assessment. IEEE
Access (2024). https://d oi.o rg/1 0.1 109/A CCESS.2 024.3 44549 9
23. Gamba-Santamaria, S., Melo-Velandia, L.F., Orozco-Vanegas, C.: Decomposition of non-performing loans dynamics
into a debt-servicing capacity and a risk taking indicators. Q. Rev. Econ. Finance 96, 101860 (2024)
24. Haitao, S.: Big data analysis of e-commerce loan risk of college students in the context of network finance. IseB
18(3), 439–454 (2020)
25. Wang, F., Ding, L., Yu, H., Zhao, Y.: Big data analytics on enterprise credit risk evaluation of e-Business platform.
IseB 18(3), 311–350 (2020)
26. Rao, C., Liu, Y., Goh, M.: Credit risk assessment mechanism of personal auto loan based on PSO-XGBoost model.
Complex Intell. Syst. 9(2), 1391–1414 (2023)
27. Shetabi, M.: Evolutionary-based ensemble feature selection technique for dynamic application-specific credit risk
optimization in FinTech lending. Ann. Oper. Res.Oper. Res. (2024). https://d oi.o rg/1 0.1 007/s 10479-0 24-0 6369-8
28. Xia, H., Liu, J., Zhang, Z.J.: Identifying Fintech risk through machine learning: analyzing the Q&A text of an online
loan investment platform. Ann. Oper. Res.Oper. Res. (2024). https://d oi.o rg/1 0.1 007/s 10479-0 20-0 3842-y
29. Sinkey, J.F., Jr., Greenawalt, M.B.: Loan-loss experience and risk-taking behavior at large commercial banks. J.
Financ. Serv. Res. 5(1), 43–59 (1991)
30. Li, Z., Liang, S., Pan, X., Pang, M.: Credit risk prediction based on loan profit: evidence from Chinese SMEs. Res.
Int. Bus. Financ.Financ. 67, 102155 (2024)
31. Wang, Y., Zhang, Y., Liang, M., Yuan, R., Feng, J., Wu, J.: National student loans default risk prediction: a hetero-
geneous ensemble learning approach and the SHAP method. Comput. Educ. Artif. Intell. 5, 100166 (2023)
32. Zhang, R., Lin, C., Tong, Z.: A visual risk identification and early warning research for college net loan based on
microblog texts. Risk Manage. 23, 261–281 (2021)
33. Liu, S., Xu, J.: Enterprise risk management, risk-taking, and macroeconomic implications: evidence from bank
mortgage loan management. J. Financ. Serv. Res. (2024). https://d oi.o rg/1 0.1 007/s 10693-0 24-0 0422-0
34. Carannante, M., D’amato, V., Fersini, P., Forte, S.: Machine learning-based climate risk sharing for an insured loan
in the tourism industry. Qual. Quant. (2024). https://d oi.o rg/1 0.1 007/s 11135-0 24-0 1958-y
35. Liu, P., Shao, Y.: Small business loan securitization and interstate risk sharing. Small Bus. Econ. 41, 449–460 (2013)
3 6. https://w ww.k aggle.c om/d atase ts/l aotse/c redit-r isk-d atase t
Int J Comput Intell Syst (2025) 18:60

60 Page 24 of 24 https://doi.org/10.1007/s44196-025-00776-w
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
affiliations.
Authors and Affiliations
Asma Aldrees1 · Sana Shahab2 · Ashit Kumar Dutta3 · Waseem Ahmad4 · Mohd Anjum5
*
Waseem Ahmad
waseemahmad2@zhcet.ac.in
Asma Aldrees
edrees@kku.edu.sa
Sana Shahab
sshahab@pnu.edu.sa
Ashit Kumar Dutta
adotta@um.edu.sa
Mohd Anjum
mohdanjum@zhcet.ac.in
1 Department of Informatics and Computer Systems, College of Computer Science, King Khalid University,
Abha 61421, Saudi Arabia
2 Department of Business Administration, College of Business Administration, Princess Nourah Bint Abdulrahman
University, PO Box 84428, Riyadh 11671, Saudi Arabia
3 Department of Computer Science and Information Systems, College of Applied Sciences, AlMaarefa University,
Ad Diriyah, Riyadh 13713, Kingdom of Saudi Arabia
4 Department of Computer Science and Engineering, Vishveshwarya Group of Institutions (VGI), Greater Noida,
Gautam Buddha Nagar, Uttar Pradesh 201314, India
5 Department of Computer Engineering, Aligarh Muslim University, Aligarh 202002, India
Int J Comput Intell Syst (2025) 18:60