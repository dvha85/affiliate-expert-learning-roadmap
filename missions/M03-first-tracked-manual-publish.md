---
mission_id: "M03"
title: "First Tracked Manual Publish"
status: draft
requires_missions: ["M02"]
bot_version_from: "v0.3"
bot_version_to: "v0.4"
estimated_hours: 14
knowledge:
  required: ["6.1", "6.2", "6.3", "7.1"]
  on_demand: []
  reference: []
milestones:
  contributes_to: ["G3"]
evidence:
  minimum_level: "E2"
  reality_required: true
safety_gate: "S2"
risk_scope:
  external_side_effects: true
  execution_actor: "human_only"
---

# Mission M03 — First Tracked Manual Publish

## Ship Target — Mục tiêu bàn giao

Learner tạo một content hypothesis từ evidence đã có, tự viết/review một micro-content artifact, gắn disclosure/tracking phù hợp và **tự tay publish** trên channel/account mình sở hữu hoặc kiểm soát.

```text
E1 evidence
→ human content hypothesis
→ human first draft
→ optional grounded AI advisory
→ claim + PolicyContext + disclosure + tracking gate
→ human exact-artifact approval
→ human manual publish
→ E2 Action record
```

Bot v0.4 hỗ trợ Decision record, content evidence, [`Publish Policy Context`](../docs/PUBLISH-POLICY-CONTEXT.md) và tracking metadata. Bot/AI không có publish tool hoặc external execution authority.

## Starting Bot State — Trạng thái Bot ban đầu

Starting state là learner commit đã PASS M02:

- trustworthy E1 history;
- deterministic baseline;
- grounded A1 advisor có validation/eval/fallback;
- chưa có public action, tracked content hoặc business outcome.

Learner phải có một owned/controlled public channel hoặc approved equivalent trước khi E2 có thể hoàn tất. Không dùng account/credential của người khác.

## Try First — Thử trước

### Checkpoint 1 — Human content attempt trước framework/AI

1. Chọn một Product/audience problem từ evidence M00–M02.
2. Viết hypothesis:

   ```text
   For <audience/problem>, content angle <X>
   may produce <expected direction/metric>
   because <evidence refs>, while <uncertainty> remains.
   ```

3. Tự viết micro-content đầu tiên trước khi gọi AI hoặc đọc content framework dài.
4. Ghi weakest claim và điều người xem có thể hiểu sai.
5. Sau attempt, pull `6.1`.

### Checkpoint 2 — Claim, PolicyContext và disclosure gate

1. Đối chiếu từng material claim với evidence.
2. Xác định platform/channel, jurisdiction scope nếu relevant và current policy source/verified time.
3. Ghi `content_origin`: human / AI-assisted / AI-generated / reused / mixed.
4. Nếu có AI/editing, review product fidelity: AI không được invent feature, result, testimonial hoặc depiction mạnh hơn evidence.
5. Nếu reuse asset/content, xác định originality/contribution và rights/authorization state khi applicable.
6. Quyết định riêng affiliate disclosure và AI-content disclosure/label nếu current rule yêu cầu.
7. Đánh dấu claim/context cần xóa, thu hẹp, `BLOCKED` hoặc human review.
8. Sau attempt, pull `6.2–6.3`.

Policy check phải được lưu thành artifact có thể review theo [`docs/PUBLISH-POLICY-CONTEXT.md`](../docs/PUBLISH-POLICY-CONTEXT.md), tối thiểu gồm:

```yaml
platform:
channel_scope:
jurisdiction_scope:
policy_source:
policy_scope:
policy_verified_at:
review_result: current | stale | unknown

content_origin: human | ai_assisted | ai_generated | reused | mixed
ai_disclosure_status: required_present | not_required | unknown
product_fidelity_status: supported | needs_review | failed | not_applicable
originality_status: original | transformed | reused_authorized | unknown
asset_rights_status: owned | licensed | authorized | not_applicable | unknown
reuse_authorization_ref:

affiliate_disclosure_required:
affiliate_disclosure_text:
affiliate_disclosure_placement:
limitations: []
```

