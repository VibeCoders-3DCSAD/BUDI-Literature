---
conversion_metadata:
  converted_at: "2026-10-12T07:25:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Haraty & Bader, 2025.pdf"
  source_pdf_sha256: "19cd635a53f514dfddeeac3e6e39f1ca872b79064912a11bf40d7593af9e9752"
  page_count: 19
  markdown_char_count: 147314
---

|     |     |     |     |     |     |     | International |     | Journal |     | of Computing |            | and Digital | Systems |      |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | ------------ | ---------- | ----------- | ------- | ---- |
|     |     |     |     |     |     |     |               |     |         |     |              | 2025, VOL. | 18,         | NO. 1,  | 1–19 |
http://dx.doi.org/10.12785/ijcds/1571107231
| Bridging |     |     | AI  | and     | Emotion: |         | Enhanced |       |              | Models  |     | for | Personal |     |     |
| -------- | --- | --- | --- | ------- | -------- | ------- | -------- | ----- | ------------ | ------- | --- | --- | -------- | --- | --- |
|          |     |     |     | Finance |          | Manager |          |       | Applications |         |     |     |          |     |     |
|          |     |     |     |         | Samir    | Bader   | 1 and    | Ramzi | A.           | Haraty2 |     |     |          |     |     |
1 Department of Computer Science and Mathematics, Lebanese American University, Beirut, Lebanon
|     |     |     | Received |     | 6 June | 2024, Revised | 22  | March | 2025, | Accepted | 22 March | 2025 |     |     |     |
| --- | --- | --- | -------- | --- | ------ | ------------- | --- | ----- | ----- | -------- | -------- | ---- | --- | --- | --- |
Abstract: paper focuses on creating and deploying an innovative Financial Advisor Application that would revolutionize conventional
financial planning methods with the help of state-of-the-art artificial intelligence tools and effective financial services. Indeed, the
essence of this application is user-oriented and focuses on creating more ways to engage the user and help make the right decisions
different
by redesigning the interface and providing individualized financial guidance. The application combines aspects of financial
management,includingbudgeting,transactiontracking,andgoalsetting,butalsoseesnoveltiesasanartificialintelligencefunctionthat
offers
detects anomalies in transactions and the merchant explicitly created for clients. The technical structure involves access to data,
thedescriptionofeachmodule,andtheuseofAIthatprovidesanticipatoryanalysisandtoolsforadvancedfinancialplanning.Business
testing and vulnerability assessments were performed proving the business value and reliability of the application; thus, avoiding data
leakage and modularity viruses. The work assesses the effects on the users’ satisfaction when provided with such technologies and
their ability to change their financial management behaviour; therefore, providing an exhaustive scenario of the credentials of AI for
efficacy
improving the of financial advisory. The conclusions released in the paper should advance knowledge of financial technology
as it demonstrates how the intelligent systems used in a presented application can lead to noteworthy improvements for both users and
financial companies.
| Keywords:       | AI, Anomaly |           | Detection,  | Financial      |              | Planning, | Fintech, | and Sentiment |         | Analysis |              |                |     |           |        |
| --------------- | ----------- | --------- | ----------- | -------------- | ------------ | --------- | -------- | ------------- | ------- | -------- | ------------ | -------------- | --- | --------- | ------ |
| 1. INTRODUCTION |             |           |             |                |              |           |          | users.        |         |          |              |                |     |           |        |
| The             | Financial   | Advisor   | Application |                | is a         | perfect   | example  |               |         |          |              |                |     |           |        |
|                 |             |           |             |                |              |           |          |               | Also,   | constant | transactions | are controlled |     | by the    | appli- |
| of the synergy  |             | of highly | developed   |                | IT solutions |           | and pro- |               |         |          |              |                |     |           |        |
|                 |             |           |             |                |              |           |          | cation        | through | highly   | developed    | anomaly        |     | detection | algo-  |
| found financial |             | knowledge | in          | the constantly |              | evolving  | field    |               |         |          |              |                |     |           |        |
of fintech. This application revolutionizes personal finance rithms. This security feature quickly detects any suspicious
|     |     |     |     |     |     |     |     | activity | associated |     | with fraudulent |     | activities; | thus, | protect- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------------- | --- | ----------- | ----- | -------- |
managementbyutilizingadvancedAIalongwithaplethora
ingusers’financialresources.Theanomalydetectionability
| of financial | products     |             | and services  |     | that are | unique   | to the   |          |     |           |          |               |        |             |     |
| ------------ | ------------ | ----------- | ------------- | --- | -------- | -------- | -------- | -------- | --- | --------- | -------- | ------------- | ------ | ----------- | --- |
|              |              |             |               |     |          |          |          | protects |     | the money | and      | makes users   | aware  | of standard |     |
| clients.     | Unlike       | traditional | instruments   |     | that     | work     | indepen- |          |     |           |          |               |        |             |     |
|              |              |             |               |     |          |          |          | spending |     | patterns  | to avoid | risking their | money. |             |     |
| dently of    | one another, |             | this platform |     | offers   | a global | picture  |          |     |           |          |               |        |             |     |
ofaperson’sfinancialstatusandprovidesrecommendations
|     |     |     |     |     |     |     |     |     | Apart | from these | features, | the | application | also | cus- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --------- | --- | ----------- | ---- | ---- |
and solutions. tomizes the shopping experience by identifying the mer-
|     |     |     |     |     |     |     |     | chants | with | whom | the users | have | transactions. | This | fea- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ---- | --------- | ---- | ------------- | ---- | ---- |
DuetotheadvancedsemanticAI,theFinancialAdvisor
|              |           |            |        |               |     |              |          | ture        | provides   | a user-friendly |              | experience | and           | can save       | the     |
| ------------ | --------- | ---------- | ------ | ------------- | --- | ------------ | -------- | ----------- | ---------- | --------------- | ------------ | ---------- | ------------- | -------------- | ------- |
| Application  | is        | proficient | in     | identifying   |     | users’       | emotions |             |            |                 |              |            |               |                |         |
|              |           |            |        |               |     |              |          | most        | money      | by              | recommending | discounts  |               | and promotions |         |
| regarding    | financial | activities |        | and textual   |     | information. | This     |             |            |                 |              |            |               |                |         |
|              |           |            |        |               |     |              |          | from        | associated | sellers.        | As           | a result,  | the Financial |                | Advisor |
| advanced     | feature   | allows     | the    | application   |     | to provide   | more     |             |            |                 |              |            |               |                |         |
|              |           |            |        |               |     |              |          | Application |            | dictates        | that         | users get  | only          | the best       | deals   |
| personalized | financial |            | advice | and emotional |     | support,     | mak-     |             |            |                 |              |            |               |                |         |
ing the financial management process more accessible and by considering past purchases and preferences, promoting
financialoptimalityandcustomerhappiness.Itquestionsthe
| sensitive. | As the | program | determines |     | the | user’s emotional |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ---------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statewhenmakingfinancialdecisions,theapplicationoffers conventional business models of financial consulting and
|                 |       |                     |       |                     |     |                |     | modernizes  |       | the principles |        | of the personal   | finance | industry. |        |
| --------------- | ----- | ------------------- | ----- | ------------------- | --- | -------------- | --- | ----------- | ----- | -------------- | ------ | ----------------- | ------- | --------- | ------ |
| recommendations |       | that                | match | the feelings        |     | and objectives | of  |             |       |                |        |                   |         |           |        |
|                 |       |                     |       |                     |     |                |     | It          | gives | an insight     | into   | the prevailing    |         | position  | of the |
| the user;       | thus, | increasing          | the   | interest            | and | satisfaction   | of  |             |       |                |        |                   |         |           |        |
|                 |       |                     |       |                     |     |                |     | application |       | of AI          | in the | financial sector, | which   | opens     | up     |
| E-mail address: |       | rharaty@lau.edu.lb, |       | samir.bader@lau.edu |     |                |     |             |       |                |        |                   |         |           |        |

2 First Author, Samir Bader. Second Author, Ramzi Haraty
future financial decision-making as informative, inclusive, planning applications.
and innovative. When reflecting on the possibilities and
B. Scope of the Work
featuresoftheFinancialAdvisorApplication,itiscrucialto
realize that this is not merely an application but a financial Thisworkiswhollydevotedtotheuser.Ourvisionisto
assistant that helps users in their economic endeavors with create a highly sophisticated Financial Advisor Application
accuracy and wisdom. as a service and a sidekick in the financial life. This work
involvesleveragingthefeaturesofNETCore6todesignan
A. Problem Statement
extremely robust and highly scalable application. We have
This desire for more effective tools to extend financial integrated advanced features of AI in Python, which are
consultancy with the help of the internet and mobile appli- generallyusedfordeeplearning,suchasanomalydetection,
cationshighlightsthenecessityofstablemethodstodevelop consecutive transaction prediction, and semantic analysis
individual, particular approaches for every user. Most con- [2]. By using this diverse approach, we aim to enhance a
temporaryapproachestomanagingfinancialandaccounting user’sexperiencebyprovidingtimelyandaccurateinforma-
activity are based on fixed structures that ignore essential tion on managing money. This project has been developed
data, such as general user behavior and attitude needed to with the needs of user experiences in mind.
define what kind of recommendations the administrators
should give. The problem is that these applications become It is also not simply a matter of incorporating the
mere carriers of simple data transfers and cannot analyze different and complex aspects of modern financial advisory
user data such as frequency, mood, and preferences crucial services’ features into the application’s architecture. It is
to providing timely financial assistance [1-3]. about developing a framework that is open and capable of
changing according to the conditions of the field. Abstract
Today’s financial platforms can process structured data classes define the application structure, and this decision
effectively, they cannot extract as much value as from the makes it possible to add new features and change the prod-
unstructured data that stems from inputs about the users uct’s behavior without affecting its essential characteristics
and descriptions of the transactions [1]. This can lead to by third parties.
recommendingotherproductsorservicesthattheuserdoes
not need or cannot handle emotionally; thus, limiting the Implementing AI and machine learning into the appli-
possibility of positive interaction and satisfaction. Specifi- cation is not just a technicality. It’s a strategic decision
cally,ithasbeenfoundthatstudiesonconcreteapplications to address three primary objectives: anomaly detection for
of the soft computing paradigms, like the applications with better transaction security, predictive analysis for better fi-
semantic analysis or the applications that include adaptive nancial decisions, and semantic analysis for better financial
learning mechanisms, help solve the problems of financial planning advice.
advising. However, the practical application of these com-
plex methods requires effort. Among them, the most important is to develop and
optimize deep learning models for detecting anomalies in
Regarding the above issue, an effective approach for financial transactions. Python and other necessary machine
improvement is to combine TensorFlow and Keras with a learning libraries will be used to create the application that
Python environment. This integration will help the applica- will assist in identifying suspicious activity and increasing
tionlearntheusers’activitiesandpreferencesbyintegrating transaction security. We know how critical security and
semantic AI and M-learning solutions. So, achieving these reliability are in financial applications and strive to provide
objectives will facilitate the receipt and analysis of transac- you with a product you can rely on.
tionaldatasuchasthenumberoftransactions,thefrequency
of transactions, the currency, and any other quantitative To develop predictive models for financial forecasting:
indicators.Itwillalsoprocessinputsthatcontainqualityor The application will analyze historical financial data and
quantity data, such as the quantity of product, the quality the user’s transaction history to predict specific financial
of material, and so on. The knowledge of the users’ re- outcomes. This will empower users to make informed and
quirements will be constructed by applying artificial neural accurate economic decisions.
networks in this application. This functionality can give
To incorporate semantic analysis for understanding user
general information concerning financial conduct and give
sentiment and behavior, the application will use NLP
particular recommendations depending on the user’s data,
techniques to better understand user inputs and feedback
significantly increasing user satisfaction.
and provide more accurate and practical financial planning
Thisstudyseekstofillthegapbetweenconventionalfi- recommendations based on the client’s emotional status.
nancialadvisoryplatformsandadvancedAI-basedsolutions
The research questions guiding the development of this
by developing a financial advisor application that analyzes,
application are:
comprehends, and responds to each user’s economic story.
This approach solves the crucial problem of improving the
• In what ways can deep learning models be used to
quality and effectiveness of digital services’ financial rec-
solve the problem of identifying anomalous transac-
ommendations, which raises users’ confidence in financial

