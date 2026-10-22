---
conversion_metadata:
  converted_at: "2026-10-21T11:48:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "Ariningsih & Muhammad, 2024.pdf"
  source_pdf_sha256: "6ff670266322f47593fd3ac5cd0318680ef5cd136eedda7362120eb1dc852bbc"
  page_count: 9
  markdown_char_count: 70135
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Intechno Journal :  
Information Technology Journal 
Vol. 6 No. 2 December 2024

Homepage: https://jurnal.amikom.ac.id/index.php/intechno

e-ISSN: 2655-1438 
p-ISSN: 2655-1632

Quality Evaluation of Ticketing Management System Using 
ISO/IEC25010:2023 Standards and AHP Method

Puji Ariningsih1, Alva Hendi Muhammad2 
1,2School of Posgraduate, Magister of Informatics, Universitas Amikom Yogyakarta, Ring Road Utara Condongcatur Depok Sleman, 
Yogyakarta 55281, Indonesia

Article Info 
Article history:

Received December 17, 2024 
Revised December 23, 2024 
Accepted December 29, 2024 
Published December 31, 2024

Keywords:

Software Evaluation  
Quality Assurance 
Ticket Management System 
ISO/IEC 25010 
Analytic Hierarchy Process

ABSTRACT

Purpose: Information Technology plays a crucial role in supporting education 
service  systems.  When  system-related  issues  arise,  a  Ticket  Management 
System (TMS) becomes essential to address various software and hardware 
problems.  Evaluating  the  performance  and  quality  of  TMS  applications  is 
necessary  to  ensure  their  effectiveness.  This  study  aims  to  evaluate  the 
performance and quality of a Ticket Management System (TMS) application 
developed by University of Amikom Yogyakarta using ISO/IEC 25010:2023, 
while  also  determining  the  priority  of  three  key  ISO/IEC  25010:2023 
characteristics through the Analytic Hierarchy Process (AHP) method. This 
dual  approach  ensures  both  comprehensive  quality  assessment  and  focused 
analysis of critical system characteristics. 
Methods/Study design/approach: The  Analytic Hierarchy Process  method 
is employed to prioritize three key ISO/IEC 25010 characteristics by engaging 
TMS  application  users.  Following  the  ranking,  the  study  conducts  quality 
measurements using questionnaires and black box testing. The questionnaire 
results  are  assessed  using  a  Likert  scale  to  determine  scores  for  the  TMS 
application  based  on  the  sub-characteristics  of  the  three  selected  ISO/IEC 
25010:2023 characteristics and the AHP-derived rankings. 
Result/Findings: The findings indicate that the TMS application achieved a 
quality score of 4.354. This shows that the TMS application is in the good 
category. 
Novelty/Originality/Value:  The  study  highlights  the  need  for  performance 
efficiency improvements, specifically in the Time Behavior sub-characteristic, 
to enhance the overall quality of the TMS application.

This is an open access article under the CC BY license.

Corresponding Author:

Puji Ariningsih 
Email: 23.55.1414@students.amikom.ac.id

1.

INTRODUCTION

Information  Technology  (IT)  plays  a  crucial  role  in  various  aspects  of  work  and  activities  in 
organizations. The role of IT is very influential in changing the way of communication and changing the way 
humans access information, both in the scope of work and daily life [1]. IT support services extend beyond 
computer  networks,  operating  systems,  internet  connections,  and  security  to  encompass  the  resolution  of 
software and hardware issues [2]. These issues, whether related to software or hardware errors, can often be 
addressed  remotely  or  within  the  organization’s  infrastructure  [3].  For  organizations,  having  an  effective 
customer service system is essential as it serves as the face of the organization and plays a significant role in

© Universitas Amikom Yogyakarta Publisher

86

---

<!-- PAGE 2 -->

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   87

maintaining  its  reputation.  Such  systems  must  efficiently  handle  complaints,  requests,  and  facilitate  clear 
communication between the organization and its users.

A Ticket Management System (TMS) serves as a  key tool in this process, enabling the systematic 
management of issues and ensuring timely resolution. TMS is a system that simplifies the process of handling 
customer requests. A reliable customer service system is essential for any company or organization, as it serves 
as the face of the organization and plays a key role in maintaining its reputation. Such a system must effectively 
manage complaints, address requests, and function as a clear communication channel between the organization 
and its customers. Most companies have TMS, the purpose of which is to help users/customers to create tickets 
by describing their problems or requests [4]. The contribution of TMS is to integrate companies and clients in 
an efficient and structured way [5]. It is indisputable that TMS is an important part of IT support in various 
industries.  Not  only  for  technical  teams,  but  it  has  penetrated  the  realm  of  management.  TMS  is  the  main 
contact point for users/customers seeking help with their queries or problems. It includes a request module that 
serves as a channel to manage requests. Customer requests will be handled by TMS admins based on Frequently 
Asked Questions (FAQ). However, if there is no solution then the request is forwarded to the technician to be 
resolved [3].

The application of TMS is not only in the industrial world, but also in the world of education. Several 
studies have developed TMS for education. [6], developed TMS at Klabat University for fault reporting and 
monitoring repair work. With TMS, the IT Department can be helped in monitoring incoming tasks and jobs. 
However, this research does not review the developed quality analysis of TMS. [7], analyzed, and implemented 
TMS  Helpdesk  at  Singaperbangsa  University  of  Karawang.  This  system  was  developed  to  facilitate  the 
academic community in reporting ICT problems and providing information to them about the progress of the 
problems reported. From this research, TMS helpdesk was produced by utilizing OS Ticket in the UPT-TIK 
work unit at Singaperbangsa University of Karawang. However, the research has not analyzed the quality of 
the system developed. [8], utilizing machine learning models to classify help desk tickets with the right service 
to minimize processing time, save human resources, and increase user satisfaction. This research helps define 
business processes, with well-defined activities and measure KPIs to assess the performance of IT staff and 
processes. However, this research has not analyzed the quality of the help desk ticket system.

Analysis  related  to  the  quality  of  the  TMS  is  important  to  ensure  the  quality  of  the  TMS 
implementation.  Testing  and  ensuring  the  quality  of  the  software  to  be  used  is  something  that  needs  to  be 
considered,  because  it  requires  sufficient  knowledge  in  finding  the  source  of  existing  errors  [9]. There  are 
several types of quality measurement models that are used as software assessment standards. One model that 
can be used to measure software quality is ISO/IEC 25010 [10]. Some studies that apply the ISO/IEC 25010 
standard  document  include:  Research  by  [9]  measures  software  quality  using  the  ISO  /  IEC  25010:  2011 
method  for  website  portal  bios  in  Bank  companies.  In  his  research,  the  Analytic  Hierarchy  Process  (AHP) 
method is used to give the weight value of each characteristic in the ISO / IEC 25010: 2011 standard document. 
There are 6 characteristics used from 8 characteristics in ISO / IEC 25010 / 2011. From the results of measuring 
the software’s quality, a value of 4.87 was obtained in the good category. Research [11], measuring the quality 
of Halodoc software using ISO 25010: 2011 using 8 characteristics and 29 sub-characteristics. In determining 
the weight of the assessment in the test using the Analytical Hierarchy Process (AHP). The testing strategy was 
carried out by Black-Box testing, push testing, and distributing surveys to 100 respondents for Convenience 
testing. From the total test results for the Halodoc application, it gets a score of 4.515 out of a maximum score 
of 5.

Several previous studies have emphasized that software quality must be determined, measured, and 
evaluated using validated measurement methods. One widely adopted approach involves the ISO/IEC 25010 
quality model. Over time, this standard has evolved, with the most recent update transitioning from ISO/IEC 
25010:2011 to ISO/IEC 25010:2023. This research develops a framework to analyse the quality of the Ticket 
Management System (TMS) in higher education using the ISO/IEC 25010:2023 standard. ISO/IEC 25010, first 
published in 2011 by the Canadian Standards Association, provides guidelines for software evaluation. It is an 
enhancement of the earlier ISO/IEC 9126 model and belongs to the broader ISO/IEC 250n series.

