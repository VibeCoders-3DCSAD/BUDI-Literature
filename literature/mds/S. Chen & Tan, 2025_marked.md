---
conversion_metadata:
  converted_at: "2026-10-12T07:35:25Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "S. Chen & Tan, 2025.pdf"
  source_pdf_sha256: "2679ce41b30a33fcdc01b858e609033bbb7f888d8e85c5f3c7b6aca85a33c241"
  page_count: 6
  markdown_char_count: 25706
---

LSTM-Based Consumer Behavior Prediction Model Research
∗
ShuhanChen WenciTan
GuanghuaSchoolofManagement GezhiFutureResearchInstitute
PekingUniversity Beijing,China
Beijing,China twwwwc@sina.com
jincyisme@163.com
Abstract analytics; • Applied computing; • Electronic commerce; •
Thispaperproposesaconsumerbehaviorpredictionmodelbased Operationsresearch.;
onLongShort-TermMemory(LSTM)networkstoaccuratelypre-
Keywords
dict consumer purchasing behavior and preference trends in e-
commerceenvironments. Weconstructamulti-dimensionalfea- Consumer behavior prediction, Long Short-Term Memory net-
ture dataset from large-scale consumer historical data contain- works,Deeplearning,E-commerce,Personalizedrecommendation
ingusercharacteristics,productattributes,andtemporalpatterns.
ACMReferenceFormat:
ThemodelemploysabidirectionalLSTMarchitectureintegrated ShuhanChenandWenciTan. 2025. LSTM-BasedConsumerBehavior
withself-attentionmechanismsforenhancedfeatureextraction. PredictionModelResearch.In20252ndInternationalConferenceonDigital
The architecture comprises six core components: an input em- EconomyandComputerScience(DECS2025),October17–19,2025,Wuhan,
beddinglayertransforming128-dimensionalsparsefeaturesinto China.ACM,NewYork,NY,USA,6pages.https://doi.org/10.1145/3785706.
256-dimensionaldenserepresentations,bidirectionalLSTMlayers 3785906
with512hiddenunitsutilizinggatingmechanismsfortemporal
With the rapid development of e-commerce and the increasing
dependencymodeling,aself-attentionlayerwithadaptivetempo-
complexityofconsumerdigitalbehavior,accuratelypredictingcon-
ralweighting(𝛼t=softmax(et)),adaptivedropoutregularization
sumerbehaviorhasbecomeakeyfactorinenhancingbusinesscom-
(scheduled0.5→0.3),fullyconnectedlayersforfeatureaggregation,
petitiveness.Thecurrentglobale-commercemarkethasreached
andasoftmaxoutputlayerforfive-classpurchaseintentionpredic-
trillionsofdollarsinscale,withpersonalizedrecommendationsys-
tion.Themodelcontainsapproximately2.1milliontrainableparam-
temscontributingover35%ofsalesrevenuethroughalgorithmicfil-
etersandisoptimizedthroughend-to-endbackpropagationwith
teringandcollaborativelearningtechniques.Traditionalconsumer
Adamoptimizer, weightedcross-entropyloss, L2regularization
behavioranalysismethodsprimarilyrelyonstatisticalmodelsand
(𝜆=0.001),gradientclipping(threshold1.0),andcosineannealing
simplemachinelearningalgorithms,suchaslinearregression,deci-
learningratescheduling. Datapreprocessingemploysdistributed
siontrees,andsupportvectormachines[8],whichexhibitobvious
computingframeworksachieving300%efficiencyimprovement
limitationswhenprocessinglarge-scale,multi-dimensionalcon-
with30-dayslidingwindowsand50%overlap.Experimentaleval-
sumerdata,particularlyincapturingtemporalfeaturesandcomplex
uationon500,000userswithover80millioninteractionrecords
dependencyrelationshipsinhigh-dimensionalfeaturespaces.
demonstratessuperiorperformancecomparedtotraditionalma-
Deeplearningtechnologieshaveachievedsignificantprogress
chinelearningmethodsandbasicneuralnetworks,achieving94.2%
acrossvariouscomputationaldomainsthroughGPU-accelerated
accuracy,93.8%precision,94.7%recall,and94.2%F1-score.Statisti-
parallelprocessing. Liuetal. [2]proposedahybridYOLO-UNet3D
calsignificancetesting(p<0.001)confirmsperformanceimprove-
frameworkforautomatedproteinparticleannotationusingconvo-
mentsacrossdiverseusersegments:high-frequencyusers(96.1%
lutionalneuralnetworks,demonstratingdeeplearningadvantages
accuracy),newusers(91.8%accuracy),andhigh-valuecustomers
incomplexdataprocessing.Xuetal.[3]developedamulti-strategy
(96.7%accuracy).Thismodelprovideseffectivecomputationalsup-
enhancedsecretbirdoptimizationalgorithmimplementingadap-
portforpersonalizedrecommendations,intelligentinventoryman-
tive parameter tuning, providing new insights for optimization
agement,andprecisionmarketingone-commerceplatforms.
problems.Thesestudiesindicatethatdeeplearningandintelligent
optimizationalgorithmshavetremendouspotentialinhandling
CCSConcepts
complexpatternrecognitionthroughhierarchicalfeaturelearning
•Computingmethodologies;•Artificialintelligence;•Ma- [4,5].
chinelearning;•Machinelearningapproaches;•Neuralnet- LongShort-TermMemory(LSTM)networks,asanadvancedre-
works;•Informationsystems;•Informationsystemsappli- currentneuralnetworkarchitecture,effectivelysolvethegradient
cations;•Datamining;;•Decisionsupportsystems;•Data vanishingproblemthroughuniquegatingmechanismsincluding
forgetgates,inputgates,andoutputgates,excellinginprocess-
∗Correspondingauthor
ingsequentialdataandcapturinglong-termdependenciesthrough
cellstatememorymechanisms.Relatedresearchshowsthatdeep
learning-basedmethodshaveachievedbreakthroughprogressin
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. multipledomainsthroughend-to-endtraining,suchassupplychain
DECS2025,Wuhan,China logisticsschedulingoptimization[6],IoTsensornetworkswithdis-
©2025Copyrightheldbytheowner/author(s).
tributededgecomputing[7],andtextsummarizationgeneration
ACMISBN979-8-4007-1951-6/2025/10
https://doi.org/10.1145/3785706.3785906 usingtransformerarchitectures[9]. Yangetal. [10]proposeda
1265

