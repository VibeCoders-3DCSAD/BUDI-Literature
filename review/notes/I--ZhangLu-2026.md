---
paper_id: I--ZhangLu-2026
first_author: Zhang
year: 2026
title: "Artificial Intelligence-Driven Transformation in Financial Technology: Applications, Agents and Challenges"
venue: "Engineered Science"
doi: 10.30919/es2245

designation: international
status: extracted
modules: [model_algorithm_integration, data_collection, model_development, software_quality_evaluation, model_performance_evaluation, system_performance_evaluation, pfm_apps_overview, pfm_apps_problems]
module_rationale:
  model_algorithm_integration: "Section 2.3 and Table 2 classify and compare AI models (LLMs, neural networks, LSTM, CNN, random forest, decision tree, XAI, fusion models, generative AI, RL) and their integration into fintech applications."
  data_collection: "Section 2.2 and Table 1 catalogue open-source datasets and resources (FinQA, FinNLI, FinBen, FRED, SEC, Zenodo, etc.) used in fintech AI research."
  model_development: "Section 2.3 describes model training, features, and development practices for credit scoring, fraud detection, trading, and insurance models."
  software_quality_evaluation: "Section 4 and Section 5 discuss XAI, fairness, transparency, auditability, and regulatory compliance as quality requirements for AI systems in fintech."
  model_performance_evaluation: "Section 2.3 reports that gradient boosted trees, support vector machines, and deep nets routinely outperform traditional scorecards and that benchmarking studies show robust gains from modern classifiers."
  system_performance_evaluation: "Section 4 examines deployment challenges including data quality, model drift, adversarial attacks, hallucination, and regulatory compliance at the system level."
  pfm_apps_overview: "Section 2.4 and Table 3 provide an overview of AI applications in fintech services including personalized recommendations, financial planning tools, robo-advisors, and customer service automation."
  pfm_apps_problems: "Section 4 and Table 4 catalogue problems in AI fintech applications including limited personalization, data dependency, model drift, explainability issues, and high false positives."
---

## Summary

A review article synthesizing the current landscape of artificial intelligence in financial technology, introducing a structured taxonomy that spans foundational machine learning for credit scoring and fraud detection through to autonomous and multi-agent systems capable of dynamic decision making. The review examines emerging agent architectures, open-source resources, algorithmic choices, and the persistent technical and ethical challenges—data privacy, model interpretability, algorithmic bias, security vulnerabilities, hallucination, and regulatory compliance—that constrain responsible deployment. It argues that model selection in fintech is task-dependent rather than universal, that AI is shifting from isolated predictive tools toward integrated decision infrastructures, and that long-term value depends less on predictive accuracy alone than on robustness, interpretability, fairness, security, and governability in high-stakes financial environments. The paper reports no primary data, no experiments, and no model performance evaluation of its own; its quantitative content is limited to market projections and dataset descriptions.

## Problem and Motivation

