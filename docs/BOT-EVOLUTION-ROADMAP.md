# Lộ trình tiến hóa Bot — M00 đến M11

Tài liệu này định nghĩa **trục sản phẩm, thực tế và quyền hành động (`product, reality, authority spine`)** của chương trình Build-First. Người học phát triển một Affiliate Bot duy nhất; mỗi phiên bản phải thêm capability (năng lực) quan sát được, evidence (bằng chứng) đúng loại và safety gate (cổng an toàn) tương ứng.

## Trục Mission

| Mission | Phiên bản Bot | Part | Mục tiêu phát hành | Mốc thực tế | AI / quyền hành động |
|---|---:|---:|---|---|---|
| M00 | v0.1 | P0 | Xếp hạng đầu tiên dựa trên evidence + so sánh người với Bot | 5 quan sát công khai thật | A0 |
| M01 | v0.2 | P1 | Validation, snapshot chỉ-thêm (`append-only`), history, freshness | Snapshot thật lần hai | A0 |
| M02 | v0.3 | P1 | AI advisor có grounding + schema/eval/fallback | AI trên evidence công khai thật | A1, không tool/write |
| M03 | v0.4 | P2 | Artifact nội dung có tracking do người publish | Hành động công khai đầu tiên của người | A1 tư vấn; người thực thi |
| M04 | v0.5 | P2 | Phân tích Decision→Action→Outcome | Cửa sổ analytics thật đầu tiên | A1 điều tra |
| M05 | v0.6 | P3 | Cải tiến có version từ bottleneck đã đo | Vòng phản hồi thật khép kín đầu tiên | A1 copilot |
| M06 | v1.0 | P4 | Tự động đọc/theo dõi đáng tin cậy + cảnh báo tất định | Bộ quan sát tự động đã vận hành | A0 lõi + A1 phân loại |
| M07 | v1.1 | P4 | `DecisionPacket`, confidence, freshness, risk và abstention | Bộ nhớ quyết định có thể phát lại | A1 hỗ trợ quyết định |
| M08 | v2.0 | P5 | Agent dùng công cụ chỉ-đọc để lấy evidence còn thiếu | Quỹ đạo gọi tool có audit | A2-RO |
| M09 | v2.1 | P5 | `ActionIntent` chạy bóng + policy + approval bền vững | Quỹ đạo dry-run/sandbox/owned-draft | A3-shadow |
| M10 | v3.0 | P5 | Tự động hóa R0/R1 giới hạn có quản trị; R2 cần approval | Canary trong phạm vi giới hạn | A3-limited |
| M11 | v4.0 | P6 | Vòng production khép kín + triển khai cải tiến đã review | Chu kỳ decision/outcome đầu-cuối | A3-production |

Các mức năng lực AI được định nghĩa tại [`AI-CAPABILITY-LEVELS.md`](AI-CAPABILITY-LEVELS.md). Multi-agent/A2A không phải Mission cốt lõi; chỉ là lựa chọn nâng cao khi M11 đã chứng minh một Agent/workflow đơn giản hơn không đủ.

## Trục Affiliate Intelligence

Mỗi phiên bản Bot phải làm trưởng thành thêm cùng một hợp đồng domain, không chỉ thêm năng lực kỹ thuật. Xem [`AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md`](AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md).

```text
M00 Sản phẩm/Offer + Evidence + lý do tất định
→ M01 history/freshness đáng tin cậy
→ M02 giả thuyết audience/angle có grounding; field không được hỗ trợ phải reject/fallback
→ M03 Audience/Problem + Content Angle + Hook/CTA + Channel + Timing + rủi ro publish của người
→ M04 funnel/outcome thật + assumption của EV
→ M05 Phép đo / Experiment tiếp theo từ bottleneck thật
→ M06 tín hiệu tự động đáng tin cậy
→ M07 DecisionPacket chuẩn + confidence/uncertainty/risk/abstention
→ M08 read tools để lấp missing evidence
→ M09 recommendation → ActionIntent, chưa phải permission
→ M10 hành động có quản trị trong giới hạn
→ M11 quyết định Affiliate Intelligence đầu-cuối → outcome → reviewed change
```

