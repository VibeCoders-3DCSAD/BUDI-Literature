---
conversion_metadata:
  converted_at: "2026-10-12T07:46:46Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Vijayanand & Smrithy, 2024.pdf"
  source_pdf_sha256: "afce7b3295139fc88d97139da884f203daa4ebfd17c192aec06e533fcbcecf27"
  page_count: 16
  markdown_char_count: 57807
---

ResearchArticle
IntelligentDecisionTechnologies
Explainable AI - enhanced ensemble 2025,Vol.19(1)52–67
©TheAuthor(s)2024
learning for financial fraud detection in Articlereuseguidelines:
sagepub.com/journals-permissions
DOI:10.1177/18724981241289751
mobile money transactions journals.sagepub.com/home/idt
Deepshika Vijayanand and Girijakumari Sreekantan Smrithy
Abstract
This research paper addresses the pressing problem of financial fraud in the changing context of digital banking by inte-
grating machine learning and explainable AI, specifically exploiting SHapley Additive exPlanations (SHAP). With a focus
on enhancing both accuracy and interpretability, this study utilizes a synthetically generated dataset from the PaySim
simulator, encompassing 6,362,620 records. The usefulness of an Ensemble Learning Model with a Voting Classifier is
shown by its evaluation of different machine learning models, which achieves an excellent accuracy of 99.904%.Empha-
sizingtransparency,accountability,andregulatorycompliance,thisworkemploysSHAPanalysistounveilattribute-level
interpretability,providingstakeholderswithclearinsights.Thegoalofthisinterdisciplinaryendeavoristoprovideasafe
spacefordigitalfinancebybridgingthegapbetweenprecisionandinterpretability,whichwillaidinthecreationofopen
methods.
Keywords
Ensemble learning, explainable AI, feature importance, financial fraud, interpretability, machine learning, mobile money,
SHAPanalysis,transparency
Received:15April2024;accepted:17September2024
1 Introduction
In today’s digitally-dominated world, the simplicity and efficacy of banking have changed due to the advancement of
financialtechnology,bringinginaneweraofpreviouslyunimaginableopportunities.Thoughtherearemanychallenges
associatedwiththisincreaseindigitalfinancialinteractions,thegrowingthreatoffinancialfraudisoneofthemostcritical
ones.Thereisanimmediateaneedreliablesystemsthatcanidentifyandstopfraudulentactionsastheyhappen, asthe
AssociationofCertifiedFraudExaminers(ACFE)reportsthatworldwidefraudlosseshavereachedaconcerning5%of
yearlyincome.1
Thesheervolumeofglobaldigitalpaymenttransactions,projectedtoreachUS$16.62tnby2028(Statista),underlines
the growing reliance on digital financial interactions.2 Nevertheless, with this digital transformation comes an alarming
increaseinthecostofcybercrime,projectedtoreachUS$10.5Trillionannuallyby2025.3 Thesophisticationofmodern
fraud schemes, leveraging advanced techniques such as machine learning to evade detection,4 poses not only a severe
financialriskbutalsojeopardizesthetrustthatunderpinstheentirefinancialecosystem.
Financialinstitutionsfaceamultifacetedchallenge,withanestimated$4.23lossforeverydollarlosttofraudin2022,5
consideringboththeimmediatefinancialimpactandthelong-termconsequences.Regulationcompliance,drivenbythe
GDPRandPSD2,necessitatesaccountabilityaswellastransparencyinprocessingofdataanddecisions.Inresponsetothis
evolvinglandscape,theadoptionofmachinelearninginfinancialservicesisgrowing,with70%offinancialinstitutions
reportingitsuseforfrauddetectionasof2020.6
SchoolofComputerScienceandEngineering,VelloreInstituteofTechnology,Chennai,India
Correspondingauthor:
GirijakumariSreekantanSmrithy,SchoolofComputerScienceandEngineering,VelloreInstituteofTechnology,Chennai,TamilNadu,600127,India.
Email:smrithy.gs@vit.ac.in

VijayanandandSmrithy 53
Traditionalmachinelearningmodelsfrequentlyfunctionasopaque,or“black-box,”entities,makingitchallengingfor
stakeholders to understand the logic underlying the models forecasts. Not only does a lack of transparency undermine
trust, but it also creates regulatory problems in sectors where explainability is essential. According to data scientists,
machine learning models can not be understood or trusted unless they are interpretable.7 Combining machine learning
withexplainableAIisthefocusofthisstudysinceitoffersasolutiontotheproblemsofaccuracyandinterpretabilityin
financialfrauddetectionsystems.
Explainable AI becomes crucial for demystifying machine learning models’ decision-making processes, especially
with SHAP (SHapley Additive exPlanations). Explainable AI is essential for fostering trust in financial institutions and
guaranteeingaccountabilityinalgorithmicdecision-making,anditsnecessityextendsbeyondcompliance.Thisresearch
combines the power of explainable AI with ensemble machine learning to create financial fraud detection models that
performwellinaccuracyandofferstakeholdersinterpretableinsights.Theultimateobjectivesaretostrengthenthebarrier
againstfinancialfraud,promotetrustinfinancialinstitutions,andcreateasafeenvironmentfordigitalfinance.
2 Literature survey
The need for robust systems to detect and prevent fraudulent activities has become paramount, leading to a shift from
traditional approaches to more adaptive and intelligent solutions. Ali et al.8 reviewed ML applications in detecting
financial fraud, emphasizing the limitations of traditional methods and highlighting SVM and ANN as key algorithms.
It addresses issues and gaps, suggesting exploration of ensemble methods and unsupervised learning like clustering.
Enhanced anomaly detection and incorporation of text-mining techniques such as Word2Vec, Doc2Vec, or BERT are
recommendedforimprovedMLmodelsincombatingfinancialfraud,providingacomprehensiveoverviewandinsights
forpotentialadvancements.Intheirextensivereviewof75publicationsspanning2009–2019,Al-Hashedietal.9classified
financial fraud as follows: bank fraud, insurance fraud, financial statement fraud, and cryptocurrency fraud. Of the 34
dataminingmethodsthatareincluded,SVMisthemostpopular,accountingfor23percentofalluses.NaïveBayesand
Random Forest followclosely behind (15percent each). The majority of studies (81.33%) focus on bank and insurance
fraud,offeringvaluableinsightsforacademiaandindustry.Thereviewcontributessignificantinformationtothefieldby
expandingthesampleandsummarizingnotableworks.Wickramanayakeetal.10addresscardpaymentfraud,asignificant
challengeintheglobaldigitaleconomy.Usingataxonomyderivedfromstudiesconductedbetween2009and2020,11 it
investigates fraud detection technologies that make use of data mining and machine learning advancements. Reviewing
45papers,thesurveyhighlightsstrategiesthattakeintoaccounthowfraudaffectsbusinesses,usefeatureengineeringto
profilecardholders,andadjusttochangingfraudtrends.Thepaperconcludeswithacomparativeevaluationofclassifica-
tionalgorithms,aimingtoprovideacomprehensiveoverviewforacademiaandcommercialdeveloperstacklingpayment
frauddetection.
A study conducted by Liu et al.12 focuses on creating a stable and interpretable model for financial fraud detection,
particularlyforimbalanceddatasets.ItidentifiesSmoteasthemosteffectiveoversamplingalgorithmandhighlightsAdap-
tive Lasso as the top performer for feature selection. LightGBM outperforms XGBoost and Random Forest in feature
importanceranking.ThestudyemphasizesthesignificanceofNULLNUMinidentifyingfraudulentcorporatedataand
recommendsincorporatingWoEencodingandIVvaluetestingforimprovedmodelperformance.Inconclusion,thepaper
suggestsfutureresearchdirections,includinglargersamplesizes,explorationofdeeplearning,andintegrationofnatural
languageprocessingtechnologiesforenhancedfinancialstatementfrauddetection.Anomalydetectionmethodsforfinan-
cialfraudarereviewedbyHilaletal.,13 withanemphasisonhowtechnologicallydrivenfraudhasledtorecentadvances
in unsupervised and semi-supervised learning. Issues with money laundering, insurance fraud, and credit card fraud are
addressed, with a focus on the transition from supervised to unsupervised and semi-supervised methods.11 Generative
modelslikeGANsandAEsarehighlightedforeffectivefeatureextraction,whiledeeplearningarchitectureslikeCNNs
and LSTMs capture temporal relations. The paper suggests future research directions, advocating for combined models
andemphasizinginterpretabilityinfrauddetection.
MittalS.&TyagiS.14examinesecurityconcernsinonlinecreditcardusagewithintheevolvinge-commercelandscape
over the past 25 years. Credit card fraud may be difficult to detect in real time, and skewed datasets are just two of the
problemshighlightedinthisanalysisofattackroutesandsolutions.15Thereviewunderscorestherecentsurgeincreditcard
transactionsandsubsequentfraud,leadingtothedevelopmentofmachinelearning-basedmodels.Someoftheproblems
that have been identified include a lack of standard algorithms and a lack of understanding of credit card processing.11
Furthermore,thearticlestressestheimportanceofbenchmarkdatasetsandinvestigatestheunrealizedpossibilitiesofbig
dataanalyticsandstreamingdatainrelationtofutureadvancementsinfrauddetection.15
Sadgali I. et al.16 evaluate machine learning techniques, emphasizing hybrid methods, for detecting various financial
fraudtypes,includingcreditcardfraud.Inordertosolveimbalanceddatasetsandincreaseaccuracyincreditcardfraud