International Journal of Computing and Digital Systems 3
tions? NET Core 6 environment? And finally, section 6 concludes the paper and provides
future directions.
• What methods can be used to effectively forecast
financial patterns and users’ actions based on trans- E. Selecting a Template (Heading 2)
actional data using Python-based AI tools? First,confirmthatyouhavethecorrecttemplateforyour
papersize.Thistemplatehasbeentailoredforoutputonthe
C. Research Objectives 21cm X 28cm Paper Size.
This work aims to bridge the gap between conven-
F. Maintaining the Integrity of the Specifications
tional financial advisory platforms and advanced AI-driven
solutions by developing a sophisticated Financial Advisor The template is used to format your paper and style
Application. The key objectives of this research are: the text. All margins, column widths, line spaces, and text
fontsareprescribed;pleasedonotalterthem.Youmaynote
• EnhancingFinancialSecurity–Developandoptimize peculiarities.Forexample,theheadmargininthistemplate
deep learning models for detecting anomalies in fi- measuresproportionatelymorethaniscustomary.Thismea-
nancial transactions, improving transaction security surementandothersaredeliberate,usingspecificationsthat
through AI-driven anomaly detection techniques. anticipate your paper as one part of the entire proceedings,
and not as an independent document. Please do not revise
• Predictive Financial Analysis – Create predictive any of the current designations.
models that analyze historical financial data and user
transaction histories to forecast financial trends and 2. LITERATUREREVIEW
empower users with informed decision-making. Thespreadanddevelopmentoffintechhavefosteredfur-
ther developmentof newapplications that wouldcontribute
• AI-PoweredFinancialPlanning–Incorporateseman- to the simplification of financial transactions and increase
ticanalysisandnaturallanguageprocessing(NLP)to the accuracy and personalization of the offered financial
understand user sentiment and behavior, enabling the recommendations. Among these innovations, the Financial
application to provide personalized financial advice Advisor Application is one of the best integrated and
based on users’ emotional and financial conditions. sophisticated applications in the world of technology. This
paper aims to provide a literature review to establish the
D. Research Contributions essential technologies and critical applications that define
This work contributes to the field of AI-driven financial this revolutionary application. This new financial advisory
advisory systems by: toolcombinescontemporarycomputationaltechniqueswith
traditional but customized services.
• Developing a Scalable and Adaptive AI-Driven Fi-
nancial Advisory Framework – The application ar- A. Comprehensive Financial Overview
chitecture is designed with abstract classes, enabling The application gives users a summary of the financial
adaptability and extensibility in financial advisory situation, combining the data from several accounts and
services. the asset summary, liability, expenditure, and savings plan.
Users can make sound financial decisions by offering pre-
• Integrating Advanced AI Techniques for Financial cise and concise financial decisions since the application
Advisory Services – By leveraging deep learning for provides a clear and concise financial picture. This feature
anomalydetection,predictiveanalytics,andsemantic correspondswithAnderson,whostatesthatdataintegration
analysis, this study enhances the accuracy and relia- and visualization play a crucial role in improving user
bility of financial recommendations. experience and their decision-making process [1].
• Enhancing Transaction Security in Digital Financial B. Technological Base and Management Framework
Services – Implementing anomaly detection tech- As stated earlier, the basis of the described Financial
niques helps identify suspicious activities, increasing Advisor Application is the use of .NET Core — a decision
users’ confidence in financial applications. that signals the readiness to build solid and scalable apps
[3].NETCoreisahighlyadaptive,fast,andsecureplatform
• Improving User-Centric Financial Advisory Services
crucial for financial applications involving users’ data. It
– The application’s NLP-based semantic analysis tai-
ensures that complex capabilities are closely integrated
lorsfinancialadvicetousers’emotionalandfinancial
and the application will not slow down or have issues
states, providing a more intuitive and personalized
with various loads. This is especially the case within the
experience.
financial services industry, where the accuracy of data and
its authenticity cannot be compromised.
The rest of the paper is organized as follows: Section
2 provides the literature review. Section 3 describes the
It is integrated with NET Core, and the application
methodologyofthework.Section4presentstheexperimen-
utilizes Python’s AI features, including TensorFlow and
talresultsandsection5suppliesadiscussionoftheresults.
Keras. These libraries are among the most advanced tools

| 4   | First | Author, | Samir | Bader. | Second | Author, | Ramzi | Haraty |     |     |     |     |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
for deep learning, which can analyze enormous amounts of classes,servesasaguideline[4].Thisarchitecturaldecision
information successfully and search for valuable informa- enables third-party developers and financial institutions to
tion.Consequently,theuseofthetwohasbecomemixedup. extendtheapplication’scorefunctionalitiestosuitdifferent
NETCoreforstructureandPythonforintelligentoperations needs while not risking the overall integrity of the appli-
are the best pairs that bring high efficiency and intelligence cation [5]. It is a strategic move that centralizes the needs
to the Financial Advisor Application. of a global user base and the required financial regulations,
|           |            |     |              |     |               |     |     | languages, | and | operational | customizations |     |     |     |     |
| --------- | ---------- | --- | ------------ | --- | ------------- | --- | --- | ---------- | --- | ----------- | -------------- | --- | --- | --- | --- |
| C. Future | Directions |     | and Research |     | Opportunities |     |     |            |     |             |                |     |     |     |     |
Thus,theapplicationofAIinfinancialadvisoryservices
|     |     |     |     |     |     |     |     | This | flexibility | is  | essential | to keeping |     | the application |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | --------- | ---------- | --- | --------------- | --- |
offersmanypotentialresearchavenues,especiallyregarding effective
|     |     |     |     |     |     |     |     | up to date | and |     | in  | a rapidly | evolving |     | financial |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --------- | -------- | --- | --------- |
the protection of users’ data, the usage of responsible environment provided by abstract classes. This aligns with
AI, and the suitability of AI in financial decision-making. researchbyTertiltandScholz,whopostulatedthatfinancial
Future research could focus on the effects of real-time data solutions must be flexible enough to suit users’ needs.
| analysis | on economic |     | forecasting, |     | the utilization |     | of AI to |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------------ | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
improve financial awareness, and how best to increase the F. Personalized Financial Advice
|               |                  |     |          |             |        |       |      | Personalization     |                 | is           | the foundation |            | of the | Financial       | Ad-    |
| ------------- | ---------------- | --- | -------- | ----------- | ------ | ----- | ---- | ------------------- | --------------- | ------------ | -------------- | ---------- | ------ | --------------- | ------ |
| degree        | of customization |     | of       | financial   | advice | using | more |                     |                 |              |                |            |        |                 |        |
|               |                  |     |          |             |        |       |      | visor Application’s |                 | proposition. |                | As         | such,  | the application |        |
| sophisticated | machine          |     | learning | algorithms. |        |       |      |                     |                 |              |                |            |        |                 |        |
|               |                  |     |          |             |        |       |      | can provide         | recommendations |              |                | consistent |        | with the        | user’s |
Moreover, the application’s architecture and features spendingpatternsandfinancialobjectivesthroughsemantic
allow for integrating quantitative and qualitative sentiment analysis and predictive models. Whether it is about saving
analyses of financial statements. Thus, perpetuating the money, investing money, or even planning for the bud-
integration of these elements can lead to further efficiency get, the application is designed to help according to the
and customization in economic consulting. particularity of the user. This level of personalization is
|     |     |     |     |     |     |     |     | accomplished |     | through | learning | and | development | to  | ensure |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | -------- | --- | ----------- | --- | ------ |
The Financial Advisor Application is a new generation efficient
|                |         |            |     |       |       |                 |     | that the     | advice | is helpful      | and             |     | in the        | future. |         |
| -------------- | ------- | ---------- | --- | ----- | ----- | --------------- | --- | ------------ | ------ | --------------- | --------------- | --- | ------------- | ------- | ------- |
| of personal    | finance | management |     | tools | that  | incorporate     | the |              |        |                 |                 |     |               |         |         |
|                |         |            |     |       |       |                 |     | G. AI-Driven |        | Merchant        | Recommendations |     |               |         |         |
| best features. | Based   | on         | NET | Core  | 6 and | AI technologies |     |              |        |                 |                 |     |               |         |         |
|                |         |            |     |       |       |                 |     | For          | better | user experience |                 | and | more savings, |         | the Fi- |
developedusingPython,itwillbepossibletoprovideusers
withapowerful,safe,andhighlycustomizedexperience[3]. nancialAdvisorApplicationalsousesArtificialIntelligence
The application stands out from other financial technology to analyze users’ transaction history and suggest merchant
applications through its capacity to predict trends, identify offers. This not only helps the consumer by making the
|               |      |             |     |             |             |                 |        | experience | more | personal   | and | tailored       | to  | their needs | but  |
| ------------- | ---- | ----------- | --- | ----------- | ----------- | --------------- | ------ | ---------- | ---- | ---------- | --- | -------------- | --- | ----------- | ---- |
| deviations    | from | standards,  |     | and analyze |             | user sentiment. |        |            |      |            |     |                |     |             |      |
|               |      |             |     |             |             |                 |        | also helps | them | save money |     | with discounts |     | and sales   | from |
| The continued |      | advancement |     | of the      | application | will            | give a |            |      |            |     |                |     |             |      |
glimpse of the possibilities and difficulties of using AI in the partnered vendors. The application also employs user
delivering effective and efficient financial services to users, data and artificial intelligence to provide users with the
propelling the development of better and more effective most enriching offers, thus giving value to their financial
operations.
| user-oriented | financial |     | technologies. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D. The Relationship between Deep Learning and Machine H. AI Predicting Trends
| Learning |     |     |     |     |     |     |     | It has | been | proved | that | AI can | perform | very | well in |
| -------- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------ | ---- | ------ | ------- | ---- | ------- |
predictivesolutionsacrossdifferentdomains,particularlyfi-
| The | programming |     | tools most | useful | for | machine | learn- |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | ---------- | ------ | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
nancialplatforms.HistoricaldataaresignificantbecauseAI
inginPythonareTensorFlowandKeras,whichcanpredict
computerscanfindhiddenpatternsthathumananalystsmay
| financial | trends, | detect | anomalies, |     | and analyze |     | semantics |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[7-8]. These capabilities enable the application to detect otherwise ignore. Deep learning and neural networks have
transaction patterns, predict the users’ future economic beencriticalinhelpingidentifythesepatterns.Forinstance,
activities, and ascertain their needs. RNNs will do the data Rezaei et al. have described how deep learning algorithms
|           |              |     |                     |     |     |      |          | can perform   | the | stock        | market’s | future | downtrends |                | with a |
| --------- | ------------ | --- | ------------------- | --- | --- | ---- | -------- | ------------- | --- | ------------ | -------- | ------ | ---------- | -------------- | ------ |
| analysis, | and insights |     | and recommendations |     |     | will | be given |               |     |              |          |        |            |                |        |
|           |              |     |                     |     |     |      |          | high accuracy |     | level, which |          | can be | helpful    | for investment |        |
withthehelpofdataanalysis.However,verysubtlepatterns
[6].
| in the data | may    | not be          | easily   | detected. |              |              |          |          |       |                 |     |              |     |             |     |
| ----------- | ------ | --------------- | -------- | --------- | ------------ | ------------ | -------- | -------- | ----- | --------------- | --- | ------------ | --- | ----------- | --- |
|             |        |                 |          |           |              |              |          | I. AI in | Other | Fields          |     |              |     |             |     |
| Substantial |        | evidence        | suggests |           | that machine |              | learning |          |       |                 |     |              |     |             |     |
|             |        |                 |          |           |              |              |          | Although | AI    | is particularly |     | incorporated |     | in finance, | it  |
| models      | should | be incorporated |          | into      | financial    | forecasting. |          |          |       |                 |     |              |     |             |     |
resonatesinmultipleindustries.Inhealthcare,AIalgorithms
Forexample,modelshelppredictmarkettrendsandidentify
areusedforoutbreakpredictionanddeeplearningisutilized
| patterns | humans       | may | not        | notice.   | These | capabilities | are     |           |            |           |     |      |            |        |      |
| -------- | ------------ | --- | ---------- | --------- | ----- | ------------ | ------- | --------- | ---------- | --------- | --- | ---- | ---------- | ------ | ---- |
|          |              |     |            |           |       |              |         | to design | individual | patients’ |     | care | plans [7]. | In the | same |
| crucial  | for creating | a   | predictive | financial |       | advisory     | setting |           |            |           |     |      |            |        |      |
way,inretail,AIisusedtokeeptrackofthestockandmake
| that responds | to  | the user’s | data | shift. |     |     |     |                 |     |              |     |      |       |              |     |
| ------------- | --- | ---------- | ---- | ------ | --- | --- | --- | --------------- | --- | ------------ | --- | ---- | ----- | ------------ | --- |
|               |     |            |      |        |     |     |     | recommendations |     | to customers |     | [8]. | These | advancements |     |
E. Customization and Extensibility also indicate that AI has the unique ability and capacity
When it comes to extensibility and customization, the to tailor applications to revolutionize several industries and
| application’s | architecture, |     | especially |     | the usage | of  | abstract | sectors | [14-16]. |     |     |     |     |     |     |
| ------------- | ------------- | --- | ---------- | --- | --------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- |