Field chưa có evidence phải giữ `unknown`/`not_yet_observable` hoặc decision state như `GET_MORE_DATA`; mức trưởng thành tự động hóa không được dùng để bịa domain intelligence.

## Quan hệ phụ thuộc

```text
M00 → M01 → M02 → M03 → M04 → M05
  → M06 → M07 → M08 → M09 → M10 → M11
```

Mission sau không thay thế operating loop (vòng vận hành) của Mission trước. Ví dụ M08 có Agent không được bỏ deterministic baseline, source provenance hoặc outcome measurement đã tạo ở M00–M07.

## Vì sao thứ tự này hợp lý

### 1. Thực tế trước hạ tầng lớn

```text
M00 evidence công khai + quyết định đầu tiên
→ M01 chất lượng dữ liệu/history vì learner đã thấy dữ liệu đổi và thiếu
```

M01 dùng persistence (lưu trữ bền) tối giản đủ để giữ snapshot. Database, repository abstraction hoặc distributed component chỉ được thêm khi nhu cầu query/recovery/scale thật xuất hiện.

### 2. AI xuất hiện sớm nhưng chưa có quyền sớm

```text
M02 deterministic/human baseline
→ phân tích AI có grounding
→ schema + evidence + uncertainty
→ evaluation + fallback
```

AI xuất hiện trước khi learner phải xây nhiều infrastructure, nhưng chỉ được phân tích evidence learner đã hiểu. M02 không cấp tool hoặc external execution.

### 3. Người làm hành động thật đầu tiên trước tự động hóa

```text
M03 Decision record + compliance/tracking gate
→ người publish exact artifact
→ M04 đo outcome
→ M05 cải tiến một version từ bottleneck quan sát được
```

Learner phải trực tiếp hiểu public action, tracking và consequence trước khi Bot tự tạo `ActionIntent` ở M09.

### 4. Chỉ tự động hóa signal đã hiểu

```text
M05 giá trị signal đã đo
→ M06 quan sát tự động đáng tin cậy
→ M07 quyết định + abstention
```

Watcher (bộ theo dõi) không được tự động hóa noise chưa xác định. Decision Engine phải biết `WAIT`, `GET_MORE_DATA` và `HUMAN_REVIEW`, không chỉ trả recommendation cho mọi input.

### 5. Công cụ chỉ-đọc trước quyền ghi

```text
M08 A2 thu evidence bằng read-only tool
→ M09 A3 shadow intent/approval
→ M10 tự động R0/R1 giới hạn
→ M11 vòng production khép kín
```

Mỗi bước tăng authority chỉ xảy ra sau khi bước trước có evaluation, failure evidence và operational control.

## Thang bằng chứng thực tế

| Gate | Bằng chứng bắt buộc | Không được dùng thay thế |
|---|---|---|
| M00 | URL/public source + observed time + human judgment | sample-only ranking |
| M01 | ít nhất hai observation khác thời điểm trên cùng subject | overwrite current row rồi gọi là history |
| M02 | claim của AI truy được về evidence; known-label eval | demo text nghe hợp lý |
| M03 | tracked public artifact do người publish + policy/disclosure evidence | local draft |
| M04 | analytics snapshot sau outcome window | hard-coded metrics |
| M05 | chain decision/action/outcome/evaluation thật | đổi công thức chỉ để output đẹp hơn |
| M06 | scheduled cycles + retry/dedup/alert evidence | gọi function một lần |
| M07 | replay stale/missing/conflict dẫn tới state đúng | confidence không có method/reason |
| M08 | tool-call trace với permission/timeout/injection cases | Agent answer không có trajectory |
| M09 | durable approval, restart, expiry, revalidation, idempotency | chat “OK” làm approval record duy nhất |
| M10 | canary log trong scope/time/budget cap | dry-run đơn lẻ |
| M11 | trigger→decision→action→outcome→reviewed change trace | self-reported end-to-end demo |

Evidence phải có `real | test | synthetic | replay`. Fixture chứng minh behavior nhưng không tự tạo `REALITY_VERIFIED`.

