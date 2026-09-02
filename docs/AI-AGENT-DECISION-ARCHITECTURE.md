# Kiến trúc AI/Agent Decision Intelligence

> Tài liệu authority cho lớp AI/Agent của Build-First. Nó triển khai ranh giới trong [`../CURRICULUM.md`](../CURRICULUM.md), không định nghĩa một curriculum song song. Active spine là `M00–M11`; multi-agent/MCP chỉ là Advanced hoặc implementation option khi có use case thật.

## 1. Mục tiêu

Affiliate Intelligence Bot phải giúp learner ra quyết định tốt hơn bằng evidence, logic xác định và AI phù hợp. “Thông minh” được chứng minh bằng chất lượng quyết định, khả năng nói không biết và outcome trace; “tự động” là authority tăng dần qua policy, không phải quyền được trao vì model trả lời tự tin.

```text
REAL EVENT / DATA
→ Provenance + Freshness + Quality Gate
→ Deterministic Baseline
→ Grounded AI Analysis khi có decision value
→ Evidence Escalation qua read-only tools khi được phép
→ DecisionPacket hoặc ABSTAIN
→ ActionIntent
→ Policy + Risk + Approval/Revalidation
→ Bounded Action
→ Outcome
→ Evaluation + Proposed Improvement
→ Test / Review / Approved Release
↺
```

## 2. Các invariant bắt buộc

```text
DATA > OPINION
MODEL OUTPUT = UNTRUSTED INPUT
DECISION ≠ EXECUTION
AI ADVICE ≠ EXECUTION AUTHORITY
POLICY BEFORE CONSEQUENTIAL ACTION
OUTCOME LEARNING ≠ SILENT SELF-MODIFICATION
```

- deterministic rule/formula là baseline khi bài toán diễn đạt rõ bằng logic xác định;
- AI dùng để hiểu dữ liệu phi cấu trúc, tổng hợp evidence, tạo hypothesis và điều tra trong vùng cho phép;
- RiskLevel và PolicyDecision không giao cho LLM làm authority duy nhất;
- RISK2 luôn cần durable Human Approval và revalidation trước execute;
- AI unavailable/invalid/unsupported phải đi vào fallback hoặc abstain, không âm thầm tạo scoring fact;
- sample output chỉ chứng minh engineering behavior, không chứng minh market intelligence;
- learning loop chỉ tạo proposed improvement qua test, review và version mới.

## 3. Capability progression trong M00–M11

| Level | Phạm vi | Authority | Mission |
|---|---|---|---|
| **A0** | Deterministic evidence/decision core | không AI, không external Bot action | M00–M01; baseline bắt buộc cho các Mission sau |
| **A1** | Grounded AI advisory | phân tích/đề xuất; human vẫn quyết định và tự publish | M02–M07 |
| **A2** | Read-only evidence agent | gọi explicit read tools theo schema/permission/audit | M08 |
| **A3-S** | Shadow action + durable approval | tạo ActionIntent và dry-run; không execute consequential action | M09 |
| **A3-G** | Limited governed automation | RISK0/RISK1 bounded canary; RISK2 cần durable approval | M10–M11 |

```text
AI APPEARS AFTER A REAL-EVIDENCE BASELINE
≠
AI GETS EXTERNAL AUTHORITY
```

MCP, A2A và multi-agent không phải Core dependency. Chúng nằm ở Advanced A09/Reference và chỉ được đưa vào implementation khi giải quyết một bottleneck đã quan sát được mà không phá cùng security boundary.

## 4. Bốn contract xuyên suốt

```text
SignalPacket
→ AnalysisPacket
→ DecisionPacket
→ ActionIntent
```

### SignalPacket

Fact đã được hệ thống phát hiện, có provenance và freshness.

```yaml
subject: product:P123
event: commission_changed
before: 0.12
after: 0.18
detected_at: 2026-08-29T08:00:00+07:00
source_ref: snapshot:abc
freshness_seconds: 30
```

### AnalysisPacket

Kết quả phân tích có thể chứa AI reasoning nhưng phải gắn evidence và uncertainty.

```yaml
summary: commission tăng đáng kể
possible_causes: []
evidence_refs: []
missing_evidence: []
confidence: 0.82
uncertainty: []
recommended_investigation: []
```

### DecisionPacket

Kết quả hợp nhất deterministic signals, AI assessment, freshness và risk/policy context. Contract chi tiết nằm trong [`DECISION-CONTRACTS.md`](DECISION-CONTRACTS.md). Decision hợp lệ có thể là `WAIT`, `GET_MORE_DATA`, `HUMAN_REVIEW` hoặc `ABSTAIN`.

### ActionIntent

Ý định hành động trước execution. ActionIntent chưa phải permission. Nó phải giữ evidence ref, target, parameters, expiry, idempotency key, requested risk và expected outcome rồi đi qua Policy/Risk boundary.

## 5. Mission-first và practice-first