The ISO/IEC models related to software quality have undergone revisions, with the latest versions 
being  ISO/IEC  25010:2023,  which  focuses  on  product  quality,  and  ISO/IEC  25002:2004,  which  includes 
quality characteristics for software evaluation. ISO/IEC provides two system quality measurement models: the 
Quality in Use model and the Software Product Quality model. The ISO/IEC 25010:2023 is an updated version 
of ISO/IEC 25010:2011.

Even  though  the  ISO/IEC  25010:2023  model  consists  of  nine  quality  characteristics:  Functional 
Interaction  Capability,  Reliability,  Security,

Suitability,  Performance  Efficiency,  Compatibility, 
Maintainability, Flexibility, and Safety. This study focuses on three key characteristics:

1.  Functional Suitability 
2.  Performance Efficiency 
3.  Reliability

---

<!-- PAGE 3 -->

88

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

These characteristics were selected based on their relevance to the current state of the system. The 
quality analysis framework for the TMS software will be implemented and simulated at University of Amikom 
Yogyakarta  (Amikom).  Amikom  has  an  IT  Directorate  responsible  for  developing  a  web-based  Ticket 
Management System (TMS) called Amikom Care that can be accessed at www.care.amikom.ac.id. The users 
of this system include work units/directorates, lecturers, students, education personnel, prospective students, 
and  the  public.  Users  can  report  issues  by  creating  tickets  within  TMS  Amikom  Care.  Once  a  ticket  is 
submitted, it is initially handled by Customer Service (CS) within the respective work unit. If the issue cannot 
be resolved at this level, the ticket is escalated to the Team Member (TM) and further, if necessary, to the Head 
of Department (HOD). Although TMS Amikom Care is currently operational, no formal quality analysis of the 
software  has  been  conducted  to  date.  This  study  has  two  primary  objectives  :  the  first  is  to  evaluate  the 
performance and quality of the TMS application at Amikom using the ISO/IEC 25010:2023 standard. And the 
second is to determine and prioritize three key characteristics of the ISO/IEC 25010:2023 standard that are 
most relevant for TMS evaluation using the  AHP  method. These objectives are designed to provide both a 
comprehensive  quality assessment and a focused analysis of critical system characteristics that impact  user 
satisfaction and system effectiveness.

2.  Literature Review

The  literature  review  provides  a  foundational  theoretical  framework  to  guide  and  optimize  the 
research process. It enables researchers to identify, understand, and adopt established concepts relevant to the 
study. In this research, the ISO/IEC 25010 standard serves as the primary model for evaluating software quality. 
This model is widely recognized for its comprehensive approach to assessing software product characteristics 
and ensuring that critical quality parameters are met during evaluation.

The  ISO/IEC  25010  standard,  first  introduced  in  2011  and  revised  in  2023,  provides  a  detailed 
framework  for  evaluating  software  and  system  quality.  It  defines  a  product  quality  model  that  categorizes 
essential quality characteristics and their sub-characteristics, which are integral to measuring a system’s ability 
to meet functional, performance, and user-specific requirements. Each characteristic reflects a key dimension 
of software quality, encompassing aspects like functionality, performance, reliability, and adaptability. These 
dimensions ensure that software not only meets technical requirements but also delivers value to its users and 
stakeholders under specified conditions. As shown in Figure 1, the product quality model listed in ISO/IEC 
25010 consists of eight quality characteristics.

Figure 1 Characteristics and Sub Characteristics of ISO 25010:2023 
(Source: https://iso25000.com/)

The  nine  quality  characteristics  outlined  in  ISO/IEC  25010:2023  are  Functional  Suitability, 
Performance  Efficiency,  Compatibility,  Interaction  Capability,  Reliability,  Security,  Maintainability, 
Flexibility, and Safety. These characteristics collectively form a robust framework for understanding software 
quality. The following sections elaborate on each characteristic and its sub-components to clarify their role in 
the evaluation process [12]. 
1)  Functional  Suitability  represents  the  system’s  ability  to  deliver  functions  that  meet  specific  user 
requirements under defined conditions. This characteristic emphasizes functional completeness, ensuring 
all  necessary  features  are  provided;  functional  correctness,  which  guarantees  accurate  outcomes;  and 
functional appropriateness, ensuring the functionality meets its intended purpose efficiently.

2)  Performance  Efficiency  addresses  the  system’s  ability  to  deliver  performance  relative  to  resource 
consumption  under  given  conditions.  Sub-characteristics  include  time  behavior  (response  time  and

---

<!-- PAGE 4 -->

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   89

latency), resource utilization (efficient use of system resources), and capacity (system’s ability to handle 
varying workloads).

4)

3)  Compatibility examines the system’s ability to operate and exchange information with other systems or 
products.  It  includes  co-existence,  ensuring  harmonious  operation  within  shared  environments,  and 
interoperability, which focuses on effective communication and data exchange between systems. 
Interaction  Capability  focuses  on  the  usability  and  user  experience  of  the  system.  It  assesses  how 
effectively the product interacts with users through its interface. Sub-characteristics include learnability 
(ease of understanding), operability (ease of operation), user error protection (prevention of misuse), and 
user  engagement  (satisfaction  and  inclusivity).  This  dimension  ensures  that  the  system  is  accessible, 
intuitive, and user-centered.

5)  Reliability  measures  the  product’s  ability  to  operate  consistently  under  specified  conditions  without 
failure.  Key  sub-characteristics  include  fault  tolerance  (system  resilience  during  failures),  availability 
(operational uptime), and recoverability (ability to restore after a failure).

6)  Security  evaluates  the  extent  to  which  the  system  safeguards  data  and  resources  against  unauthorized 
access and threats. It encompasses confidentiality (data privacy), integrity (data accuracy), non-repudiation 
(proof of actions), authenticity (verification of identities), and accountability (traceability of actions). This 
characteristic is essential for protecting sensitive organizational and user information.

7)  Maintainability highlights the product’s capacity for efficient modification, ensuring adaptability to new 
requirements and environments. Sub-characteristics such as modularity (segmented design), reusability 
(component  reuse),  modifiability  (ease  of  changes),  and  testability  (ease  of  testing)  facilitate  ongoing 
development and maintenance.

8)  Flexibility assesses the system’s ability to adapt to changes in requirements, contexts, or environments. It 
includes  adaptability  (adjustments  to  new  conditions),  scalability  (handling  increased  demands),  and 
installability (ease of deployment).

9)  Safety  ensures  the  product’s  ability  to  prevent  risks  that  may  harm  human  life,  property,  or  the 
environment. This includes hazard warnings, risk identification, and fail-safe mechanisms that minimize 
the potential for accidents or failures.

By  incorporating  these  nine  characteristics  and  their  sub-components,  ISO/IEC  25010:2023  provides  a 
structured approach to software quality evaluation.

3.  METHOD

3.1  Metode Analytical Hierarchy Process (AHP)

Analytical Hierarchy Process is a decision support model developed by Thomas L. Saaty. This model will 
decompose a complex  multicriteria problem into a hierarchical  form by  giving a  value  of how important a 
criterion variable is and determining which criteria have the highest priority so that they can affect the results 
under certain conditions. Therefore, we  need to know the problem, decision needs and objectives, decision 
criteria, sub-criteria, stakeholders and affected groups and alternative actions to be taken [13]. A sample of 
AHP Hierarchical tree is shown in Figure 2.

Figure 2. Sample AHP Hierarchical Tree

3.2  Likert Scale (AHP)

This scale is a psychometric scale that is often used in questionnaires. This scale was developed by Rensis

Likert in 1932 to measure people’s attitudes. The Likert scale provides five answers consisting of:

---