International Journal of Computing and Digital Systems 5
J. AI and Sentiment Analysis budget planning tools that leverage predictive analytics to
Considering the growing popularity of AI applications anticipate users’ future financial needs based on historical
in various industries, it is paramount to explore customer data, showcasing improved financial decision-making out-
sentimentanalysis.Ittypicallymarkstextminingtechniques comes.
that seek to identify the tone of opinion users express.
AI’s ability to detect anomalies in financial transactions
This technique finds broader usage in the financial world
has also been a focal point. Lee et al. [16] developed a
for ascertaining the market mood from news articles and
machine learning framework for fraud detection in dig-
tweets.AlistingbyBollenetal.[9]revealedthatthemood
on Twitter could affect the movements of the stock market, ital payments, combining deep learning techniques with
anomalydetectionalgorithms. Theirresultsrevealedhigher
making sentiment analysis crucial in market analysis.
accuracy in identifying fraudulent transactionscompared to
K. Behavior Prediction traditionalmethods.Additionally,astudybyRamachandran
etal.[17]highlightedtheintegrationofAIwithblockchain
Customer behavior prediction using artificial intelli-
to enhance transparency and security in financial systems.
genceincludesidentifyingpatternsanddefinitionsofbehav-
ior to make assumptions about the likely behavior of cus-
O. Sentiment Analysis in Fintech
tomersintheforeseeablefuture.Thisisparticularlyhelpful
Sentiment analysis has become a pivotal tool in un-
in marketing with personalized segments and customer
derstanding consumer behavior and market trends. A re-
maintenance programs. For instance, there are behavioral
cent study by Chen et al. [18] examined the integration
prediction models to determine which customers are most
of sentiment analysis into mobile banking applications.
likely to churn, so businesses can take preventive measures
By analyzing customer feedback and app usage patterns,
[8]. This capability is also essential in processing financial
theirAImodelprovidedpersonalizedrecommendationsand
expenditure since spending behaviors can provide valuable
improved customer satisfaction rates. Another noteworthy
insights into financial management advice [10].
contribution by Gupta et al. [19] focused on combining
L. Forecasting sentiment analysis with transaction data to offer tailored
AIhasenormouslychangedthedifferentsectorsthrough merchantrecommendations,emphasizingtheimportanceof
contextual understanding in fintech applications.
theforesightedanalysisofthedatacollected.Somemodels,
such as the LSTM and N-BEATS, have been used in
P. Advanced Machine Learning Models for Sentiment
finance studies, as shown in the time series forecasting.
Analysis
Such models can deal with intricate data patterns and offer
The application of advanced machine learning models
robust prediction, which can help make decisions [11].
has pushed the boundaries of sentiment analysis in fintech.
Therefore, there is enough ground for integrating ma- Transformer models, such as BERT and GPT, have been
chinelearningmodelsinfinancialforecasting.Forinstance, widely adopted for their superior language understanding
models aid in comprehending attitudes and climates that capabilities. For instance, Sun et al. [14] demonstrated
humans may not discern inherently. These capabilities are the use of fine-tuned BERT models in analyzing customer
essential for constructing an accurate advisory financial reviews for predicting product success in financial market-
environment that adapts to the alteration of data mentioned places. Similarly, the study by Iqbal et al. [20] showcased
by users [12]. the effectiveness of TCN and N-BEATS models in com-
bining time-series data with sentiment analysis to predict
M. AI in Natural Language Processing financial trends.
Thedevelopmentsinnaturallanguageprocessing(NLP)
In 2024, Johnson et al. introduced a hybrid model that
havecontributedimmenselytoimprovingthecapabilityand
integrates sentiment analysis with knowledge graphs for
capacity of various forms of AI to interpret and create nat-
financial decision support systems. This approach allowed
ural languages. These enhancements have ensured a better
for a more comprehensive understanding of user behavior
handling of user interactions and an excellent sentiment
and preferences, enhancing the personalization of financial
analysis. It is essential to discuss deep learning trends in
recommendations [21].
NLP, the progress made, and the future that may lie ahead
for these technologies, which was addressed by Young et
Q. Challenges and Future Directions
al. in the perspective of 2018 [13].
While recent advancements are promising, challenges
N. AI in Financial Advisory and Planning remain in deploying AI and sentiment analysis in fintech.
Scalabilityissues,dataprivacyconcerns,andthecomplexity
Recent research underscores the transformative impact
of unstructured data processing continue to be significant
of AI in financial advisory systems. For example, Wang
hurdles. Several studies, including Sharma et al. [22],
et al. [14] explored the use of generative AI for dynamic
highlightedtheneedformorerobustframeworkstoaddress
portfolio optimization, demonstrating how reinforcement
these challenges, particularly in real-world deployments.
learningalgorithmscanprovidereal-timeinvestmentstrate-
gies.Similarly,PatelandKumar[15]investigatedAI-driven

6 First Author, Samir Bader. Second Author, Ramzi Haraty
ments, fund transfers, and withdrawals.
2) Merchant Data – Contains information about mer-
chants associated with user transactions, including
vendor type, transaction frequency, and discount
eligibility.
3) Account Data – Covers financial account details,
including balance history, account type (checking,
savings, credit), spending trends, and income pat-
terns.
4) These data inputs are pre-processed and normalized
beforebeingfedintothesystem’sanalyticalmodels.
C. Processing and Analysis
ThecoreofthesystemarchitectureconsistsofthreeAI-
driven analytical components, which process the input data
Figure1.Architectureoftheapplication and extract meaningful financial insights:
Anomaly Detection (Fraud Detection and Unusual
3. METHODOLOGY Spending Patterns)
This study employs a data-driven approach that inte-
• ImplementedusingTensorFlowandKerasdeeplearn-
gratesmachinelearning(ML)andartificialintelligence(AI)
ing frameworks, the anomaly detection model evalu-
techniquestoprovidepersonalizedfinancialadvicebasedon
ates transaction data to detect irregular patterns.
users’ banking transactions. The primary objectives of this
approach are:
• Techniques such as Isolation Forests, One-Class
SVM, and Autoencoders are used to identify fraudu-
• Understanding Customer Behavior and Sentiment –
lent transactions, unauthorized spending, or financial
Utilizing sentiment analysis to assess users’ financial
distress signals
moods,spendingtendencies,andemotionalstatesthat
may impact financial decisions. • The model assigns an anomaly score to each trans-
action, flagging suspicious activity for further review
• Detecting Anomalies in Financial Transactions –
or intervention.
Implementing anomaly detection models to identify
unusual transaction patterns, such as potential fraud, D. SentimentAnalysis(UserMoodandFinancialBehavior)
unexpected spending habits, or financial distress.
• Employsnaturallanguageprocessing(NLP)anddeep
learning models (LSTMs, Transformers) to assess
• Generating Personalized Merchant Discounts and Fi-
usersentimentfromtransactionpatternsandspending
nancial Recommendations – Leveraging predictive
habits.
analytics to recommend financial products, savings
strategies, or tailored merchant discounts based on
• Uses emotional indicators derived from transaction
transaction history and user behavior.
data to determine financial well-being (e.g., stress-
related spending, impulse purchases, or conservative
To achieve these objectives, the methodology incorpo-
financial behavior).
rates semantic analysis, predictive modeling, and anomaly
detection as core analytical components [4]. The system • Outputs an emotional score that helps tailor financial
leverages advanced deep learning models, natural language advice based on the user’s current financial mood.
processing (NLP), and statistical algorithms to provide
highly accurate and real-time financial insights. E. PredictiveModeling(FinancialForecastingandPerson-
alized Recommendations)
A. Architecture
• Utilizes advanced predictive analytics models such
The system architecture, illustrated in Figure 1, is de- as Transformers, Temporal Convolutional Networks
signed to seamlessly integrate multiple data streams, apply (TCN), and N-BEATS to analyze transaction history
sophisticated AI-based analytics, and generate personalized and forecast future financial behaviors.
financial recommendations. The architecture consists of
severalkeycomponents,eachresponsiblefordistinctstages • Themodelgeneratespersonalizedfinancialforecasts,
of data processing and decision-making. such as expected cash flow, potential budget deficits,
and optimal saving strategies.
B. Data Inputs and Sources
1) TransactionData–Includesallfinancialtransactions • The system also integrates sentiment-aware financial
conducted by the user, such as purchases, bill pay- predictions, improving forecasting accuracy by 25

International Journal of Computing and Digital Systems 7
F. Backend System and Data Integration
Actsastheintegrationhubforallanalyticalcomponents
resultingfromthebackendsystem,developedin.NETCore
6.
• The backend system, developed in .NET Core 6, acts
as the integration hub for all analytical components.
• Ensures real-time data flow between the anomaly
detection,sentimentanalysis,andpredictivemodeling
layers.
• Manages user authentication, data security, and API
communicationforseamlessinteractionwithfinancial
institutions and third-party services.
G. Personalized Financial Recommendations
Theinsightsgeneratedbytheanalyticalcomponentsare Figure2.MCCdataset
processed to provide tailored financial advice and alerts:
4) User Notification & Actionable Insights – Financial
• Budgeting Recommendations – Users receive per-
recommendations, security alerts, and budget sug-
sonalized suggestions on how to optimize spending,
gestions are presented to users through the UI.
avoid unnecessary expenses, and improve savings.
5) FeedbackLoop&ModelOptimization–Thesystem
• Transaction Security Alerts – Users are notified of continuously learns from user interactions, refining
suspicious transactions, with recommendations on its prediction accuracy and recommendation preci-
how to respond. sion over time.
• Merchant Discounts & Financial Product Offers – J. Dataset
Based on spending habits, users receive customized The dataset was aggregated from bank transaction logs,
discount offers or financial product suggestions (e.g., which were processed and analyzed to extract meaningful
credit card rewards, high-yield savings accounts). insights. The data sources include:
The recommendation engine operates in real-time, en- • Bank Transaction Records: Historical records of fi-
suring that users receive timely and actionable insights. nancial transactions conducted by users.
H. User Interface and Integration • MerchantCategoryCode(MCC)Classification:Stan-
• Front-end application (Web/Mobile): Provides an in- dardized categories assigned by Visa and Mastercard
tuitive user experience, displaying financial insights, toclassifybusinessesbasedontheirprimaryservices
risk alerts, and recommended actions. as depicted in figure 2.
• Interactive Features: Users can adjust financial goals, • MerchantDataandDemographics:Additionaldetails
explore alternative budgeting strategies, and receive about businesses where transactions were made, in-
AI-driven assistance. cluding industry type and transaction frequency.
• Visual Analytics: Includes graphs and dashboards il- K. Transaction Data
lustrating spending patterns, anomaly detections, and
dbo.Customer Cards, dbo.Extraaccounts,
future financial projections.
dbo.Extratransactions, dbo.fin Category,
dbo.fina SubCategory, dbo.fin MainCategory,
I. System Flow and Execution Pipeline
dbo.fin goal fin MainCategory, dbo.fin Goals,
1) Data Collection & Pre-Processing – The system dbo.fin Budget, dbo.Budget Category.
gathers and cleans transaction, merchant, and ac-
count data. Description: Detailed records of user transactions, in-
2) AI-Based Analytics Execution – Data is processed cluding transaction amount, date, and MCC codes. These
through the anomaly detection, sentiment analysis, transactions span various categories like dining, travel,
and predictive modeling components. retail, and more, providing a comprehensive view of user
3) Backend Processing & Decision Making – The spending.
backendsystemintegratesAI-generatedinsightsand
determines appropriate recommendations.

| 8   | First | Author, | Samir | Bader. | Second | Author, | Ramzi | Haraty |     |     |     |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
Figure5.Merchantsbox
Figure3.Thedashboard
Figure4.Suggestion’sbox
Figure6.Spendingbehaviorchart
| L. Merchant  | Data |              |     |       |              |                |           |           |          |           |     |     |     |     |
| ------------ | ---- | ------------ | --- | ----- | ------------ | -------------- | --------- | --------- | -------- | --------- | --- | --- | --- | --- |
| Tables:      |      | dbo.Merchant |     | List, |              | dbo.Merchants, |           |           |          |           |     |     |     |     |
|              |      |              |     |       |              |                |           | shows the | spending | behavior. |     |     |     |     |
| dbo.Merchant |      | Suggestion,  |     |       | dbo.Merchant |                | GiftCard, |           |          |           |     |     |     |     |
| dbo.Merchant |      | Promotion,   |     |       | dbo.Merchant |                | Rewards,  |           |          |           |     |     |     |     |
N. User Profiles
| dbo.Merchant |                 | Category,   | dbo.CustomerType |          |           | Merchant.   |           |                   |             |              |          |          |             |           |
| ------------ | --------------- | ----------- | ---------------- | -------- | --------- | ----------- | --------- | ----------------- | ----------- | ------------ | -------- | -------- | ----------- | --------- |
|              |                 |             |                  |          |           |             |           | Tables:           |             | do.Customers |          |          | do.Customer | user,     |
| Description: |                 | Information |                  | about    | merchants | categorized |           | dbo.PersonalInfo. |             |              |          |          |             |           |
| by Visa      | and Mastercard. |             | This             | includes |           | details     | about the |                   |             |              |          |          |             |           |
|              |                 |             |                  |          |           |             | offers    | Description:      |             | Detailed     | profiles | for each | user,       | combin-   |
| types of     | merchants       |             | frequented       | by       | users     | and         | the       |                   |             |              |          |          |             |           |
|              |                 |             |                  |          |           |             |           | ing their         | transaction | history      | and      | account  | data,       | including |
available.
|     |             |         |     |              |     |          |        | demographic   | information, |        | spending       | habits,          | income         | levels, |
| --- | ----------- | ------- | --- | ------------ | --- | -------- | ------ | ------------- | ------------ | ------ | -------------- | ---------------- | -------------- | ------- |
|     |             |         |     |              |     |          |        | and financial | goals.       | Use    | Case: Provides |                  | the foundation | for     |
| Use | Case: Helps | provide |     | personalized |     | merchant | recom- |               |              |        |                |                  |                |         |
|     |             |         |     |              |     |          |        | personalized  | financial    | advice | and            | recommendations. |                |         |
mendationsanddiscountsbasedonusertransactionhistory.
| Figure 4,                                  | provides   | suggestions        |             | for | the user,    | and         | figure 5  |                    |           |              |             |            |     |              |
| ------------------------------------------ | ---------- | ------------------ | ----------- | --- | ------------ | ----------- | --------- | ------------------ | --------- | ------------ | ----------- | ---------- | --- | ------------ |
|                                            |            |                    |             |     |              |             |           | O. Anomaly         | Detection | Data         |             |            |     |              |
| shows the                                  | merchant’s |                    | box.        |     |              |             |           |                    |           |              |             |            |     |              |
|                                            |            |                    |             |     |              |             |           | Tables:            | dbo.ML    | Transactions |             | anomalies. |     |              |
| M. Account                                 | Data       |                    |             |     |              |             |           |                    |           |              |             |            |     |              |
|                                            |            |                    |             |     |              |             |           | Description:       |           | Data for     | identifying | irregular  |     | transactions |
| Tables:                                    |            | dbo.Extraaccounts, |             |     | dbo.Customer |             | user,     |                    |           |              |             |            |     |              |
|                                            |            |                    |             |     |              |             |           | that may           | indicate  | fraud or     | unexpected  | behavior.  |     | This table   |
| dbo.Extratransactions,                     |            |                    | dbo.Finance |     | Budget,      | dbo.Budget, |           |                    |           |              |             |            |     |              |
|                                            |            |                    |             |     |              |             |           | stores information |           | about        | detected    | anomalies. |     |              |
| dbo.CardsProducts,dbo.CardsTypes,dbo.Cards |            |                    |             |     |              |             | Cashback. |                    |           |              |             |            |     |              |
|                                            |            |                    |             |     |              |             |           | Use Case:          | Enhances  | transaction  |             | security   | by  | identifying  |
Description:Includesdataaboutusers’accountbalances
andalertingusersofpotentiallyfraudulentactivities.Figure
andactivities,suchassavings,checking,andinvestmentac-
|                    |       |                |          |     |          |         |           | 7 displays | an anomaly | transaction. |     |     |     |     |
| ------------------ | ----- | -------------- | -------- | --- | -------- | ------- | --------- | ---------- | ---------- | ------------ | --- | --- | --- | --- |
| counts. Monitoring |       | these          | accounts |     | helps in | setting | realistic |            |            |              |     |     |     |     |
| financial          | goals | and budgeting. |          |     |          |         |           | P. Budget  | and Goals  |              |     |     |     |     |
Use Case: Essential for creating comprehensive user Tables: dbo.fin Budget, dbo.Budget Category,
|          |               |     |          |           |     |         |          | dbo.Finance | Goals, | dbo.Finance |     | Goal | MainCategory. |     |
| -------- | ------------- | --- | -------- | --------- | --- | ------- | -------- | ----------- | ------ | ----------- | --- | ---- | ------------- | --- |
| profiles | and providing |     | accurate | financial |     | advice. | Figure 6 |             |        |             |     |      |               |     |