Artificial intelligence has become a pivotal force in financial technology, reshaping services through enhanced automation, improved efficiency, and personalization, but the integration of sophisticated AI models introduces significant challenges concerning data privacy, algorithmic bias, and a lack of transparency. Financial systems generate large-scale, high-frequency, and highly heterogeneous data that exceed the analytical capacity of conventional decision frameworks, and the digitalization of payments, lending, investment, insurance, and platform-based services has accelerated the need for methods that can process transactional records, behavioural signals, text, and alternative data in near real time (Sec. 1, p. 1). Prior work showed that the state of the art first developed around prediction-intensive tasks—credit assessment, lending analytics, and fraud detection—where machine learning methods increasingly outperformed conventional statistical and rule-based approaches under complex data conditions (Sec. 1, p. 3). More recently, the field has expanded beyond predictive analytics toward market intelligence, financial decision support, customer-facing service systems, and AI agents capable of interacting with data, tools, and decision environments in more adaptive and semi-autonomous ways (Sec. 1, pp. 1–3). Despite this rapid diffusion, practical deployment remains constrained by severe data-related limitations: financial datasets are often fragmented across institutions, restricted by privacy regulation, and affected by noise, missing values, reporting inconsistency, and regime shifts, all of which reduce model portability and weaken out-of-sample reliability (Sec. 1, p. 3). A second major gap concerns transparency and fairness in high-stakes financial decisions, where many high-performing models still operate as black boxes and fairness remains difficult to define and operationalize in credit contexts because different fairness criteria can conflict with each other and with profitability objectives (Sec. 1, p. 4). A third emerging gap concerns the use of large language models and generative systems in finance, where hallucination remains a central weakness and retrieval-augmented generation does not eliminate harmful or unreliable outputs (Sec. 1, p. 4). The review argues that most prior reviews treated machine learning applications, explainable AI, and regulatory governance as separate lines of inquiry, and that a comprehensive synthesis bringing together conventional predictive models, generative systems, and emerging agent-based architectures within a unified fintech framework—while simultaneously addressing governance, security, fairness, and financial stability—had remained relatively limited (Sec. 1, p. 4).

## Method

**Design.** Review article (stated in the header as "Article type: Review article"); no formal design label beyond that, and no systematic review protocol, search strategy, or inclusion criteria are reported.
**Sample.** Not reported (no count of reviewed works is stated); the review draws on 402 numbered references and covers AI applications across lending, payments, trading, insurance, compliance, and customer service, with four review tables synthesizing open-source resources, AI models, applications, and challenges.
**Context.** geography: Not reported (global scope, with no country-specific focus; examples span the US, Europe, the Philippines, and international markets); population: Not applicable (review of literature and industry developments, not human participants); setting: Not applicable (desk-based literature review; no experimental setting, no deployment, no participants).

- Synthesize the current landscape of AI in fintech through a structured taxonomy ranging from foundational machine learning to autonomous agents (Abstract, p. 1).
- Review open-source resources, datasets, and machine learning packages applied in finance and economics (Sec. 2.2, Table 1, pp. 5–7).
- Compare principal AI algorithms—LLMs, neural networks, LSTM, CNN, random forest, decision tree, XAI, fusion models, generative AI, and reinforcement learning—and their core advantages for fintech applications (Sec. 2.3, Table 2, pp. 7–9).
- Catalogue AI applications and benefits across voice recognition, sentiment analysis, fraud detection, customized recommendation, financial information processing, image identification, customer service, predictive modelling, information security, and generative AI agents (Sec. 2.4, Table 3, pp. 10–11).
- Examine the transition from task-specific models to autonomous AI agents and multi-agent systems, including agent architecture and multi-step workflow execution (Sec. 3, pp. 12–13).
- Analyse critical technical and ethical challenges: data quality and privacy, model interpretability, overfitting, hallucination, security vulnerabilities, algorithmic fairness, and regulatory compliance (Sec. 4, pp. 12–17).
- Summarize domain-specific challenges and limitations across applied fields in Table 4 (Sec. 4, Table 4, p. 15).
- Present a conceptual roadmap from 2026–2036 of AI in fintech across applications, technologies, system architecture, and governance constraints (Sec. 5, Fig. 6, p. 16).

## Software

- Scikit-learn (version not reported) — machine learning library for classification, regression, clustering, data preprocessing, model evaluation, and feature selection [Table 1, p. 7]
- TensorFlow (version not reported) — deep learning framework for building and deploying large neural networks [Table 1, p. 7]
- PyTorch (version not reported) — deep learning library with dynamic computation graph for research prototyping, computer vision, NLP, and reinforcement learning experiments [Table 1, p. 7]
- Keras (version not reported) — high-level neural networks API running on TensorFlow, for rapid prototyping of neural networks, image classification, text and sentiment analysis, sequence modelling (RNN, LSTM), and transfer learning [Table 1, p. 7]
- SHAP (Shapley Additive Explanations) — cited as a technique for rendering model decisions interpretable in complex financial scenarios [Sec. 4, p. 14]
- LIME (Local Interpretable Model-agnostic Explanations) — cited alongside SHAP as gaining traction for interpretability [Sec. 4, p. 14]
- Federated learning techniques — cited as privacy-preserving architectures for training on decentralized data [Sec. 4, p. 14]
- Retrieval-augmented generation (RAG) — cited as a mitigation technique for hallucination in generative models [Sec. 4, p. 15]

