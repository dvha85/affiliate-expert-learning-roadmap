# Lộ trình tiến hóa Bot — M00 đến M11

Tài liệu này định nghĩa **product, reality và authority spine** của chương trình Build-First. Learner phát triển một Affiliate Bot duy nhất; mỗi phiên bản phải thêm capability quan sát được, evidence đúng loại và safety gate tương ứng.

## Mission spine

| Mission | Bot version | Part | Ship target | Reality milestone | AI / authority |
|---|---:|---:|---|---|---|
| M00 | v0.1 | P0 | First evidence-backed ranking + human-vs-bot comparison | 5 public observations thật | A0 |
| M01 | v0.2 | P1 | Validation, append-only snapshots, history, freshness | Second real snapshot | A0 |
| M02 | v0.3 | P1 | Grounded AI advisor + schema/eval/fallback | AI on real public evidence | A1, no tool/write |
| M03 | v0.4 | P2 | Tracked content artifact do human publish | First public human action | A1 advisory; human execute |
| M04 | v0.5 | P2 | Decision→Action→Outcome analytics | First real analytics window | A1 investigation |
| M05 | v0.6 | P3 | Versioned improvement from a measured bottleneck | First closed real feedback loop | A1 copilot |
| M06 | v1.0 | P4 | Reliable automatic read/watch + deterministic alert | Operated automatic observer | A0 core + A1 triage |
| M07 | v1.1 | P4 | DecisionPacket, confidence, freshness, risk và abstention | Replayable decision memory | A1 decision support |
| M08 | v2.0 | P5 | Read-only tool Agent lấy missing evidence | Audited read-tool trajectory | A2-RO |
| M09 | v2.1 | P5 | Shadow ActionIntent + policy + durable approval | Dry-run/sandbox/owned-draft trajectory | A3-shadow |
| M10 | v3.0 | P5 | Limited governed R0/R1 automation; R2 approval | Bounded canary operation | A3-limited |
| M11 | v4.0 | P6 | Production closed loop + reviewed improvement deployment | End-to-end decision/outcome cycles | A3-production |

AI capability levels được định nghĩa tại [`AI-CAPABILITY-LEVELS.md`](AI-CAPABILITY-LEVELS.md). Multi-agent/A2A không phải core Mission; chỉ là advanced option sau khi M11 đã chứng minh một Agent/workflow đơn giản hơn không đủ.

## Dependency

```text
M00 → M01 → M02 → M03 → M04 → M05
  → M06 → M07 → M08 → M09 → M10 → M11
```

Mission sau không thay thế operating loop của Mission trước. Ví dụ M08 có Agent không được bỏ deterministic baseline, source provenance hoặc outcome measurement đã tạo ở M00–M07.

## Vì sao thứ tự này hợp lý

### 1. Reality trước hạ tầng lớn

```text
M00 public evidence + first decision
→ M01 data quality/history vì learner đã thấy dữ liệu đổi và thiếu
```

M01 dùng persistence tối giản đủ để giữ snapshots. Database, repository abstraction hoặc distributed components chỉ được thêm khi query/recovery/scale requirement thật xuất hiện.

### 2. AI sớm nhưng không có quyền sớm

```text
M02 deterministic/human baseline
→ grounded AI analysis
→ schema + evidence + uncertainty
→ evaluation + fallback
```

AI xuất hiện trước khi learner phải xây nhiều infrastructure, nhưng chỉ được phân tích evidence learner đã hiểu. M02 không cấp tool hoặc external execution.

### 3. Hành động thật bằng tay trước tự động hóa

```text
M03 Decision record + compliance/tracking gate
→ human publishes exact artifact
→ M04 measures outcome
→ M05 improves one version from observed bottleneck
```

Learner phải trực tiếp hiểu public action, tracking và consequence trước khi Bot tự tạo ActionIntent ở M09.

### 4. Chỉ tự động hóa signal đã hiểu

```text
M05 measured signal value
→ M06 reliable automatic observation
→ M07 decision + abstention
```

Watcher không được tự động hóa noise chưa được xác định. Decision Engine phải biết `WAIT`, `GET_MORE_DATA` và `HUMAN_REVIEW`, không chỉ trả một recommendation cho mọi input.

### 5. Read tools trước write authority

```text
M08 A2 read-only evidence collection
→ M09 A3 shadow intent/approval
→ M10 bounded R0/R1 auto action
→ M11 production closed loop
```

Mỗi bước tăng authority chỉ xảy ra sau khi bước trước có evaluation, failure evidence và operational control.

## Reality ladder