54 IntelligentDecisionTechnologies19(1)
detection, the conclusion calls for improved algorithms and hybrid models. The findings emphasize the effectiveness of
Support Vector Machines (SVMs) in instantaneous transactional fraud detection.16 In response to the growing problem
offinancialfraudinonlineservices,AlghofailiY.etal.17 provideafreshstrategybasedondeeplearning’sLongShort-
TermMemory(LSTM)forbetterdetection.Inlessthanaminute,theLSTMbasedmodelachieves99.95%accuracyon
a genuine credit card fraud dataset, outperforming previous techniques and demonstrating its potential to advance fraud
detectionforhugedatasetsandreal-timeprocessingdemands.17
ThestudybyAlarfajF.K.etal.18 addressescreditcardfrauddetectionchallenges,proposingenhanceddeeplearning
algorithms. By improving its performance on the European card benchmark dataset, the model outperforms previous
techniques, earning a f1-score of 85.71 percent, a precision of 93.1 percent, and an area under the curve (AUC) of 98.0
percent.18 Thesefindingsdemonstratethepromiseofhighlydevelopedalgorithmsfortheaccurateidentificationofcredit
cardfraudintherealworld.18Forthepurposeofdetectingcreditcardfraud,IleberiE.etal.19useAdaBoostinconjunction
with a number of machine learning methods, such as Decision Trees, Random Forest, Extra Trees, XGBoost, Logistic
Regression,andSupportVectorMachine.ET-AdaBoostachieves99.98%accuracyandanMCCof0.99inthecomparison
study conducted on the European fraudulent transactions with credit cards dataset, demonstrating exceptional levels of
accuracy.19 The suggested machine learning techniques utilizing AdaBoost demonstrate exceptional results when tested
on a biased artificial credit card fraud dataset.19 By combining an ensemble classifier with an LSTM base learner in
AdaBoostandmakinguseofSMOTE-ENNforhybridresampling,EsenoghoE.etal.20 presentedasuccessfulapproach
todetectingcreditcardfraud.Thesuggestedmethodoutperformsotheralgorithms,achievinghighspecificity(0.998)and
sensitivity(0.996),indicatingitspotentialtoimprovecreditcardfrauddetection.20 Theincreaseddifficultyofcreditcard
fraud during the COVID-19 pandemic’s spike in online purchases was discussed by Alfaiz N. S., & Fati S. M..21 The
AllKNN-CatBoost model outperformed sixty-six other ML models on a real-world dataset, with an AUC of 97.94%, a
recallof95.91%,andanF1-Scoreof87.30%.21 Theresultsemphasizeitspotentialsignificanceinpreventingfraudulent
creditcardtransactionsduringonlineactivities,outperformingpreviousapproaches.
Awosika T. et al.22 introduced a novel approach to address fraudulent transactions in the financial sector, combining
Explainable AI (XAI) and Federated Learning (FL) to enhance transparency and interpretability in fraud detection sys-
tems. The integration of SHAP ensures accurate and understandable predictions, shedding light on influential features
and justifying decisions. This emphasis on transparency becomes crucial in sensitive domains, emphasizing that XAI is
essentialforaccountability,usertrust,andregulatorycomplianceinFL-basedfrauddetectionsystems.Table1showsthe
comparativeanalysisofvariousresearchworksonfinancialfrauddetectionusingmachinelearningalgorithmsanddeep
learningalgorithms.
It is evident from the in-depth review of numerous sources on financial fraud detection that machine learning (ML)
approachesareessentialfortacklingthedifficultiesassociatedwithfinancialfrauddetection.SVMs,DecisionTrees,Ran-
domForest,ANNs,anddeeplearningmodelssuchasLSTMarehighlyfavoredfortheirexceptionalaccuracy,according
to the reviewed literature.23,24 The emphasis on ensemble methods, data resampling techniques, and feature engineer-
inghighlightstheongoingpursuitofrefiningexistingmodels.Additionally,theincorporationofadvancedtechnologies,
suchasGenerativeAdversarialNetworks(GANs)signalsagrowingawarenessoftheneedforinterpretabilityandtrans-
parency in fraud detection systems. While the field has made substantial progress, the papers collectively advocate for
future research directions, including exploration into less-studied algorithms, text-mining techniques, natural language
processing, and the integration of novel approaches like federated learning and Explainable AI (XAI). The continuous
evolutionoffinancialfrauddetectionmethodologiesremainscriticaltostayingaheadofsophisticatedfraudulentactivities
andsafeguardingfinancialsystems.
3 Proposed methodology
Whensomeone“intentionallyandknowinglydeceivesthevictimbymisrepresenting,concealing,oromittingfactsabout
promised goods, services, or other benefits and consequences that are nonexistent, unnecessary, never intended to be
provided, or deliberately distorted for the purpose of monetary gain,” they are committing actions of financial fraud.25
Financialfraudinmobilemoneytransfersisthefocusofthisresearchwork. Mobilemoneyreferstomonetaryservices
andtransactionsthatmaybecarriedoutviaamobiledevice,suchaphoneortablet.26 Connectivitytoabankaccountis
notalwaysanoptionfortheseservices.26
Thisresearchfocusesonenhancingfraudpreventionsystemsbynotonlyprioritizingmodelaccuracybutalsoempha-
sizing explainability through SHAP analysis as illustrated in Figure 1. The study’s overarching goal is to provide more
open and understandable methodology by deconstructing machine learning models, with a focus on their use in finan-
cial fraud scenarios. An ever-changing cybersecurity environment is being tackled by combining machine learning with

