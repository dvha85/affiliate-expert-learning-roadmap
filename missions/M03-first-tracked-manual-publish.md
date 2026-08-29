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
→ claim/policy/disclosure/tracking gate
→ human exact-artifact approval
→ human manual publish
→ E2 Action record
```

Bot v0.4 hỗ trợ Decision record, content evidence và tracking metadata. Bot/AI không có publish tool hoặc external execution authority.

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

### Checkpoint 2 — Claim, policy và disclosure gate

1. Đối chiếu từng material claim với evidence.
2. Xác định platform/channel và current policy source/verified time.
3. Thêm disclosure phù hợp với relationship/link thực tế.
4. Đánh dấu claim cần xóa, thu hẹp hoặc human review.
5. Sau attempt, pull `6.2–6.3`.

Policy check phải được lưu thành artifact có thể review, tối thiểu gồm:

```yaml
platform:
policy_source:
policy_scope:
policy_verified_at:
disclosure_required:
disclosure_text:
disclosure_placement:
review_result: current | stale | unknown
```

Không dùng trí nhớ, câu trả lời AI hoặc screenshot không có nguồn làm bằng chứng rằng policy hiện hành. Nếu policy là `stale`/`unknown`, publish readiness phải là `BLOCKED` cho tới khi human kiểm lại nguồn chính thức.

### Checkpoint 3 — Tracking và exact-artifact review

1. Tạo stable content/action ID và tracking link/UTM tương ứng.
2. Kiểm tracking bằng test event được gắn nhãn `test`.
3. Freeze exact artifact/version sẽ publish.
4. Human review checklist rồi tự publish.
5. Lưu public URL, publish time, actor và exact version.
6. Sau attempt, pull `7.1` khi tracking gap xuất hiện.

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
Disclosure: present | missing | not_applicable_with_reason
Tracking ID/link: <safe value>
Action risk: RISK2_PUBLIC_PUBLISH
Allowed execution actor: human only
Publish readiness: READY_FOR_HUMAN | BLOCKED
```

Bot không được gọi publish API hoặc mô phỏng publish thành công.

## Observe — Quan sát

Lưu:

- first human draft trước AI/framework;
- claim nào evidence không đủ;
- current platform/disclosure rule nào ảnh hưởng artifact;
- AI suggestion nào được accept/reject và vì sao;
- test tracking event có đi đúng ID không;
- exact content approved khác draft ban đầu thế nào;
- cảm nhận/decision nào learner chỉ hiểu sau khi tự publish.

## Knowledge Pull — Lấy kiến thức đúng lúc

- `6.1` — audience problem, product fit và testable content angle;
- `6.2` — proof, claims, disclosure và current platform boundary;
- `6.3` — human review, manual publish và Decision ≠ Execution;
- `7.1` — tracking ID, UTM/link, impression, click và outcome event.

Channel-specific format/SEO/video production chỉ pull on-demand sau khi learner chọn artifact. Paid traffic, automatic publishing và account API integration không thuộc M03.

## Improve — Cải tiến

- biến vague idea thành explicit content hypothesis;
- gắn evidence refs vào claims/angle;
- sửa hoặc xóa unsupported/deceptive claim;
- thêm disclosure rõ, dễ thấy theo current channel boundary;
- tạo tracking/action identity;
- tách test event khỏi future real events;
- thêm `READY_FOR_HUMAN | BLOCKED` gate;
- freeze content version trước human publish;
- ghi Action record sau khi learner thực hiện.

AI có thể gợi ý wording/angle, nhưng final artifact và publish decision thuộc learner.

## Tests — Kiểm thử

Draft checks:

- Decision/content/action IDs nối đúng;
- material claims thiếu evidence bị `needs_review`/`rejected`;
- missing disclosure chặn readiness khi disclosure required;
- unknown/stale policy state chặn publish;
- malformed tracking link/ID bị reject;
- test event có `event_origin: test`;
- exact approved version khác version publish thì action bị reject/flag;
- AI unavailable không chặn human baseline workflow;
- Bot không có publish/write tool;
- no secret/token trong artifact/log.

## Reality Check — Kiểm chứng thực tế

**Minimum:** E2 — real human action.

Bắt buộc:

- public artifact truy cập được theo scope channel;
- channel/account do learner sở hữu hoặc được phép kiểm soát;
- `published_at`, public URL/reference và exact content version;
- `actor: human`;
- applicable policy/disclosure source + verified time;
- policy check artifact có scope, disclosure decision và review result;
- tracking ID/link đã test;
- affiliate/non-commercial relationship được mô tả trung thực.

