---
conversion_metadata:
  converted_at: "2026-10-12T07:50:04Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Z. Zhang & Lu, 2026.pdf"
  source_pdf_sha256: "f9bfe3fe5a3fc233898173e13c2d21293bdb54391460782d2e9e010eba8f67e0"
  page_count: 36
  markdown_char_count: 175902
---

Eng. Sci., 2026, 41, 2245
..
Engineered Science
DOI: https://dx.doi.org/10.30919/es2245
Artificial Intelligence-Driven Transformation in Financial
Technology: Applications, Agents and Challenges
Zhizhou Zhang1,2,* and Meiqi Lu3,*
Abstract
Artificial intelligence (AI) has become a pivotal force in the financial technology (fintech) sector, reshaping services through
enhanced automation, improved efficiency, and personalization. The integration of sophisticated AI models, however,
introduces significant challenges concerning data privacy, algorithmic bias, and a lack of transparency, which necessitates a
systematic and comprehensive evaluation of the field. This review provides a holistic synthesis of the current landscape,
introducing a structured taxonomy of AI applications that ranges from foundational machine learning in areas like credit
scoring and fraud detection to advanced autonomous agents capable of dynamic decision making. It systematically analyzes
critical technical and ethical hurdles, including model interpretability, data quality issues, and security vulnerabilities.
Furthermore, the review examines emerging paradigms, such as the deployment of autonomous and multi-agent systems
that are revolutionizing financial workflows and strategies. By bridging the gap between AI and financial applications and
identifying unresolved challenges, this analysis delineates a clear agenda for future research aimed at fostering a more robust,
transparent, and equitable AI-driven financial ecosystem.
Keywords: Artificial intelligence; Financial research; Machine learning; Artificial intelligence agent; Financial technology.
Received: 05 February 2026; Revised: 29 March 2026; Accepted: 04 May 2026
Article type: Review article.
1. Introduction risk monitoring, and product personalization across the
Artificial intelligence became increasingly important to financial sector.[5] The growing relevance of AI in fintech was
financial technology because financial systems generated therefore tied to both economic value creation and institutional
large scale, high frequency, and highly heterogeneous data adaptation, as firms sought greater operational efficiency,
that exceeded the analytical capacity of many conventional faster decisions, and broader market reach in increasingly data
decision frameworks.[1,2] The digitalization of payments, intensive environments. More recently, this background
lending, investment, insurance, and platform based services evolved beyond predictive analytics alone, as finance began to
further accelerated this transformation, since financial incorporate AI agents capable of interacting with data, tools,
institutions and fintech firms needed methods that could and decision environments in more adaptive and semi-
process transactional records, behavioural signals, text, and autonomous ways.[6,7] Emerging studies suggested that these
alternative data in near real time.[3,4] Prior studies showed that agent based systems could extend the role of AI from
this shift was not only technical but also structural, because AI classification and forecasting toward sequential decision
supported new forms of service delivery, customer interaction, support, regulatory reasoning, portfolio adjustment, and task
orchestration across financial workflows.[8,9]
1School of Engineering, The University of Manchester, Manchester,
The importance of AI in fintech was also reinforced by
England, M13 9PL, UK
the limitations of conventional rule based and linear modelling
2Faculty of Engineering, University College London, London,
approaches in settings marked by uncertainty, fraud risk,
England, WC1E 6BT, UK
market volatility, and rapidly changing customer behaviour.[10–
3The Bartlett Faculty of the Built Environment, University College
12] In lending, machine learning methods improved the ability
London, London, England, WC1E 6BT, UK
to identify borrower risk and extract information from
*Email: zhizhou.zhang@manchester.ac.uk (Z. Zhang),
complex or nontraditional variables, while in fraud detection
meiqi.lu.22@ucl.ac.uk (M. Lu)
Engineered Science Publisher Eng. Sci., 2026, 41, 2245 | 1

Review article Engineered Science
Fig. 1: A market map of key artificial intelligence (AI) application areas in the fintech industry.
and transaction monitoring, AI based systems strengthened representative companies operating in each key area such as
anomaly recognition and adaptive surveillance capacities.[13–17] intelligent payments, credit scoring, anti-fraud technology,
In financial markets, deep learning, reinforcement learning, and algorithmic trading. The integration of AI is driving a
and multi agent architectures were increasingly used for paradigm shift from traditional financial models toward more
forecasting, sentiment extraction, trading support, and automated, intelligent, and personalized systems. This
dynamic portfolio management, which reflected the broader evolution, fuelled by breakthroughs in machine learning,
movement of finance toward automated and data driven natural language processing, and big data analytics, has
decision environments.[18–20] At the customer interface, AI also positioned AI as a cornerstone of innovation within the
became important through chatbots, advisory tools, and financial industry.[13,32] Financial institutions are increasingly
intelligent service systems that reshaped communication leveraging AI to enhance operational efficiency, improve risk
between financial institutions and users.[21–23] At the same time, management and decision making processes, and
the rise of AI agents made the background of fintech more revolutionize the customer experience.[33,34] The impact of AI
consequential because these systems raised stronger questions now spans a wide array of financial applications, including
about interpretability, accountability, compliance, and human algorithmic trading, fraud detection, credit scoring, and
oversight in high stakes financial settings.[24–26] AI became personalized financial advisory services.[35–37]
important in fintech not simply because it improved prediction, The AI in fintech market is experiencing substantial
but because it began to reshape how financial value was growth, with projections indicating its global size will expand
assessed, how decisions were made, and how increasingly significantly in the coming years. Generative AI market
autonomous financial services were delivered and governed report[38] illustrated that the global generative AI market is
across the digital economy.[27–30] projected to expand from USD 13.5 billion in 2023 to
Artificial intelligence (AI) has emerged as a approximately USD 255.8 billion by 2033, representing a
transformative force in the financial technology (fintech) compound annual growth rate (CAGR) of 34.2% over the
sector, fundamentally reshaping how financial services are forecast period. In 2023, North America established market
delivered, managed, and consumed.[31] Fig. 1 provides a primacy, accounting for over 42.1% of global revenue, valued
schematic overview of the primary application domains of at USD 5.6 billion. This expansion is driven by the profound
artificial intelligence within the fintech sector, showcasing impact AI has on the financial industry, where it is no longer
2 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
a peripheral technology but a core component of business anti money laundering studies established another major state
strategy and operations.[39] The importance of AI in this sector of the art stream, showing that AI supported adaptive anomaly
stems from its ability to process and analyze massive datasets, detection, transaction surveillance, and operational
leading to enhanced efficiency, improved accuracy in monitoring across payment systems and financial crime
decision-making, and the creation of innovative, personalized control.[12,17] The technical frontier had been shaped by large
financial services.[40] Financial institutions are increasingly scale data engineering, hybrid modelling, and the need to
leveraging AI to automate routine processes, which minimizes respond to continuously evolving fraud tactics rather than
operational costs and allows human resources to focus on static risk patterns.
more complex tasks. The state of the art then expanded from risk screening
Prior work[11,13,14] showed that the state of the art in toward market intelligence, financial decision support, and
artificial intelligence for fintech first developed around customer facing service systems. In financial markets, prior
prediction intensive tasks, particularly credit assessment, work showed that deep learning, time series forecasting,
lending analytics, and fraud detection, where machine learning sentiment analysis, and reinforcement learning were
methods were increasingly adopted to outperform many increasingly used for trading, portfolio selection, and market
conventional statistical and rule based approaches under prediction, reflecting a broader shift from static estimation
complex data conditions. The historical application of AI in toward dynamic and data responsive finance.[18–20] Research on
finance began with early computational models and rule based AI powered chatbots and advisory systems also indicated that
expert systems for tasks like algorithmic trading[41] and fraud fintech applications had moved into customer service,
detection.[42] However, the recent explosion in data availability compliance support, segmentation, and personalized financial
and computational power has enabled the deployment of more interaction, which demonstrated that AI was no longer
sophisticated AI models, such as deep neural networks, which confined to back end risk modelling alone.[21,23] The frontier of
can uncover complex, non linear patterns in vast datasets. This the field had entered a new phase characterized by
has led to significant improvements in predictive accuracy for explainability, generative AI, and finance specific large
tasks like market trend forecasting[43] and credit risk language models, because financial institutions increasingly
assessment.[33] The rise of generative AI has further expanded needed systems that could interpret text, support regulatory
the capabilities of financial institutions, allowing for the reasoning, and assist with knowledge intensive financial
automation of complex knowledge work such as financial tasks.[47] Emerging work on intelligent financial systems
report generation,[44] sentiment analysis,[45] and the creation of indicated that AI in finance was developing from narrowly
synthetic data[46] for robust model training. As a result, AI is defined predictive tools toward more integrated decision
no longer a peripheral technology but a central driver of infrastructures that combined data analysis, language
competitive advantage and innovation in the global financial processing, and adaptive support across multiple financial
ecosystem. Fintech lending studies reported that alternative functions. The contemporary state of the art in fintech had
data and machine learning improved borrower screening and been defined not only by stronger predictive models, but also
expanded the informational basis of credit evaluation, by the growing integration of explainability, language based
especially for applicants who were less well served by intelligence, and increasingly agent like forms of financial
traditional credit infrastructures.[13] Benchmarking studies in decision support.
credit scoring further showed that ensemble learning and other Despite the rapid diffusion of artificial intelligence in
advanced classifiers often delivered stronger predictive financial technology, its practical deployment remained
performance than many earlier baseline models, which made constrained by severe data related limitations. Financial
AI driven credit modelling one of the most mature areas in datasets were often fragmented across institutions, restricted
financial technology research.[14] Explainable machine by privacy regulation, and affected by noise, missing values,
learning in credit risk management became an important reporting inconsistency, and regime shifts, all of which
strand of research in response to regulatory scrutiny and the reduced model portability and weakened out of sample
need to justify automated financial decisions.[33] Recent reliability.[4,47] Privacy preserving collaboration therefore
systematic reviews[24,25] confirmed that explainable artificial became an important research direction, yet decentralized and
intelligence had become a major component of finance federated learning approaches still introduced additional
research because transparency, accountability, and traceability communication cost, computational burden, and security
were increasingly treated as core requirements in high exposure, and they did not fully resolve the tension between
consequence financial settings. In parallel, fraud detection and privacy protection and predictive utility.[14,25,33]
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 3

Review article Engineered Science
A second major gap concerned transparency and fairness applications across key financial domains and mapped them to
in high stakes financial decisions. Many high performing underlying models, ranging from foundational machine
models in lending, fraud detection, and risk monitoring still learning algorithms to advanced generative artificial
operated as black boxes, while recent reviews in finance intelligence and autonomous agents. A primary contribution
showed that explainability methods had not yet been of this work involved a detailed examination of emerging
consistently validated for domain specific decision support, paradigms, with a particular focus on the rise autonomous
regulatory audit, or stable local interpretation across agents. The research analyzed agent architecture and the
settings.[24] Fairness remained difficult to define and potential for these systems to revolutionize financial
operationalize in credit contexts because different fairness workflows through complex reasoning. Furthermore, the
criteria could conflict with each other and with profitability analysis documented the operational shift from task specific
objectives.[12] Recent evidence from credit rating research automation toward holistic and intelligent financial
further showed that fairness and explainability were tightly ecosystems. The review also provided a systematic analysis
connected, yet joint evaluation frameworks remained limited critical technical and ethical challenges that hindered the
and unfairness could still emerge in smaller or subgroup responsible adoption of artificial intelligence in finance. It
specific samples.[17] Robustness under adversarial and assessed persistent issues including data privacy, model
dynamic conditions also remained insufficiently addressed. interpretability, algorithmic bias, security against adversarial
Research across industrial machine learning showed that attacks, and the complexities of regulatory compliance.
adversarial manipulation had become a realistic concern, Finally, by identifying unresolved challenges and exploring
while defensive practice remained uneven and often immature the convergence regarding artificial intelligence with other
at the deployment stage.[18] In fintech, this challenge became frontier technologies, the study delineated a clear agenda for
more acute as transformer based credit scoring models that future research aimed at developing more robust, transparent,
used borrower text were shown to be vulnerable to small and equitable financial systems.
semantically neutral perturbations, which could materially
alter model outputs and create risks of gaming, instability, and 2. AI-driven transformation in fintech
unreliable decision making.[19] Artificial intelligence (AI) has rapidly emerged as a
Another emerging gap concerned the use of large cornerstone of modern financial technology, reshaping how
language models and generative systems in finance. Recent institutions and consumers interact with financial systems.[31]
research showed that hallucination remained a central By leveraging machine learning, natural language processing,
weakness of large language models, particularly in specialized and deep learning, AI-driven fintech extends far beyond
domains that required factual precision and verifiable traditional automation, enabling predictive analytics,
reasoning.[48] Retrieval augmented generation was increasingly personalized financial services, and real-time risk
proposed as a mitigation strategy because it improved management. Recent advances in large language models and
grounding through external knowledge access, yet current generative AI agents further accelerate this transformation by
evidence also showed that retrieval support did not eliminate enhancing interpretability, adaptability, and decision-making
harmful or unreliable outputs and that model performance still across lending, payments, trading, compliance, and customer
varied substantially across tasks and contexts.[49,50] Although engagement.[52] As a result, AI is no longer a peripheral tool
the existing literature[4,48,51] had provided valuable insights into but a central enabler of innovation, efficiency, and
specific aspects of artificial intelligence in fintech, most competitiveness in the global financial ecosystem. This
reviews had treated machine learning applications, chapter explores the core applications, benefits, and
explainable artificial intelligence, and regulatory governance challenges of AI integration into fintech, highlighting both the
as separate lines of inquiry. A comprehensive synthesis that technological breakthroughs and the governance frameworks
brought together conventional predictive models, generative necessary to ensure fairness, accountability, and trust in these
systems, and emerging agent based architectures within a high-stakes environments.
unified fintech framework, while simultaneously addressing
governance, security, fairness, and financial stability, had 2.1 Reasons to use machine learning
remained relatively limited. Artificial intelligence offered clear advantages for the modern
This review provided a holistic synthesis of the current financial technology stack because it processed large and
state of artificial intelligence within the financial technology heterogeneous data at scale, automated complex decisions,
sector. It introduced a structured taxonomy that classified and supported end to end digital services across lending,
4 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
payments, wealth, and compliance. Survey work in smart workload. A broad review of chatbot technologies described
financial technology and in banking documented how artificial how advances in natural language processing and dialog
intelligence systems increased decision quality, supported full management supported these service gains in financial
digital workflows, and reduced operational frictions across settings.[22] Experimental evidence in electronic markets
risk, service, and analytics functions.[1,2] research further reported that artificial intelligence chatbots
Credit risk management benefited most visibly. Lender shaped user behavior and compliance in service flows,
studies showed that machine learning models that used indicating value for onboarding, education, and guidance use
alternative data improved default prediction and widened cases.[21]
access for thin file borrowers while preserving or improving Finally, the adoption of explainable artificial intelligence
risk grading. Evidence from a fintech platform demonstrated strengthened trust, audit, and regulatory alignment. Recent
that rating grades that incorporated nontraditional data work on credit scoring combined deep learning with post hoc
predicted performance and reclassified some borrowers into explanation techniques and demonstrated that high performing
better priced loan grades.[13] Comparative experiments with models could be interrogated for driver analysis and policy
phone metadata, psychometrics, and other sources reported review without sacrificing predictive power, which supported
accuracy gains over traditional demographic only baselines.[15] deployment under transparency requirements.[36]
Classic reviews in credit risk established the methodological
foundation for these developments and explained why non 2.2 Open-source resources for AI in fintech
linear models and richer features improved credit scoring in The rapid integration of artificial intelligence within the
practice.[10] financial technology sector is substantially supported by the
Artificial intelligence also enhanced market sensing and broad availability of open source tools and datasets. Table 1
trading. Deep reinforcement learning studies framed portfolio reviewed open-source resources that had been applied in
rebalancing as a sequential decision problem and reported finance and economics. These resources have democratized
improved risk adjusted metrics in backtests when reward access to sophisticated analytical capabilities, enabling
functions targeted portfolio objectives directly.[18] At the same researchers and practitioners to develop, benchmark, and
time, progress in deep learning for time series forecasting deploy complex models for financial applications.[34] The
expanded the toolkit for multi horizon prediction that ecosystem of open source software libraries provides the
underpinned risk, pricing, and allocation engines in financial foundational building blocks for machine learning, while a
applications.[19] Text analysis of financial news further showed growing number of specialized and general purpose datasets
that quantified media tone and salience affected price offer the empirical grounding needed for rigorous model
formation, which motivated the use of natural language training and validation.
models in trading and surveillance pipelines.[20] A diverse range of open source datasets is crucial for
Fraud and financial crime programs gained measurable advancing financial research. For complex tasks like
efficiency from artificial intelligence. Cost sensitive and numerical reasoning over financial documents, specialized
champion challenger set ups in card authorization streams datasets such as FinQA[54] have been developed to train and
improved savings by raising detection with fewer false evaluate models on question answer pairs derived from
positives relative to static rules, which translated into lower financial reports. To test a model’s nuanced understanding of
manual review volumes and faster time to decision.[16] In anti financial language, benchmarks like FinNLI[55] offer a basis
money laundering, qualitative fieldwork with banks and for assessing natural language inference from sources such as
providers highlighted pain points in transaction monitoring regulatory filings and earnings call transcripts. More
and pointed to machine learning as a route to reduce comprehensive benchmarks, including FinBen,[56] provide a
investigative backlogs and false alerts while preserving holistic framework for evaluating large language models
coverage of evolving typologies.[53] A methods review from across a spectrum of financial tasks from information
the information systems perspective catalogued the data extraction to risk management. Beyond these specialized
engineering and model governance practices that made fraud resources, extensive macroeconomic time series data are
analytics reliable at scale.[17] available from platforms like the Federal Reserve Economic
Customer engagement and service operations also Data (FRED) database,[57] which is a cornerstone for economic
benefited. Institutions deployed conversational agents to forecasting and financial market research. General purpose
deliver always on support for balance queries, payments, and repositories also serve the fintech community; platforms like
account changes, which reduced wait times and agent Zenodo[58] promote open science by hosting accessible
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 5

