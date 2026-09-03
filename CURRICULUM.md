# Chương trình hiện hành — Affiliate Intelligence Bot có kiểm soát

**Trạng thái:** Active canonical curriculum  
**Đối tượng:** Người mới; không mặc định biết terminal, Go hay Agent framework  
**Mục tiêu:** xây một **Affiliate Intelligence Bot tiến hóa dần tới tự động hóa cao nhưng vẫn kiểm soát được**.

> Learner order được quyết định bởi **Mission spine** bên dưới, không phải số lesson cũ.

Nội dung learner-facing dùng tiếng Việt làm chính. `ActionIntent`, `DecisionPacket`, `PolicyDecision`, `RISK0`… được giữ nguyên khi đó là contract/code identifier và luôn có giải thích tiếng Việt ở lần xuất hiện đầu.

## 1. Mục tiêu đầu ra

Hệ thống cuối phải nối được:

```text
Evidence
→ Deterministic Decision
→ Grounded AI khi cần
→ ActionIntent
→ Deterministic Policy / Risk
→ Human Approval khi cần
→ Controlled Execution
→ Outcome
→ Evaluation
→ Reviewed Improvement
↺
```

Bot phải biết:

- nguồn nào hỗ trợ một fact;
- dữ liệu nào là `estimate`, `assumption` hoặc `unknown`;
- `0` khác `missing`, `pending`, `not_yet_observable` và `inconclusive`;
- khi nào phải abstain (`GET_MORE_DATA`, `HUMAN_REVIEW`, `WAIT`);
- khi nào chỉ được đề xuất;
- khi nào được tự hành động;
- action nào bắt buộc con người duyệt;
- cách audit, replay, rollback và dừng khẩn cấp.

Invariant cấp cao:

```text
AI confidence != execution permission
Decision != Approval != Execution
Agent proposal != authorized ActionIntent
Tool result != trusted evidence
```

## 2. Reality-First nhưng không Publish-First

Chương trình bắt đầu bằng **bằng chứng thị trường thật**, nhưng không ép người mới publish trước khi có Bot baseline.

```text
REALITY-FIRST
!= PUBLISH-FIRST
```

M00 chỉ cần public observation thật, provenance và human decision packet. External publish/action xuất hiện ở M03, sau khi learner đã có deterministic Bot + trustworthy history.

## 3. Mission spine — thứ tự học chuẩn

| Mission | Outcome bàn giao | Evidence tối thiểu | Authority ceiling |
|---|---|---|---|
| O00 | Safe synthetic walkthrough, không PASS | E0 | no side effect |
| **M00** | First Real Evidence Packet + Human DecisionPacket | E1 | human/read-only |
| **M01** | Smallest Deterministic Bot v0.1 | E0 + E1 support | A0 deterministic, no action |
| **M02** | Trustworthy History + Replay v0.2 | E1/E3-ready | A0 deterministic |
| **M03** | First Tracked Human Action + Outcome context | E2→E3 | human executes |
| **M04** | Grounded AI Advisor v0.4 | E3 | A1 advisory, no tools/write |
| **M05** | First Reviewed Improvement | E4 | A1 propose only |
| **M06** | Reliable Automatic Watcher | E4 | automatic read-only |
| **M07** | Read-only Evidence Agent | E4 | A2-RO |
| **M08** | Shadow ActionIntent + Policy | E4 | A3-shadow |
| **M09** | Durable Approval + Controlled Executor | E4/E5-ready | approval-gated action |
| **M10** | Governed Canary | E5 | bounded RISK0/RISK1 auto; RISK2 approval |
| **M11** | Production Closed Loop | E6 | governed production |

Canonical progression:

```text
O00
→ M00 real evidence
→ M01 deterministic advice
→ M02 memory/replay
→ M03 human action + measurement
→ M04 grounded AI
→ M05 reviewed improvement
→ M06 automatic read-only
→ M07 agent read-only
→ M08 shadow action
→ M09 approved action
→ M10 bounded auto-action
→ M11 production closed loop
```

Mỗi Mission chỉ tăng một lớp capability/authority chính. Không vừa đổi domain model, runtime, AI và execution authority trong cùng một bước nếu không có evidence gate riêng.

## 4. Learner lesson layer

Learner-facing lesson mới nằm tại `curriculum/` và dùng ID theo Mission:

```text
BOOT.1
M00.1
M00.2
M00.3
M01.1
...
```

