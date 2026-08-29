# Manual Affiliate Loop — Reality Feedback bắt buộc

> Manual Affiliate Loop không còn là lane tùy chọn chạy bên cạnh software curriculum. Nó là nguồn reality evidence bắt buộc trong Mission PASS, đồng thời là cách learner hiểu một action trước khi trao action đó cho Bot.

## 1. Vòng lặp chuẩn

```text
REAL OBSERVATION
→ RECORD EVIDENCE + PROVENANCE
→ HUMAN PREDICTION / JUDGMENT
→ BOT BASELINE / ANALYSIS / DECISION
→ COMPARE HUMAN / BOT / BASELINE
→ HUMAN ACTION OR GOVERNED ACTIONINTENT
→ OUTCOME WINDOW
→ EVALUATION
→ VERSIONED CHANGE PROPOSAL
```

Business và software không phải hai lane độc lập. Chúng gặp nhau ở mọi Mission qua cùng evidence chain.

## 2. Ba nguyên tắc

### Reality before claimed intelligence

Bot không thông minh hơn chỉ vì có nhiều code hoặc một câu trả lời AI đẹp. Learner phải chỉ ra:

- Bot đã thấy evidence nào;
- điều gì là fact/estimate/assumption/unknown;
- Bot dự đoán/quyết định gì;
- action nào thực sự xảy ra;
- outcome nào được đo;
- thay đổi tiếp theo dựa trên outcome nào.

### Human does first consequential action

Learner quan sát, phán đoán và thực hiện public publish đầu tiên. Bot chỉ được tăng authority sau khi learner hiểu exact side effect, tracking, failure mode và policy boundary.

### Outcome proposes change; it does not silently rewrite production

```text
Outcome
→ Evaluation
→ ChangeProposal
→ Offline test/eval
→ Human review
→ Versioned deploy
```

Không:

```text
Outcome
→ Agent tự sửa prompt / weights / workflow / policy production
```

## 3. Evidence contract

### Observation

| Field | Ý nghĩa |
|---|---|
| `observation_id` | định danh để Decision tham chiếu |
| `subject` | product/content/channel/metric đang quan sát |
| `observed_at` | thời điểm quan sát |
| `source` | URL/export/API/public page/manual note |
| `access_method` | manual/public/export/API và permission khi relevant |
| `evidence_kind` | `real`, `test`, `synthetic` hoặc `replay` |
| `fact_or_assumption` | `fact`, `estimate`, `assumption`, `unknown` |
| `value` | giá trị hoặc safe reference tới snapshot |
| `freshness` | current/stale/unknown hoặc policy tương đương |
| `confidence` | mức tin vào assessment, không phải xác suất truth |
| `reason` | vì sao tin/không tin và evidence còn thiếu |

### HumanPrediction

Ghi trước khi xem Bot output:

```text
prediction / ranking / hypothesis
reason
strongest evidence
weakest assumption
expected metric or direction
confidence + uncertainty
```

### Action

```text
action_id
decision_id
actor: human | bot
action_type
target
exact artifact/version
risk_level
approval reference khi relevant
executed_at
idempotency key khi Bot execute
```

### Outcome

```text
outcome_id
decision_id / action_id
observed_at
window
metrics
source
evidence_kind
status: pending | partial | final | unknown
limitations
```

### Evaluation

```text
expected vs observed
baseline/control khi có
what can and cannot be concluded
adverse events
next bottleneck / hypothesis
proposed change
required offline test/review
```

## 4. Reality progression M00–M11

### M00 — Public evidence + first decision

- chọn 5 sản phẩm/subjects từ public source thật;
- ghi source, observed time, fact/assumption và missing fields;
- human rank trước;
- chạy deterministic Bot ranking;
- ghi agreement, disagreement và “chưa đủ dữ liệu để kết luận gì”.

**PASS reality:** không dùng sample-only evidence để thay cho public observations.