## Key Findings

- num: The global generative AI market is projected to expand from USD 13.5 billion in 2023 to approximately USD 255.8 billion by 2033, representing a CAGR of 34.2% over the forecast period [Sec. 1, p. 2].
- num: In 2023, North America established market primacy in generative AI, accounting for over 42.1% of global revenue, valued at USD 5.6 billion [Sec. 1, p. 2].
- num: FinQA is described as a large-scale dataset of 8,281 question–answer pairs over 2,800 financial reports, with numerical reasoning combining structured and unstructured data [Table 1, p. 6].
- num: SEC reports contain US public firms' annual reports (10-K) from approximately 1993–2020 [Table 1, p. 6].
- The review argues that AI models in fintech are not interchangeable; model suitability depends mainly on the form of the input data, the degree of temporal dependence, the required balance between predictive accuracy and interpretability, and the practical objective of the institution [Sec. 2.3, p. 8].
- The review classifies ten principal AI algorithm families and their fintech applications: LLM, neural networks, LSTM, CNN, random forest, decision tree, XAI, fusion models, generative AI, and reinforcement learning [Table 2, pp. 8–9].
- The review identifies a progression from task-specific automation toward holistic and intelligent financial ecosystems, with AI agents connecting data interpretation, reasoning, tool use, and sequential decision-making [Sec. 3, p. 12; Sec. 5, p. 17].
- The review states that fairness was not defined by a single criterion; demographic parity and equalized odds often created trade-offs because a model satisfying one fairness objective did not necessarily satisfy another, particularly when default risk distributions differed across groups [Sec. 4, p. 16].
- The review reports that empirical studies in credit scoring and credit ratings showed fairness interventions could reduce disparate impact but could also affect predictive accuracy, profitability, and approval policies [Sec. 4, p. 16].
- The review argues that the long-term value of AI in fintech will depend less on technical performance alone than on whether systems can be made robust, interpretable, fair, secure, and governable in high-stakes financial environments [Sec. 5, p. 17].
- The review identifies a significant shift from general-purpose AI models to highly specialized financial foundation models and autonomous agents capable of complex reasoning and decision-making [Sec. 5, p. 17].
- The review anticipates a staged transition from predictive and task-specific machine learning toward generative AI and, subsequently, agentic and multi-agent financial systems with increasing levels of autonomy, while recognizing that these trajectories remain constrained by technical, regulatory, and systemic considerations [Sec. 5, p. 17–18].

## Key Figures and Tables