Nếu learner chưa có affiliate link, có thể publish owned public content với tracked non-commercial CTA. Artifact đó tạo E2 market-action evidence nhưng **không** tạo monetization evidence; phải ghi rõ.

Local draft, screenshot giả hoặc Bot log “published” không thỏa E2. Nếu không có safe owned channel, Capability có thể tiếp tục tới draft/readiness nhưng Reality giữ `BLOCKED_EXTERNAL`; M03 chưa DONE.

M03 chỉ mở outcome window; M04 mới import/đánh giá analytics.

## Operate — Vận hành

Tối thiểu:

1. validate một blocked draft có claim/disclosure/tracking issue;
2. validate final `READY_FOR_HUMAN` artifact;
3. human publish exact approved version một lần;
4. kiểm public URL/live artifact;
5. ghi observation window và scheduled review time cho M04;
6. giữ test tracking event tách biệt.

Không tự tạo artificial engagement để “kiểm outcome”.

## Failure Case — Tình huống lỗi

- unsupported/deceptive claim;
- disclosure missing/hidden/ambiguous;
- policy source stale/unknown;
- tracking link malformed hoặc sai content/action ID;
- exact artifact thay đổi sau approval;
- learner không sở hữu/không có permission trên channel;
- AI chèn claim không có evidence;
- secret/token xuất hiện trong draft/log;
- double/manual duplicate publish.

Behavior an toàn là `BLOCKED`, sửa artifact hoặc human review lại; không bypass gate vì deadline.

## Safety Gate — Cổng an toàn

**S2 — Manual Publish. External side effect: true; actor: human only.**

Bắt buộc trước publish:

- owned/controlled channel;
- current policy boundary;
- claim/evidence review;
- disclosure;
- tracking/test-event separation;
- exact-artifact human review;
- no secret in content/log.

Không cho phép:

- Bot/AI publish;
- paid spend;
- account/platform settings change;
- message/spam;
- fake click/order/engagement;
- bypass disclosure/policy;
- credential sharing.

Public publish là consequential human action. S2 không phải durable A3 approval runtime; runtime đó chỉ được build ở M09 sau khi learner đã hiểu side effect thủ công.

## Evidence — Bằng chứng

Lưu dưới `artifacts/missions/M03/`:

- E1 evidence refs và content hypothesis;
- first human draft trước AI;
- optional AI suggestions + accept/reject reasons;
- claim/evidence matrix;
- platform/disclosure source + verified time;
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
→ S2 readiness gate
→ Human Action(PUBLISH)
→ E2 public artifact
→ Outcome pending for M04
```

## Explain-back — Giải thích lại

Learner phải trỏ vào exact artifact/evidence để giải thích:

1. Audience problem và evidence nào tạo content hypothesis?
2. Claim nào mạnh/yếu nhất và limitation là gì?
3. Disclosure/policy nào áp dụng và được kiểm lúc nào?
4. Vì sao human first draft phải tồn tại trước AI-assisted version?
5. Tracking ID nối Decision với future Outcome thế nào?
6. Vì sao test click không phải market response?
7. Vì sao learner được publish nhưng Bot chưa có publish authority?
8. Điều gì sẽ khiến artifact bị BLOCKED?
9. M04 sẽ đo gì, sau window nào và zero/missing được xử lý ra sao?

## Mission PASS — Tiêu chí PASS

### Capability

- [ ] content Decision record + hypothesis + evidence refs tồn tại
- [ ] first human draft trước AI/framework được lưu
- [ ] claims/disclosure/policy/tracking gates chạy đúng
- [ ] blocked failure case đạt
- [ ] exact artifact/version được freeze trước publish
- [ ] AI unavailable vẫn giữ human baseline workflow
- [ ] Bot không có publish/write authority
- [ ] required lessons được pull sau attempt và explain-back đạt

### Reality

- [ ] có E2 public artifact trên owned/controlled channel
- [ ] human là actor thực thi
- [ ] public reference, published_at và exact version được lưu
- [ ] applicable disclosure/policy evidence hiện hành tồn tại
- [ ] policy check được thực hiện lại ngay trước publish nếu source/version đã thay đổi
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
→ v0.4 tracked content decision + human-published E2 artifact
```

Authority ceiling sau M03:

```text
AI analyze/recommend only
human executes public publish
Bot has no publish tool
```

## Next Mission — Mission tiếp theo

M04 — Real Outcome Analytics: chờ declared window, import analytics/export thật, tách test/real event và nối Decision→Human Action→Outcome mà không đổi missing thành zero.
