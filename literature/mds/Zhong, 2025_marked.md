---
conversion_metadata:
  converted_at: "2026-10-11T15:14:03Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Zhong, 2025.pdf"
  source_pdf_sha256: "2f725d1b7d7412c203d3e9e27d6458ef7284a32e18974ce5491ad5c056c29096"
  page_count: 10
  markdown_char_count: 45907
---

Adaptive Anomaly Detection Threshold for Financial Data
Quality Monitoring Based on Time Series Features
∗
MinjuZhong
M.S.inAnalytics
UniversityofChicago
Chicago,USA
jack33361@gmail.com
Abstract ACMReferenceFormat:
As financial data streams evolve continuously with changing MinjuZhong.2025.AdaptiveAnomalyDetectionThresholdforFinancial
DataQualityMonitoringBasedonTimeSeriesFeatures.In2025Interna-
anomalous patterns and customer behaviors, traditional static
tionalSymposiumonArtificialIntelligenceandComputationalSocialSciences
threshold-basedanomalydetectionsystemsexhibitsignificantlimi-
(AICSS2025),September19–21,2025,Beijing,China.ACM,NewYork,NY,
tationsinadaptingtodistributionalshifts,leadingtoelevatedfalse
USA,10pages.https://doi.org/10.1145/3776759.3776850
positivesandcompromiseddetectionaccuracy. Inthecontextof
financialtransactionmonitoring,itbecomescrucialtodistinguish 1 INTRODUCTION
betweennaturaldistributionchangesandgenuineanomalieswhile
1.1 ResearchBackgroundandMotivation
maintainingoperationalefficiency.Thispaperaddressesthechal-
lengeoftrainingwithonlynormaldatainitially,whilesubsequent Withmillionsoftransactionsbeingprocessedeverydaybybanks,
streamingdatacontainsbothnormalandanomalousinstances,ne- thedataisvastandneedstobemonitoredwithoneeyelookingfor
cessitatingadaptivethresholdmanagement.Weproposeadynamic expectedactivityandtheotherlookingforanomalies.Aserviceob-
thresholdadjustmentframeworkthatleveragestimeseriesfeature servingthecurrentdataqualityisnotsufficientforthedevelopment
extractioncombinedwithunsupervisedlearningtechniquestocal- oftransactionpatternsandmorecomplexanomalouspatterns[1].
ibratedetectionthresholdsbasedonevolvingdatacharacteristics Threshold-basedrecognitionfailstoadapttodynamictransaction
automatically. Ourmethodologyintegratesslidingwindowsta- patterns,whichleadstohighfalsepositivesandmisseddetections.
tisticalanalysiswithBayesianchangepointdetectionalgorithms Thecomplexityoffinancialdatastreamsmakesithardtoutilize
toidentifysignificantpatternshifts. Atthesametime,ensemble traditionalmonitoringmeansdirectly.Transactionsystemshave
approachescombiningIsolationForest,DBSCANclustering,and specificdifficultiesregardingtemporalchanges;thespendingbe-
LocalOutlierFactorproviderobustanomalyscoringmechanisms. haviourcalendarofagivenconsumercanindeedvaryalongthe
Theframeworkusesseasonaldecompositionandtrendanalysisto year,andalsocustomerdemographicsaresomewhatmovingtar-
capturetemporaldependenciesinfinancialtransactiondata.Exper- gets;andlastbutnotleast,newanomalousmethodsmaymake
imentalresultsonsyntheticfinancialdatasetsdemonstratesuperior one’sgainedefficiencyoverspecificstaticthresholdsettingsbe-
performancecomparedtofixedthresholdapproaches,achievinga comeoutofdate[2].Adaptivethresholdevolutionisthenextstep
precisionof0.847,arecallof0.891,andanF1-scoreof0.868,with inaddressingtheseoperationalissuesandcontinuestosupportthe
asubstantial46.5%reductioninfalsefavorablerateswhilemain- system’seffectiveperformance.However,thechallengesofquality
tainingreal-timeprocessingcapabilitiesforregulatorycompliance forfinancialfirmsarenotonlyinoperationsbutalsoextendto
requirements. howthefirmenforcesregulationsandmanagesrisk.Supervisory
stresstestingregimessuchasCCARandDFASTimposestringent
CCSConcepts requirementsonthevalidationprocessandhavemadetheaccurate
• Computing methodologies → Machine learning; Learning identificationofanomaliesanintegralaspectofsatisfyingregula-
tion[3].Solution:Innovative,evolutionaryadaptivethresholdsthat
paradigms.
satisfytheseconditionsofferamoreeffectivechoicefordetecting
novelanomalouspatterns.
Keywords
Adaptivethreshold, financialdataquality, Timeseriesanomaly 1.2 ProblemStatementandObjectives
detection,Unsupervisedlearning
Thestaticthreshold-basedtreatmentinpaymentcardsurveillance
systemshasaninherentweaknessforalltypesoftransactionpat-
∗Correspondingauthor terns,rangingfromslowupsurgestocompletetrendreversals,as
wellasfromtherelatedcustomerlifestylechanges.Staticthreshold
settingsdonotadapttogenuinedifferencesinpurchasingpolicies,
seasonalbuying,orevolvingcustomerpreferences,leadingtomany
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. falsealarms,increasedoperationalcosts,andreducedsystemef-
AICSS2025,Beijing,China ficiency[4]. Therefore,theprimaryfocusofthestudyhereison
©2025Copyrightheldbytheowner/author(s).
howtodevelopanadaptivethresholdarchitecture,whichiscapa-
ACMISBN979-8-4007-2100-7/2025/09
https://doi.org/10.1145/3776759.3776850 bleofdynamicallychangingdetectionparameterstoadapttothe
578

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
time-seriespatternsofthefinancialtransactiondata. Atitsheart, theadaptabilityoffinancialanomalydetectionsystemsisbecoming
itisanattempttoincreasedetectionreliabilityandminimizefalse moreandmoreemphasized. Anomalydetectioninbanking: We
positivesthroughwisecalibrationofthresholdsbasedontemporal noticeasignificantdifferenceacrossbankinganomalydetection
transactionpatterns[5]. Thepaperservesapracticalpurposeof systemsintermsofcharacteristicsindataundertakingandtheop-
adaptivelyadjustingthethresholdofthepeakdetectorbasedonthe eratingenvironment. SequentialanalysisbyadeeplearnedLSTM
environmentwithoutconstantlyrequiringmanualrecalibration. architectureexperiencedenhanceddetection,especiallyunderearly
Expectedresearchcontributionsincludebetterdatagovernance, stoppingtopreventoverfittingondynamicfinancialmarkets.Fed-
whichwillbeachievedbyhavingabetteranomalydetectionper- eratedlearningalgorithmshavebeenconsideredtobeanapproach
formance,areductionofoperationalburdenduetodecreasingfalse withthebestperformanceforprivateanomalydetectioninthe
positivesinanomalydetection,orbetterregulatorycompliance significantlydifferentenvironmentsofdifferentbanks.
duetoaccuratedetectionofrealqualityissuesforusers.
2.2 AdaptiveThresholdTechniquesand
1.3 PaperStructureandContributions Applications
Somenewfeaturesofouradaptivethresholdframeworkarenot Thresholding of adaptivity in stream processing has developed
availableforfinancialtransactionanalysis. Theproblemismuch fromsimplestatisticalalgorithmstocomplexmachinelearningal-
morecomplexifnonstationarysettingsaretobeconsidered. In gorithmsprocessingnon-trivialtemporalpatternsandconceptdrift.
thisPaper,wemakethefollowingcontributions: (1)wepropose Rule-baseddecisionlistsinfederatedlearningforcreditcardanom-
adynamicthresholdlearningtechniquebyanalyzingthesliding alydetection.Thispresentworkrepresentsanotableadvancement
windowstatisticalproperties;(2)wecombinedifferentunsuper- asthedecisionlistactsasanadaptivethresholdingapplicationto
visedlearningtechniquestoimprovetheanomalyscore;(3)we improvepredictionaccuracyundertheprivacyconstraintorpri-
proposeawayofautomaticallytuningtheparameterstotackle vacypreservation. Settingthresholdscontinuouslyinachanging
changesindatacharacteristics[6][7].Thetimeseriesfeaturesex- environmentbasedonmachinelearning,reinforcementlearning,
tractiontechniquesconsideredinthisworkforthedetectionof andneuralnetworks,swarmintelligencewasemployedtodetect
financialtransactionsequencesabletodescribethetemporalpat- andtunetheparametersofstreamingdatacharacteristicsautomati-
ternscharacteristicofthesesequencesarethefrequencydomain, cally.Inthedomainofcreditcardanomalydetection,architectures
seasonaldecomposition,andstatisticaltrendanalysis.Allofthese thatcanprovideexplanationsandinterpretations,suchasTabNet,
perceptualaspectsofbehaviortuneafiner-grainedthresholdand areparticularlypromisinginthesensethattheynotonlycanoffer
discovertherequisiteexceptionsinvarioustransactionalscenarios, explanationsandinterpretationswhiledetectingbutalsohaveper-
suchascustomerbehaviour[8]. Theproposedframeworkcanbe formancenotworsethananystate-of-the-artmethodsreportedso
appliedtoqualitycontrolsystemsrequiringregulatorycompliance, far. Adaptivethresholdinginfinancialanomalydetectionsystems
operationalcostreductionthroughdecreasedfalsepositives,and hasledtosignificantbreakthroughsindetectionrateaswellas
enhancedriskmanagementcapabilities. operationalefficiency.SomeGRUnetwork-basedmethodsworking
inthepastfewyearsshowedsatisfactoryresultsinsuchafieldas
2 RELATEDWORKANDLITERATURE financialanomalydetection,especiallytogetherwithensembling,
whenacoupleofalgorithmsmetinthecentreinordertohave
REVIEW
anotheralgorithmtodecidewhosesideitis.Whatthesedevelop-
2.1 TimeSeriesAnomalyDetectioninthe mentsreinforceistheneedforagileresponsesinordertoaddress
FinancialDomain upcominganomaliesandevolvingconsumerbehaviour.
Theseminalliteratureonthedetectionoffinancialanomaliesis
2.3 FinancialDataQualityMonitoringSystems
groundedinstatisticalcontrolmodels,forwhichtheoriginisrooted
intheideaofcontrolcharts. Theconceptwastouseabnormality The current practice of financial data (1) governance (i.e., data
detection(e.g.,controlchartsandweightedmovingaverages)in qualitycontrol)istogenerateautomatedmonitoringcomponents
thesamemannerasithadbecomesuccessfulfortheapplication taskedwithamassivescaleoftransactionsathighaccuracyand
inqualitycontrolprocesses. Someattemptshavebeenmadein efficiencyrequirements.Havinglearnedabouttheseinsights,the
theintroducedsetofmethodstoatleastprovideapointofdepar- machine-learning-basedalgorithmsbehindcreditcardanomaly
turefordealingwiththisproblem. Still,theylimitthemselvesto detectionreturnthatknowledgetotheflowofnewtransactions
simplecaseswhencomplextimedependenceandmorecomplex inreal-time,whereallsortsoftransactionpatternscanbeseen.
nonstationarymotionofhigh-dimensionalfinancialdataaretypical Banking’sdataqualityasksaregrowingtoaskforend-to-endvali-
[9].Withtimeseriestransactionmonitoring,poweredbymachine dationframeworks—notonlyforsourcesystemstooperatingsys-
learning,thesemethodshavecompletelyflippedthefieldonits tems,butaroundtheoperatingsystems. Structuraldataquality
head.Forexample,thelearningarchitecturesofensemblemethods challengesstemmingfromtheconsolidationoflargeandgrowing
anddeeplearningcannowdiscernextremelysubtlepatternsinfi- monitoringdatasetsarealsomainlyduetosupervisory-ledstress
nancialstreamsofdata.Adaptiveanomalydetectionhassucceeded testingprograms(e.g.,CCAR,DFAST)thatnecessitatestrongdata
inRL-basedapproaches[10]. Moreover,incomparisontoconven- qualitypractices,whichmandatetheabilitytodetectandresolve
tionalrule-basedapproaches,GNNscanbetterbeusedtodetect exceptionsearlyenoughtopreventdownstreamadverseeffects,i.e.,
anomaliesinanevolvingnetworksetting.Theseresultsshowthat reportingorregulatorypenalties. Bankingcompetitionrequires
579

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table1:AdaptiveThresholdAlgorithmParameters
Parameter Description DefaultValue Range
WindowSize(W) Numberofobservationsintheslidingwindow 1000 500-5000
SensitivityFactor(𝛼) Thresholdadjustmentsensitivity 0.15 0.05-0.30
DecayFactor(𝛽) Historicalweightdecayrate 0.95 0.80-0.99
ChangePointThreshold(𝛾) Statisticalsignificanceforpatternchanges 0.01 0.001-0.05
thesestandardstocorrespondtomoresophisticatedtechniquesof throughhistoricalcontextweighting.Additionally,robustparame-
anomalydetection. Thecombinationofdifferenttypesofcorpo- terestimationwithineachwindowemploysestimatorsthatwere
rates,locatedindifferentfinancialdatasystems,intoonefinancial designedtominimizetheimpactof”outliers”butremainsensitive
(IT)systemisacomplexchallengeinthesensethatitneedsmoni- tofundamentalpatternchanges.
toringcapabilitiesthatcrosssuchtechnologicalbordersanddata
sources.Underthecontextofdeeplearning,LSTM,asasequence 3.2 TimeSeriesFeatureExtractionforFinancial
analysis,showsbetterperformanceindynamicfinancialsystem Data
detection, andithasbeenenhancedbyearlystoppingtoavoid
Toinferthetimingofcreditcardtransactionpatternsrequiresafull
overfitting[11].
investigationofhowtimingcanexpressitselfintransactions.The
featureextractionprocessanalyzestemporalrelationshipswithin
3 METHODOLOGY
transactionsequencestoidentifycharacteristicpatterns.Thispro-
3.1 AdaptiveThresholdFrameworkDesign cesscapturesvariousstatisticalpropertiesandtemporaldependen-
Ouralgorithmusesslidingwindowstatisticalanalysistocalculate ciesthatdefinenormaltransactionbehavior.Withthedevelopment
bothglobalandlocalparametersforthresholdadjustment. The oftechnologyinthepastfewyears,peoplehaveappliedmanynew
frameworkemploysamulti-moduledesignwhereslidingwindow techniquesforfinancialtimeseriestrendanalysis,includingad-
analysiscontinuouslymonitorstransactionpatterns.Eachmodule vancedstatisticalmethods.
processesincomingtransactiondatatocalculatestatisticalparam- Howdoesvolatilitychangeoverthetimeprofileoftransactions?
eters for threshold adjustment. Through this adaptive learning Featuresofvariousdistributions—statisticalfeatureengineeringon
process,thresholdboundariesautomaticallyadjustbasedonde- transactionamountandfrequencyanalysisincludescalculations
tectedchangesindatacharacteristics. formovingaverages(rollingstats),methodsthatarebasedonthe
Timeseriessegmentationbecomesanessentialcomponentof percentiles, andmeasurestocapturetheessentialpropertiesof
adaptive thresholds and uses statistical change point detection transactionsequences.Thefeatureextractionalgorithmcarriesout
algorithmstodeterminemajorpatternshiftsthatrequireadjust- statisticalcomputationsthatchangewithtime—suchasmoving
mentindetectedthresholds. Thus,theprocessofsegmentation averagelevelsandstandarddeviations,skewness,andkurtosisover
isdonewithBayesianchangepointdetectiondetectorsthatare differenthorizons—providingacomprehensivecharacterizationof
usedtogetherwithinformation-theoreticalcriteriaandevidence transactionpatterns.
fordetectedchanges.
Formally,foratransactionsequenceX={x₁,x₂,…,xₙ},wecom-
Thesystemcontinuouslyevaluatesdetectionperformanceand pute:
a p u o t s o it m iv a e t s ic a a n l d ly m a i d s j s u e s d ts de th te r c e t s i h o o n l s d w p h a i r l a e m m e a t i e n r t s ai t n o in m g in sy im st i e z m eb e o ffi th cie fa n l c s y e . 𝑀𝑜𝑣𝑖𝑛𝑔𝐴𝑣𝑒𝑟𝑎𝑔𝑒 :𝑀𝐴(𝑡)=(1/𝑊)· (cid:213) 𝑖=1 𝑊 +1 𝑡·𝑥 𝑖 (2)
Thekeyparametersoftheadaptivethresholdalgorithmaresum- 𝑀𝑜𝑣𝑖𝑛𝑔𝑆𝑡𝑎𝑛𝑑𝑎𝑟𝑑𝐷𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛:
marizedinTable1. 𝜎(𝑡)= √ [(1/𝑊)(cid:205)
𝑖=1
𝑊
+1
𝑡(𝑥
𝑖
−𝑀𝐴(𝑡))] (3)
Note that the number of its transactions is a measure of the
Window Size. Sensitivity Factor and Decay Factor are both di- 𝑆𝑘𝑒𝑤𝑛𝑒𝑠𝑠 :𝛾 1 (𝑡)=𝐸(cid:2) (𝑋 −𝜇)3(cid:3) /𝜎3 (4)
m sta e t n is s t i i o c n a l l e s s i s gn ra ifi ti c o a s n . c H e o le w v e e v l e (𝛼 r, -l t e h v e e C ls h ) a fo n r g p e a P tt o e i r n n t s Th hi r ft e s s : h i o ts ld de is fa t u h l e t 𝐾𝑢𝑟𝑡𝑜𝑠𝑖𝑠 :𝛾 2 (𝑡)=𝐸(cid:2) (𝑋 −𝜇)4(cid:3) /𝜎4 (5)
valuewassetbycross-validationtestsonsyntheticfinancialdata.
whereWisthewindowsize,E[·]denotesexpectation,𝜇isthemean,
Theadaptivethreshold𝜏(t)attimetiscomputedusinganexponen- and𝜎isthestandarddeviation.
tialdecayfunction: Figure1illustratesthearchitectureofourtimeseriesfeatureex-
tractionpipeline.Thecoredecompositionprocessinvolvesseasonal
𝜏(𝑡)=𝜇(𝑡)+𝛼×𝜎(𝑡)×𝛽(𝑡−𝑡 0 ) (1) analysis,exponentialsmoothingtechniques,andtrendanalysis.
where𝜇(t)isthemeanofobservationsinthecurrentwindow,𝜎(t) Thecoredecompositionprocessinvolvesseasonalanalysis,expo-
is the standard deviation, 𝛼 is the sensitivity factor controlling nentialsmoothingtechniques,andtrendanalysis. Todisassemble
thresholdstrictness,𝛽isthedecayfactor(0<𝛽<1)thatreduces thetimeseriesoftransactions,weusedifferentdecomposingtech-
theinfluenceofhistoricalinformation,andt0isthereferencetime niquestoseparateitstrends,seasonalitycomponents,andresidu-
point. Thisformulationenablesautomaticthresholdadjustment als.Theinputsforthresholdamountadjustmentmethods,which
basedoncurrentdatacharacteristicswhilemaintainingstability willadaptpredictablyaccordingtoknownseasonalchangesand
580

