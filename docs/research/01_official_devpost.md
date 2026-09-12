# AI Builders Hackathon 2026 — 공식 Devpost 전수 조사

- 조사 일시: 2026-09-15 (KST)
- 대상: https://ai-builders-hackathon-2026.devpost.com/
- 주최: Open Source Connect (OSC) / 문의 이메일 `osconnect011@gmail.com`
- Devpost 내부 challenge_id: `30452`
- 태그: `OSC`, `Machine Learning/AI`, `Open Ended`, `Beginner Friendly`, `Online`, `Public`

---

## 0. 크롤링 결과 요약 (접근 가능 여부)

| 경로 | 상태 | 비고 |
|---|---|---|
| `/` (Overview) | 200 | 전체 본문 확보 |
| `/rules` | 200 | 전체 본문 확보 |
| `/details/dates` (Schedule) | 200 | 전체 확보 |
| `/updates` + 개별 업데이트 9건 | 200 | 전문 확보 |
| `/forum_topics` + 개별 스레드 10건 | 200 | 전문 확보 |
| `/project-gallery`, `/submissions/search` | 200 | **"The hackathon managers haven't published this gallery yet"** — 갤러리 미공개 |
| `/participants` | 200 | **"Please log in to browse this hackathon's participants."** — 로그인 필요 |
| `/resources` | 200 | **본문 비어 있음 (리소스 미등록)** |
| `/details`, `/judges`, `/prizes` | 404 | 별도 페이지 없음 (모두 Overview에 인라인) |

> 중요: **제출작 갤러리가 비공개**라 현재 제출 프로젝트 목록·개수를 확인할 수 없습니다. 경쟁작 파악은 불가.

---

## 1. 공식 규정 및 참가 자격

출처: https://ai-builders-hackathon-2026.devpost.com/rules

### 1-1. Dates (규정 페이지 원문)

> Registration Opens: 16 June 2026
> Hackathon Begins: 21 August 2026
> Project Submission Deadline: 15 September 2026
> Judging Period: 16 September 2026 - 20 September 2026
> Winners Announcement: September 2026
> Participants will have 25 days to design, build, test, and submit their AI-powered solutions.

### 1-2. Eligibility (규정 페이지 원문)

> The AI Builders Hackathon is open to participants from around the world.
>
> Eligible participants include:
> • Students and recent graduates
> • Software developers and engineers
> • AI/ML practitioners and researchers
> • Designers and product builders
> • Startup founders and entrepreneurs
> • Open-source contributors and technology enthusiasts
>
> Participants may compete individually or as a team.
>
> No prior hackathon experience is required. Whether you are building your first AI application or deploying advanced multi-agent systems, you are welcome to participate.

### 1-3. Overview 페이지의 "Who can participate" 박스 (원문)

> Above legal age of majority in country of residence
> Students only
> Companies/professional organizations excluded from participation
> All countries/territories, excluding standard exceptions

> **모순 주의**: Overview 박스는 "Students only", 규정 페이지는 "open to participants from around the world"입니다. 이 모순은 포럼에서 주최측(Manager)이 **명시적으로 해소**했습니다 (§8 참조): "The 'Students only' message is a display issue on the registration page."

### 1-4. Project and Submission Requirements (규정 페이지 원문)

> All submissions must be created during the hackathon period and align with the theme of Artificial Intelligence, Agentic AI, or Intelligent Systems.
>
> Your submission must include:
> • A project title and description
> • A publicly accessible source code repository (GitHub, GitLab, etc.)
> • A demo video (3–5 minutes recommended)
> • Documentation explaining the problem, solution, and technology used
> • Team member details
>
> Projects may include:
> • AI Agents and Multi-Agent Systems
> • AI Assistants and Copilots
> • Workflow Automation Solutions
> • AI for Education, Healthcare, Finance, Research, or Productivity
> • Developer Tools powered by AI
> • Innovative Generative AI Applications

### 1-5. 규정 페이지의 Prizes / Judging 섹션 (원문)

> Prizes
> TBD

> Judging Criteria and Winner Selection
> Judging will consider:
> • Innovation and originality
> • Technical implementation
> • Real-world impact
> • User experience and design
> • Scalability and feasibility
>
> Participants are encouraged to build solutions that address meaningful challenges and demonstrate how AI can create measurable value for individuals, businesses, or communities.

> 참고: 규정 페이지의 5개 항목에는 Overview의 가중치 배분에 없는 **"Scalability and feasibility(확장성·실현 가능성)"** 가 포함되어 있습니다. 즉 심사위원 안내에는 확장성 항목이 살아 있을 가능성이 높습니다.

### 1-6. 라이선스 / 기존 코드 / 팀 규모

- **라이선스 요구 조항 없음** (오픈소스 라이선스 명시 요구 문구가 사이트 어디에도 없음).
- **기존 코드 사용 규정**: 명문 규정은 `All submissions must be created during the hackathon period` 한 줄뿐. 세부 예외 규정 없음. 포럼에 3건의 질문이 올라왔으나 **주최측 답변 없음** (§8).
- **팀 규모 제한**: 사이트 어디에도 최대 인원 명시 없음. 포럼 질문("Is a team of three participants allowed, and is there a maximum team size?")에도 **답변 없음**. 규정상 `Participants may compete individually or as a team.` 뿐.
- Devpost 표준 최대 팀 인원(별도 설정 없을 시 통상 제한 없음/플랫폼 기본)을 따르는 것으로 보임.

