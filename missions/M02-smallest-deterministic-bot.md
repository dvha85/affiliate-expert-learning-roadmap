---
mission_id: "M02"
title: "Smallest Deterministic Bot"
status: draft
curriculum_version: 2
release_kind: "bot"
requires_missions: ["M00"]
bot_version_from: null
bot_version_to: "v0.1"
estimated_hours: 8
delivery:
  starter_paths:
    - "starter-kits/M02-deterministic-baseline/"
    - "starter-kits/M02-operator-profile/"
    - "starter-kits/M02-go-builder/"
  eval_pack: "evals/M02-deterministic-baseline/"
  verification_commands:
    - "python scripts/validate_m02_deterministic_pack.py"
    - "python scripts/validate_m02_profile_parity.py"
  pilot_status: untested
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: ["0.2", "2.1", "2.2", "2.3"]
  reference: []
milestones:
  contributes_to: ["G2"]
evidence:
  minimum_level: "E1"
  reality_required: true
safety_gate: "S0"
risk_scope:
  external_side_effects: false
  execution_actor: "deterministic_only"
---

# Mission M02 — Smallest Deterministic Bot

## Ship Target — Mục tiêu bàn giao

Xây baseline tất định nhỏ nhất có thể audit cho observations/context đã có:

```text
known evidence fields
→ deterministic formula + stable tie-break
→ RANK_SCENARIO hoặc GET_MORE_DATA/HUMAN_REVIEW
→ reason + missing evidence + no action
```

M02 phát hành v0.1 của Bot, nhưng không gọi AI, model call hay tool. Output
chỉ là decision-shaped scenario; không phải publish, spend hay execution.

## Starting Bot State — Trạng thái Bot ban đầu

Dùng Operator/no-code rule card hoặc Go builder profile sau khi đã thử baseline.
Hai profile dùng cùng fixtures và phải có parity 100%; Go là golden oracle,
không phải entrypoint bắt buộc trước M00. Fixture synthetic là E0 để test
plumbing, không được đổi nhãn thành E1.

## Try First — Thử trước

Từ một subset public observations E1 đã có sau M00, human viết trước:

- fields source thực sự support;
- field nào missing/unknown;
- rule tối giản mình muốn thử;
- khi nào Bot phải GET_MORE_DATA thay vì rank.

Sau đó chạy fixture synthetic để thấy safe failure trước khi đọc theory/copy
formula. Không nhìn output Bot để backfill human assumption.

## Run — Chạy

```bash
python starter-kits/M02-deterministic-baseline/run_baseline.py \
  evals/M02-deterministic-baseline/rankable-observations.json
python scripts/validate_m02_deterministic_pack.py
python scripts/validate_m02_profile_parity.py
```

Thay input bằng summary/reference được phép dùng. Không đưa raw account data,
credential hoặc customer data vào fixture/commit.

## Observe — Quan sát

Ghi formula version, input/evidence refs, ranking, stable tie-break, reason,
missing evidence và state. `0` là observed value hợp lệ; `null`/missing dẫn tới
`GET_MORE_DATA`, không bị convert thành 0.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `0.2` cho real/synthetic, fact/estimate/assumption/unknown.
- `2.1–2.3` khi human-vs-Bot baseline, confidence/uncertainty và abstention
  cần được giải thích tốt hơn.

Không pull AI, database, scheduler hoặc provider integration trong M02.

## Improve — Cải tiến

Thêm một rule/rationale/validation vì gap cụ thể, bằng test trước. Formula phải
deterministic, input contract rõ và versioned. Không tối ưu rank để khớp sale,
không biến assumption thành measured fact và không auto-promote `RECOMMEND`.

## Tests — Kiểm thử

- rankable input có stable output `RANK_SCENARIO`;
- missing price/commission/provenance có `GET_MORE_DATA`, action null;
- observed zero khác missing;
- code/contract không có AI, model call, tool, write hay external execution.

## Reality Check — Kiểm chứng thực tế

Fixture chứng minh deterministic behavior E0. M02 Reality chỉ dùng E1 public
observation/source/time thật từ M00 hoặc evidence reuse có provenance phù hợp;
Bot output không tự tạo E1/E2/E3.

## Operate — Vận hành

Lưu input reference, formula version, output state/reason và missing evidence.
M03 sẽ giữ history/measurement append-only; M02 không tự persist long-term hay
fetch data.

## Failure Case — Tình huống lỗi

Missing/invalid evidence, mixed semantics, equal score, malformed input và
unknown values phải abstain/review rõ. Không dùng default 0 để tiếp tục rank.

## Safety Gate — Cổng an toàn

S0: deterministic local calculation only. Không gọi AI, model call, tool,
network, credential, file write ngoài output do human chủ động lưu, publish hay
external execution.

## Evidence — Bằng chứng

Lưu redacted input reference, command, formula version, Decision Context Card
và output. Dùng `templates/MISSION-EVIDENCE.md`; raw/private source giữ ngoài
Git. E0 eval fixture phải luôn được gắn synthetic/test.

## Explain-back — Giải thích lại

Learner giải thích được formula dùng fact nào, assumption/missing nào làm Bot
abstain, tại sao output là scenario chứ không phải permission, và vì sao AI
không thuộc M02.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Có baseline deterministic, stable tie-break, reason và abstention tests.

### Reality

- [ ] Chạy được với E1 source/public observation thật hoặc ghi rõ chỉ có E0
  engineering fixture; không claim fixture là market evidence.

### Operated

- [ ] Lưu output/input/formula version và next missing-evidence measurement.

## Bot Version Result — Kết quả phiên bản Bot

`v0.1`: deterministic advisory baseline, no AI/tool/action. M03 nâng thành
history/measurement v0.2 sau khi M01 và M02 đều có evidence/context.

## Next Mission — Mission tiếp theo

M03 — Trustworthy History & Measurement cần M01 + M02. AI chỉ xuất hiện ở M04.