| AICSS2025,September19–21,2025,Beijing,China |     |     |     |     |     |     |     | MinjuZhong |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Figure1:TimeSeriesFeatureExtractionPipelineArchitecture
underlyingtrendpatterns,arethesecomponentsthathavebeen whileatthesametimebeingsensitivetounconventionalbehaviour
| decomposedintotheirconstituentparts. |     |     |     |     | [13]. |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ----- | --- | --- | --- |
Thefeatureextractionpipelinewillintegratemultipleparallel Integratedensemblemethodsareadoptingmultipleunsuper-
processingstreamstoofferafull-thumbnailcharacterizationof visedalgorithms.Itgivesbetterrobustnessandaccuracythrough
transactionpatterns,bothforcomputationalefficiencyinreal-time theweightedcombinationofeachindividualalgorithm.Theensem-
applicationsandtoensurerecognizability.Eachprocessingstream bleapproachintegratesIsolationForest,DBSCANclustering,and
studiesdifferentaspectsoftransactionalbehaviour,includingits
LocalOutlierFactoralgorithms,withdynamicweightadjustment
timedependencies,statisticalproperties,andfrequencydomain dependingondifferentdataregimesandtransactionmodes.
patternscharacteristicoftransactionsequencesthatcontributeto TheensembleanomalyscoreS(x)fortransactionxcombines
| adaptivethresholdcomputation. |     |     |     |     | multiplealgorithms: |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
=Σ𝑀
|     |     |     |     |     |     | 𝑆(𝑥) | 𝑤 𝑗 ×𝑠 𝑗 (𝑥) | (6) |
| --- | --- | --- | --- | --- | --- | ---- | ------------ | --- |
𝑗=1
3.3 UnsupervisedLearningIntegration whereMisthenumberofalgorithms(M=3:IsolationForest,DB-
|     |     |     |     |     | SCAN,LocalOutlierFactor),𝑠 | 𝑗(𝑥)isthenormalizedanomalyscore |     |     |
| --- | --- | --- | --- | --- | -------------------------- | ------------------------------- | --- | --- |
Robustanomalydetectioncapabilitiesthatcomplementtheadap-
|     |     |     |     |     | fromalgorithmj,and𝑤 | isthedynamicweightsatisfying(cid:205)𝑤 |     | =   |
| --- | --- | --- | --- | --- | ------------------- | -------------------------------------- | --- | --- |
𝑗 𝑗
tivethresholdmechanismareprovidedbytheimplementationof
1.Weightsareupdatedbasedonalgorithmreliability:
anIsolationForestforoutlierscorecomputation.Theformeronly
m a k es b i n a r y j u d g m e n t s , w h i l e t h e la tt e r g e n e r a t e s c on t in u ou s 𝑤 (𝑡)=𝐴𝑈𝐶_𝑅𝑂𝐶 (𝑡)/Σ 𝑀 𝐴𝑈𝐶_𝑅𝑂𝐶 (𝑡)
|                |                         |                         |                          |                  | 𝑗   | 𝑗   | 𝑘 =1 | 𝑘 (7) |
| -------------- | ----------------------- | ----------------------- | ------------------------ | ---------------- | --- | --- | ---- | ----- |
| an o m al ie s | . I s ol a t io n F o r | e s t’ s p a r a m e te | rs a r e s u b j e c t e | d to d y n am ic |     |     |      |       |
optimisationbasedondatacharacteristics,withcontaminationrates where𝐴𝑈𝐶_𝑅𝑂𝐶 𝑗(𝑡)istheareaundertheROCcurveforalgorithm
andtreedepthparametersbeingoptimisedthroughcross-validation
jattimet,evaluatedonrecentvalidationdata.Thedetailedconfigu-
techniquesthatconsidertemporaldependenciesinfinancialdata rationparametersandoptimizationmethodsforeachunsupervised
| [12]. |     |     |     |     | learningalgorithmarepresentedinTable2. |     |     |     |
| ----- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
DBSCANclusteringfortransactionpatternidentificationlays The integration framework you designed serves not only to
thefoundationsforadaptivebatch-andcross-customercalibration. balanceweightsbetweenthedifferentunsupervisedalgorithmsbut
Adaptivetransactiontype-basedbehaviouralgroupingsaremade toprovideseamlesscoordinationamongthemwithinareal-time
inordertohelpestablishthresholds. Clusteringisabletoapply processingscenario. Thealgorithmoutputiscombinedthrough
distance metrics that consider transaction proximity as well as weightedvoting,consideringthereliabilityofindividualalgorithms
volumetoachieveeffectiveclassificationofsimilartransactions inadditiontoperformance-dependentonthenatureofthedata.
581

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table2:UnsupervisedLearningAlgorithmConfiguration
Algorithm KeyParameters OptimizationMethod PerformanceMetric
IsolationForest n_estimators=200,contamination=auto GridSearchCV AUC-ROC
DBSCAN eps=adaptive,min_samples=10 SilhouetteAnalysis ClusterValidity
LocalOutlierFactor n_neighbors=20,contamination=0.1 BayesianOptimization Precision-Recall
DynamicallyadjustDBSCAN’sparametersforAdaptiveSelec- wealterthetimeindicesproducedbylongdelaysandpoornetwork
tion: bandwidthofactualfinancialdatastreamstogeneratedatasets
DBSCAN’s𝜖parameteradaptstolocaldatadensitythrough: thataremoreinlinewithourownresearchpersonnel’sphysical
𝜀(𝑖)=𝑃𝑒𝑟𝑐𝑒𝑛𝑡𝑖𝑙𝑒 90 (𝐷_𝑘(𝑊 𝑖)) (8) medium.
Thissyntheticdatasetcontainsmultipletypesofanomalies,in-
whereD_k(Wᵢ)={d_k(p)|p∈Wᵢ}representsthesetofk-nearest
cludingsuddenincreasegaps,atypicalgeographicalbackgrounds,
neighbordistancesforallpointspinwindowWᵢ,andd_k(p)is thetimeofyearwhenthishappensbeingnonseasonal,anddevi-
thedistancefrompointptoitskthnearestneighbor. The90th ationsfromtheeverydaytradingcategoriesscenarios. Statistical
percentileensuresrobustnessacrossvaryingtransactiondensities verificationsuggeststhatwehaveeffectivelycapturedinthisar-
whilemaintainingsensitivitytooutlierpatterns.Themin_samples tificialmaterialnotjustthefactsabouttransactionsbutalsotheir
parameterisfixedat10toensurereliableclusterformationwhile realisticinterrelationshipsanddependenciesfromtheoriginalau-
detectingirregulartransactionpatterns. thenticmaterial.
4 EXPERIMENTALDESIGNAND
IMPLEMENTATION 4.1.1 SyntheticDataLimitationsandReal-WorldConsiderations.
Whilesyntheticdatasetsenablecontrolledexperimentationand
4.1 DatasetDescriptionandPreprocessing
reproducibility,severalimportantdistinctionsfromrealfinancial
Asaresult,weroutinelycreatesimulatedMonteCarlotransactions. datawarrantdiscussion:
Thesetransactions,usingtheattributesofeverydaysalesitems,pay- DataDistributionCharacteristics:Realfinancialtransactiondata
mentforvariouscommodities,positioninaworkingdayorseason exhibitscomplex,evolvingpatternsinfluencedbymacroeconomic
oftheyear(occasionssuchasbirthdaysandChristmas,contracep- factors,regulatorychanges,andemergentfraudtacticsthataredif-
tives,etc.),andvariousformsoftransactionalanomalies,including ficulttofullycaptureinsyntheticgenerationmodels.Oursynthetic
unusualtransactionamountsandtimingpatternsthatrepresent dataapproximatesstatisticalpropertiesofrealtransactionsthrough
dataqualityissuesinstandardcreditcards.Afterstatisticalmodels parametricmodeling,butmaynotfullyrepresentthelong-taildis-
ofrealtransactionsareturnedintorecordsinthemannerabove, tributionsandrareeventcombinationspresentinactualfinancial
theyhavetobetransferredintoaparticularformofpublicisedmask systems.
thatcannotbecommonlyrecognised. Thesyntheticdatagenera- TemporalDependencies:Real-worldfinancialdatacontainsin-
tionprocessincorporatesvariousanomalypatternsthatchallenge tricatetemporalcorrelationsspanningmultipletimescales—from
detectionsystems,includingthosedesignedforinterpretablearchi- intradaytradingpatternstomulti-yeareconomiccycles. While
tecturessuchasTabNet[14],ensuringcomprehensiveevaluationof oursyntheticgenerationincorporatesdailyandseasonalpatterns
theproposedadaptivethresholdframework.Thecomprehensive basedonstatisticalmodels,itmaynotcaptureallnuancedtemporal
characteristicsandstatisticsofoursyntheticdatasetaredetailedin dependenciespresentinoperationalfinancialsystems,particularly
Table3. those arising from external economic shocks or unprecedented
Beforewegoon,rememberthathandlingmissingdatapointsina marketevents.
datapreprocessingtaskofsuchmagnitudeisjustonestep.Missing AnomalyRepresentation:Thesyntheticanomaliesinourdataset
valuesarehandledbythecodewithmethodssuchastemporal aregeneratedbasedonknownpatterns(unusualamounts,timing
interpolation,whichpreservestatisticalpropertiesembeddedin deviations,geographicalinconsistencies). Real-worldanomalies
the sequences of transactions. Noise reduction algorithms use mayexhibitnovelcharacteristicsnotrepresentedinhistoricalpat-
adaptivefilteringtodistinguishbetweenmeasurementnoiseand terns,presentingadditionalchallengesfordetectionsystems. This
thelegitimatetransactionvariance, soastoretaintheessential limitationispartiallymitigatedbyouradaptivethresholdframe-
patterninformationbasedonsounddataqualityconsiderations. work’s unsupervised learning approach, which can identify de-
Featurestandardizationmethodsuserobustscalingtechniquesthat viationsfromlearnednormalpatternswithoutrequiringlabeled
arelesssusceptibletooutliersbutstillallowrelativetransaction anomalyexamples.
characteristicrelationshipstobekept.Precisetimedregistration PrivacyandDataAccessConstraints: Theuseofsyntheticdata
processingneedstobedescribedsothatthetimeindexofeachdata wasnecessitatedbyprivacyregulationsandproprietaryconstraints
sourceisconsistentwithreal-worldfinancialdatastreams.Also,the preventingaccess to real financial transaction data. While this
processing-inducedoperationdelaysandsystemlatenciesfoundin limitsdirectvalidationagainstoperationalsystems,itenablesre-
suchstreamsmustnotbelost.Naturally,differentversionsofdata producibleresearchandalgorithmcomparisonwithoutexposing
oftenhavetimeindexingthatdeviatesfromeachother.Therefore, sensitivecustomerinformationorinstitutionaldata.
582

