# ADR-002 — Outcome-Driven Curriculum cho Absolute Beginner

- **Status:** Accepted
- **Date:** 2026-08-29
- **Decision owners:** Curriculum maintainers
- **Supersedes:** cấu trúc active 23 Parts / 89 Chapters / 671 lessons / 14 main projects

## Context

Curriculum trước có coverage rộng về Affiliate, data, engineering, AI, automation và production. Tuy nhiên learner chưa bắt đầu, chỉ một phần rất nhỏ lesson/Mission đã được author, và learner goal thực tế hẹp hơn knowledge inventory:

> Một người mới phải xây được Affiliate Bot thông minh, tự động có kiểm soát, học qua thực hành trước lý thuyết và cải tiến bằng evidence/outcome thật.

Cấu trúc 671 lessons tạo các rủi ro:

- biến knowledge inventory thành đường học tuần tự;
- tách quá nhiều thuật ngữ thành lesson riêng;
- lặp nội dung giữa Product Intelligence, Analytics, Decision, Bot Engineering và Production;
- trì hoãn real market feedback tới quá muộn;
- để sample output có thể bị hiểu nhầm là business validation;
- front-load platform/legal/technology facts vốn thay đổi nhanh;
- tạo 14 project rời trong khi learner cần một product spine liên tục;
- làm timeline khó hiệu chỉnh bằng learner evidence.

Các operating standards hiện có về evidence, confidence, freshness, evaluation, approval, security và outcome memory vẫn có giá trị và phải được bảo toàn.

## Decision

Adopt một active canonical curriculum mới:

```text
7 Core Parts
21 Chapters
63 Core micro-lessons
12 Missions (M00–M11)
4 Milestone Gates
1 evolving Affiliate Intelligence Bot
12 optional Advanced modules
Reference material không có PASS checkbox
```

`CURRICULUM.md` trở thành active canonical authority. `ROADMAP.md` và bảy file `roadmap/part-00.md` đến `part-06.md` là normalized index/checklist.

`sources/SYLLABUS-v2026.08.md` và `sources/SYLLABUS-v2026.09.md` được giữ nguyên để bảo toàn provenance nhưng chỉ còn historical status. Không dùng mô hình “historical baseline + active override” cho curriculum mới.

## Part architecture

| Part | Chapters | Primary outcome |
|---|---|---|
| P0 — First Evidence-Backed Decision | C0–C2 | First running Bot + real product evidence + human-vs-Bot decision |
| P1 — Trustworthy Data & Grounded AI | C3–C5 | Validated history + grounded AI advisory with fallback |
| P2 — First Tracked Market Loop | C6–C8 | Manual compliant publication + real tracked outcome |
| P3 — Outcome-Driven Improvement | C9–C11 | Experiment and reviewed improvement based on outcome |
| P4 — Reliable Intelligence & Decisions | C12–C14 | Reliable signal-to-decision service with evaluation |
| P5 — Tool Agent & Governed Automation | C15–C17 | Read-only evidence agent + policy/approval action boundary |
| P6 — Production Closed Loop | C18–C20 | Operated Bot with recovery, safety and outcome learning |

Mỗi Chapter có đúng ba micro-lessons. Con số 63 là initial authoring ceiling, không phải target cần bảo vệ vĩnh viễn; personal actuals có thể dẫn tới merge, rewrite hoặc loại lesson.

## Pedagogy invariants

### Attempt precedes explanation

Mỗi Mission bắt đầu bằng một task có thể chạy/quan sát. Learner chỉ pull knowledge sau khi gặp gap cụ thể. Không quá ba micro-lessons liên tiếp trước khi quay lại code, dữ liệu hoặc market action.

### Real evidence precedes claims of intelligence

Bot output trên sample data chỉ chứng minh engineering behavior. Business claims cần evidence thật có source, timestamp, freshness và classification.

### Real feedback arrives before autonomy

Learner quan sát public products và tạo first evidence-backed decision ngay M00, sau đó chạy manual tracked market loop ở M03–M04. Bot không có external authority trong giai đoạn này.

### Deterministic baseline precedes AI

AI chỉ enrich một capability có baseline/fallback. Invalid, unsupported hoặc unavailable AI output không được làm hỏng core path.