Review article Engineered Science
Table 1: Open-source packages, machine learning models, dataset and applications for fintech.
Machine learning Description and features Application
A large-scale dataset of 8,281 Numerical reasoning over financial documents; training
question-answer pairs over 2,800 models to answer finance questions; explainable AI; feature
FinQA[54] financial reports, with numerical extraction for predictive models using financial statements.
reasoning, combining structured and
unstructured data (tables, text)
Benchmark for Natural Language Testing understanding of financial text entailment; fine‐
FinNLI[55] Inference in financial text, using SEC tuning NLP models for inference / summarization; detecting
filings / earnings call transcripts misleading statements or consistency checking
A holistic benchmark for financial Evaluating LLMs on finance tasks; benchmarking model
LLMs, covering many datasets across performance across tasks; guiding
financial tasks: IE (information architecture/hyperparameter choices; research into
FinBen[56]
extraction), QA, forecasting, text generalization for diverse financial tasks
generation, decision, making and risk
management.
Fine-tune LLMs on financial text; use for section extraction,
Financial Reports Contains US public firms’ annual
sentiment analysis; training models to understand structure of
SEC[68] reports (10-K) from ~1993-2020.
10-K filings.
The Federal Reserve Macroeconomic trend analysis,[70] Economic forecasting,[71]
Offers extensive U.S. economic time
Economic Data Financial market research,[72] Policy impact assessment.[73]
series and indicators.[69]
(FRED) database[57]
Finding datasets for machine learning projects,[75]
Supporting academic research,[76] Sourcing data for data
Google Dataset Global dataset search, broad
journalism,[77] Enabling reproducible scientific studies,[78]
search[59] coverage, real-time updates.[74]
Market analysis and business intelligence,[79] Locating open
government and health data
Open-
Standardized datasets, measurement Benchmarking machine learning models,[82] Testing
source
NIST[80] data, scientific and technical algorithm performance,[83] Scientific research validation,[84]
datasets
benchmarks.[81] Developing measurement standards[85]
Open-access research data, Sharing open research datasets,[87] Assigning DOIs for easy
Zenodo[58] multidisciplinary, supports datasets citation,[86] Collaborative project data storage,[88] Hosting
and publications.[86] software and code archives
Sharing environmental and geospatial data,[91] Supporting
disaster management and response,[92] Facilitating cross-
AmeriGEOSS Environmental data sharing,
country scientific collaboration,[93] Monitoring climate and
Community Platform geospatial datasets, supports Americas
ecosystem changes,[94] Enabling open access to regional
DataHub[89] collaboration.[90]
datasets,[95] Promoting sustainable development initiatives in
the Americas
Predicting stock price movement based on sentiment,[97]
Analysing market reaction to news and events,[98] Training
Stock market emotions, rich labels,
StockEmotions[60] sentiment analysis models for finance,[99] Building trading
real-time updates.[96]
strategies using emotion signals,[100] Monitoring public mood
for investment decisions[101]
News impact analysis on financial markets,[103] Automatic
headline classification (e.g., positive/negative),[104] Event-
News headlines dataset, labeled,
Headline[61] driven trading system development,[105] Detecting market-
regularly updated.[102]
moving news in real time,[106] Training language models for
financial headline understanding[56]
Financial named entity recognition (NER),[107] Extracting
Financial named entity recognition companies,[108] instruments, and economic terms from
FiNER-139 open Research Dataset, annotated text,[109] Building financial knowledge graphs,[51] Improving
entities, domain-specific.[62] document search in finance,[110] Automating regulatory
compliance monitoring
6 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Machine learning Description and features Application
Multilingual financial sentiment analysis,[112] Cross-lingual
market news understanding,[113] Training models for global
Financial news dataset, multilingual,
FNXL[111] financial news monitoring,[114] Building sentiment-based
labelled for sentiment.
investment signals,[45] Studying sentiment transfer across
languages in finance[115]
Table structure recognition in financial documents,[116]
Financial table dataset, annotated Automatic extraction of financial figures from reports,[117]
FinTabNet[63]
structure, extracted from reports.[46] Training models for document digitization,[118] Enhancing
information retrieval from tabular data[119]
Machine learning library, easy-to-use, Building classification models, Regression analysis,[121]
classification, regression, Clustering and unsupervised learning,[122] Data preprocessing
Scikit-learn[64]
clustering.[120] and transformation,[123] Model evaluation and validation,[124]
Feature selection and dimensionality reduction[125]
Building deep neural networks,[127] Image and speech
Deep learning framework, flexible,
recognition,[128] Natural language processing,[129] Time series
TensorFlow[67] scalable, supports neural
forecasting,[19] Reinforcement learning,[130] Large-scale
Open- networks.[126]
machine learning deployment
source
Deep learning research prototyping,[132] Computer vision
packages Deep learning library, dynamic
applications,[133] Natural language processing tasks,[134]
PyTorch[65] computation, flexible, popular for
Custom neural network development,[135] Reinforcement
research.[131]
learning experiments, GPU-accelerated model training[136]
Rapid prototyping of neural networks,[138] Image
High-level neural networks API, user- classification tasks,[139] Text and sentiment analysis,
Keras[66]
friendly, runs on TensorFlow.[137] Sequence modelling (RNN, LSTM),[140] Transfer learning
experiments, Educational deep learning tutorials[141]
research data, and the Google Dataset[59] facilitates the reinforcement learning experiments. High level application
discovery of datasets for market analysis and academic programming interfaces like Keras,[66] which runs on top of
research. For developing sentiment analysis models, datasets frameworks like TensorFlow,[67] further simplify the process of
such as StockEmotions[60] provide news articles labeled with building and experimenting with neural networks, making
emotional indicators, while others like Headline[61] offer deep learning more accessible for a broader range of
curated news headlines for studying market impact. applications including sentiment analysis and sequence
Furthermore, domain specific resources for named entity modeling.
recognition, such as FiNER-139,[62] and for table structure
recognition, like FinTabNet,[63] are essential for automating 2.3 Artificial intelligence models in fintech
information extraction from unstructured financial documents. Artificial Intelligence now underpins core decisions across
The development of sophisticated AI models in finance is lending, payments, trading, insurance, and compliance.[142] In
heavily reliant on powerful and accessible open source supervised learning for retail and small business credit,
software packages. Foundational libraries such as Scikit- gradient boosted trees, support vector machines, and deep nets
learn[64] offer a user friendly interface for implementing a wide routinely outperform traditional scorecards on accuracy while
array of machine learning algorithms, including classification, enabling granular risk segmentation at scale.[143]
regression, and clustering, making it a primary tool for Benchmarking studies over diverse credit datasets showed
building predictive models in areas like credit scoring. For robust gains from modern classifiers and careful model
more complex deep learning applications, frameworks like selection.[11] Early evidence from bank portfolios also
TensorFlow provide a flexible and scalable environment for demonstrated the practical lift of machine learning in default
constructing and deploying large neural networks for tasks prediction and line management.[14] New work integrates
such as time series forecasting and natural language alternative data and careful sampling to improve performance
processing. Similarly, PyTorch[65] has gained significant without eroding governance standards,[15] while fairness aware
popularity, particularly in the research community, for its development is becoming standard practice, with frameworks
dynamic computational graph and intuitive interface, which to quantify and mitigate disparate impact in credit scoring and
facilitates rapid prototyping in computer vision and to evaluate fairness trade offs alongside profitability.[144,145]
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 7

Review article Engineered Science
Explainability for regulated credit decisions is advancing claim frequency and severity prediction, and practical
through techniques that surface global and local drivers, which pipelines that blend convolutional encoders with generalized
can be embedded into validation and audit processes.[33] linear models to preserve transparency and calibration.[157,158]
Payment fraud and financial crime analytics rely on Actuarial journals also document advances in model
supervised learning, cost sensitive learning, and representation calibration and risk adjusted evaluation for pricing, reserving,
learning on highly imbalanced data.[146] Classic studies in card and reinsurance decisions, including deep learning solutions
fraud detection compared logistic regression, neural networks, to optimal control problems in capital management.[159,16]
and tree ensembles, and motivated practices such as Across these domains, explainability, robustness, and
transaction aggregation and cost based evaluation.[147] fairness are central to deployment. Financial institutions must
Recently, graph neural networks exploit account and device reconcile model performance with attributable and responsible
relationships to detect coordinated rings, and are being analytics, and the literature offers frameworks for explainable
adopted for transaction monitoring in anti money laundering artificial intelligence in operations research and finance,
where scalability and regulatory auditability are essential.[35] alongside perspectives that advocate inherently interpretable
These models often combine supervised detection with models for high stakes decisions.[161,162]
unsupervised anomaly scoring to prioritize investigation Table 2 summarized the principal artificial intelligence
queues and reduce false positives. algorithms applied in fintech and their advantages. Large
In markets, predictive modeling spans supervised learning language models facilitated natural language tasks such as
on engineered features, deep sequence models for limit order financial news summarization, sentiment analysis, and
books and returns, and reinforcement learning for policy chatbots. Neural networks and LSTMs supported credit
search in trading and portfolio allocation. Deep networks and scoring, stock prediction, and volatility modeling, while
boosted trees delivered significant improvements for return CNNs addressed image-based verification tasks. Random
prediction and statistical arbitrage in liquid equities.[27,35] forests and decision trees provided interpretable models for
Recurrent and convolutional architectures capture temporal credit and risk assessment. Explainable AI enhanced
and cross asset structure, with applications to foreign transparency, fusion models combined algorithmic strengths,
exchange and volatility modelling.[148,149] For portfolio generative AI enabled synthetic data and reporting, and
construction, deep learning is used either to forecast returns reinforcement learning optimized trading and portfolio
that feed optimization or to learn allocation policies directly, strategies.
with evidence of improved risk adjusted performance in Table 2 clarified that artificial intelligence models in
controlled studies and backtests.[150,151] Reinforcement learning fintech were not interchangeable, because each model class
is also advancing in portfolio selection and execution, where offered different technical strengths and matched different
reward shaping and risk constraints can be encoded into the financial tasks. The comparison showed that model suitability
objective.[152] depended mainly on the form of the input data, the degree of
Natural language processing has moved from dictionaries temporal dependence, the required balance between predictive
to transformer based models that read news, filings, and accuracy and interpretability, and the practical objective of the
transcripts.[153] Today, deep models process news streams, institution. First, the table showed a clear distinction between
earnings call text, and even audio to extract sentiment and text oriented models and structured numerical models. Large
forward looking signals that feed trading and credit early language models were particularly suitable for tasks involving
warnings.[154] Large language models are being evaluated for unstructured textual information, such as financial news
investment analysis and screening, with peer reviewed summarization, chatbot services, sentiment analysis, report
evidence that model outputs can correlate with subsequent generation, and fraud email detection. Their main advantage
fundamentals and returns, while performance varies with task lay in natural language understanding and generation, which
design and evaluation rigor.[155] For long documents such as made them more appropriate for communication, document
financial reports, neural summarization and information processing, and language based intelligence tasks than for
extraction are being applied to accelerate analysis and support conventional tabular risk prediction. By contrast, neural
compliance reviews.[156] networks and random forest models were more naturally
Insurance has become a rich testbed for tabular deep aligned with structured financial datasets used in credit
learning, telematics analytics, and interpretable pricing. Usage scoring, default prediction, fraud detection, and market trend
based motor insurance now integrates telematics signals with analysis.
traditional factors, with studies showing material gains in Neural networks, LSTM models, and reinforcement
8 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Table 2: Artificial intelligence models and its core advantages for fintech applications.
Artificial Intelligence
Key strengths Fintech applications
Algorithm
Large language Excels at understanding and Financial news summarization,[165] chatbots for customer service,[166]
model[163] generating natural language text[164] sentiment analysis,[167] report generation,[168] fraud email detection[165]
Powerful nonlinear modeling, adapts Credit scoring,[171] stock price prediction,[172] loan default risk,[173] pattern
Neural Networks[169]
well to complex data[170] recognition in trades,[174] asset price forecasting[175]
Captures long-term dependencies, Time-series forecasting,[178] stock price prediction,[179] market volatility
Long short term
strong for sequential data modelling,[180] sequence anomaly detection,[181] economic indicator
memory (LSTM)[176]
processing[177] prediction[182]
Document image analysis,[185] cheque signature verification,[186] chart
Convolutional neural Excellent at image recognition,
pattern recognition,[187] fraudulent document detection,[42] visual
network[183] efficient feature extraction[184]
compliance screening[188]
Strong against noise, handles Credit approval,[191] fraud detection,[192] customer segmentation,[193] loan
Random forest[189]
nonlinear classification effectively[190] risk assessment,[194] market trend analysis[195]
Simple, interpretable results with fast Credit decisioning,[198] loan approval,[199] customer churn prediction,[200]
Decision tree[196]
computation speed[197] simple risk classification,[196] transaction categorization[201]
Explainable AI Improves transparency, enhances trust Transparent credit scoring,[36] regulatory compliance,[204] model
(XAI)[202] in AI systems[203] auditability,[205] bias detection,[206] explain loan decisions[207]
Multi-source risk analysis,[209] ensemble trading strategies,[210] cross-
Combines model strengths, improves
Fusion models market forecasting,[211] hybrid fraud detection,[212] integrated portfolio
prediction accuracy significantly[208]
analytics[213]
Produces creative outputs, enables Synthetic data generation,[216] scenario simulation,[217] automated report
Generative AI[214]
innovative application scenarios[215] drafting,[218] financial content creation,[219] market scenario modelling[220]
Reinforcement Learns from feedback, optimizes Algorithmic trading,[18] portfolio optimization,[223] asset allocation,[41]
Learning (RL)[221] long-term decision strategies[222] dynamic hedging,[224] market making[225]
learning were better suited to tasks characterized by model governance, bias detection, and compliance. This made
complexity, dynamic interaction, or time dependence. General it particularly relevant in high stakes applications such as
neural networks were effective when financial relationships credit scoring and regulated lending, where institutions needed
were highly nonlinear, such as in credit scoring, asset pricing, to justify automated decisions to regulators and customers.
or trade pattern recognition. LSTM models were more Convolutional neural networks were more appropriate for
specifically suited to sequential and time series problems visual financial tasks such as document image analysis,
because they captured long term temporal dependencies. This cheque signature verification, chart pattern recognition, and
made them more appropriate for stock prediction, volatility fraudulent document detection. Their strength in feature
modelling, economic indicator prediction, and anomaly extraction from image based inputs distinguished them from
detection in sequential market data. Reinforcement learning tree based methods or language models, which were not
differed from both by focusing on sequential decision designed primarily for visual pattern recognition.
optimization under feedback. For that reason, it was more Fusion models combined the strengths of multiple
suitable for algorithmic trading, portfolio optimization, asset algorithms and were therefore suitable for multi source risk
allocation, dynamic hedging, and market making, where analysis, hybrid fraud detection, and integrated portfolio
actions affected future outcomes and long horizon strategy analytics, where no single model could fully capture the
mattered. complexity of the task. Generative AI was more suitable for
Decision trees and explainable AI methods were especially synthetic data generation, scenario simulation, automated
valuable when institutions needed transparent reasoning, drafting, and financial content creation because it produced
auditability, and regulatory acceptance. Decision trees were new outputs rather than only making classifications or
useful in credit decisioning, loan approval, and transaction forecasts. This suggested that its role in fintech extended
categorization because they produced simple and beyond prediction into simulation, augmentation, and
understandable decision rules with low computational burden. workflow support.
Explainable AI played a different but complementary role. It Overall, the choice of artificial intelligence model in
did not merely improve prediction, but strengthened trust, fintech was task dependent rather than universal. Models
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 9

Review article Engineered Science
differed in their strengths because they were designed for Biometric technologies, including voice and facial recognition,
different forms of data and decision problems. Large language are increasingly used for secure identity verification and
models were more suitable for language intensive tasks, authentication, streamlining customer onboarding and
convolutional neural networks were more suitable for visual transaction authorization while reducing reliance on
analysis, LSTM models were more suitable for temporal traditional passwords.[227] In the domain of customer support,
forecasting, reinforcement learning was more suitable for Natural Language Processing (NLP) underpins the
dynamic optimization, and decision trees and explainable AI functionality of sophisticated chatbots and virtual
were more suitable when interpretability and compliance were assistants.[228] These AI driven tools provide 24 for 7 support,
essential. Neural networks and random forest models handle routine inquiries, and guide users through complex
remained broadly useful for nonlinear prediction in structured processes, thereby improving service quality and reducing
financial settings, while fusion models offered advantages operational costs for financial institutions. Furthermore, AI
when complex applications required multiple complementary algorithms are central to the delivery of personalized financial
capabilities. Therefore, certain model categories were better services. Robo advisors leverage machine learning to
suited to specific financial tasks because their technical construct and manage investment portfolios tailored to
properties aligned more closely with the informational, individual risk profiles and financial goals, making
operational, and regulatory demands of those tasks. sophisticated wealth management accessible to a broader
audience.[37] These systems also power personalized
2.4 AI applications in fintech recommendation engines that suggest relevant financial
Artificial intelligence has become a transformative force products, from credit cards to insurance plans, based on a
across the financial technoligies industry, enabling a wide user's behavior and financial data.
spectrum of applications that enhance operational efficiency, In credit underwriting and risk scoring field, supervised
improve customer experiences, and strengthen risk learning models have outperformed traditional scorecards in
management frameworks.[226] In Fig. 2, AI models are being benchmark studies, particularly on imbalanced default data
deployed to automate and optimize core financial tasks, from and for small and mid size enterprise lending.[229] These
client interaction and security to complex data analysis and systems exploit nonlinear interactions among bureau,
decision making processes. The integration of AI is not merely transactional, and alternative features to improve rank
an incremental improvement but a fundamental shift in how ordering and cut loss given default through earlier
financial services are designed, delivered, and managed, interventions. Recent work focuses on fairness and
touching virtually every aspect of the fintech ecosystem. interpretability, showing that monotone gradient boosted trees
AI has profoundly reshaped customer facing financial and rule based surrogates can preserve accuracy while
services. Table 3 summarizes the diverse applications of providing case level explanations suitable for audit and
artificial intelligence across fintech services, detailing how consumer disclosure.[145,230,231] Empirical evidence also shows
technologies from voice recognition to generative AI agents performance gains when combining feature learning with
deliver significant benefits such as enhanced security, human readable constraints.
operational efficiency, and personalized customer experiences. Machine learning models are extensively used for the real
Fig. 2: AI applications in fintech industry.
10 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Table 3: Applications and benefits of artificial intelligence in the fintech service.
AI appiled field Applications Benefit and advantages of AI in finance
Voice recognition[235] Biometric Authentication,[236] Voice Banking,[237] Transaction Providing secure, hands-free authentication,
Authorization[238] streamlining transactions, and improving
customer verification with greater speed and
efficiency
Sentiment Investment prediction,[240] chat sentiment analysis,[241] Brand, Sentiment analysis helps financial services
analysis[239] Voice-based Emotion Detection[242] anticipate trends, enhance customer
experience, and manage risks through
emotional insight and real-time feedback.
Cheating, criminal Fraud Detection in Transactions,[243] Money Laundering Monitoring AI enables real-time detection of fraud,
detection (AML),[53] Insider Trading Surveillance,[244] Document Forgery deception, and financial crimes, enhancing
Detection[243] security and regulatory compliance in financial
services.[245]
Customized Personalized Investment Advice,[246] Tailored Product Offers,[247] Delivers relevant, user-specific financial
recommendation Spending Insights and Alerts, Financial Planning Tools,[248] products and insights efficiently.
Behavior-Based Rewards Programs[249]
Financial Automated Financial Statement Generation,[44] Smart Auditing and Automating reporting, enhancing accuracy,
information process Reconciliation,[250] Data Structuring from Unstructured Sources,[251] enabling real-time insights, and ensuring
Natural Language Report Generation (NLG),[252] Credit Scoring regulatory compliance efficiently.
Enhancement[15]
Image identification KYC Document Verification,[227] Check Image Processing,[253] Speeds verification, enhances security, and
ATM Fraud Detection,[254] Signature Verification,[255] Receipt and automates visual data processing.
Invoice Scanning[256]
Customer service AI-Powered Voice Support (IVR),[257] Chatbots,[22] Automated Personalized support with reduced human
Ticket Routing,[258] Multilingual Customer Support,[259] Customer workload.
Satisfaction Analysis[260]
Predictive modelling Credit Risk Assessment,[10] Customer Churn Prediction,[261] Enables smarter decisions, risk reduction, and
Operational Risk Management,[262] Loan Pre-approval business growth forecasting.
Automation,[263] Personalized Product Recommendations[264]
Information security Intrusion Detection Systems (IDS),[265] Phishing Email Enhances protection, rapid response, and
Detection,[266] Anomaly Detection,[267] User Authentication adaptive threat detection.
Enhancement,[268] Malware Detection and Prevention[269]
Generative artificial Automated Report Generation,[270] Synthetic Data Generation,[271] Boosts efficiency, creativity, and
intelligence agent Personalized Marketing Content,[272] Conversational AI personalization in digital financial services.
(Chatbots/Assistants),[273] Code Generation and Automation[274]
time detection and prevention of fraudulent activities. By and conduct stress tests on financial portfolios to ensure
analyzing vast streams of transaction data, these systems can institutional resilience.[33]
identify anomalous patterns indicative of credit card fraud, AI is also instrumental in automating the complex and labor
identity theft, or account takeovers with high accuracy.[16,42] intensive processes of financial data analysis and reporting.
Beyond transactional fraud, AI is a crucial tool in the fight NLP and computer vision technologies are used to
against financial crime. Advanced algorithms are deployed for automatically extract and structure information from
Anti Money Laundering (AML) compliance to monitor unstructured documents like financial statements, contracts,
transactions, detect suspicious networks of activity, and and news articles.[233] Sentiment analysis models process news,
reduce the high volume of false positives often associated with social media, and earnings call transcripts to gauge market
legacy rule based systems.[232] The predictive capabilities of AI mood and provide predictive signals for investment
also extend to comprehensive risk management, where models strategies.[234] The emergence of generative AI has introduced
are used to forecast market volatility, assess operational risks, further advancements. Large language models are now
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 11