VijayanandandSmrithy 55
|     | peedfoesuekam |     |     |     |     |     | tidercnisevitagen |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
larutan,gninrael .selpmasretaerg tiderclanoitidda otseitinutroppo duarfdractiderc
|     |                            | dna,gnissecorp |               | dnasmhtirogla |                       |               |                     |                             |              |              |                        |     |
| --- | -------------------------- | -------------- | ------------- | ------------- | --------------------- | ------------- | ------------------- | --------------------------- | ------------ | ------------ | ---------------------- | --- |
|     | ehtnihcraeseR dluohserutuf |                |               | sledomdirbyh  |                       | otseuqinhcet  | eslafeziminim       | ehtfonoitadilaV nokrowemarf | morfstesatad |              |                        |     |
|     |                            |                | fonoitarolpxE |               | dnastesatad           | gnicnalabataD |                     |                             |              |              | ehtevorpmi fonoitceted |     |
|     | kroWerutuF                 |                |               |               | gnisserdda decnalabmi | gnissecorp    |                     |                             |              | snoitutitsni |                        |     |
|     |                            |                |               | decnahne      | emit-laer             |               | duarfdrac noitceted |                             | duarfdrac    |              |                        |     |
|     |                            | egaugnal       |               |               |                       |               |                     |                             |              | laicnanfi    |                        |     |
thgilhgiH
|     | LLUNfoecnatropmi | etaroproctneluduarf |     | LMfosecnamrofrep | smhtirogladecnahne |     | detsegguseht,duarf | sdohtemLMdesoporP |     |     |     |     |
| --- | ---------------- | ------------------- | --- | ---------------- | ------------------ | --- | ------------------ | ----------------- | --- | --- | --- | --- |
gniyfitnediniMUN sdnemmocer,atad erutaefgnitargetni sledomdirbyhdna CCMdnaycarucca rehtosmrofreptuo
|     |     |     |     | ssorcaseuqinhcet |     | nodetaulavenehW dractiderclautca |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
smhtiroglagninraelpeeddnasmhtiroglagninraelenihcamgnisunoitcetedduarflaicnanfinoskrowhcraesersuoiravfosisylanaevitarapmoC ehtstaebledom roirepustibihxe %89.99deveihca
|     |     |     |     |     | duarftnereffid |     | tra-eht-fo-etats | tsooBadAhtiw |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------------ | --- | --- | --- | --- |
ehtsezisahpmE ehtsezisahpmE rofsetacovda -ecnamrofrep MTSLdesoporP
gnireenigne
|     |            |     | seuqinhcet |     | ,seirogetac |     | .smhtirogla |     |     |     | smhtirogla |     |
| --- | ---------- | --- | ---------- | --- | ----------- | --- | ----------- | --- | --- | --- | ---------- | --- |
|     | noisulcnoC |     |            |     |             |     |             |     |     |     | elbmesne   |     |
decnaun
99.0fo
|     |                   |     | ,skrowteNfeileBnaiseyaB |     | larueNdna,smhtiroglA |                  |                    |                        |                    |     |     |     |
| --- | ----------------- | --- | ----------------------- | --- | -------------------- | ---------------- | ------------------ | ---------------------- | ------------------ | --- | --- | --- |
|     |                   |     |                         |     |                      |                  | dna,MVS,noissergeR | citsigoL,seerTnoisiceD |                    |     |     |     |
|     | ,MBGthgiL,tsooBGX |     |                         |     |                      | noisiceD,tsooBGX |                    | modnaR,noissergeR      | ,seerTartxE,tseroF |     |     |     |
noisiceD,senihcaM
|     |              |     |     |               |     |     | gninraeLemertxE |     |              |     | ,MTSL,elbmesne |     |
| --- | ------------ | --- | --- | ------------- | --- | --- | --------------- | --- | ------------ | --- | -------------- | --- |
|     | tseroFmodnaR |     |     | rotceVtroppuS |     |     |                 |     | ,MVS,tsooBGX |     |                |     |
citeneG,seerT
|     |            |     |     |     |          | ,tseroFmodnaR | citsigoL,eerT |     | tsooBadA-TE | krowtenlarueN | NNE-ETOMS |     |
| --- | ---------- | --- | --- | --- | -------- | ------------- | ------------- | --- | ----------- | ------------- | --------- | --- |
|     | desUsledoM |     |     |     | skrowteN |               |               |     |             |               | ,tsooBadA |     |
dohteM
|     | repaPehtfoemehT |                  |                |                 |                | rofsmhtiroglaLD |                 |              |                                 |                 |                 |             |
| --- | --------------- | ---------------- | -------------- | --------------- | -------------- | --------------- | --------------- | ------------ | ------------------------------- | --------------- | --------------- | ----------- |
|     | serapmoc,ledom  | erutaefsetaulave |                | gninraelenihcam |                | dnaLMfoesuehT   | duarfdractiderc |              | ehtniseuqinhcet duarfdractiderc |                 | agnisunoitceted |             |
|     |                 |                  | nodesabsdohteM |                 |                |                 | fonoitcetedeht  |              |                                 | duarfdractiderC | krowtenlaruen   |             |
|     |                 |                  |                | ehtotdeilppa    | duarflaicnanfi |                 |                 | LMfoycacfife |                                 |                 | dnaelbmesne     |             |
|     | elbaterpretni   | gnilpmasrevo     |                |                 |                |                 |                 |              | fonoitceted                     |                 |                 |             |
|     |                 | ,smhtirogla      |                | fomelborp       |                |                 |                 | ehtgnissessA |                                 |                 |                 | gnireenigne |
noitceted
noitceles sdohtem
|     | dnaelbatS   |     |     |              |     |                |     |               |     |                |     | erutaef |
| --- | ----------- | --- | --- | ------------ | --- | -------------- | --- | ------------- | --- | -------------- | --- | ------- |
|     |             |     |     |              |     | ,01,sseccAEEEI |     |               |     | ,01,sseccAEEEI |     |         |
|     | 1202,erauqS |     |     | ,841,ecneicS |     |                |     | ,9,sseccAEEEI |     |                |     |         |
retupmoC
dnalanruoJ noitacilbuP
aidecorP
| foetaD | hcraeeR                                 |     |                       | 9102               |     | 2202          |                                   | 1202                      |                     |                     | 2202                      |           |
| ------ | --------------------------------------- | --- | --------------------- | ------------------ | --- | ------------- | --------------------------------- | ------------------------- | ------------------- | ------------------- | ------------------------- | --------- |
|        | &,.R,eY,.Z,uiL                          |     |                       |                    |     |               | ,demhA&,.M                        |                           |                     |                     | ,.D.I,eyneiM &,.K,abelurA |           |
|        |                                         |     | ,leaS,.I,ilagdaS      |                    |     |               | ,.U.H,nahK ,mallasumlA ,nazmaR,.N | ,nuS,.E,irebelI ,gnaW&,.Y |                     |                     | ,.G.T,trawS               |           |
|        |                                         |     |                       | ,uobbaneB          |     | ,.K.F,jafralA |                                   |                           |                     | ,.E,ohgonesE        |                           | .G,odiabO |
|        | 21.R,eY                                 |     |                       |                    |     | ,.I,kilaM     |                                   |                           |                     |                     |                           |           |
|        | srohtuA                                 |     |                       | &,.N               |     |               |                                   |                           |                     |                     |                           |           |
|        |                                         |     |                       | 61.F               |     |               |                                   | 81.M                      | 91.Z                |                     |                           |           |
|        |                                         |     |                       |                    |     |               |                                   |                           | draCtiderCgnitceteD |                     | decnahnErofelbmesnE       |           |
|        | htiwduarFtnemetatS enihcaMelbaterpretnI |     | fosisylanAecnamrofreP | tiderCnismhtiroglA |     |               | dnagninraeLenihcaM                | desaB-tsooBadAdna         |                     |                     |                           |           |
|        |                                         |     |                       |                    |     |               |                                   | ETOMSfotnemssessA         |                     | dereenignE-erutaeFA |                           |           |
duarFdraCtiderC
|     |                    |     |     | gninraeLenihcaM |              |                                |                  |     | gninraeLenihcaM |     | krowteNlarueN |              |
| --- | ------------------ | --- | --- | --------------- | ------------ | ------------------------------ | ---------------- | --- | --------------- | --- | ------------- | ------------ |
|     | laicnaniFgnitceteD |     |     |                 |              | duarFdraCtiderC gnisUnoitceteD | trA-eht-fo-etatS |     |                 |     |               |              |
|     |                    |     |     |                 |              |                                | gninraeLpeeD     |     | rofseuqinhceT   |     |               |              |
|     |                    |     |     |                 | 61.noitceteD |                                | 81.smhtiroglA    |     |                 |     |               | 02.noitceteD |
duarFsdraC
21.gninraeL
91.duarF
eltiT
.1 elbaT
onS
|     | 1   |     | 2   |     |     | 3   |     | 4   |     | 5   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

