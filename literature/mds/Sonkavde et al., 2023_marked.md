---
conversion_metadata:
  converted_at: "2026-10-12T07:44:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Sonkavde et al., 2023.pdf"
  source_pdf_sha256: "2f18f5621edef0660100ffecbfef797bb9f16d5b35182f3ea86a6a58a70f0c23"
  page_count: 22
  markdown_char_count: 81607
---

International Journal o f
Financial Studies
Review
Forecasting Stock Market Prices Using Machine Learning and
Deep Learning Models: A Systematic Review, Performance
Analysis and Discussion of Implications
GaurangSonkavde1,DeepakSudhakarDharrao2,* ,AnupkumarM.Bongale1,* ,SarikaT.Deokate3 ,
DeepakDoreswamy4 andSubrayaKrishnaBhat5
1 DepartmentofArtificialIntelligenceandMachineLearning,SymbiosisInstituteofTechnology,Symbiosis
InternationalDeemedUniversity,Pune412115,Maharashtra,India;gaurangsonkavade@gmail.com
2 DepartmentofComputerScience&Engineering,SymbiosisInstituteofTechnology,SymbiosisInternational
DeemedUniversity,Pune412115,Maharashtra,India
3 DepartmentofComputerEngineering,PimpriChinchwadCollegeofEngineering,
Pune411044,Maharashtra,India;sarika.deokate@pccoepune.org
4 DepartmentofMechatronics,ManipalInstituteofTechnology,ManipalAcademyofHigherEducation,
Manipal576104,Karnataka,India;deepak.d@manipal.edu
5 DepartmentofMechanicalandIndustrialEngineering,ManipalInstituteofTechnology,ManipalAcademyof
HigherEducation,Manipal576104,Karnataka,India;sk.bhat@manipal.edu
* Correspondence:deepak.dharrao@sitpune.edu.in(D.S.D.);anupkumar.bongale@sitpune.edu.in(A.M.B.)
Abstract:Thefinancialsectorhasgreatlyimpactedthemonetarywell-beingofconsumers,traders,
and financial institutions. In the current era, artificial intelligence is redefining the limits of the
financialmarketsbasedonstate-of-the-artmachinelearninganddeeplearningalgorithms.There
Citation:Sonkavde,Gaurang, isextensiveuseofthesetechniquesinfinancialinstrumentpriceprediction,markettrendanalysis,
DeepakSudhakarDharrao, establishinginvestmentopportunities,portfoliooptimization,etc.Investorsandtradersareusing
AnupkumarM.Bongale,SarikaT. machinelearninganddeeplearningmodelsforforecastingfinancialinstrumentmovements.With
Deokate,DeepakDoreswamy,and thewidespreadadoptionofAIinfinance,itisimperativetosummarizetherecentmachinelearning
SubrayaKrishnaBhat.2023. anddeeplearningmodels,whichmotivatedustopresentthiscomprehensivereviewofthepractical
ForecastingStockMarketPrices applicationsofmachinelearninginthefinancialindustry. Thisarticleexaminesalgorithmssuch
UsingMachineLearningandDeep
assupervisedandunsupervisedmachinelearningalgorithms, ensemblealgorithms, timeseries
LearningModels:ASystematic
analysisalgorithms,anddeeplearningalgorithmsforstockpricepredictionandsolvingclassification
Review,PerformanceAnalysisand
problems. Thecontributionsofthisreviewarticleareasfollows: (a)itprovidesadescriptionof
DiscussionofImplications.
machinelearninganddeeplearningmodelsusedinthefinancialsector;(b)itprovidesageneric
InternationalJournalofFinancial
frameworkforstockpricepredictionandclassification;and(c)itimplementsanensemblemodel—
Studies11: 94. https://doi.org/
“RandomForest+XG-Boost+LSTM”—forforecastingTAINIWALCHMandAGROPHOSstock
10.3390/ijfs11030094
pricesandperformsacomparativeanalysiswithpopularmachinelearninganddeeplearningmodels.
AcademicEditor:Muneer
M.Alshater
Keywords: stockmarket;finance;linearregression;randomforest;XG-Boost;FBProphet;LSTM;
Received:22April2023 ensemblelearning;blendingensemble
Revised:13July2023
Accepted:19July2023
Published:26July2023
1. Introduction
Theperformanceofacountry’sfinancialmarketisacrucialdeterminantofitsoverall
economic condition, enabling economists and financial experts to gauge the country’s
Copyright: © 2023 by the authors.
currenteconomichealth. Amongthevariousfinancialmarkets,thestockmarketstands
Licensee MDPI, Basel, Switzerland.
outasakeydrivingforce. Acountry’seconomicsituationdirectlyorindirectlyimpacts
This article is an open access article
sectorssuchasfinance,agriculture,metal,andinvestmentbanking,amongothers. The
distributed under the terms and
growthofthesesectorshingesontheirvolatility,whichfollowsthefundamentalprinciple
conditionsoftheCreativeCommons
Attribution(CCBY)license(https:// ofsupplyanddemand. Thedemandforaparticularsectordirectlyinfluencesthestock
creativecommons.org/licenses/by/ market,withincreasedsupplypromptingtradersandfinancialinstitutionstoinvestinthat
4.0/). sectororstock,drivingupprices. Additionally,regulardividendpaymentscontributeto
Int.J.FinancialStud.2023,11,94.https://doi.org/10.3390/ijfs11030094 https://www.mdpi.com/journal/ijfs

Int.J.FinancialStud.2023,11,94 2of22
thegenerationofprofitsandreturnsoninvestedcapital. Itisimperativeforinvestorsto
identifytheopportunemomenttosellsharesandachievetheirdesiredreturns. Financial
marketsencompassvarioustypesofmarket,includingstockmarkets,derivativesmarkets,
bondmarkets,andcommoditymarkets(Obthongetal.2020). Thestockmarketservesasa
platformforinvestorstoinvestinandownaportionorfractionofacompany.Ascompanies
grow,theyoftenrequireadditionalfundingtosupporttheirfutureendeavors. Following
the approval of current shareholders, who face diluted ownership due to the issuance
of new shares, companies can sell these shares to investors to raise capital. Successful
outcomesresultinincreasedstockmarketvaluefortheshares.
Shareslistedonthestockmarketcanbeboughtforbothshort-termandlong-term
investmentstrategies. Long-terminvestmentinvolvesholdingsharesoveranextended
period, while short-term investments involve buying and selling shares within shorter
timeframes,withinvestorsaimingforprofitswithindaysorweeks. Tradersemployawide
rangeoftradingstrategies,includingswingtrading,daytrading,positiontrading,and
scalping(MannandKutz2016).
Duetotheunpredictablenatureofthestockmarket,itishighlydifficultforindividu-
alstoobtainreturnsontheirinvestments. Primary,fundamental,andtechnicalanalysis
arepopularapproachestounderstandingmarkettrends(ManishandThenmozhi2014),
but they possess inherent limitations due to the involvement of lagging indicators and
predictioninaccuracy. Thishasmotivatedresearcherstodevelopimprovedtechniquesfor
real-timemarketscenariosbasedonmachinelearninganddeeplearningmodels.Inthecur-
rentera,machinelearninganddeeplearningalgorithmsoffersubstantialadvantagesover
traditionaltechniquessuchastechnicalandfundamentalanalysis. Leveragingthepower
ofmachinelearningandartificialintelligence,thesealgorithmsfacilitatetheforecasting
ofstockpricesandindices. Machinelearningservesasanadditionalapproachalongside
technicalandfundamentalanalysis,withthecombinationofthesetoolsformingapowerful
trading platform. Machine learning models can provide solutions to problems such as
stockpriceforecastingandclassification,portfoliomanagement,algorithmictrading,stock
market sentiment analysis, risk assessment, etc. Of these problems, this review article
is focused on exploring different approaches described for stock price forecasting and
classification.
The typical steps of a machine learning model pipeline for predicting stock price
involveseveralphases: collectinghistoricaldataviaanAPI,pre-processingthedata,creat-
ingaforecastingmodel,andevaluatingthemodel. Pre-processingentailsremovingzero
values,eliminatingduplicates,andscalingfeatures. Subsequently,importantfeaturesare
shortlisted,andvaliddataareselectedforstockpricepredictionorforecasting(Raghaven-
dra et al. 2021). In this article, numerous popular machine learning and deep learning
algorithms,suchaslinearregression,randomforest,logisticregression,k-nearestneighbor,
supportvectormachine,naïveBayes,ARIMA(autoregressiveintegratedmovingaverage),
FBProphet(FacebookProphet),LSTM(longshort-termmemory),GRU(gatedrecurrent
network),aswellasensemblealgorithmssuchasrandomforestandXG-Boost(extreme
gradientboosting),aredescribed(ZhongandEnke2019;SidraandSen2020;Parrayetal.
2020). Forevaluatingaclassificationmodel’saccuracy,recall,precision,andF-score,are
commonlypreferredmetrics,andforregressionorpriceforecastingmodels,rootmean
squareerror(RMSE)andmeanabsolutepercentageerror(MAPE)areoftenemployed(Jose
etal.2019).
Thereareasignificantnumberofreviewarticlesonstockpricepredictionandfore-
casting(Polamurietal.2019;Kumaretal.2021;Sonietal.2022). Butduetotheboomin
artificialintelligenceandmachinelearning,thefrequencyofpublicationshasincreased
considerably. Hence,thisreviewarticlepresentsrecentstate-of-the-artmachinelearning
and deep learning techniques for stock price prediction. The salient contributions and
uniquenessofthisreviewarticlearelistedbelow:
• Oneoftheuniquecontributionsofthisreviewarticleisthatitisnotjustlimitedto
summarizing the research articles. Extra effort is put into implementing the well-

Int.J.FinancialStud.2023,11,94 3of22
knownmachinelearninganddeeplearningmodelstounderstandtheirnatureand
performance. Alongwithourreview,acomparativeanalysisofvariousalgorithmsis
presentedinthisarticle. Themachinelearninganddeeplearningensemblealgorithms
are tested on TAINIWALCHM and AGROPHOS stock data, which fall under the
umbrellaofthechemicalindustrymarketsector.
• Inthisreviewarticle,detailedfutureresearchdirectionsareincluded. Futureresearch
avenues for researchers are identified based on the conducted study stock trend
analysisandclassification,patternidentification,andcandlestickchartpatternanalysis
usingcomputervision.
Therestofthearticleisorganizedasfollows. Section2describesthecompletetheo-
reticalbackgroundofmachinelearninganddeeplearningmodels. Agenericstructureof
themachinelearningmodelingpipelineispresentedinSection3. Theimportanceofthe
ensemblemodel“RandomForest+XG-Boost+LSTM”forforecastingTAINIWALCHM
andAGROPHOSstockpricesandacomparativeanalysiswithpopularmachinelearning
anddeeplearningmodelsarementionedinSection4. Section5discussestheimplications
and limitations of the current review. Future research directions are given in Section 6.
Finally,thepaperisconcludedinSection7.
2. ComprehensiveSummaryofTheoreticalBasis
Forecasting stock prices and predicting market trends are challenging tasks. Over
theyears,researchershaveproposedseveralsolutionstothesechallenges(Obthongetal.
2020;Huetal.2021;Polamurietal.2019),andthesemethodsarebrieflyexplainedbelow.
Machine learning, deep learning, time series forecasting, and ensemble algorithms are
some of the most popular approaches to solving the mentioned problems. Ensemble
algorithmscanimproveaccuracyandreduceRMSE.Hadooparchitecturescanalsohandle
large volumes of stock data (Jose et al. 2019) and deep learning algorithms can predict
financialmarkets(Huetal.2021). StockforecastingusingLSTM,auniquerecurrentneural
network(RNN),overcomeslong-termdependency(Qiuetal.2020;Baniketal.2022). But
thevanishinggradientandexplodinggradientproblemsoftenneedtobeaddressedin
RNN-basedarchitectures(LiandPan2021;Zhu2020). Khanetal.,in(Khanetal.2020),
usedPyspark,MLlib,linearregression,andrandomforesttoachieve80–98%accuracy.
Multiplealgorithmshavebeenusedtoforecaststockprices,includingneuralnetworks,
which train data on layers of connected neurons, and support vector machines, which
predict stock price movement using hyperplanes. Random forest, trained on multiple
decisiontreesandNaïveBayes,predictsstockmovementbasedonnegativeorpositive
probabilityusingRelianceandInfosys’10-yearhistoricaldata(Pateletal.2015). Random
forestiscomparedtootheralgorithmson5767Europeancompanies. Thesealgorithms
includeneuralnetworks,whicharemultiplelayersofneuronsconnectedwitheachother;
logisticregression,whichoutputsabinaryvaluetopredictwhetherthestockwillmoveup
ordownbasedonprobability;supportvectormachines;andK-Nearestneighbor,which
findstheknearestdatapointsusingEuclideansimilaritymetrics. Randomforestisthebest
algorithm,followedbySVM(Ballingsetal.2015).
Stockmarketforecastingisaregressionusecasebecausestockpricesarecontinuous
(Seethalakshmi2018).(DiPersioandHonchar2017),usedRNNforforecastingGooglestock
prices. RNN,LSTM,andGRUarethethreemostefficientneuralnetworksforsequential
data. RNNisusedforhistoricaldata. LSTMandGRUcanavoidthevanishinggradient
problembasedonforget,reset,andupdategates. GRUisfoundtobefasterasitoperates
onresetandupdategates(DiPersioandHonchar2017).
AnotherstudyinvolvestheuseofARIMA,LSTM,andrandomforestforpricefore-
casting,andXG-Boost,anensemblelearningalgorithmlikerandomforest. Basedonthe
evaluationparameters,XG-BoostoutperformedARIMAandLSTM(ZhuandHe2022).
Isaacetal.alsousedensemblemachinelearningtoimprovestockmarketforecastingresults.
Cooperativeandcompetitiveclassifieralgorithmsusestackingandblending. Baggingand
boostingtechniquesareusedtoreducevarianceandbias. Mostensembleclassifiersand