| AICSS2025,September19–21,2025,Beijing,China |     |     |     | MinjuZhong |     |
| ------------------------------------------- | --- | --- | --- | ---------- | --- |
Table3:DatasetCharacteristicsandStatistics
|     | Characteristic     | TrainingSet | ValidationSet | TestSet   |     |
| --- | ------------------ | ----------- | ------------- | --------- | --- |
|     | TotalTransactions  | 2,847,392   | 356,741       | 445,928   |     |
|     | AnomalyRate(%)     | 2.14±0.08   | 2.31±0.12     | 1.97±0.09 |     |
|     | TemporalSpan(days) | 365         | 45            | 60        |     |
|     | CustomerAccounts   | 48,750      | 12,188        | 15,235    |     |
|     | TransactionTypes   | 16          | 14            | 15        |     |
|     | AverageDailyVolume | 7,801±342   | 7,927±289     | 7,432±401 |     |
|     | PeakDailyVolume    | 12,847      | 11,203        | 10,891    |     |
|     | MinimumDailyVolume | 4,231       | 4,892         | 4,567     |     |
ValidationStrategy:Toaddresstheselimitations,ourexperimen-
taldesignincorporatesstatisticalvalidationensuringthesynthetic
datasetpreserveskeydistributionalproperties,temporalcorrela-
tions,andanomalycharacteristicsrepresentativeofrealfinancial
systems.Futureworkshouldincludevalidationonanonymizedreal
transactiondatawhereregulatoryframeworkspermit,toconfirm
theframework’seffectivenessinoperationalenvironmentswith
fullcomplexityofreal-worldfinancialdatastreams.
4.2 PerformanceEvaluationMetrics
Detectionprecision,recall,andF1-scoreofanomaliesanalysisuses
temporalcross-validationtechniquestolookattime-dependent
patternsinfinancialdata,soevaluationcoefficientsactuallyreflect
actualperformancecharacteristics. Theevaluationframeworkin-
troducesslidingwindowvalidationapproachesthatrespecttempo-
ralorderingsbutstillgivereliableperformanceevaluationsacross
differentperiodsandtypesofdata[15].Thisplatformwascreated
Figure2:MultidimensionalPerformanceEvaluationFrame-
withtheintentionofkeepingfastdetectionratesfromharming work
systemperformance.Introducingatradeoffbetweendetectionsen-
sitivityandoperatingefficiencyisitsdefiningcharacteristic—andit
requiresevaluationframeworkswhichwillnotfailtotakeintocon- 4.2.1 MetricDefinitions. Weemploystandardbinaryclassification
siderationcosts(ofanykind).Theoptimisationprocedureachieves metricstoevaluateanomalydetectionperformance:
theobjectiveofminimisingfalsepositiverateswhilenotmakingde- Precisionmeasurestheproportionofcorrectlyidentifiedanom-
aliesamongallflaggedtransactions:
tectionlevelsunacceptablebysimultaneouslyusingmulti-objective
| optimisationtechniques. |     |     | 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=𝑇𝑃/(𝑇𝑃+𝐹𝑃) |     | (9) |
| ----------------------- | --- | --- | -------------------- | --- | --- |
End-to-endprocessingneedsinvolvecalculationsofperformance
Recall(orsensitivity)measurestheproportionofactualanom-
measuressuchasefficiencyanalysis,throughputmeasurements,
latency,andresourceutilizationevaluationindexes,typicallyin- aliessuccessfullydetected:
𝑅𝑒𝑐𝑎𝑙𝑙 =𝑇𝑃/(𝑇𝑃+𝐹𝑁)
volvingtransferringdatafromdifferentsystemplatformsandload (10)
formats.Performancemeasurementsoccurundertestconditions
F1-Scoreprovidestheharmonicmeanofprecisionandrecall,
laiddownbystandardbenchmarks,whichcanbefoundatfinancial
balancingbothmetrics:
institutions,tomaketheresultsofperformancemeasurementsbul-
letinstrustworthy.Ourmultidimensionalperformanceevaluation 𝐹1−𝑆𝑐𝑜𝑟𝑒 =2×(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛×𝑅𝑒𝑐𝑎𝑙𝑙)/(𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙) (11)
frameworkisillustratedinFigure2,whichencompassesdetection FalsePositiveRate(FPR)quantifiestheproportionofnormal
accuracy,computationalefficiency,andsystemrobustnessmetrics. transactionsincorrectlyflaggedasanomalies:
Inthisframework,statisticalsignificancetestinghasbeenin-
|     |     |     | 𝐹𝑃𝑅=𝐹𝑃/(𝐹𝑃+𝑇𝑁) |     | (12) |
| --- | --- | --- | -------------- | --- | ---- |
corporateddirectlysothatthedifferencesinperformancebetween
algorithmsare,infact,realimprovementsandnotjustchancevari- where TP (True Positives) represents correctly detected anom-
ation. Byusingthetechniqueofbootstrapresamplingcombined alies,FP(FalsePositives)representsnormaltransactionsincorrectly
withtechniquesforstatisticalconfidenceintervalconstruction,it flagged,FN(FalseNegatives)representsmissedanomalies,andTN
ispossibletoputrobustcomparisonsofalgorithmperformance (TrueNegatives)representscorrectlyidentifiednormaltransac-
directlybeforereaders. tions.
583

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
Table4:ComparativeAnalysisResultsSummary
Method Precision Recall F1-Score FPR Processing Significance
Time(ms/1000 (p-value)
trans)
FixedThreshold 0.724±0.031 0.831±0.024 0.774±0.022 0.142±0.008 12.3±1.4 -
Statistical 0.789±0.028 0.856±0.021 0.821±0.019 0.098±0.006 18.7±2.1 p<0.01*
ML-based 0.812±0.025 0.873±0.018 0.841±0.017 0.089±0.005 24.1±2.8 p<0.001
Adaptive
Proposed 0.847±0.023 0.891±0.016 0.868±0.015 0.076±0.004 21.5±2.3 p<0.001
Framework
Figure3:AlgorithmPerformanceComparisonAcrossMultipleDimensions
ProcessingTimemeasurescomputationalefficiencyinmillisec- Sensitivityanalysisondifferentfinancialdatacharacteristicsex-
ondsper1000transactions,criticalforreal-timedeployment. amineslinkagesbetweenthealgorithm’sperformanceandchang-
ingmarketconditionsinthedata.Studyingfactorialdesignmethod-
ologieshasbeenusedforthiskindofinspectionwork. Itallows
ustocompareandcontrastperformancesensitivityundermultiple
dataconditionsatthesametime.Table4presentsacomprehensive
summaryofthecomparativeanalysisresultsacrossallevaluated
4.3 ComparativeAnalysisSetup
methods.
Baselinecomparisonswithfixedthresholdmethodsincludeoverall Resultsrepresentmean±standarddeviationover10independent
assessmentsthatcovermostanomalydetectionsystemscommonly runs. Statistical significance was determined using McNemar’s
prescribedinfinance,causingstatisticalcharts,percentiles,and testformodelcomparisonanda5x2-foldcross-validationpaired
rule-baseddetectionsystemstobemadetomakeacomprehensive t-testwithBonferronicorrectionformultiplecomparisons. Non-
evaluation. Thecomparisonframeworkmakessuretoequalize parametricbootstrapresampling(n=1000)wasappliedtoestimate
evaluationbyusingidenticaldatasetsandinspectioncriteriafor confidenceintervalsforperformancemetrics. *p<0.01,p<0.001.
allmethods. FPR = False Positive Rate. Processing time measured per 1000
Performance achieved by benchmarking against established transactionsonIntelXeonE5-2680v4@2.40GHzwith32GBRAM.
adaptivethresholdalgorithmsincorporatesthelatestresearchfind- Figure3providesavisualcomparisonofalgorithmperformance
ings in dynamic threshold adjustment. Benchmark procedures acrossmultipleevaluationdimensions,demonstratingtheproposed
applystandardisednormsofevaluation,whichconsidertherequire- framework’ssuperiority in precision, recall, F1-score, and false
mentsofvariousalgorithmsandtheiroptimisationprocedureswith positiveratereductioncomparedtobaselinemethods.
rigourtoensureacomprehensiveandfairperformancecomparison.
584

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
Theframeworkforcomparativeanalysisemploysstatisticaltest- 5.2.1 Real-timeTransactionProcessing. Data-qualitymonitoringin
ingtechniquestodeterminewhethertheperformanceofvarious large-scalepayment-processingenvironmentspresentsparticular
pairsofmethodsisverydifferentunderpairedstatisticaltestsand problems,thankstotheglaringamountandfleetnessofincoming
effectsizemeasurements,whichcanberegardedasthereal-world streamsthataffecttransactionintegrity.Theframework’ssliding
significanceofimprovementsmadeinperformance. windowapproachmakescontinuousobservationoftransaction
patternspossiblewithoutneedingbatchprocessingdelay,which
coulddisturbsystemperformance. Thatensemblemethodbrings
5 RESULTSANALYSISANDDISCUSSION IsolationForest,DBSCANclustering,andLocalOutlierFactoralgo-
5.1 ExperimentalResultsandPerformance rithmstogethertomakeacomprehensiveanomalyscoringsystem,
capableofadjustingitselfastransactioncharacteristicschangein
Analysis
realtime.
Accordingtoobjectivemeasures,incontrasttotraditional,fixed Theframework’scomputationalefficiencycanbecrucialinthese
thresholdmethods,proposedadaptivethresholdingframeworks environments.Timemeasurementsindicatethattheadaptiveap-
hadsuperiorperformance.Inthisregard: proachcanstillmeetverytightlatencycriteriaunderhighload,
·Falsepositiveratereductionsbyfully46.5%andimprovements makingitsuitablefordeploymentinsystemswithstringentre-
inF1-scoreaccuracyincreasedto12.1%wererecorded;thisdemon- sponsetimerequirements. Themechanismfordynamicallyadjust-
stratesimproveddiscriminativecapabilityindistinguishinggen- ingparametersensuresstabledetectionprecisionnotwithstanding
uineanomaliesfromnormaltransactionvariations. howoperatingconditionsfluctuate.
Comparedtotraditionalmethods,theadaptiveframeworkshows
noticeableadvancesinbothcomputationalefficiencyandscalability.
Inpractice,ithasbetterdecodingspeedthanitsoldfixed-threshold
5.2.2 Cross-institutional Data Quality Assessment. Data quality
counterparts;wehavetotakenotethatmemoryusageanalysisindi-
monitoringhasbecomeincreasinglyimportantforfinancialinsti-
catesresourcerequirementsare23percentlowerthanconventional
tutions,andthisresponsibilityiscompoundedbythefactthatthe
thresholdmethods. Itmakesadaptablethresholdssuitableeven
informationmightstemacrossavarietyofsourcesandjurisdic-
whendeployedwithinresource-pooroperationalenvironments.
tionalboundaries. Theadaptivethresholdframework’sunsuper-
Flatgrowthcharacteristics: Wehavebeenabletoshowthatat
visedlearningapproachallowsittobeusedinfederatedenviron-
differentdatavolumes,thetimetoprocessinformationisextended
ments,wherelabeledtrainingdatacanbescarceorabsent. The
inadirectionproportionaltobusinesssize,butwithoutsacrificing
framework’sabilitytolearnnormaltransactionpatternsfromunla-
accuracyindetection.Theframeworkwasstableacrossdifferent
beleddatastreamsmakesitparticularlysuitableforestablishments
customersegmentsandtransactiontypes,somethingthatiscrucial
implementingnewmonitoringsystemsorsettingtheirsightson
forpracticaluseindiversefinancialenvironmentsrequiringfault-
transactiontypesnotpreviouslycovered.
toleranceasamandatoryminimumcriterion.
Theframework’sparametertuningcapabilitiesenableittobe
adjustedaccordingtodifferentinstitutionalsettings; itcanstill
5.2 CaseStudyApplications carryoutthebasicfunctionofdetection. Institutionscanchange
sensitivityfactorsandwindowsizestosuittheirspecificlevelofrisk
Actually,thisViewpointpaperoffersanadvancedmethodtoimple-
withoutneedingtoretraintheunderlyingmodel.Suchflexibility
mentadaptivethresholds,anditisthisfunctionalityofthesystem
meansthethingcanbecarriedoutinanorganizationpossessing
whichwewillnowpresentinaseriesofthreeexamplesdesigned
differentstructuresandexistingregulations.
toshowhowtheframeworkoperatesatgroundlevel.
RegulatoryComplianceMonitoring
Financialinstitutionsoperatingunderregulatoryframeworks
suchasCCARandDFASTrequirecontinuousmonitoringoftrans- 5.2.3 ImplementationConsiderations. Inpractice,itisnecessary
actiondataqualitytoassureaccuratestresstestingandreporting. tocarefullyconsiderhowtheadaptivethresholdframeworkfits
Traditionalstaticthresholdsystemsoftengenerateexcessivefalse intoaninstitution’songoingoperations.Theframework’smodular
positivesduringperiodsofmarketvolatilityorseasonaltransaction designenablesittobeintegratedwithexistingdataqualitymonitor-
patternchanges,forcingmanualreviewthatconsumessignificant inginfrastructurewhilealsoallowinginstitutionsthathavealready
operationalresources. Theadaptivethresholdframeworksolves madeinvestmentsinthisareatopavethewayforfurtherdevelop-
thisproblembyautomaticallyadjustingdetectionparametersbased ments.Loggingofperformancemonitoringresultsandchangesin
onemergingmarketconditionsandcustomerbehaviorpatterns. thresholdsettingsgivesinsightintothedecision-makingprocesses
Inregulatoryreportingcontexts,theframework’sseasonalde- ofthesystem,whichsupportsdemandsforauditsortheneedto
compositioncapabilitiesproveparticularlyvaluable.Transaction superviseoperations.
volumesandpatternsshowpredictablevariationsduringperiods Theframework’scapacitytoconservehistoricalpatterninforma-
suchasyear-endfinancialactivityorholidayshoppingseasons, tionwhilemovingtonewconditionsmakessurethatitsdetection
whichstaticsystemswronglyflagasanomalies. Theadaptiveway capabilitiesdevelopcorrectlywithchangesinthebusinesssituation.
recognizessuchlegitimatepatternshiftsandoffsettingthresholds, Thisisacrucialcompromisebetweenflexibilityandstability,allow-
whilemaintainingsensitivitytogenuinedataqualityproblems, ingcontinuoushigh-qualitydatamonitoringnomatterwhatthe
reducesfalsealarms. prevailingmarketconditionsorstageofgrowthforyourinstitute.
585