| Gate | Bằng chứng bắt buộc | Không được dùng thay thế |
|---|---|---|
| M00 | URL/public source + observed time + human judgment | sample-only ranking |
| M01 | ít nhất hai observations khác thời điểm trên cùng subject | overwrite current row rồi gọi là history |
| M02 | AI claims truy được về evidence; known-label eval | demo text nghe hợp lý |
| M03 | tracked public artifact do human publish + policy/disclosure evidence | local draft |
| M04 | analytics snapshot sau outcome window | hard-coded metrics |
| M05 | decision/action/outcome/evaluation chain thật | đổi công thức chỉ để output đẹp hơn |
| M06 | scheduled cycles + retry/dedup/alert evidence | gọi function một lần |
| M07 | stale/missing/conflict replay dẫn tới state đúng | confidence không có method/reason |
| M08 | tool-call trace với permission/timeout/injection cases | Agent answer không có trajectory |
| M09 | durable approval, restart, expiry, revalidation, idempotency | chat “OK” làm approval record duy nhất |
| M10 | canary log trong scope/time/budget cap | dry-run đơn lẻ |
| M11 | trigger→decision→action→outcome→reviewed change trace | self-reported end-to-end demo |

Evidence phải có `real | test | synthetic | replay`. Fixture chứng minh behavior nhưng không tự tạo `REALITY_VERIFIED`.

## Decision và outcome progression

```text
M00  Observation + HumanPrediction + baseline BotDecision
M01  provenance + freshness + history
M02  AnalysisPacket-like grounded AI output
M03  Decision record + human Action record
M04  Outcome record + window/status
M05  Evaluation + ChangeProposal
M06  SignalPacket + reliable alert
M07  DecisionPacket + abstention + RiskLevel/PolicyDecision
M08  evidence escalation qua read tools
M09  ActionIntent + ApprovalRequest + shadow ExecutionRecord
M10  governed ExecutionRecord thật trong bounded policy
M11  Decision/Outcome Memory + reviewed deployment loop
```

Logical contracts vẫn tách biệt:

```text
Fact / Signal
≠ Analysis
≠ Decision
≠ ActionIntent
≠ ExecutionRecord
≠ Outcome
```

Xem [`DECISION-CONTRACTS.md`](DECISION-CONTRACTS.md) và [`DECISION-OUTCOME-MEMORY.md`](DECISION-OUTCOME-MEMORY.md).

## Outcome không phải điểm may mắn

Mission PASS đánh giá measurement và reasoning nằm trong quyền learner kiểm soát; không đánh giá bằng việc may mắn có sale.

- test click xác nhận tracking, không phải real market response;
- zero impressions/clicks sau window là outcome thật và có thể dẫn tới distribution experiment;
- `missing` không được chuyển thành `0`;
- order/refund/valid/paid path được test bằng fixture từ M04;
- real order/commission được ghi ngay khi xuất hiện nhưng không phải gate bắt buộc;
- chỉ claim monetization validated khi có evidence thật tương ứng.

## Safety progression

```text
M00–M01  public/manual read, deterministic compute
M02–M07  A1 advisory; no AI external execution
M03      human-only public publish after compliance/tracking gate
M06      automatic read/watch only on allowed source/access method
M08      read-only allowlisted tools
M09      all side effects shadow/draft + durable approval machinery
M10      allowlisted bounded R0/R1 auto; R2 durable approval
M11      same policy boundary in production + recovery/monitoring
```

```text
RISK 0 → internal/read-only auto
RISK 1 → bounded/reversible + mandatory audit
RISK 2 → durable Human Approval + revalidation
DENY   → prohibited regardless of approval
```

Public publish, spend, account/platform setting, consequential communication và destructive action mặc định là RISK 2. Fake engagement, disclosure evasion, policy bypass, restricted scraping, credential sharing và unbounded spend là `DENY`.

## Upgrade gates

Không tăng AI/authority level chỉ vì framework mới có sẵn. Mission chỉ nâng level khi có:

1. business signal/value đã quan sát;
2. deterministic hoặc human baseline;
3. failure modes và evaluation cases;
4. evidence/freshness contract;
5. permission/risk boundary;
6. fallback, audit và acceptable cost;
7. PASS/REALITY/OPERATED evidence của Mission trước.

## Final closed loop

```text
SENSE / COLLECT
→ SignalPacket
→ deterministic analytics
→ grounded AnalysisPacket khi có giá trị
→ DecisionPacket hoặc ABSTAIN
→ Policy + Risk
→ ActionIntent
→ auto trong R0/R1 bounds hoặc durable approval cho R2
→ ExecutionRecord
→ Outcome
→ Evaluation
→ ChangeProposal
→ offline test/eval
→ human-reviewed versioned deploy
↺
```

Bot không được âm thầm rewrite production prompt, scoring weights, workflow hoặc policy từ một outcome mới.
