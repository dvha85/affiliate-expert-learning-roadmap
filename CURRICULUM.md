# Curriculum — Outcome-Driven Affiliate Intelligence Bot

**Trạng thái:** Active canonical curriculum

**Đối tượng:** Người mới bắt đầu, kể cả người chưa từng lập trình

**Sản phẩm xuyên suốt:** Một Affiliate Intelligence Bot tiến hóa qua 12 Mission

**Cấu trúc Core:** 7 Parts · 21 Chapters · 63 micro-lessons

**Tỷ lệ mục tiêu:** khoảng 15% knowledge pull · 85% build, run, measure và improve

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

> Curriculum này thay thế cấu trúc 23 Parts / 89 Chapters / 671 lessons làm nguồn thực thi chính.
> `sources/SYLLABUS-v2026.08.md` và `sources/SYLLABUS-v2026.09.md` chỉ còn là historical research input, không phải active authority.
> 63 là inventory outcome/knowledge hiện tại, không có nghĩa 63 lesson file đều đã ready. M00/Part 0 được author trước; phần sau chỉ lên `ready` sau review và learner evidence.

## 1. Mục tiêu đầu ra

Người hoàn thành Core phải chứng minh bằng artifact và evidence rằng họ có thể:

1. quan sát một workflow Affiliate thật và phân biệt `fact`, `estimate`, `assumption`, `unknown`;
2. xây Bot Go đọc, kiểm tra, lưu lịch sử và theo dõi dữ liệu sản phẩm;
3. xếp hạng cơ hội bằng deterministic baseline có giải thích, confidence và khả năng abstain;
4. tự xuất bản thủ công nội dung đúng disclosure, gắn tracking và thu outcome thật;
5. liên kết `Decision → Action → Outcome → Evaluation`;
6. chạy thí nghiệm nhỏ và chấp nhận kết quả `inconclusive` khi evidence chưa đủ;
7. thêm AI advisory có grounding, schema validation, evaluation và deterministic fallback;
8. cho agent thu thập bằng chứng qua tool read-only có permission và audit rõ;
9. tự động hóa hành động rủi ro thấp và bắt buộc approval cho hành động có hậu quả;
10. deploy, monitor, recover, dùng kill switch và tạo proposed improvement từ outcome mà không để Bot tự sửa production policy, prompt hoặc weights.

### Affiliate Intelligence answer contract

Để curriculum không trôi thành generic agent/automation course, một Bot trưởng thành phải hỗ trợ decision có bằng chứng cho các câu hỏi domain sau:

```text
Product/Offer nào?
Tại sao?
Audience/Problem nào?
Content angle nào?
Hook / CTA nào?
Channel nào?
Timing / observation window nào?
Expected Value / expected affiliate revenue bao nhiêu?
Evidence refs nào hỗ trợ?
Confidence theo method/reason nào?
Uncertainty / missing evidence là gì?
Compliance / business risk là gì?
Recommended state: ACT / WAIT / GET_MORE_DATA / HUMAN_REVIEW / DENY?
Next measurement / experiment là gì?
```

Đây là **cumulative contract**. Mission sớm chỉ điền field đã có evidence; field chưa đủ phải giữ `unknown`, `not_yet_observable` hoặc abstain. Không được bịa audience, CVR, expected revenue, risk hoặc recommendation để làm output trông đầy đủ.

Canonical field semantics, product-opportunity signals và maturity map M00→M11 nằm tại [`docs/AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md`](docs/AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md).

Nguyên tắc xuyên suốt:

> **DATA > OPINION**
>
> **EXPECTED VALUE > COMMISSION RATE**

## 2. Mission-first — Mô hình học bắt buộc

Mỗi Mission đi theo cùng một vòng lặp:

```text
Attempt first
→ Run
→ Observe a concrete gap
→ Pull no more than three micro-lessons at a time
→ Improve
→ Test a happy path and a failure path
→ Operate on real or clearly-labelled sample data
→ Save technical + business evidence
→ Explain back
→ Ship the next Bot capability
```

Không yêu cầu learner đọc hết một Part rồi mới được build. Lesson là knowledge slice được kéo đúng lúc; Mission evidence mới là đơn vị tiến độ chính.

### Ba chiều tiến độ độc lập

Mỗi Mission theo dõi riêng:

- **Capability PASS:** artifact chạy được, tests/failure case đạt và learner giải thích được implementation;
- **Reality verified:** evidence đúng cấp, có provenance/timestamp và không đánh tráo sample thành dữ liệu thật;
- **Operated:** capability đã được chạy qua số cycle, failure/recovery case và safety gate mà Mission yêu cầu.

