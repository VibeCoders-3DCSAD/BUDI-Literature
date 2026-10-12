---
conversion_metadata:
  converted_at: "2026-10-11T15:00:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Chandola et al., 2009.pdf"
  source_pdf_sha256: "64150ea3947512e2436c75ef9561349df274382e2f0b842fccf621fe14602ac1"
  page_count: 58
  markdown_char_count: 201274
---

Anomaly Detection: A Survey
VARUNCHANDOLA,ARINDAMBANERJEE,andVIPINKUMAR
UniversityofMinnesota 15
Anomaly detection is an important problem that has been researched within diverse research areas and
applicationdomains.Manyanomalydetectiontechniqueshavebeenspecificallydevelopedforcertainappli-
cationdomains,whileothersaremoregeneric.Thissurveytriestoprovideastructuredandcomprehensive
overviewoftheresearchonanomalydetection.Wehavegroupedexistingtechniquesintodifferentcategories
basedontheunderlyingapproachadoptedbyeachtechnique.Foreachcategorywehaveidentifiedkeyas-
sumptions,whichareusedbythetechniquestodifferentiatebetweennormalandanomalousbehavior.When
applyingagiventechniquetoaparticulardomain,theseassumptionscanbeusedasguidelinestoassess
theeffectivenessofthetechniqueinthatdomain.Foreachcategory,weprovideabasicanomalydetection
technique,andthenshowhowthedifferentexistingtechniquesinthatcategoryarevariantsofthebasic
technique.Thistemplateprovidesaneasierandmoresuccinctunderstandingofthetechniquesbelongingto
eachcategory.Further,foreachcategory,weidentifytheadvantagesanddisadvantagesofthetechniquesin
thatcategory.Wealsoprovideadiscussiononthecomputationalcomplexityofthetechniquessinceitisan
importantissueinrealapplicationdomains.Wehopethatthissurveywillprovideabetterunderstanding
ofthedifferentdirectionsinwhichresearchhasbeendoneonthistopic,andhowtechniquesdevelopedin
oneareacanbeappliedindomainsforwhichtheywerenotintendedtobeginwith.
CategoriesandSubjectDescriptors:H.2.8[DatabaseManagement]:DatabaseApplications—Datamining
GeneralTerms:Algorithms
AdditionalKeyWordsandPhrases:Anomalydetection,outlierdetection
ACMReferenceFormat:
Chandola,V.,Banerjee,A.,andKumar,V.2009.Anomalydetection:Asurvey.ACMComput.Surv.41,3,
Article15(July2009),58pages. DOI=10.1145/1541880.1541882
http://doi.acm.org/10.1145/1541880.1541882
1. INTRODUCTION
Anomalydetectionreferstotheproblemoffindingpatternsindatathatdonotconform
toexpectedbehavior.Thesenonconformingpatternsareoftenreferredtoasanomalies,
outliers, discordant observations, exceptions, aberrations, surprises, peculiarities, or
This work was supported by NASA under award NNX08AC36A, NSF grant number CNS-0551551, NSF
ITRGrantACI-0325949,NSFIIS-0713227,andNSFGrantIIS-0308264.Accesstocomputingfacilitieswas
providedbytheDigitalTechnologyConsortium.
Author’s address: V. Chandola, Computer Science Department, University of Minnesota, 200 Union St.,
Minneapolis,MN55414.
Permissiontomakedigitalorhardcopiesofpartorallofthisworkforpersonalorclassroomuseisgranted
withoutfeeprovidedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthat
copiesshowthisnoticeonthefirstpageorinitialscreenofadisplayalongwiththefullcitation.Copyrightsfor
componentsofthisworkownedbyothersthanACMmustbehonored.Abstractingwithcreditispermitted.
Tocopyotherwise,torepublish,topostonservers,toredistributetolists,ortouseanycomponentofthis
work in other works requires prior specific permission and/or a fee. Permissions may be requested from
PublicationsDept.,ACM,Inc.,2PennPlaza,Suite701,NewYork,NY10121-0701USA,fax+1(212)869-
0481,orpermissions@acm.org.
(cid:2)c2009ACM0360-0300/2009/07-ART15$10.00
DOI10.1145/1541880.1541882http://doi.acm.org/10.1145/1541880.1541882
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:2 V.Chandolaetal.
Fig.1. Asimpleexampleofanomaliesinatwo-dimensionaldataset.
contaminants in different application domains. Of these, anomalies and outliers are
two terms used most commonly in the context of anomaly detection; sometimes inter-
changeably. Anomaly detection finds extensive use in a wide variety of applications
such as fraud detection for credit cards, insurance, or health care, intrusion detection
for cyber-security, fault detection in safety critical systems, and military surveillance
forenemyactivities.
Theimportanceofanomalydetectionisduetothefactthatanomaliesindatatrans-
latetosignificant,andoftencritical,actionableinformationinawidevarietyofappli-
cationdomains.Forexample,ananomaloustrafficpatterninacomputernetworkcould
meanthatahackedcomputerissendingoutsensitivedatatoanunauthorizeddestina-
tion[Kumar2005].AnanomalousMRIimagemayindicatethepresenceofmalignant
tumors [Spence et al. 2001]. Anomalies in credit card transaction data could indicate
creditcardoridentitytheft[Aleskerovetal.1997],oranomalousreadingsfromaspace
craftsensorcouldsignifyafaultinsomecomponentofthespacecraft[Fujimakietal.
2005].
Detectingoutliersoranomaliesindatahasbeenstudiedinthestatisticscommunity
asearlyasthe19thcentury[Edgeworth1887].Overtime,avarietyofanomalydetection
techniqueshavebeendevelopedinseveralresearchcommunities.Manyofthesetech-
niques have been specifically developed for certain application domains, while others
aremoregeneric.
Thissurveytriestoprovideastructuredandcomprehensiveoverviewoftheresearch
onanomalydetection.Wehopethatitfacilitatesabetterunderstandingofthedifferent
directionsinwhichresearchhasbeendoneonthistopic,andhowtechniquesdeveloped
inoneareacanbeappliedindomainsforwhichtheywerenotintendedtobeginwith.
1.1. WhatareAnomalies?
Anomaliesarepatternsindatathatdonotconformtoawelldefinednotionofnormal
behavior.Figure1illustratesanomaliesinasimpletwo-dimensionaldataset.Thedata
has two normal regions, N and N , since most observations lie in these two regions.
1 2
Pointsthataresufficientlyfarawayfromtheseregions,forexample,pointso ando ,
1 2
andpointsinregion O ,areanomalies.
3
Anomalies might be induced in the data for a variety of reasons, such as malicious
activity, for example, credit card fraud, cyber-intrusion, terrorist activity or break-
downofasystem,butallofthereasonshavethecommoncharacteristicthattheyare
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:3
interesting to the analyst. The interestingness or real life relevance of anomalies is a
keyfeatureofanomalydetection.
Anomalydetectionisrelatedto,butdistinctfromnoiseremoval[Tengetal.1990]and
noiseaccommodation[RousseeuwandLeroy1987],bothofwhichdealwithunwanted
noiseinthedata.Noisecanbedefinedasaphenomenonindatathatisnotofinterest
to the analyst, but acts as a hindrance to data analysis. Noise removal is driven by
theneedtoremovetheunwantedobjectsbeforeanydataanalysisisperformed.Noise
accommodationreferstoimmunizingastatisticalmodelestimationagainstanomalous
observations[Huber1974].
Another topic related to anomaly detection is novelty detection [Markou and Singh
2003a,2003b;SaundersandGero2000],whichaimsatdetectingpreviouslyunobserved
(emergent,novel)patternsinthedata,forexample,anewtopicofdiscussioninanews
group.Thedistinctionbetweennovelpatternsandanomaliesisthatthenovelpatterns
aretypicallyincorporatedintothenormalmodelafterbeingdetected.
Itshouldbenotedthatsolutionsfortheserelatedproblemsareoftenusedforanomaly
detectionandviceversa,andhencearediscussedinthisreviewaswell.
1.2. Challenges
At an abstract level, an anomaly is defined as a pattern that does not conform to
expected normal behavior. A straightforward anomaly detection approach, therefore,
istodefinearegionrepresentingnormalbehavioranddeclareanyobservationinthe
datathatdoesnotbelongtothisnormalregionasananomaly.Butseveralfactorsmake
thisapparentlysimpleapproachverychallenging:
—Defining a normal region that encompasses every possible normal behavior is very
difficult. In addition, the boundary between normal and anomalous behavior is of-
ten not precise. Thus an anomalous observation that lies close to the boundary can
actuallybenormal,andviceversa.
—When anomalies are the result of malicious actions, the malicious adversaries of-
ten adapt themselves to make the anomalous observations appear normal, thereby
makingthetaskofdefiningnormalbehaviormoredifficult.
—In many domains normal behavior keeps evolving and a current notion of normal
behaviormightnotbesufficientlyrepresentativeinthefuture.
—The exact notion of an anomaly is different for different application domains. For
example, in the medical domain a small deviation from normal (e.g., fluctuations
in body temperature) might be an anomaly, while similar deviation in the stock
market domain (e.g., fluctuations in the value of a stock) might be considered as
normal. Thus applying a technique developed in one domain to another, is not
straightforward.
—Availabilityoflabeleddatafortraining/validationofmodelsusedbyanomalydetec-
tiontechniquesisusuallyamajorissue.
—Often the data contains noise that tends to be similar to the actual anomalies and
henceisdifficulttodistinguishandremove.
Due to these challenges, the anomaly detection problem, in its most general form,
isnoteasytosolve.Infact,mostoftheexistinganomalydetectiontechniquessolvea
specificformulationoftheproblem.Theformulationisinducedbyvariousfactorssuch
asthenatureofthedata,availabilityoflabeleddata,typeofanomaliestobedetected,
andsoon.Often,thesefactorsaredeterminedbytheapplicationdomaininwhichthe
anomaliesneedtobedetected.Researchershaveadoptedconceptsfromdiversedisci-
plines such as statistics, machine learning, data mining, information theory, spectral
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:4 V.Chandolaetal.
Fig.2. Keycomponentsassociatedwithananomalydetectiontechnique.
theory,andhaveappliedthemtospecificproblemformulations.Figure2showsthekey
componentsassociatedwithanyanomalydetectiontechnique.
1.3. RelatedWork
Anomaly detection has been the topic of a number of surveys and review articles, as
well as books. Hodge and Austin [2004] provide an extensive survey of anomaly de-
tection techniques developed in machine learning and statistical domains. A broad
review of anomaly detection techniques for numeric as well as symbolic data is pre-
sentedbyAgyemangetal.[2006].Anextensivereviewofnoveltydetectiontechniques
using neural networks and statistical approaches has been presented in Markou and
Singh [2003a] and Markou and Singh [2003b], respectively. Patcha and Park [2007]
andSnyder[2001]presentasurveyofanomalydetectiontechniquesusedspecifically
for cyber-intrusion detection. A substantial amount of research on outlier detection
has been done in statistics and has been reviewed in several books [Rousseeuw and
Leroy 1987; Barnett and Lewis 1994; Hawkins 1980] as well as other survey articles
[BeckmanandCook1983;Bakaretal.2006].
Table I shows the set of techniques and application domains covered by our survey
andthevariousrelatedsurveyarticles.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:5
| TableI. | ComparisonofourSurveytoOtherRelatedSurveyArticles.1—OurSurvey, |     |     |     |
| ------- | -------------------------------------------------------------- | --- | --- | --- |
2—HodgeandAustin[2004],3—Agyemangetal.[2006],4—MarkouandSingh[2003a],
5—MarkouandSingh[2003b],6—PatchaandPark[2007],7—BeckmanandCook[1983],
8—Bakaretal.[2006]
|     |                     | 1 2 | 3 4 5 | 6 7 8 |
| --- | ------------------- | --- | ----- | ----- |
|     |                     | √ √ | √ √   | √     |
|     | ClassificationBased | √ √ | √     | √     |
ClusteringBased
|            |                      | √ √ | √   | √ √   |
| ---------- | -------------------- | --- | --- | ----- |
|            | NearestNeighborBased | √ √ | √ √ | √ √ √ |
| Techniques | Statistical          | √   |     |       |
|            | InformationTheoretic | √   |     |       |
|            | Spectral             | √   |     | √     |
Cyber-IntrusionDetection
√
|              | FraudDetection            | √   |     |     |
| ------------ | ------------------------- | --- | --- | --- |
|              | MedicalAnomalyDetection   | √   |     |     |
| Applications | IndustrialDamageDetection | √   |     |     |
|              | ImageProcessing           | √   |     |     |
TextualAnomalyDetection
√
SensorNetworks
1.4. OurContributions
This survey is an attempt to provide a structured and broad overview of extensive
research on anomaly detection techniques spanning multiple research areas and ap-
plicationdomains.
Most of the existing surveys on anomaly detection either focus on a particu-
lar application domain or on a single research area. Agyemang et al. [2006] and
Hodge and Austin [2004] are two related works that group anomaly detection
into multiple categories and discuss techniques under each category. This survey
builds upon these two works by significantly expanding the discussion in several
directions.
Weaddtwomorecategoriesofanomalydetectiontechniques,informationtheoretic
and spectral techniques, to the four categories discussed in Agyemang et al. [2006]
and Hodge and Austin [2004]. For each of the six categories, we not only discuss the
techniques, but also identify unique assumptions regarding the nature of anomalies
madebythetechniquesinthatcategory.Theseassumptionsarecriticalfordetermining
whenthetechniquesinthatcategorywouldbeabletodetectanomalies,andwhenthey
would fail. For each category, we provide a basic anomaly detection technique, and
then show how the different existing techniques in that category are variants of the
basictechnique.Thistemplateprovidesaneasierandmoresuccinctunderstandingof
the techniques belonging to each category. Further, for each category we identify the
advantages and disadvantages of the techniques. We also provide a discussion of the
computational complexity of the techniques since that is an important issue in real
applicationdomains.
While some of the existing surveys mention the different applications of anomaly
detection,weprovideadetaileddiscussionoftheapplicationdomainswhereanomaly
detection techniques have been used. For each domain we discuss the notion of an
anomaly, the different aspects of the anomaly detection problem, and the challenges
faced by the anomaly detection techniques. We also provide a list of techniques that
havebeenappliedineachapplicationdomain.
Theexistingsurveysdiscussanomalydetectiontechniquesthatdetectthesimplest
formofanomalies.Wedistinguishsimpleanomaliesfromcomplexanomalies.Thedis-
cussionofapplicationsofanomalydetectionrevealsthatformostapplicationdomains,
theinterestinganomaliesarecomplexinnature,whilemostofthealgorithmicresearch
hasfocussedonsimpleanomalies.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:6 V.Chandolaetal.
1.5. Organization
This survey is organized into three parts and its structure closely follows Figure 2.
In Section 2, we identify the various aspects that determine the formulation of the
problem and highlight the richness and complexity associated with anomaly detec-
tion. We distinguish simple anomalies from complex anomalies and define two types
ofcomplexanomalies:contextualandcollectiveanomalies.InSection3,webrieflyde-
scribethedifferentapplicationdomainstowhichanomalydetectionhasbeenapplied.
In subsequent sections we provide a categorization of anomaly detection techniques
based on the research area to which they belong. A majority of the techniques can
becategorizedintoclassification-based(Section4),nearestneighbor-based(Section5),
clustering-based (Section 6), and statistical techniques (Section 7). Some techniques
belong to research areas such as information theory (Section 8), and spectral theory
(Section 9). For each category of techniques we also discuss their computational com-
plexity for training and testing phases. In Section 10 we discuss various contextual
anomaly detection techniques. We present some discussion of the limitations and rel-
ative performance of various existing techniques in Section 11. Section 12 contains
concludingremarks.
2. DIFFERENTASPECTSOFANANOMALYDETECTIONPROBLEM
Thissectionidentifiesanddiscussesthedifferentaspectsofanomalydetection.Asmen-
tionedearlier,aspecificformulationoftheproblemisdeterminedbyseveraldifferent
factorssuchasthenatureoftheinputdata,theavailabilityorunavailabilityoflabels
as well as the constraints and requirements induced by the application domain. This
section brings forth the richness in the problem domain and justifies the need for the
broadspectrumofanomalydetectiontechniques.
2.1. NatureofInputData
Akeyaspectofanyanomalydetectiontechniqueisthenatureoftheinputdata.Input
isgenerallyacollectionofdatainstances(alsoreferredasobject,record,point,vector,
pattern, event, case, sample, observation, or entity) [Tan et al. 2005, Chapter 2]. Each
data instance can be described using a set of attributes (also referred to as variable,
characteristic, feature, field, or dimension). The attributes can be of different types
suchasbinary,categorical,orcontinuous.Eachdatainstancemightconsistofonlyone
attribute(univariate)ormultipleattributes(multivariate).Inthecaseofmultivariate
datainstances,allattributesmightbeofsametypeormightbeamixtureofdifferent
datatypes.
The nature of attributes determines the applicability of anomaly detection tech-
niques. For example, for statistical techniques different statistical models have to be
used for continuous and categorical data. Similarly, for nearest-neighbor-based tech-
niques, the nature of attributes would determine the distance measure to be used.
Often, instead of the actual data, the pairwise distance between instances might be
providedintheformofadistanceorsimilaritymatrix.Insuchcases,techniquesthat
require original data instances are not applicable, for example, many statistical and
classification-basedtechniques.
Input data can also be categorized based on the relationship present among data
instances [Tan et al. 2005]. Most of the existing anomaly detection techniques deal
with record data or point data, in which no relationship is assumed among the data
instances.
Ingeneral,datainstancescanberelatedtoeachother.Someexamplesaresequence
data, spatial data, and graph data. In sequence data, the data instances are linearly
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:7
ordered, for example, time-series data, genome sequences, and protein sequences. In
spatial data, each data instance is related to its neighboring instances, for example,
vehicular traffic data, and ecological data. When the spatial data has a temporal (se-
quential) component it is referred to as spatio-temporal data, for example, climate
data. In graph data, data instances are represented as vertices in a graph and are
connected to other vertices with edges. Later in this section we will discuss situa-
tions where such relationships among data instances become relevant for anomaly
detection.
2.2. TypeofAnomaly
An important aspect of an anomaly detection technique is the nature of the desired
anomaly.Anomaliescanbeclassifiedintofollowingthreecategories:
2.2.1. PointAnomalies. Ifanindividualdatainstancecanbeconsideredasanomalous
withrespecttotherestofdata,thentheinstanceistermedapointanomaly.Thisisthe
simplesttypeofanomalyandisthefocusofmajorityofresearchonanomalydetection.
Forexample,inFigure1,pointso ando ,aswellaspointsinregion O ,lieoutside
1 2 3
the boundary of the normal regions, and hence are point anomalies since they are
differentfromnormaldatapoints.
As a real-life example, consider credit card fraud detection. Let the data set cor-
respond to an individual’s credit card transactions. For the sake of simplicity, let us
assume that the data is defined using only one feature: amount spent. A transaction
forwhichtheamountspentisveryhighcomparedtothenormalrangeofexpenditure
forthatpersonwillbeapointanomaly.
2.2.2. ContextualAnomalies. Ifadatainstanceisanomalousinaspecificcontext,but
not otherwise, then it is termed a contextual anomaly (also referred to as conditional
anomaly[Songetal.2007]).
The notion of a context is induced by the structure in the data set and has to be
specifiedasapartoftheproblemformulation.Eachdatainstanceisdefinedusingthe
followingtwosetsofattributes:
(1) Contextualattributes.Thecontextualattributesareusedtodeterminethecontext
(orneighborhood)forthatinstance.Forexample,inspatialdatasets,thelongitude
and latitude of a location are the contextual attributes. In time-series data, time
is a contextual attribute that determines the position of an instance on the entire
sequence.
(2) Behavioral attributes. The behavioral attributes define the noncontextual charac-
teristics of an instance. For example, in a spatial data set describing the average
rainfall of the entire world, the amount of rainfall at any location is a behavioral
attribute.
Theanomalousbehaviorisdeterminedusingthevaluesforthebehavioralattributes
within a specific context. A data instance might be a contextual anomaly in a given
context, but an identical data instance (in terms of behavioral attributes) could be
considerednormalinadifferentcontext.Thispropertyiskeyinidentifyingcontextual
andbehavioralattributesforacontextualanomalydetectiontechnique.
Contextual anomalies have been most commonly explored in time-series data
[Weigend et al. 1995; Salvador and Chan 2003] and spatial data [Kou et al. 2006;
Shekhar et al. 2001]. Figure 3 shows one such example for a temperature time-series
thatshowsthemonthlytemperatureofanareaoverthelastfewyears.Atemperature
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:8 V.Chandolaetal.
Fig.3. Contextualanomalyt2inatemperaturetime-series.Notethatthetemperatureattimet1issame
asthatattimet2butoccursinadifferentcontextandhenceisnotconsideredasananomaly.
◦
of35 Fmightbenormalduringthewinter(attimet )atthatplace,butthesamevalue
1
duringthesummer(attimet )wouldbeananomaly.
2
A similar example can be found in the credit card fraud detection domain. A con-
textual attribute in the credit card domain can be the time of purchase. Suppose an
individual usually has a weekly shopping bill of $100 except during the Christmas
week, when it reaches $1000. A new purchase of $1000 in a week in July will be con-
sidered a contextual anomaly, since it does not conform to the normal behavior of the
individualinthecontextoftimeeventhoughthesameamountspentduringChristmas
weekwillbeconsiderednormal.
Thechoiceofapplyingacontextualanomalydetectiontechniqueisdeterminedbythe
meaningfulnessofthecontextualanomaliesinthetargetapplicationdomain.Another
keyfactoristheavailabilityofcontextualattributes.Inseveralcasesdefiningacontext
isstraightforward,andhenceapplyingacontextualanomalydetectiontechniquemakes
sense. In other cases, defining a context is not easy, making it difficult to apply such
techniques.
2.2.3. CollectiveAnomalies. Ifacollectionofrelateddatainstancesisanomalouswith
respect to the entire data set, it is termed a collective anomaly. The individual data
instancesinacollectiveanomalymaynotbeanomaliesbythemselves,buttheiroccur-
rencetogetherasacollectionisanomalous.Figure4isanexamplethatshowsahuman
electrocardiogram output [Goldberger et al. 2000]. The highlighted region denotes an
anomaly because the same low value exists for an abnormally long time (correspond-
ing to an Atrial Premature Contraction). Note that that low value by itself is not an
anomaly.
As an another illustrative example, consider a sequence of actions occurring in a
computerasshownbelow:
... http-web, buffer-overflow, http-web, http-web, smtp-mail, ftp, http-web, ssh, smtp-mail,
http-web,ssh,buffer-overflow,ftp,http-web,ftp,smtp-mail,http-web...
Thehighlightedsequenceofevents(buffer-overflow,ssh,ftp)correspondtoatyp-
ical Web-based attack by a remote machine followed by copying of data from the host
computertoaremotedestinationviaftp.Itshouldbenotedthatthiscollectionofevents
is an anomaly, but the individual events are not anomalies when they occur in other
locationsinthesequence.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:9
Fig.4. CollectiveanomalycorrespondingtoanAtrialPrematureContractioninanhumanelectrocardiogram
output.
Collectiveanomalieshavebeenexploredforsequencedata[Forrestetal.1999;Sun
etal.2006],graphdata[NobleandCook2003],andspatialdata[Shekharetal.2001].
It should be noted that while point anomalies can occur in any data set, collective
anomaliescanoccuronlyindatasetsinwhichdatainstancesarerelated.Incontrast,
occurrenceofcontextualanomaliesdependsontheavailabilityofcontextattributesin
thedata.Apointanomalyoracollectiveanomalycanalsobeacontextualanomalyif
analyzedwithrespecttoacontext.Thusapointanomalydetectionproblemorcollec-
tiveanomalydetectionproblemcanbetransformedtoacontextualanomalydetection
problembyincorporatingthecontextinformation.
The techniques used for detecting collective anomalies are very different than the
point and contextual anomaly detection techniques, and require a separate detailed
discussion. Hence we chose to not cover them in this survey. For a brief review of the
research done in the field of collective anomaly detection, the reader is referred to an
extendedversionofthissurvey[Chandolaetal.2007].
2.3. DataLabels
The labels associated with a data instance denote whether that instance is normal or
anomalous.1 It should be noted that obtaining labeled data that is accurate as well
as representative of all types of behaviors, is often prohibitively expensive. Labeling
is often done manually by a human expert and hence substantial effort is required to
obtainthelabeledtrainingdataset.Typically,gettingalabeledsetofanomalousdata
instances that covers all possible type of anomalous behavior is more difficult than
gettinglabelsfornormalbehavior.Moreover,theanomalousbehaviorisoftendynamic
innature,forexample,newtypesofanomaliesmightarise,forwhichthereisnolabeled
training data. In certain cases, such as air traffic safety, anomalous instances would
translatetocatastrophicevents,andhenceareveryrare.
Basedontheextenttowhichthelabelsareavailable,anomalydetectiontechniques
canoperateinoneofthefollowingthreemodes:
1Alsoreferredtoasnormalandanomalousclasses.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:10 V.Chandolaetal.
2.3.1. Supervised Anomaly Detection. Techniques trained in supervised mode assume
the availability of a training data set that has labeled instances for normal as well
as anomaly classes. A typical approach in such cases is to build a predictive model
for normal vs. anomaly classes. Any unseen data instance is compared against the
modeltodeterminewhichclassitbelongsto.Therearetwomajorissuesthatarisein
supervisedanomalydetection.First,theanomalousinstancesarefarfewercompared
tothenormalinstancesinthetrainingdata.Issuesthatariseduetoimbalancedclass
distributionshavebeenaddressedinthedataminingandmachinelearningliterature
[Joshi et al. 2001, 2002; Chawla et al. 2004; Phua et al. 2004; Weiss and Hirsh 1998;
VilaltaandMa2002].Second,obtainingaccurateandrepresentativelabels,especially
fortheanomalyclassisusuallychallenging.Anumberoftechniqueshavebeenproposed
thatinjectartificialanomaliesintoanormaldatasettoobtainalabeledtrainingdata
set [Theiler and Cai 2003; Abe et al. 2006; Steinwart et al. 2005]. Other than these
twoissues,thesupervisedanomalydetectionproblemissimilartobuildingpredictive
models.Hencewewillnotaddressthiscategoryoftechniquesinthissurvey.
2.3.2. SemisupervisedAnomalyDetection. Techniquesthatoperateinasemisupervised
mode, assume that the training data has labeled instances only for the normal class.
Sincetheydonotrequirelabelsfortheanomalyclass,theyaremorewidelyapplicable
thansupervisedtechniques.Forexample,inspacecraftfaultdetection[Fujimakietal.
2005],ananomalyscenariowouldsignifyanaccident,whichisnoteasytomodel.The
typicalapproachusedinsuchtechniquesistobuildamodelfortheclasscorresponding
tonormalbehavior,andusethemodeltoidentifyanomaliesinthetestdata.
Alimitedsetofanomalydetectiontechniquesexiststhatassumesavailabilityofonly
theanomalyinstancesfortraining[DasguptaandNino2000;DasguptaandMajumdar
2002;Forrestetal.1999].Suchtechniquesarenotcommonlyused,primarilybecauseit
isdifficulttoobtainatrainingdatasetthatcoverseverypossibleanomalousbehavior
thatcanoccurinthedata.
2.3.3. UnsupervisedAnomalyDetection. Techniquesthatoperateinunsupervisedmode
do not require training data, and thus are most widely applicable. The techniques in
thiscategorymaketheimplicitassumptionthatnormalinstancesarefarmorefrequent
than anomalies in the test data. If this assumption is not true then such techniques
sufferfromhighfalsealarmrate.
Manysemisupervisedtechniquescanbeadaptedtooperateinanunsupervisedmode
byusingasampleoftheunlabeleddatasetastrainingdata.Suchadaptationassumes
thatthetestdatacontainsveryfewanomaliesandthemodellearnedduringtraining
isrobusttothesefewanomalies.
2.4. OutputofAnomalyDetection
An important aspect for any anomaly detection technique is the manner in which
the anomalies are reported. Typically, the outputs produced by anomaly detection
techniquesareoneofthefollowingtwotypes:
2.4.1. Scores. Scoringtechniquesassignananomalyscoretoeachinstanceinthetest
data depending on the degree to which that instance is considered an anomaly. Thus
the output of such techniques is a ranked list of anomalies. An analyst may choose to
eitheranalyzethetopfewanomaliesoruseacutoffthresholdtoselecttheanomalies.
2.4.2. Labels. Techniques in this category assign a label (normal or anomalous) to
eachtestinstance.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:11
Fig.5. Asampledatasetcomprisedofthreeoperatingsystemcalltraces.
Scoring-based anomaly detection techniques allow the analyst to use a domain-
specific threshold to select the most relevant anomalies. Techniques that provide bi-
nary labels to the test instances do not directly allow the analysts to make such a
choice,thoughthiscanbecontrolledindirectlythroughparameterchoiceswithineach
technique.
3. APPLICATIONSOFANOMALYDETECTION
Inthissectionwediscussseveralapplicationsofanomalydetection.Foreachapplica-
tiondomainwediscussthefollowingfouraspects:
—thenotionofanomaly;
—natureofthedata;
—challengesassociatedwithdetectinganomalies;
—existinganomalydetectiontechniques.
3.1. IntrusionDetection
Intrusion detection refers to detection of malicious activity (break-ins, penetrations,
andotherformsofcomputerabuse)inacomputerrelatedsystem[Phoha2002].These
maliciousactivitiesorintrusionsareinterestingfromacomputersecurityperspective.
An intrusion is different from the normal behavior of the system, and hence anomaly
detectiontechniquesareapplicableinintrusiondetectiondomain.
Thekeychallengeforanomalydetectioninthisdomainisthehugevolumeofdata.
Theanomalydetectiontechniquesneedtobecomputationallyefficienttohandlethese
largesizedinputs.Moreoverthedatatypicallycomesinastreamingfashion,thereby
requiringonlineanalysis.Anotherissuethatarisesbecauseofthelargesizedinputis
thefalsealarmrate.Sincethedataamountstomillionsofdataobjects,afewpercentof
falsealarmscanmakeanalysisoverwhelmingforananalyst.Labeleddatacorrespond-
ing to normal behavior is usually available, while labels for intrusions are not. Thus,
semisupervised and unsupervised anomaly detection techniques are preferred in this
domain.
Denning[1987]classifiesintrusiondetectionsystemsintohost-basedandnetwork-
basedintrusiondetectionsystems.
3.1.1. Host-BasedIntrusionDetectionSystems. Suchsystems(alsoreferredtoassystem
callintrusiondetectionsystems)dealwithoperatingsystemcalltraces.Theintrusions
are in the form of anomalous subsequences (collective anomalies) of the traces. The
anomaloussubsequencestranslatetomaliciousprograms,unauthorizedbehaviorand
policy violations. While all traces contain events belonging to the same alphabet, it is
theco-occurrenceofeventsthatisthekeyfactorindifferentiatingbetweennormaland
anomalousbehavior.
Thedataissequentialinnatureandthealphabetconsistsofindividualsystemcalls
asshowninFigure5.Thesecallscouldbegeneratedbyprograms[Hofmeyretal.1998]
or by users [Lane and Brodley 1999]. The alphabet is usually large (183 system calls
for SunOS 4.1x Operating System). Different programs execute these system calls in
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:12 V.Chandolaetal.
TableII. ExamplesofAnomalyDetectionTechniquesUsedforHost-BasedIntrusionDetection
TechniqueUsed Section References
StatisticalProfilingus- Section7.2.1 Forrestetal.[1996a,1999,2004,1994,1999],Hofmeyr
ingHistograms etal.[1998],KosoresowandHofmeyr[1997],Jagadish
etal.[1999],Cabreraetal.[2001],GonzalezandDas-
gupta[2003],Dasguptaetal.[2000,2002].Ghoshetal.
[1999a,1998,1999b],Debaretal.[1998],Eskinetal.
[2001],Marceau[2000],Endler[1998],Laneetal.[1999,
1997b,1997a]
MixtureofModels Section7.1.3 Eskin[2000]
NeuralNetworks Section4.1 Ghoshetal.[1998]
SupportVector Section4.3 Huetal.[2003],Helleretal.[2003]
Machines
Rule-BasedSystems Section4.4 Leeetal.[1997,1998,2000]
different sequences. The length of the sequence for each program varies. Figure 5 il-
lustrates a sample set of operating system call sequences. A key characteristic of the
datainthisdomainisthatthedatacanbetypicallyprofiledatdifferentlevels,suchas
programleveloruserlevel.Anomalydetectiontechniquesappliedforhost-basedintru-
siondetectionarerequiredtotohandlethesequentialnatureofdata.Moreover,point
anomaly detection techniques are not applicable in this domain. The techniques have
toeithermodelthesequencedataorcomputesimilaritybetweensequences.Asurveyof
differenttechniquesusedforthisproblemispresentedbySnyder[2001].Comparative
evaluations of anomaly detection for host-based intrusion detection are presented in
Forrestetal.[1999]andDasguptaandNino[2000].Someanomalydetectiontechniques
usedinthisdomainareshowninTableII.
3.1.2. Network Intrusion Detection Systems. These systems deal with detecting intru-
sions in network data. The intrusions typically occur as anomalous patterns (point
anomalies) though certain techniques model the data in a sequential fashion and de-
tectanomaloussubsequences(collectiveanomalies)[Gwaderaetal.2005b,2004].The
primaryreasonfortheseanomaliesisduetotheattackslaunchedbyoutsidehackers
whowanttogainunauthorizedaccesstothenetworkforinformationtheftortodisrupt
thenetwork.Atypicalsettingisalargenetworkofcomputersconnectedtotherestof
theworldviatheInternet.
Thedataavailableforintrusiondetectionsystemscanbeatdifferentlevelsofgran-
ularity,forexample,packetleveltraces,CISCOnet-flowsdata,andsoforth.Thedata
has a temporal aspect associated with it but most of the techniques typically do not
explicitly handle the sequential aspect. The data is high dimensional typically with a
mixofcategoricalaswellascontinuousattributes.
Achallengefacedbyanomalydetectiontechniquesinthisdomainisthatthenature
ofanomalieskeepschangingovertimeastheintrudersadapttheirnetworkattacksto
evadetheexistingintrusiondetectionsolutions.
SomeanomalydetectiontechniquesusedinthisdomainareshowninTableIII.
3.2. FraudDetection
Frauddetectionreferstodetectionofcriminalactivitiesoccurringincommercialorga-
nizationssuchasbanks,creditcardcompanies,insuranceagencies,cellphonecompa-
nies, stock market, and so on. The malicious users might be the actual customers of
the organization or might be posing as customers (also known as identity theft). The
fraudoccurswhentheseusersconsumetheresourcesprovidedbytheorganizationin
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:13
TableIII. ExamplesofAnomalyDetectionTechniquesUsedforNetworkIntrusionDetection
TechniqueUsed Section References
StatisticalProfilingusing Section7.2.1 NIDESAndersonetal.1994,1995;JavitzandValdes
Histograms 1991],EMERALD[PorrasandNeumann1997],Yaman-
ishietal.[2001,2004],Hoetal.[1999],Kruegeletal.
[2002,2003],Mahoneyetal.[2003],MahoneyandChan
[2002,2003];Sargor[1998],
ParametricStatistical Section7.1 Gwaderaetal.[2005b,2004],YeandChen[2001],Tan-
Modeling donandChan[2007]
NonparametricStatistical Section7.2.2 ChowandYeung[2002]
Modeling
BayesianNetworks Section4.2 Siaterlis and Maglaris [2004], Sebyala et al. [2002],
ValdesandSkinner[2000],Bronsteinetal.[2001],
NeuralNetworks Section4.1 HIDE [Zhang et al. 2001], NSOM [Labib and Ve-
muri2002],Smithetal.[2002],Hawkinsetal.[2002],
Kruegeletal.[2003],ManikopoulosandPapavassiliou
[2002],Ramadasetal.[2003],
SupportVectorMachines Section4.3 Eskinetal.[2002]
Rule-BasedSystems Section4.4 ADAM[Barbaraetal.2001a,2003,2001b],Fanetal.
[2001], Helmer et al. [1998], Qin and Hwang [2004],
SalvadorandChan[2003],Oteyetal.[2003]
ClusteringBased Section6 ADMIT[SequeiraandZaki2002],Eskinetal.[2002],
WuandZhang[2003],Oteyetal.[2003]
NearestNeighbor-Based Section5 MINDS[Ertozetal.2004;Chandolaetal.2006]
Spectral Section9 Shyuetal.[2003],Lakhinaetal.[2005],Thottanand
Ji[2003],Sunetal.[2007]
InformationTheoretic Section8 LeeandXiang[2001],NobleandCook[2003]
anunauthorizedway.Theorganizationsareinterestedinimmediatedetectionofsuch
fraudstopreventeconomiclosses.
Fawcett and Provost [1999] introduce the term activity monitoring as a general ap-
proachtofrauddetectioninthesedomains.Thetypicalapproachofanomalydetection
techniquesistomaintainausageprofileforeachcustomerandmonitortheprofilesto
detectanydeviations.Someofthespecificapplicationsoffrauddetectionarediscussed
below.
3.2.1. Credit Card Fraud Detection. In this domain, anomaly detection techniques are
applied to detect fraudulent credit card applications or fraudulent credit card usage
(associated with credit card thefts). Detecting fraudulent credit card applications is
similartodetectinginsurancefraud[GhoshandReilly1994].
The data is typically comprised of records defined over several dimensions such as
userID,amountspent,timebetweenconsecutivecardusage,andsoforth.Thefrauds
aretypicallyreflectedintransactionalrecords(pointanomalies)andcorrespondtohigh
payments,purchaseofitemsneverpurchasedbytheuserbefore,highrateofpurchase,
andsoforth.Thecreditcompanieshavecompletedataavailableandalsohavelabeled
records. Moreover, the data falls into distinct profiles based on the credit card user.
Henceprofilingandclusteringbasedtechniquesaretypicallyusedinthisdomain.
The challenge associated with detecting unauthorized credit card usage is that it
requiresonlinedetectionoffraudassoonasthefraudulenttransactiontakesplace.
Anomalydetectiontechniqueshavebeenappliedintwodifferentwaystoaddressthis
problem.Thefirstoneisknownasby-ownerinwhicheachcreditcarduserisprofiled
based on his/her credit card usage history. Any new transaction is compared to the
user’sprofileandflaggedasananomalyifitdoesnotmatchtheprofile.Thisapproach
istypicallyexpensivesinceitrequiresqueryingacentraldatarepository,everytimea
usermakesatransaction.Anotherapproachknownasby-operationdetectsanomalies
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:14 V.Chandolaetal.
TableIV. ExamplesofAnomalyDetectionTechniquesUsedforCreditCardFraudDetection
TechniqueUsed Section References
NeuralNetworks Section4.1 CARDWATCH[Aleskerovetal.1997],GhoshandReilly
[1994],Brauseetal.[1999],Dorronsoroetal.[1997]
Rule-BasedSystems Section4.4 Brauseetal.[1999]
Clustering Section6 BoltonandHand[1999]
TableV. ExamplesofAnomalyDetectionTechniquesUsedforMobilePhoneFraudDetection
TechniqueUsed Section References
Statistical Profiling using Section7.2.1 FawcettandProvost[1999],Coxetal.[1997]
Histograms
ParametricStatistical Section7.1 Agarwal[2005],Scott[2001]
Modeling
NeuralNetworks Section4.1 Barsonetal.[1996],Taniguchietal.[1998]
Rule-basedSystems Section4.4 Phuaetal.[2004],Taniguchietal.[1998]
from among transactions taking place at a specific geographic location. Both by-user
andby-operationtechniquesdetectcontextualanomalies.Inthefirstcasethecontext
isauser,whileinthesecondcasethecontextisthegeographiclocation.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableIV.
3.2.2. MobilePhoneFraudDetection. Mobile/cellularfrauddetectionisatypicalactivity
monitoringproblem.Thetaskistoscanalargesetofaccounts,examiningthecalling
behaviorofeach,andtoissueanalarmwhenanaccountappearstohavebeenmisused.
Calling activity may be represented in various ways, but is usually described with
call records. Each call record is a vector of features, both continuous (e.g., CALL-
DURATION)anddiscrete(e.g.,CALLING-CITY).However,thereisnoinherentprim-
itive representation in this domain. Calls can be aggregated by time, for example
intocall-hoursorcall-daysoruserorarea,dependingonthegranularitydesired.The
anomaliescorrespondtoahighvolumeofcallsorcallsmadetounlikelydestinations.
SometechniquesappliedtocellphonefrauddetectionarelistedinTableV.
3.2.3. InsuranceClaimFraudDetection. Animportantproblemintheproperty-casualty
insuranceindustryisclaimsfraud,forexample,automobileinsurancefraud.Individu-
alsandconspiratorialringsofclaimantsandprovidersmanipulatetheclaimprocessing
systemforunauthorizedandillegalclaims.Detectionofsuchfraudhasbeenveryim-
portantfortheassociatedcompaniestoavoidfinanciallosses.
The available data in this domain are the documents submitted by the claimants.
Thetechniquesextractdifferentfeatures,bothcategoricalaswellascontinuous,from
these documents. Typically, claim adjusters and investigators assess these claims for
frauds.Thesemanuallyinvestigatedcasesareusedaslabeledinstancesbysupervised
andsemisupervisedtechniquesforinsurancefrauddetection.
Insuranceclaimfrauddetectionisquiteoftenhandledasagenericactivitymonitor-
ing problem [Fawcett and Provost 1999]. Neural network-based techniques have also
been applied to identify anomalous insurance claims [He et al. 2003; Brockett et al.
1998].
3.2.4. InsiderTradingDetection. Anotherrecentapplicationofanomalydetectiontech-
niqueshasbeeninearlydetectionofInsiderTrading.Insidertradingisaphenomenon
found in stock markets, where people make illegal profits by acting on (or leak-
ing) inside information before the information is made public. The inside informa-
tion can be of different forms [Donoho 2004]. It could refer to the knowledge of a
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:15
TableVI. ExamplesofDifferentAnomalyDetectionTechniquesUsedforInsider
TradingDetection
TechniqueUsed Section References
StatisticalProfilingusingHistograms Section7.2.1 Donoho[2004],Aggarwal[2005]
InformationTheoretic Section8 Arningetal.[1996]
TableVII. ExamplesofDifferentAnomalyDetectionTechniquesUsedinMedicalandPublicHealthDomain
TechniqueUsed Section References
ParametricStatisticalModeling Section7.1 Hornetal.[2001],Laurikkalaetal.[2000],Solberg
andLahti[2005],Roberts[2002],Suzukietal.[2003]
NeuralNetworks Section4.1 CampbellandBennett[2001]
BayesianNetworks Section4.2 Wongetal.[2003]
Rule-BasedSystems Section4.4 Aggarwal[2005]
NearestNeighborbasedTechniques Section5 Linetal.[2005]
pendingmerger/acquisition,aterroristattackaffectingaparticularindustry,pending
legislation affecting a particular industry, or any information that would affect the
stock prices in a particular industry. Insider trading can be detected by identifying
anomaloustradingactivitiesinthemarket.
Theavailabledataisfromseveralheterogenoussourcessuchasoptiontradingdata,
stocktradingdata,news.Thedatahastemporalassociationssincethedataiscollected
continuously. The temporal and streaming nature has also been exploited in certain
techniques[Aggarwal2005].
Anomalydetectiontechniquesinthisdomainarerequiredtodetectfraudinanonline
manner and as early as possible, to prevent people/organizations from making illegal
profits.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableVI.
3.3. MedicalandPublicHealthAnomalyDetection
Anomalydetectioninthemedicalandpublichealthdomainstypicallyworkswithpa-
tient records. The data can have anomalies due to several reasons, such as abnormal
patientcondition,instrumentationerrors,orrecordingerrors.Severaltechniqueshave
alsofocussedondetectingdiseaseoutbreaksinaspecificarea[Wongetal.2003].Thus
the anomaly detection is a very critical problem in this domain and requires a high
degreeofaccuracy.
The data typically consists of records that may have several different types of fea-
tures,suchaspatientage,bloodgroup,andweight.Thedatamightalsohaveatemporal
aswellasspatialaspecttoit.Mostofthecurrentanomalydetectiontechniquesinthis
domain aim at detecting anomalous records (point anomalies). Typically the labeled
data belongs to the healthy patients, hence most of the techniques adopt a semisu-
pervised approach. Another form of data handled by anomaly detection techniques in
thisdomainistime-seriesdata,suchasElectrocardiograms(ECG)(Figure4)andElec-
troencephalograms(EEG).Collectiveanomalydetectiontechniqueshavebeenapplied
todetectanomaliesinsuchdata[Linetal.2005].
Themostchallengingaspectoftheanomalydetectionprobleminthisdomainisthat
thecostofclassifyingananomalyasnormalcanbeveryhigh.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableVII.
3.4. IndustrialDamageDetection
Industrial units suffer damage due to continuous usage and normal wear and tear.
Such damage needs to be detected early to prevent further escalation and losses. The
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