DECS2025,October17–19,2025,Wuhan,China ShuhanChenandWenciTan
Table1:DatasetCharacteristics. The distributed computing framework implements memory-
optimizeddatastructuresandcachemanagement,achieving300%
FeatureCategory Numberof DataType processingefficiencyimprovementthroughCPUparallelization
Features andvectorizedoperations. Figure1illustratesthecompletepre-
processingworkflowwithautomateddataqualitymonitoringand
UserDemographics 8 Categorical/Numerical
real-timeprocessingcapabilities.
ProductAttributes 25 Categorical/Numerical
BehavioralSequences 45 Sequential
TemporalFeatures 12 Numerical 1.2 DataPreprocessingandFeatureEngineering
InteractionHistory 38 Sequential/Numerical
TheLSTMmodeladoptsamulti-layerbidirectionalarchitecture
withsixmaincomponents: inputembeddinglayer,bidirectional
LSTMlayer,attentionmechanismlayer,dropoutlayer,fullycon-
largelanguagemodel-basedwebattackdetectionmethodincorpo- nectedlayer,andoutputlayer.Theinputembeddinglayerconverts
ratingattentionmechanismsandmulti-layerperceptrons,proving high-dimensionalsparsefeaturesinto256-dimensionaldensevec-
deeplearningeffectivenessincomplexpatternrecognitiontasks. tors.ThebidirectionalLSTMcoreconsistsofforwardandbackward
ThisresearchconstructsanLSTM-basedconsumerbehaviorpre- LSTMunitswith512hiddenunitseach,usinggatingmechanisms
diction model, combining self-attention mechanisms and multi- toselectivelyprocessinformationandsolvelong-termdependency
layer bidirectional architecture with backpropagation training, problems. Adropoutlayer(rate0.3)preventsoverfitting. Figure
drawingonadvancedconceptsfrombio-inspiredhybridpathplan- 2illustratesthenetworkarchitectureanddataflow. Themodel
ning [1] and multi-scale feature aggregation using hierarchical usesend-to-endtrainingwithbackpropagation,employssoftmax
neuralnetworks[5]. Throughdistributedcomputingframeworks activationformulti-classpredictionacrossfivepurchaseintention
andparalleldataprocessingofconsumers’historicalbehavioral levels(VeryLowtoVeryHigh),andcontainsapproximately2.1
data,weachieveprecisepredictionoffuturepurchasingbehavior, millionparameters.
providingscientificbasisforintelligentoperations,personalized
recommendations,andprecisionmarketingone-commerceplat-
1.3 ModelOptimizationStrategies
forms.
Toenhancepredictiveperformanceandgeneralizationcapability,
1 Methods thisstudyemploysmultipleadvancedoptimizationstrategies.First,
aself-attentionmechanismcalculatesimportanceweightsforeach
1.1 DataPreprocessingandFeatureEngineering
timestepthroughlearnedweightmatricesandneuralnetworken-
Thisstudyemploysrealconsumerdatafromamajore-commerce ergyscoring.Theattentionlayerusesmulti-headarchitecturewith
platformwithover150millionmonthlyactiveusersacrossclothing, 8attentionheadsand64-dimensionalkey-valuepairs,improving
electronics,andhomegoodscategories.Thedatasetcontainsbehav- keyfeatureidentificationaccuracyby12.5%.
ioralrecordsof500,000usersover12months,totalingmorethan80 Second,gradientclippingpreventsgradientexplosionbycon-
millioninteractiondatapointsencompassingbrowsing,searching, straininggradientnormstothreshold1.0usingL2normclipping.
cartadditions,andpurchases.DatapreprocessingutilizesApache TheAdamoptimizerimplementsmomentum-basedadaptivelearn-
Sparkdistributedcomputingframeworkwithparallelprocessing ingrateswithbeta1=0.9,beta2=0.999,andepsilon=1e-8. Learn-
across16workernodes,implementingmissingvalueimputation ingrateschedulingemployscosineannealingwithwarmrestarts,
throughiterativealgorithmsandoutlierdetectionusingstatistical wherethelearningratestartsat0.001andfollowsacosinedecay
Z-scoreandIQRmethodswithautomatedthresholdadjustment.As curve throughout training to a minimum value of 0.0001. This
showninTable1,therawdatacontainsmulti-dimensionalfeatures approachenablesthemodeltoescapelocalminimathroughperi-
with87%datacoverage,ensuringtrainingeffectivenessthrough odiclearningrateincreaseswhilemaintainingoverallconvergence
comprehensivedatavalidationpipelines. stability.
Featureengineeringemploysautomatedextractionalgorithms Training configuration optimizes computational efficiency:
and parallel processing pipelines. User behavioral sequences batchsize128balancesGPUmemoryutilizationandconvergence
include click streams with timestamp encoding, session-based speed,maximumepochs100withearlystoppingpatienceof10
browsingdurationmetrics,andfrequency-basedpurchasepatterns iterations. The loss function combines weighted cross-entropy
throughslidingwindowaggregation.Productpreferencefeatures addressingclassimbalancethroughinversefrequencyweighting
utilizecollaborativefilteringandmatrixfactorizationfromhistori- andL2regularizationwithcoefficient0.001appliedtoalltrainable
calpurchasematrices.Temporalfeaturescapturecyclicalpatterns parameters.
throughdiscreteFouriertransformsandseasonaldecomposition Dataaugmentationenhancesrobustnessthroughtemporaljit-
algorithms. Thefinal128-dimensionalfeaturevectorcomprises teringwith5%timeshiftvariance,Gaussiannoiseinjectionwith
behavioralsequences(45D),productattributes(25D),temporalfea- standarddeviation0.01,andslidingwindowsamplingwith15-day
tures(12D),userdemographics(8D),andinteractionhistory(38D). stride intervals. This increases training samples by 200% while
Sequencesegmentationuses30-dayslidingwindowswith50%over- preservingtemporaldependencies.
lapthroughparallelbatchprocessing,generatingtrainingsamples ThearchitectureimplementsXavieruniforminitializationfor
withmaintainedtemporalconsistency. weightmatricesandbatchnormalizationbetweenLSTMlayersfor
1266