<!-- PAGE 5 -->

90

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

1: strongly disagree 
2: disagree 
3: undecided 
4: agree 
5: strongly agree

For this reason, researchers implemented a Likert scale in this study with the following description (Table 1):

Skor  Likert Scale  Meaning

Tabel 1. Likert Scale Score Calculation

5 
4 
3 
2 
1

Excellent 
Good 
Fair 
Poor 
Very Poor

Features work very well, responds very quickly without errors 
Features work well, responds quickly without errors 
Features work well, but there are still things that need to be improved 
Features are available but do not work and there are many errors massages 
Features does not work at all

4.  RESULTS AND DISCUSSIONS

4.1  AHP Hierarchy Decision Making on ISO/IEC 25010:2023

The  decision  hierarchy  for  the  selected  characteristics  of  the  ISO/IEC  25010:2023  standard  was 
established using the Analytic Hierarchy Process (AHP) via an online system. The hierarchy is structured into 
multiple levels: Level 0 represents the overarching goal of the evaluation, Level 1 comprises the three selected 
characteristics  to  be  prioritized,  and  Level  2  includes  their  corresponding  sub-characteristics,  which  are 
assessed through pairwise comparisons. In the AHP framework, each sub-characteristic at Level 2 is compared 
in pairs to determine relative importance. The comparisons use a priority scale ranging from 1 to 9, where 1 
indicates equal importance, and 9 signifies extreme importance of one sub-characteristic over another. These 
pairwise comparisons are processed to generate priority weightings, which reflect the relative significance of 
the sub-characteristics and characteristics.

The priority weightings derived from the pairwise comparisons at Level 2 are aggregated to determine 
the overall ranking of the characteristics at Level 1. This process ensures a systematic evaluation, providing a 
clear understanding of the significance of each characteristic within the context of the ISO/IEC 25010:2023 
standard.  The  AHP  decision  hierarchy  results,  as  illustrated  in  Figure  3,  visually  represent  the  relationship 
between the goal, the three prioritized characteristics, and their sub-characteristics. The calculated weightings 
obtained through this process serve as the basis for subsequent quality measurements and analysis of the TMS 
application.

Figure 3. Decision hierarchy result with AHP online system

The decision hierarchy of ISO/IEC 25010:2023 characteristics is determined by inputting 3 previously 
determined characteristics into the AHP online system. Level 0 is the Goal; level 1 is the 3 characteristics that 
will  be  ranked,  and  level  2  is  the  sub-characteristics  that  will  be  pairwise.  The  AHP  decision  hierarchy  of 
ISO/IEC 25010:2023 standard is shown in Figure 3.

---

<!-- PAGE 6 -->

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   91

4.2  Analysis of AHP Hierarchy Decision Making Results

The  pairwise  comparisons  provided  by  stakeholders  for  the  sub-characteristics  of  the  ISO/IEC 
25010:2023 standard yielded the global priority weights for each sub-characteristic. These weights were used 
to  determine  the  overall  priority  of  the  Level  1  characteristics  in  the  decision  hierarchy.  The  results  are 
summarized as follows: 
1.  Functional Suitability

Among the Functional Suitability sub-characteristics, Functional Appropriateness emerged as the highest 
priority, receiving a weight of 20.4%. This indicates its critical role in ensuring that the TMS application 
meets user needs and supports task completion effectively. Following this, Functional Correctness was 
ranked  second  with  a  weight  of  14.8%,  reflecting  its  importance  in  delivering  accurate  results.  Lastly, 
Functional Completeness received the lowest weight of 6.1%, highlighting a relatively lower priority for 
including all required functions compared to appropriateness and correctness.

2.  Performance Efficiency

For Performance Efficiency, Time Behaviour was prioritized as the most significant sub-characteristic, 
with a weight of 15.2%. This reflects the critical need for the system to respond quickly and efficiently 
under defined conditions. In contrast, Capacity and Resource Utilization were equally weighted at 5.9%, 
indicating their shared but lower significance compared to Time Behaviour.

3.  Reliability

Within  the  Reliability  characteristic,  Availability  emerged  as  the  top  priority  with  a  weight  of  7.6%, 
underscoring  the  importance  of  system  uptime  and  consistent  availability.  Fault  Tolerance  followed 
closely with a weight of 7.2%, reflecting its role in maintaining system operation during failure scenarios. 
Maturity  ranked  third  with  a  weight  of  6%,  while  Recoverability  was  identified  as  the  lowest  priority 
among the Reliability sub-characteristics.

4.3  Overall Priority Ranking of Characteristics

Using  the  global  priority  weights  calculated  through  the  AHP  online  system,  the  three  main

characteristics were ranked as follows:

1.  Functional Suitability – ranked first with a weight of 49.5%, highlighting its critical role in meeting

user expectations and functional needs.

2.  Performance Efficiency – ranked second with a weight of 27%, reflecting the importance of system

performance in terms of response time and resource usage.

3.  Reliability – ranked third with a weight of 23.5%, indicating its significance in ensuring the system

operates consistently and dependably. 
The  priority  ranking  analysis  results  are  illustrated  in  Figure  4,  which  visually  represents  the

distribution of weights across the three characteristics.

Figure 4. The results of priority ranking analysis with AHP

Following the prioritization process, researchers conducted further testing of the sub-characteristics

using questionnaires and black box testing. These methods were applied to measure the actual performance 
of the TMS application based on user feedback and functional validation, providing a comprehensive 
assessment aligned with the ISO/IEC 25010:2023 standard.

4.4  Result Sub-Characteristics Questionnaires and Black Box Testing

We measured the sub-characteristics of the ISO/IEC 25010:2023 standard through systematic black

box testing. Each sub-characteristic was evaluated by testing specific functionality of the TMS application. 
1.  Functional  Completeness.  Functional  Completeness  was  assessed  through  black  box  testing,  where  all 
existing functions of the TMS application were systematically tested. The evaluation aimed to determine 
whether all necessary functions were present and operational. The test revealed that several functions did

---

<!-- PAGE 7 -->

92

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

not operate as intended, resulting in a score of 4, which is categorized as good. Despite this positive result, 
the findings indicate areas where functionality requires improvement.

2.  Functional  Correctness.  Functional  Correctness  was  measured  using  the  black  box  testing  method, 
focusing  on  critical  features  such  as  the  login,  search,  export  to Excel,  and  notification  functions.  The 
objective  was  to  verify  whether  the  application  provides  accurate  outputs  with  the  required  level  of 
precision.  While  the  test  results  demonstrated  that  the  TMS  application  largely  met  user  expectations, 
some functions still require refinement. Consequently, this sub-characteristic also received a score of 4, 
placing it in the good category.

3.  Functional  Appropriateness.  Functional  Appropriateness  was  similarly  evaluated  through  black  box 
testing by analyzing all website functions to determine whether the system adequately supports users in 
achieving  their  tasks  and  goals.  The  evaluation  confirmed  that  the  website  meets  user  expectations  by 
providing  the  necessary  facilities  and  tools.  As  a  result,  the  TMS  application  scored  4  for  this  sub-
characteristic, placing it within the good category.

Overall,  these  assessments  highlight  that  while  the  TMS  application  performs  well  in  terms  of 
functional  suitability, there remain areas  for improvement  in specific  functionalities. The black box testing 
revealed that some functions did not operate as intended, suggesting the need for targeted enhancements to 
optimize system performance. Based on the evaluation results, several key areas for improvement have been 
identified:

•  Performance Optimization

The Time Behavior sub-characteristic scored 3.700, indicating a need for response time optimization 
Recommended actions: 
o 
o 
o

Implement server-side caching to reduce database query times 
Optimize database indexes for frequently accessed data 
Consider implementing asynchronous processing for ticket updates

•  Functional Enhancement Priorities 
  While Functional Suitability scored well (4.369), specific improvements are recommended:

o 
o 
o