Int.J.FinancialStud.2023,11,94 4of22
regressorsaredevelopedbycombiningdecisiontrees,supportvectormachines,andneural
networks(Ntietal.2020). Similarly,(Xuetal.2020)alsousedbaggingensemblelearning
techniquestopredictChinesestocks.Thisapproachcombinesatwo-stagepredictionmodel
called“EnsembleLearningSVRandRandomForest(E-SVR&RF)”withKNNtoclusterit
withtentechnicalindicators. AnotherproposedmethodusesEnsembleLSTMwithCNN
onstockindexesfortrainingadversarialnetworks,whichcanhelpforecasthigh-frequency
stockandhasadvantageslikeadversarialtrainingandreducingdirectionpredictionloss
andforecasterrorloss(Zhouetal.2018). Toenhancetheeffectivenessofensemblemodel
ofXG-BoostandLSTM,XG-Boostisusedtoselectfeaturesappliedtohigh-dimensional
timeseriesdataandLSTMisusedforstockpriceforecasting(Vuongetal.2022).
Notonlyhavemachinelearningensemblemethodshelpedtoimproveforecasting
performance,butinsomeresearchwork,ithasalsobeenobservedthatneuralnetwork
blendingensemblemodelsalsoperformwell. (Yang2019)implementedamodelconsisting
oftwolayersofRNN.ThefirstonewasanLSTM-basedblendingensemblealgorithm,and
thesecondonewasGRU-based. ThemodelshowedthelowestRMSEvalueof186.32,a
precisionof60%,andanF1-scoreof66.47(LiandPan2021).
Sometimes,pricemovementisprimarilyaffectedbysentiments. Thesesentimentscan
bepositive,leadingtoabullishmovement,ornegative,leadingtoabearishmovement.
Hence, stocksentimentanalysisisimportanttounderstandstockpriceforecastingand
trendclassification. Further,inthissection,weexploresomeforecastingtechniquesbased
onsentimentanalysis. Socialmediadata,companynews,andtrendanalysiscanclassify
investors’stocksentimentsaspositive,negative,orneutral(YadavandVishwakarma2019).
Sincestockpricesrespondtonewsandglobalevents,pricevariationalonecannotbe
usedtotrainMLmodels. ANN-andLSTM-baseddeeplearningtechniquescanalsobe
trainedusingpricevaluesandtextdata. Word2vecandNGramareusedtoconverttext
datatonumericaldataandtrainthemodeltogetherwithprice-sentimentdata. Diversified
datacanpredominantlyincreaseaccuracyandlowerinaccurateresults. Analgorithmlike
arandomforestapproachisalsoagoodchoiceforTwittersentimentanalysis(Kumarand
Ningombam2018;Reddyetal.2020).
Financialnewsanduser-generatedtext,suchascommentsonsocialmediaplatforms,
cantriggernewtrendsinthestockmarket. Forexample,“Mondayhasthelowestaverage
return”showsastatementrepresentingaweakornegativesentiment.
Whilecreatingthedatasetfortrainingthemodel,arollingwindowapproachonhistorical
dataworkswellwithnews-basedtextdata.Renetal.showedanincreaseinaccuracyofupto
18.6%to89.93%pointswhenmultimodaldatawereconsidered(Renetal.2019).
Whentextdataarecollected,theycanincludecorrectandfakedata. Inonestudy,the
authorsusedfeatureselectiontoeliminatefakenewsandspamtweetscollectedfromsocial
mediadata. Thisimprovedthedataqualityfortraining,andaclassificationalgorithm,the
randomforestalgorithm,wasusedtotrainthemodel. Sentimentscanbepositive,neutral,
ornegative, whichhelpspeopledecidewhethertobuyorsellstock(Bahetietal.2021).
Negativesentimentsaffectmarketconditions. Limetal. consideredausecaseinwhich
acomparisonoftwostocks,TeslaandNio,basedonsentiments,wascarriedout. Itwas
foundthatnegativeevents,suchasTesla’s2021protest,affecteditscompetitor,Nio,aswell.
Thisresearchwasbasedonhistoricaldatausingtimeseriesforecastingwith10,15,and20
daysofdata(LimandTan2021).
In(Sharafetal.2022),newsheadlinespertainingtoTSLA,AMZ,andGOOGstockwere
consideredtoobtaingood-qualitydatatoreducespamtweetsthroughfeatureselectionmethods.
Sentimentanalysiswasalsousedforpolaritydetectionandhistoricaldatamining,forwhich
DLalgorithmswereused.Similarfeatureengineering-anddeeplearning-basedapproachesare
presentedin(ShenandShafiq2020;Nabipouretal.2020;Mohapatraetal.2022).
(Khairietal.2019)showedthattechnicalanalysiswithsentimentanalysiscanalso
provideprominentinvestmentopportunities.Technicalindicatorslikestochasticoscillators,
movingaverageconvergencedivergence(MACD),Bollingerbands,andrelativestrength
indicators(RSI)aregoodforshort-termanalysisbutnotlong-term. Incasesofnegative

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 5 of 23
mining, for which DL algorithms were used. Similar feature engineering- and deep learn-
ing-based approaches are presented in (Shen and Shafiq 2020; Nabipour et al. 2020; Mo-
hapatra et al. 2022).
(Khairi et al. 2019) showed that technical analysis with sentiment analysis can also
Int.J.FinancialStud.2023,11,94 provide prominent investment opportunities. Technical indicators like stochastic os5ciolfla22-
tors, moving average convergence divergence (MACD), Bollinger bands, and relative
strength indicators (RSI) are good for short-term analysis but not long-term. In cases of
nneegwast,ivgee nneerwasll,y g,emnaerrkaleltyt, rmenadrksewt itlrlebnedsb ewairlils bhe, abnedartihshe, satnodck thper iscteowcki lplrfiaclel. wTiolla fdadll.r eTsos
athdidsriesssus eth,iins iitsiasulsee, nintiimtiaeln steanntaimlyesnist caannablyespise crfaonr mbee dpetorfofirnmdetdh eton efignadti vtheen newegsautisvien gnePwoSs
(upsainrtg oPfosSp (epeacrht) otfa gspseienchth) etangesw ins sthtaet enmewens ts.taPtreomgreanmt. mPrionggralimbrmariinegs lliibkreaSrieenst liiWkeo rSdeNntei-t
WcanorbdeNuets ecdanf obreP uosSedta fgogri nPgo.S Ttahgisgianpgp. rTohaicsh ahpapsroreascuhl theads irneshuilgtehdp irno fihtiagbhi lpitryofiantadbilloitwy
alonsds -lmowak lionsgs-smitaukaitniogn ssit(uKahtiaoinris e(Ktahla.i2r0i 1e9t )a.l.I n20a1n9o).t hIne ranapotphreora acphpprrooapcohs pedrobpyosLeide btya lL.i( Leti
aaln. d(LBi aasntods B2a0s2t0o)s, a20t2ec0h),n ai ctaelcahnnaiclyasl iasnoaflyhsisisto orfi chailsdtoartiacaaln ddaataf uanndda am feunntdalaamneanlytasli saunsailnygsias
udseienpgl ae adreneinpg leaaprpnrinogac ahpwpreoraeccho wndeurec tceodntdougcetende rtaot egebneettrearter ebteuttrners .reHtuerren,sL. HSTeMre,i sLSchToMse ins
cfohropserned fiocrt ipornedasicittiocann asst iotr ceamn estmoroer ymaenmdodroye asnndo dtoheasv enoatv haanviesh ai nvgangirsahdiniegn gtrisasduieen(Lt iisasnude
(BLais atonsd2 B0a2s0t)o.sS i2m02il0a)r. Swimoriklairs wproerske nist epdreinse(nAtegdra iwn a(Alegtraalw.2a0l 2e2t ;aSla. t2h0i2s2h; KSautmhiasrh eKtualm.2a0r2 e0t;
aUl.m 2e0r20et; Ualm.2e0r1 e9t) .al. 2019).
BBaasseedd oonn tthhee ssttuuddiieess pprreesseenntteedd ssoo ffaarr,, tthhee bbeesstt ssttoocckk mmaarrkkeett ffoorreeccaassttiinngg ssoolluuttiioonn iiss
ddeerriivveedd ffrroommf ufunnddaammenentatlaal naanlaylsyissiasn adntde cthenchicnailcaanl aalynsailsywsisit hwsiethn tsimenetnimtaennatl yasnisalaynsdisd aenedp
dleeaerpn ilnegarmniondge mls.oEdnelsse.m Enbsleemtebchlen tieqcuhensipqruoevsi pdreoevsipdeec eiaslplyecpiarollmy pisrionmgfiosirnegca fsotriencgaostuintcgo omuets-.
cTohmeeaslg. oTrhiteh amlgsotrhitahtmarse tuhsaet darfeo russteodc kfomr satrokcekt mpraerdkiectt ipornedbiyctcioonns bidye croinngsirdeesreianrgc hrepseaaprecrhs
aregiveninFigure1.
papers are given in Figure 1.
Figure 1. Stock forecasting algorithm.
Figure1.Stockforecastingalgorithm.
22..11.. BBaassiicc MMaacchhiinnee LLeeaarrnniinngg AAllggoorriitthhmm
22..11..11.. LLiinneeaarr RReeggrreessssiioonn
Linearregressionisusedforstockorfinancialmarketpredictiontoforecastthefuture
Linear regression is used for stock or financial market prediction to forecast the future
priceofstockregressionandusesamodelbasedononeormoreattributes,suchasclosed
price of stock regression and uses a model based on one or more attributes, such as closed
price,openprice,volume,etc.,toforecastthestockprice. Regressionmodelingaimsto
price, open price, volume, etc., to forecast the stock price. Regression modeling aims to
simulatethelinearrelationshipbetweenthedependentandindependentvariables. The
simulate the linear relationship between the dependent and independent variables. The
linearregressionmodelproducesabest-fitlinethatdescribestheconnectionbetweenthe
linear regression model produces a best-fit line that describes the connection between the inde-
independentfactorsandthedependentvariable.
pendent factors and the dependent variable.
Inthistechnique,astraightlinerepresentedbyEquation(1)isdrawn,ensuringthat
In this technique, a straight line represented by Equation (1) is drawn, ensuring that
thelinecrossesthehighestpossiblenumberofthedataset’sdatapoints. Whencharting
the line crosses the highest possible number of the dataset’s data points. When charting the
thedataset’svaluesonagraph,astraightlineismathematicallyfittedbetweenthepoints
sothatthesquareofthedistanceordifferencebetweeneachpointandthelineisassmall
aspossible. Foreachgivenx,thehypothesislineisusedtoforecastthevalueofy. This
forecastingmethodisknownaslinearregression. Fortheevaluationoftheresultsand
to check how well the model fits the line, parameters such as RMSE, MAE, MSE, and
R-squaredareused(Gururajetal.2019;DospinescuandDospinescu2019).
O = S +K (1)
x

