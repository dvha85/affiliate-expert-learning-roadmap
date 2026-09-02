---
mission_id: "M00"
title: "First Safe Market Loop"
status: draft
curriculum_version: 2
release_kind: "market_artifact"
requires_missions: []
bot_version_from: null
bot_version_to: null
estimated_hours: 8
delivery:
  starter_paths:
    - "starter-kits/M00-safe-market-loop/"
  eval_pack: "evals/M00-safe-market-loop/"
  verification_commands:
    - "python scripts/validate_m00_market_loop_pack.py"
  pilot_status: untested
  pilot_evidence_refs: []
knowledge:
  required: []
  on_demand: ["6.1", "6.2", "7.1"]
  reference: []
milestones:
  contributes_to: ["G1"]
evidence:
  minimum_level: "E2"
  reality_required: true
safety_gate: "S2"
risk_scope:
  external_side_effects: true
  execution_actor: "human_only"
---

# Mission M00 — First Safe Market Loop

## Ship Target — Mục tiêu bàn giao

Human tự tạo, review và **manual publish** một micro-artifact Affiliate nhỏ
trên channel/account mình kiểm soát, có public observation E1, disclosure và
tracking context phù hợp. E2 chỉ có sau action record thật; zero/no outcome là
trạng thái hợp lệ, không cần sale.

```text
public observation E1
→ human hypothesis + exact-artifact review
→ disclosure + tracking check
→ human manual publish
→ E2 action record + next measurement
```

Bot/AI không có quyền publish, external execution, credential hay account
authority trong M00.

## Starting Bot State — Trạng thái Bot ban đầu

Không cần Bot, Go, API key hay account automation. Bắt đầu từ
`starter-kits/M00-safe-market-loop/`; O00 chỉ giúp nhìn loop synthetic và
không thay evidence M00.

## Try First — Thử trước

Trong 45–90 phút, chọn một offer/source công khai được phép quan sát. Viết bằng
lời của bạn: audience/problem, claim yếu nhất, channel và điều gì cần đo sau
publish. Chưa đọc framework dài hoặc gọi AI.

Nếu không có account/channel đủ điều kiện, ghi `BLOCKED_EXTERNAL`, lưu reason
và **không** đổi sample/fixture thành `real` để vượt gate.

## Run — Chạy

```bash
python scripts/validate_m00_market_loop_pack.py
```

Khi có evidence summary đã redact, kiểm local file trước khi review/publish:

```bash
python scripts/validate_m00_market_loop_pack.py --evidence artifacts/local/m00-evidence-summary.md
```

Raw export, credential, personal/customer data và screenshot nhạy cảm ở local
private storage; commit chỉ summary/reference đã redact.

## Observe — Quan sát

Ghi source/access method/observed_at, fact/estimate/assumption/unknown, lý do
chọn content hypothesis, disclosure/tracking, action URL/reference và outcome
window. Giữ `missing`, `zero`, `pending` và `inconclusive` tách biệt.

## Knowledge Pull — Lấy kiến thức đúng lúc

- On-demand `6.1` khi claim/audience hypothesis yếu.
- On-demand `6.2` khi disclosure/policy context chưa rõ.
- On-demand `7.1` khi chưa tạo được tracking/measurement context tối thiểu.

Không cần hoàn thành lesson nào trước attempt; pull một slice rồi quay lại
artifact thật.

## Improve — Cải tiến

Sửa claim, disclosure, CTA hoặc tracking context theo gap quan sát được. Chỉ
human sửa/review exact artifact; AI (nếu dùng ngoài scope để brainstorming)
không được tự publish hay được coi là evidence/policy authority.

## Tests — Kiểm thử

- valid pack phải có E1, manual publish, disclosure, tracking và no Bot/AI publish;
- missing source/time, missing disclosure/tracking hoặc Bot/AI publish phải fail;
- dùng synthetic/sample để gọi E2 phải fail.

## Reality Check — Kiểm chứng thực tế

E1 cần source công khai thật + observed_at; E2 cần human action record/public
artifact thực. Nếu account/platform block, Reality là `BLOCKED_EXTERNAL`, không
phải PASS. Revalidate policy/disclosure current trước publish.

## Operate — Vận hành

Một action record với declared outcome window là minimum. Khi window chưa kết
thúc, ghi `pending`; M01 mới đọc outcome snapshot thật.

## Failure Case — Tình huống lỗi

Thiếu disclosure, tracking, source/time, không kiểm soát channel/account,
claim không có evidence hoặc bất kỳ Bot/AI publish request nào đều phải block.

## Safety Gate — Cổng an toàn

S2: external side effect do `human_only` thực hiện. Không fake click/order,
spam, paid spend, login scraping, credential sharing hoặc account change.

## Evidence — Bằng chứng

Dùng `starter-kits/M00-safe-market-loop/M00-EVIDENCE-SUMMARY.md` cùng
`templates/REDACTED-EVIDENCE-SUMMARY.md`. Lưu raw/private ở ignore path;
summary commit được phải có provenance, redaction và limitations.

## Explain-back — Giải thích lại

Learner phải giải thích được vì sao action là human-only, disclosure/tracking
đang kiểm gì, evidence nào còn thiếu và observation nào sẽ thay đổi decision.

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] Tạo/review được exact artifact và complete safety checklist.

### Reality

- [ ] Có E1 public observation và E2 human manual publish record thật, hoặc ghi `BLOCKED_EXTERNAL` trung thực.

### Operated

- [ ] Có declared outcome window và next measurement cho M01.

## Bot Version Result — Kết quả phiên bản Bot

`pre-bot`: M00 không phát hành Bot. Nó tạo market/measurement context để M01
và M02 có lý do tồn tại.

## Next Mission — Mission tiếp theo

M01 snapshot outcome và M02 deterministic baseline có thể bắt đầu song song
sau M00; M03 cần cả hai.