---

## 2. 제출 요건 (Overview 페이지 원문 — 가장 상세)

출처: https://ai-builders-hackathon-2026.devpost.com/

### What to Build

> Build an AI product that solves a real problem.
> We encourage teams to focus on creating products that people would genuinely want to use beyond the hackathon.
> Your project may be an AI application, autonomous agent, multi-agent system, developer tool, workflow automation platform, research assistant, productivity tool, education solution, healthcare application, business software, creative tool, or an entirely new category of AI-powered product.

### What to Submit

> To complete your participation in the AI Builders Hackathon, each team must submit the following materials before the submission deadline.
>
> **1. Project Submission Form**
> Complete the official submission form with your project details, including team information, project name, description, and all required links.
>
> **2. Working Product**
> Your submission must include a functional prototype, application, platform, agent, or software solution that demonstrates the core capabilities of your project. Judges should be able to understand and evaluate how your product works.
>
> **3. Source Code**
> Provide a public GitHub repository containing the source code for your project. The repository should include clear documentation, setup instructions, and any information required to review your work.
>
> **4. Demo Video**
> Submit a video of up to 5 minutes showcasing your project. The video should clearly explain:
> • The problem being solved
> • How the solution works
> • Key features and functionality
> • The role of AI within the product
> • A live demonstration of the product in action
>
> **5. Presentation Deck**
> Submit a presentation deck of up to 10 slides covering:
> • Problem Statement
> • Solution Overview
> • Target Users
> • Product Features
> • Technical Architecture
> • AI Technologies Used
> • Impact and Value Proposition
> • Future Roadmap

### Get started (원문)

> 1. Register for the AI Builders Hackathon.
> 2. Form your team or participate individually.
> 3. Explore the challenge themes, resources, and sponsor technologies.
> 4. Brainstorm ideas and identify a real-world problem to solve.
> 5. Build an AI-powered solution, agent, workflow, or application.
> 6. Submit your project before the deadline with:
> Project description / Demo video / Source code repository / Presentation or documentation
> 7. Present your project to judges and compete for prizes, recognition, and opportunities.

### 영상 길이 규정 정리 (두 페이지 간 차이)

| 출처 | 문구 |
|---|---|
| Overview | "a video of **up to 5 minutes**" |
| Rules | "A demo video (**3–5 minutes recommended**)" |

→ **5분 초과 금지, 3~5분 권장**으로 해석하는 것이 안전.

### Devpost 폼 필드 (로그인 필요로 직접 확인 불가)

제출 폼 자체는 로그인 후에만 노출됩니다. 확인된 범위:
- Devpost 표준 제출 폼 사용 (업데이트 공지: "One person from each team will **Enter a Submission**").
- 팀원은 **Devpost 계정 생성 시 사용한 이메일 주소**로 추가해야 함 (§7 45957 공지).
- **슬라이드 덱 전용 업로드 필드가 존재하는지 불명확** — 포럼에 "Where to upload slides?" 질문이 2건 있으나 주최측 답변 없음 (§8). 참가자들은 "repo에 넣고 링크"를 대안으로 논의 중.
- 마감 전까지 **계속 수정 가능**: "you can keep updating your project until the deadline."

---

## 3. 심사 기준 (Overview 원문, 가중치 포함)

출처: https://ai-builders-hackathon-2026.devpost.com/

> **Innovation & Creativity (20%)**
> Judges will assess the originality and uniqueness of the idea, including how creatively AI technologies are applied to solve a problem.
>
> **Technical Implementation (25%)**
> Projects will be evaluated on the quality of their technical execution, including the design and implementation of AI models, agents, workflows, and system architecture.
>
> **Problem Solving & Impact (25%)**
> Judges will evaluate how well the solution addresses user needs, its practical applicability, potential real-world impact, and the clarity with which benefits and outcomes are demonstrated.
>
> **User Experience & Design (15%)**
> Judges will assess the quality of the user interface, ease of use, workflow design, accessibility considerations, and the overall polish and usability of the product.
>
> **Presentation & Demo (15%)**
> Teams will be evaluated on how effectively they communicate their project vision, solution, and technical decisions.

합계 100%. **Technical Implementation + Problem Solving & Impact = 50%** 가 최대 비중.

---

## 4. 상금 및 트랙

출처: https://ai-builders-hackathon-2026.devpost.com/ (Prizes 섹션)

> **$ 33,900 + in prizes** / "+ other prizes"

| 상 | 내용 | 수상자 수 |
|---|---|---|
| **Best SaaS Product** | `$ 4,000 in cash` | 1 winner |
| **Top IDEAS will get Exposure** | (별도 설명 없음) | — |
| **NexFellow Founder's Choice Award** | "3 Months of NexFellow Founder Plan for the most compelling AI product with strong user value and founder potential." | 1 winner |
| **NexFellow Product Excellence Award** | "2 Months of NexFellow Founder Plan for the best executed product with excellent usability, technical quality, and real world value." | 1 winner |
| **NexFellow Innovation Award** | "1 Month of NexFellow Founder Plan for the most creative and technically innovative use of AI." | 1 winner |
| **Tin Computer Credits** | `$ 299 in cash` | **100 winners** |

