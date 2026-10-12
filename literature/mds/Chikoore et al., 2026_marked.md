---
conversion_metadata:
  converted_at: "2026-10-12T07:20:10Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Chikoore et al., 2026.pdf"
  source_pdf_sha256: "cb034b87887cc03b5f75edc3317360ea67326b23261a2ad65da5c20ab48f3ab1"
  page_count: 11
  markdown_char_count: 71972
---

Received7May2026,accepted2June2026,dateofpublication12June2026,dateofcurrentversion18June2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3703181
Adaptive Credit Scoring Model With Concept
Drift Detection and Adaptation Technique for a
Dynamic Environment
RACHAELCHIKOORE ,SUNDAYOLUSEGUNOJO ,ANDOKUTHEPAULKOGEDA
DepartmentofComputerScience,FacultyofInformationandCommunicationTechnology,TshwaneUniversityofTechnology,Pretoria0001,SouthAfrica
DepartmentofInformationTechnology,FacultyofAccountingandInformatics,DurbanUniversityofTechnology,Durban4001,SouthAfrica
SchoolofAgricultureandScience,CollegeofAgriculture,EngineeringandScience,UniversityofKwaZulu-Natal,WestvilleCampus,Durban4000,SouthAfrica
Correspondingauthor:RachaelChikoore(maichicco@gmail.com)
ABSTRACT Despite significant advances in Machine Learning (ML) for Credit Scoring, the persistence
of drift effects manifested as performance degradation due to evolving borrower behaviour, economic
conditions,andshiftingdatadistributionsremainsacriticalchallenge.Associoeconomicconditionschange,
previously learned relationships between input features and target variables become unstable, leading to
concept drift, population drift, and label drift. These dynamics reduce model accuracy and reliability,
increasemisclassificationrates,andexposefinancialinstitutionstosubstantialfinancialandregulatoryrisks.
TraditionalstaticCreditScoringmodelslackmechanismsfordriftdetectionandadaptation,whileexisting
adaptive approaches are largely developed for advanced economies and are not well-suited to developing
contexts.Thisstudyproposesanadaptivecreditscoringframework,termedAdaptiveFusion,designedto
address drift in developing economy environments. The framework integrates baseline ML models with
dynamic adaptation strategies, including retraining, windowing, ensemble learning, and adaptive fusion.
Experimental results demonstrate that the Retrained Random Forest, Ensemble, and Adaptive Fusion
models achieve superior and consistent performance, each attaining an accuracy of 95.0%, a precision
of 0.9275, a recall of 0.9645, an F1-score of 0.9426, and ROC-AUC values exceeding 0.96. Compared
to state-of-the-art models such as the Deep Genetic Hierarchical Network of Learners (DGHNL), which
achieves94.60%accuracyandanAUCof0.9360,theproposedapproachdemonstratesimprovedpredictive
capability, highlighting the effectiveness of dynamic model integration. The Adaptive Fusion algorithm,
whichdynamicallyweightsandintegratesmodeloutputsinrealtime,emergesasthemostrobustsolution,
enabling continuous adaptation to evolving data patterns. These findings underscore the importance of
adaptive,drift-awareframeworksformaintainingaccuracy,fairness,andreliabilityinCreditScoringsystems
operatingindynamicandresource-constrainedenvironments.
INDEXTERMS Adaptivemodel,conceptdrift,creditscoring,machinelearning,prediction.
I. INTRODUCTION Itisparamountthatanentityknowsitscreditstanding.The
Credit scoring estimates the creditworthiness of an individ- scoreactsasaguideonthecharacterofentities;itprovidesa
ual, a corporation, or even a national entity. Credit scores betterdescriptionofthecreditworthinessofanindividualor
arecalculatedbasedonfinancialhistory,currentassets,and organizationbecauseitcombinesdifferentattributes.Having
liabilities.Typically,ittellsalenderorinvestortheprobability the name of an entity is not sufficient to guide one into
ofthesubjectbeingabletopaybackaloan[1]. havingarelationshipwithit.Theideaofcreditscoringisvery
noble,asitwouldgiveabetterdescriptionofentitiesbefore
committingtothem[1].
The associate editor coordinating the review of this manuscript and Thecreditscoringsystemsindifferentcountriesareman-
aged by credit scoring bureaus. The most common scoring
approvingitforpublicationwasFranciscoJ.Garcia-Penalvo .
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
VOLUME14,2026 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ 90365

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
categorizationusesarangeofvaluesandlettersinthealpha- we outline drift detection, drift understanding, and model
bet. If values are used, the smaller the value, the better the adaptationtechniques.SectionIVoutlinesthedesignofthe
creditstanding.LettersofthealphabetrangefromAAAbeing proposedalgorithm.InSectionV,wepresenttheresults,and
excellenttoDbeingpoor[2].Theaveragecreditscorefora SectionVIprovidestheconclusionandfuturework.
countrydoesnotmeanthatallindividualsandorganizations
withinthecountryhavepoorcreditstanding;hence,thereisa II. RESEARCHMETHOD
needforacreditscoringsystemthatshowsindividualcredit Increditscoringsystems,adaptingtoconceptdrift,evolving
scoresforpeopleinacountry. patterns in data over time, is crucial for preserving model
Scoringcanbeperformedforanewapplicanttoestimate accuracy. To address this problem, a range of techniques is
credit risk. Behavioral scoring is based on the client’s pre- employed,suchaswindow-basedapproaches,driftdetection
vious or current credit standing; it is believed that the way algorithms,andensemblemethodsthatdynamicallyadjustto
anindividualhandlesthepreviousorcurrentloanhasadirect changingdata.Theseadaptationstrategiesfallintothreemain
linktotheirfuturebehavior.Collectionscoringisusedtocat- categories: instance-based, model-based, and feature-based,
egorizeclientsintogroupsdependingontheirbehavior.Fraud eachdesignedtohandlebothgradualandsuddenshiftsinthe
detection classifies applicants according to their probability datastreams.Recentresearchhasincorporatedmeta-learning
ofbeingguiltyoffraud[3]. andreinforcementlearningtoanticipateandrespondtodrift
The financial environment is so unstable that the data moreeffectively,strikingabalancebetweentimelydetection
sampleusedtocomeupwithmodelsmightnotyieldaccurate androbustadaptation.
resultswhenthemodelisusedsomeyearsafteritsimplemen-
tation.Economicconditionsinsomecountriesaredynamic, A. INSTANCEBASEDDRIFTADAPTATIONTECHNIQUES
ranging from multi-currency systems to general population Instance-based approaches leverage the weighting, selec-
drifts.Sometimestheeconomicconditionsimprove;insome tion, or transfer learning of samples to counteract drift by
cases, they degrade, which can contribute to the inaccu- emphasizing relevant or recent data instances. Techniques
racy of static credit scoring models implemented before the suchasimportanceweighting,localregioncompetence,and
changes[3].Thisresearchaimstodevelopatwo-stagecredit instancetransferimprovemodelresponsivenesstopopulation
scoringsystemthatenablesthemanagementofthetemporal shifts and data scarcity in credit scoring, achieving notable
degradationofcreditscoringmodelsingeneral. AreaUndertheCurve(AUC)improvementsandoperational
Mostoftheexistingtraditionalsystemsthatareone-shot, efficiency.
fixed-memory-based,andtrainedfromfixedtrainingdatasets A Diverse Instance-Weighting Ensemble (DiwE) is an
andstaticmodelscannotmanageandprocesshighlyevolving instance-based ensemble learning algorithm developed to
financialdata.Changesthatoccurwithinapopulationcausea tackle concept drift in evolving data streams. This concept
changeinthedistributionofvariables;thechangeinvariables was first introduced in [4]. Recognizing that concept drift
wouldthencauseachangeintheperformanceofthemodel. is an inherent property of such streams and that maintain-
Hence, there is a need to design an adaptive credit-scoring ingensemblediversityisasignificantchallenge,theirwork
modelforthisdynamicenvironment. proposed a novel diversity measurement. Unlike traditional
Theneedforanadaptivecreditscoringsystemisaresult methods that assess diversity via inputs, outputs, or classi-
ofdynamicsocioeconomicchangesintheenvironment,ema- fier parameters, DiwE’s approach is based on the degree to
nating from changes in data distribution, such as concept whichensemblemembersdisagreewiththeprobabilityofa
drift[2]. regional distribution change. This method uses estimations
The model has practical applicability across multiple of regional distribution changes, as instance weights and
domains.Intheinsuranceindustry,itcanbeutilizedtosup- diversity are fostered by constructing different regional sets
portdecision-makingprocessesrelatedtotheapprovalofnew through various schemes, leading to varied drift estimation
policy applications and the renewal of existing policies by results. To maximize diversity, the algorithm strategically
assessingthecreditworthinessofapplicants.Intherealestate selectsclassifiersthatexhibitthehighestdisagreement.Eval-
sector, landlords may employ credit scoring mechanisms uations conducted on a range of synthetic and real-world
to evaluate the likelihood of prospective tenants meeting data-streambenchmarksdemonstratedtheeffectivenessand
rentalpaymentobligationsinatimelymanner.Furthermore, advantages of the proposed DiwE algorithm in adapting to
in the field of human resource management, employers conceptdrift.
may incorporate credit history and credit scores into their Workdonein[5]introducedanoveladaptivebehavioural
recruitmentprocesses,particularlyforpositionsinvolvingthe credit scoring scheme designed to address critical issues in
management of substantial financial resources, as an addi- credit risk assessment, primarily population in some cases
tionalmeasureofassessingcandidatereliabilityandfinancial concept drift, which causes underlying data distributions
responsibility. to change over time and necessitates continuous model
The remainder of this paper is organized as follows. monitoring and recalibration. The proposed approach uti-
InSectionII,weprovidetheresearchmethod.InSectionIII, lizes online training for each incoming borrower inquiry by
90366 VOLUME14,2026

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
dynamically identifying a specific region of competence and feature relevance can drift over time, rendering static
using the k-nearest neighbour (kNN) algorithm, which then models obsolete. They compared batch and stream-based
servesasalocalizedtrainingsetforatailoredclassification algorithms using the Kolmogorov–Smirnov and popula-
model. This study compared various classifiers, including tion stability index metrics, showing that data stream
logistic regression (LR), random forests (RF), and gradient learners, particularly Adaptive Random Forests, can match
boosting trees (XGBoost). Key findings indicate that local or outperform conventional models while maintaining
logistic regression models consistently and statistically sig- stability.
nificantly outperform their global counterparts and achieve DriftLens, an unsupervised real-time concept drift detec-
comparableresultstomorecomplexglobalMachineLearn- tion framework for deep learning models that operates on
ing models such as RF and XGBoost. This research also unstructureddata,addresseschallengesinmonitoringmodel
highlightsthattheselectionofaregionofcompetencebased performance as data distributions change over time [9].
on similar characteristics, as opposed to random selection, The framework computes the distribution distances of deep
is crucial for superior performance. The study concluded learning embedding representations to detect and charac-
that this adaptive scheme provides an effective solution terize drift. DriftLens can classify the presence of drift
forpopulationdrift,offeringcompetitiveperformancewhile in less than 0.2 seconds, making it at least five times
maintaininginterpretability,particularlywithlocalLR,which faster than other detectors. It outperformed techniques in
isbeneficialforregulatorycompliance. 11 out of 13 use cases, demonstrating its high effective-
In recent advances in credit risk modelling, an innova- ness in drift discrimination. The correlation index of the
tive personal credit risk assessment framework based on drift curve modelled by DriftLens was ≥ 0.85, indicating
Instance-Based Transfer Learning (TL) that addresses key a strong alignment with the actual drift patterns. DriftLens
limitations in traditional models, such as data sparsity and is robust to parameter settings and ensures consistent per-
platform-specific variability, was introduced. The approach formance across various data types and classification tasks.
rebalances sample weights in the source domain and trans- Thisstudyaddressedthechallengesofconceptdriftdetection
fersknowledgetotargetdomainswithlimiteddata,thereby in dynamic environments, in which actual labels are often
uncovering shared patterns across financial platforms [6]. unavailable.
Through integrating base learners such as decision trees, A novel approach called CatSight for detecting concept
logistic regression, and XGBoost, and applying the model drift in multivariate time series data, particularly in indus-
todatasetsfromP2Pplatformsandbanks,thestudydemon- trial processes, by utilizing Common Spatial Patterns and
strated a significant 24% improvement in AUC compared Machine Learning algorithms, was presented in [10]. The
to conventional Machine Learning techniques. This under- CatSight method addresses concept drift in industrial mon-
scores the robustness and practical applicability of the itoringbyutilizingCommonSpatialPatternstodifferentiate
model in diverse financial contexts. Wang and Yang [6] data distributions and employing machine-learning algo-
further emphasized the potential for broader domain adap- rithms for detection. This approach effectively identifies
tation and continued refinement to enhance the model’s suddenchangesindatastreamsandenhancespredictiveper-
scalability and effectiveness in real-world credit evaluation formance in real-time applications. The evaluation of six
scenarios. state-of-the-art classifiers demonstrated its adequacy. Cat-
The cold-start problem in credit scoring is addressed SightcombinesaCommonSpatialPattern(CSP)forfeature
by introducing transfer-learning techniques tailored to the selection and conventional Machine Learning classifiers for
financial data context [7]. Wei et al. proposed two novel conceptdriftdetection.
models: the SPY-Transfer model, which adapts the SPY The method was tested on three datasets, including two
algorithmfrompositive-unlabelledlearningtoselectvaluable public and one industrial dataset, and showed superior per-
sourcesamplesfortargetdomainenhancement,andtheSPY- formance. CatSight achieved an average accuracy increase
TrAdaBoostmodel,whichcombinesSPY’ssampleselection of 10.5% compared to conventional classification methods.
withTrAdaBoost’sweightingmechanismtoimprovepredic- The best-performing combination was CSP with Support
tiveaccuracy.Theexperimentalresultsdemonstratethatboth Vector Machine (SVM), which yielded higher accuracy
models outperform traditional cold-start problem-solving scores than the other methods. This study emphasized the
approachesandtheclassicTrAdaBoostalgorithm,highlight- potential application of CatSight in various industrial prob-
ing the effectiveness of sample-based transfer learning in lems owing to its effective drift detection capability. Future
creditscoringtasks. research should explore classifier ensembles and streaming
There is a need to explore the limitations of tradi- data analysis to enhance the effectiveness of the method.
tional batch Machine Learning models in dynamic credit The study in [10] also discussed the need to address limita-
scoring environments and advocate the use of data-stream tionsandconsiderunbalancedclassdataproblemsforbetter
classification techniques. By analysing three anonymized driftdetection.Overall,CatSightdemonstratedimproveddis-
real-world datasets from Brazilian financial institutions, crimination rates in multivariate time-series data that were
Barddal et al. [8] demonstrated that customer behaviour affectedbyconceptdrift.
VOLUME14,2026 90367

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
B. MODEL-BASEDDRIFTADAPTATIONTECHNIQUES predictive performance was evaluated using publicly avail-
Model-based methods focus on updating model parameters abledatasets,andcomparisonswithexistingstate-of-the-art
or structures to accommodate drift, including incremen- models demonstrated that ADHE significantly outperforms
tal learning, adaptive ensemble models, and reinforcement theminpredictionaccuracy,asconfirmedbynon-parametric
learning-drivenupdatescheduling.Thesestrategiesenhance tests,whilealsoconsideringthecomputationalcost[13].
predictiveperformanceandcomputationalefficiencybutface The study in [14] addressed the challenges of credit
challenges in balancing the update frequency and avoiding card fraud detection, particularly the issue of concept drift,
catastrophicforgetting. wherecustomerspendingbehavioursandmarketpurchasing
Adaptive Model Updating using a Simulated Environ- trendsfrequentlyvaryovertime,andtheinherentimbalanced
ment(AMUSE),areinforcementlearning-basedframework class distribution in real transaction data. To address these
designedtoaddressconceptdriftinpredictivemodellingby problems,theyproposedandinvestigatedacard-basedincre-
learningoptimalupdatepolicieswithinasimulatedenviron- mentalGradientBoostingTree(GBT)model.Thisapproach
ment, was proposed in [11]. Unlike traditional approaches allows the GBT model to incrementally learn from trans-
that rely on fixed schedules or reactive drift detection, actions of fraudulent credit cards reported daily, thereby
AMUSE leverages a parametric model to simulate diverse adapting in real time to drifts in online transactions. This
drift scenarios and trains a model that proactively recom- study compares card-based incremental GBT with a reg-
mends model updates based on the expected performance ular GBT model and a retraining method that combines
gains and update costs. This method enables classifiers to previous and new fraudulent transaction sets. Experiments
maintain accuracy while minimizing unnecessary retrain- conductedonfourmonthsofrealtransactiondata(December
ing, making it particularly valuable in domains such as 2019 to March 2020) demonstrated improvements in fraud
finance and healthcare, where data distribution evolves and detection performance across all months, noting a signif-
updatecostsarehigh.Theempiricalresultsdemonstratethat icant concept drift in December that impacted the GBT
AMUSE outperforms conventional strategies in simulated model’s performance. The effectiveness of the card-based
settings, offering a robust and cost-sensitive solution for incremental learning was further validated by comparing it
adaptivemodelmaintenance. withtransaction-basedincrementallearning,whichisprone
Thestudyin[12]addressedthechallengeofconceptdrift tocatastrophicforgetting.
in Machine Learning, particularly in incremental learning
scenarios, where data distributions are not static, and train- C. FEATUREBASEDDRIFTADAPTATIONTECHNIQUES
ing data may be incomplete. Traditional retraining methods Feature-based adaptation addresses changes in the feature
are often time-consuming and computationally expensive. relevance or distribution through adaptive feature selection,
To overcome this, they proposed an incremental Support representationlearning,anddomainadaptation.Approaches
Vector Machine (SVM) learning approach that incorporates include random subspace methods, feature weighting, and
domain adaptation. Their method focuses on two critical transferlearningtomitigatefeaturedriftandredundancyand
issues: acquiring new knowledge without forgetting pre- toenhancemodelgeneralizationandinterpretabilityincredit
viously learned information, and discarding obsolete data riskevaluation.
without corrupting valid information. The proposed solu- ArecentliteraturesurveybyRabashetal.[15]addressed
tion involves fine-tuning the previous model with a small the significant challenges in stream data learning, particu-
amountofnewdatatocreateamodelthatissensitivetonew larly focusing on the dynamic behaviours and changes in
information, while retaining old knowledge through param- theenvironmentthatleadtoconceptandfeaturedrifts.This
etertransfer.Furthermore,anensembleandmodelselection studyprovidesacomprehensiveoverviewofthefundamental
mechanismbasedonBayesiantheorywasintroducedtopre- concepts and definitions in this domain, along with various
serve valid information. Experimental results demonstrated modelsandmethodsdevelopedfordetectingfeaturedriftand
improved performance as new data were acquired, and the maintaining the validity of Machine Learning models when
effectiveness of the algorithm was also explored in relation suchdriftsoccur.Itdetailsthegeneratorsutilizedforcreating
to the degree of data drift. The model demonstrated perfor- datasetswithfeaturedrift,whichiscrucialforbenchmarking
mance gains over the standard SVM and incremental SVM detection and handling approaches. The authors also pre-
algorithms on four out of five industrial datasets and four sented a taxonomy of feature selection methods applicable
syntheticdatasets. to both static and dynamic environments. Concluding their
To address the challenge of credit scoring in scenarios analysis, they suggested that reinforcement-based models
wherecustomerbehaviourandfinancialvariablesdriftover holdsignificantpromiseinaddressingthesechallenges.
time, an Adaptive and Dynamic Heterogeneous Ensemble
(ADHE) approach was introduced in this study. ADHE D. METALEARNINGANDSELF-ADAPTIVESYSTEMS
leverages data stream learning techniques to enable incre- Meta-learning frameworks, including fairness-aware online
mental learning and adaptation to drifting variables. The meta-learning and lifelong self-adaptation, are advancing
ADHEisdesignedtoexploitdiversitybyincorporatingmod- credit scoring by dynamically selecting models and adapt-
els derived from various learning algorithms. The model’s ing them to non-stationary environments. These methods
90368 VOLUME14,2026

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
improverobustnessagainstheterogeneousdriftpatternsand occurs, which is crucial for timely and accurate adaptation.
evolving fairness constraints by using bi-level optimization Driftadaptationinvolvesupdatingthemodeleitherbyretrain-
andlifelongMLlayerstotrackthesystemandenvironmen- ing, building specialized models for different drift types,
tal changes. They offer promising avenues for continuous or incrementally adjusting existing models. Adaptation can
learning and decision-making enhancements under drift beactive,triggeredbydetecteddrift,orpassive,withperiodic
conditions. updates, regardless of detection. The framework considers
AConceptDriftDetectionFrameworkwithHybridMeta- strategies for forgetting outdated data, either by discarding
Learning (CDDF-HML), a unified framework designed to orstoringitforfutureuse.Thisstructuredapproachenables
addressthechallengeofconceptdriftindynamicdatastream models to remain accurate and responsive in non-stationary
mining,wasintroducedin[16].Recognizingthattraditional environments,particularlyinregressiontasks,wherecontin-
methods often specialize in either gradual or abrupt drifts, uoustargetvariablesevolveovertime[18].
CDDF-HMLemploysanovelapproachthatcombinesmeta-
learning,adaptivefeatureselection,andensemble-basedpro- III. CONCEPTDRIFTDETECTIONANDMODEL
cessestoeffectivelyidentifybothtypesofconceptchanges. ADAPTATION
The framework is particularly suited for environments in Good Concept drift detection methods generally use a test
which data distributions are continuously evolving, demon- statistictokeeptabsonthedatastreamandprovideameasure
stratingitscapabilitytodetectdeviationsandadapttovarious of the similarity between old and new samples to identify
dataconditions.Thecomparativeanalysisperformedinthis the change in the concept. The similarity value was then
study indicated that CDDF-HML is an effective tool for comparedwithapredefinedthresholdtodeterminethedrift
discoveringconceptdrift,therebyenhancingthereliabilityof magnitude. The generic scheme for the concept drift detec-
Machine Learning models in dynamic data situations. This tion methods is shown in Figure 1. In the figure, the null
work can be further improved by implementing the method hypothesisisthattheteststatisticwouldnotyieldasignificant
in specific domains, refining adjustment approaches, and differencebetweentheoldandnewdata,thatis,noconcept
improving scalability; hence, the purpose of this study is to driftisdetected.Ifthenullhypothesisisrejected,thesystem
applyittoCreditScoring. continues with the current learner and slides on the data
| Thesignificantchallengeofconceptdriftindatastreams, |     |     |     |     |     |     |     | stream. |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
whereevolvingdatacharacteristicscanrenderclassification
modelsobsolete,wasaddressedin[17].Acoredifficultylies
| in selecting | an  | appropriate | drift | detector |     | for a given | stream, |     |     |     |     |
| ------------ | --- | ----------- | ----- | -------- | --- | ----------- | ------- | --- | --- | --- | --- |
aspriorknowledgemaybeunavailable,andstreamproperties
| may change   | over           | time.     | To             | overcome | this       | problem,      | a novel     |     |     |     |     |
| ------------ | -------------- | --------- | -------------- | -------- | ---------- | ------------- | ----------- | --- | --- | --- | --- |
| framework    | that           | leverages | meta-learning  |          |            | was proposed. | This        |     |     |     |     |
| framework    | extracts       |           | statistical    | and      | temporal   | meta-features |             |     |     |     |     |
| from sliding | windows        |           | to dynamically |          | recommend  |               | the most    |     |     |     |     |
| suitable     | drift detector |           | in real-time   |          | for unseen |               | data chunks |     |     |     |     |
basedontheirproperties.Theeffectivenessofthisapproach
| was evaluated |           | through    | experiments |          | on      | 10 real-world | and     |     |     |     |     |
| ------------- | --------- | ---------- | ----------- | -------- | ------- | ------------- | ------- | --- | --- | --- | --- |
| 18 synthetic  | data      | streams,   | all         | of which | were    | subject       | to con- |     |     |     |     |
| cept drift    | and class | imbalance. |             | The      | results | demonstrate   | that    |     |     |     |     |
theproposedframeworksignificantlyenhancesconceptdrift
| detection | across | various | scenarios, |     | exhibiting | robustness | to  |     |     |     |     |
| --------- | ------ | ------- | ---------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- |
classimbalanceandhighlightingthebenefitsofdynamically
| adaptingthedriftdetector. |           |     |           |          |     |             |       | FIGURE1. Conceptdriftdetection. |     |     |     |
| ------------------------- | --------- | --- | --------- | -------- | --- | ----------- | ----- | ------------------------------- | --- | --- | --- |
| There                     | is a need | for | a generic | approach |     | to learning | under |                                 |     |     |     |
conceptdriftthatextendstraditionalMachineLearningwork-
|          |             |     |         |      |               |     |         | In this | study, the original | dataset, | the German Credit |
| -------- | ----------- | --- | ------- | ---- | ------------- | --- | ------- | ------- | ------------------- | -------- | ----------------- |
| flows to | accommodate |     | dynamic | data | environments. |     | Instead |         |                     |          |                   |
dataset,wasmodifiedbyintroducingdifferenttypesofdrifts
| of the | usual | two-phase | process |     | of training |     | and testing. |     |     |     |     |
| ------ | ----- | --------- | ------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- |
bysimulation.Thefirstcaseconsideredtohavecausedcon-
| A generic | approach |     | to learning |     | under | concept | drift that |     |     |     |     |
| --------- | -------- | --- | ----------- | --- | ----- | ------- | ---------- | --- | --- | --- | --- |
ceptdriftwasachangeinthefeaturedistribution.
| extends | traditional | Machine |     | Learning | workflows |     | to accom- |     |     |     |     |
| ------- | ----------- | ------- | --- | -------- | --------- | --- | --------- | --- | --- | --- | --- |
Scenario1
| modate | dynamic | data | environments |     | was | articulated | in [18]. |     |     |     |     |
| ------ | ------- | ---- | ------------ | --- | --- | ----------- | -------- | --- | --- | --- | --- |
Inthiscase,conceptdriftisintroducedbyincreasingallthe
The authors outlined a three-phase structure, namely drift ageinstancesbyfive;hence,theassumptionisthatthenew
| detection, | drift | understanding, |     | and | drift | adaptation. | Drift |                |                  |            |                   |
| ---------- | ----- | -------------- | --- | --- | ----- | ----------- | ----- | -------------- | ---------------- | ---------- | ----------------- |
|            |       |                |     |     |       |             |       | dataset is now | being considered | five years | later, as denoted |
detectioninvolvesidentifyingchangesinthedatadistribution
by(1):
| using various |     | statistical | or  | model-based |     | techniques. | Drift |     |     |     |     |
| ------------- | --- | ----------- | --- | ----------- | --- | ----------- | ----- | --- | --- | --- | --- |
understandingfocusesonpinpointingwhenandwhereadrift X =X +5 (1)
|     |     |     |     |     |     |     |     |     | d   | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VOLUME14,2026 90369

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
| whereX |     | isthedriftedinstanceandX |     |     | isaninstanceinthe |     |     |     |     |     |     |     |     |     |
| ------ | --- | ------------------------ | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        | d   |                          |     |     | n                 |     |     |     |     |     |     |     |     |     |
dataset.
| The        | drift       | simulation,  | where           | all      | age values    | are                | increased  |     |     |     |     |     |     |     |
| ---------- | ----------- | ------------ | --------------- | -------- | ------------- | ------------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| by         | five years, | represents   | a               | temporal | shift         | in the population, |            |     |     |     |     |     |     |     |
| reflecting |             | how borrower | characteristics |          | evolve        |                    | over time. |     |     |     |     |     |     |     |
| This       | mimic       | real-world   | changes         | in       | risk profiles | due                | to aging   |     |     |     |     |     |     |     |
andlifecycleeffects,allowingevaluationofthemodel’sabil-
itytoadapttosuchshifts.
Scenario2
| This | case | was | simulated | by adding | noise | to  | the credit |     |     |     |     |     |     |     |
| ---- | ---- | --- | --------- | --------- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
amount.Thiswasdonebyincreasingthecreditamountusing
| random | noise | from | a Gaussian | distribution |     | with | a mean of |     |     |     |     |     |     |     |
| ------ | ----- | ---- | ---------- | ------------ | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
0andastandarddeviationof1000.
| Newcreditamount=OriginalCreditamount+N |     |            |            |     |          |          | (0,1000) |     |     |     |     |     |     |     |
| -------------------------------------- | --- | ---------- | ---------- | --- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Here,                                  | (N  | (0, 1000)) | represents |     | a random | variable | drawn    |     |     |     |     |     |     |     |
(µ)
| from | a Gaussian | (normal) |     | distribution | with | a mean | of  |     |     |     |     |     |     |     |
| ---- | ---------- | -------- | --- | ------------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
0andstandarddeviationσ of1000,asgivenby(2): FIGURE2. Modeladaptationarchitecture.
−(x−µ)2
1
|     |     |     | f(x)= | √ e | 2σ2 |     | (2) |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
σ 2π
IV. ALGORITHMDESIGN
Withthestandarddeviation,theequationbecomes(3): AnAdaptivemethodisdesignedtodealwithfeaturechanges
|     |     |     |     |     |       |     |     | in the dataset | by adjusting | accordingly |     | to maintain |     | model |
| --- | --- | --- | --- | --- | ----- | --- | --- | -------------- | ------------ | ----------- | --- | ----------- | --- | ----- |
|     |     |     |     | 1   | − x 2 |     |     |                |              |             |     |             |     |       |
f(x)= √ e 2·1 0 002 (3) accuracy. The process starts by training the initial model
2π
|          |     |               | 1000 |            |     |           |        | using the  | vanilla models, | CART,   | XGBoost, |     | Naïve   | Bayes, |
| -------- | --- | ------------- | ---- | ---------- | --- | --------- | ------ | ---------- | --------------- | ------- | -------- | --- | ------- | ------ |
|          |     |               |      |            |     |           |        | and Random | Forest. The     | machine | used     | to  | run the | sim-   |
| Equation |     | (3) describes | the  | likelihood | of  | different | values |            |                 |         |          |     |         |        |
occurringinaGaussiandistributioncenteredaround0witha ulations has the following specifications: Processor: 11th
spreaddeterminedbyastandarddeviationof1000. Gen Intel(R) Core (TM) i5-1135G7 @ 2.40GHz 2.40 GHz,
This represents random fluctuations and increased vari- Installed RAM:8.00 GB. In this vanilla testing phase, Ran-
ability in loan sizes over time. In real-world settings, such domForestprovedtobethebestperformer;hence,itwasused
|     |     |     |     |     |     |     |     | as the baseline | for adaptive | model | development. |     | To  | handle |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ----- | ------------ | --- | --- | ------ |
changesmayarisefromfactorslikeinflation,shiftinglending
policies, or evolving customer behaviour, all of which can conceptdrift,threeRandomForestmodelsweremaintained:
alterthedistributionofcreditamounts. m trainedontheoriginalpre-driftdata,mr etain obtainedby
|     |     |     |     |     |     |     |     | 0   |     |     |     | 1   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mwindow
Scenario3 retraining on the detected drifted data, and trained
1
The original dataset has a proportion of the good and using a sliding window over a recently drifted sample.
the bad represented as 70:30. This dataset was created by For each instance, the model’s output class probabilities
,p ,p
introducingachangeinClassDistribution,inthiscase,credit (p 0 r w ), which are fused to produce the final prediction
risk,therebyreducingtheproportionofthedefaultedclassto asgivenby(5):
20%.
|     |     |     |     |     |     |     |     |     | jp =w0p | +w  | p +w | p   |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---- | --- | --- | --- |
Theoriginalclassprobabilitiesaredenotedby(P(C))for final 0 r r w w
i
| class(C | ).Tointroduceachange,aweightingfactor(w |     |     |     |     |     | )was |             |       |     |     |     |     |     |
| ------- | --------------------------------------- | --- | --- | --- | --- | --- | ---- | ----------- | ----- | --- | --- | --- | --- | --- |
|         | i                                       |     |     |     |     |     | i    | Inthiscasew | +w +w | =1  |     |     |     |     |
|         |                                         |     |     |     |     |     |      |             | 0 r   | w   |     |     |     |     |
appliedtoeachclassprobability,asgivenby(4).
Figure2illustratesthemodel-adaptationarchitecture.
ThemodeladaptationalgorithmisdetailedinAlgorithm1
|     |     |     |         | w i ·P(C | i )  |     |     |                                                       |     |     |     |     |     |     |
| --- | --- | --- | ------- | -------- | ---- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | P   | ′ (C )= |          |      |     | (4) |                                                       |     |     |     |     |     |     |
|     |     |     | i       | P        | ·P(C |     |     |                                                       |     |     |     |     |     |     |
|     |     |     |         | W J      | j )  |     |     | V. RESULTSANDPERFORMANCEANALYSIS                      |     |     |     |     |     |     |
|     |     |     |         | j        |      |     |     | TheVanillatestresultsdemonstratethegeneralperformance |     |     |     |     |     |     |
where: of the algorithms under static conditions. In this particular
(P(C))istheoriginalprobabilityoftheclassC. case,therewereno changingparametersorattributesinthe
|     | i   |     |     |     |     |     | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(w)istheweightingfactorfortheclass(C ) dataset.TheresultsshowedthattheRandomForestalgorithm
|     | i   |     |     |     |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(P′(C))isthenewprobabilityofclass(C)afterapplying
|     | i   |     |     |     |     | i   |     | outperformedtheothervanillaalgorithms. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
theweightingfactor. Table 1 and Figure 3 present the performance evaluation
Thedenominatorensuresthenewprobabilitiessumto1. resultsofthevanillamodelontheoriginaldataset.
Thisreflectsashiftinunderlyingriskprevalence.Inreal- RandomForestconsistentlydemonstratedsuperiorresults.
world credit environments, such changes may occur due It achieved the highest accuracy (0.77), precision (0.737),
to improved economic conditions, stricter lending policies, F1score(0.680),andROC-AUC(0.768),indicatingastrong
orenhancedriskscreening,allofwhichcanlowerobserved predictivecapabilityandbalancedperformanceinidentifying
defaultratesovertime. truepositiveswhileminimizingfalsepositives.
| 90370 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
Algorithm1ModelAdaptation TABLE1. Vanillamodelperformanceonoriginaldataset.
Let
D:Originaldataset
Dorig :Originaldatasplit
| Di :Driftedversionsof | thedataset, |     |     |     |     |     |     |     |
| --------------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
drift
=1,2......,n
∈{CART,NB,RF,XGB}
Mjbasemodel j
| :Slidingwindowof | sizeW=100attimet |     |     |     |     |     |     |     |
| ---------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
wt
Metrics={Accuracy,Precison,Recall,F1,AUC}
BaselinemodelTraining
ForeachmodelMj
M orig=Train(Dorig)
j
| o rig=Evaluate(M | orig,Dorig,test) |     |     |     |     |     |     |     |
| ---------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
Metrics
| j   | j   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
RetrainingonDriftedData
Foreachdrifteddataset
| Di    |            |     | that ensemble-based |     | methods | such | as Random | Forest and |
| ----- | ---------- | --- | ------------------- | --- | ------- | ---- | --------- | ---------- |
| drift | andmodelMj |     |                     |     |         |      |           |            |
Mretrain,i=Train(Di XGBoost are more robust and effective for classification
)
| j                | drift |     |        |     |     |     |     |     |
| ---------------- | ----- | --- | ------ | --- | --- | --- | --- | --- |
| WindowedLearning |       |     | tasks. |     |     |     |     |     |
ForeachdrifteddatasetDi ,timesteptandmodelMj To adapt to concept drift and evaluate the model perfor-
drift
| W i=Di | [t−W+1:t] |     |     |     |     |     |     |     |
| ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
t drift mance,thefollowingdriftadaptationtechniqueswereimple-
| window,t,i=Train(W | i)  |     |                                                     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- |
| M                  |     |     | mented:modelretraining,windowing,votingensemble,and |     |     |     |     |     |
| j                  | t   |     |                                                     |     |     |     |     |     |
Metricswindow,t,i= AdaptiveFusion.Figure4showsthemodelEvaluationresults
j
Evaluate(Mwindow,t,i,
|     | Di [t+1]) |     | onalltheadaptivestrategies. |     |     |     |     |     |
| --- | --------- | --- | --------------------------- | --- | --- | --- | --- | --- |
| j   | drift     |     |                             |     |     |     |     |     |
EnsembleLearning
Letyˆi
(x)bethepredictionfromthemodelMjondrifteddatasetiThen
j
yˆensemble,i(x)=
mode({yˆi(x)}4=1)
j j
AdaptiveFusion
Let
:Modeltrainedontheoriginaldata
m0
mr :Modelretrainedondrifteddata
mw :Modeltrainedonaslidingwindow
Let
p0(x),pr (x),pw(x):
Predictedclassprobabilitiesfromeachmodel
| ,wr ,ww :Fusionweightssuchthatw0 |     | +wr +ww =1 |     |     |     |     |     |     |
| -------------------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
w0
Then
| pfinal (x)=w0      | .p0 (x)+wr .pr (x)+ww | .pw(x) |     |     |     |     |     |     |
| ------------------ | --------------------- | ------ | --- | --- | --- | --- | --- | --- |
| yˆ fusion (x)=argm | axpfinal(x)c          |        |     |     |     |     |     |     |
c
FIGURE4. ROC-AUCforadaptiveretraining.
|     |     |     | The ROC-AUC |              | is a useful | metric  | for        | detecting con- |
| --- | --- | --- | ----------- | ------------ | ----------- | ------- | ---------- | -------------- |
|     |     |     | cept drift, | particularly | when        | dealing | with class | imbalance,     |
|     |     |     | by tracking | changes      | in a        | model’s | ability    | to distinguish |
betweenclasses.AsignificantdropinAUCovertimeshows
thatthemodelencountersunfamiliarpatterns,indicatingthat
|     |     |     | the data | distribution | may have | shifted | and         | that retraining |
| --- | --- | --- | -------- | ------------ | -------- | ------- | ----------- | --------------- |
|     |     |     | could be | necessary.   | Figure   | 5 shows | the ROC-AUC | for the         |
adaptiveretrainingapproach.
FIGURE3. Vanillamodelperformanceonoriginaldataset.
Figure6showstheROC-AUCfortheadaptiveWindowing
approach
XGBoost followed closely, particularly excelling in the Figure 7 shows the ROC-AUC for the Ensemble Adapta-
ROC-AUC (0.760) and maintaining competitive precision tionandAdaptiveFusionapproach.
and recall values. In contrast, CART and Naïve Bayes Across all three drift scenarios (drift1–drift3), the adap-
exhibited lower performance across all metrics, with Naïve tive_fusion strategy delivered the strongest and most stable
BayesslightlyoutperformingCARTinROC-AUC(0.662and performance, achieving the highest values for accuracy,
0.602), but trailing in other areas. These findings suggest precision, recall, F1-score, and ROC-AUC with minimal
| VOLUME14,2026 |     |     |     |     |     |     |     | 90371 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
FIGURE7. ROC-AUCforensembleadaptationandadaptivefusion.
|     |     |     |     | algorithm | that dynamically | integrates | multiple classifiers |     |
| --- | --- | --- | --- | --------- | ---------------- | ---------- | -------------------- | --- |
FIGURE5. Modelevaluationonadaptivestrategies.
|     |     |     |     | to maintain     | predictive      | accuracy. The         | proposed Adaptive_ |          |
| --- | --- | --- | --- | --------------- | --------------- | --------------------- | ------------------ | -------- |
|     |     |     |     | Fusion          | method differs  | from static ensembles | by                 | updating |
|     |     |     |     | model weights   | dynamically     | rather than           | keeping them       | fixed    |
|     |     |     |     | after training. | Unlike periodic | retraining,           | it adjusts         | contin-  |
|     |     |     |     | uously          | based on recent | performance,          | enabling faster    | and      |
moreefficientresponsestoconceptdrift.Theresearchbegan
|     |     |     |     | by benchmarking | four                 | vanilla models: | CART, Naive            | Bayes, |
| --- | --- | --- | --- | --------------- | -------------------- | --------------- | ---------------------- | ------ |
|     |     |     |     | Random          | Forest, and XGBoost, | which           | are commonly           | used   |
|     |     |     |     | in financial    | risk modelling       | because of      | their interpretability |        |
androbustness.AGermanCreditRiskbenchmarkdatasetis
|     |     |     |     | used. Among    | these, Random     | Forest demonstrated |                     | superior |
| --- | --- | --- | --- | -------------- | ----------------- | ------------------- | ------------------- | -------- |
|     |     |     |     | performance,   | consistent        | with the findings   | of Museba           | [13],    |
|     |     |     |     | who emphasized | the effectiveness | of heterogeneous    |                     | ensem-   |
|     |     |     |     | ble models     | in credit         | scoring under       | dynamic conditions. |          |
Toaddressthedriftproblem,fouradaptivestrategies,namely,
|     |     |     |     | retraining, | windowing,   | ensemble, and       | adaptive fusion, | were  |
| --- | --- | --- | --- | ----------- | ------------ | ------------------- | ---------------- | ----- |
|     |     |     |     | explored.   | The Adaptive | Fusion outperformed | all the          | other |
strategies;theRetrainedRandomForestmodelachievedhigh
|     |     |     |     | metrics, | reaffirming the | value of comprehensive | retraining, |     |
| --- | --- | --- | --- | -------- | --------------- | ---------------------- | ----------- | --- |
assupportedbyKrempletal.[19],whoadvocatedforexplicit
FIGURE6. ROC-AUCforadaptivewindowing.
driftmodellinginevolvingfinancialdatasets.Thewindowed
RandomForest,whichincrementallyupdatesusingasliding
degradationasdriftoccurred,indicatingsuperiorrobustness
datawindow,underperforms,reflectinglimitationsincaptur-
to distributional shifts. The ensemble approach was consis- ing long-term behavioural shifts, a challenge also noted in
tently the second best, remaining close to adaptive_fusion adaptiveonlinescoringmodels[20].
but with slightly larger drops. most notably in recall; con- Ensemble learning based on soft voting across the four
sequently, F1. Batch retraining yielded middling results: classifiers yielded good results, demonstrating its useful-
| accuracy | and precision were | reasonable, | yet recall and F1 |          |                       |         |                  |     |
| -------- | ------------------ | ----------- | ----------------- | -------- | --------------------- | ------- | ---------------- | --- |
|          |                    |             |                   | ness for | maintaining stability | without | full retraining. | The |
lagged,suggestingasloweradaptationtoevolvingdatacom- most significant contribution of this study is the Adaptive
pared with methods that combine or continuously integrate Fusion algorithm, which dynamically weighsand integrates
models. The sliding window method performed the worst modeloutputsbasedonevolvingdatapatterns.Thisapproach
overall,withthelargestdeficitsinrecallandF1score.These matchestheretrainedmodelinallperformancemetrics,offer-
findingssupporttheadoptionofadaptive_fusionasadefault
|     |     |     |     | ing a scalable | and efficient | solution to | concept drift. | Unlike |
| --- | --- | --- | --- | -------------- | ------------- | ----------- | -------------- | ------ |
strategyfordrift-pronesettings. static ensembles or retrained models, the fusion algorithm
wasadaptedinrealtime.
VI. RESULTSDISCUSSION A card-based incremental Gradient Boosting Tree (GBT)
In response to the growing challenge of concept drift in model was designed to address concept drift and data
creditscoring,thisstudyintroducedanoveladaptivefusion imbalance in credit card transaction streams. This model
| 90372 |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------- | --- |

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
incrementally updates itself using daily reported fraudulent on relevance and feature space stability, thereby enabling
cardsandtheirassociatedtransactions,therebymaintaininga accurate predictions through weighted classifier outputs.
highdetectionperformancewithouttheneedforfullretrain- Experiments using Java and the MOA framework showed
ing.ComparedtotraditionalandretrainedGBTmodels,the that KME outperforms eight state-of-the-art algorithms on
incrementalapproachdemonstratedcomparableAUCscores syntheticandreal-worlddatasets,offeringarobustandeffi-
andrecallrates,whilesignificantlyreducingthetrainingtime cient solution for dynamic data environments. On synthetic
andcomputationalcost.Importantly,itmitigatescatastrophic datasets,KMEachievedaccuracyratesrangingfrom85%to
forgetting and eliminates the need for costly data balancing 95%dependingonthetypeofconceptdrift[22].
techniques. These findings suggest that similar incremen- The proposed Adaptive Fusion algorithm is designed
tal learning strategies can be effectively applied to adaptive to operate alongside existing credit scoring infrastructures.
creditscoringsystems,enablingthemtoresponddynamically It can be integrated as a complementary enhancement to
toevolvingborrowerbehaviourandriskpatternswhilepre- existingscorecardsordeployedasaparallelchallengermodel
servingoperationalefficiency[14]. for performance benchmarking and validation. Outputs can
In evaluating adaptive credit scoring models, the be mapped to standard risk grades, ensuring compatibility
card-based incremental Gradient Boosting Tree (GBT) with established decision workflows. The algorithm would
approach for fraud detection offers valuable insights into not introduce significant scalability constraints, as model
handling concept drift and maintaining model performance updates are performed dynamically and can be integrated
over time. Similar to adaptive fusion strategies that com- withinexistingdataprocessingpipelines.Fromaregulatory
bineretrainingandwindowing,theincrementalGBTmodel perspective,thedesignincorporatescontrolledupdatemech-
updates itself daily using transactions from reported fraud- anisms, auditability and explainability features, which align
ulent cards, thereby avoiding full retraining and reducing with prevailing model governance requirements. As such,
the computational cost. Both approaches aim to balance deployment is not expected to pose substantial compliance
responsivenesswithefficiency;however,theadaptivefusion challenges,althoughstandardvalidationandmonitoringpro-
modelintroducesanovelintegrationofdynamicwindowing ceduresremainnecessary.
and selective retraining, allowing the system to adaptively
respond to data shifts while preserving historical learning. VII. CONCLUSIONANDFUTUREWORK
This fusion enables more robust and interpretable credit ThisstudyanalyzedtheperformanceoffourMachineLearn-
scoring, particularly when combined with ensemble tech- ing models, CART, Naive Bayes, Random Forest, and
niques and explainability tools. The success of incremental XGBoost, on the German Credit benchmark dataset under
GBT in maintaining high AUC and recall with minimal different adaptation techniques for handling concept drift.
trainingtimesupportstheviabilityofadaptivemechanismsin Initialevaluationsontheoriginaldatasetestablishedbaseline
financialmodelling,reinforcingtherelevanceandinnovation performance,withXGBoostandRandomForestoutperform-
ofadaptivefusionincreditriskprediction. ingtheothermodels,withRandomForestbeingthebest.
Thisinnovationfillsacriticalgapinthecurrentliterature, Four adaptive techniques- retraining, windowed learning,
asmostadaptivecreditscoringmodelsrelyoneitherretrain- ensemble learning, and Adaptive Fusion based on the Ran-
ing or fixed ensemble strategies. By introducing a dynamic domForestbaselinewereappliedtotestthemodels’abilityto
fusionmechanismthatrespondstodrift,thisstudyadvances handledrift.AdaptiveFusionoutperformedallotheradapta-
thefieldoffinancialMachineLearningandoffersapractical tiontechniques,whichimpliesthattheadaptiveintegrationof
framework for real-time credit risk assessments in volatile multiplemodelscanachieveahighlevelofpredictivepower.
environments. ThiswasfollowedbytheRetrainedRandom,whichshowed
The findings resonate well with contemporary studies, high performance across all metrics, particularly excelling
in which the designed DynED framework emphasizes the inrecallandROC-AUC.Thisshowsastrongsensitivityfor
importance of diversity and dynamic selection in ensem- identifyingtruepositivesandanexcellentoverallclassifica-
bles to effectively handle concept drift [21]. The analysis tioncapability.
of the German Credit benchmark dataset includes several TheensembleModelmatchedtheretrainedmodelinterms
modelling approaches, such as logistic regression, discrim- ofaccuracy,precision,recall,andF1score,butslightlytrailed
inant analysis, tree-based methods, and random forest. The in the ROC-AUC. This indicates robust performance with
Knowledge-Maximized Ensemble (KME) is a hybrid data marginallylessconfidenceintherankingpredictions.Visu-
stream classification algorithm designed to handle various alizations,suchasbarchartsandROC-AUCplots,illustrate
types of concept drift- abrupt, gradual, incremental, and thecomparativestrengthsofeachtechnique.
recurrent,particularlyinscenarioswithlimitedlabelleddata. The adaptive Credit Scoring model accounts for fair-
TheKMEintegratesbothchunk-basedandonlineensemble ness and bias, as historical data can reflect inequalities.
models, leveraging supervised and unsupervised knowledge Byincorporatingfairness-awareevaluationandtransparency
to detect drift, reuse past labelled data, and recognize inadaptation,theapproachaimstoensurebothaccuracyand
recurring patterns. It evaluates ensemble components based equitabledecision-making.AdaptiveCreditScoringenables
VOLUME14,2026 90373

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
lenders to respond more dynamically to changing borrower [14] B. Bayram, B. Köroglu, and M. Gönen, ‘‘Improving fraud detection
risk profiles, improving portfolio performance and expand- and concept drift adaptation in credit card transactions using
|     |     |     |     |     |     |     | incremental | gradient |     | boosting | trees,’’ | in Proc. | 19th | IEEE Int. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | -------- | -------- | -------- | ---- | --------- |
ingaccesstocredit,butitalsorequiresstrongermonitoring
|                |             |     |     |             |     |             | Conf. | Mach. | Learn. Appl. | (ICMLA), |     | Dec. 2020, | pp.545–550, | doi: |
| -------------- | ----------- | --- | --- | ----------- | --- | ----------- | ----- | ----- | ------------ | -------- | --- | ---------- | ----------- | ---- |
| and governance | frameworks. |     | For | regulators, | the | use of con- |       |       |              |          |     |            |             |      |
10.1109/ICMLA51294.2020.00091.
|                   |              |        |        |                   |                |     | [15] A. J. | Rabash, | M. Z. A. | Nazri,      | A. Shapii, | and A.       | Al-Jumaily, | ‘‘Stream |
| ----------------- | ------------ | ------ | ------ | ----------------- | -------------- | --- | ---------- | ------- | -------- | ----------- | ---------- | ------------ | ----------- | -------- |
| tinuously         | updating     | models | raises | important         | considerations |     |            |         |          |             |            |              |             |          |
|                   |              |        |        |                   |                |     | learning   | under   | concept  | and feature | drift:     | A literature | survey,’’   | J. Auto. |
| around stability, | transparency |        |        | and auditability, | necessitating  |     |            |         |          |             |            |              |             |          |
Intell.,vol.6,no.3,pp.1–16,Sep.2023,doi:10.32629/jai.v6i3.880.
| oversight | approaches | that | can | accommodate | adaptive | deci- |     |     |     |     |     |     |     |     |
| --------- | ---------- | ---- | --- | ----------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] G.V.PrasadandK.Sharma,‘‘Aunifiedframeworkfordetectinggradual
sionsystems. andabruptconceptdriftsindatastreammining:Theconceptdriftdetection
frameworkwithhybridmeta-learning(CDDF-HML),’’SSRGInt.J.Electr.
| Future | work needs | to  | include | the use | of a | data stream |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Electron.Eng.,vol.11,no.7,pp.39–50,2024.
thatcanbestudiedandanalyzedtodetectdifferentkindsof [17] G.J.AguiarandA.Cano,‘‘Enhancingconceptdriftdetectionindrifting
concept drift the datamay suffer in order todesign systems andimbalanceddatastreamsthroughmeta-learning,’’inProc.IEEEInt.
todetectchangesandchooseaspecificanddifferentmodel Conf.BigData(BigData),Dec.2023,pp.2648–2657.
|     |     |     |     |     |     |     | [18] M. Lima, | M.  | Neto, | T. S. | Filho, | and R. | A. D. | A. Fagundes, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ----- | ------ | ------ | ----- | ------------ |
tomakepredictions.Thismaybesuitableforareasthatantic- ‘‘Learning under concept drift for regression—A systematic litera-
ipateabruptchangesthatmayhaveoccurredinthepastand ture review,’’ IEEE Access, vol. 10, pp.45410–45429, 2022, doi:
10.1109/ACCESS.2022.3169785.
thatcanbecheckedforinthefuture.Theresearchareacanbe
|     |     |     |     |     |     |     | [19] G. Krempl, | V.  | Hofer, M. | K. Nielsen, | and | T. Verge, | ‘‘Models | for drift- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ----------- | --- | --------- | -------- | ---------- |
furtherexploredasadeeplearningorreinforcementproblem adaptivescoring,’’Univ.Graz,Austria,Tech.Rep.,2000.
withtheapplicationofdeeplearningorreinforcementalgo- [20] T. Museba, ‘‘Adaptive particle swarm optimized XGBoost ensemble
algorithmforonlinecreditscoring,’’Dept.AppliedInf.Syst.,Univ.Johan-
| rithms to | observe | whether | the | deep learning | algorithms | can |     |     |     |     |     |     |     |     |
| --------- | ------- | ------- | --- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nesburg,CollegeBus.&Econ.,Johannesburg,SouthAfrica,Tech.Rep.,
adapttothechangesintheoriginaldataset.
May26,2022,doi:10.21203/rs.3.rs-1660274/v1.
[21] S.Abadifard,S.Bakhshi,S.Gheibuni,andF.Can,‘‘DynED:Dynamic
|     |     |     |     |     |     |     | ensemble | diversification |     | in data | stream | classification,’’ | in  | Proc. 32nd |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------- | ------ | ----------------- | --- | ---------- |
REFERENCES
|     |     |     |     |     |     |     | ACM | Int. Conf. | Inf. Knowl. | Manage., |     | Oct. 2023, | pp.3707–3711, | doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | -------- | --- | ---------- | ------------- | ---- |
[1] WorldBankGroup.(2019).DisruptiveTechnologiesintheCreditInfor- 10.1145/3583780.3615266.
| mation | Sharing | Industry: | Developments | and | Implications. | [Online]. |              |          |         |     |        |                       |     |        |
| ------ | ------- | --------- | ------------ | --- | ------------- | --------- | ------------ | -------- | ------- | --- | ------ | --------------------- | --- | ------ |
|        |         |           |              |     |               |           | [22] S. Ren, | B. Liao, | W. Zhu, | and | W. Li, | ‘‘Knowledge-maximized |     | ensem- |
Available:http://hdl.handle.net/10986/31714 ble algorithm for different types of concept drift,’’ Inf. Sci., vol. 430,
[2] FasterCapital. (2025). Credit Scoring Models: A Comparison pp.261–281,Feb.2018.
| of Different |                                                           | Approaches | and | Their | Applications. | [Online]. |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------------------------------- | ---------- | --- | ----- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Available:   | https://fastercapital.com/content/Credit-Scoring-Models-- |            |     |       |               |           |     |     |     |     |     |     |     |     |
A-Comparison-of-Different-Approaches-and-Their-Applications.html
[3] W.A.Addy,A.O.Ajayi-Nifise,B.G.Bello,S.T.Tula,O.Odeyemi,
andT.Falaiye,‘‘AIincreditscoring:Acomprehensivereviewofmodels
| and predictive | analytics,’’ |     | Global | J. Eng. Technol. | Adv., | vol. 18, no. 2, |     |     |     |     |     |     |     |     |
| -------------- | ------------ | --- | ------ | ---------------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.118–129,Feb.2024,doi:10.30574/gjeta.2024.18.2.0029.
[4] A.Liu,J.Lu,andG.Zhang,‘‘Diverseinstance-weightingensemblebased
onregiondriftdisagreementforconceptdriftadaptation,’’IEEETrans.
| NeuralNetw. | Learn.Syst.,vol. |     | 32,no. | 1,pp.293–307, |     | Jan.2021, doi: |     |     |     |     |     |     |     |     |
| ----------- | ---------------- | --- | ------ | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.1109/TNNLS.2020.2978523.
[5] D.NikolaidisandM.Doumpos,‘‘Creditscoringwithdriftadaptationusing
localregionsofcompetence,’’OperationsRes.Forum,vol.3,no.4,p.67, RACHAELCHIKOOREreceivedtheB.Sc.degree
Nov.2022,doi:10.1007/s43069-022-00177-1.
|     |     |     |     |     |     |     |     |     | (Hons.) | in  | computer | science | from | Midlands |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | ------- | ---- | -------- |
[6] M.WangandH.Yang,‘‘Researchonpersonalcreditriskassessmentmodel
|     |     |     |     |     |     |     |     |     | State | University, |     | Zimbabwe, | and | the M.Tech. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --------- | --- | ----------- |
basedoninstance-basedtransferlearning,’’Int.J.Intell.Sci.,vol.11,no.1,
|     |     |     |     |     |     |     |     |     | degree | in  | information | networks | from | Tshwane |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | -------- | ---- | ------- |
pp.44–55,2021,doi:10.4236/ijis.2021.111004.
|     |     |     |     |     |     |     |     |     | University |     | of Technology, |     | South | Africa. She |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ----- | ----------- |
[7] Q.Wei,Y.Liu,andK.Wu,‘‘Transferlearningbasedcreditscoring,’’in
Proc.IEEE24thInt.Conf.Comput.SupportedCooperat.WorkDesign is currently pursuing the Doctor of Computing
(CSCWD),May2021,pp.1251–1255. degreeincomputerscienceanddataprocessing.
[8] J. P. Barddal, L. Loezer, F. Enembreck, and R. Lanzuolo, ‘‘Lessons She is a Researcher, a Reviewer, a Consultant,
learned from data stream classification applied to credit scoring,’’ a Mentor, an Entrepreneur, and is currently the
|        |              |      |      |            |                |      |     |     | Dean | of the | School | of Information |     | Science and |
| ------ | ------------ | ---- | ---- | ---------- | -------------- | ---- | --- | --- | ---- | ------ | ------ | -------------- | --- | ----------- |
| Expert | Syst. Appl., | vol. | 162, | Dec. 2020, | Art.no.113899, | doi: |     |     |      |        |        |                |     |             |
10.1016/j.eswa.2020.113899. Technology at Harare Institute of Technology, Zimbabwe. She has over
[9] S. Greco, B. Vacchetti, D. Apiletti, and T. Cerquitelli, ‘‘Unsupervised 16yearsoflecturingexperience,duringwhichshehassupervisednumer-
conceptdriftdetectionfromdeeplearningrepresentationsinreal-time,’’ ous undergraduate and postgraduate projects and mentored individuals in
IEEETrans.Knowl.DataEng.,vol.37,no.10,pp.6232–6245,Oct.2025, developing business ideas using emerging technologies. She has actively
doi:10.1109/TKDE.2025.3593123. participatedinresearch,teaching,mentoring,andacademicadministration,
[10] A.Flórez,I.Rodríguez-Moreno,A.Artetxe,I.G.Olaizola,andB.Sierra,
andhascontributedtothenationaldigitalecosystemmappingasadigital
‘‘CatSight,adirectpathtopropermulti-variatetimeserieschangedetec-
|     |     |     |     |     |     |     | ecosystem | champion. | She is | a certified | Data | Protection | Trainer | and has |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | ----------- | ---- | ---------- | ------- | ------- |
tion:Perceivingaconceptdriftthroughcommonspatialpattern,’’Int.J.
|       |                 |      |         |                  |      |            | been involved | in developing |     | the Data | Protection | Training | curriculum | for |
| ----- | --------------- | ---- | ------- | ---------------- | ---- | ---------- | ------------- | ------------- | --- | -------- | ---------- | -------- | ---------- | --- |
| Mach. | Learn. Cybern., | vol. | 14, no. | 9, pp.2925–2944, | Sep. | 2023, doi: |               |               |     |          |            |          |            |     |
Zimbabwe.Shehaspresentedatseveralconferences,servedontheconfer-
10.1007/s13042-023-01810-z.
[11] L.Chislett,C.A.Vallejos,T.I.Cannings,andJ.Liley,‘‘AMUSE:Adaptive enceorganizingcommittees,andadjudicatedvarioushackathons.Sheisalso
anErasmus+TeachingExchangeFellowandaTechWomen2024Emerg-
modelupdatingusingasimulatedenvironment,’’2024,arXiv:2412.10119.
|     |     |     |     |     |     |     | ing Leader. | Her research | interests |     | include | artificial | intelligence, | machine |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --------- | --- | ------- | ---------- | ------------- | ------- |
[12] J.Tang,K.-Y.Lin,andL.Li,‘‘Usingdomainadaptationforincremental
learning,softwareprojectmanagement,theInternetofThings,anddesign
SVMclassificationofdriftdata,’’Mathematics,vol.10,no.19,p.3579,
andanalysisofalgorithms.Sheisamemberofseveralprofessionalbodies,
Sep.2022,doi:10.3390/math10193579.
includingtheComputerSocietyofZimbabwe,theWomeninICTZimbabwe,
| [13] T. Museba, | ‘‘An | adaptive | and dynamic | heterogeneous | ensemble | model |     |     |     |     |     |     |     |     |
| --------------- | ---- | -------- | ----------- | ------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
forcreditscoring,’’inDigital-for-Development:EnablingTransformation, the Girls in ICT Zimbabwe, the Internet Society, the Forum for African
InclusionandSustainabilityThroughICTs,vol.1774.Cham,Switzerland: WomeninEducationZimbabwe(FAWEZI),theDataScienceZimbabwe,
Springer,2023,pp.304–319,doi:10.1007/978-3-031-28472-4_19. theIndabaXZimbabweChapter,andtheWomeninAcademiaZimbabwe.
| 90374 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