### M01 — Second snapshot + trustworthy history

- quan sát lại cùng subject ở thời điểm khác;
- lưu snapshot mới, không overwrite snapshot cũ;
- phân biệt unchanged, missing, zero, stale và unknown;
- giải thích change nào có business meaning và change nào chỉ là noise/hypothesis.

**PASS reality:** ít nhất hai timestamps thực trên cùng subject hoặc trạng thái `BLOCKED_EXTERNAL`; fixture chỉ tạo capability evidence.

### M02 — Grounded AI advisor

- learner gắn label thủ công cho một tập evidence nhỏ;
- AI extract/summarize/hypothesize trên cùng evidence;
- claim phải dẫn về source/span hoặc bị unsupported;
- so với human/deterministic baseline;
- lưu invalid output, unsupported claim, abstention và fallback case.

**PASS reality:** AI thực sự được đánh giá trên evidence thật; output đẹp không đủ.

### M03 — Human tracked publish

Trước publish:

1. learner chọn product–audience/content hypothesis;
2. ghi Decision record và outcome window;
3. kiểm official platform policy/disclosure áp dụng;
4. kiểm claim/evidence;
5. tạo tracking link và phân biệt test event;
6. review exact artifact;
7. human tự publish trên account/channel mình sở hữu hoặc kiểm soát.

Không yêu cầu paid ads. Nếu learner chưa có affiliate link, có thể dùng owned public content với tracked non-commercial CTA; phải ghi rõ đây chưa phải monetization evidence.

**PASS reality:** public URL/artifact + policy/disclosure/tracking evidence. Local draft không đủ.

### M04 — Real outcome analytics

- chờ outcome window đã định trước;
- import real impressions/exposures/clicks và order/commission nếu có;
- giữ test events tách khỏi market events;
- nối Decision→Action→Outcome;
- không đổi missing thành zero;
- test order/valid/refund/paid path bằng fixture dù chưa có order thật.

**PASS reality:** analytics snapshot thật sau window. Metric bằng 0 vẫn hợp lệ nếu measurement đúng.

### M05 — First real improvement

Chọn bottleneck từ M04:

```text
no exposure      → distribution hypothesis
exposure/no click → hook/angle/CTA hypothesis
click/no order    → product–audience/landing hypothesis
order invalid/refund → quality/compliance hypothesis
missing data      → measurement hypothesis
```

Pre-register một change chính, primary metric, expected direction, outcome window và stop rule. Human publish/execute variant trong cùng safety boundary M03. Sau window, lưu evaluation và một versioned ChangeProposal.

**PASS reality:** một closed decision/action/outcome/evaluation loop. Negative, zero hoặc inconclusive vẫn PASS; fabricated certainty thì không.

### M06 — Automatic observer

- learner xác nhận access method/source được phép;
- Bot tự chạy scheduled read/watch;
- lưu snapshots/deltas, retry/dedup và alert;
- AI triage chỉ enrich deterministic alert;
- operate đủ cycle để thấy no-change, material-change và failure/recovery.

**PASS reality:** scheduled operating evidence, không chỉ unit test hoặc manual function call.

### M07 — Decision + abstention

- replay real observations/outcomes từ M00–M06;
- stale, missing hoặc conflict phải dẫn tới state phù hợp;
- compare human vs Bot DecisionPacket;
- lưu confidence method/reason, missing evidence, expiry và risk.

**PASS reality:** decision memory truy được về evidence/outcome; Bot biết không quyết định.

### M08 — Read-only tool Agent

- Agent chỉ dùng allowlisted read tools để lấy missing evidence;
- lưu tool selection, arguments, permission, result, cost/latency và evidence refs;
- thử permission denial, timeout, malicious retrieved content và unnecessary call.

**PASS reality:** audited trajectory; final answer không có trace/evidence thì không đủ.

### M09 — Shadow approval