Review article Engineered Science
capable of generating sophisticated outputs, including agents introduce a new level of sophistication by
automated financial report summaries, personalized marketing autonomously gathering market intelligence, developing
content, and synthetic data for training more robust machine strategies, and executing trades.[278] Reinforcement learning
learning models without compromising customer privacy.[52] techniques are often employed to train these agents, enabling
These generative tools are poised to further automate them to learn and refine their strategies through continuous
knowledge work and unlock new efficiencies across the interaction with market environments.[279] This allows them to
financial industry. adapt to market volatility and optimize for risk adjusted
returns in ways that surpass traditional algorithmic methods.
3. AI agents in fintech Furthermore, the concept of multi agent systems is
The evolution of artificial intelligence in the financial sector is gaining traction, where multiple specialized agents collaborate
marked by a significant transition from task specific models to to solve complex financial problems.[280] These systems can
autonomous AI agents.[275] AI agents were particularly suitable simulate real world market dynamics by assigning different
for financial tasks that required autonomous decision support, roles to various agents, such as fundamental analysts,
multi step workflow execution, and real time interaction with sentiment analysts, and risk managers.[281] Through structured
dynamic information. In fintech settings, they were especially debate and collaboration, these agents can reduce cognitive
appropriate for intelligent customer service, personalized biases and improve the robustness of investment decisions.
financial advisory, automated compliance monitoring, fraud Multi agent frameworks are being explored to enhance market
investigation, portfolio rebalancing support, and trading analysis, manage portfolios, and even stress test financial
assistance, because these tasks involved continuous strategies within simulated environments, providing deeper
information gathering, context aware reasoning, and adaptive insights than single agent systems can offer.[6] In Fig. 4, a multi
responses rather than single step prediction alone. Compared agent classifies the user query and routes it to a credit agent or
with conventional models that focused mainly on a fraud agent, which call scoring and anomaly models with
classification or forecasting, AI agents were more useful when transaction and profile data to return an approval or fraud
the system needed to combine language understanding, tool suspicion as the final answer.
use, rule based checking, and sequential decision making The application of AI agents also extends to critical back
within one process. For this reason, AI agents were better office and compliance functions. In anti money laundering and
suited to complex financial tasks that required coordination fraud detection, agents can automate the investigation of
across data sources, repeated feedback, and operational action, suspicious activities by gathering data from various systems,
particularly in areas such as customer interaction, risk analyzing patterns, and even generating suspicious activity
monitoring, regulatory reporting, and decision support for reports for human review.[282] This automation of compliance
investment management. These agents are capable of sensing workflows helps financial institutions manage operational
their environment, making independent decisions, executing risks, reduce manual workloads, and ensure adherence to
actions to achieve predefined goals with minimal human complex regulations. However, the deployment of these
intervention and learn from feedback, as shown in Fig. 3. This autonomous systems introduces significant challenges.
progression represents a move from tools that provide analysis Ensuring reliability, preventing erroneous or malicious actions,
to autonomous entities that perform complex knowledge work, and maintaining transparency are critical concerns that require
fundamentally reshaping financial operations. An AI agent's robust governance frameworks.[283] The "black box" nature of
architecture typically uses a large language model as a some advanced models necessitates the development of
reasoning engine, augmented with specialized tools, memory, explainable AI (XAI) to ensure that the decisions made by
and planning capabilities, allowing it to perform multi step agents are interpretable and auditable by regulators and
tasks that were previously infeasible for a single model.[276] stakeholders.[8] The successful integration of AI agents in
AI agents are being deployed across a spectrum of fintech will depend on balancing their innovative potential
financial applications, driving innovation and efficiency. In with stringent security protocols and a commitment to
personalized finance, they function as autonomous financial responsible, human supervised deployment.
assistants, offering services that range from customized
investment advice to dynamic portfolio management.. These 4. Challenges of AI in fintech
agents analyze user data and market trends to provide tailored The integration of artificial intelligence into the financial
recommendations, making sophisticated financial guidance technology sector has catalyzed a paradigm shift, offering
more accessible. In the domain of algorithmic trading, AI unprecedented efficiencies in areas like algorithmic trading,
12 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Fig. 3: Core architecture and functional components of AI agents in fintech.
Fig. 4: Multi-agent workflow for credit assessment and fraud detection in fintech.
credit scoring, and fraud detection.[284] However, as shown in in the fintech industry, focusing on data related issues, model
Fig. 5, the deployment of these sophisticated systems interpretability, security vulnerabilities, algorithmic fairness,
introduces a unique set of technical challenges that require and regulatory compliance.
rigorous scientific inquiry to overcome. These challenges span A foundational challenge for AI in fintech revolves
the entire lifecycle of an AI model, from data acquisition and around data quality, availability, and privacy.[287] Financial
model development to deployment and ongoing datasets are often characterized by significant noise, missing
governance.[285] Addressing these issues is paramount for values, and non stationary distributions, which can severely
ensuring the creation of robust, fair, and trustworthy AI degrade the performance of machine learning models.[288] For
powered financial systems.[286] This section reviews the instance, stock market data is notoriously volatile and subject
primary technical obstacles confronting the application of AI to sudden regime changes, making historical data a potentially
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 13

Review article Engineered Science
Fig. 5: Technical, regulatory and system challenges of AI deployment in fintech.
unreliable predictor of future performance. Furthermore, the in complex financial scenarios is still an active area of research.
most valuable financial data, such as individual transaction The challenge is to provide meaningful explanations without
histories, is protected by stringent privacy regulations like the sacrificing the predictive accuracy that makes these models
General Data Protection Regulation.[289] This creates a valuable in the first place.
complicated environment for data acquisition and sharing. Model overfitting is another challenge. This occurs when
Techniques such as federated learning[290] have been proposed a machine learning model learns the training data too precisely,
to train models on decentralized data without compromising capturing not only the underlying patterns but also the noise
user privacy, yet these methods introduce their own and random fluctuations specific to that dataset.[295] While such
complexities related to communication overhead and a model may exhibit excellent performance during testing on
statistical heterogeneity. The successful application of AI is historical data, its ability to generalize to new, unseen data is
therefore heavily dependent on advanced data preprocessing severely compromised. In finance, the consequences can be
techniques and privacy preserving machine learning catastrophic. An overfitted algorithmic trading strategy may
architectures.[291] perform exceptionally in backtests only to incur substantial
The most widely discussed technical challenge is the lack losses when deployed in live markets.[296] The technical
of transparency in complex AI models, often termed the ‘black challenge involves implementing robust validation techniques
box’ problem.[292] Many high performing models, such as deep beyond simple data splitting. Methods such as k fold cross
neural networks, operate in a way that is not readily validation, walk forward optimization, and strict
understandable to human. In the high stakes environment of regularization are essential for building models that
finance, this opacity is unacceptable to regulators, customers, demonstrate genuine predictive power rather than a mere
and internal risk managers who need to understand the ability to memorize the past.[297]
rationale behind automated decisions, such as a loan With the rise of large language models and other
application denial decision. This necessity has spurred the generative AI, the problem of hallucination has emerged as a
growth of eXplainable AI, or XAI, a field dedicated to critical concern. Hallucination refers to the tendency of these
developing techniques that can render model decisions models to generate outputs that are nonsensical, factually
interpretable.[202] Methods like Shapley Additive Explanations incorrect, or entirely fabricated, yet are presented with a high
(SHAP)[293] and Local Interpretable Model agnostic degree of confidence. In a fintech context, a customer service
Explanations (LIME)[294] are gaining traction, their application chatbot might invent a nonexistent financial product, or an
14 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science                                                                                                                                                                                Review article

Table 4: Challenges and limitations of artificial intelligent applied in fintech.
| Applied Field  | Challenges  | Applications  | Limitations  |
| -------------- | ----------- | ------------- | ------------ |
Voice recognition[304]  Accents and noisy  Voice-activated banking,[305] phone payment  Accent sensitivity,[310] background noise
input  authentication,[306] customer identity  interference,[311] privacy concerns,[312]
|     |     | verification,[307] voice-controlled chatbots,[308]  | limited language support,[313] error in voice  |
| --- | --- | --------------------------------------------------- | ---------------------------------------------- |
|     |     | fraud call detection[309]                           | matching[314]                                  |
Sentiment analysis[315]  Misinterpretation of  Social media monitoring,[1] news-based trading  Sarcasm detection difficulty,[319] context
emotions  signals,[316] customer feedback analysis,[234]  misunderstanding,[320] language
|     |     | product review mining,[317,318] market mood  | limitations,[321] data labelling cost,[322]  |
| --- | --- | -------------------------------------------- | -------------------------------------------- |
|     |     | tracking                                     | overfitting to text style[322]               |
Cheating, criminal  Evolving fraud and  Suspicious transaction alerts,[320] identity theft  High false positives,[320] privacy
detection[232]  crime tactics  detection,[323] insider trading surveillance,[324]  intrusion,[327] evolving tactics,[328] data
|     |     | money laundering screening,[325] synthetic  | shortage,[329] legal restrictions[330]  |
| --- | --- | ------------------------------------------- | --------------------------------------- |
identity flagging[326]
Customized  Incomplete user  Personalized product offers,[331] tailored  Filter bubble risk,[335] user privacy
recommendation[331]  profiles  investment portfolios,[332] credit card spend  issues,[327] cold start problem,[336] over-
|     |     | suggestions,[333] loan product targeting,[334]  | personalization,[337] limited cross-channel  |
| --- | --- | ----------------------------------------------- | -------------------------------------------- |
|     |     | insurance plan customization[331]               | data[338]                                    |
Fraud detection[320]  Changing fraud  Real-time transaction screening,[339] credit card  Adaptive fraud tactics,[343] model drift,[1]
patterns  fraud alerts, account takeover detection,[340]  imbalanced data,[344] latency in
|     |     | insurance claim verification,[341] payment  | detection,[345] high computational cost[346]  |
| --- | --- | ------------------------------------------- | --------------------------------------------- |
gateway monitoring[342]
Credit scoring[347]  Biased or  Loan eligibility assessment,[348] dynamic credit  Biased training data,[352] lack of
incomplete data  limit setting,[349] small business loan  transparency,[347] limited data sources,[13]
|     |     | evaluation,[350] peer-to-peer lending risk[351]  | regulatory barriers,[353] explainability  |
| --- | --- | ------------------------------------------------ | ----------------------------------------- |
issues[347]
Algorithmic trading[18]  High market  Automated buy/sell execution,[354] arbitrage  Overfitting models,[320] flash crash risk,[357]
volatility  strategy deployment,[355] trend-following  high transaction costs,[359] latency
|     |     | bots,[356] high-frequency trading,[357] portfolio  | sensitivity, market regime changes[360]  |
| --- | --- | -------------------------------------------------- | ---------------------------------------- |
rebalancing[358]
Robo-advisory[37]  Automated portfolio management,[361] risk  Limited personalization,[366] regulatory
Low user trust
|     |     | profiling for clients,[362] tax optimization  | constraints,[367] user trust issues,[368] lack of  |
| --- | --- | --------------------------------------------- | -------------------------------------------------- |
|     |     | strategies,[363] goal-based investment        | human insight,[369] data dependency[1]             |
planning,[364] retirement savings
automation[365]
Risk management[370]  Complex risk  Market risk forecasting,[335] credit analysis,[371]  Incomplete data,[320] scenario coverage
factors  stress testing portfolios,[372] liquidity risk  limits,[375] stress test assumptions,[376]
|     |     | monitoring,[373] operational risk detection[374]  | response lag[377]  |
| --- | --- | ------------------------------------------------- | ------------------ |
Customer service  Limited language  AI chatbots for inquiries,[379] 24/7 virtual  Limited empathy,[383] misunderstanding
automation[378]  understanding  assistants,[228] automated complaint  intent,[384] language limitations,[385]
|     |     | resolution,[380] loan application support,[381]  | escalation issues,[386] data privacy  |
| --- | --- | ------------------------------------------------ | ------------------------------------- |
|     |     | transaction status updates[382]                  | concerns[303]                         |

automated market analysis tool could generate a report based  institutions increasingly rely on AI for core functions, these
on  hallucinated  economic  data,  leading  to  misguided  systems become attractive targets for adversarial attacks.[300]
investment decisions.[298] The core technical challenge is to  An adversarial attack involves making small, often
ensure  the  factual  grounding  of  generative  models.  imperceptible, perturbations to a model's input data with the
Techniques such as retrieval augmented generation (RAG),[299]  goal of inducing an incorrect output. In fintech, this could
which enable a model to retrieve and incorporate information  manifest as manipulating input data to have a fraudulent
from a verified knowledge base before generating a response,  transaction approved or to trigger a desirable outcome in an
represent a promising direction for mitigating this significant  algorithmic trading system.[301] AI models in finance and other
risk.  domains faced adversarial attacks, data poisoning, model
Security is another critical technical concern. As financial   inversion, and evasion tactics that reduced reliability and
Engineered Science Publisher                                                                                                                                    Eng. Sci., 2026, 41, 2245| 15

Review article Engineered Science
Fig. 6: A conceptual roadmap from 2026-2036 of AI in fintech across applications, technologies, system architecture, and
governance constraints. Solid elements represent developments supported by current empirical or industry evidence, while dashed
elements indicate forward looking or more speculative trajectories. Arrows denote directional evolution and increasing system
autonomy across time.
exposed sensitive information. The main challenges lay in the scoring and fraud detection, this made bias auditing, the use of
high dimensionality of input data, the opacity of deep models, representative data, and fairness aware model design essential
the dynamic nature of adversaries, and the trade off between for reducing the risk of systematically unfair outcomes across
robustness and accuracy. Defences included adversarial demographic and socioeconomic groups. Importantly, fairness
training to expose models to perturbed inputs, differential was not defined by a single criterion. Demographic parity
privacy and regularization to limit information leakage, focused on whether positive outcomes were distributed at
anomaly detection to flag manipulated queries and monitoring similar rates across groups, whereas equalized odds focused
with human in the loop oversight. Despite progress, defending on whether error rates were balanced conditional on actual
AI models required continuous adaptation since attackers outcomes. In financial practice, these definitions often created
evolved strategies quickly and traditional static defenses often trade offs because a model that satisfied one fairness objective
degraded under novel threats. did not necessarily satisfy another, particularly when default
Furthermore, the potential for AI models to perpetuate and risk distributions differed across groups. Empirical studies in
even amplify existing societal biases is a significant ethical credit scoring and credit ratings showed that fairness
and technical challenge.[302] AI systems learn from historical interventions could reduce disparate impact, but they could
data, and if this data reflects past discriminatory practices, the also affect predictive accuracy, profitability, and approval
resulting models will inherit these biases. In fintech policies, which highlighted a practical fairness versus
applications like credit scoring, this can lead to unfair or performance trade off in regulated financial settings.[145] For
discriminatory outcomes for certain demographic groups, this reason, implementing a system that was both accurate and
even if sensitive attributes like race or gender are excluded demonstrably fair according to legal and ethical standards
from the model's input. Ensuring fairness requires careful remained a major technical hurdle for the industry.
auditing of data and models, as well as the development of The dynamic and stringent regulatory landscape presents
fairness aware machine learning algorithms.[145] More an ongoing technical challenge for AI adoption in fintech.
specifically, AI systems trained on historical or socially Financial institutions must ensure their AI systems comply
derived data could inadvertently reproduce structural with a complex web of regulations governing data privacy,
inequities when the underlying data reflected patterns of model risk management, and consumer protection.[303]
exclusion or discrimination. In applications such as credit Translating these legal and ethical principles into concrete
16 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
technical specifications for AI systems is not straightforward. language processing, generative AI, autonomous agents and
This requires the development of new frameworks for AI multi-agent systems. These developments are expanding the
governance, model validation, and continuous monitoring to scope of fintech from task-specific automation towards
ensure that systems operate within prescribed boundaries over adaptive, interactive and increasingly autonomous financial
their entire lifecycle.[142] workflows. In this context, AI agents are especially important
AI driven financial decision making also raised because they connect data interpretation, reasoning, tool use
substantive ethical and governance concerns beyond technical and sequential decision-making, thereby offering a new model
performance alone. The review showed that algorithmic bias for intelligent financial services rather than merely improving
remained a major risk because models learned from historical existing predictive pipelines.
financial data that could encode past discrimination, which in The long-term value of AI in fintech will depend less on
turn could produce unfair outcomes in credit scoring, risk technical performance alone than on whether these systems
assessment, and customer targeting even when protected can be made robust, interpretable, fair, secure and governable
attributes were excluded from model inputs. It also showed in high-stakes financial environments. Persistent challenges
that accountability and traceability were essential in high remain in data quality and privacy, model opacity, algorithmic
stakes financial contexts because institutions had to explain bias, adversarial vulnerability, hallucination in generative
how automated decisions were produced, identify the data and models, regulatory compliance and human oversight. Future
model factors that shaped those outcomes, and maintain research should therefore move beyond accuracy-centred
auditable records for internal governance and regulatory evaluation and develop integrated frameworks for trustworthy
review. In addition, data governance remained central to financial AI, including privacy-preserving learning, domain-
responsible deployment. Financial institutions had to address specific explainability, fairness-aware validation, agent safety,
privacy, informed consent, lawful data use, and secure data continuous monitoring and regulatory auditability. The next
sharing, particularly when alternative data and cross platform stage of AI-driven fintech will require closer coordination
behavioral information were incorporated into model between technical innovation, institutional governance and
development. These concerns extended to model risk responsible regulation. If these challenges are addressed, AI
management, where validation, monitoring, and lifecycle has the potential not only to improve efficiency and
controls were needed to detect drift, bias, hallucination, and personalization in financial services, but also to support a
adversarial vulnerabilities after deployment. Taken together, more transparent, accountable and resilient financial
these issues showed that responsible AI adoption in fintech ecosystem.
depended not only on predictive accuracy, but also on fairness, A significant shift is underway from general purpose AI
transparency, privacy protection, and continuous compliance models to highly specialized financial foundation models and
with evolving regulatory frameworks. autonomous agents capable of complex reasoning and
Table 4 summarized how different AI applications in decision making.[387] These autonomous systems are poised to
fintech such as voice recognition, sentiment analysis, fraud revolutionize core financial processes by operating with
detection, credit scoring, algorithmic trading, robo advisory, minimal human input to perform tasks like dynamic portfolio
risk management, and customer service automation faced rebalancing, real time risk analysis, and automated compliance
domain specific challenges and practical limitations despite checks.[388] The development of AI agents that can perceive
offering diverse applications across financial services. their environment, analyze vast streams of information, and
execute actions to achieve specific financial goals will move
5. Conclusion and outlook the industry closer to a state of autonomous finance. This will
Artificial intelligence has moved from being a set of isolated enable financial institutions to enhance workflow
analytical tools to becoming a foundational infrastructure for optimization, improve customer experiences, and strengthen
financial technology. Across lending, payments, fraud decision making, thereby gaining a significant competitive
detection, trading, wealth management, customer service and advantage.
compliance, AI systems are reshaping how financial Fig. 6 presents a structured roadmap of the evolution of
information is processed, how risks are assessed and how artificial intelligence in financial technology over the period
financial decisions are delivered. This Review has shown that 2026 to 2036, integrating developments across applications,
the field is no longer defined only by conventional machine- underlying technologies, system architecture, and governance
learning models for prediction and classification, but constraints within a unified analytical framework. The
increasingly by the convergence of deep learning, natural roadmap illustrates a staged transition from predictive and task
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 17

