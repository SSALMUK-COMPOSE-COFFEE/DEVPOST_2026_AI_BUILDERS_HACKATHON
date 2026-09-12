# 01. 대회 개요와 트랙 구조

조사 시각: 2026-09-15 21:20 KST

## 1. 기본 정보

| 항목 | 값 |
| --- | --- |
| 대회명 | AI Builders Hackathon |
| 부제 | `Building the Future of Intelligent Systems. The Internet Needs Better AI.` |
| 공식 URL | https://ai-builders-hackathon-2026.devpost.com/ |
| 주최 | **Open Source Connect (OSC)** / osconnect.org |
| 문의 | `hello@osconnect.org`, `osconnect011@gmail.com` |
| 플랫폼 | Devpost (내부 challenge_id `30452`) |
| 형식 | 온라인, 공개 |
| Devpost 태그 | `OSC`, `Machine Learning/AI`, `Open Ended`, `Beginner Friendly`, `Online`, `Public` |
| 등록 참가자 | **3,449명** (2026-09-15 21:20 KST 실측) |
| 기간 | 2026-08-21 ~ 2026-09-15 (26일) |
| 상금 표기 | `$ 33,900 + in prizes` |

> 규정 페이지는 `Participants will have 25 days to design, build, test, and submit their AI-powered solutions.` 라고 적고 있으나 8/21~9/15는 실제 26일입니다. 사소하지만 규정 문서의 정밀도를 보여주는 지표입니다.

---

## 2. 테마 원문 (가장 중요한 문서)

주최측이 무엇을 원하고 무엇을 싫어하는지가 이 한 섹션에 전부 있습니다. 전문을 그대로 옮깁니다.

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

### 여기서 뽑아내는 실행 지침

1. `"I would use this tomorrow"` 가 사실상 최종 평가 렌즈입니다. 영상 마지막 문장을 이 문구에 맞춰 설계하십시오.
2. **명시적 감점 시그널 3종**: `pitch decks`, `concept videos`, `AI wrappers with minimal differentiation`. LLM 호출 한 번 감싼 챗봇 UI는 즉사입니다.
3. `save time, create value` → 정량 수치가 곧 Impact 25%입니다. "N분을 M초로" 형태의 숫자를 최소 3개 준비하십시오.
4. 최고 현금상 이름이 **Best SaaS Product**입니다. 에이전트 데모가 아니라 **제품**으로 포지셔닝해야 합니다.

---

## 3. What to Build (원문)

> Build an AI product that solves a real problem.
> We encourage teams to focus on creating products that people would genuinely want to use beyond the hackathon.
> Your project may be an AI application, autonomous agent, multi-agent system, developer tool, workflow automation platform, research assistant, productivity tool, education solution, healthcare application, business software, creative tool, or an entirely new category of AI-powered product.

규정 페이지의 대응 문구:

> All submissions must be created during the hackathon period and align with the theme of Artificial Intelligence, Agentic AI, or Intelligent Systems.
>
> Projects may include:
> • AI Agents and Multi-Agent Systems
> • AI Assistants and Copilots
> • Workflow Automation Solutions
> • AI for Education, Healthcare, Finance, Research, or Productivity
> • Developer Tools powered by AI
> • Innovative Generative AI Applications

---

## 4. 트랙 구조 : 사실상 없음

**본 해커톤에는 제출 트랙이 존재하지 않습니다.** 단일 풀에서 모든 프로젝트가 같은 배점표로 평가되고, 상만 6종으로 나뉩니다.

혼동하기 쉬운 두 가지를 구분하십시오.

| 무엇 | 실체 |
| --- | --- |
| `Machine Learning/AI`, `Open Ended`, `Beginner Friendly` | Devpost의 **검색용 카테고리 태그**. 제출 시 선택하는 트랙이 아님 |
| `SaaS & Products / AI & Agents / Developer & Open Source / Web3 & Emerging Tech` | **NexFellow 펠로십**(별도 8주 프로그램)의 트랙. 해커톤과 무관. 출처: `/updates/46412` |

### 트랙별 필수 스폰서 기술: 없음

사이트 전체에서 특정 스폰서 SDK/API 사용을 의무화하는 문구는 **발견되지 않았습니다**. 가장 가까운 문구는 Get started 4단계의 권장 수준입니다.

> `Explore the challenge themes, resources, and sponsor technologies.`

그리고 `/resources` 페이지는 **본문이 비어 있습니다**. 즉 "탐색하라"고 안내된 리소스 목록 자체가 게시되지 않았습니다.

**유일한 강제 사항은 Discord 가입입니다.**

> `Joining our Discord server is mandatory for all participants, as all important hackathon updates, announcements, discussions, and community interactions will happen there.` (`/updates/46223`)

---

## 5. 심사위원 20인

| 이름 | 소속 / 직함 |
| --- | --- |
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

상세 bio는 제공되지 않고 이름과 직함만 게시됩니다.

### 구성 분석과 대응

- **Product Manager 계열 7명 = 35%.** 문제 정의 / 타깃 유저 / 지표 슬라이드가 기술 디테일만큼 중요합니다.
- 엔지니어 계열 약 9명. Apple, PayPal, Microsoft, Visa, AWS, IBM, Dell, ServiceNow 등 **대기업 프로덕션 경험자** 중심이고, 연구자는 2명뿐입니다. 논문성 딥러닝 깊이보다 **아키텍처와 운영 관점**이 먹힙니다.
- **품질/보안/성능 평가자가 3명 존재**합니다. Peri(TMMi America, QA 성숙도 모델 이사회), Vemuri(보안 분석가), Vudathala(성능 엔지니어). 아키텍처 슬라이드에 확장성·성능·보안·테스트를 한 줄씩 넣으면 이 3표를 직접 겨냥할 수 있고, 이는 규정 페이지에만 있는 심사 항목 `Scalability and feasibility`와 정확히 맞습니다.
- 심사 기간은 9/16 22:00 ~ 9/21 10:00 KST. 20명이 수백 건을 나눠 봅니다. **첫 60초 안에 가치가 전달되지 않으면 끝입니다.**

---

## 6. 스폰서

| 스폰서 | URL | 역할 |
| --- | --- | --- |
| **NexFellow** | https://www.nexfellow.com/ | 비현금 상 3종 제공. 빌더와 리뷰어를 잇는 제품 피드백 플랫폼 |
| **Tin Computer** | https://tin.computer/ | $299 크레딧 × 100팀. 코딩 에이전트용 오픈소스 마케팅 시스템 (Apache 2.0) |
| **Algoverse** | https://algoverseairesearch.org/ | 대학생 AI 연구 프로그램. 상금 제공 아님, 기회 제공형 |
| **Sylus AI** | https://sylusai.com/ | 로고만 게시. 상금 항목 없음 |
| Open Source Connect | osconnect.org | 주최 커뮤니티 |

---

## 출처

- https://ai-builders-hackathon-2026.devpost.com/
- https://ai-builders-hackathon-2026.devpost.com/rules
- https://ai-builders-hackathon-2026.devpost.com/resources
- https://ai-builders-hackathon-2026.devpost.com/updates/46223
- https://ai-builders-hackathon-2026.devpost.com/updates/46412
- https://www.nexfellow.com/ , https://tin.computer/ , https://algoverseairesearch.org/ , https://sylusai.com/