| 15:16 |     |     |     |     |     | V.Chandolaetal. |     |     |
| ----- | --- | --- | --- | --- | --- | --------------- | --- | --- |
TableVIII. ExamplesofAnomalyDetectionTechniquesUsedforFaultDetectioninMechanicalUnits
| TechniqueUsed | Section |     |     |     | References |     |     |     |
| ------------- | ------- | --- | --- | --- | ---------- | --- | --- | --- |
ParametricStatisticalModeling Section7.1 Guttormsson et al. [1999], Keogh et al. [1997, 2002,
2006]
| Non-parametricStatistical | Section7.2.2 |     | Desforgesetal.[1998] |     |     |     |     |     |
| ------------------------- | ------------ | --- | -------------------- | --- | --- | --- | --- | --- |
Modeling
NeuralNetworks Section4.1 Bishop[1994],CampbellandBennett[2001],Diazand
|     |     |     | Hollmen [2002], | Harris | [1993], | Jakubek | and | Strasser |
| --- | --- | --- | --------------- | ------ | ------- | ------- | --- | -------- |
[2002],Kingetal.[2002],Lietal.[2002],Petscheetal.
[1996],Streifeletal.[1996],WhiteheadandHoyt[1993]
| Spectral         | Section9   |     | Parraetal.[1996],Fujimakietal.[2005] |     |     |     |     |     |
| ---------------- | ---------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
| RuleBasedSystems | Section4.4 |     | Yairietal.[2001]                     |     |     |     |     |     |
TableIX. ExamplesofAnomalyDetectionTechniquesUsedforStructuralDamageDetection
| TechniqueUsed |     | Section |     |     | References |     |     |     |
| ------------- | --- | ------- | --- | --- | ---------- | --- | --- | --- |
StatisticalProfilingusingHistograms Section7.2.1 Manson[2002],Mansonetal.[2001,2000]
| ParametricStatisticalModeling |     | Section7.1 | RuotoloandSurace[1997] |     |     |     |     |     |
| ----------------------------- | --- | ---------- | ---------------------- | --- | --- | --- | --- | --- |
MixtureofModels Section7.1.3 Hickinbothametal.[2000a,2000b],Hollierand
Austin[2002]
NeuralNetworks Section4.1 Brothertonetal.[1998,2001],Nairacetal.[1999,
|     |     |     | 1997], | Surace | et al. | [1998, 1997], | Sohn | et al. |
| --- | --- | --- | ------ | ------ | ------ | ------------- | ---- | ------ |
[2001],Worden[1997]
data in this domain is usually referred to as sensor data because it is recorded using
different sensors and collected for analysis. Anomaly detection techniques have been
extensivelyappliedinthisdomaintodetectsuchdamage.Industrialdamagedetection
can be further classified into two domains, one that deals with defects in mechanical
components such as motors, engines, and so on, and the other that deals with de-
fects in physical structures. The former domain is also referred to as system health
management.
Theanomalydetectiontechniquesinthisdo-
3.4.1. FaultDetectioninMechanicalUnits.
main monitor the performance of industrial components such as motors, turbines, oil
flowinpipelinesorothermechanicalcomponents,anddetectdefectsthatmightoccur
duetowearandtearorotherunforseencircumstances.
Thedatainthisdomaintypicallyhasatemporalaspectandtime-seriesanalysisis
alsousedinsometechniques[Keoghetal.2002,2006;BasuandMeckesheimer2007].
Theanomaliesoccurmostlybecauseofanobservationinaspecificcontext(contextual
anomalies)orasananomaloussequenceofobservations(collectiveanomalies).
Typically,normaldatapertainingtocomponentswithoutdefectsisreadilyavailable
and hence semisupervised techniques are applicable. Anomalies are required to be
detectedinanonlinefashionaspreventivemeasuresarerequiredtobetakenassoon
asananomalyoccurs.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableVIII.
|                                     |     | Structural | defect | and damage |     | detection | techniques |     |
| ----------------------------------- | --- | ---------- | ------ | ---------- | --- | --------- | ---------- | --- |
| 3.4.2. Structural Defect Detection. |     |            |        |            |     |           |            |     |
detect structural anomalies in structures, for example, cracks in beams or strains in
airframes.
The data collected in this domain has a temporal aspect. The anomaly detection
techniquesaresimilartonoveltydetectionorchangepointdetectiontechniquessince
they try to detect change in the data collected from a structure. The normal data and
hence the models learned are typically static over time. The data might have spatial
correlations.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableIX.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

