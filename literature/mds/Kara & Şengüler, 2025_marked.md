---
conversion_metadata:
  converted_at: "2026-10-12T07:29:25Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Kara & Şengüler, 2025.pdf"
  source_pdf_sha256: "ee3a1f3befa3833b065b162fb84f3c6b4b6c9beaa00438226ad2e67f9c5cf80f"
  page_count: 18
  markdown_char_count: 111264
---

| Public Budgeting |         | & Finance    |     |            |     |             |          |     |     |
| ---------------- | ------- | ------------ | --- | ---------- | --- | ----------- | -------- | --- | --- |
| ORIGINAL         | ARTICLE |              |     |            |     |             |          |     |     |
| A Comparative    |         | Analysis     |     | of Budget  |     | Forecasting |          |     |     |
| Methods:         |         | A Systematic |     | Literature |     | Review      | Covering |     |     |
–
| the | 1983 2024 | Period |     |     |     |     |     |     |     |
| --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Şengüler
| BeratKara | | Hasan |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
FacultyofPoliticalScience,IstanbulMedeniyetUniversity,Istanbul,Turkey
Correspondence:BeratKara(berat.kara@medeniyet.edu.tr)
| Received:11September2025 |     | | Revised:18October2025 |     | | Accepted:27October2025 |     |     |     |     |     |
| ------------------------ | --- | ----------------------- | --- | ------------------------ | --- | --- | --- | --- | --- |
Keywords:budgetforecasting|machinelearning|methodcomparison|performancemetrics|systematicreview
ABSTRACT
Thisstudysystematicallyanalyzes69peer‐reviewedworkscomparingbudgetforecastingmethods.Itexploresmethodological
evolution, geographic distribution, and evaluation trends. Four phases of development are identified: statistical methods,
diversification,machinelearning,anddeeplearning.Adivisionemergesbetweentraditionalandnext‐generationtechniques.
Geographically,43%ofstudiesfocusontheUnitedStates,whiledevelopingeconomiesremainunderrepresented.Inevaluation,
MAPE, RMSE, and MAE dominate, with directional errors largely neglected. Findings show that optimal method choice
dependsoncontext,supportingapluralistic,context‐sensitiveapproachratherthanuniversalrelianceonasingleforecasting
method.
(Botrić
1 | Introduction implementation of fiscal policy measures and Vizek
|     |     |     |     |     | 2012) | and the design | and execution | of sound fiscal | policies |
| --- | --- | --- | --- | --- | ----- | -------------- | ------------- | --------------- | -------- |
Public budgets, which lie at the core of fiscal management (Derrick 2002; Danninger 2005) depend critically on the
systems, function both as instruments of economic policy and accuracy of forecasts. Moreover, forecasts serve as key in-
as frameworks for managing public resources. The forecasts dicators for economic agents: various financial indicators,
used in budget preparation determine the government's future particularly interest rates, are influenced by these forecasts;
fiscal capacity, spending priorities, and economic orientation. householdsandfinancialmarketparticipantsbasetheirlong‐
The forecasting process is shaped by a wide range of factors, term decisions on them; and central banks that pursue
including macroeconomic indicators, political preferences, inflation targeting rely on such data to guide their policy
| institutional | capacity,        | and technical   | methodologies. | In this   | decisions. |     |     |     |     |
| ------------- | ---------------- | --------------- | -------------- | --------- | ---------- | --- | --- | --- | --- |
| respect,      | budget forecasts | go beyond being | a merely       | technical |            |     |     |     |     |
elementoffiscalplanning,constitutingastrategiccomponentof Accurateforecastsserveasafundamentaltoolfordetermining
thepolicy‐making process. the extent to which public services and programs can be
financed(Auld1970;Bretschneideretal.1989).Thesuccessof
This strategic position necessitates that budget forecasts be forecasting is particularly critical for the efficient financing of
preparedinarealistic,reliable,andaccuratemanner.Efficient large future public expenditures (Auld 1970), as multiyear ex-
allocation of scarce public resources and the successful coor- penditure forecasts represent an estimate of the cost of pro-
public–private
dination of sector planning are only possible viding a certain level of public service (Schroeder 2007).
through a budget process grounded in robust forecasts Furthermore, establishing a robust link between long‐term
(Krause and Corder 2007). Similarly, the timely and effective planning and implementation depends on the accuracy of
©2025PublicFinancialPublications,Inc.
| PublicBudgeting&Finance,2025;1–18 |     |     |     |     |     |     |     |     | 1   |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1111/pbaf.70008

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
approachesemergeinthisregard.Thefirstinvolvesidentifying
Summary
|     |     |     |     |     |     |       | the causes | of past | forecasting |     | errors and | developing |     | remedial |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ------- | ----------- | --- | ---------- | ---------- | --- | -------- |
| •   |     |     |     |     |     | peer‐ |            |         |             |     |            |            |     |          |
This study provides a systematic analysis of 69 mechanisms. This approach aims to eliminate recurring error
| reviewed         | studies | comparing     | budget | forecasting       |     | meth- |           |              |           |           |                 |     |                 |     |
| ---------------- | ------- | ------------- | ------ | ----------------- | --- | ----- | --------- | ------------ | --------- | --------- | --------------- | --- | --------------- | --- |
|                  |         |               |        |                   |     |       | patterns  | by examining |           | in detail | the structural, |     | institutional,  |     |
| ods, identifying |         | four distinct | phases | of methodological |     |       |           |              |           |           |                 |     |                 |     |
|                  |         |               |        |                   |     |       | economic, | and          | political | factors   | influencing     |     | the forecasting |     |
evolution from basic statistical models to the deep process. The second approach focuses on improving the meth-
learning era. ods and models used in the preparation of forecasts. Such
• Thefindingsrevealthatnosingleforecastingmethodis methodologicaladvancementencompassesboththerefinement
universally superior; instead, the optimal choice criti- ofexistingtechniquesandtheimplementationofnewmodeling
|       |         |               |         |      |        |      | approaches, | with | the | goal | of strengthening |     | the analytical |     |
| ----- | ------- | ------------- | ------- | ---- | ------ | ---- | ----------- | ---- | --- | ---- | ---------------- | --- | -------------- | --- |
| cally | depends | on contextual | factors | such | as the | eco- |             |      |     |      |                  |     |                |     |
nomic environment, data quality, and the forecast capacityofthe forecastingprocess.
horizon.
Theliteraturecontainsnumerousstudiesthatfocusonthesetwo
| • A significant |     | finding is | the pronounced |     | geographical |     |             |       |         |      |          |     |             |     |
| --------------- | --- | ---------- | -------------- | --- | ------------ | --- | ----------- | ----- | ------- | ---- | -------- | --- | ----------- | --- |
|                 |     |            |                |     |              |     | approaches. | These | studies | have | compared | the | performance | of  |
concentrationofresearch,with43%ofstudiesfocusedon
|            |         |         |             |               |     |     | various forecasting |     | techniques |          | across different |         | country | contexts |
| ---------- | ------- | ------- | ----------- | ------------- | --- | --- | ------------------- | --- | ---------- | -------- | ---------------- | ------- | ------- | -------- |
| the United | States, | leaving | forecasting | methodologies |     | in  |                     |     |            |          |                  |         |         |          |
|            |         |         |             |               |     |     | and datasets.       | The | models     | employed | range            | widely, | from    | simple   |
developingeconomiessubstantiallyunderrepresented.
|             |     |                       |     |      |          |     | time‐series    | methods | based    | on            | trend analysis | to         | complex | econo-     |
| ----------- | --- | --------------------- | --- | ---- | -------- | --- | -------------- | ------- | -------- | ------------- | -------------- | ---------- | ------- | ---------- |
| • The field | is  | further characterized |     | by a | hegemony | of  |                |         |          |               |                |            |         |            |
|             |     |                       |     |      |          |     | metric models, |         | and from | deterministic |                | approaches | to      | artificial |
certainperformancemetrics(MAPE,RMSE,andMAE), intelligence (AI) and machine learning (ML)‐based algorithms.
which, while allowing for comparison, largely neglect While simpler methods offer advantages such as ease of imple-
| the critical |     | policy dimension | of  | directional | forecast |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mentationandlowdatarequirements,morecomplextechniques,
errors. despite requiring greater computational power and extensive
• data sources, possess the potential to capture dynamic relation-
Consequently,thestudyadvocatesforashiftawayfrom
“ideal”
the quest for a single best model toward a more plu- ships. This diversity indicates that there is no single
ralistic, context‐sensitive, and potentially hybrid method for budget forecasting; rather, the choice of method
|            |                    |     |     |     |     |     | depends | on factors | such | as economic | conditions, |     | data | quality, |
| ---------- | ------------------ | --- | --- | --- | --- | --- | ------- | ---------- | ---- | ----------- | ----------- | --- | ---- | -------- |
| approachto | budgetforecasting. |     |     |     |     |     |         |            |      |             |             |     |      |          |
institutionalcapacity,andpolicypriorities.
|             |           |           |        |       |      |       | The existing |               | literature | does         | not provide |          | a homogeneous |           |
| ----------- | --------- | --------- | ------ | ----- | ---- | ----- | ------------ | ------------- | ---------- | ------------ | ----------- | -------- | ------------- | --------- |
|             |           |           |        |       |      |       | assessment   | of the        | success    | of methods   | used        | in       | budget        | forecast- |
| medium‐ and | long‐term | forecasts | (Asher | 1978; | Jena | 2006; |              |               |            |              |             |          |               |           |
|             |           |           |        |       |      |       | ing, due     | to variations |            | in datasets, | time        | periods, | countries,    | and       |
Zakaria and Ali 2010; Fedotov 2017). Having sufficient infor- modeltypes.Forecastsproducedacrossabroadspectrum,from
mation about available resources enables more effective man- simple time‐series techniques to complex ML approaches, ex-
agementoflong‐termprogramsandprojectswithinthebudget
|     |     |     |     |     |     |     | hibit varying | performance |     | in  | different | contexts. | This | situation |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --- | --------- | --------- | ---- | --------- |
process, while careful evaluation of this information guides necessitatesasystematicevaluationofwhichmethodsperform
project and program selection, helping to determine what is betterunderspecificconditions.Suchanassessmentwouldnot
feasible in the medium term (Jena 2006). In this context, fore- onlycontributetotheadvancementofacademicknowledgebut
casts related to a country's key sectors provide a scientific also serve as a practical guide for institutions, policymakers,
foundationfor strategicplanning (Fedotov 2017). and analysts involved in the budget process regarding method
selectionandmodeldevelopment.Inresponsetothisneed,the
The realistic preparation of budget forecasts is also a critical present study offers a comprehensive review of the existing
prerequisite for the government to achieve its planned objec- literature, providing a comparative evaluation of different
tives(KhanandAnwarHussain2018;BretschneiderandGorr models andtechniques.
| 1992; Agostini | 1991). | As observed | in  | modern | economies, | a   |     |     |     |     |     |     |     |     |
| -------------- | ------ | ----------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
government's ability to respond effectively to any crisis is The critical need for advancing budget forecasting accuracy is
directlyinfluenced bythequality ofthefinancialinformation further underscored by recent large‐scale efforts to define the
available to it, and consequently, by the accuracy of forecasts research priorities for the entire field of public budgeting and
agenda‐setting
(Willoughby and Guo 2008). In other words, the success of finance. In a comprehensive study, McDonald
forecasting shapes public perception regarding the effective- et al. (2024) engaged a wide community of academics and
ness of a government's fiscal policy (Leal et al. 2008). There- practitioners to identify the most pressing research needs.
ranked‐choice
fore, major errors in budget forecasting negatively affect the Notably, their findings, derived from a voting
|     |     |     |     |     |     |     |     |     | “Data |     | Methods” |     | top‐tier |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | --- | -------- | --- |
outcomes of governmental programs and policies, potentially process, highlighted and as a priority,
leading to policy failure (Srinivasan and Misra 2020). explicitly calling for research that improves “the accuracy of
Accordingly, it can be argued that forecast accuracy plays a forecasting.”
|     |     |     |     |     |     |     | budget | and revenue |     |     | This | consensus | positions |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | --- | ---- | --------- | --------- | --- |
significantroleinthebudgetarypolicyprocessbycontributing methodologicalinvestigations,suchasthepresentstudy,atthe
to transparency, accountability, and fiscal discipline (McNab forefront of the field's agenda. Our systematic review directly
et al. 2005). addressesthiscallbysynthesizingthecomparativeperformance
four‐decade
|     |     |     |     |     |     |     | of a wide | array | of forecasting |     | techniques | over | a   |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------------- | --- | ---------- | ---- | --- | --- |
Asanaturalconsequenceofthisstrategicimportance,effortsto period. By doing so, this study aims not only to contribute to
enhance the accuracy of budget forecasts have remained a academic knowledge but also to provide a practical, evidence‐
continuous focus in the field of public finance. Two principal based guide for practitioners in selecting and developing
| 2   |     |     |     |     |     |     |     |     |     |     | PublicBudgeting&Finance,2025 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
forecastingmodels,therebybridgingthegapbetweenacademic instance,variousvariantsofartificialneuralnetworks(ANNs),
inquiryandtheoperationalneedsidentifiedbythecommunity evenwhenlabeledwithdifferentprefixesintheoriginalstudies,
ofpractice. were grouped under the ANN category in the dataset. This
|                                                         |             |           |            |           |     | standardization | enables | accurate | and meaningful |     | comparisons |
| ------------------------------------------------------- | ----------- | --------- | ---------- | --------- | --- | --------------- | ------- | -------- | -------------- | --- | ----------- |
| Thepaperisstructuredasfollows.First,thedatasetusedinthe |             |           |            |           |     | acrossmethods.  |         |          |                |     |             |
| analysis is                                             | introduced, | detailing | its scope, | coverage, | and | key             |         |          |                |     |             |
characteristics. Second, the methodology is explained. Third, The primary motivation for constructing this dataset is to en-
the state of the literature on budget forecasting methods is ex- ableanobjectiveevaluationofthecomparativeperformanceof
amined, with a focus on comparative findings and methodo- budget forecasting methods and to conduct a systematic anal-
logicaldiversity.Finally,theconclusionsectionsummarizesthe ysisoffindingsintheliterature.Inthisway,thestudyaimsto
mainfindingsandoutlinesimplicationsforfutureresearchand provide clearer and more reliable insights into the conditions
policydesign. under which different methods yield superior results, both for
|          |     |     |     |     |     | theacademic | community | andforpractical |     | applications. |     |
| -------- | --- | --- | --- | --- | --- | ----------- | --------- | --------------- | --- | ------------- | --- |
| 2 | Data | Set |     |     |     |     |             |           |                 |     |               |     |
|          |     |     |     |     |     | 3 | Methods |           |                 |     |               |     |
Thedatasetconstructedinthisstudyencompassestheacademic
literature in which budget forecasting methods have been The purpose of this study is to examine the distribution, tem-
comparatively evaluated. In creating the dataset, a series of poral trends, and interrelationships of methods and metrics
selectioncriteriawasestablishedtoclearlydefinethescopeand employed in the budget forecasting literature. While classical
peer‐
ensure comparability. First, only articles published in bibliometric analyses are typically conducted through citation
|     |     |     |     |     |     |     | co‐authorship |     |     |     | co‐ |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
reviewed journals, books, book chapters, and scientific confer- networks, collaborations, or journal
ence proceedings were included. This choice aims to ensure occurrencemapping(Passas2024),thisstudyadoptsadifferent
thatthemethodsemployedandtheresultsobtainedhavebeen perspective. Instead of focusing on citation relationships or
scrutinized according to academic standards and are highly collaborative networks, the analysis emphasizes the frequency
reliable. Reports, technical notes, or institutional assessments of method applications, the prevalence of metric preferences,
that have not undergone a peer‐review process were excluded thecharacteristicsoftrainingdatasets,thelengthofforecasting
from thedataset. horizons, and the interconnections among methods. Thus,
|     |     |     |     |     |     | although | the research | shares | certain | features | with biblio- |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------ | ------- | -------- | ------------ |
Second,sincethefocusofthisstudyisonmethodcomparison, metrics, it is primarily designed within the framework of sta-
budget forecasting studies that employ only a single method tistical analysis and network analysis. The analytical process
were not included. The dataset consists of research in which consists of three stages: (i) descriptive statistical analysis, (ii)
multiple forecasting methods were applied within the same trend analysis, and(iii)network analysis.
| study and           | their performance |     | compared. This  | approach    | allows |                   |     |             |          |     |     |
| ------------------- | ----------------- | --- | --------------- | ----------- | ------ | ----------------- | --- | ----------- | -------- | --- | --- |
| for the direct      | observation       |     | and analysis of | performance |        | differ-           |     |             |          |     |     |
| encesacrossmethods. |                   |     |                 |             |        | 3.1 | Descriptive |     | Statistical | Analysis |     |     |
Third, it was not sufficient for the included studies to provide Descriptive statistical analysis aims to summarize the funda-
onlyforward‐lookingforecasts;theseforecastswererequiredto mental characteristics of collected data and provide an overall
be compared with actual outcomes for thecorresponding peri- frameworkfortheresearchfield(Cooksey2020).Suchanalyses
ods. Studies that did not perform such comparisons were ex- are frequently used in bibliometric studies to reveal the quan-
cluded from the dataset, as they could not objectively titativestructureoftheliterature(Castelinoetal.2024).Inthis
demonstrate the success of the forecasting methods. This study, descriptive analyses include the frequency of method
requirement is critical for ensuring a robust assessment of applications, the annual distribution of publications, the geo-
(country‐level)
methodological performance, which constitutes the primary graphical distribution of research, the extent of
motivation ofthestudy. metricpreferences,andthelengthofforecastinghorizons.The
|     |     |     |     |     |     | findings | are visualized | through | graphs, | offering | a general |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | ------- | ------- | -------- | --------- |
In some studies, forecasts cover both past periods, for which overviewofmethodological diversity intheliterature.
| actual outcomes | are | available, | and future | periods, | which | have |     |     |     |     |     |
| --------------- | --- | ---------- | ---------- | -------- | ----- | ---- | --- | --- | --- | --- | --- |
notyetoccurred.Insuchcases,onlytheperiodswithavailable
|             |               |     |                 |              |     | 3.2 | Trend | Analysis |     |     |     |     |
| ----------- | ------------- | --- | --------------- | ------------ | --- | ----------- | -------- | --- | --- | --- | --- |
| actual data | were included |     | in the dataset. | For example, |     | in a        |          |     |     |     |     |
studywitha10‐yearforecastinghorizonwhereactualoutcomes
areavailableforonlythefirstfiveyears,thedatasetrepresents Trend analysis is a method used to examine temporal changes
onlythefive‐yearsegment.Thisapproachensuresthatmethod
inagivenphenomenonandtoidentifyunderlyingpatterns.Itis
performanceis measured solelyover verifiableperiods. frequently employed to illustrate the evolution of research
|     |     |     |     |     |     | domains | and methodological |     | transformations, |     | thereby con- |
| --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | ---------------- | --- | ------------ |
Finally, terminological consistency was maintained in the tributing to the understanding of the developmental trajectory
namingofmethodswithinthestudy.Indifferentstudies,minor ofafield(Li2025).Inthisstudy,trendanalysiswasconducted
variations in model structure or configuration often led to the to investigate the intensity of method applications over time.
same method being referred to by different names; in the da- The results were visualized with line graphs, highlighting
taset, these were consolidated under a single heading. For methodsthat gained prominenceduring different periods.
PublicBudgeting&Finance,2025 3