LSTM-BasedConsumerBehaviorPredictionModelResearch DECS2025,October17–19,2025,Wuhan,China
Figure1:DataPreprocessingWorkflow.
Figure2:LSTMModelArchitecture.
trainingstability.Tooptimizeregularizationthroughoutthetrain- trainingwithFP16computation,reducingmemoryfootprintby
ingprocess,anadaptivedropoutschedulingstrategyisemployed: 40%whilemaintainingnumericalstability.
thedropoutratebeginsat0.5duringtheinitial30epochstoprovide Toaddressthecriticalchallengeoftrainingstabilityandconver-
strongregularizationagainstoverfitting,thenlinearlydecreases genceefficiency,weimplementedcarefullydesignedscheduling
to0.3andremainsatthisvaluefortheremainingtrainingepochs. strategiesforbothlearningrateanddropoutregularization. For
Thisscheduledapproachallowsthemodeltolearnrobustfeature learningrateoptimization,weadoptedacosineannealingschedule
representationsearlyintrainingwhileenablingfine-grainedpa- rather than conventional step-wise or exponential decay meth-
rametertuninginlaterstages. Thedropoutisappliedafterthe ods. The learning rate followsa smooth cosine curve fromthe
bidirectionalLSTMlayersandbeforethefullyconnectedlayersto initial value of 0.001 to the minimum value of 0.0001 over the
preventco-adaptationofhiddenunits. Memoryoptimizationuses entiretrainingprocess. Thisapproachoffersseveraladvantages:
gradientaccumulationover4mini-batchesandmixed-precision first,thegradualandcontinuousdecaypatternpreventsabrupt
1267