AdaptiveAnomalyDetectionThresholdforFinancialDataQualityMonitoringBasedonTimeSeriesFeatures AICSS2025,September19–21,2025,Beijing,China
5.3 LimitationsandFutureResearchDirections historicalpatterns. Futureresearchdirectionsshouldfocusonin-
Theproblemwiththeproposedadaptivethresholdalgorithmis corporatingexternaleconomicindicatorsandexploringfederated
thatifthemarketisabnormalandentirelyunexpectedbehaviour learningapproachestoenableprivacy-preservingcollaboration
shouldoccurinthemarkets,thenthisapproachdoesnothandleit acrossfinancialinstitutions. Additionally,investigatingtheframe-
well.Additionally,theevaluationonsyntheticdatasets,whileen- work’sadaptabilitytoemergingfinancialtechnologiesandtransac-
ablingcontrolledexperimentation,introduceslimitationsregarding tiontypeswillbecrucialformaintaininglong-termeffectiveness
generalizationtoreal-worldfinancialsystems.Thesyntheticdata intherapidlyevolvingfinanciallandscape.
generationprocess,thoughstatisticallycalibratedtomirrorreal
transactioncharacteristics,cannotfullycapturethecomplexityof Acknowledgments
actualfinancialecosystems,includingrarecombinationanomalies,
IamgratefulforthehelpfulstudythatIqbaldevelopedlastyear
emergent fraud patterns, and the full spectrum of temporal de-
withAmin,R.,Alsubaei,F.S.,andAlzahrani.Theirresearchfocuses
pendenciespresentinoperationaldata. Validationonanonymized
onanabnormalintelligentcentreusingcloudmonitoringdataof
real-worlddatasetsfromfinancialinstitutionswouldprovidecrucial
multivariatetimeseries, which ismadeeasier thaneverbefore
evidenceoftheframework’soperationaleffectivenessandiden-
byusingdeepensemblemethodmodels. ”Anomalydetectionin
tifyadditionaledgecasesrequiringalgorithmicrefinement. The
multivariatetimeseriesdatausingdeepensemblemodels”Paper
frameworkmayfacechallengeswhenencounteringunprecedented
reportedinPlosOne(2024)[1]. Asaresult, myunderstanding
marketconditionsorregulatorychangesthatfundamentallyalter
of the deep ensemble method in time series anomaly detection
transactionpatternsbeyondhistoricalnorms.Futureresearchdirec-
hasbeendeepened,andthishaschangedhowIlookatadvanced
tionsincludeincorporatingexternaldatasourcessuchassocialme-
techniquesformultivariatefinancialdataanalysis. Includedare
diasentimentindicatorsandmacroeconomicstatisticstoenhance
alsonotes,whichIacknowledgeAsmar,M.,andAqel,B.Y.,fortheir
featureextractioncapabilities. Theseadditionaldatasourcescould
studyoncreditcardanomalydetectionanalysisfromaprocess
improve detection accuracy under changing market conditions.
and techniques perspective. The paper ”Analysis of credit card
Externaldatasourcesrequirepreprocessingthroughadvancedfea-
anomalydetection:processandtechniquesperspective”appeared
tureengineeringandselectiontechniques.Futureimplementations
inArtificialIntelligence(AI)andFinance(2023)[2].Theiranalysis
couldincorporatefederatedlearningapproachestoenableprivacy-
oftheprocedureandmeansofinfectionfordetectionprocessing,
preservingcollaborationacrossinstitutions. Thisapproachallows
however, hasenhancedmyunderstandingoffinancialanomaly
formultiplefinancialinstitutionstocollaborateonanomalyde-
detectionsystemsandresearchintoadaptivemethodsoffinancial
tectionwhilemaintainingregulatorycomplianceanddataprivacy
dataqualitymonitoringwithabnormaldetectionframeworks.
requirements. Theuseoffederativeapproachescanimprovedetec-
tionaccuracy,butitshouldalsobestrictlyinlinewithrequirements
fordataconfidentiality. References
[1] Iqbal,A.,Amin,R.,Alsubaei,F.S.,&Alzahrani,A.(2024).Anomalydetection
inmultivariatetimeseriesdatausingdeepensemblemodels.Plosone,19(6),
e0303890.
6 CONCLUSION [2] Asmar,M.,&Aqel,B.Y.(2023).Analysisofcreditcardanomalydetection:process
andtechniquesperspective.InArtificialIntelligence(AI)andFinance(pp.899-
Thisresearchpresentsacomprehensiveadaptivethresholdframe- 911).Cham:SpringerNatureSwitzerland.
workforfinancialdataqualitymonitoringthatsuccessfullyad- [3] Liu,H.(2025).Multi-variabletime-seriesanomalydetectionforintelligentopera-
tionandmaintenance.In2025,the5thInternationalSymposiumonComputer
dressesthelimitationsoftraditionalstaticthresholdapproaches. TechnologyandInformationScience(ISCTIS)(pp.1030-1034,2025,May).IEEE.
Theproposedmethodologyintegratesslidingwindowstatistical [4] Jain,J.S.,Sapra,A.,Gupta,A.,Dagar,L.,&Niranjan,V.(2025).Performance
AnalysisofMachineLearningModelsandDeepLearningModelsforCreditCard
analysiswithensembleunsupervisedlearningtechniques,achiev-
AnomalyDetection.In2025,the3rdInternationalConferenceonCommunication,
ingsignificantimprovementsinanomalydetectionperformance. Security,andArtificialIntelligence(ICCSAI)(Vol.3,pp.1533-1538,2025,April).
Experimentalresultsdemonstratethatourframeworkoutperforms IEEE.
[5] Chen,Z.,Wang,S.,Yan,D.,&Li,Y.(2023).Researchandimplementationof
conventionalmethodswithaprecisionof0.847,recallof0.891,and
abankcreditcardanomalydetectionsystembasedonreinforcementlearning
F1-scoreof0.868,whileachievingasubstantial46.5%reduction andLSTM.In2023,the3rdInternationalConferenceonMobileNetworksand
infalsepositiverates. Theframework’sabilitytoautomatically WirelessCommunications(ICMNWC)(pp.1-8,2023,December).IEEE.
[6] Ida,S.J.,&Balasubadra,K.(2024).Enhancingcreditcardanomalydetection
adjustdetectionparametersbasedonevolvingtransactionpatterns throughLSTM-basedsequentialanalysiswithearlystopping.In20242ndIn-
representsasignificantadvancementinfinancialdataqualitymoni- ternationalConferenceonNetworkingandCommunications(ICNWC)(pp.1-6,
2024,April).IEEE.
toring,particularlyforinstitutionsoperatingunderstrictregulatory
[7] Chen,Y.,Zhao,C.,Xu,Y.,&Nie,C.(2025).Year-over-yeardevelopmentsin
requirementssuchasCCARandDFASTcompliance. financialanomalydetectionviadeeplearning:Asystematicliteraturereview.
Thepracticalimplicationsofthisworkextendbeyondimproved arXivpreprintarXiv:2502.00201.
[8] Sathe,R.,&Shinde,S.(2024,).ADeepLearningFrameworkforEffectiveAnomaly
detectionaccuracytoencompassoperationalefficiencyandregu-
DetectioninTimeSeriesData.In20244thAsianConferenceonInnovationin
latorycompliancebenefits.Theframework’sreal-timeprocessing Technology(ASIANCON)(pp.1-7,2024,August).IEEE.
capabilitiesandmodulardesignenableseamlessintegrationinto [9] Cui,Y.,Han,X.,Chen,J.,Zhang,X.,Yang,J.,&Zhang,X.(2025).FraudGNN-RL:a
graphneuralnetworkwithreinforcementlearningforadaptivefinancialanomaly
existing financial monitoring infrastructure while reducing the detection.IEEEOpenJournaloftheComputerSociety.
operational burden associated with manual threshold recalibra- [10] Suganthi,V.,&Jebathangam,J.(2024).ANovelApproachforCreditCardanomaly
detectionusingGatedRecurrentUnit(GRU)Networks.In20248thInternational
tion. However,theapproachfaceslimitationswhenencountering
ConferenceonI-SMAC(IoTinSocial,Mobile,AnalyticsandCloud)(I-SMAC)
unprecedentedmarketconditionsthatdeviatesignificantlyfrom (pp.1716-1721,2024,October).IEEE.
586