|     |     |     |     |     |     | International | Journal | of Computing | and | Digital Systems |     |     | 9   |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | ------------ | --- | --------------- | --- | --- | --- |
Figure7.Anomalytransaction
Figure9.Budgetwidgets
Figure10.Budgetdashboard
|     |     |     |     |     |     |     | scaled to | a manageable | level | to enable | their | use in | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----- | --------- | ----- | ------ | --- |
Figure8.Budgetcreation
|              |             |     |                |        |             |               | analysis       | aiming to | standardize   | the results | by        | either     | using |
| ------------ | ----------- | --- | -------------- | ------ | ----------- | ------------- | -------------- | --------- | ------------- | ----------- | --------- | ---------- | ----- |
|              |             |     |                |        |             |               | the current    | US dollar | exchange      | rate or     | inflating | the amount |       |
|              |             |     |                |        |             |               | to the current | year      | if necessary. |             |           |            |       |
| Description: | Information |     | about          | users’ | budgets     | and financial |                |           |               |             |           |            |       |
| goals. This  | includes    | the | categorization |        | of expenses | and the       |                |           |               |             |           |            |       |
2) Training
| tracking | of progress | towards | financial |     | targets. |     |          |         |              |         |      |          |     |
| -------- | ----------- | ------- | --------- | --- | -------- | --- | -------- | ------- | ------------ | ------- | ---- | -------- | --- |
|          |             |         |           |     |          |     | Language | Models: | To determine | whether | each | transac- |     |
Use Case: It helps users set and manage financial tion description is positive, negative, or neutral, we em-
goals and budgets, ensuring they stay on track with their ployed pre-trained language models specialized in financial
financialplans.Figure8showsthebudgetcreationwindow data for sentiment analysis on the cleaned transaction de-
and figure 9 portrays the budget widgets. Figures 9 and scriptions. These models included BERT and GPT, which
10 depicts the budget dashboard and the goal creation were fine-tuned on a financial text corpus to enhance the
respectfully. Figure 11 specifies the goal creation. model’s performance on context-dependent terms.
Q. Sentiment Analysis and Data Integration Classification: Based on the nature and details of the
| This | is an essential |     | component | of  | the Financial | Advisor |     |     |     |     |     |     |     |
| ---- | --------------- | --- | --------- | --- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Applicationasitcategorizescustomers’emotionsaccording
| to their | transactions. | This | process | is  | necessary | to analyze |     |     |     |     |     |     |     |
| -------- | ------------- | ---- | ------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
theuser’sbehaviorandrecommendfinancialdecisions.This
sectionreportsadetailedplanonhowthestudywillprocess
| the sentiment | analysis |     | and integrate | data | [9]. |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ------------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
1) Preprocessing
| Data         | Cleaning:       | Transaction |      | descriptions  |         | were prepro-    |     |     |     |     |     |     |     |
| ------------ | --------------- | ----------- | ---- | ------------- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| cessed to    | eliminate       | noise       | and  | ensure        | that    | all the entries |     |     |     |     |     |     |     |
| were in      | the same        | format.     | This | step included |         | preprocessing   |     |     |     |     |     |     |     |
| the text     | by adjusting    | common      |      | formatting    | issues, | including       |     |     |     |     |     |     |     |
| punctuation, | capitalization, |             | and  | spelling      | errors. |                 |     |     |     |     |     |     |     |
Normalization: The transaction amounts and dates were Figure11.Goalcreation

| 10  | First | Author, | Samir | Bader. | Second | Author, | Ramzi | Haraty |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- |
transaction descriptions, these transactions were then di- by data and, simultaneously may consider the emotional
vided into a set of pre-determined emotional types, namely context of the situation.
| Outgoing,  | Sad,            | Feeling | Generous, | Shopping, |            | Roadtrip, | Ad- |               |          |     |     |
| ---------- | --------------- | ------- | --------- | --------- | ---------- | --------- | --- | ------------- | -------- | --- | --- |
|            |                 |         |           |           |            |           |     | R. Predictive | Modeling |     |     |
| venturous, | Health-Focused, |         |           | Stressed, | Culturally | Engaged,  |     |               |          |     |     |
and Tech Enthusiast. We used sophisticated statistical tools to forecast future
spendingpatternsandrecommendproperfinancialmanage-
3) Integration ment. These models were meant to evaluate past financial
Sentiment Scores: The sentiment of each transaction transactions to predict future actions. Here’s a detailed
was then determined based on the emotion associated with breakdownofourapproachtopredictivemodeling:Here’sa
it. These scores were then compiled and computed over detailed breakdown of our approach to predictive modeling
| various | intervals | to give | insights | into | the user’s | emotional |     | [5]. |     |     |     |
| ------- | --------- | ------- | -------- | ---- | ---------- | --------- | --- | ---- | --- | --- | --- |
patterns.
|     |     |     |     |     |     |     |     | 1) Transformer | Models |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | --- |
Profile Enrichment: The sentiment scores were com- Architecture: Transformer architectures efficiently learn
bined with other user data, such as transaction history long-term dependencies inherent in data and thus do not
and account details, to augment the user profiles. This require sequential computations, making them suitable for
integration provided a more comprehensive picture of the time series prediction. They employ self-attention mecha-
user’s financial activity. nisms that determine the relevance of different points in a
sequence.
| Contextual | Analysis: |     | This | would | have the | added | advan- |     |     |     |     |
| ---------- | --------- | --- | ---- | ----- | -------- | ----- | ------ | --- | --- | --- | --- |
tageofcomplementingnumericaldataandthefindingsfrom Implementation: The Transformer model was devel-
sentiment analysis in a way that was impossible through oped using TensorFlow/Keras. It comprises several stacked
conventional statistical modeling. For instance, many small blocks of multi-head self-attention and feed-forward net-
purchasesinterspersedwithmoresignificantamountscould work, normalized across the layers and dropout layers to
| indicatethatthepersonisspendingmoneybecauseofstress. |     |          |     |     |     |     |     | avoid overfitting. |     |     |     |
| ---------------------------------------------------- | --- | -------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
| 4) Personalized                                      |     | Insights |     |     |     |     |     |                    |     |     |     |
Training:Itwastrainedonsequencesofhistoricaltrans-
Behavior Prediction: By combining the data, the appli- action data. We fine-tuned it with a learning rate scheduler,
cation could suggest how the user will spend money in the theAdamoptimizer,andameansquarederrorlossfunction.
| future and | give | recommendations. |     | For | example, | a   | user in |     |     |     |     |
| ---------- | ---- | ---------------- | --- | --- | -------- | --- | ------- | --- | --- | --- | --- |
the Health-Focused segment will be given suggestions for 2) Temporal Convolutional Networks (TCN)
|            |     |           |      |          |        | offers. |     | Architecture:    | TCNs are developed  | for sequence | model-    |
| ---------- | --- | --------- | ---- | -------- | ------ | ------- | --- | ---------------- | ------------------- | ------------ | --------- |
| membership | in  | a fitness | club | or other | health |         |     |                  |                     |              |           |
|            |     |           |      |          |        |         |     | ing; they employ | causal convolutions | to prevent   | the model |
Anomaly Detection: The sentiment analysis also high- from producing the temporal order of the data. They can
effective
lighted possible abnormalities. For instance, an abrupt address long-term dependencies and are in train-
| changeinspendingbehaviorfromauserclassifiedasRisk- |           |          |     |       |        |           |     | ing.            |         |                   |           |
| -------------------------------------------------- | --------- | -------- | --- | ----- | ------ | --------- | --- | --------------- | ------- | ----------------- | --------- |
| Averse to                                          | high-risk | spending |     | would | prompt | an alert. |     |                 |         |                   |           |
|                                                    |           |          |     |       |        |           |     | Implementation: | The TCN | model was trained | using the |
Merchant Recommendations: It could even recommend TCN library available in Keras. The architecture comprised
merchants based on people’s emotional trends and spend- severaldilationconvolutions,residualconnections,andnor-
| ing habits. | For | example, | users | categorized |     | as Adventurous |     | malization layers. |     |     |     |
| ----------- | --- | -------- | ----- | ----------- | --- | -------------- | --- | ------------------ | --- | --- | --- |
offered
| might be        |     | specific  | coupons | and  | deals | on         | products |                   |                          |                    |             |
| --------------- | --- | --------- | ------- | ---- | ----- | ---------- | -------- | ----------------- | ------------------------ | ------------------ | ----------- |
|                 |     |           |         |      |       |            |          | Training:         | The model was fine-tuned | using the          | historical  |
| from subscribed |     | merchants | that    | fall | under | the travel | cate-    |                   |                          |                    |             |
| gory.           |     |           |         |      |       |            |          | transaction data. | The hyperparameters      | were               | adjusted to |
|                 |     |           |         |      |       |            |          | select the number | of filters, kernel       | size, and dilation | rate.       |
5) Feedback Loop For optimization, the mean squared error loss function was
| User         | Interaction: | Users     | could     | engage          | with      | the         | applica- | employed.     |                |                  |        |
| ------------ | ------------ | --------- | --------- | --------------- | --------- | ----------- | -------- | ------------- | -------------- | ---------------- | ------ |
| tion by      | confirming   | or        | disputing | the             | sentiment | categoriza- |          |               |                |                  |        |
| tions. This  | feedback     |           | process   | helped          | improve   | the         | models   | 3) N-BEATS    |                |                  |        |
|              |              |           |           |                 |           |             |          | Architecture: | N-BEATS stands | for Neural basis | expan- |
| and increase | the          | precision | of        | the predictions |           | over        | time.    |               |                |                  |        |
sionanalysisforinterpretabletimeseriesforecasting,atime
Continuous Learning: These sentiment analysis models series forecasting model. It breaks down time-series data
were refined using user feedback and fresh transaction data into trends and seasonality features, giving a more human-
| incorporated | into | the system. |     |     |     |     |     | friendly forecast. |     |     |     |
| ------------ | ---- | ----------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
The Financial Advisor Application incorporated senti- Implementation:TheN-BEATSmodelwasimplemented
ment analysis and information about the user’s transactions using custom Keras layers, as described in the following
and accounts, allowing for sophisticated and feasible rec- section. The architecture comprised several dense layers
ommendations.Thiscreatedaholisticapproachthathelped with ReLU activations and final linear layers that output
provide users with recommendations and insights backed the trend and seasonality components.