| DECS2025,October17–19,2025,Wuhan,China |     |     |     |     |     | ShuhanChenandWenciTan |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --------------------- | --- |
changesingradientmagnitudesthatcoulddestabilizetraining;sec- Table2:ModelPerformanceComparison.
ond,thecosinefunctionnaturallyprovidesfasterdecayinearly
epochswhencoarseadjustmentsarebeneficial,andslowerdecay Model Accuracy Precision Recall F1-Score
| in later epochs | to enable fine-tuning; | third, unlike | exponential |          |             |             |     |
| --------------- | ---------------------- | ------------- | ----------- | -------- | ----------- | ----------- | --- |
|                 |                        |               |             | Logistic | 0.782 0.756 | 0.798 0.776 |     |
decaywhichrequiresmanualtuningofdecayintervals,cosinean-
Regression
nealingprovidesamathematicallyprincipledschedulethatadapts
|     |     |     |     | Random | 0.835 0.821 | 0.849 0.835 |     |
| --- | --- | --- | --- | ------ | ----------- | ----------- | --- |
automaticallytothetotaltrainingduration.Fordropoutregular-
Forest
ization,weemployedanadaptiveschedulingstrategytobalance
|     |     |     |     | SVM | 0.798 0.789 | 0.807 0.798 |     |
| --- | --- | --- | --- | --- | ----------- | ----------- | --- |
overfittingpreventionandmodelcapacityutilizationthroughout
|     |     |     |     | BasicRNN | 0.856 0.842 | 0.871 0.856 |     |
| --- | --- | --- | --- | -------- | ----------- | ----------- | --- |
training.Thedropoutratebeginsat0.5duringtheinitial30epochs,
|     |     |     |     | Standard | 0.912 0.903 | 0.921 0.912 |     |
| --- | --- | --- | --- | -------- | ----------- | ----------- | --- |
providingstrongregularizationwhenthemodelparametersare
| randomlyinitializedandmostsusceptibletooverfittingontraining |                                      |     |     | LSTM     |             |             |     |
| ------------------------------------------------------------ | ------------------------------------ | --- | --- | -------- | ----------- | ----------- | --- |
|                                                              |                                      |     |     | Proposed | 0.942 0.938 | 0.947 0.942 |     |
| data. Afterepoch30,                                          | thedropoutratelinearlydecreasesto0.3 |     |     |          |             |             |     |
LSTM
overthenext20epochs,andremainsfixedat0.3forallsubsequent
training.Thisdesignrationaleisgroundedintheobservationthat
early-stagetrainingbenefitsfromaggressiveregularizationtolearn
| generalizablefeaturerepresentations, |     | whilelater-stagetraining |     |     |     |     |     |
| ------------------------------------ | --- | ------------------------ | --- | --- | --- | --- | --- |
Table2presentsdetailedcomparisonresultsofdifferentmodels
requiresreducedregularizationtoallowthemodeltofullyexploit acrossvariousmetrics,includingtraditionalmachinelearningmeth-
itscapacityforcapturingsubtlepatternsinconsumerbehavior ods(logisticregression,randomforest,supportvectormachine),
sequences.Thedropoutlayersarestrategicallypositionedafterthe basicneuralnetworkmodels(basicRNN,standardLSTM),andthe
bidirectionalLSTMoutputsandbeforethefullyconnectedlayers, improvedLSTMmodelproposedinthisstudy. Experimentalre-
ensuringregularizationisappliedtothemostparameter-richcom-
sultsdemonstratethattheLSTMmodelproposedinthisresearch
ponentswhilepreservingthetemporalinformationflowwithin significantlyoutperformscomparisonmethodsacrossallevalua-
therecurrentlayers. Theseschedulingstrategieswerevalidated tionmetrics,achievinganaccuracyof94.235%,representinga3.0
throughablationexperiments:modelsusingfixedlearningratesor percentagepointimprovementoverthebestbaselinemodel(stan-
fixeddropoutratesshowed2.3-4.7%loweraccuracyandexhibited dardLSTM)andanaverageimprovementof10.7percentagepoints
eitherprematureconvergenceortraininginstability,confirming
overtraditionalmachinelearningmethods.Statisticalsignificance
thenecessityofouradaptiveapproach. testing(p<0.001)indicatesthattheseperformanceimprovements
arestatisticallysignificant.
2.2 ModelPerformanceAnalysis
2 Experiments
TheLSTMmodeldemonstratesexcellentperformanceinconsumer
2.1 ExperimentalSetupandEvaluationMetrics
behaviorpredictiontasks.Figure3showstraininglosscurves,re-
TheexperimentalenvironmentwasconfiguredwithUbuntu20.04
vealingrapidconvergenceandgoodstability.TheproposedLSTM
system,Python3.8,TensorFlow2.6deeplearningframework,us-
modelachievesconvergencearoundthe25thepoch,whiletradi-
ingNVIDIARTX3080GPU(24GBmemory)formodeltraining,
tionalmethodslikelogisticregressionandSVMconvergeslowly
complementedbyIntelXeonE5-2680v4processorand64GBDDR4
|     |     |     |     | withhigherfinallosses. | Comparedtotraditionalmachinelearning |     |     |
| --- | --- | --- | --- | ---------------------- | ------------------------------------ | --- | --- |
memorytoensuresufficientcomputationalresources.Thedataset
methods,theLSTMmodel’saccuracyimprovedby16.2%,benefit-
wasrandomlydividedintotrainingset(350,000samples),validation
ingfrompowerfulsequentialmodelingandlong-termdependency
set(100,000samples),andtestset(50,000samples)ina7:2:1ratio,
capture. Themodelexcelsinhandlingcomplexuserbehaviorpat-
withstratifiedsamplingtoensurebalanceddistributionofdiffer-
|     |     |     |     | terns, particularly | purchase cyclicity, | seasonal preferences, | and |
| --- | --- | --- | --- | ------------------- | ------------------- | --------------------- | --- |
entcategorysamplesacrosssets,avoidingtheimpactofclassbias
cross-categorybehaviors.
| onmodelevaluation. | Tocomprehensivelyevaluatemodelperfor- |     |     |     |     |     |     |
| ------------------ | ------------------------------------- | --- | --- | --- | --- | --- | --- |
Table3demonstratesexcellentgeneralizationcapabilityacross
mance,thisstudyselectedAccuracy,Precision,Recall,andF1-score
|     |     |     |     | usergroups. | High-frequencyusersachievethehighestaccuracy |     |     |
| --- | --- | --- | --- | ----------- | -------------------------------------------- | --- | --- |
asprimaryevaluationmetrics,whichcanreflectthemodel’spre-
(96.1%)duetostablepatternsandabundantdata.Forchallenging
| dictivecapabilitiesfromdifferentperspectives. |     | Accuracymeasures |     |     |     |     |     |
| --------------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- |
newusers,themodelachieves91.8%accuracywith23.6%improve-
theproportionofcorrectlypredictedsamples,precisionreflects
mentovertraditionalmethodsbyutilizingshort-termbehavioral
theproportionoftruepositivesamongpredictedpositives,recall
|     |     |     |     | features | and similar user patterns. | High-value customers | with |
| --- | --- | --- | --- | -------- | -------------------------- | -------------------- | ---- |
representstheproportionoftruepositivesthatwerecorrectlypre-
complexbehaviorsreach96.7%accuracy,provingthemodel’ssupe-
dicted,andF1-scoreistheharmonicmeanofprecisionandrecall,
riorityinhandlingcomplexdecision-making.
| providingcomprehensivemodelperformanceevaluation. |     |     | Addi- |     |     |     |     |
| ------------------------------------------------- | --- | --- | ----- | --- | --- | --- | --- |
tionally,10-foldcross-validationwasemployedtoensureresult
2.3 FeatureImportanceandModel
reliabilityandstability,witheachexperimentrepeated5timesand
Interpretation
| averagedtoreducetheimpactofrandomfactors. |     |     | Furthermore, |     |     |     |     |
| ----------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- |
AUC-ROCareaunderthecurveandconfusionmatriceswerecal- Thisstudyrevealsthemodel’sinternalworkingprinciplesthrough
culatedtofurtheranalyzemodelperformancedifferencesacross attentionweightanalysisandfeatureimportanceassessment. Fig-
differentcategories. ure4displaysattentionmechanismweightdistributionfor15key
1268