Int.J.FinancialStud.2023,11,94 6of22
whereOistheoutput,S representstheslope,andKisaconstant.
x
2.1.2. K-NearestNeighbor(KNN)
KNNisaclassificationandregressiontechniqueandhasbeentermedasalazylearner
becauseitdoesnotneedahugetimeperiodforlearning. OneofKNN’sadvantagesisthat
itisoneoftheeasiestMLalgorithms. TheonlyactionthatneedstobetakenforKNNisto
calculatethevalueofKandtheEuclideandistance. Thisalgorithm’sslowlearningaspect
makesitquickerthanotheralgorithms. Itmaynotgeneralizewellforbigdatasinceit
skipsthelearningstep(TanuwijayaandHansun2019). Theeuclideandistancecalculation
isgiveninEquation(2),
(cid:113)
D(h i ,p r ) = ∑ . n l . =1 (P r −h i )2 (2)
whereP representsthepredictedvalueandh representsthedatavalue.
r i
2.1.3. SupportVectorMachine(SVM)
StockmarketpredictionusinganSVMcanbethemostusefultechniqueforpredicting
stockprice,asitcanbeusedasaclassificationandregressionalgorithm. Thecomparisonof
SVManditsvariants,suchas“Peeling+SVM”and“CC+SVM”,showsthatitsprediction
canbeimprovedbyadvancedSVMmethods(Grigoryan2017). Asupportvectormachine
involvessupervisedlearningusedtocategorizeaspectsusingaseparator. Theseparatoris
thendiscoveredwhenthedataareinitiallymappedtoahigh-dimensionalfeaturespace. It
findsthecategorizationofdatapointsoccurringinann-dimensionalspaceandfindsthe
optimalhyperplane. Thedatapointsaregroupedaccordingtotheirlocationinrelation
to the hyperplanes. The performance of the SVM algorithm can be elevated by tuning
parameters such as regularization, gamma, and kernel parameters (Bustos et al. 2017).
SVMcanalsobeusedforsentimentanalysistoassessinvestors’sentiments,whichwould
indirectlyaffectmarketconditions. Itiswellsuitedtobothhigh-dimensionaldatasetsand
small-scaledatasets.
2.1.4. NaïveBayesAlgorithm
NaïveBayesisasupervisedmachinelearningtechniquethatcanbeusedtoforecast
pricesofvariousstocksinresearchonbankingstock.
NaïveBayesisaclassificationalgorithminwhichacombinationofprobabilitysum-
mingupthefrequenciesandvaluecombinationsistakenfromadataset. Dependingonthe
valuesoftheclassvariables,theBayestheoremmakesanassumptionregardingwhether
the attributes of naïve Bayes are independent or interdependent. The basic concept of
naïveBayesisthatattributevaluesareindependentinthepresenceofanoutputvalue
(Setianietal.2020). ThesetupGNBmodelsweregradedbasedontheirperformanceusing
Kendall’stestofconcordanceforseveralassessmentparameters. Theoutcomesshowed
thattheGNBLDApredictivemodel(Kardanietal.2020)performedbetterthanallother
GNBmodels.TheposteriorprobabilitywascalculatedasshowninEquation(3)(Ampomah
etal.2021).
P(U|H)·P(H)
P(H|U) = (3)
P(U)
whereUisunknownclassdata, Histhehypothesisfordataofcertainclass,P(H)isthe
hypothesisprobability, P(U|H) istheprobabilityofUbeingdependentonthecondition
inhypothesisH,andP(U)istheprobabilityofU.
TheformulafornaïveBayesusedinstockpredictionisgivenbyEquation(4):
1 −
(ai−µi
. j
)2
P(A = a |B = b) = √ e 2€4ij (4)
i 1 i 2π€
whereπrepresentspi(3.14),eistheexponential(2.7183),µrepresentsthemean,and€is
thestandarddeviation.