### Tin Computer Credits 원문

> The first 100 eligible AI Builders Hackathon teams can each claim $299 in Tin Computer credits, equivalent to one month of the Tin Computer Growth Plan. Credits are available exclusively to official participating teams, with one claim per team. No credit card, payment, paperwork, or ongoing commitment is required.
>
> Teams can claim their credits, and the claim window will remain open for 60 days from the date the page goes live. Credits are available on a first come, first served basis and are limited to the first 100 eligible teams.

> 금액 구성 추정: $4,000(현금) + $299 × 100 = $29,900 → 합계 $33,900. 즉 **실제 현금 상금은 $4,000 단 하나**이고 나머지는 스폰서 크레딧/구독권입니다.

### Devpost Achievements

> Submitting to this hackathon could earn you: ... level Judges

(배지 이미지 기반, 텍스트 정보 최소)

### 참가 증서

> Please note that Certificates of Participation will be awarded to all eligible participants who meet the participation requirements.
> (출처: /updates/45816)

---

## 5. 일정 (타임존 포함)

출처: https://ai-builders-hackathon-2026.devpost.com/details/dates

| Period | Begins | Ends |
|---|---|---|
| **Submissions** | August 21 at 12:00am EDT | **September 15 at 11:00pm EDT** |
| **Judging** | September 16 at 9:00am EDT | September 20 at 9:00pm EDT |
| **Winners Announced** | September 25 at 9:00am EDT | — |

- 헤더 표기: `Deadline: Sep 15, 2026 @ 11:00pm EDT`
- **KST 환산: 2026-09-16 12:00 (정오)** — EDT(UTC-4) + 13시간.
- 규정 페이지의 "Winners Announcement: September 2026"과 스케줄의 "September 25" 중 **스케줄(9/25 9:00am EDT)** 이 더 구체적.
- 규정 페이지는 "25 days to build"라고 하나, 8/21~9/15는 실제 26일.

---

## 6. 심사위원 (20명, Overview 원문)

| 이름 | 소속/직함 |
|---|---|
| Disha Patel | Software Engineer, Apple |
| Pulkit Arya | Founding Engineer, Pointer |
| Ishan Shah | Staff Software Engineer, Paypal |
| Iryna Havryliuk | Sr. Product Manager at CareerPlug |
| Lakshmi Supriya Namana | Product Founder of FlowOps at WebCreators UK |
| Anudeep Reddy Mutyala | AI Engineer, Themachinist.org |
| Gayathri Chilukala | Software Engineer, Microsoft |
| Kunal Jain | Research Engineer - TMD Labs, NYU Tandon |
| Aakanksha Joshi | Senior AI Solution Architect, IBM |
| Nanda Kishore Kande | Sr. Software Engineer, Visa |
| Krystal Phan | Senior Product Manager, Global Chamber |
| Udaya Bhaskar Vemuri | Sr. Security Analyst at Corteva Agriscience |
| Vasuki Uday Kiran Vudathala | Staff Performance Engineer at ServiceNow |
| Sourav Sarkar | Sr. Worldwide Specialist Solutions Architect at AWS |
| Lakshmi Vidya Peri | Board of Director at TMMi America, Ex-Principal Engineer at Dell Technologies |
| Ashish Tripathi | Founder at GraphicNote |
| Shania Rasheed Nalagath | Sr. Product Manager at Microsoft |
| Aniruddha Nikam | Sr. Product Manager at TechCareers |
| Gouthami Boinpally | Sr. Product Manager at Omnissa |
| Nilesh Dhage | Dr Product Management at Fidelity Investments |

> 상세 bio는 제공되지 않고 이름 + 직함만 표기됩니다.

### 심사위원 구성 분석 (중요)

- **Product Manager 직함이 7명** (Iryna, Krystal, Shania, Aniruddha, Gouthami, Nilesh, + Product Founder Lakshmi Supriya) = **35%**.
- 엔지니어링 직함 약 9명 (Apple/PayPal/Microsoft/Visa/AWS/IBM/Dell/ServiceNow 등 대기업 중심).
- 보안 분석가 1명(Corteva), 성능 엔지니어 1명(ServiceNow), QA/TMMi 임원 1명 → **보안·성능·품질 관점 평가자 존재**.
- 즉 **딥러닝 연구 깊이보다 "제품 완성도 + 아키텍처 + 비즈니스 임팩트"** 가 먹히는 심사진 구성.

---

## 7. 주최측 공지 전문 (Updates, 9건)

출처: https://ai-builders-hackathon-2026.devpost.com/updates

### (1) 약 16시간 전 — "AI Builders Hackathon participants, this opportunity is for you!" (`/updates/46412`)

> Dear Participant,
> We're excited to share one more way you can be part of the NexFellow Fellowship .
> If you're planning to apply, we'd love to know which track you're interested in.
> The fellowship offers four tracks:
> SaaS & Products / AI & Agents / Developer & Open Source / Web3 & Emerging Tech
> Here's what you can do:
> 1. Like & comment on the official fellowship announcement with the track you're planning to choose. For example: "Interested in AI & Agents track"
> 2. Repost the announcement and share NexFellow Fellowship with your network.
> 3. Encourage other builders to apply and let them know that participation is completely free for everyone .
> This is a great opportunity to build a real product, learn from industry leaders, receive meaningful feedback, connect with global builders, and showcase your work.
> Official Fellowship Announcement: Click here
> Your repost could help another builder discover an opportunity that changes their journey.
> Let's help more builders build something meaningful.

