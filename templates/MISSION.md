---
mission_id: "MXX"
title: "Tên Mission"
status: planned
curriculum_version: 2
release_kind: market_artifact # market_artifact | bot
requires_missions: []
bot_version_from: null
bot_version_to: "vX.Y"
estimated_hours: 6
delivery:
  starter_paths: []
  eval_pack: null
  verification_commands: []
knowledge:
  required: []
  on_demand: []
  reference: []
milestones:
  contributes_to: []
evidence:
  minimum_level: "E0"
  reality_required: false
safety_gate: "S0"
risk_scope:
  external_side_effects: false
---

# Mission MXX — Tên Mission

## Ship Target — Mục tiêu bàn giao

Nêu một capability có thể demo và evidence level phải đạt. `status: ready` chỉ
có nghĩa Mission đã được biên soạn. Delivery metadata chỉ mô tả starter, eval
và verification có thể kiểm trong repository; personal execution nằm local.

## Starting Bot State — Trạng thái Bot ban đầu

Chỉ learner state từ Mission trước; reference không phải starting state.

## Try First — Thử trước

Cho learner chạy/thử/ra human judgment trước khi đọc theory. Chia checkpoint 45–90 phút.

## Run — Chạy

Lệnh/input/output có thể quan sát.

## Observe — Quan sát

Ghi expected, observed, failure/gap và evidence kind.

## Knowledge Pull — Lấy kiến thức đúng lúc

- Required: tối đa vài micro-lesson giải quyết gap hiện tại.
- On-demand: chỉ mở khi blocker xuất hiện.
- Reference: không phải PASS gate.

## Improve — Cải tiến

Áp dụng knowledge vào đúng artifact vừa chạy.

## Tests — Kiểm thử

Happy path và failure cases tương xứng scope.

## Reality Check — Kiểm chứng thực tế

Nêu E-level, source/access method, sample fallback, outcome window và điều kiện Evidence Pending.

## Operate — Vận hành

Số cycle/window/restart cần quan sát.

## Failure Case — Tình huống lỗi

Ít nhất một invalid/stale/missing/conflicting/permission/failure case.

## Safety Gate — Cổng an toàn

Nêu S-level, authority ceiling và prohibited action.

## Evidence — Bằng chứng

Lưu Observation → HumanPrediction → BotDecision → Action/Intent → Outcome/Evaluation tùy scope, kèm version.

## Explain-back — Giải thích lại

Rubric phải kiểm correctness, causal reasoning, evidence, limitation và next measurement.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] ...

### Reality

- [ ] ...

### Operated

- [ ] ...

## Bot Version Result — Kết quả phiên bản Bot

Nêu capability mới và authority ceiling.

## Next Mission — Mission tiếp theo

Nêu Mission sau và gap sẽ được mở.
