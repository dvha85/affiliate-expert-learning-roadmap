# Chương trình v2 — Affiliate Intelligence Bot hướng Reality-First

**Trạng thái:** Active canonical curriculum
**Đối tượng:** Người mới bắt đầu, không mặc định đã biết terminal hay lập trình
**Architecture:** [ADR-004](docs/ADR-004-DETERMINISTIC-CORE-IMPLEMENTATION-FLEXIBILITY.md) + [ADR-005](docs/ADR-005-REALITY-FIRST-CURRICULUM.md)

Nội dung learner-facing dùng tiếng Việt làm chính; xem
[Quy chuẩn ngôn ngữ](docs/VIETNAMESE-LANGUAGE-STYLE.md).

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

> **Migration in progress:** inventory lesson và Mission files v1 được giữ làm
> baseline/reference. V2 là sequence chuẩn cho work mới; trạng thái delivery
> thật xem tại [missions/README.md](missions/README.md) và
> [Curriculum migration](docs/CURRICULUM-MIGRATION-v2.md).

## Mục tiêu đầu ra

Người học xây một hệ thống hỗ trợ quyết định Affiliate có evidence, biết giữ
`unknown`/`GET_MORE_DATA`, dùng outcome để đề xuất cải tiến đã review, rồi mới
tăng automation. Bot/AI không có quyền publish, spend, nhắn tin hay đổi tài
khoản chỉ vì confidence cao.

Affiliate Intelligence Decision Contract phải nối được:

```text
Offer + audience/problem + content/channel hypothesis
→ evidence + uncertainty + policy/risk
→ human or deterministic decision
→ action / tracking
→ outcome / evaluation
→ proposed improvement / review
```

Field chưa có evidence phải là `unknown`, `not_yet_observable` hoặc state
abstain hợp lệ; không bịa audience, conversion, revenue hoặc compliance claim.

## Mission-first và practice-first

```text
TRY ON A SMALL REAL CONTEXT
→ OBSERVE A GAP
→ PULL THE SMALLEST USEFUL KNOWLEDGE SLICE
→ IMPROVE / TEST
→ SAVE EVIDENCE
→ EXPLAIN LIMITS AND NEXT MEASUREMENT
```

Lesson ID là knowledge inventory, **không phải reading order** và không tự
trao Mission PASS. Một Mission chỉ DONE khi capability, reality và operated
evidence theo contract của chính Mission đều đạt.

## Real Evidence Ladder

| Level | Evidence | First v2 use |
|---|---|---|
| E0 | synthetic/test/replay, chỉ chứng minh plumbing | O00 orientation, không phải PASS |
| E1 | public observation thật, có source + observed_at | M00 |
| E2 | public action do human review và tự thực hiện | M00 |
| E3 | outcome snapshot/analytics/export thật, kể cả 0 | M01 |
| E4 | Decision → Action → Outcome → Evaluation → reviewed improvement | M05 |
| E5 | bounded governed canary có policy/audit/kill-switch | M10 |
| E6 | production loop khép kín qua recovery/learning review | M11 |

Sample không thể thay E1–E6. `0`, missing, pending và inconclusive là các
trạng thái khác nhau; sale không phải điều kiện PASS.

## Core / Advanced / Reference

Core / Advanced / Reference là ba phạm vi riêng. Core hiện có 7 Parts · 21
Chapters · 63 micro-lessons. Advanced chỉ mở sau evidence/bottleneck thật.
Reference (Go, n8n, providers, platform policy, SQL, deployment) không phải
prerequisite hay PASS shortcut.

| Part | Chapters | Lessons | V2 Mission focus |
|---|---:|---:|---|
| P0 — Reality trước | C0–C2 | 9 | M00 safe market loop |
| P1 — Outcome + baseline | C3–C5 | 9 | M01–M02 snapshot + deterministic Bot |
| P2 — Trustworthy intelligence | C6–C8 | 9 | M03–M04 history/measurement + grounded AI |
| P3 — Improve from reality | C9–C11 | 9 | M05 reviewed improvement |
| P4 — Reliable decisions | C12–C14 | 9 | M06–M07 |
| P5 — Governed tools/actions | C15–C17 | 9 | M08–M10 |
| P6 — Production loop | C18–C20 | 9 | M11 |

## Canonical Mission spine v2

`O00` là orientation synthetic để thấy full loop và không có PASS/side effect.
M01 và M02 có thể làm song song sau M00; M03 cần cả hai.

| Mission | Outcome thử trước | Evidence | Authority | Delivery state |
|---|---|---|---|---|
| M00 — First Safe Market Loop | human tự tạo/review/publish một artifact nhỏ có disclosure + tracking | E1→E2 | human_only; Bot/AI không publish | planned |
| M01 — First Outcome Snapshot | ghi outcome/measurement snapshot nhỏ nhất, không ép kết quả dương | E3 | manual/read-only | planned |
| M02 — Smallest Deterministic Bot | baseline audit được cho evidence/context đã có | E0 + hỗ trợ E1/E2 | A0 deterministic | planned |
| M03 — Trustworthy History & Measurement | history append-only, provenance/freshness/reconcile | E3 | A0 deterministic | planned |
| M04 — Grounded AI Advisor | AI advisory grounded + fallback, không tool/write | E3 | A1 advisory | planned |
| M05 — First Reviewed Improvement | hypothesis từ outcome → test/review/rollback | E4 | A1 propose only | planned |
| M06 — Reliable Watcher | reliable read/alert/recovery | E4 | A0 core + A1 triage | planned |
| M07 — Decision and Abstention | DecisionPacket/policy/evaluation | E4 | A1 advisory | planned |
| M08 — Read-only Evidence Agent | allowlisted read-only tool evidence | E4 | A2-RO | planned |
| M09 — Shadow Action and Approval | ActionIntent + durable approval/shadow | E4 | A3-shadow | planned |
| M10 — Governed Canary | bounded RISK0/RISK1 automation; RISK2 approval | E5 | A3-limited | planned |
| M11 — Production Closed Loop | deploy/recover/outcome learning without silent self-modification | E6 | A3-production | planned |

## Milestone gates

| Gate | Missions | Required truth |
|---|---|---|
| G1 — First market contact | M00 | human-owned E1→E2 loop, safe/manual/tracked |
| G2 — Measurable baseline | M01–M03 | outcome snapshot + auditable baseline/history |
| G3 — Learn safely | M04–M05 | grounded advice + reviewed improvement from outcome |
| G4 — Governed production | M06–M11 | reliability, policy, approval, audit, recovery |

## Authority order

1. `CURRICULUM.md` — outcome, sequence, evidence and PASS boundary;
2. `ROADMAP.md` and `roadmap/part-00..06.md` — normalized inventory/index;
3. active v2 Mission/lesson files — execution detail;
4. ADR/operating standards — safety and quality detail;
5. v1 artifacts and `sources/` — historical/reference only.

Xem [ADR-005](docs/ADR-005-REALITY-FIRST-CURRICULUM.md) và
[migration rules](docs/CURRICULUM-MIGRATION-v2.md) trước khi tạo hoặc đổi
Mission.