### (2) 2일 전 — "Final call for submissions" (`/updates/44787`)

> There are only 3 days left to complete your submission for AI Builders Hackathon .

### (3) 4일 전 — "AI Builders Hackathon participants, this opportunity is for you!" (`/updates/46369`)

> Dear Participant,
> If you're building an AI product, working on a startup idea, or simply love turning ideas into real products, you should definitely apply for NexFellow Fellowship .
> Why participate?
> Build a real product and take your idea beyond a hackathon
> Learn from industry leaders and experienced builders
> Get meaningful mentor and peer feedback
> Improve, iterate, and actually ship
> Showcase your work through Demo Day
> Get access to exclusive perks and opportunities from partner companies
> The fellowship will select 100 builders for an intensive 8 week global experience.
> The journey is simple: Learn → Build → Get Feedback → Ship
> If you're serious about building something meaningful, don't miss your chance to apply.
> 🔗 Apply for NexFellow Fellowship: https://fellowship.nexfellow.com/
> Your hackathon project could be the beginning of something much bigger.

### (4) 12일 전 — "Join the AI Builders Hackathon Discord" (`/updates/46223`)

> Dear Participant,
> We're excited to have you as part of the AI Builders Hackathon.
> **Joining our Discord server is mandatory for all participants**, as all important hackathon updates, announcements, discussions, and community interactions will happen there.
> Once you join, please complete these two steps:
> 1. Introduce yourself: Go to # introductions and share a short introduction along with your country name.
> 2. Join the conversation: Head over to # ai-builders-hackathon to connect with other participants, discuss ideas, ask questions, and stay updated throughout the hackathon.
> We have also announced half of our judges team on LinkedIn . Please support the announcement by liking and commenting on the post. Your engagement helps us give our judges and the hackathon greater visibility.
> Please make sure to join Discord and complete your introduction as soon as possible.
> Best regards, AI Builders Hackathon Team

> ⚠️ **"Discord 가입은 모든 참가자에게 필수(mandatory)"** — 사실상 제출 전 체크리스트 항목.

### (5) 23일 전 — "Welcome Algoverse as an official sponsor!" (`/updates/46003`)

> We're happy to share an exciting opportunity from our sponsor, Algoverse , a leading AI research program for college students interested in publishing at Tier One AI conferences.
> This Fall, Algoverse is inviting talented students to work alongside Ph.D. and industry researchers from OpenAI, Anthropic, Google DeepMind, Meta, Stanford, and UC Berkeley to develop and publish novel AI research at conferences such as NeurIPS, ICLR, and ICML .
> Algoverse teams report an average 70% acceptance rate on the papers they submit, and two students were admitted to Anthropic's Fellows program based on the strength of their research.
> The program runs for 12 weeks and is designed to fit alongside a full course load. ...
> Application Details
> • Rolling admissions are currently open for the Fall cohort
> • Program discounts are available
> • Merit based and financial aid scholarships are available
> • Application deadline: Sunday, August 23 at 11:59 PM PT
> • Learn more: Click here
> • Questions: admissions@algoverse.us

### (6) 24일 전 — "Welcome NexFellow as an official sponsor!" (`/updates/45995`)

> We're excited to welcome NexFellow as an official sponsor of the AI Builders Hackathon!
> Building a great AI product is only half the journey. The real challenge is knowing whether people actually want to use it.
> That's where NexFellow comes in.
> NexFellow connects builders with experienced people who provide honest, actionable product feedback so founders can validate ideas, improve their products, and launch faster.
> For AI Builders Hackathon participants, this means more than just building a prototype. It's an opportunity to get real feedback, learn from experienced builders, and continue improving your product beyond the hackathon.
> We're excited to have NexFellow supporting the builders who are turning ambitious AI ideas into products people actually want.
> Read & Like LinkedIn Post: Click here

### (7) 25일 전 — "Get setup with Devpost for AI Builders Hackathon" (`/updates/45957`)