|     |     |     |     |     |     |     | International | Journal | of Computing | and | Digital | Systems |     | 11  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------------ | --- | ------- | ------- | --- | --- |
Training: The model was trained using historical trans- 1) Model Selection and Training
actional data. We included learning rate scheduling and Algorithm Choice: We divided the chosen anomaly
early stopping to enhance the training process. The mean detection algorithms into two categories: unsupervised and
| squared error | loss | function | was | employed | for | optimization. |     |            |          |           |             |       |            |           |
| ------------- | ---- | -------- | --- | -------- | --- | ------------- | --- | ---------- | -------- | --------- | ----------- | ----- | ---------- | --------- |
|               |      |          |     |          |     |               |     | supervised | machine  | learning  | algorithms, |       | namely     | Isolation |
|               |      |          |     |          |     |               |     | Forest,    | LOF, and | One-Class | SVM.        | These | algorithms | are       |
4) Data Preparation
|     |     |     |     |     |     |     |     | beneficial | in detecting | anomalies |     | in transactional |     | data and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --------- | --- | ---------------- | --- | -------- |
Normalization: All input data were normalized, as the do not need to be trained, as they are given labeled data
| models need | to receive  | data | in          | a proper | format. | This | step   | sets. |     |     |     |     |     |     |
| ----------- | ----------- | ---- | ----------- | -------- | ------- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- |
| required    | normalizing | the  | transaction |          | amounts | and  | equal- |       |     |     |     |     |     |     |
izing the time intervals. Sequence Generation: For the TrainingData:Transactiondatacollectedovertheyears
Transformer and TCN models, sequences of data points were employed to train the models. This data contained
werecreatedtoformtheinputtothemodels.Eachsequence standardspendingpatterns,asampleoftheactualfraudulent
was a predetermined number of data points, representing a transactions that the models could learn, and normal and
| window of | transactions | over | history. |     |     |     |     | abnormal | spending. |     |     |     |     |     |
| --------- | ------------ | ---- | -------- | --- | --- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- |
Feature Engineering: To improve the model’s perfor- 2) Data Preprocessing
mance,featureslikeuserageandgender,accountbalances, Feature Extraction: To fine-tune the anomaly detection
| and sentiment | scores  | derived | from | the | transaction |     | descrip- |          |             |                |            |           |           |       |
| ------------- | ------- | ------- | ---- | --- | ----------- | --- | -------- | -------- | ----------- | -------------- | ---------- | --------- | --------- | ----- |
|               |         |         |      |     |             |     |          | models,  | features    | of transaction |            | data were | selected. | These |
| tions were    | added.  |         |      |     |             |     |          |          |             |                |            |           |           |       |
|               |         |         |      |     |             |     |          | include  | transaction | amount,        | frequency, |           | time, MCC | code, |
|               |         |         |      |     |             |     |          | and user | profile.    |                |            |           |           |       |
| 5) Evaluation | Metrics |         |      |     |             |     |          |          |             |                |            |           |           |       |
Mean Absolute Percentage Error (MAPE): This was Normalization: The data was scaled to a standardized
used to assess the models’ performance in predicting the rangetoensureconsistencyacrossalldatapoints.Thispro-
outcomes.MAPEistheaverageofrelativeerrorsandgives cess is crucial for optimizing the performance of distance-
an idea of the size of the mistakes, which is easier to based anomaly detection algorithms, such as LOF and
| understand | than absolute |     | errors. |     |     |     |     | Isolation | Forest. |     |     |     |     |     |
| ---------- | ------------- | --- | ------- | --- | --- | --- | --- | --------- | ------- | --- | --- | --- | --- | --- |
Accuracy: The validity of the models was measured 3) Model Implementation
by how well they forecasted future transactions within a IsolationForest:Thisalgorithmisolatesobservationsby
tolerance level. This involved assessing the models on new randomly choosing one feature and then choosing a split
data to test for their applicability across different contexts. valuebetweenthelargestandthemostminorfeatures.Thus,
|                |              |         |     |        |      |              |     | fewer splits | which | must        | be made   | to isolate | an observation |     |
| -------------- | ------------ | ------- | --- | ------ | ---- | ------------ | --- | ------------ | ----- | ----------- | --------- | ---------- | -------------- | --- |
| 6) Integration | and          | Testing |     |        |      |              |     |              |       |             |           |            |                |     |
|                |              |         |     |        |      |              |     | means that   | the   | observation | is likely | to be      | an outlier.    |     |
| Real-Time      | Predictions: |         | The | models | were | incorporated |     |              |       |             |           |            |                |     |
into the application to enable a predictive model of users’ Local Outlier Factor (LOF): LOF estimates the density
spending patterns. This entailed applying the models to the of the given data point concerning its neighbors. Anomaly
real world and designing a data processing and prediction means that there is a point in the data set whose density is
output system. significantly less than the density of its neighbors.
User Feedback: The users were given the forecasts and One-Class SVM: This algorithm learns the decision
asked to verifying whether they were correct or not. This function for anomaly detection, which is the hyperplane
| feedback      | helped | to enhance | the  | models | and | made | them |              |           |                   |             |      |           |     |
| ------------- | ------ | ---------- | ---- | ------ | --- | ---- | ---- | ------------ | --------- | ----------------- | ----------- | ---- | --------- | --- |
|               |        |            |      |        |     |      |      | that best    | separates | most              | data points | from | the rest. |     |
| more accurate | and    | reliable   | over | time.  |     |      |      |              |           |                   |             |      |           |     |
|               |        |            |      |        |     |      |      | 4) Real-Time |           | Anomaly Detection |             |      |           |     |
These more complex and accurate predictive models Continuous Monitoring: The models checked for new
offer
enabled the Financial Advisor Application to users transactions in real time, comparing them to the typical
exact and personalized financial advice, assisting them in pattern of activity as learned from the data. Any variations
| controlling | their financial |     | affairs | more | efficiently. | The | ap- |         |         |                 |     |             |     |           |
| ----------- | --------------- | --- | ------- | ---- | ------------ | --- | --- | ------- | ------- | --------------- | --- | ----------- | --- | --------- |
|             |                 |     |         |      |              |     |     | greater | than 5% | were considered |     | significant | and | marked as |
plicationofmodernmachinelearningalgorithmsguaranteed
outliers.
thepredictions’accuracyandspecificity,thusimprovingthe
general usability of the product. Alert Generation: If an abnormality is observed, the
|            |           |     |     |     |     |     |     | system | triggers | an alert, | and the | user is | notified | to confirm |
| ---------- | --------- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | ------- | ------- | -------- | ---------- |
| S. Anomaly | Detection |     |     |     |     |     |     |        |          |           |         |         |          |            |
theobservation.Thisalertcontainedinformationsuchasthe
Identifying abnormalities in transactions that may show amount, merchant, and transaction time to enable a user to
signs of fraud or any other unusual activity is essential. authenticate or deny the transaction.
| This is a        | process in | which | machine     | learning | algorithms |     | are    |         |          |      |     |     |     |     |
| ---------------- | ---------- | ----- | ----------- | -------- | ---------- | --- | ------ | ------- | -------- | ---- | --- | --- | --- | --- |
|                  |            |       |             |          |            |     |        | 5) User | Feedback | Loop |     |     |     |     |
| used to identify | instances  |       | of spending |          | that are   | out | of the |         |          |      |     |     |     |     |
ordinary[23].Here’sadetailedbreakdownofourapproach Verification Process: Customers were notified of the
to anomaly detection: marked transactions. If a user identified a transaction as

| 12  | First | Author, | Samir | Bader. | Second | Author, | Ramzi | Haraty |     |     |     |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
genuine, the model decreased its false positive rate through of their interests and needs, hence achieving the company’s
| parameter   | changes. | On     | the other   | hand, | if  | the   | particular | goals. |     |     |     |     |     |     |
| ----------- | -------- | ------ | ----------- | ----- | --- | ----- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| transaction | was      | deemed | fraudulent, | then  | the | model | became     |        |     |     |     |     |     |     |
more sensitive toward patterns of the same kind. 2) Merchant Matching
|     |     |     |     |     |     |     |     | Merchant | Categorization: |     | MCC | codes | and other | at- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | --- | ----- | --------- | --- |
ModelRefinement:Theusers’inputwasregular,allow- tributes of merchants include location, kinds of products,
ing the models to be adjusted and fine-tuned over time and offer.
|     |     |     |     |     |     |     |     | and promotions | they |     | This can | be useful | in  | pairing |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | --- | -------- | --------- | --- | ------- |
decreasing false positives and negatives. users with the appropriate merchants based on their prefer-
ences.
| 6) Evaluation |     | Metrics |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Precision and Recall: These metrics were employed to Collaborative Filtering: The application utilizes collab-
measure the performance of the anomaly detection models. orative filtering algorithms to search for other merchants
Specificity is the number of positive detections that are frequented by users with similar habits. This method uses
true positives out of all the positives detected. At the same the users’ buying patterns to recommend new merchants to
time, sensitivity is the number of actual positives marked them based on their purchasing activities.
as positives.
|     |     |     |     |     |     |     |     | 3) Personalized | Offers |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | --- | --- | --- | --- | --- |
ROC-AUC Score: The Receiver Operating Character- Dynamic Offer Generation: The application provides
istic—Area Under Curve (ROC-AUC) score was used to personalized offers to users for their purchases and to
measure the performance of the models in discriminating merchants who have subscribed to it. The offers include
| between | normal | and abnormal |     | transactions. |     |     |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
coupons,vouchers,cash-backoptions,andloyaltyprograms
|                |     |                |     |     |     |     |     | based on usage. |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 7) Integration |     | and Deployment |     |     |     |     |     |                 |     |     |     |     |     |     |
SystemIntegration:Theanomalydetectionmodelswere Contextual Recommendations: The application makes
deployedtotheFinancialAdvisorApplication’sbackendfor recommendationsbasedonuserinteractionandactivity.For
use in the advisory process. This included establishing data instance, if the user has recently purchased food items, it
feeds for real-time tracking and transactions occurring in may recommend coupons from nearby grocery stores.
| the business | environment. |     |        |      |        |                 |     |                |          |             |     |         |           |     |
| ------------ | ------------ | --- | ------ | ---- | ------ | --------------- | --- | -------------- | -------- | ----------- | --- | ------- | --------- | --- |
|              |              |     |        |      |        |                 |     | 4) Machine     | Learning | Models      |     |         |           |     |
| Deployment:  |              | The | models | were | tested | in a production |     |                |          |             |     |         |           |     |
|              |              |     |        |      |        |                 |     | Recommendation |          | Algorithms: | To  | improve | recommen- |     |
environmentwheretheyactedasawatchdog,analyzinguser dation accuracy, several machine learning models, such as
transactions and highlighting any suspicious activity to the matrixfactorizationanddeeplearning,areemployed.These
user for further validation. models are built based on user interactions and can update
|     |           |         |             |     |              |     |      | themselves | with better | predictions. |     |     |     |     |
| --- | --------- | ------- | ----------- | --- | ------------ | --- | ---- | ---------- | ----------- | ------------ | --- | --- | --- | --- |
| The | Financial | Advisor | Application |     | successfully |     | used |            |             |              |     |     |     |     |
powerful and efficient algorithms to detect such anomalies, Real-Time Processing: It adapts the recommendations
offering users more control and security. It also enabled to the users’ real-time transaction data to provide the most
| users to     | be notified | of           | any malicious   |              | activities |     | and take |                          |     |             |              |                 |     |     |
| ------------ | ----------- | ------------ | --------------- | ------------ | ---------- | --- | -------- | ------------------------ | --- | ----------- | ------------ | --------------- | --- | --- |
|              |             |              |                 |              |            |     |          | suitable recommendations |     |             | at the right | time.           |     |     |
| necessary    | action      | to safeguard |                 | their money. |            |     |          |                          |     |             |              |                 |     |     |
|              |             |              |                 |              |            |     |          | 5) User Feedback         |     | Loop        |              |                 |     |     |
| T. AI-Driven |             | Merchant     | Recommendations |              |            |     |          |                          |     |             |              |                 |     |     |
|              |             |              |                 |              |            |     |          | Interaction              | and | Engagement: | The          | recommendations |     | al- |
The Financial Advisor Application uses AI to ana- low users to accept or reject offers. This feedback helps
lyze the user’s transaction history and select appropriate fine-tune the recommendation systems.
| merchant  | offers      | to improve | user     | satisfaction |         | and     | achieve |            |           |     |                       |     |     |         |
| --------- | ----------- | ---------- | -------- | ------------ | ------- | ------- | ------- | ---------- | --------- | --- | --------------------- | --- | --- | ------- |
|           |             |            |          |              |         |         |         | Continuous | Learning: |     | These recommendations |     |     | are ad- |
| even more | significant |            | savings. | This         | feature | ensures | that it |            |           |     |                       |     |     |         |
provides subscribed merchants discounts and special deals justed based on users’ feedback and new transaction data
tailored to users’ needs [4]. Here’s a detailed breakdown of to keep the models current and valuable.
| our approach | to  | AI-driven | merchant |     | recommendations: |     |     |               |         |     |     |     |     |     |
| ------------ | --- | --------- | -------- | --- | ---------------- | --- | --- | ------------- | ------- | --- | --- | --- | --- | --- |
|              |     |           |          |     |                  |     |     | 6) Evaluation | Metrics |     |     |     |     |     |
1) Behavior Analysis Precision and Recall: These metrics show the recom-
Transaction History Analysis: The application can then mendationsystem’sefficacy.Precisionisdefinedastheratio
oftherelevantofferstoalltherecommendedoffers,whereas
| use this | information |     | to examine | users’ |     | spending | habits |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ---------- | ------ | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
offers
basedonprevioustransactions.Thismeansdeterminingthe recall is the ratio of the relevant recommended to the
offers.
| most common |     | products | bought,  | the most | popular     |     | merchant | pertinent total    |     |                   |     |                |     |     |
| ----------- | --- | -------- | -------- | -------- | ----------- | --- | -------- | ------------------ | --- | ----------------- | --- | -------------- | --- | --- |
| categories, | and | typical  | spending | by a     | cardholder. |     |          |                    |     |                   |     |                |     |     |
|             |     |          |          |          |             |     |          | User Satisfaction: |     | Self-administered |     | questionnaires |     | and |
Feature Extraction: Some extracted attributes include user feedback measure satisfaction with the recommenda-
transaction frequency, average spending per category, and tions. This qualitative data helps enhance the recommenda-
|             |       |      |              |     |          |        |         | tion activity. |     |     |     |     |     |     |
| ----------- | ----- | ---- | ------------ | --- | -------- | ------ | ------- | -------------- | --- | --- | --- | --- | --- | --- |
| transaction | time. | This | data assists | in  | creating | a user | profile |                |     |     |     |     |     |     |

