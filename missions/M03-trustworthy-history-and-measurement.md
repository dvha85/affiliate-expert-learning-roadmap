---
mission_id: "M03"
title: "Trustworthy History and Measurement"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M01", "M02"]
bot_version_from: "v0.1"
bot_version_to: "v0.2"
estimated_hours: 10
delivery:
  starter_paths:
    - "starter-kits/M03-trustworthy-history/"
  eval_pack: "evals/M03-trustworthy-history/"
  verification_commands:
    - "python scripts/validate_m03_history_pack.py"
  pilot_status: untested
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: ["3.1", "3.2", "3.3", "4.1", "4.2", "4.3"]
  reference: []
milestones:
  contributes_to: ["G2"]
evidence:
  minimum_level: "E3"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
  execution_actor: "deterministic_only"
---

# Mission M03 — Trustworthy History and Measurement

## Ship Target — Mục tiêu bàn giao

Nâng v0.1 thành v0.2: append-only history cho snapshots M01, với provenance,
freshness và missing semantics có thể query/reconcile:

```text
M01 E3 snapshot + M02 baseline context
→ append-only record
→ same-subject historical query / compare
→ freshness using explicit as_of + policy
→ changed / unchanged / missing / unknown / review
```

M03 không fetch, publish, call AI/tool hay đổi evidence cũ tại chỗ.

## Starting Bot State — Trạng thái Bot ban đầu

M01 có one outcome snapshot/read-only measurement context và M02 có v0.1
deterministic baseline. Bắt đầu ở `starter-kits/M03-trustworthy-history/`;
JSONL là profile nhỏ nhất để thấy behavior, không phải yêu cầu dùng database.

## Try First — Thử trước

Trước khi đọc architecture, cố ý lưu một snapshot t1, overwrite bằng t2, rồi
trả lời: evidence nào đã mất? Nếu một source đến muộn nhưng `observed_at` cũ
hơn, arrival order có biến nó thành world-time mới hơn không? Ghi gap.

## Run — Chạy

```bash
python scripts/validate_m03_history_pack.py
```

Starter có thể được gọi từ local private workspace; chỉ đưa fixture synthetic
hoặc redacted records vào Git. Exact command không phải contract; invariants là
append-only, provenance, freshness và missing.

## Observe — Quan sát

Ghi `subject_id`, `observation_id`, `observed_at`, `ingested_at`, provenance
reference, missing fields, duplicate/conflict state, query order và freshness
inputs. `observed_at` khác `ingested_at`; late evidence không được bị drop chỉ
vì out-of-order.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `3.1–3.3` khi identity, validation, normalization hoặc provenance yếu.
- `4.1–4.3` khi overwrite, append-only, delta, freshness, restart hoặc second
  observation cycle bộc lộ gap.

Không kéo scheduler/watcher/AI vào để che một history contract chưa đúng.

## Improve — Cải tiến

Thêm validation/test cho one observed failure: duplicate exact idempotent,
conflicting ID `HUMAN_REVIEW`, copy-on-append, sorting by observed time hoặc
explicit freshness policy. Correction là record mới/reference review, không
overwrite history.

## Tests — Kiểm thử

- append snapshot rồi restart/query giữ đủ history append-only;
- exact duplicate idempotent, same ID different content conflict;
- out-of-order arrival vẫn query theo `observed_at`;
- provenance/missing bắt buộc; freshness unknown khi thiếu policy;
- không AI/tool/action/network/write external.

## Reality Check — Kiểm chứng thực tế

E3 đến từ M01 analytics/export/outcome thật. History fixture synthetic chỉ
kiểm behavior; không thể relabel thành learner E3. Real record phải retain
provenance/access limitation và privacy boundary.

## Operate — Vận hành

Mỗi run lưu input reference, append result, conflict/reconciliation decision,
`as_of`/policy và report. Khi conflict/missing không resolve được, return
`HUMAN_REVIEW`/`GET_MORE_DATA`, không silently choose a row.

## Failure Case — Tình huống lỗi

Invalid timestamp, same ID content khác, missing provenance, mixed scope/unit,
late arrival, stale record và no policy phải reject/quarantine/review/unknown.

## Safety Gate — Cổng an toàn

S0 local deterministic. Không publish, change account, call AI/tool/network,
share credential hay mutate external system. `write` ở đây chỉ là local
append-only learner-owned history, không phải external execution.

## Evidence — Bằng chứng

Dùng `[M03 contract](../docs/M03-MEASUREMENT-HISTORY-CONTRACT.md)`, starter
pack và `templates/MISSION-EVIDENCE.md`. Raw analytics/history ở private path;
commit redacted reference plus command/output/limitation.

## Explain-back — Giải thích lại

Learner phải phân biệt subject/observation/ingested time, lý do correction
không overwrite, provenance nào support record và khi nào freshness là unknown.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Query/append/reconcile deterministic history đúng invariant và có tests.

### Reality

- [ ] Nối được M01 E3 source thật vào history hoặc ghi evidence access/blocker
  trung thực; fixture không được claim E3.

### Operated

- [ ] Có query/reconciliation/freshness report và next measurement/review path.

## Bot Version Result — Kết quả phiên bản Bot

`v0.2`: deterministic history/measurement foundation. M04 mới thêm grounded
AI advisory, không thay evidence/history truth.

## Next Mission — Mission tiếp theo

M04 — Grounded AI Advisor với evidence refs, fallback và no tool/write/execute.