> Dear Participant,
> We want to share some important instructions for this weekend. We're using Devpost to showcase all your projects and support the judging.
> You need to register now and submit your projects before the deadline (**Tue Sep 15, 2026 at 11:00 PM EDT**), both at this link: Click here
> Have **EVERY person on your team** go to the link above and click Register for this hackathon. (You must all create Devpost accounts.)
> **One person from each team will Enter a Submission** (which is a button you'll see after you Register). Where it asks you to add your teammates' email addresses, make sure to use the **same ones they used to create their Devpost accounts**.
> Submit early and include as much information as you can, so you won't be rushed toward the end. And remember, **you can keep updating your project until the deadline**.
> Like & comment on our Hackathon Announcement post: Click here
> That's it for now, happy hacking!

### (8) 약 1개월 전 — "Join Our Discord Community" (`/updates/45816`)

> Dear Participant,
> Thank you for registering for the AI Builders Hackathon!
> As the next step, please join our Discord Server to stay updated with all hackathon announcements, connect with participants, and receive support throughout the event.
> Join our Discord Server: Click here
> Once you've joined, please:
> Introduce yourself in the introduction channel and mention that you're joining from the AI Builders Hackathon so our team can welcome you.
> Use the #ai-builders-hackathon channel to find teammates, discuss ideas, ask questions, and collaborate with other participants.
> Invite your friends to participate as well. We have something exciting planned for all participants, so don't let them miss out!
> **Please note that Certificates of Participation will be awarded to all eligible participants who meet the participation requirements.**
> We're looking forward to seeing you in the Discord community and can't wait to see what you'll build!
> Questions? If you have any questions about the hackathon, please post on the discussion forum .

### (9) 3개월 전 — "Your Next Startup Could Begin at This Hackathon." (`/updates/44984`)

> Hi Builder,
> We hope you're as excited as we are because AI Builders Hackathon is just around the corner!
> Now is the perfect time to finalize your team, brainstorm ideas, and get ready to build. This isn't just another hackathon. It's a builder-first experience designed for people who want to create real AI products, solve meaningful problems, and collaborate with ambitious innovators from around the world.
> If you're passionate about startups, AI, or building products that people love, you're in the right place.
> We're also expanding our global community and are currently looking for Core Team Members from North America and Africa who are passionate about growing developer communities and driving innovation. ...
> To learn more about **Open Source Connect** and what we're building, follow our LinkedIn page ...
> If you have any questions, feel free to reach out to us anytime at **hello@osconnect.org** .
> We can't wait to see what you build. See you at the hackathon!

---

## 8. 포럼/디스커션 전체 (10개 스레드)

출처: https://ai-builders-hackathon-2026.devpost.com/forum_topics

> **핵심 관찰: 주최측(Manager) 답변은 전체 10개 스레드 중 단 1건뿐입니다.** 나머지 규정 관련 질문(기존 코드, 팀 규모, 슬라이드 업로드 위치, 미성년자 동의, 비공개 레포)은 **전부 미응답** 상태.

### (1) "Eligibility criteria is confusing" (`/forum_topics/44559`, 약 2개월 전, 4 comments) — **유일한 주최측 답변**

**Damon Bree:**
> Eligible participants include: • Students and recent graduates • Software developers and engineers • AI/ML practitioners and researchers • Designers and product builders • Startup founders and entrepreneurs • Open-source contributors and technology enthusiasts
> __
> I'm not a student, I'm an Entrepreneur. But when I go to join it says "Students only" which means I don't qualify.

**melissahelen78-alt Markwell:**
> The start dates also don't match. The current schedule page says submissions run from August 10, 2026 at 9:00 a.m. EDT through August 25 at 10:00 p.m. EDT. But the rules page says the hackathon begins August 21 and that participants have only five days to build.

**Deependra Gaur (Manager) — 공식 답변:**
> Yes, you're absolutely eligible! The "Students only" message is a display issue on the registration page. Entrepreneurs, founders, developers, researchers, and all other eligible participants listed are welcome to join.

**FritzAnibas Garcia Anibas:**
> Is a team of three participants allowed, and is there a maximum team size?  → **미응답**
> Also the discord link isnt adviable

### (2) "Discord server or communication platform for hackathon?" (`/forum_topics/44603`, 0 comments)

> Is there any discord server or communication platform for participants to communicate with eachother for the hackathon?

### (3) "Questions regarding competition entry criteria" (`/forum_topics/44624`, 0 comments)

> I am a high school student participant. I registered for AI Builders Hackathon and provided my real age during registration. I would like to confirm whether there are any additional requirements for participants under 18, such as parental consent. Thank you.  → **미응답**

### (4) "Discord Server Invalid" (`/forum_topics/44715`, 1 comment)

> The link to the Discord server is invalid
> (댓글) Is their a link to the discord, because I can't join it?

### (5) "About the public GitHub repository requirement" (`/forum_topics/44732`, 0 comments) — **중요**

> Hello! I have a question regarding the source code submission requirement.
> Since the hackathon emphasizes building real AI products that people could actually use beyond the event, I'm considering developing my project as a product that could continue evolving after the hackathon.
> With that in mind, I'm a little hesitant to make the entire source code publicly available, particularly if the project contains implementation details that could become part of a future commercial product.
> Would it be possible to submit a live, fully functional demo instead of a public GitHub repository, along with detailed technical documentation explaining the architecture, AI components, and how the system works?
> I completely understand the need for judges to verify that the project is functional and genuinely built by the participants. I'm just wondering whether there is an option that allows teams to demonstrate the technical work while still protecting potentially proprietary code.
> → **미응답. 즉 "public GitHub repo"는 예외 없이 필수로 간주해야 함.**

### (6) "Questions about eligibility" (`/forum_topics/44785`, 0 comments) — **기존 코드 관련**

> 1) How crucial is timing? I started my project before I found your hackathon, but I didn't post it anywhere yet, and time wise it could reach current point within provided time, and I am still working on it. May I take part if I started earlier?
> 2) How crucial is AI aspect? My program is about automating Data Analysis - it makes EDA that usually takes a lot of time to do, in a few seconds. ... But, for now, I haven't implemented LLM or similar things.
> → **미응답**

### (7) "The Project creating time question" (`/forum_topics/45000`, 17일 전, 0 comments)

> Hi, I got a project, and I have already realised some front-end parts, but the main core AI-related part will be realised during this hackathon competition time. Is that acceptable? thank you
> → **미응답**