- Fig. 1 (p. 2): Market map of key AI application areas in the fintech industry — intelligent payments, credit scoring, anti-fraud technology, algorithmic trading, and representative companies in each area.
- Fig. 2 (p. 10): AI applications in the fintech industry — visual overview of how AI models are deployed across client interaction, security, data analysis, and decision-making processes.
- Fig. 3 (p. 13): Core architecture and functional components of AI agents in fintech — an AI agent's architecture typically uses a large language model as a reasoning engine, augmented with specialized tools, memory, and planning capabilities.
- Fig. 4 (p. 13): Multi-agent workflow for credit assessment and fraud detection — a multi-agent classifies a user query and routes it to a credit agent or a fraud agent, which call scoring and anomaly models with transaction and profile data to return an approval or fraud suspicion.
- Fig. 5 (p. 14): Technical, regulatory and system challenges of AI deployment in fintech — visual overview of the primary obstacle categories.
- Fig. 6 (p. 16): Conceptual roadmap from 2026–2036 of AI in fintech across applications, technologies, system architecture, and governance constraints — solid elements represent developments supported by current empirical or industry evidence, while dashed elements indicate forward-looking or more speculative trajectories.
- Table 1 (pp. 6–7): Open-source packages, machine learning models, datasets, and applications for fintech — lists FinQA, FinNLI, FinBen, SEC, FRED, Google Dataset Search, NIST, Zenodo, AmeriGEOSS, StockEmotions, Headline, FiNER-139, FNXL, FinTabNet, Scikit-learn, TensorFlow, PyTorch, and Keras with descriptions and applications.
- Table 2 (pp. 8–9): Artificial intelligence models and core advantages for fintech applications — lists ten algorithm families with key strengths and fintech applications.
- Table 3 (p. 11): Applications and benefits of artificial intelligence in fintech service — lists ten applied fields (voice recognition, sentiment analysis, cheating/criminal detection, customized recommendation, financial information process, image identification, customer service, predictive modelling, information security, generative AI agent) with applications and benefits.
- Table 4 (p. 15): Challenges and limitations of artificial intelligence applied in fintech — lists ten applied fields with challenges, applications, and limitations.

## Limitations and Gaps

- The review reports no primary data, no experiments, no model performance evaluation of its own, and no empirical results; it is a synthesis of published literature and industry developments (Abstract; Sec. 1; Data Availability statement, p. 18).
- The review does not report a systematic search strategy, inclusion criteria, screening process, or count of reviewed works, so its coverage cannot be assessed or reproduced [unacknowledged].
- The only quantitative market figures (USD 13.5 billion in 2023, USD 255.8 billion by 2033, 34.2% CAGR, 42.1% North America share, USD 5.6 billion North America revenue) are cited from a single market report [38] and are not independently verified, contextualized, or accompanied by confidence intervals [unacknowledged].
- The review acknowledges that financial datasets were often fragmented across institutions, restricted by privacy regulation, and affected by noise, missing values, reporting inconsistency, and regime shifts, all of which reduced model portability and weakened out-of-sample reliability (Sec. 1, p. 3).
- The review acknowledges that privacy-preserving collaboration approaches, including decentralized and federated learning, introduce additional communication cost, computational burden, and security exposure, and do not fully resolve the tension between privacy protection and predictive utility (Sec. 1, p. 3).
- The review acknowledges that explainability methods had not yet been consistently validated for domain-specific decision support, regulatory audit, or stable local interpretation across settings (Sec. 1, p. 4).
- The review acknowledges that fairness remained difficult to define and operationalize in credit contexts because different fairness criteria could conflict with each other and with profitability objectives (Sec. 1, p. 4).
- The review acknowledges that hallucination remained a central weakness of large language models, particularly in specialized domains requiring factual precision and verifiable reasoning, and that retrieval-augmented generation did not eliminate harmful or unreliable outputs (Sec. 1, p. 4).
- The review acknowledges that AI models in finance and other domains faced adversarial attacks, data poisoning, model inversion, and evasion tactics that reduced reliability and exposed sensitive information (Sec. 4, p. 15–16).
- The review acknowledges that the dynamic and stringent regulatory landscape presents an ongoing technical challenge and that translating legal and ethical principles into concrete technical specifications for AI systems is not straightforward (Sec. 4, p. 16).
- The review states that adversarial manipulation had become a realistic concern while defensive practice remained uneven and often immature at the deployment stage (Sec. 1, p. 4).
- [unacknowledged] The review contains no discussion of the Philippine context, Philippine financial data, or Philippine regulatory frameworks, despite citing a chatbot application for the Bangko Sentral ng Pilipinas [380].
- [unacknowledged] The review does not include any cost analysis, scalability analysis, or deployment timeline for the AI systems it discusses.
- [unacknowledged] The review's four tables (Tables 1–4) are qualitative and contain no performance metrics, effect sizes, or statistical comparisons; the review reports no meta-analytic synthesis of the literature it surveys.
- [unacknowledged] The review's forward-looking roadmap (Fig. 6, 2026–2036) is described as including "forward looking or more speculative trajectories" but the review provides no method for distinguishing speculative from evidence-supported elements beyond visual dashed lines.