Không dùng trí nhớ, câu trả lời AI hoặc screenshot không có nguồn làm bằng chứng rằng policy hiện hành. Nếu material policy/legal requirement là `stale`/`unknown`, publish readiness phải là `BLOCKED` hoặc `HUMAN_REVIEW` theo current verified boundary; không mặc định “platform cho đăng = hợp pháp ở mọi jurisdiction”.

Platform-derived creator/account score nếu có chỉ là evidence về platform state. Nó không override claim evidence, product fidelity hoặc disclosure gate.

### Checkpoint 3 — Tracking và exact-artifact review

1. Tạo stable content/action ID và tracking link/UTM tương ứng.
2. Kiểm tracking bằng test event được gắn nhãn `test`.
3. Kiểm public URL/tracking metadata không chứa secret hoặc obvious personal data không cần thiết.
4. Freeze exact artifact/version sẽ publish, gồm cả media/AI-edited asset nếu có.
5. Human review checklist rồi tự publish.
6. Lưu public URL, publish time, actor và exact version.
7. Sau attempt, pull `7.1` khi tracking gap xuất hiện.

## Run — Chạy

Draft Bot workflow:

```bash
cd lab/learner/affiliate-bot
go run ./cmd/bot
go test ./...
```

Bot output cần kiểm tra được:

```text
Bot version: v0.4
Content decision ID: <id>
Evidence refs: <ids>
Hypothesis: <text>
Claims: supported | needs_review | rejected
Content origin: <human | ai_assisted | ai_generated | reused | mixed>
PolicyContext: current | needs_review | blocked
Disclosure: present | missing | not_applicable_with_reason
Tracking ID/link: <safe value>
Action risk: RISK2_PUBLIC_PUBLISH
Allowed execution actor: human only
Publish readiness: READY_FOR_HUMAN | HUMAN_REVIEW | BLOCKED
```

Bot không được gọi publish API hoặc mô phỏng publish thành công.

## Observe — Quan sát

Lưu:

- first human draft trước AI/framework;
- claim nào evidence không đủ;
- current platform/jurisdiction/disclosure rule nào ảnh hưởng artifact;
- content origin và asset nào được AI tạo/chỉnh/reuse;
- AI suggestion nào được accept/reject và vì sao;
- product-fidelity/originality/rights issue nào xuất hiện;
- test tracking event có đi đúng ID không;
- exact content approved khác draft ban đầu thế nào;
- cảm nhận/decision nào learner chỉ hiểu sau khi tự publish.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `6.1` — audience problem, product fit và testable content angle;
- `6.2` — proof, claims, disclosure và current platform boundary;
- `6.3` — human review, manual publish và Decision ≠ Execution;
- `7.1` — tracking ID, UTM/link, impression, click và outcome event.

Current policy/legal examples nằm ở reference/freshness layer, không biến thành permanent lesson title. Channel-specific format/SEO/video production chỉ pull on-demand sau khi learner chọn artifact. Paid traffic, automatic publishing và account API integration không thuộc M03.

## Improve — Cải tiến

- biến vague idea thành explicit content hypothesis;
- gắn evidence refs vào claims/angle;
- sửa hoặc xóa unsupported/deceptive claim;
- giữ content origin/provenance và product fidelity;
- xác minh rights/authorization cho reused asset khi applicable;
- tách affiliate disclosure khỏi AI-content disclosure/label;
- thêm disclosure rõ, dễ thấy theo current channel/jurisdiction boundary;
- tạo tracking/action identity không leak secret/PII;
- tách test event khỏi future real events;
- thêm `READY_FOR_HUMAN | HUMAN_REVIEW | BLOCKED` gate;
- freeze content version trước human publish;
- ghi Action record sau khi learner thực hiện.

AI có thể gợi ý wording/angle hoặc hỗ trợ tạo asset, nhưng final artifact, current-policy review và publish decision thuộc learner.

## Tests — Kiểm thử

Draft checks:

- Decision/content/action IDs nối đúng;
- material claims thiếu evidence bị `needs_review`/`rejected`;
- AI invents product feature/result/testimonial → `BLOCKED`;
- product depiction thay đổi gây hiểu sai → `BLOCKED`/`HUMAN_REVIEW`;
- missing affiliate disclosure chặn readiness khi required;
- required AI disclosure/label missing hoặc applicability unresolved → `BLOCKED`/`HUMAN_REVIEW`;
- reused asset + rights/authorization unknown khi relevant → `BLOCKED`/`HUMAN_REVIEW`;
- unknown/stale material policy state chặn publish;
- jurisdiction requirement chưa resolve không được auto-assume;
- malformed tracking link/ID bị reject;
- tracking URL/content/log có secret hoặc obvious unnecessary PII bị reject;
- test event có `event_origin: test`;
- exact approved version khác version publish thì action bị reject/flag;
- AI unavailable không chặn human baseline workflow;
- platform score không bypass unsupported-claim gate;
- Bot không có publish/write tool.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E2 — real human action.

Bắt buộc:

- public artifact truy cập được theo scope channel;
- channel/account do learner sở hữu hoặc được phép kiểm soát;
- `published_at`, public URL/reference và exact content version;
- `actor: human`;
- applicable platform/jurisdiction/disclosure source + verified time;
- PolicyContext có content origin, fidelity/originality/rights state khi relevant;
- affiliate/AI disclosure decisions được tách và trace về current scope;
- tracking ID/link đã test và không leak secret/obvious unnecessary PII;
- affiliate/non-commercial relationship được mô tả trung thực.

Nếu learner chưa có affiliate link, có thể publish owned public content với tracked non-commercial CTA. Artifact đó tạo E2 market-action evidence nhưng **không** tạo monetization evidence; phải ghi rõ.

Local draft, screenshot giả hoặc Bot log “published” không thỏa E2. Nếu không có safe owned channel, Capability có thể tiếp tục tới draft/readiness nhưng Reality giữ `BLOCKED_EXTERNAL`; M03 chưa DONE.

M03 chỉ mở outcome window; M04 mới import/đánh giá analytics.

## Operate — Vận hành

Tối thiểu:

1. validate một blocked draft có claim/policy/disclosure/fidelity/rights/tracking issue;
2. validate final `READY_FOR_HUMAN` artifact;
3. human publish exact approved version một lần;
4. kiểm public URL/live artifact;
5. ghi observation window và scheduled review time cho M04;
6. giữ test tracking event tách biệt.

Không tự tạo artificial engagement để “kiểm outcome”.

## Failure Case — Tình huống lỗi

- unsupported/deceptive claim;
- AI invents/misrepresents product feature, result hoặc testimonial;
- disclosure missing/hidden/ambiguous;
- AI-content disclosure requirement unknown/missing khi applicable;
- reused content/asset nhưng rights/authorization không rõ;
- policy source stale/unknown;
- jurisdiction applicability unresolved cho material requirement;
- tracking link malformed hoặc sai content/action ID;
- tracking/content/log leak secret hoặc unnecessary PII;
- exact artifact thay đổi sau approval;
- learner không sở hữu/không có permission trên channel;
- AI chèn claim không có evidence;
- platform score được dùng để rationalize unsupported claim;
- double/manual duplicate publish.

Behavior an toàn là `BLOCKED` hoặc `HUMAN_REVIEW`, sửa artifact/context rồi review lại; không bypass gate vì deadline.

## Safety Gate — Cổng an toàn

**S2 — Manual Publish. External side effect: true; actor: human only.**

Bắt buộc trước publish:

- owned/controlled channel;
- current platform/jurisdiction policy boundary khi relevant;
- claim/evidence review;
- content origin + product fidelity review khi AI/editing được dùng;
- originality/rights/authorization review khi reuse content/asset;
- affiliate disclosure và AI-content disclosure/label decisions tách rõ;
- tracking/test-event separation;
- exact-artifact human review;
- no secret/obvious unnecessary PII in public content/tracking/log.

Không cho phép:

- Bot/AI publish;
- paid spend;
- account/platform settings change;
- message/spam;
- fake click/order/engagement;
- fake/misleading AI product/result depiction;
- bypass disclosure/policy/rights;
- credential sharing.