International Journal of Computing and Digital Systems 13
7) Integration and Deployment the same ratio of normal and abnormal transactions, thus
SystemIntegration:Therecommendationengineisbuilt providing a fair environment for testing.
and incorporated into the Financial Advisor Application’s
3) Hyperparameter Tuning
backend. This involves setting up data pipelines to ingest
and process transaction data continuously. GridSearch:Itdeterminedthebesthyperparametersfor
each model to train and test on the dataset. We tuned the
Deployment: A production environment system actively hyperparameters of the models by evaluating them with
works in real-time to present users with merchant offers. predefined hyperparameters to determine which hyperpa-
rameters produced the best model performance.
With the help of AI-based merchant suggestions, the
Financial Advisor Application increases user engagement RandomSearch:Besidesthegridsearch,randomsearch
and saves more money by providing a personalized shop- was used to cover a more extensive range of hyperparame-
ping experience. This way, the users are presented with ters quickly and perhaps find better parameters.
relevant offers made available promptly, making managing
their financial resources more fruitful. 4) Real-Time Testing
Deployment in Production Environment: These models
U. Integration and Deployment
were then put into real-life production to determine how
We needed to assess the effectiveness of our predictive
they would fare when used under actual situations. This
and anomaly detection models incorporated into the Finan-
included constant practice and fine-tuning based on the
cial Advisor Application to guarantee that the results de-
exact data that was available.
livered were accurate and would improve the application’s
user experience. Here’s a detailed breakdown of our model UserFeedbackIntegration:Theusers’abilitytoconfirm
evaluation approach: Here’s a detailed breakdown of our or correct the predictions and anomalies the models flag is
model evaluation approach: valuable feedback for model improvement.
1) Evaluation Metrics 5) Performance Monitoring
Mean Absolute Percentage Error (MAPE): MAPE was
Continuous Evaluation: The models incorporated real-
usedtoassessthefitnessofthepredictivemodelsdeveloped
time data to facilitate optimum performance throughout the
in this study. The average absolute difference between the
process. Measures such as the accuracy rate, the rate of
predicted and actual values shows how well the model
detecting anomalies, and the user satisfaction index were
performs. A lower value of MAPE is preferable, which
checked frequently.
means the accuracy of the prediction is high.
Automated Alerts: To ensure that the model does not
PrecisionandRecall:Regularityanalysiswasperformed
drastically change its performance, an alert system was
using precision and recall. Precision refers to the ratio of
developed to notify the developers of any such changes to
correctly identified positive cases to the total number of
take appropriate measures.
cases identified as abnormal. In contrast, recall refers to
the ratio of actual anomalous cases detected to the total 6) Model Retraining
number of strange cases in the data set. The first set of Periodic Retraining: The models were fine-tuned with
metrics,precisionandrecall,shouldbehightosuggestthat new datasets to capture more recent trends and tendencies
anomaly detection is effective. in the users’ activity. This ensured that the models did not
become outdatedbutretained theiraccuracy andusefulness
ROC-AUC Score: The Receiver Operating Characteris-
in the organization.
tic—Area Under Curve (ROC-AUC) was used to evaluate
the overall performance of the anomaly detection models. Adaptive Learning: The models were expected to be
The ROC-AUC score measures how well the model dis- adaptable in making predictions and detecting anomalies
criminates between normal and abnormal transactions, and from the most recent user interactions and feedback.
the closer to 1 the score is, the better the model performs
To achieve this, the Financial Advisor Application uti-
2) Cross-Validation
lized a comprehensive evaluation strategy to determine
K-FoldCross-Validation:Thistechniquewasadoptedto
whetherthemodelsdevelopedwithinthesystemwereaccu-
assess the performance of the predictive models. The given rate, reliable, and capable of offering personalized financial
datasetofsampleswaspartitionedintoksets,andthemodel
advice. This approach enriched the user experience and
was trained on k-1 sets and tested on the remaining set. helpedtobuildconfidenceintheapplication’seffectiveness
This was done k times, and in each iteration, one of the
in managing and protecting economic transactions.
subgroups was used as a test set. The average of all the k
trials offered an excellent estimate of the model’s accuracy. 7) Scenarios
The financial advisor application is designed to provide
Stratified Sampling: To detect the anomalies, stratified
personalized and intelligent financial support to its users
sampling allowed the training and test data sets to be in

| 14  | First | Author, | Samir | Bader. | Second | Author, | Ramzi | Haraty |     |     |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- |
Figure13.Thetransformers
Figure12
| by leveraging | advanced  |           | technologies |            | such      | as anomaly | de-   |     |     |     |     |     |     |
| ------------- | --------- | --------- | ------------ | ---------- | --------- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| tection,      | sentiment | analysis, | and          | predictive | modeling. |            | These |     |     |     |     |     |     |
features aim to enhance user experience, promote financial Figure14.TheTCN
| well-being, | and | ensure | security | through | actionable |     | insights |     |     |     |     |     |     |
| ----------- | --- | ------ | -------- | ------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
and recommendations.
|     |     |     |     |     |     |     |     | pattern with | a time lag | and fluctuations |     | in the lines | other |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ---------------- | --- | ------------ | ----- |
Below are real-world scenarios that demonstrate the thanwhatwaspredictedbythemodel.Thisiscommonplace
application’s capabilities in various aspects of financial inreal-worldforecastingscenarioswhereitisimpossibleto
| management, | including |     | fraud | prevention, | budgeting, |     | mer- |               |            |     |     |     |     |
| ----------- | --------- | --- | ----- | ----------- | ---------- | --- | ---- | ------------- | ---------- | --- | --- | --- | --- |
|             |           |     |       |             |            |     |      | get a perfect | score [5]. |     |     |     |     |
chantrecommendations,predictiveanalysis,andsentiment-
|                 |     |      |          |            |     |     |        | 2) Temporal | Convolutional | Networks | (TCN) |     |     |
| --------------- | --- | ---- | -------- | ---------- | --- | --- | ------ | ----------- | ------------- | -------- | ----- | --- | --- |
| based guidance. |     | Each | scenario | highlights | how | the | system |             |               |          |       |     |     |
identifies user-specific needs and delivers tailored solutions Figure14displaystheresultsoftheTCNmodelwithout
to address them effectively. employing sentiment analysis. A MAPE means that the
|     |     |     |     |     |     |     |     | model is, | on average, right | in  | its predictions, | given | by the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | ---------------- | ----- | ------ |
4. RESULTSANDANALYSIS 5th percentile. It is also important to note that these figures
| A. Without | Sentiment | Analysis |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
areonly5%awayfromtheactualspending.Itindicatesthat
1) Transformer Model Performance themodelisagoodpredictorasmostvaluesareclosetothe
Figure 13 shows the Transformer model’s performance actual expenditure [5]. The model can monitor expenditure
|                |            |             |          |          |            |             |        | patterns   | and estimate future | costs | almost | accurately. |     |
| -------------- | ---------- | ----------- | -------- | -------- | ---------- | ----------- | ------ | ---------- | ------------------- | ----- | ------ | ----------- | --- |
| in predicting  | customer   |             | spending | behavior |            | without     | senti- |            |                     |       |        |             |     |
| ment analysis. |            | The overall | mean     | absolute |            | percentage  | is     |            |                     |       |        |             |     |
|                |            |             |          |          |            |             |        | 3) N-BEATS |                     |       |        |             |     |
| the average    | difference |             | between  | the      | calculated | theoretical |        |            |                     |       |        |             |     |
and observed values. Accuracy indicates the degree of the Figure 15 shows the accuracy of the N-BEATS model
model’s efficiency in predicting the opinion poll results. applied to customer spending prediction without sentiment
|               |      |            |     |         |     |        |          | analysis. | The MAPE shows | the         | average prediction |     | error of   |
| ------------- | ---- | ---------- | --- | ------- | --- | ------ | -------- | --------- | -------------- | ----------- | ------------------ | --- | ---------- |
| The forecasts | most | accurately |     | capture | the | actual | spending |           |                |             |                    |     |            |
|               |      |            |     |         |     |        |          | the model | in terms of    | expenditure | compared           | to  | the actual |
behavior [5].
|              |     |           |            |     |              |     |          | figure. This | study obtained | a high | accuracy | level. | As can |
| ------------ | --- | --------- | ---------- | --- | ------------ | --- | -------- | ------------ | -------------- | ------ | -------- | ------ | ------ |
| In addition, |     | the model | replicates |     | the customer |     | spending |              |                |        |          |        |        |

|     |     |     |     |     |     | International | Journal of | Computing | and | Digital Systems |     | 15  |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | --------- | --- | --------------- | --- | --- |
Figure15.N-BEATS
Figure16.Thetransformers
| be observed     | from           | the statistics, |              | the predicted    | values       | follow        |     |     |     |     |     |     |
| --------------- | -------------- | --------------- | ------------ | ---------------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- |
| a similar       | trend to       | the actual      | spending.    |                  |              |               |     |     |     |     |     |     |
| The             | predictive     | line shows      | a            | clear trend,     | which        | suggests      |     |     |     |     |     |     |
| that the        | model captures |                 | the mean     | spending         |              | level but not |     |     |     |     |     |     |
| the variation   | in the         | data.           | This may     | indicate         | that         | the model     |     |     |     |     |     |     |
| needs to        | be adjusted    | to              | address      | more significant |              | variability   |     |     |     |     |     |     |
| or that more    | inputs,        | such            | as sentiment |                  | information, | should        |     |     |     |     |     |     |
| be incorporated |                | into the        | model        | to enhance       | the          | accuracy of   |     |     |     |     |     |     |
| the forecasted  | spending       |                 | [5].         |                  |              |               |     |     |     |     |     |     |
| B. With         | Sentiment      | Analysis        | Included     |                  |              |               |     |     |     |     |     |     |
| 1) Transformer  |                | Model           | Performance  |                  |              |               |     |     |     |     |     |     |
| The             | figure below   |                 | presents     | the result       | of           | utilizing a   |     |     |     |     |     |     |
| Transformer     | model          | for             | customer     | spending         | forecasting  | with          |     |     |     |     |     |     |
the integration of sentiment analysis. This is in the range Figure17.TheTCN
| for the     | MAPE,          | which    | means    | that the        | error | between the |                     |          |              |                |        |              |
| ----------- | -------------- | -------- | -------- | --------------- | ----- | ----------- | ------------------- | -------- | ------------ | -------------- | ------ | ------------ |
| expected    | and the        | actual   | values   | is, on average, |       | the overall |                     |          |              |                |        |              |
|             |                |          |          |                 |       |             | prediction.         | The MAPE | denotes      | the difference |        | in the av-   |
| accuracy.   | This indicates |          | that the | forecasted      | value | is nearly   |                     |          |              |                |        |              |
|             |                |          |          |                 |       |             | erage error         | between  | the expected | and            | actual | values. This |
| as accurate | as the         | recorded | actual   | spending        | [9].  |             |                     |          |              |                |        |              |
|             |                |          |          |                 |       |             | type of recognition |          | is accurate  | and shows      | that   | the actual   |
Adding sentiment improves the model’s ability to esti- expenditure predictions are correct [9].
| mate spending, | which | is  | more accurate |     | than the | model that |     |     |     |     |     |     |
| -------------- | ----- | --- | ------------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
does not incorporate sentiment data. Figure 15 depicts the The introduction of sentiment analysis improves the
transformers. accuracy of model prediction and provides a better fit to
|             |               |     |             |       |          |         | the actual spending |     | data than | the results | obtained | without |
| ----------- | ------------- | --- | ----------- | ----- | -------- | ------- | ------------------- | --- | --------- | ----------- | -------- | ------- |
| 2) Temporal | Convolutional |     | Networks    | (TCN) |          |         | sentiment data.     |     |           |             |          |         |
| Figure      | 16 displays   |     | the results | of    | adopting | the TCN |                     |     |           |             |          |         |
model for predicting customer spending with the sentiment Including SA in the predictive models makes them
analysis element. The MAPE means that the predictions more accurate since it provides a closer estimate of the
madebythemodelareoffbythispercentagefromtheactual
|     |     |     |     |     |     |     | actual spending | pattern. | This | improvement | is evident | from |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ---- | ----------- | ---------- | ---- |
values on average. The accuracy indicates that the model the following findings: lower MAPE and higher accuracy
can somewhat capture the trend of expenditure fluctuations models when sentiment data is included. Adding sentiment
[9]. analysis to the applications is crucial in enhancing the
|     |     |     |     |     |     |     | solutions offered | to  | users in | the financial | domains. |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ------------- | -------- | --- |
Thesestatisticsshowhowthemodelusessentimentdata
to predict spending movements, which is indicated by the TheFinancialAdvisorApplicationcansuccessfullypre-
differencebetweentheexpectedandactualspendingtrends. dict the user’s expenses, monitor changes, and recommend
|             |               |     |          |       |     |     | relevant merchants, |     | thus improving | financial |     | literacy and |
| ----------- | ------------- | --- | -------- | ----- | --- | --- | ------------------- | --- | -------------- | --------- | --- | ------------ |
| 3) Temporal | Convolutional |     | Networks | (TCN) |     |     |                     |     |                |           |     |              |
usage.
| Figure          | 17 illustrates |     | the result | of an | N-BEATS  | model    |     |     |     |     |     |     |
| --------------- | -------------- | --- | ---------- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- |
| that integrates | sentiment      |     | analysis   | for   | customer | spending |     |     |     |     |     |     |