56 IntelligentDecisionTechnologies19(1)
Figure 1. Architectureoftheproposedmethodology.
explainable AI. The goal is to strengthen defences and provide stakeholders with interpretable information to combat
financialcrime.27
3.1 Dataset description and data preprocessing
Withthisdataset,wewanttoaddressaknowledgevacuuminpubliclyavailablefinancialservicesdatasets,withafocuson
mobilemoneytransactionsasarelativelyyoungindustry.Manyreal-worlddatasetsarenotavailabletothepublicbecause
ofthesensitivenatureoffinancialtransactions.28Togetaroundthisconstraint,thedatasetisartificiallyconstructedusing
a simulator called PaySim. To simulate mobile money transactions, PaySim uses a subset of real transactions extracted
fromaprovider’smonthlyfinancialdata.Amultinationalfirmisnowrunningthemobilebankingserviceinmorethan14
countriesacrosstheworld,andtheyaretheoneswhoprovidedtheinitiallogs.
TheSwedishKnowledgeFoundation(grant:20140032)issupportingthestudy“Scalableresource-efficientsolutions
for big data analytics,” which includes this dataset.29 The dataset encompasses a comprehensive 6,362,620 records, of
which6,354,407arevalidtransactions,constituting99.87%,and8213arefraudulenttransactions,amountingto0.13%.
Among the flagged transactions, totaling 16, all fall under the “TRANSFER” type and are marked as fraudulent. The
transactionamountsinthissubsetrangefrom353,874.22to10,000,000.0.
Inthispreliminaryphase,wecommencebyimportingessentiallibrariesandconductingacomprehensiveexamination
ofthedataset.Ourinitialfocusinvolvesscrutinizingforanymissingdataanddelvingintothedistributionpatternsofboth
validandfraudulenttransactions,establishingafoundationalunderstandingforsubsequentpreprocessingsteps.
In addition, we enhance our exploratory analysis through data visualization techniques, enabling a more insightful
understandingofthedataset’scharacteristicsandaidingintheidentificationofpatternsortrendsthatmayinfluencethe
subsequentmodelingprocess.Figure2presentsapiechartillustratingthedistributionoftransactiontypes,revealingthat
TransferTransactionsconstitute19%,whileCashOutTransactionsdominatethemajoritywithan81%representation.
In Figure 3, a bar graph delineates the total monetary value associated with each transaction type. Cash Out trans-
actions exhibit a substantial total amount of 394,412,995,224, while Transfer transactions surpass with a total amount
of 485,291,987,263, offering a comprehensive visual representation of the financial magnitudes associated with each
transactioncategory.InFigure4,abargraphmeticulouslyportraystheincidenceoffraudulenttransactionswithineach
transactiontype.Notably,CashOuttransactionsaccountfor223,750instances,whileTransfertransactionsrevealahigher
frequency with 532,909 cases, providing a nuanced insight into the distribution of fraudulent activities across different
transactioncategories.
Tofortifytherobustnessofouranalysis,wediligentlyaddresspotentialimbalancesinherentinthedataset.Moreover,
we meticulously investigate and rectify disparities in balances at both the origin and destination following transactions.

VijayanandandSmrithy 57
Figure 2. Piechartofratiooftransactiontypes.
Figure 3. Totalamounttransactedineachtransactiontype.

58 IntelligentDecisionTechnologies19(1)
Figure 4. Fraudulenttransactionstypes-cashoutandtransfer.
Theidentificationandanalysisoftransactionswithamountslessthanorequaltozerooffervaluableinsightsintopotential
anomaliesthatmayimpactthemodel’sperformance.Table2showsdifferentattributesofthedataset.
3.2 Feature engineering
Followingtheinitialexploratoryphase,wetransitiontoameticulousfeatureengineeringprocesstoenhancethedataset’s
suitability for machine learning model training. Begin with the 11 columns that make up the original features: “step,”
“type,”“amount,”“nameOrig,”“oldbalanceOrg,”“newbalanceOrig,”“nameDest,”“oldbalanceDest,”“newbalanceDest,”
“isFraud,” and “isFlaggedFraud.” Then we go on to the current features. Unwanted features such as “step,” “type,”
“nameOrig,”“nameDest,”“error_orig,”“error_dest,”and“isFlaggedFraud”aresubsequentlyremovedtostreamlinethe
dataset.
Toensureuniformity,continuousvalueswithinthecolumns“amount,”“oldbalanceOrg,”“oldbalanceDest,”“newbal-
anceOrig,” and “newbalanceDest” are standardized to fall within the 0 to 1 range using the StandardScaler. One of the
mostimportantstepsingettingdatareadytotrainmachinelearningmodelsisemployingthe‘traintestsplit’approachto
dividetheresultantdatasetintoseveralsets:trainingandtesting.Tomakesurethesplitisacceptable,welookatthesize
ofthetrainingandtestingsets.
Additionally, we conduct checks for missing values in the target variable, “isFraud,” and address them by dropping
rows with missing values. After cleaning the data, it is divided into two sets: one for testing and one for training. The
stratification is kept and the test size is set at 20%. The final dimensions of the split datasets are verified to confirm the
successfulcompletionofthepreprocessingsteps.

