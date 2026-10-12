---
conversion_metadata:
  converted_at: "2026-10-12T07:36:11Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Salvador, 2024.pdf"
  source_pdf_sha256: "ac4c9ac0274274dab6d0ed1c67265512a3882d4471ed45f73f4d9b96645d4fd2"
  page_count: 10
  markdown_char_count: 35824
---

Highlights
UseofBoostingAlgorithmsinHousehold-LevelPovertyMeasurement:AMachineLearn-
ingApproachtoPredictandClassifyHouseholdWealthQuintilesinthePhilippines
ErikaLynetV.Salvador
• CatBoostachievedthehighestaccuracy(90.93%)andoverallperformancemetrics,followedbyXGBoost,
GBM,andLightGBM.AdaBoosthadthelowestperformance.
• AUC-ROC scores indicated that CatBoost, GBM, LightGBM, and XGBoost excelled in distinguishing
betweenpovertyclasses,whileAdaBoostlaggedbehind.
• Computationalefficiencyvaried,withAdaBoosthavingtheshortesttrainingtimebutlongesttestingtime.
CatBoost had the longest training time but was highly efficient during testing. GBM, LightGBM, and
XGBoostbalancedwellbetweentrainingandtestingtimes.
4202
yaM
82
]YC.sc[
1v16031.7042:viXra

Use of Boosting Algorithms in Household-Level Poverty
Measurement: A Machine Learning Approach to Predict and
Classify Household Wealth Quintiles in the Philippines
Ms.ErikaLynetV.Salvadora,b,∗,1 (Researcher)
aDepartmentofMathematicsandStatistics,AmherstCollege,CollegeSt.,Amherst,01002,Massachusetts,UnitedStatesofAmerica
bScience,Technology,Engineering,andMathematicsStrand,SeniorHighSchoolDepartment,DeLaSalleUniversityIntegratedSchool
Manila,TaftAvenue,Malate,Manila,2401,NationalCapitalRegion,Philippines
ARTICLE INFO ABSTRACT
Keywords: This study assessed the effectiveness of machine learning models in predicting poverty
machinelearning levels in the Philippines using five boosting algorithms: Adaptive Boosting (AdaBoost),
classification Cat Boosting (CatBoost), Gradient Boosting Machine (GBM), Light Gradient Boosting
householdwealthindex Machine(LightGBM),andExtremeGradientBoosting(XGBoost). CatBoostemergedas
Philippines thesuperiormodelandachievedthehighestscoresacrossaccuracy,precision,recall,and
F1-scoreat91%,whileXGBoostandGBMfollowedcloselywith89%and88%respectively.
Additionally,theresearchexaminedthecomputationalefficiencyofthesemodelstoanalyze
thebalancebetweentrainingtime,testingspeed,andmodelsize—factorscrucialforreal-
worldapplications.Despiteitslongertrainingduration,CatBoostdemonstratedhightesting
efficiency.Theseresultsindicatethatmachinelearningcanaidinpovertypredictionandinthe
developmentoftargetedpolicyinterventions.Futurestudiesshouldfocusonincorporatinga
widervarietyofdatatoenhancethepredictiveaccuracyandpolicyutilityofthesemodels.
1. Introduction
Asof2024,over700millionpeoplegloballyliveinextremepovertyandsurviveonlessthan$2.15(Php125)
perday[1].Toaddressthis,governmentsworldwideareintensifyingeffortstoachieveSustainableDevelopment
Goal 1 (SDG) which targets the eradication of poverty in all its forms by 2030. However, recent research
suggests that the lingering effects of the COVID-19 pandemic may endure in various countries until 2030 [2].
This presents a significant challenge to the goal of reducing global poverty—a target already at risk prior to
the crisis. Hence, the need for significant political intervention is now more pressing than ever [1]. In order for
policymakerstoformulatetargetedinterventionsandallocateresourcesefficiently,accuratelydeterminingpoverty
levelsisparamount[3].Dataempowersgovernmentsandorganizationstodevisestrategiesthatgenuinelyuplift
individualsandcommunitiesfrompoverty.Withoutaccuratedata,policyinitiativesriskfallingshortinaddressing
theunderlyingcausesofpovertyorreachingthosemostinneed[4].
Poverty, however, is defined diversely. Broadly, poverty measurement approaches fall into two categories:
monetaryandnon-monetary[5].Themonetaryapproach,asthenamesuggests,definespovertybasedonincome
orexpenditure.Forinstance,theestablishedpovertymethodologyinthePhilippinesemployspre-taxincomeas
anindicatorofhouseholdwell-being[6,7].Ontheotherhand,severalresearcherscontendthatpovertyextends
beyondfinanciallackandincludesaspectssuchasopportunity,education,andhealthcaredeficits[8].Simplyput,
theyviewpovertyasmultidimensional,notsolelydefinedbymoney.
Unfortunately, the drawback of conventional econometric methodologies in forecasting poverty is their
tendencytooversimplifythemultidimensionalnatureofpoverty.Manyprevailingmeasurementsforpovertyare
structuredwithoutconsiderationfornon-monetaryindicatorsofwelfare,suchasanindividual’sandhousehold’s
health,nutritional,oreducationalstatus[9].Econometricmodelsoftenrelyonpre-selectedfeatures(i.e.,income)
basedoneconomictheoryorpriorknowledge,whichmayoftenoverlookimportantrelationshipsorinteractions
inthedata.Therefore,itisofvitalimportancetoconductassessmentsconsideringdiversedimensionsofpoverty
toformulateeffectivereductionpolicies.
Effortstorefinepovertymeasurementincreasinglyemploydiversedataandmachinelearningmethodologies.
Machine learning models present distinct advantages over econometric counterparts because they can mitigate
multicollinearity, achieve heightened accuracy, process data expeditiously, accommodate extensive datasets,
and minimize human involvement [10]. Furthermore, machine learning algorithms excel in feature selection
∗Correspondingauthor
erisalvador28@amherst.edu(E.L.V.Salvador)
linkedin.com/in/salvadorerika/(E.L.V.Salvador)
ORCID(s):0009-0003-2045-5459(E.L.V.Salvador)
E.L.V. Salvador: PreprintsubmittedtoElsevier Page1of9

Predicting poverty via boosting algorithms
by automatically identifying relevant variables and capturing data relationships, even amidst nonlinearity or
obscured patterns [11]. Each variable’s impact on poverty is scrutinized during selection and favors those with
significant effects to construct models. These capabilities allow machine learning models to effectively handle
high-dimensionaldataandgeneratemoreaccuratepredictivemodels.
Only a limited number of studies have employed machine learning methods to address poverty in the
Philippines, utilized nationwide data from the Demographic and Health Survey (DHS) Program and compared
variousthesemachinelearningmodels.Forexample,onestudy[12]utilizedgeospatialdata,includingnighttime
lightsanddaytimesatelliteimagery,tomodelsocioeconomicwell-being,whichachievedanR2 (goodnessoffit)
of 0.63. Similarly, another study [13] used social media data, low-resolution satellite images, and volunteered
geographic information to map poverty, which obtained an R2 of 0.66 compared to 0.63 with satellite imagery
alone.Thesestudiesprimarilyreliedongeospatialdata.Conversely,anotherresearch[14]analyzedadatasetfrom
theCommunity-BasedMonitoringSystem(CBMS)DatabaseofLagangilang,Abra,utilizingvariousmodelsbut
with only 13 features, where the Naive Bayes model yielded the best performance. Another related study [15]
appliedK-meansclusteringand17featureswithinasmall,undisclosedcommunityinthePhilippines.
Significantly, a gap exists in the utilization and comparison of various machine learning methodologies
for assessing poverty in the Philippines. None of the previously mentioned studies explored extensive datasets
comprisinghundredsofhouseholdcharacteristicfeaturessuitableformodelestimation.While[12]utilizeddata
fromtheDHS,theyfocusedononlyfourmainfeatures.Therefore,thisstudyaimedtobroadenpovertyanalysis
using machine learning techniques across an extensive dataset, working under less restrictive assumptions to
effectively identify low-income households. Furthermore, this research aimed to tackle the underutilization of
boostingalgorithmsinpovertyprediction[16].Infact,XGBoostisthesoleboostingalgorithmwitha14%usage
rateinarecentscopingreviewonmachinelearningandpovertyprediction[17].However,recentresearchindicates
thatthefamilyofboostingalgorithmshasexpandedwithseveralcompellingproposalsandboastsimprovementsin
bothspeedandaccuracy[18].Asaresult,thisstudysoughttoutilizeasubsetofboostingalgorithmsinpredicting
povertyinthePhilippines.
2. DataandMethods
2.1. DataCleaning
The data for this study was obtained from the 2022 DHS in the Philippines. The original dataset consisted
of2,099featurescollectedfrom30,372households.Athresholdof3,050wasassigned(FigureX)becausemost
featureshadfewerthan3,050missingvalues.Columnsexceedingthemissingvaluethresholdwereremoved,and
rowswithanyremainingnullvaluesweredeleted.Furthermore,someinterview-relatedlogisticfeatures,suchas
the date of the interview, were manually removed. After this step, the dataset was reduced to 396 features from
2,099features,and20,679householdsfrom30,372households.
Figure 1: Distribution of Missing Values across Features. Blue Line = 3,050
E.L.V. Salvador: PreprintsubmittedtoElsevier Page 2 of 9

|     | Predicting | poverty via | boosting algorithms |     |     |
| --- | ---------- | ----------- | ------------------- | --- | --- |
2.2. DataPartitioning
After data cleaning, the dataset underwent random partitioning, with 80% allocated for training and the
remaining20%reservedforassessingmodelperformance.Additionally,tooptimizethemodel’shyperparameters,
a validation set comprising 10% of the training set was required. This division was executed using a stratified
samplingtechnique.
2.3. FeatureScaling
Afterwards,scalingwasimplementedtoensureuniformscalingacrossallfeatures.Binaryfeatureswereleft
unscaled,whilenumericalandordinalfeatureswerescaled.First,thescalerwastrainedonthetrainingdatausing
z-scorenormalization.Thetrainingdatawasthentransformedaccordingtothesenormalizationparameters.Finally,
thesameparameterswereappliedtothetestingdata.Thisensuredconsistencyandpreventeddataleakage.
2.4. FeatureSelection
Toaddresspotentialefficiencyissuesassociatedwithanexcessivenumberoffeatures[11],thestudyemployed
the SelectFromModel() method to identify significant features for each model. SelectFromModel is a feature
selection technique in scikit-learn that acts as a meta-transformer compatible with any estimator that evaluates
featureimportance,suchasdecisiontreesorL1-normregularizedlinearmodels.Afterevaluatingallmodels,the
studytalliedthefrequencyofeachfeature’sselectionandidentifiedthosemostfrequentlychosenasthefinalsetof
selectedfeatures.Thisprocessresultedintheselectionof66featuresdeemedmostrelevantforpredictingpoverty.
Pearson’sCorrelationCoefficientwasappliedtothesubsetofselectedfeaturestocheckformulticollinearity.For
pairs of features with a correlation coefficient of 0.8 or higher, the feature with the lower selection frequency
wasremoved.Fromtheoriginal36featuresinitiallyselectedviaSelectFromModel(),thefinalcountremainedthe
same, as there is minimal to no multicollinearity among them. These features, ranked by their frequency in the
SelectFromModel()results,arelistedinTable1.
Table1:DescriptionofFeatures
| No. Feature |     | Description |     |     |     |
| ----------- | --- | ----------- | --- | --- | --- |
1 Sourceofdrinkingwater Can take on 20 different values from ‘piped water’ (10), ‘tube
wellwater’(20),‘dugwell’(30),‘surfacefromspring’(40),and
more.
2 Typeoftoiletfacility Cantakeon17valuesfrom‘flushtoilet’(10),‘pittoiletlatrine’
(20),‘nofacility’(30),andmore.
| 3 Hastelevision         |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
| ----------------------- | --- | --------------------------------- | --- | --- | --- |
| 4 Hasrefrigerator       |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
| 5 Hasbicycle            |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
| 6 Hasmotorcycle/scooter |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
| 7 Hascar/truck          |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
8 Mainfloormaterial Cantakeon15differentvaluesfrom‘natural’(10),‘rudimentary’
(20),‘finished’(30),andmore.
9 Mainwallmaterial Cantakeon22differentvaluesfrom‘natural’(10),‘rudimentary’
(20),‘finished’(30),andmore.
10 Mainroofmaterial Cantakeon18differentvaluesfrom‘natural’(10),‘rudimentary’
(20),‘finished’(30),andmore.
| 11 Hastelephone(landline) |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |
| ------------------------- | --- | --------------------------------- | --- | --- | --- |
12 Typeofcookstove Can take on 11 different values from ‘electric stove’ (1), ‘solar
|     |     | cooker’ | (2), ‘liquefied petroleum | gas (LPG)/cooking | gas stove’ |
| --- | --- | ------- | ------------------------- | ----------------- | ---------- |
(3),andmore.
13 Sharetoiletwithotherhouseholds Cantakeonvalues‘yes’(1)or‘no’(0).
14 Typeofcookingfuel Can take on 13 values from ‘alcohol/ethanol’ (1), ‘gaso-
line/diesel’(2),kerosene/paraffin(3),andmore.
| E.L.V. Salvador: | PreprintsubmittedtoElsevier |     |     |     | Page 3 of 9 |
| ---------------- | --------------------------- | --- | --- | --- | ----------- |

|             |     | Predicting | poverty via | boosting algorithms |     |     |     |
| ----------- | --- | ---------- | ----------- | ------------------- | --- | --- | --- |
| No. Feature |     |            | Description |                     |     |     |     |
15 Locationoftoiletfacility Can take on 11 different values from ‘electric stove’ (1), ‘solar
|     |     |     | cooker’ | (2), ‘liquefied petroleum | gas (LPG)/cooking | gas | stove’ |
| --- | --- | --- | ------- | ------------------------- | ----------------- | --- | ------ |
(3),andmore.
| 16 Haswatch       |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| ----------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 17 Hasacomputer   |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| 18 Hasbankaccount |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
19 Typeoflightathome Can take on 16 different values from ‘electricity’ (1), ‘solar
lantern’(2),‘rechargeableflashlight’(3),andmore.
| 20 Haswashingmachine |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 21 Hasairconditioner |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
22 Hasgasrange/stovewithoven Cantakeonvalues‘yes’(1)or‘no’(0).
23 Hasmicrowave/toasteroven Cantakeonvalues‘yes’(1)or‘no’(0).
24 Hasaudiocomponent/karaoke Cantakeonvalues‘yes’(1)or‘no’(0).
| 25 Hascableservices |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| ------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
26 Tenurestatusofthehousingunit Cantakeon7valuesfrom‘ownorowner-likepossessionofthe
|     |     |     | house and | lot’ (1), ‘own | the house, rent | the lot’ (2), ‘own | the |
| --- | --- | --- | --------- | -------------- | --------------- | ------------------ | --- |
house,rent-freelotwithconsentoftheowner’(3),andmore.
27 Typeofplaceofresidence Cantakeonvalues‘urban’(1)or‘rural’(2).
| 28 Time | to get to water | source (min- | Numericalvalue. |     |     |     |     |
| ------- | --------------- | ------------ | --------------- | --- | --- | --- | --- |
utes)
| 29 Haselectricity               |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| ------------------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 30 Numberofroomsusedforsleeping |     |     | Numericalvalue.                   |     |     |     |     |
| 31 Hasmobiletelephone           |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
32 Mobile phone used for financial Cantakeonvalues‘yes’(1)or‘no’(0).
transactions
| 33 Hasinductionstove |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
| -------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| 34 HasDVDplayer      |     |     | Cantakeonvalues‘yes’(1)or‘no’(0). |     |     |     |     |
35 BeneficiaryofPantawidPamilyang Cantakeonvalues‘yes’(1)or‘no’(0).
PilipinoProgram(4Ps)
36 Observedplaceforhandwashing Can take on 6 different values from ‘observed, fixed facility
(sink/tap)indwelling’(1),‘observed,fixedfacility(sink/tap)in
|     |     |     | yard/plot’ | (2), ‘observed, | mobile object (bucket/jug/kettle)’ |     | (3), |
| --- | --- | --- | ---------- | --------------- | ---------------------------------- | --- | ---- |
andmore.
2.5. MachineLearningModels
This study employed five boosting algorithms: Adaptive Boosting (AdaBoost), Cat Boosting (CatBoost),
Gradient Boosting Machine (GBM), Light Gradient Boosting Machine (LightGBM), and Extreme Gradient
Boosting(XGBoost).Thesemodelswerechosenfortheirrobustnessandtheirabilitytohandlehigh-dimensional
data, which is crucial for a study that aimed to consider the multidimensional nature of poverty. To handle
classimbalance,theSyntheticMinorityOver-samplingTechnique(SMOTE)wasemployedonthetrainingdata.
Hyperparameter tuning was conducted both using manual trial and error and grid search on the validation data.
Table2showcasesthehyperparametersfortheproject.
| E.L.V. Salvador: | PreprintsubmittedtoElsevier |     |     |     |     | Page | 4 of 9 |
| ---------------- | --------------------------- | --- | --- | --- | --- | ---- | ------ |

Predicting poverty via boosting algorithms
Table2:ParametersforDifferentGradientBoostingAlgorithms
|     | Algorithm                              | Parameter     | Value |     |
| --- | -------------------------------------- | ------------- | ----- | --- |
|     | AdaptiveBoosting(AdaBoost)             | learning_rate | 0.5   |     |
|     |                                        | n_estimators  | 200   |     |
|     | CatBoosting(CatBoost)                  | depth         | 4     |     |
|     |                                        | iterations    | 300   |     |
|     |                                        | learning_rate | 0.3   |     |
|     | GradientBoostingMachine(GBM)           | learning_rate | 0.3   |     |
|     |                                        | max_depth     | 3     |     |
|     |                                        | n_estimators  | 300   |     |
|     | LightGradientBoostingMachine(LightGBM) | learning_rate | 0.1   |     |
|     |                                        | n_estimators  | 200   |     |
|     |                                        | num_leaves    | 31    |     |
|     | ExtremeGradientBoosting(XGBoost)       | learning_rate | 0.3   |     |
|     |                                        | max_depth     | 3     |     |
|     |                                        | n_estimators  | 300   |     |
2.6. PerformanceMetrics
Toevaluatetheperformanceofvariousmachinelearningalgorithmsinpredictingandclassifyinghousehold
povertylevels,arangeofperformancemetricswascalculatedandcomparedtothoroughlyevaluatethemodels.
Theperformanceofeachalgorithmwasassessedbasedontheaverageofthemetrics.Thesemetricsinclude:
AccuracyScore.Theaccuracyscoreistheratioofcorrectlypredictedinstancestothetotalinstancesinthe
dataset.Itiscalculatedasthesumoftruepositivesandtruenegativesdividedbythetotalnumberofpredictions:
𝑇𝑃 +𝑇𝑁
| Accuracy= |     |     |     | (1) |
| --------- | --- | --- | --- | --- |
𝑇𝑃 +𝑇𝑁 +𝐹𝑃 +𝐹𝑁
whereTPrepresentstruepositives(i.e.,poorhouseholdscorrectlyidentifiedaspoor),TNrepresentstruenegatives
(i.e.,non-poorhouseholdscorrectlyidentifiedasnon-poor),FPrepresentsfalsepositives(i.e.,non-poorhouseholds
incorrectly identified as poor), and FN represents false negatives (i.e., poor households incorrectly identified as
non-poor).
Precision measures the proportion of correctly predicted positive instances to the total
| Precision | Score. |     |     |     |
| --------- | ------ | --- | --- | --- |
predictedpositiveinstances.Itiscalculatedas:
𝑇𝑃
| Precision= |     |     |     | (2) |
| ---------- | --- | --- | --- | --- |
𝑇𝑃 +𝐹𝑃
Recall.Recall,alsoknownassensitivityorthetruepositiverate,measurestheproportionofcorrectlypredicted
positiveinstancestoallactualpositiveinstances.Itiscalculatedas:
| Recall= | 𝑇𝑃  |     |     | (3) |
| ------- | --- | --- | --- | --- |
𝑇𝑃 +𝐹𝑁
F1Measure.TheF1scoreistheharmonicmeanofprecisionandrecallandprovidesabalancedmeasurethat
takesbothintoaccount.Itiscalculatedas:
Precision×Recall
| F1Score=2× |     |     |     | (4) |
| ---------- | --- | --- | --- | --- |
Precision+Recall
AreaUndertheReceiverOperatingCharacteristicCurve(AUC-ROC).TheROC,orReceiverOperating
Characteristiccurve,plotstherecallagainsttheFPRate(FPR)atvariousthresholdsettings.TheAUC,orArea
Under the Curve, quantifies the overall performance of the model by calculating the area under the ROC curve,
withvaluesrangingfrom0to1.AmodelwithanAUCcloserto1indicatesexcellentperformanceandeffectively
distinguishesbetweenpositiveandnegativeclasses,whileanAUCcloserto0.5suggeststhemodelperformsno
betterthanrandomguessing.
Confusion Matrix. A confusion matrix is a tabular representation of actual versus predicted classifications,
composedoftruepositives,truenegatives,falsepositives,andfalsenegatives.Thismatrixprovidesanoverview
ofmodelperformancethroughhelpingidentifyspecifictypesofclassificationerrors.Whiletheconfusionmatrix
| E.L.V. Salvador: | PreprintsubmittedtoElsevier |     |     | Page 5 of 9 |
| ---------------- | --------------------------- | --- | --- | ----------- |

Predicting poverty via boosting algorithms
provides detailed data, it can be less informative in high-dimensional problems with many classes and requires
carefulinterpretationtounderstandthesignificanceofeachcomponent.Metricslikeaccuracy,precision,andrecall
counterbalancetheconfusionmatrixbysummarizingthesedetailsintomoreinterpretableforms.
The computational efficacy of various metrics in addition to traditional performance metrics above was also
examined.Thecomputationalefficacywasobtainedbymeasuringthetrainingtime,testingtime,andmodelsize.
Tocapturethesemetrics,thetimemodulewasutilizedtorecordthedurationoftrainingandtestingprocesses,and
thememory_profilerlibrarytomonitorthememoryusageandmodelsize.Theseadditionalassessmentsprovided
acomprehensiveunderstandingoftheefficiencyandpracticalityofthemodelsinreal-worldapplications.
2.7. ToolsandLibraries
ThestudyemployedvariousPythonlibrariesandsoftwarefordataanalysisandmachinelearningoperations.
Specifically,thestudyutilizedNumPy(version1.25.0)andpandas(version1.5.1)fordatamanipulationandpre-
processing,seaborn(version0.13.2)andmatplotlib(version3.6.0)fordatavisualization,andscipy(version1.10.0)
forstatisticalanalysis.Formachinelearningmodelingandevaluation,thestudyusedscikit-learn(version1.4.2),
lightgbm (version 4.2.0), xgboost (version 1.8.0), and catboost (version 1.1.0). Additionally, memory_profiler
(version0.61.0)wasutilizedtomonitorandoptimizememoryusageduringtheimplementation.Thesepackages
areaccessibleviathewebsitePythonPackageIndexorthroughpip.
3. Results
TheresearchemployedfivemachinelearningmodelsonDHSdatafromthePhilippines:AdaptiveBoosting
(AdaBoost), Cat Boosting (CatBoost), Gradient Boosting Machine (GBM), Light Gradient Boosting Machine
(LightGBM), and Extreme Gradient Boosting (XGBoost). Wealth classification was approached as a five-class
problem (Richest, Richer, Middle, Poorer, Poorest). Each model was trained on 80% of the cleaned dataset and
evaluatedontheremaining20%.Hyperparameterswereoptimizedusingavalidationset,whichcomprised10%
ofthetrainingdata,withperformanceassessedthroughmetricssuchasaccuracy,precision,recall,andF1-score.
AsshowninTable3,theperformancemetricsforthefivemodelswereasfollows:CatBoostachievedthehighest
accuracyat90.93%,followedbyXGBoostat89.41%,GBMat89.05%,andLightGBMat88.52%.AdaBoosthad
the lowest accuracy at 80.39%. In terms of precision, CatBoost again ranked highest with 90.92%, followed by
XGBoostat89.39%,GBMat89.04%,andLightGBMat88.51%,withAdaBoostrecordingaprecisionof83.55%.
For recall, CatBoost led with 90.93%, while XGBoost had 89.41%, GBM showed 89.05%, and LightGBM was
closebehindwith88.52%.AdaBoosthadthelowestrecallat80.39%.RegardingtheF1score,CatBoostachieved
the highest at 90.92%, followed by XGBoost with 89.40%, GBM at 89.04%, and LightGBM at 88.50%, with
AdaBoostrecordingthelowestF1scoreat80.15%.Therankingsofthemodelswithrespecttoallmetricswere
consistent:CatBoostwasfirst,followedbyXGBoost,GBM,LightGBM,andAdaBoostinthatorder.However,the
metric values for the top four models are remarkably similar, with only AdaBoost exhibiting significantly lower
performancemetrics.
Table3:PerformanceEvaluationMetricsoftheBoostingModels
Model Accuracy Precision Recall F1Score
AdaBoost 0.803917 0.835551 0.803917 0.801523
CatBoost 0.909333 0.909193 0.909333 0.909191
GBM 0.890474 0.890362 0.890474 0.890353
LightGBM 0.885155 0.885137 0.885155 0.884996
XGBoost 0.894101 0.893919 0.894101 0.893981
Meanwhile,Table4providestheAUC-ROCscorestoassesstheperformanceofdifferentmodelsinpredicting
household poverty levels. For the "Poorest" class, CatBoost, GBM, LightGBM, and XGBoost achieved scores
around 0.98 to 0.99, while AdaBoost scored significantly lower at 0.90. This is reflected in the confusion
matrix for AdaBoost (Figure 1), which shows a higher number of misclassifications, particularly with true
"Poorest"instancesbeingpredictedas"Poorer"andsomeas"Richer."Ontheotherhand,forthe"Poorer"class,
CatBoost,GBM,LightGBM,andXGBoostallachievedhighscoresof0.99,whileAdaBoostscoredlowerat0.73.
AdaBoost’s confusion matrix reveals significant misclassifications for the "Poorer" class, with many instances
being misclassified as "Poorest" or "Middle." In both classes, CatBoost, GBM, LightGBM, and XGBoost show
fewermisclassifications(FigureS2.2-2.5),consistentwiththeirhigherAUC-ROCscores.Forthe"Middle"class,
allmodelsdemonstratedperfectperformancewithscoresof1.00,whichisconfirmedbytheirconfusionmatrices
showingalmostnomisclassificationsforthisclass.
E.L.V. Salvador: PreprintsubmittedtoElsevier Page 6 of 9

|     |     |     | Predicting | poverty | via boosting | algorithms |     |     |     |
| --- | --- | --- | ---------- | ------- | ------------ | ---------- | --- | --- | --- |
Inthe"Richer"class,CatBoost,GBM,LightGBM,andXGBoostagainachievedperfectscoresof1.00,while
AdaBoost scored lower at 0.79. AdaBoost’s confusion matrix shows misclassifications for the "Richer" class,
withsomeinstancesbeingmisclassifiedas"Poorer"or"Richest."Conversely,CatBoost,GBM,LightGBM,and
XGBoostshowedstrongperformancewithminimalmisclassifications.Lastly,forthe"Richest"class,CatBoost,
GBM,LightGBM,andXGBoostachievednear-perfectscoresof1.00,andAdaBoostscoredslightlylowerat0.99.
TheconfusionmatrixforAdaBoostshowsasmallnumberofmisclassificationsforthisclass,withsomeinstances
predictedas"Richer."
Table4:AUC-ROCScoresforEachClassAcrosstheBoostingModels
|     |     | Class   | AdaBoost | CatBoost | GBM  | LightGBM | XGBoost |     |     |
| --- | --- | ------- | -------- | -------- | ---- | -------- | ------- | --- | --- |
|     |     | Poorest | 0.90     | 0.99     | 0.98 | 0.98     | 0.98    |     |     |
|     |     | Poorer  | 0.73     | 0.99     | 0.99 | 0.99     | 0.99    |     |     |
|     |     | Middle  | 0.99     | 1.00     | 1.00 | 1.00     | 1.00    |     |     |
|     |     | Richer  | 0.79     | 0.99     | 0.99 | 0.99     | 0.99    |     |     |
|     |     | Richest | 1.00     | 1.00     | 1.00 | 1.00     | 1.00    |     |     |
Additionally,thestudyexaminedthemodels’computationalefficacytoassessthepracticalapplicabilityofthe
models.Recentresearchoftenneglectsthesemetricsandfocusesinsteadonpreviousbenchmarks.Table5provides
thecomparisonofvariousmodelsintermsoftrainingtime,testingtime,andmodelsize.AdaBooststandsoutwith
theshortesttrainingtimeatapproximately4.48seconds,makingitthequickestmodeltotrain.However,ittakes
thelongesttimefortestingat0.23seconds.Incontrast,CatBoost,whilehavingthelongesttrainingtimeof69.29
secondsandthelargestmodelsizeat30.50MB,demonstratesexceptionalefficiencyduringtesting,takingonly0.01
seconds.GBM(GradientBoostingMachine)showsmoderateperformance,withatrainingtimeof16.81seconds,
atestingtimeof0.02seconds,andamodelsizeof15.80MB.LightGBMandXGBoostexhibitagoodbalance,
featuring relatively quick training times of 2.17 and 2.58 seconds, respectively, along with small model sizes of
2.50MBand3.10MB.LightGBMtakesslightlylongerduringtestingat0.07seconds,comparedtoXGBoost’s
0.03seconds.
Table5:ComputationalEfficacyMetricsAcrosstheBoostingModels
|     | Metric                |     |     | AdaBoost | CatBoost | GBM   | LightGBM | XGBoost |     |
| --- | --------------------- | --- | --- | -------- | -------- | ----- | -------- | ------- | --- |
|     | TrainingTime(seconds) |     |     | 4.48     | 69.29    | 16.81 | 2.17     | 2.58    |     |
|     | TestingTime(seconds)  |     |     | 0.23     | 0.01     | 0.02  | 0.07     | 0.03    |     |
|     | ModelSize(MB)         |     |     | 1.20     | 30.50    | 15.80 | 2.50     | 3.10    |     |
4. Discussion
The evaluation of five machine learning models—AdaBoost, CatBoost, GBM, LightGBM, and XGBM—on
DHS data from the Philippines revealed that CatBoost consistently achieved the highest performance metrics,
including accuracy, precision, recall, and F1-score. XGBoost followed closely, with GBM and LightGBM also
demonstrating strong performance. AdaBoost lagged behind with the lowest performance across all metrics.
Moreover, AUC-ROC curves further validated the models’ discriminative capabilities in predicting household
poverty levels. CatBoost, GBM, LightGBM, and XGBoost achieved near-perfect AUC values across most
classes,particularlyindistinguishingthe"Poorest,""Middle,""Richer,"and"Richest"classes.AdaBoostshowed
significantly lower AUC scores, especially for the "Poorest" and "Poorer" classes, which was reflected in its
higher misclassification rates. In terms of computational efficiency, AdaBoost had the shortest training time but
thelongesttestingtime.CatBoostrequiredthelongesttrainingtimeandthelargestmodelsizebutdemonstrated
exceptionaltestingefficiency.GBM,LightGBM,andXGBoostbalancedwellbetweentrainingandtestingtimes,
withLightGBMandXGBoostalsoshowingsmallermodelsizes.
Overall,CatBoostemergedasthetopperformeracrossallmetrics,followedcloselybyXGBoost,GBM,and
LightGBM.AdaBoost,whileefficientintrainingtime,showedlowerperformanceinaccuracy,precision,recall,
andF1-score,aswellashighermisclassificationrates.LightGBMandXGBoostdemonstratedagoodbalanceof
highperformanceandcomputationalefficiency,thusarestrongcandidatesforpracticalapplications.
This study also highlighted the most impactful features in predicting poverty through the feature selection
method,asoutlinedinTable1,indirectlysuggestingpotentialareasforpolicyfocus.Futureresearchcouldmodel
howchangesinthesefeaturesaffectpredictedpovertyclassesexplicitly.Thesefindingshaveglobalimplications
| E.L.V. Salvador: |     | PreprintsubmittedtoElsevier |     |     |     |     |     |     | Page 7 of 9 |
| ---------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | ----------- |

|     |     | Predicting | poverty via boosting algorithms |     |
| --- | --- | ---------- | ------------------------------- | --- |
Figure2:Figures2.1-2.5(FromLefttoRight):ConfusionMatricesforAdaBoost(Fig2.1),CatBoost(Fig2.2),GBM
| (Fig 2.3), LightGBM | (Fig 2.4), | and XGBoost | (Fig 2.5). |     |
| ------------------- | ---------- | ----------- | ---------- | --- |
forpovertyalleviationefforts.Policymakerscangainmoreaccurateinsightsintopovertydynamicsanddevelop
targeted interventions addressing the multifaceted nature of poverty by utilizing machine learning techniques.
However, the limitations in this study, such as the reliance on DHS data and the need for further validation
usingalternativedatasetsormethodologiesmustbeacknowledged.Therefore,incorporatingmorecomplextypes
of information for analysis and poverty prediction is necessary. Combining GPS data with survey data, for
instance, could significantly enhance the accuracy of poverty level classification in the Philippines. Utilizing
more sophisticated information, such as GPS data, night light data, and other advanced metrics, could improve
theprecisionofpovertypredictions.
| E.L.V. Salvador: | PreprintsubmittedtoElsevier |     |     | Page 8 of 9 |
| ---------------- | --------------------------- | --- | --- | ----------- |

Predicting poverty via boosting algorithms
5. Conclusion
This study demonstrated the effectiveness of machine learning boosting algorithms, particularly CatBoost,
in predicting household poverty levels in the Philippines. CatBoost emerged as the top performer by offering
highaccuracyandcomputationalefficiency.However,AdaBoostlaggedbehindinperformancemetrics.Feature
selection highlighted areas for potential policy intervention. Overall, this research contributes development to
povertyalleviationeffortsthroughtheutilizationofadvancedtechnology.
6. Bibliography
References
[1] WorldBank.Povertyoverview:Developmentnews,research,data,April2024.RetrievedMay1,2024,fromhttps://www.worldbank.
org/en/topic/poverty/overview.
[2] KatharinaShulla,BenediktF.Voigt,SabinCibian,GiovanniScandone,ElenaMartinez,FilipNelkovski,andPegahSalehi. Effectsof
covid-19onthesustainabledevelopmentgoals(sdgs).DiscoverSustainability,2:1–19,2021.
[3] MichaelRiegner.Implementingthedatarevolutionforthepost-2015sustainabledevelopmentgoals:Towardaglobaladministrativelaw
ofinformation.WorldBankLegalReview,7:17,2016.
[4] MerileeS.Grindle.Goodenoughgovernance:Povertyreductionandreformindevelopingcountries.Governance,17:525–548,2004.
[5] BenoitDecerf. Apreference-basedtheoryunifyingmonetaryandnon-monetarypovertymeasurement. JournalofPublicEconomics,
222:104898,2023.
[6] JoseRamonG.Albert. [analysis]onpovertylinesandcountingthepoor,May2023. Retrievedfromhttps://www.rappler.com/
voices/thought-leaders/228230-analysis-poverty-lines-counting-poor-filipino.
[7] KarenJoyceBriones,JohnLopez,RonJosephElumbre,andTimothyMiguelAngangco.Income,consumption,andpovertymeasurement
inthephilippines,2021.Retrievedfromhttps://mpra.ub.uni-muenchen.de/106025/.
[8] Sabina Alkire, Jose Manuel Roche, Paola Ballon, James Foster, Maria Emma Santos, and Suman Seth. Multidimensional poverty
measurementandanalysis.OxfordUniversityPress,USA,2015.
[9] DorothyWatson,ChristopherT.Whelan,BertrandMaître,andJamesWilliams.Non-monetaryindicatorsandmultipledimensions:The
esriapproachtopovertymeasurement.TheEconomicandSocialReview,48(4):369–392,2017.
[10] G.ShobanaandK.Umamaheswari.Forecastingbymachinelearningtechniquesandeconometrics:Areview.In20216thInternational
ConferenceonInventiveComputationTechnologies(ICICT),pages1010–1016.IEEE,2021.
[11] JundongLi,KeweiCheng,SuhangWang,FredMorstatter,RobertP.Trevino,JiliangTang,andHuanLiu. Featureselection:Adata
perspective.ACMComputingSurveys(CSUR),50(6):1–45,2017.
[12] IsaiahTingzon,AbigailOrden,KeaneTeruelGo,SelenaSy,VedranSekara,IngmarWeber,andDongKim. Mappingpovertyinthe
philippinesusingmachinelearning,satelliteimagery,andcrowd-sourcedgeospatialinformation. InTheInternationalArchivesofthe
Photogrammetry,RemoteSensingandSpatialInformationSciences,volume42,pages425–431,2019.
[13] CarlaLedesma,OmarLaurenteGaronita,LeonardoJayFlores,IsaiahTingzon,andDeliaDalisay. Interpretablepovertymappingusing
socialmediadata,satelliteimages,andgeospatialinformation,2020.arXivpreprintarXiv:2011.13563.
[14] JohnArloTalingdan. Performancecomparisonofdifferentclassificationalgorithmsforhouseholdpovertyclassification. In20194th
InternationalConferenceonInformationSystemsEngineering(ICISE),pages11–15.IEEE,2019.
[15] MariaPilarRepollo,RenierAurelius,andCarlRobielos. Applyingclusteringalgorithmonpovertyanalysisinacommunityinthe
philippines.InIEOMSocietyInternational,pages1511–1521,2021.
[16] QiangLi,SherryYu,DamienÉchevin,andMingFan.Ispovertypredictablewithmachinelearning?astudyofdhsdatafromkyrgyzstan.
Socio-EconomicPlanningSciences,81:101195,2022.
[17] AigulUsmanova,AzeddineAziz,DostonbekRakhmonov,andWalidOsamy. Utilitiesofartificialintelligenceinpovertyprediction:a
review.Sustainability,14(21):14238,2022.
[18] ChristopheBentéjac,AndrásCsörgő,andGuillermoMartínez-Muñoz.Acomparativeanalysisofgradientboostingalgorithms.Artificial
IntelligenceReview,54:1937–1967,2021.
E.L.V. Salvador: PreprintsubmittedtoElsevier Page 9 of 9