LSTM-BasedConsumerBehaviorPredictionModelResearch DECS2025,October17–19,2025,Wuhan,China
Figure3:TrainingLossCurvesComparison.
Table3:PerformanceAnalysisbyUserGroups.
UserGroup SampleSize LSTMAccuracy TraditionalMLAccuracy Improvement
| High-frequencyUsers | 15,420 | 0.961 | 0.798 | 20.430% |
| ------------------- | ------ | ----- | ----- | ------- |
| Medium-frequency    | 28,670 | 0.935 | 0.821 | 13.890% |
Users
| Low-frequencyUsers  | 18,230 | 0.923 | 0.775 | 19.100% |
| ------------------- | ------ | ----- | ----- | ------- |
| NewUsers            | 12,890 | 0.918 | 0.743 | 23.560% |
| High-valueCustomers | 8,560  | 0.967 | 0.812 | 19.090% |
Table4:FeatureImportanceRanking.
| Rank |                           | FeatureName | ImportanceScore | FeatureType |
| ---- | ------------------------- | ----------- | --------------- | ----------- |
| 1    | PurchaseFrequencySequence |             | 0.187           | Behavioral  |
| 2    | ProductBrowsingDuration   |             | 0.156           | Behavioral  |
| 3    | PriceSensitivityIndex     |             | 0.142           | Preference  |
| 4    | CategoryPreferenceHistory |             | 0.123           | Behavioral  |
| 5    | SeasonalPurchasePattern   |             | 0.108           | Temporal    |
| 6    | CartAdditionFrequency     |             | 0.095           | Behavioral  |
| 7    | UserAgeGroup              |             | 0.078           | Demographic |
| 8    | TimeSinceLastPurchase     |             | 0.067           | Temporal    |
| 9    | AverageOrderValue         |             | 0.058           | Economic    |
| 10   | BrandLoyaltyScore         |             | 0.052           | Preference  |
featureswithina30-daywindow.Keypatternsinclude:obviousre- seasonalpreferences(0.108). Table4presentsthecompletefea-
cencybiaswithhigherweightsforrecent7-daybehaviors(recency tureimportancerankingwithdetailedscoresandfeaturetypes.
biasratio1.847),behavioralfeatures(purchasefrequency,browsing Thesefindingsalignwithconsumerbehaviortheory,validatingthe
duration)receivinghigherweightsthandemographicfeatures,and model’spracticalsignificance.
seasonalpreferencesshowingincreasedweightsatspecifictime Behavioralfeaturesdominate(cumulativescore0.521),proving
pointslikeholidays. morepredictivethandemographicfeatures.Ablationexperiments
Analysisidentifieskeyinfluencingfactors:purchasefrequency confirmremovinganyTop-5featurecauses3.2percentagepoint
(0.187), browsing duration (0.156), price sensitivity (0.142), and performancedecrease. SHAPanalysisshowspositivevaluesfor
1269