Bài `BOOT.1 — Chạy, sửa và kiểm thử Bot` là credit đã học từ pilot cũ; nó là tooling bootcamp, **không phải M00 business/reality gate**.

Numeric lesson IDs cũ trong `lessons/` chỉ là **reference knowledge library** trong giai đoạn cleanup. Learner mới không dùng `V2-LESSON-MAP.json` để xác định bài tiếp theo.

## 5. M00 — First Real Evidence Packet

M00 không cần Go, API key, n8n, AI, account automation hoặc publish.

Learner làm ba knowledge/practice cards đầu tiên:

1. `M00.1` — Affiliate Intelligence Bot đang tối ưu điều gì?
2. `M00.2` — Evidence, uncertainty và missing data.
3. `M00.3` — Decision ≠ Approval ≠ Execution.

Ship target:

```text
3+ public observations có source + observed_at
→ fact / estimate / assumption / unknown
→ audience/problem/offer hypothesis
→ Human DecisionPacket
→ decision state + missing evidence + next measurement
→ NO external execution
```

M00 PASS không yêu cầu sale, click hay publish.

## 6. Authority progression

```text
M00 human/read-only
→ M01–M02 A0 deterministic
→ M03 human executes
→ M04–M05 A1 advisory/propose
→ M06 automatic read-only
→ M07 A2 read-only tools
→ M08 A3-shadow
→ M09 approval-gated execution
→ M10 bounded governed automation
→ M11 governed production
```

Hành động có hậu quả đáng kể luôn đi qua deterministic policy/risk boundary. LLM/Agent không được tự assign high-risk action rồi tự authorize chính nó.

## 7. Implementation principles

```text
DETERMINISTIC CORE FIRST
!= CODE FIRST

NO-CODE WHEN AUDITABLE
CODE WHEN IT REDUCES AMBIGUITY OR FAILURE SURFACE
AGENT WHEN DETERMINISTIC LOGIC IS NOT ENOUGH
AUTOMATION ONLY AFTER EVIDENCE + POLICY + RECOVERY
```

Reference roles:

- Go: deterministic reference/fallback khi code là implementation rõ nhất;
- n8n: orchestration/integration/retry/approval routing khi có measured need;
- AgentRuntime: research/reasoning/tool use trong permission ceiling;
- policy/rule engine: deterministic authorization implementation nếu parity/fail-closed/reason/version gate đạt.

Vendor/framework không phải PASS gate.

## 8. Real Evidence Ladder

| Level | Bằng chứng |
|---|---|
| E0 | synthetic/test/replay; chỉ chứng minh plumbing/behavior |
| E1 | public observation thật có source + observed_at + access method |
| E2 | human external action thật có action record |
| E3 | outcome/analytics/export thật, kể cả observed value = 0 |
| E4 | Decision → Action → Outcome → Evaluation → reviewed proposal |
| E5 | bounded governed canary có policy/audit/kill switch |
| E6 | production loop qua observation window + recovery + reviewed improvement |

Sample không thể thay E1–E6.

## 9. PASS model

Một Mission chỉ PASS khi contract của chính Mission đạt cả ba lớp nếu áp dụng:

```text
Capability
+ Reality
+ Operated
```

`draft`, `ready`, CI xanh hoặc fixture PASS không tự tạo Reality PASS.

## 10. Reference knowledge inventory

Trong giai đoạn dọn migration, `ROADMAP.md` và `roadmap/part-00..06.md` vẫn giữ **7 phần · 21 chương · 63 bài học** làm reference knowledge inventory để không phá provenance/validator hiện hữu.

Tổng cộng: **7 phần · 21 chương · 63 bài học**.

Con số này **không phải reading order** và sẽ được thu gọn ở cleanup sau khi learner path Mission-based đã ổn định.

## 11. Authority order

1. `CURRICULUM.md` — canonical outcome/sequence/evidence/authority/PASS;
2. `curriculum/README.md` + `curriculum/<Mission>/` — learner path hiện hành;
3. active `missions/` files — execution contract;
4. `ROADMAP.md` / `roadmap/` — reference knowledge inventory;
5. ADR/operating standards — safety/quality detail;
6. `lessons/` numeric legacy knowledge + `sources/` — reference/provenance only.

Nếu hai file mâu thuẫn, file có authority thấp hơn phải được sửa hoặc demote; không tạo thêm mapping layer để che mâu thuẫn.