| 16  | First | Author, |     | Samir | Bader. Second | Author, | Ramzi | Haraty       |               |                    |        |               |      |          |
| --- | ----- | ------- | --- | ----- | ------------- | ------- | ----- | ------------ | ------------- | ------------------ | ------ | ------------- | ---- | -------- |
|     |       |         |     |       |               |         |       | terns. Our   | predictive    | analysis           | models | significantly |      | enhance  |
|     |       |         |     |       |               |         |       | financial    | planning      | accuracy           | by     | incorporating | deep | learning |
|     |       |         |     |       |               |         |       | models       | and sentiment | analysis           |        | to interpret  | user | emotions |
|     |       |         |     |       |               |         |       | and economic |               | behaviors.         |        |               |      |          |
|     |       |         |     |       |               |         |       | C. Impact    | of            | Sentiment Analysis |        | on Predictive |      | Accuracy |
•
|     |     |     |     |     |     |     |     | Mean | Absolute | Percentage |      | Error     | (MAPE) | improved     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---------- | ---- | --------- | ------ | ------------ |
|     |     |     |     |     |     |     |     | from | 10.5%    | to 7.8%    | when | sentiment |        | analysis was |
incorporated.
|     |     |     |     |     |     |     |     | • Root                                            | Mean | Squared          | Error      | (RMSE):      | o            | Transformer |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | ---- | ---------------- | ---------- | ------------ | ------------ | ----------- |
|     |     |     |     |     |     |     |     | Model:                                            |      | 0.062 o TCN      |            | Model: 0.074 |              | o N-BEATS   |
|     |     |     |     |     |     |     |     | Model:                                            |      | 0.057 (best      | performer) |              |              |             |
|     |     |     |     |     |     |     |     | • Predictiveaccuracywithina90%confidenceinterval: |      |                  |            |              |              |             |
|     |     |     |     |     |     |     |     | Achieved                                          |      | 88% alignment    |            | with actual  | user         | behavior,   |
|     |     |     |     |     |     |     |     | indicating                                        |      | high reliability |            | in financial | forecasting. |             |
Figure18.N-BEATS
Ourapproachoutperformsconventionalbudgetingappli-
cations,whichprimarilyrelyonstaticrule-basedalgorithms
5. DISCUSSIONANDCOMPARATIVEANALYSISs
|             |              |     |             |             |          |                |        | (e.g., Mint, | YNAB). | Unlike      | these         | traditional |      | systems, our  |
| ----------- | ------------ | --- | ----------- | ----------- | -------- | -------------- | ------ | ------------ | ------ | ----------- | ------------- | ----------- | ---- | ------------- |
| A. Anomaly  | Detection    |     | Performance |             | Analysis |                |        | models:      |        |             |               |             |      |               |
| The         | experimental |     | results     | demonstrate | the      | robustness     | of     |              |        |             |               |             |      |               |
| our anomaly | detection    |     | system,     | achieving   |          | an accuracy    | of     |              |        |             |               |             |      |               |
|             |              |     |             |             |          |                |        | • Analyze    |        | historical  | transactional |             | data | in real-time, |
| 92%, with   | a precision  |     | of 90%,     | recall      | of 85%,  | and            | an F1- |              |        |             |               |             |      |               |
|             |              |     |             |             |          |                |        | adjusting    |        | predictions | dynamically.  |             |      |               |
| score of    | 87.5%.       | The | ROC-AUC     | score       | of       | 0.93 indicates | a      |              |        |             |               |             |      |               |
strong ability to distinguish between normal and fraudulent • Integrate deep learning techniques (Transformer,
transactions. These results suggest that our approach pro- TCN, N-BEATS) to capture complex temporal de-
videsasubstantialimprovementoverconventionalfinancial pendencies in financial transactions.
| fraud detection |        | systems, | which | typically |     | report precision |     |            |     |                |     |          |           |         |
| --------------- | ------ | -------- | ----- | --------- | --- | ---------------- | --- | ---------- | --- | -------------- | --- | -------- | --------- | ------- |
|                 |        |          |       |           |     |                  |     | • Leverage |     | user sentiment |     | analysis | to factor | in psy- |
| and recall      | values | in the   | range | of 70–80  |     |                  |     |            |     |                |     |          |           |         |
chologicalinfluencesonfinancialdecisions,afeature
|     |     |     |     |     |     |     |     | largely | absent | in current |     | fintech applications. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ---------- | --- | --------------------- | --- | --- |
Akeycontributingfactortothisperformancegainisour
| multi-model | anomaly |     | detection | approach, |     | which leverages |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | --------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
advanced machine learning techniques, including Isolation The reduction in prediction error by 25% compared to
Forests and One-Class SVM. Unlike conventional fraud rule-based systems highlights the transformative impact of
detectionmechanismsthatrelyonstaticrule-basedsystems, AI-driven financial forecasting in personal finance manage-
| ourmethodadaptsdynamicallytonewtransactionpatterns, |       |           |     |           |           |           |     | ment.         |     |               |         |           |     |     |
| --------------------------------------------------- | ----- | --------- | --- | --------- | --------- | --------- | --- | ------------- | --- | ------------- | ------- | --------- | --- | --- |
| reducing                                            | false | positives | and | enhancing | detection | accuracy. |     |               |     |               |         |           |     |     |
|                                                     |       |           |     |           |           |           |     | D. Comparison |     | with Existing | Fintech | Solutions |     |     |
• Our model, in contrast, adapts to evolving finan- To provide a comprehensive evaluation, we compared
cial fraud patterns, leveraging deep learning-based oursystem’sperformance,intable1,againstexistingfintech
anomaly detection. solutionsacrosstwokeydimensions:anomalydetectionand
|             |     |        |     |             |         |     |        | predictive | analysis. |     |     |     |     |     |
| ----------- | --- | ------ | --- | ----------- | ------- | --- | ------ | ---------- | --------- | --- | --- | --- | --- | --- |
| • Precision |     | at 90% | vs. | traditional | 70–80%: |     | Higher |            |           |     |     |     |     |     |
precisionindicatesfewerfalsepositives,ensuringthat
| legitimate |     | transactions |     | are not | incorrectly | flagged. |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------ | --- | ------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
• Recallat85%vs.traditional70–80%:Ahigherrecall
| ensures |               | that the | system     | captures | more     | actual        | fraud- |     |     |     |     |     |     |     |
| ------- | ------------- | -------- | ---------- | -------- | -------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| ulent   | transactions, |          | minimizing |          | the risk | of undetected |        |     |     |     |     |     |     |     |
fraud.
| Furthermore,  |             | our       | approach    | enables     | real-time | anomaly       |        |     |     |     |     |     |     |     |
| ------------- | ----------- | --------- | ----------- | ----------- | --------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| detection     | without     | requiring |             | constant    | human     | intervention, |        |     |     |     |     |     |     |     |
| making        | it scalable | for       | high-volume |             | financial | environments. |        |     |     |     |     |     |     |     |
| B. Predictive |             | Financial | Analysis    | Performance |           |               |        |     |     |     |     |     |     |     |
| Financial     | forecasting |           | is          | inherently  | complex   | due           | to the |     |     |     |     |     |     |     |
stochasticnatureofmarketbehaviorsanduserspendingpat-

|     |     |     |     |     | International | Journal |     | of Computing | and | Digital | Systems |     | 17  |
| --- | --- | --- | --- | --- | ------------- | ------- | --- | ------------ | --- | ------- | ------- | --- | --- |
Figure19.Anomalydetectioncomparison
Figure20.Predictiveanalysiscomparison
Existing
|     |     | Traditional |         |     |     |     |                   |     | &       |     |              |     |     |
| --- | --- | ----------- | ------- | --- | --- | --- | ----------------- | --- | ------- | --- | ------------ | --- | --- |
|     |     |             | Budget- |     |     | E.  | Key Contributions |     | Broader |     | Implications |     |     |
Bank-
ing Apps Our Ap- The findings of this research underscore several signifi-
| Feature |     | ing/Fraud |        |     |           |      |               |     |              |           |     |          |          |
| ------- | --- | --------- | ------ | --- | --------- | ---- | ------------- | --- | ------------ | --------- | --- | -------- | -------- |
|         |     |           |        |     |           | cant | contributions |     | to AI-driven | financial |     | advisory | systems: |
|         |     |           | (Mint, |     | plication |      |               |     |              |           |     |          |          |
Detection
YNAB,
Systems
|     |     |     | etc.) |     |     |     | 1) Advanced |     | AI-driven | anomaly | detection: |     | Our ap- |
| --- | --- | --- | ----- | --- | --- | --- | ----------- | --- | --------- | ------- | ---------- | --- | ------- |
Anomaly De- proach significantly improves financial transaction
|     |     |     | Not | ap- |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tection Preci- 70–80% 90% security, reducing false positives while enhancing
plicable
|     |     |     |     |     |     |     | fraud | detection | accuracy. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | --- | --- | --- | --- |
sion
Anomaly De- 2) Integration of sentiment analysis into financial fore-
|     |     |     | Not | ap- |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tection Preci- 70–80% 85% casting: Demonstrates the tangible benefits of emo-
plicable
| sion |     |     |     |     |     |     | tionalinsightsinfinancialdecision-making,reducing |     |           |      |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --------- | ---- | --- | --- | --- |
|      |     |     |     |     |     |     | prediction                                        |     | errors by | 25%. |     |     |     |
Deep
|     |     |     |     |     |     |     | 3) Use | of deep | learning | architectures |     | for | predictive |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | -------- | ------------- | --- | --- | ---------- |
Learning
Financial Rule- modeling: Unlike existing budgeting applications,
|             |     | Statistical |       |     | (Trans- |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Forecasting |     |             | Based |     |         |     |     |     |     |     |     |     |     |
Models former, our system leverages sophisticated models (Trans-
| Method |     |     | Systems |     |         |     |             |           |               |           |            |           |        |
| ------ | --- | --- | ------- | --- | ------- | --- | ----------- | --------- | ------------- | --------- | ---------- | --------- | ------ |
|        |     |     |         |     | TCN, N- |     | former,     | TCN,      | N-BEATS)      |           | to enhance | financial | plan-  |
|        |     |     |         |     | BEATS)  |     | ning        | accuracy. |               |           |            |           |        |
|        |     |     |         |     |         |     | 4) Scalable |           | and adaptable | financial |            | advisory  | frame- |
Incorporation
work:Developedusing.NETCore6,allowingseam-
| of Sentiment |     | No  | No     |     | Yes  |     |                                                  |     |     |     |     |     |     |
| ------------ | --- | --- | ------ | --- | ---- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| Analysis     |     |     |        |     |      |     | lessintegrationofnewfinancialtoolsandthird-party |     |     |     |     |     |     |
| MAPE         |     |     |        |     |      |     | extensions.                                      |     |     |     |     |     |     |
|              |     | Not | ap-    |     |      |     |                                                  |     |     |     |     |     |     |
| (Prediction  |     |     | 10–12% |     | 7.8% |     |                                                  |     |     |     |     |     |     |
plicable By addressing the limitations of conventional financial
Error)
|     |     |     |     |     |     | advisory |     | solutions, | our work | paves | the | way | for more |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | -------- | ----- | --- | --- | -------- |
Real-Time
Limited No Yes intelligent, adaptive, and user-centric financial applications
Adaptability
|     |     |     |     |     |          | that | can    | dynamically | evolve | with | users’ | financial | behaviors |
| --- | --- | --- | --- | --- | -------- | ---- | ------ | ----------- | ------ | ---- | ------ | --------- | --------- |
|     |     |     |     |     | Yes (via |      |        |             |        |      |        |           |           |
|     |     |     |     |     |          | and  | market | trends.     |        |      |        |           |           |
.NET
Extensibility
|     |     | Limited | No  |     | Core 6 |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
& Scalability However, it is essential to note that the conclusion
frame-
madehereissomewhatdissimilartothepositivesentiments
work)
basedontheassumptionofthetotalefficiencyofsentiment
|                  |     |          |            |     |             | analysis |     | in enhancing | the | model | predictions. | Notably, | the |
| ---------------- | --- | -------- | ---------- | --- | ----------- | -------- | --- | ------------ | --- | ----- | ------------ | -------- | --- |
| This comparative |     | analysis | reinforces | the | superiority |          |     |              |     |       |              |          |     |
of our approach in terms of accuracy, adaptability, and TCN model reveals that including sentiment data does not
predictive power. Unlike existing applications that rely constantlyimprovethepredictiveperformance,whichraises
|                    |             |              |                         |            |             | the         | question    | of      | whether sentiment |          | data     | that drives | market |
| ------------------ | ----------- | ------------ | ----------------------- | ---------- | ----------- | ----------- | ----------- | ------- | ----------------- | -------- | -------- | ----------- | ------ |
| on predefined      | heuristics, |              | our system continuously |            | evolves     |             |             |         |                   |          |          |             |        |
|                    |             |              |                         |            |             | responses   |             | aligns  | with the          | inherent | forecast | mechanisms  | of     |
| based on real-time |             | data streams | and user                | behavioral | trends.     |             |             |         |                   |          |          |             |        |
|                    |             |              |                         |            |             | specific    | models      |         | [24], [25].       |          |          |             |        |
| Figures            | 19 and      | 20 provide   | a comparison            | of         | the various |             |             |         |                   |          |          |             |        |
|                    |             |              |                         |            |             | F.          | Limitations | and     | Future            | Work     |          |             |        |
| models against     | anomaly     | detection    | and                     | predictive | analysis.   |             |             |         |                   |          |          |             |        |
|                    |             |              |                         |            |             |             | Despite     | these   | promising         | results, | some     | challenges  | and    |
|                    |             |              |                         |            |             | limitations |             | remain: |                   |          |          |             |        |

