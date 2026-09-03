---
mission_id: "M03"
title: "First Tracked Human Action and Outcome Context"
status: draft
curriculum_version: 2
release_kind: "market_artifact"
requires_missions: ["M02"]
bot_version_from: "v0.2"
bot_version_to: "v0.3"
estimated_hours: 8
delivery:
  starter_paths:
    - "templates/"
  eval_pack: null
  verification_commands: []
knowledge:
  required: []
  on_demand: []
  reference: ["6.1", "6.2", "7.1", "7.2", "7.3"]
evidence:
  minimum_level: "E3"
  reality_required: true
safety_gate: "S2"
risk_scope:
  external_side_effects: true
  execution_actor: "human_only"
---

# Mission M03 — First Tracked Human Action and Outcome Context

## Ship Target — Mục tiêu bàn giao

Thực hiện **một external action nhỏ do con người review và tự thực hiện**, có tracking/measurement context để sau đó đọc outcome thật:

```text
M00 evidence + M01 decision + M02 replayable history
→ exact artifact/action intent written by human
→ disclosure/policy/tracking review khi áp dụng
→ human manual execution
→ ActionRecord E2
→ declared measurement window
→ first real outcome snapshot E3 khi observable
```

Bot/AI không execute. M03 là điểm đầu tiên chương trình cho phép external side effect.

## Starting Bot State — Trạng thái Bot ban đầu

Bot v0.2 có deterministic decision + history/replay. Human chọn một action nhỏ, reversible/low-spend (mặc định no paid spend), trên account/channel mình kiểm soát.

## Try First — Thử trước

Freeze trước khi hành động:

- exact artifact/action;
- source/evidence refs;
- disclosure/claim/rights/policy checks khi áp dụng;
- tracking/measurement context;
- outcome window;
- điều gì sẽ khiến bạn không execute.

## Run — Chạy

M03 không có auto-executor command. Human review exact version rồi tự publish/send/perform action đúng scope. Sau action, lưu `ActionRecord` và measurement reference.

## Observe — Quan sát

Ghi action/version, actor, executed_at, external reference, tracking ID/context, outcome window, policy limitation và first observable outcome state:

```text
0 | missing | pending | not_yet_observable | inconclusive | observed value
```

## Knowledge Pull — Lấy kiến thức đúng lúc

Numeric cards cũ chỉ là reference cho audience/claim/disclosure/tracking/measurement khi blocker thật xuất hiện.

## Improve — Cải tiến

M03 không tự tối ưu từ một outcome. Chỉ sửa readiness/tracking/data-quality gap trước action kế tiếp. Outcome-driven change proposal thuộc M05.

## Tests — Kiểm thử

- action phải do `human_only` execute;
- exact reviewed version phải khớp executed version;
- missing disclosure/tracking/policy requirement phải block khi applicable;
- synthetic click/order/outcome không được gọi là E2/E3;
- pending không được đổi thành 0;
- Bot/AI execution attempt phải fail.

## Reality Check — Kiểm chứng thực tế

E2 cần external action thật do human thực hiện. E3 cần analytics/export/outcome thật có provenance; zero là hợp lệ nếu thực sự được quan sát.

Nếu không có safe account/channel/access, ghi `BLOCKED_EXTERNAL`; không dùng fixture để vượt gate.

## Operate — Vận hành

Ít nhất một ActionRecord + declared outcome window. Nếu window chưa kết thúc, giữ `pending` và ghi next read time.

## Failure Case — Tình huống lỗi

Publish version khác bản review, tracking thiếu, policy/disclosure chưa rõ, account không thuộc quyền kiểm soát, paid spend ngoài scope, fake engagement/outcome, hoặc Bot/AI execute đều phải block.

## Safety Gate — Cổng an toàn

S2: external side effect được phép **chỉ bởi human_only**. Không credential sharing, spam, login scraping, auto-publish hay silent account mutation.

## Evidence — Bằng chứng

Dùng các template phù hợp trong `templates/` để lưu Market/Action/Measurement/Outcome context. Raw analytics/PII/credentials giữ ở private ignored path; commit chỉ redacted summary/reference.

## Explain-back — Giải thích lại

Learner giải thích được vì sao M03 mới mở external action, vì sao human execution khác approval/decision, tracking đang nối action với outcome thế nào và limitation attribution nào còn tồn tại.

## Mission PASS — Tiêu chí PASS

### Capability
- [ ] Freeze/review exact action và measurement context trước execution.
- [ ] Lưu ActionRecord + outcome state đúng semantics.

### Reality
- [ ] Có E2 human external action thật và E3 outcome snapshot khi observable, hoặc blocker/pending được ghi trung thực.

### Operated
- [ ] Có next measurement/read time và history linkage để M04 dùng grounded evidence.

## Bot Version Result — Kết quả phiên bản Bot

`v0.3`: tracked human-action/outcome context. Bot vẫn không có external execution authority.

## Next Mission — Mission tiếp theo

M04 — Grounded AI Advisor.