## Definitions

- **Fintech** — Financial technology; the sector in which AI is reshaping services through enhanced automation, improved efficiency, and personalization (Abstract, p. 1).
- **AI agent** — An autonomous system capable of sensing its environment, making independent decisions, executing actions to achieve predefined goals with minimal human intervention, and learning from feedback; typically uses a large language model as a reasoning engine augmented with specialized tools, memory, and planning capabilities (Sec. 3, p. 12).
- **Multi-agent system** — A system in which multiple specialized agents collaborate to solve complex financial problems, simulating real-world market dynamics by assigning different roles to various agents such as fundamental analysts, sentiment analysts, and risk managers (Sec. 3, p. 12).
- **XAI (Explainable AI)** — A field dedicated to developing techniques that can render model decisions interpretable, spurred by the need for transparency in high-stakes financial environments (Sec. 4, p. 14).
- **SHAP (Shapley Additive Explanations)** — A technique for explaining model predictions by attributing feature importance (Sec. 4, p. 14).
- **LIME (Local Interpretable Model-agnostic Explanations)** — A technique for local model-agnostic explanation (Sec. 4, p. 14).
- **Federated learning** — A technique proposed to train models on decentralized data without compromising user privacy, though it introduces complexities related to communication overhead and statistical heterogeneity (Sec. 4, p. 14).
- **Hallucination** — The tendency of large language models and other generative AI to generate outputs that are nonsensical, factually incorrect, or entirely fabricated, yet presented with a high degree of confidence (Sec. 4, p. 14).
- **Retrieval-augmented generation (RAG)** — A technique that enables a model to retrieve and incorporate information from a verified knowledge base before generating a response, proposed as a mitigation for hallucination (Sec. 4, p. 15).
- **Adversarial attack** — Making small, often imperceptible, perturbations to a model's input data with the goal of inducing an incorrect output (Sec. 4, p. 15).
- **Demographic parity** — A fairness criterion focused on whether positive outcomes are distributed at similar rates across groups (Sec. 4, p. 16).
- **Equalized odds** — A fairness criterion focused on whether error rates are balanced conditional on actual outcomes (Sec. 4, p. 16).
- **RegTech (Regulatory Technology)** — The use of AI as a tool for monitoring compliance and overseeing financial markets (Sec. 5, p. 18).
- **SupTech (Supervisory Technology)** — The use of AI in supervisory functions to analyze vast datasets in real time, identify systemic risks, and enforce regulations more effectively (Sec. 5, p. 18).
- **FinQA** — A large-scale dataset of 8,281 question–answer pairs over 2,800 financial reports, with numerical reasoning combining structured and unstructured data (Table 1, p. 6).
- **FinNLI** — A benchmark for natural language inference in financial text, using SEC filings and earnings call transcripts (Table 1, p. 6).
- **FinBen** — A holistic benchmark for financial LLMs, covering many datasets across financial tasks including information extraction, QA, forecasting, text generation, decision making, and risk management (Table 1, p. 6).

## Key Equations

Not applicable. The paper is a review article and reports no equations.

## Remember This