Mission chỉ `DONE` khi cả ba chiều bắt buộc đều đạt. Learner có thể tiếp tục engineering trong lúc chờ observation window, nhưng không được tuyên bố Reality đã verified hoặc Mission đã DONE.

## 3. Real Evidence Ladder

| Cấp | Bằng chứng | Mission đầu tiên |
|---|---|---|
| E0 | Sample/synthetic, chỉ dùng cho engineering test | pre-M00 scaffold |
| E1 | Quan sát nguồn công khai thật, có source và thời gian | M00 |
| E2 | Human action thật: nội dung được publish thủ công | M03 |
| E3 | Analytics/export thật: impression/click/order, kể cả giá trị `0` | M04 |
| E4 | Decision → Action → Outcome và reviewed improvement liên kết được | M05 |
| E5 | Bounded governed canary có policy, audit và kill-switch evidence | M10 |
| E6 | Closed-loop production evidence | M11 |

Quy tắc:

- sample data không thể thỏa business-evidence gate;
- không có conversion không phải là FAIL;
- `0` chỉ hợp lệ khi source thật báo `0`; missing data không được đổi thành `0`;
- external publish ban đầu luôn do con người thực hiện;
- outcome có thể `positive`, `negative`, `zero`, `inconclusive` hoặc `not_yet_observable`;
- Bot không tự tăng authority chỉ vì model confidence cao.

## 4. Core structure

| Part | Chapters | Core lessons | Missions | Capability outcome |
|---|---:|---:|---|---|
| [P0 — First Evidence-Backed Decision](roadmap/part-00.md) | C0–C2 | 9 | M00 | Bot chạy được, dùng evidence thật và tạo quyết định đầu tiên |
| [P1 — Trustworthy Data & Grounded AI](roadmap/part-01.md) | C3–C5 | 9 | M01–M02 | Data history đáng tin cậy và AI advisory có grounding/fallback |
| [P2 — First Tracked Market Loop](roadmap/part-02.md) | C6–C8 | 9 | M03–M04 | Nội dung thật, tracking thật và human-vs-AI outcome comparison |
| [P3 — Outcome-Driven Improvement](roadmap/part-03.md) | C9–C11 | 9 | M05 | Một thay đổi có hypothesis, outcome và rollback path |
| [P4 — Reliable Intelligence & Decisions](roadmap/part-04.md) | C12–C14 | 9 | M06–M07 | Reliable signal-to-decision service có evaluation |
| [P5 — Tool Agent & Governed Automation](roadmap/part-05.md) | C15–C17 | 9 | M08–M10 | Read-only tool agent và governed action workflow |
| [P6 — Production Closed Loop](roadmap/part-06.md) | C18–C20 | 9 | M11 | Bot production có recovery, safety và outcome-learning loop |

## 5. Mission spine và knowledge pull

| Mission | Attempt / ship target | Knowledge pull |
|---|---|---|
| M00 — First Evidence-Backed Decision | Chạy Bot, thu 5 public observations, human rank trước và giải thích Bot ranking | 0.1–2.3, theo ba attempt/pull cycles |
| M01 — Trustworthy History | Tự build ingest/validation, lưu ít nhất hai snapshot thật và phát hiện thay đổi | 3.1–4.3 |
| M02 — Grounded AI Advisor | Thêm AI advisory trên deterministic baseline; invalid AI output phải fallback | 5.1–5.3 |
| M03 — Human Tracked Publish | Người học tự duyệt và publish một micro-content có disclosure/tracking | 6.1–7.1 |
| M04 — Real Outcome Analytics | Import outcome thật, reconcile và so human baseline với AI-assisted variant | 7.2–8.3 |
| M05 — First Real Improvement | Chạy một experiment; tạo proposed change, offline test, review và version mới | 9.1–11.3 |
| M06 — Reliable Automatic Watcher | Watcher/alerts chạy được qua retry, duplicate và recovery cases | 12.1–12.3 |
| M07 — Decision and Abstention | DecisionPacket xử lý đúng stale, missing và conflicting evidence | 13.1–14.3 |
| M08 — Read-Only Evidence Agent | Agent dùng explicit tools để lấy missing evidence, không có external side effect | 15.1–15.3 |
| M09 — Shadow Action and Approval | Tạo ActionIntent, durable approval và shadow/dry-run execution | 16.1–16.3, 17.1 |
| M10 — Limited Governed Automation | Chạy bounded RISK0/RISK1 canary; RISK2 vẫn cần durable approval | 17.2–17.3, reuse C16 |
| M11 — Production Closed Loop | Deploy, chạy qua observation window, recovery drill và outcome review | 18.1–20.3 |

