# Vòng Affiliate thủ công — phản hồi thực tế bắt buộc

> Manual Affiliate Loop (vòng Affiliate thủ công) không còn là lane tùy chọn chạy bên cạnh curriculum phần mềm. Nó là nguồn **reality evidence (bằng chứng thực tế)** bắt buộc trong Mission PASS, đồng thời là cách người học hiểu một hành động trước khi trao hành động đó cho Bot.

## 1. Vòng lặp chuẩn

```text
QUAN SÁT THẬT
→ GHI BẰNG CHỨNG + PROVENANCE
→ PHÁN ĐOÁN / DỰ ĐOÁN CỦA NGƯỜI
→ BASELINE / PHÂN TÍCH / QUYẾT ĐỊNH CỦA BOT
→ SO SÁNH NGƯỜI / BOT / BASELINE
→ HÀNH ĐỘNG CỦA NGƯỜI HOẶC ACTIONINTENT CÓ QUẢN TRỊ
→ CỬA SỔ OUTCOME
→ ĐÁNH GIÁ
→ CHANGE PROPOSAL CÓ PHIÊN BẢN
```

Business (kinh doanh) và software (phần mềm) không phải hai lane độc lập. Chúng gặp nhau ở mọi Mission qua cùng chuỗi evidence.

## 2. Ba nguyên tắc

### Thực tế trước tuyên bố “thông minh” (`Reality before claimed intelligence`)

Bot không thông minh hơn chỉ vì có nhiều code hoặc một câu trả lời AI đẹp. Người học phải chỉ ra:

- Bot đã thấy evidence nào;
- điều gì là `fact` (sự thật), `estimate` (ước lượng), `assumption` (giả định), `unknown` (chưa biết);
- Bot dự đoán/quyết định gì;
- action nào thực sự xảy ra;
- outcome nào được đo;
- thay đổi tiếp theo dựa trên outcome nào.

### Người thực hiện hành động có hậu quả đầu tiên

Người học quan sát, phán đoán và tự thực hiện public publish đầu tiên. Bot chỉ được tăng authority (quyền hành động) sau khi người học hiểu side effect (tác động), tracking, failure mode và policy boundary.

### Outcome chỉ đề xuất thay đổi, không âm thầm viết lại production

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

## 3. Hợp đồng bằng chứng (`evidence contract`)

### Observation — quan sát

| Field | Ý nghĩa |
|---|---|
| `observation_id` | định danh để Decision tham chiếu |
| `subject` | product/content/channel/metric đang quan sát |
| `observed_at` | thời điểm quan sát |
| `source` | URL/export/API/public page/manual note |
| `access_method` | cách truy cập và permission khi liên quan |
| `evidence_kind` | `real`, `test`, `synthetic` hoặc `replay` |
| `fact_or_assumption` | `fact`, `estimate`, `assumption`, `unknown` |
| `value` | giá trị hoặc safe reference tới snapshot |
| `freshness` | độ mới: current/stale/unknown hoặc policy tương đương |
| `confidence` | mức tin vào assessment, không mặc định là xác suất truth |
| `reason` | vì sao tin/không tin và evidence còn thiếu |

### HumanPrediction — dự đoán của người

Ghi trước khi xem Bot output:

```text
prediction / ranking / hypothesis
reason
strongest evidence
weakest assumption
expected metric or direction
confidence + uncertainty
```

### Action — hành động

```text
action_id
decision_id
actor: human | bot
action_type
target
exact artifact/version
risk_level
approval reference khi liên quan
executed_at
idempotency key khi Bot thực thi
```

### Outcome — kết quả quan sát được

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

### Evaluation — đánh giá

```text
expected vs observed
baseline/control khi có
what can and cannot be concluded
adverse events
next bottleneck / hypothesis
proposed change
required offline test/review
```

## 4. Tiến triển thực tế M00–M11

> **V1 detail below:** M00–M04 labels in this section are retained reference.
> In v2, the same manual loop is M00, outcome snapshot M01, deterministic Bot
> M02, history M03, and AI advisory M04.

### V1 M00 — Evidence công khai + quyết định đầu tiên

- chọn 5 sản phẩm/subject từ nguồn công khai thật;
- ghi source, observed time, fact/assumption và field còn thiếu;
- người xếp hạng trước;
- chạy Bot ranking tất định;
- ghi agreement, disagreement và “chưa đủ dữ liệu để kết luận gì”.

**PASS reality:** không dùng sample-only evidence để thay cho public observations.

### M01 — Snapshot lần hai + history đáng tin

- quan sát lại cùng subject ở thời điểm khác;
- lưu snapshot mới, không overwrite snapshot cũ;
- phân biệt unchanged, missing, zero, stale và unknown;
- giải thích change nào có ý nghĩa kinh doanh và change nào mới chỉ là noise/hypothesis.

**PASS reality:** ít nhất hai timestamp thực trên cùng subject hoặc trạng thái `BLOCKED_EXTERNAL`; fixture chỉ tạo capability evidence.

### M02 — AI advisor có grounding

- người học gắn label thủ công cho một tập evidence nhỏ;
- AI extract/summarize/hypothesize trên cùng evidence;
- claim phải dẫn về source/span hoặc bị đánh dấu unsupported;
- so với human/deterministic baseline;
- lưu invalid output, unsupported claim, abstention và fallback case.

**PASS reality:** AI phải được đánh giá trên evidence thật; output đẹp không đủ.

### M03 — Người publish nội dung có tracking

Trước publish:

1. chọn giả thuyết product–audience/content;
2. ghi Decision record và outcome window;
3. kiểm policy/disclosure chính thức đang áp dụng;
4. kiểm claim/evidence;
5. tạo tracking link và phân biệt test event;
6. review exact artifact;
7. người tự publish trên account/channel mình sở hữu hoặc kiểm soát.