3.3 | Network Analysis such as LSTM networks and XGBoost have been incorporated
into the forecasters' toolkit (e.g., Yang et al. 2023; M. Khalifa
Networkanalysisisapowerfulmethodforexaminingstructures et al. 2024). At the same time, hybrid models and innovative
composed of nodes (e.g., methods, authors, or metrics) and approaches such as MIDAS, which address the issue of fre-
edges that represent the connections among them. This quencymismatch(GhyselsandOzkan2012,2015),havegained
approach is widely used to investigate the structural char- prominence in performance comparisons. This evolution dem-
acteristics and methodological diversity of scientific domains onstrates that researchers have not only sought to improve
(Campbell et al. 2024), offering valuable insights into the in- traditional methods but have also pushed the boundaries of
teractions amongdifferentcomponents ofthe literature. forecasting accuracy by leveraging data abundance and ad-
vancesin computational power.
In this study, network analysis was performed using Gephi
software, resulting in three distinct network structures: The expansion in geographical coverage is also noteworthy.
method–method, method–year, and method–metric relation- Whereas early studies were almost entirely United States‐
ships. Nodes represented methods, years, and metrics, while centered, recent years have witnessed significant contributions
edges denoted their co‐occurrences. This analysis enabled the from a wide range of economies, including China, Turkey,
visualization of which methods were prominent in specific Brazil, South Africa, India, and numerous Eastern European
periods, which metrics they were evaluated with, and which countries, as illustrated in Table 1. This diffusion underscores
methodstended to beemployed jointly. thatbudgetforecastingisauniversalissueinpublicfinanceand
highlights that method performance may vary across different
economic structures, institutional arrangements, and levels of
4 | Results data quality.
The table below provides a comprehensive summary of em- Therefore,thefindingsintheliteraturearenothomogeneous;a
piricalstudiesonbudgetforecastingmethods.Itsystematically methodthatdeliversthe“best”performanceinonecountryor
classifies results based on different country contexts, data fre- period may yield only modest results in another context. This
quencies, time periods, and types of methods, thereby high- heterogeneity further underscores the need for a systematic
lightingtherelativeperformanceofvariousapproaches.Inthis assessment of which methods perform better under specific
way, the fragmented findings in the literature regarding the conditionsandreinforcestheprimarymotivationofthisstudy.
successofbudgetforecastingmethodscanbeevaluatedfroma
holistic perspective, allowing for a comparative assessment of First, the distribution and frequency of forecasting methods
which methods perform better or worse under specific condi- employed in the comparative studies under review were ana-
tions. Within this framework, the table not only serves as an lyzed over time. This analysis provides an objective lens
inventory of previous research but also makes methodological through which to observe the evolution of methodological
diversityandperformancedifferences,centraltothemotivation trends, technological capabilities, and academic interest in the
of this paper, explicit, laying the groundwork for subsequent budget forecasting literature. Such a historical perspective is
analyses. crucial for understanding whichmethods dominatedin partic-
ularperiods,howthepopularityofspecificmodelshasshifted,
Academic interest in the comparative performance of budget and when pioneering contributions introduced innovations to
forecasting methods has shown a steady and remarkable thefield.
increase over the past four decades. The reviewed literature
reveals not only a numerical growth in studies but also a sig- The analysis of Figure 1 demonstrates that the methodological
nificant evolution in terms of scope, methodology, and geo- trajectoryofthebudgetforecastingliteraturecanbecharacterized
graphicaldiversity.Earlycontributions(e.g.,DownsandRocke as a four‐stage evolution. The first stage, emerging in the 1980s,
1983; Litterman and Thomas 1983) were largely confined to was dominated by basic statistical methods. During this period,
advancedeconomies(particularlytheUnitedStates)andrelied traditional time series and econometric models such as ARIMA,
primarily on relatively simple time‐series models (ARMA and VAR, and various regression techniques constituted the main
ARIMA).Overtime,however,researchhasexpandedtoinclude focus of academic studies. In subsequent years, greater diversifi-
developing countries as well as far more complex econometric cationandsophisticationinmodelingtechniquesbecameevident,
and AI‐based models. Thisexpansion is a clear indication that with more complex and theoretically grounded approaches such
thepursuitofgreaterforecastingaccuracyhastakenonaglobal asBVAR,ECM,andMIDASbeingintroduced.Thisphasemarked
and interdisciplinary character. Table 1 provides a systematic aperiodinwhichresearcherssoughttoenhanceforecastingpower
summary of this rich anddynamic body ofwork, detailing the by making model structures more dynamic and by integrating
scope,methods,andkeyfindingsofthe68comparativestudies differenttypesofdata.Bythe2010s,anotablemethodologicalshift
that form thebasisof thepresent analysis. had occurred: ML algorithms such as ANN and SVM began to
feature regularly in the literature, bringing an interdisciplinary
From a methodological perspective, the literature exhibits a dimensiontothefield.Thistransitionwasdrivenbythegrowing
clear trend toward increasing complexity and diversity. While availabilityoflargedatasets,advancesincomputationalcapacity,
the 1980s and early 1990s were dominated by classical econo- and increasing interest in modeling nonlinear relationships.
metricapproaches suchas ARIMA,VAR,andECM, the2000s Finally, since the 2020s, the literature has entered the era of DL
markedtheentryofMLanddeeplearning(DL)algorithmsinto and hybrid models. Cutting‐edge algorithms such as LSTM and
thefield.ANN,SVM,and,morerecently,cutting‐edgemethods XGBoosthavebecomefrequentlytestedincomparativeanalyses.
4 PublicBudgeting&Finance,2025
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