AICSS2025,September19–21,2025,Beijing,China MinjuZhong
[11] Tang,Y.,&Liu,Z.(2024).ACreditCardanomalydetectionAlgorithmBasedon IEEE/CAAJournalofAutomaticaSinica.
SDTandFederatedLearning.IEEEAccess,12,182547-182560. [14] Meng,C.C.,Lim,K.M.,Lee,C.P.,&Lim,J.Y.(2023,August).CreditCardanomaly
[12] Chidambaranathan,P.,&MuthuPriya,V.(2024).RiskPredictioninFinancial detectionusingTabNet.In202311thInternationalConferenceonInformation
TransactionsUsingIoTBigDataAnalytics.In20245thInternationalConference andCommunicationTechnology(ICoICT)(pp.394-399).IEEE.
onElectronicsandSustainableCommunicationSystems(ICESC)(pp.328-332, [15] Alamri,M.A.,&Ykhlef,M.A.(2023).AMachineLearning-BasedFramework
2024,August).IEEE. forDetectingCreditCardAnomaliesandFraud.In202327thInternational
[13] Xie,Y.,Zhou,M.,Liu,G.,Wei,L.,Zhu,H.,&DeMeo,P.(2025).Atransactional- ConferenceonInformationTechnology(IT)(pp.1-7,2023,February).IEEE.
behavior-basedhierarchicalgatednetworkforcreditcardanomalydetection.
587