---
conversion_metadata:
  converted_at: "2026-10-11T15:10:26Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Hernadez et al., 2023.pdf"
  source_pdf_sha256: "b5c0a86260ab705821eccb16c09f04557a550765d6d55be202c9c8d18f80d671"
  page_count: 20
  markdown_char_count: 122562
---

Article published online: 2023-01-09
THIEME
Original Article e19
Synthetic Tabular Data Evaluation in the Health Domain
Covering Resemblance, Utility, and Privacy Dimensions
Mikel Hernadez1 Gorka Epelde1,2 Ane Alberdi3 Rodrigo Cilla1 Debbie Rankin4
1DigitalHealthandBiomedicalTechnologiesDepartment,Vicomtech Addressforcorrespondence MikelHernandez,PhDStudent,Digital
Foundation,BasqueResearchandTechnologyAlliance(BRTA), HealthandBiomedicalTechnologiesDepartment,Vicomtech
Donostia-SanSebastian,Spain Foundation,BasqueResearchandTechnologyAlliance(BRTA),
2eHealthGroup,BiodonostiaHealthResearchInstitute,Donostia-San Mikeletegi57,20009Donostia-SanSebastian,Spain
Sebastian,Spain (e-mail:mhernandez@vicomtech.org).
3BiomedicalEngineeringDepartment,MondragonUnibertsitatea,
Arrasate-Mondragón,Spain
4SchoolofComputing,EngineeringandIntelligentSystems,Ulster
University,Derry-Londonderry,UnitedKingdom
MethodsInfMed2023;62:e19–e38.
Abstract Background Synthetic tabular data generation is a potentially valuable technology
withgreatpromisefordataaugmentationandprivacypreservation.However,priorto
adoption, an empirical assessment of generated synthetic tabular data is required
acrossdimensionsrelevanttothetargetapplicationtodetermineitsefficacy.Alackof
standardizedandobjectiveevaluationandbenchmarkingstrategyforsynthetictabular
datainthehealthdomainhas beenfound intheliterature.
Objective Theaimofthispaperistoidentifykeydimensions,perdimensionmetrics,
andmethodsforevaluatingsynthetictabulardatageneratedwithdifferenttechniques
and configurations for health domain application development and to provide a
strategytoorchestratethem.
Methods Based on the literature, the resemblance, utility, and privacy dimensions
havebeenprioritized,andacollectionofmetricsandmethodsfortheirevaluationare
orchestratedintoacompleteevaluationpipeline.Thisway,aguidedandcomparative
assessmentofgenerated synthetic tabular data canbedone,categorizing itsquality
intothreecategories(“Excellent,”“Good,”and“Poor”).Sixhealthcare-relateddatasets
andfoursynthetictabulardatagenerationapproacheshavebeenchosentoconductan
analysisandevaluationtoverify theutilityof the proposed evaluationpipeline.
Keywords Results The synthetic tabular data generated with the four selected approaches has
► synthetictabulardata maintainedresemblance,utility,andprivacyformostdatasetsandsynthetic tabulardata
generation generationapproachcombination.Inseveraldatasets,someapproacheshaveoutperformed
► synthetictabulardata others,whileinotherdatasets,morethanoneapproachhasyieldedthesameperformance.
evaluation Conclusion Theresultshaveshownthattheproposedpipelinecaneffectivelybeusedto
► resemblance evaluateandbenchmarkthesynthetictabulardatageneratedbyvarioussynthetictabular
evaluation datagenerationapproaches.Therefore,thispipelinecansupportthescientificcommunity
► utilityevaluation inselectingthemostsuitablesynthetictabulardatagenerationapproachesfortheirdata
► privacyevaluation andapplicationofinterest.
received DOI https://doi.org/ ©2023.TheAuthor(s).
June13,2022 10.1055/s-0042-1760247. ThisisanopenaccessarticlepublishedbyThiemeunderthetermsofthe
acceptedafterrevision ISSN 0026-1270. CreativeCommonsAttribution-NonDerivative-NonCommercial-License,
October29,2022 permittingcopyingandreproductionsolongastheoriginalworkisgiven
articlepublishedonline appropriatecredit.Contentsmaynotbeusedforcommercialpurposes,or
January9,2023 adapted,remixed,transformedorbuiltupon.(https://creativecommons.org/
licenses/by-nc-nd/4.0/)
GeorgThiemeVerlagKG,Rüdigerstraße14,70469Stuttgart,
Germany