Review article Engineered Science
specific machine learning systems toward generative AI and, unlock capabilities previously thought impossible. Quantum
subsequently, agentic and multi-agent financial systems with Machine Learning (QML)[398] holds the potential to solve
increasing levels of autonomy. In the near term, developments complex optimization problems in portfolio management and
are primarily grounded in established machine learning, risk assessment at speeds and scales unattainable for classical
explainable AI, and early generative systems, which augment computers. This could revolutionize algorithmic trading and
decision making in areas such as credit assessment, fraud the development of sophisticated financial models. In parallel,
detection, and financial advisory services. The mid term phase generative AI is becoming a powerful tool for creating highly
is characterized by the scaling of domain specific large realistic financial market simulations.[399] These simulations
language models, retrieval augmented systems, and AI allow for robust stress testing of investment strategies and risk
copilots, alongside the emergence of orchestrated agent models against a wide range of potential economic scenarios,
workflows that extend automation across financial processes. enhancing financial stability and improving data driven
In the long term, a potential shift toward autonomous financial decision making.
ecosystems enabled by multi-agent coordination and self Finally, the future of AI in fintech will be shaped by the
improving systems, while explicitly recognizing that these symbiotic evolution of technology and regulation. As AI's role
trajectories remain constrained by technical, regulatory, and expands, regulatory bodies are developing more sophisticated
systemic considerations. frameworks to govern its use, ensuring fairness,
The future of customer interaction in fintech will be accountability, and stability.[400] This has spurred the growth of
defined by AI driven hyper personalization, moving far Regulatory Technology (RegTech) and Supervisory
beyond current segmentation and basic customization.[389] By Technology (SupTech), where AI itself is used as a tool for
leveraging real time data analytics and machine learning, monitoring compliance and overseeing financial markets.[401]
financial institutions can create uniquely tailored experiences, The integration of AI into these supervisory functions enables
products, and advice that align with an individual's specific regulators to analyze vast datasets in real time, identify
financial situation, behaviors, and life goals.[390] This approach systemic risks, and enforce regulations more effectively.[402]
allows banks to anticipate customer needs, provide proactive This collaborative and technology enabled approach to
financial guidance, and foster deeper, more meaningful governance will be essential for fostering responsible
relationships.[391] AI powered virtual assistants and chatbots innovation while safeguarding the integrity of the global
will evolve to handle more complex and nuanced interactions, financial system.
providing personalized support that improves accuracy,
accelerates response times, and ultimately enhances customer Acknowledgments
The authors would like to acknowledge the support from
satisfaction and loyalty.[392]
EPSRC Grant Number EP/R00661X/1 & EP/P02470X/1.
As AI systems become more powerful, the imperative to
address their inherent challenges with next generation
Data Availability
solutions grows stronger. The "black box" problem is being
Data sharing is not applicable to this research as no data were
actively countered by progress in explainable AI (XAI), which
generated or analysed.
aims to make model decisions transparent and auditable, a
critical requirement for regulatory compliance and building Ethical Approval
trust.[393] Research is increasingly focused on developing This article does not contain any studies with human
hybrid and inherently interpretable models that do not participants performed by any of the authors.
sacrifice predictive accuracy for transparency.[394]
Informed Consent
Simultaneously, the critical need for data privacy is being met
This article does not contain any studies with human
by the maturation of Privacy Enhancing Technologies
participants performed by any of the authors.
(PETs).[395] Techniques like homomorphic encryption,[396]
which allows computation on encrypted data, and federative
Conflict of Interest
learning[397] are enabling collaborative data analysis and model The authors declare that they have no known competing
training across institutions without exposing sensitive raw financial interests or personal relationships that could have
data, fostering innovation while upholding stringent privacy appeared to influence the work reported in this paper.
standards.
Looking further ahead, the convergence of AI with other Supporting Information
frontier technologies like quantum computing promises to Not applicable.
18 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
CRediT Statement 10.1016/j.ejor.2006.09.100.
Zhizhou Zhang: Writing - Original draft, Writing – Review [11] S. Lessmann, B. Baesens, H.-V. Seow, L. C. Thomas,
and editing, Visualisation, Validation, Methodology, Benchmarking state-of-the-art classification algorithms for credit
Investigation, Conceptualisation, Funding acquisition, Project scoring: an update of research, European Journal of Operational
administration. Meiqi Lu: Writing - Review and editing. All Research, 2015, 247, 124-136, doi: 10.1016/j.ejor.2015.05.030.
authors have read and agreed to the published version of the [12] N. F. Ryman-Tubb, P. Krause, W. Garn, How Artificial
manuscript. Intelligence and machine learning research impacts payment card
fraud detection: a survey and industry benchmark, Engineering
References Applications of Artificial Intelligence, 2018, 76, 130-157, doi:
[1] L. Cao, Q. Yang, P. S. Yu, Data science and AI in FinTech: 10.1016/j.engappai.2018.07.008.
an overview, International Journal of Data Science and [13] J. Jagtiani, C. Lemieux, The roles of alternative data and
Analytics, 2021, 12, 81-99, doi: 10.1007/s41060-021-00278-w. machine learning in fintech lending: Evidence from the
[2] M. Doumpos, C. Zopounidis, D. Gounopoulos, E. Platanakis, LendingClub consumer platform, Financial Management, 2019,
W. Zhang, Operational research and artificial intelligence 48, 1009-1029, doi: 10.1111/fima.12295.
methods in banking, European Journal of Operational Research, [14] A. E. Khandani, A. J. Kim, A. W. Lo, Consumer credit-risk
2023, 306, 1-16, doi: 10.1016/j.ejor.2022.04.027. models via machine-learning algorithms, Journal of Banking &
[3] J. W. Goodell, S. Kumar, W. M. Lim, D. Pattnaik, Artificial Finance, 2010, 34, 2767-2787, doi:
intelligence and machine learning in finance: Identifying 10.1016/j.jbankfin.2010.06.001.
foundations, themes, and research clusters from bibliometric [15] V. B. Djeundje, J. Crook, R. Calabrese, M. Hamid,
analysis, Journal of Behavioral and Experimental Finance, 2021, Enhancing credit scoring with alternative data, Expert Systems
32, 100577, doi: 10.1016/j.jbef.2021.100577. with Applications, 2021, 163, 113766, doi:
[4] D. B. Vuković, S. Dekpo-Adza, S. Matović, AI integration in 10.1016/j.eswa.2020.113766.
financial services: a systematic review of trends and regulatory [16] E. Kim, J. Lee, H. Shin, H. Yang, S. Cho, S.-K. Nam, Y.
challenges, Humanities and Social Sciences Communications, Song, J.-A. Yoon, J.-I. Kim, Champion-challenger analysis for
2025, 12, 562, doi: 10.1057/s41599-025-04850-8. credit card fraud detection: Hybrid ensemble and deep learning,
[5] S. Bahoo, M. Cucculelli, X. Goga, J. Mondolo, Artificial Expert Systems with Applications, 2019, 128, 214-224, doi:
intelligence in Finance: a comprehensive review through 10.1016/j.eswa.2019.03.042.
bibliometric and content analysis, Springer Nature Business & [17] B. Baesens, S. Höppner, T. Verdonck, Data engineering for
Economics, 2024, 4, 23, doi: 10.1007/s43546-023-00618-x. fraud detection, Decision Support Systems, 2021, 150, 113492,
[6] A. Shavandi, M. Khedmati, A multi-agent deep reinforcement doi: 10.1016/j.dss.2021.113492.
learning framework for algorithmic trading in financial markets, [18] T. Théate, D. Ernst, An application of deep reinforcement
Expert Systems with Applications, 2022, 208, 118124, doi: learning to algorithmic trading, Expert Systems with Applications,
10.1016/j.eswa.2022.118124. 2021, 173, 114632, doi: 10.1016/j.eswa.2021.114632.
[7] A. T. Khan, S. Li, X. Cao, Bridging finance and AI: a [19] B. Lim, S. Zohren, Time-series forecasting with deep
comprehensive survey of large language models in financial learning: a survey, Philosophical Transactions of the Royal
system, Digital Finance, 2025, 7, 679-701, doi: 10.1007/s42521- Society A: Mathematical, Physical and Engineering Sciences,
025-00146-3. 2021, 379, 20200209, doi: 10.1098/rsta.2020.0209.
[8] A. de-la-Rica-Escudero, E. C. Garrido-Merchán, M. [20] P. C. Tetlock, Giving content to investor sentiment: the role
Coronado-Vaca, Explainable post hoc portfolio management of media in the stock market, The Journal of Finance, 2007, 62,
financial policy of a Deep Reinforcement Learning agent, Public 1139-1168, doi: 10.1111/j.1540-6261.2007.01232.x.
Library of Science One, 2025, 20, e0315528, doi: [21] M. Adam, M. Wessel, A. Benlian, AI-based chatbots in
10.1371/journal.pone.0315528. customer service and their effects on user compliance, Electronic
[9] B. Fazlija, M. Ibraimi, A. Forouzandeh, A. Fazlija, Reasoning Markets, 2021, 31, 427-445, doi: 10.1007/s12525-020-00414-7.
with financial regulatory texts via Large Language Models, [22] E. Adamopoulou, L. Moussiades, Chatbots: history,
Journal of Behavioral and Experimental Finance, 2025, 47, technology, and applications, Machine Learning with
101067, doi: 10.1016/j.jbef.2025.101067. Applications, 2020, 2, 100006, doi:
[10] J. N. Crook, D. B. Edelman, L. C. Thomas, Recent 10.1016/j.mlwa.2020.100006.
developments in consumer credit risk assessment, European [23] H. Zhu, O. Vigren, I.-L. Söderberg, Implementing artificial
Journal of Operational Research, 2007, 183, 1447-1465, doi: intelligence empowered financial advisory services: a literature
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 19

Review article Engineered Science
review and critical research agenda, Journal of Business for fraud detection via context encoding and adaptive
Research, 2024, 174, 114494, doi: aggregation, Expert Systems with Applications, 2025, 261,
10.1016/j.jbusres.2023.114494. 125473, doi: 10.1016/j.eswa.2024.125473.
[24] J. Černevičienė, A. Kabašinskas, Explainable artificial [36] F. M. Talaat, A. Aljadani, M. Badawy, M. Elhosseini,
intelligence (XAI) in finance: a systematic literature review, Toward interpretable credit scoring: integrating explainable
Artificial Intelligence Review, 2024, 57, 216, doi: artificial intelligence with deep learning for credit card default
10.1007/s10462-024-10854-8. prediction, Neural Computing and Applications, 2024, 36, 4847-
[25] P. Weber, K. V. Carl, O. Hinz, Applications of Explainable 4865, doi: 10.1007/s00521-023-09232-2.
Artificial Intelligence in Finance: a systematic review of Finance, [37] D. Belanche, L. V. Casaló, C. Flavián, Artificial Intelligence
Information Systems, and Computer Science literature, in FinTech: understanding robo-advisors adoption among
Management Review Quarterly, 2024, 74, 867-907, doi: customers, Industrial Management & Data Systems, 2019, 119,
10.1007/s11301-023-00320-0. 1411-1430, doi: 10.1108/imds-08-2018-0368.
[26] M. Fundira, C. Mbohwa, AI ethics in banking services: a [38] Generative AI Market, https://market.us/report/generative-
systematic and bibliometric review of regulatory and consumer ai-market/.
perspectives, Discover Artificial Intelligence, 2025, 5, 319, doi: [39] R. Becerra-Vicario, B. Salas-Compás, L. Valcarce-Ruiz, S.
10.1007/s44163-025-00432-4. Serrano, J. Ramón, The impact of artificial intelligence in the
[27] Z. Zhang, C. Jiang, M. Lu, Fusion of sentiment and market financial sector: opportunities and challenges, International
signals for Bitcoin forecasting: a SentiStack network based on a Journal of Business & Management Studies, 2024, 5, 33-42, doi:
stacking LSTM architecture, Big Data and Cognitive Computing, 10.56734/ijbms.v5n10a4.
2025, 9, 161, doi: 10.3390/bdcc9060161. [40] M. Jakšič, M. Marinč, Relationship banking and information
[28] Z. Zhang, P. Mativenga, W. Zhang, S.-Q. Huang, Deep technology: the role of artificial intelligence and FinTech, Risk
learning-driven prediction of mechanical properties of 316L Management, 2019, 21, 1-18, doi: 10.1057/s41283-018-0039-y.
stainless steel metallographic by laser powder bed fusion, [41] O. Jangmin, J. Lee, J. W. Lee, B.-T. Zhang, Adaptive stock
Micromachines, 2024, 15, 1167, doi: 10.3390/mi15091167. trading with dynamic asset allocation using reinforcement
[29] Z. Zhang, Z. Z. Tao, R. Du, R. Huo, X. Zheng, Artificial learning, Information Sciences, 2006, 176, 2121-2147, doi:
intelligence informed hydrogel biomaterials in additive 10.1016/j.ins.2005.10.009.
manufacturing, Gels, 2025, 11, 981, doi: 10.3390/gels11120981. [42] K. Fu, D. Cheng, Y. Tu, L. Zhang, Credit card fraud
[30] Z. Zhang, Y. Wang, W. Wang, Machine learning in gel- detection using convolutional neural networks, Neural
based additive manufacturing: from material design to process Information Processing, Springer International Publishing,
optimization, Gels, 2025, 11, 582, doi: 10.3390/gels11080582. Cham, 2016, 483-490, doi: 10.1007/978-3-319-46675-0_53.
[31] H. Chikri, M. Kassou, Financial revolution: Innovation [43] H. AbouGrad, A. Qadoos, L. Sankuru, Financial Decision-
powered by FinTech and artificial intelligence, Journal of Making AI-Framework to Predict Stock Price Using LSTM
Theoretical and Applied Information Technology, 2024, 102, Algorithm and NLP-Driven Sentiment Analysis Model,
4145–4157. Proceedings on Engineering Sciences, 2025, https://uel-
[32] K. R. Janamolla, S. Balammagary, A. Mohammed, repository.worktribe.com/output/440235.
Blockchain Enabled Cybersecurity to Protect LLM Models in [44] H. K. Sriram, Integrating generative AI into financial
FinTech, International Journal of Advanced Research in reporting systems for automated insights and decision support,
Computer and Communication Engineering, 2024, 13, 392–396, Social Science Research Network Electronic Journal, 2025, doi:
doi: 10.17148/IJARCCE.2024.131262. 10.2139/ssrn.5232395.
[33] N. Bussmann, P. Giudici, D. Marinelli, J. Papenbrock, [45] M. Liutvinavicius, V. Sakalauskas, D. Kriksciuniene,
Explainable machine learning in credit risk management, Sentiment-based decision making model for financial markets,
Computational Economics, 2021, 57, 203-216, doi: Data Science: New Issues, Challenges and Applications, Springer
10.1007/s10614-020-10042-0. International Publishing, Cham, 2020, 297-313, ISBN - 978-3-
[34] T. T. Adewale, T. D. Olorunyomi, T. N. Odonkor, Big data- 030-39249-9.
driven financial analysis: a new paradigm for strategic insights [46] E. Bradley, M. Roman, K. Rafferty, B. Devereux,
and decision-making, International Journal of Frontiers in SynFinTabs: a dataset of synthetic financial tables for
Science and Technology Research, 2023, 4, 33-54, doi: information and table extraction, Document Analysis and
10.53294/ijfstr.2023.4.2.0060. Recognition – International Conference on Document Analysis
[35] C. Lou, Y. Wang, J. Li, Y. Qian, X. Li, Graph neural network and Recognition 2025 Workshops, Springer Nature, Charm,
20 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
2026, 85-100, ISBN - 978-3-032-09370-7. [57] M. W. McCracken, S. Ng, FRED-MD: a monthly database
[47] I. Aldasoro, L. Gambacorta, A. Korinek, V. Shreeti, M. for macroeconomic research, Journal of Business & Economic
Stein, Intelligent financial system: How AI is transforming Statistics, 2016, 34, 574-589, doi:
finance, Journal of Financial Stability, 2025, 81, 101472, doi: 10.1080/07350015.2015.1086655.
10.1016/j.jfs.2025.101472. [58] M.-A. Sicilia, E. García-Barriocanal, S. Sánchez-Alonso,
[48] S. S. Rahman, M. A. Islam, M. M. Alam, M. Zeba, M. A. Community curation in open dataset repositories: insights from
Rahman, S. S. Chowa, M. A. K. Raiaan, S. Azam, Hallucination zenodo, Procedia Computer Science, 2017, 106, 54-60, doi:
to truth: a review of fact-checking and factuality evaluation in 10.1016/j.procs.2017.03.009.
large language models, Artificial Intelligence Review, 2026, 59, [59] D. Brickley, M. Burgess, N. Noy, Google Dataset Search:
70, doi: 10.1007/s10462-025-11454-w. Building a search engine for datasets in an open Web ecosystem,
[49] L. Masanneck, S. G. Meuth, M. Pawlitzki, Evaluating base The World Wide Web Conference, Association for Computing
and retrieval augmented LLMs with document or online support Machinery, New York, 2019, 1365-1375, ISBN -
for evidence based neurology, Nature Partner Journals – Digital 9781450366748.
Medicine, 2025, 8, 137, doi: 10.1038/s41746-025-01536-y. [60] Z. Wei, J. Zhang, Z. Lin, J.-Y. Lee, N. Balasubramanian, M.
[50] R. Yang, Y. Ning, E. Keppo, M. Liu, C. Hong, D. S. Hoai, D. Samaras, Learning visual emotion representations from
Bitterman, J. C. L. Ong, D. S. W. Ting, N. Liu, Retrieval- web data, Institute of Electrical and Electronics Engineers /
augmented generation for generative artificial intelligence in Conference on Computer Vision and Pattern Recognition, WA,
health care, Nature Partner Journals Health Systems, 2025, 2, USA, June 13-19, 2020, 13103-13112, doi:
doi: 10.1038/s44401-024-00004-1. 10.1109/cvpr42600.2020.01312.
[51] A. Zafar, V. B. Parthasarathy, C. Le Van, S. Shahid, A. I. [61] R. Misra, News headlines dataset for sarcasm detection,
Khan, A. Shahid, Building trust in conversational AI: a review ArXiv, 2020, doi: 10.48550/arXiv.2212.06035.
and solution architecture using large language models and [62] L. Loukas, M. Fergadiotis, I. Chalkidis, E. Spyropoulou, P.
knowledge graphs, Big Data and Cognitive Computing, 2024, 8, Malakasiotis, I. Androutsopoulos, G. Paliouras, FiNER: financial
70, doi: 10.3390/bdcc8060070. numeric entity recognition for XBRL tagging, Proceedings of the
[52] P. M. S. Choi, S. H. Huang, Q. Wang, Large language 60th Annual Meeting of the Association for Computational
models in finance: an overview, Finance and Large Language Linguistics, Dublin, Ireland, 22 – 27 May, 2022, 4419–4431, doi:
Models, Springer Nature, Singapore, 2025, 1-26, ISBN - 978- 10.18653/v1/2022.acl-long.303.
981-96-5832-9. [63] J. Huang, M. Xiao, D. Li, et al, Open-finllms: Open
[53] B. Oztas, D. Cetinkaya, F. Adedoyin, M. Budka, G. Aksu, multimodal large language models for financial applications,
H. Dogan, Transaction monitoring in anti-money laundering: a ArXiv, 2024, doi: 10.48550/arXiv.2408.11878.
qualitative analysis and points of view from industry, Future [64] G. Varoquaux, L. Buitinck, G. Louppe, O. Grisel, F.
Generation Computer Systems, 2024, 159, 161-171, doi: Pedregosa, A. Mueller, Scikit-learn: machine learning without
10.1016/j.future.2024.05.027. learning the machinery, GetMobile: Mobile Computing and
[54] Z. Chen, W. Chen, C. Smiley, S. Shah, I. Borova, D. Communications, 2015, 19, 29-33, doi:
Langdon, R. Moussa, M. Beane, T.-H. Huang, B. Routledge, W. 10.1145/2786984.2786995.
Y. Wang, FinQA: a dataset of numerical reasoning over financial [65] E. Stevens, L. Antiga, T. Viehmann, Deep Learning with
data, Proceedings of the Conference on Empirical Methods in PyTorch: Build, Train, and Tune Neural Networks Using Python
Natural Language Processing, Pennsylvania, USA, 2021, doi: Tools, Manning Publications, 2020, 520, ISBN - 978-
10.18653/v1/2021.emnlp-main.300. 1617295740.
[55] J. Magomere, E. Kochkina, S. Mensah, S. Kaur, C. Smiley, [66] A. Gulli, S. Pal, Deep Learning with Keras, Packt Publishing
FinNLI: novel dataset for multi-genre financial natural language Ltd, 2017, ISBN: 978-1787128422.
inference benchmarking, Findings of the Association for [67] S. Lagouvardos, J. Dolby, N. Grech, A. Antoniadis, Y.
Computational Linguistics: North American Chapter of the Smaragdakis, Static Analysis of Shape in TensorFlow Programs,
Association for Computational Linguistics, Pennsylvania, USA, In 34th European Conference on Object-Oriented Programming,
April 29 – May 4, 2025, 4545–4568, doi: Leibniz International Proceedings in Informatics, 2020, 166,
10.18653/v1/2025.findings-naacl.257. 15:1-15:29, doi: 10.4230/LIPIcs.ECOOP.2020.15.
[56] M. Hirano, Construction of a Japanese financial benchmark [68] K. Aman, Amanat acquisition corporation, Financial Reports
for large language models, Social Science Research Network SEC, 2026.
Electronic Journal, 2024, 28–35, doi: 10.2139/ssrn.4769124. [69] J. H. Stock, M. W. Watson, Business Cycle Properties of
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 21