DECS2025,October17–19,2025,Wuhan,China ShuhanChenandWenciTan
Figure4:AttentionWeightVisualization.
purchasefrequencyandbrowsingdurationinhigh-intentionusers. References
Erroranalysisrevealsimprovementneedsforimpulsivepurchasing, [1] YuanF,LinZ,TianZ,etal.Bio-inspiredhybridpathplanningforefficientand
externalevent-drivenconsumption,andearlyadopterbehaviors. smoothroboticnavigation:F.Yuanetal[J].InternationalJournalofIntelligent
RoboticsandApplications,2025:1-31.
[2] LiuZ,YuanC,ZhangZ,etal.AhybridYOLO-UNet3Dframeworkforautomated
3 Conclusion proteinparticleannotationinCryo-ETimages[J].ScientificReports,2025,15(1):
25033.
ThisstudysuccessfullyconstructedanLSTM-basedconsumerbe- [3] XuL,YuanC,JiangZ.Multi-strategyenhancedsecretbirdoptimizationalgorithm
havior prediction model, effectively improving prediction accu- forsolvingobstacleavoidancepathplanningformobilerobots[J].Mathematics,
2025,13(5):717.
racyandgeneralizationcapabilitythroughdeeplearningtechnol-
[4] XiaoN,YuanCH,PeiYT,etal.Astudyofartificialintelligenceinwriting
ogy. Experimentalresultsvalidatethesignificantadvantagesof assessmentforsecondaryschoolstudents:acomparativeanalysisbasedonthe
LSTMnetworksinprocessingconsumerbehaviorsequentialdata, GPT-4andhumanraters[J].EducationalStudies,2025:1-23.
[5] Cui,J.,&Yuan,C.(2025).Multi-scalefeatureaggregationwithhierarchical
withthemodelachieving94.235%accuracy,representinga3.0per- semanticsanduncertaintyassessment:enablinghigh-accuracyvisualretrieval.
centagepointimprovementoverthebestbaselinemodelandan TheJournalofSupercomputing,81(10),1-26.
[6] WangY,ZhangH,YuanC,etal.Anefficientschedulingmethodinsupplychain
averageimprovementof10.7percentagepointsovertraditional
logisticsbasedonnetworkflow[J].Processes,2025,13(4):969.
machine learning methods. Through introducing self-attention [7] Liu,Z.,Chen,P.,Wang,Z.,Ala,A.,&Pethuraj,M.S.(2024).OpHSS:Optimized
mechanismsandoptimizedmulti-layerbidirectionalarchitecture, pHSensingSynergyAlignmentinIoTBackboneNetworksforPrecisionFarming.
IEEESensorsJournal,24(24),20910-20920.
themodelpreciselycapturestemporalfeaturesandlong-termde-
[8] Wang,Zongshan,etal.”EnergyEfficientClusterBasedRoutingProtocolfor
pendenciesofuserbehavior,providingstrongtechnicalsupportfor WSNUsingFireflyAlgorithmandAntColonyOptimization.”WirelessPersonal
e-commerceplatforms’personalizedrecommendations,intelligent Communications(2022):1-34.
[9] Yang,J.,Qin,H.,Sun,Y.,Wang,H.,Khan,A.A.,Por,L.Y.,&Alizadehsani,R.
inventorymanagement,andprecisionmarketingstrategies.Future (2025).Agenerativeadversarialnetwork-basedextractivetextsummarization
researchdirectionsincludeintegratingexternalenvironmentalfac- usingtransductiveandreinforcementlearning.IEEEAccess,9.
[10] Yang,J.,Wu,Y.,Yuan,Y.,Xue,H.,Bourouis,S.,&Mahmoud,…(2025).LLM-AE-
tors,exploringmultimodaldatafusiontechnologies,developing
MP:Webattackdetectionusingalargelanguagemodelwithautoencoderand
lightweightmodelarchitecturesforreal-timeprediction,andcon- multilayerperceptron.ExpertSystemswithApplications,12.
structingdynamicmodelupdatemechanismstoensuresustained
predictionperformancestability.
1270