VijayanandandSmrithy 59
Table 2. Detailedinformationofthedatasetattributes
Attribute Description DataType
step Areal-worldtimemeasurewhereonestepisequivalenttoonehour. int64
type TypeofTransaction:Transfer,Debit,Payment,Cash-In,Cash-Out. object
amount Thetransactionamountexpressedinlocalcurrency. float64
nameOrig Transactionstartedbythecustomer. object
oldbalanceOrg Startingbalancepriortothetransaction. float64
newbalanceOrig Newbalancefollowingthetransaction. float64
nameDest Customerreceivingthetransaction. object
oldbalanceDest Therecipient’sstartingbalancepriortothetransaction. float64
newbalanceDest Therecipient’snewbalancefollowingthetransaction. float64
isFraud Fortransactionscarriedoutbyfraudulentagentsinthesimulation,abinaryindicator(1or0). int64
isFlaggedFraud Asignalthatsuggestsattemptstosendmorethan$200,000inasingletransaction. int64
3.3 Classification models
Oneofthemostimportantusesofmachinelearningisfrauddetection,wherechoosingtherightmodelmayhaveahuge
impact on efficiency. In this study, we dive headfirst into the complex world of fraud detection and analyse six well-
known machine learning models: Neural Network, XGBoost, Decision Tree, Random Forest, and Logistic Regression.
Theresearchaimstoprovideadetailedandthoroughknowledgeofeachmodel’seffectivenessandsuitabilityforhandling
theintricaciesoffrauddetectionbycarefullyusingseveralperformanceindicators,suchasaccuracy,F1score,confusion
matrix,andROCAUCscore.
3.3.1 Logistic regression. David Cox developed the basic technique for creating a logistic model (sometimes called the
logitmodel)in1958andnameditlogisticregression.Duetoitsconnectiontologisticdatadistribution,itsprimarybenefit
isthatitcanbeappliedtobothclassprobabilityestimationandclassification.Itappliesanonlinearsigmoidalfunctionas
showninequation1onalinearcombinationoffeatures.30
S(x)=1÷(1+e (−x)) (1)
Logisticregressionisbotharobustandflexiblemethodfordichotomousclassificationprediction,whichinvolvesmaking
predictionsforstatesoroutcomesthatmayberepresentedasyes/no,success/failure,orwilloccur/willnotoccur.31 Since
the classes in a supervised classification issue are discrete, the goal of the methods is to find the decision boundaries
betweenthem.32
3.3.2 Decisiontree. Whenitcomestosupervisedlearning,decisiontreesarethewaytogo.33Toaidindecision-making,
decision trees use a tree structure that mimics human brain processes.33 Attribute selection as the decision tree’s root
nodeisthefirststep.33 Additionally,foreachsingleattributevalue,itcreatesabranchandsplitstheinstanceintomany
subgroups. Thirdly, there is a connection to a branch from the root node in each subset.34 With each branch completed,
thealgorithmrepeatedlycontinuestheprocess.35
3.3.3 Randomforest. Whenitcomestocategorization,theRandomForest(RF)algorithmisamongthetopoptions.RF
iscapableofproperlycategorizingmassivevolumesofdata.Thismethodoflearninginvolvestrainingalargenumberof
decision trees,with thegoal of having each treeanticipate themodal outputs.36 According to,36 RFuses random vector
valuesforeachtreeasitspredictors.Thebasicpremiseisthatagroupof“weaklearners”mayworktogethertocreatea
“stronglearner."36–40
3.3.4 XGBoost. An implementation of Gradient Boosting that makes use of gradients derived from decision trees is
knownasExtremeGradientBoosting(XGBoost).Iteratively,itbuildssimple,briefdecisiontrees.Becauseofitsextreme
bias,everytreeisreferredtoasa“weaklearner.”XGBooststartsbyconstructingthefirst,mostbasictree,whichperforms
poorly. After then, it creates a second tree that is trained to predict actions that the previous tree—a poor learner—was
unable to do. The method generates progressively weaker learners, each of them fixing the preceding tree before the
stoppingcondition—forexample,thequantityoftrees(estimators)thatneedtobeproduced—issatisfied.XGBoostoffers
furtherbenefits:Trainingisquickandcanbesplitupordividedamongmultipleclusters.41,42

| 60  |     |     | IntelligentDecisionTechnologies19(1) |     |     |
| --- | --- | --- | ------------------------------------ | --- | --- |
Table 3. Crossvalidationresultsonaccuracy(%)
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 99.82 | 99.83 | 99.81 | 99.82 | 99.83 |
| DecisionTree       | 99.94 | 99.93 | 99.94 | 99.93 | 99.94 |
| RandomForest       | 99.92 | 99.92 | 99.92 | 99.93 | 99.92 |
| XGBoost            | 99.91 | 99.90 | 99.91 | 99.90 | 99.92 |
| LightGBM           | 99.75 | 99.75 | 99.75 | 99.76 | 99.76 |
| NeuralNetwork      | 99.86 | 99.85 | 99.85 | 99.87 | 99.85 |
Table 4. CrossvalidationresultsonF1scores
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 0.60  | 0.62  | 0.61  | 0.60  | 0.60  |
| DecisionTree       | 0.89  | 0.90  | 0.89  | 0.90  | 0.89  |
| RandomForest       | 0.86  | 0.85  | 0.85  | 0.85  | 0.86  |
| XGBoost            | 0.83  | 0.83  | 0.82  | 0.83  | 0.83  |
| LightGBM           | 0.51  | 0.50  | 0.51  | 0.50  | 0.50  |
| NeuralNetwork      | 0.68  | 0.68  | 0.69  | 0.68  | 0.68  |
Table 5. CrossvalidationresultsonROCAUCscores
| Model              | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ------------------ | ----- | ----- | ----- | ----- | ----- |
| Logisticregression | 0.98  | 0.98  | 0.97  | 0.98  | 0.98  |
| DecisionTree       | 0.94  | 0.94  | 0.94  | 0.94  | 0.94  |
| RandomForest       | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
| XGBoost            | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
| LightGBM           | 0.64  | 0.64  | 0.64  | 0.64  | 0.65  |
| NeuralNetwork      | 0.98  | 0.98  | 0.98  | 0.98  | 0.98  |
3.3.5 LightGBM. LightGBMisaframeworkforgradientboostingthatmakesuseoftechniquesfortree-basedlearning.
Thefollowingadvantagesareachievedbyitsefficientdistribution:quickertrainingspeed,lessmemoryuse,higheraccu-
racy,supportforGPU,distributed,andparallellearning,andbetterefficiencyoverall.43 Manyboostingprogramsemploy
pre-sort-based algorithms for decision tree learning, such XGBoost’s default approach.44,45 It is not easy to optimize,
histograms,46–48
despite being a straightforward solution. LightGBM uses methods that are based on which divide the
valuesofcontinuousfeatures(attributes)intodiscretebins.Thisdecreasesmemoryuseandspeedsuptraining.49
3.3.6 Neuralnetwork. Neuralnetworks(NNs)andartificialneuralnetworks(ANNs)aretwonamesforthesamekindof
AImodelthatattemptstosimulatebrainactivity.Inthe1990s,theywerepresentedasadifferentapproachtoaddressgeo-
graphicissues,andmorerecently,theyhavegrownbecauseofdevelopmentsincomputerpower,artificialintelligence,and
dataavailability,amongotherareas.50NeuralNetworkscanlearncomplexnonlinearrelationshipsusingtrainingexample
sets.Theyworkparticularlyeffectivelyinpatternidentificationscenarioswherecomplextrendsinhigh-dimensionaldata
needtobeidentified.51
AstratifiedK-Foldcrossvalidationwasperformedtoensurethereliabilityandrobustnessoftheexperiments.Tables3,
4 and 5 show the cross validation results of various models on the metrics accuracy, F1 score and ROC AUC scores
respectively. We summarize the average performance characteristics of our machine learning models for classification
in Table 6, providing a thorough understanding of their efficacy. Accuracy, F1 score, and ROC AUC score are some of
themostimportantmetricsthatrevealthemodels’overallclassificationaccuracy,precision-recallbalance,andabilityto
discernbetweenpositiveandnegativeexamples.
Additionally,Friedman’sstatisticaltestisusedtocomparetheperformanceofdifferentmodels.Theresultingp-value
is 0.000139 which is significantly less than the significance level 0.05 indicating that there are significant differences
betweentheperformancesofthemodels.TheNemenyipost-hoctestprovidespairwisecomparisonsbetweenthemodels.
Table7showsthep-valuesforthecomparisons.