Review article Engineered Science
Selected US Economic Time Series, 1990, 1959-1988, doi: [84] F. T. Peters, O. H. Drummer, F. Musshoff, Validation of new
10.3386/w3376. methods, Forensic Science International, 2007, 165, 216-224,
[70] G. Ascari, A. M. Sbordone, The macroeconomics of trend doi: 10.1016/j.forsciint.2006.05.021.
inflation, Journal of Economic Literature, 2014, 52, 679-739, [85] I. McDowell, C. Jenkinson, Development standards for
doi: 10.1257/jel.52.3.679. health measures, Journal of Health Services Research & Policy,
[71] G. Elliott, A. Timmermann, Economic forecasting, Journal 1996, 1, 238-246, doi: 10.1177/135581969600100410.
of Economic Literature, 2008, 46, 3-56, doi: 10.1257/jel.46.1.3. [86] I. Peters, P. Kraker, E. Lex, C. Gumpenberger, J. I. Gorraiz,
[72] N. F. Johnson, P. Jefferies, P. M. Hui, Financial Market Zenodo in the spotlight of traditional and new metrics, Frontiers
Complexity, Oxford University Press, 2003, doi: in Research Metrics and Analytics, 2017, 2, 13, doi:
10.1093/acprof:oso/9780198526650.001.0001. 10.3389/frma.2017.00013.
[73] C. Adelle, S. Weiland, Policy assessment: the state of the art, [87] H. A. Piwowar, W. W. Chapman, Public sharing of research
Impact Assessment and Project Appraisal, 2012, 30, 25-33, doi: datasets: a pilot study of associations, Journal of Informetrics,
10.1080/14615517.2012.663256. 2010, 4, 148-156, doi: 10.1016/j.joi.2009.11.010.
[74] A. Halevy, F. Korn, N. F. Noy, C. Olston, N. Polyzotis, S. [88] S.-E. Schapke, J. Beetz, M. König, C. Koch, A. Borrmann,
Roy, S. E. Whang, Goods: organizing google’s datasets, Collaborative data management, Building Information Modeling,
Proceedings of the International Conference on Management of Springer International Publishing, Cham, 2018, 251-277, ISBN -
Data, Association for Computing Machinery, 2016, 795 - 806, 978-3-319-92861-6.
ISBN - 9781450335317. [89] A. Gutierrez, N. Searby, I. DeLoatch, E. Frazier,
[75] S. Bang, M. O. Aarvold, W. J. Hartvig, N. O. E. Olsson, A. SectorInsights.org: AmeriGEOSS: a framework for capacity
Rauzy, Application of machine learning to limited datasets: building and collaboration in the americas, Photogrammetric
prediction of project success, Journal of Information Technology Engineering & Remote Sensing, 2018, 84, 477-479, doi:
in Construction, 2022, 27, 732-755, doi: 10.14358/pers.84.8.477.
10.36680/j.itcon.2022.036. [90] Gutierrez-Magness, A. et al., GEO Global Water
[76] M. Meyer, Academic entrepreneurs or entrepreneurial Sustainability (GEOGLOWS): Earth Observations for
academics? research–based ventures and public support sustainability in water management in the Americas and around
mechanisms, Research and Development Management, 2003, 33, the world, International Water Resources Associations, Mexico,
107-115, doi: 10.1111/1467-9310.00286. 29 May - 3 June, 2017.
[77] M. Knight, Data journalism in the UK: a preliminary analysis [91] H. Pundt, Y. Bishr, Domain ontologies for data sharing–an
of form and content, Journal of Media Practice, 2015, 16, 55-72, example from environmental monitoring using field GIS,
doi: 10.1080/14682753.2015.1015801. Computers & Geosciences, 2002, 28, 95-102, doi:
[78] V. Stodden, Enabling reproducible research: Open licensing 10.1016/s0098-3004(01)00018-8.
for scientific innovation, International Journal of [92] C. Avalon-Cullen, C. Caudill, N. K. Newlands, M. Enenkel,
Communications Law and Policy, 2009, 13, 1-25, doi: Big data, small island: earth observations for improving flood and
10.7916/d8n01h1z. landslide risk assessment in Jamaica, Geosciences, 2023, 13, 64,
[79] M. Bahrami, S. M. Arabzad, M. Ghorbani, Innovation in doi: 10.3390/geosciences13030064.
market management by utilizing business intelligence: [93] C. H. Jakobsen, T. Hels, W. J. McLaughlin, Barriers and
introducing proposed framework, Procedia - Social and facilitators to integration among scientists in transdisciplinary
Behavioral Sciences, 2012, 41, 160-167, doi: landscape analyses: a cross-country comparison, Forest Policy
10.1016/j.sbspro.2012.04.020. and Economics, 2004, 6, 15-31, doi: 10.1016/s1389-
[80] G. Greene, R. Plante, R. Hanisch, Building open access to 9341(02)00080-1.
research (OAR) data infrastructure at NIST, Data Science [94] R. A. Ims, N. G. Yoccoz, Ecosystem-based monitoring in the
Journal, 2019, 18, 30, doi: 10.5334/dsj-2019-030. age of rapid climate change and new technologies, Current
[81] Plan, National Institute of Standards and Technology. Opinion in Environmental Sustainability, 2017, 29, 170-176, doi:
[82] J. Rauber, W. Brendel, M. Bethge, Foolbox: A python 10.1016/j.cosust.2018.01.003.
toolbox to benchmark the robustness of machine learning models, [95] C. Feng, D. Yang, B.-M. Hodge, J. Zhang, OpenSolar:
ArXiv, 2017, doi: 10.48550/arXiv.1707.04131. Promoting the openness and accessibility of diverse public solar
[83] M. R. Garey, R. L. Graham, Performance bounds on the datasets, Solar Energy, 2019, 188, 1369-1379, doi:
splitting algorithm for binary testing, Acta Informatica, 1974, 3, 10.1016/j.solener.2019.07.016.
347-355, doi: 10.1007/BF00263588. [96] R. L. Peterson, Trading on Sentiment: The Power of Minds
22 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Over Markets, John Wiley & Sons, 2016, 368, ISBN - extraction approach with evidence from Fortune 500 companies,
9781119219149. Technological Forecasting and Social Change, 2024, 200,
[97] V. S. Pagolu, K. N. Reddy, G. Panda, B. Majhi, Sentiment 123154, doi: 10.1016/j.techfore.2023.123154.
analysis of Twitter data for predicting stock market movements, [109] C. Freudlsperger, S. Meunier, When foreign policy
International Conference on Signal Processing, Communication, becomes trade policy: the EU’s anti-coercion instrument, Journal
Power and Embedded System, Odisha, India, October 3-5, 2016, of Common Market Studies, 2024, 62, 1063-1079, doi:
1345-1350, doi: 10.1109/scopes.2016.7955659. 10.1111/jcms.13593.
[98] S. Jiang, H. Chen, J. F. Nunamaker, D. Zimbra, Analyzing [110] S. Setty, H. Thakkar, A. Lee, E. Chung, N. Vidra,
firm-specific social media and market: a stakeholder-based event Improving retrieval for rag based question answering models on
analysis framework, Decision Support Systems, 2014, 67, 30-39, financial documents, ArXiv, 2024, doi:
doi: 10.1016/j.dss.2014.08.001. 10.48550/arXiv.2404.07221.
[99] D. Araci, Finbert: Financial sentiment analysis with pre- [111] S. Sharma, S. Khatuya, M. Hegde, A. Shaikh, K. Dasgupta,
trained language models, ArXiv, 2019, P. Goyal, N. Ganguly, Financial numeric extreme labelling: a
doi:10.48550/arXiv.1908.10063. dataset and benchmarking, Findings of the Association for
[100] E. P. Torres, E. A. Torres, M. Hernandez-Alvarez, S. G. Computational Linguistics, Toronto, Canada, July 9–14, 2023,
Yoo, Emotion recognition related to stock trading using machine 3550–3561, doi: 10.18653/v1/2023.findings-acl.219.
learning algorithms with feature selection, Institute of Electrical [112] A. Rizvi, N. Thamindu, A. M. N. H. Adhikari, W. P. U.
and Electronics Engineers Access, 2020, 8, 199719-199732, doi: Senevirathna, D. Kasthurirathna, L. Abeywardhana, Enhancing
10.1109/access.2020.3035539. Multilingual Sentiment Analysis with Explainability for Sinhala,
[101] L. Malandri, F. Z. Xing, C. Orsenigo, C. Vercellis, E. English, and Code-Mixed Content, ArXiv, 2025,
Cambria, Public mood–driven asset allocation: the importance of doi:10.48550/arXiv.2504.13545.
financial sentiment in portfolio management, Cognitive [113] A. Iana, G. Glavaš, H. Paulheim, MIND Your Language: A
Computation, 2018, 10, 1167-1176, doi: 10.1007/s12559-018- Multilingual Dataset for Cross-lingual News Recommendation,
9609-2. ArXiv, 2024, 553–563, doi: 10.48550/arXiv.2403.17876.
[102] K. Baraniak, M. Sydow, A dataset for Sentiment analysis [114] H. W. A. Hanley, Z. Durumeric, Machine-made media:
of Entities in News headlines (SEN), Procedia Computer monitoring the mobilization of machine-generated articles on
Science, 2021, 192, 3627-3636, doi: misinformation and mainstream news websites, Proceedings of
10.1016/j.procs.2021.09.136. the International Association for the Advancement of Artificial
[103] A. Fedyk, Front-page news: the effect of news positioning Intelligence Conference on Web and Social Media, 2024, 18, 542-
on financial markets, The Journal of Finance, 2024, 79, 5-33, doi: 556, doi: 10.1609/icwsm.v18i1.31333.
10.1111/jofi.13287. [115] K. Ahmad, D. Cheng, Y. Almas, Multi-lingual sentiment
[104] Y. Chen, A Study on News Headline Classification Based analysis of financial news streams, 1st International Workshop on
on BERT Modeling, Proceedings of the 2nd International Grid Technology for Financial Modeling and Simulation, 2007,
Conference on Image, Algorithms and Artificial Intelligence, 26, doi: 10.22323/1.026.0001.
Atlantis Press, 2024, 345–355, ISBN - 978-94-6463-540-9. [116] M. Holecek, A. Hoskovec, P. Baudis, P. Klinger, Table
[105] A. Mehra, S. Singh, Event-driven architectures for real- understanding in structured documents, International Conference
time error resolution in high-frequency trading systems, on Document Analysis and Recognition Workshops, Sydney,
International Journal of Research in Modern Engineering and Australia, September 22-25, 2019, doi:
Emerging Technology, 2024, 12, 671, doi: 10.1109/icdarw.2019.40098.
10.63345/ijrmeet.org.v12.i12.31. [117] J. Smailović, M. Žnidaršič, A. Valentinčič, I. Lončarski, M.
[106] A. Boris, S. Martin, Real-Time Threat Detection in Forex Pahor, P. T. Martins, S. Pollak, Automatic analysis of annual
Markets Using AI and Big Data Analytics, 2024. financial reports: a case study, Computing and Systems, 2018, 21,
[107] H. Zhang, Y. Dang, Y. Zhang, S. Liang, J. Liu, L. Ji, 809–818, doi: 10.13053/cys-21-4-2863.
Chinese nested entity recognition method for the finance domain [118] K. C. Nguyen, C. T. Nguyen, M. Nakagawa, Nom
based on heterogeneous graph network, Information Processing document digitalization by deep convolution neural networks,
& Management, 2024, 61, 103812, doi: Pattern Recognition Letters, 2020, 133, 8-16, doi:
10.1016/j.ipm.2024.103812. 10.1016/j.patrec.2020.02.015.
[108] B.-X. Hsu, Y.-M. Chen, Does corporate social [119] J. Qin, W. Zhang, R. Su, Z. Liu, W. Liu, R. Tang, X. He,
responsibility influence performance persistence? A signal Y. Yu, Retrieval & interaction machine for tabular data prediction,
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 23

Review article Engineered Science
Association for Computing Machinery's Special Interest Group Cognitive Science, 2016, 7, 92-111, doi: 10.1002/wcs.1378.
on Knowledge Discovery and Data Mining, Singapore, August [133] S. Paneru, I. Jeelani, Computer vision applications in
14–18, 2021, 1379 – 1389, doi: 10.1145/3447548.3467216. construction: Current state, opportunities & challenges,
[120] G. Hackeling, Mastering Machine Learning with Scikit- Automation in Construction, 2021, 132, 103940, doi:
Learn, Packt Publishing Ltd, 2017, ISBN - 978-1-78829-987-9. 10.1016/j.autcon.2021.103940.
[121] I. Ridwana, N. Nassif, W. Choi, Modeling of building [134] Y. Xiao, W. Y. Wang, Quantifying uncertainties in natural
energy consumption by integrating regression analysis and language processing tasks, Proceedings of the Association for the
artificial neural network with data classification, Buildings, 2020, Advancement of Artificial Intelligence Conference on Artificial
10, 198, doi: 10.3390/buildings10110198. Intelligence, 2019, 33, 7322-7329, doi:
[122] G. Bonaccorso, Hands-on Unsupervised Learning with 10.1609/aaai.v33i01.33017322.
Python: Implement Machine Learning and Deep Learning [135] E. Wang, J. J. Davis, R. Zhao, H.-C. Ng, X. Niu, W. Luk,
Models Using Scikit-Learn, TensorFlow and More, Packt P. Y. K. Cheung, G. A. Constantinides, Deep neural network
Publishing Ltd, 2019, ISBN - 1789348277. approximation for custom hardware: where we’ve been, where
[123] V. Çetin, O. Yıldız, A comprehensive review on data we’re going, Association for Computing Machinery Computing
preprocessing techniques in data analysis, Pamukkale University Surveys, 2020, 52, 1-39, doi: 10.1145/3309551.
Journal of Engineering Sciences, 2022, 28, 299-312, doi: [136] J. Gardner, G. Pleiss, K. Q. Weinberger, D. Bindel, A. G.
10.5505/pajes.2021.62687. Wilson, Gpytorch: Blackbox matrix-matrix gaussian process
[124] N. Oreskes, Evaluation (not validation) of quantitative inference with gpu acceleration, Advances in Neural Information
models, Environmental Health Perspectives, 1998, 106, 1453- Processing Systems, 2018, 31, doi: 10.48550/arXiv.1809.11165.
1460, doi: 10.1289/ehp.98106s61453. [137] B. T. Chicho, A. Bibo Sallow, A comprehensive survey of
[125] J. J. A. Mendes Jr, M. L. B. Freitas, H. V. Siqueira, A. E. deep learning models based on keras framework, Journal of Soft
Lazzaretti, S. F. Pichorim, S. L. Stevan Jr, Feature selection and Computing and Data Mining, 2021, 2, 49-62, doi:
dimensionality reduction: an extensive comparison in hand 10.30880/jscdm.2021.02.02.005.
gesture classification by sEMG in eight channels armband [138] A. Garg, K. Tai, M. M. Savalani, State-of-the-art in
approach, Biomedical Signal Processing and Control, 2020, 59, empirical modelling of rapid prototyping processes, Rapid
101920, doi: 10.1016/j.bspc.2020.101920. Prototyping Journal, 2014, 20, 164-178, doi: 10.1108/rpj-08-
[126] Abadi, M. et al, TensorFlow: a system for Large-Scale 2012-0072.
machine learning, ArXiv, 2016, 265–283, doi: [139] W. Rawat, Z. Wang, Deep convolutional neural networks
10.48550/arXiv.1605.08695. for image classification: a comprehensive review, Neural
[127] D. M. Skapura, Building Neural Networks, Addison- Computation, 2017, 29, 2352-2449, doi: 10.1162/neco_a_00990.
Wesley Professional, Massachusetts, 1996, 304, ISBN - 10: 0- [140] S. Zargar, Introduction to sequence learning models: RNN,
201-53921-7. LSTM, GRU, Department of Mechanical and Aerospace
[128] S. Dupont, J. Luettin, Audio-visual speech modeling for Engineering, North Carolina State University, Preprints, 2021,
continuous speech recognition, Institute of Electrical and doi: 10.13140/RG.2.2.36370.99522.
Electronics Engineers Transactions on Multimedia, 2000, 2, 141- [141] Ł. Kidziński, M. Giannakos, D. G. Sampson, P.
151, doi: 10.1109/6046.865479. Dillenbourg, A tutorial on machine learning in educational
[129] T. Ganegedara, Natural Language Processing with science, State-of-the-Art and Future Directions of Smart
TensorFlow: Teach Language to Machines Using Python’s Deep Learning, Springer, Singapore, 2015, 453-459, ISBN - 10: 981-
Learning Library, Packt Publishing Ltd, 2018, ISBN - 978-1- 287-868-8.
78847-831-1. [142] Z. Syed, O. Okegbola, C. A. Akiotu, Utilising Artificial
[130] L. P. Kaelbling, M. L. Littman, A. W. Moore, Intelligence and Machine Learning for Regulatory Compliance in
Reinforcement learning: a survey, Journal of Artificial Financial Institutions, Idea Group Inc Global, 2024, 269-296, doi:
Intelligence Research, 1996, 4, 237-285, doi: 10.1613/jair.301. 10.4018/979-8-3693-5966-2.ch010.
[131] S. Imambi, K. B. Prakash, G. R. Kanagachidambaresan, [143] M. M. Kowsar, M. Mohiuddin, H. A. Mohna, Credit
PyTorch, Programming with TensorFlow, Springer International decision automation in commercial banks: a review of ai and
Publishing, Cham, 2021, 87-104, doi: 10.1007/978-3-030-57077- predictive analytics in loan assessment, American Journal of
4_10. Interdisciplinary Studies, 2023, 4, 1-26, doi: 10.63125/1hh4q770.
[132] M. Biehl, B. Hammer, T. Villmann, Prototype-based [144] Y. Chen, P. Giudici, K. Liu, E. Raffinetti, Measuring
models in machine learning, Wiley Interdisciplinary Reviews fairness in credit ratings, Expert Systems with Applications, 2024,
24 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
258, 125184, doi: 10.1016/j.eswa.2024.125184. Techniques for Long Financial Document, Discussion Papers No.
[145] N. Kozodoi, J. Jacob, S. Lessmann, Fairness in credit 317 Department of Economics and Management, University of
scoring: Assessment, implementation and profit implications, Pisa, 2024,
European Journal of Operational Research, 2022, 297, 1083- https://www.ec.unipi.it/documents/Ricerca/papers/2024-317.pdf.
1094, doi: 10.1016/j.ejor.2021.06.023. [157] Y. Huang, S. Meng, Automobile insurance classification
[146] S. Bhattacharyya, S. Jha, K. Tharakunnel, J. C. Westland, ratemaking based on telematics driving data, Decision Support
Data mining for credit card fraud: a comparative study, Decision Systems, 2019, 127, 113156, doi: 10.1016/j.dss.2019.113156.
Support Systems, 2011, 50, 602-613, doi: [158] H. Peiris, H. Jeong, J.-K. Kim, H. Lee, Integration of
10.1016/j.dss.2010.08.008. traditional and telematics data for efficient insurance claims
[147] M. Idrus, N. Adriana, A. Rustam, N. W. Sulistyowati, K. prediction, Actuarial Studies in Non-Life Insurance Bulletin,
A. Rewa, The impact of forensic accounting on financial fraud 2024, 54, 263-279, doi: 10.1017/asb.2024.6.
prevention: a comparative analysis across countries, The Journal [159] M. Denuit, A. Charpentier, J. Trufin, Autocalibration and
of Academic Science, 2024, 1, 1074-1084, doi: Tweedie-dominance for insurance pricing with machine learning,
10.59613/m6jrt421. Insurance: Mathematics and Economics, 2021, 101, 485-497, doi:
[148] C. Alzaman, Deep learning in stock portfolio selection and 10.1016/j.insmatheco.2021.09.001.
predictions, Expert Systems with Applications, 2024, 237, [160] X. Cheng, Z. Jin, H. Yang, Optimal insurance strategies: a
121404, doi: 10.1016/j.eswa.2023.121404. hybrid deep learning Markov chain approximation approach,
[149] L. Ni, Y. Li, X. Wang, J. Zhang, J. Yu, C. Qi, Forecasting Actuarial Studies in Non-Life Insurance Bulletin, 2020, 50, 449-
of forex time series data based on deep learning, Procedia 477, doi: 10.1017/asb.2020.9.
Computer Science, 2019, 147, 647-652, doi: [161] K. W. De Bock, K. Coussement, A. De Caigny, R.
10.1016/j.procs.2019.01.189. Słowiński, B. Baesens, R. N. Boute, T.-M. Choi, D. Delen, M.
[150] H. Yun, M. Lee, Y. S. Kang, J. Seok, Portfolio management Kraus, S. Lessmann, S. Maldonado, D. Martens, M. Óskarsdóttir,
via two-stage deep learning with a joint cost, Expert Systems with C. Vairetti, W. Verbeke, R. Weber, Explainable AI for
Applications, 2020, 143, 113041, doi: Operational Research: a defining framework, methods,
10.1016/j.eswa.2019.113041. applications, and a research agenda, European Journal of
[151] Y. Jiang, J. Olmo, M. Atwi, Deep reinforcement learning Operational Research, 2024, 317, 249-272, doi:
for portfolio selection, Global Finance Journal, 2024, 62, 10.1016/j.ejor.2023.09.026.
101016, doi: 10.1016/j.gfj.2024.101016. [162] C. Rudin, Stop explaining black box machine learning
[152] C. Alzaman, Optimizing portfolio selection through stock models for high stakes decisions and use interpretable models
ranking and matching: a reinforcement learning approach, Expert instead, Nature Machine Intelligence, 2019, 1, 206-215, doi:
Systems with Applications, 2025, 269, 126430, doi: 10.1038/s42256-019-0048-x.
10.1016/j.eswa.2025.126430. [163] A. J. Thirunavukarasu, D. S. J. Ting, K. Elangovan, L.
[153] L. Tunstall, L. Von Werra, T. Wolf, Natural Language Gutierrez, T. F. Tan, D. S. W. Ting, Large language models in
Processing with Transformers, O’Reilly Media, 2022, 408, ISBN medicine, Nature Medicine, 2023, 29, 1930-1940, doi:
- 978-1-098-13679-6. 10.1038/s41591-023-02448-8.
[154] F. R. Madadzade, Time Series Sentiment Analysis on [164] N. Karanikolas, E. Manga, N. Samaridi, E. Tousidou, M.
Financial Earnings Calls: A Deep Learning Approach Vassilakopoulos, Large language models versus natural language
Investigating the Combination of Sentiment Extracted from Text understanding and generation, Proceedings of the 27th Pan-
and Audio Data From Earnings Calls, KTH Royal Institute of Hellenic Conference on Progress in Computing and Informatics,
Technology, Stockholm, Sweden, Master’s Thesis, 2024, 2023, 278 – 290, doi: 10.1145/3635059.3635104.
https://kth.diva- [165] T. Koide, N. Fukushi, H. Nakano, D. Chiba,
portal.org/smash/record.jsf?pid=diva2%3A1885510&dswid= ChatSpamDetector: leveraging large language models for
-5804. effective phishing email detection, Security and Privacy in
[155] Y. Kong, Y. Nie, X. Dong, J. M. Mulvey, H. V. Poor, Q. Communication Networks, Springer Nature, Cham, 2025, 297-
Wen, S. Zohren, Large language models for financial and 319, ISBN - 978-3-031-94455-0.
investment management: applications and benchmarks, The [166] B. Ilse, F. Blackwood, Comparative analysis of finetuning
Journal of Portfolio Management, 2024, 51, 162-210, doi: strategies and automated evaluation metrics for large language
10.3905/jpm.2024.1.645. models in customer service chatbots, Preprints, 2024, doi:
[156] M. S. Mavillonio, Natural Language Processing 10.21203/rs.3.rs-4895456/v1.
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 25