Mỗi Mission phải làm trưởng thành thêm một phần của Affiliate Intelligence Decision Contract; automation capability không được thay thế domain reasoning. Mission file phải đưa learner tới attempt trước khi trỏ tới giải thích dài. Reference implementation chỉ được mở sau attempt hoặc khi learner chủ động dùng hint ladder.

## 6. Milestone gates

### G1 — First Evidence-Backed Decision — M00

- Bot chạy, test và tạo output kiểm tra được;
- có E1 evidence từ ít nhất 5 product observations;
- human judgment tồn tại trước Bot ranking;
- decision có reason, confidence và weakest assumption.

### G2 — Trustworthy Intelligence — M01–M02

- validation và history không overwrite evidence;
- change detection dùng provenance/freshness;
- deterministic capability vẫn chạy khi AI unavailable;
- AI claim không có evidence ref không được đi vào scoring fact.

### G3 — First Market Learning Loop — M03–M05

- có ít nhất một manual, compliant, tracked publication;
- có outcome thật sau một declared observation window;
- missing khác zero và inconclusive được giữ nguyên;
- có một improvement từ hypothesis đến reviewed release hoặc documented rejection.

### G4 — Governed Production Loop — M06–M11

- Signal/Analysis/Decision/Action contracts có trace;
- agent tools có schema, permission và audit;
- RISK2 không thể execute nếu thiếu durable approval và revalidation;
- production bot có recovery, kill switch và Decision↔Outcome learning tạo proposed change thay vì silent self-modification.

## 7. Core / Advanced / Reference

### Core

63 micro-lessons trong 7 Part là toàn bộ phạm vi bắt buộc. Một lesson chỉ được ở Core khi:

1. cần để PASS Mission hiện tại hoặc ngay kế tiếp;
2. làm thay đổi implementation hoặc business decision;
3. có artifact, test hoặc evidence áp dụng ngay;
4. không thể thay bằng một reference card ngắn.

### Advanced modules — không tính Core/PASS

| ID | Module |
|---|---|
| A01 | Platform-specific APIs và production adapters |
| A02 | Server-side tracking, webhook và identity resolution |
| A03 | Data warehouse, dashboard và BI nâng cao |
| A04 | Advanced experimentation và statistical power |
| A05 | Time-series, anomaly detection và forecasting |
| A06 | Machine Learning và Learning-to-Rank |
| A07 | Explore–Exploit và Multi-Armed Bandit |
| A08 | RAG, embeddings và vector retrieval |
| A09 | MCP, A2A và multi-agent orchestration |
| A10 | Distributed workflows và high-scale operations |
| A11 | Paid traffic và multi-channel portfolio optimization |
| A12 | SaaS productization, multi-tenancy và billing |

Advanced module chỉ được mở khi learner đã có Core evidence và một bottleneck/use case thật. Không module nào được dùng để trì hoãn real market loop đầu tiên.

### Reference — không có lesson checkbox

Reference gồm:

- glossary;
- Go/SQL/HTTP/testing cookbook;
- JSON schemas và decision contracts;
- platform playbook có `verified_at`;
- legal/tax/current-policy source register;
- provider capability matrix;
- deployment recipes;
- security và troubleshooting checklists.

Thông tin platform, pháp lý, thuế, model/SDK và current versions phải đi qua freshness policy. Chúng không trở thành Core lesson chỉ vì quan trọng.

## 8. Definition of Done của chương trình

Core chỉ hoàn tất khi:

- M00–M11 đều có Capability PASS, Reality verified và Operated theo contract của Mission;
- bốn Milestone Gate có artifact/demo và retrospective;
- learner có ít nhất một real tracked market loop, kể cả outcome bằng `0` hoặc `inconclusive`;
- Affiliate Intelligence Decision Contract được điền bằng evidence hoặc explicit abstention, không bằng fabricated completeness;
- AI capability có deterministic baseline, eval cases và fallback;
- agent không bypass tool permission, policy, approval hoặc kill switch;
- một trace nối được trigger → evidence → decision → action → outcome → evaluation;
- outcome learning chỉ tạo proposed improvement qua test/review;
- learner giải thích được điều Bot biết, không biết và chưa được phép làm.

## 9. Authority

Khi tài liệu mâu thuẫn, thứ tự authority là:

1. `CURRICULUM.md` — mục tiêu, cấu trúc Core, Mission spine và PASS boundary;
2. `ROADMAP.md` cùng `roadmap/part-00.md` đến `part-06.md` — normalized checklist/index;
3. Mission và active lesson files — execution detail;
4. operating standards trong `docs/` — contract, safety và quality detail;
5. `sources/` — historical/research input, không phải active implementation authority.

Chi tiết quyết định kiến trúc nằm tại [`docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md`](docs/ADR-002-OUTCOME-DRIVEN-CURRICULUM.md).