| VijayanandandSmrithy |     |     |     |     |     | 61  |
| -------------------- | --- | --- | --- | --- | --- | --- |
Table 6. Performancemetricsofclassificationmachinelearningmodels
| Machine/Deep          |     | Accuracy(%)ofthe |     | F1Scoreofthe | ROCAUCScoreofthe |     |
| --------------------- | --- | ---------------- | --- | ------------ | ---------------- | --- |
| LearningModel         |     | ML/DLModel       |     | ML/DLModel   | ML/DLModel       |     |
| LogisticRegression.30 |     | 99.826           |     | 0.606        | 0.978            |     |
| DecisionTree.33       |     | 99.937           |     | 0.893        | 0.943            |     |
| RandomForest.36       |     | 99.922           |     | 0.855        | 0.996            |     |
| XGBoost.41,42         |     | 99.908           |     | 0.829        | 0.990            |     |
LightGBM.49
|                     |     | 99.753 |     | 0.507 | 0.641 |     |
| ------------------- | --- | ------ | --- | ----- | ----- | --- |
| NeuralNetwork.50,51 |     | 99.855 |     | 0.682 | 0.983 |     |
Table 7. NemenyiPost-HocTestResults
|     | 0        | 1        | 2        | 3        | 4        | 5        |
| --- | -------- | -------- | -------- | -------- | -------- | -------- |
| 0   | 1.000000 | 0.009434 | 0.114066 | 0.532706 | 0.900000 | 0.900000 |
| 1   | 0.009434 | 1.000000 | 0.900000 | 0.532706 | 0.001000 | 0.114066 |
| 2   | 0.114066 | 0.900000 | 1.000000 | 0.900000 | 0.009434 | 0.532706 |
| 3   | 0.532706 | 0.532706 | 0.900000 | 1.000000 | 0.114066 | 0.900000 |
| 4   | 0.900000 | 0.001000 | 0.009434 | 0.114066 | 1.000000 | 0.532706 |
| 5   | 0.900000 | 0.114066 | 0.532706 | 0.900000 | 0.532706 | 1.000000 |
Table 8. Crossvalidationresultsofensemblelearningclassifier
| Metrics     |     | Fold1 | Fold2 | Fold3 | Fold4 | Fold5 |
| ----------- | --- | ----- | ----- | ----- | ----- | ----- |
| Accuracy    |     | 99.90 | 99.91 | 99.90 | 99.90 | 99.92 |
| F1Score     |     | 0.81  | 0.82  | 0.81  | 0.81  | 0.82  |
| ROCAUCScore |     | 0.99  | 0.99  | 0.99  | 0.99  | 0.99  |
TheresultssuggestthatcertainmodelssuchasLogisticRegression,DecisionTrees,RandomForest,LightGBMhave
performancedifferencesthatarestatisticallysignificant.
| 4 Ensemble | learning | model- voting | classifier |     |     |     |
| ---------- | -------- | ------------- | ---------- | --- | --- | --- |
When solving tasks like classification, ensemble learning uses a combination of many learning models that have been
deliberatelygenerated.52 Thisisbasedonthenotionthattwomindsarepreferabletoone.Additionally,wegatherinfor-
mation from various sources and rank or combine them in order to make strategic judgments. A supervised learning
algorithm is an ensemble in and of itself. Many classifier systems are another name for ensemble learning systems.32
Usingthesamedatatotrainseveralmodelsandthencombiningtheirpredictionsisknownasensemblelearning.53
The
goal of ensemble learning is to improve performance above that of a single model by combining many models into a
singleensemble.53 Thefirststepistodeterminehowtobuildtheensemblemodels,andthesecondistofigureouthowto
aggregatetheforecastsofeachmemberoftheensemble.Onewaytomakepredictionsmoreaccurateistouseensemble
learning.54
This instance makes use of a meta classifier, which is able to merge prediction models from different or comparable
machine learning datasets by means of a majority vote or soft voting. To choose the most likely class, soft voting aver-
ages the base models’ class pseudo-probabilities.55 The voting classifier outperforms the other baseline models because
to its ability to incorporate the predictions of many ML and DL models.56 Figure 5 illustrates our proposed ensemble
model, a culmination of various classifiers aimed at elevating predictive performance through strategic combination. A
number of classifiers—including XGBoost, LightBGM, Neural Networks, Decision Tree Classifier, and Random Forest
Classifier—arepartofthisensemble.Table8showstheStratifiedK-Foldcrossvalidationresultsoftheensemblelearning
model.
Table9providestheaveragesummaryoftheperformancemetricsoftheensemblelearningmodel,withafocusonaccu-
racy,F1score,andROCAUCscore.Thecollectiveassessmenthighlightsthemodel’sexceptionalaccuracyof99.904%,
underscoringitsefficacyacrossdiverseclassificationscenarios.

62 IntelligentDecisionTechnologies19(1)
Figure 5. Proposedensemblemodel.
Table 9. Performancemeasureofensemblelearningclassifier
Accuracy(%)oftheModel F1ScoreoftheModel ROCAUCScoreoftheModel
EnsembleLearningModel 99.904 0.814 0.990
Figure 6. ProcessofexplainableAI.
5 Explainable AI
Coined by DARPA in 2016, Explainable AI (XAI) addresses the need for transparency in AI systems, countering the
‘blackbox’natureofmachinelearning.Crucialindelicatefieldslikehealthcareandbanking,XAIseekstoensurethatAI
systemsaretransparentandeasytointerpret.Usingwhite-boxmodelssuchasConceptBottleneckModels,XAIjustifies
decisions,promotingtrustandfacilitatingusercomprehension.Symbolicregressionisproposedforsupervisedmachine
learningtoensuretransparencyandauditability.Overall,XAIseekstodemystifyAIdecisions,enhancingusertrustand
understanding.57–60
InFigure6,wecanseehowtherequirementsorapplicationdomaindictatetheinputdatausedtotrainthemodels,the
predictionapproachthatisselected,andtheXAImethodsthatareusedtoexplainthemodels’innerworkingsandoutput

VijayanandandSmrithy 63
Table 10. Averageimpactofattributesonmodeloutput
Attribute MeanSHAPValue
OldBalanceOrg 0.065
NewBalanceOrg 0.055
Amount 0.04
NewBlanceDest 0.03
OldBalanceDest 0.03
Figure 7. MeanSHAPvalue(averageimpactofattributeonmodeloutput).
viaanexplanationinterface.57BecauseweareawareofExplainableAI’sresults,wewillbemoreconfidentinAImodels.
Userscanenhancethemodel’saccuracyandidentifyitsshortcomingsbyusingtheoutputinformation.Theendeffectwill
bethatconsumersarebetterabletodecidehowtoenhancethemodel.61
Inthisstudy,weinterpretmachinelearningmodeloutputusingSHAP,acommonexplainabilitytechniqueutilizedin
ExplainableAI(XAI).Basically,SHAPfunctionsasa“featureattributionmethod”.62Similartoagametheoryapproach,
SHAPenhancesthereadabilityofeachpredictionindependentlybydeterminingtheimportancevaluesforeachattribute.
ThreeimportantattributesmakeuptheaggregatedegreeoffeatureimportancemaintainedbytheSHAPvalues:“Missing-
ness,accuracy,andconsistency”.Intermsofinterpretation,SHAPismoreintuitiveandsimplertocompute.63Inaddition
tobeingmodel-agnostic,itprovidesexplanationsthatarebothlocalandglobalandismoredependablewhendealingwith
anykindofdata.Inordertoempowerplayersaccordingtotheirlevelofparticipation,weemployShapleyvalues,which
adhere to the four axioms of player engagement: “Efficiency, Symmetry, Dummy, Additive”.64 Shapley first coined the
termSHAPin1951.Itisusedtodescribeacertainoutputdependingonhoweachinputisinvolvedinaprediction.
Table 10, along with Figures 7 and 8, unveils the mean SHAP values, shedding light on the pivotal role of selected
attributeswithintheframeworkofapredictivemodel.TheutilizationofSHAPvaluesfacilitatesanuancedunderstanding
ofeachattribute’scontributiontothemodel’soutput.Remarkably,theOldBalanceOrgattributetakesprecedencewiththe
highest mean SHAP value of 0.065, signifying its discernibly stronger impact on the model’s predictive outcomes. By
givingaquantifiablemeasureofattributeimpactandprovidinginsightintothemodel’sdecision-makingprocesses,these
valuesimprovetheinterpretabilityandunderstandingoffeaturesignificance.65
6 Result
The assessment of individual machine learning models underscores their exceptional performance in detecting financial
fraud,withtheDecisionTreemodelshowcasingremarkableresults.AnF1Scoreof0.893,aROCAUCScoreof0.943,
andamaximumaccuracyof99.937percentdistinguishtheDecisionTreemodelasthebestperformeramongthemodels
thatwereevaluated.

