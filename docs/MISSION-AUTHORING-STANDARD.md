# Tiêu chuẩn biên soạn Mission

Mission là đơn vị **try + build + run + observe + pull + improve + operate + evidence** và là progress gate chính.

## Metadata

~~~yaml
mission_id: "M00"
title: "..."
status: planned
curriculum_version: 2
release_kind: market_artifact # market_artifact | bot
requires_missions: []
bot_version_from: null
bot_version_to: "v0.0"
estimated_hours: 6
delivery:
  starter_paths: []
  eval_pack: null
  verification_commands: []
  pilot_status: untested # untested | validated
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: []
  reference: []
milestones:
  contributes_to: ["G1"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
~~~

Core Mission ready phải trỏ tới micro-lesson đã authored ready. Lesson chỉ cung cấp knowledge slice; Mission không tự đánh dấu lesson applied. `status: ready` chỉ là authoring state: phải dùng delivery metadata để nói starter/eval/pilot đã có hay chưa.

## Section bắt buộc

1. Ship Target;
2. Starting Bot State;
3. Try First;
4. Run;
5. Observe;
6. Knowledge Pull;
7. Improve;
8. Tests;
9. Reality Check;
10. Operate;
11. Failure Case;
12. Safety Gate;
13. Evidence;
14. Explain-back;
15. Mission PASS;
16. Bot Version Result;
17. Next Mission.

## Thiết kế checkpoint

Mission cho absolute beginner phải chia thành checkpoint khoảng 45–90 phút:

~~~text
TRY
→ observable output/gap
→ pull 1–3 micro-lessons
→ improve/test
→ run on required evidence
→ compare
→ save
~~~

Không đưa PostgreSQL, interface architecture, concurrency hoặc agent runtime vào trước khi failure/bottleneck thật tạo ra nhu cầu.

## Real evidence

Mission phải nói rõ:

- evidence kind tối thiểu;
- source/access method/observed_at;
- sample fallback có thể giúp phần nào;
- phần nào vẫn Evidence Pending;
- outcome window và pending/partial/final nếu có.

Không yêu cầu outcome nằm ngoài kiểm soát như sale để PASS.

## AI và authority

- human/deterministic baseline trước AI;
- evaluation trước authority;
- model output là untrusted input;
- Decision khác Execution;
- external authority chỉ tăng sau policy/risk/approval gate;
- Bot không tự sửa prompt/policy/weights trong production.

## Definition of Done

Mission ready phải có:

- starting state tái lập được;
- attempt trước knowledge;
- checkpoint vừa sức người mới;
- required lesson ready và link được;
- real-evidence contract rõ;
- happy/failure test;
- safety gate cụ thể;
- measurable Capability/Reality/Operated criteria;
- evidence/review path;
- không cần secret hoặc paid service để hoàn thành Core.

## V2 sequencing and promotion

V2 starts with M00 human-only market action, then M01 outcome snapshot in
parallel with M02 deterministic baseline; AI is first allowed at M04 as A1
advisory. Do not use v1 filename/lesson order as a v2 dependency.

Before a v2 Mission is promoted, it needs an auditable starter or manual-only
rationale, eval fixture/pack, reproducible verification commands, pilot actuals
and evidence refs. `python scripts/validate_readiness.py --strict` is the
metadata gate, not a substitute for human market-evidence review.