Không yêu cầu paid ads. Nếu chưa có affiliate link, có thể dùng owned public content với tracked non-commercial CTA; phải ghi rõ đây chưa phải monetization evidence.

**PASS reality:** public URL/artifact + policy/disclosure/tracking evidence. Local draft không đủ.

### M04 — Phân tích outcome thật

- chờ outcome window đã định trước;
- import impression/exposure/click thật và order/commission nếu có;
- giữ test event tách khỏi market event;
- nối Decision→Action→Outcome;
- không đổi missing thành zero;
- test order/valid/refund/paid path bằng fixture dù chưa có order thật.

**PASS reality:** analytics snapshot thật sau window. Metric bằng `0` vẫn hợp lệ nếu measurement đúng.

### M05 — Cải tiến thật đầu tiên

Chọn bottleneck từ M04:

```text
không exposure         → giả thuyết distribution
có exposure/no click   → giả thuyết hook/angle/CTA
có click/no order      → giả thuyết product–audience/landing
order invalid/refund   → giả thuyết quality/compliance
missing data           → giả thuyết measurement
```

Pre-register (đăng ký trước) một thay đổi chính, primary metric, expected direction, outcome window và stop rule. Người publish/execute variant trong cùng safety boundary M03. Sau window, lưu evaluation và một `ChangeProposal` có version.

**PASS reality:** một vòng decision/action/outcome/evaluation khép kín. Negative, zero hoặc inconclusive vẫn PASS; fabricated certainty thì không.

### M06 — Bộ quan sát tự động

- xác nhận access method/source được phép;
- Bot tự chạy scheduled read/watch;
- lưu snapshot/delta, retry/dedup và alert;
- AI triage chỉ enrich deterministic alert;
- vận hành đủ cycle để thấy no-change, material-change và failure/recovery.

**PASS reality:** có bằng chứng vận hành theo lịch, không chỉ unit test hoặc manual function call.

### M07 — Decision + abstention

- replay real observations/outcomes từ M00–M06;
- stale, missing hoặc conflict phải dẫn tới state phù hợp;
- so sánh người với `DecisionPacket` của Bot;
- lưu confidence method/reason, missing evidence, expiry và risk.

**PASS reality:** decision memory truy được về evidence/outcome; Bot biết khi nào không quyết định.

### M08 — Agent dùng tool chỉ-đọc

- Agent chỉ dùng allowlisted read tools để lấy missing evidence;
- lưu tool selection, arguments, permission, result, cost/latency và evidence refs;
- thử permission denial, timeout, malicious retrieved content và unnecessary call.

**PASS reality:** có audited trajectory (quỹ đạo thao tác được kiểm toán); final answer không có trace/evidence thì không đủ.

### M09 — Approval chạy bóng (`shadow approval`)

- Agent tạo `ActionIntent` nhưng executor chỉ chạy dry-run/sandbox/owned draft;
- durable approval hỗ trợ approve/reject/expire/cancel;
- thử restart, changed context, duplicate callback, revalidation và kill switch.

**PASS reality:** complete approval trajectory; chat confirmation đơn lẻ không đủ.

### M10 — Tự động hóa giới hạn có quản trị

- chỉ allowlist bounded R0/R1 action;
- RISK 1 có audit; RISK 2 tiếp tục durable approval;
- chạy canary giới hạn thời gian với rate/resource/cost cap;
- theo dõi policy block, duplicate prevention, intervention, rollback và outcome.

**PASS reality:** canary đã vận hành không vượt scope; dry-run đơn lẻ không đủ.

### M11 — Vòng production khép kín

- chứng minh trace trigger→decision→action→outcome đầu-cuối;
- có real public evidence, tracked content và real analytics trong history;
- có A2 read-tool path, R0/R1 governed auto path và R2 approval path;
- outcome tạo `ChangeProposal`;
- change được offline test/evaluate/review trước deploy;
- recovery, monitoring, cost và kill switch hoạt động.

**PASS reality:** nhiều chain có thể replay/audit; Bot không tự khai “đã học” nếu production version chưa qua review.

## 5. Mức trưởng thành click/order/revenue

Phép tính metric chuẩn và semantics của event nằm tại [`AFFILIATE-METRIC-REVENUE-SPINE.md`](AFFILIATE-METRIC-REVENUE-SPINE.md).

Mô hình tối thiểu:

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

## 6. Ranh giới an toàn

### M00–M02

- đọc công khai/thủ công hoặc provider analysis;
- không external action;
- secret không vào prompt/log/artifact.

### M03–M05

- public action do người thực hiện;
- account do người học sở hữu/kiểm soát;
- current policy, disclosure, claim review và tracking;
- không yêu cầu spend, transaction hoặc artificial engagement.

### M06–M08

- automatic read chỉ trên source/access được phép;
- rate limit, least privilege, timeout, retry, audit;
- A2 chỉ read tools.

### M09–M11

```text
RISK 0 → nội bộ/chỉ-đọc tự động
RISK 1 → giới hạn/có thể đảo ngược + audit bắt buộc
RISK 2 → Human Approval bền vững + revalidate
DENY   → cấm bất kể có approval
```

`DENY`: fake click/order, spam, né disclosure, bypass policy, restricted/private scraping, credential sharing và unbounded spend.

## 7. Ghi chú so sánh người với Bot

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

Manual Affiliate Loop kết thúc vai trò “lane riêng” khi M11 hoàn tất; các nguyên tắc evidence, human judgment và outcome evaluation vẫn tiếp tục tồn tại trong vòng production khép kín.