e20 Synthetic Tabular Data Evaluation Hernadez et al.
Introduction correlationsbetweenattributes).Theutilitydimensioneval-
uatestheusabilityofstatisticalconclusionsdrawnfromSD
Background ortheresultsfromMLmodelstrainedwithSD.Finally,the
Weareinadigitalerawheretheamountofdatageneratedis privacydimensioncanmeasurehowprivateSDisintermsof
growing exponentially, leading to a paradigm shift from thedisclosureriskofprivateorsensitivedata.Theresultsof
traditional and manual processes toward artificial intelli- such an assessment will support developers in selecting
gence(AI)applicationsindifferentcontexts.However,many the ideal STDG approach for their particular application
AIdevelopmentsarebeingsloweddownbydata-protection requirements.
lawsandimbalanceddata.Therefore,syntheticdatagenera- The study developed by Dankar et al41 classified STD
tion(SDG)researchhasgainedimportanceinrecent years. evaluation metrics and methods into univariate fidelity,
Syntheticdata(SD)wasfirstproposedanddefinedbyRubin1 bivariate fidelity, population fidelity, and analysis-specific
and Little2 in 1993 as datasets consisting of records of measures. However, similar to the studies developed by
individualsyntheticvaluesinsteadofrealvalues.Nowadays, Hittmeiretal,39Gilesetal,40andAlaaetal,44thisclassifica-
the term SD has been extended and can be defined as tion only covers resemblance and utility dimensions.
artificial data generated by a model trained or built to Hittmeir et al42 also proposed and gathered different STD
replicaterealdata(RD)basedonitsdistributions(i.e.,shape evaluationmetricsand methodsfor theutilityand privacy
and variance) and structure (i.e., correlations among the dimensionswithoutincludingresemblance.Incontrast,the
attributes).3 As claimed by Hernandez et al,4 Hu,5 Reiter6 evaluationproposedbyPlatzerandReutterer43onlycovers
and Taub et al,7 fully SD does not contain data from the resemblanceandprivacyevaluation.
original real dataset and less information is lost compared Since our work aims to provide a collection ofdifferent
to other anonymization techniques (i.e., Parzen Window,8 metricsandmethodsforevaluatingdifferentSTDgeneration
Additional Noise Model,8 Random Noise9 and Independent techniquesfortargetedhealthdomainapplications,thefocus
Sampling9) or data balancing techniques (i.e., SMOTE,10 has been placed on the resemblance, utility, and privacy
ADASYN,11 ROS12). For this reason, SDG has shown great dimensions. This manuscript’s approach has not included
promise for (1) augmenting RD by balancing datasets or otherdimensionssuchasgenerationperformance(interms
supplementing the available data to train predictive oftimeandrequiredcomputationresources).
models13–21
and (2) preserving privacy to enable secure All abbreviations used throughout this manuscript are
and private data sharing.8,22–35 In the health domain, SDG gatheredin►AppendixA.
has been researched for different types of data, such as
biomedical signals,14,27 medical images,15–18 electronic RelatedWork
health records (EHR) free-text content,36 time-series This section presents some existing STDG approaches for
smart-home and living labs activity data,19,20,23,28,37 and tabularhealthcaredataandthemostcommonmetricsand
tabulardatafromEHR.8,22,29,30,33–35
methodsforevaluatingtheproposedSTDdimensions.
This study focused on synthetic tabular data generation
(STDG),asitisthepredominanttypeofdatausedtodevelop STDGApproaches
machinelearning (ML) models to aid health care decision- TogenerateSTDinthehealthcarecontext,manyapproaches
making.Therefore,tabularhealthdatapotentiallyoffersthe canbefoundintheliterature.ThesimplestSTDGapproaches
most valuable opportunities to develop AI-based health include Gaussian Multivariate (GM),8,35 Bayesian Net-
care systems. Most of the research studies on STDG in the works,22,29,45 Categorical maximum entropy model,46 and
health domain have focused on proposing new STDG Movement-based kernel density estimation.47 These
approaches8,29,30,32–35,38andevaluatingandbenchmarking
approachesemployastatisticalmodeltolearnthemultivariate
differentSTDGapproachesovervariousdatasets.39–44There
distributionsoftheRDtosampleasetofSTD.Theyaretypically
arealsostudiesthathavehighlightedthepotentialvalueof usedforsmallamountsofdataandarenotveryscalable.
STDG for secure data exchange that ensures patient data Duetotheefficiencyandpopularityofgenerativemodels
privacy. In the workflows proposed by Rankin et al22 and forSDG,specificallygenerativeadversarialnetworks(GAN),in
Hernandez et al,23 STDG techniques are incorporated into otherareasandapplicationsofhealthcare,thereisaninterest
complete data processing workflows that can be used to inexploringwhethertheyhavethepotentialtogeneratehigh-
accelerate research on ML model development for health qualitySTDforhealthcare.GANsarecomposedoftwoneural
caredecision-making. networks (a generator and a discriminator) that learn to
Allpreviouslyreferencedstudieshavedemonstratedthat generate high-quality STD through an adversarial training
althoughSTDGisapotentiallyvaluabletechnologyforhealth process.48Severalauthorshaveusedthesegenerativemodels,
careapplications,priortoitsadoption,anempiricalassess- presentingimprovements,tuninghyperparameters,oradding
ment of the synthetic tabular data (STD) generated with new features.8,9,13,21,24,25,33,34,38,49 While ehrGAN13,21 and
variousapproachesisrequiredacrossdifferentdimensions. medGAN8,9,13,33,34 were proposed to synthesize mainly
These dimensions include resemblance, utility, privacy, numerical and binary data, Wasserstein GAN (WGAN) with
computational cost, veracity, diversity, and generalization. Gradient Penalty,8,13,33,34,38 healthGAN8 and Conditional
The resemblance dimension evaluates how well SD repre- Tabular GAN (CTGAN)24,25,49 synthesize numerical, binary,
sentsRD(coveringaspectsrelatedtodatadistributionand andcategoricaldataefficiently.
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

|     |     |     |     |     |     | Synthetic | Tabular | Data | Evaluation |     | Hernadezet | al. e21 |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | ---------- | --- | ---------- | ------- |
Furthermore, different open-source and commercial ToanalyzewhetherthesemanticsorsignificanceofRDis
packages for STDG have also been released. For example, maintainedinSTD,Choietal,9Wangetal,29Beaulieu-Jones
etal,30andLeeetal55askedsomeclinicalexpertstoevaluate
| the Synthetic | Data | Vault (SDV) | is an | ecosystem | of STDG |     |     |     |     |     |     |     |
| ------------- | ---- | ----------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
approachesfortabulardataandtime-seriesdatacomposed the STD qualitatively, scoring between 1 and 10. This score
ofensemble approaches thatcombineseveral probabilistic indicatedhowrealtheSTDrecordsappearedtothem,wherea
graphical modeling and Deep Learning (DL)-based techni- score of 10was most realistic. Another method that can be
ques.50,51 This ecosystem has been incorporated into the usedifaccesstoclinicalexpertsisunavailableistotrainsome
MLclassifierstolabelrecordsasrealorsynthetic,asLeeetal55
| controlled | data processing |     | workflow | proposed | by Hernan- |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | -------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
dezetalforsecuredataexchange.23Otheropen-sourceand proposedintheirstudy.Bourouetal25alsoproposedusingML
SYNTHO,52 classifierstoanalyzehowdifficultitistodifferentiatebetween
| commercial                                    | packagesfor | STDG | are |     | the Medkit- |                   |     |     |     |     |     |     |
| --------------------------------------------- | ----------- | ---- | --- | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- |
| Learningenvironment,53andYData.54             |             |      |     |     |             | SDandRDsamples.   |     |     |     |     |     |     |
| STDEvaluationMetricsandMethodsforResemblance, |             |      |     |     |             | UtilityEvaluation |     |     |     |     |     |     |
Utility,andPrivacyDimensions The evaluation of the utility dimension has mainly been
Themetricsandmethodsusedtoevaluatetheresemblance, performedusingSTDinMLmodelsbytrainingandanalyzing
utility,andprivacyofSTDintheliteraturearediverse.Most theperformanceofthesemodels.
studiesrelatedtoSTDGinthehealthcarecontextevaluate TrainonRealTestonReal(TRTR)andTrainonSynthetic
TestonReal(TSTR)methodswereusedbyParketal,56Wang
| the resemblance |     | and utility | dimensions, | but | only a few |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
evaluatetheprivacy dimension.Themost relevant metrics etal,31Beaulieu-Jonesetal,30Chin-Cheongetal,38Baowaly
|     |     |     |     |     |     | al,34 | al,24 |     | al,25 |     |     | al,39 |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | ----- | --- | --- | ----- |
andmethodsforSTDreportedintheliteraturearepresented et Kotal et Bourou et Hittmeir et Giles
| below. |     |     |     |     |     | etal,40Dankaretal,41andRashidianetal.32Theseauthors |        |      |        |                |     |          |
| ------ | --- | --- | --- | --- | --- | --------------------------------------------------- | ------ | ---- | ------ | -------------- | --- | -------- |
|        |     |     |     |     |     | trained ML                                          | models | with | RD and | STD separately |     | and then |
ResemblanceEvaluation testedthemwithheld-outRDnotusedfortraining.Theyuse
Thefirststepinresemblanceevaluationistoanalyzewhether differentclassificationmetrics(e.g.,Accuracy,F1-score,ROC,
thedistributionofSTDattributesisequivalenttothedistribu- andAUC-ROC)toevaluateandanalyzethedifferencesinthe
tionoftheRD.Cheetal,21Chin-Cheongetal,38andBourou models’performancewhentrainingthemodelswithRDand
| et al25 compared |     | the distributions | of  | the attributes | of RD | STD. |     |     |       |     |       |     |
| ---------------- | --- | ----------------- | --- | -------------- | ----- | ---- | --- | --- | ----- | --- | ----- | --- |
|                  |     | al13              |     |                |       |      |     |     | al,21 |     | al,31 |     |
against STD. Yang et compared the frequency of the On the other hand, Che et Wang et and Yang
attributes. Additionally, Choi et al,9 Wang et al,31 Abay et al13 augmented the training set of RD with STD. The
etal,45Baowalyetal,34andYaleetal8comparedthedimen-
|     |     |     |     |     |     | authors compared |     | the performance |     | ML  | models | trained |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | --- | ------ | ------- |
sionalprobabilityorprobabilitydistributionsofRDandSTD. onlywithRDandmodelstrainedwithRDandSTDcombined.
Fordistributionscomparison,Yangetal13andRashidian Furthermore,inthestudydevelopedbyGilesetal,40they
etal32analyzedthemeanabsoluteerrorbetweenthemean
analyzedtheutilityoftheSTDbasedonhowwellthefeature
andstandarddeviationvaluesofRDandSTD.Someauthors importancefromRDisrepresentedinSTD.
| also use statistical |                | tests to | analyze the  | univariate | resem-     |                   |     |     |     |     |     |     |
| -------------------- | -------------- | -------- | ------------ | ---------- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- |
| blance of            | STD. Baowalyet |          | al,34 Bourou | et al,25   | and Dankar | PrivacyEvaluation |     |     |     |     |     |     |
et al41 used Kolmogorov–Smirnov (KS) tests to compare Thefewmetricsandmethodsauthorshaveusedforprivacy
distributions,Dashetal37appliedWelscht-tests,andYoon
|     |     |     |     |     |     | assessment | of STD | are based | on  | distance | and | similarity |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | --- | -------- | --- | ---------- |
etal33performedtheStudentt-testtocomparemeanvalues metricsandre-identificationriskevaluation.
theattributes.Yoonetal23andBourouetal25usedChi-
| of  |     |     |     |     |     | Regarding | distance | and | similarity-based |     | metrics, | Park |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ---------------- | --- | -------- | ---- |
square tests to compare the independence of categorical et al56 and Platzer and Reutterer43 used distance to the
attributes. In these studies, they analyzed the p-values closest record, computing the pairwise Euclidean distance
obtained from the statistical tests to determine whether between real and synthetic records where the closer
the null hypothesis is accepted to assure that the STD the mean distance value is to 0, the more the privacy is
preserved.AccordingtoNorgaardetal,28themaximumreal
attributespreservethepropertiesofRDattributesanalyzed
withthestatisticaltests. tosyntheticsimilarityvalue,computedbythecosinesimi-
Additionally,otherauthorshaveuseddistancemetricsto larity, indicates whether the model has memorized and
evaluatetheresemblanceofSTD.Hittmeiretal39measured
|     |     |     |     |     |     | stored RDand | is reallygeneratingdata |     |     | and | notcopying | it. |
| --- | --- | --- | --- | --- | --- | ------------ | ----------------------- | --- | --- | --- | ---------- | --- |
the distance between RD and SD, computing the nearest Other distance-based metrics used by Yoon et al33 are the
neighborsrow-by-row. Jensen-Shannon divergence (JSD) and the Wasserstein dis-
In evaluating multivariate relationships, Rankin et al,22 tance. The authors used them to compute the balance
Yale et al,8 Wang et al,29 Bourou et al,25 Hittmeir et al,39 betweentheidentifiabilityandqualityofSTD.
|     | al,41 |     | al32 |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dankar et and Rashidian et visually compared Severaldisclosureattacksimulationshavebeenproposed
the Pairwise Pearson Correlation (PPC) matrices to assess intheliteraturetoassessthere-identificationofRDdisclosure
riskthroughSTD.Choietal,9Parketal,56Yaleetal,8Hittmeir
| whether correlations |     | between | attributes | of RD | are main- |     |     |     |     |     |     |     |
| -------------------- | --- | ------- | ---------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
tained in STD. Additionally, principal component analysis et al,42 and Mendelevitch et al57 simulated membership
transformationhasbeenusedbyYaleetal8tocomparethe inferenceattackstoanalyzethedisclosureriskofacomplete
dimensionalpropertiesofSTDandRD. recordinRDbycomputingdistancemetricsbetweenRDand
|     |     |     |     |     |     | MethodsofInformationinMedicine |     |     | Vol.62 No.S1/2023 |     | ©2023.TheAuthor(s). |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | ----------------- | --- | ------------------- | --- |

| e22 | Synthetic | Tabular | Data | Evaluation |     | Hernadez | et al. |     |     |     |     |     |     |     |     |
| --- | --------- | ------- | ---- | ---------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
STD records and using accuracy and precision metrics to 3. Weanalyzeandevaluatethesuggestedpipelineusingsix
quantify the membership risk. In contrast, Choi et al9 and differenthealthcare-relatedopen-sourcedatasetsandfour
Lesh57
Mendelevitch and additionally simulated attribute STDG approaches. The proposed evaluation metrics and
inference attacks to quantify the disclosure risk of some methodsareusedtoevaluatethequalityoftheSTDgener-
attributesofthedataset.Definingattributesconsideredqua-
atedforeachdatasetandSTDGapproachcombination.
si-identifiers(QID)andtrainingsomeMLmodelswithSTDto 4. Based on the evaluation results, we benchmark the STDG
predicttherestoftheattributes,theyanalyzehowaccurately approachesusedto generate STDanddiscusstheveracity
anattackercouldpredictsomeRDattributesiftheyobtained andefficiencyoftheproposedSTDevaluationmetricsand
accesstotheSTD. methods.Wedemonstratethatthepresentedpipelinecan
|     |     |     |     |     |     |     |     | effectively | be  | used to   | evaluate | and | benchmark  |           | different |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------- | --- | ---------- | --------- | --------- |
|     |     |     |     |     |     |     |     | approaches  |     | for STDG, | helping  | the | scientific | community |           |
Objectives
|     |     |     |     |     |     |     |     | select | the most | suitable | approaches |     | for | their | data and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ---------- | --- | --- | ----- | -------- |
Published studies that evaluate STD generated using one or applicationofinterest.
moreSTDGapproachesusedifferentmetricsandmethodsto
Methods
|     | evaluate | STDquality.Althoughsome |     |     | publishedstudiespro- |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | ----------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
poseorcategorizeSTDevaluationmetricsandmethodsinto SyntheticTabularDataEvaluationMetricsand
|     | differentgroups,theyhaveonlyfocusedonevaluatingoneor |     |     |     |     |     |     | Methods |     |     |     |     |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
two of the previously defined dimensions. Furthermore, as TheproposedmetricsandmethodsforevaluatingSTDcanbe
concludedinthereviewbyGhoshehetal,58auniversaland clustered into three dimensions: resemblance, utility, and
standardizedevaluationmethodologyfordevelopingreliable privacy. Different metrics and methods from theliterature
STDGapproachesforSTDhasnotyetbeendefined. have been selected and configured in an organized way
Acomplete,guided,andobjectiveevaluationandbench- within each dimension. The complete taxonomy of the
marking strategy for STD over the dimensions of resem- selected methods, which can be used within the defined
blance, utility, and privacy does not exist in the literature. pipelinetoevaluateSTDgeneratedwithoneSTDGapproach
Thus,anorganizedpipelineorprocessisrequiredtoassess orcomparetheSTDgeneratedbydifferentSTDGapproaches,
|     | STDinthesethreedimensionstoenabletheselectionofthe |     |     |     |     |     |     | isdepictedin►Fig.1. |     |     |     |     |     |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
bestapproachorapproachestogeneratethedesiredSTDfor
|     | individualusecases. |     |     |     |     |     |     | ResemblanceEvaluation |     |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
The aim of this paper is to identify key dimensions, per Intheresemblancedimension,thecapacityofSTDtorepre-
dimensionmetrics,andmethodsforevaluatingSTDgenerated sentRDisevaluated.Statistical,distribution,andinterpret-
with different techniques and configurations for health do- ability characteristics are analyzed using four methods:
mainapplicationsdevelopmentandtoprovideastrategyto univariate resemblance analysis (URA), multivariate rela-
orchestrate them. We propose and assess a collection of tionshipsanalysis(MRA),anddatalabelinganalysis(DLA).
standardized metrics and methods to evaluate the resem- Two other metrics havebeen proposed for resemblance
blance,utility,andprivacydimensionsofSTDforuseinthe evaluation,i.e.,visualanalysisofattributesanddimensional
health domain. The proposed metrics and methods were reduction analysis (DRA). However, due to the difficulties
selectedfromtheliteratureandorchestratedintoacomplete associated with quantitatively analyzing these, they have
evaluationpipelinetoenableaguidedandcomparableevalu- beenexcludedfromthefinalmethodologyandincludedin
ationofSTD.Ourcontributionscanbesummarizedasfollows: Appendix B and Supplementary Material 1, available in
onlineversiononly.
1. Weproposeasetofmetricsandmethodstoevaluatethe
resemblance,utility,andprivacydimensionsofSTDand
UnivariateResemblanceAnalysis
|     | present   | a   | meaningful | orchestration   |          | of them.  | Different   |               |              |     |                |     |            |             |       |
| --- | --------- | --- | ---------- | --------------- | -------- | --------- | ----------- | ------------- | ------------ | --- | -------------- | --- | ---------- | ----------- | ----- |
|     |           |     |            |                 |          |           |             | This analysis | examines     |     | the attributes |     | of RD      | and STD     | inde- |
|     | universal |     | metrics    | and methods     | are      | suggested | for inde-   |               |              |     |                |     |            |             |       |
|     |           |     |            |                 |          |           |             | pendently     | to determine |     | whether        | the | univariate | statistical |       |
|     | pendent   | use | for        | each dimension. | Although |           | the metrics |               |              |     |                |     |            |             |       |
characteristicsofRDarepreservedinSTD.Statisticaltests,
andmethodsproposedarenotnew,theirorchestrationin
distancecalculation,andvisualcomparisonsareproposed.
anorganizedwayandthecalculationofoverallscoresfor
Statisticaltestscanbeusedtocomparetheattributesfrom
eachdimensionarenovel.
RDandSTD.Theyshouldbeperformedindependentlyforeach
2. Tothebestofourknowledge,thisworkisthefirstattempt
attributewithaproposedsignificancelevelofα¼0.05,mean-
toproposeanduseacompleteanduniversalSTDevalua-
ingthatifthep-valueobtainedfromthetestishigherthanthis
tionpipelinecoveringtheresemblance,utility,andpriva-
|     |     |     |     |     |     |     |     | value, the | null | hypothesis | (h0) | is accepted. |     | Otherwise, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | ---- | ------------ | --- | ---------- | --- |
cydimensions.Thepipelineisgeneralizabletoanykindof
|     |     |       |             |     |         |      |               | alternative | hypothesis | (h1) | is  | accepted. | The | properties | ana- |
| --- | --- | ----- | ----------- | --- | ------- | ---- | ------------- | ----------- | ---------- | ---- | --- | --------- | --- | ---------- | ---- |
|     | STD | since | the metrics | and | methods | have | been selected |             |            |      |     |           |     |            |      |
lyzedineachtestarepreservedinSTDifh0isaccepted.For
|     | according |     | to the | most commonly | used | STD | evaluation |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ------ | ------------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
numericalattributes,thefollowingtestsareproposed:
metricsandmethodsreportedintheliterature.Addition-
ally,wepresentamethodologytocategorizetheperfor- (cid:129) StudentT-testforthecomparisonofmeans.
mance of each STDG approach in each dimension as oh0:MeansofRDfeatureandSTDattributeareequal.
“Excellent,”“Good,”and“Poor.”
oh1:MeansofRDfeatureandSTDattributearedifferent.
|     | MethodsofInformationinMedicine |     |     | Vol.62 | No.S1/2023 | ©2023.TheAuthor(s). |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | ------ | ---------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     | Synthetic |     | Tabular | Data | Evaluation | Hernadezet | al. e23 |
| --- | --- | --- | --- | --------- | --- | ------- | ---- | ---------- | ---------- | ------- |
Fig.1 TaxonomyoftheproposedpipelineofmetricsandmethodstoevaluateSTDinthreedimensions:resemblance,utility,andprivacy.STD,
synthetictabulardata.
(cid:129) MannWhitneyU-testforpopulationcomparison. Cosine distance is defined as the complement of cosine
oh0:RDfeatureandSTDattributecomefrom thesame similarity,whichisthecosineoftheanglebetweentwovectors
population. inn-dimensionalspace;i.e.,thedotproductofthetwovectors
oh1:RDfeatureandSTDattributedonotcomefromthe isdividedbytheproductofthetwovectors’lengths(Equation
samepopulation. 1).Ascosinesimilarityisdefinedpositive,thecosinedistance
isboundedbetween0and1,indicatingthedistancebetween
(cid:129) Kolmogorov–Smirnovtestfordistributionscomparison.
oh0:RDfeaturedistributionandSTDattributedistribu- two sets of values. The lower the value is, the higher the
resemblancebetweenthetwosetsofvalueswillbe.Therefore,
tionareequal.
athresholdof0.3hasbeenexperimentallysetbasedonthe
oh1:RDfeaturedistributionandSTDattributedistribu-
|     |     |     |     | exploratory | analysis | of  | the results | to indicate |     | that the STD |
| --- | --- | --- | --- | ----------- | -------- | --- | ----------- | ----------- | --- | ------------ |
tionarenotequal.
|     |     |     |     | attribute   | significantly |           | resembles | the RD    | attribute. | A value     |
| --- | --- | --- | --- | ----------- | ------------- | --------- | --------- | --------- | ---------- | ----------- |
|     |     |     |     | higher than | this          | threshold | would     | represent | no         | substantial |
For categorical features, the Chi-square (χ2) test is pro- resemblancebetweentheSTDattributeandRDattribute.
posedtoanalyzethefeatureindependencebetweenrealand
syntheticcategoricalattributes.Ifh0isaccepted,thestatis-
ticalpropertiesarenotpreservedinthiscase.h0andh1are
definedas:
Equation1:Cosinedistance
| (cid:129) h0: No statistical | relationship | exists between | the real |     |     |     |     |     |     |     |
| ---------------------------- | ------------ | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
categoricalvariableandthesyntheticcategoricalvariable.
|     |     |     |     | Jensen-Shannon |     | distance |     | is the square | root | of the JSD, |
| --- | --- | --- | --- | -------------- | --- | -------- | --- | ------------- | ---- | ----------- |
(cid:129) h1:Thereisastatisticalrelationshipbetweentherealand
|     |     |     |     | which measures |     | the | similarity | between | two | probability |
| --- | --- | --- | --- | -------------- | --- | --- | ---------- | ------- | --- | ----------- |
syntheticcategoricalvariables.
|     |     |     |     | distributions | (Equation |     | 2); m | is the pointwise |     | mean of p |
| --- | --- | --- | --- | ------------- | --------- | --- | ----- | ---------------- | --- | --------- |
Somedistancemetricscanalsobecomputedbetweenthe and q, and D is the Kullback-Leibler divergence, defined in
RDandSTDattributesforURA.Thelowerthedistancevalues Equation3.Theprobabilitydistributionsofthefeatureshave
are, the better the univariate resemblance is preserved in been usedto computethesedistances: p is the probability
STD. Three distancemetrics are proposed: cosine distance, distribution of the RD attribute, and q is the probability
Jensen-Shannon distance,and Wassersteindistance.Before distribution of the STD attribute. A value lower than 0.1
computingalldistances,RDandSTDneedtobescaled.Inthe representsaperfectresemblancesincehighervalueswould
following(Equations1to5),ristheattributeofRD,andsis indicatethatthedifferencesindistributionsaresignificantly
| theattributeofSTD. |     |     |     | higher.                        |     |     |        |            |                     |     |
| ------------------ | --- | --- | --- | ------------------------------ | --- | --- | ------ | ---------- | ------------------- | --- |
|                    |     |     |     | MethodsofInformationinMedicine |     |     | Vol.62 | No.S1/2023 | ©2023.TheAuthor(s). |     |

e24 Synthetic Tabular Data Evaluation Hernadez et al.
Additionally,foreachmatrix,thedifferencesbetweenthe
correlations of RD and STD are calculated to compute the
percentageofrelationshipsmaintainedintheSTD(thosethat
Equation2:Jensen-ShannonDistance haveadifferent valuelower than0.1).Thisway,twovalues
between0and1areobtained,oneexpressingthepercentage
ofnumericalattributerelationshipsmaintainedandtheother
the percentage of categorical attribute relationships main-
tained.Ifthevaluesarehigherthan0.6,theSTDGapproachis
categorizedas“Excellent”sincemorethanhalfoftherelation-
Equation3:Kullback-LeiblerDivergence shipsarepreservedinRD.Iftheyareequalorbetween0.4and
0.6,it iscategorizedas“Good,”representing thathalfofthe
Wasserstein distance can be seen as the minimum cost relationshipsarepreserved.Finally,ifthevaluesarelowerthan
required to transform a vector (r) into another vector (s), 0.4,theperformanceoftheSTDGapproachis“Poor”asithas
where the cost is measured as the amount of distribution preservedlessthanhalfoftherelationships.Aftercompleting
weightthatmustbemoved,multipliedbythedistanceithas thiscategorizationforeachmatrix,atotalMRAperformanceis
to be moved (Equation 4); R and S are the cumulative obtainedbygivingequalweight(50%)tobothanalyses.
distributionfunctionoftheRD,andSTDattributes,respec-
tively.Asincosinedistance,athresholdof0.3isproposedto DataLabellingAnalysis(DLA)
assuretheresemblanceoftheattribute. The final step proposed for resemblance evaluation can be
usedtoevaluatethesemanticsofSTD.Thismethodisproposed
toanalyzetheperformanceofsomeclassifierswhenlabeling
recordsasrealorsyntheticthroughthefollowingsteps:
Equation4:WassersteinDistance 1. Combineandlabelrealand syntheticdatasets(0forRD
and1forSTD)inasingledataset.
2. Split the combined dataset into train and test sets, i.e.,
For statistical tests and the distance calculation, the
80:20split.
number of STD attributes that fulfill the requirements to
3. Pre-processthetrainandtestdata,i.e.,standardizenumer-
resembleRDattributeshasbeenconsideredtocategorizethe
icalattributesandone-hotencodecategoricalattributes.
STDGapproachperformance.Ifmorethanhalfoftheattrib-
4. Train (with training data) and evaluate (with test data)
utes maintain resemblance, the approach is classified as
some ML classifiers to analyze their performance in
“Excellent.” If less than half maintained resemblance, it is
labellingrecordsasrealorsynthetic.
classifiedas“Good”andifnoneoftheattributesmaintained
resemblance,itisclassifiedas“Poor.” ThecommonlyusedanddiverseMLclassifiersproposed
To get an overall score of URA, the performancesfor all forthisanalysisareRandomForest(RF),K-NearestNeighbors
previouslypresentedmetricscanbecalculatedaccordingto (KNN),DecisionTree(DT), SupportVectorMachines(SVM)
their results. First, the categorization is translated into a and Multilayer Perceptron (MLP). For our analysis, these
numericalvalue(“Excellent”¼3,“Good”¼2and“Poor”¼1), classifiers have been implemented using Python’s Scikit-
and then the same weight (33.33%) is given for the three Learn0.24.2MLlibrarywiththelistedparameters:
methodspresented(statisticaltestsofnumericalattributes,
(cid:129) The RFmodel has been implemented usingRandomFor-
statisticaltestsofcategoricalattributes,anddistancecalcu-
estClassifierwithn_estimators¼100,n_jobs¼3,random_-
lationsfornumericalattributes).Theresultingscore,round-
state¼9andallotherparameterssettotheirdefaults.
edtothenearestinteger,givesavaluebetween1and3that
(cid:129) TheKNNmodelhasbeenimplementedusingKNeighbor-
indicatestheURAscoreofSTD.
sClassifier withn_neighbors¼10,njobs¼3andallother
parameterssettotheirdefaults.
MultivariateRelationshipAnalysis
(cid:129) TheDTmodelhasbeenimplementedusingDecisionTree-
This analysis involves assessing whether the multivariate
Classifierwithrandom_state¼9andallotherparameters
relationshipsof RDare preserved in STD or not. To dothat,
settotheirdefaults.
the computation of two correlation matrices has been
(cid:129) The SVM model has been implemented using SVC with
definedforRDandSTD:PPCmatricesfornumericalvariables
C¼100, max_iter¼300, kernel¼“linear,” probability¼
(Equation5)foreachpairoffeaturesxandy;x̂ andŷ arethe
True, random state¼9 and all other parameters set to
meanvalueofthefeaturesandnormalizedcontingencytables
theirdefaults.
forcategoricalvariables.ThecorrelationmatricesofRDcanbe
(cid:129) TheMLPmodelhasbeenimplementedusingMLPClassi-
visuallycomparedwiththematricesofSTDusingheatmaps.
fier with hidden_layer_sizes¼(128,64,32), max_iteration
¼300, random_state¼9 and all other parameters set to
theirdefaults.
Aftertrainingandtestingthemodels,classificationperfor-
Equation5:PPC mancemetrics(accuracy,precision,recall,andF1-score)canbe
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

Synthetic Tabular Data Evaluation Hernadezet al. e25
analyzedvisuallywithboxplots.Toindicatethatthesemantics Section1.2.2,threemetricsareproposedforthis:Euclidean
ofRDarepreservedinSTD,aclassifiershouldnotdistinguishifa distance between each pair of records, Hausdorff distance
recordissyntheticorreal.Thus,theclassificationmetricsshould betweenSTDandRD,andSyntheticToReal(STR)similarity.
be lower than or equal to 0.6 for “Excellent” resemblance, The Euclidean distance is the square root of the sum of
meaningthatthemodelshaveclassifiedmostofthesynthetic squares of differences between RD and STD features, as
records as real. Obtaining metric values higher than 0.6 and defined in Equation 6. In this case, the Euclidean distance
lower than 0.8 indicate a “Good” resemblance, while values canbecomputedforeachpairofrecords.Then,themeanand
equaltoorgreaterthan0.8indicatea“Poor”resemblance. standarddeviationofalldistancesshouldbeanalyzed.The
higherthemeandistanceandthelowerthestandarddevia-
TotalResemblancePerformance tion are, the more the privacy is preserved. Thus, mean
Aftercompletingthefouranalysesproposedforresemblance valueshigherthan0.8andstandarddeviationvalueslower
evaluation,aweightedaveragecanbecomputedtoobtaina thanorequalto0.3indicateprivacyispreserved.
total resemblance score. This allows us to assign higher or
lower importance to each result based on the researchers’
STDGgoals.AnexampleweightingappliedinSTDEvaluation
(section 4) has been URA¼0.4, MRA¼0.4, and DLA¼0.2.
These weights were experimentally set to prioritize the
abilityof STD to resemble univariateand multivariatepat- Equation6:EuclideanDistance
ternsovertheabilityofaclassifiertodistinguishbetweenRD
and STD for this evaluation. Finally, by applying these Thecosinesimilaritymetricisproposedtocomputethe
weights, the total score is obtained, and after rounding it STRsimilarity,whichcomputessimilarityasthenormalized
to the nearest integer, the total score is categorized as dotproductoftwodatasets(Equation7;RisarecordfromRD
“Excellent”iftheresultingvalueis3,“Good”iftheresulting andSisarecordfromSTD).Thepairwisesimilarityvaluecan
valueis2,or“Poor”iftheresultingvalueis1. be computed for each pair of records, and the mean and
maximumvaluesofthosepairwisesimilarityvaluesshould
UtilityEvaluation beanalyzed.Ifthemeanvalueishigherthan0.5,theSTDis
Intheutilitydimension,theabilityofSTD,insteadofRD,to veryclosetotheRD,soprivacyisnotpreserved.Inallother
train ML models is analyzed to determine if ML models cases,itcanbesaidthatprivacyispreserved.
trained with STD produce similar results to ML models
trained with RD. To do that, TRTR and TSTR analyses are
proposed.MLclassifiersshouldbetrainedwithRDandthen
separately with STD. Thesame ML classifiers described for
DLA analysis are proposed for this evaluation due to their Equation7:CosineSimilarity
simplicity,scalability,andtrainingefficiency.
The data must be pre-processed before training and TheHausdorffdistancemeasureshowfartwosubsetsofa
testing the models, i.e., by standardizing numerical attrib- metricspacearefromeachotherasitisthegreatestofallthe
utesandone-hotencodingcategoricalattributes.Alltrained distancesfromapointinonesettotheclosestpointintheother
modelsshouldbetestedwiththesameRD(20%ofthereal set(Equation8;Ristherealdataset;Sisthesyntheticdataset).
dataset held out before training the STDG approaches). To TwosetsarecloseintheHausdorffdistanceifeverypointof
analyzetheclassificationresults,accuracy,precision,recall, eithersetisclosetosomepointintheotherset.Thus,thehigher
and F1-score classification metrics are proposed, and their thisdistancevalueis,thebettertheprivacyispreservedinSTD,
absolutedifferenceswhenTRTRandTSTR.ToassurethatSTD asahighvalueindicatesthattheSTDisfarfromtheRD.Since
utility is “Excellent,” the metrics differences should not thismetricisnotboundedbetween0and1,avaluehigherthan
exceed a proposed threshold of 0.2. Ifdifferences between 1hasbeenconsideredtoassurethatprivacyispreserved.
0.2 and 0.8 are obtained, the performance in the utility
dimension shouldbe categorizedas “Good” andif theyare haus_dist(S,R)¼max{h(S,R),h(R,S)}
higherthan0.8,theperformanceisconsidered“Poor.”
Equation8:HausdorffDistance
PrivacyEvaluation
For the privacy dimension, it is proposed to evaluate the Forthesethreedistance-basedmetrics,ifallthreemetrics
similarityofRDandSTDandthere-identificationriskofreal fulfill the condition to preserve privacy, the categorization
patientsorrecords. forprivacypreservationis“Excellent.”Ifoneortwometrics
fulfillthecondition,itis“Good”;otherwise,itis“Poor.”
SimilarityEvaluationAnalysis(SEA)
In the SEA, it is proposed to evaluate how private STD is Re-IdentificationRiskAnalysis(RIRA)
compared to RD in terms of similarity between real and Thisanalysisproposestoevaluatethelevelofdisclosurerisk
syntheticrecords.Basedonthedistanceandsimilaritymetrics ifanattackeroranadversarialobtainsaccesstoSTDanda
forprivacyevaluationusedbyotherauthorsandmentionedin subset of RD. For this, two simulations are proposed: (1)
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

| e26 Synthetic | Tabular Data                                | Evaluation | Hernadez | et al. |     |     |     |
| ------------- | ------------------------------------------- | ---------- | -------- | ------ | --- | --- | --- |
| Fig.2         | SimulatedMIA.MIA,membershipinferenceattack. |            |          |        |     |     |     |
membershipinferenceattack(MIA)whenanattackertriesto theSTDandasubsetoftheRDrandomlydistributed.Usinga
identify if real patient records havebeen used totrain the patientrecord(r)fromtheRDsubset,theattackerwilltryto
STDGapproach(►Fig.2),and(2)attributeinferenceattack identifytheclosestrecordsintheSTDwithadistancemetric
(AIA)whenanattackerhasaccesstosomeattributesofthe calculation.Ifthereisanydistancelowerthansomethreshold,
RDandtriestoguessthevalueofanunknownattributeofa the attackerdetermines that there is at leastone rowclose
patientfromtheSTD(►Fig.3).57
|     |     |     |     | enough to | RD in the STD, meaning | that r has been | used to |
| --- | --- | --- | --- | --------- | ---------------------- | --------------- | ------- |
InanMIA,iftheattackerdeterminesthatrealrecordswere generate STD. This process is depicted in Algorithm 1
usedtotraintheSTDGapproach,itcouldbesaidthattheyhave and►Fig.2.
re-identifiedthepatientfromtheSTD.57►Fig.2illustratesthis
Forthisanalysis,theattacker’ssuccessrateisproposedto
attackwhereahypotheticalattackerhasaccesstoallrecordsof beevaluatedbysimulatingthiskindofattackbycalculating
| Fig.3                          | SimulatedAIA.AIA,attributeinferenceattack. |                   |                     |     |     |     |     |
| ------------------------------ | ------------------------------------------ | ----------------- | ------------------- | --- | --- | --- | --- |
| MethodsofInformationinMedicine |                                            | Vol.62 No.S1/2023 | ©2023.TheAuthor(s). |     |     |     |     |

Synthetic Tabular Data Evaluation Hernadezet al. e27
Algorithm1:SimulationofaMIA made by the models trained on STD for each data batch
combinationcanbeevaluatedusingaccuracyforcategorical
attacker_data realsetofdataknownbytheattacker attributesandroot-mean-squared-error(RMSE)fornumeri-
synthetic_data syntheticsetofdatathatispublicly
cal attributes. Higher accuracy values (close to 1) indicate
available
higherdisclosurerisk,whilelowerRMSEvalues(closeto0)
forrowinattacker_data
dist compute_distances(row,synthetic_data)
reflecthigherdisclosurerisk.Themetricvaluesareobtained
ifany(dist)<thrthen for each QID combination, and all attributes are evaluated
record_identified True visuallywithaboxplotforeachriskattribute.Additionally,
else
the percentage of correctly predicted attributes has been
record_identified False
calculatedtocategorizethere-identificationrisk.Themode
oftheanalyzedmetricshasbeenconsideredtodetermineif
the Hamming distance (Equation 9), which represents the an attribute has been predicted; for categorical attributes,
proportion of non-equal attributes between two records, accuracy mode is equal to 1, and for numerical attributes,
betweeneachrowoftheRDsubsetandSTDrows. RMSEmodeisequalto0.Ifahighpercentage(higherthan
0.6)isobtained,asmorethanhalfoftheattributeshavebeen
re-identified,theAIAresultsarecategorizedas“Poor.”Fora
percentagebetween0.4and0.6,theresultiscategorizedas
Equation9:Hammingdistance
“Good”sinceapproximatelyhalfoftheattributeshavebeen
re-identified.Apercentagelowerthan0.4indicatesthatless
Reasonablethresholdstoassurethatriscloseenoughtoa thanhalfoftheattributeshavebeenre-identified, demon-
recordinSTDare0.4,0.3,0.2,and0.1becausealowerHamming strating“Excellent”privacypreservationforthisattack.
distance representsmoresimilarity in therecords.Since it is
known if r belongs to the training data or not, accuracy TotalPrivacyPerformance
(proportion ofcorrect predictions madeby the attacker) and Aftercomputingtheresultsforthethreeprivacyevaluation
precision (proportion of records used for training the STDG methodsproposed,atotalprivacyscoreshouldbecalculated,
approachidentifiedbytheattacker)valueshavebeencalculated. weightingtheresultsfromallthemethods.Forexample,in
To obtain an “Excellent” privacy preservation categorization, theSTDevaluation,thefollowingweightshavebeenexperi-
accuracy and precision values should be 0.5 or lower for all mentallygiventothethreeanalysesfortheprivacydimen-
thresholds. Any value above 0.5 indicates increasing levels of sion: SEA¼0.4 and RIRA¼0.6 (MIA¼0.3 and AIA¼0.3). A
disclosurerisk,obtaininga“Good”or“Poor”privacypreserva- higherweightwasassignedtoRIRAtoprioritizethemetrics
tion categorization depending on the number of thresholds analyzing whetherRDcouldbeinferredfromSTDover the
wherethevaluesarehigherthan0.5.Theaccuracyandprecision metric and investigating howsimilar STD is to RD. Finally,
valueshavebeenplottedtoanalyzeandinterprettheseresults oncethisweightingisappliedandtheresultisroundedtothe
asafunctionoftheproportionofrecordsintheSTDpresentin nearestinteger(i.e.,assignedto1,2or3),theprivacyofSTDis
theRDsubsetknownbytheattackerforeachthreshold. categorizedas“Excellent”(3),“Good”(2),or“Poor”(1)based
In an AIA, an attackerhas accessto STDand a subsetof onthetotalscoreobtainedwhenapplyingtheseweights.
attributesforsomeRDrecords,generallyQIDssuchasage,
gender, height, weight, etc.57 As shown in ►Fig. 3 and SyntheticTabularDataEvaluation
Algorithm 2 the attacker will use ML models trained with To prove and trust the efficiency and usability of the pro-
STDtopredictthevaluesofrestoftheattributesoftheRD posedpipelineforSTDevaluation,severaldifferentdatasets
records. havebeenselectedandthensynthesizedwithdifferentSTDG
Thesuccessofthisattackcanbemeasuredbydefiningthe approaches. The STD generated for the selected datasets is
QIDofeachdatasetandthenusingthemtotrainMLmodels, then evaluated and benchmarked. All code and example
i.e.,DTmodels,withSTDtopredicttherestoftheattributes. notebooksareavailableinaGithubrepository.59
Next, 50%of the RD(randomlydistributed)can beused to
evaluatetheperformanceofthemodels,generatingbatches SelectedData
ofdatawitheachQIDcombination.Thisway,thepredictions Six open-source health care-related datasets have been
selected forsynthesis.A briefdescription of these datasets
Algorithm2:SimulationofanAIA
and the number of attributes and records are presented
in ►Table 1. Each dataset wasfirst pre-processed, deleting
attacker_data realdatasetofQIDknownbytheattacker
synthetic_data syntheticsetofdatathatispublicly
missingvaluesandperformingadatasplitintotwosubsets.
available Eightypercentoftherecordshavebeenusedfortrainingthe
x_train QIDofthesyntheticsetofdata STDGapproaches,and20%oftherecordsforutilitydimen-
attributes ListofnonQIDattributesofthesetofdata sionevaluationandRIRAsimulations.
y_train NonQIDattributesofthesyntheticsetofdata
forattributeinattributes
FullySyntheticTabularDataGenerationApproaches
ml_model.train(x_train,y_train[attribute])
inferred_values ml_model.predict(attacker_data) TogenerateSTDforthedatasetspresentedpreviously,four
open-sourceSTDGapproacheshavebeenused,twoofwhich
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

| e28 | Synthetic | Tabular | Data | Evaluation |     | Hernadez |     | et al. |     |     |     |     |     |     |     |
| --- | --------- | ------- | ---- | ---------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Table 1 Briefdescriptionoftheselectedhealth-relateddatasetsforSTDGandSTDevaluation
|     | ID  | Datasetname |     |     |     |     |     |     |     | Year |     | Num.attrib. |     | Num.records |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----------- | --- | ----------- | --- |
Diabetes130-U.S.hospitalsforyears1999–2008dataset65
|     | A   |                                              |     |     |     |     |     |     |     | 2014 |     | 55  |     | 101,766 |     |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- |
|     | B   | Cardiovasculardisease(CVD)dataset66          |     |     |     |     |     |     |     | 2019 |     | 13  |     | 70,000  |     |
|     | C   | Estimationofobesitylevelsbasedoneatinghabits |     |     |     |     |     |     |     | 2019 |     | 17  |     | 2,111   |     |
andphysicalconditiondataset67
|     | D   | ContraceptiveMethodChoice(CMC)dataset68 |     |     |     |     |     |     |     | 1997 |     | 9   |     | 1,473 |     |
| --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ----- | --- |
|     | E   | PimaIndiansDiabetes(PID)dataset69       |     |     |     |     |     |     |     | 2016 |     | 9   |     | 769   |     |
|     | F   | IndianLiverPatient(ILP)dataset70        |     |     |     |     |     |     |     | 2012 |     | 11  |     | 583   |     |
areGANs,andtheothertwoareclassicalapproaches.These tionoftheresultsfromallmetricsandmethodsisavailable
in(►SupplementaryMaterial1,availableinonlineversion
approachesareasfollows:
|     |             |     |              |       |     |           |      |          | only). In | this supplementary |     |     | material | there are | additional |
| --- | ----------- | --- | ------------ | ----- | --- | --------- | ---- | -------- | --------- | ------------------ | --- | --- | -------- | --------- | ---------- |
|     | 1. Gaussian |     | Multivariate | (GM): | A   | classical | STDG | approach |           |                    |     |     |          |           |            |
metricsthathavebeenexcludedfromthemethodologyand
|     | based | on  | statistical | modeling |     | that implements |     | a multi- |           |        |          |     |          |             |        |
| --- | ----- | --- | ----------- | -------- | --- | --------------- | --- | -------- | --------- | ------ | -------- | --- | -------- | ----------- | ------ |
|     |       |     |             |          |     |                 |     |          | explained | in the | Appendix | B.  | Based on | the results | ofeach |
variatedistributionusingaGaussianCopulatocombine
|     |     |     |     |     |     |     |     |     | evaluation | analysis | presented |     | in the | pipeline, | the results |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | --- | ------ | --------- | ----------- |
marginalprobabilitiesestimatedusingunivariatedistri-
|     |          |     |              |     |              |     |            |       | obtained  | for each    | synthesized |                 | dataset | have been | summa-     |
| --- | -------- | --- | ------------ | --- | ------------ | --- | ---------- | ----- | --------- | ----------- | ----------- | --------------- | ------- | --------- | ---------- |
|     | butions. |     | The approach |     | is available |     | at Copulas | 0.5.0 |           |             |             |                 |         |           |            |
|     |          |     |              |     |              |     |            |       | rized and | categorized |             | as “Excellent,” | “Good,” | or        | “Poor” for |
documentation.60
eachdimension(resemblance,utility,andprivacy),basedon
|     | 2. Synthetic |     | Data Vault | (SDV): | This | approach |     | is an STDG |     |     |     |     |     |     |     |
| --- | ------------ | --- | ---------- | ------ | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
thefinalweightedscores.
|     | ecosystem |     | of libraries |     | that uses | several     | probabilistic |           |     |     |     |     |     |     |     |
| --- | --------- | --- | ------------ | --- | --------- | ----------- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
|     | graphical |     | modeling     | and | DL-based  | techniques. |               | To enable |     |     |     |     |     |     |     |
ResemblanceEvaluation
avarietyofdatastoragestructures,theyemployunique
►Table2showstheresultsofapplyingtheproposedresem-
hierarchicalgenerativemodelingandrecursivesampling
|     |     |     |     |     |     |     |     |     | blanceevaluationmetricsandmethods |     |     |     |     | totheSTDsynthe- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --------------- | --- |
techniques.61ItisavailableatTheSyntheticDataVault.51
sizedwitheachSTDGapproachforeachdataset.
|     | 3. Conditional |     | Tabular | Generative |     | Adversarial |     | Network     |     |             |           |     |          |           |       |
| --- | -------------- | --- | ------- | ---------- | --- | ----------- | --- | ----------- | --- | ----------- | --------- | --- | -------- | --------- | ----- |
|     |                |     |         |            |     |             |     |             | The | resemblance | dimension |     | has been | perfectly | main- |
|     | (CTGAN):       |     | A STDG  | approach   |     | proposed    | by  | Xu et al in |     |             |           |     |          |           |       |
201949 tained with GM for the six datasets. SDV has performed
|     |     | defined | as  | a collection |     | of DL | models | based on |             |        |             |     |           |     |             |
| --- | --- | ------- | --- | ------------ | --- | ----- | ------ | -------- | ----------- | ------ | ----------- | --- | --------- | --- | ----------- |
|     |     |         |     |              |     |       |        |          | excellently | on the | resemblance |     | dimension | for | half of the |
GANmodelsforasingledatatable.ItcanlearnfromRD
datasets(C,E,F)andperformancewasgoodforotherdata-
fidelity.
|     | and | generate | synthetic |     | clones | with | high | It is |          |        |           |     |               |      |         |
| --- | --- | -------- | --------- | --- | ------ | ---- | ---- | ----- | -------- | ------ | --------- | --- | ------------- | ---- | ------- |
|     |     |          |           |     |        |      |      |       | sets (A, | B, and | D). CTGAN |     | has performed | very | well in |
availableat.62
|     |     |     |     |     |     |     |     |     | retaining | resemblance |     | for one | dataset | (B), quite | well for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | ------- | ---------- | -------- |
4. WassersteinGenerativeAdversarialNetworkwithGradient
|     |     |     |     |     |     |     |     |     | four datasets | (A, | C, D, | and F), | and poorly | for | one dataset |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------- | ---------- | --- | ----------- |
Penalty(WGANGP):ThisapproachisaGANproposedby
(E).Finally,WGANGPhasbeentheworstapproachingener-
|     | Yale | et al | in 20208 | and | is composed |     | of a generator | and |           |      |           |     |       |              |      |
| --- | ---- | ----- | -------- | --- | ----------- | --- | -------------- | --- | --------- | ---- | --------- | --- | ----- | ------------ | ---- |
|     |      |       |          |     |             |     |                |     | ating STD | that | resembles | RD, | as it | has produced | good |
discriminator.ThegeneratorlearnstogeneratebetterSTD
|     |     |     |     |     |     |     |     |     | resemblance | for | four datasets |     | (A, B, C, | and D) | and poor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | --------- | ------ | -------- |
basedonthefeedbackreceivedbythediscriminatorand
resemblancefortheothertwodatasets(EandF).Although
usingtheWassersteindistancewithgradientpenaltyas
theoptimizationfunction.Theapproachisavailableat.63 theSTDgeneratedwiththefourapproacheshasmaintained
|     |     |     |     |     |     |     |     |     | the univariate | and | multivariate |     | resemblance | perfectly | for |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ----------- | --------- | --- |
EthicalConsiderations most of the datasets, the results from the DLA analyzes
Thisresearchhasnotinvolveddatacollectionfromhuman propose that the generated STD is easily distinguishable
subjects.Useddataisopen-sourcedata. from RD for all approaches and all datasets, except GM.
ThisapproachhasobtainedthebestresultforDLAanalysis.
Despitethepoorresemblancefortwodatasets(EandF),
Results
applyingtheproposedmetricsandmethodsforresemblance
Using the datasets and STDG approaches described in the evaluationcanassurethatresemblancehasbeenmaintained
previoussections,themetricsandmethodsproposedforSTD formostofthedatasetsusingthefourSTDGapproaches.
|     | evaluation | in        | the resemblance, |     | utility, | and | privacy   | dimen- |                   |     |     |     |     |     |     |
| --- | ---------- | --------- | ---------------- | --- | -------- | --- | --------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- |
|     | sions      | have been | applied          | to  | evaluate | the | generated | STD to | UtilityEvaluation |     |     |     |     |     |     |
evidenceandprovidetrustintheirefficiencyandusability. Theresultsfromtheutilityevaluationforeachdatasetand
Additionally, comparison and benchmarking of the STDG STDGapproachareshownin►Table3.Theutilityhasbeen
approaches have been performed based on the proposed perfectlymaintainedacrossallapproachesforonlyDatasetA
sincethedifferenceintheclassificationmetricswhenTRTR
strategyforSTDevaluation.
In the following subsections, the results obtained after andTSTRarelowerthan0.2inallcases.ForDatasetB,only
applyingthedefinedweightingcriteriaforeachdimension withSDVadifferenceinclassificationmetricshigherthan0.2
areexplainedperdataset.Adetailedandcompletedescrip- hasbeenobtained,categorizingthismodelashaving“Good”
|     | MethodsofInformationinMedicine |     |     |     | Vol.62 | No.S1/2023 | ©2023.TheAuthor(s). |     |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | ------ | ---------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     | Synthetic | Tabular | Data Evaluation | Hernadezet | al. e29 |
| --- | --- | --- | --------- | ------- | --------------- | ---------- | ------- |
Table 2 Resultsoftheresemblanceevaluationforeachdataset
DataID STDGapproaches URA(40%) MRA(40%) DLA(20%) TotalResemblance
| A   | GM     | (3)Excellent | (3)Excellent |     | (2)Good      | (3)Excellent |     |
| --- | ------ | ------------ | ------------ | --- | ------------ | ------------ | --- |
|     | SDV    | (2)Good      | (3)Excellent |     | (1)Poor      | (2)Good      |     |
|     | CTGAN  | (2)Good      | (3)Excellent |     | (2)Good      | (2)Good      |     |
|     | WGANGP | (1)Poor      | (2)Good      |     | (2)Good      | (2)Good      |     |
| B   | GM     | (3)Excellent | (3)Excellent |     | (2)Good      | (3)Excellent |     |
|     | SDV    | (2)Good      | (3)Excellent |     | (2)Good      | (2)Good      |     |
|     | CTGAN  | (2)Good      | (3)Excellent |     | (3)Excellent | (3)Excellent |     |
|     | WGANGP | (2)Good      | (2)Good      |     | (1)Poor      | (2)Good      |     |
| C   | GM     | (3)Excellent | (3)Excellent |     | (1)Poor      | (3)Excellent |     |
|     | SDV    | (3)Excellent | (3)Excellent |     | (1)Poor      | (3)Excellent |     |
|     | CTGAN  | (2)Good      | (3)Excellent |     | (1)Poor      | (2)Good      |     |
|     | WGANGP | (2)Good      | (2)Good      |     | (1)Poor      | (2)Good      |     |
| D   | GM     | (2)Good      | (3)Excellent |     | (3)Excellent | (3)Excellent |     |
|     | SDV    | (2)Good      | (3)Excellent |     | (2)Good      | (2)Good      |     |
|     | CTGAN  | (2)Good      | (1)Poor      |     | (2)Good      | (2)Good      |     |
|     | WGANGP | (2)Good      | (3)Excellent |     | (1)Poor      | (2)Good      |     |
| E   | GM     | (3)Excellent | (3)Excellent |     | (2)Good      | (3)Excellent |     |
|     | SDV    | (3)Excellent | (3)Excellent |     | (2)Good      | (3)Excellent |     |
|     | CTGAN  | (2)Good      | (1)Poor      |     | (1)Poor      | (1)Poor      |     |
|     | WGANGP | (2)Good      | (1)Poor      |     | (1)Poor      | (1)Poor      |     |
| F   | GM     | (3)Excellent | (2)Good      |     | (3)Excellent | (3)Excellent |     |
|     | SDV    | (3)Excellent | (3)Excellent |     | (1)Poor      | (3)Excellent |     |
|     | CTGAN  | (2)Good      | (2)Good      |     | (2)Good      | (2)Good      |     |
|     | WGANGP | (2)Good      | (1)Poor      |     | (1)Poor      | (1)Poor      |     |
Table 3 Resultsoftheutilityevaluationforeachdataset
DataID STDGapproaches Acc.diff. Prec.diff. Rec.diff. F1diff. Utilityscore
| A   | GM     | 0.05 | 0.05 | 0.05 | 0.05 | (3)Excellent |     |
| --- | ------ | ---- | ---- | ---- | ---- | ------------ | --- |
|     | SDV    | 0.05 | 0.10 | 0.05 | 0.10 | (3)Excellent |     |
|     | CTGAN  | 0.05 | 0.05 | 0.05 | 0.10 | (3)Excellent |     |
|     | WGANGP | 0.15 | 0.10 | 0.10 | 0.10 | (3)Excellent |     |
| B   | GM     | 0.05 | 0.10 | 0.05 | 0.15 | (3)Excellent |     |
|     | SDV    | 0.20 | 0.20 | 0.20 | 0.40 | (2)Good      |     |
|     | CTGAN  | 0.10 | 0.05 | 0.10 | 0.15 | (3)Excellent |     |
|     | WGANGP | 0.20 | 0.20 | 0.15 | 0.20 | (3)Excellent |     |
| C   | GM     | 0.60 | 0.60 | 0.60 | 0.60 | (2)Good      |     |
|     | SDV    | 0.80 | 0.75 | 0.75 | 0.75 | (2)Good      |     |
|     | CTGAN  | 0.90 | 0.85 | 0.90 | 0.90 | (1)Poor      |     |
|     | WGANGP | 0.60 | 0.60 | 0.65 | 0.70 | (2)Good      |     |
| D   | GM     | 0.15 | 0.10 | 0.10 | 0.15 | (3)Excellent |     |
|     | SDV    | 0.15 | 0.20 | 0.20 | 0.25 | (2)Good      |     |
|     | CTGAN  | 0.15 | 0.15 | 0.15 | 0.15 | (3)Excellent |     |
|     | WGANGP | 0.15 | 0.20 | 0.15 | 0.25 | (2)Good      |     |
| E   | GM     | 0.20 | 0.20 | 0.20 | 0.20 | (2)Good      |     |
|     | SDV    | 0.05 | 0.05 | 0.05 | 0.10 | (3)Excellent |     |
|     | CTGAN  | 0.35 | 0.25 | 0.35 | 0.40 | (2)Good      |     |
|     | WGANGP | 0.25 | 0.20 | 0.25 | 0.25 | (2)Good      |     |
| F   | GM     | 0.25 | 0.15 | 0.30 | 0.30 | (2)Good      |     |
|     | SDV    | 0.35 | 0.20 | 0.40 | 0.40 | (2)Good      |     |
|     | CTGAN  | 0.20 | 0.20 | 0.20 | 0.20 | (2)Good      |     |
|     | WGANGP | 0.40 | 0.25 | 0.35 | 0.40 | (2)Good      |     |
Note:ThefirstandsecondcolumnsrefertothedatasetandSTDGapproach.Thethirdtosixthcolumnsindicatethemaximumdifferenceinthe
classificationmetricwhenTRTRandTSTR.Thelastcolumnindicatesthefinalutilitycategorizationbasedonthemetricsdifferencesandapplyinga
thresholdof0.2foran“Excellent”categorization.
|     |     |     | MethodsofInformationinMedicine |     | Vol.62 No.S1/2023 | ©2023.TheAuthor(s). |     |
| --- | --- | --- | ------------------------------ | --- | ----------------- | ------------------- | --- |

| e30 Synthetic | Tabular Data | Evaluation | Hernadez | et al. |     |     |     |     |     |
| ------------- | ------------ | ---------- | -------- | ------ | --- | --- | --- | --- | --- |
performanceandtheotheras“Excellent.”FordatasetC,the STDismorepronetore-identificationintermsofattributes
utility of the STD is poor for CTGAN, which have obtained ratherthanmembership.
metrics differences higher than 0.8, while for the other Applying the proposed privacy dimension evaluation
approaches(GM,SDV,andWGANGP),utilityhasbeenmain- metrics and methods shows that the STD generated with
tained but not perfectly, with metrics values differences GM has yielded better privacy preservation than for other
between 0.6 and 0.8. For Dataset D, GM and CTGAN have approaches. However, privacy is still preserved quite well
performedperfectly(classificationmetricsdifferencelower withtheotherapproaches,offeringbetter preservationfor
than0.2)whileSDVandWGANGPhavebeencategorizedas certaindatasetsandSTDGapproachcombinations.
“Good”(classificationmetricshigherthan0.2andlowerthan
0.8).ForDatasetE,onlySDVhasbeenscoredas“Excellent,”
ResultsSummary
whilethe others are “Good.” Finally, fordataset F, since all The categorizations made for each dataset and STDG
classificationmetricsarehigherthan0.2butlowerthan0.8, approach combination as a result of applying the proposed
thefourSTDGapproacheshavebeencategorizedas“Good” metricsandmethodsaredescribedineachsubsection.Since
fortheutilitydimension. givingequalweightstothethreedimensionscouldundervalue
Using the proposed methods and threshold for utility theothers,threedifferentweightingscenariosareproposedto
evaluation,theseresultsshowthattheutilityofSTDhasbeen computethefinalperformancescoreforeachSTDGapproach
maintainedinallcasesexceptfordataset(C). perdataset.ThesescenarioshavebeeninspiredbyElEmam
al.64
|                   |     |     |     |     | et Next,                             | each weighting | scenario | is presented, | and the |
| ----------------- | --- | --- | --- | --- | ------------------------------------ | -------------- | -------- | ------------- | ------- |
| PrivacyEvaluation |     |     |     |     | resultsobtainedfromthemareexplained. |                |          |               |         |
Asshownin►Table4,theprivacyofSTDhasbeenquitewell
maintainedwithGMforallthedatasets.ForSDV,privacyhas WeightingScenario1:NoPreference
beenperfectlymaintainedinthreedatasets(C,D,andF)and Forthisscenariothesameweight(33.33%)hasbeengivento
quitewellmaintainedfortheotherthree(A,B,andE).With the three evaluation dimensions (resemblance, utility, and
CTGAN, privacy has been perfectly maintained for three privacy) since there is no preference on which dimension
datasets(A,C,andF)andquitewellmaintainedfortheother shouldhavemoreimportance.
three (B, D, and E). With WGANGP, privacy has only been ►Table5showstheresultsobtainedwhenapplyingthis
perfectly maintained for two datasets (A and D) and quite weightingscenario.Fromthetableitcanbeconcludedthatit
wellmaintainedfortheotherfourdatasets(B,C,E,andF). isnotclearwhichSTDGapproachisbetteringeneral(across
Regarding the RIRA, the MIA has yielded better results all datasets), using the evaluation metrics defined and the
Thisfinding
than the AIA for most cases. indicates that for appliedweights.However,itispossibletodeterminethebest
most of the dataset and STDG approach combinations, the STDG approach(es) for each application (i.e., dataset). GM
| Table | 4 Resultsoftheprivacyevaluationforeachdataset |     |     |     |     |     |     |     |     |
| ----- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
DataID STDGapproaches SEA (40%) MIA(30%) AIA(30%) Totalresemblance
| A                              | GM     |                   | (1)Poor             |     | (3)Excellent | (3)Excellent |     | (2)Good      |     |
| ------------------------------ | ------ | ----------------- | ------------------- | --- | ------------ | ------------ | --- | ------------ | --- |
|                                | SDV    |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | WGANGP |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
| B                              | GM     |                   | (1)Poor             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | SDV    |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | WGANGP |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
| C                              | GM     |                   | (2)Good             |     | (2)Good      | (3)Excellent |     | (2)Good      |     |
|                                | SDV    |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | WGANGP |                   | (2)Good             |     | (2)Good      | (3)Excellent |     | (2)Good      |     |
| D                              | GM     |                   | (2)Good             |     | (3)Excellent | (2)Good      |     | (2)Good      |     |
|                                | SDV    |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (2)Good      |     | (2)Good      |     |
|                                | WGANGP |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
| E                              | GM     |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | SDV    |                   | (2)Good             |     | (2)Good      | (1)Poor      |     | (2)Good      |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (1)Poor      |     | (2)Good      |     |
|                                | WGANGP |                   | (2)Good             |     | (2)Good      | (1)Poor      |     | (2)Good      |     |
| F                              | GM     |                   | (2)Good             |     | (2)Good      | (3)Excellent |     | (2)Good      |     |
|                                | SDV    |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | CTGAN  |                   | (2)Good             |     | (3)Excellent | (3)Excellent |     | (3)Excellent |     |
|                                | WGANGP |                   | (2)Good             |     | (2)Good      | (3)Excellent |     | (2)Good      |     |
| MethodsofInformationinMedicine |        | Vol.62 No.S1/2023 | ©2023.TheAuthor(s). |     |              |              |     |              |     |

|     |     |     |     |     |     |     |     | Synthetic | Tabular | Data | Evaluation | Hernadezet | al. e31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | ---------- | ---------- | ------- |
Table 5 Overall results of the STD evaluation for all datasets and STDG approaches combination when applying Weighting
Scenario1(nopreferenceonwhichdimensionismoreimportant)
ID Datashape STDGappr. Resemblance(33.33%) Utility(33.33%) Privacy(33.33%) Finalscore
GM(cid:2)
A Records:101,766 (3)Excellent (3)Excellent (2)Good (3)Excellent
|     | Attributes:20 |     | SDV |     | (2)Good |     |     | (3)Excellent |     |     | (2)Good | (2)Good |     |
| --- | ------------- | --- | --- | --- | ------- | --- | --- | ------------ | --- | --- | ------- | ------- | --- |
CTGAN(cid:2)
|     |     |     |     |     | (2)Good |     |     | (3)Excellent |     |     | (3)Excellent | (3)Excellent |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | ------------ | --- | --- | ------------ | ------------ | --- |
WGANGP(cid:2)
|     |     |     |     |     | (2)Good |     |     | (3)Excellent |     |     | (3)Excellent | (3)Excellent |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | ------------ | --- | --- | ------------ | ------------ | --- |
GM(cid:2)
B Records:70,000 (3)Excellent (3)Excellent (2)Good (3)Excellent
|     | Attributes:13 |     | SDV |     | (2)Good |     |     | (2)Good |     |     | (2)Good | (2)Good |     |
| --- | ------------- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- | ------- | ------- | --- |
CTGAN(cid:2)
|     |               |     |        |     | (3)Excellent |     |     | (3)Excellent |     |     | (2)Good | (3)Excellent |     |
| --- | ------------- | --- | ------ | --- | ------------ | --- | --- | ------------ | --- | --- | ------- | ------------ | --- |
|     |               |     | WGANGP |     | (2)Good      |     |     | (3)Excellent |     |     | (2)Good | (2)Good      |     |
| C   | Records:2,111 |     | GM     |     | (3)Excellent |     |     | (2)Good      |     |     | (2)Good | (2)Good      |     |
SDV(cid:2)
|     | Attributes:17 |     |        |     | (3)Excellent |     |     | (2)Good |     |     | (3)Excellent | (3)Excellent |     |
| --- | ------------- | --- | ------ | --- | ------------ | --- | --- | ------- | --- | --- | ------------ | ------------ | --- |
|     |               |     | CTGAN  |     | (2)Good      |     |     | (1)Poor |     |     | (3)Excellent | (2)Good      |     |
|     |               |     | WGANGP |     | (2)Good      |     |     | (2)Good |     |     | (2)Good      | (2)Good      |     |
GM(cid:2)
D Records:1,473 (3)Excellent (3)Excellent (2)Good (3)Excellent
|     | Attributes:10 |     | SDV   |     | (2)Good |     |     | (2)Good      |     |     | (3)Excellent | (2)Good |     |
| --- | ------------- | --- | ----- | --- | ------- | --- | --- | ------------ | --- | --- | ------------ | ------- | --- |
|     |               |     | CTGAN |     | (2)Good |     |     | (3)Excellent |     |     | (2)Good      | (2)Good |     |
WGANGP(cid:2)
|     |             |     |     |     | (2)Good      |     |     | (2)Good |     |     | (3)Excellent | (2)Good |     |
| --- | ----------- | --- | --- | --- | ------------ | --- | --- | ------- | --- | --- | ------------ | ------- | --- |
| E   | Records:769 |     | GM  |     | (3)Excellent |     |     | (2)Good |     |     | (2)Good      | (2)Good |     |
SDV(cid:2)
|     | Attributes:9 |     |        |     | (3)Excellent |     |     | (3)Excellent |     |     | (2)Good | (3)Excellent |     |
| --- | ------------ | --- | ------ | --- | ------------ | --- | --- | ------------ | --- | --- | ------- | ------------ | --- |
|     |              |     | CTGAN  |     | (1)Poor      |     |     | (2)Good      |     |     | (2)Good | (2)Good      |     |
|     |              |     | WGANGP |     | (1)Poor      |     |     | (2)Good      |     |     | (2)Good | (2)Good      |     |
| F   | Records:583  |     | GM     |     | (3)Excellent |     |     | (2)Good      |     |     | (2)Good | (2)Good      |     |
SDV(cid:2)
|     | Attributes:11 |     |        |     | (3)Excellent |     |     | (2)Good |     |     | (3)Excellent | (3)Excellent |     |
| --- | ------------- | --- | ------ | --- | ------------ | --- | --- | ------- | --- | --- | ------------ | ------------ | --- |
|     |               |     | CTGAN  |     | (2)Good      |     |     | (2)Good |     |     | (3)Excellent | (2)Good      |     |
|     |               |     | WGANGP |     | (1)Poor      |     |     | (2)Good |     |     | (2)Good      | (2)Good      |     |
Note:TheSTDGapproachesthatyieldedan“Excellent”scorearemarkedwith(cid:2).
“Excellent”
and SDV scored for three datasets, CTGAN for thisscenario,privacyisthedimensionthathasleastimpor-
only two and WGANGP for onlyone dataset. This suggests tance and utility is the one with the most importance.
thatGMandSDVhavegiventhebestoverallresultsfromthe However,ahighlevelofsignificanceshouldbegiventothe
chosenSTDGapproachesanddatasetswhenapplyingequal resemblanceevaluation.Theappliedweightsforthisscenar-
weightstothethreedimensions. ioareasfollows:30%toresemblance,60%toutility,and10%
toprivacy.
WeightingScenario2:ExternalSoftwareCompany ►Table7showstheresultsobtainedwhenapplyingthis
Inthisweightingscenariothatmightbeusedbyanexternal weighting scenario. Using the evaluation metrics defined
softwarecompanyforsoftware andSTDGapproaches vali- andtheappliedweightstheresultshavechangedalotfrom
dation,moreimportanceshouldbegiventoresemblanceand the previous scenarios. GM, CTGAN, and WGANGP scored
Specifically, “Excellent”forthreedatasetswhileSDVonlyforonedataset.
| privacy | than | to utility. |     | due | to privacy | guaran- |     |     |     |     |     |     |     |
| ------- | ---- | ----------- | --- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tees,thedimensionthatshouldhavemoreimportanceinthis Apartfromthat,therearetwodatasetsinwhichnoneofthe
scenario is privacy. Therefore, the applied weights for this fourSTDGapproacheshaveyieldedan“Excellent”score.This
scenarioarethefollowing:40%toresemblance,10%toutility, suggeststhatGM,CTGAN,andWGANGPhavegiventhebest
and50%toprivacy. overallresultsfromthechosenSTDGapproachesanddata-
►Table
6 shows the resultsobtainedwhenapplyingthis setswhengivingmoreimportancetoutilityandlessimpor-
weightingscenario.Usingtheevaluationmetricsdefinedand tancetoprivacy.Additionally,inthisspecificcase,forcertain
theappliedweightstheresultsarequitesimilartotheprevious datasetsanoptimalscorehasnotbeenobtained.
| weighting |     | scenario except | for | a few differences. |     | SDV scored |     |     |     |     |     |     |     |
| --------- | --- | --------------- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
“Excellent”forfourdatasets,GMandCTGANforthreedatasets,
Discussion
andWGANGPforonlytwodatasets.ThissuggeststhatSDVhas
| given | the | best overall | results | from | the chosen | STDG | PrincipalResults |     |     |     |     |     |     |
| ----- | --- | ------------ | ------- | ---- | ---------- | ---- | ---------------- | --- | --- | --- | --- | --- | --- |
approaches and datasets when giving more importance to Overall, the results haveshownthat theproposed pipeline
privacyandresemblanceandlessimportancetoutility. forSTDevaluationinthethreedimensionsdefined(resem-
|     |     |     |     |     |     |     | blance, | utility, | and | privacy) | can be | used to assess | and |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | -------- | ------ | -------------- | --- |
WeightingScenario3:InternalOrganizationwith benchmark STD generated with different approaches and
SecurityMeasures applying different weighting scenarios according to which
Thisweightingscenariomightbeusedbyaninternalorga- dimensiontheresearcherswanttoprioritize.Contrarytothe
evaluationframeworksproposedbyDankaretal,41Hittmeir
| nization |     | that implements | security | measures. | Therefore, | in  |                                |     |     |     |                   |                     |     |
| -------- | --- | --------------- | -------- | --------- | ---------- | --- | ------------------------------ | --- | --- | --- | ----------------- | ------------------- | --- |
|          |     |                 |          |           |            |     | MethodsofInformationinMedicine |     |     |     | Vol.62 No.S1/2023 | ©2023.TheAuthor(s). |     |

| e32 | Synthetic | Tabular Data | Evaluation | Hernadez | et al. |     |     |     |
| --- | --------- | ------------ | ---------- | -------- | ------ | --- | --- | --- |
Table 6 Overall results of the STD evaluation for all datasets and STDG approaches combination when applying Weighting
Scenario2(privacythemostimportantdimensionandutilitytheleast)
ID Datashape STDGappr. Resemblance(40%) Utility(10%) Privacy(50%) Finalscore
GM(cid:2)
A Records:101,766 (3)Excellent (3)Excellent (2)Good (3)Excellent
|     |     | Attributes:20 | SDV |     | (2)Good | (3)Excellent | (2)Good | (2)Good |
| --- | --- | ------------- | --- | --- | ------- | ------------ | ------- | ------- |
CTGAN(cid:2)
|     |     |     |     |     | (2)Good | (3)Excellent | (3)Excellent | (3)Excellent |
| --- | --- | --- | --- | --- | ------- | ------------ | ------------ | ------------ |
WGANGP(cid:2)
|     |     |     |     |     | (2)Good | (3)Excellent | (3)Excellent | (3)Excellent |
| --- | --- | --- | --- | --- | ------- | ------------ | ------------ | ------------ |
GM(cid:2)
B Records:70,000 (3)Excellent (3)Excellent (2)Good (3)Excellent
|     |     | Attributes:13 | SDV |     | (2)Good | (2)Good | (2)Good | (2)Good |
| --- | --- | ------------- | --- | --- | ------- | ------- | ------- | ------- |
CTGAN(cid:2)
|     |     |               |        |     | (3)Excellent | (3)Excellent | (2)Good | (3)Excellent |
| --- | --- | ------------- | ------ | --- | ------------ | ------------ | ------- | ------------ |
|     |     |               | WGANGP |     | (2)Good      | (3)Excellent | (2)Good | (2)Good      |
|     | C   | Records:2,111 | GM     |     | (3)Excellent | (2)Good      | (2)Good | (2)Good      |
SDV(cid:2)
|     |     | Attributes:17 |        |     | (3)Excellent | (2)Good | (3)Excellent | (3)Excellent |
| --- | --- | ------------- | ------ | --- | ------------ | ------- | ------------ | ------------ |
|     |     |               | CTGAN  |     | (2)Good      | (1)Poor | (3)Excellent | (2)Good      |
|     |     |               | WGANGP |     | (2)Good      | (2)Good | (2)Good      | (2)Good      |
GM(cid:2)
D Records:1,473 (3)Excellent (3)Excellent (2)Good (3)Excellent
SDV(cid:2)
|     |     | Attributes:10 |       |     | (2)Good | (2)Good      | (3)Excellent | (3)Excellent |
| --- | --- | ------------- | ----- | --- | ------- | ------------ | ------------ | ------------ |
|     |     |               | CTGAN |     | (2)Good | (3)Excellent | (2)Good      | (2)Good      |
WGANGP(cid:2)
|     |     |             |     |     | (2)Good      | (2)Good | (3)Excellent | (3)Excellent |
| --- | --- | ----------- | --- | --- | ------------ | ------- | ------------ | ------------ |
|     | E   | Records:769 | GM  |     | (3)Excellent | (2)Good | (2)Good      | (2)Good      |
SDV(cid:2)
|     |     | Attributes:9 |        |     | (3)Excellent | (3)Excellent | (2)Good | (3)Excellent |
| --- | --- | ------------ | ------ | --- | ------------ | ------------ | ------- | ------------ |
|     |     |              | CTGAN  |     | (1)Poor      | (2)Good      | (2)Good | (2)Good      |
|     |     |              | WGANGP |     | (1)Poor      | (2)Good      | (2)Good | (2)Good      |
|     | F   | Records:583  | GM     |     | (3)Excellent | (2)Good      | (2)Good | (2)Good      |
SDV(cid:2)
|     |     | Attributes:11 |     |     | (3)Excellent | (2)Good | (3)Excellent | (3)Excellent |
| --- | --- | ------------- | --- | --- | ------------ | ------- | ------------ | ------------ |
CTGAN(cid:2)
|     |     |     |        |     | (2)Good | (2)Good | (3)Excellent | (3)Excellent |
| --- | --- | --- | ------ | --- | ------- | ------- | ------------ | ------------ |
|     |     |     | WGANGP |     | (1)Poor | (2)Good | (2)Good      | (2)Good      |
Note:TheSTDGapproachesthatyieldedan“Excellent”scorearemarkedwith(cid:2).
Table 7 Overall results of the STD evaluation for all datasets and STDG approaches combination when applying Weighting
Scenario3(preferenceonutility,resemblancealsoimportant,butprivacynotimportant)
ID Datashape STDGappr. Resemblance(30%) Utility(60%) Privacy(10%) Finalscore
A Records:101,766 GM(cid:2) (3)Excellent (3)Excellent (2)Good (3)Excellent
Attributes:20 SDV(cid:2) (2)Good (3)Excellent (2)Good (3)Excellent
|     |     |     | CTGAN(cid:2)  |     | (2)Good | (3)Excellent | (3)Excellent | (3)Excellent |
| --- | --- | --- | ------------- | --- | ------- | ------------ | ------------ | ------------ |
|     |     |     | WGANGP(cid:2) |     | (2)Good | (3)Excellent | (3)Excellent | (3)Excellent |
B Records:70,000 GM(cid:2) (3)Excellent (3)Excellent (2)Good (3)Excellent
|     |     | Attributes:13 | SDV           |     | (2)Good      | (2)Good      | (2)Good      | (2)Good      |
| --- | --- | ------------- | ------------- | --- | ------------ | ------------ | ------------ | ------------ |
|     |     |               | CTGAN(cid:2)  |     | (3)Excellent | (3)Excellent | (2)Good      | (3)Excellent |
|     |     |               | WGANGP(cid:2) |     | (2)Good      | (3)Excellent | (2)Good      | (3)Excellent |
|     | C   | Records:2,111 | GM            |     | (3)Excellent | (2)Good      | (2)Good      | (2)Good      |
|     |     | Attributes:17 | SDV           |     | (3)Excellent | (2)Good      | (3)Excellent | (2)Good      |
|     |     |               | CTGAN         |     | (2)Good      | (1)Poor      | (3)Excellent | (2)Good      |
|     |     |               | WGANGP        |     | (2)Good      | (2)Good      | (2)Good      | (2)Good      |
D Records:1,473 GM(cid:2) (3)Excellent (3)Excellent (2)Good (3)Excellent
|     |     | Attributes:10 | SDV           |     | (2)Good      | (2)Good      | (3)Excellent | (2)Good      |
| --- | --- | ------------- | ------------- | --- | ------------ | ------------ | ------------ | ------------ |
|     |     |               | CTGAN(cid:2)  |     | (2)Good      | (3)Excellent | (2)Good      | (3)Excellent |
|     |     |               | WGANGP(cid:2) |     | (2)Good      | (2)Good      | (3)Excellent | (2)Good      |
|     | E   | Records:769   | GM            |     | (3)Excellent | (2)Good      | (2)Good      | (2)Good      |
Attributes:9 SDV(cid:2) (3)Excellent (3)Excellent (2)Good (3)Excellent
|     |     |               | CTGAN  |     | (1)Poor      | (2)Good | (2)Good      | (2)Good |
| --- | --- | ------------- | ------ | --- | ------------ | ------- | ------------ | ------- |
|     |     |               | WGANGP |     | (1)Poor      | (2)Good | (2)Good      | (2)Good |
|     | F   | Records:583   | GM     |     | (3)Excellent | (2)Good | (2)Good      | (2)Good |
|     |     | Attributes:11 | SDV    |     | (3)Excellent | (2)Good | (3)Excellent | (2)Good |
|     |     |               | CTGAN  |     | (2)Good      | (2)Good | (3)Excellent | (2)Good |
|     |     |               | WGANGP |     | (1)Poor      | (2)Good | (2)Good      | (2)Good |
Note:TheSTDGapproachesthatyieldedan“Excellent”scorearemarkedwith(cid:2).
|     | MethodsofInformationinMedicine |     | Vol.62 No.S1/2023 |     | ©2023.TheAuthor(s). |     |     |     |
| --- | ------------------------------ | --- | ----------------- | --- | ------------------- | --- | --- | --- |

Synthetic Tabular Data Evaluation Hernadezet al. e33
etal,39andPlatzerandReutterer,43ourpipelinehascovered PrivacyEvaluation
andevaluatedallthreedimensionsidentifiedasrelevantfor RegardingtheprivacyofSTD,thesimilaritybetweenSTDand
ensuring the delivery of high-quality STD in the health RDhasfirstbeenevaluatedintheSEA,andthenapairofdata
domain as well as giving the option to tune the weighting inferenceattacks(MIAandAIA)havebeensimulatedinthe
methodologyaccordingtothedesiredoutput.Additionally, RIRA analysis. Although these simulations have not been
theproposedcategorizationstrategyisusefulforcomparing quitesignificant,theycouldbeusefultoestimatethequan-
different STDG approaches to select the best ones and tificationofthere-identificationriskofSTD.However,these
evaluatingthequalityofSTDgeneratedbyoneapproach. metricsandmethodsmustbeimprovedtoquantifythere-
NoneoftheSTDGapproacheshavebeenbetteracrossall identification risk of STD more reliably. Thus, future work
STDdimensionsconsideredintheexperimentsdescribedfor mightincludedefiningastrategythathelpsidentifywhich
thethreeproposedweightingscenarios.Therefore,itcanbe attributesaremorepronetore-identificationandconsiders
said that it is difficult to get a trade-off between resem- therealconsequencesofpotentialpersonaldatadisclosure.
blance,privacy,andutilityscores.However,thecategoriza-
tion system provided and the per dimension score WeightingScenariosforOverallScore
calculation and overall score calculation can help select Regardingthethreeproposedweightingscenariostoobtain
the most appropriate STDG approaches by looking at indi- an overall score for the four STDG approaches per dataset,
vidual scores and configuring overall scores by computing similarresultshavebeenobtainedforthefirsttwoscenarios
weights according to priorities defined for each specific (giving equal weights and prioritizing privacy over resem-
application. blanceandutility).Fortheproposedthirdweightingscenar-
io (prioritizing utility over resemblance and privacy), the
ResemblanceEvaluation results have changed a lot, yielding no “Excellent” STDG
Differentmetricsandmethodshavebeenproposedtoeval- approach for two datasets. Apart from that, in the first
uatethe resemblance of STDatdifferent levels: univariate, scenario GM and SDV were the best approaches while in
multivariate, dimensional, and semantics. Among the met- thesecondscenarioitwasSDV.Inthethirdscenariothebest
rics used in URA, statistical tests and distance calculations approaches were GM, CTGAN and WGANGP. From these
provide quantitative results, which have been more trust- resultsitcanbeconcludedthatSDVisagoodapproachfor
worthy in assessing how well STD attributes resemble RD privacypreservation,whiletheotherthree(GM,CTGANand
thanvisualcomparisonsoftheattributedistributions,which WGANGP)haveperformedbetterforutilitypreservation.
provide a more qualitative view. MRA has appeared to be
useful in analyzing the multivariate relationships between LimitationsandFutureWork
attributes and how well these are maintained in STD. Al- Although the proposed STD evaluation pipeline has been
thoughDRAhasnotbeenincludedinthetotalresemblance used to evaluate STD generated with different approaches
calculation due to the difficulty in interpreting the results andcontexts,thedatasetsusedfortheevaluationhavebeen
obtained, it can be useful in illustrating how well the limitedduetothelackofqualityhealth-relatedopen-source
dimensional properties of RDare preserved. DLA has been datasets.Fromthesixdatasetsselected,onlytwo(AandB)
lesseffectiveduetothelackofmedicalspecialiststoquali- comprisedanappropriatenumberof recordstobe consid-
tativelyevaluatethegenerateddata’ssignificance.However, ered representative of real health-related data, with the
theanalysiscomposedofdifferentMLmodelstrainedtolabel remaining four containing a limited number of entries.
records as real or synthetic has simplified this process, Moreover, these open-source datasets might have been
approximating how a medical expert would label the anonymized or synthesized before, inducing new bias in
records. STD and analysis. Therefore, further work is required to
judge and benchmark the proposed pipeline with more
UtilityEvaluation datasetsinothercontextsandRDthatcomesdirectlyfrom
TRTRandTSTRmethodshavebeenproposedintermsofthe hospitalsorlaboratorieswithoutanyanonymizationorother
utilitydimension,whereafewMLclassificationmodelshave modificationprocessesappliedtothedata.Apartfromthat,
beentrainedwith RDand separatelywith STD. This meth- different weighting scenarios should be tested when com-
odology has been very useful in evaluating whether STD puting the final score that considers the three defined
couldbeusedinsteadofRDfordatamodeling.Furtherwork dimensions and also weighting of each of the metrics and
inthisarea mayincludetryingandvalidatingdifferentML methods categorized in each dimension. Furthermore, the
modelstoselectthebestonesforthespecificapplicationand proposed methodology for STD and the results obtained
using mixed data for model training in contrast to the must be compared with the methodologies other authors
separateuseofRDorSTD.Furthermore,otherdatamodeling followedtoevaluateSTDquality.
taskscanbeproposedtoassesstheutilityofSTDinthesame Anotherimportantfindingfromthisworkisthelackofa
way, e.g., regression or clustering. Additionally, statistical trade-offbetweentheresemblance,utility,andprivacydimen-
tests can be applied to analyze if the classification metrics sionsinSTDgeneratedwithdifferentapproachesintheevalu-
differencesarestatisticallysignificantsothecategorization ation section. Thus, further work on improving the STDG
into “Excellent”; “Good” and “Poor” performance can be approaches to generate more quality STD that maintains an
madebasedontheresultsofthesestatisticaltests. appropriatetrade-offbetweenthesedimensionsisrequired.
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

| e34 | Synthetic | Tabular   | Data         | Evaluation |            | Hernadez |          | et al.   |         |     |     |     |     |     |     |
| --- | --------- | --------- | ------------ | ---------- | ---------- | -------- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
|     | In        | addition, | the proposed |            | evaluation |          | pipeline | has been | Funding |     |     |     |     |     |     |
centered on the resemblance, utility, and privacy dimen- ThisresearchwaspartiallyfundedbytheDepartmentof
sions, which are the most commonly used dimensions for EconomicDevelopmentandInfrastructureoftheBasque
evaluating the quality of STD for targeted health domain Government through Emaitek Plus Action Plan
|     | applications |     | found | in the literature. |     | Several | metrics | and | Programme. |     |     |     |     |     |     |
| --- | ------------ | --- | ----- | ------------------ | --- | ------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
methodsshouldalsobeproposedanddevelopedaspartof AneAlberdiispartoftheIntelligentSystemsforIndustrial
futureworktoevaluatetheperformanceofSTDGapproaches Systems research group of Mondragon Unibertsitatea
in terms of other dimensions, such as cost (computational (IT1676-22),supportedbytheDepartmentofEducation,
resources, training time, and footprint) or diversity (How UniversitiesandResearchoftheBasqueCountry.
|     | diverse                                           | is the   | generated    | STD? | Is it   | biased | to any  | minority |                    |     |     |     |     |     |     |
| --- | ------------------------------------------------- | -------- | ------------ | ---- | ------- | ------ | ------- | -------- | ------------------ | --- | --- | --- | --- | --- | --- |
|     | class?).                                          |          |              |      |         |        |         |          | ConflictofInterest |     |     |     |     |     |     |
|     | Furthermore,anonlinetoolkitorlibrarycouldbedevel- |          |              |      |         |        |         |          | Nonedeclared.      |     |     |     |     |     |     |
|     | oped                                              | to unify | the proposed |      | metrics | and    | methods | to help  |                    |     |     |     |     |     |     |
researcherswhoworkonSTDGevaluatethegeneratedSTD.
References
|     | This tool | could | help       | them | focus   | more      | on improving | or     |            |            |                                  |     |     |     |          |
| --- | --------- | ----- | ---------- | ---- | ------- | --------- | ------------ | ------ | ---------- | ---------- | -------------------------------- | --- | --- | --- | -------- |
|     |           |       |            |      |         |           |              |        | 1 RubinDB. | Discussion | statisticaldisclosurelimitation. |     |     |     | JOffStat |
|     | proposing | STDG  | approaches |      | without | investing | time         | in de- |            |            |                                  |     |     |     |          |
1993;9(02):461–468
fininganddevelopinganSTDevaluationprocess.
2 LittleRJA.StatisticalAnalysisofMaskedData.JOffStat1993;9
(02):407–426
3 ElEmamK,HoptroffR.Thesyntheticdataparadigmforusingand
Conclusion
sharingdata.DATAAnalDigitTechnol2019;19(06):12
4 HernandezM,EpeldeG,AlberdiA,CillaR,RankinD.Synthetic
|     | In this | work, | we proposed |     | a comprehensive |     | and | universal |     |     |     |     |     |     |     |
| --- | ------- | ----- | ----------- | --- | --------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
datagenerationfortabularhealthrecords:asystematicreview.
|     | STD evaluation |     | pipeline | covering | resemblance, |     | utility, | and |     |     |     |     |     |     |     |
| --- | -------------- | --- | -------- | -------- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Neurocomputing2022;493:28–45
privacy dimensions, with a methodology to categorize the 5 HuJ.Bayesianestimationofattributeandidentificationdisclo-
performance of STDG approaches across each dimension. sure risks in synthetic data. arXiv preprint arXiv:1804.02784,
2018
Additionally,weconductedanextensiveanalysisandevalu-
ReiterJP.Newapproachestodatadissemination:aglimpseinto
|     | ation | of the | proposed | STD | evaluation | pipeline |     | using six | 6   |     |     |     |     |     |     |
| --- | ----- | ------ | -------- | --- | ---------- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
thefuture.Chance2004;17(03):11–15
differenthealthcare-relatedopen-sourcedatasetsandfour
|     |     |     |     |     |     |     |     |     | Taub J, Elliot | M,  | Pampaka | M, Smith | D. Differential |     | Correct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | -------- | --------------- | --- | ------- |
7
STDGapproachestoprovetheefficiencyandveracityofthe Attribution Probability for Synthetic Data: An Exploration. In:
|     | proposed | STDevaluationpipeline. |     |     |     | Thisanalysis |     | hasshown |                              |     |     |                                |     |     |     |
| --- | -------- | ---------------------- | --- | --- | --- | ------------ | --- | -------- | ---------------------------- | --- | --- | ------------------------------ | --- | --- | --- |
|     |          |                        |     |     |     |              |     |          | Domingo-FerrerJ,MontesF,eds. |     |     | PrivacyinStatisticalDatabases. |     |     |     |
Cham:SpringerInternationalPublishing;2018:122–137
thattheproposedpipelinecanbeusedeffectivelytoevaluate
andbenchmarkdifferentapproachesforSTDG, helping the 8 YaleA,DashS,DuttaR,GuyonI,PavaoA,BennettKP.Generation
scientificcommunityselectthemostsuitableapproachesfor and evaluation of privacy preserving synthetic health data.
Neurocomputing2020;416:244–255
theirdataandapplicationofinterest.Althoughotherauthors
9 ChoiE,BiswalS,MalinB,DukeJ,StewartWF,SunJ.Generating
|     | have | proposed | metrics | or methods |     | to evaluate |     | STD, none |     |     |     |     |     |     |     |
| --- | ---- | -------- | ------- | ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
multi-labeldiscretepatientrecordsusinggenerativeadversarial
defined
have or used a complete pipeline covering the networks. Machine learning for healthcare conference 2017:
|     | resemblance, |     | utility, | and privacy | dimensions |     | in  | providing | 286–305 |     |     |     |     |     |     |
| --- | ------------ | --- | -------- | ----------- | ---------- | --- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
different weighting scenarios togeta finalscorethat indi- 10 ChawlaNV,BowyerKW,HallLO,KegelmeyerWP.SMOTE:syn-
theticminorityover-samplingtechnique.JArtifIntellRes2002;
catesthequalityofgeneratedSTD.
16:321–357
Regardingthelimitationsofthiswork,wehavefoundthat
|     |     |     |     |     |     |     |     |     | 11 HeH,BaiY,GarciaEA,LiS.ADASYN:Adaptivesyntheticsampling |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
(1) some metrics and methods are not as trustworthy as approachforimbalancedlearning. Paperpresentedat:2008IEEE
initiallyconsidered,(2)itisdifficulttofindaperfecttrade- InternationalJointConferenceonNeuralNetworks.IEEEWorld
off between STD evaluation dimensions of resemblance, CongressonComputationalIntelligence;2008:1322–1328
|     |          |     |          |                |     |             |     |           | 12 MenardiG,TorelliN.Trainingandassessingclassificationrules |       |      |           |        |              |     |
| --- | -------- | --- | -------- | -------------- | --- | ----------- | --- | --------- | ------------------------------------------------------------ | ----- | ---- | --------- | ------ | ------------ | --- |
|     | utility, | and | privacy, | (3) previously |     | synthesized |     | or anony- |                                                              |       |      |           |        |              |     |
|     |          |     |          |                |     |             |     |           | with imbalanced                                              | data. | Data | Min Knowl | Discov | 2014;28(01): |     |
mizeddatahasbeenusedand(4)thepipelinehasnotbeen
92–122
comparedwithothermethodsusedintheliteratureforSTD Yang F, Yu Z, Liang Y, et al. Grouped Correlational Generative
13
evaluation(asnosimilarproposalhasbeenidentifiedinthe Adversarial Networks for Discrete Electronic Health Records.
literature). Paperpresentedat:2019IEEEInternationalConferenceonBio-
informaticsandBiomedicine(BIBM);2019:906–913
Futureworkincludes(1)judgingandbenchmarkingthe
|     |         |              |     |     |          |              |     |      | Hernandez-Matamoros |           | A,        | Fujita H,  | Perez-Meana | H.    | A novel |
| --- | ------- | ------------ | --- | --- | -------- | ------------ | --- | ---- | ------------------- | --------- | --------- | ---------- | ----------- | ----- | ------- |
|     | metrics | andmethodsin |     | the | proposed | pipelinewith |     | more | 14                  |           |           |            |             |       |         |
|     |         |              |     |     |          |              |     |      | approach            | to create | synthetic | biomedical | signals     | using | BiRNN.  |
datasets,inothercontexts,moreweightingscenariosand InfSci2020;541:218–241
|     | with     | RD from | health | care    | authorities, | (2) | improving | the       |                                                         |         |                  |     |                   |     |       |
| --- | -------- | ------- | ------ | ------- | ------------ | --- | --------- | --------- | ------------------------------------------------------- | ------- | ---------------- | --- | ----------------- | --- | ----- |
|     |          |         |        |         |              |     |           |           | 15 AndreiniP,CianoG,BonechiS,etal.ATwo-StageGANforHigh- |         |                  |     |                   |     |       |
|     | proposed | RIRA    | in the | privacy | dimension,   |     | (3)       | proposing |                                                         |         |                  |     |                   |     |       |
|     |          |         |        |         |              |     |           |           | Resolution                                              | Retinal | Image Generation |     | and Segmentation. |     | Elec- |
newmetricsandmethodstoevaluatetheperformanceof tronics(Basel)2022;11(01):60
STDG approaches in terms of time and footprint, (4) 16 Porcu S, Floris A, Atzori L. Evaluation of Data Augmentation
TechniquesforFacialExpressionRecognitionSystems.Electronics
|     | enhancing | the | STDG | approaches | to  | improve | the | trade-off |     |     |     |     |     |     |     |
| --- | --------- | --- | ---- | ---------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
(Basel)2020;9(11):1892
betweenthedimensions,and(5)unifyingalltheproposed
|     |     |     |     |     |     |     |     |     | 17 HanC,HayashiH,RundoL,etal.GAN-basedsyntheticbrainMR |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
metricsandmethodsintoaneasy-to-useonlinetoolkitor
imagegeneration.Paperpresentedat:2018IEEE15thInternational
|     | library.                       |     |     |        |            |     |                     |     | SymposiumonBiomedicalImaging(ISBI2018);2018:734–738 |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | ------ | ---------- | --- | ------------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | MethodsofInformationinMedicine |     |     | Vol.62 | No.S1/2023 |     | ©2023.TheAuthor(s). |     |                                                     |     |     |     |     |     |     |

Synthetic Tabular Data Evaluation Hernadezet al. e35
18 StephensM,EsteparRSJ,Ruiz-CabelloJ,Arganda-CarrerasI,Macía Conference on Bioinformatics and Biomedicine (BIBM).
I,López-LinaresK.MRItoCTATranslationforPulmonaryArtery 2018:374–380
Evaluation Using CycleGANs Trained with Unpaired Data. In: 37 Dash S, Yale A, Guyon I, Bennett KP. Medical Time-Series
Petersen J, San José Estépar R, Schmidt-Richberg A, et al., eds. Data Generation Using Generative Adversarial Networks. In:
ThoracicImageAnalysis.Cham:SpringerInternationalPublish- Michalowski M, Moskovitch R, eds. Artificial Intelligence in
ing;2020:118–129 Medicine. Cham: Springer International Publishing; 2020:
19 DahmenJ,CookD.SynSys:asyntheticdatagenerationsystemfor 382–391
healthcareapplications.Sensors(Basel)2019;19(05):1181 38 Chin-CheongK,SutterT,VogtJE.GenerationofHeterogeneous
20 Li Z, Ma C, Shi X, Zhang D, Li W, Wu L. TSA-GAN: A Robust Synthetic Electronic Health Records using GANs. ETH Zurich,
GenerativeAdversarialNetworksforTimeSeriesAugmentation. InstituteforMachineLearning;2019
2021. Paper presented at: International Joint Conference on 39 HittmeirM,EkelhartA,MayerR.OntheUtilityofSyntheticData:
NeuralNetworks(IJCNN).Shenzhen,China:IEEE;2021:1–8 An Empirical Evaluation on Machine Learning Tasks. Paper
21 CheZ,ChengY,ZhaiS,SunZ,LiuY.BoostingDeepLearningRisk presentedat:Proceedingsofthe14thInternationalConference
PredictionwithGenerativeAdversarialNetworksforElectronic on Availability, Reliability and Security. Canterbury CA United
Health Records. Paper presented at: 2017 IEEE International Kingdom:ACM;2019:1–6
ConferenceonDataMining(ICDM).2017:787–792 40 Giles O, Hosseini K, Mingas G. Faking feature importance: A
22 Rankin D, Black M, Bond R, Wallace J, Mulvenna M, Epelde G. cautionary tale on the use of differentially-private synthetic
Reliabilityofsupervisedmachinelearningusingsyntheticdatain data. arXivpreprintarXiv:2203.01363,2022
healthcare:modeltopreserveprivacyfordatasharing.JMIRMed 41 DankarFK,IbrahimMK,IsmailL.Amulti-dimensionalevaluation
Inform2020;8(07):e18910 ofsyntheticdatagenerators.IEEEAccess2022;10:11147–11158
23 Hernandez M, Epelde G, Beristain A, et al. Incorporation of 42 HittmeirM,EkelhartA,MayerR.UtilityandPrivacyAssessments
synthetic data generation techniques within a controlled data ofSyntheticDataforRegressionTasks. Paperpresentedat:2019
processingworkflowinthehealthandwellbeingdomain.Elec- IEEEInternationalConferenceonBigData(BigData).2019:5763–
tronics(Basel)2022;11(05):812 5772
24 KotalA,PiplaiA,ChukkapalliSSL,JoshiA.PriveTAB:Secureand 43 Platzer M, Reutterer T. Holdout-based empirical assessment of
Privacy-PreservingsharingofTabularData. ACMIntWorkshop mixed-typesyntheticdata.FrontBigData2021;4:679939
SecurPrivAnal;2022 44 AlaaAM,vanBreugelB,SavelievE,vanderSchaarM.Howfaithful
25 BourouS,ElSaerA,VelivassakiT-H,VoulkidisA,ZahariadisT.A isyoursyntheticdata?sample-levelmetricsforevaluatingand
reviewoftabulardatasynthesisusingGANsonanIDSdataset. auditinggenerativemodels.InternationalConferenceonMachine
Information(Basel)2021;12(09):375 Learning2022:290–306
26 Piacentino E, Guarner A, Angulo C. Generating Synthetic ECGs 45 AbayNC,ZhouY,KantarciogluM,ThuraisinghamB,SweeneyL.
UsingGANsforAnonymizingHealthcareData.Electronics(Basel) Privacypreservingsyntheticdatareleaseusingdeeplearning.In:
2021;10(04):389 BerlingerioM,BonchiF,GärtnerT,HurleyN,IfrimG,eds.Machine
27 HazraD,ByunY-C.SynSigGAN:generativeadversarialnetworks LearningandKnowledgeDiscoveryinDatabases.Cham:Springer
forsyntheticbiomedicalsignalgeneration.Biology(Basel)2020;9 InternationalPublishing;2019:510–526
(12):441 46 WuH,NingY,ChakrabortyP,VreekenJ,TattiN,RamakrishnanN.
28 NorgaardS,SaeediR,SasaniK,GebremedhinAH.SyntheticSensor Generating realistic synthetic population datasets. ACM Trans
Data Generation for Health Applications: A Supervised Deep KnowlDiscovData2018;12(04):45:1–45:22
Learning Approach. Paper presented at: 2018 40th Annual 47 FowlerEE,BerglundA,SchellMJ,SellersTA,EschrichS,HeineJ.
International Conference of the IEEE Engineering in Medicine Empirically-derivedsyntheticpopulationstomitigatesmallsam-
andBiologySociety(EMBC).2018:1164–1167 plesizes.JBiomedInform2020;105:103408
29 WangZ,MylesP,TuckerA.GeneratingandEvaluatingSynthetic 48 AlqahtaniH,Kavakli-ThorneM,KumarG.Applicationsofgenera-
UK Primary Care Data: Preserving Data Utility Patient Privacy. tiveadversarialnetworks(GANs):anupdatedreview.ArchCom-
Paperpresentedat:2019IEEE32ndInternationalSymposiumon putMethodsEng2021;28(02):525–552
Computer-BasedMedicalSystems(CBMS).2019:126–131 49 XuL,SkoularidouM,Cuesta-InfanteA,VeeramachaneniK.Model-
30 Beaulieu-JonesBK,WuZS,WilliamsC,etal.Privacy-preserving ing tabular data using conditional gan. Advances in Neural
generativedeep neural networkssupportclinicaldatasharing. InformationProcessingSystems;2019:32
CircCardiovascQualOutcomes2019;12(07):e005122 50 PatkiN,WedgeR,VeeramachaneniK.TheSyntheticDataVault.
31 Wang L, Zhang W, He X. Continuous patient-centric sequence Paperpresentedat:2016IEEEInternationalConferenceonData
generationviasequentiallycoupledadversariallearning.In:LiG, ScienceandAdvancedAnalytics(DSAA).2016:399–410
YangJ,GamaJ,NatwichaiJ,TongY,eds. DatabaseSystemsfor 51 The Synthetic Data Vault. Put synthetic data to work! 2022.
AdvancedApplications.Cham:SpringerInternationalPublishing; AccessedJanuary24,2022,at:https://sdv.dev/
2019:36–52 52 SYNTHO.2022.AccessedJanuary13,2022,at:https://www.syntho.
32 Rashidian S, Wang F, Moffitt R, et al. SMOOTH-GAN: Towards ai/
Sharp and Smooth Synthetic EHR Data Generation. In: Micha- 53 TheMedkit-Learn(ing)Environment.2022.AccessedJanuary24,
lowskiM,MoskovitchR,eds. ArtificialIntelligenceinMedicine. 2022,https://github.com/vanderschaarlab/medkit-learn
Cham:SpringerInternationalPublishing;2020:37–48 54 BuildbetterdatasetsforAIwithsyntheticdata.2022.Accessed
33 YoonJ,DrumrightLN,vanderSchaarM.Anonymizationthrough January24,2022,at:https://ydata.ai
datasynthesisusinggenerativeadversarialnetworks(ADS-GAN). 55 LeeD,YuH,JiangX,etal.Generatingsequentialelectronichealth
IEEEJBiomedHealthInform2020;24(08):2378–2388 records using dual adversarial autoencoder. J Am Med Inform
34 BaowalyMK,LinC-C,LiuC-L,ChenK-T.Synthesizingelectronic Assoc2020;27(09):1411–1419
healthrecordsusingimprovedgenerativeadversarialnetworks.J 56 ParkN,MohammadiM,GordeK,JajodiaS,ParkH,KimY.Data
AmMedInformAssoc2019;26(03):228–241 synthesisbasedongenerativeadversarialnetworks.ProcVLDB
35 GoncalvesA,RayP,SoperB,StevensJ,CoyleL,SalesAP.Generation Endow2018;11(10):1071–1083
andevaluationofsyntheticpatientdata.BMCMedResMethodol 57 Mendelevitch O, Lesh MD. Fidelity and privacy of synthetic
2020;20(01):108 medicaldata. arXivpreprintarXiv:2101.08658,2021
36 Guan J, Li R, YuS, Zhang X. Generation of Synthetic Electronic 58 GhoshehG,LiJ,ZhuT.AreviewofGenerativeAdversarialNet-
MedicalRecordText. Paperpresentedat:2018IEEEInternational works for Electronic Health Records: applications, evaluation
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

| e36 | Synthetic Tabular | Data Evaluation | Hernadez | et al. |     |     |     |     |
| --- | ----------------- | --------------- | -------- | ------ | --- | --- | --- | --- |
measures and data sources. arXiv preprint arXiv:2203.07018, 65 Strack B, DeShazo JP, Gennings C, et al. Impact of HbA1c
|     | 2022 |     |     |     | measurementonhospitalreadmissionrates:analysisof70,000 |     |     |     |
| --- | ---- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
59 HernandezM,EpeldeG.SyntheticTabularDataEvaluationMet- clinical database patient records. BioMed Res Int 2014;2014;
|     | rics. 2022.AccessedJune1,2022,at:https://github.com/Vicom- |     |     |     | 781670 |     |     |     |
| --- | ---------------------------------------------------------- | --- | --- | --- | ------ | --- | --- | --- |
tech/STDG-evaluation-metrics UlianovaS.CardiovascularDiseasedataset.Kaggle2018.Accessed
66
MultivariateDistributions–Copulas0.5.0documentation. 2022. January26,2021,at:https://www.kaggle.com/sulianova/cardio-
60
|     | Accessed March | 3, 2021, at: https://sdv.dev/Copulas/tutorials/ |     |     | vascular-disease-dataset |     |     |     |
| --- | -------------- | ----------------------------------------------- | --- | --- | ------------------------ | --- | --- | --- |
03_Multivariate_Distributions.html#Gaussian-Multivariate 67 Palechor FM, Manotas AH. Dataset for estimation of obesity
PatkiN,WedgeR,VeeramachaneniK.“TheSyntheticDataVault.”
|     | 61  |     |     |     | levels based | on eating habits | and physical | condition in |
| --- | --- | --- | --- | --- | ------------ | ---------------- | ------------ | ------------ |
Paperpresentedat:2016IEEEInternationalConferenceonData individualsfromColombia,PeruandMexico.DataBrief2019;25;
2016:399–410.
|     | Science and | Advanced Analytics | (DSAA), | Doi: | 104344 |     |     |     |
| --- | ----------- | ------------------ | ------- | ---- | ------ | --- | --- | --- |
10.1109/DSAA.2016.49 68 MachineLearningRepositoryUCI.ContraceptiveMethodChoice
62 XuL,SkoularidouM,Cuesta-InfanteA,VeeramachaneniK.Model- DataSet. 2022.AccessedMarch14,2022,at:https://archive.ics.
uci.edu/ml/datasets/ContraceptiveþMethodþChoice
|     | ing tabular | data using conditional | gan. Advances | in Neural |     |     |     |     |
| --- | ----------- | ---------------------- | ------------- | --------- | --- | --- | --- | --- |
InformationProcessingSystems;2019,32 69 Pima Indians Diabetes Database. 2022. Accessed March 14,
63 Gulrajani I, Ahmed F, Arjovsky M, Dumoulin V, Courville AC. 2022, at: https://kaggle.com/uciml/pima-indians-diabetes-
|     | ImprovedtrainingofWassersteinGANs.AdvNeuralInfProcess |     |     |     | database |     |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- |
Syst2017;30:5767–5777 70 MachineLearningRepositoryUCI.ILPD(IndianLiverPatientData-
64 El Emam K, Mosquera L, Hoptroff R. Practical Synthetic Data set)DataSet.2022.AccessedMarch14,2022,at:https://archive.ics.
Generation: Balancing Privacy and the Broad Availability of uci.edu/ml/datasets/ILPDþ(IndianþLiverþPatientþDataset)
|     | Data. Ilustrated.O’ReillyMedia,Incorporated;2020 |        |                                |     |     |     |     |     |
| --- | ------------------------------------------------ | ------ | ------------------------------ | --- | --- | --- | --- | --- |
|     | MethodsofInformationinMedicine                   | Vol.62 | No.S1/2023 ©2023.TheAuthor(s). |     |     |     |     |     |

Synthetic Tabular Data Evaluation Hernadezet al. e37
AppendixA:Abbreviationslist
Abbreviation Definition
AI ArtificialIntelligence
AIA AttributeInferenceAttack
AUC AreaUndertheCurve
BN BayesianNetwork
CMC ContraceptiveMethodChoice
CMEM CategoricalMaximumEntropyModel
CTGAN ConditionalTabularGenerativeAdversarialNetwork
CVD CardioVascularDisease
DCR DistancetotheClosestRecord
DL DeepLearning
DLA DataLabellingAnalysis
DRA DimensionalityReductionAnalysis
DT DecisionTree
EHR ElectronicHealthRecords
GAN GenerativeAdversarialNetwork
GM GaussianMultivariate
ILP IndianLiverPatient
JSD Jensen-ShannonDivergence
KNN K-NearestNeighbors
KS Kolmogorov-Smirnov
MAE MeanAbsoluteError
MIA MembershipInferenceAttack
MKDE Movement-basedKernelDensityEstimation
ML MachineLearning
MLP MultiLayerPerceptron
MRA MultivariateRelationshipAnalysis
PCA PrincipalComponentAnalysis
PID PimaIndiansDiabetes
PPC PairwisePearsonCorrelation
QID Quasi-IDentifiers
RD RealData
RF RandomForest
RIRA Re-IdentificationRiskAnalysis
RMSE RootMeanSquaredError
RNN RecurrentNeuralNetwork
ROC ReceiverOperatingCharacteristic
RTS RealToSynthetic
SD SyntheticData
SDG SyntheticDataGeneration
SDV SyntheticDataVault
SEA SimilarityEvaluationAnalysis
STD SyntheticTabularData
STDG SyntheticTabularDataGeneration
(Continued)
MethodsofInformationinMedicine Vol.62 No.S1/2023 ©2023.TheAuthor(s).

| e38 Synthetic | Tabular Data | Evaluation | Hernadez | et al. |
| ------------- | ------------ | ---------- | -------- | ------ |
(Continued)
| Abbreviation |     |     |     | Definition                              |
| ------------ | --- | --- | --- | --------------------------------------- |
| STR          |     |     |     | SyntheticToReal                         |
| SVM          |     |     |     | SupportVectorMachines                   |
| TRTR         |     |     |     | TrainonRealTestonReal                   |
| TSTR         |     |     |     | TrainonSyntheticTestonReal              |
| URA          |     |     |     | UnivariateResemblanceAnalysis           |
| WGAN         |     |     |     | WassersteinGenerativeAdversarialNetwork |
WGANGP WassersteinGenerativeAdversarialNetworkwithGradientPenalty
Appendix B: Evaluation metrics and methods not included in the Final Methodology
| AppendixB.1.Visualanalysisof |     |     | individualattributes |     |
| ---------------------------- | --- | --- | -------------------- | --- |
AnextramethodfortheURA,isproposedtovisuallycomparethevaluesofeachattribute(RDvs.STD).Fornumericaland
categoricalattributes,distributionplotsandhistogramscanbeused.TheSTDGapproacheshavebeencategorizeddepending
onthenumberofattributesthatmaintainedresemblanceoftheRDattributes.Sincethisvisualizationissubjectiveandcannot
begivenanobjectiveevaluationvalueithasbeendeletedfromtheproposedevaluationmethodology.However,theresultsof
applyingthismethodcanbeseenintheSupplementaryMaterial1,availableintheonlineversiononly,availableintheonline
versiononly).
AppendixB.2.Dimensionalityresemblanceanalysis(DRA)
ToanalyzeifthedimensionalpropertiesofRDarepreservedinSTD,itisproposedtoanalyzetheperformanceofalinear,
principal component analysis (PCA), and a non-linear, Isomap, dimensionality reduction method for RD and STD. The
transformationshouldbeindependentlycomputedforRDandSTDforthetwomethodsafterscalingthenumericalattributes
andone-hotencodingthecategoricalattributes.Aftercomputingthetransformations,theresultscanbevisuallyanalyzed
withscatterplotsforeachmethod.ThemoresimilartheshapesofRDandSTDplotsare,themoreresemblanceismaintained.
Additionally,adistancemetricbetweenRDandSTDdimensionalityreductionplotsisproposedtocalculateanumerical
valuefromthevisualresults.Thisdistancemetricisthejointdistanceofthebarycenterdistanceandspreaddistanceofboth
plots (Equation 10). Thebarycenter distance is the distancebetween the meanvalues of the RDand STD dimensionality
reductionmatrices,whilethespreaddistanceisthedistancebetweenthestandarddeviationvaluesofthesamematrices.αis
aregularizationparameter thatgivesdifferent weightstoeachdistance.Intheequationμisthemeanvalueandσisthe
standarddeviationorRD(r)andSTD(s).
Equation10:JointDistanceofdimensionalityreductionplots
Intheseexperiments,α¼0.05hasbeenchosenexperimentally,asthebarycenterdistanceusingPCAandIsomapisvery
lowsincethebarycentersarecalculatedsimilarlyinbothdimensionalityreductionmethods.Asthisdistancemetriccannotbe
normalized,itisnotpossibletodefineamethodologytoquantitativelyclassifytheresemblanceofSTDgeneratedwithoneor
moreSTDGapproachesinto“Excellent,”“Good,”and“Poor,”althoughthelowerthisdistancevalueis,themoresimilarthe
dimensionality reduction plots for RD and STD are. For this reason, this analysis has not been considered for the total
resemblance calculation, but the results of both the plots and the distance metric are provided and discussed in the
SupplementaryMaterial1,availableintheonlineversiononly).
| MethodsofInformationinMedicine |     | Vol.62 No.S1/2023 | ©2023.TheAuthor(s). |     |
| ------------------------------ | --- | ----------------- | ------------------- | --- |