Enhance the ticket categorization system to improve routing efficiency 
Implement automated ticket status updates 
Develop a knowledge base integration for common issues

•  Reliability Improvements

Despite strong overall reliability (4.619), the following enhancements are suggested:

o 
o

Develop a comprehensive disaster recovery plan 
Enhance the backup system for improved recoverability

•  User Experience Considerations

Based on user feedback, the following improvements are recommended:

o 
o

Enhance the notification system 
Improve the mobile responsiveness of the interface

These recommendations are prioritized based on their potential impact on system quality and user 
satisfaction. Implementation should be phased, with immediate focus on performance optimization due to its 
direct impact on user experience.

4.5  Total Assessment of Characteristics and Sub-Characteristics

After testing and evaluating the three characteristics and their respective sub-characteristics of the 
ISO/IEC  25010:2023  standard,  the  total  score  was  calculated  to  determine  the  overall  quality  of  the  TMS 
application. The calculations were based on the characteristic weights obtained through the AHP method and 
the assessment results for each sub-characteristic, as detailed in Table 2.

---

<!-- PAGE 8 -->

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   93

Tabel 2. TMS App score calculation result 
Assessment 
Result

Sub-characteristic

Sub-
characteristic

4.552

Total 
Subcategor
ies

Total 
Result

Characteristic

Characteristic 
Weight

Functional 
Suitability

0.495

Functional 
completeness

Functional 
correctness

Functional 
appropriateness

Time behavior

Performance 
Efficiency

0.27

Resource utilization

Reliability

0.235

Capacity

Faultlessness

Availability

Fault tolerance

Recoverability

4.123

4.369

2.162

4.431

3.700

4.250

4.333

4.527

5.000

4.750

4.200

4.094

1.106

4.619

1.086

TOTAL

1

TOTAL

4.354

The  evaluation  results  demonstrate  that  Functional  Suitability  played  the  most  significant  role  in 
determining the overall quality score of the TMS application, with a weight of 0.495. The sub-characteristics 
— Functional Completeness, Functional Correctness, and Functional Appropriateness — achieved an average 
score of 4.369, resulting in a weighted contribution of 2.162. This highlights the importance of ensuring that 
the system provides accurate, complete, and appropriate functionality to meet user requirements effectively. 
Performance  Efficiency,  with  a  weight  of  0.27,  ranked  second  in  priority.  The  sub-characteristics  assessed 
included  Time  Behaviour,  Resource  Utilization,  and  Capacity,  achieving  an  average  score  of  4.094  and 
contributing  1.106  to  the  total  score.  Among  these,  Time  Behaviour  recorded  the  lowest  individual 
performance, signalling the need for optimization to improve response time and overall system efficiency.

The Reliability characteristic, weighted at 0.235, performed well overall, with sub-characteristics such 
as  Faultlessness,  Availability,  Fault  Tolerance,  and  Recoverability  achieving  the  highest  average  score  of 
4.619.  Availability  stood  out  with  a  perfect  score  of  5.000,  underscoring  the  system's  strong  capability  to 
remain operational and accessible without interruptions.

The  final  evaluation  yielded  a  total  score  of  4.354,  placing  the  TMS  application  in  the  “Good” 
category. This result reflects the system’s overall effectiveness in meeting the critical quality requirements of 
functionality, performance, and reliability, as outlined by the ISO/IEC 25010:2023 standard. Overall, while 
Functional Suitability emerged as the most influential factor due to its high weight and consistent performance 
across  sub-characteristics,  Performance  Efficiency  revealed  room  for  improvement,  particularly  in  Time 
Behaviour.  The  Reliability  characteristic  demonstrated  strong  results,  especially  in  Availability,  further 
enhancing  the  overall  quality.  These  findings  provide  valuable  insights  into  the  strengths  and  areas  for 
improvement  in  the  TMS  application,  emphasizing  the  need  for  targeted  enhancements  to  optimize  system 
performance.

5.  CONCLUSION

In this study, the prioritization of three selected characteristics from the ISO/IEC 25010:2023 standard 
was conducted using the Analytic Hierarchy Process method. The evaluation of each sub-characteristic was 
carried  out  through  a  combination  of  questionnaires  and  black  box  testing.  The  measurement  results  were 
analyzed  using  a  Likert  scale  to  assign  scores  to  each  sub-characteristic.  The  scores  for  individual  sub-
characteristics were averaged and weighted based on the characteristic prioritization derived from the  AHP 
method.  This  process  ensured  a  systematic  and  data-driven  evaluation  of  the  software  quality.  The  results 
revealed that the Ticket Management System application, evaluated in the case study at University of Amikom

---

<!-- PAGE 9 -->

94

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

Yogyakarta, achieved a score of 4.354. This score indicates that the TMS application falls within the “good” 
category, reflecting a positive overall quality while highlighting areas for potential improvement.