### Decision is separate from execution

AI/analytics có thể đề xuất decision. External execution luôn đi qua explicit ActionIntent, deterministic risk/policy, permission, approval khi cần, revalidation, idempotency và audit.

### Outcome learning is controlled change

Outcome memory tạo proposed improvement. Không model/agent nào được tự rewrite production policy, prompt, weights hoặc code mà không qua test, review và approved release.

## Assessment decision

Tiến độ chính được đo bằng Mission và Milestone Gate, không bằng việc tick toàn bộ knowledge inventory.

Mỗi Mission có hai cổng:

- **Capability PASS** — working artifact, tests/failure case và explain-back;
- **Reality verified** — đúng cấp real evidence, provenance và no sample/real substitution;
- **Operated** — đủ cycle/failure/safety evidence theo Mission contract.

Mission `DONE` cần cả ba chiều bắt buộc. Kết quả kinh doanh không cần tích cực: zero hoặc inconclusive là hợp lệ khi measurement trung thực.

## Scope tiers

### Core

Core chỉ chứa knowledge cần để ship Mission hiện tại/ngay kế tiếp và có áp dụng ngay.

### Advanced

12 module tùy chọn bao phủ platform adapters, advanced tracking/analytics/statistics, time-series/ML/bandit, RAG/MCP/multi-agent, distributed systems, paid traffic/portfolio và SaaS. Advanced không tính Core completion và chỉ mở khi có use case/bottleneck thật.

### Reference

Glossary, cookbooks, platform/legal/tax current facts, schemas, provider matrix, deployment và security checklists là reference không có PASS checkbox. Volatile facts phải có source/freshness metadata.

## Consequences

### Positive

- learner tạo giá trị quan sát được trong Mission đầu;
- first real market loop đến trước agent autonomy;
- giảm mạnh cognitive load và duplicated mastery gates;
- một product spine giúp evidence/versioning rõ;
- AI và automation được đánh giá bằng behavior/outcome thay vì độ phức tạp;
- current platform facts có thể cập nhật mà không rewrite curriculum structure.

### Trade-offs

- không còn tuyên bố coverage mọi chủ đề Affiliate ở Core;
- old IDs và count-based reporting không còn tương thích;
- validators, progress tracking, plans và Mission map cần migration;
- một số tài liệu cũ vẫn có thể nói 23/89/671 trong thời gian chuyển đổi;
- authoring phải được kiểm bằng personal actuals theo từng wave thay vì viết đủ 63 lesson trước.

## Migration rules

1. Không sửa historical files trong `sources/`.
2. Không giữ compatibility chỉ để bảo toàn 23/89/671/14.
3. Chỉ link lesson vào active roadmap khi lesson đã được rewrite theo new ID/title và authoring standard.
4. Migrate M00/P0 trước, sau đó M01–M04/P1–P2; chạy personal validation trước khi author toàn bộ Core.
5. Rewrite validators để kiểm 7/21/63, Mission mapping, real-evidence gates và Core/Advanced/Reference boundary.
6. Giữ learner/reference workspace separation và operating safety contracts.
7. Archive hoặc un-link legacy lesson artifacts; file tồn tại không tự động khiến nó thành active Core.

## Non-goals

- Không đảm bảo revenue hoặc conversion dương.
- Không yêu cầu paid traffic.
- Không yêu cầu multi-agent, MCP, ML, SaaS hoặc high-scale infrastructure để hoàn thành Core.
- Không cấp autonomous publishing/spending authority sớm để Bot trông “thông minh hơn”.
- Không biến platform/legal/tax facts thành chân lý tĩnh.

## Revisit criteria

ADR cần được review sau:

- owner hoàn thành personal validation M00–M04 hoặc ghi `BLOCKED_EXTERNAL` trung thực;
- có planned-vs-actual effort cho từng Mission, ghi rõ `n=1`;
- có blocker data từ personal execution;
- có ít nhất một real tracked outcome loop;
- có evidence lesson nào không được dùng, quá dài hoặc xuất hiện quá sớm.

Mọi thay đổi count/sequence sau review phải dựa trên learner evidence, không dựa trên nhu cầu giữ hình thức cân đối.