.gnitsaceroftegdubnisledomfoecnamrofrepevitarapmocehtnoweivererutaretiL
|
1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
enoN
WR
AMRA
WR;AM;AMRA
9791−6491
launnA
8791–6491
16
ASU
)3891(
ekcoRdnasnwoD
EP;EAM
CFO
FOC
CFO;FOC
;RAV
2891–1791
ylretrauQ
2891−7691
46
ASU
dna
namrettiL
)3891(samohT
ESMR
RGR
AMRA
RGR;AMRA
3891–1891
ylretrauQ
0891–0791
44
ASU
)5891(enaJdnaimzaN
EP
RAV
AMIRA
RAV;AMIRA
4891–3891
ylhtnoM
4891–0791
651
ASU
)5891(gnoWdnasennietS
ESM
tfirD
FOC
FOC
;tfirD
;AMIRA
3891–0891
launnA
0891–4791
264
ASU
)7891(notxeS
EM
;EAM;ESMR
RGR
AMIRA
AMIRA
;RGR
2891–1891
ylretrauQ
0891–0791
44
ASU
)8891(
dlohtueLdnaimzaN
EP
;ESMR
AMIRA
FOC
CFO;FOC
;AMIRA
5891–2891
ylretrauQ
1891–8791
61
ASU
)9891(notrelluF
EPAM
tiFevruC
AM
tiFevruC
;AMIRA
;WH;SE
;AM
6891
ylhtnoM
5891–2891
84
ASU
)0991(knarF
;EPAM;ESMR
CFO
WH
CFO;FOC
;FAG
;WH
;SE;AM
8891
ylhtnoM
7891–3891
06
ASU
)0991(somisareGdnaknarF
EP;EPA
ESMR
;EAM;EM
RAV
AMIRA
CFO;MCE
;RAV
;AMIRA
7891–0891
ylretrauQ
9791–5591
001
ASU
dna inatsehgaB )2991(nwoNcM
EPM
;EPAM
FKSM
FKSM‐C
FKSM‐C;FKSM
6891–9791
launnA
6891–2791
006
ASU
)3991(.latenacnuD
EPAM
WH
AMIRA
;SE;WH
;AM
;RGR
0991
ylhtnoM
0991–3891
27
ASU
dnasikanaiG
;FAG
;AMIRA
)3991(
drawoH
EPAM
RGR
SE
;SE
;RGR
2991–0991
launnA
2991–5791
81
ASU
)4991(gnaWdnaknarF
EPAM
AM
tiFevruC
;RGR
;SE;naeM
;AM
;FCOL
5891–0891
launnA
5891–5791
007
ASU
)4991(yalK
dnaelzzirG
tiFevruC
EAM
;ESMR
CFO
RAVB
CFO;RAVB
7991–0991
ylretrauQ
7991–3891
85
ASU
)7991(selrahCdna
kortO
EPAM
AM
SE
;RGR
;AMIRA;SE
;AM
6991–5991
noM
,auQ
6991–0991
99
ASU
)9991(.la
teenoicniriC
EAM
;ESMR
MCM
;RAV
AMRA
FOC
;MCM;MCS
;RAV;AMRA
2002–6991
launnaiB
5991–1891
03
lenaP
dnaorevaF
)5002(onillecraM
EP
NNA
CFO
;NNA
CFO
;NNA
0002–5991
ylretrauQ
0002–5791
401
ASU
)6002(seehrooV
EPAM
naeM
RGR
naeM
;tfirD
;TRL;RGR;CFO
1002–5991
launnA
1002–5891
71
ASU
)7002(gnoK
ESMR
WR
FOC
CFO
;WR;FOC;RGR
3002–4991
ylretrauQ
3002–0791
631
lenaP
)7002(zeréP
EPAM
MCE
RGR
MCE
;RGR
5002–3002
ylretrauQ
5002–8991
82
ainauhtiL
dnasikzduR
)7002(ėtytialuičaM
;ESMR
CFO
AMIRA
CFO;AMIRA
4002–2002
ylhtnoM
4002–6991
801
ecnarF
)8002(.lateinirtsevliS
EPAM;EAM
EP
CFO
AMIRA
CFO;AMIRA
6002–9791
launnA
6002–5491
26
dnalreztiwS
)2102(leugoSdnayngatahC
EPAM
NNA
MVS
MG
;MVS
;NNA
1002–9991
launnA
8991–0991
9
anihC
)9002(
.lateuL
)seunitnoC(
PublicBudgeting&Finance,2025 5
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on [27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by the
applicable
Creative
Commons
License

)deunitnoC(
|
1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
ESMR
WR
XIM
WR
;XIM
7002–1002
,nnA
7002–4891
882
lenaP
)0102(
zeréPdnalagerdeP
noM
,auQ
EPAM
AMIRA
MCE
AMIRA;MCE
1002
ylhtnoM
1002–5991
58
lizarB
)0102(.la
teoãlavroC
ESRR;EAR
RGR
MVS
;RGR;MVS
;NNA
6002–3002
launnA
6002–3002
8081
aihcezC
)0102(jelOdna
kejáH
ESMR
WR
RAVB
WR;RAVB;RAV
9002–4002
ylretrauQ
3002–9791
001
ASU
)0102(lorK
MD
;ESMR
WR
XIM
WR;MCE;XIM
;RA
6002–4991
ylhtnoM
6102–3691
273
lenaP
)0102(.la
teetnaronO
EAM
;ESMR
tfirD
FOC
CFO
;tfirD;FOC;WH
;AMIRA
1102–8991
launnA
7991–0791
82
ASU
)1102(
hsotnIcMdnaekooC
EPAM
SE
FOC
FOC
;SE
;MG
9002–9991
launnA
9002–9991
11
anihC
)1102(gnahZ
iefuRdnauiL
EPAM
NNA
MVS
MVS
;NNA
3002–3991
launnA
9991–0991
01
anihC
)1102(.la
teaix‐iL
EPAM
RGR
;AMIRA
MCE
;WR
MCE
;RGR;AMIRA
;WR
;tfirD
8002–7002
ylretrauQ
8002–5991
001
aitaorC
)2102(keziVdna
ćirtoB
ESMR
RA
SADIM
FOC;LDA
;RA
;SADIM
1102–0991
ylretrauQ
1102–8691
671
ASU
)2102(
nakzOdnaslesyhG
EPM
;EPAM
WH
AMIRAS
tfirD;AMIRAS
;RGR
;WH
2102–7991
ylhtnoM
2102–7991
291
lapeN
)2102(
alarioK
ESMR
naeM
SADIM
CFO
;naeM
;SADIM
1102–8002
ylretrauQ
2102–1991
611
lenaP
naoJdnasoluopokamisA
)3102(sederaP
EPSM
;EPAM
AMRA
NNA
MVS;AMRA
;NNA
1102–8002
launnA
1102–0891
23
anihC
)3102(nujihZ
EMR
;ESMR
CFO
MVS
CFO
;MVS
2102–0891
launnA
2102–0891
33
anihC
)4102(gnahZ
ESMR
RA
SADIM
FOC;LDA
;RA
;SADIM
2102–3991
launnA
2102–6591
75
ASU
)5102(
nakzOdnaslesyhG
EPAM;ESM;EPM
AMIRAS
AMSWH
;AMSWH;AMIRAS
3102–4002
ylhtnoM
2102–4002
101
hsedalgnaB
risatnuMdnaidnaN
CFO;AASWH
)5102(yruhduahC
ESMR
enoN
enoN
NNA
9002–7002
launnA
6002–3691
44
narI
)6102(.la
teiradmalA
EAM
;ESMR
AM
FOC
AM
;HCRAG;FOC;AMRA
5102–4102
ylhtnoM
5102–0002
281
ainaznaT
)7102(
alilimihC
ESMR
;EAM;EM
XAMIRA
RAVB
XAMIRA
;SADIM;RAVB
4102–0102
ylretrauQ
4102–3991
011
nedewS
nitraMdnanairazanhahS
)7102(regrebloS
ER;EPAM
CFO
FOC
CFO;FOC
;LAG
;NNA
4102–3102
ylhtnoM
2102–0002
441
lizarB
)7102(.late
anociT
;EAM;ESMR
;EM
AMIRAS
WH
RGR
;AMIRAS
;WH
7102–5102
ylretrauQ
7102–9002
63
acirfAhtuoS
dnaasinanakaM
ESAM;EPM
)8102(orerE
;ESMR
CFO
FOC
;RAVB;RAV
;MCE;WH
;WR
5102–1102
ylretrauQ
6102–5002
55
ainablA
)8102(icevhaKdna
jabaS
EPAM;EAM
CFO;FOC
;AMIRAS
;ESMR
RA
AMIRA
RAV
;AMIRA
;RA
7102
ylhtnoM
6102–5891
873
natsikaP
)8102(.la
teeneikimiertS
EPAM;EAM
EPAM
AMIRA
PLM
MTSL
;PLM;AMIRA
8102–5102
ylretrauQ
8102–9991
077
ASU
)9102(.la
tenotxuB
)seunitnoC(
6 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles are
governed
by the applicable
Creative
Commons
License

)deunitnoC(
| 1ELBAT
)s(cirteM
tsroW
tseB
sdohteM
.rep.roF
.qerf
.sbO
RYT
OT
yrtnuoC
)s(rohtuA
;EAM;ESMR
WR
STAB
CFO;STAB
;AMIRAS
;WR
8102–5102
ylhtnoM
4102–6002
801
eyikrüT
dna
udğodrE
;EM;EPAM
)9102(zamluroY
ESAM;EPM
;ESMR
WR
RAVB
WR;RAVB
;RAV
;RA
4102–9002
launnA
8002–7791
23
ASU
)9102(sedroCdnaaehScM
EPAM;EAM EAM
;ESMR
AMIRA
SE;RAVB
SE;AMIRA;RAVB
5102–2102
ylretrauQ
2102–8991
65
acirfAhtuoS
)9102(.la
teopaloM
EPM
CFO
AMIRA
CFO;AMIRA
7102–5102
ylhtnoM
4102–6002
801
eyikrüT
)9102(zamlıY
;EAM;EPAM
;RVSK‐W
‐ACP
;RVSK‐ACP;RVSK‐W
;RVSK
9102–7102
ylretrauQ
6102–1891
441
airegiN
)0202(.la
tenassahlA
ESMR
;ESM
RVSK‐ACP
RVSK‐W
RVSK‐W‐ACP
;ESMR
CFO
SADIM‐RA
CFO
;SADIM‐RA
7102–6102
ylretrauQ
6102–3991
29
ohtoseL
)0202(enamaD
EPAM;EAM EPAM
;ESMR
WH
AMIRA
WH ;AMIRA
9102–7102
ylhtnoM
6102–2002
081
anahG
lebA
dnairofO
)0202(yemuF
enoN
CFO
MG
CFO
;MG
9102–7102
launnA
6102–6002
11
eyikrüT
)0202.la
telasnÜ
ESM;EPAM
TRAC
AMIRA
;NNA
;AMIRA;SE
;AM
4102–4991
launnA
4102–4991
611
ASU
)2202(.la
tegnuhC
TRAC;NNK
ESMR
WR
SADIM
WR
;FOC;LDA
;RA
;SADIM
8102–9991
launnA
2102–8591
14
ASU
)2202(.la
teslesyhG
;EAM;ESMR
WR
BGC
CFO;BGC;WR;OSSAL;SADIM
1202–0202
noM
,auQ
1202–6002
471
ASU
)2202(gnaYdnairihaL
EPAM
;EPM
ESMR;EPAM
AMIRAS
RAV
AMIRAS
;RAV
3202–1202
ylretrauQ
3202–1102
94
tarahB
dnaeejrehkuM
)3202(ayrahcattahB
;ESMR
NNA
FOC
FOC
;NNA;SE
;STABT
2202–1202
ylhtnoM
2202–7102
44
tarahB
)3202(.late
biyyahT
EPAM;EAM
;EAM
AMIRA
URG
;TSOOBGX
;RVS;STE
;AMIRA
0202–5102
launnA
0202–0991
13
lenaP
)3202(.lategnaY
EPAM
;ESMR
;NNRiB;MTSL;NNC
URG ;NNRSA
;EPAM
seyaBevïaN
MTSL
;TSOOBGX
;FR;MTSL;AMIRA
3202–9102
auQ,nnA
3202–9102
02
tpygE
)4202(.la
teafilahK.M
ESMR
;ESM
seyaBevïaN
;NNK
EPAM
naeM
;NNA
;TRL;NNK
;NNA
;NNK;SE
;AMIRA
7102–6102
,nnA
5102–1991
5001
ASU
)4202(notrevOdnanosraL
tfirD
;naeM
;FCOL;TRL
;TSOOBGX
noM
,auQ
tfirD
EPAM;EAM
RLM
NNA
NNA
;RLM
1202–9102
launnA
1202–2002
03
anihC
)4202(eiX
EAM
;ESMR
RGR
OSSAL
;RA
;RGR;OSSAL;FR
;WR
;RA
9102–9002
ylretrauQ
9002–2991
17
ailartsuA
)4202(
aLdnagnoW
NNA
;TSOOBGX
)seunitnoC(
PublicBudgeting&Finance,2025 7
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley Online
Library
on [27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
larueNtnerruceRlanoitceridiB,NNRiB;noitamrofsnarTxoC–xoBhtiwledoMecapSetatSgnihtoomSlaitnenopxE,STAB;krowteNlarueNtnerruceRlaitneuqeSdesaB‐noitnettA,NNRSA;egarevA‐gnivoMevissergerotuA,AMRA;stupnI larueNlanoitulovnoC,NNC;retliFnamlaKetatS‐itluMdetsujdAyllanoitceS‐ssorC,FKSM‐C;gnitsooBtneidarGesiW‐tnenopmoC,BGC;eerTnoissergeRdnanoitacifissalC,TRAC;noissergerotuArotceVnaiseyaB,RAVB;krowteN yarG,MG;yticitsadeksoreteHlanoitidnoCevissergeRotuAdezilareneG,HCRAG;smhtiroglAciteneG,LAG;gniretliFevitpadAlareneG,FAG;gnihtoomSlaitnenopxE,SE;noitcerroCrorrE,MCE;stsaceroFfogninibmoC,FOC;krowteN evitiddAlanosaeSretniW‐tloH,AASWH;hcaorppAevitacilpitluMlanosaeSretniW‐tloH,AMSWH;sretniW‐tloH,WH;doirePdetsaceroF,.rep.roF;tinUtnerruceRdetaG,URG;krowteNlarueNnoissergeRdezilareneG,NNRG;ledoM larutcurtSyrtnuoC‐itluM,MCM;egarevAgnivoM,AM;krowteNyromeMmreTtrohSgnoL,MTSL;dnerTraeniL,TRL;drawroFdeirraCnoitavresbOtsaL,FCOL;rotarepOnoitceleSdnaegaknirhSetulosbAtsaeL,OSSAL;hcaorppA ,RVS;enihcaMrotceVtroppuS,MVS;ledoMlarutcurtSyrtnuoC‐elgniS,MCS;egarevAgnivoMdetargetnIevissergerotuAlanosaeS,AMIRAS;klaWmodnaR,WR;noissergeR,RGR;tseroFmodnaR,FR;sisylanAtnenopmoClapicnirP ,RAV;egnarsraeys'atadgniniarT,RYT;ledomehtniartotdesusnoitavresbolatoT,OT;stnenopmoClanosaeSdnadnerT—srorrEAMRA—noitamrofsnarTxoC–xoB—ytilanosaeScirtemonogirT,STABT;noissergeRrotceVtroppuS Inparticular,theemergenceofcomplexhybridmodelssupported
suonegoxEhtiwegarevAgnivoMdetargetnIevissergeRotuA,XAMIRA;egarevAgnivoMdetargetnIevissergerotuA,AMIRA;evissergerotuA,RA;krowteNlarueNlaicifitrA,NNA;gaLdetubirtsiDdetnemguA,LDA:snoitaiverbbA ,ACP;ycneuqerFnoitavresbO,.qerf.sbO;stsaceroFlaiciffO,CFO;retliFnamlaKetatS‐itluM,FKSM;noissergeRraeniLelpitluM,RLM;nortpecrePreyaL‐itluM,PLM;ycneuqerF‐dexiM,XIM;gnilpmaSataD‐dexiM,SADIM;ledoM
byPCArepresentsanewstageinwhichresearchersstrategically
|     | combine | feature | engineering | with | advanced | algorithms |     | to maxi- |
| --- | ------- | ------- | ----------- | ---- | -------- | ---------- | --- | -------- |
)s(cirteM
EPAM EPAM EPAM
mizemodelperformance.
|     | The overall | assessment | of        | this methodological |             | evolution |      | reveals  |
| --- | ----------- | ---------- | --------- | ------------------- | ----------- | --------- | ---- | -------- |
|     | that the    | field of   | budget    | forecasting         | is not      | static    | but  | rather a |
|     | dynamic     | area of    | research, | constantly          | interacting |           | with | develop- |
tehporP;MTSL ments in neighboring disciplines such as econometrics, opera-
naeM
AMIRA tions research, and AI. The journey from simple time‐series
tsroW
|     | models to | complex | neural | networks | reflects | both | the methodo- |     |
| --- | --------- | ------- | ------ | -------- | -------- | ---- | ------------ | --- |
;NNA
|     | logical maturity |             | and the accumulated |          | intellectual |       | capital        | of the |
| --- | ---------------- | ----------- | ------------------- | -------- | ------------ | ----- | -------------- | ------ |
|     | field. At        | the same    | time,               | however, | the          | dense | methodological |        |
|     | diversity        | illustrated | in Figure           |          | 1 suggests   | the   | presence       | of a   |
FCOL “methodologicalinflation”intheliterature,aphenomenonthat
AMIRAS
tseB WH increasinglycomplicatesthetaskofselectinganoptimalmethod
| ;tfirD | withinagivencontextforpolicymakersandpractitioners. |     |     |     |     |     |     |     |
| ------ | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Second,thefrequencywithwhichdifferentforecastingmethods
;NNA FCOL are used together within the same study has been examined.
|     | This analysis | makes | it possible |     | to understand | which | methods |     |
| --- | ------------- | ----- | ----------- | --- | ------------- | ----- | ------- | --- |
;NNK ;tehporP;MTSL
;NNK ;naeM;tfirD researchers most frequently evaluate side by side when con-
FCOL;NNRG FOC;AMIRA
|     | ducting performance |     | comparisons, |     | and | thus which | methodo- |     |
| --- | ------------------- | --- | ------------ | --- | --- | ---------- | -------- | --- |
sdohteM
;AMIRA;WH
| ;RGR;SE | logicalcombinations |     | havegained |     | wider acceptance. |     |     |     |
| ------- | ------------------- | --- | ---------- | --- | ----------------- | --- | --- | --- |
TheconnectionsinFigure2indicatewhichpairsofmethodsare
;TSOOBGX
;WH most frequently tested together in comparative studies in the
;AMIRA
literature.Theanalysesclearlyshowthattraditionalmethodsare
oftenusedbothamongthemselvesandinconjunctionwithnext‐
.gnitsooBtneidarGemertxE,TSOOBGX;noissergeRrotceVtroppuSlenreKhtiwtelevaW,RVSK‐W;noissergerotuArotceV
|     | generation | techniques | for | comparison | purposes. |     | For instance, |     |
| --- | ---------- | ---------- | --- | ---------- | --------- | --- | ------------- | --- |
.rep.roF 9102–7102 4202–3202 7102–6102 ARIMAisfrequentlycomparednotonlywithitsownderivatives,
suchasSARIMA,whichincorporateseasonalvariations,butalso
withML‐basedmethods,suchasANNorSVM.Similarly,official
|     | agency forecasts |           | and various | regression |                    | techniques | appear   | to  |
| --- | ---------------- | --------- | ----------- | ---------- | ------------------ | ---------- | -------- | --- |
|     | serve as a       | benchmark | for         | almost     | all methodological |            | classes. | In  |
.qerf ylhtnoM ylhtnoM noM particular, when evaluating the performance of ML algorithms
| ,nnA | (XGBoost,LSTM,andSVM),comparisonswiththesetraditional |     |     |     |     |     |     |     |
| ---- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
.sbO ,auQ
methodsemergeasawidespreadtrend.Itisalsonoteworthythat
variationswithinthesamemodelfamily(e.g.,VARvs.BVARor
|     | AR vs. ARIMA)are |     | frequently | analyzed | together. |     | This | suggests |
| --- | ---------------- | --- | ---------- | -------- | --------- | --- | ---- | -------- |
9102–9002 2202–5002 5102–1991
|     | that researchers |     | aim to understand |     | how different |     | specifications |     |
| --- | ---------------- | --- | ----------------- | --- | ------------- | --- | -------------- | --- |
RYT
orenhancementswithinagivenmodelfamily,suchasBayesian
|     | approaches | or seasonal | adjustments, |         | affect    | forecasting | perform- |      |
| --- | ---------- | ----------- | ------------ | ------- | --------- | ----------- | -------- | ---- |
|     | ance. In   | sum, this   | visual       | network | structure | reveals     | that     | com- |
5001
OT 021 612 parative analyses in the budget forecasting literature follow a
certainsystematicpattern:thevalidityandcontributionofanew
|     | method are | most | often assessed |     | against established |     | and | widely |
| --- | ---------- | ---- | -------------- | --- | ------------------- | --- | --- | ------ |
yrtnuoC
eyikrüT
ASU ASU accepted traditional methods, while the relative strengths and
|     | weaknesses | of different | methodological |     | families |     | are empirically |     |
| --- | ---------- | ------------ | -------------- | --- | -------- | --- | --------------- | --- |
evaluatedthroughthesetypicalcomparisons.
)5202(notrevOdnanosraL Third,thechangingtrendsinthepopularityofspecificforecasting
)5202(araKdnarelügneŞ
|     | methods | over time | have been | examined. |     | This analysis | makes | it  |
| --- | ------- | --------- | --------- | --------- | --- | ------------- | ----- | --- |
)deunitnoC(
|     | possible to | objectively | observe | the | shifts in | academic | interest | to- |
| --- | ----------- | ----------- | ------- | --- | --------- | -------- | -------- | --- |
)5202(.la
|     | ward particular | methodologies |        | and         | the dominance |         | cycles   | of cer- |
| --- | --------------- | ------------- | ------ | ----------- | ------------- | ------- | -------- | ------- |
|     | tain methods    | within        | the    | literature. | The           | graph   | displays | the     |
|     | changing        | frequencies   | of use | over        | the years     | for the | six most | fre-    |
)s(rohtuA
|
tegnuhC quentlycomparedmethodsintheanalyzedstudies.
1ELBAT
ThefindingsderivedfromGraph1clearlyrevealshiftsinacademic
|     | trends. Official |     | forecasts | were frequently |     | used | as benchmark |     |
| --- | ---------------- | --- | --------- | --------------- | --- | ---- | ------------ | --- |
8 PublicBudgeting&Finance,2025

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FIGURE1 | | Evolutionofforecastingmethodsinbudgetingliteratureovertime.  |     |     |     |
| ------- | -------------------------------------------------------------- | --- | --- | --- |
| FIGURE2 | | Co‐occurrenceofforecastingmethodsincomparativebudgetstudies. |     |     |     |
AI‐based
references. The ARIMA model, however, has remained a con- generation, approaches. Overall, the current methodo-
sistentlypopulartoolforcomparisonsincethe1990s.Regression‐ logicalspectrumhasexpandedtoencompassbothbasicstatistical
modelsandadvancedcomputationaltechniques(Tables2–4).
| based methods    | experienced  | a resurgence | in the early 2000s,   | but |
| ---------------- | ------------ | ------------ | --------------------- | --- |
| their popularity | subsequently | declined     | somewhat. ML methods, |     |
such as ANN, have increasingly featured in comparative studies Fourth,thestructuralcharacteristicsofthedatasetsusedinthe
sincethe2010s.COF,ontheotherhand,hasmaintainedastable trainingofforecastingmodelsinthereviewedstudieshavebeen
presence among the methods consistently used for comparison analyzed.Thisanalysisiscriticalforunderstandingthecapacity
throughout the entire period under review. These trends indicate and diversity of the data sources feeding the models. Below,
thattheliteraturehaspreserveditsreferencepointsbasedontra- an assessment is presented showing the distributions of the
whilegraduallytransitioningtowardnew‐
ditionalmethodologies training datasets in terms of time span (number of years),
PublicBudgeting&Finance,2025 9

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
GRAPH1 | Trendsinthepopularityofkeyforecastingmethodsovertime(best5).
TABLE2 | Characteristicsoftrainingdatasetsinbudgetforecastingstudies.
Period Studies(N) Observation range Studies(N) Frequency Studies(N)
| 1–5years   |     | 1–25     |     |     |           |     |
| ---------- | --- | -------- | --- | --- | --------- | --- |
|            | 4   |          |     | 8   | Quarterly | 28  |
| 6–10years  |     | 26–50    |     |     |           |     |
|            | 13  |          |     | 16  | Annual    | 26  |
| 11–15years |     | 51–75    |     |     |           |     |
|            | 17  |          |     | 10  | Monthly   | 23  |
| 16–20years |     | 76–100   |     |     |           |     |
|            | 10  |          |     | 6   | Biannual  | 1   |
| 21–25years |     | 101–150  |     |     |           |     |
|            | 9   |          |     | 12  |           |     |
| 26–30years |     | 151–250  |     |     |           |     |
|            | 2   |          |     | 7   |           |     |
| 31–35years |     | 251–400  |     |     |           |     |
|            | 7   |          |     | 3   |           |     |
| 35–50years |     | 401–1000 |     |     |           |     |
|            | 4   |          |     | 4   |           |     |
| 50+years   | 3   | 1000+    |     | 3   |           |     |
Country‐leveldistributionofbudgetforecasting
| TABLE3 | |     |     | TABLE4 | | Numberofstudiesusingeachevaluationmetric. |     |     |
| -------- | --- | --- | ------ | ------------------------------------------- | --- | --- |
research.
|             |     |            | Metric |     |     | Frequency |
| ----------- | --- | ---------- | ------ | --- | --- | --------- |
| Countries   |     | Studies(N) |        |     |     |           |
|             |     |            | MAPE   |     |     | 38        |
| USA         |     | 30         | RMSE   |     |     | 36        |
| China       |     | 6          | MAE    |     |     | 22        |
| Panel       |     | 6          | MPE    |     |     | 7         |
| Türkiye     |     | 4          | PE     |     |     | 6         |
| Bharat      |     | 2          | MSE    |     |     | 5         |
| Brazil      |     | 2          | ME     |     |     | 5         |
| SouthAfrica |     | 2          | Others |     |     | 9         |
| Others*     |     | 17         | None   |     |     | 2         |
*17differentcountriesstudiedonce.
6–25years.
number of observations, and the most commonly used data on datasets covering Notably, datasets spanning
frequencies(Graph2). 11–15years are the most commonly used period (17 studies),
|     |     |     | indicating | a clear tendency | in the literature toward | a medium‐ |
| --- | --- | --- | ---------- | ---------------- | ------------------------ | --------- |
Examining the distribution of the time spans of the training da- term forecasting horizon. This approach allows for capturing
tasets,itisevidentthatthevastmajorityofstudies(over60%)rely macroeconomic cycles by maintaining sufficient historical depth
| 10  |     |     |     |     | PublicBudgeting&Finance,2025 |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- |

GRAPH2 | Averagetrainingdataspanbyforecastingmodel(best10).
while limiting potential parameter instability issues associated the tabular data. Notably, studies based on relatively simple
with very long time series. On the other hand, studies using da- models such as ADL and AR have average training periods
tasets of 31years or more are relatively few (14 studies in total), exceeding 40years, indicating that long seriesarenecessaryto
reflecting both the accessibility challenges and methodological ensure the parametric stability of these models. In contrast,
risksposedbystructuralbreaksinverylongseries.Conversely,the morecomplexmodelssuchasMIDASorARMAcanbeapplied
small number of studies (4 studies) relying solely on short‐term with comparatively shorter datasets, demonstrating the adapt-
dataof1–5yearscanbeconsideredcharacteristicofcontextswith ability of methods to series of different lengths. However, it is
limiteddatadepth,particularlyindevelopingeconomies. noteworthy that the relationship between model type and
numberofobservationsdoesnotfollowalinearpattern.While
In terms of the number of observations, the literature exhibits someshort‐term studiescorrespondto low‐complexitymodels,
considerable diversity. A significant portion of studies is con- long‐term seriestend to be associated with models sensitive to
centrated in the 26–50 observation range (16 studies), while parametric stability. This suggests that the alignment between
those based on more than 100 observations also constitute a model choice and training data length is shaped not only by
notablegroup(28studies).However,only16ofthese28studies technical considerations but also by data accessibility and the
contain 150 or more observations, indicating that studies rely- objectives ofthestudy.
ingonlongseriesremainrelativelylimitedintheliterature.The
presence of eight studies with only 1–25 observations raises Fifth,theaverageforecastinghorizonsofthemethodsusedinthe
serious concerns regarding the reliability of the models used. reviewed studies have been analyzed. This analysis provides
Forecasting based on such short series entails substantial important insights into which time spans are preferred for dif-
methodologicalweaknesses,particularlyintermsoftestingthe ferent methodological approaches and whether certain methods
statistical significance of parameters and producing robust arecharacteristicallyassociatedwithshort‐orlong‐termforecasts.
forecasts.Thisissuemaypreventdata‐intensivemethods,such
asDL,frombeingfullyevaluated,highlightingvaryinglevelsof The findingsin Graph 3 indicateaclear clusteringof methods
reliability in the literature and necessitating cautious interpre- intermsofforecastinghorizons.Traditionalstatisticalmethods,
tationof resultsfrom studieswith limited observations. such as AR and MA models, stand out with long average
horizons of 14.3 and 12years, respectively. Similarly, the
Examining data frequencies, it is observed that quarterly (28 MIDASmethod,withanaveragehorizonof9.7years,isamong
studies), annual (26 studies), and monthly (23 studies) data are the methods used for long‐term forecasts. This suggests that
chosen with relatively similar frequency. This distribution indi- relatively simple linear methods tend to provide a more stable
cates that, rather than a concentration on a single frequency, optionfor long‐term forecasts.
different frequenciesareusedatcomparablerates. Accordingly,
researchers' choices are largely shaped by data availability, the In contrast, parametric and multivariate models tend to focus
scopeofthestudy,andtheintendedforecastinghorizon. on shorter forecasting horizons. For example, ARIMA
(5.5years), VAR (5.1years), and BVAR (4.7years) are predom-
The findings on the average training periods of models in inantlyappliedinshort‐tomedium‐termforecasts.Thispattern
Figure3showsignificantalignmentwhenconsideredalongside indicates that as the number of parameters and the modeling
PublicBudgeting&Finance,2025 11
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| FIGURE3 |                                                     | Relationshipbetweenmethodsandperformancemetrics. |     |
| ------------------------------------------------------------- | ------------------------------------------------ | --- |
| GRAPH3 | Averageforecastinghorizonsbymethodinreviewedstudies. |                                                  |     |
long‐term
flexibilityofthesemodelsincrease,theirstabilitydiminishesin concentrated in relatively forecasts, parametric and
thefaceof long‐termuncertainty. multivariatemodelsinmedium‐termhorizons,andMLandDL
methodsinshort‐termforecasts.Thisdistributionindicatesthat
| InML‐ DL‐based |     |     |
| -------------- | --- | --- |
and methods,the forecastinghorizonis notably forecasting horizons are determined not only by researchers'
shorter.ANNstandsoutwithanaveragehorizonof5.3years,while preferences but also by the structural limitations inherent in
LSTMislimitedtoonly3.3years.Theseresultsindicatethatsuch eachmethod.
| methods are strong | in capturing complex, | nonlinear relationships |
| ------------------ | --------------------- | ----------------------- |
short‐term long‐term
over periods but are more constrained in Sixth, the geographic distribution of the reviewed comparative
forecastsduetorisksofparameterinstabilityandoverfitting. studies has been analyzed. This analysis provides important
insightsintowhichcountriesandregionsacademicresearchon
Overall, a methodological division of labor emerges among budget forecasting methods is concentrated, thereby shedding
forecasting methods: simple linear statistical methods are light onthe geographiccoverageof theexistingliterature.
12 PublicBudgeting&Finance,2025

The findings on country distribution reveal a pronounced forthevastmajorityofusage,establishingadominantposition
concentration and imbalance in the literature. The United in assessing forecasting accuracy. The prominence of MAPE
Statesaccountsforthelargestsharewith30studies,followedby andRMSEcanbeexplainedbytheireaseofinterpretationand
China(6),paneldatasets(6),andTurkey(4).Brazil,India,and their suitability for comparisons across series of different
South Africa are represented by two studies each. The magnitudes.
remaining17countriesarecoveredonlyonceandaregrouped
under the “Others” category. This pattern indicates that em- In contrast, metrics such as MPE (7 studies), ME (5 studies),
piricalresearchisheavilyfocusedonalimitedsetofcountries, MSE (5 studies), and PE (6 studies) are used relatively infre-
while a wide range of other nations receives very limited quently. Their limited representation indicates that the litera-
attention. ture tends to favor standardized metrics that allow for
international comparisons. Additionally, in nine studies cate-
The reasons for the United States' clear predominance include gorized as “Others,” more specific or context‐specific metrics
easy access to data, long historical macroeconomic series, the were employed, while two studies did not report any perform-
perception of U.S. data as a global benchmark in academic ance metric at all. The latter case can be regarded as a signifi-
publications, and the dominance of Anglo‐Saxon literature. In cantshortcoming interms ofmethodological transparency.
contrast,fordevelopingcountries,bothdifficultiesinaccessing
long‐term reliable data series and differences in institutional The network structure in the graph further clarifies the re-
contextsresultintheirunderrepresentationinstudies.Turkey's lationships between methods and metrics. RMSE and MAPE
representationbyonlyfourstudiesservesasaconcreteexample stand out as nodes with the most extensive connections,
ofthis overall imbalance. showingstrongassociationswithwidelyusedmethodssuchas
ARIMA, ANN, HW, VAR, OFC, COF, and SARIMA. This
On the other hand, the presence of six studies using panel da- finding indicates that performance evaluations of prominent
tasets indicates that researchers have also pursued cross‐ methods in the literature generally rely on the same set of
country comparisons rather than focusing solely on single‐ metrics, and comparability is largely established around these
countryanalyses.However,thelimitednumberofpanelstudies measures. In contrast, less frequently used methods such as
suggests that the literature has not yet fully developed a com- LSTM, XGBoost, or Prophet are linked to a relatively limited
parativeperspectivecapableofprovidinggeneralizableinsights number of metrics, suggesting both low methodological diver-
andrevealing cross‐countrydifferences. sityandtheabsenceofastandardizedapproachfor evaluating
theperformanceof thesemethods.
Seventh,thedistributionofmetricsusedtoevaluateforecasting
performance in the reviewed comparative studies has been Eighth and finally, the relationship between method diversity
analyzed. This analysisprovides important insights into which and academic impact in the reviewed comparative studies has
evaluation criteria are prioritized in the literature and, conse- been analyzed. This analysis provides important insights into
quently,whichdimensionsoferrorareconsideredmostcritical whether the number of methods compared in a study has any
in methodcomparisons. effect onthe number ofcitationsthestudy receives(Graph4).
Examiningthemetricsusedtoevaluatemethodperformance,a The analysis results indicate a notable but nonlinear relation-
clear concentration is observed in the literature. The most fre- shipbetweenthenumberofmethodsinastudyanditscitation
quently used evaluation criteria are MAPE (38 studies), RMSE count. The vast majority of the reviewed studies (over 70%)
(36studies),andMAE(22studies).Thesethreemetricsaccount compare between 2 and 5 methods. Studies with 2 methods
GRAPH4 | Relationshipbetweenstudies,methods,andcitations.
PublicBudgeting&Finance,2025 13
15405850,
0,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
representthemostcommoncategorywith18cases,followedby product not of a single, static process, but of political negotia-
| 3‐method |     |     |     |     | 4‐method |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studies with 15 cases and studies with 14 tions,economicshocks,institutionalchanges,andadministrative
cases. In terms of citation counts, the highest average citation rules.Accordingly, thefocus shouldshift fromfinding theopti-
performance is observed among studies comparing between 3 malmodeltoidentifyingtherightmodelfortherightcontext.
and6methods.Studieswith3methodsreceiveanaverageof26
citations,whilethosewith6methodsreachasimilaraverageof
| 26 citations. |     | This | finding | suggests | that | a moderate | level of |       |              |     |      |           |        |     |     |
| ------------- | --- | ---- | ------- | -------- | ---- | ---------- | -------- | ----- | ------------ | --- | ---- | --------- | ------ | --- | --- |
|               |     |      |         |          |      |            |          | 5.2 | | The Enduring |     | Role | of Simple | Models |     | and |
method diversitymayenhance academic impact. the Benchmarking Paradox
| However, | it  | is also | evident | that citation |     | performance | does not |         |            |            |             |     |        |        |      |
| -------- | --- | ------- | ------- | ------------- | --- | ----------- | -------- | ------- | ---------- | ---------- | ----------- | --- | ------ | ------ | ---- |
|          |     |         |         |               |     |             |          | Despite | the influx | of complex | techniques, |     | simple | models | such |
increase consistently with the number of methods. Studies as OFC, RW, and various regression approaches remain not
| including | 7       | or more | methods  | exhibit | a           | noticeable | decline in   |               |     |            |     |             |             |     |     |
| --------- | ------- | ------- | -------- | ------- | ----------- | ---------- | ------------ | ------------- | --- | ---------- | --- | ----------- | ----------- | --- | --- |
|           |         |         |          |         |             |            |              | only relevant | but | also serve | as  | fundamental | benchmarks. |     | Any |
| citation  | counts. | This    | suggests | that    | comparisons |            | involving an |               |     |            |     |             |             |     |     |
newmodelmustconsistentlyoutperformthesenaïveorsimple
excessive number of methods may be less favored by readers standards to justify its added complexity. The fact that these
andresearchersorthatsuchstudiesmaygivetheimpressionof
|             |     |                |     |         |      |            |        | simple models | still | frequently | rank | among | the | top performers, |     |
| ----------- | --- | -------------- | --- | ------- | ---- | ---------- | ------ | ------------- | ----- | ---------- | ---- | ----- | --- | --------------- | --- |
| emphasizing |     | methodological |     | breadth | over | analytical | depth. |               |       |            |      |       |     |                 |     |
oratleastarenotconsistentlytheworst,incomparativestudies
Interestingly,studiesemployingonlyasinglemethodarequite
servesasacautionaryreminderforthefield.Itunderscoresthat
rare (3 studies), and their average citation count (7 citations) statistical sophistication does not automatically translate into
| remains | relatively |     | low. | This finding |     | suggests | that non‐ |             |              |     |              |     |          |       |          |
| ------- | ---------- | --- | ---- | ------------ | --- | -------- | --------- | ----------- | ------------ | --- | ------------ | --- | -------- | ----- | -------- |
|         |            |     |      |              |     |          |           | forecasting | superiority, |     | particularly | in  | contexts | where | data are |
comparativestudiesmayhaveamorelimitedacademicimpact
|     |     |     |     |     |     |     |     | noisy, short, | and | subject | to unpredictable |     | political |     | interven- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ---------------- | --- | --------- | --- | --------- |
compared tocomparative studies. tions. This creates a paradox: as research energy increasingly
|     |     |     |     |     |     |     |     | focuses | on developing | complex |     | models, | the practical |     | value of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ------- | --- | ------- | ------------- | --- | -------- |
Inconclusion,thisanalysissuggeststheexistenceofanoptimal
|     |     |     |     |     |     |     |     | these advancements |     | often | remains | marginal |     | when compared |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | ------- | -------- | --- | ------------- | --- |
range for method diversity. Comparisons with very few meth- against well‐defined, simple benchmarks.
| ods are | considered |     | insufficient, | while | studies | including | an ex-      |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ------------- | ----- | ------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| cessive | number     | of  | methods       | may   | be less | favored   | by readers. |     |     |     |     |     |     |     |     |
Studiescomparingbetween3and6methodsexhibitthehighest
|          |         |            |     |      |               |     |             | 5.3 |      | Data Quality, |     | Quantity, |     | and the | Global |     |
| -------- | ------- | ---------- | --- | ---- | ------------- | --- | ----------- | ---------- | ------------- | --- | --------- | --- | ------- | ------ | --- |
| academic | impact, | indicating |     | that | comprehensive |     | yet focused |            |               |     |           |     |         |        |     |
|          |         |            |     |      |               |     |             | Inequality | Issue         |     |           |     |         |        |     |
comparisonscontributemorevaluableinsightstotheliterature.
|     |     |     |     |     |     |     |     | The analysis | of        | training   | data characteristics |     | highlights |              | a sig- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ---------- | -------------------- | --- | ---------- | ------------ | ------ |
|     |     |     |     |     |     |     |     | nificant     | and often | overlooked | challenge:           |     | data       | constraints. | The    |
5 | Discussion and Policy Recommendations prevalence of studies using 11–15 years of data indicates that
|     |     |     |     |     |     |     |     | many models | are | built | on relatively |     | limited information |     | sets. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------------- | --- | ------------------- | --- | ----- |
The comprehensive analysis presented in this study offers a This poses a critical limitation for data‐hungry methods such
multidimensional examination of the comparative structure of as DL, potentially leading to overfitting and reduced out‐of‐
| the budget |     | forecasting | literature, |     | characterized |     | by methodo- |        |                |              |     |     |            |     |           |
| ---------- | --- | ----------- | ----------- | --- | ------------- | --- | ----------- | ------ | -------------- | ------------ | --- | --- | ---------- | --- | --------- |
|            |     |             |             |     |               |     |             | sample | generalization | performance. |     | The | geographic |     | distribu- |
logical diversity, geographic biases, and the ongoing tension tion of studies further exposes a substantial data gap. The
between model complexity and practical applicability within a dominance of United States‐based research reflects not merely
| dynamic | and   | evolving | field.  | The     | following | discussion    | synthe- |          |             |     |                     |        |     |                    |     |
| ------- | ----- | -------- | ------- | ------- | --------- | ------------- | ------- | -------- | ----------- | --- | ------------------- | ------ | --- | ------------------ | --- |
|         |       |          |         |         |           |               |         | academic | preference  | but | is directly         | linked | to  | data availability, |     |
| sizes   | these | findings | to draw | broader |           | implications, | address |          |             |     |                     |        |     |                    |     |
|         |       |          |         |         |           |               |         | quality, | and length. | The | underrepresentation |        |     | of developing      |     |
inherenttensionsinthefield,andsuggestdirectionsforfuture economiesconstitutesacriticalgapintheliterature.Budgetary
researchandpractice. processes,institutionalframeworks,andeconomicfluctuations
inthesecontextsdiffersubstantially.Modelsoptimizedonlong,
|             |                  |         |     |            |     |                |           | stable U.S.       | time           | series          | may fail | when | applied   | to economies |     |
| ----------- | ---------------- | ------- | --- | ---------- | --- | -------------- | --------- | ----------------- | -------------- | --------------- | -------- | ---- | --------- | ------------ | --- |
|             |                  |         |     |            |     |                |           | proneto           | fiscal shocks, | characterizedby |          |      | lowerdata | quality      | and |
| 5.1         | | Methodological |         |     | Diversity  | and | the            | Quest for |                   |                |                 |          |      |           |              |     |
| the Optimal |                  | Model   |     |            |     |                |           | shorterhistorical |                | records.        |          |      |           |              |     |
| The most    | striking         | finding | of  | this study | is  | the relentless | diversi-  |                   |                |                 |          |      |           |              |     |
fication offorecasting methods.The evolution from simple AR- 5.4 | Evaluation Inconsistency and the
|     |        |                  |     |      |          |     | PCA‐   | Hegemony | of  | Metrics |     |     |     |     |     |
| --- | ------ | ---------------- | --- | ---- | -------- | --- | ------ | -------- | --- | ------- | --- | --- | --- | --- | --- |
| IMA | models | to sophisticated |     | LSTM | networks | and | hybrid |          |     |         |     |     |     |     |     |
W‐KSVR
|     | frameworks |     | represents |     | a true | methodological | arms |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | ---------- | --- | ------ | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
race. This expansion is undoubtedly fueled by the quest for The near‐absolute dominance of MAPE, RMSE, and MAE as
| accuracy, | supported |     | by increasing |     | computational |     | power and ri- |                            |     |     |                            |     |     |     |     |
| --------- | --------- | --- | ------------- | --- | ------------- | --- | ------------- | -------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- |
|           |           |     |               |     |               |     |               | performancemetricsprovides |     |     | acommonlanguageforcompari- |     |     |     |     |
cher data availability. However, the analyses indicate that this son but also poses a potential pitfall: the tyranny of averages.
proliferation does not yield a universally superior algorithm; These metrics measure themagnitudeof errors but remain lar-
rather, ithas led to a formof methodological inflation that can gelyagnostic to thedirection and timingofmistakes. Ina bud-
overwhelm practitioners and obscure clear guidance. The getary context, the cost of overestimating a deficit (potentially
absence of a single “best” method should not be viewed as a leading to unnecessary austerity measures) is substantially dif-
failure of the research community but as a reflection of the ferentfromthecostofunderestimatingit(potentiallytriggeringa
near‐complete
inherentcomplexityofbudgetaryprocesses.Budgetdataarethe fiscal crisis). The neglect of directional metrics
| 14  |     |     |     |     |     |     |     |     |     |     |     | PublicBudgeting&Finance,2025 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |

 15405850, 0, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008 by Berat Kara - Istanbul Medeniyet University , Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
horizon.Theresilienceoftraditionalstatisticalmethodsinlong‐
| such as | MPE in | the current |     | literature | represents | a   | significant |     |     |     |     |     |     |     |     |
| ------- | ------ | ----------- | --- | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
shortcoming. Evaluations should incorporate asymmetric loss termforecasts,alongsidethestrengthofMLandDLapproaches
functionsthatreflectthereal‐worldpoliticalandeconomiccosts in capturing short‐term complex relationships, indicates the
oferrors,ratherthansolelytheirstatisticalproperties. existenceofamethodological division oflabor.
|           |                   |          |          |        |          |         |            | The pronounced    |            | geographic          | concentration |                      |             | in the | literature, |
| --------- | ----------------- | -------- | -------- | ------ | -------- | ------- | ---------- | ----------------- | ---------- | ------------------- | ------------- | -------------------- | ----------- | ------ | ----------- |
|           |                   |          |          |        |          |         |            | particularly      | the        | underrepresentation |               |                      | of emerging |        | economies,  |
| 5.5 |     | Academia–Practice |          |          | Gap    |          |         |            |                   |            |                     |               |                      |             |        |             |
|           |                   |          |          |        |          |         |            | poses significant |            | limitations         | to            | the generalizability |             |        | of existing |
|           |                   |          |          |        |          |         |            | findings.         | Similarly, | the                 | near‐absolute |                      | dominance   |        | of metrics  |
| Citation  | impact            | analysis | provides | a      | striking | insight | into the   |                   |            |                     |               |                      |             |        |             |
|           |                   |          |          |        |          |         |            | such as           | MAPE,      | RMSE,               | and MAE       | in                   | performance |        | evaluation  |
| sociology | of the            | field.   | The      | higher | citation | rates   | of studies |                   |            |                     |               |                      |             |        |             |
comparing 3–6 methods suggestthat theacademic community leads to theneglectof criticaldimensions, including thedirec-
|                      |       |          |             |              |      |           |          | tionoferrors | andasymmetriccosts. |     |     |     |     |     |     |
| -------------------- | ----- | -------- | ----------- | ------------ | ---- | --------- | -------- | ------------ | ------------------- | --- | --- | --- | --- | --- | --- |
| values comprehensive |       |          | yet focused | comparisons. |      | However,  | this     |              |                     |     |     |     |     |     |     |
| academic             | ideal | does not | always      | align        | with | practical | needs. A |              |                     |     |     |     |     |     |     |
practitioner in a treasury department does not require a com- The findings of this study offer important implications for
|         |                  |     |            |     |           |           |         | future research. |      | First, contextual |     | appropriateness |     | should  | take     |
| ------- | ---------------- | --- | ---------- | --- | --------- | --------- | ------- | ---------------- | ---- | ----------------- | --- | --------------- | --- | ------- | -------- |
| parison | of six different |     | ML models; |     | they need | a single, | robust, |                  |      |                   |     |                 |     |         |          |
|         |                  |     |            |     |           |           |         | precedence       | over | methodological    |     | complexity.     |     | Second, | the geo- |
interpretable,andoperationallyfeasiblemodeltailoredtotheir
|          |          |          |      |        |                |     |           | graphic | scope should | be  | expanded | to  | include | emerging | econo- |
| -------- | -------- | -------- | ---- | ------ | -------------- | --- | --------- | ------- | ------------ | --- | -------- | --- | ------- | -------- | ------ |
| specific | national | context. | This | points | to a potential |     | academia– |         |              |     |          |     |         |          |        |
practice disconnect. The complexity of state‐of‐the‐art models mies, and datasets should be enriched accordingly. Third,
|              |     |          |       |         |      |        | “black | performance | evaluation |     | criteria | should | be diversified |     | to reflect |
| ------------ | --- | -------- | ----- | ------- | ---- | ------ | ------ | ----------- | ---------- | --- | -------- | ------ | -------------- | --- | ---------- |
| (e.g., LSTMs | and | XGBoost) | often | renders | them | opaque |        |             |            |     |          |        |                |     |            |
thepolicycostsofforecasterrors.Finally,hybridandensemble
| boxes” for | policymakers. |     | Simpler | models | or  | official | forecasts, |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------- | ------ | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
evenifslightlylessaccuratebysomemetrics,offertransparency learning approaches warrant further investigation to leverage
|     |     |     |     |     |     |     |     | therelativestrengths |     | ofdifferentmethods. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------- | --- | --- | --- | --- | --- |
andaccountability.Futureresearchshouldaddressthisgapby
| not only | reporting | accuracy | metrics |     | but also | considering | oper- |     |     |     |     |     |     |     |     |
| -------- | --------- | -------- | ------- | --- | -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ational aspects, such as computational requirements, inter- For policymakers and practitioners, this study emphasizes the
|                            |     |     |                       |     |     |     |            | importance | of  | avoiding | dogmatic | method | selection |     | in budget |
| -------------------------- | --- | --- | --------------------- | --- | --- | --- | ---------- | ---------- | --- | -------- | -------- | ------ | --------- | --- | --------- |
| pretability,andintegration |     |     | intoexistingbudgetary |     |     |     | processes. |            |     |          |          |        |           |     |           |
forecasting.Adoptingaflexibleandpluralisticapproach,taking
intoaccountinstitutionalcapacity,dataquality,andforecasting
|       |         |        |     |          |     |            |     | objectives, | can | contribute | to producing |     | more | realistic | and reli- |
| ----- | ------- | ------ | --- | -------- | --- | ---------- | --- | ----------- | --- | ---------- | ------------ | --- | ---- | --------- | --------- |
| 5.6 | | Rise of | Hybrid | and | Ensemble |     | Approaches |     |             |     |            |              |     |      |           |           |
able budgetforecasts.
Theemergenceofhybridmodelspoints,albeitmodestly,toward
Inconclusion,progressinthefieldofbudgetforecastingdepends
| a promising         | direction |     | for the    | field. Rather | than      | treating    | meth- |          |            |                         |     |         |           |      |            |
| ------------------- | --------- | --- | ---------- | ------------- | --------- | ----------- | ----- | -------- | ---------- | ----------------------- | --- | ------- | --------- | ---- | ---------- |
|                     |           |     |            |               |           |             |       | less on  | developing | increasingly            |     | complex | models    | and  | more on    |
| ods as competitors, |           | the | discipline | is            | gradually | recognizing | the   |          |            |                         |     |         |           |      |            |
|                     |           |     |            |               |           |             |       | managing | the        | existing methodological |     |         | diversity | in a | systematic |
valueofhybridizationandensembletechniques.Thestrengths context‐sensitive
|              |     |            |     |         |            |     |             | and |     | manner. |     | This study | provides |     | a compre- |
| ------------ | --- | ---------- | --- | ------- | ---------- | --- | ----------- | --- | --- | ------- | --- | ---------- | -------- | --- | --------- |
| of one model | can | compensate |     | for the | weaknesses |     | of another. |     |     |         |     |            |          |     |           |
hensivefoundationforsucheffortsandaimstocontributetothe
Forinstance,aclassicalstatisticalmodelmaycapturelong‐term
developmentofbudgetforecastingasbothascienceandanart.
| trends, while    | an  | ANN       | can adjust | for       | recent | nonlinear | devia- |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---------- | --------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| tions. Combining |     | forecasts | from       | different | model  | families  | often  |     |     |     |     |     |     |     |     |
yieldsmoreaccurateandrobustresultsthananysinglemodel.
| meta‐modeling |     |           |     |       |         |     |             | References |     |     |     |     |     |     |     |
| ------------- | --- | --------- | --- | ----- | ------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| This          |     | approach, |     | which | focuses | on  | integrating |            |     |     |     |     |     |     |     |
informationratherthanselectingasingle“winner,”appearsto “Searching
|     |     |     |     |     |     |     |     | Agostini, | S. J. 1991. |     | for | a Better | Forecast: | San | Francisco's |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --- | -------- | --------- | --- | ----------- |
Model.”
be a more efficient pathway than developing isolated, increas- Revenue Forecasting Government Finance Review 7, no. 6:
13–16.
inglycomplexalgorithms.
“Forecasting
|     |     |     |     |     |     |     |     | Alamdari, | S. H., | H. Khalizadeh, | and | A. Zayer. | 2016. |     | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------------- | --- | --------- | ----- | --- | --- |
Models.”
|     |     |     |     |     |     |     |     | Iranian | Tax Revenues: | Application |     | of Nonlinear |     |     | Journal of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ----------- | --- | ------------ | --- | --- | ---------- |
InternationalEconomicsandManagementStudies1,no.2:21–48.
6 | Conclusion
“Assimi-
|     |     |     |     |     |     |     |     | Alhassan, | B. G.,    | F. B. Yusof, | and S.   | M. Norrulashikin. |             | 2020. |        |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | -------- | ----------------- | ----------- | ----- | ------ |
|     |     |     |     |     |     |     |     | lation of | Principal | Component    | Analysis |                   | and Wavelet | With  | Kernel |
Thisstudysystematicallyanalyzestheliteratureexaminingthe Medium‐Term
|             |               |     |               |        |                       |                |      | Support       | Vector        | Regression | for                   |            | Financial |                  | Time Series |
| ----------- | ------------- | --- | ------------- | ------ | --------------------- | -------------- | ---- | ------------- | ------------- | ---------- | --------------------- | ---------- | --------- | ---------------- | ----------- |
| comparative | performance   |     | of            | budget | forecasting           | methods,       | pro- | Forecasting.” |               |            |                       |            |           |                  |             |
|             |               |     |               |        |                       |                |      |               | International |            | Journalof             | Management |           | and Humanities4, |             |
| viding a    | comprehensive |     | overview      | of     | the field's           | methodological |      | no.7:40–48.   |               |            |                       |            |           |                  |             |
| evolution,  | geographic    |     | distribution, |        | data characteristics, |                | and  |               |               |            |                       |            |           |                  |             |
|             |               |     |               |        |                       |                |      | Asher, M.     | G.1978.       | “Accuracy  | of BudgetaryForecasts |            |           | of Central       | Gov-        |
| performance | evaluation    |     | trends.       | The    | findings              | indicate       | that |               |               |            |                       |            |           |                  |             |
ernment,1967‐68to1975‐76.”EconomicandPoliticalWeekly13,no.8:
budgetforecastingisnotastaticdomainbutadynamicresearch
423–432.
| area in | continuous | evolution, |     | deeply | influenced |     | by develop- |                |     |                   |     |            |              |     |        |
| ------- | ---------- | ---------- | --- | ------ | ---------- | --- | ----------- | -------------- | --- | ----------------- | --- | ---------- | ------------ | --- | ------ |
|         |            |            |     |        |            |     |             | Asimakopoulos, |     | S., Joan Paredes, |     | and Thomas | Warmedinger. |     | “Fore- |
ments in relateddisciplines.
castingFiscalTimeSeriesUsingMixedFrequencyData.”ECBWorking
PaperNo.1550,2013.
| The analyses | of          | this study | clearly | demonstrate |            | that | there is no  |          |       |               |              |     |     |          |          |
| ------------ | ----------- | ---------- | ------- | ----------- | ---------- | ---- | ------------ | -------- | ----- | ------------- | ------------ | --- | --- | -------- | -------- |
|              |             |            |         |             |            |      |              | Auld, D. | A. L. | 1970. “Fiscal | Marksmanship |     | in  | Canada.” | Canadian |
| single,      | universally | optimal    |         | method      | for budget |      | forecasting. |          |       |               |              |     |     |          |          |
JournalofEconomics3,no.3:507–511.
| Instead, | the performance |     | of  | forecasting | methods |     | varies subs- |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | --- | ----------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
tantially depending on contextual factors such as economic Baghestani,H.,andR.McNown.1992.“ForecastingtheFederalBudget
WithTime‐SeriesModels.”JournalofForecasting11,no.2:127–139.
| conditions,                  | data | quality, | institutional |     | structures, | and | forecast |     |     |     |     |     |     |     |     |
| ---------------------------- | ---- | -------- | ------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| PublicBudgeting&Finance,2025 |      |          |               |     |             |     |          |     |     |     |     |     |     |     | 15  |

Botrić, V., and M. Vizek. 2012. “Forecasting Fiscal Revenues in a Favero, C. A., and M. Marcellino. 2005. “Modelling and Forecasting
TransitionCountry:TheCaseofCroatia.”ZagrebInternationalReview FiscalVariablesfortheEuroArea.”OxfordBulletinofEconomicsand
ofEconomics&Business15,no.1:23–36. Statistics67,no.1:755–783.
Bretschneider,S.I.,W.L.Gorr,G.Grizzle,andE.Klay.1989.“Politicaland Fedotov,D.Y.2017.“ForecastingofRegionalEconomicDevelopment
Organizational Influences on the Accuracy of Forecasting State Govern- and Budget Based on the Example of Irkutsk Oblast.” Studies on
mentRevenues.”InternationalJournalofForecasting5,no.3:307–319. RussianEconomicDevelopment28,no.4:416–422.
Bretschneider,S.,andW.Gorr.1992.“Economic,Organizational,and Frank, H. A. 1990. “Municipal Revenue Forecasting With Time. Series
PoliticalInfluencesonBiasesinForecastingStateSalesTaxReceipts.” Models:AFloridaCaseStudy.”AmericanReviewofPublicAdministration
InternationalJournalofForecasting7,no.4:457–466. 20,no.1:45–59.
Buxton,E.K.,A.K.Kenneth,M.Cremeens,andK.Jay.2019.“AnAuto Frank, H. A., and A. G. Gerasimos. 1990. “Raising the Bridge Using
RegressiveDeepLearningModelforSalesTaxForecastingFromMul- Time Series Forecasting Models.” Public Productivity & Management
tiple Short Time Series.” In 18th IEEE International Conference on Review14,no.2:171–188.
MachineLearningandApplications,1359–1364.IEEE.
Frank, H. A., and X. H. Wang. 1994. “Judgmental vs. Time Series Vs.
Campbell, J. E., M. E. Ogunsanya, N. Holmes, T. VanWagoner, and DeterministicModelsinLocalRevenueForecasting:AFloridaCaseStudy.”
J.James.2024.“BibliometricandSocialNetworkAnalysisofaClinical JournalofPublicBudgeting,Accounting&FinancialManagement6,no.4:
and Translational Resource Awardee: An Oklahoma Experience 493–517.
2014–2021.”JournalofClinicalandTranslationalScience8:e10.
Fullerton, T. M. 1989. “A Composite Approach to Forecasting State
Castelino,M.S.,R.C.B.Belluzzo,J.P.Albino,andV.C.P.N.Valente. Government Revenues: Case Study of the Idaho Sales Tax.”
2024.“BibliometricAnalysis:LiteratureReviewandProposalofaMeth- InternationalJournalofForecasting5,no.3:373–380.
odologicalFrameworkin12Steps.”RevistaAracê6,no.4:13421–13446.
Ghysels,E.,andN.Ozkan.2015.“Real‐TimeForecastingoftheUSFederal
https://doi.org/10.56238/arev6n4-146.
Government Budget: A Simple Mixed Frequency Data Regression
Chatagny, F., and N. C. Soguel. 2012. “The Effect of Tax Revenue Approach.”InternationalJournalofForecasting31,no.4:1009–1020.
BudgetingErrorsonFiscalBalance:EvidenceFromtheSwissCantons.”
Ghysels, E., and N. Ozkan. Real‐Time Predictions of the U.S. Federal InternationalTaxandPublicFinance19:319–337.
Government Budget: Expenditures, Revenues and Deficits. UNC
Chimilila, C. 2017. “Forecasting Tax Revenue and Its Volatility in Kenan‐FlaglerResearchPaper,2012.
Tanzania.”AfricanJournalofEconomicReview5,no.1:84–109. Ghysels,E., F.Grigoris, and N.Özkan. 2022.“Real‐Time Forecastsof
Chung, I. H., B. Kara, M. McShea, R. Pathak, and D. Williams. 2025. State and Local Government Budgets With an Application to the
“Using Large Language Models to Forecast Local Government Reve- COVID‐19Pandemic.”NationalTaxJournal75,no.4:731–763.
nue.”PublicFinanceJournal2,no.2:85–98.
Gianakis, G.A., and A. F. Howard. 1993. “Implementing Time Series
Chung,I.H.,W.W.Daniel,andM.R.Do.2022.“ForBetterorWorse? Forecasting Models: Considerations for Local Governments.” State &
Revenue Forecasting With Machine Learning Approaches.” Public LocalGovernmentReview25,no.2:130–144.
Performance&ManagementReview45,no.5:1133–1154.
Grizzle, G., and W. E. Klay. 1994. “Forecasting State Sales Tax Reve-
Cirincione,C.,G.A.Gurrieri,andB. vandeSande.1999.“Municipal nues: Comparing the Accuracy of Different Methods.” State & Local
GovernmentRevenueForecasting:IssuesofMethodandData.”Public GovernmentReview26,no.3:142–152.
Budgeting&Finance19,no.1:26–46.
Hájek, P., and V. Olej. 2010. “Municipal Revenue Prediction by En-
Cooke,S.,andC.McIntosh.2011.“ForecastingGeneralFundRevenue:An sembles of Neural Networks and Support Vector Machines.” WSEAS
AnalysisofIdahoFY1998toFY2011.”PublicBudgeting&Finance31,no.4: TransactionsonComputers9,no.11:1255–1264.
51–73.
Jena, P. R. 2006. “Fiscal Marksmanship: Link Between Forecasting
Cooksey, R. W. 2020. Descriptive Statistics for Summarising Data. Central Tax Revenues and State Fiscal Management.” Economic and
SpringerSingapore. PoliticalWeekly41,no.37:3971–3976.
Corvalão,E.,R.W.Daniel,Samohyl,andG.H.Brasil.2010.“Forecastingthe Khan,T.,AnwarHussain,andZ.K.M.2018.“FiscalMarksmanshipin
Collection of the State Value Added Tax (ICMS) in Santa Catarina: The Pakistan: With Special Focus on Province Khyber Pakhtunkhwa.”
GeneraltoSpecificApproachinRegressionAnalysis.”BrazilianJournalof PakistanJournalofEconomicStudies1,no.1:21–43.
Operations&ProductionManagement7,no.1:105–121.
Koirala,T.P.2012.“GovernmentRevenueForecastinginNepal.”NRB
Damane,M.2020.“ForecastingtheGovernmentofLesotho'sBudget:An EconomicReview24,no.2:47–60.
AR‐MIDAS Approach.” African Journal of Economic and Sustainable
Kong,D.2007.“LocalGovernmentRevenueForecasting:TheCalifornia
Development7,no.3:256–285.
County Experience.” Journal of Public Budgeting, Accounting &
Danninger,S.2005.“RevenueForecastsasPerformanceTargets.”IMF FinancialManagement19,no.2:178–199.
WorkingPaper,1–20.https://doi.org/10.5089/9781451860337.001.
Krause,G.A.,andJ.K.Corder.2007.“ExplainingBureaucraticOptimism:
Derrick,R.A.2002.BetterRevenueForecasting:IsFiscalStressaStim- Theoryand EvidenceFromU.S.Executive AgencyMacroeconomic Fore-
ulant? A Look at Nevada Local Governments. UNLV Theses, Disserta- casts.”AmericanPoliticalScienceReview101,no.1:129–142.
tions,ProfessionalPapers,andCapstones.
Krol,R. 2010.ForecastingState TaxRevenue:ABayesianVectorAuto-
Downs,G.W.,andD.M.Rocke.1983.“MunicipalBudgetForecastingWith regression Approach, 1–18. California State University, Department of
MultivariateARMAModels.”JournalofForecasting2,no.4:377–387. Economics.
Duncan,G.,W.Gorr,andJ.Szczypula.1993.“BayesianForecastingfor Lahiri, K., and C. Yang. 2022. “Boosting Tax Revenues With Mixed‐
Seemingly Unrelated Time Series: Application to Local Government FrequencyDataintheAftermathofCovid‐19:TheCaseofNewYork.”
RevenueForecasting.”ManagementScience39,no.3:275–293. InternationalJournalofForecasting38,no.2:545–566.
Erdoğdu, H., and R. Yorulmaz. 2019. “Comparison of Tax Revenue Larson,S.,andM.Overton.2024.“ModelingApproachMatters,ButNotas
Forecasting Models for Turkey.” In 34. International Public Finance MuchasPreprocessing:ComparisonofMachineLearningandTraditional
Conference,482–492. RevenueForecastingTechniques.”PublicFinanceJournal1,no.1:29–48.
16 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Larson,S.,andM.Overton.2025.“IsThereaGoldStandardorNeedfor Otrok,C.,andH.W.Charles.1997.“WhatToDoWhentheCrystalBall
a City‐Centric Approach for Sales Tax Revenue Forecasting.” Public Is Cloudy: Conditional and Unconditional Forecasting in Iowa.”
FinanceJournal2,no.2:99–120.https://doi.org/10.59469/pfj.2025.45. Proceedings.AnnualConferenceonTaxationandMinutesoftheAnnual
MeetingoftheNationalTaxAssociation90:326–334.
Leal,T.,J.J.Pérez,M.Tujula,andJ.P.Vidal.2008.“FiscalForecasting:
LessonsFromtheLiteratureandChallenges.”FiscalStudies29,no.3: Passas,I.2024.“BibliometricAnalysis:TheMainSteps.”Encyclopedia
347–386. 4:1014–1025.
Li‐xia, L., Z. Yi‐Qi, and X. Liu. 2011. “Tax Forecasting Theory and Pedregal, D. J., and J. J. Pérez. 2010. “Should Quarterly Government
Model Based on SVM Optimized by PSO.” Expert Systems With Finance Statistics Be Used for Fiscal Surveillance in Europe?”
Applications38,no.1:116–120. InternationalJournalofForecasting26,no.4:794–807.
Li,W.,Q.Xie,J.Ao,etal.2025.“SystematicReview:AScientometric Pérez,J.J.2007.“LeadingIndicatorsforEuroAreaGovernmentDefi-
Analysis of the Status, Trends and Challenges in the Application of cits.”InternationalJournalofForecasting23,no.2:259–275.
DigitalTechnologytoCulturalHeritageConservation(2019–2024).”npj
Rudzkis, R., and E. Mačiulaitytė. 2007. “Econometrical Modelling of
HeritageScience13.https://doi.org/10.1038/s40494-025-01636-8.
Profit Tax Revenue.” Nonlinear Analysis: Modelling and Control 12,
Litterman, R. B., and M. S. Thomas. 1983. “Using Vector Autoregres- no.1:95–112.
sions to Measure the Uncertainty in Minnesota's Revenue Forecasts.”
Sabaj, E., and M. Kahveci. 2018. Forecasting Tax Revenues in an FederalReserveBankofMinneapolisQuarterlyReview7,no.2:10–22.
EmergingEconomy:TheCaseofAlbania.UniversityLibraryofMunich
Liu, D., Rufei Zhang, and Jaun Li. 2011. “Tax Revenue Combination MPRAPaper84404.
Forecast of Hebei Province Based on the IOWA Operator.” In Fourth
Schroeder,L.2007.“ForecastingLocalRevenuesandExpenditures.”In
International Joint Conference on Computational Sciences and Optimi-
LocalBudgeting,editedbyAnwarShah,53–79.WorldBank.
zation,516–519.IEEE.
Şengüler,H.,andB.Kara.2025.“ForecastingtheInflationforBudget
Lu, S., Zhong‐jian Cai, and X.‐bin Zhang. 2009. “Application of GA‐ Forecasters: An Analysis of ANN Model Performance in Türkiye.”
SVM Time Series Prediction in Tax Forecasting.” In 2nd IEEE Inter-
EkonomiPolitikaveFinansArastirmalariDergisi10,no.1:58–91.
nationalConferenceonComputerScienceandInformationTechnology,
34–36.IEEE. Sexton, T. A. 1987. “Forecasting Property Taxes: A Comparison and
EvaluationofMethods.”NationalTaxJournal40,no.1:47–59. M.Khalifa,H.,S.I.al‐Said,andS.AboulFotouhSaleh.2024.“ASmart
Approach For Budget Deficits Prediction Under Economic Shocks.” Shahnazarian,H.,MartinSolberger,andE.Spanberg.2017.“Forecast-
InternationalJournalofAccountingandManagementSciences3,no.3: ingandAnalyzingCorporateTaxRevenuesinSwedenUsingBayesian
276–308. VARModels.”FinnishEconomicPapers28,no.1:50–74.
Makananisa, M. P., and J. L. Erero. 2018. “Predicting South African Silvestrini,A.,M.Salto,L.Moulin,andD.Veredas.2008.“Monitoring
Personal Income Tax—Using Holt–Winters and SARIMA.” Journal of and Forecasting Annual Public Deficit Every Month: The Case of
EconomicsandManagement31,no.1:24–49. France.”EmpiricalEconomics34:493–524.
McDonald,B.,S.Larson,C.Maher,etal.2024.“EstablishinganAgenda Srinivasan, S., and P. Misra. 2020. “Grants From Centre and States'
forPublicBudgetingandFinanceResearch.”PublicFinanceJournal1, FiscalMarksmanship.”IndianPublicPolicyReview2,no.1:65–83.
no.1:9–28.
Steinnes, D.,and S. Wong. ForecastingState TaxRevenues: ASimple
McNab, R.,M. Rider, and K. Wall. AreErrors in OfficialU.S. Budget Alternative. Working Paper No. 85‐16, Bureau of Business and Eco-
ReceiptsForecastsJustNoise?AndrewYoungSchoolofPolicyStudies nomicResearch,1985.
ResearchPaperNo.07‐22,2005.
Streimikiene,D.,R.RaheemAhmed,J.Vveinhardt,S.P.Ghauri,and
McShea, M., and J. Cordes. 2019. “Forecasting Post‐Crisis Virginia Tax S. Zahid. 2018. “Forecasting Tax Revenues Using Time Series
Revenue.”InThePalgraveHandbookofGovernmentBudgetForecasting, Techniques—A Case of Pakistan.” Economic Research‐Ekonomska
byDanielWilliamsandThadCalabrese,177–200.PalgraveMacmillan. Istraživanja31,no.1:722–754.
Molapo,M. A.,J. O.Olaomi, and N.O. Ama. 2019.“BayesianVector Thayyib, P. V., Muhammed Navas Thorakkattle, F. Usmani,
Auto‐Regression Method as an Alternative Technique for Forecasting A.T.Yahya,andN.H.S.Farhan.2023.“ForecastingIndianGoodsand
SouthAfricanTaxRevenue.”SouthernAfricanBusinessReview23:1–28. ServicesTaxRevenueUsingTBATS,ETS,NeuralNetworks,andHybrid
TimeSeriesModels.”CogentEconomics&Finance11,no.2:1–23.
Mukherjee, S., and R. Bhattacharya. 2023. “Revenue Forecasting of
Corporate Income Tax (CIT) in India.” Indian Economic Review 58: Ticona,W.,K.Figueiredo,andM.Vellasco.2017.“HybridModelBased
329–349. on Genetic Algorithms and Neural Networks to Forecast Tax Collec-
Nandi,B.K.,MuntasirChaudhury,andG.Q.Hasan.2015.“Univariate tion.” In XXIV International Conference on Electronics, Electrical En-
gineeringandComputing(INTERCON),1–4.IEEE.
TimeSeriesForecasting:AStudyofMonthly TaxRevenueofBangla-
desh.”EastWestJournalofBusinessandSocialStudies4:1–28. Ünsal,H., A. Çalişkan, DenizKoçak, and YasinErtürk. 2020. “Kamu
Mali
̇
Yönetim
̇
i
̇ KapsamindaçokDeğiş̇
kenli
̇
gri
̇
Tahmin
̇
Modeli
̇
il
̇
eVergi
̇
Nazmi, N., and H. L. Jane. Forecasting State Income Tax Receipts: A Gelir ̇ leri ̇ Tahmin ̇ i. ̇” Mehmet Akif Ersoy Üniversitesi İktisadi ve İdari
TimeSeriesApproach.BEBRFacultyWorkingPaperNo.1105,1985.
BilimlerFakültesiDergisi7,ÖzelSayı:1104–1120.
Nazmi, N., and J. H. Leuthold. 1988. “Forecasting Economic Time
Series That Require a Power Transformation: Case of State Tax
Voorhees,W.R.2006.“NeuralNetworksandRevenueForecasting:A
Receipts.”JournalofForecasting7,no.3:173–184. Smarter Forecast?” International Journal of Public Policy 1, no. 4:
379–388.
Ofori,M.S.,AbelFumey,andE.Nketiah‐Amponsah.2020.“Forecast-
ing Value Added Tax Revenue in Ghana.” Journal of Economics and Willoughby, K., and H. Guo. 2008. “The State of the Art: Revenue
FinancialAnalysis4,no.2:63–99. Forecasting in US State Governments.” In Government Budget Fore-
casting:TheoryandPractice,editedbyJinpingSunandThomasLynch, Onorante, L., D. J. Pedregal, J. J. Pérez, and S. Signorini. 2010. “The 27–42.Taylor&FrancisGroup.
UsefulnessofInfra‐AnnualGovernmentCashBudgetaryDataforFiscal
Forecasting in the Euro Area.” Journal of Policy Modeling 32, no. 1: Wong(Jeffrey),C.H.,andN.La.2024.“ApplyingMachineLearningin
98–119. TaxRevenueForecasting.”Victoria'sEconomicBulletin8,no.2:1–12.
PublicBudgeting&Finance,2025 17
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by
Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

Xie,H.2024.“ResearchontheModelsforForecastofTaxRevenueof
Wenzhou City.” Highlights in Science, Engineering and Technology 88:
1043–1049.
Yang,C.H.,T.Molefyane,andY.D.Lin.2023.“TheForecastingofa
LeadingCountry'sGovernmentExpenditureUsingaRecurrentNeural
NetworkWithaGatedRecurrentUnit.”Mathematics11,no.14:3085.
Yılmaz, E. 2019. “Vergi Gelirlerinin Tahminlenmesine Yönelik Eko-
nometrikModel.”VergiDünyası38,no.449:38–47.
Zakaria, M., and S. Ali. 2010. “Fiscal Marksmanship in Pakistan.”
LahoreJournalofEconomics15,no.2:113–133.
Zhang, Y. 2014. “Research on the Model of Tax Revenue Forecast of
Jilin Province Based on Gray Correlation Analysis.” In Sixth Interna-
tional Conference on Intelligent Human‐Machine Systems and Cyber-
netics,30–33.IEEE.
Zhijun, Y. 2013. “RBF Neural Networks Optimization Algorithm and
Application on Tax Forecasting.” Indonesian Journal of Electrical
Engineering11,no.7:3491–3497.
18 PublicBudgeting&Finance,2025
15405850,
0, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/pbaf.70008
by Berat
Kara
- Istanbul
Medeniyet
University
, Wiley
Online
Library
on
[27/11/2025].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License