Int.J.FinancialStud.2023,11,94 7of22
2.1.5. LogisticRegression
Logisticregressionisasupervisedmethodofmachinelearning. Byutilizingvariables
forlogisticcurves,logisticregressiongroupsseveralindependentfactorsintotwoormore
mutuallyexclusivegroupsandforecaststhelikelihoodofequitiesthatperformwell(Ali
etal.2018).Toclassifystockperformanceusinglogisticregression,themaximumlikelihood
iscalculatedasperEquation(5):
Z = β +β EPS +β PB +β ROE +β CR +β DE +β sales +V (5)
it 1 2 it 2 it 2 it 2 it 2 it 2 it it
(cid:16) (cid:17)
wherez = loglog Pr andPr=probabilityofoutcomeispositive.
1−Pr
Therearevariants,suchasbinarylogisticregression,thatcanimprovefinanceratios
andinvestors’abilitytoanticipatestockprice(Smita2021).
2.2. ForecastingofStockMarketUsingTimeSeriesForecasting
Stockpricedataaretimeseriesdata. Someoftheclassicalmethods,suchasautore-
gressivemovingaverage(ARIMA)andFBProphet,arediscussedinthissubsection. These
methodswereverywelladoptedbeforethesuccessofdeeplearningmodels.
2.2.1. ARIMA
ARIMAisanalgorithmthatusestimeseriesforecastingtopredictthefuturevalueof
stocks. InastudypresentedbyTamerlanetal.,in(Mashadihasanli2022),itisdemonstrated
that the ARIMA model best fits the stock market index. The ARIMA model comprises
three steps—identify, estimate, and diagnose. These steps can be used for forecasting
anyfinancemarketsuchasequity, derivative, etc. (Mashadihasanli2022). ARIMAcan
becombinedwithanotheralgorithm,symmetricgeneralizedautoregressiveconditional
heteroskedasticity(SGARCH),toimproveforecastingperformance. Thiscombinationhas
beenmodeledandtestedontheS&P500Index(VoandS´lepaczuk2022). ARIMAhaseven
beenextendedforstocksentimentanalysis(Kedar2021).
TheformulaofARIMA,whichcombinesAR(autoregression)andMA(movingaver-
age),isshowninEquation(6),
y (cid:48)(t) = k+β p ∗ωDy (cid:48) t−1 +···+ β p ∗ωDy (cid:48) t−p +θ 1 ∗ε t−1 +···+θq∗ε (ti−q) +ε ti (6)
where prepresentstheautoregressivemodel’sgivendegree,Disthedegreeofdifferent
orders,andqisthemovingaverage’sgivendegree.
2.2.2. FBProphetModel
FBProphetisatimeseriesforecastinglibrarydevelopedbyFacebook. FBProphet
bettersuitsdatathathaveanullvalueanditrelativelyshowsmoreaccurateresultsinsuch
situations. TheformulaofFBProphetispresentedinEquation(7):
Yt = l(t)+sp(t)+v(t)+εt, yt = g(t)+s(t)+h(t)+εn (7)
wherel(t)representsthelineartrend,sp(t)representsseasonalpatterns,v(t)represents
holidayeffects,andεnisthewhitenoiseerror.ThealgorithmdesignedbasedonFBProphet
isimplementedusingthePyStanlibrary(Sureshetal.2022). Researchershaveextensively
usedFBProphetinstockpriceforecasting(Kanindeetal.2022;Shahietal.2020).
2.3. DeepLearningMethods
Deeplearningmodelshavewide-rangingpopularityinmanyareasofscienceand
engineering. They are especially widely adopted in stock price forecasting and trend
predictionduetotheirabilitytocapturecomplexpatterns,handlelargevolumesofdata,
and undertake feature learning and representation, and their adaptability to changing
market conditions. In this subsection, some of the popular deep learning models are
discussedinrelationtothefinancedomain.

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 8 of 23
𝑌𝑡 = 𝑙(𝑡)+𝑠𝑝(𝑡)+𝑣(𝑡)+𝜀𝑡,𝑦 𝑡 = 𝑔( 𝑡 ) + 𝑠( 𝑡 ) + ℎ( 𝑡 ) + 𝜀𝑛 (7)
where 𝑙(𝑡) represents the linear trend, 𝑠𝑝(𝑡) represents seasonal patterns, 𝑣(𝑡) repre-
sents holiday effects, and 𝜀𝑛 is the white noise error. The algorithm designed based on
FB Prophet is implemented using the PyStan library (Suresh et al. 2022). Researchers have
extensively used FB Prophet in stock price forecasting (Kaninde et al. 2022; Shahi et al.
2020).
2.3. Deep Learning Methods
Deep learning models have wide-ranging popularity in many areas of science and
engineering. They are especially widely adopted in stock price forecasting and trend pre-
diction due to their ability to capture complex patterns, handle large volumes of data, and
undertake feature learning and representation, and their adaptability to changing market
conditions. In this subsection, some of the popular deep learning models are discussed in
relation to the finance domain.
2.3.1. Long Short-Term Memory (LSTM)
LSTM is an advanced model of Recurrent Neural Networks (RNNs), a deep learning
algorithm. An LSTM model can handle lengthy sequences of data units as it can remember
the data sequence, which can be used for future inputs. Figure 2 shows a general LSTM
cell structure. It comprises three gates—the input gate, the forget gate, and the
output gate. All of the gates employ the sigmoid activation function. All of the
gates used in the LSTM are mathematically represented as per Equations (8)–(10).
Input gate (New information in cell state):
Int.J.FinancialStud.2023,11,94 8of22
𝑖𝑔𝑎 = 𝜎 (𝑊 (cid:4670)ℎ ,𝑋𝑐(cid:4671) + 𝑏𝑖) (8)
(cid:3036)(cid:3043) (cid:3047)(cid:2879)(cid:2869)
Forget gate (useless information is eliminated):
2.3.1. LongShort-TermMemory(LSTM)
𝑓 = 𝜎 (𝑊 (cid:4670)ℎ ,𝑋𝑐(cid:4671) + 𝑏𝑓) (9)
(cid:3034)(cid:3028) (cid:3033)(cid:3034) (cid:3047)(cid:2879)(cid:2869)
LSTMisanadvancedmodelofRecurrentNeuralNetworks(RNNs),adeeplearning
algoOrituhtmpu.tA gnatLeS (TaMctimvaotdioenl ctoan lahsat nbdloleckle onfg fithnyals eoquutpenuct)e:s ofdataunitsasitcanremember
thedatasequence,whichcan b𝑂eus=ed 𝜎f (o𝑊rfu t(cid:4670)uℎrei,n𝑋p𝑐u(cid:4671)t s+. F𝑏i𝑜g)u re2showsageneralLS
(1
T
0
M
)
(cid:3043)(cid:3034) (cid:3042)(cid:3043) (cid:3047)(cid:2879)(cid:2869)
cellstructure. Itcomprisesthreegates—theinputgate,theforgetgate,andtheoutputgate.
wAhlleoref t𝜎h eisg astiegsmeomidp,l 𝑊oy𝑥t hise tshieg mneouidroanc tgiavtaet i(o𝑥n) wfuenicgthiot,n .ℎA(cid:3047)(cid:2879)l(cid:2869)l oisf tthhee greastuesltu osfe tdhein ptrheeceLdSiTnMg
LaSrTeMm abtlhoecmk,a t𝑋ic𝑡a ilsly threep irnepsuent,t aednda s𝑏p𝑥e risE bqiuasa.t ions(8)–(10).
FFiigguurree 22. .LLSSTTMM sstrtruuccttuurree. .
AInsp suhtogwante i(nN Feiwguirnef o2r,m thaeti otonpi npcaerltl osfta tthee): memory line in every cell can be used to
connect with the transport line with the help of the model, which can be used to handle
(cid:0) (cid:1)
the data from the prior memor i y g a to = th σ e c W uripre [ n h tt− m1 , em Xc o ] r + y. b E i ach LSTM node should have ( 8 a )
set of cells that is used for storage of the data stream (Pramod and Pm 2021). In order to
Forgetgate(uselessinformationiseliminated):
provide a recursive network with plenty of time to train and allow for the creation of a
long-distance causal link, LSTM main(cid:16)tains errors at a more(cid:17) constant level (Mukherjee et
f ga = σ W fg [h t−1 , Xc]+bf (9)
Outputgate(activationtolastblockoffinaloutput):
(cid:0) (cid:1)
O pg = σ W op [h t−1 , Xc]+bo (10)
whereσissigmoid,Wxistheneurongate(x)weight,h t−1 istheresultofthepreceding
LSTMblock,Xtistheinput,andbxisbias.
AsshowninFigure2, thetoppartofthememorylineineverycellcanbeusedto
connectwiththetransportlinewiththehelpofthemodel,whichcanbeusedtohandle
thedatafromthepriormemorytothecurrentmemory. EachLSTMnodeshouldhavea
setofcellsthatisusedforstorageofthedatastream(PramodandPm2021). Inorderto
providearecursivenetworkwithplentyoftimetotrainandallowforthecreationofa
long-distancecausallink,LSTMmaintainserrorsatamoreconstantlevel(Mukherjeeetal.
2021). Inseveralcases,neuralnetworksanddeepneuralnetworkshaveshownsuperior
forecastingperformancecomparedtoothermachinelearningmodels. However,whenit
comestopredictingfinancialdistress,thelogisticregressionmodelhasexhibitedbetter
resultsincomparisontoneuralnetworks(Zizietal.2021).
2.3.2. GatedRecurrentNeuralNetwork(GRU)
AGRUisyetanotherRNN-basedmodelwithcomparabledifferencestoLSTM.It
is computationally efficient and faster to train than LSTM, while capturing long-term
dependenciesinsequentialdata. GRUutilizesgatingmechanismstocontroltheflowof
informationbetweenthecurrentandprevioustimesteps. However,itutilizesonlytwo
gates,aresetgateandanupdategate,whereasLSTMhasthreegates. Figure3showsthe
generalstructureofaGRU.

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 9 of 23
al. 2021). In several cases, neural networks and deep neural networks have shown supe-
rior forecasting performance compared to other machine learning models. However,
when it comes to predicting financial distress, the logistic regression model has exhibited
better results in comparison to neural networks (Zizi et al. 2021).
2.3.2. Gated Recurrent Neural Network (GRU)
A GRU is yet another RNN-based model with comparable differences to LSTM. It is
computationally efficient and faster to train than LSTM, while capturing long-term de-
pendencies in sequential data. GRU utilizes gating mechanisms to control the flow of in-
formation between the current and previous time steps. However, it utilizes only two
Int.J.FinancialStud.2023,11,94 gates, a reset gate and an update gate, whereas LSTM has three gates. Figure 3 show9so tfh22e
general structure of a GRU.
FFiigguurree 33.. GGRRUU ssttrruuccttuurree..
TThhee ttwwoo ggaatteess tthhaatt GGRRUU uusseess aarree::
((11)) UUppddaattee ggaattee
𝑍 Z (cid:4670) [ 𝑡 t (cid:4671) ] = = 𝜎 σ ( ( 𝑊 W( ( (cid:3053) z ) ) 𝑥 x t+ + U 𝑈 ( ((cid:3053) z) )ℎ h t−1 ) ( ( 1 1 1 1 ) )
(cid:3047) (cid:3047)(cid:2879)(cid:2869)
(2) Resetgate
(2) Reset gate
r[t] = σ(W (r) x t +U (r) h t−1 ) (12)
where Z[t] is update gate, 𝑟 r[ (cid:4670) t 𝑡 ] (cid:4671) i = s r 𝜎 es ( e 𝑊 t g ((cid:3045) a ) t 𝑥 e(cid:3047), + σ r 𝑈 e ( p (cid:3045) r ) e ℎ s(cid:3047)(cid:2879)e(cid:2869)n ts sigmoid function, W(x()1 i 2 s )
wherne e𝑍u(cid:4670)r𝑡o(cid:4671)n igs autpe,dUat ( e x ) giastep,r 𝑟e(cid:4670)v𝑡i(cid:4671)o uiss rweseeitg ghat,teh,t σ− 1reisptrheseernetssu slitgomfothide pfurneccetidoinn,g 𝑊G(R(cid:3051))U isb lnoecuk-,
ron gaanted, x𝑈t(i(cid:3051)s) thise pcruervrieonutsi nwpeuitg.ht, ht−1 is the result of the preceding GRU block, and 𝑥
(cid:3047)
is
the cFuorrresntto cinkppurti.c edata,GRUreceivestheinputasasequenceofhistoricalstockprices
andgFeonre srtaotceks tphreicoeu dtpatuat, aGsRaUs erqecueeinvcees othfep irnepduictt eads as tsoecqkuperniccee so.fT hhisetoinrpicuatl ssetoqcuke npcrieceiss
faenddt hgreonuegrahteths ethGeR oUutnpeutwt aosr ka, sweqhuicehncuep odfa tperseidtsicitnetde rsntoaclks tpatreicaets.e aTchhe tiinmpeust tseepq,uaenndcteh ies
nfeedtw thorroku’sgfih nthale sGtaRteUi nseutsweodrkto, wgehnicehra utepdthaeteos uittsp iuntte(DrniaPl estrastioe aatn edacHho tnimchea srte2p01, 7a)ndB oththe
LnSeTtwMorakn’ds fiGnRaUl shtaatvee itsh ueisredad tvoa gnetangeerastde uteheto otuhtepiurtc a(Dpai bPielirtsyioto aenldim Hinoantcehtahre 2v0a1n7i)s hBiontgh
gLrSaTdMie natnpdr oGbRleUm haanvde bthleenird addeveapnetangseesm dbulee atlog othreitihr mcasp(aLbiialintyd tPoa enli2m02in1a).te the vanishing
gradient problem and blend deep ensemble algorithms (Li and Pan 2021).
2.4. EnsembleLearningMethods
22..44..1 E.nRsaenmdbolem LeFaorrneisntgA Mlgeothroitdhsm
Int. J. Financial Stud. 2023, 11, x FOR PEER RREaVnIdEoWm forest is a supervised learning method and employs a technique1c0a lolfe d23
2.4.1. Random Forest Algorithm
ensemble learning. It works well for both classification and regression use cases. It is
Random forest is a supervised learning method and employs a technique called en-
derivedfromtheconceptofadecisiontreeasitcreatesseveraldecisiontreestoprovide
semble learning. It works well for both classification and regression use cases. It is derived
resultSste(Kp a2c:z Am daereckisiaonnd trPeeer eisz b2u0i2lt1 b).aTsehde opnr o𝑁ce sinspouftrsa. ndomforestisshowninFigure4.
from the concept of a decision tree as it creates several decision trees to provide results
ThegSetneepr i3c: sTtehpes noufmabrearn dofo mtrefeosr teos tbael gcoornisthidmeraepdp ilsi epdictkoesdt.o ckmarketprediction(Yadav
(Kaczmarek and Perez 2021). The process of random forest is shown in Figure 4. The ge-
andVSitsehpw 4a:k Baarsmead 2o0n1 9th)ea rsete:ps performed before, the output is predicted for each tree.
neric steps of a random forest algorithm applied to stock market prediction (Yadav and
Vishwakarma 2019) are:
Step 1: 𝑁 random records are picked.
FFiigguurree4 4.. RRaannddoomm ffoorreesstt..
Random forest can perform well on large datasets, but the possibility of the formation
of large number of trees can slow down the algorithm’s performance (Salles et al. 2018).
The random forest approach can also be used for various other use cases, such as predict-
ing the direction of stocks (Sadorsky 2021). This algorithm is used in the Zagreb Stock
Exchange (Manojlović and Štajduhar 2015) and is compared with SVM, KNN, and logistic
regression based on the evaluation parameters accuracy, precession, recall, and F-Score
(Pathak and Pathak 2020).
2.4.2. XG-Boost Regression Algorithm
XG-Boost is an ensembled machine learning algorithm that is like random forest with
subtle differences. It is a combination of weak learners such as decision trees. It is a good
prediction model for stock forecasting as it works on a sequential model that considers
the gradient for each iteration so that the weights are updated for each iteration of the
decision tree (Zhu and He 2022). The process of XG-Boost is depicted in Figure 5.
Figure 5. XG-Boost algorithm.
2.4.3. E-SVR-RF (Ensemble Support Vector Machine–Random Forest)
Ensemble support vector regression with random forest is an ensemble technique
that follows the bagging method. An ensemble learning algorithm that consists of a sup-
port vector regressor and random forest is used to handle the complex relationship for

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 10 of 23
Step 2: A decision tree is built based on 𝑁 inputs.
Step 3: The number of trees to be considered is picked.
Step 4: Based on the steps performed before, the output is predicted for each tree.
Int.J.FinancialStud.2023,11,94 10of22
Step1: Nrandomrecordsarepicked.
Step2: AdecisiontreeisbuiltbasedonNinputs.
FigurSet e4.p R3a:nTdhomen fourmesbt.e roftreestobeconsideredispicked.
Step4: Basedonthestepsperformedbefore,theoutputispredictedforeachtree.
RRaannddoomm ffoorreesstt ccaann ppeerrffoorrmm wweellll oonn llaarrggee ddaattaasseettss,, bbuutt tthhee ppoossssiibbiilliittyy ooff tthhee ffoorrmmaattiioonn
ooff llaarrggeen nuummbbeerro offtr tereesecsa cnasnl oswlowdo dwonwtnh ethaleg aolrgitohrmith’smp’esr fpoerrmfoarnmcean(Scael l(eSsaellteasl .e2t 0a1l8. )2.0T1h8e).
rTahned roamndfoormes ftoarpepstr oaapcphrocaancha lcsaonb aelsuos ebde fuosrevda froior uvsaroitohuesr outsheecra usesse, csauscehs,a ssupcrhe dasic ptirnegdtihcte-
dinirge ctthieo ndoirfescttoiocnk so(fS satdoocrkssk y(S2a0d2o1r)s.kTyh 2is02a1lg).o Trihthism aligsoursiethdmin itsh uesZedag irne bthSet oZcakgErxebch Satnogcek
(EMxachnaonjlogve i(c´MaanndoŠjltoavjdiću hanard2 Š0t1a5jd)uahndari 2s0c1o5m) panarde dis wcoimthpSaVreMd, wKiNthN S,VanMd, lKoNgiNsti, carnedg rloesgsiisotinc
breagseredsosinonth beaesveadl uoant itohne peavraalmuaettieorns apcacruarmaecyte,rpsr eaccecsusriaocny,, rpecraeclle,sasniodnF, -rSeccoarlel, (aPnadth Fa-kScaonrde
P(Paaththaakk2 a0n20d) .Pathak 2020).
22..44..22.. XXGG--BBoooosstt RReeggrreessssiioonn AAllggoorriitthhmm
XXGG--BBoooosstt iiss aann eennsseemmbblleedd mmaacchhiinnee lleeaarrnniinngg aallggoorriitthhmm tthhaatt iiss lliikkee rraannddoomm ffoorreesstt wwiitthh
ssuubbttllee ddiiffffeerreenncceess.. IItt iiss aa ccoommbbiinnaattiioonn ooff wweeaakk lleeaarrnneerrss ssuucchh aass ddeecciissiioonn ttrreeeess.. IItt iiss aa ggoooodd
pprreeddiiccttiioonn mmooddeellf oforrs tsotcokckf ofroerceacsatsintigngas aist wit owrkosrkosn oans eaq sueeqnuteianltmialo dmeoldtheal tthcoant sciodnesrisdtehres
gthraed giernadtfieonrte afochr eitaecrhat iiotenrastoiothna stot htehawt etihgeh twsaerigehutps daartee dupfodraeteadch foitre reaatciohn iotefrtahteiodne coifs itohne
tdreeeci(sZiohnu tarened (HZheu2 0a2n2d) .HTeh 2e0p2r2o)c. eTshseo pfrXoGce-Bsso oosf tXisGd-Beopoicstte ids idneFpiigctuerde i5n. Figure 5.
FFiigguurree 55.. XXGG--BBoooosstt aallggoorriitthhmm..
22..44..33.. EE--SSVVRR--RRFF ((EEnnsseemmbbllee SSuuppppoorrtt VVeeccttoorr MMaacchhiinnee––RRaannddoomm FFoorreesstt))
EEnnsseemmbbllee ssuuppppoorrttv vecetcotrorr ergergersessiosinonw iwthitrha nrdanomdofmor efostreissta nis eanns eemnbselemtbecleh nteiqcuhenitqhuaet
ftohlalot wfoslltohwesb tahgeg binagggminegth modet.hAond.e Annse emnbselemlbealer nleinargnainlggo arligthomritthhmat tchoant sciosntssiosftsa osfu ap psuoprt-
vpeocrtto vrercetgorre sresogrreasnsodrr aanndd ormandfoormes tfoisreusst eids utosehda ntod lheatnhdelec otmhep cleoxmrpelleaxti ornelsahtiiopnfsohripea fcohr
clusterandindividualforecast. Thesearefinallycombinedusingthebaggingmethodto
showthefinalpredictionusingaweightedaveragemodel(Xuetal.2020). Thesuggested
ensemblingcanleveragetheadvantagesofboththesupportvectormachineandrandom
forest,wherethesupportvectormachinecancapturecomplexrelationshipsbyfinding
thehyperplanethatmaximizesthemarginbetweentheforecastedandactualprice,and
randomforestdecreasestheoverfittingproblembycombiningthedecisiontrees.
XG-Boost+LSTM,blendingensemble(LSTM+GRU)(LiandPan2021),andensemble
techniquesforsentimentanalysis(Giteetal.2023)areproposedbytheresearchcommunity
forfinancialinstrumentpriceforecasting. Tosummarizefurther,basedonourreview,it
canbeunderstoodthatdeeplearning-andmachinelearning-basedensembletechniques
havegainedpopularityduetotheirperformance.
3. GeneralMachineLearningPipeline
ThegeneralapproachtotrainingamachinelearningmodelisgiveninFigure6:

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 11 of 23
each cluster and individual forecast. These are finally combined using the bagging method
to show the final prediction using a weighted average model (Xu et al. 2020). The sug-
gested ensembling can leverage the advantages of both the support vector machine and
random forest, where the support vector machine can capture complex relationships by
finding the hyperplane that maximizes the margin between the forecasted and actual
price, and random forest decreases the overfitting problem by combining the decision
trees.
XG-Boost + LSTM, blending ensemble (LSTM + GRU) (Li and Pan 2021), and ensem-
ble techniques for sentiment analysis (Gite et al. 2023) are proposed by the research com-
munity for financial instrument price forecasting. To summarize further, based on our
review, it can be understood that deep learning- and machine learning-based ensemble
techniques have gained popularity due to their performance.
Int.J.FinancialStud.2023,11,94 3. General Machine Learning Pipeline 11of22
The general approach to training a machine learning model is given in Figure 6:
Figure 6. Workflow of basic ML model.
Figure6.WorkflowofbasicMLmodel.
TTrraaiinniinngg tthhee MMLLm mooddeelli ninvvoolvlvesess isxixs tsetpesp,sw, whihchichar aerdee dscersicbreidbeidn tinhe thfoel lfoowlloinwginsegc tsieocn-:
tion: S tep1: LoadthedatafromacsvfileorcallthehistoricaldatawiththehelpofanAPI.
(examStpelpe s1:: YLaohaodo tFhien daantcae ,frQouma na dcls,vI EfiXleF oinr acnaclle t,heetc h.)i.storical data with the help of an API.
(examSptelpes2: :YPahreopor Foicneasnscteh,e Qhuisatnodrilc, aIElXdFatinaatnocree, metocv.)e. anyredundancies,nullvalues,etc.
andfSetaetpu r2e: sPerleepctrioocnesssh othueld hbisetocroincadlu dctaetda .to remove any redundancies, null values, etc.
and fSetaetpur3e: sBeelefocrtieotnr asihnoinugldt hbee McoLndmuocdteedl,. fe aturessuchasopen,close,adjclose,volume,
etc.,cSatenpb 3e: sBeelefoctreed traalionninggw tihteh MseLco mndoadreyl, dfeaatatu.res such as open, close, adj close, volume,
etc., cSatnep be4 :sDelievcitdeed tahleonpgre wpriothc essesceodnddaatray idnatotat.r a iningandtestingdata,preferably,where
preferably75%ofthedatashouldbeusedtotrainthemodel, whiletheremaining25%
shouldbeusedtoevaluatethemodel’sperformance.
Step 5: After splitting the data, use the training data to train the model; then, per-
formance evaluation can be carried out based on the model’s output using the testing
data.
Step6: Oncethemodelisconstructed,themodel’srespectiveevaluationparameters
forregressionorclassificationcanbeusedtoevaluatethemodel.Theevaluationparameters
areprecision,recall,F1Score,andaccuracy. Themeanabsoluteerror,meansquareerror,
rootmeansquarederror,R-squared,chisquare,andmeanabsolutepercenterror(mean
absolutepercentageerror)canbeused.
Step7: Fine-tunethehyperparameterstoimprovetheevaluationparametersofthe
model. Following hyperparameter tuning, the model should be evaluated to check for
improvedpredictionparameters,afterwhichthepredictioncanbeplotted.
4. SignificanceofEnsembleModeling
Thissectionofthearticleisaboutthecomparativeanalysisofthemostsignificant
methodsexploredinSections2and3. Basedonthestudy,itisobservedthatmostcommon
algorithms, such as SVR, MLPR, KNN, random forest, XG-Boost, and LSTM, are used

Int.J.FinancialStud.2023,11,94 12of22
byvariousresearchersintheirresearchwork. Inthisreviewarticle,weattemptedtouse
thesealgorithmsforforecastingthestockpriceoftwostocks,namely,TainwalaChemicals
andPlastics(Mumbai,India)Lt. (TAINIWALCHM)andAgroPhos(Indore,India)Ltd.
(AGROPHOS),andproposedanensemblealgorithmbasedon“RandomForest+XG-Boost
+ LSTM”. The idea behind including a comparison of the algorithms is to understand
thegenericperformanceofthepopularmachinelearninganddeeplearningalgorithms
identifiedduringtheliteraturereview.
After studying various algorithms, we developed an ensemble model of random
forest,XG-Boost,andLSTM.Randomforestissimplerthanthegradientboostingalgorithm
buthastheabilitytohandlehigh-dimensionaldatasetsandcapturenon-linearpatterns
common in stock market forecasting. Gradient boosting is a top choice algorithm for
classification and regression predictive modeling projects because it often achieves the
best performance, but it takes lot of time to converge to the solution. The ensemble of
XG-Boostprovidesanefficientimplementationofgradientboostingthatcanbeconfigured
totrainrandomforestensemblesandaddressthespeedproblemsofgradientboosting. In
ordertoachievethebestperformanceinstockpriceforecasting,theLSTMiscombinedin
thismodelduetoitscapabilityofstoringpastinformation. Tomakethemostofthetwo
models,itisgoodpracticetocombinethesetwoandapplyahigherweighttothemodel,
whichyieldsalowerlossfunction(meanabsoluteerror). Theparametersettingusedfor
implementingtheproposedensemblemodelismentionedTable1.
Table1.Ensemblemodelparameterconfiguration.
Parameter Description
Modeltype Stackedensemblemodel
Libraries Keras,TensorFlow,sklearn
Algorithms RandomForest+XG-Boost+LSTM
Training/testingsize 80%fortrainingand20%fortesting
Lossfunction MSE
Optimizer Adam
Maximumepochs 50
RandomForestConfiguration
Numberofestimators [50,100,200]
Maximumdepth [3,5,7]
Maximumfeatures [‘sqrt’,‘log2’]
Hyperparametertuningmethod Gridsearch
XG-BoostConfiguration
Maximumdepth [3,4,5]
Learningrate [0.1,0.01,0.001]
Numberofestimators [50,100,150,500,1000]
Hyperparametertuningmethod Gridsearch
LSTMConfiguration
LSTMLayers 2
Dropoutrate 0.2
Denselayer 25units
Batchsize 32
Hyperparametertuningmethod Gridsearch
The necessary comparison and evaluations are depicted in Figures 7 and 8. We
implementedallofthesealgorithmsusingPythonprogramminglanguage. Figure7shows
thestockforecastingresultsofTainwalaChemicalsandPlastics(India)(TAINIWALCHM).
ThedatasetforimplementationwasobtainedfromYahooFinanceAPI,andweconsidered

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW  13 of 23

| Hyperparameter tuning method  |     | Grid search  |     |     |
| ----------------------------- | --- | ------------ | --- | --- |
XG-Boost Configuration
| Maximum depth                 |     | [3, 4, 5]                  |     |     |
| ----------------------------- | --- | -------------------------- | --- | --- |
| Learning rate                 |     | [0.1, 0.01, 0.001]         |     |     |
| Number of estimators          |     | [50, 100, 150, 500, 1000]  |     |     |
| Hyperparameter tuning method  |     | Grid search                |     |     |
LSTM Configuration
| LSTM Layers                   |     | 2            |     |     |
| ----------------------------- | --- | ------------ | --- | --- |
| Dropout rate                  |     | 0.2          |     |     |
| Dense layer                   |     | 25 units     |     |     |
| Batch size                    |     | 32           |     |     |
| Hyperparameter tuning method  |     | Grid search  |     |     |
Int.J.FinancialStud.2023,11,94 13of22
The necessary comparison and evaluations are depicted in Figures 7 and 8. We im-
plemented all of these algorithms using Python programming language. Figure 7 shows
| the  stock  forecasting  | results  of  Tainwala  | Chemicals  | and  Plastics  (India)  | (TAINI- |
| ------------------------ | ---------------------- | ---------- | ----------------------- | ------- |
WALCHM). The dataset for implementation was obtained from Yahoo Finance API, and
thedatwase ectonfosirdeTrAedI NtheI WdaAtaLseCt fHorM TAfIrNoImWAtLhCeHyMea frro2m0 1th4e tyoeatrh 2e01y4e tao rth2e0 y2e3a.r T20h23e. RThMe SEandR2
scoreswRMerSeE uansde dR2f oscroerevsa wlueraet uinsegd tfhore epvaelrufaotrinmg athnec peeorffortmheanvcea roifo thues vmaroiodues lms.odels.
|      |     |      |     |     |
| ---- | --- | ---- | --- | --- |
| (a)  |     | (b)  |     |     |

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW  14 of 23

| (c)  |     | (d)  |     |     |
| ---- | --- | ---- | --- | --- |

|      |     |      |     |     |
| ---- | --- | ---- | --- | --- |
| (e)  |     | (f)  |     |     |

(g)
Figure 7. TANIWALCHM stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
Figure7.TANIWALCHMstockpriceforecasting:(a)SVR,(b)MLPR,(c)KNN,(d)randomforest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
(e)XG-Boost,(f)LSTM,(g)EnsembleRandomForest+XG-Boost+LSTM.
Figure 8 shows the stock forecasting results of Agro Phos (India) Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have con-
sidered the dataset for TAINIWALCHM from the year 2018 to the year 2023. The RMSE
and R2 scores were used for evaluating the performance of the various models.

| (a)  |     | (b)  |     |     |
| ---- | --- | ---- | --- | --- |

Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 14 of 23
(e) (f)
(g)
Figure 7. TANIWALCHM stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
(e) XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
Figure 8 shows the stock forecasting results of Agro Phos (India) Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have con-
Int.J.FinancialStud.2023,11,94 14of22
sidered the dataset for TAINIWALCHM from the year 2018 to the year 2023. The RMSE
and R2 scores were used for evaluating the performance of the various models.
Int. J. Financial Stud. 2023, 11, x FOR PEER REVIEW 15 of 23
(a) (b)
(c) (d)
(e) (f)
(g)
Figure 8. AGROPHOS stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest, (e)
Figure 8. AGROPHOS stock price forecasting: (a) SVR, (b) MLPR, (c) KNN, (d) random forest,
XG-Boost, (f) LSTM, (g) Ensemble Random Forest + XG-Boost + LSTM.
(e)XG-Boost,(f)LSTM,(g)EnsembleRandomForest+XG-Boost+LSTM.
The analysis results in Table 2 indicate that the ensemble algorithm demonstrated the
best performance compared to other distinct algorithmsʹ.

| Int.J.FinancialStud.2023,11,94 |     |     |     |     |     | 15of22 |
| ------------------------------ | --- | --- | --- | --- | --- | ------ |
Figure8showsthestockforecastingresultsofAgroPhos(India)Ltd. (AGROPHOS).
The dataset for implementation was obtained from Yahoo Finance API, and we have
consideredthedatasetforTAINIWALCHMfromtheyear2018totheyear2023. TheRMSE
andR2scoreswereusedforevaluatingtheperformanceofthevariousmodels.
TheanalysisresultsinTable2indicatethattheensemblealgorithmdemonstratedthe
bestperformancecomparedtootherdistinctalgorithms’.
Table2.RMSEandR2scoresofalgorithms.
TANIWALCHM AGROPHOS
|     |     | Algorithm    | RMSE    | R2     | RMSE    | R2     |
| --- | --- | ------------ | ------- | ------ | ------- | ------ |
|     |     | SVR          | 4.525   | 0.9279 | 1.5074  | 0.9432 |
|     |     | MLPR         | 2.5893  | 0.9611 | 2.4764  | 0.9472 |
|     |     | KNN          | 4.4249  | 0.9311 | 4.7877  | 0.7262 |
|     |     | LSTM         | 5.6241  | 0.8867 | 5.2494  | 0.8809 |
|     |     | Randomforest | 87.8839 | 0.9818 | 98.5633 | 0.9428 |
|     |     | XG-Boost     | 2.0686  | 0.9842 | 1.7618  | 0.9379 |
RandomForest+
|     |     |     | 2.0247 | 0.9921 | 1.2658 | 0.9897 |
| --- | --- | --- | ------ | ------ | ------ | ------ |
XG-Boost+LSTM
From this study and experimental analysis, we observed that the modification of
hyperparametersisacrucialstageintheprocessofstockforecastingasitcanmaximize
theperformanceofmachinelearningmodels. Table3listsmachinelearningmodelsthat
arefrequentlyusedinstockpriceforecasting. Nevertheless,theefficacyofthesemodels
ishighlydependentonthechoiceofhyperparameters,whichareparametersthatarenot
learnedfromthedata,butrather,definedbeforethelearningprocess.
Table3.Summaryofexistingstockpredictionandforecastingalgorithmswithperformanceanalysis.
| SrNo | AlgorithmName |     | GapAnalysis |     | PerformanceEvaluation |     |
| ---- | ------------- | --- | ----------- | --- | --------------------- | --- |
Linearregressionassumesalinear
relationshipbetweendependentand Thisisaregressiontypeofalgorithmthat
independentvariablesandisnotsuitable showsgraphsinalinearway,wherein
| 1   | Linearregression |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- |
formostreal-timeapplications,andisused RMSEis3.22,MAEis2.53,MSEis10.37,
toperformobservationsonreadily andR-squaredis0.73(Gururajetal.2019).
accessiblesampledata(Gururajetal.2019).
Thisisaclassificationtypeofalgorithm,
SVM’sexcellentmemoryefficiencyand andwhenusedforstockprediction,the
effectivenessmakeitanidealestimating resultsareasfollows:accuracyis68.2,
techniqueinhigh-dimensionalspace.The recallis65.2,precisionis64.2,andF1-Score
Supportvector
| 2   |     | shortcomingofSVMisthatitmight |     | is64.9%(0.65). |     |     |
| --- | --- | ----------------------------- | --- | -------------- | --- | --- |
machine
experienceoverfitting,butitperforms Whenusedasasupportvectorregression
exceptionallywellontinydatasets(Pathak (SVR)algorithm,theevaluationparameters
|     |     | andPathak2020;Grigoryan2017). |     | areasfollows:SMAPE=5.59, |     |     |
| --- | --- | ----------------------------- | --- | ------------------------ | --- | --- |
R-squared=1.69,andRMSE=43.36.
ThisisaclassificationtypeofML
algorithminwhichtheresultsofstock
KNNisanalgorithmthatskipsthe
predictionareasfollows:accuracyis65.2,
learningstep,soitmaynotgeneralize
recallis63.6,precisionis64.8,andF1Score
effectively.Withahugedataset,ittakes
| 3   | K-nearestneighbor |     |     | is64.1%(0.64). |     |     |
| --- | ----------------- | --- | --- | -------------- | --- | --- |
longersinceitmustsortallthedistances
ForKNNregressor,theevaluation
fromtheunknownitem(Tanuwijayaand
parametersareasfollows:SMAPE=14.32,
Hansun2019;PathakandPathak2020).
R-squared=−2.42,andRMSE=56.44
(Venkat2022).

Int.J.FinancialStud.2023,11,94 16of22
Table3.Cont.
SrNo AlgorithmName GapAnalysis PerformanceEvaluation
ModelswithanintegratedGNBalgorithm GaussiannaïveBayesusedbyauthorsin
willyieldfeatureextractionandfeature theirresearch.Kendall’sTestof
scalingoutcomesthataresuperiortothose Concordanceisusedinthisfeature,which
Gaussiannaïve
4 alreadyachievedusingmodelsthat isscaledandextracted.Theresultsareas
Bayes
incorporateeithertheGNBalgorithmor follows:accuracyis84,F1Scoreis62.44%
featurescaling(Setianietal.2020; (0.62),specificityis0.70,andAUCvaluesis
Ampomahetal.2021). 0.90(Bansaletal.2022).
Inthisalgorithm,withthehelpofresearch
Bothbinaryandmulticlassclassification papers,variousfinancialfactorsare
usethisalgorithm.Thefindingsobtained consideredthroughwhichfactorsare
vialogisticregressionarethemostaccurate; groupedforprediction.Theresultsofthis
5 Logisticregression
however,identifyingthebest-fittingfeature algorithmareasfollows:accuracyis78.6,
isnecessary(PathakandPathak2020;Ali recallis76.6,precisionis77.8,andF1Score
etal.2018). is77.1%(0.77)(PathakandPathak2020;Ali
etal.2018).
ARIMAisatimeseriesforecasting
techniqueforpredictingmarketorstock
ARIMAcanbeconsideredbecauseitisa prices.Itisacombinationorintegrationof
uniquemodelwithsignificantcoefficients autoregressivemovingaverages;the
6 ARIMA
andpassesallthediagnostictests resultsareasfollows:RMSE,88.05;MAE,
(Mashadihasanli2022). 65.88;andMAPE,5.73,andifperformed
withsentimentanalysis,theRMSEscoreis
6.41(Kedar2021).
ThisalgorithmwascreatedbyFacebook
Prophetcanuseregressionmodelsto
fortimeseriesforecasting.Oneofits
determineseasonalityonadaily,monthly,
advantagesisthatitdoesnotconsider
7 FBProphet andannualbasis,aswellaseffectsrelated
holidaysornullvalues.Theresultofits
toholidays(Sureshetal.2022;Kaninde
RMSEisachieved93(Sureshetal.2022;
etal.2022).
Kanindeetal.2022).
GRUisadeeplearningalgorithmthathas
fewerparametersandhandlesshort-term
GRUisaneuralnetworkapproachthatis
dataproperly.Theevaluationparameters
animprovementuponRNNbuthasfewer
ofGRUare,withoutsentimentanalysis,
parametersthanLSTM,soittrainsfaster.
8 GRU MAE=42.8,RMSE=47.31,andR-squared
Also,thechancesofoverfittingarelower
=0.879,andwithsentimentanalysisbased
comparedtoRNN,anditcanhandle
onnewsevaluationparameters,
long-termdependency(Shahietal.2020).
MAE=24.472,RMSE=29.153,and
R-squared=0.967(Shahietal.2020).
LSTMisamoredevelopedtypeofRNN
andisadeeplearningtechnique.Thisis
oneofthemostusedMLalgorithmsfor
Inthisalgorithm,weightsareadjustedfor
stockforecasting,andwhenusedalong
eachlongshort-termmemorydatapoint
withsentimentanalysis,itshowsbetter
viastochasticgradientdescent.
resultsthanwithoutsentimentanalysis.
LSTMcanhandlemoreverylong-term
9 LSTM Theresultwithoutsentimentanalysisare
dependencycomparedtoanyotherneural
MAE=48.47,RMSE=55.993,and
networkalgorithm(Shahietal.2020;
R-squared=0.867,andwithsentiment
PramodandPm2021;Mukherjeeetal.
analysisbasedonnewsevaluation
2021).
parameters,areMAE=17.689,
RMSE=23.070,andR-squared=0.867
(Shahietal.2020).

Int.J.FinancialStud.2023,11,94 17of22
Table3.Cont.
SrNo AlgorithmName GapAnalysis PerformanceEvaluation
Theeffectivenessofrandomforestonlarge
datasetsisoneofitsadvantages.Itcanbe Thisisanensembletypeofalgorithmthat
appliedtoclassificationandregression isusedforstockforecasting.Theresultsfor
issues.Themodelbecomesmorerandom randomforestareasfollows:accuracyis
10 Randomforest
asaresult,improvingit.Thismodel’suse 80.7,recallis78.3,precisionis75.2,andF1
ofahugenumberoftreesslowsitdown, Scoreis76.7%(0.77)(PathakandPathak
whichisadrawback(PathakandPathak 2020;Polamurietal.2019).
2020;Polamurietal.2019).
XG-Boostisanensembledlearning
techniquethatusesdecisiontreesbutina
sequentialmannerandusesgradient
boostinginaniterativemannertoobtain XG-Boosthasthefollowingevaluation
11 XG-Boost
betterresults. parameter:MSE=360.0(ZhuandHe2022).
XG-Boostissensitivetohyperparameters
andwillnotworkaswellonlargedatasets
asrandomforest(ZhuandHe2022).
Ensemblesupportvectorregressionand
randomforestshowsimprovedaccuracyas TheE-SVR-RFensembledalgorithmshows
itleveragestheadvantagesofboth thefollowingevaluationparameters:
12 E-SVR-RF algorithms,anditsrobustnessisincreased, MAPE=1.335,MAE=0.1537,
butduetotheincreasedcomplexityofboth RMSE=0.0188,andMAE=0.0485
algorithms,overfittingisanissue (Xuetal.2020).
(Xuetal.2020).
EnsemblingXG-BoostandLSTMcan
leveragetheadvantagesofbothalgorithms.
XG-Boostcanhandlelinearandnon-linear TheensemblealgorithmofXG-Boost+
13 XG-Boost+LSTM relationshipsandLSTMcanhandle LSTMshowsthefollowingevaluation
long-termdependence.Duetothis parameter:MSE=3.465(Vuongetal.2022).
algorithm’scomplexity,hyperparameter
tuningcanbeanissue(Vuongetal.2022).
Blendingensemble(LSTM+GRU)isa
combinationoftwotoofthemost-used
Theblendingensemblealgorithm,which
improvementstoRNNandsolvesthe
consistsofamodifiedversionofRNN,i.e.,
vanishinggradientproblem.Bothofthem
LSTMandGRU,hasthefollowing
Blendingensemble canhandlelong-termdependencewell,
14 evaluationparameters:
(LSTM+GRU) andcombiningthemwouldimprove
MSE=186.32,MPA=99.65,
forecasting;also,overfittingcanbereduced.
precision=60%,Recall=75%,
Itmayrequirehighcomputationalpower
F1-Score=66.67%(LiandPan2021).
andtimetotrainbothLSTMandGRU(Li
andPan2021).
Thenextpartofthissectionillustratesthecomparativeanalysisofworkconductedby
multipleauthorsonvariousclassification,regression,andtimeseries-basedalgorithmsto
evaluatetheirperformanceinstockmarketforecasting,asshowninTable3. Thealgorithms
wereassessedusingvariousevaluationparameters,includingaccuracy,recall,precision,F1
Score,MSE,MAE,RMSE,andR-squarederror. Theaimwastoidentifyeffectivealgorithms
thatcouldbenefitawideraudience,includinggeneralappliedresearchersandintelligent
laypersons,enablingthemtomakeinformedinvestmentdecisions. Thesefindingswillalso
providevaluableinsightsforresearchers,investors,andgeneralaudiences,enablingthem
tomakewell-informeddecisionsandnavigatethecomplexitiesofthefinancialmarket.
5. ImplicationsandLimitationsoftheStudy
Thisstudyfocusedontheapplicationofmachinelearninganddeeplearningmodels
instockforecasting. Itcanbenotedthatmachinelearningordeeplearningmodelsalone

Int.J.FinancialStud.2023,11,94 18of22
arenotsufficient. Ensembletechniquesarecapableofprovidingsuperiorperformance.
But merely developing a model is not enough, and emphasis should also be placed on
hyperparametertuning. Theperformanceofthemodelcanbeimprovedusinghyperpa-
rameterssuchaslearningrates,regularizationincasesofdeeplearning,thenumberof
hiddenlayers,max_depth,n_estimators,andlearningrate. Choosingthepropersettings
forthesehyperparameterscanconsiderablyenhancetheprecisionofstockforecasts. For
instance,amodelwithagreaterlearningratemayconvergemorequicklybutmayalso
besusceptibletooverfitting,whereasamodelwithalowerlearningratemayconverge
moreslowlybutgeneralizebettertonewdata. Tuninghyperparametersentailschoosing
theoptimalcombinationofhyperparametersforagivendatasetandmodelarchitecture.
Thisprocedureoftenentailstrainingmanymodelswithdistincthyperparametervalues
andevaluatingtheirperformanceonavalidationdataset. Typically,theoptimalcombi-
nationofhyperparametersisdeterminedbythemodel’scapacitytoreducethedeviation
betweenpredictedandactualstockprices. Thestudyofmachinelearningmodelsanddeep
learningmodelsandthecomparativeresultspresentedinthisarticlewillguideresearchers
inchoosingidealandpreferredmachinelearninganddeeplearningalgorithmsfortheir
respectiveresearchwork.
6. FutureResearchDirections
Thepresentedreviewarticleisfocusedonthereviewofrelatedandpublishedarticles
onstockpriceprediction,forecasting,andclassification. Theanalysisoffinancialinstru-
mentssuchasstocksandequitiesisaconsiderablechallenge.Itissaidthatthestockmarket
evolvesoveraperiodoftime(LimandBrooks2011),andhence,theapproachesdeveloped
forhandlingspecificproblemswillseelowperformancesoonerorlatereventhoughtheir
performanceisfoundtobeappreciatedinitially. Asthestockmarketevolvesunderthe
influence of various factors such as geopolitical issues, equity trading, and investment,
theunderlyingchallengesalsochange,andsodothemethodologiesforaddressingthe
newchallenges(SprengerandWelpe2011;Shahetal.2019). Sufficientresearchhasbeen
presentedonstockpricepredictionandstockclassification,whichistheprimaryfocusof
thisreviewarticle. Basedonthestudypresentedinthisarticle,wehaveidentifiedsomeof
thekeyareaswhereresearchersshouldfocustheirattentionandexplorebettersolutions.
Inthissection,anattemptismadetoopennewresearchavenuesforresearchersinthefield
ofstockmarketresearch.
6.1. TrendAnalysisandClassification
Most researchers are inclined towards solving the problem of price prediction or
forecastingstockvalueseries. Itisimportanttoknowthemovementofstockprices,aswell.
Webelievethatresearcherscanexplorethepossibleusageofstate-of-the-artdeeplearning
andmachinelearningalgorithmsinstocktrendpredictionandclassification(Jiang2021;
Nikouetal.2019).
6.2. PatternIdentificationUsingComputerVision
Most researchers see stock price as time series data, which is true. But time series
numericaldatacanbetransformedintoimages,andpatternsintheimagescanbeidentified
tounderstandnewtrendsoccurringinthepricechanges(Barraetal.2020). Duetothe
advancement of deep learning in the form of pre-trained models and transfer learning,
researcherscanexploreopportunitiestoapplythesemodelstounderstandingtheimages
generatedbasedontimeseriesdata.
6.3. ChartPatternAnalysisUsingComputerVision
Chart pattern analysis is one of the most-applied approaches among traders and
investors. Candlesticksoftenformfascinatingpatterns(Caglieroetal.2023;Huetal.2019),
whichhelpstradersincapturingpriceactionwellbeforeitoccurs.Butthebiggestdrawback
ofchartpatternanalysisistheperceptionoftheviewer. Generally,thesechartpatternsare

Int.J.FinancialStud.2023,11,94 19of22
identifiedbasedontheperceptionsoftraders. Everytraderwillhaveadifferentperception
ofthemarket,andtheemotionsoftraderstendtoprojectdifferentpatternsforthesame
priceaction. Forexample,itisdifficulttodifferentiatebetweendouble-topandtriple-top
candlestickpatterns(Lambert2009). Researcherscanaddresstheproblemofcandlestick
patternidentificationusingsuitabledeep-learningtechniquessothatperceptionbiascan
beavoidedamongsttraders.
7. Conclusions
Inthisreview,severalconventional,machinelearning,anddeeplearningtechniques
that are employed in stock market forecasting are investigated. This review describes
variousmachinelearningtechniques,deeplearningtechniques,andtimeseriesforecasting
techniques. Thisarticlepresentsrecentapplicationsofmachinelearninganddeeplearning
models,andanensemblemodelisalsotestedontheTAINIWALCHMandAGROPHOS
stockdatasets. Despitetheexistenceofseveralpopularmethodsforstockpriceforecasting,
eventoday,thereisnouniversalsolutiontoaccuratelypredictthestockpriceortrendofthe
market. ThereisstillapossibilitythatAI-basedmodelscanalsofailiftheyarenottrained
efficientlywithfreshdata. Toconcludethisarticle,weassertthatresearchersshouldkeep
exploringnewavenuestosolvepriceactionproblemsusingensembletechniques. Stock
forecastingmodelsshouldbeenhancedwithsuitablehyperparametertuningsothatthey
canserveasprecisestockpricepredictionmodels. Tradersandinvestmentadvisorscan
usemachinelearninganddeeplearningmodelsasadditionalconfirmationindicatorsto
supporttheirdecisions,anddecisionsshouldnotrelyonlyonAI-basedpriceforecasting
methods. Alongwithstockforecastingtechniques,researchersinthefuturecanexpand
theirstudiestoportfoliomanagement,tradingstrategydesign,andinvestmentdecision
making.
AuthorContributions: ConceptualizationG.S.,D.S.D.andA.M.B.; Visualization,G.S.; Writing—
originaldraft,G.S.,D.S.D.andA.M.B.;Supervision,D.S.D.andA.M.B.;Writing—review&editing,
S.T.D.,D.D.,S.K.B.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
References
Agrawal,Manish,PiyushKumarShukla,RajitNair,AnandNayyar,andMehediMasud.2022.StockPredictionBasedonTechnical
IndicatorsUsingDeepLearningModel.Computers,Materials&Continua70:287–304.
Ali,SyedShahan,MuhammadMubeen,andAdnanHussain.2018.Predictionofstockperformancebyusinglogisticregressionmodel:
EvidencefromPakistanStockExchange(PSX).AsianJournalofEmpiricalResearch15:212.
Ampomah,ErnestKwame,GabrielNyame,ZhiguangQin,PrinceClementAddo,EnochOpaninGyamfi,andMichealGyan.2021.
StockMarketPredictionwithGaussianNaïveBayesMachineLearningAlgorithm.Informatica45:2.[CrossRef]
Baheti,Radhika,GauriShirkande,SnehaBodake,JanhaviDeokar,andArchanaK.2021.StockMarketAnalysisfromSocialMediaand
NewsusingMachineLearningTechniques.InternationalJournalonDataScienceandMachineLearningwithApplications1:59–67.
Ballings,Michel,DirkVandenPoel,NathalieHespeels,andRubenGryp.2015.Evaluatingmultipleclassifiersforstockpricedirection
prediction.ExpertSystemswithApplications42:7046–56.[CrossRef]
Banik,Shouvik,NonitaSharma,MonikaMangla,SachiNandanMohanty,andSelvarajanShitharth. 2022. LSTMbaseddecision
supportsystemforswingtradinginstockmarket.Knowledge-BasedSystems239:107994.[CrossRef]
Bansal,Malti,ApoorvaGoyal,andApoorvaChoudhary.2022.StockMarketPredictionwithHighAccuracyusingMachineLearning
Techniques.ProcediaComputerScience215:247–65.[CrossRef]
Barra, Silvio, SalvatoreMarioCarta, AndreaCorriga, AlessandroSebastianPodda, andDiegoReforgiatoRecupero. 2020. Deep
learningandtimeseries-to-imageencodingforfinancialforecasting.IEEE/CAAJournalofAutomaticaSinica7:683–92.[CrossRef]
Bustos,Oscar,AlexandraPomares,andEnriqueGonzalez.2017.AcomparisonbetweenSVMandmultilayerperceptroninpredicting
an emerging financial market: Colombian stock market. Paper presented at 2017 Congreso Internacional de Innovacion y
TendenciasenIngenieria(CONIITI),Bogotá,Colombia,October4–6;pp.1–6.

Int.J.FinancialStud.2023,11,94 20of22
Cagliero, Luca, Jacopo Fior, and Paolo Garza. 2023. Shortlisting machine learning-based stock trading recommendations using
candlestickpatternrecognition.ExpertSystemswithApplications216:119493.[CrossRef]
Di Persio, Luca, and Oleksandr Honchar. 2017. Recurrent neural networks approach to the financial forecast of Google assets.
InternationalJournalofMathematicsandComputersinSimulation11:7–13.
Dospinescu,Nicoleta,andOctavianDospinescu.2019.AProfitabilityRegressionModelInFinancialCommunicationOfRomanian
StockExchange’sCompanies.EcoforumJournal8:4.
Gite,Shilpa,ShrutiPatil,DeepakDharrao,MadhuriYadav,SnehaBasak,ArundarasiRajendran,andKetanKotecha.2023.Textual
FeatureExtractionUsingAntColonyOptimizationforHateSpeechClassification. BigDataandCognitiveComputing7: 45.
[CrossRef]
Grigoryan,Hakob.2017.StockMarketTrendPredictionUsingSupportVectorMachinesandVariableSelectionMethods.Advancesin
IntelligentSystemsResearch(AISR)2017:210–13.[CrossRef]
Gururaj,Vaishnavi,V.R.Shriya,andK.Ashwini.2019.StockMarketPredictionusingLinearRegressionandSupportVectorMachines.
InternationalJournalofAppliedEngineeringResearch14:1931–34.
Hu,Weilong,Yain-WharSi,SimonFong,andRaymondYiuKeungLau.2019.Aformalapproachtocandlestickpatternclassification
infinancialtimeseries.AppliedSoftComputing84:105700.[CrossRef]
Hu,Zexin,YiqiZhao,andMatloobKhushi.2021.Asurveyofforexandstockpricepredictionusingdeeplearning.AppliedSystem
Innovation4:9.[CrossRef]
Jiang,Weiwei.2021.Applicationsofdeeplearninginstockmarketprediction:Recentprogress.ExpertSystemswithApplications184:
115537.[CrossRef]
Jose,Jithina,SujaCherukullapurathMana,andB.KeerthiSamhitha. 2019. AnEfficientSystemtoPredictandAnalyzeStockData
usingHadoopTechniques.InternationalJournalofRecentTechnologyandEngineering(IJRTE)8:1039–43.[CrossRef]
Kaczmarek, Tomasz, andKatarzynaPerez. 2021. Buildingportfoliosbasedonmachinelearningpredictions. EconomicResearch-
EkonomskaIstraživanja35:19–37.[CrossRef]
Kaninde, Sumedh, Manish Mahajan, Aditya Janghale, and Bharti Joshi. 2022. Stock Price Prediction Using Facebook Prophet.
InternationalJournalofResearchinEngineeringandScience44:03060.[CrossRef]
Kardani,Navid,AnnanZhou,MajidrezaNazem,andShui-LongShen.2020.Improvedpredictionofslopestabilityusingahybrid
stackingensemblemethodbasedonfiniteelementanalysisandfielddata.JournalofRockMechanicsandGeotechnicalEngineering
13:188–201.[CrossRef]
Kedar,S.V.2021.StockMarketIncreaseandDecreaseusingTwitterSentimentAnalysisandARIMAModel.TurkishJournalofComputer
andMathematicsEducation(TURCOMAT)12:146–61.[CrossRef]
Khairi,TeabaW.A.,RanaM.Zaki,andWisamA.Mahmood.2019.StockPricePredictionusingTechnical,FundamentalandNews
basedApproach.Paperpresentedat20192ndScientificConferenceofComputerSciences(SCCS),Baghdad,Iraq,March27–28.
Khan,Wasiat,MustansarAliGhazanfar,MuhammadAwaisAzam,AminKarami,KhaledH.Alyoubi,andAhmedS.Alfakeeh.2020.
Stockmarketpredictionusingmachinelearningclassifiersandsocialmedia,news.JournalofAmbientIntelligenceandHumanized
Computing13:3433–56.[CrossRef]
Kumar,Deepak,PradeeptaKumarSarangi,andRajitVerma. 2021. Asystematicreviewofstockmarketpredictionusingmachine
learningandstatisticaltechniques.MaterialsToday:Proceedings49:3187–91.[CrossRef]
Kumar,Saurav,andDhrubaNingombam. 2018. Short-TermForecastingofStockPricesUsingLongShortTermMemory. Paper
presentedat2018InternationalConferenceonInformationTechnology(ICIT),HongKong,China,December29–31.
Lambert,Clive.2009.CandlestickCharts:AnIntroductiontoUsingCandlestickCharts.Petersfield:HarrimanHouseLimited.
Li,AudelianoWolian,andGuilhermeSousaBastos.2020.StockMarketForecastingUsingDeepLearningandTechnicalAnalysis:A
SystematicReview.IEEEAccess8:185232–242.[CrossRef]
Li,Yang,andYiPan.2021.Anovelensembledeeplearningmodelforstockpredictionbasedonstockpricesandnews.International
JournalofDataScienceandAnalytics13:139–49.[CrossRef][PubMed]
Lim,Kian-Ping,andRobertBrooks. 2011. Theevolutionofstockmarketefficiencyovertime: Asurveyoftheempiricalliterature.
JournalofEconomicSurveys25:69–108.[CrossRef]
Lim,YiXuan,andConsilzTan.2021.Donegativeeventsreallyhavedeterioratingeffectsonstockperformance?Acomparativestudy
onTesla(US)andNio(China).JournalofAsianBusinessandEconomicStudies29:105–19.[CrossRef]
Manish,Kumar,andM.Thenmozhi.2014.ForecastingstockindexreturnsusingARIMA-SVM,ARIMA-ANN,andARIMA-random
foresthybridmodels.InternationalJournalofBankingAccountingandFinance5:284–308.
Mann,Jordan,andJ.NathanKutz. 2016. Dynamicmodedecompositionforfinancialtradingstrategies. QuantitativeFinance16:
1643–55.[CrossRef]
Manojlovic´,Teo,andIvanŠtajduhar.2015.Predictingstockmarkettrendsusingrandomforests:AsampleoftheZagrebstockexchange.
PaperpresentedatInternationalConventiononInformationandCommunicationTechnologyElectronicsandMicroelectronics,
Opatija,Croatia,May25–29.
Mashadihasanli,Tamerlan.2022.StockMarketPriceForecastingUsingtheArimaModel:AnApplicationtoIstanbul,Turkiye.Journal
ofEconomicPolicyResearches9:439–54.[CrossRef]

Int.J.FinancialStud.2023,11,94 21of22
Mohapatra,Sabyasachi,RohanMukherjee,ArindamRoy,AnirbanSengupta,andAmitPuniyani. 2022. CanEnsembleMachine
LearningMethodsPredictStockReturnsforIndianBanksUsingTechnicalIndicators?JournalofRiskandFinancialManagement8:
350.[CrossRef]
Mukherjee,Somenath,BikashSadhukhan,NairitaSarkar,DebajyotiRoy,andSoumilDe.2021.Stockmarketpredictionusingdeep
learningalgorithms.CAAITransactionsonIntelligenceTechnology8:82–94.[CrossRef]
Nabipour,Mojtaba,PooyanNayyeri,HamedJabani,S.Shahab,andAmirMosavi.2020.PredictingStockMarketTrendsUsingMachine
LearningandDeepLearningAlgorithmsViaContinuousandBinaryData;aComparativeAnalysis.IEEEAccess8:150199–212.
[CrossRef]
Nikou,Mahla,GholamrezaMansourfar,andJamshidBagherzadeh.2019.StockpricepredictionusingDEEPlearningalgorithmandits
comparisonwithmachinelearningalgorithms.IntelligentSystemsinAccounting,FinanceandManagement26:164–74.[CrossRef]
Nti,IsaacKofi,AdebayoFelixAdekoya,andBenjaminAsubamWeyori.2020.Acomprehensiveevaluationofensemblelearningfor
stock-marketprediction.JournalofBigData7:1–40.[CrossRef]
Obthong,Mehtabhorn,NongnuchTantisantiwong,WatthanasakJeamwatthanachai,andGaryWills. 2020. ASurveyonMachine
LearningforStockPricePrediction:AlgorithmsandTechniques.Paperpresentedat2ndInternationalConferenceonFinance,
Economics,ManagementandITBusiness,Prague,CzechRepublic,May5–6.
Parray,IrfanRamzan,SurinderSinghKhurana,MunishKumar,andAliA.Altalbe. 2020. Timeseriesdataanalysisofstockprice
movementusingmachinelearningtechniques.SoftComputing24:16509–17.[CrossRef]
Patel,Jigar,SahilShah,PriyankThakkar,andKetanKotecha. 2015. PredictingstockandstockpriceindexmovementusingTrend
DeterministicDataPreparationandmachinelearningtechniques.ExpertSystemswithApplications42:259–68.[CrossRef]
Pathak,Ashwini,andSakshiPathak.2020.StudyofMachinelearningAlgorithmsforStockMarketPrediction.InternationalJournalof
EngineeringResearch&Technology(IJERT)9:6.
Polamuri,SubbaRao,KudipudiSrinivas,andA.KrishnaMohan.2019.StockMarketPricesPredictionusingRandomForestandExtra
TreeRegression.InternationalJournalofRecentTechnologyandEngineering8:1224–28.[CrossRef]
Pramod,B.S.,andMallikarjunaShastryPm.2021.StockPricePredictionUsingLSTM.TestEngineeringandManagement83:5246–51.
Qiu,Jiayu,BinWang,andChangjunZhou. 2020. Forecastingstockpriceswithlong-shorttermmemoryneuralnetworkbasedon
attentionmechanism.PLoSONE15:e0227222.[CrossRef][PubMed]
Raghavendra,Kumar,PardeepKumar,andYugalKumar.2021.Analysisoffinancialtimeseriesforecastingusingdeeplearningmodel.
Paperpresentedat202111thInternationalConferenceonCloudComputing,DataScience&Engineering(Confluence),Uttar
Pradesh,India,January28–29;pp.877–81.
Reddy,NivedithaN.,E.Naresh,andVijayaKumarB.P.2020. PredictingStockPriceUsingSentimentalAnalysisThroughTwitter
Data. Paperpresentedat2020IEEEInternationalConferenceonElectronics,ComputingandCommunicationTechnologies
(CONECCT),Bangalore,India,July2–4.
Ren,Rui,DeshengDashWu,andTianxiangLiu.2019.ForecastingStockMarketMovementDirectionUsingSentimentAnalysisand
SupportVectorMachine.IEEESystemsJournal13:760–70.[CrossRef]
Sadorsky,Perry.2021.ARandomForestsApproachtoPredictingCleanEnergyStockPrices.JournalofRiskandFinancialManagement
14:48.[CrossRef]
Salles,Thiago,MarcosGonçalves,VictorRodrigues,andLeonardoRocha.2018.Improvingrandomforestsbyneighborhoodprojection
foreffectivetextclassification.InformationSystems77:1–21.[CrossRef]
SathishKumar,R.,R.Girivarman,S.Parameshwaran,andV.Sriram.2020.StockPricePredictionUsingDeepLearningandSentimental
Analysis.JETIR7:346–54.
Seethalakshmi,Ramaswamy.2018.Analayisofstockmarketpredictorvariablesusinglinearregression.InternationalJournalofPureand
AppliedMathematics119:369–78.
Setiani,Ida,MeilanyNonsiTentua,andSunggitoOyama.2020.PredictionofBankingStockPricesUsingNaïveBayesMethod.Journal
ofPhysicsConferenceSeries1823:012059.[CrossRef]
Shah,Dev,HarunaIsah,andFarhanaZulkernine.2019.StockMarketAnalysis:AReviewandTaxonomyofPredictionTechniques.
InternationalJournalofFinancialStudies7:26.[CrossRef]
Shahi, Tej Bahadur, Ashish Shrestha, Arjun Neupane, and William Guo. 2020. Stock Price Forecasting with Deep Learning: A
ComparativeStudy.MathematicsandComputerScience8:1441.[CrossRef]
Sharaf,Marwa,EzzEl-DinHemdan,AymanEl-Sayed,andNirmeenA.El-Bahnasawy.2022.Anefficienthybridstocktrendprediction
systemduringCOVID-19pandemicbasedonstacked-LSTMandnewssentimentanalysis.MultimediaToolsandApplications28:
1–33.[CrossRef]
Shen,Jingyi,andM.OmairShafiq.2020.Short-termstockmarketpricetrendpredictionusingacomprehensivedeeplearningsystem.
JournalofBigData7:1–33.[CrossRef]
Sidra,Mehtab,andJaydipSen.2020.Atimeseriesanalysis-basedstockpricepredictionusingmachinelearninganddeeplearning
models.arXivarXiv:2004.11697.
Smita,Mrinalini.2021.LogisticRegressionModelForPredictingPerformanceofS&PBSE30CompanyUsingIBMSPSS.International
JournalofMathematicsTrendsandTechnology67:118–34.[CrossRef]
Soni,Payal,YogyaTewari,andDeepaKrishnan.2022.MachineLearningapproachesinstockpriceprediction:Asystematicreview.
JournalofPhysicsConferenceSeries2161:012065.[CrossRef]

Int.J.FinancialStud.2023,11,94 22of22
Sprenger,TimmO.,andIsabellM.Welpe.2011.Newsornoise?Thestockmarketreactiontodifferenttypesofcompany-specificnews
events.SSRNElectronicJournal.[CrossRef]
Suresh,N.,B.Priya,andG.Lakshmi.2022.HistoricalAnalysisandForecastingofStockMarketUsingFbprophet.SouthAsianJournal
ofEngineeringandTechnology12:152–57.[CrossRef]
Tanuwijaya,Julius,andSengHansun.2019.LQ45StockIndexPredictionusingk-NearestNeighborsRegression.InternationalJournalof
RecentTechnologyandEngineering8:2388–91.[CrossRef]
Umer,Muhammad,MuhammadAwais,andMuhammadMuzammul.2019.StockMarketPredictionUsingMachineLearning(ML)
Algorithms.ADCAIJAdvancesinDistributedComputingandArtificialIntelligenceJournal8:97–116.[CrossRef]
Venkat,Projects.2022.StockMarketTrendPredictionUsingK-NearestNeighbor(KNN)Algorithm.JournalofEngineeringSciences
3:32–44.
Vo,Nguyen,andRobertS´lepaczuk.2022.ApplyingHybridARIMA-SGARCHinAlgorithmicInvestmentStrategiesonS&P500Index.
Entropy24:158.[CrossRef][PubMed]
Vuong,PhamHoang,TrinhTanDat,TieuKhoiMai,andPhamHoangUyen.2022.Stock-PriceForecastingBasedonXGBoostand
LSTM.ComputerSystemsScience&Engineering40:237–46.
Xu,Ying,CuijuanYang,ShaoliangPeng,andYusukeNojima.2020.Ahybridtwo-stagefinancialstockforecastingalgorithmbasedon
clusteringandensemblelearning.AppliedIntelligence50:3852–67.[CrossRef]
Yadav,Ashima,andDineshKumarVishwakarma. 2019. Sentimentanalysisusingdeeplearningarchitectures: Areview. Artificial
IntelligenceReview53:4335–85.[CrossRef]
Yang,Liu.2019.Novelvolatilityforecastingusingdeeplearning-longshorttermmemoryrecurrentneuralnetworks.ExpertSystems
withApplications132:99–109.
Zhong,Xiao,andDavidEnke.2019.Predictingthedailyreturndirectionofthestockmarketusinghybridmachinelearningalgorithms.
FinancialInnovation5:1–20.[CrossRef]
Zhou,Xingyu,ZhisongPan,GuyuHu,SiqiTang,andChengZhao.2018.StockMarketPredictiononHigh-FrequencyDataUsing
GenerativeAdversarialNets.MathematicalProblemsinEngineering2018:4907423.[CrossRef]
Zhu,Yongqiong.2020.StockpricepredictionusingtheRNNmodel.JournalofPhysicsConferenceSeries1650:032103.[CrossRef]
Zhu,Zhe,andKexinHe. 2022. PredictionofAmazon’sStockPriceBasedonARIMA,XGBoost,andLSTMModels. Proceedingsof
BusinessandEconomicStudies5:127–36.[CrossRef]
Zizi,Youssef,AmineJamali-Alaoui,BadreddineElGoumi,MohamedOudgou,andAbdeslamElMoudden.2021.AnOptimalModel
ofFinancialDistressPrediction:AComparativeStudybetweenNeuralNetworksandLogisticRegression.Risks9:200.[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.