### (8) "Presentation" (`/forum_topics/45157`, 6일 전, 2 comments) — **슬라이드 제출 위치 이슈**

> where exactly do i upload my powerpoint presentation? (ps. this is my first time )
>
> (MattCremeens Cremeens, 2일 전) I just posted this question myself without seeing this one. Wondering the same thing.
> (MattCremeens Cremeens, 2일 전) If we don't get an answer soon, I might just put it into my repo and link to it.
> → **주최측 미응답**

### (9) "Eligibility confirmation for our new Santé AI build" (`/forum_topics/45165`, 5일 전, 0 comments)

> Hi! We need a quick eligibility confirmation.
> We are building Santé: Adaptive Week, a new AI system under our existing Santé women's wellness brand. An earlier Santé prototype exists, but we are not submitting it unchanged.
> The hackathon project will introduce a newly built AI workflow that adapts a woman's weekly wellness plan using her daily capacity, completed sessions and feedback, with deterministic safety limits. We will clearly document everything created during the hackathon and separate it from the earlier foundation.
> Would this qualify as a new hackathon submission if the submitted and judged system is built during the event? We can maintain it in a dedicated repository with a transparent changelog.
> → **미응답**

### (10) "Slides" (`/forum_topics/45206`, 2일 전, 0 comments)

> Where to upload slides?
> → **미응답**

---

## 9. 스폰서 및 파트너

출처: Overview "Hackathon Sponsors" 섹션 + Updates

| 스폰서 | URL | 역할 |
|---|---|---|
| **NexFellow** | https://www.nexfellow.com/ (펠로십: https://fellowship.nexfellow.com/) | 3개 상(Founder's Choice / Product Excellence / Innovation) 제공. 빌더 ↔ 리뷰어 매칭 제품 피드백 플랫폼. 24시간 내 응답, 제출당 10+ 리뷰, 3,000+ 활성 리뷰어를 표방. 무료 티어 30 크레딧. |
| **Algoverse** | https://algoverseairesearch.org/ | 대학생 AI 연구 프로그램 (NeurIPS/ICLR/ICML 논문 출판 지원). 상금 제공 아님 — 기회 제공형 스폰서. |
| **Tin Computer** | https://tin.computer/ | $299 크레딧 × 100팀. "open-source marketing system built for coding agents", MCP 서버로 연동, Apache 2.0, Docker 셀프호스팅. GSC/GitHub/Stripe/애널리틱스 연동. |
| **Sylus AI** | https://sylusai.com/ | 로고만 게시(상금 항목 없음). AI 소셜미디어 자동화 플랫폼. |
| **Open Source Connect (OSC)** | hello@osconnect.org / osconnect011@gmail.com | 주최 커뮤니티. Devpost 태그에 `OSC` 포함. |
| **Devpost** | — | 제출·심사 플랫폼 |

### "반드시 X 도구를 써야 한다"는 요구사항: **없음**

사이트 전체에서 특정 스폰서 SDK/API 사용을 의무화하는 문구는 **존재하지 않습니다**. 유일한 강제 사항은 **Discord 가입(mandatory)** 입니다.
단, Overview의 Get started 4단계에 `Explore the challenge themes, resources, and **sponsor technologies**.` 문구가 있어 **스폰서 기술 활용은 권장(가점 가능성)** 수준입니다.
`/resources` 페이지는 **비어 있음** → 지정 리소스/크레딧 배포 목록 없음.

### Discord

- 해커톤 전용 서버 초대: `https://discord.com/invite/umEXASsAev` → **유효**. 서버명 **"Open Source Connect"**, 약 2,607명 멤버 (2026-09-15 확인).
- 푸터의 `https://discord.com/invite/HP4BhW3hnp` 는 Devpost 공식 서버(해커톤과 무관).
- 채널: `#introductions`, `#ai-builders-hackathon`

---

## 10. 참가자·제출작 현황

- **등록 참가자: 3,403명** (Overview 헤더 및 네비게이션 "Participants (3403)", 2026-09-15 기준)
- **제출작 수: 확인 불가.** `/project-gallery` 및 `/submissions/search` 모두:
  > "The hackathon managers haven't published this gallery yet, but hang tight!"
  갤러리가 **미공개** 상태라 현재 제출 프로젝트 목록·개수·기술스택을 전혀 볼 수 없습니다.
- `/participants` 는 로그인 필요:
  > "Please log in to browse this hackathon's participants."

### 경쟁 강도 추정

- Discord 서버 멤버 2,607명 vs 등록 3,403명 → 실제 활동 인원은 등록의 상당 부분.
- 일반적인 대형 온라인 해커톤 제출 전환율(등록 대비 5~15%)을 적용하면 **제출작은 대략 170~500건** 규모로 추정. (추정치, 검증 불가)
- 상금 구조상 **현금 상(Best SaaS Product $4,000)은 단 1개**이므로 최상위 1건 경쟁이 매우 치열. 반면 **Tin 크레딧은 선착순 100팀**이라 사실상 별도 트랙.

---

## 11. 심사위원이 원하는 것에 대한 숨은 힌트 (테마 문구 원문)

Overview "About the challenge" 전문 (가장 중요한 톤 지표):