- Agent tạo ActionIntent nhưng executor chạy dry-run/sandbox/owned draft;
- durable approval hỗ trợ approve/reject/expire/cancel;
- thử restart, changed context, duplicate callback, revalidation và kill switch.

**PASS reality:** complete approval trajectory; chat confirmation đơn lẻ không đủ.

### M10 — Limited governed automation

- chỉ allowlist bounded R0/R1 action;
- RISK 1 có audit; RISK 2 tiếp tục durable approval;
- chạy time-bounded canary với rate/resource/cost cap;
- theo dõi policy blocks, duplicate prevention, intervention, rollback và outcome.

**PASS reality:** operated canary không vượt scope; dry-run đơn lẻ không đủ.

### M11 — Production closed loop

- chứng minh trigger→decision→action→outcome trace đầu-cuối;
- có real public evidence, tracked content và real analytics trong history;
- có A2 read-tool path, R0/R1 governed auto path và R2 approval path;
- outcome tạo ChangeProposal;
- change được offline test/evaluate/review trước deploy;
- recovery, monitoring, cost và kill switch hoạt động.

**PASS reality:** nhiều chain replay/audit được; Bot không tự khai “đã học” nếu production version chưa qua review.

## 5. Click/order/revenue maturity

Canonical metric math và event semantics nằm tại [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md).

Minimum model:

```text
Clicks = Exposure × CTR
Orders = Clicks × CVR
Valid Orders = Orders × Valid Order Rate
Expected Affiliate Revenue = Valid Orders × Commission per Valid Order
```

Mỗi factor phải giữ state riêng `observed | estimated | assumed | unknown`; không được trình bày một assumption chain như measured revenue.

Các milestone này được ghi riêng, không biến may mắn kinh doanh thành điểm học:

```text
REAL_EXPOSURE_OBSERVED
REAL_CLICK_OBSERVED
REAL_ORDER_OBSERVED
REAL_VALID_ORDER_OBSERVED
REAL_COMMISSION_PAID
```

Quy tắc:

- self/test click phải gắn `test` và không tính business validation;
- không có traffic sau window là distribution outcome, không phải lý do thay bằng sample;
- real order được nhập ngay khi xuất hiện nhưng không bắt buộc để M04/M05 PASS;
- pending, invalid, refunded và paid order không được gộp;
- chỉ claim monetization validated ở milestone mà evidence hỗ trợ;
- `missing ≠ zero`; `order ≠ valid order ≠ final/paid commission`.

## 6. Safety boundary

### M00–M02

- public/manual read hoặc provider analysis;
- không external action;
- secret không vào prompt/log/artifact.

### M03–M05

- public action do human thực hiện;
- owned/controlled account;
- current policy, disclosure, claim review và tracking;
- không yêu cầu spend, transaction hoặc artificial engagement.

### M06–M08

- automatic read chỉ trên source/access được phép;
- rate limit, least privilege, timeout, retry, audit;
- A2 chỉ read tools.

### M09–M11

```text
RISK 0 → internal/read-only auto
RISK 1 → bounded/reversible + mandatory audit
RISK 2 → durable Human Approval + revalidate
DENY   → prohibited regardless of approval
```

`DENY`: fake click/order, spam, né disclosure, bypass policy, restricted/private scraping, credential sharing và unbounded spend.

## 7. Human-vs-Bot note

Template tối thiểu cho mỗi Mission có judgment/decision:

```text
Real observations:
Human prediction before Bot:
Bot output:
Agreement:
Disagreement:
Strongest evidence:
Weakest assumption:
Missing evidence:
Allowed actor/action now:
Outcome window:
Observed outcome:
What can/cannot be concluded:
Next versioned change proposal:
```

Manual Affiliate Loop kết thúc vai trò “lane riêng” khi M11 hoàn tất; các nguyên tắc evidence, human judgment và outcome evaluation vẫn tiếp tục tồn tại trong production closed loop.
