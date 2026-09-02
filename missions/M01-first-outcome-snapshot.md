---
mission_id: "M01"
title: "First Outcome Snapshot"
status: draft
curriculum_version: 2
release_kind: "market_artifact"
requires_missions: ["M00"]
bot_version_from: null
bot_version_to: null
estimated_hours: 4
delivery:
  starter_paths:
    - "starter-kits/M01-outcome-snapshot/"
  eval_pack: "evals/M01-outcome-snapshot/"
  verification_commands:
    - "python scripts/validate_m01_outcome_snapshot_pack.py"
  pilot_status: untested
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: ["7.2", "7.3"]
  reference: []
milestones:
  contributes_to: ["G2"]
evidence:
  minimum_level: "E3"
  reality_required: true
safety_gate: "S1"
risk_scope:
  external_side_effects: false
  execution_actor: "human_only"
---

# Mission M01 — First Outcome Snapshot

## Ship Target — Mục tiêu bàn giao

Tạo một **read-only outcome snapshot thật** cho action/tracking context từ M00:

```text
M00 action/reference + declared window
→ human reads analytics/export
→ metric + status + provenance + limitation
→ E3 snapshot, kể cả zero/pending/inconclusive
```

M01 không publish thêm, không yêu cầu sale và không phát hành Bot. Analytics,
export hay outcome thật là input; không dùng synthetic metric để gọi E3.

## Starting Bot State — Trạng thái Bot ban đầu

`pre-bot`. Dùng `starter-kits/M01-outcome-snapshot/`; chỉ cần access hợp lệ,
read-only vào analytics/export hoặc public measurement context đã dùng ở M00.
Không cần API key, scraping, Go hay AI.

## Try First — Thử trước

Trong 30–60 phút, nhìn source measurement trước khi đọc lesson. Ghi metric đầu
tiên source thực sự cho thấy, `observed_at`, window và câu trả lời thật cho:

```text
zero? pending? missing? partial? inconclusive?
```

Nếu không có access/export hoặc window chưa mở, ghi `BLOCKED_EXTERNAL` hay
`pending`; không điền `0` để làm snapshot trông complete.

## Run — Chạy

```bash
python scripts/validate_m01_outcome_snapshot_pack.py
```

Copy `starter-kits/M01-outcome-snapshot/M01-OUTCOME-SNAPSHOT.md` vào local
private evidence path, điền bằng analytics/export thật, rồi validate bản
redacted summary trước review:

```bash
python scripts/validate_m01_outcome_snapshot_pack.py --snapshot artifacts/local/m01-outcome-snapshot.md
```

## Observe — Quan sát

Ghi source/reference, `observed_at`, `window_start`, `window_end`, metric/scope,
`outcome_status`, `observed_value`, missing fields và attribution limitation.
Tách `0` quan sát được khỏi missing, pending và not_yet_observable.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `7.2` khi chưa phân biệt được observation window, zero, missing và pending.
- `7.3` khi cần import analytics/export, provenance hoặc reconciliation.

Chỉ pull slice giải quyết gap vừa thấy, sau đó quay lại snapshot thật.

## Improve — Cải tiến

Sửa scope/window, source reference hoặc label status để người review có thể
hiểu đúng. Không sửa raw metric, bịa attribution hay cộng nhiều source không
reconcile. Cải tiến ở M01 là evidence quality, không phải tối ưu content/action.

## Tests — Kiểm thử

- valid structural pack có real source, time/window, status, value semantics và
  no-action/read-only boundary;
- synthetic/test metric, missing provenance, `pending = 0` hoặc missing/zero
  bị gộp phải fail;
- raw/private analytics không được commit vào evidence summary.

## Reality Check — Kiểm chứng thực tế

E3 chỉ đến từ analytics/export/outcome thật có provenance. A fixture trong
`evals/` chỉ kiểm schema; nó không chứng minh account/channel hay outcome của
learner. Không có result dương vẫn hoàn thành Reality nếu snapshot trung thực.

## Operate — Vận hành

Đặt next observation window/reference. Nếu result là `pending`, ghi thời điểm
đọc lại; nếu `inconclusive`, ghi missing measurement quyết định nào cần trước
khi M03 xây history/reconcile.

## Failure Case — Tình huống lỗi

Platform report trễ, attribution không rõ, export bị deny, metric missing,
window overlap hoặc privacy restriction đều phải giữ status/limitation rõ,
không suy diễn revenue/conversion.

## Safety Gate — Cổng an toàn

S1 read-only: human_only chỉ đọc/export dữ liệu được phép. Không share
credential, không scrape trái policy, không thay attribution/account setting
và không tạo external side effect.

## Evidence — Bằng chứng

Dùng `starter-kits/M01-outcome-snapshot/M01-OUTCOME-SNAPSHOT.md`,
`templates/MEASUREMENT-CONTEXT.md`, `templates/OUTCOME-SNAPSHOT.md`,
`templates/REDACTED-EVIDENCE-SUMMARY.md` và
[M01 contract](../docs/M01-OUTCOME-SNAPSHOT-CONTRACT.md). Raw export giữ local
private; commit summary đã redact cùng limitation/reference.

## Explain-back — Giải thích lại

Learner giải thích được vì sao `0` khác `pending`, source nào support value,
window/scope giới hạn kết luận gì và measurement nào phải có trước M03.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Tạo và review được one outcome snapshot có status/value semantics đúng.

### Reality

- [ ] Có E3 analytics/export/outcome thật, hoặc `BLOCKED_EXTERNAL`/pending được
  ghi trung thực kèm source/access limitation.

### Operated

- [ ] Có next observation/reconciliation step cho M03; không có action mới.

## Bot Version Result — Kết quả phiên bản Bot

`pre-bot`: M01 tạo measurement context thật. M02 có thể làm song song, nhưng
M03 chỉ bắt đầu khi có cả snapshot M01 và baseline M02.

## Next Mission — Mission tiếp theo

M02 — Smallest Deterministic Bot chạy song song sau M00; M03 nối M01 + M02
thành history/measurement đáng tin.