Review article Engineered Science
[167] W. Zhang, Y. Deng, B. Liu, S. Pan, L. Bing, Sentiment September 13-16, Udupi, India, 2017, 1643-1647, doi:
analysis in the era of large language models: a reality check, 10.1109/icacci.2017.8126078.
Findings of the Association for Computational Linguistics, [180] H. Y. Kim, C. H. Won, Forecasting the volatility of stock
Mexico, USA, 17 – 19 June, 2024, 3881–3906, doi: price index: a hybrid model integrating LSTM with multiple
10.18653/v1/2024.findings-naacl.246. GARCH-type models, Expert Systems with Applications, 2018,
[168] M. M. Mohsan, M. U. Akram, G. Rasool, N. S. Alghamdi, 103, 25-37, doi: 10.1016/j.eswa.2018.03.002.
M. A. A. Baqai, M. Abbas, Vision transformer and language [181] P. Malhotra, A. Ramakrishnan, G. Anand, L. Vig, P.
model based radiology report generation, Institute of Electrical Agarwal, G. Shroff, LSTM-based Encoder-Decoder for Multi-
and Electronics Engineers Access, 2023, 11, 1814-1824, doi: sensor Anomaly Detection, ArXiv, 2016, doi:
10.1109/access.2022.3232719. 10.48550/arXiv.1607.00148.
[169] K. Gurney, An Introduction to Neural Networks, CRC [182] B. Lindemann, N. Jazdi, M. Weyrich, Anomaly detection
Press, 2018, ISBN - 9781315273570. and prediction in discrete manufacturing based on cooperative
[170] J. S. Almeida, Predictive non-linear modeling of complex LSTM networks, Institute of Electrical and Electronics
data by artificial neural networks, Current Opinion in Engineers 16th International Conference on Automation Science
Biotechnology, 2002, 13, 72-76, doi: 10.1016/s0958- and Engineering, Hong Kong, China, August 20-21, 2020, 1003-
1669(02)00288-4. 1010, doi: 10.1109/case48305.2020.9216855.
[171] D. West, Neural network credit scoring models, Computers [183] Z. Li, F. Liu, W. Yang, S. Peng, J. Zhou, A survey of
& Operations Research, 2000, 27, 1131-1152, doi: convolutional neural networks: analysis, applications, and
10.1016/s0305-0548(99)00149-5. prospects, Institute of Electrical and Electronics Engineers
[172] L. Di Persio, O. Honchar, Artificial neural networks Transactions on Neural Networks and Learning Systems, 2022,
architectures for stock price prediction: Comparisons and 33, 6999-7019, doi: 10.1109/tnnls.2021.3084827.
applications, International Journal of Circuits, Systems and [184] Y. H. Liu, Feature extraction and image recognition with
Signal Processing, 2016, 10, 403–413, convolutional neural networks, Journal of Physics: Conference
https://iris.univr.it/handle/11562/955101. Series, 2018, 1087, 062032, doi: 10.1088/1742-
[173] E. Angelini, G. di Tollo, A. Roli, A neural network 6596/1087/6/062032.
approach for credit risk evaluation, The Quarterly Review of [185] L. Kang, J. Kumar, P. Ye, Y. Li, D. Doermann,
Economics and Finance, 2008, 48, 733-755, doi: Convolutional neural networks for document image
10.1016/j.qref.2007.04.001. classification, 22nd International Conference on Pattern
[174] C. M. Bishop, Neural Networks for Pattern Recognition, Recognition, Stockholm, Sweden, August 24-28, 2014, 3168-
Oxford University Press, 1995, 482, ISBN - 9781383026382. 3172, doi: 10.1109/icpr.2014.546.
[175] J. Yao, Y. Li, C. L. Tan, Option price forecasting using [186] P. Agrawal, D. Chaudhary, V. Madaan, A. Zabrovskiy, R.
neural networks, Omega, 2000, 28, 455-466, doi: 10.1016/s0305- Prodan, D. Kimovski, C. Timmerer, Automated bank Cheque
0483(99)00066-3. verification using image processing and deep learning methods,
[176] Y. Yu, X. Si, C. Hu, J. Zhang, A review of recurrent neural Multimedia Tools and Applications, 2021, 80, 5319-5350, doi:
networks: LSTM cells and network architectures, Neural 10.1007/s11042-020-09818-1.
Computation, 2019, 31, 1235-1270, doi: 10.1162/neco_a_01199. [187] T. Zan, Z. Liu, H. Wang, M. Wang, X. Gao, Control chart
[177] S. M. Al-Selwi, M. F. Hassan, S. J. Abdulkadir, A. Muneer, pattern recognition using the convolutional neural network,
LSTM inefficiency in long-term dependencies regression Journal of Intelligent Manufacturing, 2020, 31, 703-716, doi:
problems, Journal of Advanced Research in Applied Sciences and 10.1007/s10845-019-01473-0.
Engineering Technology, 2023, 30, 16-31, doi: [188] Y. Zheng, C. Yang, A. Merkulov, Breast cancer screening
10.37934/araset.30.3.1631. using convolutional neural network and follow-up digital
[178] H. Abbasimehr, R. Paki, Improving time series forecasting mammography, Computational Imaging III, Orlando, USA, April
using LSTM and attention models, Journal of Ambient 15-19, 2018, 1066905, doi: 10.1117/12.2304564.
Intelligence and Humanized Computing, 2022, 13, 673-691, doi: [189] S. J. Rigatti, Random forest, Journal of Insurance
10.1007/s12652-020-02761-x. Medicine, 2017, 47, 31-39, doi: 10.17849/insm-47-01-31-39.1.
[179] S. Selvin, R. Vinayakumar, E. A. Gopalakrishnan, V. K. [190] H. B. Li, W. Wang, H. W. Ding, J. Dong, Trees weighting
Menon, K. P. Soman, Stock price prediction using LSTM, RNN random forest method for classifying high-dimensional noisy
and CNN-sliding window model, International Conference on data, IEEE 7th International Conference on E-Business
Advances in Computing, Communications and Informatics, Engineering, Shanghai, China, November 10-12, 2010, 160-163,
26 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
doi: 10.1109/icebe.2010.99. 10.1109/icsssm.2007.4280145.
[191] V. S. S. Nandipati, L. V. Boddala, Credit Card Approval [201] B. Gupta, A. Rawat, A. Jain, A. Arora, N. Dhami, Analysis
Prediction: A Comparative Analysis between Logistic Regression, of various decision tree algorithms for classification in data
KNN, Decision Trees, Random Forest, XGBoost. Karlskrona: mining, International Journal of Computer Applications, 2017,
Blekinge Institute of Technology, Sweden, Master’s Thesis, 2024, 163, 15-19, doi: 10.5120/ijca2017913660.
https://www.diva- [202] R. Dwivedi, D. Dave, H. Naik, S. Singhal, R. Omer, P.
portal.org/smash/record.jsf?pid=diva2%3A1883598&dswid=45 Patel, B. Qian, Z. Wen, T. Shah, G. Morgan, R. Ranjan,
95. Explainable AI (XAI): core ideas, techniques, and solutions,
[192] S. Xuan, G. Liu, Z. Li, L. Zheng, S. Wang, C. Jiang, Association for Computing Machinery Computing Surveys, 2023,
Random forest for credit card fraud detection, Institute of 55, 1-33, doi: 10.1145/3561048.
Electrical and Electronics Engineers 15th International [203] N. Thalpage, Unlocking the black box: explainable
Conference on Networking, Sensing and Control, Zhuhai, China, artificial intelligence (XAI) for trust and transparency in AI
March 27-29, 2018, 1-6, doi: 10.1109/icnsc.2018.8361343. systems, Journal of Digital Art & Humanities, 2023, 4, 31-36,
[193] H. Valecha, A. Varma, I. Khare, A. Sachdeva, M. Goyal, doi: 10.33847/2712-8148.4.1_4.
Prediction of consumer behaviour using random forest algorithm, [204] C. Panigutti, R. Hamon, I. Hupont, D. Fernandez Llorca, D.
5th Institute of Electrical and Electronics Engineers Uttar Fano Yela, H. Junklewitz, S. Scalzo, G. Mazzini, I. Sanchez, J.
Pradesh Section International Conference on Electrical, Soler Garrido, E. Gomez, The role of explainable AI in the
Electronics and Computer Engineering, Gorakhpur, India, context of the AI Act, Association for Computing Machinery
November 2-4, 2018, 1-6, doi: 10.1109/upcon.2018.8597070. Conference on Fairness, Accountability, and Transparency,
[194] M. Malekipirbazari, V. Aksakalli, Risk assessment in social Chicago, USA, 2023, 1139 - 1150, doi:
lending via random forests, Expert Systems with Applications, 10.1145/3593013.3594069.
2015, 42, 4621-4631, doi: 10.1016/j.eswa.2015.02.001. [205] C. A. Zhang, S. Cho, M. Vasarhelyi, Explainable artificial
[195] L. Yin, B. Li, P. Li, R. Zhang, Research on stock trend intelligence (XAI) in auditing, International Journal of
prediction method based on optimized random forest, Chinese Accounting Information Systems, 2022, 46, 100572, doi:
Association for Artificial Intelligence Transactions on 10.1016/j.accinf.2022.100572.
Intelligence Technology, 2023, 8, 274-284, doi: [206] I. Palatnik de Sousa, M. M. B. R. Vellasco, E. Costa da
10.1049/cit2.12067. Silva, Explainable artificial intelligence for bias detection in
[196] Y. Y. Song, Y. Lu, Decision tree methods: applications for COVID CT-scan classifiers, Sensors, 2021, 21, 5657, doi:
classification and prediction, Shanghai Archives of Psychiatry, 10.3390/s21165657.
2015, 27, 130-5, doi: 10.11919/j.issn.1002-0829.215044. [207] B. Hadji Misheva, A. Hirsa, J. Osterrieder, O. Kulkarni, S.
[197] J. Gama, R. Rocha, P. Medas, Accurate decision trees Fung Lin, Explainable AI in credit risk management, Social
for mining high-speed data streams, Proceedings of the 9th Science Research Network Electronic Journal, 2021, 1–16, doi:
Association for Computing Machinery Special Interest Group 10.2139/ssrn.3795322.
on Knowledge Discovery and Data Mining International [208] B. Chen, B. Huang, B. Xu, Comparison of spatiotemporal
Conference on Knowledge Discovery and Data Mining, fusion models: a review, Remote Sensing, 2015, 7, 1798-1835,
Washington, USA, 2003, 523 - 528, doi: doi: 10.3390/rs70201798.
10.1145/956750.956813. [209] T. Wang, R. Liu, G. Qi, Multi-classification assessment of
[198] H. C. Koh, W. C. Tan, C. P. Goh, A two-step method to bank personal credit risk based on multi-source information
construct credit scoring models with data mining techniques, fusion, Expert Systems with Applications, 2022, 191, 116236, doi:
International Journal of Business and Information, 2006, 1, 96– 10.1016/j.eswa.2021.116236.
118, https://api.semanticscholar.org/CorpusID:17400653. [210] S. Carta, A. Corriga, A. Ferreira, A. S. Podda, D. R.
[199] M. S. Sivasree, S. T. Rekha, Loan credibility prediction Recupero, A multi-layer and multi-ensemble stock trader using
system based on decision tree algorithm, International Journal of deep learning and deep reinforcement learning, Applied
Engineering Research & Technology, 2015, V4, doi: Intelligence, 2021, 51, 889-905, doi: 10.1007/s10489-020-
10.17577/ijertv4is090708. 01839-5.
[200] B. Luo, P. Shao, J. Liu, Customer churn prediction based [211] S. I. Lee, S. J. Yoo, Multimodal deep learning for finance:
on the decision tree in personal handyphone system service, integrating and forecasting international stock markets, The
International Conference on Service Systems and Service Journal of Supercomputing, 2020, 76, 8294-8312, doi:
Management, Changdu, China, June 9-11, 2007, 1-5, doi: 10.1007/s11227-019-03101-3.
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 27

Review article Engineered Science
[212] Y. Wang, J. Peng, J. Zhang, R. Yi, Y. Wang, C. Wang, August, 2019, 2810 - 2818, doi: 10.1145/3292500.3330668.
Multimodal industrial anomaly detection via hybrid fusion, The [223] P. Yu, J. S. Lee, I. Kulyatin, Z. Shi, S. Dasgupta, Model-
Institute of Electrical and Electronics Engineers / The Computer based deep reinforcement learning for dynamic portfolio
Vision Foundation Conference on Computer Vision and Pattern optimization. ArXiv, 2019, doi: 10.48550/arXiv.1901.08740.
Recognition, Vancouver, Canada, June 17-24, 2023, 8032-8041, [224] J. Cao, J. Chen, J. C. Hull, Z. Poulos, Deep hedging of
doi: 10.1109/cvpr52729.2023.00776. derivatives using reinforcement learning, Social Science
[213] D. K. Padhi, N. Padhy, A. K. Bhoi, J. Shafi, S. H. Yesuf, Research Network, Electronic Journal, 2019, doi:
An intelligent fusion model with portfolio selection and machine 10.2139/ssrn.3514586.
learning for stock market prediction, Computational Intelligence [225] T. Beysolow, Market making via reinforcement learning,
and Neuroscience, 2022, 2022, 7588303, doi: Applied Reinforcement Learning with Python, A Press, Berkeley,
10.1155/2022/7588303. 2019, 77-94, doi: 10.1007/978-1-4842-5127-0_4.
[214] S. Feuerriegel, J. Hartmann, C. Janiesch, P. Zschech, [226] D. K. Nguyen, G. Sermpinis, C. Stasinakis, Big data,
Generative AI, Business & Information Systems Engineering, artificial intelligence and machine learning: a transformative
2024, 66, 111-126, doi: 10.1007/s12599-023-00834-7. symbiosis in favour of financial technology, European Financial
[215] R. T. Hughes, L. Zhu, T. Bednarz, Generative adversarial Management, 2023, 29, 517-548, doi: 10.1111/eufm.12365.
networks–enabled human–artificial intelligence collaborative [227] P. Khare, S. Srivastava, Transforming KYC with AI: A
applications for creative and design industries: a systematic Comprehensive Review of Artificial Intelligence-Based Identity
review of current approaches and trends, Frontiers in Artificial Verification, Journal of Emerging Technologies and Innovative
Intelligence, 2021, 4, 604234, doi: 10.3389/frai.2021.604234. Research, 2023, 10, 525–531,
[216] M. Goyal, Q. H. Mahmoud, A systematic review of https://www.jetir.org/papers/JETIR2305G74.pdf.
synthetic data generation techniques using generative AI, [228] M. Mori, AI-powered virtual assistants in the realms of
Electronics, 2024, 13, 3509, doi: 10.3390/electronics13173509. banking and financial services, Virtual Assistant, IntechOpen,
[217] M. Xu, D. Niyato, J. Chen, H. Zhang, J. Kang, Z. Xiong, S. London, 2021, 1-12, ISBN - 978-1-83968-808-9.
Mao, Z. Han, Generative AI-empowered simulation for [229] V. Moscato, A. Picariello, G. Sperlí, A benchmark of
autonomous driving in vehicular mixed reality metaverses, The machine learning approaches for credit score prediction, Expert
Institute of Electrical and Electronics Engineers Journal of Systems with Applications, 2021, 165, 113986, doi:
Selected Topics in Signal Processing, 2023, 17, 1064-1079, doi: 10.1016/j.eswa.2020.113986.
10.1109/jstsp.2023.3293650. [230] Y. Chen, R. Calabrese, B. Martin-Barragan, Interpretable
[218] K. D. Betts, K. R. Jaep, The dawn of fully automated machine learning for imbalanced credit scoring datasets,
contract drafting: Machine learning breathes new life into a European Journal of Operational Research, 2024, 312, 357-372,
decades-old promise, Duke Law & Technology Review, 2016, 15, doi: 10.1016/j.ejor.2023.06.036.
216-233, https://scholarship.law.duke.edu/dltr/vol15/iss1/11. [231] G. Babaei, P. Giudici, How fair is machine learning in
[219] G. Blank, WHO CREATES CONTENT? : Stratification credit lending, Quality and Reliability Engineering International,
and content creation on the Internet, Information, Communication 2024, 40, 3452-3464, doi: 10.1002/qre.3579.
& Society, 2013, 16, 590-612, doi: [232] G. Saporta, S. Maraney, Practical Fraud Prevention:
10.1080/1369118x.2013.777758. Fraud and Aml Analytics for Fintech and eCommerce, Using Sql
[220] M. J. Meixell, S. D. Wu, Scenario analysis of demand in a and Python, O’Reilly Media, 2022, 396, ISBN - 1492093327.
technology market using leading indicators, The Institute of [233] R. Wang, J. Liu, W. Zhao, S. Li, D. Zhang, AuditBench: a
Electrical and Electronics Engineers Transactions on benchmark for large language models in financial statement
Semiconductor Manufacturing, 2001, 14, 65-75, doi: auditing, Artificial Intelligence for Research and Scalable,
10.1109/66.909656. Efficient Systems, Springer Nature, Singapore, 2025, 59-81,
[221] Y. Li, Deep reinforcement learning: An overview, ArXiv, ISBN - 978-981-96-8912-5.
2017, doi:10.48550/arXiv.1701.07274. [234] A. Patel, P. Oza, S. Agrawal, Sentiment analysis of
[222] L. Zou, L. Xia, Z. Ding, J. Song, W. Liu, D. Yin, customer feedback and reviews for airline services using
Reinforcement learning to optimize long-term user engagement language representation model, Procedia Computer Science,
in recommender systems, Proceedings of the 25th Association for 2023, 218, 2459-2467, doi: 10.1016/j.procs.2023.01.221.
Computing, Machinery Special Interest Group on Knowledge [235] J. S. Wang, Exploring biometric identification in FinTech
Discovery and Data Mining, International Conference on applications based on the modified TAM, Financial Innovation,
Knowledge Discovery & Data Mining, Anchorage, USA, 4 – 8 2021, 7, 42, doi: 10.1186/s40854-021-00260-2.
28 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
[236] N. Singh, A. Agrawal, R. A. Khan, Voice biometric: a customized offers: conceptual framework and research
technology for voice based authentication, Advanced Science, propositions, Journal of Marketing, 2005, 69, 32-45, doi:
Engineering and Medicine, 2018, 10, 754-759, doi: 10.1509/jmkg.69.1.32.55512.
10.1166/asem.2018.2219. [248] S. D. Rajan, V. Loganathan, Personal financial planning,
[237] J. Yamagishi, C. Veaux, S. King, S. Renals, Speech Multidisciplinary Approaches for Sustainable Development,
synthesis technologies for individuals with vocal disabilities: CRC Press, 1998, 183–189, ISBN - 9781032894904.
Voice banking and reconstruction, Acoustical Science and [249] B. H. W. Guo, Y. M. Goh, K. Le Xin Wong, A system
Technology, 2012, 33, 1-5, doi: 10.1250/ast.33.1. dynamics view of a behavior-based safety program in the
[238] P. C. Mondal, R. Deb, M. N. Huda, Transaction construction industry, Safety Science, 2018, 104, 202-215, doi:
authorization from Know Your Customer (KYC) information in 10.1016/j.ssci.2018.01.014.
online banking, 9th International Conference on Electrical and [250] S. O. Ikponmwoba, O. K. Chima, O. J. Ezeilo, B. M.
Computer Engineering, Dhaka, Bangladesh, December 20-22, Ojonugwa, A. Ochefu, M. O. Adesuyi, Conceptual framework for
2016, 523-526, doi: 10.1109/icece.2016.7853972. improving bank reconciliation accuracy using intelligent audit
[239] C. Qian, N. Mathur, N. H. Zakaria, R. Arora, V. Gupta, M. controls, Journal of Frontiers in Multidisciplinary Research,
Ali, Understanding public opinions on social media for financial 2020, 1, 57-70, doi: 10.54660/.ijfmr.2020.1.1.57-70.
sentiment analysis using AI-based techniques, Information [251] S. Mishra, A. Misra, Structured and unstructured big data
Processing & Management, 2022, 59, 103098, doi: analytics, International Conference on Current Trends in
10.1016/j.ipm.2022.103098. Computer, Electrical, Electronics and Communication, Mysore,
[240] J. Beneke, Marketing the institution to prospective Karnataka, India, September 8-9, 2017, 740-746, doi:
students–a review of brand (reputation) management in higher 10.1109/ctceec.2017.8454999.
education, International Journal of Business and Management, [252] A. Gatt, E. Krahmer, Survey of the State of the Art in
2010, 6, doi: 10.5539/ijbm.v6n1p29. Natural Language Generation: Core tasks, applications and
[241] J. J. Thompson, B. H. Leung, M. R. Blair, M. Taboada, evaluation, Journal of Artificial Intelligence Research, 2018, 61,
Sentiment analysis of player chat messaging in the video game 65-170, doi: 10.1613/jair.5477.
StarCraft 2: Extending a lexicon-based model, Knowledge-Based [253] J. Ding, T. Wu, J. Q. Lu, X.-H. Hu, Self-checked
Systems, 2017, 137, 149-162, doi: 10.1016/j.knosys.2017.09.022. metamorphic testing of an image processing program, Fourth
[242] S. Chamishka, I. Madhavi, R. Nawaratne, D. Alahakoon, International Conference on Secure Software Integration and
D. De Silva, N. Chilamkurti, V. Nanayakkara, A voice-based Reliability Improvement, Singapore, June 9-11, 2010, 190-197,
real-time emotion detection technique using recurrent neural doi: 10.1109/ssiri.2010.25.
network empowered feature modelling, Multimedia Tools and [254] K. Rathor, S. Vidya, M. Jeeva, M. Karthivel, S. N. Ghate,
Applications, 2022, 81, 35173-35194, doi: 10.1007/s11042-022- V. Malathy, Intelligent system for ATM fraud detection system
13363-4. using C-LSTM approach, 4th International Conference on
[243] S. Elkasrawi, F. Shafait, Printer identification using Electronics and Sustainable Communication Systems,
supervised learning for document forgery detection, 11th IAPR Coimbatore, Tamil Nadu, India, July 6-8, 2023, 1439-1444, doi:
International Workshop on Document Analysis Systems, Tours, 10.1109/icesc57686.2023.10193398.
France, April 7-10, 2014, 146-150, doi: 10.1109/das.2014.48. [255] D. Impedovo, G. Pirlo, Automatic signature verification:
[244] M. Aitken, D. Cumming, F. Zhan, Exchange trading rules, the state of the art, Institute of Electrical and Electronics
surveillance and suspected insider trading, Journal of Corporate Engineers Transactions on Systems, Man, and Cybernetics, Part
Finance, 2015, 34, 311-330, doi: 10.1016/j.jcorpfin.2015.07.013. C (Applications and Reviews), 2008, 38, 609-635, doi:
[245] O. O. Elumilade, I. A. Ogundeji, G. O. Achumie, H. E. 10.1109/tsmcc.2008.923866.
Omokhoa, B. M. Omowole, Enhancing fraud detection and [256] A. Realyvásquez Vargas, J. L. García Alcaraz, S.
forensic auditing through data-driven techniques for financial Satapathy, J. R. Díaz-Reza, Case study 2. raw material receipt
integrity and security, Journal of Advanced Education and process optimization, The Plan-Do-Check-Act Cycle for
Sciences, 2021, 1, 55-63, doi: 10.54660/.jaes.2021.1.2.55-63. Industrial Improvement, Springer Nature, Switzerland, 2023, 47-
[246] A. Capponi, S. Ólafsson, T. Zariphopoulou, Personalized 77, ISBN - 978-3-031-26805-2.
robo-advising: enhancing investment through client interaction, [257] P. Singh, AI-powered IVR and chat: a new era in telecom
Management Science, 2022, 68, 2485-2512, doi: troubleshooting, Social Science Research Network Electronic
10.1287/mnsc.2021.4014. Journal, 2025, 1-29, doi: 10.2139/ssrn.5218979.
[247] I. Simonson, Determinants of customers’ responses to [258] S. Ackerman, L. Alexander, M. Bennett, D. Chen, E.
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 29

