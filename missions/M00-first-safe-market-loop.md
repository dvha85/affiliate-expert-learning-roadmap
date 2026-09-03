---
mission_id: "M00"
title: "First Real Evidence Packet"
status: draft
curriculum_version: 2
release_kind: "market_artifact"
requires_missions: []
bot_version_from: null
bot_version_to: null
estimated_hours: 4
delivery:
  starter_paths:
    - "curriculum/M00/"
  eval_pack: null
  verification_commands: []
knowledge:
  required: []
  on_demand: []
  reference: []
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
  execution_actor: "none"
---

# Mission M00 — First Real Evidence Packet

## Ship Target — Mục tiêu bàn giao

Tạo observation/evidence packet thật cho một câu hỏi Affiliate nhỏ và một Human DecisionPacket có uncertainty/missing evidence rõ ràng.

```text
public observations E1
→ classify fact / estimate / assumption / unknown
→ human decision context
→ Human DecisionPacket
→ next measurement
→ NO external execution
```

## Learner cards

1. [`M00.1`](../curriculum/M00/M00.1-affiliate-intelligence-objective.md) — Bot đang tối ưu điều gì?
2. [`M00.2`](../curriculum/M00/M00.2-evidence-uncertainty.md) — evidence/uncertainty/missing.
3. [`M00.3`](../curriculum/M00/M00.3-decision-approval-execution.md) — Decision ≠ Approval ≠ Execution.

Không dùng numeric legacy lesson IDs làm reading order.

> `delivery.eval_pack: null` là có chủ đích: Mission đã có learner cards nhưng evaluator pack mới chưa được remap xong. `draft` không được nâng thành `ready` chỉ vì validator cấu trúc PASS.

## Starting state

Không cần Bot, Go, API key, n8n, Agent, affiliate account automation hay public publish. O00 synthetic walkthrough chỉ là orientation E0.

## Evidence bundle tối thiểu

Ít nhất 3 public observations thật, mỗi record có:

```text
source_url
observed_at
access_method
claim/value
claim_kind
limitation
```

Sau đó tạo Human DecisionPacket:

```text
question
supported_facts
assumptions
unknowns
decision_state: RANK_SCENARIO | GET_MORE_DATA | HUMAN_REVIEW
reason
missing_evidence
next_measurement
action: null
```

## Safety boundary

M00 không publish, spend, send, mutate account, scrape login-protected data hoặc execute external action.

```text
real source
!= permission to recommend

DecisionPacket
!= ActionIntent
!= Approval
!= Execution
```

Không dùng `RECOMMEND` chỉ vì evidence origin là `real`.

## Reality Check

E1 cần source công khai thật + `observed_at` + access method. Fixture/sample không được đổi nhãn để vượt gate.

## Failure cases

M00 phải fail/rework nếu:

- placeholder URL được gọi là E1;
- assumption được ghi thành fact;
- missing bị đổi thành observed zero;
- Bot/AI output được dùng để backfill evidence;
- DecisionPacket tạo external action;
- learner chọn offer chỉ vì commission cao nhất mà không ghi limitation.

## PASS

### Capability

- [ ] Tạo được evidence packet có provenance và uncertainty semantics đúng.
- [ ] Tạo được Human DecisionPacket có state/reason/missing evidence/next measurement.

### Reality

- [ ] Có ít nhất 3 public observations E1 thật, hoặc ghi `BLOCKED_EXTERNAL` trung thực nếu không thể quan sát source phù hợp.

### Operated

- [ ] Lưu packet/version và next measurement đủ để M01 dùng làm deterministic baseline input.

## Kết quả

`pre-bot`: M00 tạo market truth/context. Bot v0.1 bắt đầu ở M01.