| AnomalyDetection:ASurvey |     |     |     |     | 15:17 |
| ------------------------ | --- | --- | --- | --- | ----- |
TableX. ExamplesofAnomalyDetectionTechniquesUsedinImageProcessingDomain
| TechniqueUsed | Section |     | References |     |     |
| ------------- | ------- | --- | ---------- | --- | --- |
MixtureofModels Section7.1.3 Byers and Raftery [1998], Spence et al. [2001],
Tarassenko[1995]
| Regression       | Section7.1.2 | Chenetal.[2005],TorrandMurray[1993] |     |     |     |
| ---------------- | ------------ | ----------------------------------- | --- | --- | --- |
| BayesianNetworks | Section4.2   | DiehlandHampshire[2002]             |     |     |     |
SupportVectorMachines Section4.3 DavyandGodsill[2002],Songetal.[2002]
NeuralNetworks Section4.1 AugusteijnandFolkert[2002],Cunetal.[1990],
|     |     | Hazel [2000], | Moya et | al. [1993], Singh | and |
| --- | --- | ------------- | ------- | ----------------- | --- |
Markou[2004]
| Clustering | Section6 | Scarthetal.[1995] |     |     |     |
| ---------- | -------- | ----------------- | --- | --- | --- |
NearestNeighbor-BasedTechniques Section5 Pokrajacetal.[2007],ByersandRaftery[1998]
TableXI. ExamplesofAnomalyDetectionTechniquesUsedforAnomalousTopicDetectioninTextData
| TechniqueUsed                       | Section      |                         | References |     |     |
| ----------------------------------- | ------------ | ----------------------- | ---------- | --- | --- |
| MixtureofModels                     | Section7.1.3 | Bakeretal.[1999]        |            |     |     |
| StatisticalProfilingusingHistograms | Section7.2.1 | FawcettandProvost[1999] |            |     |     |
| SupportVectorMachines               | Section4.3   | ManevitzandYousef[2002] |            |     |     |
| NeuralNetworks                      | Section4.1   | ManevitzandYousef[2000] |            |     |     |
ClusteringBased Section6 Allan et al. [1998], Srivastava and Zane-Ulman
[2005],Srivastava[2006]
3.5. ImageProcessing
Anomalydetectiontechniquesdealingwithimagesareeitherinterestedinanychanges
inanimageovertime(motiondetection)orinregionsthatappearabnormalonthestatic
image. This domain includes satellite imagery [Augusteijn and Folkert 2002; Byers
and Raftery 1998; Moya et al. 1993; Torr and Murray 1993; Theiler and Cai 2003],
digit recognition [Cun et al. 1990], spectroscopy [Chen et al. 2005; Davy and Godsill
2002; Hazel 2000; Scarth et al. 1995], mammographic image analysis [Spence et al.
2001;Tarassenko1995],andvideosurveillance[DiehlandHampshire2002;Singhand
Markou2004;Pokrajacetal.2007].Theanomaliesarecausedbymotion,orinsertion
ofaforeignobject,orinstrumentationerrors.Thedatahasspatialaswellastemporal
characteristics.Eachdatapointhasafewcontinuousattributessuchascolor,lightness,
texture, and so on. The interesting anomalies are either anomalous points or regions
intheimages(pointandcontextualanomalies).
Oneofthekeychallengesinthisdomainisthelargesizeoftheinput.Whendealing
withvideodata,onlineanomalydetectiontechniquesarerequired.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableX.
3.6. AnomalyDetectioninTextData
Anomaly detection techniques in this domain primarily detect novel topics or events
ornewsstoriesinacollectionofdocumentsornewsarticles.Theanomaliesarecaused
duetoanewinterestingeventorananomaloustopic.
Thedatainthisdomainistypicallyhighdimensionalandverysparse.Thedataalso
hasatemporalaspectsincethedocumentsarecollectedovertime.
A challenge for anomaly detection techniques in this domain is to handle the large
variationsindocumentsbelongingtoonecategoryortopic.
SomeanomalydetectiontechniquesusedinthisdomainarelistedinTableXI.
3.7. SensorNetworks
Sensornetworkshavelatelybecomeanimportanttopicofresearch;morefromthedata
analysisperspective,sincethesensordatacollectedfromvariouswirelesssensorshas
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:18 V.Chandolaetal.
TableXII. ExamplesofAnomalyDetectionTechniquesUsedforAnomalyDetectioninSensorNetworks
TechniqueUsed Section References
BayesianNetworks Section4.2 Janakirametal.[2006]
Rule-BasedSystems Section4.4 Branchetal.[2006]
ParametricStatisticalModeling Section7.1 Phuongetal.[2006],Duetal.[2006]
NearestNeighbor-BasedTechniques Section5 Subramaniametal.[2006],Zhangetal.[2007],
Ide´etal.[2007]
Spectral Section9 Chatzigiannakisetal.[2006]
severaluniquecharacteristics.Anomaliesindatacollectedfromasensornetworkcan
eithermeanthatoneormoresensorsarefaulty,ortheyaredetectingevents(suchas
intrusions)thatareinterestingforanalysts.Thusanomalydetectioninsensornetworks
cancapturesensorfaultdetectionorintrusiondetectionorboth.
A single sensor network might be comprised of sensors that collect different types
of data, such as binary, discrete, continuous, audio, video, and so forth. The data is
generated in a streaming mode. Often times the environment in which the various
sensorsaredeployed,andthecommunicationchannel,inducenoiseandmissingvalues
inthecollecteddata.
Anomalydetectioninsensornetworksposesasetofuniquechallenges.Theanomaly
detectiontechniquesarerequiredtooperateonline.Duetosevereresourceconstraints,
theanomalydetectiontechniquesneedtobelightweight.Anotherchallengeisthatdata
is collected in a distributed fashion, and hence a distributed data mining approach is
requiredtoanalyzeit[Chatzigiannakisetal.2006].Moreover,thepresenceofnoisein
the data collected from the sensor makes anomaly detection more challenging, since
it has to now distinguish between interesting anomalies and unwanted noise/missing
values.
TableXIIlistssomeanomalydetectiontechniquesusedinthisdomain.
3.8. OtherDomains
Anomalydetectionhasalsobeenappliedtoseveralotherdomainssuchasspeechrecog-
nition[Albrechtetal.2000;Emamianetal.2000],noveltydetectioninrobotbehavior
[CrookandHayes2001;Crooketal.2002;Marslandetal.1999,2000b,2000a],traffic
monitoring[Shekharetal.2001],click-throughprotection[Ihleretal.2006],detecting
faultsinWebapplications[IdeandKashima2004;Sunetal.2005],detectinganomalies
inbiologicaldata[Kadotaetal.2003;Sunetal.2006;Gwaderaetal.2005a;MacDonald
andGhosh2007;Tomlinsetal.2005;TibshiraniandHastie2007],detectinganomalies
in census data [Lu et al. 2003], detecting associations among criminal activities [Lin
and Brown 2003], detecting anomalies in Customer Relationship Management (CRM)
data [He et al. 2004b], detecting anomalies in astronomical data [Dutta et al. 2007;
Escalante2005;Protopapasetal.2006]anddetectingecosystemdisturbances[Blender
etal.1997;Kouetal.2006;SunandChawla2004].
4. CLASSIFICATIONBASEDANOMALYDETECTIONTECHNIQUES
Classification [Tan et al. 2005; Duda et al. 2000] is used to learn a model (classifier)
fromasetoflabeleddatainstances(training)andthen,classifyatestinstanceintoone
oftheclassesusingthelearnedmodel(testing).Classification-basedanomalydetection
techniquesoperateinasimilartwo-phasefashion.Thetrainingphaselearnsaclassifier
using the available labeled training data. The testing phase classifies a test instance
asnormaloranomalous,usingtheclassifier.
Classificationbasedanomalydetectiontechniquesoperateunderthefollowinggen-
eralassumption:
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:19
Fig.6. Usingclassificationforanomalydetection.
Assumption. Aclassifierthatcandistinguishbetweennormalandanomalousclasses
canbelearnedinthegivenfeaturespace.
Based on the labels available for the training phase, classification-based anomaly
detection techniques can be grouped into two broad categories: multi-class and one-
classanomalydetectiontechniques.
Multi-classclassificationbasedanomalydetectiontechniquesassumethatthetrain-
ingdatacontainslabeledinstancesbelongingtomultiplenormalclasses[Stefanoetal.
2000; Barbara et al. 2001b]. Such anomaly detection techniques teach a classifier to
distinguish between each normal class and the rest of the classes. See Figure 6(a) for
illustration. A test instance is considered anomalous if it is not classified as normal
by any of the classifiers. Some techniques in this subcategory associate a confidence
scorewiththepredictionmadebytheclassifier.Ifnoneoftheclassifiersareconfident
inclassifyingthetestinstanceasnormal,theinstanceisdeclaredtobeanomalous.
One-classclassificationbasedanomalydetectiontechniquesassumethatalltraining
instances have only one class label. Such techniques learn a discriminative boundary
around the normal instances using a one-class classification algorithm, for example,
one-class SVMs [Scho¨lkopf et al. 2001], one-class Kernel Fisher Discriminants [Roth
2004, 2006], as shown in Figure 6(b). Any test instance that does not fall within the
learnedboundaryisdeclaredasanomalous.
In the following subsections, we discuss a variety of anomaly detection techniques
thatusedifferentclassificationalgorithmstobuildclassifiers:
4.1. NeuralNetworks-Based
Neuralnetworkshavebeenappliedtoanomalydetectioninmulti-classaswellasone-
classsettings.
A basic multi-class anomaly detection technique using neural networks operates in
two steps. First, a neural network is trained on the normal training data to learn the
differentnormalclasses.Second,eachtestinstanceisprovidedasaninputtotheneural
network. If the network accepts the test input, it is normal and if the network rejects
a test input, it is an anomaly [Stefano et al. 2000; Odin and Addison 2000]. Several
variants of the basic neural network technique have been proposed that use different
typesofneuralnetworks,assummarizedinTableXIII.
ReplicatorNeuralNetworkshavebeenusedforone-classanomalydetection[Hawkins
et al. 2002; Williams et al. 2002]. A multi-layer feed forward neural network is con-
structedthathasthesamenumberofinputandoutputneurons(correspondingtothe
featuresinthedata).Thetraininginvolvescompressingdataintothreehiddenlayers.
The testing phase involves reconstructing each data instance, x , using the learned
i
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:20 V.Chandolaetal.
TableXIII. SomeExamplesofClassification-BasedAnomalyDetectionTechniquesUsingNeuralNetworks
NeuralNetworkUsed References
MultilayeredPerceptrons [AugusteijnandFolkert2002;Cunetal.1990;Sykacek1997;Ghosh
etal.1999a,1998;Barsonetal.1996;Heetal.1997;Nairacetal.1997;
HickinbothamandAustin2000b;Vasconcelosetal.1995,1994]
NeuralTrees [Martinez1998]
AutoassociativeNetworks [Aeyels 1991; Byungho and Sungzoon 1999; Japkowicz et al. 1995;
Hawkinsetal.2002;KoandJacyna2000;ManevitzandYousef2000;
Petscheetal.1996;Sohnetal.2001;Songetal.2001;Streifeletal.
1996;Thompsonetal.2002;Worden1997;Williamsetal.2002;Diaz
andHollmen2002]
AdaptiveResonanceTheoryBased [Moya et al. 1993; Dasgupta and Nino 2000; Caudell and Newman
1993]
RadialBasisFunction-Based [Albrechtetal.2000;Bishop1994;Brothertonetal.1998;Brotherton
andJohnson2001;Lietal.2002;Nairacetal.1999,1997;Ghoshand
Reilly1994;JakubekandStrasser2002]
HopfieldNetworks [Jagota1991;CrookandHayes2001;Crooketal.2002;Addisonetal.
1999;Murray2001]
OscillatoryNetworks HoandRouat1997,1998;KojimaandIto1999;Borisyuketal.2000;
MartinelliandPerfetti1994]
networktoobtainthereconstructedoutput,o .Thereconstructionerror,δ ,forthetest
i i
instance x isthencomputedas:
i
(cid:2)n
1
δ = (x −o )2,
i ij ij
n
j=1
where n is the number of features over which the data is defined. The reconstruction
errorδ isdirectlyusedasananomalyscoreforthetestinstance.
i
4.2. BayesianNetworks-Based
Bayesiannetworkshavebeenusedforanomalydetectioninthemulti-classsetting.A
basictechniqueforaunivariatecategoricaldatasetusingana¨ıveBayesiannetworkes-
timatestheposteriorprobabilityofobservingaclasslabelfromasetofnormalclassla-
belsandtheanomalyclasslabel,givenatestdatainstance.Theclasslabelwithlargest
posteriorischosenasthepredictedclassforthegiventestinstance.Thelikelihoodof
observing the test instance given a class and the prior on the class probabilities, is
estimatedfromthetrainingdataset.Thezeroprobabilities,especiallyfortheanomaly
class,aresmoothedusingLaplaceSmoothing.
The basic technique can be generalized to multivariate categorical data sets by ag-
gregatingtheper-attributeposteriorprobabilitiesforeachtestinstanceandusingthe
aggregatedvaluetoassignaclasslabeltothetestinstance.
Several variants of the basic technique have been proposed for network intrusion
detection[Barbaraetal.2001b;Sebyalaetal.2002;ValdesandSkinner2000;Mingming
2000; Bronstein et al. 2001], for novelty detection in video surveillance [Diehl and
Hampshire2002],foranomalydetectionintextdata[Bakeretal.1999],andfordisease
outbreakdetection[Wongetal.2002,2003].
This basic technique assumes independence between the different attributes. Sev-
eralvariationsofthebasictechniquehavebeenproposedthatcapturetheconditional
dependenciesbetweenthedifferentattributesusingmorecomplexBayesiannetworks
[SiaterlisandMaglaris2004;Janakirametal.2006;DasandSchneider2007].
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:21
4.3. SupportVectorMachines-Based
SupportVectorMachines(SVMs)[Vapnik1995]havebeenappliedtoanomalydetection
in the one-class setting. Such techniques use one class learning techniques for SVM
[Ratsch et al. 2002] and learn a region that contains the training data instances (a
boundary). Kernels, such as radial basis function (RBF) kernel, can be used to learn
complex regions. For each test instance, the basic technique determines if the test
instance falls within the learned region. If a test instance falls within the learned
region,itisdeclaredasnormal,elseitisdeclaredasanomalous.
Variants of the basic technique have been proposed for anomaly detection in audio
signaldata[DavyandGodsill2002],noveltydetectioninpowergenerationplants[King
et al. 2002] and system call intrusion detection [Eskin et al. 2002; Heller et al. 2003;
Lazarevicetal.2003].Thebasictechniquehasalsobeenextendedtodetectanomalies
intemporalsequences[MaandPerkins2003a,2003b].
A variant of the basic technique [Tax and Duin 1999a, 1999b; Tax 2001] finds the
smallesthypersphereinthekernelspacethatcontainsalltraininginstances,andthen
determinesonwhichsideofthathypersphereatestinstancelies.Ifatestinstancelies
outsidethehypersphere,itisdeclaredtobeanomalous.
Songetal.[2002]useRobustSupportVectorMachines(RSVM),whicharerobustto
thepresenceofanomaliesinthetrainingdata.RSVMhavebeenappliedtosystemcall
intrusiondetection[Huetal.2003].
4.4. Rule-Based
Rule-basedanomalydetectiontechniqueslearnrulesthatcapturethenormalbehavior
of a system. A test instance that is not covered by any such rule is considered as an
anomaly. Rule-based techniques have been applied in multi-class as well as one-class
settings.
Abasicmulti-classrule-basedtechniqueconsistsoftwosteps.Thefirststepistolearn
rulesfromthetrainingdatausingarulelearningalgorithm,suchasRIPPER,Decision
Trees, and so on. Each rule has an associated confidence value that is proportional to
ratio between the number of training instances correctly classified by the rule and
the total number of training instances covered by the rule. The second step is to find,
for each test instance, the rule that best captures the test instance. The inverse of
the confidence associated with the best rule is the anomaly score of the test instance.
Severalminorvariantsofthebasicrule-basedtechniquehavebeenproposed[Fanetal.
2001;Helmeretal.1998;Leeetal.1997;SalvadorandChan2003;Tengetal.1990].
Association rule mining [Agrawal and Srikant 1995] has been used for one-class
anomaly detection by generating rules from the data in an unsupervised fashion. As-
sociation rules are generated from a categorical data set. To ensure that the rules
correspondtostrongpatterns,asupportthresholdisusedtopruneoutruleswithlow
support [Tan et al. 2005]. Association rule mining-based techniques have been used
fornetworkintrusiondetection[MahoneyandChan2002,2003;Mahoneyetal.2003;
Tandon and Chan 2007; Barbara et al. 2001a; Otey et al. 2003, system call intrusion
detection[Leeetal.2000;LeeandStolfo1998;QinandHwang2004],creditcardfraud
detection [Brause et al. 1999], and fraud detection in spacecraft housekeeping data
[Yairietal.2001].Frequentitemsetsaregeneratedintheintermediatestepofassocia-
tionruleminingalgorithms.Heetal.[2004a]proposeananomalydetectionalgorithm
for categorical data sets in which the anomaly score of a test instance is equal to the
numberoffrequentitemsetsinwhichitoccurs.
Computational Complexity. The computational complexity of classification-based
techniques depends on the classification algorithm being used. For a discussion on
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:22 V.Chandolaetal.
the complexity of training classifiers, see Kearns [1990]. Generally, training decision
treestendstobefaster,whiletechniquesthatinvolvequadraticoptimization,suchas
SVMs, are more expensive; though linear time SVMs [Joachims 2006] have been pro-
posed that have linear training time. The testing phase of classification techniques is
usuallyveryfastsincethetestingphaseusesalearnedmodelforclassification.
AdvantagesandDisadvantagesofClassification-BasedTechniques.Theadvantages
ofclassification-basedtechniquesareasfollows:
(1) Classification-basedtechniques,especiallythemulti-classtechniques,canmakeuse
ofpowerfulalgorithmsthatcandistinguishbetweeninstancesbelongingtodifferent
classes.
(2) Thetestingphaseofclassification-basedtechniquesisfast,sinceeachtestinstance
needstobecomparedagainsttheprecomputedmodel.
Thedisadvantagesofclassification-basedtechniquesareasfollows:
(1) Multi-classclassification-basedtechniquesrelyontheavailabilityofaccuratelabels
forvariousnormalclasses,whichisoftennotpossible.
(2) Classification-basedtechniquesassignalabeltoeachtestinstance,whichcanalso
become a disadvantage when a meaningful anomaly score is desired for the test
instances.Someclassificationtechniquesthatobtainaprobabilisticpredictionscore
fromtheoutputofaclassifier,canbeusedtoaddressthisissue[Platt2000].
5. NEARESTNEIGHBOR-BASEDANOMALYDETECTIONTECHNIQUES
The concept of nearest neighbor analysis has been used in several anomaly detection
techniques.Suchtechniquesarebasedonthefollowingkeyassumption:
Assumption. Normaldatainstancesoccurindenseneighborhoods,whileanomalies
occurfarfromtheirclosestneighbors.
Nearest neighbor-based anomaly detection techniques require a distance or sim-
ilarity measure defined between two data instances. Distance (or similarity) be-
tween two data instances can be computed in different ways. For continuous
attributes, Euclidean distance is a popular choice, but other measures can be used
[Tanetal.2005,Chapter2].Forcategoricalattributes,asimplematchingcoefficientis
often used but more complex distance measures can also be used [Boriah et al. 2008;
Chandolaetal.2008].Formultivariatedatainstances,distanceorsimilarityisusually
computedforeachattributeandthencombined[Tanetal.2005,Chapter2].
Mostofthetechniquesthatwillbediscussedinthissection,aswellastheclustering-
basedtechniques(Section6)donotrequirethedistancemeasuretobestrictlymetric.
Themeasuresaretypicallyrequiredtobepositive-definiteandsymmetric,buttheyare
notrequiredtosatisfythetriangleinequality.
Nearest neighbor-based anomaly detection techniques can be broadly grouped into
twocategories:
(1) techniques that use the distance of a data instance to its kth nearest neighbor as
theanomalyscore;
(2) techniques that compute the relative density of each data instance to compute its
anomalyscore.
Additionally there are some techniques that use the distance between data instances
inadifferentmannertodetectanomalies,andwillbebrieflydiscussedlater.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:23
5.1. UsingDistancetokthNearestNeighbor
A basic nearest neighbor anomaly detection technique is based on the following defi-
nition:Theanomalyscoreofadatainstanceisdefinedasitsdistancetoitskth nearest
neighbor in a given data set. This basic technique has been applied to detect land
mines from satellite ground images [Byers and Raftery 1998] and to detect shorted
turns (anomalies) in the DC field windings of large synchronous turbine-generators
[Guttormssonetal.1999].Inthelatterpapertheauthorsusek =1.Usually,athresh-
oldisthenbeappliedontheanomalyscoretodetermineifatestinstanceisanomalous
ornot.Ramaswamyetal.[2000],ontheotherhand,selectninstanceswiththelargest
anomalyscoresastheanomalies.
The basic technique has been extended by researchers in three different ways. The
firstsetofvariantsmodifiesthedefinitiontoobtaintheanomalyscoreofadatainstance.
Thesecondsetofvariantsusesdifferentdistance/similaritymeasurestohandlediffer-
entdatatypes.Thethirdsetofvariantsfocusesonimprovingtheefficiencyofthebasic
technique(thecomplexityofthebasictechniqueisO(N2),where N isthedatasize)in
differentways.
Eskinetal.[2002],AngiulliandPizzuti[2002]andZhangandWang[2006]compute
the anomaly score of a data instance as the sum of its distances from its k nearest
neighbors.Asimilartechnique,calledPeerGroupAnalysishasbeenappliedtodetect
creditcardfraudsbyBoltonandHand[1999].
A different way to compute the anomaly score of a data instance is to count the
number of nearest neighbors (n) that are not more than d distance apart from the
given data instance [Knorr and Ng 1997, 1998, 1999; Knorr et al. 2000]. This method
can also be viewed as estimating the global density for each data instance, since it
involvescountingthenumberofneighborsinahypersphereofradiusd.Forexample,
ina2-Ddataset,thedensityofadatainstance= n .Theinverseofthedensityisthe
πd2
anomaly score for the data instance. Instead of computing the actual density, several
techniques fix the radius d and use 1 as the anomaly score, while several techniques
n
fixnanduse 1 astheanomalyscore.
d
Whilemosttechniquesdiscussedsofarinthiscategoryhavebeenproposedtohandle
continuousattributes,severalvariantshavebeenproposedtohandleotherdatatypes.
A hypergraph-based technique, called HOT, is proposed by Wei et al. [2003] in which
the authors model the categorical values using a hypergraph, and measure distance
between two data instances by analyzing the connectivity of the graph. A distance
measure for data containing a mix of categorical and continuous attributes has been
proposedforanomalydetection[Oteyetal.2006].Theauthorsdefinelinksbetweentwo
instancesbyaddingdistanceforcategoricalandcontinuousattributesseparately.For
categorical attributes, the number of attributes for which the two instances have the
same values defines the distance between them. For continuous attributes, a covari-
ancematrixismaintainedtocapturethedependenciesbetweenthecontinuousvalues.
Palshikar[2005]adaptsthetechniqueproposedinKnorrandNg[1999]tocontinuous
sequences.Kouetal.[2006]extendthetechniqueproposedinRamaswamyetal.[2000]
tospatialdata.
Severalvariantsofthebasictechniquehavebeenproposedtoimprovetheefficiency.
Some techniques prune the search space by either ignoring instances that cannot be
anomalous or by focussing on instances that are most likely to be anomalous. Bay
andSchwabacher[2003]showthatforsufficientlyrandomizeddata,asimplepruning
stepcouldresultintheaveragecomplexityofthenearestneighborsearchtobenearly
linear. After calculating the nearest neighbors for a data instance, the algorithm sets
theanomalythresholdforanydatainstancetothescoreoftheweakestanomalyfound
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:24 V.Chandolaetal.
so far. Using this pruning procedure, the technique discards instances that are close,
andhencenotinteresting.
Ramaswamy et al. [2000] propose a partition-based technique, which first clusters
theinstancesandcomputeslowerandupperboundsonthedistanceofaninstancefrom
itskthnearestneighborforinstancesineachpartition.Thisinformationisthenusedto
identifythepartitionsthatcannotpossiblycontainthetopkanomalies;suchpartitions
arepruned.Anomaliesarethencomputedfromtheremaininginstances(belongingto
unprunedpartitions)inafinalphase.Similarcluster-basedpruninghasbeenproposed
byEskinetal.[2002],McCallumetal.[2000],Ghotingetal.[2006],andTaoetal.[2006].
Wu and Jermaine [2006] use sampling to improve the efficiency of the nearest
neighbor-basedtechnique.Theauthorscomputethenearestneighborofeveryinstance
within a smaller sample from the data set. Thus the complexity of the proposed tech-
niqueisreducedtoO(MN),where M isthesamplesizechosen.
To prune the search space for nearest neighbors, several techniques partition the
attribute space into a hypergrid consisting of hypercubes of fixed sizes. The intuition
behindsuchtechniquesisthatifahypercubecontainsmanyinstances,suchinstances
arelikelytobenormal.Moreover,ifforagiveninstance,thehypercubethatcontainsthe
instance,anditsadjoininghypercubes,containveryfewinstances,thegiveninstance
is likely to be anomalous. Techniques based on this intuition have been proposed by
Knorr and Ng [1998]. Angiulli and Pizzuti [2002] extend by linearizing the search
spacethroughtheHilbertspacefillingcurve.Thed-dimensionaldatasetisfittedina
hypercube D = [0,1]d.Thishypercubeisthenmappedtotheinterval I = [0,1]using
the Hilbert Space Filling Curve and the k-nearest neighbors of a data instance are
obtainedbyexaminingitssuccessorsandpredecessorsin I.
5.2. UsingRelativeDensity
Density-basedanomalydetectiontechniquesestimatethedensityoftheneighborhood
of each data instance. An instance that lies in a neighborhood with low density is
declaredtobeanomalouswhileaninstancethatliesinadenseneighborhoodisdeclared
tobenormal.
Foragivendatainstance,thedistancetoitskthnearestneighborisequivalenttothe
radius of a hypersphere, centered at the given data instance, which contains k other
instances.Thusthedistancetothekth nearestneighborforagivendatainstancecan
be viewed as an estimate of the inverse of the density of the instance in the data set
and the basic nearest neighbor-based technique described in the previous subsection
canbeconsideredasadensity-basedanomalydetectiontechnique.
Density-basedtechniquesperformpoorlyifthedatahasregionsofvaryingdensities.
Forexample,considerthetwo-dimensionaldatasetshowninFigure7.Duetothelow
density of the cluster C , it is apparent that for every instance q inside the cluster
1
C , the distance between the instance q and its nearest neighbor is greater than the
1
distancebetweentheinstance p andthenearestneighborfromtheclusterC ,andthe
2 2
instance p will not be considered as anomaly. Hence, the basic technique will fail to
2
distinguishbetween p andinstancesinC .However,theinstance p maybedetected.
2 1 1
Tohandletheissueofvaryingdensitiesinthedataset,asetoftechniqueshasbeen
proposedtocomputethedensityofinstancesrelativetothedensityoftheirneighbors.
Breunigetal.[1999,2000]assignananomalyscoretoagivendatainstance,known
as Local Outlier Factor (LOF). For any given data instance, the LOF score is equal to
ratio of average local density of the k nearest neighbors of the instance and the local
density of the data instance itself. To find the local density for a data instance, the
authorsfirstfindtheradiusofthesmallesthyper-spherecenteredatthedatainstance,
thatcontainsitsk nearestneighbors.Thelocaldensityisthencomputedbydividingk
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:25
Fig.7. Advantageoflocaldensity-basedtechniquesoverglobaldensity-basedtechniques.
Fig.8. DifferencebetweentheneighborhoodscomputedbyLOFandCOF.
by the volume of this hyper-sphere. For a normal instance lying in a dense region, its
local density will be similar to that of its neighbors, while for an anomalous instance,
itslocaldensitywillbelowerthanthatofitsnearestneighbors.Hencetheanomalous
instancewillgetahigherLOFscore.
In the example shown in Figure 7, LOF will be able to capture both anomalies, p
1
and p ,duetothefactthatitconsidersthedensityaroundthedatainstances.
2
Several researchers have proposed variants of the LOF technique. Some of these
variants estimate the local density of an instance in a different way. Some variants
have adapted the original technique to more complex data types. Since the original
LOF technique is O(N2) (N is the data size), several techniques have been proposed
thatimprovetheefficiencyofLOF.
Tangetal.[2002]discussavariationoftheLOF,whichtheycallConnectivity-based
OutlierFactor(COF).ThedifferencebetweenLOFandCOFisthemannerinwhichthe
k neighborhoodforaninstanceiscomputed.InCOF,theneighborhoodforaninstance
iscomputedinanincrementalmode.Tostart,theclosestinstancetothegiveninstance
is added to the neighborhood set. The next instance added to the neighborhood set is
suchthatitsdistancetotheexistingneighborhoodsetisminimumamongallremaining
data instances. The distance between an instance and a set of instances is defined as
the minimum distance between the given instance and any instance belonging to the
given set. The neighborhood is grown in this manner until it reaches size k. Once the
neighborhoodiscomputed,theanomalyscore(COF)iscomputedinthesamemanner
asLOF.COFisabletocaptureregionssuchasstraightlines,asshowninFigure8.
AsimplerversionofLOFwasproposedbyHautamakietal.[2004],whichcalculates
a quantity called Outlier Detection using In-degree Number (ODIN) for each data in-
stance.Foragivendatainstance,ODINisequaltothenumberofk nearestneighbors
ofthedatainstancewhichhavethegivendatainstanceintheirknearestneighborlist.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:26 V.Chandolaetal.
The inverse of ODIN is the anomaly score for the data instance. A similar technique
wasproposedbyBritoetal.[1997].
Papadimitriou et al. [2002] propose a measure called Multi-Granularity Deviation
Factor(MDEF),whichisavariationofLOF.MDEFforagivendatainstanceisequalto
thestandarddeviationofthelocaldensitiesofthenearestneighborsofthegivendata
instance (including the data instance itself). The inverse of the standard deviation is
theanomalyscoreforthedatainstance.Theanomalydetectiontechniquepresentedin
thepaperiscalledLOCI,whichnotonlyfindsanomalousinstancesbutalsoanomalous
micro-clusters.
Several variants of LOF have been proposed to handle different data types. A vari-
antofLOFisappliedbySunandChawla[2004,2006]fordetectingspatialanomalies
in climate data. Yu et al. [2006] use a similarity measure instead of distance to han-
dle categorical attributes. A similar technique has been proposed to detect sequential
anomaliesinproteinsequencesbySunetal.[2006].ThistechniqueusesProbabilistic
Suffix Trees (PST) to find the nearest neighbors for a given sequence. Pokrajac et al.
[2007] extend LOF to work in an incremental fashion to detect anomalies in video
sensordata.
Some variants of the LOF technique have been proposed to improve its efficiency.
Jinetal.[2001]proposeavariantinwhichonlythetopnanomaliesarefoundinstead
of finding LOF score for every data instance. The technique includes finding micro-
clusters in the data and then finding upper and lower bounds on LOF for each of the
micro-clusters.ChiuandCheeFu[2003]proposedthreevariantsofLOF,whichenhance
its performance by making certain assumptions about the problem to prune all those
clusters that definitely do not contain instances that will figure in the top n anomaly
list. For the remaining clusters a detailed analysis is done to find the LOF score for
eachinstanceintheseclusters.
Computational Complexity. A drawback of the basic nearest neighbor-based tech-
nique and of the LOF technique, is the O(N2) complexity required. Since these tech-
niques involve finding nearest neighbors for each instance, efficient data structures
such as k-d trees [Bentley 1975] and R-trees [Roussopoulos et al. 1995] can be used.
But such techniques do not scale well as the number of attributes increases. Several
techniqueshavedirectlyoptimizedtheanomalydetectiontechniqueundertheassump-
tion that only the top few anomalies are interesting. If an anomaly score is required
for every test instance, such techniques are not applicable. Techniques that partition
theattributespaceintoahypergrid,arelinearindatasizebutareexponentialinthe
number of attributes, and hence are not well suited for large number of attributes.
Sampling techniques try to address the O(N2) complexity issue by determining the
nearestneighborswithinasmallsampleofthedataset.Butsamplingmightresultin
incorrectanomalyscoresifthesizeofthesampleisverysmall.
Advantages and Disadvantages of Nearest Neighbor-Based Techniques. The advan-
tagesofnearestneighbor-basedtechniquesareasfollows:
(1) Akeyadvantageofnearestneighbor-basedtechniquesisthattheyareunsupervised
innatureanddonotmakeanyassumptionsregardingthegenerativedistribution
forthedata.Instead,theyarepurelydatadriven.
(2) Semisupervisedtechniquesperformbetterthanunsupervisedtechniquesinterms
of missed anomalies, since the likelihood that an anomaly will form a close neigh-
borhoodinthetrainingdatasetisverylow.
(3) Adapting nearest neighbor-based techniques to a different data type is straight-
forward, and primarily requires defining an appropriate distance measure for the
givendata.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:27
Thedisadvantagesofnearestneighbor-basedtechniquesareasfollows:
(1) For unsupervised techniques, if the data has normal instances that do not have
enoughcloseneighbors,orifthedatahasanomaliesthathaveenoughcloseneigh-
bors,thetechniquefailstolabelthemcorrectly;resultinginmissedanomalies.
(2) Forsemisupervisedtechniques,ifthenormalinstancesinthetestdatadonothave
enough similar normal instances in the training data, the false positive rate for
suchtechniquesishigh.
(3) The computational complexity of the testing phase is also a significant challenge
since it involves computing the distance of each test instance—with all instances
belonging to either the test data itself, or to the training data—to compute the
nearestneighbors.
(4) Performance of a nearest neighbor-based technique greatly relies on a distance
measure, defined between a pair of data instances, which can effectively distin-
guish between normal and anomalous instances. Defining distance measures be-
tweeninstancescanbechallengingwhenthedataiscomplex,forexample,graphs,
sequences,andsoon.
6. CLUSTERING-BASEDANOMALYDETECTIONTECHNIQUES
Clustering[JainandDubes1988;Tanetal.2005]isusedtogroupsimilardatainstances
intoclusters.Clusteringisprimarilyanunsupervisedtechniquethoughsemisupervised
clustering [Basu et al. 2004] has also been explored lately. Even though clustering
and anomaly detection appear to be fundamentally different from each other, several
clustering-basedanomalydetectiontechniqueshavebeendeveloped.Clustering-based
anomalydetectiontechniquescanbegroupedintothreecategories.
Thefirstcategoryofclustering-basedtechniquesreliesonthefollowingassumption:
Assumption. Normaldatainstancesbelongtoaclusterinthedata,whileanomalies
donotbelongtoanycluster.
Techniques based on this assumption apply a known clustering-based algorithm to
the data set and declare any data instance that does not belong to any cluster as
anomalous.Severalclusteringalgorithmsthatdonotforceeverydatainstancetobelong
to a cluster, such as DBSCAN [Ester et al. 1996], ROCK[Guha et al. 2000], and SNN
clustering [Erto¨z et al. 2003] can be used. The FindOut algorithm [Yu et al. 2002] is
an extension of the WaveCluster algorithm [Sheikholeslami et al. 1998] in which the
detectedclustersareremovedfromthedataandtheresidualinstancesaredeclaredas
anomalies.
Adisadvantageofsuchtechniquesisthattheyarenotoptimizedtofindanomalies,
sincethemainaimoftheunderlyingclusteringalgorithmistofindclusters.
The second category of clustering-based techniques relies on the following
assumption:
Assumption. Normal data instances lie close to their closest cluster centroid, while
anomaliesarefarawayfromtheirclosestclustercentroid.
Techniquesbasedonthisassumptionconsistoftwosteps.Inthefirststep,thedata
isclusteredusingaclusteringalgorithm.Inthesecondstep,foreachdatainstance,its
distancetoitsclosestclustercentroidiscalculatedasitsanomalyscore.
A number of anomaly detection techniques that follow this two step approach have
been proposed using different clustering algorithms. Smith et al. [2002] studied Self-
OrganizingMaps(SOM),K-meansClustering,andExpectationMaximization(EM)to
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:28 V.Chandolaetal.
clustertrainingdataandthenusetheclusterstoclassifytestdata.Inparticular,SOM
[Kohonen 1997] has been widely used to detect anomalies in a semisupervised mode
in several applications such as intrusion detection [Labib and Vemuri 2002; Smith
et al. 2002; Ramadas et al. 2003], fault detection [Harris 1993; Ypma and Duin 1998;
Emamianetal.2000],andfrauddetection[Brockettetal.1998].Barbaraetal.[2003]
proposeatechniquethatisrobusttoanomaliesinthetrainingdata.Theauthorsfirst
separatenormalinstancesfromanomaliesinthetrainingdata,usingfrequentitem-set
mining,andthenusetheclustering-basedtechniquetodetectanomalies.Severaltech-
niqueshavealsobeenproposedtohandlesequencedata[Blenderetal.1997;Bejerano
andYona2001;VinuezaandGrudic2004;Budalakotietal.2006].
Techniquesbasedonthesecondassumptioncanalsooperateinsemisupervisedmode,
in which the training data is clustered and instances belonging to the test data are
compared against the clusters to obtain an anomaly score for the test data instance
[Marchette1999;WuandZhang2003;VinuezaandGrudic2004;Allanetal.1998].If
thetrainingdatahasinstancesbelongingtomultipleclasses,semisupervisedclustering
can be applied to improve the clusters. He et al. [2002] incorporate the knowledge of
labelstoimproveontheirunsupervisedclustering-basedanomalydetectiontechnique
[Heetal.2003]bycalculatingameasurecalledsemanticanomalyfactor,whichishigh
iftheclasslabelofanobjectinaclusterisdifferentfromthemajorityoftheclasslabels
inthatcluster.
Notethatiftheanomaliesinthedataformclustersbythemselves,thesetechniques
will not be able to detect such anomalies. To address this issue, a third category of
clustering-basedtechniqueshasbeenproposed,whichreliesonthefollowingassump-
tion:
Assumption. Normaldatainstancesbelongtolargeanddenseclusters,whileanoma-
lieseitherbelongtosmallorsparseclusters.
Techniquesbasedonthisassumptiondeclareinstancesbelongingtoclusterswhose
sizeand/ordensityisbelowathreshold,asanomalous.
Several variations of the third category of techniques have been proposed [Pires
and Santos-Pereira 2005; Otey et al. 2003; Eskin et al. 2002; Mahoney et al. 2003;
Jiang et al. 2001; He et al. 2003]. The technique proposed by He et al. [2003], called
FindCBLOF, assigns an anomaly score known as Cluster-Based Local Outlier Factor
(CBLOF) for each data instance. The CBLOF score captures the size of the cluster to
whichthedatainstancebelongs,aswellasthedistanceofthedatainstancetoitscluster
centroid.
Several clustering-based techniques have been proposed to improve the efficiency
of these existing techniques. Fixed width clustering is a linear time (O(Nd)) approx-
imation algorithm used by various anomaly detection techniques [Eskin et al. 2002;
Portnoy et al. 2001; Mahoney et al. 2003; He et al. 2003]. An instance is assigned to
a cluster whose center is within a pre-specified distance to the given instance. If no
suchclusterexiststhenanewclusterwiththeinstanceasthecenteriscreated.Then
theydeterminewhichclustersareanomaliesbasedontheirdensityanddistancefrom
other clusters. The width can either be a user-specified parameter [Eskin et al. 2002;
Portnoyetal.2001]orcanbederivedfromthedata[Mahoneyetal.2003].Chaudhary
et al. [2002] propose an anomaly detection technique using k-d trees that provide a
partitioningofthedatainlineartime.Theyapplytheirtechniquetodetectanomalies
inastronomicaldatasetswherecomputationalefficiencyisanimportantrequirement.
Another technique that addresses this issue is proposed by Sun et al. [2004]. The au-
thors propose an indexing technique called CD-trees to efficiently partition data into
clusters.Thedatainstancesthatbelongtosparseclustersaredeclaredasanomalies.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:29
6.1. DistinctionbetweenClustering-BasedandNearestNeighbor-BasedTechniques
Several clustering-based techniques require distance computation between a pair of
instances.Thus,inthatrespect,theyaresimilartonearestneighbor-basedtechniques.
The choice of the distance measure is critical to the performance of the technique;
hence the discussion in the previous section regarding the distance measures holds
for clustering-based techniques also. The key difference between the two techniques,
however,isthatclustering-basedtechniquesevaluateeachinstancewithrespecttothe
cluster it belongs to, while nearest neighbor-based techniques analyze each instance
withrespecttoitslocalneighborhood.
Computational Complexity. The computational complexity of training a clustering-
based anomaly detection technique depends on the clustering algorithm used to gen-
erate clusters from the data. Thus such techniques can have quadratic complexity if
the clustering technique requires computation of pairwise distances for all data in-
stances, or linear when using heuristic-based techniques such as k-means [Hartigan
and Wong 1979] or approximate clustering techniques [Eskin et al. 2002]. The test
phaseofclustering-basedtechniquesisfast,sinceitinvolvescomparingatestinstance
withasmallnumberofclusters.
Advantages and Disadvantages of Clustering-Based Techniques. The advantages of
clusteringbasedtechniquesareasfollows:
(1) Clustering-basedtechniquescanoperateinanunsupervisedmode.
(2) Suchtechniquescanoftenbeadaptedtoothercomplexdatatypesbysimplyplug-
ginginaclusteringalgorithmthatcanhandletheparticulardatatype.
(3) Thetestingphaseforclustering-basedtechniquesisfastsincethenumberofclusters
againstwhicheverytestinstanceneedstobecomparedisasmallconstant.
Thedisadvantagesofclustering-basedtechniquesareasfollows:
(1) Performanceofclustering-basedtechniquesishighlydependentontheeffectiveness
ofclusteringalgorithmsincapturingtheclusterstructureofnormalinstances.
(2) Manytechniquesdetectanomaliesasabyproductofclustering,andhencearenot
optimizedforanomalydetection.
(3) Several clustering algorithms force every instance to be assigned to some cluster.
This might result in anomalies getting assigned to a large cluster, thereby being
considered as normal instances by techniques that operate under the assumption
thatanomaliesdonotbelongtoanycluster.
(4) Several clustering-based techniques are effective only when the anomalies do not
formsignificantclustersamongthemselves.
(5) Thecomputationalcomplexityforclusteringthedataisoftenabottleneck,especially
ifO(N2d)clusteringalgorithmsareused.
7. STATISTICALANOMALYDETECTIONTECHNIQUES
Theunderlyingprincipleofanystatisticalanomalydetectiontechniqueis:“Ananomaly
is an observation which is suspected of being partially or wholly irrelevant because
it is not generated by the stochastic model assumed” [Anscombe and Guttman 1960].
Statisticalanomalydetectiontechniquesarebasedonthefollowingkeyassumption:
Assumption. Normaldatainstancesoccurinhighprobabilityregionsofastochastic
model,whileanomaliesoccurinthelowprobabilityregionsofthestochasticmodel.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:30 V.Chandolaetal.
Statisticaltechniquesfitastatisticalmodel(usuallyfornormalbehavior)tothegiven
dataandthenapplyastatisticalinferencetesttodetermineifanunseeninstancebe-
longs to this model or not. Instances that have a low probability of being generated
fromthelearnedmodel,basedontheappliedteststatistic,aredeclaredasanomalies.
Both parametric as well as nonparametric techniques have been applied to fit a sta-
tistical model. While parametric techniques assume the knowledge of the underlying
distributionandestimatetheparametersfromthegivendata[Eskin2000],nonpara-
metric techniques do not generally assume knowledge of the underlying distribution
[Desforges et al. 1998]. In the next two subsections we will discuss parametric and
nonparametricanomalydetectiontechniques.
7.1. ParametricTechniques
As mentioned before, parametric techniques assume that the normal data is gener-
atedbyaparametricdistributionwithparameters(cid:4)andprobabilitydensityfunction
f(x,(cid:4)), where x is an observation. The anomaly score of a test instance (or observa-
tion)xistheinverseoftheprobabilitydensityfunction, f(x,(cid:4)).Theparameters(cid:4)are
estimatedfromthegivendata.
Alternatively, a statistical hypothesis test (also referred to as discordancy test in
statisticaloutlierdetectionliterature[BarnettandLewis1994])maybeused.Thenull
hypothesis (H ) for such tests is that the data instance x has been generated using
0
the estimated distribution (with parameters (cid:4)). If the statistical test rejects H , x is
0
declaredtobeanomaly.Astatisticalhypothesistestisassociatedwithateststatistic,
whichcanbeusedtoobtainaprobabilisticanomalyscoreforthedatainstancex.
Based on the type of distribution assumed, parametric techniques can be further
categorizedasfollows:
7.1.1. GaussianModel-Based. Suchtechniquesassumethatthedataisgeneratedfrom
a Gaussian distribution. The parameters are estimated using Maximum Likelihood
Estimates(MLE).Thedistanceofadatainstancetotheestimatedmeanistheanomaly
score for that instance. A threshold is applied to the anomaly scores to determine the
anomalies.Differenttechniquesinthiscategorycalculatethedistancetothemeanand
thethresholdindifferentways.
A simple outlier detection technique, often used in process quality control domain
[Shewhart1931],istodeclarealldatainstancesthataremorethan3σ distanceaway
from the distribution mean μ, where σ is the standard deviation for the distribution.
Theμ±3σ regioncontains99.7%ofthedatainstances.
More sophisticated statistical tests have also been used to detect anomalies, as dis-
cussedinBarnettandLewis[1994],Barnett[1976],andBeckmanandCook[1983].We
willdescribeafewtestshere.
Theboxplotrule(Figure9)isthesimpleststatisticaltechniquethathasbeenapplied
to detect univariate and multivariate anomalies in medical domain data [Laurikkala
et al. 2000; Horn et al. 2001; Solberg and Lahti 2005] and turbine rotors data [Gut-
tormssonetal.1999].Aboxplotgraphicallydepictsthedatausingsummaryattributes
such as smallest non-anomaly observation (min), lower quartile (Q ), median, upper
1
quartile (Q ), and largest non-anomaly observation (max). The quantity Q − Q is
3 3 1
called the Inter Quartile Range (IQR). The box plots also indicates the limits beyond
which any observation will be treated as an anomaly. A data instance that lies more
than 1.5∗IQR lower than Q or 1.5∗IQR higher than Q is declared as an anomaly.
1 3
Theregionbetween Q −1.5IQRand Q +1.5IQRcontains99.3%ofobservations,and
1 3
hencethechoiceofthe1.5IQRboundarymakestheboxplotruleequivalenttothe3σ
techniqueforGaussiandata.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:31
Fig.9. Aboxplotforaunivariatedataset.
Grubb’s test (also known as the maximum normed residual test) is used to detect
anomalies in a univariate data set [Grubbs 1969; Stefansky 1972; Anscombe and
Guttman1960]undertheassumptionthatthedataisgeneratedbyaGaussiandistri-
bution.Foreachtestinstancex,itsz scoreiscomputedasfollows:
|x−x¯|
z= , (1)
s
wherex¯ andsarethemeanandstandarddeviationofthedatasample,respectively.A
testinstanceisdeclaredtobeanomalousif:
(cid:3)
(cid:4)
z> N √ −1 (cid:4) (cid:5) t α 2 /(2N),N−2 , (2)
N N −2+t2
α/(2N),N−2
where N is the data size and tα/(2N),N−2 is a threshold used to declare an instance to
be anomalous or normal. This threshold is the value taken by a t-distribution at a
α
significance level of . The significance level reflects the confidence associated with
2N
thethresholdandindirectlycontrolsthenumberofinstancesdeclaredasanomalous.
AvariantoftheGrubb’stestformultivariatedatawasproposedbyLaurikkalaetal.
[2000], which uses the Mahalanobis distance of a test instance x to the sample mean
x¯,toreducemultivariateobservationstounivariatescalars:
y2 =(x−x¯) (cid:6) S −1(x−x¯), (3)
where S is the sample covariance matrix. The univariate Grubb’s test is applied to y
to determine if the instance x is anomalous or not. Several other variants of Grubb’s
testhavebeenproposedtohandlemultivariatedatasets[AggarwalandYu2001,2008;
Laurikkalaetal.2000],graphstructureddata[Shekharetal.2001],andOnlineAna-
lyticalProcessing(OLAP)datacubes[Sarawagietal.1998].
Thestudent’st-testhasalsobeenappliedforanomalydetectioninSuraceandWorden
[1998]andSuraceetal.[1997]todetectdamagesinstructuralbeams.Anormalsam-
ple,N iscomparedwithatestsample,N usingthet-test.Ifthetestshowssignificant
1 2
differencebetweenthem,itsignifiesthepresenceofananomalyin N .Themultivari-
2
ate version of students’ t-test called the Hotelling t2-test is also used as an anomaly
detection test statistic in Liu and Weng [1991] to detect anomalies in bioavailability/
bioequivalencestudies.
Ye and Chen [2001] use a χ2 statistic to determine anomalies in operating system
calldata.Thetrainingphaseassumesthatthenormaldatahasamultivariatenormal
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:32 V.Chandolaetal.
distribution.Thevalueoftheχ2 statisticisdeterminedas:
(cid:2)n (X −E )2
χ2 = i i , (4)
E
i=1 i
where X is the observed value of the i variable, E is the expected value of the i
i th i th
variable (obtained from the training data), and n is the number of variables. A large
valueof X2 denotesthattheobservedsamplecontainsanomalies.
Several other statistical anomaly detection techniques that assume that the data
follows a Gaussian distribution have been proposed, but use other statistical tests,
suchas:Rosnertest[Rosner1983],Dixontest[Gibbons1994],SlippageDetectiontest
[Hawkins1980],andsoon.
7.1.2. Regression Model-Based. Anomaly detection using regression has been exten-
sively investigated for time-series data [Abraham and Chuang 1989; Abraham and
Box1979;Fox1972].
Thebasicregressionmodel-basedanomalydetectiontechniqueconsistsoftwosteps.
Inthefirststep,aregressionmodelisfittedonthedata.Inthesecondstep,foreachtest
instance,theresidualforthetestinstanceisusedtodeterminetheanomalyscore.The
residualisthepartoftheinstancewhichisnotexplainedbytheregressionmodel.The
magnitudeoftheresidualcanbeusedastheanomalyscoreforthetestinstance,though
statistical tests have been proposed to determine anomalies with certain confidence
[Anscombe and Guttman 1960; Beckman and Cook 1983; Hawkins 1980; Torr and
Murray 1993]. Certain techniques detect the presence of anomalies in a data set by
analyzingtheAkaikeInformationContent(AIC)duringmodelfitting[Kitagawa1979;
Kadotaetal.2003].
Presence of anomalies in the training data can influence the regression parame-
ters and hence the regression model might not produce accurate results. A popular
technique to handle such anomalies while fitting regression models is called robust
regression[RousseeuwandLeroy1987]:estimationofregressionparameterswhileac-
commodatinganomalies.Theauthorsarguethattherobustregressiontechniquesnot
onlyhidetheanomalies,butcanalsodetecttheanomalies,becausetheanomaliestend
to have larger residuals from the robust fit. A similar robust anomaly detection ap-
proachhasbeenappliedinAutoregressiveIntegratedMovingAverage(ARIMA)models
[Biancoetal.2001;Chenetal.2005].
Variantsofthebasicregressionmodels-basedtechniquehavebeenproposedtohan-
dlemultivariatetime-seriesdata.Tsayetal.[2000]discusstheadditionalcomplexity
in multivariate time-series over the univariate time-series and come up with statis-
tics that can be applied to detect anomalies in multivariate ARIMA models. This is a
generalizationofstatisticsproposedearlierbyFox[1972].
Another variant that detects anomalies in multivariate time-series data generated
by an Autoregressive Moving Average (ARMA) model, was proposed by Galeano et al.
[2004]. In this technique the authors transform the multivariate time-series to a uni-
variate time-series by linearly combining the components of the multivariate time-
series.Theinterestinglinearcombinations(projectionsin1-dspace)areobtainedusing
aprojectionpursuittechnique[Huber1985]thatmaximizestheKurtosiscoefficient(a
measureforthedegreeofpeakedness/flatnessinthevariabledistribution)ofthetime-
seriesdata.Theanomalydetectionineachprojectionisdonebyusingunivariatetest
statistics,asproposedbyFox[1972].
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:33
7.1.3. MixtureofParametricDistributions-Based. Suchtechniquesuseamixtureofpara-
metric statistical distributions to model the data. Techniques in this category can be
groupedintotwosubcategories.Thefirstsubcategoryoftechniquesmodelthenormal
instances and anomalies as separate parametric distributions, while the second sub-
category of techniques model only the normal instances as a mixture of parametric
distributions.
Forthefirstsubcategoryoftechniques,thetestingphaseinvolvesdeterminingwhich
distribution—normal or anomalous—the test instance belongs to. Abraham and Box
[1979]assumethatthenormaldataisgeneratedfromaGaussiandistribution(N(0,σ2))
and the anomalies are also generated from a Gaussian distribution with same mean
butwithlargervariance,N(0,k2σ2).AtestinstanceistestedusingtheGrubb’steston
bothdistributions,andaccordinglylabeledasnormaloranomalous.Similartechniques
havebeenproposedinLauer[2001],Eskin[2000],AbrahamandBox[1979],Boxand
Tiao[1968],andAgarwal[2005].Eskin[2000]usestheExpectationMaximization(EM)
algorithmtodevelopamixtureofmodelsforthetwoclasses,assumingthateachdata
point is an anomaly with apriori probability λ, and normal with apriori probability
1−λ.Thus,ifDrepresentstheactualprobabilitydistributionoftheentiredata,andM
andArepresentthedistributionsofthenormalandanomalousdatarespectively,then
D=λA+(1−λ)M.Mislearnedusinganydistributionestimationtechnique,whileA
is assumed to be uniform. Initially all points are considered to be in M. The anomaly
score is assigned to a point based on how much the distributions change if that point
isremovedfromMandaddedtoA.
The second subcategory of techniques model the normal instances as a mixture of
parametric distributions. A test instance that does not belong to any of the learned
modelsisdeclaredtobeananomaly.Gaussianmixturemodelshavebeenmostlyused
for such techniques Agarwal [2006], and have been used to detect strains in airframe
data[HickinbothamandAustin2000a;HollierandAustin2002],todetectanomaliesin
mammographicimageanalysis[Spenceetal.2001;Tarassenko1995],andfornetwork
intrusiondetection[YamanishiandichiTakeuchi2001;Yamanishietal.2004].Similar
techniqueshavebeenappliedtodetectinganomaliesinbiomedicalsignaldata[Roberts
andTarassenko1994;Roberts1999,2002],whereextremevaluestatistics2 areusedto
determine if a test point is an anomaly with respect to the learned mixture of models
or not. Byers and Raftery [1998] use a mixture of Poisson distributions to model the
normaldataandthendetectanomalies.
7.2. NonparametricTechniques
Theanomalydetectiontechniquesinthiscategoryusenonparametricstatisticalmod-
els, such that the model structure is not defined a prioiri, but is instead determined
fromgivendata.Suchtechniquestypicallymakefewerassumptionsregardingthedata,
suchassmoothnessofdensity,whencomparedtoparametrictechniques.
7.2.1. Histogram-Based. The simplest nonparametric statistical technique is to use
histogramstomaintainaprofileofthenormaldata.Suchtechniquesarealsoreferred
toasfrequency-basedorcounting-based.Histogrambasedtechniquesareparticularly
2Extreme Value Theory (EVT) [Pickands 1975] is a similar concept as anomaly detection, and deals with
extremedeviationsofaprobabilitydistribution.EVThasbeenappliedtoriskmanagement[McNeil1999]
as a method for modeling and measuring extreme risks. The key difference between extreme values and
statisticalanomaliesisthatextremevaluesareknowntooccurattheextremitiesofaprobabilitydistribution,
whileanomaliesaremoregeneral.Anomaliescanalsobegeneratedfromadifferentdistributionaltogether.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:34 V.Chandolaetal.
popularintheintrusiondetectioncommunity[Eskin2000;Eskinetal.2001;Denning
1987]andfrauddetection[FawcettandProvost1999],sincethebehaviorofthedatais
governedbycertainprofiles(userorsoftwareorsystem)thatcanbeefficientlycaptured
usingthehistogrammodel.
Abasichistogram-basedanomalydetectiontechniqueforunivariatedataconsistsof
two steps. The first step involves building a histogram based on the different values
takenbythatfeatureinthetrainingdata.Inthesecondstep,thetechniquechecksif
atestinstancefallsinanyoneofthebinsofthehistogram.Ifitdoes,thetestinstance
isnormal,otherwiseitisanomalous.Avariantofthebasichistogram-basedtechnique
is to assign an anomaly score to each test instance based on the height (frequency) of
thebininwhichitfalls.
Thesizeofthebinusedwhenbuildingthehistogramiskeyforanomalydetection.If
thebinsaresmall,manynormaltestinstanceswillfallinemptyorrarebins,resulting
in a high false alarm rate. If the bins are large, many anomalous test instances will
fall in frequent bins, resulting in a high false negative rate. Thus a key challenge for
histogram-basedtechniquesistodetermineanoptimalsizeofthebinstoconstructthe
histogramthatmaintainsalowfalsealarmrateandalowfalsenegativerate.
Histogram-basedtechniquesrequirenormaldatatobuildthehistograms[Anderson
etal.1994;JavitzandValdes1991;HelmanandBhangoo1997].Sometechniqueseven
constructhistogramsfortheanomalies[DasguptaandNino2000],iflabeledanomalous
instancesareavailable.
For multivariate data, a basic technique is to construct attribute-wise histograms.
Duringtesting,foreachtestinstance,theanomalyscoreforeachattributevalueofthe
test instance is calculated as the height of the bin that contains the attribute value.
Theper-attributeanomalyscoresareaggregatedtoobtainanoverallanomalyscorefor
thetestinstance.
Thebasichistogram-basedtechniqueformultivariatedatahasbeenappliedtosys-
temcallintrusiondetectionEndler[1998],networkintrusiondetection[Hoetal.1999;
Yamanishi and ichi Takeuchi 2001; Yamanishi et al. 2004], fraud detection [Fawcett
andProvost1999],damagedetectioninstructures[Manson2002;Mansonetal.2001,
2000], detecting Web-based attacks [Kruegel and Vigna 2003; Kruegel et al. 2002],
andanomaloustopicdetectionintextdata[Allanetal.1998].Avariantofthesimple
techniqueisusedinPacketHeaderAnomalyDetection(PHAD)andApplicationLayer
Anomaly Detection (ALAD) [Mahoney and Chan 2002], applied to network intrusion
detection.
TheSRIInternational’sreal-timeNetworkIntrusionDetectionSystem(NIDES)[An-
dersonetal.1994;Andersonetal.1995;PorrasandNeumann1997]hasasubsystem
that maintains long-term statistical profiles to capture the normal behavior of a com-
putersystem[JavitzandValdes1991].TheauthorsproposeaQstatistictocomparea
long-termprofilewithashorttermprofile(observation).Thestatisticisusedtodeter-
mineanothermeasurecalledSstatistic,whichreflectstheextenttowhichthebehavior
inaparticularfeatureisanomalouswithrespecttothehistoricalprofile.Thefeature-
wiseSstatisticsarecombinedtogetasinglevaluecalledISstatistic,whichdetermines
ifatestinstanceisanomalousornot.AvarianthasbeenproposedbySargor[1998]for
anomalydetectioninlink-stateroutingprotocols.
7.2.2. KernelFunction-Based. Anon-parametrictechniqueforprobabilitydensityesti-
mation is parzen windows estimation [Parzen 1962]. This involves using kernel func-
tions to approximate the actual density. Anomaly detection techniques based on ker-
nel functions are similar to the parametric methods described earlier. The only dif-
ference is the density estimation technique used. Desforges et al. [1998] proposed a
semi-supervisedstatisticaltechniquetodetectanomalies,whichuseskernelfunctions
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:35
toestimatetheprobabilitydistributionfunction(pdf)forthenormalinstances.Anew
instance,whichliesinthelowprobabilityareaofthispdfisdeclaredtobeanomalous.
Similar application of parzen windows is proposed for network intrusion detection
[Chow and Yeung 2002], for novelty detection in oil flow data [Bishop 1994], and for
mammographicimageanalysis[Tarassenko1995].
ComputationalComplexity.Thecomputationalcomplexityofstatisticalanomalyde-
tectiontechniquesdependsonthenatureofthestatisticalmodelthatisrequiredtobe
fittedonthedata.Fittingsingleparametricdistributionsfromtheexponentialfamily,
forexample,Gaussian,Poisson,Multinomial,andsoon,istypicallylinearindatasize
aswellasnumberofattributes.Fittingcomplexdistributions(suchasmixturemodels,
HMM, etc.) using iterative estimation techniques such as Expectation Maximization
(EM), are also typically linear per iteration, though they might be slow in converging
depending on the problem and/or convergence criterion. Kernel-based techniques can
potentiallyhavequadratictimecomplexityintermsofthedatasize.
Advantages and Disadvantages of Statistical Techniques. The advantages of statis-
ticaltechniquesare:
(1) Iftheassumptionsregardingtheunderlyingdatadistributionholdtrue,statistical
techniquesprovideastatisticallyjustifiablesolutionforanomalydetection.
(2) Theanomalyscoreprovidedbyastatisticaltechniqueisassociatedwithaconfidence
interval, which can be used as additional information while making a decision re-
gardinganytestinstance.
(3) If the distribution estimation step is robust to anomalies in data, statistical tech-
niquescanoperateinaunsupervisedsettingwithoutanyneedforlabeledtraining
data.
Thedisadvantagesofstatisticaltechniquesare:
(1) Thekeydisadvantageofstatisticaltechniquesisthattheyrelyontheassumption
that the data is generated from a particular distribution. This assumption often
doesnotholdtrue,especiallyforhighdimensionalrealdatasets.
(2) Even when the statistical assumption can be reasonably justified, there are sev-
eralhypothesisteststatisticsthatcanbeappliedtodetectanomalies;choosingthe
best statistic is often not a straightforward task [Motulsky 1995]. In particular,
constructinghypothesistestsforcomplexdistributionsthatarerequiredtofithigh
dimensionaldatasetsisnontrivial.
(3) Histogram-based techniques are relatively simple to implement, but a key short-
comingofsuchtechniquesformultivariatedataisthattheyarenotabletocapture
the interactions between different attributes. An anomaly might have attribute
values that are individually very frequent, but whose combination is very rare,
however an attribute-wise histogram-based technique would not be able to detect
suchanomalies.
8. INFORMATIONTHEORETICANOMALYDETECTIONTECHNIQUES
Information theoretic techniques analyze the information content of a data set using
different information theoretic measures such as Kolomogorov Complexity, entropy,
relativeentropy,andsoon.Suchtechniquesarebasedonthefollowingkeyassumption:
Assumption. Anomalies in data induce irregularities in the information content of
thedataset.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:36 V.Chandolaetal.
LetC(D)denotethecomplexityofagivendataset, D.Abasicinformationtheoretic
technique can be described as follows. Given a data set D, find the minimal subset of
instances, I, such that C(D)−C(D− I) is maximum. All instances in the subset thus
obtained,aredeemedasanomalous.Theproblemaddressedbythisbasictechniqueis
to find a Pareto-optimal solution, which does not have a single optimum, since there
aretwodifferentobjectivesthatneedtobeoptimized.
Inthistechnique,thecomplexityofadataset(C)canbemeasuredindifferentways.
Kolomogorov complexity [Li and Vitanyi 1993] has been used by several techniques
[Arningetal.1996;Keoghetal.2004].Arningetal.[1996]usethesizeoftheregular
expression to measure the Kolomogorov Complexity of data (represented as a string)
for anomaly detection. Keogh et al. [2004] use the size of the compressed data file
(usinganystandardcompressionalgorithm),asameasureofthedataset’sKolomogorov
Complexity.Otherinformationtheoreticmeasuressuchasentropy,relativeuncertainty,
andsoon,havealsobeenusedtomeasurethecomplexityofacategoricaldataset[Lee
andXiang2001;Heetal.2005,2006;Ando2007].
This basic technique involves dual optimization to minimize the subset size while
maximizing the reduction in the complexity of the data set. Thus an exhaustive ap-
proachinwhicheverypossiblesubsetofthedatasetisconsideredwouldruninexpo-
nentialtime.Severaltechniqueshavebeenproposedthatperformapproximatesearch
for the most anomalous subset. He et al. [2006] use an approximate algorithm called
LocalSearchAlgorithm(LSA)[Heetal.2005]toapproximatelydeterminesuchasub-
set in a linear fashion, using entropy as the complexity measure. A similar technique
thatusesaninformationbottleneckmeasurewasproposedbyAndo[2007].
Information theoretic techniques have also been used in data sets in which data
instancesarenaturallyordered,forexample,sequentialdataandspatialdata.Insuch
cases, the data is broken into substructures (segments for sequences, subgraphs for
graphs,etc.),andtheanomalydetectiontechniquefindsthesubstructure, I,suchthat
C(D)−C(D−I)ismaximum.Thistechniquehasbeenappliedtosequences[Linetal.
2005;Chakrabartietal.1998;Arningetal.1996],graphdata[NobleandCook2003],
and spatial data [Lin and Brown 2003]. A key challenge of such techniques is to find
theoptimalsizeofthesubstructurethatwouldresultindetectinganomalies.
Computational Complexity. As mentioned earlier, the basic information theoretic
anomaly detection technique has exponential time complexity, though approximate
techniqueshavebeenproposedthathavelineartimecomplexity.
AdvantagesandDisadvantagesofInformationTheoreticTechniques.Theadvantages
ofinformationtheoretictechniquesareasfollows:
(1) Theycanoperateinanunsupervisedsetting.
(2) Theydonotmakeanyassumptionsabouttheunderlyingstatisticaldistributionfor
thedata.
Thedisadvantagesofinformationtheoretictechniquesareasfollows:
(1) Theperformanceofsuchtechniquesishighlydependentonthechoiceoftheinforma-
tiontheoreticmeasure.Often,suchmeasurescandetectthepresenceofanomalies
onlywhenthereisasignificantlylargenumberofanomaliespresentinthedata.
(2) Informationtheoretictechniquesappliedtosequences,andspatialdatasetsrelyon
thesizeofthesubstructure,whichisoftennontrivialtoobtain.
(3) Itisdifficulttoassociateananomalyscorewithatestinstanceusinganinformation
theoretictechnique.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:37
9. SPECTRALANOMALYDETECTIONTECHNIQUES
Spectral techniques try to find an approximation of the data using a combination of
attributes that capture the bulk of the variability in the data. Such techniques are
basedonthefollowingkeyassumption:
Assumption. Data can be embedded into a lower dimensional subspace in which
normalinstancesandanomaliesappearsignificantlydifferent.
Thus the general approach adopted by spectral anomaly detection techniques is to
determine such subspaces (embeddings, projections, etc.) in which the anomalous in-
stances can be easily identified [Agovic et al. 2007]. Such techniques can work in an
unsupervisedaswellasasemisupervisedsetting.
Several techniques use Principal Component Analysis (PCA) [Jolliffe 2002] for pro-
jecting data into a lower dimensional space. One such technique [Parra et al. 1996]
analyzestheprojectionofeachdatainstancealongtheprincipalcomponentswithlow
variance.Anormalinstancethatsatisfiesthecorrelationstructureofthedatawillhave
a low value for such projections while an anomalous instance that deviates from the
correlationstructurewillhavealargevalue.Duttaetal.[2007]adoptthisapproachto
detectanomaliesinastronomycatalogs.
Ide and Kashima [2004] propose a spectral technique to detect anomalies in a time
seriesofgraphs.Eachgraphisrepresentedasanadjacencymatrixforagiventime.At
everytimeinstance,theprinciplecomponentofthematrixischosenastheactivityvec-
torforthegivengraph.Thetime-seriesoftheactivityvectorsisconsideredasamatrix
and the principal left singular vector is obtained to capture the normal dependencies
over time in the data. For a new test graph, the angle between its activity vector and
the principal left singular vector obtained from the previous graphs is computed and
usedtodeterminetheanomalyscoreofthetestgraph.Inasimilarapproach,Sunetal.
[2007] propose an anomaly detection technique on a sequence of graphs by perform-
ingCompactMatrixDecomposition(CMD)ontheadjacencymatrixforeachgraphand
thusobtaininganapproximationoftheoriginalmatrix.Foreachgraphinthesequence,
theauthorsperformCMDandcomputetheapproximationerrorbetweentheoriginal
adjacency matrix and the approximate matrix. The authors construct a time-series of
the approximation errors and detect anomalies in the time-series of errors; the graph
correspondingtoanomalousapproximationerrorisdeclaredtobeanomalous.
Shyuetal.[2003]presentananomalydetectiontechniquewheretheauthorsperform
robust PCA [Huber 1974] to estimate the principal components from the covariance
matrix of the normal training data. The testing phase involves comparing each point
with the components and assigning an anomaly score based on the point’s distance
fromtheprincipalcomponents.Thusiftheprojectionofx ontheprincipalcomponents
is y , y ,..., y andthecorrespondingeigen-valuesareλ ,λ ,...,λ ,then
1 2 p 1 2 p
(cid:2)q y2 y2 y2 y2
i = 1 + 2 +...+ q ,q ≤ p (5)
λ λ λ λ
i=1 i 1 2 q
has a chi-square distribution [Hawkins 1974]. Using this result, the authors propose
that,foragivensignificancelevelα,observation x isananomalyif
(cid:2)q
y2
i >χ2(α). (6)
λ q
i=1 i
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:38 V.Chandolaetal.
ItcanbeshownthatthequantitycalculatedinEquation5isequaltotheMahalanobis
distance of the instance x from the sample mean (See Equation 3) when q = p[Shyu
etal.2003].ThustherobustPCA-basedtechniqueisthesameasastatisticaltechnique
discussedinSection7.1.1inasmallersubspace.
TherobustPCA-basedtechniquehasbeenappliedtothenetworkintrusiondetection
domain[Shyuetal.2003;Lakhinaetal.2005;ThottanandJi2003]andfordetecting
anomaliesinspacecraftcomponents[Fujimakietal.2005].
Computational Complexity. Standard PCA based techniques are typically linear in
data size but often quadratic in the number of dimensions. Nonlinear techniques can
improvethetimecomplexitytobelinearinthenumberofdimensionsbutpolynomial
in the number of principal components [Gunter et al. 2007]. Techniques that perform
SVDonthedataaretypicallyquadraticindatasize.
Advantages and Disadvantages of Spectral Techniques. The advantages of spectral
anomalydetectiontechniquesareasfollows:
(1) Spectraltechniquesautomaticallyperformdimensionalityreductionandhenceare
suitable for handling high dimensional data sets. Moreover, they can also be used
as a preprocessing step followed by application of any existing anomaly detection
techniqueinthetransformedspace.
(2) Spectraltechniquescanbeusedinanunsupervisedsetting.
Thedisadvantagesofspectralanomalydetectiontechniquesareasfollows:
(1) Spectral techniques are useful only if the normal and anomalous instances are
separableinthelowerdimensionalembeddingofthedata.
(2) Spectraltechniquestypicallyhavehighcomputationalcomplexity.
10. HANDLINGCONTEXTUALANOMALIES
Theanomalydetectiontechniquesdiscussedintheprevioussectionsprimarilyfocuson
detectingpointanomalies.Inthissection,wewilldiscussanomalydetectiontechniques
thathandlecontextualanomalies.
AsdiscussedinSection2.2.2,contextualanomaliesrequirethatthedatahasasetof
contextual attributes (to define a context), and a set of behavioral attributes (to detect
anomalieswithinacontext).Songetal.[2007]usethetermsenvironmentalandindi-
cator attributes, which are analogous to our terminology. Some of the ways in which
contextualattributescanbedefinedare:
(1) Spatial.Thedatahasspatialattributes,whichdefinethelocationofadatainstance
and hence a spatial neighborhood. A number of context-based anomaly detection
techniques [Lu et al. 2003; Shekhar et al. 2001; Kou et al. 2006; Sun and Chawla
2004]havebeenproposedfordatawithspatialdata.
(2) Graphs:Theedgesthatconnectnodes(datainstances)definetheneighborhoodfor
each node. Contextual anomaly detection techniques have been applied to graph-
baseddatabySunetal.[2005].
(3) Sequential: The data is sequential: the contextual attribute of a data instance is
itspositioninthesequence.Time-seriesdatahasbeenextensivelyexploredinthe
contextualanomalydetectioncategory[AbrahamandChuang1989;Abrahamand
Box 1979; Rousseeuw and Leroy 1987; Bianco et al. 2001; Fox 1972; Salvador and
Chan2003;Tsayetal.2000;Galeanoetal.2004;Zeevietal.1997].
Anotherformofsequentialdataforwhichanomalydetectiontechniqueshavebeen
developed is event data, in which each event has a timestamp (such as operating
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:39
systemcalldataorWebdata[Ilgunetal.1995;VilaltaandMa2002;WeissandHirsh
1998; Smyth 1994]). The difference between time series data and event sequences
isthatforthelatter,theinter-arrivaltimebetweenconsecutiveeventsisuneven.
(4) Profile:Oftentimesthedatamightnothaveanexplicitspatialorsequentialstruc-
ture, but can still be segmented or clustered into components using a set of con-
textual attributes. These attributes are typically used to profile and group users
in activity monitoring systems, such as cell-phone fraud detection [Fawcett and
Provost 1999; Teng et al. 1990], CRM databases [He et al. 2004b] and credit-card
frauddetection[BoltonandHand1999].Theusersarethenanalyzedwithintheir
groupforanomalies.
In comparison to the rich literature on point anomaly detection techniques, the re-
search on contextual anomaly detection has been limited. Broadly, such techniques
can be classified in two categories. The first category of techniques reduces a contex-
tualanomalydetectionproblemtoapointanomalydetectionproblemwhilethesecond
category of techniques model the structure in the data and use the model to detect
anomalies.
10.1. ReductiontoPointAnomalyDetectionProblem
Since contextual anomalies are individual data instances (like point anomalies), but
areanomalousonlywithrespecttoacontext,oneapproachistoapplyaknownpoint
anomalydetectiontechniquewithinacontext.
A generic reduction-based technique consists of two steps. First, identify a context
for each test instance using the contextual attributes. Second, compute an anomaly
score for the test instance within the context using a known point anomaly detection
technique.
Anexampleofthegenericreduction-basedtechniquehasbeenproposedforthesce-
nario where identifying the context is not straightforward [Song et al. 2007]. The au-
thorsassumethattheattributesarealreadypartitionedintocontextualandbehavioral
attributes.Thuseachdatainstanced canberepresentedas[x, y].Thecontextualdata
ispartitionedusingamixtureofGaussianmodels,sayU.Thebehavioraldataisalso
partitioned using another mixture of Gaussian models, say V. A mapping function,
p(V |U )isalsolearned.Thismappingindicatestheprobabilityoftheindicatorpartof
j i
adatapoint y tobegeneratedfromamixturecomponentV ,whentheenvironmental
j
part x isgeneratedbyU .Thusforagiventestinstanced =[x, y],theanomalyscore
i
isgivenby:
(cid:2)nU (cid:2)nV
AnomalyScore= p(x ∈U ) p(y ∈ V )p(V |U ),
i j j i
i=1 j=1
wheren isthenumberofmixturecomponentsinU and N isthenumberofmixture
U V
componentsinV. p(x ∈U )indicatestheprobabilityofasamplepointxtobegenerated
i
fromthemixturecomponentU while p(y ∈U )indicatestheprobabilityofasample
i j
point y tobegeneratedfromthemixturecomponent V .
j
Another example of the generic technique is applied to cell phone fraud detection
[FawcettandProvost1999].Thedatainthiscaseconsistsofcellphoneusagerecords.
Oneoftheattributesinthedataisthecellphoneuser,whichisusedasthecontextual
attribute. The activity of each user is then monitored to detect anomalies using other
attributes. A similar technique is adopted for computer security [Teng et al. 1990],
wherethecontextualattributesare:userid,timeoftheday.Theremainingattributes
are compared with existing rules representing normal behavior to detect anomalies.
Peergroupanalysis[BoltonandHand1999]isanothersimilartechniquewhereusers
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:40 V.Chandolaetal.
aregroupedtogetheraspeersandanalyzedwithinagroupforfraud.Heetal.[2004b]
proposetheconceptofclassanomalydetection,whichisessentiallysegmentingthedata
usingtheclasslabels,andthenapplyingaknownclustering-basedanomalydetection
technique[Heetal.2002]todetectanomalieswithinthissubset.
Forspatialdata,neighborhoodsareintuitiveandstraightforwardtodetect[Ngand
Han1994]byusingthelocationcoordinates.Graph-basedanomalydetection[Shekhar
etal.2001;Luetal.2003;Kouetal.2006]useGrubb’sscore[Grubbs1969]orsimilar
statistical point anomaly detection techniques to detect anomalies within a spatial
neighborhood. Sun and Chawla [2004] use a distance-based measure called SLOM
(Spatial Local Outlier Measure [Sun and Chawla 2006]) to detect spatial anomalies
withinaneighborhood.
Another example of the generic technique applied to time-series data is proposed
by Basu and Meckesheimer [2007]. For a given instance in a time-series the authors
comparetheobservedvaluetothemedianoftheneighborhoodvalues.Atransformation
techniquefortime-seriesdatahasbeenproposedbyusingphasespaces[MaandPerkins
2003b].Thistechniqueconvertsatime-seriesintoasetofvectorsbyunfoldingthetime-
seriesintoaphasespaceusingatimedelayembeddingprocess.Thetemporalrelations
atanytimeinstanceareembeddedinthephasevectorforthatinstance.Theauthors
usethistechniquetotransformatime-seriesintofeaturespaceandthenuseone-class
SVMstodetectanomalies.Eachanomalycanbetranslatedtoavalueatcertaintime
instanceintheoriginaltime-series.
10.2. UtilizingtheStructureinData
In several scenarios, breaking up data into contexts is not straightforward. This is
typicallytruefortime-seriesdataandeventsequencedata.Insuchcases,time-series
modelingandsequencemodelingtechniquesareextendedtodetectcontextualanoma-
liesinthedata.
Agenerictechniqueinthiscategorycanbedescribedasfollows.Amodelislearned
fromthetrainingdata,whichcanpredicttheexpectedbehaviorwithrespecttoagiven
context.Iftheexpectedbehaviorissignificantlydifferentfromtheobservedbehavior,an
anomalyisdeclared.Asimpleexampleofthisgenerictechniqueisregressioninwhich
the contextual attributes can be used to predict the behavioral attribute by fitting a
regressionlineonthedata.
For time series data, several regression based techniques for time-series modeling
such as robust regression [Rousseeuw and Leroy 1987], auto-regressive models [Fox
1972], ARMA models [Abraham and Chuang 1989; Abraham and Box 1979; Galeano
etal.2004;Zeevietal.1997],andARIMAmodels[Biancoetal.2001;Tsayetal.2000],
have been developed for contextual anomaly detection. Regression-based techniques
havebeenextendedtodetectcontextualanomaliesinasetofcoevolvingsequencesby
modelingtheregressionaswellascorrelationbetweenthesequences[Yietal.2000].
One of the earliest works in time-series anomaly detection was proposed by Fox
[1972], where a time-series was modeled as a stationary autoregressive process. Any
observation is tested to be anomalous by comparing it with the covariance matrix of
the autoregressive process. If the observation falls outside the modeled error for the
process,itisdeclaredtobeananomaly.Anextensiontothistechniqueismadebyusing
Support Vector Regression to estimate the regression parameters and then using the
learnedmodeltodetectnoveltiesinthedata[MaandPerkins2003a].
A technique to detect a single anomaly (discord) in a sequence of alphabets was
proposedbyKeoghetal.[2004].Thetechniqueadoptsadivideandconquerapproach.
ThesequenceisdividedintotwopartsandtheKolmogorovComplexityiscalculatedfor
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:41
each.Theonewithhighercomplexitycontainstheanomaly.Thesequenceisrecursively
divided until they are left with a single event which is declared to be the anomaly in
thesequence.
WeissandHirsh[1998]proposeatechniquetodetectrareeventsinsequentialdata,
wheretheyuseeventsoccurringbeforeaparticulartimetopredicttheeventoccurring
at that time instance. If the prediction does not match the actual event, it is declared
toberare.Thisideaisextendedinotherareas,wheretheauthorshaveusedFrequent
ItemsetMining[VilaltaandMa2002],FiniteStateAutomaton(FSA)[Ilgunetal.1995;
Salvador and Chan 2003] and Markov Models [Smyth 1994] to determine conditional
probabilities for events based on the history of events. Marceau [2000] uses FSA to
predict the next event of a sequence based on the previous n events. They apply this
techniquetothedomainofsystemcallintrusiondetection.HollmenandTresp[1999]
employ HMM for cell phone fraud detection. The authors use a hierarchical regime
switchingcallmodeltomodelthecellphoneactivityofauser.Themodelpredictsthe
probability of a fraud taking place for a call using the learned model. The parameter
estimationisdoneusingtheEMalgorithm.
A model to detect intrusions in telephone networks was proposed by Scott [2001]
andformodelingWebclickdatabyIhleretal.[2006].Botharticlesfollowatechnique
in which they assume that the normal behavior in a time-series is generated by a
nonstationary Poisson process while the anomalies are generated by a homogenous
Poisson process. The transition between normal and anomalous behavior is modeled
usingaMarkovprocess.TheproposedtechniquesinallofthesearticlesusetheMarkov
ChainMonteCarlo(MCMC)estimationtechniquetoestimatetheparametersforthese
processes.Fortesting,atimeseriesismodeledusingthisprocessandthetimeinstances
forwhichtheanomalousbehaviorwasactiveareconsideredasanomalies.
BipartitegraphstructureinP2Pnetworkshasbeenusedtofirstidentifyaneighbor-
hood for any node in the graph [Sun et al. 2005], and then detecting the relevance of
thatnodewithintheneighborhood.Anodewithalowrelevancescoreistreatedasan
anomaly.Theauthorsalsoproposeanapproximatetechniquewherethegraphisfirst
partitioned into nonoverlapping subgraphs using graph partitioning algorithms such
as METIS [Karypis and Kumar 1998]. The neighborhood of a node is then computed
withinitspartition.
Computational Complexity. The computational complexity of the training phase in
reduction-based contextual anomaly detection techniques depends on the reduction
techniqueaswellasthepointanomalydetectiontechniqueusedwithineachcontext.
Whilesegmenting/partitioningtechniqueshaveafastreductionstep,techniquesthat
useclustering,oramixtureofmodelsestimation,arerelativelyslower.Sincethereduc-
tionsimplifiestheanomalydetectionproblem,fastpointanomalydetectiontechniques
canbeusedtospeedupthesecondstep.Thetestingphaseisrelativelyexpensivesince
foreachtestinstance,itscontextisdetermined,andthenananomalylabelorscoreis
assignedusingapointanomalydetectiontechnique.
Thecomputationalcomplexityofthetrainingphaseincontextualanomalydetection
techniquesthatutilizethestructureinthedatatobuildmodels,istypicallyhigherthan
that of techniques that reduce the problem to point anomaly detection. An advantage
for such techniques is the testing phase is relatively fast, since each instance is just
comparedtothesinglemodelandassignedananomalyscoreorananomalylabel.
Advantages and Disadvantages of Contextual Anomaly Detection Techniques. The
keyadvantageofcontextualanomalydetectiontechniquesisthattheyallowanatural
definitionofananomalyinmanyreal-lifeapplicationswheredatainstancestendtobe
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:42 V.Chandolaetal.
Fig.10. 2-Ddatasets.Normalinstancesareshownascirclesandanomaliesareshownassquares.
similarwithinacontext.Suchtechniquesareabletodetectanomaliesthatmightnot
bedetectedbypointanomalydetectiontechniquesthattakeaglobalviewofthedata.
Thedisadvantageofcontextualanomalydetectiontechniquesisthattheyareappli-
cableonlywhenacontextcanbedefined.
11. RELATIVESTRENGTHSANDWEAKNESSESOFANOMALYDETECTIONTECHNIQUES
Each of the large number of anomaly detection techniques discussed in the previous
sections have their unique strengths and weaknesses. It is important to know which
anomalydetectiontechniqueisbestsuitedforagivenproblem.Giventhecomplexityof
theproblemspace,itisnotfeasibletoprovidesuchanunderstandingforeveryanomaly
detection problem. In this section we analyze the relative strengths and weakenesses
ofdifferentcategoriesoftechniquesforafewsimpleproblemsettings.
For example, let us consider the following anomaly detection problem. The input is
2-D continuous data (Figure 10(a)). The normal data instances are generated from a
Gaussiandistributionandarelocatedinatightclusterinthe2-Dspace.Theanomalies
are a very few instances generated from another Gaussian distribution whose mean
isveryfarfromthefirstdistribution.Arepresentativetrainingdatasetthatcontains
instances from the normal data set is also available. Thus the assumptions made by
techniques in Sections 4–9 hold for this data set, and hence any anomaly detection
techniquesbelongingtothesecategorieswilldetecttheanomaliesinsuchascenario.
Nowletusconsideranother2-Ddataset(Figure10(b)).Letthenormalinstancesbe
suchthattheyaregeneratedbyalargenumberofdifferentGaussiandistributionswith
meansarrangedonacircleandverylowvariance.Thusthenormaldatawillbeaset
oftightclustersarrangedonacircle.Aone-classclassification-basedtechniquemight
learnacircularboundaryaroundtheentiredatasetandhencewillnotbeabletodetect
theanomaliesthatliewithinthecircleofclusters.Ontheotherhandifeachclusterwas
labeledasadifferentclass,amulti-classclassification-basedtechniquemightbeableto
learnboundariesaroundeachcluster,andhencebeabletodetecttheanomaliesinthe
center.A statisticaltechnique thatuses amixture model approachto modelthe data,
maybeabletodetecttheanomalies.Similarly,clustering-basedandnearestneighbor
basedtechniqueswillbeabletodetecttheanomaliessincetheyarefarfromallother
instances.Inasimilarexample(Figure10(c)),iftheanomalousinstancesformatight
clusterofsignificantsizeatthecenterofthecircle,bothclustering-basedandnearest
neighbor-based techniques will treat these instances as normal, thus exhibiting poor
performance.
For more complex data sets, different types of techniques face different challenges.
Nearest neighbor and clustering-based techniques suffer when the number of dimen-
sions is high, because the distance measures in a high number of dimensions are not
able to differentiate between normal and anomalous instances. Spectral techniques
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:43
explicitly address the high dimensionality problem by mapping data to a lower di-
mensional projection. But their performance is highly dependent on the assumption
that the normal instances and anomalies are distinguishable in the projected space.
Classification-basedtechniquescanbeabetterchoiceinsuchscenario.Buttobemost
effective, classification-based techniques require labels for both normal and anoma-
lous instances, which are not often available. Even if the labels for both normal and
anomalousinstancesareavailable,theimbalanceinthedistributionofthetwolabels
often makes learning a classifier quite challenging. Semisupervised nearest neigh-
bor and clustering techniques, that only use the normal labels, can often be more
effective than the classification-based techniques. Statistical techniques, though un-
supervised, are effective only when the dimensionality of data is low and statistical
assumptions hold. Information theoretic techniques require a measure that is sen-
sitive enough to detect the effects of even a single anomaly. Otherwise, such tech-
niques can detect anomalies only when there are a significantly adequate number of
anomalies.
Nearestneighborandclustering-basedtechniquesrequiredistancecomputationbe-
tween a pair of data instances. Thus, such techniques assume that the distance mea-
sure can discriminate between the anomalies and normal instances well enough. In
situations where identifying a good distance measure is difficult, classification-based
orstatisticaltechniquesmightbeabetterchoice.
The computational complexity of an anomaly detection technique is a key aspect,
especially when the technique is applied to a real domain. While classification-based,
clustering-based, and statistical techniques have expensive training times, testing is
usuallyfast.Oftenthisisacceptable,sincemodelscanbetrainedinanofflinefashion
while testing is required to be in real time. In contrast, techniques such as nearest
neighbor-based, information theoretic, and spectral techniques, which do not have a
training phase, have an expensive testing phase, which can be a limitation in a real
setting.
Anomalydetectiontechniquestypicallyassumethatanomaliesindataarerarewhen
comparedtonormalinstances.Thoughthisassumptionisgenerallytrue,anomaliesare
notalwaysrare.Forexample,whendealingwithwormdetectionincomputernetworks,
theanomalous(worm)trafficisactuallymorefrequentthanthenormaltraffic.Unsu-
pervised techniques are not suited for such bulk anomaly detection. Techniques oper-
ating in supervised or semisupervised modes can be applied to detect bulk anomalies
[Sunetal.2007;Souleetal.2005].
12. CONCLUDINGREMARKSANDFUTUREWORK
Inthissurveywehavediscusseddifferentwaysinwhichtheproblemofanomalydetec-
tionhasbeenformulatedintheliterature,andhaveattemptedtoprovideanoverview
of the huge literature on various techniques. For each category of anomaly detection
techniques,wehaveidentifiedauniqueassumptionregardingthenotionofnormaland
anomalous data. When applying a given technique to a particular domain, these as-
sumptionscanbeusedasguidelinestoassesstheeffectivenessofthetechniqueinthat
domain. Ideally, a comprehensive survey on anomaly detection should allow a reader
to not only understand the motivation behind using a particular anomaly detection
technique,butalsoprovideacomparativeanalysisofvarioustechniques.Butthecur-
rent research has been done in an unstructured fashion, without relying on a unified
notion of anomalies, which makes the job of providing a theoretical understanding of
theanomalydetectionproblemverydifficult.Apossiblefutureworkwouldbetounify
the assumptions made by different techniques regarding the normal and anomalous
behavior into a statistical or machine learning framework. A limited attempt in this
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:44 V.Chandolaetal.
direction is provided by Knorr and Ng [1997], where the authors show the relation
betweendistance-basedandstatisticalanomaliesfortwo-dimensionaldatasets.
There are several promising directions for further research in anomaly detection.
Contextualandcollectiveanomalydetectiontechniquesarebeginningtofindincreas-
ing applicability in several domains and there is much scope for development of new
techniquesinthisarea.Thepresenceofdataacrossdifferentdistributedlocationshas
motivated the need for distributed anomaly detection techniques [Zimmermann and
Mohay 2006]. While such techniques process information available at multiple sites,
theyoftenhavetosimultaneouslyprotecttheinformationpresentineachsite,thereby
requiringprivacy-preservinganomalydetectiontechniques[VaidyaandClifton2004].
With the emergence of sensor networks, processing data as it arrives has become a
necessity. Many techniques discussed in this survey require the entire test data be-
foredetectinganomalies.Recently,techniqueshavebeenproposedthatcanoperatein
an online fashion [Pokrajac et al. 2007]; such techniques not only assign an anomaly
scoretoatestinstanceasitarrives,butalsoincrementallyupdatethemodel.Another
upcoming area where anomaly detection is finding more and more applicability is in
complexsystems.Anexampleofsuchasystemwouldbeanaircraftsystemwithmulti-
plecomponents.Anomalydetectioninsuchsystemsinvolvesmodelingtheinteraction
amongvariouscomponents[Bronsteinetal.2001].
ACKNOWLEDGMENTS
TheauthorsthankShyamBoriahandGangFangforextensivecommentsonthefinaldraftofthearticle.
REFERENCES
ABE,N.,ZADROZNY,B.,ANDLANGFORD,J. 2006. Outlierdetectionbyactivelearning.InProceedingsofthe
12thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress,
NewYork,504–509.
ABRAHAM, B. AND BOX, G. E. P. 1979. Bayesian analysis of some outlier problems in time series.
Biometrika66,2,229–236.
ABRAHAM, B. AND CHUANG, A. 1989. Outlier detection and time series modeling. Technometrics 31, 2,
241–248.
ADDISON,J.,WERMTER,S.,ANDMACINTYRE,J. 1999. Effectivenessoffeatureextractioninneuralnetwork
architecturesfornoveltydetection.InProceedingsofthe9thInternationalConferenceonArtificialNeural
Networks.vol.2.976–981.
AEYELS,D. 1991. Onthedynamicbehaviourofthenoveltydetectorandthenoveltyfilter.InAnalysisof
ControlledDynamicalSystems:ProgressinSystemsandControlTheory,B.Bonnard,B.Bride,J.Gau-
thier,andI.Kupka,Eds.vol.8.Springer,Berlin,1–10.
AGARWAL, D. 2005. An empirical Bayes approach to detect anomalies in dynamic multidimensional ar-
rays.InProceedingsofthe5thIEEEInternationalConferenceonDataMining.IEEEComputerSociety,
26–33.
AGARWAL,D. 2006. Detectinganomaliesincross-classifiedstreams:ABayesianapproach.Knowl.Inform.
Syst.11,1,29–44.
AGGARWAL,C. 2005. Onabnormalitydetectioninspuriouslypopulateddatastreams.InProceedingsofthe
5thSIAMDataMin.Conference.80–91.
AGGARWAL, C. AND YU, P. 2001. Outlier detection for high dimensional data. In Proceedings of the ACM
SIGMODInternationalConferenceonManagementofData.ACMPress,37–46.
AGGARWAL,C.C.ANDYU,P.S. 2008. Outlierdetectionwithuncertaindata.InProceedingsoftheInterna-
tionalConferenceonDataMining(SDM).483–493.
AGOVIC,A.,BANERJEE,A.,GANGULY,A.R.,ANDPROTOPOPESCU,V. 2007. Anomalydetectionintransportation
corridors using manifold embedding. In Proceedings of the 1st International Workshop on Knowledge
DiscoveryfromSensorData.ACMPress.
AGRAWAL,R.ANDSRIKANT,R. 1995. Miningsequentialpatterns.InProceedingsofthe11thInternational
ConferenceonDataEngineering.IEEEComputerSociety,3–14.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:45
AGYEMANG,M.,BARKER,K.,ANDALHAJJ,R. 2006. Acomprehensivesurveyofnumericandsymbolicoutlier
miningtechniques.Intel.DataAnal.10,6,521–538.
ALBRECHT,S.,BUSCH,J.,KLOPPENBURG,M.,METZE,F.,ANDTAVAN,P. 2000. Generalizedradialbasisfunction
networksforclassificationandnoveltydetection:Self-organizationofoptionalBayesiandecision.Neural
Netw.13,10,1075–1093.
ALESKEROV,E.,FREISLEBEN,B.,ANDRAO,B. 1997. Cardwatch:Aneuralnetworkbaseddatabaseminingsys-
temforcreditcardfrauddetection.InProceedingsoftheIEEEConferenceonComputationalIntelligence
forFinancialEngineering.220–226.
ALLAN,J.,CARBONELL,J.,DODDINGTON,G.,YAMRON,J.,ANDYANG,Y. 1998. Topicdetectionandtrackingpilot
study.InProceedingsoftheDARPABroadcastNewsTranscriptionandUnderstandingWorkshop.194–
218.
ANDERSON,D.LUNT,T.F.,JAVITZ,H.,TAMARU,A.,ANDVALDES,A. 1995. Detectingunusualprogrambehavior
usingthestatisticalcomponentsofNIDES.Tech.rep.SRI–CSL–95–06,ComputerScienceLaboratory,
SRIInternational.
ANDERSON, D., FRIVOLD, T., TAMARU, A., AND VALDES, A. 1994. Next-generation intrusion detection expert
system (NIDES), software users manual, beta-update release. Tech. rep. SRI–CSL–95–07, Computer
ScienceLaboratory,SRIInternational.
ANDO,S. 2007. Clusteringneedlesinahaystack:Aninformationtheoreticanalysisofminorityandoutlier
detection.InProceedingsofthe7thInternationalConferenceonDataMining.13–22.
ANGIULLI,F.ANDPIZZUTI,C. 2002. Fastoutlierdetectioninhighdimensionalspaces.InProceedingsofthe
6thEuropeanConferenceonPrinciplesofDataMiningandKnowledgeDiscovery.Springer-Verlag,15–26.
ANSCOMBE,F.J.ANDGUTTMAN,I. 1960. Rejectionofoutliers.Technometrics2,2,123–147.
ARNING, A., AGRAWAL, R., AND RAGHAVAN, P. 1996. A linear method for deviation detection in large
databases.InProceedingsofthe2ndInternationalConferenceofKnowledgeDiscoveryandDataMining.
164–169.
AUGUSTEIJN, M. AND FOLKERT, B. 2002. Neural network classification and novelty detection. Int. J. Rem.
Sens.23,14,2891–2902.
BAKAR,Z.,MOHEMAD,R.,AHMAD,A.,ANDDERIS,M. 2006. Acomparativestudyforoutlierdetectiontechniques
indatamining.ProceedingsoftheIEEEConferenceonCyberneticsandIntelligentSystems.1–6.
BAKER,D.,HOFMANN,T.,MCCALLUM,A.,ANDYANG,Y. 1999. Ahierarchicalprobabilisticmodelfornovelty
detectionintext.InProceedingsoftheInternationalConferenceonMachineLearning.
BARBARA,D.,COUTO,J.,JAJODIA,S.,ANDWU,N. 2001a. Adam:Atestbedforexploringtheuseofdatamining
inintrusiondetection.SIGMODRec.30,4,15–24.
BARBARA, D., COUTO, J., JAJODIA, S., AND WU, N. 2001b. Detecting novel network intrusions using Bayes
estimators.InProceedingsofthe1stSIAMInternationalConferenceonDataMining.
BARBARA,D.,LI,Y.,COUTO,J.,LIN,J.-L.,ANDJAJODIA,S. 2003. Bootstrappingadataminingintrusiondetec-
tionsystem.InProceedingsoftheACMSymposiumonAppliedComputing.ACMPress,421–425.
BARNETT,V. 1976. Theorderingofmultivariatedata(withdiscussion).J.RoyalStatis.Soc.SeriesA139,
318–354.
BARNETT,V.ANDLEWIS,T. 1994. OutliersinStatisticalData.JohnWiley.
BARSON,P.,DAVEY,N.,FIELD,S.D.H.,FRANK,R.J.,ANDMCASKIE,G. 1996. Thedetectionoffraudinmobile
phonenetworks.NeuralNetw.World6,4.
BASU,S.,BILENKO,M.,ANDMOONEY,R.J. 2004. Aprobabilisticframeworkforsemi-supervisedclustering.
InProceedingsofthe10thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining.ACMPress,59–68.
BASU,S.ANDMECKESHEIMER,M. 2007. Automaticoutlierdetectionfortimeseries:anapplicationtosensor
data.Know.Inform.Syst.11,2,137–154.
BAY,S.D.ANDSCHWABACHER,M. 2003. Miningdistance-basedoutliersinnearlineartimewithrandomiza-
tionandasimplepruningrule.InProceedingsofthe9thACMSIGKDDInternationalConferenceon
KnowledgeDiscoveryandDataMining.ACMPress,29–38.
BECKMAN,R.J.ANDCOOK,R.D. 1983. Outlier...s.Technometrics25,2,119–149.
BEJERANO,G.ANDYONA,G. 2001. Variationsonprobabilisticsuffixtrees:statisticalmodelingandprediction
ofproteinfamilies.Bioinformatics17,1,23–43.
BENTLEY, J. L. 1975. Multi-dimensional binary search trees used for associative searching. Comm.
ACM18,9,509–517.
BIANCO,A.M.,BEN,M.G.,MARTINEZ,E.J.,ANDYOHAI,V.J. 2001. Outlierdetectioninregressionmodels
witharimaerrorsusingrobustestimates.J.Forecast.20,8,565–579.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:46 V.Chandolaetal.
BISHOP,C. 1994. Noveltydetectionandneuralnetworkvalidation.InProceedingsoftheIEEEConference
onVision,ImageandSignalProcessing.vol.141.217–222.
BLENDER,R.,FRAEDRICH,K.,ANDLUNKEIT,F. 1997. Identificationofcyclone-trackregimesinthenorthat-
lantic.Quart.J.RoyalMeteor.Soc.123,539,727–741.
BOLTON,R.ANDHAND,D. 1999. Unsupervisedprofilingmethodsforfrauddetection.InProceedingsofthe
ConferenceonCreditScoringandCreditControlVII.
BORIAH, S., CHANDOLA, V., AND KUMAR, V. 2008. Similarity measures for categorical data: A com-
parative evaluation. In Proceedings of the 8th SIAM International Conference on Data Mining.
243–254.
BORISYUK,R.,DENHAM,M.,HOPPENSTEADT,F.,KAZANOVICH,Y.,ANDVINOGRADOVA,O. 2000. Anoscillatoryneural
networkmodelofsparsedistributedmemoryandnoveltydetection.Biosystems58,265–272.
BOX,G.E.P.ANDTIAO,G.C. 1968. Bayesiananalysisofsomeoutlierproblems.Biometrika55,1,119–129.
BRANCH,J.,SZYMANSKI,B.,GIANNELLA,C.,WOLFF,R.,ANDKARGUPTA,H. 2006. In-networkoutlierdetection
inwirelesssensornetworks.InProceedingsofthe26thIEEEInternationalConferenceonDistributed
ComputingSystems.
BRAUSE,R.,LANGSDORF,T.,ANDHEPP,M. 1999. Neuraldataminingforcreditcardfrauddetection.InPro-
ceedingsoftheIEEEInternationalConferenceonToolswithArtificialIntelligence.103–106.
BREUNIG, M. M., KRIEGEL, H.-P., NG, R. T., AND SANDER, J. 1999. Optics-of: Identifying local outliers. In
Proceedings of the 3rd European Conference on Principles of Data Mining and Knowledge Discovery.
Springer-Verlag,262–270.
BREUNIG,M.M.,KRIEGEL,H.-P.,NG,R.T.,ANDSANDER,J. 2000. LOF:Identifyingdensity-basedlocaloutliers.
In Proceedings of the ACM SIGMOD International Conference on Management of Data. ACM Press,
93–104.
BRITO,M.R.,CHAVEZ,E.L.,QUIROZ,A.J.,ANDYUKICH,J.E. 1997. Connectivityofthemutualk-nearest-
neighborgraphinclusteringandoutlierdetection.Statis.Prob.Lett.35,1,33–42.
BROCKETT,P.L.,XIA,X.,ANDDERRIG,R.A. 1998. UsingKohonen’sself-organizingfeaturemaptouncover
automobilebodilyinjuryclaimsfraud.J.RiskInsur.65,2,245–274.
BRONSTEIN,A.,DAS,J.,DURO,M.,FRIEDRICH,R.,KLEYNER,G.,MUELLER,M.,SINGHAL,S.,ANDCOHEN,I. 2001.
BayesiannetworksfordetectinganomaliesinInternet-basedservices.InProceedingsoftheInternational
SymposiumonIntegratedNetworkManagement.
BROTHERTON,T.ANDJOHNSON,T. 2001. Anomalydetectionforadvancedmilitaryaircraftusingneuralnet-
works.InProceedingsoftheIEEEAerospaceConference.
BROTHERTON,T.,JOHNSON,T.,ANDCHADDERDON,G. 1998. Classificationandnoveltydetectionusinglinear
models and a class dependent-elliptical basis function neural network. In Proceedings of the IJCNN
Conference.
BUDALAKOTI,S.,SRIVASTAVA,A.,AKELLA,R.,ANDTURKOV,E. 2006. Anomalydetectioninlargesetsofhigh-
dimensionalsymbolsequences.Tech.rep.NASATM-2006-214553,NASAAmesResearchCenter.
BYERS,S.D.ANDRAFTERY,A.E. 1998. Nearestneighborclutterremovalforestimatingfeaturesinspatial
pointprocesses.J.Amer.Statis.Assoc.93,577–584.
BYUNGHO,H.ANDSUNGZOON,C. 1999. CharacteristicsofautoassociativeMLPasanoveltydetector.InPro-
ceedingsoftheIEEEInternationalJointConferenceonNeuralNetworks.Vol.5.3086–3091.
CABRERA,J.B.D.,LEWIS,L.,ANDMEHRA,R.K. 2001. Detectionandclassificationofintrusionsandfaults
usingsequencesofsystemcalls.SIGMODRec.30,4,25–34.
CAMPBELL,C.ANDBENNETT,K. 2001. Alinearprogrammingapproachtonoveltydetection.InProceedings
oftheConferenceonAdvancesinNeuralInformationProcessing.vol.14.CambridgePress.
CAUDELL, T. AND NEWMAN, D. 1993. An adaptive resonance architecture to define normality and detect
noveltiesintimeseriesanddatabases.InProceedingsoftheIEEEWorldCongressonNeuralNetworks.
IEEE,166–176.
CHAKRABARTI,S.,SARAWAGI,S.,ANDDOM,B. 1998. Miningsurprisingpatternsusingtemporaldescription
length.InProceedingsofthe24rdInternationalConferenceonVeryLargeDataBases.MorganKaufmann
PublishersInc.,606–617.
CHANDOLA,V.,BANERJEE,A.,ANDKUMAR,V. 2007. Anomalydetection:Asurvey.Tech.rep.07-017,Computer
ScienceDepartment,UniversityofMinnesota.
CHANDOLA,V.,BORIAH,S.,ANDKUMAR,V. 2008. Understandingcategoricalsimilaritymeasuresforoutlier
detection.Tech.rep.08-008,UniversityofMinnesota.
CHANDOLA,V.,EILERTSON,E.,ERTOZ,L.,SIMON,G.,ANDKUMAR,V. 2006. Dataminingforcybersecurity.In
DataWarehousingandDataMiningTechniquesforComputerSecurity,A.Singhal,Ed.Springer.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:47
CHATZIGIANNAKIS,V.,PAPAVASSILIOU,S.,GRAMMATIKOU,M.,ANDMAGLARIS,B. 2006. Hierarchicalanomalyde-
tectionindistributedlarge-scalesensornetworks.InProceedingsofthe11thIEEESymposiumonCom-
putersandCommunications(ISCC).IEEEComputerSociety,761–767.
CHAUDHARY,A.,SZALAY,A.S.,ANDMOORE,A.W. 2002. Veryfastoutlierdetectioninlargemultidimensional
datasets.InProceedingsoftheACMSIGMODWorkshopinResearchIssuesinDataMiningandKnowl-
edgeDiscovery(DMKD).ACMPress.
CHAWLA,N.V.,JAPKOWICZ,N.,ANDKOTCZ,A. 2004. Editorial:specialissueonlearningfromimbalanceddata
sets.SIGKDDExplor.6,1,1–6.
CHEN,D.,SHAO,X.,HU,B.,ANDSU,Q. 2005. Simultaneouswavelengthselectionandoutlierdetectionin
multivariateregressionofnear-infraredspectra.Anal.Sci.21,2,161–167.
CHIU, A. AND CHEE FU, A. W. 2003. Enhancements on local outlier detection. In Proceedings of the 7th
InternationalDatabaseEngineeringandApplicationsSymposium.298–307.
CHOW,C.ANDYEUNG,D.-Y. 2002. Parzen-windownetworkintrusiondetectors.InProceedingsofthe16th
InternationalConferenceonPatternRecognition.vol.4.IEEEComputerSociety,40385.
COX,K.C.,EICK,S.G.,WILLS,G.J.,ANDBRACHMAN,R.J. 1997. Visualdatamining:Recognizingtelephone
callingfraud.J.DataMin.Knowl.Disc.1,2,225–231.
CROOK,P.ANDHAYES,G. 2001. Arobotimplementationofabiologicallyinspiredmethodfornoveltydetec-
tion.InProceedingsoftheTowardsIntelligentMobileRobotsConference.
CROOK,P.A.,MARSLAND,S.,HAYES,G.,ANDNEHMZOW,U. 2002. Ataleoftwofilters:Onlinenoveltydetection.
InProceedingsoftheInternationalConferenceonRoboticsandAutomation.3894–3899.
CUN, Y. L., BOSER, B., DENKER, J. S., HOWARD, R. E., HUBBARD, W., JACKEL, L. D., AND HENDERSON, D. 1990.
Handwritten digit recognition with a back-propagation network. In Advances in Neural Information
ProcessingSystems.396–404.MorganKoufamann.
DAS,K.ANDSCHNEIDER,J. 2007. Detectinganomalousrecordsincategoricaldatasets.InProceedingsofthe
13thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress.
DASGUPTA,D.ANDMAJUMDAR,N. 2002. Anomalydetectioninmultidimensionaldatausingnegativeselection
algorithm.InProceedingsoftheIEEEConferenceonEvolutionaryComputation.1039–1044.
DASGUPTA,D.ANDNINO,F. 2000. Acomparisonofnegativeandpositiveselectionalgorithmsinnovelpattern
detection.InProceedingsoftheIEEEInternationalConferenceonSystems,Man,andCybernetics.vol.1.
125–130.
DAVY,M.ANDGODSILL,S. 2002. Detectionofabruptspectralchangesusingsupportvectormachines,anap-
plicationtoaudiosignalsegmentation.InProceedingsoftheIEEEInternationalConferenceonAcoustics,
Speech,andSignalProcessing.
DEBAR,H.,DACIER,M.,NASSEHI,M.,ANDWESPI,A. 1998. Fixedvs.variable-lengthpatternsfordetecting
suspiciousprocessbehavior.InProceedingsofthe5thEuropeanSymposiumonResearchinComputer
Security.Springer-Verlag,1–15.
DENNING,D.E. 1987. Anintrusiondetectionmodel.IEEETrans.Softw.Eng.13,2,222–232.
DESFORGES,M.,JACOB,P.,ANDCOOPER,J. 1998. Applicationsofprobabilitydensityestimationtothedetec-
tionofabnormalconditionsinengineering.InProceedingsoftheInstituteoftheMechanicalEngineers.
vol.212.687–703.
DIAZ, I. AND HOLLMEN, J. 2002. Residual generation and visualization for understanding novel process
conditions.InProceedingsoftheIEEEInternationalJointConferenceonNeuralNetworks.IEEE,2070–
2075.
DIEHL,C.ANDHAMPSHIRE,J. 2002. Real-timeobjectclassificationandnoveltydetectionforcollaborative
video surveillance. In Proceedings of the IEEE International Joint Conference on Neural Networks.
IEEE.
DONOHO,S. 2004. Earlydetectionofinsidertradinginoptionmarkets.InProceedingsofthe10thACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress,420–429.
DORRONSORO, J. R., GINEL, F., SANCHEZ, C., AND CRUZ, C. S. 1997. Neural fraud detection in credit card
operations.IEEETrans.NeuralNetw.8,4,827–834.
DU,W.,FANG,L.,ANDPENG,N. 2006. Lad:Localizationanomalydetectionforwirelesssensornetworks.J.
Paral.Distrib.Comput.66,7,874–886.
DUDA,R.O.,HART,P.E.,ANDSTORK,D.G. 2000. PatternClassification2ndEd.Wiley-Interscience.
DUTTA,H.,GIANNELLA,C.,BORNE,K.,ANDKARGUPTA,H. 2007. Distributedtop-koutlierdetectioninastron-
omycatalogsusingtheDEMACsystem.InProceedingsofthe7thSIAMInternationalConferenceon
DataMining.
EDGEWORTH,F.Y. 1887. Ondiscordantobservations.Philosoph.Mag.23,5,364–375.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:48 V.Chandolaetal.
EMAMIAN, V., KAVEH, M., AND TEWFIK, A. 2000. Robust clustering of acoustic emission signals using the
Kohonennetwork.InProceedingsoftheIEEEInternationalConferenceofAcoustics,SpeechandSignal
Processing.IEEEComputerSociety.
ENDLER,D. 1998. Intrusiondetection:Applyingmachinelearningtosolarisauditdata.InProceedingsof
the14thAnnualComputerSecurityApplicationsConference.IEEEComputerSociety,268.
ERTOZ,L.,EILERTSON,E.,LAZAREVIC,A.,TAN,P.-N.,KUMAR,V.,SRIVASTAVA,J.,ANDDOKAS,P. 2004. MINDS—
MinnesotaIntrusionDetectionSystem.InDataMining—NextGenerationChallengesandFutureDirec-
tions.MITPress.
ERTO¨Z,L.,STEINBACH,M.,ANDKUMAR,V. 2003. Findingtopicsincollectionsofdocuments:Asharednearest
neighborapproach.InClusteringandInformationRetrieval.83–104.
ESCALANTE,H.J. 2005. Acomparisonofoutlierdetectionalgorithmsformachinelearning.InProceedings
oftheInternationalConferenceonCommunicationsinComputing.
ESKIN, E. 2000. Anomaly detection over noisy data using learned probability distributions. In Proceed-
ings of the 17th International Conference on Machine Learning. Morgan Kaufmann Publishers Inc.,
255–262.
ESKIN,E.,ARNOLD,A.,PRERAU,M.,PORTNOY,L.,ANDSTOLFO,S. 2002. Ageometricframeworkforunsupervised
anomalydetection.InProceedingsoftheConferenceonApplicationsofDataMininginComputerSecurity.
KluwerAcademics,78–100.
ESKIN,E.,LEE,W.,ANDSTOLFO,S. 2001. Modelingsystemcallforintrusiondetectionusingdynamicwindow
sizes.InProceedingsofDARPAInformationSurvivabilityConferenceandExposition(DISCEX).
ESTER,M.,KRIEGEL,H.-P.,SANDER,J.,ANDXU,X. 1996. Adensity-basedalgorithmfordiscoveringclusters
inlargespatialdatabaseswithnoise.InProceedingsofthe2ndInternationalConferenceonKnowledge
DiscoveryandDataMining,E.Simoudis,J.Han,andU.Fayyad,Eds.AAAIPress,226–231.
FAN, W., MILLER, M., STOLFO, S. J., LEE, W., AND CHAN, P. K. 2001. Using artificial anomalies to detect
unknownandknownnetworkintrusions.InProceedingsoftheIEEEInternationalConferenceonData
Mining.IEEEComputerSociety,123–130.
FAWCETT,T.ANDPROVOST,F. 1999. Activitymonitoring:noticinginterestingchangesinbehavior.InProceed-
ingsofthe5thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM
Press,53–62.
FORREST,S.,D’HAESELEER,P.,ANDHELMAN,P. 1996a. Animmunologicalapproachtochangedetection:Al-
gorithms,analysisandimplications.InProceedingsoftheIEEESymposiumonSecurityandPrivacy.
IEEEComputerSociety,110.
FORREST, S., ESPONDA, F., AND HELMAN, P. 2004. A formal framework for positive and negative detection
schemes.InIEEETrans.Syst.ManCybernetics,PartB.IEEE,357–373.
FORREST,S.,HOFMEYR,S.A.,SOMAYAJI,A.,ANDLONGSTAFF,T.A. 1996b. Asenseofselfforunixprocesses.In
ProceedingsoftheIEEEISRSP.120–128.
FORREST,S.,PERELSON,A.S.,ALLEN,L.,ANDCHERUKURI,R. 1994. Self-nonselfdiscriminationinacomputer.
InProceedingsoftheIEEESymposiumonSecurityandPrivacy.IEEEComputerSociety,202.
FORREST,S.,WARRENDER,C.,ANDPEARLMUTTER,B. 1999. Detectingintrusionsusingsystemcalls:Alternate
datamodels.InProceedingsoftheIEEEISRSP.IEEEComputerSociety,133–145.
FOX,A.J. 1972. Outliersintimeseries.J.RoyalStatis.Soc.SeriesB34,3,350–363.
FUJIMAKI,R.,YAIRI,T.,ANDMACHIDA,K. 2005. Anapproachtospacecraftanomalydetectionproblemusing
kernelfeaturespace.InProceedingsofthe11thACMSIGKDDInternationalConferenceonKnowledge
DiscoveryinDataMining.ACMPress,401–410.
GALEANO, P., PEA, D., AND TSAY, R. S. 2004. Outlier detection in multivariate time series via projec-
tion pursuit. Statistics and econometrics working articles ws044211, Departamento de Estad¨ıstica y
Econometr¨ıca,UniversidadCarlosIII.
GHOSH,A.K.,SCHWARTZBARD,A.,ANDSCHATZ,M. 1999a. Learningprogrambehaviorprofilesforintrusion
detection.InProceedingsofthe1stUSENIXWorkshoponIntrusionDetectionandNetworkMonitoring.
51–62.
GHOSH,A.K.,SCHWARTZBARD,A.,ANDSCHATZ,M. 1999b. Usingprogrambehaviorprofilesforintrusionde-
tection.InProceedingsoftheSANS3rdConferenceandWorkshoponIntrusionDetectionandResponse.
GHOSH,A.K.,WANKEN,J.,ANDCHARRON,F. 1998. Detectinganomalousandunknownintrusionsagainstpro-
grams.InProceedingsofthe14thAnnualComputerSecurityApplicationsConference.IEEEComputer
Society,259.
GHOSH,S.ANDREILLY,D.L. 1994. Creditcardfrauddetectionwithaneural-network.InProceedingsofthe
27thAnnualHawaiiInternationalConferenceonSystemScience.vol.3.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:49
GHOTING,A.,PARTHASARATHY,S.,ANDOTEY,M. 2006. Fastminingofdistance-basedoutliersinhighdimen-
sionaldatasets.InProceedingsoftheSIAMInternationalConferenceonDataMining.
GIBBONS,R.D. 1994. StatisticalMethodsforGroundwaterMonitoring.JohnWiley&Sons,Inc.
GOLDBERGER,A.L.,AMARAL,L.A.N.,GLASS,L.,HAUSDORFF,J.M.,IVANOV,P.C.,MARK,R.G.,MIETUS,J.E.,MOODY,
G.B.,PENG,C.-K.,ANDSTANLEY,H.E. 2000. PhysioBank,PhysioToolkit,andPhysioNet:Components
ofanewresearchresourceforcomplexphysiologicsignals.Circulation101,23,e215–e220.Circulation
ElectronicPages:http://circ.ahajournals.org/cgi/content/full/101/23/e215.
GONZALEZ,F.A.ANDDASGUPTA,D. 2003. Anomalydetectionusingreal-valuednegativeselection.Genetic
Program.Evolv.Mach.4,4,383–403.
GRUBBS, F. 1969. Procedures for detecting outlying observations in samples. Technometrics 11, 1,
1–21.
GUHA,S.,RASTOGI,R.,ANDSHIM,K. 2000. ROCK:Arobustclusteringalgorithmforcategoricalattributes.
Inform.Syst.25,5,345–366.
GUNTER,S.,SCHRAUDOLPH,N.N.,ANDVISHWANATHAN,S.V.N. 2007. Fastiterativekernelprincipalcomponent
analysis.J.Mach.Learn.Res.8,1893–1918.
GUTTORMSSON,S.E,MARKSR.J.II,EL-SHARKAWI,M.A.,ANDKERSZENBAUM,I. 1999. Ellipticalnoveltygrouping
foronlineshort-turndetectionofexcitedrunningrotors.IEEETrans.EnergyConv.14,1.
GWADERA,R.,ATALLAH,M.J.,ANDSZPANKOWSKI,W. 2004. Detectionofsignificantsetsofepisodesinevent
sequences.InProceedingsofthe4thIEEEInternationalConferenceonDataMining.IEEEComputer
Society,3–10.
GWADERA,R.,ATALLAH,M.J.,ANDSZPANKOWSKI,W. 2005a. Markovmodelsforidentificationofsignificant
episodes.InProceedingsofthe5thSIAMInternationalConferenceonDataMining.
GWADERA,R.,ATALLAH,M.J.,ANDSZPANKOWSKI,W. 2005b. Reliabledetectionofepisodesineventsequences.
Knowl.Inform.Syst.7,4,415–437.
HARRIS,T. 1993. Neuralnetworkinmachinehealthmonitoring.ProfessionalEngin.
HARTIGAN,J.A.ANDWONG,M.A. 1979. Ak-meansclusteringalgorithm.Appl.Stat.28,100–108.
HAUTAMAKI,V.,KARKKAINEN,I.,ANDFRANTI,P. 2004. Outlierdetectionusingk-nearestneighbourgraph.In
Proceedingsofthe17thInternationalConferenceonPatternRecognition.vol.3.IEEEComputerSociety,
430–433.
HAWKINS,D. 1980. IdentificationofOutliers.ChapmanandHall,LondonandNewYork.
HAWKINS,D.M. 1974. Thedetectionoferrorsinmultivariatedatausingprincipalcomponents.J.Amer.
Statis.Assoc.69,346,340–344.
HAWKINS, S., HE, H., WILLIAMS, G. J., AND BAXTER, R. A. 2002. Outlier detection using replicator neural
networks.InProceedingsofthe4thInternationalConferenceonDataWarehousingandKnowledgeDis-
covery.Springer-Verlag,170–180.
HAZEL,G.G. 2000. MultivariateGaussianMRFformulti-spectralscenesegmentationandanomalyde-
tection.GeoRS38,3,1199–1211.
HE,H.,WANG,J.,GRACO,W.,ANDHAWKINS,S. 1997. Applicationofneuralnetworkstodetectionofmedical
fraud.ExpertSyst.Appl.13,4,329–336.
HE, Z., DENG, S., AND XU, X. 2002. Outlier detection integrating semantic knowledge. In Proceedings of
the3rdInternationalConferenceonAdvancesinWeb-AgeInformationManagement.Springer-Verlag,
126–131.
HE,Z.,DENG,S.,XU,X.,ANDHUANG,J.Z. 2006. Afastgreedyalgorithmforoutliermining.InProceedings
ofthe10thPacific-AsiaConferenceonKnowledgeandDataDiscovery.567–576.
HE,Z.,XU,X.,ANDDENG,S. 2003. Discoveringcluster-basedlocaloutliers.PatternRecog.Lett.24,9–10,
1641–1650.
HE,Z.,XU,X.,ANDDENG,S. 2005. Anoptimizationmodelforoutlierdetectionincategoricaldata.InPro-
ceedingsoftheInternationalConferenceonIntelligentComputing.LectureNotesinComputerScience,
vol.3644.Springer.
HE,Z.,XU,X.,HUANG,J.Z.,ANDDENG,S. 2004a. AFrequentPatternDiscoveryMethodforOutlierDetection.
Springer,726–732.
HE,Z.,XU,X.,HUANG,J.Z.,ANDDENG,S. 2004b. MiningClassOutliers:Concepts,AlgorithmsandAppli-
cations.Springer,588–589.
HELLER,K.A.,SVORE,K.M.,KEROMYTIS,A.D.,ANDSTOLFO,S.J. 2003. Oneclasssupportvectormachines
fordetectinganomalouswindowsregistryaccesses.InProceedingsoftheWorkshoponDataMiningfor
ComputerSecurity.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:50 V.Chandolaetal.
HELMAN,P.ANDBHANGOO,J. 1997. Astatistically-basedsystemforprioritizinginformationexplorationun-
deruncertainty.InProceedingsoftheIEEEInternationalConferenceonSystems,Man,andCybernetics.
vol.27.IEEE,449–466.
HELMER,G.,WONG,J.,HONAVAR,V.,ANDMILLER,L. 1998. Intelligentagentsforintrusiondetection.InPro-
ceedingsoftheIEEEInformationTechnologyConference.121–124.
HICKINBOTHAM,S.J.ANDAUSTIN,J. 2000a. Noveltydetectioninairframestraindata.InProceedingsofthe
15thInternationalConferenceonPatternRecognition.Vol.2.536–539.
HICKINBOTHAM,S.J.ANDAUSTIN,J. 2000b. Noveltydetectioninairframestraindata.InProceedingsofthe
IEEE-INNS-ENNSInternationalJointConferenceonNeuralNetworks.vol.6.24–27.
HO, L. L., MACEY, C. J., AND HILLER, R. 1999. A distributed and reliable platform for adaptive anomaly
detectioninIPnetworks.InProceedingsofthe10thIFIP/IEEEInternationalWorkshoponDistributed
Systems:OperationsandManagement.Springer-Verlag,33–46.
HO,T.V.ANDROUAT,J. 1997. Anoveltydetectorusinganetworkofintegrateandfireneurons.Lecture
NotesinComputerScience, vol.1327.103–108.
HO,T.V.ANDROUAT,J. 1998. Noveltydetectionbasedonrelaxationtimeofanetworkofintegrate-and-fire
neurons.InProceedingsofthe2ndIEEEWorldCongressonComputationalIntelligence.1524–1529.
HODGE, V. AND AUSTIN, J. 2004. A survey of outlier detection methodologies. Artif. Intel. Rev. 22, 2,
85–126.
HOFMEYR,S.A.,FORREST,S.,ANDSOMAYAJI,A. 1998. Intrusiondetectionusingsequencesofsystemcalls.
J.Comput.Secur.6,3,151–180.
HOLLIER,G.ANDAUSTIN,J. 2002. Noveltydetectionforstrain-gaugedegradationusingmaximallycorrelated
components.InProceedingsoftheEuropeanSymposiumonArtificialNeuralNetworks.257–262–539.
HOLLMEN, J. AND TRESP, V. 1999. Call-based fraud detection in mobile communication networks using a
hierarchicalregime-switchingmodel.InProceedingsoftheConferenceonAdvancesinNeuralInformation
ProcessingSystemsII.MITPress,889–895.
HORN,P.S.,FENG,L.,LI,Y.,ANDPESCE,A.J. 2001. Effectofoutliersandnonhealthyindividualsonreference
intervalestimation.ClinicalChem.47,12,2137–2145.
HU, W., LIAO, Y., AND VEMURI, V. R. 2003. Robust anomaly detection using support vector machines. In
ProceedingsoftheInternationalConferenceonMachineLearning.MorganKaufmannPublishersInc.,
282–289.
HUBER,P. 1974. RobustStatistics.Wiley,NewYork.
HUBER,P.J. 1985. Projectionpursuit(withdiscussions).Ann.Stat.13,2,435–475.
IDE,T.ANDKASHIMA,H. 2004. Eigenspace-basedanomalydetectionincomputersystems.InProceedingsof
the10thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress,
440–449.
IDE´,T.,PAPADIMITRIOU,S.,ANDVLACHOS,M. 2007. Computingcorrelationanomalyscoresusingstochastic
nearestneighbors.InProceedingsoftheInternationalConferenceDataMining.523–528.
IHLER,A.,HUTCHINS,J.,ANDSMYTH,P. 2006. Adaptiveeventdetectionwithtime-varyingPoissonprocesses.
InProceedingsofthe12thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining.ACMPress,207–216.
ILGUN,K.,KEMMERER,R.A.,ANDPORRAS,P.A. 1995. Statetransitionanalysis:Arule-basedintrusionde-
tectionapproach.IEEETrans.Softw.Eng.21,3,181–199.
JAGADISH,H.V.,KOUDAS,N.,ANDMUTHUKRISHNAN,S. 1999. Miningdeviantsinatimeseriesdatabase.InPro-
ceedingsofthe25thInternationalConferenceonVeryLargeDataBases.MorganKaufmannPublishers
Inc.,102–113.
JAGOTA,A. 1991. Noveltydetectiononaverylargenumberofmemoriesstoredinahopfield-stylenetwork.
InProceedingsoftheInternationalJointConferenceonNeuralNetworks.vol.2.905.
JAIN,A.K.ANDDUBES,R.C. 1988. AlgorithmsforClusteringData.Prentice-Hall,Inc.
JAKUBEK,S.ANDSTRASSER,T. 2002. Fault-diagnosisusingneuralnetworkswithellipsoidalbasisfunctions.
InProceedingsoftheAmericanControlConference.vol.5.3846–3851.
JANAKIRAM,D.,REDDY,V.,ANDKUMAR,A. 2006. OutlierdetectioninwirelesssensornetworksusingBayesian
beliefnetworks.InProceedingsofthe1stInternationalConferenceonCommunicationSystemSoftware
andMiddleware.1–6.
JAPKOWICZ,N.,MYERS,C.,ANDGLUCK,M.A. 1995. Anoveltydetectionapproachtoclassification.InPro-
ceedingsoftheInternationalJointConferenceonArtificialIntelligence.518–523.
JAVITZ,H.S.ANDVALDES,A. 1991. TheSRIIDESstatisticalanomalydetector.InProceedingsoftheIEEE
SymposiumonResearchinSecurityandPrivacy.IEEEComputerSociety.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:51
JIANG,M.F.,TSENG,S.S.,ANDSU,C.M. 2001. Two-phaseclusteringprocessforoutliersdetection.Patt.
Recog.Lett.22,6-7,691–700.
JIN,W.,TUNG,A.K.H.,ANDHAN,J. 2001. Miningtop-nlocaloutliersinlargedatabases.InProceedingsof
the7thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress,
293–298.
JOACHIMS,T. 2006. TraininglinearSVMSinlineartime.InProceedingsofthe12thACMSIGKDDInter-
nationalConferenceonKnowledgeDiscoveryandDataMining.ACM,217–226.
JOLLIFFE,I.T. 2002. PrincipalComponentAnalysis,2ndEd.Springer.
JOSHI,M.V.,AGARWAL,R.C.,ANDKUMAR,V. 2001. Miningneedleinahaystack:classifyingrareclassesvia
two-phaseruleinduction.InProceedingsoftheACMSIGMODInternationalConferenceonManagement
ofData.ACMPress,91–102.
JOSHI,M.V.,AGARWAL,R.C.,ANDKUMAR,V. 2002. Predictingrareclasses:canboostingmakeanyweak
learnerstrong?InProceedingsofthe8thACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining.ACM,297–306.
KADOTA,K.,TOMINAGA,D.,AKIYAMA,Y.,ANDTAKAHASHI,K. 2003. Detectingoutlyingsamplesinmicro-array
data:Acriticalassessmentoftheeffectofoutliersonsampleclassification.Chem-BioInformatics3,1,
30–45.
KARYPIS, G. AND KUMAR, V. 1998. Multi-level k-way partitioning scheme for irregular graphs. J. Paral.
Distrib.Comput.48,1,96–129.
KEARNS,M.J. 1990. ComputationalComplexityofMachineLearning.MITPress.
KEOGH,E.,LIN,J.,LEE,S.-H.,ANDHERLE,H.V. 2006. Findingthemostunusualtimeseriessubsequence:
Algorithmsandapplications.Knowl.Inform.Syst.11,1,1–27.
KEOGH,E.,LONARDI,S.,ANDCHI’CHIU,B.Y. 2002. Findingsurprisingpatternsinatimeseriesdatabasein
lineartimeandspace.InProceedingsofthe8thACMSIGKDDInternationalConferenceonKnowledge
DiscoveryandDataMining.ACMPress,550–556.
KEOGH,E.,LONARDI,S.,ANDRATANAMAHATANA,C.A. 2004. Towardsparameter-freedatamining.InProceed-
ingsofthe10thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM
Press,206–215.
KEOGH,E.ANDSMYTH,P. 1997. Aprobabilisticapproachtofastpatternmatchingintimeseriesdatabases.
InProceedingsofthe3rdInternationalConferenceonKnowledgeDiscoveryandDataMining,D.Heck-
erman,H.Mannila,D.Pregibon,andR.Uthurusamy,Eds.AAAIPress,24–30.
KING, S., KING, D., P. ANUZIS, K. A., TARASSENKO, L., HAYTON, P., AND UTETE, S. 2002. The use of novelty
detectiontechniquesformonitoringhigh-integrityplant.InProceedingsoftheInternationalConference
onControlApplications.vol.1.,221–226.
KITAGAWA,G. 1979. OntheuseofAICforthedetectionofoutliers.Technometrics21,2,193–199.
KNORR,E.M.ANDNG,R.T. 1997. Aunifiedapproachforminingoutliers.InProceedingsoftheConference
oftheCentreforAdvancedStudiesonCollaborativeResearch.IBMPress,11.
KNORR,E.M.ANDNG,R.T. 1998. Algorithmsforminingdistance-basedoutliersinlargedatasets.InPro-
ceedingsofthe24rdInternationalConferenceonVeryLargeDataBases.MorganKaufmannPublishers
Inc.,392–403.
KNORR, E. M. AND NG, R. T. 1999. Finding intensional knowledge of distance-based outliers. VLDB J.
211–222.
KNORR,E.M.,NG,R.T.,ANDTUCAKOV,V. 2000. Distance-basedoutliers:Algorithmsandapplications.VLDB
J.8,3-4,237–253.
KO,H.ANDJACYNA,G. 2000. Dynamicalbehaviorofautoassociativememoryperformingnoveltyfiltering.
InIEEETrans.NeuralNetw.Vol.11.1152–1161.
KOHONEN,T.,Ed. 1997. Self-OrganizingMaps.Springer-Verlag.
KOJIMA, K. AND ITO, K. 1999. Autonomous learning of novel patterns by utilizing chaotic dynamics. In
Proceedings of the IEEE International Conference on Systems, Man, and Cybernetics. Vol. 1. IEEE,
284–289.
KOSORESOW,A.P.ANDHOFMEYR,S.A. 1997. Intrusiondetectionviasystemcalltraces.IEEESoftw.14,5,
35–42.
KOU,Y.,LU,C.-T.,ANDCHEN,D. 2006. Spatialweightedoutlierdetection.InProceedingsoftheSIAMCon-
ferenceonDataMining.
KRUEGEL, C., MUTZ, D., ROBERTSON, W., AND VALEUR, F. 2003. Bayesian event classification for intrusion
detection.InProceedingsofthe19thAnnualComputerSecurityApplicationsConference.IEEEComputer
Society,14.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:52 V.Chandolaetal.
KRUEGEL,C.,TOTH,T.,ANDKIRDA,E. 2002. Servicespecificanomalydetectionfornetworkintrusiondetec-
tion.InProceedingsoftheACMsymposiumonAppliedComputing.ACMPress,201–208.
KRUEGEL,C.ANDVIGNA,G. 2003. AnomalydetectionofWeb-basedattacks.InProceedingsofthe10thACM
ConferenceonComputerandCommunicationsSecurity.ACMPress,251–261.
KUMAR,V. 2005. Parallelanddistributedcomputingforcybersecurity.IEEEDistrib.Syst.Online6,10.
LABIB,K.ANDVEMURI,R. 2002. NSOM:Areal-timenetwork-basedintrusiondetectionusingself-organizing
maps.Netw.Security.
LAKHINA, A., CROVELLA, M., AND DIOT, C. 2005. Mining anomalies using traffic feature distributions. In
ProceedingsoftheConferenceonApplications,Technologies,Architectures,andProtocolsforComputer
Communications.ACMPress,217–228.
LANE,T.ANDBRODLEY,C.E. 1997a. Anapplicationofmachinelearningtoanomalydetection.InProceedings
oftheConferenceon20thNIST-NCSCNationalInformationSystemsSecurityConference.366–380.
LANE,T.ANDBRODLEY,C.E. 1997b. Sequencematchingandlearninginanomalydetectionforcomputer
security.InProceedingsoftheConferenceonAIApproachestoFraudDetectionandRiskManagement,
Fawcett,Haimowitz,Provost,andStolfo,Eds.AAAIPress,43–49.
LANE,T.ANDBRODLEY,C.E. 1999. Temporalsequencelearninganddatareductionforanomalydetection.
ACMTrans.Inform.Syst.Secur.2,3,295–331.
LAUER,M. 2001. Amixtureapproachtonoveltydetectionusingtrainingdatawithoutliers.InProceedings
ofthe12thEuropeanConferenceonMachineLearning.Springer-Verlag,300–311.
LAURIKKALA,J.,JUHOLA,M.,ANDKENTALA.,E. 2000. Informalidentificationofoutliersinmedicaldata.In
Proceedingsofthe5thInternationalWorkshoponIntelligentDataAnalysisinMedicineandPharmacol-
ogy.20–24.
LAZAREVIC,A.,ERTOZ,L.,KUMAR,V.,OZGUR,A.,ANDSRIVASTAVA,J. 2003. Acomparativestudyofanomaly
detectionschemesinnetworkintrusiondetection.InProceedingsoftheSIAMInternationalConference
onDataMining.(SIAM).
LEE,W.ANDSTOLFO,S. 1998. Dataminingapproachesforintrusiondetection.InProceedingsofthe7th
USENIXSecuritySymposium.
LEE,W.,STOLFO,S.,ANDCHAN,P. 1997. LearningpatternsfromUNIXprocessexecutiontracesforintrusion
detection.InProceedingsoftheAAAIWorkshoponAIMethodsinFraudandRiskManagement.
LEE,W.,STOLFO,S.J.,ANDMOK,K.W. 2000. Adaptiveintrusiondetection:Adataminingapproach.Artif.
Intell.Rev.14,6,533–567.
LEE,W.ANDXIANG,D. 2001. Information-theoreticmeasuresforanomalydetection.InProceedingsofthe
IEEESymposiumonSecurityandPrivacy.IEEEComputerSociety,130.
LI,M.ANDVITANYI,P.M.B. 1993. AnIntroductiontoKolmogorovComplexityandItsApplications.Springer-
Verlag.
LI,Y.,PONT,M.J.,ANDJONES,N.B. 2002. Improvingtheperformanceofradialbasisfunctionclassifiers
inconditionmonitoringandfaultdiagnosisapplicationswhereunknownfaultsmayoccur.Patt.Recog.
Lett.23,5,569–577.
LIN, J., KEOGH, E., FU, A., AND HERLE, H. V. 2005. Approximations to magic: Finding unusual medical
timeseries.InProceedingsofthe18thIEEESymposiumonComputer-BasedMedicalSystems.IEEE
ComputerSociety,329–334.
LIN,S.ANDBROWN,D.E. 2003. Anoutlier-baseddataassociationmethodforlinkingcriminalincidents.In
Proceedingsofthe3rdSIAMDataMiningConference.
LIU,J.P.ANDWENG,C.S. 1991. Detectionofoutlyingdatainbioavailability/bioequivalencestudies.Stat.
Med.10,9,1375–89.
LU,C.-T.,CHEN,D.,ANDKOU,Y. 2003. Algorithmsforspatialoutlierdetection.InProceedingsofthe3rd
InternationalConferenceonDataMining.597–600.
MA, J. AND PERKINS, S. 2003a. Online novelty detection on temporal sequences. In Proceedings of the
9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM Press,
613–618.
MA,J.ANDPERKINS,S. 2003b. Time-seriesnoveltydetectionusingone-classsupportvectormachines.In
ProceedingsoftheInternationalJointConferenceonNeuralNetworks.Vol.3.1741–1745.
MACDONALD, J. W. AND GHOSH, D. 2007. Copa–cancer outlier profile analysis. Bioinformatics 22, 23,
2950–2951.
MAHONEY,M.V.ANDCHAN,P.K. 2002. Learningnonstationarymodelsofnormalnetworktrafficfordetecting
novelattacks.InProceedingsofthe8thACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining.ACMPress,376–385.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:53
MAHONEY, M. V. AND CHAN, P. K. 2003. Learning rules for anomaly detection of hostile network traffic.
In Proceedings of the 3rd IEEE International Conference on Data Mining. IEEE Computer Society,
601.
MAHONEY,M.V.,CHAN,P.K.,ANDARSHAD,M.H. 2003. Amachinelearningapproachtoanomalydetection.
Tech.rep.CS–2003–06,DepartmentofComputerScience,FloridaInstituteofTechnologyMelbourne.
MANEVITZ,L.M.ANDYOUSEF,M. 2000. Learningfrompositivedatafordocumentclassificationusingneural
networks.InProceedingsofthe2ndBar-IlanWorkshoponKnowledgeDiscoveryandLearning.
MANEVITZ,L.M.ANDYOUSEF,M. 2002. One-classSVMSfordocumentclassification.J.Mach.Learn.Res.2,
139–154.
MANIKOPOULOS,C.ANDPAPAVASSILIOU,S. 2002. Networkintrusionandfaultdetection:Astatisticalanomaly
approach.IEEEComm.Mag.40.
MANSON,G. 2002. Identifyingdamagesensitive,environmentinsensitivefeaturesfordamagedetection.
InProceedingsofIESConference.
MANSON,G.,PIERCE,G.,ANDWORDEN,K. 2001. Onthelong-termstabilityofnormalconditionsfordamage
detectioninacompositepanel.InProceedingsofthe4thInternationalConferenceonDamageAssessment
ofStructures.Cardiff,UK.
MANSON,G.,PIERCE,S.G.,WORDEN,K.,MONNIER,T.,GUY,P.,ANDATHERTON,K. 2000. Long-termstabilityof
normalconditiondatafornoveltydetection.InProceedingsoftheConferenceonSmartStructuresand
IntegratedSystems.323–334.
MARCEAU,C. 2000. Characterizingthebehaviorofaprogramusingmultiple-lengthn-grams.InProceedings
oftheWorkshoponNewSecurityParadigms.ACMPress,101–110.
MARCHETTE,D. 1999. Astatisticalmethodforprofilingnetworktraffic.InProceedingsofthe1stUSENIX
WorkshoponIntrusionDetectionandNetworkMonitoring.119–128.
MARKOU, M. AND SINGH, S. 2003a. Novelty detection: A review-part 1: Statistical approaches. Sig.
Proc.83,12,2481–2497.
MARKOU,M.ANDSINGH,S. 2003b. Noveltydetection:Areview-part2:Neuralnetworkbasedapproaches.
Sig.Proc.83,12,2499–2521.
MARSLAND,S.,NEHMZOW,U.,ANDSHAPIRO,J. 1999. Amodelofhabituationappliedtomobilerobots.InPro-
ceedingsofTowardsIntelligentMobileRobotsConference.DepartmentofComputerScience,Manchester
University,Technicalrep.UMCS-99-3-1.
MARSLAND,S.,NEHMZOW,U.,ANDSHAPIRO,J. 2000a. Noveltydetectionforrobotneotaxis.InProceedingsof
the2ndInternationalSymposiumonNeuralCompuatation.554–559.
MARSLAND, S., NEHMZOW, U., AND SHAPIRO, J. 2000b. A real-time novelty detector for a mobile robot. In
ProceedingsoftheEURELConferenceonAdvancedRoboticsSystems.
MARTINELLI, G. AND PERFETTI, R. 1994. Generalized cellular neural network for novelty detection. IEEE
Trans.Circ.Syst.I:FundamentalTheoryApplication41,2,187–190.
MARTINEZ,D. 1998. Neuraltreedensityestimationfornoveltydetection.IEEETrans.NeuralNetw.9,2,
330–338.
MCCALLUM,A.,NIGAM,K.,ANDUNGAR,L.H. 2000. Efficientclusteringofhigh-dimensionaldatasetswith
applicationtoreferencematching.InProceedingsofthe6thACMSIGKDDInternationalConferenceon
KnowledgeDiscoveryandDataMining.ACMPress,169–178.
MCNEIL,A. 1999. Extremevaluetheoryforriskmanagers.InInternalModellingandCADII,93–113.
MINGMING,N.Y. 2000. Probabilisticnetworkswithundirectedlinksforanomalydetection.InProceedings
oftheIEEESystems,Man,andCyberneticsInformationAssuranceandSecurityWorkshop.175–179.
MOTULSKY, H. 1995. Intuitive Biostatistics: Choosing a Statistical Test. Oxford University Press, Chap-
ter37.
MOYA,M.,KOCH,M.,ANDHOSTETLER,L. 1993. One-classclassifiernetworksfortargetrecognitionapplica-
tions.InProceedingsoftheWorldCongressonNeuralNetworks,InternationalNeuralNetworkSociety.
797–801.
MURRAY,A.F. 2001. Noveltydetectionusingproductsofsimpleexperts:Apotentialarchitectureforem-
beddedsystems.NeuralNetw.14,9,1257–1264.
NAIRAC,A.,CORBETT-CLARK,T.,RIPLEY,R.,TOWNSEND,N.,ANDTARASSENKO,L. 1997. Choosinganappropriate
modelfornoveltydetection.InProceedingsofthe5thIEEEInternationalConferenceonArtificialNeural
Networks.227–232.
NAIRAC,A.,TOWNSEND,N.,CARR,R.,KING,S.,COWLEY,P.,ANDTARASSENKO,L. 1999. Asystemfortheanalysis
ofjetenginevibrationdata.Integ.Comput.-AidedEng.6,1,53–56.
NG,R.T.ANDHAN,J. 1994. Efficientandeffectiveclusteringmethodsforspatialdatamining.InProceedings
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:54 V.Chandolaetal.
of the 20th International Conference on Very Large Data Bases. Morgan Kaufmann Publishers Inc.,
144–155.
NOBLE,C.C.ANDCOOK,D.J. 2003. Graph-basedanomalydetection.InProceedingsofthe9thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining.ACMPress,631–636.
ODIN,T.ANDADDISON,D. 2000. Noveltydetectionusingneuralnetworktechnology.InProceedingsofthe
COMADENConference.
OTEY,M.,PARTHASARATHY,S.,GHOTING,A.,LI,G.,NARRAVULA,S.,ANDPANDA,D. 2003. TowardsNIC-based
intrusion detection. In Proceedings of the 9th ACM SIGKDD International Conference on Knowledge
DiscoveryandDataMining.ACMPress,723–728.
OTEY,M.E.,GHOTING,A.,ANDPARTHASARATHY,S. 2006. Fastdistributedoutlierdetectioninmixed-attribute
datasets.DataMin.Knowl.Disc.12,2-3,203–228.
PALSHIKAR,G.K. 2005. Distance-basedoutliersinsequences.LectureNotesinComputerScience,vol.3816,
547–552.
PAPADIMITRIOU,S.,KITAGAWA,H.,GIBBONS,P.B.,ANDFALOUTSOS,C. 2002. Loci:Fastoutlierdetectionusing
thelocalcorrelationintegral.Tech.rep.IRP-TR-02-09,IntelResearchLaboratory.
PARRA,L.,DECO,G.,ANDMIESBACH,S. 1996. Statisticalindependenceandnoveltydetectionwithinformation
preservingnonlinearmaps.NeuralComput.8,2,260–269.
PARZEN,E. 1962. Ontheestimationofaprobabilitydensityfunctionandmode.AnnalsMath.Stat.33,
1065–1076.
PATCHA, A. AND PARK, J.-M. 2007. An overview of anomaly detection techniques: Existing solutions and
latesttechnologicaltrends.Comput.Netw.51,12,3448–3470.
PETSCHE,T.,MARCANTONIO,A.,DARKEN,C.,HANSON,S.,KUHN,G.,ANDSANTOSO,I. 1996. Aneuralnetwork
autoassociatorforinductionmotorfailureprediction.InProceedingsoftheConferenceonAdvancesin
NeuralInformationProcessing.vol.8.924–930.
PHOHA,V.V. 2002. TheSpringerInternetSecurityDictionary.Springer-Verlag.
PHUA, C., ALAHAKOON, D., AND LEE, V. 2004. Minority report in fraud detection: Classification of skewed
data.SIGKDDExplorerNewsletter6,1,50–59.
PHUONG,T.V.,HUNG,L.X.,CHO,S.J.,LEE,Y.,ANDLEE,S. 2006. Ananomalydetectionalgorithmfordetecting
attacksinwirelesssensornetworks.Intel.Secur.Inform.3975,735–736.
PICKANDS,J. 1975. Statisticalinferenceusingextremeorderstatistics.AnnalsStat.3,1,119–131.
PIRES,A.ANDSANTOS-PEREIRA,C. 2005. Usingclusteringandrobustestimatorstodetectoutliersinmulti-
variatedata.InProceedingsoftheInternationalConferenceonRobustStatistics.
PLATT,J. 2000. ProbabilisticOutputsforSupportVectorMachinesandComparisontoRegularizedLike-
lihood Methods. In Advances in Large Margin Classifiers, A. Smola, P. Bartlett, B. Schoelkopf, and
D.Schuurmans,Eds.MITPress,61–74.
POKRAJAC,D.,LAZAREVIC,A.,ANDLATECKI,L.J. 2007. Incrementallocaloutlierdetectionfordatastreams.
InProceedingsoftheIEEESymposiumonComputationalIntelligenceandDataMining.
PORRAS,P.A.ANDNEUMANN,P.G. 1997. EMERALD:Eventmonitoringenablingresponsestoanomalouslive
disturbances.InProceedingsofthe20thNIST-NCSCNationalInformationSystemsSecurityConference.
353–365.
PORTNOY,L.,ESKIN,E.,ANDSTOLFO,S. 2001. Intrusiondetectionwithunlabeleddatausingclustering.In
ProceedingsoftheACMWorkshoponDataMiningAppliedtoSecurity.
PROTOPAPAS,P.,GIAMMARCO,J.M.,FACCIOLI,L.,STRUBLE,M.F.,DAVE,R.,ANDALCOCK,C. 2006. Findingoutlier
lightcurvesincataloguesofperiodicvariablestars.MonthlyNoticesRoyalAstronomicalSoc.369,2,
677–696.
QIN,M.ANDHWANG,K. 2004. FrequentepisoderulesforInternetanomalydetection.InProceedingsofthe
3rdIEEEInternationalSymposiumonNetworkComputingandApplications.IEEEComputerSociety.
RAMADAS, M., OSTERMANN, S., AND TJADEN, B. C. 2003. Detecting anomalous network traffic with self-
organizing maps. In Proceedings of the Conference on Recent Advances in Intrusion Detection.
36–54.
RAMASWAMY,S.,RASTOGI,R.,ANDSHIM,K. 2000. Efficientalgorithmsforminingoutliersfromlargedata
sets.InProceedingsoftheACMSIGMODInternationalConferenceonManagementofData.ACMPress,
427–438.
RATSCH,G.,MIKA,S.,SCHOLKOPF,B.,ANDMULLER,K.-R. 2002. ConstructingboostingalgorithmsfromSVMS:
Anapplicationtoone-classclassification.IEEETrans.Patt.Anal.Mach.Intel.24,9,1184–1199.
ROBERTS, S. 1999. Novelty detection using extreme value statistics. In Proceedings of the IEEE Vision,
ImageandSignalProcessingConferenceVol.146.124–129.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:55
ROBERTS,S. 2002. Extremevaluestatisticsfornoveltydetectioninbiomedicalsignalprocessing.InPro-
ceedingsofthe1stInternationalConferenceonAdvancesinMedicalSignalandInformationProcessing.
166–172.
ROBERTS, S. AND TARASSENKO, L. 1994. A probabilistic resource allocating network for novelty detection.
NeuralComput.6,2,270–284.
ROSNER,B. 1983. PercentagepointsforageneralizedESDmany-outlierprocedure.Technometrics25,2,
165–172.
ROTH,V. 2004. Outlierdetectionwithone-classkernelFisherdiscriminants.InProceedingsoftheConfer-
enceonAdvancesinNeuralInformationProcessingSystems(NIPS).
ROTH,V. 2006. Kernelfisherdiscriminantsforoutlierdetection.NeuralComput.18,4,942–960.
ROUSSEEUW,P.J.ANDLEROY,A.M. 1987. RobustRegressionandOutlierDetection.JohnWiley&Sons,Inc.
ROUSSOPOULOS,N.,KELLEY,S.,ANDVINCENT,F. 1995. Nearestneighborqueries.InProceedingsoftheACM-
SIGMODInternationalConferenceonManagementofData.
RUOTOLO,R.ANDSURACE,C. 1997. Astatisticalapproachtodamagedetectionthroughvibrationmonitoring.
InProceedingsofthe5thPan-AmericanCongressofAppliedMechanics.
SALVADOR,S.ANDCHAN,P. 2003. Learningstatesandrulesfortime-seriesanomalydetection.Tech.rep.
CS–2003–05,DepartmentofComputerScience,FloridaInstituteofTechnologyMelbourne.
SARAWAGI, S., AGRAWAL, R., AND MEGIDDO, N. 1998. Discovery-driven exploration of OLAP data cubes. In
Proceedings of the 6th International Conference on Extending Database Technology. Springer-Verlag,
168–182.
SARGOR,C. 1998. Statisticalanomalydetectionforlink-stateroutingprotocols.InProceedingsofthe6th
InternationalConferenceonNetworkProtocols.IEEEComputerSociety,62.
SAUNDERS,R.ANDGERO,J. 2000. Theimportanceofbeingemergent.InProceedingsoftheConferenceon
ArtificialIntelligenceinDesign.
SCARTH,G.,MCINTYRE,M.,WOWK,B.,ANDSOMORJAI,R. 1995. Detectionofnoveltyinfunctionalimagesusing
fuzzyclustering.InProceedingsofthe3rdMeetingoftheInternationalSocietyforMagneticResonance
inMedicine.238.
SCHO¨LKOPF,B.,PLATT,J.C.,SHAWE-TAYLOR,J.C.,SMOLA,A.J.,ANDWILLIAMSON,R.C. 2001. Estimatingthe
supportofahigh-dimensionaldistribution.NeuralComput.13,7,1443–1471.
SCOTT,S.L. 2001. DetectingnetworkintrusionusingaMarkovmodulatednonhomogeneousPoissonPro-
cess.JournaloftheAmericanStatisticalAssociation.
SEBYALA, A. A., OLUKEMI, T., AND SACKS, L. 2002. Active platform security through intrusion detection
using naive Bayesian network for anomaly detection. In Proceedings of the London Communications
Symposium.
SEQUEIRA,K.ANDZAKI,M. 2002. Admit:Anomaly-baseddataminingforintrusions.InProceedingsofthe
8th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM Press,
386–395.
SHEIKHOLESLAMI, G., CHATTERJEE, S., AND ZHANG, A. 1998. Wavecluster: A multi-resolution clustering ap-
proach for very large spatial databases. In Proceedings of the 24rd International Conference on Very
LargeDatabases.MorganKaufmannPublishersInc.,428–439.
SHEKHAR,S.,LU,C.-T.,ANDZHANG,P. 2001. Detectinggraph-basedspatialoutliers:Algorithmsandappli-
cations (a summary of results). In Proceedings of the 7th ACM SIGKDD International Conference on
KnowledgeDiscoveryandDataMining.ACMPress,371–376.
SHEWHART,W.A. 1931. EconomicControlofQualityofManufacturedProduct.D.VanNostrandCompany.
SHYU,M.-L.,CHEN,S.-C.,SARINNAPAKORN,K.,ANDCHANG,L. 2003. Anovelanomalydetectionscheme-based
on principal component classifier. In Proceedings of the 3rd IEEE International Conference on Data
Mining.353–365.
SIATERLIS,C.ANDMAGLARIS,B. 2004. Towardsmulti-sensordatafusionfordosdetection.InProceedingsof
theACMSymposiumonAppliedComputing.ACMPress,439–446.
SINGH,S.ANDMARKOU,M. 2004. Anapproachtonoveltydetectionappliedtotheclassificationofimage
regions.IEEETrans.Knowl.DataEng.16,4,396–407.
SMITH, R., BIVENS, A., EMBRECHTS, M., PALAGIRI, C., AND SZYMANSKI, B. 2002. Clustering approaches for
anomaly-basedintrusiondetection.InProceedingsoftheIntelligentEngineeringSystemsthroughArti-
ficialNeuralNetworks.ASMEPress,579–584.
SMYTH,P. 1994. Markovmonitoringwithunknownstates.IEEEJ.Select.AreasComm.(SpecialIssueon
IntelligentSignalProcessingforCommunications)12,9,1600–1612.
SNYDER,D. 2001. Onlineintrusiondetectionusingsequencesofsystemcalls.M.S.thesis,Departmentof
ComputerScience,FloridaStateUniversity.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:56 V.Chandolaetal.
SOHN,H.,WORDEN,K.,ANDFARRAR,C. 2001. Noveltydetectionunderchangingenvironmentalconditions.
InProceedingsofthe8thAnnualSPIEInternationalSymposiumonSmartStructuresandMaterials.
SOLBERG,H.E.ANDLAHTI,A. 2005. Detectionofoutliersinreferencedistributions:PerformanceofHorn’s
algorithm.ClinicalChem.51,12,2326–2332.
SONG,Q.,HU,W.,ANDXIE,W. 2002. Robustsupportvectormachinewithbulletholeimageclassification.
IEEETrans.Syst.ManCyber.—PartC:ApplicationsandReviews32,4.
SONG,S.,SHIN,D.,ANDYOON,E. 2001. Analysisofnoveltydetectionpropertiesofauto-associators.InPro-
ceedingsoftheConferenceonConditionMonitoringandDiagnosticEngineeringManagement.577–584.
SONG,X.,WU,M.,JERMAINE,C.,ANDRANKA,S. 2007. Conditionalanomalydetection.IEEETrans.Knowl.
DataEng.19,5,631–645.
SOULE, A., SALAMATIAN, K., AND TAFT, N. 2005. Combining filtering and statistical methods for anomaly
detection. In Proceedings of the 5th ACM SIGCOMM Conference on Internet Measurement. ACM,
1–14.
SPENCE,C.,PARRA,L.,ANDSAJDA,P. 2001. Detection,synthesisandcompressioninmammographicimage
analysiswithahierarchicalimageprobabilitymodel.InProceedingsoftheIEEEWorkshoponMathe-
maticalMethodsinBiomedicalImageAnalysis.IEEEComputerSociety,3.
SRIVASTAVA, A. 2006. Enabling the discovery of recurring anomalies in aerospace problem reports using
high-dimensionalclusteringtechniques.InProceedingsoftheIEEEAerospaceConference,17–34.
SRIVASTAVA,A.ANDZANE-ULMAN,B.2005.Discoveringrecurringanomaliesintextreportsregardingcomplex
spacesystems.InProceedingsoftheIEEEAerospaceConference,3853–3862.
STEFANO,C.,SANSONE,C.,ANDVENTO,M. 2000. Torejectornottoreject:thatisthequestion:Ananswerin
thecaseofneuralclassifiers.IEEETrans.Syst.Manag.Cyber.30,1,84–94.
STEFANSKY,W. 1972. Rejectingoutliersinfactorialdesigns.Technometrics14,2,469–479.
STEINWART,I.,HUSH,D.,ANDSCOVEL,C. 2005. Aclassificationframeworkforanomalydetection.J.Mach.
Learn.Res.6,211–232.
STREIFEL, R., MAKS, R., AND EL-SHARKAWI, M. 1996. Detection of shorted-turns in the field of turbine-
generatorrotorsusingnoveltydetectors–developmentandfieldtests.IEEETrans.EnergyConv.11,2,
312–317.
SUBRAMANIAM,S.,PALPANAS,T.,PAPADOPOULOS,D.,KALOGERAKI,V.,ANDGUNOPULOS,D. 2006. Onlineoutlierde-
tectioninsensordatausingnon-parametricmodels.InProceedingsofthe32ndInternationalConference
onVeryLargeDataBases(VLDB).VLDBEndowment,187–198.
SUN,H.,BAO,Y.,ZHAO,F.,YU,G.,ANDWANG,D. 2004. CD-trees:Anefficientindexstructureforoutlierdetec-
tion.InProceedingsofthe5thInternationalConferenceonWeb-AgeInformationManagement(WAIM).
600–609.
SUN,J.,QU,H.,CHAKRABARTI,D.,ANDFALOUTSOS,C. 2005. Neighborhoodformationandanomalydetection
in bipartite graphs. In Proceedings of the 5th IEEE International Conference on Data Mining. IEEE
ComputerSociety,418–425.
SUN,J.,XIE,Y.,ZHANG,H.,ANDFALOUTSOS,C. 2007. Lessismore:Compactmatrixrepresentationoflarge
sparsegraphs.InProceedingsofthe7thSIAMInternationalConferenceonDataMining.
SUN,P.ANDCHAWLA,S. 2004. Onlocalspatialoutliers.InProceedingsofthe4thIEEEInternationalCon-
ferenceonDataMining.209–216.
SUN,P.ANDCHAWLA,S. 2006. SLOM:Anewmeasureforlocalspatialoutliers.Knowl.Inform.Syst.9,4,
412–429.
SUN,P.,CHAWLA,S.,ANDARUNASALAM,B. 2006. Miningforoutliersinsequentialdatabases.InProceedings
oftheSIAMInternationalConferenceonDataMining.
SURACE,C.ANDWORDEN,K. 1998. Anoveltydetectionmethodtodiagnosedamageinstructures:Anappli-
cationtoanoffshoreplatform.InProceedingsofthe8thInternationalConferenceofOff-ShoreandPolar
Engineering.vol.4.Colorado,64–70.
SURACE,C.,WORDEN,K.,ANDTOMLINSON,G. 1997. Anoveltydetectionapproachtodiagnosedamageina
crackedbeam.InProceedingsoftheSPIE.vol.3089.947–953.
SUZUKI,E.,WATANABE,T.,YOKOI,H.,ANDTAKABAYASHI,K. 2003. Detectinginterestingexceptionsfrommed-
icaltestdatawithvisualsummarization.InProceedingsofthe3rdIEEEInternationalConferenceon
DataMining.315–322.
SYKACEK,P. 1997. EquivalenterrorbarsforneuralnetworkclassifierstrainedbyBayesianinference.In
ProceedingsoftheEuropeanSymposiumonArtificialNeuralNetworks.121–126.
TAN,P.-N.,STEINBACH,M.,ANDKUMAR,V. 2005. IntroductiontoDataMining.Addison-Wesley.
TANDON,G.ANDCHAN,P. 2007. Weightingversuspruninginrulevalidationfordetectingnetworkandhost
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

AnomalyDetection:ASurvey 15:57
anomalies.InProceedingsofthe13thACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining.ACMPress.
TANG,J.,CHEN,Z.,CHEEFU,A.W.,ANDW.CHEUNG,D. 2002. Enhancingeffectivenessofoutlierdetections
forlowdensitypatterns.InProceedingsofthePacific-AsiaConferenceonKnowledgeDiscoveryandData
Mining.535–548.
TANIGUCHI,M.,HAFT,M.,HOLLMN,J.,ANDTRESP,V. 1998. Frauddetectionincommunicationsnetworksusing
neural and probabilistic methods. In Proceedings of the IEEE International Conference on Acoustics,
SpeechandSignalProcessing.vol.2.IEEEComputerSociety,1241–1244.
TAO,Y.,XIAO,X.,ANDZHOU,S. 2006. Miningdistance-basedoutliersfromlargedatabasesinanymetric
space.InProceedingsofthe12thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryand
DataMining.ACMPress,394–403.
TARASSENKO,L. 1995. Noveltydetectionfortheidentificationofmassesinmammograms.InProceedings
ofthe4thIEEEInternationalConferenceonArtificialNeuralNetworks.vol.4.442–447.
TAX,D.ANDDUIN,R. 1999a. Datadomaindescriptionusingsupportvectors.InProceedingsoftheEuropean
SymposiumonArtificialNeuralNetworks,M.Verleysen,Ed.,251–256.
TAX,D.ANDDUIN,R. 1999b. Supportvectordatadescription.Patt.Recog.Lett.20,11-13,1191–1199.
TAX,D.M.J. 2001. One-classclassification;concept-learningintheabsenceofcounter-examples.Ph.D.
thesis,DelftUniversityofTechnology.
TENG,H.,CHEN,K.,ANDLU,S. 1990. Adaptivereal-timeanomalydetectionusinginductivelygenerated
sequentialpatterns.InProceedingsoftheIEEEComputerSocietySymposiumonResearchinSecurity
andPrivacy.IEEEComputerSocietyPress,278–284.
THEILER,J.ANDCAI,D.M. 2003. Resamplingapproachforanomalydetectioninmultispectralimages.In
ProceedingsoftheSPIE.vol.5093,230–240.
THOMPSON,B.,II,R.M.,CHOI,J.,EL-SHARKAWI,M.,HUANG,M.,ANDBUNJE,C. 2002. Implicitlearninginauto-
encodernoveltyassessment.InProceedingsoftheInternationalJointConferenceonNeuralNetworks.
2878–2883.
THOTTAN, M. AND JI, C. 2003. Anomaly detection in IP networks. IEEE Trans. Sig. Proc. 51, 8,
2191–2204.
TIBSHIRANI,R.ANDHASTIE,T. 2007. Outliersumsfordifferentialgeneexpressionanalysis.Biostatistics8,1,
2–8.
TOMLINS,S.A.,RHODES,D.R.,PERNER,S.,DHANASEKARAN,S.M.,MEHRA,R.,SUN,X.W.,VARAMBALLY,S.,CAO,
X., TCHINDA, J., KUEFER, R., LEE, C., MONTIE, J. E., SHAH, R., PIENTA, K. J., RUBIN, M., AND CHINNAIYAN,
A.M. 2005. Recurrentfusionoftmprss2andetstranscriptionfactorgenesinprostatecancer.Sci-
ence310,5748,603–611.
TORR, P. AND MURRAY, D. 1993. Outlier detection and motion segmentation. In Proceedings of the SPIE.
SensorFusionVI,S.Schenker,Ed.vol.2059.432–443.
TSAY, R. S., PEA, D., AND PANKRATZ, A. E. 2000. Outliers in multi-variate time series. Biometrika 87, 4,
789–804.
VAIDYA,J.ANDCLIFTON,C. 2004. Privacy-preservingoutlierdetection.InProceedingsofthe4thIEEEInter-
nationalConferenceonDataMining.233–240.
VALDES, A. AND SKINNER, K. 2000. Adaptive, model-based monitoring for cyber attack detection. In Pro-
ceedingsofthe3rdInternationalWorkshoponRecentAdvancesinIntrusionDetection.Springer-Verlag,
80–92.
VAPNIK,V.N. 1995. TheNatureofStatisticalLearningTheory.Springer-Verlag.
VASCONCELOS,G.,FAIRHURST,M.,ANDBISSET,D. 1994. Recognizingnoveltyinclassificationtasks.InProceed-
ingsoftheNeuralInformationProcessingSystemsWorkshoponNoveltyDetectionandAdaptiveSystems
Monitoring.
VASCONCELOS,G.C.,FAIRHURST,M.C.,ANDBISSET,D.L. 1995. Investigatingfeed-forwardneuralnetworks
withrespecttotherejectionofspuriouspatterns.Patt.Recog.Lett.16,2,207–212.
VILALTA, R. AND MA, S. 2002. Predicting rare events in temporal domains. In Proceedings of the IEEE
InternationalConferenceonDataMining.IEEEComputerSociety,474.
VINUEZA,A.ANDGRUDIC,G. 2004. Unsupervisedoutlierdetectionandsemi-supervisedlearning.Tech.rep.
CU-CS-976-04,UniversityofColoradoatBoulder.
WEI,L.,QIAN,W.,ZHOU,A.,ANDJIN,W. 2003. Hot:Hypergraph-basedoutliertestforcategoricaldata.In
Proceedingsofthe7thPacific-AsiaConferenceonKnowledgeandDataDiscovery.399–410.
WEIGEND,A.S.,MANGEAS,M.,ANDSRIVASTAVA,A.N. 1995. Nonlineargatedexpertsfortime-series:Discov-
eringregimesandavoidingoverfitting.Int.J.NeuralSyst.6,4,373–399.
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.

15:58 V.Chandolaetal.
WEISS,G.M.ANDHIRSH,H. 1998. Learningtopredictrareeventsineventsequences.InProceedingsof
the4thInternationalConferenceonKnowledgeDiscoveryandDataMining,R.Agrawal,P.Stolorz,and
G.Piatetsky-Shapiro,Eds.AAAIPress,359–363.
WHITEHEAD,B.ANDHOYT,W. 1993. Afunctionapproximationapproachtoanomalydetectioninpropulsion
system test data. In Proceedings of the 29th AIAA/SAE/ASME/ASEE Joint Propulsion Conference.
IEEEComputerSociety.
WILLIAMS,G.,BAXTER,R.,HE,H.,HAWKINS,S.,ANDGU,L. 2002. AcomparativestudyofRNNforoutlier
detectionindatamining.InProceedingsoftheIEEEInternationalConferenceonDataMining.IEEE
ComputerSociety,709.
WONG, W.-K., MOORE, A., COOPER, G., AND WAGNER, M. 2002. Rule-based anomaly pattern detection for
detectingdiseaseoutbreaks.InProceedingsofthe18thNationalConferenceonArtificialIntelligence.
MITPress.http://www.cs.cmu.edu/simawm/antiterror.
WONG,W.-K.,MOORE,A.,COOPER,G.,ANDWAGNER,M. 2003. Bayesiannetworkanomalypatterndetection
fordiseaseoutbreaks.InProceedingsofthe20thInternationalConferenceonMachineLearning.AAAI
Press,808–815.
WORDEN,K. 1997. Structuralfaultdetectionusinganoveltymeasure.J.SoundVibr.201,1,85–101.
WU,M.ANDJERMAINE,C. 2006. Outlierdetectionbysamplingwithaccuracyguarantees.InProceedings
ofthe12thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,
767–772.
WU,N.ANDZHANG,J. 2003. Factoranalysisbasedanomalydetection.InProceedingsoftheIEEEWorkshop
onInformationAssurance.UnitedStatesMilitaryAcademy.
YAIRI,T.,KATO,Y.,ANDHORI,K. 2001. Faultdetectionbyminingassociationrulesfromhousekeepingdata.
InProceedingsoftheInternationalSymposiumonArtificialIntelligence,RoboticsandAutomationin
Space.
YAMANISHI,K.ANDICHITAKEUCHI,J. 2001. Discoveringoutlierfilteringrulesfromunlabeleddata:Combining
asupervisedlearnerwithanunsupervisedlearner.InProceedingsofthe7thACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining.ACMPress,389–394.
YAMANISHI, K., TAKEUCHI, J.-I., WILLIAMS, G., AND MILNE, P. 2004. Online unsupervised outlier de-
tection using finite mixtures with discounting learning algorithms. Data Min. Knowl. Disc. 8,
275–300.
YE,N.ANDCHEN,Q. 2001. Ananomalydetectiontechniquebasedonachi-squarestatisticfordetecting
intrusionsintoinformationsystems.QualityReliabilityEngin.Int.17,105–112.
YI,B.-K.,SIDIROPOULOS,N.,JOHNSON,T.,JAGADISH,H.V.,FALOUTSOS,C.,ANDBILIRIS,A. 2000. Onlinedata
mining for co-evolving time sequences. In Proceedings of the 16th International Conference on Data
Engineering.IEEEComputerSociety,13.
YPMA,A.ANDDUIN,R. 1998. Noveltydetectionusingself-organizingmaps.InProgressinConnectionist
BasedInformationSystems.vol.2.Springer,1322–1325.
YU,D.,SHEIKHOLESLAMI,G.,ANDZHANG,A. 2002. Findout:Findingoutliersinverylargedatasets.Knowl.
Inform.Syst.4,4,387–412.
YU,J.X.,QIAN,W.,LU,H.,ANDZHOU,A. 2006. Findingcentriclocaloutliersincategorical/numericalspaces.
Knowl.Inform.Syst.9,3,309–338.
ZEEVI,A.J.,MEIR,R.,ANDADLER,R. 1997. Timeseriespredictionusingmixturesofexperts.InAdvances
inNeuralInformationProcessing.vol.9.MITPress.
ZHANG, J. AND WANG, H. 2006. Detecting outlying subspaces for high-dimensional data: The new task,
algorithms,andperformance.Knowl.Inform.Syst.10,3,333–355.
ZHANG,K.,SHIS.,GAO,H.,ANDLI,J. 2007. Unsupervisedoutlierdetectioninsensornetworksusingaggre-
gationtree.InAdvancedDataMiningandApplications4632,158–169.
ZHANG,Z.,LI,J.,MANIKOPOULOS,C.,JORGENSON,J.,ANDUCLES,J. 2001. Hide:Ahierarchicalnetworkintrusion
detectionsystemusingstatisticalpreprocessingandneuralnetworkclassification.InProceedingsofthe
IEEEWorkshoponInformationAssuranceandSecurity.WestPoint,85–90.
ZIMMERMANN,J.ANDMOHAY,G. 2006. Distributedintrusiondetectioninclustersbasedonnon-interference.
InProceedingsoftheAustralasianWorkshopsonGridComputingandE-Research(ACSWFrontiers).
AustralianComputerSociety,Inc.,89–95.
ReceivedNovember2007;revisedMarch2008;acceptedMay2008
ACMComputingSurveys,Vol.41,No.3,Article15,Publicationdate:July2009.