> **The world doesn't need another AI demo.**
>
> Every day, thousands of AI projects are launched. Most never move beyond a prototype, a landing page, or a collection of prompts. What the world truly needs are AI products that solve real problems, save time, create value, and earn a place in people's daily lives.
>
> AI Builders Hackathon is designed for builders who want to go beyond experimentation and create software that matters.
>
> Over the course of the challenge, participants will design, build, and launch AI-powered applications, agents, workflows, and platforms that address real-world needs. Whether you're creating a productivity tool, developer platform, research assistant, business automation system, education solution, healthcare application, or an entirely new category of software, the focus remains the same: **build something useful**.
>
> **We are not looking for pitch decks, concept videos, or AI wrappers with minimal differentiation.** We are looking for products that demonstrate **thoughtful problem solving, strong technical execution, excellent user experience, and clear value for users**.
>
> The best submissions will be those that people can actually **use, adopt, and recommend**. Projects should showcase how AI can move beyond novelty and become a meaningful part of everyday workflows.
>
> This is your opportunity to build the product you've always wanted to exist, validate your ideas with experienced judges, gain visibility within the AI community, and compete alongside some of the most ambitious builders from around the world.
>
> **If you can build something that makes people say, "I would use this tomorrow," you're exactly who this challenge is for.**

부제(태그라인):
> **Building the Future of Intelligent Systems. The Internet Needs Better AI.**

### 추출되는 힌트

1. **"I would use this tomorrow"** — 이 문장이 사실상 최상위 평가 렌즈. 데모 영상 마지막에 이 문구를 의도적으로 겨냥하는 것이 유효.
2. **금지 시그널 명시**: "pitch decks, concept videos, or **AI wrappers with minimal differentiation**" → 단순 LLM 프롬프트 래퍼는 명시적 감점 대상.
3. **"save time, create value"** — 정량적 시간 절감 수치를 제시하면 Problem Solving & Impact(25%)에 직결.
4. **"use, adopt, and recommend"** — 실제 사용자/얼리어답터 증거(가입자 수, 피드백 인용, 사용 로그)가 있으면 강력.
5. **최고 현금상 이름이 "Best SaaS Product"** → 상금을 노린다면 **SaaS 형태(멀티테넌트, 가입/온보딩, 요금제, 배포된 라이브 URL)** 로 포지셔닝하는 것이 결정적.
6. 규정 페이지에만 있는 **"Scalability and feasibility"** → 아키텍처 다이어그램에 확장성(큐, 캐시, 비용 모델) 언급 권장.
7. NexFellow 상 3종의 문구가 각각 다른 축을 명시:
   - Founder's Choice: "strong **user value and founder potential**"
   - Product Excellence: "**best executed** product with excellent **usability, technical quality, and real world value**"
   - Innovation: "**most creative and technically innovative** use of AI"
   → 한 프로젝트로 4개 상(현금 1 + NexFellow 3)에 동시 적합하게 서사를 짤 수 있음.
8. 스폰서 NexFellow의 정체성이 "제품 피드백/검증" → **사용자 검증(user validation)을 이미 수행했다는 증거**가 스폰서상 수상에 유리.
9. 심사위원 35%가 PM → **문제 정의·타깃 유저·지표**가 담긴 슬라이드가 기술 디테일만큼 중요.

---

## 12. 접근 불가/미확인 항목

| 항목 | 상태 |
|---|---|
| Devpost 제출 폼의 실제 필드 구성 | 로그인 필요, 미확인 |
| 슬라이드 덱 업로드 전용 필드 존재 여부 | 미확인 (포럼 미응답) |
| 현재 제출작 목록·개수·기술스택 | **갤러리 미공개로 확인 불가** |
| 참가자 명단 | 로그인 필요 |
| `/resources` 콘텐츠 | 페이지 존재하나 **내용 없음** |
| 최대 팀 규모 | **공식 미명시** |
| 미성년자(18세 미만) 보호자 동의 요건 | **공식 미응답** |
| 기존 코드 재사용 허용 범위 세부 | **공식 미응답** (규정은 "created during the hackathon period" 한 줄) |
| 라이선스 요구사항 | **요구 조항 없음** |
| 심사위원 상세 bio | 제공되지 않음(이름+직함만) |

---

## 우승을 위한 핵심 시사점

### A. 포지셔닝 — "SaaS 제품"으로 프레이밍하라
유일한 현금상 이름이 **Best SaaS Product ($4,000)** 다. 프로젝트를 단순 "AI 에이전트/툴"이 아니라 **배포된 멀티테넌트 SaaS**로 제시해야 한다. 최소 충족 요소:
- 공개 접근 가능한 **라이브 URL** (로그인 없이 체험 가능한 데모 계정 or 게스트 모드 제공)
- 회원가입/온보딩 플로우
- (가짜가 아닌) 요금제 페이지 또는 가격 모델 슬라이드
- 대시보드/설정 등 "제품스러운" 화면