Review article Engineered Science
Farchi, A. Houseknecht, P. Santhanam, Deploying automated X. Huang, Multimodal recurrent model with attention for
ticket router across the enterprise, Artificial Intelligence automated radiology report generation, Medical Image
Magazine, 2023, 44, 97-111, doi: 10.1002/aaai.12079. Computing and Computer Assisted Intervention, Springer
[259] V. Kasinathan, A. Mustapha, C. K. Bin, A customizable International Publishing, Cham, 2018, 457-466, ISBN - 978-3-
multilingual chatbot system for customer support, Annals of 030-00927-4.
Emerging Technologies in Computing, 2021, 5, 51-59, doi: [271] A. Figueira, B. Vaz, Survey on synthetic data generation,
10.33166/aetic.2021.05.006. evaluation methods and GANs, Mathematics, 2022, 10, 2733,
[260] D. M. Szymanski, D. H. Henard, Customer satisfaction: a doi: 10.3390/math10152733.
meta-analysis of the empirical evidence, Journal of the Academy [272] S. Chandra, S. Verma, W. M. Lim, S. Kumar, N. Donthu,
of Marketing Science, 2001, 29, 16-35, doi: Personalization in personalized marketing: Trends and ways
10.1177/0092070301291002. forward, Psychology & Marketing, 2022, 39, 1529-1562, doi:
[261] P. Lalwani, M. K. Mishra, J. S. Chadha, P. Sethi, Customer 10.1002/mar.21670.
churn prediction system: a machine learning approach, [273] M. Hasal, J. Nowaková, K. Ahmed Saghair, H. Abdulla, V.
Computing, 2022, 104, 271-294, doi: 10.1007/s00607-021- Snášel, L. Ogiela, Chatbots: Security, privacy, data protection,
00908-y. and social aspects, Concurrency and Computation: Practice and
[262] I. A. Moosa, Operational Risk Management, Palgrave Experience, 2021, 33, e6426, doi: 10.1002/cpe.6426.
Macmillan, Hampshire, 2007, 1–255, ISBN - 978-0-230-50644- [274] Z. I. Batouta, R. Dehbi, M. Talea, O. Hajoui, Automation
2. in code generation: Tertiary and systematic mapping review, 4th
[263] A. S. Almheiri, Automated loan Approval System for Institute of Electrical and Electronics Engineers International
banks, Rochester Institute of Technology, Master's Thesis, 2023, Colloquium on Information Science and Technology, Tangier,
https://repository.rit.edu/theses/11401. Morocco, October 24-26, 2016, 200-205, doi:
[264] S. Basu, Personalized product recommendations and firm 10.1109/cist.2016.7805042.
performance, Electronic Commerce Research and Applications, [275] N. Dongare, A. Bhirange, S. Kharche, A. Buchade, P.
2021, 48, 101074, doi: 10.1016/j.elerap.2021.101074. Mahalle, Equity research chatbot using LLM: a responsive agent
[265] E. Biermann, E. Cloete, L. M. Venter, A comparison of for investment research, Institute of Electrical and Electronics
intrusion detection systems, Computers & Security, 2001, 20, Engineers Pune Section International Conference, Pune, India,
676-683, doi: 10.1016/s0167-4048(01)00806-9. December 13-15, 2024, 1-5, doi:
[266] S. Salloum, T. Gaber, S. Vadera, K. Shaalan, A systematic 10.1109/punecon63413.2024.10895230.
literature review on phishing email detection using natural [276] AI agents in finance: the new era of banking services,
language processing techniques, Institute of Electrical and https://www.digitalsense.ai/blog/ai-agents-in-finance.
Electronics Engineers Access, 2022, 10, 65703-65727, doi: [277] C. Fieberg, L. Hornuf, M. Meiler, D. Streich, Using large
10.1109/access.2022.3183083. Language models for financial advice, Social Science Research
[267] G. Pang, C. Shen, L. Cao, A. Van Den Hengel, Deep Network Electronic Journal Entry, 2025, doi:
learning for anomaly detection: a review, Association for 10.2139/ssrn.5133294.
Computing Machinery Computing Surveys, 2022, 54, 1-38, doi: [278] Y. Li, Y. Yu, H. Li, Z. Chen, K. Khashanah, TradingGPT:
10.1145/3439950. Multi-Agent System with Layered Memory and Distinct
[268] T.-H. Chen, H.-C. Hsiang, W.-K. Shih, Security Characters for Enhanced Financial Trading Performance, ArXiv,
enhancement on an improvement on two remote user 2023, doi: 10.48550/arXiv.2309.03736.
authentication schemes using smart cards, Future Generation [279] O. Jin, H. El-Saawy, Portfolio management using
Computer Systems, 2011, 27, 377-380, doi: reinforcement learning, Stanford University, 2016.
10.1016/j.future.2010.08.007. [280] A. De Ridder, SmythOS - Multi-agent Systems in Finance:
[269] M. J. Hossain Faruk, H. Shahriar, M. Valero, F. L. Barsha, Enhancing Decision-Making and Market Analysis, 2024,
S. Sobhan, M. A. Khan, M. Whitman, A. Cuzzocrea, D. Lo, A. https://smythos.com/developers/agent-development/multi-agent-
Rahman, F. Wu, Malware detection and prevention using systems-in-finance/.
artificial intelligence techniques, Institute of Electrical and [281] F. Grosu, How can Multi-Agents AI Systems help Reduce
Electronics Engineers International Conference on Big Data, Biases in Trading Algorithms, Review of International
Orlando, USA, December 15-18, 2021, 5369-5377, doi: Comparative Management, 2025, 26, 364-373, doi:
10.1109/bigdata52589.2021.9671434. 10.24818/RMCI.2025.2.364.
[270] Y. Xue, T. Xu, L. R. Long, Z. Xue, S. Antani, G. R. Thoma, [282] dwillis. How AI agents are transforming AML compliance
30 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
and reducing operational risks, FinTech Global, 2024, Springer International Publishing, Cham, 2022, 109-126, doi:
https://fintech.global/2024/12/17/how-ai-agents-are- 10.1007/978-3-031-07472-1_7.
transforming-aml-compliance-and-reducing-operational-risks/. [294] D. Singh, Foreign direct investment and local interpretable
[283] AI Agents in Finance: Use Cases, Benefits & Trends, model-agnostic explanations: a rational framework for FDI
https://www.knacklabs.ai/blogs/ai-agents-in-financial-services- decision making, Journal of Economics, Finance and
use-cases-benefits-and-future-trends. Administrative Science, 2024, 29, 98-120, doi: 10.1108/jefas-05-
[284] R. Singh, R. Bansal, M. Niranjanamurthy, Use and 2021-0069.
application of artificial intelligence in accounting and finance: [295] Tirumala, K., Markosyan, A., Zettlemoyer, L. &
Benefits and challenges. Data Wrangling: Concepts, Applications Aghajanyan, A. Memorization Without Overfitting: Analyzing
and Tools, 2023, 251–274, doi: 10.1002/9781119879862.ch12. the Training Dynamics of Large Language Models, Advances in
[285] M. Saleem, C. Chawla, A. K. Agarwal, D. Ather, Neural Information Processing Systems, New Orleans,
Responsible AI in fintech: addressing challenges and strategic Louisiana, USA, November 28 – December 9, 2022, 38274—
solutions, Generative Artificial Intelligence in FinTech: 38290, doi: 10.48550/arXiv.2205.10770.
Revolutionizing Finance Through Intelligent Algorithms, [296] Y.-L. Peng, W.-P. Lee, Data selection to avoid overfitting
Springer Nature, Switzerland, 2025, 61-72, doi: 10.1007/978-3- for foreign exchange intraday trading with machine learning,
031-76957-3_4. Applied Soft Computing, 2021, 108, 107461, doi:
[286] R. P. Buckley, D. A. Zetzsche, D. W. Arner, B. W. Tang, 10.1016/j.asoc.2021.107461.
Regulating artificial intelligence in finance: Putting the human in [297] C. F. G. Dos Santos, J. P. Papa, Avoiding overfitting: a
the loop, Sydney Law Review, 2021, 43, 43–81, survey on regularization methods for convolutional neural
https://ssrn.com/abstract=3831758. networks, Association for Computing Machinery Computing
[287] S. Juddoo, Overview of data quality challenges in the Surveys, 2022, 54, 1-25, doi: 10.1145/3510413.
context of Big Data, International Conference on Computing, [298] H. Kang, X. Y. Liu, Deficiency of large language models
Communication and Security, Pamplemousses, Mauritius, in finance: An empirical examination of hallucination, ArXiv,
December 4-5, 2015, 1–9, doi: 10.1109/cccs.2015.7374131. 2023, doi: 10.48550/arXiv.2311.15548.
[288] A. Y. Chen, J. McCoy, Missing values handling for [299] M. Barry, G. Caillaut, P. Halftermeyer, R. Qader, M.
machine learning portfolios, Journal of Financial Economics, Mouayad, F. L. Deit, D. Cariolaro, J. Gesnouin, Graphrag:
2024, 155, 103815, doi: 10.1016/j.jfineco.2024.103815. leveraging graph-based efficiency to minimize hallucinations in
[289] D. Kumar, P. K. Sarangi, R. Verma, A systematic review llm-driven rag for finance data, Proceedings of the Workshop on
of stock market prediction using machine learning and statistical Generative Artificial Intelligence and Knowledge Graphs, Abu
techniques, Materials Today: Proceedings, 2022, 49, 3187-3191, Dhabi, UAE, 19 January, 2025, 54 – 65,
doi: 10.1016/j.matpr.2020.11.399. https://aclanthology.org/2025.genaik-1.6/.
[290] K. Bonawitz, H. Eichner, W. Grieskamp, D. Huba, A. [300] H. Baniecki, P. Biecek, Adversarial attacks and defenses in
Ingerman, V. Ivanov, C. Kiddon, J.Konen, S. Mazzocchi, H. B. explainable artificial intelligence: a survey, Information Fusion,
Mcmahan, Towards federated learning at scale: System design, 2024, 107, 102303, doi: 10.1016/j.inffus.2024.102303.
Proceedings of Machine Learning and Systems, 2019, 1, 374–388, [301] P. Kumar, Adversarial attacks and defenses for large
doi: 10.48550/arXiv.1902.01046. language models (LLMs): methods, frameworks & challenges,
[291] C. V. Gonzalez Zelaya, Towards explaining the effects of International Journal of Multimedia Information Retrieval, 2024,
data preprocessing on machine learning, Institute of Electrical 13, 26, doi: 10.1007/s13735-024-00334-8.
and Electronics Engineers 35th International Conference on Data [302] Z. Lin, S. Guan, W. Zhang, H. Zhang, Y. Li, H. Zhang,
Engineering, Macao, China, April 8-11, 2019, 2086-2090, doi: Towards trustworthy LLMs: a review on debiasing and
10.1109/icde.2019.00245. dehallucinating in large language models, Artificial Intelligence
[292] A. Adadi, M. Berrada, Peeking inside the black-box: a Review, 2024, 57, 243, doi: 10.1007/s10462-024-10896-y.
survey on explainable artificial intelligence (XAI), Institute of [303] H. H. H. Aldboush, M. Ferdous, Building trust in fintech:
Electrical and Electronics Engineers Access, 2018, 6, 52138- an analysis of ethical and privacy considerations in the
52160, doi: 10.1109/access.2018.2870052. intersection of big data, AI, and customer trust, International
[293] P. Fukas, J. Rebstadt, L. Menzel, O. Thomas, Towards Journal of Financial Studies, 2023, 11, 90, doi:
explainable artificial intelligence in financial fraud detection: 10.3390/ijfs11030090.
using shapley additive explanations to explore feature [304] H. Guo, P. Polak, Artificial intelligence and financial
importance, Advanced Information Systems Engineering, technology FinTech: how AI is being used under the pandemic in
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 31