REFERENCES 
[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

[11]

[12]

[13]

R. S. Mission, “Multi-channel support and ticketing interface for online support management system platforms,”  Int. J. Appl. 
Sci. Eng., vol. 18, no. 4(Special Issue), pp. 1–9, 2021, doi: 10.6703/IJASE.202106_18(4).006. 
M. Al-Emran and H. Al Chalabi, “‘Developing an IT Help Desk Troubleshooter Expert System for diagnosing and solving IT 
Problems,’” BCS Learning & Development, Feb. 2015. doi: 10.14236/ewic/bcsme2014.16. 
F.  Gohil  and  M.  Vikash  Kumar,  “Ticketing  System  the  Creative  Commons  Attribution  License  (CC  BY  4.0).”  [Online]. 
Available: http://creativecommons.org/licenses/by/4.0 
S. Fuchs, C. Drieschner, and H. Wittges, “Improving Support Ticket Systems Using Machine Learning: A Literature Review,” 
in Proceedings of the Annual Hawaii International Conference on System Sciences, IEEE Computer Society, 2022, pp. 1893–
1902. doi: 10.24251/hicss.2022.238. 
K. D. Aglibar and N. Rodelas, “Impact of Critical and Auto Ticket: Analysis for Management and Workers Productivity in using 
a Ticketing System,” Int. J. Comput. Sci. Res., vol. 6, pp. 988–1004, Jan. 2022, doi: 10.25147/ijcsr.2017.001.1.84. 
S. I. Adam, J. H. Moedjahedy, and O. Lengkong, “Pengembangan IT Helpdesk Ticketing Sistem Berbasis Web di Universitas 
Klabat Development of Web-based IT Helpdesk Ticketing System at Universitas Klabat,” Cogito Smart J. |, vol. 6, no. 2, 2020. 
D.  Yunadi,  N.  Sulistiyowati,  and  A.  A.  Ridho,  “Analisis  Dan  Implementasi  Sistem  Ticketing  Helpdesk  Pada  Universitas 
Singaperbangsa Karawang,” 2020. 
F. Al-Hawari and H. Barham, “A machine learning based help desk system for IT service management,” J. King Saud Univ. - 
Comput. Inf. Sci., vol. 33, no. 6, pp. 702–718, Jul. 2021, doi: 10.1016/J.JKSUCI.2019.04.001. 
A. Yulianty and A. Kurniawati, “Quality Analysis of Bios Portal Website at Banking Companies Using ISO / IEC 25010:2011 
Method,” Int. Res. J. Adv. Eng. Sci., vol. 6, no. 2, pp. 11–16, 2021. 
M.  Mulyawan,  I.  N.  S.  Kumara,  A.  Swamardika,  and  K.  Saputra,  “Kualitas  Sistem  Informasi  Berdasarkan  ISO/IEC  25010: 
Literature Review,” Maj. Ilm. Teknol. Elektro, vol. 20, p. 15, Mar. 2021, doi: 10.24843/MITE.2021.v20i01.P02. 
A.  Arga  Pratama  and  A.  B.  Mutiara,  “Software  Quality  Analysis  for  Halodoc  Application  using  ISO  25010:2011,”  2021. 
[Online]. Available: www.ijacsa.thesai.org 
ISO/IEC25010,  “Systems  and  software  engineering-Systems  and  software  Quality  Requirements  and  Evaluation  (SQuaRE)-
Product quality model,” Switzerland, vol. 2023, 2023. 
T.  L.  Saaty,  “Decision  making  with  the  Analytic  Hierarchy  Process,”  Sci.  Iran.,  vol.  9,  no.  3,  pp.  215–229,  2002,  doi: 
10.1504/ijssci.2008.017590.

<!-- MARKITDOWN CONVERSION -->

<!-- The following is the full MarkItDown conversion for formatting fidelity. -->

Intechno Journal :
Information Technology Journal
Vol. 6 No. 2 December 2024

Homepage: https://jurnal.amikom.ac.id/index.php/intechno

e-ISSN: 2655-1438
p-ISSN: 2655-1632

Quality Evaluation of Ticketing Management System Using
ISO/IEC25010:2023 Standards and AHP Method

Puji Ariningsih1, Alva Hendi Muhammad2
1,2School of Posgraduate, Magister of Informatics, Universitas Amikom Yogyakarta, Ring Road Utara Condongcatur Depok Sleman,
Yogyakarta 55281, Indonesia

Article Info
Article history:

Received December 17, 2024
Revised December 23, 2024
Accepted December 29, 2024
Published December 31, 2024

Keywords:

Software Evaluation
Quality Assurance
Ticket Management System
ISO/IEC 25010
Analytic Hierarchy Process

  ABSTRACT

Purpose: Information Technology plays a crucial role in supporting education
service  systems.  When  system-related  issues  arise,  a  Ticket  Management
System (TMS) becomes essential to address various software and hardware
problems.  Evaluating  the  performance  and  quality  of  TMS  applications  is
necessary  to  ensure  their  effectiveness.  This  study  aims  to  evaluate  the
performance and quality of a Ticket Management System (TMS) application
developed by University of Amikom Yogyakarta using ISO/IEC 25010:2023,
while  also  determining  the  priority  of  three  key  ISO/IEC  25010:2023
characteristics through the Analytic Hierarchy Process (AHP) method. This
dual  approach  ensures  both  comprehensive  quality  assessment  and  focused
analysis of critical system characteristics.
Methods/Study design/approach: The  Analytic Hierarchy Process  method
is employed to prioritize three key ISO/IEC 25010 characteristics by engaging
TMS  application  users.  Following  the  ranking,  the  study  conducts  quality
measurements using questionnaires and black box testing. The questionnaire
results  are  assessed  using  a  Likert  scale  to  determine  scores  for  the  TMS
application  based  on  the  sub-characteristics  of  the  three  selected  ISO/IEC
25010:2023 characteristics and the AHP-derived rankings.
Result/Findings: The findings indicate that the TMS application achieved a
quality score of 4.354. This shows that the TMS application is in the good
category.
Novelty/Originality/Value:  The  study  highlights  the  need  for  performance
efficiency improvements, specifically in the Time Behavior sub-characteristic,
to enhance the overall quality of the TMS application.

This is an open access article under the CC BY license.

Corresponding Author:

Puji Ariningsih
Email: 23.55.1414@students.amikom.ac.id

1.

INTRODUCTION

Information  Technology  (IT)  plays  a  crucial  role  in  various  aspects  of  work  and  activities  in
organizations. The role of IT is very influential in changing the way of communication and changing the way
humans access information, both in the scope of work and daily life [1]. IT support services extend beyond
computer  networks,  operating  systems,  internet  connections,  and  security  to  encompass  the  resolution  of
software and hardware issues [2]. These issues, whether related to software or hardware errors, can often be
addressed  remotely  or  within  the  organization’s  infrastructure  [3].  For  organizations,  having  an  effective
customer service system is essential as it serves as the face of the organization and plays a significant role in

© Universitas Amikom Yogyakarta Publisher

     86

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   87

maintaining  its  reputation.  Such  systems  must  efficiently  handle  complaints,  requests,  and  facilitate  clear
communication between the organization and its users.

A Ticket Management System (TMS) serves as a  key tool in this process, enabling the systematic
management of issues and ensuring timely resolution. TMS is a system that simplifies the process of handling
customer requests. A reliable customer service system is essential for any company or organization, as it serves
as the face of the organization and plays a key role in maintaining its reputation. Such a system must effectively
manage complaints, address requests, and function as a clear communication channel between the organization
and its customers. Most companies have TMS, the purpose of which is to help users/customers to create tickets
by describing their problems or requests [4]. The contribution of TMS is to integrate companies and clients in
an efficient and structured way [5]. It is indisputable that TMS is an important part of IT support in various
industries.  Not  only  for  technical  teams,  but  it  has  penetrated  the  realm  of  management.  TMS  is  the  main
contact point for users/customers seeking help with their queries or problems. It includes a request module that
serves as a channel to manage requests. Customer requests will be handled by TMS admins based on Frequently
Asked Questions (FAQ). However, if there is no solution then the request is forwarded to the technician to be
resolved [3].

The application of TMS is not only in the industrial world, but also in the world of education. Several
studies have developed TMS for education. [6], developed TMS at Klabat University for fault reporting and
monitoring repair work. With TMS, the IT Department can be helped in monitoring incoming tasks and jobs.
However, this research does not review the developed quality analysis of TMS. [7], analyzed, and implemented
TMS  Helpdesk  at  Singaperbangsa  University  of  Karawang.  This  system  was  developed  to  facilitate  the
academic community in reporting ICT problems and providing information to them about the progress of the
problems reported. From this research, TMS helpdesk was produced by utilizing OS Ticket in the UPT-TIK
work unit at Singaperbangsa University of Karawang. However, the research has not analyzed the quality of
the system developed. [8], utilizing machine learning models to classify help desk tickets with the right service
to minimize processing time, save human resources, and increase user satisfaction. This research helps define
business processes, with well-defined activities and measure KPIs to assess the performance of IT staff and
processes. However, this research has not analyzed the quality of the help desk ticket system.

Analysis  related  to  the  quality  of  the  TMS  is  important  to  ensure  the  quality  of  the  TMS
implementation.  Testing  and  ensuring  the  quality  of  the  software  to  be  used  is  something  that  needs  to  be
considered,  because  it  requires  sufficient  knowledge  in  finding  the  source  of  existing  errors  [9]. There  are
several types of quality measurement models that are used as software assessment standards. One model that
can be used to measure software quality is ISO/IEC 25010 [10]. Some studies that apply the ISO/IEC 25010
standard  document  include:  Research  by  [9]  measures  software  quality  using  the  ISO  /  IEC  25010:  2011
method  for  website  portal  bios  in  Bank  companies.  In  his  research,  the  Analytic  Hierarchy  Process  (AHP)
method is used to give the weight value of each characteristic in the ISO / IEC 25010: 2011 standard document.
There are 6 characteristics used from 8 characteristics in ISO / IEC 25010 / 2011. From the results of measuring
the software’s quality, a value of 4.87 was obtained in the good category. Research [11], measuring the quality
of Halodoc software using ISO 25010: 2011 using 8 characteristics and 29 sub-characteristics. In determining
the weight of the assessment in the test using the Analytical Hierarchy Process (AHP). The testing strategy was
carried out by Black-Box testing, push testing, and distributing surveys to 100 respondents for Convenience
testing. From the total test results for the Halodoc application, it gets a score of 4.515 out of a maximum score
of 5.

Several previous studies have emphasized that software quality must be determined, measured, and
evaluated using validated measurement methods. One widely adopted approach involves the ISO/IEC 25010
quality model. Over time, this standard has evolved, with the most recent update transitioning from ISO/IEC
25010:2011 to ISO/IEC 25010:2023. This research develops a framework to analyse the quality of the Ticket
Management System (TMS) in higher education using the ISO/IEC 25010:2023 standard. ISO/IEC 25010, first
published in 2011 by the Canadian Standards Association, provides guidelines for software evaluation. It is an
enhancement of the earlier ISO/IEC 9126 model and belongs to the broader ISO/IEC 250n series.

The ISO/IEC models related to software quality have undergone revisions, with the latest versions
being  ISO/IEC  25010:2023,  which  focuses  on  product  quality,  and  ISO/IEC  25002:2004,  which  includes
quality characteristics for software evaluation. ISO/IEC provides two system quality measurement models: the
Quality in Use model and the Software Product Quality model. The ISO/IEC 25010:2023 is an updated version
of ISO/IEC 25010:2011.

Even  though  the  ISO/IEC  25010:2023  model  consists  of  nine  quality  characteristics:  Functional
Interaction  Capability,  Reliability,  Security,

Suitability,  Performance  Efficiency,  Compatibility,
Maintainability, Flexibility, and Safety. This study focuses on three key characteristics:

1.  Functional Suitability
2.  Performance Efficiency
3.  Reliability

88

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

These characteristics were selected based on their relevance to the current state of the system. The
quality analysis framework for the TMS software will be implemented and simulated at University of Amikom
Yogyakarta  (Amikom).  Amikom  has  an  IT  Directorate  responsible  for  developing  a  web-based  Ticket
Management System (TMS) called Amikom Care that can be accessed at www.care.amikom.ac.id. The users
of this system include work units/directorates, lecturers, students, education personnel, prospective students,
and  the  public.  Users  can  report  issues  by  creating  tickets  within  TMS  Amikom  Care.  Once  a  ticket  is
submitted, it is initially handled by Customer Service (CS) within the respective work unit. If the issue cannot
be resolved at this level, the ticket is escalated to the Team Member (TM) and further, if necessary, to the Head
of Department (HOD). Although TMS Amikom Care is currently operational, no formal quality analysis of the
software  has  been  conducted  to  date.  This  study  has  two  primary  objectives  :  the  first  is  to  evaluate  the
performance and quality of the TMS application at Amikom using the ISO/IEC 25010:2023 standard. And the
second is to determine and prioritize three key characteristics of the ISO/IEC 25010:2023 standard that are
most relevant for TMS evaluation using the  AHP  method. These objectives are designed to provide both a
comprehensive  quality assessment and a focused analysis of critical system characteristics that impact  user
satisfaction and system effectiveness.

2.  Literature Review

The  literature  review  provides  a  foundational  theoretical  framework  to  guide  and  optimize  the
research process. It enables researchers to identify, understand, and adopt established concepts relevant to the
study. In this research, the ISO/IEC 25010 standard serves as the primary model for evaluating software quality.
This model is widely recognized for its comprehensive approach to assessing software product characteristics
and ensuring that critical quality parameters are met during evaluation.

The  ISO/IEC  25010  standard,  first  introduced  in  2011  and  revised  in  2023,  provides  a  detailed
framework  for  evaluating  software  and  system  quality.  It  defines  a  product  quality  model  that  categorizes
essential quality characteristics and their sub-characteristics, which are integral to measuring a system’s ability
to meet functional, performance, and user-specific requirements. Each characteristic reflects a key dimension
of software quality, encompassing aspects like functionality, performance, reliability, and adaptability. These
dimensions ensure that software not only meets technical requirements but also delivers value to its users and
stakeholders under specified conditions. As shown in Figure 1, the product quality model listed in ISO/IEC
25010 consists of eight quality characteristics.

Figure 1 Characteristics and Sub Characteristics of ISO 25010:2023
(Source: https://iso25000.com/)

The  nine  quality  characteristics  outlined  in  ISO/IEC  25010:2023  are  Functional  Suitability,
Performance  Efficiency,  Compatibility,  Interaction  Capability,  Reliability,  Security,  Maintainability,
Flexibility, and Safety. These characteristics collectively form a robust framework for understanding software
quality. The following sections elaborate on each characteristic and its sub-components to clarify their role in
the evaluation process [12].
1)  Functional  Suitability  represents  the  system’s  ability  to  deliver  functions  that  meet  specific  user
requirements under defined conditions. This characteristic emphasizes functional completeness, ensuring
all  necessary  features  are  provided;  functional  correctness,  which  guarantees  accurate  outcomes;  and
functional appropriateness, ensuring the functionality meets its intended purpose efficiently.

2)  Performance  Efficiency  addresses  the  system’s  ability  to  deliver  performance  relative  to  resource
consumption  under  given  conditions.  Sub-characteristics  include  time  behavior  (response  time  and

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   89

latency), resource utilization (efficient use of system resources), and capacity (system’s ability to handle
varying workloads).