64 IntelligentDecisionTechnologies19(1)
Figure 8. SHAPvalueandfeaturevalue.
Witha99.904%accuracyrate,anF1Scoreof0.814,andaremarkableROCAUCScoreof0.990,theEnsembleLearn-
ing Model—implemented via a Voting Classifier—demonstrates itself as a strong solution. This collective performance
underscorestheefficacyofamalgamatingdiversemodelsforenhancedfrauddetection.
Todelveintotheinterpretabilityofthesemodels,athoroughSHAPanalysiswasconducted,revealingkeyattributesand
theirmeanSHAPvalues.ParticularlynoteworthywereattributessuchasOldBalanceOrg,NewBalanceOrg,Amount,New-
BlanceDest,andOldBalanceDest,whichexhibitedsignificantimpactsonmodeloutputs.Theseinsightsprovidevaluable
claritytostakeholders,fosteringadeeperunderstandingofthemodels’decision-makingprocessesandtherebyaugmenting
transparencyandinterpretabilityintherealmoffinancialfrauddetection.
7 Conclusion
Inthisresearch,wetackledthegrowingchallengesinfinancialtechnology,specificallyaddressingtherisingthreatoffraud
inmobilemoneytransactions.Whiledigitalfinancebringsconvenience,italsoexposesinstitutionstosophisticatedfraud.
OurstudyemphasizedbothhighmodelaccuracyandexplainabilitybyintegratingmachinelearningwithExplainableAI,
leveragingSHAPanalysis.Thisworknotonlyadvances fraudpreventionindigitalfinancebutalsosetsaprecedentfor
transparent and interpretable machine learning systems. By prioritizing clarity, it empowers stakeholders with effective
decision-makingtoolsintheevolvingcybersecuritylandscape,markingasignificantstrideagainstfinancialfraudinthe
digitalera.
8 Future work
Thefutureoffinancialfrauddetectionandpreventioninvolvesintegratingcutting-edgetechnologiestocombatsophisti-
catedfraudschemes.Keyadvancementsincludethedevelopmentofreal-timeanalysisandadaptivesystemsfordynamic
threat response, the use of behavioral biometrics for enhanced user recognition, blockchain technology for immutable
andtransparentledgers,quantum-resistantencryptionmethods,collaborativethreatintelligencesharing,theexamination
ofnon-financialdataforcontextualinsights,regulatorycompliancesolutionsleveragingadvancedtechnologies,andAI-
driven user authentication processes. These innovations aim to create more resilient and intelligent systems, crucial for
stayingaheadintheever-evolvinglandscapeofdigitalfinance.
Statementsanddeclarations
Ethicalapproval
Informedconsent
Funding
Theauthorsreceivednofinancialsupportfortheresearch,authorship,and/orpublicationofthisarticle.

VijayanandandSmrithy 65
Declarationofconflictinginterests
Theauthorsdeclarednopotentialconflictsofinterestwithrespecttotheresearch,authorship,and/orpublicationofthisarticle.
References
1. https://www.acfe.com/about-the-acfe/newsroom-for-media/press-releases/press-release-detail?s=ACFE-Estimates-Organizations-
Lose-5-percent-to-Fraud
2. https://www.statista.com/outlook/dmo/fintech/digital-payments/worldwide
3. https://cybersecurityventures.com/cybercrime-damages-6-trillion-by-2021/
4. https://www.europol.europa.eu/cms/sites/default/files/documents/Spotlight-Report_Online-fraud-schemes.pdf
5. https://risk.lexisnexis.com/about-us/press-room/press-release/20221116-study-finds-fraud-costs
6. https://www.forbes.com/sites/louiscolumbus/2020/10/31/the-state-of-ai-adoption-in-financial-services/?sh=739a49282aac
7. HallPandGillN.Anintroductiontomachinelearninginterpretability.Sebastopol,CA:O’ReillyMedia,Incorporated,2019.
8. AliA,AbdRazakS,OthmanSH,etal.Financialfrauddetectionbasedonmachinelearning:asystematicliteraturereview.Appl
Sci2022;12:9637.
9. Al-HashediKGandMagalingamP.Financialfrauddetectionapplyingdataminingtechniques:acomprehensivereviewfrom2009
to2019.ComputSciRev2021;40:100402.
10. WickramanayakeB,GeeganageDK,OuyangC,etal.Asurveyofonlinecardpaymentfrauddetectionusingdatamining-based
methods.arXivpreprintarXiv:2011.14024(2020).
11. SenguptaKandDasPK.Detectionoffinancialfraud:comparisonsofsometree-basedmachinelearningapproaches.JDataInf
Manag2023;5:23–37.
12. LiuZ,YeRandYeR.Detectingfinancialstatementfraudwithinterpretablemachinelearning,2021.
13. HilalW,GadsdenSAandYawneyJ.Financialfraud:areviewofanomalydetectiontechniquesandrecentadvances.ExpertSyst
Appl2022;193:116429.
14. MittalSandTyagiS.Computationaltechniquesforreal-timecreditcardfrauddetection.Handbookofcomputernetworksand
cybersecurity:principlesandparadigms,2020,pp.653–681.
15. GuptaBB,PerezGM,AgrawalDP,etal.Handbookofcomputernetworksandcybersecurity.Springer2020;10:978–973.
16. SadgaliI,SaelNandBenabbouF.Performanceofmachinelearningtechniquesinthedetectionoffinancialfrauds.ProcComput
Sci2019;148:45–54.
17. AlghofailiY,AlbattahAandRassamMA.AfinancialfrauddetectionmodelbasedonLSTMdeeplearningtechnique.JAppl
SecurRes2020;15:498–516.
18. Alarfaj FK, Malik I, Khan HU, et al. Credit card fraud detection using state-of-the-art machine learning and deep learning
algorithms.IEEEAccess2022;10:39700–39715.
19. IleberiE,SunYandWangZ.PerformanceevaluationofmachinelearningmethodsforcreditcardfrauddetectionusingSMOTE
andAdaBoost.IEEEAccess2021;9:165286–165294.
20. Esenogho E, Mienye ID, Swart TG, et al. A neural network ensemble with feature engineering for improved credit card fraud
detection.IEEEAccess2022;10:16400–16407.
21. AlfaizNSandFatiSM.Enhancedcreditcardfrauddetectionmodelusingmachinelearning.Electronics2022;11:662.
22. AwosikaT,ShuklaRMandPranggonoB.Transparencyandprivacy:theroleofexplainableAIandfederatedlearninginfinancial
frauddetection.arXivpreprintarXiv:2312.13334,2023.
23. Jayasinghe SL, Thomas DT, Anderson JP, et al. Global application of regenerative agriculture: a review of definitions and
assessmentapproaches.Sustainability2023;15:15941.
24. SharmaN,ChakrabartiAandBalasVE.Datamanagement,analyticsandinnovation.ProcICDMAI2019;1:1–740.
25. https://bjs.ojp.gov/taxonomy/term/financial-fraud
26. https://www.itu.int/en/ITU-T/techwatch/Pages/mobile-money-standards.aspx#:∼:text=Mobile%20money%20refers%20to%20
financial,directly%20to%20a%20bank%20account
27. MunaRK,HossainMI,AlamMGR,etal.DemystifyingmachinelearningmodelsofmassiveIoTattackdetectionwithexplainable
AIforsustainableandsecurefuturesmartcities.IoT2023;24:100919.
28. GardnerC.Classifyingimbalancedfinancialfrauddatautilizingenhancedrandomforestalgorithm,2020.
29. Lopez-RojasEA,ElmirAandAxelssonS.PaySim:Afinancialmobilemoneysimulatorforfrauddetection.In:The28thEuropean
ModelingandSimulationSymposium-EMSS,Larnaca,Cyprus,2016.
30. AshendenSK,ed.Theeraofartificialintelligence,machinelearning,anddatascienceinthepharmaceuticalindustry. Cambridge,
MA:AcademicPress,2021.
31. SeufertEB.Thefreemiumbusinessmodel.FreemiumEconomics,2014,pp.1–27.
32. GudivadaVN,IrfanMT,FathiE,etal.Cognitiveanalytics:goingbeyondbigdataanalyticsandmachinelearning.In:Handbook
ofstatistics.Vol.35.Amsterdam,Netherlands:Elsevier,2016,pp.169–205.