Mỗi capability AI/Agent phải được học theo vòng:

```text
attempt trên evidence thật hoặc sample được gắn nhãn
→ run baseline
→ observe gap/failure
→ pull tối đa ba micro-lessons
→ add AI/tool behavior
→ test valid + invalid + unavailable + adversarial path
→ compare với human/baseline
→ save technical + business evidence
```

Không bắt learner học toàn bộ LLM/agent stack trước M02. Không đưa tool agent vào trước khi learner đã thấy grounded advisory có thể sai. Không đưa automation vào trước khi có real tracked outcome và explicit action boundary.

## 6. Event-driven decision

Không dùng mẫu mặc định:

```text
cron → hỏi LLM toàn bộ dữ liệu liên tục
```

Ưu tiên:

```text
deterministic event/change
→ material change?
→ collect required evidence
→ invoke AI/decision workflow khi expected decision value đủ lớn
```

Trigger điển hình:

- state changed;
- anomaly detected;
- threshold crossed;
- freshness expired;
- experiment completed;
- outcome reconciled;
- approval completed;
- policy/platform snapshot changed.

Mục tiêu là giảm latency khi có thay đổi thật, đồng thời giảm model cost, repeated work và alert noise.

## 7. Decision Fusion và evidence escalation

```text
Rules / scoring / ranking
+ real outcome and experiment evidence
+ grounded AnalysisPacket
→ conflict and freshness check
→ enough evidence?
   ├─ YES → DecisionPacket
   └─ NO  → allowed read tools hoặc ABSTAIN
```

AI không được âm thầm override rule/policy. Conflict phải xuất hiện dưới dạng evidence, confidence, uncertainty, missing evidence hoặc request lấy thêm dữ liệu.

## 8. Provider-neutral domain core

Core Go application dùng provider-neutral interface. Không để provider SDK type lan vào Signal/Analysis/Decision/Policy/Action domain model.

Provider-specific model routing, deferred tool loading, programmatic tool calling hoặc hosted workflow là implementation option thuộc config/freshness layer. Thay provider không được làm đổi business truth hay permission boundary.

## 9. Tool và safety boundary

```text
A0/A1: no external AI authority
A2: explicit read-only tools + schema + least privilege + audit
A3-S: ActionIntent + policy simulation + durable approval
A3-G: bounded executor + revalidation + idempotency + kill switch
```

Mọi external content từ web/product/review/email/API/RAG/MCP đều là untrusted input. Tool description và tool output cũng không được coi là instruction có authority.

Publish, spend, account/security change, destructive delete và consequential communication không được free-orchestrate. Chúng phải có risk classification, policy decision, approval khi cần, revalidation và execution record.

## 10. Mapping vào Mission và Real Evidence Ladder

| Mission | AI/Agent outcome | Evidence gate |
|---|---|---|
| M00 | no AI/Bot; human-only safe market loop | E1→E2 public observation + manual tracked publish |
| M01 | no AI/Bot; first outcome snapshot | E3 real analytics/export; zero khác missing |
| M02 | smallest deterministic baseline | evidence/context + abstain behavior test |
| M03 | trustworthy history/change baseline | provenance/freshness/reconcile, không overwrite |
| M04 | grounded AI advisor với schema/eval/fallback | claim có evidence ref; invalid/unavailable path được test |
| M05 | outcome tạo proposed improvement | E4 decision/action/outcome/review trace |
| M06 | reliable automatic watcher | retry, duplicate, timeout và recovery evidence |
| M07 | DecisionPacket + confidence/uncertainty/abstain | stale/missing/conflicting cases |
| M08 | read-only evidence agent | explicit tool permission, trace và no side effect |
| M09 | ActionIntent + approval + shadow execution | durable approval/rejection/revalidation records |
| M10 | limited governed canary | E5 bounded RISK0/RISK1 + kill-switch evidence |
| M11 | production closed loop | E6 operated trace + recovery + reviewed improvement |

## 11. Bốn Milestone Gate

- **G1 — M00:** first safe human market loop;
- **G2 — M01–M03:** outcome snapshot, deterministic baseline và trustworthy history;
- **G3 — M04–M05:** grounded advisory và reviewed improvement;
- **G4 — M06–M11:** reliable, governed production loop.

Authority không được tăng chỉ vì Capability PASS. Mission phải có Reality verified, Operated và đạt gate trước đó; outcome có thể `zero`, `negative` hoặc `inconclusive` miễn measurement trung thực.

## 12. Quy tắc thay đổi

Nếu framework, protocol hoặc provider capability thay đổi, ưu tiên cập nhật [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md), adapter và test. Không tự đổi Core/Mission hay policy authority vì một vendor feature mới.

Nếu learner pilot cho thấy một capability đến quá sớm, quá muộn hoặc không được dùng, sửa `CURRICULUM.md` qua ADR/review dựa trên evidence; không giữ số lượng chỉ để bảo toàn inventory.