### B. 제출물 체크리스트 (마감 2026-09-16 12:00 KST)
1. Devpost 제출 폼 — **팀원 전원이 각자 Devpost 계정 등록 후**, 대표 1인이 Enter a Submission. 팀원 이메일은 **계정 생성 이메일과 동일**해야 함.
2. **동작하는 제품** — 라이브 URL 필수급. 심사위원이 직접 눌러볼 수 있어야 함.
3. **공개 GitHub 레포** — 비공개 대안은 포럼에서 요청했으나 **답변 없음 → 예외 없다고 가정**. README에 문제/솔루션/아키텍처/설치법/데모 계정 정보 포함.
4. **데모 영상 ≤ 5분** (3~5분 권장). 필수 5요소를 순서대로 커버: 문제 → 동작 원리 → 핵심 기능 → **AI의 역할** → 라이브 시연.
5. **슬라이드 ≤ 10장**, 지정된 8개 섹션(Problem / Solution / Target Users / Features / Technical Architecture / AI Technologies Used / Impact & Value / Future Roadmap)을 **슬라이드 제목에 그대로 사용**. 업로드 위치가 불명확하므로 **레포에 PDF를 넣고 Devpost 설명에 링크 + 가능하면 Devpost 업로드도 병행**.
6. **Discord 가입(필수)** — `https://discord.com/invite/umEXASsAev`, `#introductions`에 국가명 포함 자기소개. 공지상 mandatory이므로 실격 리스크 제거 차원에서 반드시 수행.
7. **Tin Computer 크레딧($299) 클레임** — 선착순 100팀, 별도 심사 없음. 제출과 무관하게 즉시 신청.

### C. 점수 배분에 맞춘 자원 배치
가중치가 **Technical Implementation 25% + Problem Solving & Impact 25% = 50%**, UX 15% + Presentation 15% = 30%, Innovation 20%.
- 남은 시간의 절반은 **아키텍처 설명 자산**(다이어그램, 에이전트/워크플로 설계 문서, 평가 지표)에 투자. 코드 품질보다 **"설계가 보이게 만드는 것"** 이 점수가 된다.
- Impact 25%는 **정량 수치**로만 확보된다: "X 작업을 N분 → M초", "테스트 사용자 K명, 재방문율 R%" 형태의 구체 숫자를 최소 3개 준비.
- Innovation 20%는 "AI wrapper 아님"을 증명하는 **고유 메커니즘 1개**로 확보: 멀티에이전트 오케스트레이션, 자체 평가 루프, 도메인 특화 검증 레이어, 결정론적 안전 가드 등.

### D. 반드시 피해야 할 것 (주최측이 명시적으로 배제한 것)
- "pitch decks, concept videos" → **콘셉트 영상 금지. 반드시 라이브 시연 화면이 들어가야 한다.**
- "AI wrappers with minimal differentiation" → GPT 호출 한 번 감싼 챗봇 UI는 즉시 감점. 차별화 지점을 영상 30초 안에 명시할 것.

### E. 서사 설계 — 4개 상 동시 조준
한 편의 스토리로 아래 4개 상 문구를 모두 만족시켜라.
- Best SaaS Product → "배포된, 요금제 있는, 여러 사용자가 쓰는 제품"
- NexFellow Founder's Choice → "strong user value and founder potential": **실사용자 인용 + 시장 규모 + 창업 의지** 슬라이드 1장
- NexFellow Product Excellence → "usability, technical quality, real world value": **온보딩 30초 이내** + 테스트/CI 배지 + 실제 사용 사례
- NexFellow Innovation → "creative and technically innovative use of AI": 고유 메커니즘 다이어그램 1장

### F. 심사진 특성 대응
- PM 출신이 35%다. 슬라이드 1~3장(Problem / Target Users / Impact)에 **가장 공을 들여라**. 기술 디테일은 4~6장으로 압축.
- AWS Solutions Architect, ServiceNow 성능 엔지니어, 보안 분석가, TMMi(QA) 임원이 포함 → **확장성·성능·보안·테스트 한 줄씩** 아키텍처 슬라이드에 넣으면 이들 표를 얻는다. (규정 페이지의 "Scalability and feasibility" 항목과 정확히 일치)
- 심사 기간 9/16~9/20 EDT. 심사위원 20명이 수백 건을 나눠 보므로 **첫 60초 안에 가치가 전달되지 않으면 끝난다.** 영상 오프닝을 "이 제품은 X를 Y초에 해결합니다" 한 문장으로 시작할 것.

### G. 규정 리스크 관리
- "All submissions must be created during the hackathon period" — 기존 코드 재사용 관련 질문 3건이 모두 미응답이다. **방어적으로**: 레포에 `HACKATHON.md`를 두고 8/21 이후 작성된 범위를 커밋 해시와 함께 명시하고, 가급적 **해커톤 기간 커밋만 있는 전용 레포**를 제출하라 (포럼 45165의 참가자가 제안한 방식과 동일).
- 레포는 반드시 **public**. 제출 직전 private 여부 재확인.
- 영상은 **5분 초과 시 실격 리스크**. 4분 40초 내외로 편집.

### H. 지금(마감 D-1) 우선순위
1. 라이브 배포 URL 확보 + 게스트 체험 경로 (없으면 UX 15% + Impact 25% 동시 손실)
2. 데모 영상 촬영·편집 (Presentation 15%, 그리고 심사위원이 유일하게 끝까지 보는 자산)
3. 10장 슬라이드 (섹션 제목을 공식 8개 항목과 1:1 매칭)
4. README + 아키텍처 다이어그램
5. Discord 가입 + Tin 크레딧 클레임 (각 5분, 리스크 제거)