Public publish là consequential human action. S2 không phải durable A3 approval runtime; runtime đó chỉ được build ở M09 sau khi learner đã hiểu side effect thủ công.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M03/`:

- E1 evidence refs và content hypothesis;
- first human draft trước AI;
- optional AI suggestions/assets + accept/reject reasons;
- claim/evidence matrix;
- PolicyContext với platform/jurisdiction source + verified time;
- content-origin/product-fidelity/originality/rights review khi relevant;
- affiliate/AI disclosure decisions;
- tracking/action ID + labeled test event;
- blocked readiness case;
- final exact artifact hash/version;
- human review checklist;
- Action record với `actor: human`;
- public URL/reference + `published_at`;
- declared M04 outcome window;
- learner commit.

Evidence chain:

```text
Observation/History(E1)
→ HumanPrediction + Content Decision
→ optional grounded AI advisory
→ claim + PolicyContext + disclosure + tracking gates
→ S2 readiness gate
→ Human Action(PUBLISH)
→ E2 public artifact
→ Outcome pending for M04
```

## Explain-back — Giải thích lại

Learner phải trỏ vào exact artifact/evidence để giải thích:

1. Audience problem và evidence nào tạo content hypothesis?
2. Claim nào mạnh/yếu nhất và limitation là gì?
3. Platform/jurisdiction/disclosure policy nào áp dụng và được kiểm lúc nào?
4. Content origin là gì; AI/reuse có làm phát sinh fidelity/originality/rights gate nào không?
5. Vì sao affiliate disclosure và AI-content disclosure là hai câu hỏi khác nhau?
6. Vì sao human first draft phải tồn tại trước AI-assisted version?
7. Tracking ID nối Decision với future Outcome thế nào, và vì sao không nhét PII vào tracking URL?
8. Vì sao test click không phải market response?
9. Vì sao learner được publish nhưng Bot chưa có publish authority?
10. Điều gì sẽ khiến artifact bị `BLOCKED` hoặc `HUMAN_REVIEW`?
11. M04 sẽ đo gì, sau window nào và zero/missing được xử lý ra sao?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] content Decision record + hypothesis + evidence refs tồn tại
- [ ] first human draft trước AI/framework được lưu
- [ ] claims/PolicyContext/disclosure/tracking gates chạy đúng
- [ ] AI fidelity và reused-rights failure cases được xử lý an toàn khi relevant
- [ ] blocked failure case đạt
- [ ] exact artifact/version được freeze trước publish
- [ ] AI unavailable vẫn giữ human baseline workflow
- [ ] Bot không có publish/write authority
- [ ] required lessons được pull sau attempt và explain-back đạt

### Reality

- [ ] có E2 public artifact trên owned/controlled channel
- [ ] human là actor thực thi
- [ ] public reference, published_at và exact version được lưu
- [ ] applicable platform/jurisdiction/disclosure evidence hiện hành tồn tại
- [ ] policy check được thực hiện lại ngay trước publish nếu source/version đã thay đổi
- [ ] content origin/fidelity/originality/rights state được lưu khi relevant
- [ ] tracking đã test và test event được phân loại
- [ ] không claim monetization nếu chưa có affiliate/outcome evidence

### Operated

- [ ] chạy blocked draft và ready artifact paths
- [ ] exact approved artifact được publish đúng một lần
- [ ] public artifact/live reference được kiểm
- [ ] M04 outcome window/review time đã khai báo
- [ ] S2 đạt, không prohibited action

## Bot Version Result — Kết quả phiên bản Bot

```text
v0.3 grounded A1 advisor
→ v0.4 tracked, policy-context-aware content decision + human-published E2 artifact
```

Authority ceiling sau M03:

```text
AI analyze/recommend only
human executes public publish
Bot has no publish tool
```

## Next Mission — Mission tiếp theo

M04 — Real Outcome Analytics: chờ declared window, import analytics/export thật, tách test/real event và nối Decision→Human Action→Outcome mà không đổi missing thành zero.
