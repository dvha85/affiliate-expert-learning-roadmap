---
mission_id: "M02"
title: "Trustworthy History and Replay"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M01"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 8
delivery:
  starter_paths:
    - "starter-kits/M03-trustworthy-history/"
  eval_pack: "evals/M03-trustworthy-history/"
  verification_commands:
    - "python scripts/validate_m03_history_pack.py"
knowledge:
  required: []
  on_demand: []
  reference: ["3.1", "3.2", "3.3", "4.1", "4.2", "4.3"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
  execution_actor: "deterministic_only"
---

# Mission M02 — Trustworthy History and Replay

## Ship Target — Mục tiêu bàn giao

Nâng v0.1 thành v0.2 bằng history append-only cho Observation và DecisionPacket, có provenance, freshness, replay và correction semantics:

```text
M00 E1 evidence + M01 deterministic decision
→ append-only records
→ replay same input/version
→ same deterministic result
→ query history / compare / reconcile
```

M02 không fetch, publish, call AI/tool hay mutate evidence cũ tại chỗ.

## Starting Bot State — Trạng thái Bot ban đầu

M01 có deterministic baseline v0.1 và ít nhất một input/output trace. Starter/eval hiện tái sử dụng history pack trước reset; naming cũ chỉ là compatibility artifact, không thay Mission authority.

## Try First — Thử trước

Cố ý lưu t1 rồi overwrite bằng t2 và tự hỏi evidence nào biến mất. Sau đó thử replay cùng input + formula version và kiểm output có thay đổi không.

## Run — Chạy

```bash
python scripts/validate_m03_history_pack.py
```

Fixture synthetic chỉ kiểm behavior. Khi đưa E1 thật vào history, giữ provenance/reference và privacy boundary.

## Observe — Quan sát

Ghi `observation_id`, subject/reference, `observed_at`, `ingested_at`, formula/rule version, DecisionPacket state/reason, duplicate/conflict state và replay result.

## Knowledge Pull — Lấy kiến thức đúng lúc

`3.1–4.3` chỉ là reference khi identity, normalization, provenance, append-only, freshness hoặc reconciliation trở thành blocker thật.

## Improve — Cải tiến

Thêm test cho một failure đã thấy: exact duplicate idempotent, same ID different content → `HUMAN_REVIEW`, out-of-order evidence, correction record, restart/replay hoặc unknown freshness.

## Tests — Kiểm thử

- append-only, không overwrite canonical history;
- exact duplicate idempotent;
- identity conflict → review;
- replay cùng input/version → deterministic result;
- out-of-order query theo world/observed time hợp lệ;
- missing provenance/freshness → unknown/review;
- no AI/tool/external action.

## Reality Check — Kiểm chứng thực tế

E1 từ M00 có thể được lưu/replay; fixture E0 không được đổi nhãn thành E1. Outcome E3 chưa phải prerequisite của M02.

## Operate — Vận hành

Lưu ít nhất hai version/observation cycles hoặc một replay + correction/conflict case, cùng report giải thích result.

## Failure Case — Tình huống lỗi

Overwrite history, duplicate tạo record/action trùng, late arrival bị coi là fresh chỉ vì đến sau, missing provenance hoặc replay khác result mà không đổi version đều phải fail/review.

## Safety Gate — Cổng an toàn

S0 local deterministic persistence/replay. Không publish, account mutation, AI/tool/network action hay external execution.

## Evidence — Bằng chứng

Lưu append/replay commands, record refs, version, conflict/reconciliation result và limitation. Raw/private data ở ignored local storage.

## Explain-back — Giải thích lại

Learner phân biệt được `observed_at` và `ingested_at`, vì sao correction không overwrite, provenance support record nào và vì sao replay là nền móng cho eval/recovery sau này.

## Mission PASS — Tiêu chí PASS

### Capability
- [ ] Append/query/replay/reconcile deterministic history đúng invariant.

### Reality
- [ ] Nối được ít nhất E1 evidence thật từ M00 vào history hoặc ghi blocker trung thực.

### Operated
- [ ] Có replay/conflict/correction evidence và next measurement/action context cho M03.

## Bot Version Result — Kết quả phiên bản Bot

`v0.2`: deterministic history + replay foundation.

## Next Mission — Mission tiếp theo

M03 — First Tracked Human Action + Outcome Context.
