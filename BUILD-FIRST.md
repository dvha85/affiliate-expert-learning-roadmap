# Build-First, Reality-First — Mission-based

> Canonical sequence: [`CURRICULUM.md`](CURRICULUM.md). Đây là execution model cho learner path hiện hành; historical numeric lesson mapping không được ghi đè Mission spine.

## Learner loop

```text
DO A SMALL THING A REAL PERSON CAN VERIFY
→ observe the gap
→ pull the smallest useful knowledge slice
→ improve/test
→ save evidence
→ explain limitations
→ choose the next measurement
```

O00 là synthetic walkthrough, không PASS. M00 là first Reality candidate nhưng **không Publish-First**: learner thu public observations E1 và tạo Human DecisionPacket, không external execution.

M01 tạo deterministic Bot v0.1; M02 thêm trustworthy history/replay. M03 mới là external action đầu tiên, do human review và tự execute, có tracking/measurement context. AI xuất hiện ở M04 dưới dạng grounded advisory, không tool/write/execute.

## Evidence taxonomy

- origin/eligibility: `real | synthetic`;
- use context khi relevant: `test | replay`;
- claim: `fact | estimate | assumption | unknown`;
- `0`, `missing`, `pending`, `not_yet_observable`, `inconclusive` là state khác nhau.

Synthetic data hữu ích cho test/replay nhưng không chứng minh market reality.

## Authority progression

```text
M00 human/read-only evidence + DecisionPacket
→ M01 A0 deterministic Bot
→ M02 A0 history/replay
→ M03 human-only external action + measurement
→ M04–M05 A1 advisory/propose-only
→ M06 automatic read-only watcher
→ M07 A2 read-only tools
→ M08 A3 shadow ActionIntent/policy
→ M09 approval-gated execution
→ M10 bounded governed automation
→ M11 governed production
```

Invariant:

```text
Decision != Approval != Execution
AI confidence != execution permission
real evidence != automatic recommendation
Agent proposal != authorization
```

## Implementation principle

```text
DETERMINISTIC CORE FIRST
!= CODE FIRST

NO-CODE WHEN AUDITABLE
CODE WHEN IT REDUCES AMBIGUITY
AGENT WHEN DETERMINISTIC LOGIC IS NOT ENOUGH
AUTOMATION ONLY AFTER POLICY + AUDIT + RECOVERY
```

Go là deterministic reference/fallback khi code phù hợp. n8n có thể orchestration. AgentRuntime cung cấp intelligence trong permission ceiling. Không tool/runtime nào tự trở thành source of truth hay policy authority.

## Delivery vs learner PASS

Mỗi Mission khai báo authoring/delivery riêng. `draft`, `ready`, fixture PASS hoặc CI xanh không tự tạo Reality/PASS. Mission PASS phải theo Capability + Reality + Operated contract của Mission đó.

## External action boundary

External action đầu tiên thuộc M03:

```text
review exact action
→ disclosure/policy/tracking check khi áp dụng
→ human manual execution
→ ActionRecord
→ outcome window
```

Từ M09 trở đi, machine execution chỉ được mở qua deterministic policy/risk, durable approval khi cần, revalidation, idempotency, audit và kill switch.