- The paper is a review article synthesizing AI in fintech, drawing on 402 references and presenting four review tables (open-source resources, AI models, applications, challenges).
- It proposes a structured taxonomy from foundational machine learning (credit scoring, fraud detection) to advanced autonomous agents and multi-agent systems.
- The only quantitative content is market projections (generative AI market from USD 13.5 billion in 2023 to approximately USD 255.8 billion by 2033, 34.2% CAGR, North America 42.1% share at USD 5.6 billion) and dataset descriptions (FinQA: 8,281 QA pairs over 2,800 reports; SEC: ~1993–2020).
- The review argues AI models in fintech are task-dependent rather than universal; model suitability depends on input data form, temporal dependence, accuracy–interpretability balance, and institutional objective.
- Persistent challenges identified: data quality and privacy, model opacity, algorithmic bias, adversarial vulnerability, hallucination in generative models, regulatory compliance, and human oversight.
- The review anticipates a staged transition toward agentic and multi-agent financial systems with increasing autonomy, constrained by technical, regulatory, and systemic considerations.
- The review reports no primary data, no experiments, and no model performance metrics of its own.

## Cited Works

- Cao, L.; Yang, Q.; Yu, P. S. (2021) (context) — Data science and AI in FinTech: an overview. [ref 1, p. 19]
- Doumpos, M.; Zopounidis, C.; Gounopoulos, D.; Platanakis, E.; Zhang, W. (2023) (context) — Operational research and artificial intelligence methods in banking. [ref 2, p. 19]
- Goodell, J. W.; Kumar, S.; Lim, W. M.; Pattnaik, D. (2021) (context) — AI and machine learning in finance: bibliometric analysis. [ref 3, p. 19]
- Vuković, D. B.; Dekpo-Adza, S.; Matović, S. (2025) (context) — AI integration in financial services: systematic review of trends and regulatory challenges. [ref 4, p. 19]
- Bahoo, S.; Cucculelli, M.; Goga, X.; Mondolo, J. (2024) (context) — AI in Finance: comprehensive review through bibliometric and content analysis. [ref 5, p. 19]
- Shavandi, A.; Khedmati, M. (2022) (methodology) — Multi-agent deep reinforcement learning framework for algorithmic trading. [ref 6, p. 19]
- Khan, A. T.; Li, S.; Cao, X. (2025) (context) — Bridging finance and AI: survey of large language models in financial system. [ref 7, p. 19]
- de-la-Rica-Escudero, A.; Garrido-Merchán, E. C.; Coronado-Vaca, M. (2025) (methodology) — Explainable post hoc portfolio management financial policy of a Deep Reinforcement Learning agent. [ref 8, p. 19]
- Crook, J. N.; Edelman, D. B.; Thomas, L. C. (2007) (context) — Recent developments in consumer credit risk assessment. [ref 10, p. 19]
- Lessmann, S.; Baesens, B.; Seow, H.-V.; Thomas, L. C. (2015) (methodology) — Benchmarking state-of-the-art classification algorithms for credit scoring. [ref 11, p. 19]
- Ryman-Tubb, N. F.; Krause, P.; Garn, W. (2018) (context) — How AI and machine learning research impacts payment card fraud detection. [ref 12, p. 19]
- Jagtiani, J.; Lemieux, C. (2019) (methodology) — Roles of alternative data and machine learning in fintech lending. [ref 13, p. 19]
- Khandani, A. E.; Kim, A. J.; Lo, A. W. (2010) (methodology) — Consumer credit-risk models via machine-learning algorithms. [ref 14, p. 19]
- Djeundje, V. B.; Crook, J.; Calabrese, R.; Hamid, M. (2021) (methodology) — Enhancing credit scoring with alternative data. [ref 15, p. 19]
- Kim, E.; Lee, J.; Shin, H.; Yang, H.; Cho, S.; Nam, S.-K.; Song, Y.; Yoon, J.-A.; Kim, J.-I. (2019) (methodology) — Champion-challenger analysis for credit card fraud detection. [ref 16, p. 19]
- Baesens, B.; Höppner, S.; Verdonck, T. (2021) (methodology) — Data engineering for fraud detection. [ref 17, p. 19]
- Théate, T.; Ernst, D. (2021) (methodology) — Application of deep reinforcement learning to algorithmic trading. [ref 18, p. 19]
- Lim, B.; Zohren, S. (2021) (methodology) — Time-series forecasting with deep learning: a survey. [ref 19, p. 19]
- Tetlock, P. C. (2007) (context) — Giving content to investor sentiment: role of media in the stock market. [ref 20, p. 19]
- Chen, Z.; Chen, W.; Smiley, C.; Shah, S.; Borova, I.; Langdon, D.; Moussa, R.; Beane, M.; Huang, T.-H.; Routledge, B.; Wang, W. Y. (2021) (methodology) — FinQA: a dataset of numerical reasoning over financial data. [ref 54, p. 21]
- Magomere, J.; Kochkina, E.; Mensah, S.; Kaur, S.; Smiley, C. (2025) (methodology) — FinNLI: novel dataset for multi-genre financial natural language inference benchmarking. [ref 55, p. 21]
- Hirano, M. (2024) (methodology) — Construction of a Japanese financial benchmark for large language models. [ref 56, p. 21]
- McCracken, M. W.; Ng, S. (2016) (methodology) — FRED-MD: a monthly database for macroeconomic research. [ref 57, p. 21]
- Varoquaux, G.; Buitinck, L.; Louppe, G.; Grisel, O.; Pedregosa, F.; Mueller, A. (2015) (methodology) — Scikit-learn: machine learning without learning the machinery. [ref 64, p. 21]
- Stevens, E.; Antiga, L.; Viehmann, T. (2020) (methodology) — Deep Learning with PyTorch. [ref 65, p. 21]
- Gulli, A.; Pal, S. (2017) (methodology) — Deep Learning with Keras. [ref 66, p. 21]
- Lagouvardos, S.; Dolby, J.; Grech, N.; Antoniadis, A.; Smaragdakis, Y. (2020) (methodology) — Static Analysis of Shape in TensorFlow Programs. [ref 67, p. 21]
- Zhang, Z.; Jiang, C.; Lu, M. (2025) (context) — Fusion of sentiment and market signals for Bitcoin forecasting. [ref 27, p. 20]
- Bussmann, N.; Giudici, P.; Marinelli, D.; Papenbrock, J. (2021) (methodology) — Explainable machine learning in credit risk management. [ref 33, p. 20]
- Talaat, F. M.; Aljadani, A.; Badawy, M.; Elhosseini, M. (2024) (methodology) — Toward interpretable credit scoring: integrating XAI with deep learning for credit card default prediction. [ref 36, p. 20]
- Belanche, D.; Casaló, L. V.; Flavián, C. (2019) (context) — AI in FinTech: understanding robo-advisors adoption among customers. [ref 37, p. 20]
- Kozodoi, N.; Jacob, J.; Lessmann, S. (2022) (methodology) — Fairness in credit scoring: assessment, implementation and profit implications. [ref 145, p. 22]
- Rudin, C. (2019) (context) — Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. [ref 162, p. 22]
- Kang, H.; Liu, X. Y. (2023) (methodology) — Deficiency of large language models in finance: empirical examination of hallucination. [ref 298, p. 31]
- Barry, M.; Caillaut, G.; Halftermeyer, P.; Qader, R.; Mouayad, M.; Deit, F. L.; Cariolaro, D.; Gesnouin, J. (2025) (methodology) — GraphRAG: leveraging graph-based efficiency to minimize hallucinations in LLM-driven RAG for finance data. [ref 299, p. 31]
- Bonawitz, K.; Eichner, H.; Grieskamp, W.; Huba, D.; Ingerman, A.; Ivanov, V.; Kiddon, C.; Konen, J.; Mazzocchi, S.; McMahan, H. B. (2019) (methodology) — Towards federated learning at scale: system design. [ref 290, p. 30]
- di Castri, S.; Grasser, M.; Kulenkampff, A. (2020) (context) — Chatbot application and complaints management system for the Bangko Sentral ng Pilipinas (BSP). [ref 380, p. 35]