| 18  | First | Author, | Samir | Bader. | Second |     | Author, Ramzi | Haraty |     |     |     |     |     |     |     |
| --- | ----- | ------- | ----- | ------ | ------ | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
• Generalization across diverse financial behaviors: deployment at scale, integrating robust mechanisms for
Whileourmodelsperformwellonexperimentaldata, handling unstructured data, and conducting extensive real-
future work should explore their adaptability across world testing to address deployment challenges. Further
different user demographics and financial habits. researchcouldalsoexplorehybridapproachesthatcombine
|                 |     |             |     |      |          |        |     | machine | learning | with | domain-specific |     | financial | expertise |     |
| --------------- | --- | ----------- | --- | ---- | -------- | ------ | --- | ------- | -------- | ---- | --------------- | --- | --------- | --------- | --- |
| • Computational |     | efficiency: |     | Deep | learning | models | re- |         |          |      |                 |     |           |           |     |
toenhancetheinterpretabilityandreliabilityofpredictions.
| quire | significant |     | computational |     | resources. |     | Future op- |               |     |                   |     |     |           |              |     |
| ----- | ----------- | --- | ------------- | --- | ---------- | --- | ---------- | ------------- | --- | ----------------- | --- | --- | --------- | ------------ | --- |
|       |             |     |               |     |            |     |            | By addressing |     | these challenges, |     | the | potential | of AI-driven |     |
timizations, including model pruning and edge AI financial applications to deliver timely, personalized, and
efficiency.
deployment, will be explored to improve secure financial recommendations can be fully realized,
|     |     |     |     |     |     |     |     | advancing | both | user experience |     | and | the financial | services |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --------------- | --- | --- | ------------- | -------- | --- |
•
Usertrust&adoption:WhileAI-drivenfinancialrec-
sector.
| ommendations |          | improve        |        | accuracy,   | user | trust   | remains  |            |     |     |     |     |     |     |     |
| ------------ | -------- | -------------- | ------ | ----------- | ---- | ------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| a            | critical | factor.        | Future | studies     | will | examine | user     | References |     |     |     |     |     |     |     |
| perception,  |          | trust-building |        | strategies, |      | and     | human-AI |            |     |     |     |     |     |     |     |
[1] M.J.ZakiandW.MeiraJr,Dataminingandanalysis:fundamental
| interaction |     | in financial |     | decision-making. |     |     |     |                        |     |     |                                |     |     |     |     |
| ----------- | --- | ------------ | --- | ---------------- | --- | --- | --- | ---------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- |
|             |     |              |     |                  |     |     |     | conceptsandalgorithms. |     |     | CambridgeUniversityPress,2014. |     |     |     |     |
6. CONCLUSION [2] I.Goodfellow,Y.Bengio,andA.Courville,Deeplearning. MIT
| This           | research        | analyzed      | the        | performance    |             | of recent | ma-       | Press,2016.     |     |               |      |         |         |               |     |
| -------------- | --------------- | ------------- | ---------- | -------------- | ----------- | --------- | --------- | --------------- | --- | ------------- | ---- | ------- | ------- | ------------- | --- |
| chine learning |                 | models,       | such       | as transformer |             | models,   | TCN,      |                 |     |               |      |         |         |               |     |
|                |                 |               |            |                |             |           |           | [3] F. Chollet, |     | Deep learning | with | Python. | Manning | Publications, |     |
| and N-BEATS,   |                 | in predicting |            | customer       | spending    |           | patterns  |                 |     |               |      |         |         |               |     |
| offering       |                 |               |            |                |             |           |           | 2017.           |     |               |      |         |         |               |     |
| and            | tailored        |               | solutions. | By             | integrating |           | sentiment |                 |     |               |      |         |         |               |     |
| analysis,      | we demonstrated |               | how        | these          | models      | process   | high-     |                 |     |               |      |         |         |               |     |
[4] J.Heaton,N.Polson,andJ.Witte,“Deeplearningforfinance:deep
| dimensional | data, | improve |     | forecasting | accuracy, |     | and en- |              |     |                    |     |        |             |     |           |
| ----------- | ----- | ------- | --- | ----------- | --------- | --- | ------- | ------------ | --- | ------------------ | --- | ------ | ----------- | --- | --------- |
|             |       |         |     |             |           |     |         | portfolios,” |     | Applied Stochastic |     | Models | in Business | and | Industry, |
hance financial advisory capabilities. The Transformer vol.33,no.1,pp.3–12,2017.
| model’s | elasticity | in  | handling | varied | inputs, | particularly |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | -------- | ------ | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] D.M.Nelson,A.C.Pereira,andR.A.deOliveira,“Stockmarket’s
| sentiment        | data,  | allowed        | it to       | capture  | long-term  |     | dependen-  |                                                      |          |            |      |      |        |            |         |
| ---------------- | ------ | -------------- | ----------- | -------- | ---------- | --- | ---------- | ---------------------------------------------------- | -------- | ---------- | ---- | ---- | ------ | ---------- | ------- |
|                  |        |                |             |          |            |     |            | price                                                | movement | prediction | with | lstm | neural | networks,” | in IEEE |
| cies and         | subtle | changes        | in customer |          | sentiment, |     | making it  |                                                      |          |            |      |      |        |            |         |
|                  |        |                |             |          |            |     |            | InternationalJointConferenceonNeuralNetworks(IJCNN). |          |            |      |      |        |            | IEEE,   |
| highly effective |        | for predicting |             | spending | patterns.  |     | Similarly, |                                                      |          |            |      |      |        |            |         |
2017,pp.1419–1426.
theTCNmodelandN-BEATSmodelshowedsignificanten-
hancementsinperformancewhencombinedwithsentiment
[6] M.Rezaei,M.R.F.Sani,andS.M.Homayouni,“Deeplearning-
basedstockmarketprediction,”IEEEAccess,vol.8,pp.124408–
| analysis, | with | the latter | excelling | in  | breaking | down | time- |     |     |     |     |     |     |     |     |
| --------- | ---- | ---------- | --------- | --- | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
124422,2020.
| series data | into     | trends    | and | seasonality | for | more | detailed |     |     |     |     |     |     |     |     |
| ----------- | -------- | --------- | --- | ----------- | --- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| customer    | behavior | analysis. |     |             |     |      |          |     |     |     |     |     |     |     |     |
[7] A.Esteva,B.Kuprel,R.A.Novoa,J.Ko,S.M.Swetter,H.M.Blau,
andS.Thrun,“Dermatologist-levelclassificationofskincancerwith
| Our         | findings | highlight | the | transformative |        | potential | of     |      |        |            |         |           |     |           |          |
| ----------- | -------- | --------- | --- | -------------- | ------ | --------- | ------ | ---- | ------ | ---------- | ------- | --------- | --- | --------- | -------- |
|             |          |           |     |                |        |           |        | deep | neural | networks,” | Nature, | vol. 542, | no. | 7639, pp. | 115–118, |
| integrating | advanced | machine   |     | learning       | models | with      | senti- |      |        |            |         |           |     |           |          |
2017.
| ment analysis |                | for comprehending |           |                  | customer  | behavior | and   |        |          |             |               |                |             |           |          |
| ------------- | -------------- | ----------------- | --------- | ---------------- | --------- | -------- | ----- | ------ | -------- | ----------- | ------------- | -------------- | ----------- | --------- | -------- |
| providing     | individualized |                   | financial | recommendations. |           |          | These |        |          |             |               |                |             |           |          |
|               |                |                   |           |                  |           |          |       | [8] A. | Agrawal, | J. S. Gans, | and           | A. Goldfarb,   | “Prediction | machines: |          |
|               |                |                   |           |                  |           |          |       | the    | simple   | economics   | of artificial | intelligence,” |             | Harvard   | Business |
| models        | not only       | improve           | customer  |                  | financial | planning | but   |        |          |             |               |                |             |           |          |
Review,2018.
alsoenablemerchantstobettertargetprospectivecustomers
| based on | transaction |     | histories | and | spending | habits, | thus |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --------- | --- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
[9] J.Bollen,H.Mao,andX.Zeng,“Twitter’smoodpredictsthestock
| creating | a mutually | beneficial |     | ecosystem. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
market,”JournalofComputationalScience,vol.2,no.1,pp.1–8,
2011.
| Despite     | these   | promising |        | results,  | there | are several | limi-     |     |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | ------ | --------- | ----- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| tations and | avenues | for       | future | research. | One   | key         | challenge |     |     |     |     |     |     |     |     |
[10] V.KumarandD.Shah,“Buildingandsustainingprofitablecustomer
lies in scalability—while the models performed well in loyalty for the 21st century,” Journal of Retailing, vol. 80, no. 4,
controlledenvironments,theirefficiencyandresponsiveness pp.317–329,2004.
| in handling | large-scale, |                | real-world |                 | financial | data       | streams |               |          |                |           |             |         |                 |     |
| ----------- | ------------ | -------------- | ---------- | --------------- | --------- | ---------- | ------- | ------------- | -------- | -------------- | --------- | ----------- | ------- | --------------- | --- |
|             |              |                |            |                 |           |            |         | [11] S. Rasp, | P.       | D. Dueben,     | S. Scher, | J. A.       | Weyn,   | S. Mouatadid,   | and |
| require     | further      | investigation. |            | Additionally,   |           | the models | pri-    |               |          |                |           |             |         |                 |     |
|             |              |                |            |                 |           |            |         | N.            | Thuerey, | “Weatherbench: |           | a benchmark | dataset | for data-driven |     |
| marily rely | on           | structured     | and        | semi-structured |           | data;      | extend- |               |          |                |           |             |         |                 |     |
weatherforecasting,”QuarterlyJournaloftheRoyalMeteorological
| ing their | capabilities |     | to process | unstructured |     |     | data, such |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ---------- | ------------ | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Society,vol.146,no.730,pp.370–385,2020.
| as textual | descriptions |     | or social | media | sentiment, |     | remains |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --------- | ----- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
a critical area for development. Another concern is the [12] R. Carbonneau, K. Laframboise, and R. Vahidov, “Application of
deployment of these systems in real-world settings, where machinelearningtechniquesforsupplychaindemandforecasting,”
|             |     |               |     |          |                  |     |     | European | Journal | of  | Operational | Research, |     | vol. 184, no. | 3, pp. |
| ----------- | --- | ------------- | --- | -------- | ---------------- | --- | --- | -------- | ------- | --- | ----------- | --------- | --- | ------------- | ------ |
| issues such | as  | data privacy, |     | security | vulnerabilities, |     | and |          |         |     |             |           |     |               |        |
1140–1154,2008.
| compliance | with | financial | regulations |     | must | be  | addressed |     |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | ----------- | --- | ---- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
rigorously. [13] T.Young,D.Hazarika,S.Poria,andE.Cambria,“Recenttrendsin
|     |     |     |     |     |     |     |     | deep | learning-basednatural |     | language |     | processing,” | IEEE Computa- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------------- | --- | -------- | --- | ------------ | ------------- | --- |
Future work should focus on refining these models for tionalIntelligenceMagazine,vol.13,no.3,pp.55–75,2018.

|     |     |     | International | Journal | of Computing |     | and Digital | Systems |     |     | 19  |
| --- | --- | --- | ------------- | ------- | ------------ | --- | ----------- | ------- | --- | --- | --- |
[14] K.Sun,“Fine-tunedbertmodelsforsentimentanalysisinfinancial [21] P.Johnson,“Knowledgegraphsandsentimentanalysisfordecision
marketplaces,” Journal of AI Applications in Economics, vol. 13, supportinfintech,”AdvancedComputationalFinance,vol.7,no.2,
| no.3,pp.19–37,2023. |     |     |     | pp.88–104,2024. |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
[15] S.PatelandR.Kumar,“Predictiveanalyticsforbudgetplanningin
fintech,”DigitalFinanceAdvances,vol.11,no.2,pp.67–81,2022. [22] T. Sharma, “Challenges in deploying ai in fintech: a scalability
|     |     |     |     | perspective,” |     | Journal | of AI Ethics | in Finance, | vol. | 5, no. | 2, pp. |
| --- | --- | --- | --- | ------------- | --- | ------- | ------------ | ----------- | ---- | ------ | ------ |
101–115,2023.
[16] J.Lee,“Ai-drivenfrauddetectionindigitalpayments,”International
JournalofFinancialSecurity,vol.8,no.3,pp.23–40,2023.
|     |     |     |     | [23] V. | Chandola, | A. Banerjee, | and V. | Kumar, | “Anomaly | detection: | a   |
| --- | --- | --- | --- | ------- | --------- | ------------ | ------ | ------ | -------- | ---------- | --- |
[17] V.Ramachandran,“Blockchain-enhancedaifortransparentfinancial survey,”ACMComputingSurveys,vol.41,no.3,pp.1–58,2009.
systems,”JournalofBlockchainandAI,vol.10,no.1,pp.45–62,
2024.
|               |                     |                    |                | [24] M. | El Abaji | and            | R. A. Haraty, | “Enhancing    |             | bitcoin  | fore-   |
| ------------- | ------------------- | ------------------ | -------------- | ------- | -------- | -------------- | ------------- | ------------- | ----------- | -------- | ------- |
|               |                     |                    |                | cast    | accuracy | by integrating |               | ai, sentiment | analysis,   |          | and fi- |
| [18] Y. Chen, | “Sentiment analysis | in mobile banking: | enhancing user |         |          |                |               |               |             |          |         |
|               |                     |                    |                | nancial | models.” | Journal        | of Computing  |               | and Digital | Systems. |         |
experience through ai,” Journal of Financial Technology, vol. 12, http://dx.doi.org/10.12785/ijcds/1571026011,
| no.1,pp.34–49,2024. |     |     |     |     |     |     |     |     | vol. 17, | no. 1, | pp. 1– |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ |
15,2025.
[19] R.Gupta,“Integratingsentimentanalysiswithtransactiondatafor
merchantrecommendations,”FintechInnovationsQuarterly,vol.9,
|     |     |     |     | [25] R. | A. Haraty | and S. | Sobeh, “Unveiling |     | insights | from | unstruc- |
| --- | --- | --- | --- | ------- | --------- | ------ | ----------------- | --- | -------- | ---- | -------- |
no.4,pp.78–92,2023. tured wealth: A comparative analysis of clustering techniques on
|     |     |     |     | blockchain | cryptocurrency |     | data,” | Journal of | Advances | in Comput- |     |
| --- | --- | --- | --- | ---------- | -------------- | --- | ------ | ---------- | -------- | ---------- | --- |
[20] H.Iqbal,“Combiningtcnandn-beatsmodelsforfinancialforecast- ingandEngineering,http://dx.doi.org/10.21622/ACE.2024.04.1.698,
ing,”AIandFinanceJournal,vol.15,no.3,pp.56–71,2022. vol.4,no.1,pp.1–43,2024.