Review article Engineered Science
2020, The 4th Industrial Revolution: Implementation of Artificial 2017.7975207.
Intelligence for Growing Business Success, Springer [318] C. Caldeira, Y. Chen, L. Chan, V. Pham, Y. Chen, K. Zheng,
International Publishing, Cham, 2021, 169-186, ISBN - 978-3- Mobile apps for mood tracking: an analysis of features and user
030-62796-6. review, American Medical Informatics Association Annual
[305] T. Isobe, M. Morishima, F. Yoshitani, N. Koizumi, K. Symposium Proceedings, 2018, 2017, 495-504,
Murakami, Voice-activated home banking system and its field https://pmc.ncbi.nlm.nih.gov/articles/PMC5977660/?utm.
trial, 4th International Conference on Spoken Language [319] D. I. H. Farias, P. Rosso, Irony, sarcasm, and sentiment
Processing, Philadelphia, Pennsylvania, USA, 3–6 October, analysis, Sentiment Analysis in Social Networks, Elsevier,
1996, 1688-1691, doi: 10.21437/icslp.1996-429. Amsterdam, 2017, 113-128, doi: 10.1016/b978-0-12-804412-
[306] L. Doddipatla, Exploring the role of biometric 4.00007-3.
authentication in modern payment solutions, European Chemical [320] B. Stojanović, J. Božić, K. Hofer-Schmitz, K. Nahrgang,
Bulletin, 2022, 20, 220-229, doi: 10.53555/ecb.v10:i1.17783. A. Weber, A. Badii, M. Sundaram, E. Jordan, J. Runevic, Follow
[307] J. A. Markowitz, Voice biometrics, Communications of the the trail: machine learning for fraud detection in fintech
Association for Computing Machinery, 2000, 43, 66-73, doi: applications, Sensors, 2021, 21, 1594, doi: 10.3390/s21051594.
10.1145/348941.348995. [321] M. Abu Sufian Mozumder, T. N. Nguyen, S. Devi, M. Arif,
[308] A. Jain, P. Bhati, Comparative analysis and development of M. P. Ahmed, E. Ahmed, M. Bhuiyan, M. H. Rahman, A. Al
voice-based chatbot system for differently-abled, Institute of Mamun, A. Uddin, Enhancing customer satisfaction analysis
Physics Publishing, Journal of Physics: Conference Series, 2022, using advanced machine learning techniques in fintech industry,
2273, 012003, doi: 10.1088/1742-6596/2273/1/012003. Journal of Computer Science and Technology Studies, 2024, 6,
[309] Q. Zhao, K. Chen, T. Li, Y. Yang, X. Wang, Detecting 35-41, doi: 10.32996/jcsts.2024.6.3.4.
telecommunication fraud by understanding the contents of a call, [322] S. Khan, H. U. Khan, S. Nazir, B. Albahooth, M. Arif,
Cybersecurity, 2018, 1, 8, doi: 10.1186/s42400-018-0008-5. Users sentiment analysis using artificial intelligence-based
[310] S. V. Stevenage, G. Clarke, A. McNeill, The “other-accent” FinTech data fusion in financial organizations, Mobile Networks
effect in voice recognition, Journal of Cognitive Psychology, and Applications, 2024, 29, 477-488, doi: 10.1007/s11036-023-
2012, 24, 647-653, doi: 10.1080/20445911.2012.675321. 02246-z.
[311] J. Meyer, L. Dentel, F. Meunier, Speech recognition in [323] S. Saluja, Identity theft fraud- major loophole for FinTech
natural background noise, Public Library of Science One, 2013, industry in India, Journal of Financial Crime, 2024, 31, 146-157,
8, e79279, doi: 10.1371/journal.pone.0079279. doi: 10.1108/jfc-08-2022-0211.
[312] A. Easwara Moorthy, K. L. Vu, Privacy concerns for use of [324] S. Zeranski, I. E. Sancak, Prudential supervisory disclosure
voice activated personal assistant in the public space, (PSD) with supervisory technology (SupTech): lessons from a
International Journal of Human-Computer Interaction, 2015, 31, FinTech crisis, International Journal of Disclosure and
307-335, doi: 10.1080/10447318.2014.986642. Governance, 2021, 18, 315-335, doi: 10.1057/s41310-021-
[313] T. K. Perrachione, S. N. Del Tufo, J. D. E. Gabrieli, Human 00111-7.
voice recognition depends on language ability, Science, 2011, [325] M. Turki, A. Hamdan, J. Al Ajmi, A. Razzaque, Regulatory
333, 595, doi: 10.1126/science.1207327. technology (RegTech) and money laundering prevention:
[314] O. Tosi, H. Oyer, W. Lashbrook, C. Pedrey, J. Nicol, E. exploratory study from Bahrain, Advanced Machine Learning
Nash, Experiment on voice identification, The Journal of the Technologies and Applications, Springer, Singapore, 2020, 349-
Acoustical Society of America, 1972, 51, 2030-2043, doi: 359, ISBN - 978-981-15-3383-9.
10.1121/1.1913064. [326] A. K. Pakina, D. Kejriwal, A. Goel, T. D. Pujari, AI-
[315] Y. Sreedhar, Fintech risk management: Challenges for Generated Synthetic Identities in Fin Tech: Detecting Deep fakes
artificial intelligence in finance, International Journal of KYC Fraud Using Behavioral Biometrics, International
Advances Engineering and Civil Research, 2022, 24, 49-67. Organization of Scientific Research Journal of Computer
[316] S. Feuerriegel, H. Prendinger, News-based trading Engineering, 2023, 25, 26–37, doi: 10.9790/0661-2503032637.
strategies, Decision Support Systems, 2016, 90, 65-74, doi: [327] K. Gai, M. Qiu, X. Sun, H. Zhao, Security and privacy
10.1016/j.dss.2016.06.020. issues: a survey on FinTech, Smart Computing and
[317] T. K. Shivaprasad, J. Shetty, Sentiment analysis of product Communication, Springer International Publishing, Cham, 2017,
reviews: a review, International Conference on Inventive 236-247, doi: 10.1007/978-3-319-52015-5_24.
Communication and Computational Technologies, Coimbatore, [328] A. Ashta, G. Biot-Paquerot, FinTech evolution: Strategic
Tamil Nadu, India, March 10-11, 2017, 5-9, doi: 10.1109/icicct. value management issues in a fast changing industry, Strategic
32 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
Change, 2018, 27, 301-311, doi: 10.1002/jsc.2203. cognitive computing against fintech fraud, Big Data and
[329] G. Christopher, A.Syed, F. Attila, S. Ray, Managing Risks Cognitive Computing, 2023, 7, 76, doi: 10.3390/bdcc7020076.
In Fintech: Applications And Challenges Of Artificial [341] V. Chatzara, FinTech, InsurTech, and the regulators,
Intelligence-Based Risk Management, Economics and Business InsurTech: A Legal and Regulatory View, Springer International
Journal, 2024, 2, 249-268, doi:10.47353/ecbis.v2i3.127. Publishing, Cham, 2019, 3-25, ISBN- 978-3-030-27385-9.
[330] W. Magnuson, W. J. Magnuson, Regulating fintech, [342] J. Jain, Optimizing payment gateways in fintech using AI-
Vanderbilt Law Review, 2018, 71, 1167, augmented OCR and intelligent workflow, Journal of Electrical
https://scholarship.law.vanderbilt.edu/vlr/vol71/iss4/2. Systems, 2024, 17, 115-127, doi: 10.52783/jes.8179.
[331] A. Marchev, V. Marchev, Individualised fin-tech [343] H. P. Josyula, Fraud detection in fintech leveraging
investment services, Journal of Global Strategic Management, machine learning and behavioral analytics, Preprints, 2023, doi:
2023, 17, doi: 10.20460/jgsm.2024.330. 10.21203/rs.3.rs-3548343/v1.
[332] B. Cummings, D. Andrus, How Fintech is enabling more [344] X. Tian, J. S. He, M. Han, Data-driven approaches in
customized investing, Journal of Financial Planning, 2022, 35, FinTech: a survey, Information Discovery and Delivery, 2021,
40–45, 49, 123-135, doi: 10.1108/idd-06-2020-0062.
https://www.financialplanningassociation.org/learning/publicati [345] Zhu, J., Xu, T., Zhang, Y. & Fan, Z. Scalable edge
ons/journal/MAR22-how-fintech-enabling-more-customized- computing framework for real-time data processing in fintech
investing-OPEN. applications, International Journal of Advance in Applied
[333] T. Moenjak, A. Kongprajya, C. Monchaitrakul, Fintech, Science Research, 2024, 3, 85–92, doi:
Financial Literacy, and Consumer Saving and Borrowing: The 10.56726/IRJMETS74368.
Case of Thailand, Asian Development Bank Institute Working [346] S.-C. Huang, C.-F. Wu, C.-C. Chiou, M.-C. Lin, Intelligent
Paper Series, 2020, https://www.adb.org/publications/fintech- FinTech data mining by advanced deep learning approaches,
financial-literacy-consumer-saving-borrowing-thailand. Computational Economics, 2022, 59, 1407-1422, doi:
[334] M. Siek, A. Sutanto, Impact analysis of fintech on banking 10.1007/s10614-021-10118-5.
industry, International Conference on Information Management [347] S. Agarwal, S. Alok, P. Ghosh, S. Gupta, Financial
and Technology, 2019, 1, 356-361, doi: inclusion and alternate credit scoring for the millennials: role of
10.1109/icimtech.2019.8843778. big data and machine learning in fintech, Business School,
[335] S. M. Chaudhry, R. Ahmed, T. L. D. Huynh, C. Benjasak, National University of Singapore, 2020, doi:
Tail risk and systemic risk of finance and technology (FinTech) 10.2139/ssrn.3507827.
firms, Technological Forecasting and Social Change, 2022, 174, [348] M. Bazarbash, FinTech in financial inclusion: machine
121191, doi: 10.1016/j.techfore.2021.121191. learning applications in assessing credit risk, International
[336] T.-Y. Hung, S.-H. Huang, Addressing the cold-start Monetary Fund Working Papers, 2019, 2019, 34, doi:
problem of recommendation systems for financial products by 10.5089/9781498314428.001.
using few-shot deep learning, Applied Intelligence, 2022, 52, [349] T. Balyuk, FinTech lending and bank credit access for
15529-15546, doi: 10.1007/s10489-022-03374-x. consumers, Management Science, 2023, 69, 555-575, doi:
[337] L. Hamzat, D. Abiodun, A. Joseph, Empowering 10.1287/mnsc.2022.4319.
entrepreneurial growth through data-driven financial literacy, [350] S. J. Chaplinsky, StreetShares, inc.: fintech platform
market research, and personalized education tool, World Journal lending business, Social Science Research Network Electronic
of Advanced Research and Reviews, 2023, 19, 1692-1711, doi: Journal, 2020, doi: 10.2139/ssrn.3682585.
10.30574/wjarr.2023.19.2.1568. [351] H. S. Disemadi, M. A. Yusro, W. G. Balqis, The problems
[338] A. M. Adebowale, O. B. Akinnagbe, Cross-platform of consumer protection in fintech peer to peer lending business
financial data unification to strengthen compliance, fraud activities in Indonesia, Sociological Jurisprudence Journal,
detection and risk controls, World Journal of Advanced Research 2020, 3, 91-97, doi: 10.22225/scj.3.2.1798.91-97.
and Reviews, 2023, 20, 2326-2343, doi: [352] M. Rizinski, H. Peshov, K. Mishev, L. T. Chitkushev, I.
10.30574/wjarr.2023.20.3.2459. Vodenska, D. Trajanov, Ethically responsible machine learning
[339] N. Kandregula, Leveraging artificial intelligence for real- in fintech, Institute of Electrical and Electronics Engineers
time fraud detection in financial transactions: a fintech Access, 2022, 10, 97531-97554, doi:
perspective, World Journal of Advanced Research and Reviews, 10.1109/access.2022.3202889.
2019, 3, 115-127, doi: 10.30574/wjarr.2019.3.3.0129. [353] P. Treleaven, Financial regulation of FinTech,
[340] A. Faccia, National payment switches and the power of Journal of Financial Perspectives, 2015, 3, 114-121,
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 33

Review article Engineered Science
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3084015. 75-124, doi: 10.1093/jfr/fjaa004.
[354] S. E. Chang, M.-H. Wang, Blockchain-enabled fintech [368] H. Stewart, J. Jürjens, Data security and consumer trust in
innovation: a case of reengineering stock trading services, FinTech innovation in Germany, Information & Computer
Institute of Electrical and Electronics Engineers Access, 2023, Security, 2018, 26, 109-128, doi: 10.1108/ics-06-2017-0039.
11, 137125-137137, doi: 10.1109/access.2023.3339570. [369] J. O. Oladipo, C. C. Okoye, O. A. Elufioye, T. Falaiye, E.
[355] E. Ng, B. Tan, Y. Sun, T. Meng, The strategic options of E. Nwankwo, Human factors in cybersecurity: Navigating the
fintech platforms: an overview and research agenda, Information fintech landscape, International Journal of Science and Research
Systems Journal, 2023, 33, 192-231, doi: 10.1111/isj.12388. Archive, 2024, 11, 1959-1967, doi:
[356] M. Yu, The impact of financial technology on traditional 10.30574/ijsra.2024.11.1.0258.
financial systems and future trends, Journal of Modern Business [370] P. Giudici, Fintech risk management: a research challenge
and Economics, 2024, 1, doi: 10.70767/jmbe.v1i1.134. for artificial intelligence in finance, Frontiers in Artificial
[357] I. Aldridge, S. Krawciw, Real-Time Risk: What Investors Intelligence, 2018, 1, 1, doi: 10.3389/frai.2018.00001.
Should Know About FinTech, High-Frequency Trading, and [371] L. Nguyen, S. Tran, T. Ho, Fintech credit, bank regulations
Flash Crashes, John Wiley & Sons, 2017, 83-102, ISBN - 978- and bank performance: a cross-country analysis, Asia-Pacific
1-119-31904-7. Journal of Business Administration, 2022, 14, 445-466, doi:
[358] I. Henriques, P. Sadorsky, Do clean energy stocks diversify 10.1108/apjba-05-2021-0196.
the risk of FinTech stocks? Connectedness and portfolio [372] M. Kolev, 12 reverse stress testing with strategic
implications, Global Finance Journal, 2024, 62, 101019, doi: management tools, Reverse Stress Testing in Banking, De
10.1016/j.gfj.2024.101019. Gruyter, 2021, 269-290, ISBN - 13: 978-3-11-064482-1.
[359] S. Agarwal, W. Qian, Y. Ren, H.-T. Tsai, B. Y. Yeung, The [373] R. Yudaruddin, B. A. Nugroho, Mardiany, Z. Fitrian, P.
real impact of FinTech: evidence from mobile payment Hapsari, Y. Fitrianto, E. N. Santi, Liquidity and credit risk in
technology, Social Science Research Network Electronic Indonesia: the role of FinTech development, Sage Open, 2024,
Journal, 2020, 72, doi: 10.2139/ssrn.3556340. 14, 21582440241245248, doi: 10.1177/21582440241245248.
[360] D. W. Arner, J. N. Barberis, R. P. Buckley, The evolution [374] P. Girling, Operational Risk Management: A Complete
of fintech: a new post-crisis paradigm, Social Science Research Guide to a Successful Operational Risk Framework, John Wiley
Network Electronic Journal, 2015, 45, doi: & Sons, 2013, ISBN - 9781118532454.
10.2139/ssrn.2676553. [375] S. Belozyorov, O. Sokolovska, Y. S. Kim, Fintech as a
[361] C. Nielsen, Unlocking the Power of Digital Tools: precondition of transformations in global financial markets,
Designing an Efficient IT Contract Portfolio Management Foresight and Science, Technology, and Innovation Governance,
System for Fintech Success, Master’s Thesis, 2023, 79-89. 2020, 14, 23-35, doi: 10.17323/2500-2597.2020.2.23.35.
[362] A. Tyagi, Risk Management in Fintech, The Emerald [376] L. Allen, Y. Shan, Y. Shen, Do FinTech mortgage lenders
Handbook of Fintech: Reshaping Finance, Emerald Publishing fill the credit gap? evidence from natural disasters, Journal of
Limited, 2024, 157–175, ISBN - 978-1-83753-609-2. Financial and Quantitative Analysis, 2023, 58, 3342-3383, doi:
[363] O. F. Dudu, O. B. Alao, E. O. Alonge, Conceptual 10.1017/s002210902200120x.
framework for AI-driven tax compliance in fintech ecosystems, [377] D. Ahern, Regulatory lag, regulatory friction and regulatory
International Journal of Frontiers in Engineering and transition as FinTech disenablers: calibrating an EU response to
Technology Research, 2024, 7, 1-10, doi: the regulatory sandbox phenomenon, European Business
10.53294/ijfetr.2024.7.2.0045. Organization Law Review, 2021, 22, 395-432, doi:
[364] P. Sironi, FinTech Innovation: From Robo-Advisors to 10.1007/s40804-021-00217-z.
Goal Based Investing and Gamification, John Wiley & Sons, [378] A. Mehrotra, Artificial intelligence in financial services–
2016, doi: 10.1002/9781119227205. need to blend automation with human touch, International
[365] J. Agnew, O. S. Mitchell, The Disruptive Impact of FinTech Conference on Automation, Computational and Technology
on Retirement Systems, Oxford University Press, 2019, ISBN – Management, London, United Kingdom, April 24-26, 2019, 342-
9780191880728. 347, doi: 10.1109/icactm.2019.8776741.
[366] Y. Lin, Q. Ye, H. Xia, Optimal interest rates personalization [379] D. El-Shihy, M. Abdelraouf, M. Hegazy, N. Hassan, The
in FinTech lending, Information Technology and Management, influence of AI chatbots in fintech services on customer loyalty
2025, 26, 117-137, doi: 10.1007/s10799-023-00406-x. within the banking industry, Future of Business Administration,
[367] S. T. Omarova, Technology v technocracy: fintech as a 2024, 3, 16-28, doi: 10.33422/fba.v3i1.644.
regulatory challenge, Journal of Financial Regulation, 2020, 6, [380] S. di Castri, M. Grasser, A. Kulenkampff, A chatbot
34 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher

Engineered Science Review article
application and complaints management system for the bangko [392] P. Mingsakul, Hyper-personalization: Giving banks AI-
sentral ng Pilipinas (BSP). R2A project retrospective and lessons powered insight into their customers, Krungsri Research, 2024,
learned, Social Science Research Network Electronic Journal, https://www.krungsri.com/en/research/research-intelligence/ai-
2020, 18, doi: 10.2139/ssrn.3596268. hyper-personalization-2024.
[381] S. Lee, Evaluation of mobile application in user’s [393] T. Klein, T. Walther, Advances in explainable artificial
perspective: Case of P2P lending apps in FinTech industry, intelligence (xAI) in finance, Finance Research Letters, 2024, 70,
Korean Society for Internet Information Transactions on Internet 106358, doi: 10.1016/j.frl.2024.106358.
& Information Systems, 2017, 11, 1105-1115, doi: [394] C. Wilson, Explainable AI in Finance: Addressing the
10.3837/tiis.2017.02.027. Needs of Diverse Stakeholders, CFA Institute Research and
[382] J. Kang, Mobile payment in Fintech environment: trends, Policy Center, 2025, doi: 10.56227/25.1.25.
security challenges, and services, Human-Centric Computing and [395] O. Fadi, Z. Karim, E. G. Abdellatif, B. Mohammed, A
Information Sciences, 2018, 8, 32, doi: 10.1186/s13673-018- survey on blockchain and artificial intelligence technologies for
0155-4. enhancing security and privacy in smart environments, Institute
[383] C. Edwin, S. Seery, H. C. Webb, Innovative pathways: of Electrical and Electronics Engineers Access, 2022, 10, 93168-
mentoring fintech start-ups through design thinking 93186, doi: 10.1109/access.2022.3203568.
methodology, The Palgrave Handbook of FinTech in Africa and [396] R. K. Dhanaraj, S. Suganyadevi, V. Seethalakshmi, M.
Middle East, Springer Nature, Singapore, 2024, 1-30, ISBN - Ouaissa, Introduction to homomorphic encryption for financial
978-981-96-6143-5. cryptography, Homomorphic Encryption for Financial
[384] M. Tariq, S. Z. Maryam, W. A. Shaheen, Cognitive factors Cryptography, Springer International Publishing, Cham, 2023, 1-
and actual usage of Fintech innovation: Exploring the UTAUT 12, doi: 10.1007/978-3-031-35535-6_1.
framework for digital banking, Heliyon, 2024, 10, e35582, doi: [397] G. Long, Y. Tan, J. Jiang, C. Zhang, Federated learning for
10.1016/j.heliyon.2024.e35582. open banking, Federated Learning, Springer International
[385] G. Bhardwaj, G. Sinha, A. Gupta, Language in fintech: a Publishing, Cham, 2020, 240-254, ISBN - 13: 978-3-030-63075-
synergist to growth, Manthan: Journal of Commerce and 1.
Management, 2019, 6, 38, doi: 10.17492/manthan.v6i1.182682. [398] N. K. Bhasin, S. Kadyan, K. Santosh, R. Hp, R. Changala,
[386] U. Rahardja, M. Miftah, M. Rakhmansyah, J. Zanubiya, B. K. Bala, Enhancing quantum machine learning algorithms for
Revolutionizing financial services with big data and fintech: a optimized financial portfolio management, Third International
scalable approach to innovation, Lecturer Association Indonesia Conference on Intelligent Techniques in Control, Optimization
Journal on Recent Innovation, 2024, 6, 118-129, doi: and Signal Processing, Virudhunagar, Tamil Nadu, India, March
10.34306/ajri.v6i2.1180. 14-16, 2024, 1-7, doi: 10.1109/incos59338.2024.10527612.
[387] AI Agents and the Transformation of the Financial [399] B. Chen, Z. Wu, R. Zhao, From fiction to fact: the growing
Industry, https://global.fujitsu/en-global/insight/tl-aiagents- role of generative AI in business and finance, Journal of Chinese
financial-industry-20250418. Economic and Business Studies, 2023, 21, 471-496, doi:
[388] D. Cooper, Autonomous AI Agents in Finance: Portfolio 10.1080/14765284.2023.2245279.
Management to Fraud Detection, Heliosz.ai Blog, 2025, [400] AI governance in finance: balancing ethics and practice,
https://www.heliosz.ai/blog/ai-agents-in-finance/. CGI US, https://www.cgi.com/us/en-us/article/artificial-
[389] G. Aston, Hyper-personalization in banking: The new intelligence/ai-governance-finance.
imperative, DXC Technology, 2024, [401] P. F. Azuikpe, J. A. Fabuyi, A. Y. Balogun, P. A. Adetunji,
https://dxc.com/insights/knowledge-base/blogs/hyper- K. N. Peprah, E. Mmaduekwe, M. C. Ejidare, The necessity of
personalization-future-of-banking. artificial intelligence in fintech for SupTech and RegTech
[390] Kyanon Digital Blog, Hyper Personalization in Banking: supervisory in banks and financial organizations, International
Transforming Customer Experience With AI, Medium, 2024, Journal of Science and Research Archive, 2024, 12, 2853-2860,
https://medium.com/@kyanon.digital/hyper-personalization-in- doi: 10.30574/ijsra.2024.12.2.1614.
banking-transforming-customer-experience-with-ai- [402] AI Applications in Web3 SupTech and RegTech: A
49d924e97cb4. Regulatory Perspective, 2024,
[391] J. Moss, How AI-Powered Hyper-Personalisation Is https://www.adgmacademy.com/publications/AI-Applications-
Driving the Customer Experience, International Banker, 2025, in-Web3-SupTech-and-RegTech-A-Regulatory-Perspective.
https://internationalbanker.com/technology/how-ai-powered-
hyper-personalisation-is-driving-the-customer-experience/. Publisher’s Note: Engineered Science Publisher remains
Engineered Science Publisher Eng. Sci., 2026, 41, 2245| 35

Review article Engineered Science
neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
Open Access
This article is licensed under a Creative Commons Attribution
4.0 International License, which permits the use, sharing,
adaptation, distribution and reproduction in any medium or
format, as long as appropriate credit to the original author(s)
and the source is given by providing a link to the Creative
Commons license and changes need to be indicated if there are
any. The images or other third-party material in this article are
included in the article's Creative Commons license, unless
indicated otherwise in a credit line to the material. If material
is not included in the article's Creative Commons license and
your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this
license, visit http://creativecommons.org/ licenses/by/4.0/.
©The Author(s) 2026.
36 | Eng. Sci., 2026, 41, 2245 Engineered Science Publisher