## Statistical Evidence

| Outcome | Metric | Value | CI | p | Locator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Global generative AI market size in 2023 | market size | USD 13.5 billion | — | — | Sec. 1, p. 2 |
| Projected global generative AI market size by 2033 | market size | approximately USD 255.8 billion | — | — | Sec. 1, p. 2 |
| Compound annual growth rate of the global generative AI market | CAGR | 34.2% | — | — | Sec. 1, p. 2 |
| North America share of global generative AI revenue in 2023 | market share | over 42.1% | — | — | Sec. 1, p. 2 |
| North America generative AI revenue in 2023 | revenue | USD 5.6 billion | — | — | Sec. 1, p. 2 |
| FinQA question–answer pairs | count | 8,281 | — | — | Table 1, p. 6 |
| FinQA financial reports | count | 2,800 | — | — | Table 1, p. 6 |
| SEC 10-K report coverage period | period | ~1993–2020 | — | — | Table 1, p. 6 |
| References cited in the review | count | 402 | — | — | Reference list, pp. 19–35 |

## Quotes

| Text | Locator | Module |
| :--- | :--- | :--- |
| "Artificial intelligence (AI) has become a pivotal force in the financial technology (fintech) sector, reshaping services through enhanced automation, improved efficiency, and personalization." | Abstract, p. 1 | pfm_apps_overview |
| "The integration of sophisticated AI models, however, introduces significant challenges concerning data privacy, algorithmic bias, and a lack of transparency" | Abstract, p. 1 | software_quality_evaluation |
| "This review provides a holistic synthesis of the current landscape, introducing a structured taxonomy of AI applications that ranges from foundational machine learning in areas like credit scoring and fraud detection to advanced autonomous agents capable of dynamic decision making." | Abstract, p. 1 | model_algorithm_integration |
| "Artificial intelligence became increasingly important to financial technology because financial systems generated large scale, high frequency, and highly heterogeneous data that exceeded the analytical capacity of many conventional decision frameworks." | Sec. 1, p. 1 | data_collection |
| "The importance of AI in fintech was also reinforced by the limitations of conventional rule based and linear modelling approaches in settings marked by uncertainty, fraud risk, market volatility, and rapidly changing customer behaviour." | Sec. 1, p. 1 | model_algorithm_integration |
| "Despite the rapid diffusion of artificial intelligence in financial technology, its practical deployment remained constrained by severe data related limitations." | Sec. 1, p. 3 | data_collection |
| "A second major gap concerned transparency and fairness in high stakes financial decisions." | Sec. 1, p. 4 | software_quality_evaluation |
| "Another emerging gap concerned the use of large language models and generative systems in finance." | Sec. 1, p. 4 | model_algorithm_integration |
| "The long-term value of AI in fintech will depend less on technical performance alone than on whether these systems can be made robust, interpretable, fair, secure and governable in high-stakes financial environments." | Sec. 5, p. 17 | software_quality_evaluation |
| "AI agents are being deployed across a spectrum of financial applications, driving innovation and efficiency." | Sec. 3, p. 12 | model_algorithm_integration |
| "The most widely discussed technical challenge is the lack of transparency in complex AI models, often termed the 'black box' problem." | Sec. 4, p. 14 | software_quality_evaluation |
| "Furthermore, the potential for AI models to perpetuate and even amplify existing societal biases is a significant ethical and technical challenge." | Sec. 4, p. 16 | software_quality_evaluation |
| "The dynamic and stringent regulatory landscape presents an ongoing technical challenge for AI adoption in fintech." | Sec. 4, p. 16 | system_performance_evaluation |
| "Table 2 clarified that artificial intelligence models in fintech were not interchangeable, because each model class offered different technical strengths and matched different financial tasks." | Sec. 2.3, p. 8 | model_algorithm_integration |
| "Overall, the choice of artificial intelligence model in fintech was task dependent rather than universal." | Sec. 2.3, p. 9 | model_algorithm_integration |