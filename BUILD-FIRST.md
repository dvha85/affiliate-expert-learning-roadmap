# Lộ trình học Build-First, Reality-First

> **BẮT ĐẦU TỪ ĐÂY.** Người học xây một Affiliate Bot duy nhất qua các phiên bản nhỏ. Mỗi capability phải xuất phát từ một vấn đề đã quan sát, chạy trên evidence đúng loại và được cải tiến bằng outcome thật trước khi Bot nhận thêm quyền.

Nguồn cấu trúc có thẩm quyền là [`CURRICULUM.md`](CURRICULUM.md); tài liệu này triển khai execution order của canonical đó.

## Mục tiêu của chương trình

Chương trình dành cho người mới và phải đồng thời đạt bốn mục tiêu:

1. có Bot chạy được ngay từ Mission đầu;
2. thực hành trước, chỉ pull kiến thức khi attempt làm lộ nhu cầu;
3. dùng dữ liệu và phản hồi thị trường thật sớm;
4. tiến tới tự động hóa thông minh nhưng có policy, approval, audit và kill switch.

```text
SMART BOT
= evidence-aware
+ biết phân biệt fact / estimate / assumption / unknown
+ biết confidence và uncertainty
+ biết WAIT / GET_MORE_DATA / HUMAN_REVIEW
+ nối Decision với Outcome
+ chỉ hành động trong quyền được cấp
```

LLM output nghe hợp lý nhưng không có evidence, evaluation hoặc safety boundary không được coi là Bot thông minh.

## Vòng học mặc định

```text
REAL OBSERVATION
→ HUMAN PREDICTION / JUDGMENT
→ BUILD SMALLEST WORKING SLICE
→ RUN / OBSERVE FAILURE OR GAP
→ PULL KNOWLEDGE JUST-IN-TIME
→ IMPROVE / TEST
→ RUN ON THE REQUIRED EVIDENCE
→ COMPARE HUMAN / BOT / BASELINE
→ ACTION WITH THE ALLOWED ACTOR AND RISK BOUNDARY
→ OUTCOME
→ EVALUATION
→ VERSIONED CHANGE PROPOSAL
→ NEXT BOT VERSION
```

Không đợi học hết một Part mới thực hành. Không build hạ tầng chỉ vì “sau này có thể cần”. Không dùng sample data để thay thế âm thầm cho reality evidence.

## Bảy Part thực thi

Part là một capability stage (giai đoạn năng lực), không phải kho chủ đề phải học tuần tự.

| Part | Mission | Câu hỏi người học phải trả lời bằng artifact |
|---|---|---|
| P0 — First Evidence Decision | M00 | Bot và tôi đang quyết định gì từ bằng chứng công khai thật? |
| P1 — Trustworthy Data & Grounded AI | M01–M02 | Dữ liệu có đáng tin và AI có thực sự bám nguồn không? |
| P2 — Publish & Measure | M03–M04 | Hành động thủ công nào đã được publish an toàn và thị trường phản hồi gì? |
| P3 — Improve from Reality | M05 | Outcome thật đã làm thay đổi giả thuyết/phiên bản nào? |
| P4 — Automatic Observation & Decision | M06–M07 | Bot tự quan sát gì, khi nào cảnh báo, quyết định hoặc từ chối quyết định? |
| P5 — Governed Agent | M08–M10 | Agent được dùng tool/hành động tới đâu và control nào chứng minh điều đó? |
| P6 — Production Closed Loop | M11 | Hệ thống có vận hành closed loop an toàn và tạo cải tiến được review không? |

Chi tiết knowledge pull nằm tại [`docs/MISSION-KNOWLEDGE-MAP.md`](docs/MISSION-KNOWLEDGE-MAP.md).

## Mission spine M00–M11