66 IntelligentDecisionTechnologies19(1)
33. AlMamunMHandKeikhosrokianiP.Predictingonset(type-2)ofdiabetesfrommedicalrecordsusingbinaryclassclassification.
In:Bigdataanalyticsforhealthcare.Cambridge,MA:AcademicPress,2022,pp.301–312.
34. Keikhosrokiani P, ed. Big data analytics for healthcare: datasets, techniques, life cycles, management, and applications.
Cambridge,MA:AcademicPress,2022.
35. KohaviR.Scalinguptheaccuracyofnaive-bayesclassifiers:Adecision-treehybrid.InKdd,1996,August,Vol.96,pp.202–207.
36. ChatterjeeA,BalaP,GedamS,etal.Machinelearninganddeeplearning-basedadvancedclassificationtechniquesforthedetection
ofmajordepressivedisorder.AslibJInfManag2023.
37. Mishra A and Suhas MV. Classification of benign and malignant bone lesions on CT images using random forest. In 2016
IEEEinternationalconferenceonrecenttrendsinelectronics,Information&CommunicationTechnology(RTEICT),2016,May,
pp.1807–1810).IEEE.
38. Chu G, Lo P, Ramakrishna B, et al. Bone tumor segmentation on bone scans using context information and random forests.
InMedicalImageComputingandComputer-AssistedIntervention–MICCAI2014:17thInternationalConference,Boston,MA,
USA,September14–18,2014,Proceedings,PartI17,2014,pp.601–608.SpringerInternationalPublishing.
39. NguyenC,WangYandNguyenHN.Randomforestclassifiercombinedwithfeatureselectionforbreastcancerdiagnosisand
prognostic.2013.
40. ShrivastavaD,SanyalS,MajiAK,etal.Bonecancerdetectionusingmachinelearningtechniques.In:Smarthealthcarefordisease
diagnosisandprevention.Cambridge,MA:AcademicPress,2020,pp.175–183.
41. RamrajS,UzirN,SunilR,etal.ExperimentingXGBoostalgorithmforpredictionandclassificationofdifferentdatasets.IntJ
ControlTheoryAppl2016;9:651–662.
42. SubasiA,PanigrahiSS,PatilBS,etal.Advancedpatternrecognitiontoolsfordiseasediagnosis.In:5GIotandedgecomputing
forsmarthealthcare.Cambridge,MA:AcademicPress,2022,pp.195–229.
43. https://lightgbm.readthedocs.io/
44. Mehta M, Agrawal R and Rissanen J. SLIQ: A fast scalable classifier for data mining. In Advances in Database
Technology—EDBT’96:5thInternationalConferenceonExtendingDatabaseTechnologyAvignon,France,March25–29,1996
Proceedings5,1996,pp.18–32.SpringerBerlinHeidelberg.
45. ShaferJ,AgrawalRandMehtaM.SPRINT:Ascalableparallelclassifierfordatamining.InVldb,1996,September,Vol.96,
pp.544–555.
46. AlsabtiK,RankaSandSinghV.CLOUDS:Adecisiontreeclassifierforlargedatasets,1998.
47. JinRandAgrawalG.Communicationandmemoryefficientparalleldecisiontreeconstruction.InProceedingsofthe2003SIAM
internationalconferenceondatamining,2003,May,pp.119–129.SocietyforIndustrialandAppliedMathematics.
48. LiP,WuQandBurgesC.Mcrank:Learningtorankusingmultipleclassificationandgradientboosting.AdvNeurInfProcessSyst
2007;20:897–904.
49. https://lightgbm.readthedocs.io/en/latest/README.html
50. KobayashiA.Internationalencyclopediaofhumangeography.Amsterdam,Netherlands:Elsevier,2019.
51. Guenther FH. Neural networks: Biological models and applications. Oxford: International Encyclopedia of the Social &
BehavioralSciences,2001,pp.10534–10537.
52. PolikarR.Ensemblelearning.Ensemblemachinelearning:Methodsandapplications,2012,pp.1–34.
53. BENNOUHRandOussamaAIADI.Ahealthcaresystemusingdeeplearning(Doctoraldissertation),2022.
54. SchneiderPandXhafaF.AnomalydetectionandcomplexeventprocessingoverIoTdatastreams:withapplicationtoEHealth
andpatientdatamonitoring.Cambridge,MA:AcademicPress,2022.
55. ManconiA,ArmanoG,GnocchiM,etal.Asoft-votingensembleclassifierfordetectingpatientsaffectedbyCOVID-19.ApplSci
2022;12:7554.
56. AftabiSZ,AhmadiAandFarziS.FrauddetectioninfinancialstatementsusingdataminingandGANmodels.ExpertSystAppl
2023;227:120144.
57. Saranya A and Subhashini R. A systematic review of Explainable Artificial Intelligence models and applications: recent
developmentsandfuturetrends.DecisAnalJ2023:100230.
58. https://www.darpa.mil/program/explainable-artificial-intelligence
59. https://onlinelibrary.wiley.com/toc/26895595/2021/2/4
60. https://xaitk.org/
61. https://higherlogicdownload.s3.amazonaws.com/ISACA/71336a0d-5200-45d1-ba3d-b1b5116f8456/UploadedImages/2023_
Documents/ISACA_KE_Newsletter_2023_Edition.pdf
62. VandenBroeckG,LykovA,SchleichM,etal.OnthetractabilityofSHAPexplanations.JArtifIntellRes2022;74:851–886.
63. Linardatos P, Papastefanopoulos V and Kotsiantis S. Explainable AI: a review of machine learning interpretability methods.
Entropy2021;23:18.

VijayanandandSmrithy 67
64. LohHW,OoiCP,SeoniS,etal.Applicationofexplainableartificialintelligenceforhealthcare:asystematicreviewofthelast
decade(2011–2022).ComputMethodsProgramsBiomed2022;226:107161.
65. KademM,NoseworthyMandDoyleT.XGBoostforinterpretableAlzheimer’sdecisionsupport.ProcAAAISymposSer2023;
1:135–141.