R.Chikooreetal.:AdaptiveCreditScoringModelWithConceptDriftDetectionandAdaptationTechnique
SUNDAY OLUSEGUN OJO received the B.Sc. OKUTHE PAUL KOGEDA received the Ph.D.
degree(Hons.)incomputersciencefromtheUni- degree in computer science from the University
versityofIbadanandthePh.D.degreeincomputer oftheWesternCape(UWC),in2023.Heiscur-
sciencefromtheUniversityofGlasgow.Heisa rently an Associate Professor at the Department
distinguishedacademicwithover40yearsofexpe- ofComputerScience,SchoolofAgricultureand
rience. He has held various academic positions, Science, University of KwaZulu Natal (UKZN).
includingalecturer,aseniorlecturer,aresearch, He previously worked at UWC as a Lecturer
andaninnovation professor,theheadof depart- while doing his Ph.D. degree and UFH as a
ment,andthefacultyexecutivedeanacrossseveral Senior Lecturer, where he did a lot of research
African universities. He is currently an Adjunct inICT4DmainlyaroundDwesainEasternCape,
ProfessoratDurbanUniversityofTechnologyandanAcademicExpertCon- in 2009, and TUT as a Senior Lecturer, where he continued to work in
sultantattheUniversityofSouthAfrica.HeisalsotheExecutiveDirectorof ICT4D in Ekangala, Sokhulumi, and Pongola, in 2011; and UFS as an
theInclusiveAfricanIndigenousLanguageTechnology(AfrILT)Institute, Associate Professor, where he continued doing research in ICT4D, the
anon-profitorganizationinSouthAfrica,involvedinglobalcollaborative IoT, and wireless networks, in 2019. He has supervised over 80 honors,
projects,suchasDataScientiaandCL4YEJC.Hehascontributedextensively 40M.Sc./M.Tech./M.Computing,andfivedoctoralgraduates.Hehaspub-
toteaching,research,andinnovation,particularlyinICTandlanguagetech- lishedover45peer-reviewedjournals,eightChaptersinbooks,threebooks,
nologies.Hehasalsoprovidedprofessionalconsultancyservicestonational and over 70 conference proceedings. He has attracted various funding’s,
andinternationalbodiesonICT-relatedprojects,includinginitiativesfocused includingKenya/SAJointScienceandTechnologyResearchCollaboration
on language digitization, climate change, and youth employment in sub- andtheZambia/SAResearchCooperationProgram.Heiscurrentlyamem-
SaharanAfrica. berofIITPSA,IEEE,ACM,andIAENG.Heisaneditorandareviewerof
manyinternationaljournalsandconferenceproceedings.Heisaholderof
onepatent.
VOLUME14,2026 90375