4)

3)  Compatibility examines the system’s ability to operate and exchange information with other systems or
products.  It  includes  co-existence,  ensuring  harmonious  operation  within  shared  environments,  and
interoperability, which focuses on effective communication and data exchange between systems.
Interaction  Capability  focuses  on  the  usability  and  user  experience  of  the  system.  It  assesses  how
effectively the product interacts with users through its interface. Sub-characteristics include learnability
(ease of understanding), operability (ease of operation), user error protection (prevention of misuse), and
user  engagement  (satisfaction  and  inclusivity).  This  dimension  ensures  that  the  system  is  accessible,
intuitive, and user-centered.

5)  Reliability  measures  the  product’s  ability  to  operate  consistently  under  specified  conditions  without
failure.  Key  sub-characteristics  include  fault  tolerance  (system  resilience  during  failures),  availability
(operational uptime), and recoverability (ability to restore after a failure).

6)  Security  evaluates  the  extent  to  which  the  system  safeguards  data  and  resources  against  unauthorized
access and threats. It encompasses confidentiality (data privacy), integrity (data accuracy), non-repudiation
(proof of actions), authenticity (verification of identities), and accountability (traceability of actions). This
characteristic is essential for protecting sensitive organizational and user information.

7)  Maintainability highlights the product’s capacity for efficient modification, ensuring adaptability to new
requirements and environments. Sub-characteristics such as modularity (segmented design), reusability
(component  reuse),  modifiability  (ease  of  changes),  and  testability  (ease  of  testing)  facilitate  ongoing
development and maintenance.

8)  Flexibility assesses the system’s ability to adapt to changes in requirements, contexts, or environments. It
includes  adaptability  (adjustments  to  new  conditions),  scalability  (handling  increased  demands),  and
installability (ease of deployment).

9)  Safety  ensures  the  product’s  ability  to  prevent  risks  that  may  harm  human  life,  property,  or  the
environment. This includes hazard warnings, risk identification, and fail-safe mechanisms that minimize
the potential for accidents or failures.

By  incorporating  these  nine  characteristics  and  their  sub-components,  ISO/IEC  25010:2023  provides  a
structured approach to software quality evaluation.

3.  METHOD

3.1  Metode Analytical Hierarchy Process (AHP)

Analytical Hierarchy Process is a decision support model developed by Thomas L. Saaty. This model will
decompose a complex  multicriteria problem into a hierarchical  form by  giving a  value  of how important a
criterion variable is and determining which criteria have the highest priority so that they can affect the results
under certain conditions. Therefore, we  need to know the problem, decision needs and objectives, decision
criteria, sub-criteria, stakeholders and affected groups and alternative actions to be taken [13]. A sample of
AHP Hierarchical tree is shown in Figure 2.

Figure 2. Sample AHP Hierarchical Tree

3.2  Likert Scale (AHP)

This scale is a psychometric scale that is often used in questionnaires. This scale was developed by Rensis

Likert in 1932 to measure people’s attitudes. The Likert scale provides five answers consisting of:

90

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

1: strongly disagree
2: disagree
3: undecided
4: agree
5: strongly agree

For this reason, researchers implemented a Likert scale in this study with the following description (Table 1):

