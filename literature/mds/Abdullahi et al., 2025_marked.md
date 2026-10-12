---
conversion_metadata:
  converted_at: "2026-10-12T07:07:11Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Abdullahi et al., 2025.pdf"
  source_pdf_sha256: "1945bea2daf6675092ab0fe40aa56835d7f87f1b09b4f4a21abb089117f94633"
  page_count: 31
  markdown_char_count: 176178
---

Received23June2025,accepted2July2025,dateofpublication10July2025,dateofcurrentversion16July2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3587231
A Systematic Literature Review of Concept Drift
Mitigation in Time-Series Applications
MUJAHEEDABDULLAHI 1,(GraduateStudentMember,IEEE),
HITHAMALHUSSIAN 1,2,(SeniorMember,IEEE),NORSHAKIRAHAZIZ 1,3,
SAIDJADIDABDULKADIR 1,2,(SeniorMember,IEEE),YAHIABAASHAR 4,
ABDUSSALAMAHMEDALASHHAB5,
ANDAFROZAAFRIN 1,(GraduateStudentMember,IEEE)
1DepartmentofComputing,UniversitiTeknologiPETRONAS,SeriIskandar32610,Malaysia
2CentreforResearchinDataScience(CeRDaS),UniversitiTeknologiPETRONAS,SeriIskandar32610,Malaysia
3CentreforCyber-PhysicalSystems(C2PS),UniversitiTeknologiPETRONAS,SeriIskandar32610,Malaysia
4FacultyofComputingandInformatics,UniversitiMalaysiaSabah,Labuan87000,Malaysia
5DepartmentofComputerScience,AlasmaryaIslamicUniversity,Zliten,Libya
Correspondingauthor:MujaheedAbdullahi(abdullahi_18001208@utp.edu.my)
ThisworkwassupportedinpartbytheUniversitiTeknologiPETRONASunderGrantYUTP-FRG(015LC0-487).
ABSTRACT Machine Learning (ML) plays a key role in time-series applications because it analyzes
observed data and predicts future values. The effectiveness of ML models in time-series forecasting is
reducedbytheoccurrenceofConceptDrift(CD).CDreferstocontinuouschangesinthestatisticalproperties
ofdatasets.ThisaffectsthepredictiveperformanceofMLmodels.Toaddressthisissue,researchershave
developed several CD detection and adaptation techniques. However, certain limitations exist, and most
studies on CD detection and adaptation in time-series data have focused on classification learning, with
minimalattentionpaidtoregressionlearning.ThisstudyconductedaSystematicLiteratureReview(SLR)
that classified, identified, and recommended an optimal method for the detection and adaptation of CD
inregressionandclassificationtasksinvolvingtime-seriesdata.Asystematicsearchwasperformedusing
the SCOPUS, ScienceDirect, IEEE Xplore, Web of Science, MDPI, and ACM databases. Based on the
identified records, 60 studies published between 2013 and 2024 were thoroughly surveyed and evaluated
using PRISMA guidelines. The findings show that Support Vector Machines (SVM) is the most effective
learningalgorithmsforthedetectionandadaptationofCDinregressionandclassificationtasksusingtime-
series data. This is possible because of their high detection accuracy and effective memory. Moreover,
this SLR presents a roadmap for detecting CDs using Artificial Intelligence (AI)-based learners, along
with a comparative analysis of well-known baseline methods. Future work should focus on developing
adaptivelearningmodelscapableofadaptingtoCDwithoutexplicitre-training,thereby,ensuringoptimal
performance.
INDEX TERMS Systematic literature review, concept drift, time series, data stream, regression,
nonstationaryenvironment,machinelearning.
I. INTRODUCTION consumption, have increased in popularity in recent
In real-world applications, time-series data represent any decades [1]. Additionally, time-series data are used for
set of recorded observations. Significant applications analyses in various domains such as financial variables,
of time-series data in various fields, such as energy astronomy, energy, and weather forecasting [2]. Recent
technologicaladvancementshaveledtosignificantprogress
The associate editor coordinating the review of this manuscript and in data collection, facilitating the accumulation of large
approvingitforpublicationwasChaoTong . amountsoftime-seriesdataovertime[3].Thephenomenon
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
119380 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
known as Concept Drift (CD) signifies a change in the approaches based on accuracy, adaptability, and compu-
relationship between input data and model target values. tational efficiency was conducted by synthesizing recent
CD continuously changes the statistical properties of a developments and identifying research gaps. Additionally,
datasetovertime,whichaffectstheperformanceofMachine the SLR posed and answered four research questions
Learning (ML) models, particularly after deployment. For based on existing empirical studies on drift detection and
example, a comparative analysis of an artificial time-series adaptation. To the best of our knowledge, this is one of
with a simulated CD problem demonstrated the presence the first comprehensive SLR to investigate the detection
of changing data over time. Three artificial time-series and adaptation of CD in regression and classification tasks
exhibiting CD were generated by combining data from two involvingtime-seriesapplications.
autoregressive (AR) processes. Each generated time-series The main contributions of this study are twofold: First,
had 20,000 instances, with CD occurring at 10,001 [4]. it provides a comprehensive review of the most effective
In addition, CD occurs when a target concept encounters learning algorithms for detection and adaptation to CD in
changesinanonstationaryenvironment[5].TheCDproblem regression and classification tasks using time-series data.
can reduce the efficacy of ML models trained using these ManysurveysandreviewershaveaddressedtheissueofCD
data. Therefore, consistent monitoring of ML applications in ML classification learning tasks; however, this remains a
throughout the development lifecycle is essential to address challenge. This study investigated the CD problem for both
systematicfluctuationsinthedatadistribution. classificationandregressionlearningtasksusingtime-series
DetectingCDintime-seriesdataensuresthereliabilityof data. Second, this study provides a roadmap for detecting
thepredictivemodelindynamiccontexts.Varioustechniques CDusingAI-basedlearners,thelimitationsofthestudy,and
potentialfuturerecommendations.
| such as ML, | statistical |      | methods, | and      | adaptive | combination |        |     |     |     |     |     |     |     |     |
| ----------- | ----------- | ---- | -------- | -------- | -------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| ensemble    | learning    | have | been     | proposed | to       | address     | the CD |     |     |     |     |     |     |     |     |
problem[6],[7],[8].Forinstance,inthehealthfield,aML A. CONCEPTDRIFTOVERVIEW
model has been used to evaluate the impact of data drift This section provides a background on CD mitigation,
on clinical sepsis prediction, emphasizing the necessity of including methods for time-series applications. As CD
|     |     |     |     |     |     |     |     | continuously | changes |     | the statistical |     | properties | of  | a dataset |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | --------------- | --- | ---------- | --- | --------- |
continuousmodelmonitoringandupdatingtomaintainpre-
dictive accuracy [9]. In addition, a transfer learning method over time, it deteriorates ML performance. In addition,
hasbeenusedtoaddresstemporalperformancedriftovertime changes in the statistical properties of the data CD or the
inclinicalpredictionmodels[10].Asimilarstudyproposed relationships between target variables during training and
a hybrid early drift detection method (HEDDM) that uses testing(datashift)affecttheMLmodels.CDcanbeclassified
|             |          |              |     |     |             |        |     | according | to their | speed | as  | incremental, |     | gradual, | sudden, |
| ----------- | -------- | ------------ | --- | --- | ----------- | ------ | --- | --------- | -------- | ----- | --- | ------------ | --- | -------- | ------- |
| statistical | distance | measurements |     | to  | efficiently | detect | CD. |           |          |       |     |              |     |          |         |
In addition, it improves the accuracy of drift detection in orrecurring(Figure1).AnincrementalCDoccurswhenthere
data streams [11]. However, several adaptive combinations is a minimal change in the original data distribution, and a
gradualCDoccurswhentherearenoticeablechangesinthe
| and ensemble-based |     | learning |     | algorithms | have | demonstrated |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the ability to detect CD in multiple domains. An adaptive target data distribution. Sudden CD refers to a significant
|          |          |        |     |           |     |            |     | change in | the original |     | data | distribution | at  | a specific | time |
| -------- | -------- | ------ | --- | --------- | --- | ---------- | --- | --------- | ------------ | --- | ---- | ------------ | --- | ---------- | ---- |
| ensemble | learning | method | was | presented |     | to address | CD  |           |              |     |      |              |     |            |      |
detection, thereby improving the performance of intrusion point,whereasrecurrentCDreferstoasituationinwhichan
detectionsystemsindynamicnetworkenvironments[12]. oldconceptreappearsafteraperiodofabsence.Anidentical
|         |       |               |     |          |     |         |       | concept | called | dataset | shift | in the | context | of time-series |     |
| ------- | ----- | ------------- | --- | -------- | --- | ------- | ----- | ------- | ------ | ------- | ----- | ------ | ------- | -------------- | --- |
| Despite | these | advancements, |     | previous |     | studies | on CD |         |        |         |       |        |         |                |     |
detection and adaptation have several limitations. Studies data represents any change in the joint distribution of input
|                |     |         |     |                |     |           |      | and target | variables | between |     | the training | and | testing | stages. |
| -------------- | --- | ------- | --- | -------------- | --- | --------- | ---- | ---------- | --------- | ------- | --- | ------------ | --- | ------- | ------- |
| have primarily |     | focused | on  | classification |     | learning, | with |            |           |         |     |              |     |         |         |
minimal attention paid to regression learning tasks. Several Dataset shifts encompass several types including concepts,
issuesremainintheefficientidentificationofchangesindata covariates, and prior probability shifts. The key difference
betweenCDanddatasetshiftisthatCDisinherentlydynamic
| distribution | features | and | responses |     | to CD | in a time-series |     |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------- | --- | ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
context in the contemporary literature. Additionally, the and refers to real-time changes in the data distribution.
evaluation metric performance for the validation of CD in In contrast,a datasetshift frequentlyrefers todiscrepancies
ML models using benchmark datasets may not accurately that exist between different datasets, such as training or
reflectreal-worldindustrialdata.Determininganappropriate testing, but does not always imply time evolution [13]. The
combinedCDanddatasetshiftproblemsignificantlyaffects
| CD detection | technique |     | for various |     | datasets | is challenging. |     |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ----------- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Addressing these limitations can enhance ML performance theMLdevelopmentlifecycle.
andcomputationalefficiency. In addition, time-series intelligent application integrity
This study systematically examined state-of-the-art CD relies on the ML development life cycle, where the phe-
detectiontechniquesintime-seriesapplications,highlighting nomenon ‘CD’ interrupts the process by changing the data
distribution,whichleadstoadecreaseinmodelperformance.
theirstrengthsandtheirlimitations.TheSLRbeganwithan
in-depth investigation of the issue of CD in a time-series This has attracted the attention of many researchers who
context for both ML classification and regression learning have developed methods to address CD problems in time-
algorithms. A comparative review of existing CD detection seriesdata[15],[16],[17].Severalstudieshaveinvestigated
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 119381 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
|     |     |     |     |     |     |     | predictive | maintenance |     | tasks, such | as  | autonomous | vehicles |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----------- | --- | ---------- | -------- | --- |
andrecommendationsystems,inwhichadaptingtoevolving
datadistributionsiscritical.Theseapproachesmaintainaset
ofcompetingmodels,allowingdynamicselectionofthemost
relevanthypothesisbasedonthecurrentinput.Thisstrategy
|     |     |     |     |     |     |     | is particularly   | important    |           | in areas      | such  | as fraud  | detection     |        |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | --------- | ------------- | ----- | --------- | ------------- | ------ |
|     |     |     |     |     |     |     | and healthcare    | diagnostics, |           | where         | both  | gradual   | and           | sudden |
|     |     |     |     |     |     |     | changes require   | strong       |           | and adaptable |       | detection | methods       | to     |
|     |     |     |     |     |     |     | ensure predictive |              | accuracy. | This          | study | aimed     | to identify   | the    |
|     |     |     |     |     |     |     | most efficient    | method       |           | for detecting |       | CD in     | a time-series |        |
setting.DuetotheCDissue,ithasbeenincreasinglydifficult
topredicttime-seriesusingMLoutputsaftertrainingthedata.
|     |     |     |     |     |     |     | However, | the effectiveness |     | of  | models | trained | on historical |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | --- | ------ | ------- | ------------- | --- |
datacandecreaseovertimeowingtothesechanges.
Bayrametal.[14]conductedacomprehensiveanalysisand
FIGURE1. Conceptdrifttypesbasedonspeed[14].
|     |     |     |     |     |     |     | categorization | of       | performance-based |         | CD    | detection | methods  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ----------------- | ------- | ----- | --------- | -------- | --- |
|     |     |     |     |     |     |     | proposed       | over the | past              | decade. | These | methods   | leverage | the |
declineinperformanceofthepredictivemodelasanindicator
CD using time-series data and workable solutions. Uchitel- of significant system alterations. The authors also used a
evaetal.[18],forexample,introducedanewapproachthat hierarchical diagram to present a systematic organization
issensitivetodriftformodelingmultivariatetime-seriesdata
|     |     |     |     |     |     |     | of the classification, |     | facilitating |     | a structured |     | and coherent |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------------ | --- | ------------ | --- | ------------ | --- |
innonstationaryenvironmentsofIndustrialInternetofThings navigation among various methods. A similar study by
(IIoT).Thethree-layered,three-state(TriLS)systemenables
Shenetal.[19]presentedacomprehensivesurveyofcurrent
collaboration between the gateway and cloud to adjust the unsupervisedCDdetectionmethods.Additionally,thisstudy
lightweightpredictivemodelintime. provides a thorough overview and innovative taxonomy of
| This SLR | consists | of  | eight | sections | and is organized | as  |     |     |     |     |     |     |     |     |
| -------- | -------- | --- | ----- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
unsupervisedCDdetectionapproachesforrealapplications,
follows: Section I provides an introduction and background highlighting their effectiveness in identifying appropriate
| on CD mitigation, |     | including |     | its methods | in time-series |     |              |        |     |      |          |      |                |     |
| ----------------- | --- | --------- | --- | ----------- | -------------- | --- | ------------ | ------ | --- | ---- | -------- | ---- | -------------- | --- |
|                   |     |           |     |             |                |     | model update | timing |     | amid | evolving | data | distributions; |     |
applications. Section II presents a comprehensive review of however, it lacks an empirical evaluation. Han et al. [20]
theliteratureon CDdetectionmethods.SectionIIIpresents presented a survey that introduced the concept of CD to
| the survey | methodology |     | based | on the | Preferred Reporting |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nonstationarydatastreams.CDposessignificantchallenges
ItemsforSystematicReviewsandMeta-Analyses(PRISMA) invariousdomainssuchasdataminingandML.Thisstudy
| guidelines. | Section | IV  | presents | the results, | including | an  |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | -------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
introducesanovelapproachtoclassifyingthesemethodsand
in-depth summary of screening and search procedures. providesacomprehensiveexplanationofthecurrentmethods
Section V presents the major SLR findings based on the formanagingCD,includingbothactiveandpassivemethods.
| research | questions. | Section | VI  | presents | a taxonomy | that |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------- | --- | -------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Gemaqueetal.[21]investigatedvarioustechniquestohandle
provides a brief overview of advances in the handling, CD in unsupervised classification tasks. An additional con-
| experimental | evaluation, |     | and comparative |     | analysis | of CD. |     |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | --------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tributionistheproposalofataxonomythatcategorizesstate-
| Section | VII discusses |     | the study | findings. | Section | VIII |            |              |     |            |          |     |              |     |
| ------- | ------------- | --- | --------- | --------- | ------- | ---- | ---------- | ------------ | --- | ---------- | -------- | --- | ------------ | --- |
|         |               |     |           |           |         |      | of-the-art | CD detection |     | approaches | focusing |     | specifically | on  |
presents summary of lessons learned and best practices. unsupervisedstrategies.Theauthorsalsoconductedasurvey
SectionIX.presentsconclusions,limitations,anddirections
andanalysisofvariousapproachestoCD.Nayaketal.[22]
forfutureresearch. presented an overview of the research field of CD and a
|     |     |     |     |     |     |     | comprehensive | review |     | of the diverse | approaches |     | employed |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | -------------- | ---------- | --- | -------- | --- |
II. RELATEDREVIEWS by researchers to address the challenges associated with
Thissectionpresentsacomprehensivereviewoftheliterature CD. In addition, it emphasizes ensemble learning, adaptive
on CD detection. Drift problems occur when a relationship windowing, and weighting techniques as essential methods
changes over time, affecting prediction accuracy. Different for sustaining model performance, despite changing data
CD methods exist, such as data distribution, performance- distributions. However, this study did not provide insights
basedmethods,andmultiplehypotheses.Forexample,data- intounsupervisedorsemi-supervisedcontexts.Anotherstudy
distribution-basedmethodsmonitorchangesinfundamental by Poenaru-Olaru et al. [23] evaluated the efficacy of
datadistribution,whichmayindicateashiftintheunderlying CD detectors in detecting temporal drift by examining the
patternsandrelationships.Thesemethodscanbeappliedto timeliness of drift reports and frequency of generated false
early financial forecasting and network intrusion detection. alarms. The authors also conducted a comparative analysis
Performance-based techniques detect CD by evaluating of the performance of prominent drift detectors, which
modelaccuracyorerrorratesovertime.Multiplehypothesis were categorized into two distinct groups: error-rate-based
methods are commonly employed in CD detection for detectorsanddata-distribution-baseddetectors.
| 119382 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE1. Comparisonwithotherstudiesinthesamedomain(✓:Yes).
In addition, this study considers studies that attempt to Taxonomic details and comparisons of existing techniques
mitigate CD problems using a substantial body of literature highlight the complexity and interdisciplinary nature of the
ondomainadaptation.Forexample,KarimianandBeigy[24] problems and provide useful guidance for researchers and
proposedamethodforaddressingCDindatastreamsusing practitioners.
a domain-adaptation technique. The authors proposed a Due to certain limitations in the existing literature, most
techniquecalledConceptDriftDomainAdaptation(CDDA), studieshavefocusedonclassificationlearningwithminimal
which effectively addresses CD using multi-source domain attention to regression learning within the context of time-
adaptation. The model efficiency was enhanced in terms of series. This review focuses on the applications of CD
executiontimeandmemoryusagebyadoptingthistechnique. detection techniques between 2013 and 2024. However,
Thesestudiesalsoincludeathoroughtheoreticalanalysisof before2013,driftdetectionwasaccomplishedusingseveral
CDDAandpresentageneralizationboundthatdemonstrates approachesandconventionalprocedures.Themethodologies
the problem of predicting the data streams. The proposed employed during this period included statistical hypothesis
method was tested using both synthetic and real-world data testing,classificationerrordistancemeasurement,Enhanced
streams. A similar study by Gama et al. [25] provided Customer Due Diligence (ECDD), and online MapReduce.
a comprehensive overview of adaptive learning methods Hoens et al. [26] provided a comprehensive overview of
for handling CD problems in dynamic data environments. variousCDdomainsin2012.Eachoftheseareasisdiscussed
Thisstudyalsocategorizedandevaluatedvariousstrategies, in detail, highlighting the difficulties involved. In 2009,
includingwindow-basedapproachesandensemblemethods, Guzella and Caminhas [27] presented a broad overview
along with their strengths and limitations. The survey is of CD detection using ML algorithms for spam filtering.
well-structured,coveringtheoreticalfoundations,evaluation In2007,Gaberetal.[28]presentedacomprehensivesurvey
methodologies,andpracticalapplicationsinvariousdomains. on CD detection and the challenges associated with the
VOLUME13,2025 119383

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
FIGURE2. Systematicliteraturereviewmappingprocess.
FIGURE3. GoogleScholarkeywordcombinationresults.
data-stream domain. Furthermore, the methodologies used methodologyofpreviousin-depthstudieswereadopted[43],
for the problem necessitate a comprehensive redesign to [44],[45].Figure2showstheSLRmappingprocessforthe
effectively tackle the challenges posed by the limited surveymethodologysectionofthisstudy,whichencompasses
resources and CD phenomenon. A summary of the addi- fourstagesinthescreeningprocess.
| tional research | related to these | domains | is presented in |     |     |     |     |     |
| --------------- | ---------------- | ------- | --------------- | --- | --- | --- | --- | --- |
Table1.
A. STAGE1:PRELIMINARYSTUDY
|     |     |     |     | This section | presents      | the preliminary | study. Consequently, |            |
| --- | --- | --- | --- | ------------ | ------------- | --------------- | -------------------- | ---------- |
|     |     |     |     | an initial   | investigation | was conducted   | to obtain            | a thorough |
III. SURVEYMETHODOLOGY
|                 |                   |               |           | understanding. | This | step motivated | the authors | to develop |
| --------------- | ----------------- | ------------- | --------- | -------------- | ---- | -------------- | ----------- | ---------- |
| This systematic | literature review | was performed | using the |                |      |                |             |            |
robustRQs,keywords,andstudyparametersforthereview.
PreferredReportingItemsforSystematicReviewsandMeta-
|                   |                |       |                 | Three tasks | were | performed during | the preliminary | stage: |
| ----------------- | -------------- | ----- | --------------- | ----------- | ---- | ---------------- | --------------- | ------ |
| Analyses (PRISMA) | 2020 statement | [40], | [41]. The study |             |      |                  |                 |        |
keywordidentification(1),researchquestion(RQ)formula-
| screening and | selection processes | followed | the standard |     |     |     |     |     |
| ------------- | ------------------- | -------- | ------------ | --- | --- | --- | --- | --- |
tion(2),andsearchcriteriaandstrategy(3).
guidelinesestablishedbyKitchenhamandCharters[42].This
reviewaimstopresentclassificationandregressionlearning
approaches while investigating the most efficient methods 1) KEYWORDIDENTIFICATION
for detecting and adapting CD in time-series and data Thesearchstrategyforkeywordidentificationwasdeveloped
streams.Toensurecomprehensivereporting,thestructureand forsixdatabasesusingthefollowingsearchterms:‘Concept
| 119384 |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------- |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE2. Formulatedresearchquestionsandmotivation.
Drift’ OR ‘CD’ AND ‘Model Degradation’ AND ‘Drift TABLE3. Inclusionandexclusioncriteria.
| Handling’ | OR  | ‘Drift Detector’ |     | AND | ‘Concept | Evaluation’ |     |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
AND‘Time-Series’OR‘Time-SeriesData’AND‘Artificial
| Intelligence’    | OR  | ‘AI’ AND | ‘Machine          |     | Learning’ | OR       | ‘ML’ |     |     |     |     |     |     |
| ---------------- | --- | -------- | ----------------- | --- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
| AND ‘Regression’ |     | AND      | ‘Classification.’ |     | These     | keywords |      |     |     |     |     |     |     |
wereselectedtorepresentCDresearch.Thisstudyconducted
| a preliminary | search | of  | the Google | Scholar |     | database | using |     |     |     |     |     |     |
| ------------- | ------ | --- | ---------- | ------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
thekeyword‘ConceptDrift’toexploretheexistingliterature
| on this topic. | Figure       | 3 shows | the     | results | based     | on different |     |     |     |     |     |     |     |
| -------------- | ------------ | ------- | ------- | ------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| keyword        | combinations |         | and the | number  | of papers | obtained     |     |     |     |     |     |     |     |
throughGoogleScholarsearch.Theinitialsearchoutputwas
reducedto5,850afterthequalityoftheretrievalresultswas
| evaluated        | using   | filtering. | In addition, | various |               | synonyms     | for    |     |     |     |     |     |     |
| ---------------- | ------- | ---------- | ------------ | ------- | ------------- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
| ‘‘Concept        | Drift’’ | were       | obtained     | from    | Lima          | et al. [34]. | All    |     |     |     |     |     |     |
| journal articles |         | published  | in English   |         | were included |              | in all |     |     |     |     |     |     |
searchescovering2013–2024intheselecteddatabases.
|     |     |     |     |     |     |     |     | AND ‘Time-series.’ |     | Figure | 4 depicts | the screening | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | --------- | ------------- | --- |
2) RESEARCHQUESTIONSFORMULATION selection process using PRISMA 2020 standards, where
Authors(M.A.andY.)B.)collaboratedtodescribetheRQs relevantpublicationswereidentified.
| and their | motivations | for | this | study based |     | on a literature |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ---- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
review. Table 2 presents the research questions and their B. STAGE2:SCREENINGPROCESS
motivations.
|     |     |     |     |     |     |     |     | The database  | search, | which   | used identified | keywords   | and    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------- | --------------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | a generalized | search  | string, | yielded         | 183 unique | papers |
3) SEARCHCRITERIAANDSTRATEGIES that were reviewed thoroughly. The screening process of
Search criteria and strategies are crucial when searching the articles was evaluated by two authors (S.J.A. and
N.A.).
| for specific | domains.    | Six     | databases | were | used    | to search | for     |     |     |     |     |     |     |
| ------------ | ----------- | ------- | --------- | ---- | ------- | --------- | ------- | --- | --- | --- | --- | --- | --- |
| selected     | literature: | SCOPUS, | Science   |      | Direct, | IEEE      | Xplore, |     |     |     |     |     |     |
WebofScience,ACMDigitalLibrary,andMDPI.Asearch 1) INCLUSIONANDEXCLUSIONCRITERIA
was conducted using titles, abstracts, and keywords to This study systematically reviewed the available literature
identifystudiesrelevanttoCD.Theselectedpublicationtypes onCDdetectionandtime-seriesdatainthefieldsofmathe-
included journals and conference proceedings published matics,computerscience,engineering,anddecisionscience.
between 2013 and 2024 covering decades. To refine the Thesearchalsoencompassedtheperiodfrom2013to2024,
search, a comprehensive search query was developed and except for articles published earlier in 2012. In addition,
used to examine the titles, abstracts, and keywords in the ratherthanbeinglimitedtoasinglenationorarea,asearch
literature.ThedomainfocusisCDthekeywordsare‘Concept was conducted worldwide. After excluding 123 articles,
drift, time-series’ the search method is ‘Title, Abstract, 60researcharticleswereselected.Thecriteriausedtoselect
Keywords’ and the search strings are ‘Concept Drift’ OR theresearcharticlesforinclusionandexclusionarepresented
| ‘CD’ AND      | ‘Model | Degradation’ |     | AND | ‘Drift | Handling’ |     | inTable3. |     |     |     |     |        |
| ------------- | ------ | ------------ | --- | --- | ------ | --------- | --- | --------- | --- | --- | --- | --- | ------ |
| VOLUME13,2025 |        |              |     |     |        |           |     |           |     |     |     |     | 119385 |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
|     | FIGURE4. | PRISMA2020flowdiagramofstudyscreeningandselection. |     |     |     |     |     |
| --- | -------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
C. STAGE3:ELIGIBILITYANDQUALITYASSESSMENT of 1 was assigned for ‘‘Yes,’’ 0.5 for ‘‘Partially’’ and 0 for
Eligibility and quality assessments were conducted using ‘‘No.’’Theeligibilityandqualityassessmentscoringcriteria
reviews and primary research. Each duplicate record was were validated based on the selected studies. The decision
|           |             |               |          | was made after | excluding studies | that failed | to meet the |
| --------- | ----------- | ------------- | -------- | -------------- | ----------------- | ----------- | ----------- |
| carefully | examined to | ensure review | quality. | In partic-     |                   |             |             |
ular, the abstracts of research articles that were part scoringcriteria;however,allstudiesthatreceivedascoreof
of the review process were thoroughly examined and 1or0.5wereincludedinthedataextractionprocessrelatedto
screened to determine their quality and significance. The theRQs.However,thiswasnotperformedcarelesslybecause
subsequent step involved in-depth evaluation of each the study followed a thorough evaluation of eligibility and
quality.Theeffectivenessoftheassessmentprovedvaluable
| research | article. Another | exclusion criterion | was | restricting |     |     |     |
| -------- | ---------------- | ------------------- | --- | ----------- | --- | --- | --- |
the articles to those published in English. Hence, eight in examining existing related studies, specifically those
articles written in languages other than English were focusingontheirobjectivesandmethodologiesformitigating
excluded. CDintime-seriesenvironments.Thisevaluationensuredthat
After screening, 60 papers were evaluated for eligibility the final selection consisted only of studies with clearly
|              |                |               |       | defined objectives, | thoroughly | explained methodologies, |     |
| ------------ | -------------- | ------------- | ----- | ------------------- | ---------- | ------------------------ | --- |
| and quality. | The evaluation | was performed | using | specific            |            |                          |     |
criteriaandcorrespondingscoringvalues(Table4).Ascore acknowledgedlimitations,andclearconclusions.
| 119386 |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | ------------- |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE4. Eligibilityandqualityassessmentscoringcriteria.
|     |     |     |     |     |     | of the data  | from                | a selected   |           | group      | of research    |             | studies, |
| --- | --- | --- | --- | --- | --- | ------------ | ------------------- | ------------ | --------- | ---------- | -------------- | ----------- | -------- |
|     |     |     |     |     |     | describing   | the characteristics |              | according |            | to publication |             | year,    |
|     |     |     |     |     |     | journal,     | problem             | scope        | of ML,    | evaluation |                | metrics,    | and      |
|     |     |     |     |     |     | learning     | algorithms.         | Furthermore, |           | this       | study          | categorized |          |
|     |     |     |     |     |     | the selected | studies             | using        | learner   |            | algorithms,    | evaluated   |          |
modelperformance,andemployedtechniquesthateffectively
addressedCD.
|     |     |     |     |     |     | A. CHARACTERISTICSOFTHESELECTEDSTUDIES |              |             |      |                 |        |                |          |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | ------------ | ----------- | ---- | --------------- | ------ | -------------- | -------- |
|     |     |     |     |     |     | Figure 5                               | presents     | the number  |      | of publications |        | on CD          | using    |
|     |     |     |     |     |     | time-series                            | applications |             | from | 2013 to         | 2024   | and highlights |          |
|     |     |     |     |     |     | the growing                            | body         | of research |      | on this         | topic. | The            | findings |
FIGURE5. Distributionofstudiesbythepublicationyear.
|     |     |     |     |     |     | indicate   | that the | number         | of published |                  | papers   | has increased |          |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | -------------- | ------------ | ---------------- | -------- | ------------- | -------- |
|     |     |     |     |     |     | over time, | with     | a particularly |              | significant      | increase |               | over the |
|     |     |     |     |     |     | last few   | decades. | Additionally,  |              | the distribution |          | of            | studies  |
D. STAGE4:DATAEXTRACTIONANDCOMPILATION showsagrowingemphasisonCDresearch,asevidencedby
| After completing | the | eligibility | and quality | assessments, |     |                 |          |     |                 |     |      |      |          |
| ---------------- | --- | ----------- | ----------- | ------------ | --- | --------------- | -------- | --- | --------------- | --- | ---- | ---- | -------- |
|                  |     |             |             |              |     | the significant | increase |     | in publications |     | from | 2021 | to 2022, |
the selected studies were entered for data extraction using with the highest number of publications occurring in 2022.
Microsoft Excel (version 16.77). The data extracted from This high number can be attributed to the concentration of
theselectedstudiesincludedthepublicationyear,algorithm
|     |     |     |     |     |     | CD issues | in response |     | to practical | challenges |     | encountered |     |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------------ | ---------- | --- | ----------- | --- |
used, metrics evaluation, domain, and ML techniques. inreal-worldapplications,especiallyinsectorswheremodel
However, data extraction was conducted by two authors reliabilityovertimeiscrucial,includingfinance,healthcare,
(S.J.A.andN.A.).
andenergy.Theresultsdemonstratetheimportanceofensur-
In addition, the extracted data included authors, title, ing the robustness and relevance of predictive ML models
| abstract, volume, | number, | pages, | publisher, | keywords, | year, |                |               |     |     |         |          |     |        |
| ----------------- | ------- | ------ | ---------- | --------- | ----- | -------------- | ------------- | --- | --- | ------- | -------- | --- | ------ |
|                   |         |        |            |           |       | in time-series | environments. |     | The | highest | temporal |     | number |
datasets, CD algorithm, evaluation metrics, problem scope, increases in 2021 and 2022 may represent advancements in
andalgorithmlearning.Finally,60studieswereincludedand CD detection and adaptation methodologies, which can be
| systematically | analyzed | to address | the RQs | of this | review. |            |             |     |     |       |              |     |          |
| -------------- | -------- | ---------- | ------- | ------- | ------- | ---------- | ----------- | --- | --- | ----- | ------------ | --- | -------- |
|                |          |            |         |         |         | attributed | to advances | in  | ML  | model | development. |     | Finally, |
ThesestudiesprovideusefulinsightsintothedetectionofCD thegrowinginterestinCDcanbeattributedtotheincreasing
intime-seriesapplications.
|     |     |     |     |     |     | complexity | of time-series |     | data          | and data | streams, | as   | well as |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------------- | -------- | -------- | ---- | ------- |
|     |     |     |     |     |     | increased  | awareness      | of  | the potential | problems |          | that | CD can  |
cause.
IV. RESULTSANDANALYSIS
Thissectionpresentsanin-depthsummaryofthefindingsof Figure6showsthedistributionofstudiesclassifiedaccord-
the screening and search procedures based on the PRISMA ing to specific journals, where (N = 46) were published
=
guidelines.First,thestudyprovidesaquantitativedescription in journals and the remaining (N 14) were published in
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 119387 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
FIGURE6. Distributionofstudiesbyjournals.
FIGURE7. Characteristicsofstudiesbasedontheproblemscopeofmachine
learning.
conferenceproceedings.JournalSource:ACMTrans.Softw. Things,JournalofArtificialIntelligenceandSoftComputing
Eng. Methodol., ACM Transactions on Intelligent Systems Research, Journal of Network and Computer Applications,
and Technology, Applied Energy, Computers & Indus- Knowledge-Based Systems, MDPI Applied Sciences, MDPI
trial Engineering, Computers and Electrical Engineering, Mathematics, MDPI Sensors, Neural Networks, Neuro-
Engineering Applications of Artificial Intelligence, Expert computing, Springer Applied Intelligence, Springer Cluster
Systems with Applications, Future Generation Computer Computing, and Springer Machine Learning. This result
Systems, IEEE Internet of Things Journal, IEEE Sensors demonstrates that the research was conducted in reputable
Journal, IEEE Systems Journal, IEEE Transactions on journals.
Cybernetics, IEEE Transactions on Industrial Informatics, In addition, the distribution of studies across journals
IEEE Transactions on Knowledge and Data Engineering, indicates that CD research is published in diverse scientific
IEEE Transactions On Neural Networks and Learning areas,withsignificantconcentrationsinthejournals‘‘Expert
Systems, Information Sciences, Intelligent Data Analysis, Systems with Applications’’ and ‘‘Information Sciences,’’
InternationalJournalofMachineLearningandCybernetics, whichhavethehighestnumberofpublications,fiveandfour,
International Journal of Medical Informatics, Internet of respectively. The selected journals also show an increasing
119388 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
FIGURE8. Characteristicsofstudiesbasedonevaluationmetrics.
FIGURE9. Characteristicsofstudiesusinglearningalgorithms.
emphasize on the practical deployments and real-world Figure 8 presents the attributes of the selected studies
challenges of CD, in which the predictive accuracy of ML based on the metrics used for model evaluation. The eval-
models suffers owing to unseen data shifts, particularly in uation metrics were accuracy, area under the curve (AUC),
time-sensitive applications such as IoT, industrial systems, receiver operating characteristic curve (AUROC), architec-
and real-time decision-making. These results indicate that turalvulnerabilityfactor(AVF),cost-benefitanalysis(CBA),
complications associated with CD detection have been confusion matrix, f1 score, geometric mean (G-Mean),
reportedinseveralstudies. meanabsoluteerror(MAE),meanabsolutepercentageerror
Figure7showsthedistributionofthescopeoftheselected (MAPE), mean absolute scaled error (MASE), Matthews
study-based problems for ML. Most studies focused on correlationcoefficient(MCC),medianabsoluteerror(MED),
classification tasks (60%), followed by time-series (12%), mean squared error (MSE), normalized root-mean-square
supervised(7%),imbalance(7%),unsupervised(6%),regres- deviation (NRMSD), precision, root cause analysis (RCA),
sion (6%), and semi-supervised (2%). This indicates that recall,rootmeansquareerror(RMSE),andreceiveroperator
researchersareinterestedinscopingMLproblemsusingclas- characteristic (ROC). The findings demonstrated that most
sificationmethods.Thisindicatesthatmostadvancementsin studiesemployedaccuracyastheprimarymeasuretoevaluate
CD detection and adaptation can be attributed to the focus theirmodels,whereasotherstudiesconcentratedonarange
onclassificationproblemswithintime-seriescontexts.Inthe of alternative metrics to evaluate CD detection models. The
future,distributionpatternscouldbeimprovedbyexpanding accuracy evaluation metric can serve as the primary means
thedetectionofCDindifferentMLcontexts. for ML models because of its easy interpretation and direct
VOLUME13,2025 119389

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE5. Abriefoverviewofstudiescategorizedbasedonclassificationlearningalgorithms.
reflection of the model’s predictive performance. In CD once (YOLO). The research findings tended to explore the
scenarios, maintaining the stability of the ML model in use of SVM-based learning algorithms for CD detection.
changingdatadistributionsisessential.Thus,accuracyserves In addition, most studies have employed SVM and LSTM
as a direct measure of a model’s ability to adapt to new models for CD detection and adaptation because of their
patterns. Future studies could benefit from deeper metric ability to handle dynamic data shifts. SVMs perform well
adoption to improve the robustness of CD detection models in high-dimensional spaces and are useful for detecting
under various drift conditions and their adaptability to real- shifts in various data distributions that are important in
worldapplications. CD scenarios. Specifically designed for sequential data,
Figure 9 presents the characteristics of the selected LSTMs can capture temporal dependencies and adapt to
studiesthatinvestigatedtheimplementationofdifferentCD gradual changes over time, which is a common feature of
algorithms. The algorithms are an artificial neural network CD in time-series data. The findings indicate that future
(ANN), autoencoder, convolutional neural network (CNN), frameworksforCDdetectionandadaptationcanincorporate
deep neural network (DNN), decision tree (DT), fully advanced ML models, particularly for complex time-series
convolutionalnetwork(FCN),GaussiannaïveBayes(GNB), data,ascomputationalefficiencyincreases.
gated recurrent unit (GRU), k-nearest neighbors (k-NNs),
logistic regression (LR), long short-term memory (LSTM), B. CLASSIFICATIONOFSELECTEDSTUDIES
multilayer perceptron (MLP), naive Bayes (NB), neural 1) SUMMARYOFSTUDIESBASEDONCLASSIFICATIONAND
networks (NN), perceptron neural network (PNN), random REGRESSIONALGORITHMSOFLEARNERS
forest (RF), regularized greedy forests (RGF), recurrent The classification of studies based on learners’ CD
neural network (RNN), support vector machine (SVM), CD-detection algorithms is presented in Table 5. The
eXtreme gradient boosting (XGBoost), and you only look table also includes datasets, descriptions of their work,
119390 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE6. Abriefoverviewofstudiescategorizedbasedonregressionlearningalgorithms.
publication years, and algorithm learners. Classification- in error rates, such as the mean squared error (MSE),
based algorithm learners play a crucial role in detecting, classificationerror,orabruptdecreasesinconfidencescores,
handling, and serving CD adaptors. Selected learners with indicate drift. Various metrics, such as accuracy, precision,
complementary characteristics, such as SVM, ANN, and recall, and F1 measure, reveal drift characteristics, such
DT, enhance drift detection capabilities. Algorithm learners as changes in specific classes or larger changes in the
are essential components of CD detection in time-series distribution. Variations in feature importance help identify
data and data streams. In addition, their ability to sense the affected features, facilitating root cause analysis. These
changes and adapt accordingly is critical for maintaining metrics also assess the efficacy of adaptation strategies,
the accuracy and reliability of the model in dynamic such as re-training and online learning, by comparing the
environments. According toa summary of previousstudies, performance before and after drift. Selecting appropriate
SVM, LSTM, k-NN, and NB algorithms are the most metrics specifically designed for a given application and
frequentlyusedtoaddressCD-relatedproblems.Inaddition, data is critical. Performance metrics serve as tools for
previous studies have combined various learner methods identifyingandaddressingCDproactively.Additionally,the
to compare their performance, leading to the development performance of the model was evaluated using appropriate
of intelligent hybrid models. Table 6 summarizes the evaluation metrics after training the ML models on various
classification of studies based on regression algorithm CD detection and adaptation datasets. For example, the
learners for CD detection. The table also includes datasets, authors who investigated class imbalance employed ACC,
descriptionsoftheirwork,publicationyears,andregression REC, PRE, and F1 to evaluate their predictive models to
algorithmlearners.Regression-basedalgorithmlearnersplay ensurethatthemodelswereeffectiveinsignificantinstances
acrucialroleindetecting,handling,andinterpretingCDby withinimbalanceddatasets.MetricssuchasMSEandMAE
predictingcontinuousvalues.Learnerswithcomplementary are employed in time-series forecasting because of their
characteristics, such as ANN, LR, RT, SVR, and MSR, accuratemeasurementoferrormagnitudeovertime.Finally,
enhance drift detection capabilities. However, regression the targeted use of evaluation metrics highlights model
algorithmlearnersareessentialcomponentsofCDdetection performance and enables meaningful comparisons between
in time-series data and data streams. In addition, their studies.
ability to sense changes and adapt accordingly is critical
for maintaining the accuracy and reliability of the model in
3) SUMMARYOFSTUDIESCLASSIFIEDBASEDONA
dynamicenvironments.
TECHNIQUETHATHANDLESCONCEPTDRIFT
2) SUMMARYOFSTUDIESCLASSIFIEDBASEDONMODEL The studies classified according to the techniques used
PERFORMANCE to handle the CD types are presented in Table 8. Most
The studies classified according to the model performance previous studies used the ADWIN, HDDM, and DDM
for CD drift detection and adaptation in a general context techniquestoovercomedriftproblems.Commondrifttypes
are listed in Table 7. Most previous studies have focused are real, incremental, gradual, sudden, and recurrent drift.
on data streaming, imbalances, and anomaly detection. However,CDcansurfaceinseveralways,includinggradual
In contrast, CD detection is based on the evaluation of shifts and sudden changes. Each of these presents specific
model performance metrics. For example, abrupt increases challenges for detection and adaptation. The summarized
VOLUME13,2025 119391

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE7. AbriefoverviewofstudiescategorizedbymodelperformanceforCDdetectionandadaptationinageneralcontext.
study technique combines the years and types of CD to theexistenceofseveralapproaches(Figure10).Inaddition,
provide a more in-depth understanding of the performance thisquestionrevealshowtheircharacteristicsaffectdetection
of algorithmic techniques for CD detection. In addition, accuracy and adaptability to other methods. CD poses a
each technique employed for the detection of various types significant challenge in time-series data analysis, rendering
of CD exhibits special qualities suited to the type of drift modelsineffectiveasunderlyingpatternschange.Ensemble-
pattern. For example, ADWIN and KSWIN dynamically basedlearningmethodshaveemergedaspromisingsolutions
changewithchanges,whichqualifiesthemaseithergradual becauseoftheirinherentdiversityandrobustness.Investigat-
or sudden shifts in data distribution. CUSUM and EWMA ingtheirefficacyandcomparingthemwithsingle-classifier
use cumulative changes or weighted averages to facilitate approachesiscriticalformakinginformeddecisions.
the rapid identification of incremental drifts. EDDM and Several ensemble-based techniques have shown potential
HDDM use statistical distance measures that effectively for detecting CD in time-series data. For example, Thalor
detect gradual drifts by tracking slow changes. Finally, this and Patil [100] proposed an ensemble-based classification
canenablefutureresearchtoaddresstheobstaclesposedby algorithm for nonstationary data streams (ENSDS) with
CDtypesinreal-worldapplicationsacrossmultipledomains an emphasis on two-class problems for the incremental
byselectingappropriatealgorithms. learning of nonstationary data streams. The authors also
foundthatENSDSoutperformedLearn++.NSEinvarious
V. MAJORFINDINGSBASEDONTHERESEARCH evaluationmetrics.Toaddresstheproblemofpatterndrifting
QUESTION inMLapplicationsundernonstationaryoperatingconditions,
A. RQ1:WHICHENSEMBLE-BASEDLEARNINGMETHODS Liu and Zio [101] presented an ensemble model based on
AREMOSTEFFECTIVEFORDETECTINGCDINTIME-SERIES a support vector regression (SVR) model with steaming
DATAUSINGCLASSIFICATIONANDREGRESSION data points. In addition, the proposed method reduces
APPROACHES? computational complexity by updating a portion of the
Toidentifyexistingensemble-basedlearningapproachesfor newly available data and enabling the timely tracking of
CDdetectionintime-seriesdata(RQ1),thisstudyconfirmed ongoing patterns using feature vector selection. According
119392 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE8. Anoverviewofstudiesiscategorizedbasedonatechniquethathandlesconceptdrift.
to Cavalcante and Oliveira [4], addressing CD in finan- Machine (ELM) with explicit drift detection and updated
cial time-series predictions improves forecasting accuracy. the decision model online when a CD occurred in the
The authors employed an ensemble Extreme Learning data. This study found that drift detection can improve the
VOLUME13,2025 119393

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE9. Summaryofensemble-basedlearningconceptdriftdetectiontechniques.
predictiontimeofonlinesequentialELMwhilemaintaining potentialpatterns.Thisleadstomorerobustandgeneralizable
accuracy. detections, especially when shifting concepts, which is
A similar study by Grim and Gradvohl [102] intro- difficult for individual models. In addition, the diversity of
duced an online sequential extreme learning machine (OS- available models was used to improve the performance of
ELM) to address the challenge of forecasting data streams each base learner with different parameter settings [104].
using CDs. The proposed method involves the creation However,dynamicadaptationplaysavitalrole;unlikestatic
of three ensembles that use the OS-ELM and employ single models, ensembles incorporate mechanisms, such as
high-performancetechniques.High-performancetechniques dynamic weighting, to prioritize base learners that perform
involve advanced computational approaches that improve well in the current concept. This enables faster adaptation
the speed and efficiency of ensembles for regression and to both gradual and abrupt drifts while maintaining pace
time-seriesforecastingusingOS-ELM.Thefindingsshowed with evolving data patterns. For example, [101] employed
that high-performance ensembles outperformed the corre- a dynamic ensemble selection strategy that was integrated
spondingserialversions.Additionally,drift-basedensemble intothemethodologytoselectthesub-modelsthatweremost
member selection using clustering (DEMSC) has been pro- relevanttothenewdatapointtoderivethepredictionwhile
posedforadaptiveselectionandacombinationoftime-series simultaneously minimizing the impact of irrelevant mod-
forecastingmodels.Thisassumptionfacilitatesthedynamic els. However, compared to other classification approaches,
selection of initial ensemble-based model candidates by ensembles frequently demonstrate superior adaptability in
implementing a performance drift detection mechanism. dynamic environments because of their inherent diversity
Additionally, a comprehensive empirical analysis of the and dynamic update mechanisms. The characteristics of
proposed method was conducted to assess both the stan- ensemble-based learning provide significant advantages in
dardization error and scalability of the proposed approach termsofdetectionaccuracyandadaptabilitywhendetecting
usingtime-seriesdatafromvariousreal-worlddomains[103]. CD in time-series datasets. The techniques for detecting
Boulegane et al. [104] reported that dynamic ensemble CDusingensemble-basedlearners(Table9).Finally,itwas
selection (DES) is a promising method for forecasting found that ensemble-based learning with classification and
time-seriesinrealtimeusingmulti-targetregression(MTR). regression approaches based on ENSDS, SVR, ELM, OS-
The authors introduced a new method to use potential ELM, DEMSC, and DES were the most commonly used
interconnectionswithinthebehavioralcharacteristicsofbase methodsfordetectingCDinatime-seriesenvironment.This
modelsusingincrementalMTRtoachieveDESandenhance could be due to their inherent diversity and effectiveness in
modelperformance. mitigatingCD.
Furthermore, several characteristics of ensemble-based
learningapproachessignificantlyaffecttheirdetectionaccu- B. RQ2:WHATARETHEVARIOUSMLMODELSUSEDINA
racyandadaptabilitytootherclassificationmethods,despite GENERALCONTEXTTODETECTCDANDHOWDOTHEY
theCDinthetime-seriesdata.Forexample,usingdiversity PERFORMINTERMSOFACTIONABILITYINDRIFT
to combine multiple base learners trained on different data DETECTIONANDADAPTATIONTASKS?
samples or algorithms, ensembles can inherently avoid Several ML models have been employed for CD detection
individual model biases and capture a broader spectrum of in time-series forecasting tasks, where each learner exhibits
119394 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
| FIGURE10. | Ensemble-basedlearnersforconceptdriftdetectionintime-seriesdata. |     |     |     |     |     |     |     |
| --------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
benefitsanddrawbacksintermsoftheiractionability.Based the authors presented a universal incremental least-squares
onthesefindings,SVM,k-NN,andLSTMhavebeenwidely support vector classifier (LS-SVC) and particle adaptive
usedbecauseoftheirefficacyindriftdetection.Inaddition, classifier (PAC) that generated a particle adaptive learning
bothMLmodelspossessspecificadvantagesinCDdetection: strategy.Realisticdatacollectedoverasingledaywasused
theSVMandk-NNmodelsarerobustagainstfeature-based tovalidatetheproposedmethod.
changes, whereas LSTM captures temporal dependencies, However, the rapid development of DL models such
making them appropriate options for various types of drifts as LSTM, ANN, and RNN models offers effective drift
in time-series applications. Learners can be classified into detection capabilities. It was found that [46], [47], [63],
supervised,unsupervised,andDLmodels. [71], [80], [81], [105] used LSTM-based learners for CD
Supervised learners are crucial for CD detection and detection, adapting, understanding, and analyzing CDs.
adaptation. For example, Tang et al. [64] used domain Moreover,toaddressCDinstreamingdata,[6]usedadeep
adaptation to decrease CD in incremental learning through neural network to propose a technique known as selective
| a method | called (incremental | support | vector machine | with |     |     |     |     |
| -------- | ------------------- | ------- | -------------- | ---- | --- | --- | --- | --- |
ensemble-basedonlineadaptive(SEOA).Theadaptivedepth
domain adaptation) which is based on SVM. The experi- unitbuildsshallowfeatureswithdeepfeaturesandadjuststhe
mentalresultsdemonstratedagreaterefficiencywhentested informationflowoftheneuralnetworkinresponsetonearby
using both real and synthetic data. Similar research by datavariationstoimprovetheconvergenceoftheonlineDL
Jain et al. [70] employed SVM classifier to detect CD in model.TheexperimentalresultsdemonstratethatSEOAcan
network anomaly detection. The model was retrained using combatCDandisgeneralizedandrobust.Table10presents
statisticaltests.TheauthorsfocusedonseveraltypesofCD, variousMLmodeltechniquesfordetectingCDinageneral
including sudden, gradual, and incremental drifts. In the context. Finally, the most frequently employed ML models
followingexperimentsonthreedatasets,namely,theTestbed for CD detection in a general context were investigated.
Dataset, NSL-KDD, and CIDDS-2017, SVM demonstrated According to these findings, SVM, k-NN, and LSTM are
better classification accuracy. Hinder et al. [66] presented widely used owing to their efficacy in drift detection. The
a novel supervised ML approach using RF, k-NN, and studyalsofoundthatotherdeepneuralnetworkmodels,such
DT as general theoretical frameworks to address the drift asSEOA,caneffectivelycombatCDinageneralcontext.
| localization | problem. | In addition, | the authors provided | a   |     |     |     |     |
| ------------ | -------- | ------------ | -------------------- | --- | --- | --- | --- | --- |
theoreticalframeworkthatrelatesprobabilisticclassification C. RQ3:WHATALGORITHMSHAVEBEENUSEDINTHE
to drift localization. The empirical results demonstrate that LASTDECADESFORANALYSINGANDHANDLINGCDIN
TIME-SERIESDATAANDDATASTREAMS?
| the proposed | method | is a promising | approach for both | drift |     |     |     |     |
| ------------ | ------ | -------------- | ----------------- | ----- | --- | --- | --- | --- |
localizationandadditionalfeaturerelevanceanalysis. ThepaperfoundthatSeveralalgorithmshavebeenproposed
|              |              |          |                 | to address | this problem. | For example, | DDM, ECDD, | and |
| ------------ | ------------ | -------- | --------------- | ---------- | ------------- | ------------ | ---------- | --- |
| In addition, | unsupervised | learning | can be employed | to         |               |              |            |     |
address drift detection challenges. For example, Kamin- ADWIN are available for handling and analyzing CD [4],
skyietal.[61]proposedanautoencoder-basedunsupervised [72]. Wang et al. [82] employed a multiscale drift detection
|                 |           |                  |           | test (MDDT) | algorithm | to identify | CD in a nonstationary |     |
| --------------- | --------- | ---------------- | --------- | ----------- | --------- | ----------- | --------------------- | --- |
| drift detection | algorithm | for multivariate | streaming | data.       |           |             |                       |     |
The proposed approach is known as the autoencoder-based time-series environment. The authors efficiently used an
concept drift detector (AECDD), which is an unsupervised archive to identify sudden changes in feature values that
drift detection model based on reconstruction that tracks requiredimmediateadaptation.Theresultsdemonstratethat
changes in data distribution using an autoencoder. AECDD theproposedmethodoutperformsothermethodsinhandling
|               |       |                |                    | abrupt shifts | and achieves | the highest | recall score | for |
| ------------- | ----- | -------------- | ------------------ | ------------- | ------------ | ----------- | ------------ | --- |
| was evaluated | using | synthetic data | designed to assess | the           |              |             |              |     |
capacity of the model to capture contextual information, identifying drift points. In a similar study conducted by
and the proposed approach demonstrated positive results. Ramanan et al. [106], the Unsupervised Temporal Drift
Huang et al. [85] introduced an innovative unsupervised Detector (UTDD) algorithm was employed to identify
adaptiveapproachthatreducesthedegradationoflong-term real-timeCDsintime-seriesdata.Thegoalofthisstudywas
|               |            |                   |                    | to detect seasonal | variation | and temporal | CD in time-series |        |
| ------------- | ---------- | ----------------- | ------------------ | ------------------ | --------- | ------------ | ----------------- | ------ |
| myoelectric   | control at | low computational | cost. In addition, |                    |           |              |                   |        |
| VOLUME13,2025 |            |                   |                    |                    |           |              |                   | 119395 |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
datawithoutgroundtruthandthenadjusttheMLmodelsto (c) Step 3. Concept drift characterization: In general,
handleCDtoimprovetheirgeneralizability. CD characterization involves determining the type of
In addition, Dehghan et al. [93] employed an NDE drift (sudden, gradual, incremental, or recurring) to
algorithm that depended on ensemble classifiers to detect select suitable mitigation methods for any scenario.
CD.Theauthors’methodanalyzessamplesindividuallyand In [109], the authors characterized their automated
tracks the distribution of the ensemble error to identify methodfordetectingCDbasedonsuddenandgradual
potential drifts. The experimental results demonstrate that drifts in business processes using execution traces.
the proposed method can effectively detect and adapt to Additionally,ananalysisofsyntheticlogsrevealedthat
several types of CDs and outperforms existing methods. the proposed approach effectively identified typical
Pesaranghader and Viktor [94] introduced the FHDDM process changes and nested compositions, surpassing
methodasameansofdetectingdriftpointsindatastreams. state-of-the-artbaselinesforsuddenandgradualdrifts.
This was achieved using a sliding window and Hoeffding (d) Step 4. Model adaptation: Adaptation of CD in a
inequality.TheexperimentalresultsverifiedthattheFHDDM generalcontextalsoinvolvesre-trainingmodelsusing
had a lower detection delay, fewer false positives, and recent data, incrementally updating them, employ-
fewer false negatives when drifts were detected. Table 11 ing ensemble methods, or using techniques such as
summarizestheexistingalgorithmsusedoverthelastdecade weighted re-training. For example, an optimized DL
to detect, handle, and analyze CD in time-series and data andadaptiveslidingwindowapproachwereemployed
streams. Finally, it was discovered that various algorithms, for the CD adaptation framework. The authors also
suchasADWIN,HDDM,andADD,havebeenusedtodetect, analyzed dynamic streaming data based on improved
handle,andanalyzeCDintime-seriesanddatastreams.
|     |     |     |     |     |     | DL       | techniques | and  | adaptive | and          | sliding | window |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | -------- | ------------ | ------- | ------ |
|     |     |     |     |     |     | methods, | which      | work | well     | with limited | memory  | and    |
time[110].
D. RQ4:WHATARETHEMAINSTEPSTOADDRESS
|     |     |     |     |     |     | (e) Step | 5. Evaluation |     | and | validation: | The | adapted |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | --- | ----------- | --- | ------- |
CONCEPTDRIFTPROBLEMS,SPECIFICALLYIN
|     |     |     |     |     |     | models | were | continuously |     | evaluated | and | validated |
| --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | --- | --------- | --- | --------- |
TIME-SERIESDATAANDTHEGENERALCONTEXT?
|               |      |             |     |                  |     | by employing |     | performance |     | metrics, | such | as ACC, |
| ------------- | ---- | ----------- | --- | ---------------- | --- | ------------ | --- | ----------- | --- | -------- | ---- | ------- |
| This question | aims | to identify | a   | general pipeline | for |              |     |             |     |          |      |         |
ROC,andAUC,aswellascross-validationtechniques,
detectingCDintime-seriesdataandgeneralcontexts,which
|     |     |     |     |     |     | to ensure | the | accurate | capture | of new | data | patterns. |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ------- | ------ | ---- | --------- |
involvesseveralkeystepsthatensurethatthemodelremains
|     |     |     |     |     |     | In [80] | and | [111], | the | authors used | ACC, | ROC, |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | ------------ | ---- | ---- |
accurateandreliabledespitechangesintheunderlyingdata
|               |              |     |         |                   |       | and | AUC to | evaluate | their | models | for CD | detection, |
| ------------- | ------------ | --- | ------- | ----------------- | ----- | --- | ------ | -------- | ----- | ------ | ------ | ---------- |
| distribution. | In addition, | to  | address | CD in time-series | data, |     |        |          |       |        |        |            |
adaptationtofakenews,andcyberattackscenarios.
| it is necessary | to understand |     | the | nature of the | data and |     |     |     |     |     |     |     |
| --------------- | ------------- | --- | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
thedetection,characterization,adaptation,andevaluationof
modelperformancetoensurethatitsaccuracyismaintained.
|           |           |            |     |              |          | 2) ADDRESSINGCONCEPTDRIFTINTIME-SERIESDATA |           |     |          |             |      |         |
| --------- | --------- | ---------- | --- | ------------ | -------- | ------------------------------------------ | --------- | --- | -------- | ----------- | ---- | ------- |
| The basic | steps for | addressing | CD  | are the same | for both |                                            |           |     |          |             |      |         |
|           |           |            |     |              |          | (a) Step                                   | 1. Nature |     | of data: | Time-series | data | consist |
generalcontexts,withtime-seriesdataprovidedinSectionsI
|     |     |     |     |     |     | of a | sequential |     | collection | of data | points | that are |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | ---------- | ------- | ------ | -------- |
andII.
|     |     |     |     |     |     | gathered | and | combined |     | at equally | spaced | intervals. |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | ---------- | ------ | ---------- |
Forexample,thesequentialdependencyintime-series
1) ADDRESSINGCONCEPTDRIFTINTHEGENERALCONTEXT datacomprisessequentialobservationstakenovertime,
(a) Step 1. Nature of data: The nature of the data in which each data point relies on the previous point.
includednosequentialdependency,andthedatawere Temporaltrendsfrequentlyexhibittrends,seasonality,
independentandidenticallydistributed.Thedatatypes and autocorrelations. In [112], the authors employed
includedtabulardata,text,andimageswithoutinherent two public real-world time-series datasets to evaluate
temporal order. For example, a dataset based on text their proposed CD detection method based on incre-
data streams was validated using the proposed model mentallearninginnonstationaryenvironments.
forthree-layerCDdetection.Thesedatasetscontained (b) Step 2. Concept drift detection: CD detection in
driftcategories[108]. time-series data can be accomplished via statistical
(b) Step 2. Concept drift detection: Detection CD tests or by employing drift detection algorithms such
involves identifying drift using statistical tests, mon- as Page-Hinkley, CUSUM, DDM, and ECDD. The
itoring prediction errors, or specialized algorithms. detection method focuses on the temporal sequence
However, the same algorithms, such as Page-Hinkley, of data points. For example, the DDM and ECDD
CUSUM, and EDDM, can be applied in different methodshavebeenemployedtodetectCDinfinancial
contexts.Forexample,theEDDM,DDM,andADWIN time-seriespredictionstoenhancethepredictionaccu-
methodshavebeenthoroughlyanalyzedtoinvestigate racyoftheproposedmodel[4].
theCDprobleminfake-reviewdetection.Theproposed (c) Step 3. Concept drift characterization: The char-
method was also tested using the Yelp consumer acterization of time-series data involves identifying
electronicsdatasetfromYelp.com[72]. temporal patterns, such as seasonal fluctuations or
| 119396 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE10. Summaryofmachinelearningtechniquesfordetectingconceptdriftinageneralcontext.
TABLE11. Summaryofalgorithmsusedinthepastdecadetohandleconceptdrift.
long-term tendencies that can influence drift. In addi- databecomeavailableandcanadapttochangesindata
tion, CD can be used to determine whether the distribution[113].
drift is sudden, gradual, incremental, or recurring (e) Step5.Evaluationandvalidation:Regularevaluation
to determine the most effective mitigation strat- and validation of the adapted time-series models
egy. A recent study investigated a new method for require specific validation methods, such as cross-
| detecting | CD in nonstationary | environments | during |            |             |                 |            |
| --------- | ------------------- | ------------ | ------ | ---------- | ----------- | --------------- | ---------- |
|           |                     |              |        | validation | techniques, | and performance | metrics to |
incremental learning. Furthermore, the authors char- ensureaccuracy,suchasACC,MAE,andRMSE.For
acterizeddifferenttypesofdrift:sudden,gradual,and example, RMSE and MASE evaluation metrics have
incremental[112]. been used to evaluate the CD model in a time-series
(d) Step 4. Model adaptation: The adaptation technique context[8],[81].
| in time-series | models involves  | re-training  | recent data, |              |     |     |     |
| -------------- | ---------------- | ------------ | ------------ | ------------ | --- | --- | --- |
| incrementally  | updating models, | or employing | ensem-       | VI. TAXONOMY |     |     |     |
ble methods. Methods such as sliding windows and ThissectionpresentsataxonomyfortheAIlearnerroadmap,
weighted re-training are highly efficient. To address which provides a brief overview of advances in handling,
the challenges posed by sudden or consistent changes detecting, and adapting to CD. However, understanding the
| in normal | behavior, an | ensemble DL | model with |                 |          |                               |     |
| --------- | ------------ | ----------- | ---------- | --------------- | -------- | ----------------------------- | --- |
|           |              |             |            | different types | of CD is | essential for the development | of  |
CDadaptationwasemployedfortime-seriesanomaly robust AI systems. Recognizing a specific drift type and
detection. The model is trained incrementally as new itscharacteristicsenablesresearcherstodevelopappropriate
| VOLUME13,2025 |     |     |     |     |     |     | 119397 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
detection methods that ensure the effectiveness of models analyzedtodetectsuddendrift[9].Thisstudyalsointroduced
in dynamic environments. The taxonomy was developed XGBoost and RNN learners to model the impact of data
after a critical review of existing literature and the present drift on model performance, such as sudden and potentially
experimental evaluation of the proposed roadmap for CD catastrophic events, such as COVID-19. In addition, this
detection.SubsectionBprovidesanevaluationofAImodels studycontributestothecreationofbetterpatientmonitoring
forCDdetectionintime-seriesapplications. systems in hospitals that can stratify patients according to
their risk of changing their disease states. A novel chunk-
A. ROADMAPFORCONCEPTDRIFTDETECTION based technique for classifying nonstationary data streams
An in-depth analysis of the ability of AI-based learners to is proposed, and GBN and MLP are used to detect sudden
detect CD based on categories such as speed and severity. drifts. To respond effectively to CD, the classifier ensemble
The methods were classified according to their speed and techniqueemploysashiftingensembleline-up[48].
severity, which were categorized as incremental, gradual,
sudden,orrecurring(Figure11). 4) AI-BASEDLEARNERSFORDETECTINGRECURRENTDRIFT
Recurrent CD signifies a situation in which an old concept
1) AI-BASEDLEARNERSFORDETECTINGINCREMENTAL reappearsafterabsence.However,thiswassimilartogradual
DRIFT CD. The effects of recurrent CD include changes in previ-
Incremental CD occurs when there is a minimal and ouslyobservedconcepts.Sunetal.[71]addressedrecurrent
continuous change in the original data distribution and drift in process industry streaming data by employing
the relationship between features and target variables. The DLSTM,LSTM,andOARlearners.Theproposedpredictive
effectsofincrementalchangesinCDoccurinsmall,gradual method supports the handling of streaming data by using
incrementsovertime,makingthemdifficulttodetectinreal- hybridrecurringCDsintheprocessingindustry.Inaddition,
time. AI-based learners can also detect this type of CD. thepredictiontaskforrecurringconceptsisdistributedacross
For example, Wang et al. [47] presented a quadruple-based multiple independent sub-models. Further investigations
approachforunderstandingCDindatastreams(QuadCDD) presented a novel algorithm learner for classifying data
framework, which is a novel deep neural network (DNN)- streamsusingarandomforest,wherethefeatureimportance
basedlearnerthatdetectsandpredictsCD,butalsopredicts metric was used as the drift detector [53]. Furthermore,
incremental drift. The quadruple provides a comprehensive the proposed algorithm combines the ability of ensemble
picture of CD, including its start, end, severity, and type. methodstohandleslowchangesindatastreamswithanovel
In addition, recent studies have proposed robust models for methodfordetectingCDoccurrences.
detectingincrementalCDusingSVM,GNB,andMLP[48],
[83]. B. EXPERIMENTALEVALUATION
The evaluation of AI models for CD detection using
2) AI-BASEDLEARNERSFORDETECTINGGRADUALDRIFT time-series data involves several experimental methods.
Gradual CD occurs when there are gradual and noticeable This study presents an experimental evaluation of the
changesinthetargetdatadistribution.Theeffectsofgradual CD roadmap, which includes data evaluation, performance
CDincludelong-termeffects.However,thisapproachallows metrics,evaluationprocedures,andbaselinemethods.
for detection earlier than incremental drift. Disabato and
Roveri [50] presented a Tiny Machine Learning (TML) 1) EVALUATIONDATA
solutionforCDthatintegratesk-NN,SVM,andNNlearners. The data for CD detection using AI models will be
These learners include a hybrid adaptation module that evaluatedusingreal-worldtime-seriesdatasuchasfinancial,
can handle the gradual drift that affects the data-generation weather, and sensor data. These datasets ensure that the
process.Theaccuracyofthemodelinthespeech-command- detection algorithms can efficiently handle the complex
identificationscenariowasevaluatedovertimewithgradual natureofreal-worlddriftsafterallowingmodelperformance
and abrupt noise addition. In addition, a framework for evaluation in an authentic scenario. In addition, the use of
classifying CD based on FCN learning was proposed. This real-world data helps to confirm the effectiveness of the
framework involves offline pre-training of a model on data model in addressing real-world challenges associated with
streams with known drifts and then fine-tuning the model CDindynamicenvironments.
onlinetoimprovedetectionaccuracy[68].
2) PERFORMANCEMETRICS
3) AI-BASEDLEARNERSFORDETECTINGSUDDENDRIFT Performance metrics are crucial for determining the effec-
AsuddenCDcanbeinterpretedasanabruptandsignificant tivenessoftheproposedroadmapforCDdetectionintime-
change in the original data distribution at a particular time series environments. Performance evaluation metrics were
point and as a relationship between the features and target employed based on classification and regression problems.
variables. The effect of a sudden CD leads to abrupt and Collectively,thesemetricsensurearobustevaluationframe-
unforeseenbehaviors,whichpresentsasignificantchallenge work for AI models that address both the classification and
to models trained on previous data. AI learners have been regressionaspectsofCDdetection.Inaddition,theaccuracy,
119398 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
|     | FIGURE11. |     | IllustrationofAIlearnersforconceptdriftdetection. |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precision, recall, F1 score, and AUC were based on the (g) Mean absolute error (MAE): This represents the
classificationmetrics.RMSE,MSE,andMAEareregression absolute difference between the predicted and actual
| metrics. | The definitions | and | mathematical |     | equations | for the | values. |     |     |     |     |     |     |
| -------- | --------------- | --- | ------------ | --- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
evaluationmetricsareasfollows:
|              |        |     |          |     |                |     |     |     | 1Xn |     | (cid:12) (cid:12)      |     |     |
| ------------ | ------ | --- | -------- | --- | -------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
|              |        |     |          |     |                |     |     | MAE | =   |     | (cid:12)yˆi−yi(cid:12) |     | (7) |
| (a) Accuracy | (ACC): | ACC | measures |     | the proportion | of  |     |     |     | i=1 |                        |     |     |
n
| correctly | identified | instances |     | (both | drift and | no drift) |            |     |       |        |     |          |     |
| --------- | ---------- | --------- | --- | ----- | --------- | --------- | ---------- | --- | ----- | ------ | --- | -------- | --- |
|           |            |           |     |       |           |           | Area under | the | curve | (AUC): |     |          |     |
|           |            |           |     |       |           |           | (h)        |     |       |        | AUC | measures | the |
amongthetotalnumberofinstances.
|     |     |     |     |     |     |     | ability of | the model | to  | distinguish | between | drift | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ----------- | ------- | ----- | --- |
TP+TN no-drift cases across different threshold settings. The
|     | Accuracy= |     |       |        |     | (1) |            |              |     |           |                |     |       |
| --- | --------- | --- | ----- | ------ | --- | --- | ---------- | ------------ | --- | --------- | -------------- | --- | ----- |
|     |           |     | TP+TN | +FP+FN |     |     |            |              |     |           |                |     |       |
|     |           |     |       |        |     |     | area under | the receiver |     | operating | characteristic |     | curve |
wasalsocalculated.
| (b) Precision | (P):       | This  | measures | the       | proportion | of the     |     |     |     |     |     |     |     |
| ------------- | ---------- | ----- | -------- | --------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| positive      | predictive | value | and      | indicates | the        | proportion |     |     |     |     |     |     |     |
ofdetecteddrift,whichistheactualdriftofthemodel. 3) EVALUATIONPROCEDURE
Extensiveevaluationproceduresarerequiredtoensureaccu-
TP
Precision= (2) rate results when evaluating the proposed CD roadmap for
TP+FP
time-seriesdata.Thepredictiveevaluation,holdoutmethod,
(c) Recall(R):Thismeasurestheproportionofactualdrift
|                     |     |        |       |     |     |     | and cross-validation | evaluation  |         | procedures | are    | described | as   |
| ------------------- | --- | ------ | ----- | --- | --- | --- | -------------------- | ----------- | ------- | ---------- | ------ | --------- | ---- |
| detectedbythemodel. |     |        |       |     |     |     | follows:             |             |         |            |        |           |      |
|                     |     |        |       | TP  |     |     | (a) Prequential      | evaluation: |         | This       | method | involves  | con- |
|                     |     | Recall | =     |     |     | (3) |                      |             |         |            |        |           |      |
|                     |     |        | TP+FN |     |     |     | stant updating       | and         | testing | of the     | model  | as new    | data |
(d) F1 score (F1): The F1 score measures precision and arrives.Eachnewdatapointwasusedtotestthemodel,
|     |     |     |     |     |     |     | followed | by training. |     | This method | also | simulates |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ----------- | ---- | --------- | --- |
recall,providingabalancebetweenthetwometrics.
|     |     |     |     |     |     |     | real-world | scenarios | in  | which | the data | streams | are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ----- | -------- | ------- | --- |
Precision×Recall
F1=2× (4) constant, enabling dynamic evaluation of the model’s
|     |     |     | Prescision+Recall |     |     |     | abilitytodetectCDovertime. |     |     |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
(e) Root mean square error (RMSE): RMSE measures (b) Holdoutmethod:Thedataweresplitintotrainingand
the square root of the average squared difference testingsets.Theinitialtrainingsetwasusedtotrainthe
model,whichwasthentested.Thisstandardapproach
betweenthepredictedandactualvalues.
|     |     |     | r   |     |     |     | improvesthemodelperformanceonpreviouslyunseen |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
1Xn
|     |      | =   |     | (yˆi−yi)2 |     |     | dataandisusefulforthepreliminarybenchmarkingof |     |     |     |     |     |     |
| --- | ---- | --- | --- | --------- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | RMSE |     |     |           |     | (5) |                                                |     |     |     |     |     |     |
|     |      |     | n   | i=1       |     |     |                                                |     |     |     |     |     |     |
driftdetectioncapabilities.
(f) Meansquarederror(MSE):Thisrepresentstheaver- (c) Cross validation: Model robustness is guaranteed
age of the squared differences between the predicted usingcross-valuationmethods,includingk-foldcross-
andactualvalues. valuation. The data were then split into k subsets.
|               |     |     |       |           |     |     | Each time, | the model |        | was trained | and        | validated | by     |
| ------------- | --- | --- | ----- | --------- | --- | --- | ---------- | --------- | ------ | ----------- | ---------- | --------- | ------ |
|               |     |     | 1Xn   | (yˆi−yi)2 |     |     |            |           |        |             |            |           |        |
|               | MSE | =   |       |           |     | (6) |            |           |        |             |            |           |        |
|               |     |     | n i=1 |           |     |     | using a    | different | subset | as the      | validation | set.      | This   |
| VOLUME13,2025 |     |     |       |           |     |     |            |           |        |             |            |           | 119399 |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
approachprovidesacompleteevaluationbyaveraging many struggle to handle high-dimensional or complex
the performance over several data splits and helps time-series data because of scalability issues. For example,
understandthegeneralizationcapacityofthemodelin the WSTD method is limited because it is computationally
thepresenceofCD. expensive due to the sorting of observations [84]. Despite
theircomputationalcomplexity,AItechniquesexhibitsupe-
4) BASELINEMETHODS rior scalability when applied to large and high-dimensional
The baseline method compares the performance of AI datasets. The XGBoost and DNN techniques exhibit excep-
learnerswithconventionalmethodsfordetectingCDintime- tionalperformancewhenhandlinglargedatasets.
series data. However, standard drift detection techniques
such as Page-Hinkley, ADWIN, DDM, and EDDM have VII. DISCUSSION
been used as baselines. The performance of AI learners This section presents the findings concerning the RQs
was evaluated using these established methods to ensure a described in Section III. This study summarizes the key
thoroughassessmentoftheireffectivenessindetectingCDs. conclusions by analyzing and assessing empirical research
on CD detection using time-series data. Because of the
nonstationarycharacteristicsofreal-worlddata,CDdetection
C. COMPARATIVEANALYSIS
is essential for reliable time-series analysis and forecasting.
This section compares the roadmap for CD detection with
Over time, the underlying processes that generate data can
well-knownbaselinemethodsinthefieldbyassessingtheir
evolve,renderingthehistoricalpatternsinapplicabletofuture
effectiveness and novelty. The roadmap uses advanced AI
predictions. By identifying these CDs, the efficacy of the
techniquessuchasSVM,GBN,NN,andXGBoosttodetect
model could be maintained. Early detection enables timely
varioustypesofCD.Thesemethodshaveseveraladvantages
adaptation, such as re-training models with the new data
overtraditionalapproachesbecauseoftheirabilitytomodel
distribution,whichresultsinmorereliableandgeneralizable
complex, nonlinear relationships. The comparative analysis
forecasts.Additionally,time-seriesanalysesandforecasting
wasdividedintothreemaincategories:detectioncapability,
modelsaresusceptibletoCD,whichcanoccurincrementally,
adaptabilityandflexibility,andperformanceandscalability.
gradually,suddenly,orrecurring.Understandingthesedrifts
is essential for creating robust forecasting models that
1) DETECTIONCAPABILITY
can adapt to the evolving characteristics of real-world
Well-knownbaselinetechniques,suchasDDMandEDDM,
data.
are effective at detecting abrupt and gradual drifts; how-
Several methods are available for detecting CD in time-
ever, their effectiveness is reduced in scenarios involving
series data. Statistical techniques such as monitoring the
incremental or recurrent drifts because the technique relies
average and variability can detect deviations from existing
on fixed statistical thresholds. In addition, their limitations
data distributions. The windowing method compares recent
include sensitivity to noise, false alarms, and difficulty in
data with historical windows to identify changes in dis-
handling class-imbalance scenarios [114], [115]. Although
tribution patterns. This study focuses on ensemble-based
the proposed DNN and XGBoost can capture complex
learning techniques that are efficient in detecting CD in
patterns in the data, they are better at detecting incremental
time-seriesdata.Theseadvantagesallowmultiplelearnersto
andrecurrentdrifts.Thesemodelscanadaptivelylearnfrom
createrobustmodelswithimprovedadaptabilitytochanging
andadjusttochangesindatadistribution,therebyproviding
data patterns. The core functionalities of ensemble-based
amoresophisticateddetectionmechanism.
learning include diverse base learners, error correction and
aggregation, and continuous learning. In nonstationary data
2) ADAPTABILITYANDFLEXIBILITY streams,anensemble-basedclassificationalgorithmwasused
Baselinetechniques,suchasADWINandDW_HDDM,are to detect CD with a focus on two-class problems via incre-
adaptable for handling several types of drifts. However, mentallearning[100].Theensembledriftdetectionapproach
their performance can be reduced owing to the selection reducesthecomputationalcomplexityoftheupdatingprocess
of parameters and the assumption of specific distribution byselectingonlyasubsetofnewlyavailabledataandenables
properties.However,theirlimitationsincludecomputational the timely tracking of ongoing patterns through feature
complexity and detection delays [116], [117]. The adapt- vector selection [101]. CD has been addressed in financial
ability of the proposed method to AI, including DNNs, time-series prediction to improve forecasting accuracy by
XGBoost,andRF,allowsittodynamicallyadjusttoevolving employing ELM with explicit drift detection and online
data streams. Their natural flexibility in handling various updating of the decision model when CD occurs in the
data distributions improves their robustness in real-world data[4].Moreimportantly,ensemble-basedmethodsprovide
applications. a flexible and effective framework for CD detection in
time-seriesanalyses,enablingresearcherstomaintainmodel
3) PERFORMANCEANDSCALABILITY accuracyandimproveforecastingperformance.
Conventional techniques centered around a baseline are In addition, various AI-based learners play a vital role
computationallyefficientandsimpletoimplement;however, in effective CD detection. For example, providing a diverse
119400 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
| framework | for | detecting | CD  | in time-series |     | data | enables |     |     |     |     |     |     |
| --------- | --- | --------- | --- | -------------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
proactiveadaptationandimprovesforecastingperformance.
| Decision | tree-based | learners,    |     | such as | XGBoost, | k-NN,   | and     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | --- | ------- | -------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
| FR, are  | effective  | in detecting |     | sudden  | changes  | in data | distri- |     |     |     |     |     |     |
butionandrespondingtoincrementalandabruptdrifts[59],
| [66]. Neural | networks | comprising    |     | RNN    | and  | MLP can  | learn |     |     |     |     |     |     |
| ------------ | -------- | ------------- | --- | ------ | ---- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| complex      | temporal | dependencies, |     | making | them | suitable | for   |     |     |     |     |     |     |
detectingCDs,suchasgradualandrecurringdrifts[48],[68],
[118].Inaddition,SVM-basedlearnersfocusonthedecision
boundarybetweenclasses,andSVMscaneffectivelydetect
| shifts in  | the underlying |         | data structure, |        | which   | is particularly |         |     |     |     |     |     |     |
| ---------- | -------------- | ------- | --------------- | ------ | ------- | --------------- | ------- | --- | --- | --- | --- | --- | --- |
| useful for | sudden         | drifts. | Critical        | issues | related | to              | CD have |     |     |     |     |     |     |
beenaddressedusingincrementallearningwithSVM,which
|     |     |     |     |     |     |     |     | FIGURE12. | Lessonslearnedandbestpracticesforconceptdrift |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- |
allows the acquisition of new knowledge without retaining mitigationintime-seriesapplications.
previousknowledge[64].PNN,anotherAI-basedlearner,has
beenusedtoanalyzeandinvestigateCDproblemsinmodels
designedforfakereviewdetection[72]. Table12summarizestheevaluationmetricsanddatasetsfor
CDdetectionintheselectedstudies.
| The proposed |     | study selected |     | 60 studies |     | on CD | detection |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | ---------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
and thoroughly investigated dataset sources to better under- In general, each learner and algorithm have strengths
|           |          |          |     |               |     |          |      | and weaknesses | in terms | of CD, | handling, | and | adaptation. |
| --------- | -------- | -------- | --- | ------------- | --- | -------- | ---- | -------------- | -------- | ------ | --------- | --- | ----------- |
| stand the | research | results. | The | investigation |     | revealed | that |                |          |        |           |     |             |
some studies used real-world datasets, whereas others used This could include the computational complexity of certain
synthetic datasets or a combination of both. Rahmani et al. algorithms,sensitivityofspecificmethodstooutliers,orthe
|          |      |            |        |         |     |          |      | inability | of some methods | to detect | certain | types | of drift |
| -------- | ---- | ---------- | ------ | ------- | --- | -------- | ---- | --------- | --------------- | --------- | ------- | ----- | -------- |
| [9] used | real | electronic | health | records | to  | simulate | data |           |                 |           |         |       |          |
drift, covariate shift, concept shift, and a major event to (e.g., gradual drift). Table 13 summarizes the state-of-the-
study their effects on ML-based clinical sepsis prediction art studies, along with their contributions, strengths, and
weaknesses.
| models.    | A novel          | uncertain | label     | request | strategy | based         | on  |     |     |     |     |     |     |
| ---------- | ---------------- | --------- | --------- | ------- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| a variable | least-confidence |           | threshold |         | vector   | was evaluated |     |     |     |     |     |     |     |
using a real network traffic dataset [62]. In addition, the VIII. SUMMARYOFLESSONSLEARNEDANDBEST
| proposed | strategy | attempts | to  | address | the challenges |     | posed | PRACTICES |     |     |     |     |     |
| -------- | -------- | -------- | --- | ------- | -------------- | --- | ----- | --------- | --- | --- | --- | --- | --- |
by the variable multiclass imbalance ratio and CD in All in all, this SLR examines recent research contributions
network traffic classification. The Intel Berkeley Research relatedtoCDdetectionintimeseriesapplications.Thestudy
Lab provided real temperature data from 54 Mica2Dot of CD in time-series applications is important because of
|     |     |     |     |     |     |     |     | the increasing | number | of time-series | and | data streams | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | -------------- | --- | ------------ | --- |
sensorsthatcontainedweatherplates.Theproposedmethod
was evaluated using the fog-DeepStream method, which frequentchangesintheirunderlyingstatisticalpropertiesover
integrates three fields of study: signal processing, CD, and time. Detecting and adapting to these changes is required
|             |          |       |     |           |        |     |         | to maintain | the performance | of  | predictive | models. | This |
| ----------- | -------- | ----- | --- | --------- | ------ | --- | ------- | ----------- | --------------- | --- | ---------- | ------- | ---- |
| deep neural | networks | [63]. | In  | a similar | study, | the | authors |             |                 |     |            |         |      |
used the real NTUST_EE_Lobby dataset with CD and sectionsummarizesthelessonslearnedandthebestpractices.
Figure12presentsagraphicalrepresentationofthesummary
| reused the | knowledge | learned |     | from the | VOC | dataset | to test |     |     |     |     |     |     |
| ---------- | --------- | ------- | --- | -------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
their proposed counterparts for streaming image analytics oflessonslearnedandbestpracticesforCDdetectionintime-
models [51]. Kaminskyi et al. [61] used synthetic datasets seriesapplications.
| that contain | Changing |     | Sine Sudden |     | (CS sud | ) and Changing |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ----------- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Sine Incremental (CS ), to effectively capture drifts in A. COMPUTATIONALCOSTANDEFFICIENCY
incr
|     |     |     |     |     |     |     |     | A critical | lesson from the | literature | is the | necessity | of pre- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | ---------- | ------ | --------- | ------- |
multivariatedatastreams.
Mehmood et al. [46] also used both synthetic and real dictiveperformancewithcomputationalcostandefficiency,
datasetstodetectCDandadaptittosmartcityapplications. particularly in real-time applications based on time-series
Wangetal.[47]alsousedbothtotestanovelquadruple-based data. The literature consistently prioritizes the development
approach for understanding CD in a data stream framework ofmorecomputationallytractableadaptationtechniquesdue
using two real-world datasets as well as artificial datasets. to the significant overhead associated with complete model
The proposed method detects and predicts the start points re-training in response to CD. These include incremental
of the CD. The effectiveness of incremental support vector learningmethods,suchasincrementaladaptationusingSVM
MLinhandlingincreasingandchangingdata(datadrift)was fordriftdata,whichadaptswithoutre-trainingfromscratch,
evaluated using five industrial datasets, including clean and and partial-update mechanisms that modify only specific
credit data [64]. Finally, a dataset from the Australian New modelcomponents[64].
SouthWales(ElectricityMarket),includingspamandmixed Additionally, innovative architectural solutions such as
abrupt changes, was used to test an error-based weighted the TriLS approach effectively address lightweight model
averaging ensemble model for adaptation to CD [65]. tuning by transferring the computationally demanding tasks
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 119401 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
of drift detection and model rebuilding to the cloud [18]. model performance [83]. The model may become outdated
Thisprocessleadstoanotabledecreaseinthecomputational if it is overly resistant to noise, which may delay the
load, memory requirements, and communication overheads identificationoftheactualdrift.
of the gateway. At the most constrained level, TML-
CD solutions are being developed to facilitate on-device E. DIVERSITYANDMANAGEMENTOFENSEMBLES
adaptation while operating under stringent memory and Ensemble learning combines many base learners to provide
energy constraints [50]. The collective approaches illustrate a robust paradigm for detecting CD in time-series data.
a notable lesson for developing lightweight, efficient, and Recent research indicates that, in ensemble approaches,
architecturallyinformedsolutionsthatfacilitatepracticalCD maintaining diversity among base learners is important for
handlingforreal-worldimplementations. optimal performance, especially in the context of recurring
drifts. Algorithms such as HDWM using ‘‘seed’’ learners
B. SELECTINGAPPROPRIATEWINDOWSIZES preserve diversity [88]. A diverse ensemble consisting of
In window-based methods, the selection of an appropriate modelstrainedondistinctdatasubsetsoremployingvarious
windowsizeisimportantandpresentschallengesfortheCD. algorithms can collectively sustain high performance by
However,fixed-sizewindowscanencounterdifficultieswith changing CD [76]. Additionally, in ensemble methods,
suddendrifts,whereasadaptivewindowsintroduceadditional preserving diversity among base learners is essential for
complexities[70].However,adaptivewindowingtechniques ensuringrobustnessandadaptability,particularlyinthecon-
have been identified as the most effective approach. For text ofrecurring drifts.Thus, diversity isnot anappropriate
example,ADWINdynamicallyadjuststhewindowsizebased replacement for accuracy. The optimal level of diversity
on variations in the observed data. Additionally, it operates dependsonthespeedandseverityofdrift.
by controlling a window and decreasing its size when
the statistical differences between sub-windows surpass the F. THOROUGHEXPERIMENTALEVALUATION
specifiedconfidencelevel,indicatingadrift. An experimental evaluation is necessary to validate CD
detection methods. This process involves using various
C. HANDLINGDIFFERENTDRIFTTYPES datasets,includingbothsyntheticandreal-worldtimeseries,
Effective detection of CD requires the implementation of toevaluateperformanceacrossdifferenttypesofdrifts[76].
techniquesspecificallydesignedfordifferenttypesofdrifts. Thenecessityforthoroughexperimentalanalysisemploying
Sudden drift, defined by abrupt shifts in concept, often various datasets, both synthetic and real-world, to simulate
requiresimmediatemodelre-training[88].Incrementallearn- different types of drift and data conditions (imbalance and
ersmayeffectivelymanagegradualchanges,whereasabrupt noise) is consistently emphasized for the validation of new
drifts may necessitate rapid adaptation or model resetting. methods [48]. Multiple metrics can be considered during
Recurringconceptsareenhancedbymechanismsthatenable evaluation, including accuracy, F1-score, detection delay,
the recall or reactivation of information from the previous falsealarmrate,computationalcomplexity,andmemoryuse.
model. Additionally, incremental drift, characterized by Thebestpracticesrevealedthatacomprehensiveevaluation
continuousandconsistentchange,maybeenhancedthrough across CD models is important for assessing a technique in
online learning or techniques that facilitate incremental time-seriesforecasting.
updating of knowledge bases [89]. The OAR-DLSTM
method assigns prediction tasks to multiple sub-models G. SYSTEMARCHITECTUREFORDRIFTHANDLING
based on recurring concepts to manage hybrid recurring An effective system architecture for handling CD in
drifts in industrial processes [71]. The lesson learned is time-series data typically consists of several interconnected
that it is essential to differentiate these types of drifts to modules, which are considered the best practices. The
select the most suitable and resource-efficient adaptation interconnectedmodulesincorporatenoveledgearchitectures,
mechanism,therebyoptimizingmodelperformanceintime- including a hybrid cloud-edge continuum, which are pro-
seriesenvironments. posed to support AI workloads and facilitate automated
CD handling for smart city applications [46]. Based on
D. DIFFERENTIATINGDRIFTFROMNOISE resourceavailability,thesearchitecturescanenableworkload
Differentiating between the actual CD and random fluctu- migration on demand (e.g., model retraining). Additionally,
ations or outliers is a key challenge, as misidentification hybrid cloud-edge architectures can move computation-
leadstoexcessivemodelupdatesandinstability.Forexample, ally intensive drift detection and model rebuilding to
multiscale structure of MDDT was designed to effectively the cloud, whereas edge devices handle local lightweight
filter the noise present in drift indicators [82]. This study adaptation[18].
additionally confirmed that a significant challenge in CD
detection is the accurate differentiation between actual H. REAL-WORLDVERSUSSYNTHETICDATA
conceptshiftsandmerenoiseorrandomfluctuationspresent Evaluating CD detection methods requires careful analysis
intime-seriesdata.Excessivesensitivitytonoisemayresult ofdatasources,especiallydistinguishingbetweenreal-world
in frequent, pointless model updates and possibly degrade andsyntheticdata.Real-worlddataareextremelyimportant
119402 VOLUME13,2025

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE12. SummarizesoftheevaluationmetricsanddatasetsforCDdetectionfromtheselectedstudies.
for validating the robustness, practicality, and applicability published between 2013 and 2024 were carefully selected
ofCDdetectionmethods[72].Syntheticdataenableprecise and assessed. This SLR also confirms that using AI-based
control over drift characteristics [80]. This allows for a learners to detect, handle, and adapt to CD in time-series
systematic evaluation of detection accuracy, latency, and scenariosisapromisingapproach.
falsepositiveratesunderspecifiedconditions.However,real- However, the SLR has some limitations. First, the study
worlddriftsoftendifferfromsimulateddrifts.Additionally, analyzed 60 research articles selected based on a search
it is important to evaluate the methods on various datasets, strategy that involved searching multiple databases, such as
includingreal-worldandsyntheticdatasetswithknowndrift SCOPUS, Science Direct, IEEE Xplore, Web of Science,
types.Thelessonlearnedisthatbothdatatypesareimportant MDPI, and ACM. Therefore, because the search criteria
because synthetic data allow rigorous and controlled exper- focusedonjournalpaperspublishedbetween2013and2024,
imentation, whereas real-world data demonstrate practical somerelevantstudieswereexcludedfromthereview.Studies
applicabilityandunforeseenchallenges. conducted in languages other than English were excluded.
Second, most of the currently proposed drift detection,
IX. CONCLUSIONANDFUTUREDIRECTIONS handling, and adaptation methods have not been solved.
In conclusion, forecasting time-series applications rely on However, reliance on simulation datasets may not fully
theoutputfromtheMLmodelaftertrainingthedata,which capturereal-worldscenarios.Moreover,severalstudieshave
becomes more challenging because of the CD problem. testedtheproposedmethodusingasingledataset,whichmay
Thisstudyexaminesthecurrentstate-of-the-artmethodsthat limit generalizability. In addition, comparisons with active
detect and adapt CD in time-series data for regression and approachesfromstate-of-the-artstudiesarelimited.Finally,
classificationlearningtasks.Thesestudieshaveenabledthe thisstudywasunabletoinvestigateotherapproachestoCD
development of a taxonomy for this area. After critically detection,suchassimilarityanddissimilarity-basedmethods,
reviewing the existing literature, this study developed a usingtime-seriesdata.
taxonomy and presented an experimental evaluation of the This study recommends that further research investigate
proposedroadmapforCDdetection.Additionally,thisstudy existing algorithms for AI-based learners by introducing
summarized,categorized,mapped,andsurveyedtheexisting next-generation approaches for detecting CD in time-series
literatureondriftdetectionintime-seriesdatabydeveloping and data streams. The analysis of databases other than
RQs based on existing empirical studies. The PRISMA SCOPUS, Science Direct, IEEE Xplore, Web of Science,
2020methodwasusedtoconductthesurvey,and60studies ACM, and MDPI is also recommended. The following
VOLUME13,2025 119403

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE13. Summaryofstate-of-the-artstudiesandtheircontributions,strengths,andweaknesses.
research directions are recommended based on the SLR time-consuming and disruptive in real-world scenar-
| findings. |     |     |     | ios [14], [19]. | Adaptive learning | models that | can |
| --------- | --- | --- | --- | --------------- | ----------------- | ----------- | --- |
respondtoCDwithoutexplicittrainingandensureopti-
| 1) Most existing | methods     | in the literature | require |                 |                      |               |     |
| ---------------- | ----------- | ----------------- | ------- | --------------- | -------------------- | ------------- | --- |
|                  |             |                   |         | mal performance | are being developed. | For example,  |     |
| training models  | after drift | detection, which  | can be  |                 |                      |               |     |
| 119404           |             |                   |         |                 |                      | VOLUME13,2025 |     |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
TABLE14. PRISMA2020checklist.
| onlinelearningalgorithmscontinuouslyupdatemodels |          |            |     |         |         |         | ABBREVIATIONS                                |     |     |     |
| ------------------------------------------------ | -------- | ---------- | --- | ------- | ------- | ------- | -------------------------------------------- | --- | --- | --- |
| basedonnewdata.                                  |          |            |     |         |         |         | Thismanuscriptusesthefollowingabbreviations: |     |     |     |
| 2) Several                                       | existing | approaches |     | require | labeled | data to |                                              |     |     |     |
AA AverageAccuracy.
detectdrift,whichcanbedifficultorexpensive[119].
ACC Accuracy.
| Exploring | unsupervised |     | and semi-supervised |     |     | learning |                |         |       |           |
| --------- | ------------ | --- | ------------------- | --- | --- | -------- | -------------- | ------- | ----- | --------- |
|           |              |     |                     |     |     |          | ACDDM Accurate | Concept | Drift | Detection |
approachesforCDdetectionthatuseasmallamountof Method.
labeleddatatoguidethedetectionprocessinscenarios
ADWIN AdaptiveWindowing.
withlimitedlabeleddata.
|                    |     |         |             |     |               |     | ADDM Adaptive | sliding window-based |     | Detec- |
| ------------------ | --- | ------- | ----------- | --- | ------------- | --- | ------------- | -------------------- | --- | ------ |
| 3) The distinction |     | between | correlation |     | and causation |     |               |                      |     |        |
tionMethod.
| remains | a significant |     | challenge | in  | CD identifica- |     |     |     |     |     |
| ------- | ------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- |
ADD ActiveDriftDetection.
tion [120]. Future studies should investigate causal AVF ArchitecturalVulnerabilityFactor.
| representation | learning |     | methods, | such | as causal | dis- |     |     |     |     |
| -------------- | -------- | --- | -------- | ---- | --------- | ---- | --- | --- | --- | --- |
ANN ArtificialNeuralNetwork.
| covery and | counterfactual |     | reasoning, |     | to enhance | the |     |     |     |     |
| ---------- | -------------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
AUC AreaUndertheCurve.
robustnessandgeneralizabilityofCDmodels.
|     |     |     |     |     |     |     | AGE Accuracy | and Growth | rate | updated |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ---- | ------- |
4) Asingleapproachmaynotbeeffectiveinallscenarios.
Ensemble.
| Hybrid | approaches | that | combine |     | several detection |     |     |     |     |     |
| ------ | ---------- | ---- | ------- | --- | ----------------- | --- | --- | --- | --- | --- |
AIOps ArtificialIntelligenceforITOperations.
| methods | are potentially |     | transformative. |     | For example, |     |     |     |     |     |
| ------- | --------------- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- |
CSDD CosineSimilarityDriftDetector.
| combining | statistical | methods |     | with | windowing | tech- |     |     |     |     |
| --------- | ----------- | ------- | --- | ---- | --------- | ----- | --- | --- | --- | --- |
CDDA ConceptDriftDomainAdaptation.
niquescanresultinmorerobustdetection.
|                          |     |        |     |         |               |     | CDBD Confidence | Distribution | Batch | Detec- |
| ------------------------ | --- | ------ | --- | ------- | ------------- | --- | --------------- | ------------ | ----- | ------ |
| 5) Future investigations |     | should |     | explore | DL techniques |     |                 |              |       |        |
tion.
| that integrate | complementary |     |     | data sources, | including |     |     |     |     |     |
| -------------- | ------------- | --- | --- | ------------- | --------- | --- | --- | --- | --- | --- |
CUSUM ConceptDriftusingCUmulativeSUM.
| sensor readings, |     | images, | and | text, | for CD detection. |     |     |     |     |     |
| ---------------- | --- | ------- | --- | ----- | ----------------- | --- | --- | --- | --- | --- |
CBA CostBenefitAnalysis.
Advancedmodels,includingmultimodaltransformers,
CNN ConvolutionNeuralNetworks.
canintegratethesetechniquestoenhancethedetection CDT ChangeDetectionTest.
accuracy.
CD ConceptDrift.
DT DecisionTree.
APPENDIXA
DNN DeepNeuralNetwork.
Tables12and13.
DDM DriftDetectionMethod.
ELM ensembleExtremeLearningMachines.
| APPENDIXB |     |     |     |     |     |     | XGBoost eXtremeGradientBoosting. |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
ThePRISMA2020checklistwasobtainedfromhttps://www. EDDM EarlyDriftDetectionMethod.
prisma-statement.org/s/PRISMA_2020_checklist-k3f4.docx FCN FullyConvolutionalNetwork.
(accessedMay19,2025).Table14presentsthechecklistused EDDM EarlyDriftDetectionMethod.
inthisSLR,includingthesections,numbers,andplacements EWMA Exponentially Weighted Moving Aver-
age.
inthepublication.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 119405 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
ECDD Exponentially Weighted Moving Aver- RHP RotatingHyperPlane.
|     | ageConceptDriftDetection. |     |     |     | RNN | RecurrentNeuralNetwork. |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
ELM ExtremeLearningMachine. RDCAL Realtime Dynamic Concept Adaptive
| FPR      | FalsePositiveRate.                 |     |     |      |        | Learning.                 |         |           |     |                |     |     |
| -------- | ---------------------------------- | --- | --- | ---- | ------ | ------------------------- | ------- | --------- | --- | -------------- | --- | --- |
| FP       | FalsePositive.                     |     |     |      | RGF    | RegularizedGreedyForests. |         |           |     |                |     |     |
| FN       | FalseNegative.                     |     |     |      | ROC    | Receiver                  |         | Operating |     | Characteristic |     |     |
| FHDDM    | FastHoeffdingDriftDetectionMethod. |     |     |      |        | Curve.                    |         |           |     |                |     |     |
| FTRL-ADP | Follow-the-Regularized-Leader      |     |     | with |        |                           |         |           |     |                |     |     |
|          |                                    |     |     |      | SAM    | Self-AdjustingMemory.     |         |           |     |                |     |     |
|          | AdaptiveDecayingProximal.          |     |     |      | SVM    | SupportVectorMachine.     |         |           |     |                |     |     |
| FSDD     | FisherSquareDriftDetector.         |     |     |      | SD     | StandardDeviations.       |         |           |     |                |     |     |
| FPDD     | FisherProportionsDriftDetector.    |     |     |      | TP     | TruePositive.             |         |           |     |                |     |     |
| GNB      | GaussianNaïveBayes.                |     |     |      | TML    | TinyMachineLearning.      |         |           |     |                |     |     |
| G-Mean   | GeometricMean.                     |     |     |      |        |                           |         |           |     |                |     |     |
|          |                                    |     |     |      | TML-CD | Tiny                      | Machine | Learning  |     | for Concept    |     |     |
| GA       | GeneticAlgorithm.                  |     |     |      |        | Drift.                    |         |           |     |                |     |     |
GMA GeometricMovingAverage. WSTD WilcoxonRankSumTestDriftDetector.
| GMM   | GaussianMixtureModel.            |     |     |     | YOLO | YouOnlyLookOnce. |     |     |     |     |     |     |
| ----- | -------------------------------- | --- | --- | --- | ---- | ---------------- | --- | --- | --- | --- | --- | --- |
| GRU   | GatedRecurrentUnit.              |     |     |     |      |                  |     |     |     |     |     |     |
| HDDDM | HellingerDistanceDriftDetection. |     |     |     |      |                  |     |     |     |     |     |     |
DECLARATIONOFINTERESTS
| HDDM | HoeffdingDriftDetectionMethod. |         |          |     |             |           |             |               |     |       |           |      |
| ---- | ------------------------------ | ------- | -------- | --- | ----------- | --------- | ----------- | ------------- | --- | ----- | --------- | ---- |
|      |                                |         |          |     | The authors | declare   | that        | they have     | no  | known | competing |      |
| HDWM | Heterogeneous                  | Dynamic | Weighted |     |             |           |             |               |     |       |           |      |
|      |                                |         |          |     | financial   | interests | or personal | relationships |     | that  | could     | have |
Majority.
influencedtheworkreportedinthisstudy.
| HW_DDM | Hybrid Weighting-based |     | Concept | Drift |     |     |     |     |     |     |     |     |
| ------ | ---------------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
DetectionMethod.
REFERENCES
| KSWIN | Kolmogorov–Smirnovwindowing. |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k-NNs k-nearestNeighbors. [1] A.Kahraman,M.Kantardzic,M.M.Kahraman,andM.Kotan,‘‘Adata-
|     |     |     |     |     | driven | multi-regime | approach | for | predicting | energy | consumption,’’ |     |
| --- | --- | --- | --- | --- | ------ | ------------ | -------- | --- | ---------- | ------ | -------------- | --- |
KSWIN Kolmogorov-SmirnovWindowing. Energies,vol.14,no.20,p.6763,Oct.2021,doi:10.3390/en14206763.
KELM KernelExtremeLearningMachine. [2] O. B. Sezer, M. U. Gudelek, and A. M. Ozbayoglu, ‘‘Financial time
LR LogisticRegression. seriesforecastingwithdeeplearning:Asystematicliteraturereview:
2005–2019,’’Appl.SoftComput.,vol.90,May2020,Art.no.106181,
| KRR | KernelRidgeRegression. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1016/j.asoc.2020.106181.
| LSTM | LongShort-TermMemory. |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[3] A.Blázquez-García,A.Conde,U.Mori,andJ.A.Lozano,‘‘Areview
Learn++.CDS Learn++ for Concept Drift with onoutlier/anomalydetectionintimeseriesdata,’’ACMComput.Surveys,
vol.54,no.3,pp.1–33,Apr.2021,doi:10.1145/3444690.
SMOTE.
[4] R.C.CavalcanteandA.L.I.Oliveira,‘‘Anapproachtohandleconcept
| MAE | MeanAbsoluteError. |     |     |     |       |             |             |         |         |                  |     |     |
| --- | ------------------ | --- | --- | --- | ----- | ----------- | ----------- | ------- | ------- | ---------------- | --- | --- |
|     |                    |     |     |     | drift | infinancial | time series | basedon | extreme | learningmachines |     | and |
MAPE MeanAbsolutePercentageError. explicitdriftdetection,’’inProc.Int.JointConf.NeuralNetw.(IJCNN),
MSE MeanSquaredError. Jul.2015,pp.1–8,doi:10.1109/IJCNN.2015.7280721.
MED MedianAbsoluteError. [5] A. S. Iwashita and J. P. Papa, ‘‘An overview on concept drift
|     |     |     |     |     | learning,’’ | IEEE | Access, | vol. | 7, pp.1532–1547, |     | 2019, | doi: |
| --- | --- | --- | --- | --- | ----------- | ---- | ------- | ---- | ---------------- | --- | ----- | ---- |
MOS-ELM Meta-Cognitive Online Sequential 10.1109/ACCESS.2018.2886026.
ExtremeLearningMachine. [6] H. Guo, S. Zhang, and W. Wang, ‘‘Selective ensemble-based
|     |                        |     |     |     | online  | adaptive | deep neural   | networks | for  | streaming   | data | with  |
| --- | ---------------------- | --- | --- | --- | ------- | -------- | ------------- | -------- | ---- | ----------- | ---- | ----- |
| MLP | Multi-LayerPerceptron. |     |     |     |         |          |               |          |      |             |      |       |
|     |                        |     |     |     | concept | drift,’’ | Neural Netw., | vol.     | 142, | pp.437–456, | Oct. | 2021, |
MDDT MultiscaleDriftDetectionTest. doi:10.1016/j.neunet.2021.06.027.
MSPE MeanSquaredPredictionError. [7] B.Feng,Y.Gu,H.Yu,X.Yang,andS.Gao,‘‘DME:Anadaptiveandjust-
in-timeweightedensemblelearningmethodforclassifyingblock-based
| MASE | Meanabsolutescalederror. |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conceptdriftsteam,’’IEEEAccess,vol.10,pp.120578–120591,2022,
| MCC | Matthew’scorrelationcoefficient. |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1109/ACCESS.2022.3222178.
NN NeuralNetworks. [8] B.Heidrich,N.Ludwig,M.Turowski,R.Mikut,andV.Hagenmeyer,
NB NaiveBayes. ‘‘Adaptivelycopingwithconceptdriftsinenergytimeseriesforecasting
|     |                            |     |     |     | using | profiles,’’ | in Proc. | 13th ACM | Int. Conf. | Future | Energy | Syst., |
| --- | -------------------------- | --- | --- | --- | ----- | ----------- | -------- | -------- | ---------- | ------ | ------ | ------ |
| NDE | NumberandDistanceofErrors. |     |     |     |       |             |          |          |            |        |        |        |
Jun.2022,pp.459–470,doi:10.1145/3538637.3539759.
NRMSD Normalized Root-Mean-Square Devia- [9] K.Rahmani,R.Thapa,P.Tsou,S.CasieChetty,G.Barnes,C.Lam,
tion. and C. Foon Tso, ‘‘Assessing the effects of data drift on the perfor-
OAUE OnlineAccuracyUpdatedEnsemble. manceofmachinelearningmodelsusedinclinicalsepsisprediction,’’
|     |                          |     |     |     | Int.                            | J. Med. | Informat., vol. | 173, | May 2023, | Art.no.104930, |     | doi: |
| --- | ------------------------ | --- | --- | --- | ------------------------------- | ------- | --------------- | ---- | --------- | -------------- | --- | ---- |
| PNN | PerceptronNeuralNetwork. |     |     |     | 10.1016/j.ijmedinf.2022.104930. |         |                 |      |           |                |     |      |
PHT Page-HinkleyTest. [10] X. Zhang, Y. Xue, X. Su, S. Chen, K. Liu, W. Chen, M. Liu, and
Y.Hu,‘‘Atransferlearningapproachtocorrectthetemporalperformance
| RMSE | RootMeanSquareError.            |     |     |     |                |                                        |          |              |       |                    |             |      |
| ---- | ------------------------------- | --- | --- | --- | -------------- | -------------------------------------- | -------- | ------------ | ----- | ------------------ | ----------- | ---- |
|      |                                 |     |     |     | driftof        | clinicalpredictionmodels:Retrospective |          |              |       | cohortstudy,’’JMIR |             |      |
| RCA  | RootCauseAnalysis.              |     |     |     |                |                                        |          |              |       |                    |             |      |
|      |                                 |     |     |     | Med.           | Informat.,                             | vol. 10, | no. 11, Nov. | 2022, | Art.               | no. e38053, | doi: |
| ROC  | ReceiverOperatorCharacteristic. |     |     |     | 10.2196/38053. |                                        |          |              |       |                    |             |      |
[11] S.S.Dongre,L.G.Malik,andA.Thomas,‘‘Detectingconceptdriftusing
| RNN | RecurrentNeuralNetwork. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HEDDMindatastream,’’Int.J.Intell.Eng.Informat.,vol.7,nos.2–3,
| RF  | RandomForest. |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p.164,Jan.2019,doi:10.1504/ijiei.2019.099087.
| 119406 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
[12] D. Mulimani, S. G. Totad, P. Patil, and S. V. Seeri, ‘‘Adaptive [33] T. Mahmood and T. Fatima, ‘‘Concept drift in streaming data: A
ensemblelearningwithconceptdriftdetectionforintrusiondetection,’’ systematicliteraturereview,’’KIETJ.Comput.Inf.Sci.,vol.4,no.1,
| inProc.DataEng.Intell.Comput.,Jan.2021,pp.331–339. |     |     |     |     |     |     |     | p.17,Jan.2021. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
[13] J.Quionero-Candela,M.Sugiyama,A.Schwaighofer,andN.Lawrence, [34] M. Lima, M. Neto, T. S. Filho, and R. A. De A. Fagundes,
‘‘Datasetshiftinmachinelearning,’’MassachusettsInst.Technol.,USA, ‘‘Learning under concept drift for regression—A systematic litera-
|     |     |     |     |     |     |     |     | ture | review,’’ | IEEE | Access, | vol. 10, | pp.45410–45429, |     | 2022, doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---- | ------- | -------- | --------------- | --- | ---------- |
Tech.Rep.,Jan.2009.
[14] F. Bayram, B. S. Ahmed, and A. Kassler, ‘‘From concept drift to 10.1109/ACCESS.2022.3169785.
modeldegradation:Anoverviewonperformance-awaredriftdetectors,’’ [35] K. S. Desale and S. Shinde, ‘‘Addressing concept drifts using deep
Knowledge-Based Syst., vol. 245, Jun. 2022, Art.no.108632, doi: learningforheartdiseaseprediction:Areview,’’inProc.2ndDoctoral
10.1016/j.knosys.2022.108632. Symp.Comput.Intell.,Sep.2021,pp.157–167.
|     |     |     |     |     |     |     |     | [36] N. B. | Ghatage | and | P. D. Patil, | ‘‘Evolving | time | series data | streams: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | ------------ | ---------- | ---- | ----------- | -------- |
[15] M.Ceci,R.Corizzo,N.Japkowicz,P.Mignone,andG.Pio,‘‘ECHAD:
|                 |          |              |           |                      |              |       |           | A review,’’ |     | in Proc. | Smart | Trends | Comput. | Commun., | Jan. 2023, |
| --------------- | -------- | ------------ | --------- | -------------------- | ------------ | ----- | --------- | ----------- | --- | -------- | ----- | ------ | ------- | -------- | ---------- |
| Embedding-based |          | change       | detection | from                 | multivariate | time  | series in |             |     |          |       |        |         |          |            |
| smart           | grids,’’ | IEEE Access, | vol.      | 8, pp.156053–156066, |              | 2020, | doi:      | pp.93–101.  |     |          |       |        |         |          |            |
10.1109/ACCESS.2020.3019095. [37] A. L. Suárez-Cetrulo, D. Quintana, and A. Cervantes, ‘‘A survey
[16] F.BattagliaandM.K.Protopapas,‘‘Multi–regimemodelsfornonlinear on machine learning for recurring concept drifting data streams,’’
|     |     |     |     |     |     |     |     | Expert | Syst. | Appl., | vol. 213, | Mar. | 2023, | Art.no.118934, | doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------ | --------- | ---- | ----- | -------------- | ---- |
nonstationarytimeseries,’’Comput.Statist.,vol.27,no.2,pp.319–341,
10.1016/j.eswa.2022.118934.
Jun.2012,doi:10.1007/s00180-011-0259-z.
[17] Z. Lu, J. Xia, M. Wang, Q. Nie, and J. Ou, ‘‘Short-term traffic [38] V. P. M. Goncalves, L. P. Silva, F. L. S. Nunes, J. E. Ferreira, and
flow forecasting via multi-regime modeling and ensemble learning,’’ L. V. Araújo, ‘‘Concept drift adaptation in video surveillance: A sys-
Appl.Sci.,vol.10,no.1,p.356,Jan.2020,doi:10.3390/app10010356. tematicreview,’’MultimediaToolsAppl.,vol.83,no.4,pp.9997–10037,
Jan.2024,doi:10.1007/s11042-023-15855-3.
[18] E.Uchiteleva,S.L.Primak,M.Luccini,A.R.Hussein,andA.Shami,
|     |     |     |     |     |     |     |     | [39] R.Mohandas,M.Southern,E.O’Connell,andM.Hayes,‘‘Asurveyof |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
‘‘TheTriLSapproachfordrift-awaretime-seriespredictioninIIoTenvi-
incrementaldeeplearningfordefectdetectioninmanufacturing,’’Big
ronment,’’IEEETrans.Ind.Informat.,vol.18,no.10,pp.6581–6591,
Oct.2022,doi:10.1109/TII.2021.3129825. DataCogn.Comput.,vol.8,no.1,p.7,Jan.2024.
[19] P. K. Shen, Y. Ming, H. Li, J. Gao, and W. Zhang, ‘‘Unsupervised [40] N.R.Haddaway,M.J.Page,C.C.Pritchard,andL.A.McGuinness,
‘‘PRISMA2020:AnRpackageandshinyappforproducingPRISMA
conceptdriftdetectors:Asurvey,’’inProc.Adv.NaturalComput.,Fuzzy
2020-compliantflowdiagrams,withinteractivityforoptimiseddigital
Syst.Knowl.Discovery,Jan.2023,pp.1117–1124.
|     |     |     |     |     |     |     |     | transparency |     | and open | synthesis,’’ | Campbell | Systematic | Rev., | vol. 18, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------ | -------- | ---------- | ----- | -------- |
[20] M.Han,Z.Chen,M.Li,H.Wu,andX.Zhang,‘‘Asurveyofactiveand
no.2,p.1230,Jun.2022,doi:10.1002/cl2.1230.
passiveconceptdrifthandlingmethods,’’Comput.Intell.,vol.38,no.4,
pp.1492–1535,Aug.2022,doi:10.1111/coin.12520. [41] M.J.Pageetal.,‘‘ThePRISMA2020statement:Anupdatedguideline
forreportingsystematicreviews,’’BMJ,vol.372,p.71,Mar.2021,doi:
| [21] R. N. | Gemaque, | A. F. J. | Costa, | R. Giusti, | and E. | M. Dos | Santos, |     |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ------ | ---------- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.1136/bmj.n71.
‘‘Anoverviewofunsuperviseddriftdetectionmethods,’’WIREsData
|        |        |            |      |            |         |            |      | [42] B.KitchenhamandS.Charters,‘‘Guidelinesforperformingsystematic |         |     |          |                |       |             |       |
| ------ | ------ | ---------- | ---- | ---------- | ------- | ---------- | ---- | ------------------------------------------------------------------ | ------- | --- | -------- | -------------- | ----- | ----------- | ----- |
| Mining | Knowl. | Discovery, | vol. | 10, no. 6, | p.1381, | Nov. 2020, | doi: |                                                                    |         |     |          |                |       |             |       |
|        |        |            |      |            |         |            |      | literature                                                         | reviews | in  | software | engineering,’’ | Keele | University, | U.K., |
10.1002/widm.1381.
Tech.Rep.EBSE-2007-01,2007.
[22] P. A. Nayak, P. Sriganesh, K. M. Rakshitha, M. V. Manoj Kumar, [43] M.G.Ragab,S.J.Abdulkadir,A.Muneer,A.Alqushaibi,E.H.Sumiea,
B.S.Prashanth,andH.R.Sneha,‘‘Literaturereviewonphenomenon
|            |        |               |             |               |            |          |       | R. Qureshi, |        | S. M. Al-Selwi, |      | and H.      | Alhussian,      | ‘‘A comprehensive |            |
| ---------- | ------ | ------------- | ----------- | ------------- | ---------- | -------- | ----- | ----------- | ------ | --------------- | ---- | ----------- | --------------- | ----------------- | ---------- |
| of concept |        | drift and its | handling    | approaches,’’ |            | in Proc. | Asian |             |        |                 |      |             |                 |                   |            |
|            |        |               |             |               |            |          |       | systematic  | review | of              | YOLO | for medical | object          | detection         | (2018      |
| Conf.      | Innov. | Technol.      | (ASIANCON), |               | Aug. 2021, | pp.1–7,  | doi:  |             |        |                 |      |             |                 |                   |            |
|            |        |               |             |               |            |          |       | to 2023),’’ |        | IEEE Access,    |      | vol. 12,    | pp.57815–57836, |                   | 2024, doi: |
10.1109/ASIANCON51346.2021.9544693.
10.1109/ACCESS.2024.3386826.
[23] L. Poenaru-Olaru, L. Cruz, A. van Deursen, and J. S. Rellermeyer, [44] S.M.Al-Selwi,M.F.Hassan,S.J.Abdulkadir,A.Muneer,E.H.Sumiea,
‘‘Areconceptdriftdetectorsreliablealarmingsystems—Acomparative
A.Alqushaibi,andM.G.Ragab,‘‘RNN-LSTM:Fromapplicationsto
| study,’’ | in Proc. | IEEE Int. | Conf. | Big Data | (Big | Data), Dec. | 2022, |          |            |     |                       |     |           |     |           |
| -------- | -------- | --------- | ----- | -------- | ---- | ----------- | ----- | -------- | ---------- | --- | --------------------- | --- | --------- | --- | --------- |
|          |          |           |       |          |      |             |       | modeling | techniques |     | and beyond—Systematic |     | review,’’ | J.  | King Saud |
pp.3364–3373,doi:10.1109/BigData55660.2022.10020292.
Univ.-Comput.Inf.Sci.,vol.36,no.5,Jun.2024,Art.no.102068,doi:
[24] M.KarimianandH.Beigy,‘‘Conceptdrifthandling:Adomainadaptation
10.1016/j.jksuci.2024.102068.
perspective,’’ExpertSyst.Appl.,vol.224,Aug.2023,Art.no.119946, [45] M. Abdullahi, Y. Baashar, H. Alhussian, A. Alwadain, N. Aziz,
doi:10.1016/j.eswa.2023.119946. L. F. Capretz, and S. J. Abdulkadir, ‘‘Detecting cybersecurity attacks
| [25] J. Gama, | I.  | Žliobaite˙, A. | Bifet, | M. Pechenizkiy, | and | A. Bouchachia, |     |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | ------ | --------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inInternetofThingsusingartificialintelligencemethods:Asystematic
‘‘Asurveyonconceptdriftadaptation,’’ACMComput.Surveys,vol.46,
|     |     |     |     |     |     |     |     | literature | review,’’ | Electronics, |     | vol. 11, | no. 2, p.198, | Jan. | 2022, doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------ | --- | -------- | ------------- | ---- | ---------- |
no.4,pp.1–37,Mar.2014,doi:10.1145/2523813.
10.3390/electronics11020198.
[26] T.R.Hoens,R.Polikar,andN.V.Chawla,‘‘Learningfromstreaming [46] H.Mehmood,A.Khalid,P.Kostakos,E.Gilman,andS.Pirttikangas,
datawithconceptdriftandimbalance:Anoverview,’’Prog.Artif.Intell., ‘‘A novel edge architecture and solution for detecting concept drift
vol.1,no.1,pp.89–101,Apr.2012,doi:10.1007/s13748-011-0008-0. in smart environments,’’ Future Gener. Comput. Syst., vol. 150,
| [27] T. S. | Guzella | and W. M. | Caminhas, | ‘‘A | review of | machine | learning |     |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | --------- | --- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.127–143,Jan.2024,doi:10.1016/j.future.2023.08.023.
| approaches | to  | spam filtering,’’ |     | Expert Syst. | Appl., | vol. 36, | no. 7, |               |     |        |         |         |        |                    |     |
| ---------- | --- | ----------------- | --- | ------------ | ------ | -------- | ------ | ------------- | --- | ------ | ------- | ------- | ------ | ------------------ | --- |
|            |     |                   |     |              |        |          |        | [47] P. Wang, | H.  | Yu, N. | Jin, D. | Davies, | and W. | L. Woo, ‘‘QuadCDD: |     |
pp.10206–10222,Sep.2009. A quadruple-based approach for understanding concept drift in data
[28] M. M. Gaber, A. Zaslavsky, and S. Krishnaswamy, ‘‘A survey of streams,’’ExpertSyst.Appl.,vol.238,Mar.2024,Art.no.122114,doi:
classification methods in data streams,’’ in Data Streams: Models 10.1016/j.eswa.2023.122114.
and Algorithms. Boston, MA, USA: Springer, 2007, pp.39–59, doi: [48] M.Woźniak,P.Zyblewski,andP.Ksieniewicz,‘‘Activeweightedaging
| 10.1007/978-0-387-47534-9_3. |     |     |     |     |     |     |     |          |     |         |             |                   |     | Inf. Sci., |           |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ----------- | ----------------- | --- | ---------- | --------- |
|                              |     |     |     |     |     |     |     | ensemble | for | drifted | data stream | classification,’’ |     |            | vol. 630, |
[29] S.AminikhanghahiandD.J.Cook,‘‘Asurveyofmethodsfortimeseries pp.286–304,Jun.2023,doi:10.1016/j.ins.2023.02.046.
changepointdetection,’’Knowl.Inf.Syst.,vol.51,no.2,pp.339–367, [49] A.KuppaandN.-A.Le-Khac,‘‘Learntoadapt:Robustdriftdetection
May2017. in security domain,’’ Comput. Electr. Eng., vol. 102, Sep. 2022,
[30] S. Wang, L. L. Minku, and X. Yao, ‘‘A systematic study of online Art.no.108239,doi:10.1016/j.compeleceng.2022.108239.
class imbalance learning with concept drift,’’ IEEE Trans. Neural [50] S.DisabatoandM.Roveri,‘‘Tinymachinelearningforconceptdrift,’’
Netw. Learn. Syst., vol. 29, no. 10, pp.4802–4821, Oct. 2018, doi: IEEETrans.NeuralNetw.Learn.Syst.,vol.35,no.6,pp.8470–8481,
10.1109/TNNLS.2017.2771290. Jun.2024,doi:10.1109/TNNLS.2022.3229897.
[31] R. S. M. D. Barros and S. G. T. D. C. Santos, ‘‘An overview and [51] C.-H.LuandC.-R.Chen,‘‘IoT-enabledstreamingimageanalyticswith
comprehensivecomparisonofensemblesforconceptdrift,’’Inf.Fusion, privacy-awareself-adaptiveandreflectivedesigns,’’IEEESyst.J.,vol.15,
no.1,pp.1214–1223,Mar.2021,doi:10.1109/JSYST.2020.2983057.
vol.52,pp.213–244,Dec.2019,doi:10.1016/j.inffus.2019.03.006.
|            |           |             |     |           |           |       |        | [52] S. Priya | and | R. Annie | Uthra, | ‘‘An effective | concept | drift | detection |
| ---------- | --------- | ----------- | --- | --------- | --------- | ----- | ------ | ------------- | --- | -------- | ------ | -------------- | ------- | ----- | --------- |
| [32] N. L. | A. Ghani, | I. A. Aziz, | and | M. Mehat, | ‘‘Concept | drift | detec- |               |     |          |        |                |         |       |           |
tion on unlabeled data streams: A systematic literature review,’’ in technique with kernel extreme learning machine for email spam
Proc.IEEEConf.BigDataAnalytics(ICBDA),Nov.2020,pp.61–65, filtering,’’inProc.3rdInt.Conf.Intell.Sustain.Syst.(ICISS),Dec.2020,
doi:10.1109/ICBDA50157.2020.9289802. pp.774–779,doi:10.1109/ICISS49785.2020.9316055.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 119407 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
[53] P. Duda, K. Przybyszewski, and L. Wang, ‘‘A novel drift detection [71] L.Sun,Y.Ji,M.Zhu,F.Gu,F.Dai,andK.Li,‘‘Anewpredictivemethod
algorithm based on features’ importance analysis in a data streams supportingstreamingdatawithhybridrecurringconceptdriftsinprocess
environment,’’ J. Artif. Intell. Soft Comput. Res., vol. 10, no. 4, industry,’’Comput.Ind.Eng.,vol.161,Nov.2021,Art.no.107625,doi:
pp.287–298,Oct.2020,doi:10.2478/jaiscr-2020-0019. 10.1016/j.cie.2021.107625.
[54] P. Ksieniewicz, M. Woźniak, B. Cyganek, A. Kasprzak, and [72] R.Mohawesh,S.Tran,R.Ollington,andS.Xu,‘‘Analysisofconcept
K. Walkowiak, ‘‘Data stream classification using active learned driftinfakereviewsdetection,’’ExpertSyst.Appl.,vol.169,May2021,
neuralnetworks,’’Neurocomputing,vol.353,pp.74–82,Aug.2019,doi: Art.no.114318,doi:10.1016/j.eswa.2020.114318.
10.1016/j.neucom.2018.05.130. [73] M. Jain and G. Kaur, ‘‘Distributed anomaly detection using concept
[55] D.Han,C.Giraud-Carrier,andS.Li,‘‘Efficientminingofhigh-speed driftdetectionbasedhybridensembletechniquesinstreamednetwork
uncertain data streams,’’ Appl. Intell., vol. 43, no. 4, pp.773–785, data,’’ClusterComput.,vol.24,no.3,pp.2099–2114,Sep.2021,doi:
Dec.2015,doi:10.1007/s10489-015-0675-9. 10.1007/s10586-021-03249-9.
[56] D. M. Farid, L. Zhang, A. Hossain, C. M. Rahman, R. Strachan, [74] X. Xie, Z. Jin, J. Wang, L. Yang, Y. Lu, and T. Li, ‘‘Confidence
|     |     |     |     |     |     |     | guided | anomaly | detection | model for anti-concept | drift in | dynamic |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --------- | ---------------------- | -------- | ------- |
G.Sexton,andK.Dahal,‘‘Anadaptiveensembleclassifierformining
concept drifting data streams,’’ Expert Syst. Appl., vol. 40, no. 15, logs,’’J.Netw.Comput.Appl.,vol.162,Jul.2020,Art.no.102659,doi:
pp.5895–5906,Nov.2013,doi:10.1016/j.eswa.2013.05.001. 10.1016/j.jnca.2020.102659.
[57] W. Grote-Ramm, D. Lanuschny, F. Lorenzen, M. Oliveira Brito, and [75] N. A. Huynh, W. K. Ng, and K. Ariyapala, ‘‘Learning under con-
F.Schönig,‘‘Continuallearningforneuralregressionnetworkstocope cept drift with follow the regularized leader and adaptive decaying
|              |       |               |           |       |                        |     | proximal,’’ | Expert | Syst. Appl., | vol. 96, pp.49–63, | Apr. 2018, | doi: |
| ------------ | ----- | ------------- | --------- | ----- | ---------------------- | --- | ----------- | ------ | ------------ | ------------------ | ---------- | ---- |
| with concept | drift | in industrial | processes | using | convex optimisation,’’ |     |             |        |              |                    |            |      |
10.1016/j.eswa.2017.11.042.
| Eng. Appl. | Artif. | Intell., vol. | 120, Apr. | 2023, | Art.no.105927, | doi: |     |     |     |     |     |     |
| ---------- | ------ | ------------- | --------- | ----- | -------------- | ---- | --- | --- | --- | --- | --- | --- |
10.1016/j.engappai.2023.105927. [76] P.SidhuandM.P.S.Bhatia,‘‘Anonlineensemblesapproachforhandling
conceptdriftindatastreams:Diversifiedonlineensemblesdetection,’’
[58] Y.Lyu,H.Li,M.Sayagh,Z.M.Jiang,andA.E.Hassan,‘‘Anempirical
study of the impact of data splitting decisions on the performance of Int.J.Mach.Learn.Cybern.,vol.6,no.6,pp.883–909,Dec.2015,doi:
AIOpssolutions,’’ACMTrans.Softw.Eng.Methodology,vol.30,no.4, 10.1007/s13042-015-0366-1.
[77] D.BrzezinskiandJ.Stefanowski,‘‘Combiningblock-basedandonline
pp.1–38,Jul.2021,doi:10.1145/3447876.
|                |     |                  |     |                   |     |            | methods | in learning | ensembles | from concept | drifting data | streams,’’ |
| -------------- | --- | ---------------- | --- | ----------------- | --- | ---------- | ------- | ----------- | --------- | ------------ | ------------- | ---------- |
| [59] F. Savva, | C.  | Anagnostopoulos, | and | P. Triantafillou, |     | ‘‘Adaptive |         |             |           |              |               |            |
Inf.Sci.,vol.265,pp.50–67,May2014,doi:10.1016/j.ins.2013.12.011.
| learning | of aggregate | analytics | under | dynamic | workloads,’’ | Future |     |     |     |     |     |     |
| -------- | ------------ | --------- | ----- | ------- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
[78] K.Waiyamai,T.Kangkachit,B.Saengthongloun,andT.Rakthanmanon,
| Gener. | Comput. | Syst., vol. | 109, pp.317–330, |     | Aug. | 2020, doi: |     |     |     |     |     |     |
| ------ | ------- | ----------- | ---------------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
10.1016/j.future.2020.03.063. ‘‘ACCD:Associativeclassificationoverconcept-driftingdatastreams,’’
[60] B. Dong, Y. Li, Y. Gao, A. Haque, L. Khan, and M. M. Masud, in Proc. Mach. Learn. Data Mining Pattern Recognit., Jan. 2014,
pp.78–90.
‘‘Multistreamregressionwithasynchronousconceptdriftdetection,’’in
[79] A.S.Palli,J.Jaafar,H.M.Gomes,M.A.Hashmani,andA.R.Gilal,
Proc.IEEEInt.Conf.BigData(BigData),Dec.2017,pp.596–605,doi:
|     |     |     |     |     |     |     | ‘‘An | experimental | analysis | of drift detection | methods on multi-class |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | -------- | ------------------ | ---------------------- | --- |
10.1109/BIGDATA.2017.8257975.
imbalanceddatastreams,’’Appl.Sci.,vol.12,no.22,p.11688,Nov.2022,
[61] D.Kaminskyi,B.Li,andE.Müller,‘‘Reconstruction-basedunsupervised
doi:10.3390/app122211688.
| drift detection |     | over multivariate | streaming | data,’’ | in  | Proc. IEEE |     |     |     |     |     |     |
| --------------- | --- | ----------------- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Int.Conf.DataMiningWorkshops(ICDMW),Nov.2022,pp.807–813, [80] H.Qiao,B.Novikov,andJ.O.Blech,‘‘Conceptdriftanalysisbydynamic
residualprojectionforeffectivelydetectingbotnetcyber-attacksinIoT
doi:10.1109/ICDMW58026.2022.00109.
scenarios,’’IEEETrans.Ind.Informat.,vol.18,no.6,pp.3692–3701,
[62] W.Liu,C.Zhu,Z.Ding,H.Zhang,andQ.Liu,‘‘Multiclassimbalanced
Jun.2022,doi:10.1109/TII.2021.3108464.
| and concept | drift | network | traffic classification |     | framework | based on |     |     |     |     |     |     |
| ----------- | ----- | ------- | ---------------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- |
[81] A.Saadallah,M.Jakobs,andK.Morik,‘‘Explainableonlineensembleof
| online | active learning,’’ | Eng. | Appl. Artif. | Intell., | vol. 117, | Jan. 2023, |     |     |     |     |     |     |
| ------ | ------------------ | ---- | ------------ | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
deepneuralnetworkpruningfortimeseriesforecasting,’’Mach.Learn.,
Art.no.105607,doi:10.1016/j.engappai.2022.105607. vol. 111, no. 9, pp.3459–3487, Sep. 2022, doi: 10.1007/s10994-022-
| [63] B. M. | Alencar, | J. P. Canário,    | R. Lobão | Neto, | C. Prazeres, | A. Bifet, | 06218-4. |     |     |     |     |     |
| ---------- | -------- | ----------------- | -------- | ----- | ------------ | --------- | -------- | --- | --- | --- | --- | --- |
| and R.     | A. Rios, | ‘‘Fog-DeepStream: |          | A new | approach     | combining |          |     |     |     |     |     |
[82] X.Wang,Q.Kang,M.Zhou,L.Pan,andA.Abusorrah,‘‘Multiscale
| LSTM | and concept | drift for | data stream | analytics | on  | fog com- |     |     |     |     |     |     |
| ---- | ----------- | --------- | ----------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
driftdetectiontesttoenablefastlearninginnonstationaryenvironments,’’
| puting,’’                  | Internet | Things, vol. | 22, Jul. | 2023, | Art.no.100731, | doi: |                            |                 |      |                          |            |      |
| -------------------------- | -------- | ------------ | -------- | ----- | -------------- | ---- | -------------------------- | --------------- | ---- | ------------------------ | ---------- | ---- |
|                            |          |              |          |       |                |      | IEEE                       | Trans. Cybern., | vol. | 51, no. 7, pp.3483–3495, | Jul. 2021, | doi: |
| 10.1016/j.iot.2023.100731. |          |              |          |       |                |      | 10.1109/TCYB.2020.2989213. |                 |      |                          |            |      |
[64] J.Tang,K.-Y.Lin,andL.Li,‘‘Usingdomainadaptationforincremental [83] H. Gâlmeanu and R. Andonie, ‘‘Concept drift adaptation with
SVMclassificationofdriftdata,’’Mathematics,vol.10,no.19,p.3579, incremental–decremental SVM,’’ Appl. Sci., vol. 11, no. 20, p.9644,
Sep.2022,doi:10.3390/math10193579.
Oct.2021,doi:10.3390/app11209644.
[65] D.Mulimani,S.G.Kanakaraddi,S.G.Totad,andP.R.Patil,‘‘Weighted [84] R.S.M.D.Barros,J.I.G.Hidalgo,andD.R.D.L.Cabral,‘‘Wilcoxon
| averaging | ensemble | model | for concept | drift adaptation |     | in streaming |     |     |     |     |     |     |
| --------- | -------- | ----- | ----------- | ---------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
ranksumtestdriftdetector,’’Neurocomputing,vol.275,pp.1954–1963,
data,’’inProc.2ndInt.Conf.Intell.Technol.(CONIT),Jun.2022,pp.1–8, Jan.2018,doi:10.1016/j.neucom.2017.10.051.
doi:10.1109/CONIT55038.2022.9848151. [85] Q.Huang,D.Yang,L.Jiang,H.Zhang,H.Liu,andK.Kotani,‘‘Anovel
[66] F. Hinder, V. Vaquet, J. Brinkrolf, A. Artelt, and B. Hammer, unsupervisedadaptivelearningmethodforlong-termelectromyography
‘‘Localizationofconceptdrift:Identifyingthedriftingdatapoints,’’in (EMG)patternrecognition,’’Sensors,vol.17,no.6,p.1370,Jun.2017,
| Proc. | Int. Joint | Conf. Neural | Netw. (IJCNN), | Jul. | 2022, | pp.1–9, doi: |     |     |     |     |     |     |
| ----- | ---------- | ------------ | -------------- | ---- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
doi:10.3390/s17061370.
10.1109/IJCNN55064.2022.9892374.
|     |     |     |     |     |     |     | [86] P. Kumari | and | M. Saini, ‘‘Anomaly | detection | in audio with | concept |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------- | --------- | ------------- | ------- |
[67] O. Abdel Wahab, ‘‘Intrusion detection in the IoT under data and driftusingdynamicHuffmancoding,’’IEEESensorsJ.,vol.22,no.17,
conceptdrifts:Onlinedeeplearningapproach,’’IEEEInternetThings pp.17126–17138,Sep.2022,doi:10.1109/JSEN.2022.3193969.
J.,vol.9,no.20,pp.19706–19716,Oct.2022,doi:10.1109/JIOT.2022. [87] X. Zheng, P. Li, X. Hu, and K. Yu, ‘‘Semi-supervised classification
3167005. on data streams with recurring concept drift and concept evolu-
[68] H. Yu, Q. Zhang, T. Liu, J. Lu, Y. Wen, and G. Zhang, ‘‘Meta- tion,’’ Knowl.-Based Syst., vol. 215, Mar. 2021, Art.no.106749, doi:
| ADD: | A meta-learning | based | pre-trained | model | for concept | drift |     |     |     |     |     |     |
| ---- | --------------- | ----- | ----------- | ----- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
10.1016/j.knosys.2021.106749.
| active | detection,’’ | Inf. Sci., | vol. 608, | pp.996–1009, | Aug. | 2022, doi: |            |         |              |           |               |          |
| ------ | ------------ | ---------- | --------- | ------------ | ---- | ---------- | ---------- | ------- | ------------ | --------- | ------------- | -------- |
|        |              |            |           |              |      |            | [88] M. M. | Idrees, | L. L. Minku, | F. Stahl, | and A. Badii, | ‘‘A het- |
10.1016/j.ins.2022.07.022. erogeneous online learning ensemble for non-stationary environ-
[69] J. Yin, M. Tang, J. Cao, H. Wang, and M. You, ‘‘A real-time ments,’’Knowl.-BasedSyst.,vol.188,Jan.2020,Art.no.104983,doi:
dynamic concept adaptive learning algorithm for exploitability pre- 10.1016/j.knosys.2019.104983.
diction,’’ Neurocomputing, vol. 472, pp.252–265, Feb. 2022, doi: [89] M. M. W. Yan, ‘‘Accurate detecting concept drift in evolving data
10.1016/j.neucom.2021.01.144.
|     |     |     |     |     |     |     | streams,’’ | ICT | Exp., vol. | 6, no. 4, pp.332–338, | Dec. 2020, | doi: |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --------------------- | ---------- | ---- |
10.1016/j.icte.2020.05.011.
| [70] M. Jain, | G. Kaur, | and V. Saxena, | ‘‘A | K-means | clustering | and SVM |     |     |     |     |     |     |
| ------------- | -------- | -------------- | --- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
based hybrid concept drift detection technique for network anomaly [90] J. I. G. Hidalgo, L. M. P. Mariño, and R. S. M. D. Barros, ‘‘Cosine
detection,’’ExpertSyst.Appl.,vol.193,May2022,Art.no.116510,doi: similarity drift detector,’’ in Proc. Artif. Neural Netw. Mach. Learn.,
| 10.1016/j.eswa.2022.116510. |     |     |     |     |     |     | Jan.2019,pp.669–685. |     |     |     |               |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ------------- | --- |
| 119408                      |     |     |     |     |     |     |                      |     |     |     | VOLUME13,2025 |     |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
[91] D.R.D.L.CabralandR.S.M.D.Barros,‘‘Conceptdriftdetectionbased [112] Z.Yang,S.Al-Dahidi,P.Baraldi,E.Zio,andL.Montelatici,‘‘Anovel
onFisher’sexacttest,’’Inf.Sci.,vols.442–443,pp.220–234,May2018, conceptdriftdetectionmethodforincrementallearninginnonstationary
doi:10.1016/j.ins.2018.02.054. environments,’’IEEETrans.NeuralNetw.Learn.Syst.,vol.31,no.1,
[92] B.MirzaandZ.Lin,‘‘Meta-cognitiveonlinesequentialextremelearning pp.309–320,Jan.2020,doi:10.1109/TNNLS.2019.2900956.
machineforimbalancedandconcept-driftingdataclassification,’’Neural [113] S.Saurav,P.Malhotra,T.V.Vishnu,N.Gugulothu,L.Vig,P.Agarwal,
|     |     |     |     |     |     |     | and G. | Shroff, | ‘‘Online anomaly | detection | with | concept drift | adap- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------------- | --------- | ---- | ------------- | ----- |
Netw.,vol.80,pp.79–94,Aug.2016,doi:10.1016/j.neunet.2016.04.008.
[93] M. Dehghan, H. Beigy, and P. ZareMoodi, ‘‘A novel concept drift tation using recurrent neural networks,’’ in Proc. ACM India Joint
detectionmethodindatastreamsusingensembleclassifiers,’’Intell.Data Int. Conf. Data Sci. Manage. Data, Jan. 2018, pp.78–87, doi:
Anal.,vol.20,no.6,pp.1329–1350,Nov.2016,doi:10.3233/ida-150207. 10.1145/3152494.3152501.
[94] A. Pesaranghader and H. L. Viktor, ‘‘Fast Hoeffding drift detection [114] F.Pinagé,E.M.DosSantos,andJ.Gama,‘‘Adriftdetectionmethod
basedondynamicclassifierselection,’’DataMiningKnowl.Discovery,
methodforevolvingdatastreams,’’inProc.Mach.Learn.Knowl.Dis-
vol.34,no.1,pp.50–74,Jan.2020,doi:10.1007/s10618-019-00656-w.
coveryDatabases,Jan.2016,pp.96–111.
[95] Y. Sakamoto, K.-I. Fukui, J. Gama, D. Nicklas, K. Moriyama, and [115] J.Lu,A.Liu,F.Dong,F.Gu,J.Gama,andG.Zhang,‘‘Learningunder
M.Numao,‘‘Conceptdriftdetectionwithclusteringviastatisticalchange conceptdrift:Areview,’’IEEETrans.Knowl.DataEng.,vol.31,no.12,
detection methods,’’ in Proc. 7th Int. Conf. Knowl. Syst. Eng. (KSE), pp.2346–2363,Dec.2019,doi:10.1109/TKDE.2018.2876857.
[116] M.Han,D.Mu,A.Li,S.Liu,andZ.Gao,‘‘Conceptdriftdetectionmeth-
Oct.2015,pp.37–42,doi:10.1109/KSE.2015.19.
odsbasedondifferentweightingstrategies,’’Int.J.Mach.Learn.Cybern.,
| [96] I.            | Frías-Blanco, | J.            | D.        | Campo-Ávila,           | G.Ramos-Jiménez, |                |          |         |               |      |            |                     |     |
| ------------------ | ------------- | ------------- | --------- | ---------------------- | ---------------- | -------------- | -------- | ------- | ------------- | ---- | ---------- | ------------------- | --- |
|                    |               |               |           |                        |                  |                | vol. 15, | no. 10, | pp.4709–4732, | Oct. | 2024, doi: | 10.1007/s13042-024- |     |
| R.Morales-Bueno,   |               | A.Ortiz-Díaz, |           | and Y. Caballero-Mota, |                  | ‘‘Online       |          |         |               |      |            |                     |     |
| and non-parametric |               | drift         | detection | methods                | based            | on Hoeffding’s | 02186-4. |         |               |      |            |                     |     |
bounds,’’IEEETrans.Knowl.DataEng.,vol.27,no.3,pp.810–823, [117] T. Bartz-Beielstein and L. Hans, ‘‘Drift detection and handling,’’
|     |     |     |     |     |     |     | in Online | Machine | Learning: | A Practical | Guide | With Examples | in  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | ----------- | ----- | ------------- | --- |
Mar.2015,doi:10.1109/TKDE.2014.2345382.
Python.Singapore:Springer,2024,pp.23–39,doi:10.1007/978-981-99-
[97] J.-W.LiaoandB.-R.Dai,‘‘Anensemblelearningapproachforconcept
7007-0_3.
drift,’’inProc.Int.Conf.Inf.Sci.Appl.(ICISA),May2014,pp.1–4,doi:
10.1109/ICISA.2014.6847357. [118] M. N. Fekri, H. Patel, K. Grolinger, and V. Sharma, ‘‘Deep learning
[98] L.Du,Q.Song,andX.Jia,‘‘Detectingconceptdrift:Aninformation for load forecasting with smart meter data: Online adaptive recurrent
neuralnetwork,’’Appl.Energy,vol.282,Jan.2021,Art.no.116177,doi:
entropybasedmethodusinganadaptiveslidingwindow,’’Intell.Data
10.1016/j.apenergy.2020.116177.
Anal.,vol.18,no.3,pp.337–364,Apr.2014,doi:10.3233/ida-140645.
[119] S.AgrahariandA.K.Singh,‘‘Conceptdriftdetectionindatastreammin-
[99] G.DitzlerandR.Polikar,‘‘Incrementallearningofconceptdriftfrom
ing:Aliteraturereview,’’J.KingSaudUniv.-Comput.Inf.Sci.,vol.34,
| streaming | imbalanced | data,’’ | IEEE | Trans. Knowl. | Data | Eng., vol. 25, |     |     |     |     |     |     |     |
| --------- | ---------- | ------- | ---- | ------------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
no.10,pp.2283–2301,Oct.2013,doi:10.1109/TKDE.2012.136. no.10,pp.9523–9540,Nov.2022,doi:10.1016/j.jksuci.2021.11.006.
|     |     |     |     |     |     |     | [120] C. Lalletti | and | S. Teso, ‘‘Spurious |     | correlations in | concept | drift: Can |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------- | --- | --------------- | ------- | ---------- |
[100] M.A.ThalorandS.Patil,‘‘Incrementallearningonnon-stationarydata
explanatoryinteractionhelp?’’2024,arXiv:2407.16515.
streamusingensembleapproach,’’Int.J.Electr.Comput.Eng.,vol.6,
no.4,pp.1811–1817,Aug.2016,doi:10.11591/ijece.v6i4.10255.
| [101] J. Liu | and E.  | Zio, ‘‘A       | SVR-based   | ensemble | approach      | for drifting |     |     |     |     |     |     |     |
| ------------ | ------- | -------------- | ----------- | -------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| data         | streams | with recurring | patterns,’’ | Appl.    | Soft Comput., | vol. 47,     |     |     |     |     |     |     |     |
pp.553–564,Oct.2016,doi:10.1016/j.asoc.2016.06.030.
| [102] L. F. | L. Grim | and A. L. | S. Gradvohl, | ‘‘High-performance |     | ensembles |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | ------------ | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
ofonlinesequentialextremelearningmachineforregressionandtime
| series   | forecasting,’’ | in Proc.    | 30th | Int. Symp. | Comput.     | Archit. High |     |     |          |           |     |           |         |
| -------- | -------------- | ----------- | ---- | ---------- | ----------- | ------------ | --- | --- | -------- | --------- | --- | --------- | ------- |
| Perform. | Comput.        | (SBAC-PAD), |      | Sep. 2018, | pp.394–401, | doi:         |     |     |          |           |     |           |         |
|          |                |             |      |            |             |              |     |     | MUJAHEED | ABDULLAHI |     | (Graduate | Student |
10.1109/CAHPC.2018.8645863.
[103] A. Saadallah, F. Priebe, and K. Morik, ‘‘A drift-based dynamic Member, IEEE) received the B.Sc. degree in
ensemble members selection usingclustering fortime seriesforecast- information technology from Infrastructure Uni-
ing,’’ in Proc. Mach. Learn. Knowl. Discovery Databases, Jan. 2020, versity, Kuala Lumpur, Malaysia, in 2018, and
| pp.678–694. |     |     |     |     |     |     |     |     | theM.Sc.degreeininformationtechnologyfrom |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
[104] D.Boulegane,A.Bifet,H.Elghazel,andG.Madhusudan,‘‘Streaming theUniversitiTeknologiPETRONAS,Malaysia,
| time | series forecasting |     | using multi-target | regression |     | with dynamic |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | ------------------ | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
in2022,whereheiscurrentlypursuingthePh.D.
| ensemble | selection,’’ | in  | Proc. IEEE | Int. Conf. | Big Data | (Big Data), |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ---------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
degreeininformationtechnology.HeisaGraduate
Dec.2020,pp.2170–2179,doi:10.1109/BigData50022.2020.9378264. ResearchAssistant.Hisresearchinterestsinclude
[105] T. Fields, G. Hsieh, and J. Chenou, ‘‘Mitigating drift in time machine learning, data analytics, cybersecurity,
series data with noise augmentation,’’ in Proc. Int. Conf. Com- andtheInternetofThings.
| put. | Sci. Comput. | Intell. | (CSCI), | Dec. 2019, | pp.227–230, | doi: |     |     |     |     |     |     |     |
| ---- | ------------ | ------- | ------- | ---------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
10.1109/CSCI49370.2019.00046.
[106] N.Ramanan,R.Tahmasbi,M.S.Deokwoo,J.Shalini,H.Claudionor,
andN.Coelho.(2021).Real-TimeDriftDetectiononTime-SeriesData.
[Online].Available:https://www.paloaltonetworks.com/
| [107] Y. Xu, | R. Xu,      | W. Yan, | and P.     | Ardis, ‘‘Concept | drift  | learning with  |     |     |     |     |     |     |     |
| ------------ | ----------- | ------- | ---------- | ---------------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
| alternating  | learners,’’ | in      | Proc. Int. | Joint Conf.      | Neural | Netw. (IJCNN), |     |     |     |     |     |     |     |
May2017,pp.2104–2111,doi:10.1109/IJCNN.2017.7966109.
[108] Y.Zhang,G.Chu,P.Li,X.Hu,andX.Wu,‘‘Three-layerconceptdrifting
|     |     |     |     |     |     |     |     |     | HITHAM | ALHUSSIAN | (SeniorMember,IEEE) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ------------------- | --- | --- |
detectionintextdatastreams,’’Neurocomputing,vol.260,pp.393–403,
|     |     |     |     |     |     |     |     |     | received | the B.Sc. | and M.Sc. | degrees | in com- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | ------- | ------- |
Oct.2017,doi:10.1016/j.neucom.2017.04.047.
|     |     |     |     |     |     |     |     |     | puter science | from | the School | of Mathemati- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------- | ------------- | --- |
[109] A.Maaradji,M.Dumas,M.L.Rosa,andA.Ostovar,‘‘Detectingsudden
|     |     |     |     |     |     |     |     |     | cal Sciences, | Khartoum | University, | Sudan, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ----------- | ------ | --- |
andgradualdriftsinbusinessprocessesfromexecutiontraces,’’IEEE the Ph.D. degree from the Universiti Teknologi
Trans.Knowl.DataEng.,vol.29,no.10,pp.2140–2154,Oct.2017,doi:
PETRONAS,Malaysia.HeiscurrentlyaSenior
10.1109/TKDE.2017.2720601.
|     |     |     |     |     |     |     |     |     | Lecturer | with the | Department | of Computer | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---------- | ----------- | --- |
[110] K.S.DesaleandS.V.Shinde,‘‘Conceptdriftdetectionandadaption
InformationSciencesandaCoreResearchMem-
frameworkusingoptimizeddeeplearningandadaptiveslidingwindow
|                     |        |        |          |                 |     |                 |     |     | ber of    | the Centre | for Research | in Data   | Science |
| ------------------- | ------ | ------ | -------- | --------------- | --- | --------------- | --- | --- | --------- | ---------- | ------------ | --------- | ------- |
| approach,’’         | Expert | Syst., | vol. 40, | no. 9, p.13394, |     | Nov. 2023, doi: |     |     |           |            |              |           |         |
| 10.1111/exsy.13394. |        |        |          |                 |     |                 |     |     | (CERDAS), | Universiti | Teknologi    | PETRONAS. |         |
[111] B.D.Horne,J.Nørregaard,andS.Adali,‘‘Robustfakenewsdetection His current research interests include real-time parallel distributed sys-
overtimeandattack,’’ACMTrans.Intell.Syst.Technol.,vol.11,no.1, tems, cloud computing, big data mining, machine learning, and secure
pp.1–23,Dec.2019,doi:10.1145/3363818. computer-basedmanagementsystems.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 119409 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Abdullahietal.:SLRofConceptDriftMitigationinTime-SeriesApplications
NORSHAKIRAH AZIZ received the Diploma ABDUSSALAM AHMED ALASHHAB received
degreeinmanagementtechnology,thebachelor’s the B.Sc. degree in computer networks from
andM.Sc.degreesininformationtechnology(IT), the Faculty of Information Technology, Univer-
andthePh.D.degreeine-business(e-SCM).She sity of Tripoli, Libya, in 2014, and the M.Sc.
iscurrentlyaSeniorLecturerwiththeUniversiti degree (Hons.) in computer networks from the
Teknologi PETRONAS (UTP), Malaysia. She Limkokwing University of Creative Technology,
is also a Researcher with the UTP Centre of Malaysia, in 2017. He is currently pursuing the
ResearchinDataSciences(CeRDaS)andtheData Ph.D. degree with the Computer and Informa-
Governance Leader with the High-Performance tion Sciences Department, Universiti Teknologi
CloudComputingDataCentre(HPCCC).Sheis PETRONAS (UTP), Malaysia. He is a Lec-
a Qualified Technologist. She has a total experience of 19 years in both turer with Alasmarya Islamic University, Libya. His research interests
academic institutions and industry. Her industry working experience is includecybersecurity,software-definednetworking,andmachinelearning
| related to business | intelligence, e-business,  | and IT project | management.          | techniques. |     |     |     |
| ------------------- | -------------------------- | -------------- | -------------------- | ----------- | --- | --- | --- |
| Her research        | interests include business | intelligence,  | data analytics, data |             |     |     |     |
governance,anddigitaladdiction.
|     | SAID JADID     | ABDULKADIR | (Senior Member,    |     |     |     |     |
| --- | -------------- | ---------- | ------------------ | --- | --- | --- | --- |
|     | IEEE) received | the B.Sc.  | degree in computer |     |     |     |     |
sciencefromMoiUniversity,theM.Sc.degreein
|     | computer            | science from the    | Universiti Teknologi |     |     |     |     |
| --- | ------------------- | ------------------- | -------------------- | --- | --- | --- | --- |
|     | Malaysia,           | and the Ph.D.       | degree in informa-   |     |     |     |     |
|     | tion technology     | from the Universiti | Teknologi            |     |     |     |     |
|     | PETRONAS.           | He is currently     | a Senior Lecturer    |     |     |     |     |
|     | with the Department | of Computer         | and Informa-         |     |     |     |     |
tionSciences,UniversitiTeknologiPETRONAS.
Hiscurrentresearchinterestsincludesupervised
machinelearningandpredictiveandstreaminganalytics.Heisservingas
| a Journal Reviewer | for Artificial Intelligence | Review, | IEEE ACCESS, and |     |     |     |     |
| ------------------ | --------------------------- | ------- | ---------------- | --- | --- | --- | --- |
Knowledge-BasedSystems.
|     |     |     |     |     | AFROZA AFRIN   | (Graduate        | Student Member, |
| --- | --- | --- | --- | --- | -------------- | ---------------- | --------------- |
|     |     |     |     |     | IEEE) received | the B.Sc. degree | in computer     |
scienceandengineering(CSE)fromUnitedInter-
|     |     |     |     |     | national University | (UIU), Dhaka, | Bangladesh, |
| --- | --- | --- | --- | --- | ------------------- | ------------- | ----------- |
YAHIA BAASHAR received the B.S. degree in in2023.SheiscurrentlypursuingtheM.Sc.degree
network computing from Coventry University, in information technology with the Computing
in2008,andtheM.S.degreeinMISfromINTI Department, Universiti Teknologi PETRONAS
International University and College, Malaysia, (UTP),SeriIskandar,Perak,Malaysia.Inaddition,
in2010.HeiscurrentlypursuingthePh.D.degree shehasbeenaGraduateResearchAssistant(GRA)
in information technology with the Universiti and a Teaching Assistant (TA) with the CIS
Malaysia Sabah (UMS). His research interests Department, UTP, since 2025. Her research interests include artificial
includetechnologyacceptance,medicalinformat- intelligence,biometrics,cybersecurity,datamining,theIoT,andmachine
|     | ics, e-health, | artificial intelligence, | the IoT, and | learning. |     |     |     |
| --- | -------------- | ------------------------ | ------------ | --------- | --- | --- | --- |
blockchain.
| 119410 |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | ------------- |