## Tiến triển của Decision và Outcome

```text
M00  Observation + HumanPrediction + baseline BotDecision
M01  provenance + freshness + history
M02  output AI có grounding dạng AnalysisPacket
M03  Decision record + Action record của người
M04  Outcome record + window/status
M05  Evaluation + ChangeProposal
M06  SignalPacket + cảnh báo đáng tin cậy
M07  DecisionPacket + abstention + RiskLevel/PolicyDecision
M08  tăng cường evidence qua read tools
M09  ActionIntent + ApprovalRequest + shadow ExecutionRecord
M10  governed ExecutionRecord thật trong bounded policy
M11  Decision/Outcome Memory + vòng triển khai đã review
```

Các hợp đồng logic vẫn tách biệt:

```text
Fact / Signal
≠ Analysis
≠ Decision
≠ ActionIntent
≠ ExecutionRecord
≠ Outcome
```

Xem [`DECISION-CONTRACTS.md`](DECISION-CONTRACTS.md), [`AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md`](AFFILIATE-INTELLIGENCE-DECISION-CONTRACT.md) và [`DECISION-OUTCOME-MEMORY.md`](DECISION-OUTCOME-MEMORY.md).

## Outcome không phải điểm may mắn

Mission PASS đánh giá measurement và reasoning nằm trong quyền learner kiểm soát; không đánh giá bằng việc may mắn có sale.

- test click xác nhận tracking, không phải phản hồi thị trường thật;
- zero impression/click sau window là outcome thật và có thể dẫn tới giả thuyết distribution;
- `missing` không được chuyển thành `0`;
- order/refund/valid/paid path được test bằng fixture từ M04;
- real order/commission được ghi ngay khi xuất hiện nhưng không phải gate bắt buộc;
- chỉ claim monetization validated khi có evidence thật tương ứng.

## Tiến triển an toàn

```text
M00–M01  đọc công khai/thủ công, tính toán tất định
M02–M07  A1 tư vấn; AI không tự thực thi bên ngoài
M03      người tự publish sau compliance/tracking gate
M06      tự động read/watch chỉ trên source/access method được phép
M08      tool chỉ-đọc trong allowlist
M09      mọi side effect ở shadow/draft + approval bền vững
M10      R0/R1 trong allowlist và giới hạn; R2 cần approval bền vững
M11      cùng policy boundary trong production + recovery/monitoring
```

```text
RISK 0 → nội bộ/chỉ-đọc tự động
RISK 1 → giới hạn/có thể đảo ngược + audit bắt buộc
RISK 2 → Human Approval bền vững + revalidation
DENY   → cấm bất kể có approval
```

Public publish, spend, account/platform setting, consequential communication và destructive action mặc định là RISK 2. Fake engagement, disclosure evasion, policy bypass, restricted scraping, credential sharing và unbounded spend là `DENY`.

## Cổng nâng cấp

Không tăng AI/authority level chỉ vì framework mới có sẵn. Mission chỉ nâng level khi có:

1. business signal/value đã quan sát;
2. deterministic hoặc human baseline;
3. failure mode và evaluation case;
4. evidence/freshness contract;
5. permission/risk boundary;
6. fallback, audit và acceptable cost;
7. PASS/REALITY/OPERATED evidence của Mission trước.

## Vòng khép kín cuối cùng

```text
CẢM NHẬN / THU THẬP
→ SignalPacket
→ analytics tất định
→ AnalysisPacket có grounding khi có giá trị
→ Affiliate Intelligence DecisionPacket hoặc ABSTAIN
   (Product/Offer, Audience/Problem, Content/Channel, EV,
    Evidence, Confidence, Uncertainty, Risk, Next Measurement)
→ Policy + Risk
→ ActionIntent
→ tự động trong giới hạn R0/R1 hoặc durable approval cho R2
→ ExecutionRecord
→ Outcome
→ Evaluation
→ ChangeProposal
→ offline test/eval
→ human-reviewed versioned deploy
↺
```

Bot không được âm thầm rewrite production prompt, scoring weight, workflow hoặc policy từ một outcome mới.