Skor  Likert Scale  Meaning

Tabel 1. Likert Scale Score Calculation

5
4
3
2
1

Excellent
Good
Fair
Poor
Very Poor

Features work very well, responds very quickly without errors
Features work well, responds quickly without errors
Features work well, but there are still things that need to be improved
Features are available but do not work and there are many errors massages
Features does not work at all

4.  RESULTS AND DISCUSSIONS

4.1  AHP Hierarchy Decision Making on ISO/IEC 25010:2023

The  decision  hierarchy  for  the  selected  characteristics  of  the  ISO/IEC  25010:2023  standard  was
established using the Analytic Hierarchy Process (AHP) via an online system. The hierarchy is structured into
multiple levels: Level 0 represents the overarching goal of the evaluation, Level 1 comprises the three selected
characteristics  to  be  prioritized,  and  Level  2  includes  their  corresponding  sub-characteristics,  which  are
assessed through pairwise comparisons. In the AHP framework, each sub-characteristic at Level 2 is compared
in pairs to determine relative importance. The comparisons use a priority scale ranging from 1 to 9, where 1
indicates equal importance, and 9 signifies extreme importance of one sub-characteristic over another. These
pairwise comparisons are processed to generate priority weightings, which reflect the relative significance of
the sub-characteristics and characteristics.

The priority weightings derived from the pairwise comparisons at Level 2 are aggregated to determine
the overall ranking of the characteristics at Level 1. This process ensures a systematic evaluation, providing a
clear understanding of the significance of each characteristic within the context of the ISO/IEC 25010:2023
standard.  The  AHP  decision  hierarchy  results,  as  illustrated  in  Figure  3,  visually  represent  the  relationship
between the goal, the three prioritized characteristics, and their sub-characteristics. The calculated weightings
obtained through this process serve as the basis for subsequent quality measurements and analysis of the TMS
application.

Figure 3. Decision hierarchy result with AHP online system

The decision hierarchy of ISO/IEC 25010:2023 characteristics is determined by inputting 3 previously
determined characteristics into the AHP online system. Level 0 is the Goal; level 1 is the 3 characteristics that
will  be  ranked,  and  level  2  is  the  sub-characteristics  that  will  be  pairwise.  The  AHP  decision  hierarchy  of
ISO/IEC 25010:2023 standard is shown in Figure 3.

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   91

4.2  Analysis of AHP Hierarchy Decision Making Results

The  pairwise  comparisons  provided  by  stakeholders  for  the  sub-characteristics  of  the  ISO/IEC
25010:2023 standard yielded the global priority weights for each sub-characteristic. These weights were used
to  determine  the  overall  priority  of  the  Level  1  characteristics  in  the  decision  hierarchy.  The  results  are
summarized as follows:
1.  Functional Suitability

Among the Functional Suitability sub-characteristics, Functional Appropriateness emerged as the highest
priority, receiving a weight of 20.4%. This indicates its critical role in ensuring that the TMS application
meets user needs and supports task completion effectively. Following this, Functional Correctness was
ranked  second  with  a  weight  of  14.8%,  reflecting  its  importance  in  delivering  accurate  results.  Lastly,
Functional Completeness received the lowest weight of 6.1%, highlighting a relatively lower priority for
including all required functions compared to appropriateness and correctness.

2.  Performance Efficiency

For Performance Efficiency, Time Behaviour was prioritized as the most significant sub-characteristic,
with a weight of 15.2%. This reflects the critical need for the system to respond quickly and efficiently
under defined conditions. In contrast, Capacity and Resource Utilization were equally weighted at 5.9%,
indicating their shared but lower significance compared to Time Behaviour.

3.  Reliability

Within  the  Reliability  characteristic,  Availability  emerged  as  the  top  priority  with  a  weight  of  7.6%,
underscoring  the  importance  of  system  uptime  and  consistent  availability.  Fault  Tolerance  followed
closely with a weight of 7.2%, reflecting its role in maintaining system operation during failure scenarios.
Maturity  ranked  third  with  a  weight  of  6%,  while  Recoverability  was  identified  as  the  lowest  priority
among the Reliability sub-characteristics.

4.3  Overall Priority Ranking of Characteristics

Using  the  global  priority  weights  calculated  through  the  AHP  online  system,  the  three  main

characteristics were ranked as follows:

1.  Functional Suitability – ranked first with a weight of 49.5%, highlighting its critical role in meeting

user expectations and functional needs.

2.  Performance Efficiency – ranked second with a weight of 27%, reflecting the importance of system

performance in terms of response time and resource usage.

3.  Reliability – ranked third with a weight of 23.5%, indicating its significance in ensuring the system

operates consistently and dependably.
The  priority  ranking  analysis  results  are  illustrated  in  Figure  4,  which  visually  represents  the

distribution of weights across the three characteristics.

Figure 4. The results of priority ranking analysis with AHP

Following the prioritization process, researchers conducted further testing of the sub-characteristics

using questionnaires and black box testing. These methods were applied to measure the actual performance
of the TMS application based on user feedback and functional validation, providing a comprehensive
assessment aligned with the ISO/IEC 25010:2023 standard.

4.4  Result Sub-Characteristics Questionnaires and Black Box Testing

We measured the sub-characteristics of the ISO/IEC 25010:2023 standard through systematic black

box testing. Each sub-characteristic was evaluated by testing specific functionality of the TMS application.
1.  Functional  Completeness.  Functional  Completeness  was  assessed  through  black  box  testing,  where  all
existing functions of the TMS application were systematically tested. The evaluation aimed to determine
whether all necessary functions were present and operational. The test revealed that several functions did

92

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

not operate as intended, resulting in a score of 4, which is categorized as good. Despite this positive result,
the findings indicate areas where functionality requires improvement.

2.  Functional  Correctness.  Functional  Correctness  was  measured  using  the  black  box  testing  method,
focusing  on  critical  features  such  as  the  login,  search,  export  to Excel,  and  notification  functions.  The
objective  was  to  verify  whether  the  application  provides  accurate  outputs  with  the  required  level  of
precision.  While  the  test  results  demonstrated  that  the  TMS  application  largely  met  user  expectations,
some functions still require refinement. Consequently, this sub-characteristic also received a score of 4,
placing it in the good category.

3.  Functional  Appropriateness.  Functional  Appropriateness  was  similarly  evaluated  through  black  box
testing by analyzing all website functions to determine whether the system adequately supports users in
achieving  their  tasks  and  goals.  The  evaluation  confirmed  that  the  website  meets  user  expectations  by
providing  the  necessary  facilities  and  tools.  As  a  result,  the  TMS  application  scored  4  for  this  sub-
characteristic, placing it within the good category.

Overall,  these  assessments  highlight  that  while  the  TMS  application  performs  well  in  terms  of
functional  suitability, there remain areas  for improvement  in specific  functionalities. The black box testing
revealed that some functions did not operate as intended, suggesting the need for targeted enhancements to
optimize system performance. Based on the evaluation results, several key areas for improvement have been
identified:

•  Performance Optimization

The Time Behavior sub-characteristic scored 3.700, indicating a need for response time optimization
Recommended actions:
o
o
o

Implement server-side caching to reduce database query times
Optimize database indexes for frequently accessed data
Consider implementing asynchronous processing for ticket updates

•  Functional Enhancement Priorities
  While Functional Suitability scored well (4.369), specific improvements are recommended:

o
o
o

Enhance the ticket categorization system to improve routing efficiency
Implement automated ticket status updates
Develop a knowledge base integration for common issues

•  Reliability Improvements

Despite strong overall reliability (4.619), the following enhancements are suggested:

o
o

Develop a comprehensive disaster recovery plan
Enhance the backup system for improved recoverability

•  User Experience Considerations

Based on user feedback, the following improvements are recommended:

o
o

Enhance the notification system
Improve the mobile responsiveness of the interface

