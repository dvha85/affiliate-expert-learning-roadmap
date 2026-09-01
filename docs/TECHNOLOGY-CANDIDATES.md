# Technology Candidates — ứng viên công nghệ để đánh giá tại đúng Mission boundary

- **Status:** Reference only — không phải Core/PASS requirement
- **Last reviewed:** 2026-09-01
- **Primary architecture authority:** [`ADR-001-GO-FIRST-BOT-STACK.md`](ADR-001-GO-FIRST-BOT-STACK.md)

Tài liệu này ghi lại các công nghệ đáng xem xét cho Affiliate Intelligence Bot khi learner đã có evidence/bottleneck thực tế. Nó **không** khóa roadmap vào một vendor/framework và không cho phép công nghệ mới tăng authority của Bot sớm hơn Mission hiện tại.

## 1. Nguyên tắc không đổi

```text
Go core
= evidence / history / deterministic decision / policy / audit authority

Orchestrator / Agent runtime
= optional implementation layer
= chỉ được thêm khi Mission/bottleneck thật sự justify
```

Không chuyển business truth, scoring authority hoặc risk/policy authority sang workflow canvas hay LLM chỉ vì integration nhanh hơn.

Adoption progression mặc định:

```text
manual / deterministic Go
→ reliable Go capability
→ optional orchestration
→ read-only agent
→ shadow action
→ governed bounded automation
```

## 2. Candidate A — n8n

### Candidate role

Ưu tiên đánh giá n8n như **workflow/orchestration layer**, không phải decision engine.

Potential fit:

- scheduler / trigger / webhook;
- API/integration glue;
- notification/alert routing;
- human approval routing;
- analytics/import workflow;
- calling Go services/CLI/API;
- bounded workflow execution sau khi Go policy đã quyết định.

Không mặc định đặt trong n8n:

- Product ranking logic;
- evidence truth classification;
- deterministic risk policy;
- final `ALLOW | DENY | HUMAN_REVIEW` authority;
- canonical business state nếu không có explicit persistence/audit contract.

### Roadmap evaluation points

| Mission | Mức xem xét | Lý do |
|---|---|---|
| M00–M05 | Chưa cần | Core evidence/decision/market loop phải tự chứng minh trước |
| M06 | **Candidate mạnh** | watcher, trigger, integration và alert orchestration bắt đầu có giá trị |
| M07 | Optional | DecisionPacket/policy vẫn ưu tiên Go core |
| M08 | Optional bridge | có thể gọi read-only agent/tool workflow nhưng không thay Tool Registry/policy |
| M09 | **Candidate mạnh** | approval/shadow workflow/routing |
| M10 | **Candidate mạnh** | bounded RISK0/RISK1 workflow sau deterministic policy gate |
| M11 | Candidate production layer | integration/orchestration nếu reliability/audit đạt yêu cầu |

### Adoption gate cho n8n

Chỉ promote từ `candidate` thành implementation choice khi có ít nhất một bottleneck cụ thể, ví dụ:

- số integration/webhook bắt đầu tạo nhiều glue code;
- scheduler/approval routing làm Go application phức tạp nhưng không phải business logic;
- cần visual operational workflow cho single operator;
- integration cần thay đổi nhanh hơn release cycle của Go core.

Phải chứng minh trước adoption:

```text
same Go Decision/Policy contract
+ n8n failure/retry behavior
+ idempotency
+ audit/correlation
+ secret handling
+ no authority bypass
```

## 3. Candidate B — Hermes Agent

Ở đây `Hermes Agent` chỉ ứng viên cho **agent runtime / research-tool layer**, không phải Bot core.

### Candidate role

Potential fit:

- read-only research khi `GET_MORE_DATA`;
- web/file/tool evidence collection qua explicit permission;
- decomposition/delegation của research task;
- memory/session hỗ trợ investigation;
- scheduled read-only research nếu Mission sau justify.

Không cho Hermes mặc định:

- tự tạo measured fact từ inference;
- tự sửa canonical Product/history/scoring input;
- tự quyết định risk level;
- tự publish/send/spend/change account;
- unrestricted terminal/browser/tool access chỉ vì framework hỗ trợ.

### Roadmap evaluation points

| Mission | Mức xem xét | Lý do |
|---|---|---|
| M00–M01 | Không dùng | deterministic evidence/data foundation trước |
| M02 | Chỉ reference | AI advisory chưa có tools/write authority |
| M03–M07 | Chưa cần cho Core | tiếp tục tích lũy real outcome + reliable DecisionPacket |
| M08 | **Candidate mạnh** | khớp `read-only evidence agent` với explicit tool permission/audit |
| M09 | Shadow-only nếu cần | agent có thể đề xuất ActionIntent nhưng không execute |
| M10–M11 | Re-evaluate | chỉ mở thêm authority qua deterministic policy/approval/kill-switch |

### Adoption gate cho Hermes

Chỉ chạy spike khi M08 có một missing-evidence case thật mà deterministic/manual retrieval bắt đầu tốn công.

Spike phải so ít nhất:

```text
manual / deterministic retrieval baseline
vs
Hermes read-only agent
```

Theo các tiêu chí:

- evidence correctness / grounding;
- unsupported claim rate;
- tool-call success/failure;
- permission compliance;
- prompt-injection resistance;
- auditability;
- latency/cost;
- human intervention rate.

Nếu framework không thể giới hạn tool/permission/audit theo contract của repo, **không adopt** dù demo trông thông minh.

## 4. Kiến trúc ứng viên dài hạn

```text
                    Go Decision / Policy Core
                    evidence + history + audit
                              │
              ┌───────────────┴───────────────┐
              │                               │
      n8n orchestration               Hermes Agent
      trigger/integration              read-only research
      approval/routing                 explicit tools only
              │                               │
              └───────────────┬───────────────┘
                              │
                        External world
```

Ranh giới bắt buộc:

```text
Hermes candidate evidence
→ Go validation/grounding
→ Go Decision/Policy
→ ActionIntent
→ n8n workflow/routing (nếu được adopt)
→ approval/execution theo Mission authority
```

Không cho phép shortcut:

```text
Agent confidence
→ direct execution
```

hoặc:

```text
n8n workflow branch
→ tự nâng RISK2 thành auto execute
```

## 5. Candidate status

| Công nghệ | Hiện trạng | Revisit earliest | Mandatory? |
|---|---|---|---|
| n8n | Candidate | M06 | Không |
| Hermes Agent | Candidate | M08 | Không |

`Revisit earliest` không có nghĩa Mission đó phải dùng công nghệ này. Đến Mission boundary, learner phải hỏi lại:

1. bottleneck thật là gì?
2. Go/core implementation hiện tại còn đủ đơn giản không?
3. candidate giải quyết bottleneck nào đo được?
4. candidate có phá deterministic/policy/audit boundary không?
5. failure/fallback khi candidate unavailable là gì?
6. dependency/operational cost có đáng không?

Nếu chưa có câu trả lời đủ mạnh, giữ candidate ở trạng thái **không adopt**.

## 6. Freshness note

Capabilities của n8n/Hermes thay đổi nhanh. Trước spike/adoption phải kiểm lại official docs, version, license/deployment model, security/tool-permission behavior và integration support tại thời điểm đó.

Tài liệu này ghi **architectural candidate**, không đóng băng current feature list thành curriculum truth.