| Mission | Ship target | Reality milestone | AI / authority |
|---|---|---|---|
| M00 | Evidence-backed ranking đầu tiên; human judgment trước Bot | 5 public observations có URL và thời điểm | A0 |
| M01 | Validated append-only snapshots, history và freshness | Quan sát thật lần hai trên cùng subject | A0 |
| M02 | Grounded AI advisor có schema, evidence, uncertainty và fallback | AI phân tích một tập evidence công khai thật | A1, không tool/write |
| M03 | Tracked content artifact được con người review và publish | Public action đầu tiên trên kênh learner sở hữu/kiểm soát | A1 advisory; human execute |
| M04 | Decision→Action→Outcome analytics | Analytics thật đầu tiên, kể cả kết quả bằng 0 | A1 investigation |
| M05 | Một vòng cải tiến từ outcome thật | Closed real feedback loop đầu tiên | A1 hypothesis copilot |
| M06 | Reliable automatic read/watch + alert | Bot tự quan sát nguồn được phép | A0 core + A1 triage |
| M07 | DecisionPacket có confidence, freshness và abstention | Replay quyết định trên evidence/outcome đã lưu | A1 decision support |
| M08 | Agent tự lấy missing evidence bằng read-only tools | Automatic read-only investigation | A2-RO |
| M09 | Shadow ActionIntent + durable approval runtime | Side effect chỉ ở dry-run/sandbox/owned draft | A3-shadow |
| M10 | Limited governed R0/R1 automation; R2 phải duyệt | Time-bounded canary có audit và kill switch | A3-limited |
| M11 | Production closed loop từ signal tới reviewed improvement | Nhiều decision/outcome chain truy vết đầu-cuối | A3-production; multi-agent chỉ advanced optional |

Xem phiên bản Bot, dependency và gate chi tiết tại [`docs/BOT-EVOLUTION-ROADMAP.md`](docs/BOT-EVOLUTION-ROADMAP.md).

## Reality ladder — Thang bằng chứng thực tế

Reality không phải lane tùy chọn. Đây là phần của Mission PASS theo đúng scope:

```text
M00  REAL_PUBLIC_OBSERVATION
M01  REAL_SECOND_SNAPSHOT
M02  GROUNDED_AI_ON_REAL_EVIDENCE
M03  HUMAN_PUBLISHED_TRACKED_ARTIFACT
M04  REAL_ANALYTICS_OUTCOME
M05  REAL_DECISION_OUTCOME_IMPROVEMENT
M06  OPERATED_AUTOMATIC_OBSERVER
M07  REPLAYABLE_DECISION_MEMORY
M08  AUDITED_READ_TOOL_TRAJECTORY
M09  SHADOW_APPROVAL_TRAJECTORY
M10  GOVERNED_CANARY_TRAJECTORY
M11  PRODUCTION_CLOSED_LOOP
```

Ở mức khái niệm, evidence phải tách **nguồn gốc/eligibility** khỏi **vai trò sử dụng**:

```text
origin / eligibility: real | synthetic
use context khi relevant: test | replay
```

Hai chiều có thể chồng nhau: một synthetic fixture có thể được dùng cho test; một snapshot từng là real observation có thể được replay về sau. Không ép `real | synthetic | test | replay` thành bốn giá trị loại trừ trên cùng một enum. Fixture có thể chứng minh code path, nhưng không tạo `REALITY_VERIFIED`.

### Click, order và doanh thu

Không yêu cầu learner phải có sale để PASS vì sale nằm ngoài quyền kiểm soát trực tiếp. Thay vào đó lưu các milestone độc lập:

```text
REAL_EXPOSURE_OBSERVED
REAL_CLICK_OBSERVED
REAL_ORDER_OBSERVED
REAL_VALID_ORDER_OBSERVED
REAL_COMMISSION_PAID
```

- test click chỉ kiểm tracking plumbing, không phải business outcome;
- hết outcome window mà metric bằng 0 vẫn là outcome thật;
- `missing` khác `zero`;
- order/refund/commission path phải được test bằng fixture trước khi có order thật;
- chỉ claim monetization đã được validate khi evidence thực tế tương ứng tồn tại.

## Một artifact tích lũy, không nhiều bài tập rời

Learner workspace:

```text
lab/learner/affiliate-bot/
```

Mỗi Mission bắt đầu từ commit đã PASS Mission trước. Reference implementation chỉ được mở sau attempt hoặc khi có blocker thật:

```text
TRY
→ RUN
→ OBSERVE
→ PULL 1–3 KNOWLEDGE SLICES
→ FIX / TEST
→ COMPARE
→ SAVE EVIDENCE
→ mới đối chiếu reference nếu cần
```

Không copy một reference version cao rồi coi đó là learner progress.

## Beginner-first và Go just-in-time

Mỗi Mission nên chia thành checkpoint 45–90 phút. Knowledge card bắt buộc nên ngắn, gắn với một failure/gap vừa xuất hiện và tạo artifact ngay.

```text
M00 → terminal, package/function, nullable data/evidence gate có scaffold, output test
M01 → struct, JSON/CSV, file, timestamp, validation
M02 → provider adapter, structured output, error/secret/cost tối thiểu
M06 → context, scheduler, retry, deduplication, observability
M09 → state machine, durable state, idempotency, approval
```

M01 dùng append-only file store hoặc implementation tối giản trước. PostgreSQL, repository abstraction và distributed components chỉ được pull khi scale/recovery/query requirement thật làm chúng cần thiết.

```text
USE BEFORE MASTER
≠
COPY BEFORE UNDERSTAND
```

## AI xuất hiện sớm, authority tăng chậm

```text
A0 — deterministic baseline                         M00–M01
A1 — grounded advisory, không external execute      M02–M07
A2-RO — read-only tool agent                        M08
A3-shadow — intent + policy + durable approval      M09
A3-limited — allowlisted R0/R1 auto; R2 approval    M10
A3-production — governed closed loop                M11
A4 — multi-agent optional sau core, không phải mục tiêu bắt buộc
```

M03 cho learner publish thủ công sau compliance/tracking gate. Đây là business action của human, không phải quyền publish của AI.

## Safety / autonomy

```text
Decision ≠ Execution
Model output = untrusted input
ActionIntent ≠ permission

RISK 0 → internal/read-only, có thể auto
RISK 1 → bounded/reversible side effect + mandatory audit
RISK 2 → consequential action + durable Human Approval
DENY   → hành động bị cấm dù có người bấm approve
```

`DENY` gồm ít nhất: fake click/order, spam, né disclosure, bypass platform policy, restricted/private scraping, credential sharing và unbounded spend.

Public publish, spend, account/platform settings, xóa dữ liệu quan trọng và consequential external communication mặc định là RISK 2. Trước execution phải revalidate evidence, policy, approval expiry, target và idempotency state. Kill switch phải chặn execution độc lập với Agent.

## Evidence và PASS

Mỗi Mission phải lưu chain phù hợp scope:

```text
Observation
→ HumanPrediction
→ BotDecision
→ Action / ActionIntent
→ Outcome
→ Evaluation
→ ChangeProposal
→ BotVersion
```

Trường tối thiểu khi relevant:

- source, `observed_at`, freshness và access/permission method;
- `evidence_kind: real | synthetic` khi contract M00 áp dụng; `test`/`replay` được lưu như role/use context hoặc metadata tương đương khi relevant;
- `fact | estimate | assumption | unknown`;
- human prediction trước Bot output;
- actor thực thi, risk, approval và exact side effect;
- outcome window cùng `pending | partial | final`;
- expected-vs-observed, limitation và next hypothesis;
- code/workflow/model/policy version.

Trạng thái evidence được ghi riêng:

- `CAPABILITY_PASS` — behavior, test và explain-back đạt;
- `REALITY_VERIFIED` — evidence thực tế bắt buộc của Mission đạt;
- `OPERATED` — capability đã chạy đủ window/cycle yêu cầu.

Mission có reality gate không được ghi PASS đầy đủ chỉ bằng sample/replay. Kết quả âm, bằng 0 hoặc inconclusive vẫn có thể PASS nếu measurement đúng và interpretation trung thực.

## Quy tắc cuối

```text
ONE CURRENT MISSION
+ ONE CUMULATIVE BOT
+ REALITY EVIDENCE REQUIRED BY SCOPE
+ ONLY JUST-IN-TIME KNOWLEDGE
+ BASELINE BEFORE AI
+ EVIDENCE BEFORE CONFIDENCE
+ POLICY BEFORE AUTHORITY
+ OUTCOME BEFORE CLAIMED IMPROVEMENT
```