These recommendations are prioritized based on their potential impact on system quality and user
satisfaction. Implementation should be phased, with immediate focus on performance optimization due to its
direct impact on user experience.

4.5  Total Assessment of Characteristics and Sub-Characteristics

After testing and evaluating the three characteristics and their respective sub-characteristics of the
ISO/IEC  25010:2023  standard,  the  total  score  was  calculated  to  determine  the  overall  quality  of  the  TMS
application. The calculations were based on the characteristic weights obtained through the AHP method and
the assessment results for each sub-characteristic, as detailed in Table 2.

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94                   93

Tabel 2. TMS App score calculation result
Assessment
Result

Sub-characteristic

Sub-
characteristic

4.552

Total
Subcategor
ies

Total
Result

Characteristic

Characteristic
Weight

Functional
Suitability

0.495

Functional
completeness

Functional
correctness

Functional
appropriateness

Time behavior

Performance
Efficiency

0.27

Resource utilization

Reliability

0.235

Capacity

Faultlessness

Availability

Fault tolerance

Recoverability

4.123

4.369

2.162

4.431

3.700

4.250

4.333

4.527

5.000

4.750

4.200

4.094

1.106

4.619

1.086

TOTAL

1

TOTAL

4.354

The  evaluation  results  demonstrate  that  Functional  Suitability  played  the  most  significant  role  in
determining the overall quality score of the TMS application, with a weight of 0.495. The sub-characteristics
— Functional Completeness, Functional Correctness, and Functional Appropriateness — achieved an average
score of 4.369, resulting in a weighted contribution of 2.162. This highlights the importance of ensuring that
the system provides accurate, complete, and appropriate functionality to meet user requirements effectively.
Performance  Efficiency,  with  a  weight  of  0.27,  ranked  second  in  priority.  The  sub-characteristics  assessed
included  Time  Behaviour,  Resource  Utilization,  and  Capacity,  achieving  an  average  score  of  4.094  and
contributing  1.106  to  the  total  score.  Among  these,  Time  Behaviour  recorded  the  lowest  individual
performance, signalling the need for optimization to improve response time and overall system efficiency.

The Reliability characteristic, weighted at 0.235, performed well overall, with sub-characteristics such
as  Faultlessness,  Availability,  Fault  Tolerance,  and  Recoverability  achieving  the  highest  average  score  of
4.619.  Availability  stood  out  with  a  perfect  score  of  5.000,  underscoring  the  system's  strong  capability  to
remain operational and accessible without interruptions.

The  final  evaluation  yielded  a  total  score  of  4.354,  placing  the  TMS  application  in  the  “Good”
category. This result reflects the system’s overall effectiveness in meeting the critical quality requirements of
functionality, performance, and reliability, as outlined by the ISO/IEC 25010:2023 standard. Overall, while
Functional Suitability emerged as the most influential factor due to its high weight and consistent performance
across  sub-characteristics,  Performance  Efficiency  revealed  room  for  improvement,  particularly  in  Time
Behaviour.  The  Reliability  characteristic  demonstrated  strong  results,  especially  in  Availability,  further
enhancing  the  overall  quality.  These  findings  provide  valuable  insights  into  the  strengths  and  areas  for
improvement  in  the  TMS  application,  emphasizing  the  need  for  targeted  enhancements  to  optimize  system
performance.

5.  CONCLUSION

In this study, the prioritization of three selected characteristics from the ISO/IEC 25010:2023 standard
was conducted using the Analytic Hierarchy Process method. The evaluation of each sub-characteristic was
carried  out  through  a  combination  of  questionnaires  and  black  box  testing.  The  measurement  results  were
analyzed  using  a  Likert  scale  to  assign  scores  to  each  sub-characteristic.  The  scores  for  individual  sub-
characteristics were averaged and weighted based on the characteristic prioritization derived from the  AHP
method.  This  process  ensured  a  systematic  and  data-driven  evaluation  of  the  software  quality.  The  results
revealed that the Ticket Management System application, evaluated in the case study at University of Amikom

94

Ariningsih, et al. / INTECHNO: Inf. Tech. J., Vol. 6, No. 2 December 2024 :  86 – 94

Yogyakarta, achieved a score of 4.354. This score indicates that the TMS application falls within the “good”
category, reflecting a positive overall quality while highlighting areas for potential improvement.

REFERENCES
[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

[11]

[12]

[13]

R. S. Mission, “Multi-channel support and ticketing interface for online support management system platforms,”  Int. J. Appl.
Sci. Eng., vol. 18, no. 4(Special Issue), pp. 1–9, 2021, doi: 10.6703/IJASE.202106_18(4).006.
M. Al-Emran and H. Al Chalabi, “‘Developing an IT Help Desk Troubleshooter Expert System for diagnosing and solving IT
Problems,’” BCS Learning & Development, Feb. 2015. doi: 10.14236/ewic/bcsme2014.16.
F.  Gohil  and  M.  Vikash  Kumar,  “Ticketing  System  the  Creative  Commons  Attribution  License  (CC  BY  4.0).”  [Online].
Available: http://creativecommons.org/licenses/by/4.0
S. Fuchs, C. Drieschner, and H. Wittges, “Improving Support Ticket Systems Using Machine Learning: A Literature Review,”
in Proceedings of the Annual Hawaii International Conference on System Sciences, IEEE Computer Society, 2022, pp. 1893–
1902. doi: 10.24251/hicss.2022.238.
K. D. Aglibar and N. Rodelas, “Impact of Critical and Auto Ticket: Analysis for Management and Workers Productivity in using
a Ticketing System,” Int. J. Comput. Sci. Res., vol. 6, pp. 988–1004, Jan. 2022, doi: 10.25147/ijcsr.2017.001.1.84.
S. I. Adam, J. H. Moedjahedy, and O. Lengkong, “Pengembangan IT Helpdesk Ticketing Sistem Berbasis Web di Universitas
Klabat Development of Web-based IT Helpdesk Ticketing System at Universitas Klabat,” Cogito Smart J. |, vol. 6, no. 2, 2020.
D.  Yunadi,  N.  Sulistiyowati,  and  A.  A.  Ridho,  “Analisis  Dan  Implementasi  Sistem  Ticketing  Helpdesk  Pada  Universitas
Singaperbangsa Karawang,” 2020.
F. Al-Hawari and H. Barham, “A machine learning based help desk system for IT service management,” J. King Saud Univ. -
Comput. Inf. Sci., vol. 33, no. 6, pp. 702–718, Jul. 2021, doi: 10.1016/J.JKSUCI.2019.04.001.
A. Yulianty and A. Kurniawati, “Quality Analysis of Bios Portal Website at Banking Companies Using ISO / IEC 25010:2011
Method,” Int. Res. J. Adv. Eng. Sci., vol. 6, no. 2, pp. 11–16, 2021.
M.  Mulyawan,  I.  N.  S.  Kumara,  A.  Swamardika,  and  K.  Saputra,  “Kualitas  Sistem  Informasi  Berdasarkan  ISO/IEC  25010:
Literature Review,” Maj. Ilm. Teknol. Elektro, vol. 20, p. 15, Mar. 2021, doi: 10.24843/MITE.2021.v20i01.P02.
A.  Arga  Pratama  and  A.  B.  Mutiara,  “Software  Quality  Analysis  for  Halodoc  Application  using  ISO  25010:2011,”  2021.
[Online]. Available: www.ijacsa.thesai.org
ISO/IEC25010,  “Systems  and  software  engineering-Systems  and  software  Quality  Requirements  and  Evaluation  (SQuaRE)-
Product quality model,” Switzerland, vol. 2023, 2023.
T.  L.  Saaty,  “Decision  making  with  the  Analytic  Hierarchy  Process,”  Sci.  Iran.,  vol.  9,  no.  3,  pp.  215–229,  2002,  doi:
10.1504/ijssci.2008.017590.

