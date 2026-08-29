# Kiến trúc AI/Agent Decision Intelligence

> Tài liệu authority cho lớp AI/Agent của Build-First. Nó mở rộng execution layer, **không thay** canonical curriculum `v2026.09`, 23 Parts / 89 Chapters / 671 Lessons / 14 Projects hay Mission spine `M00–M15`.

## 1. Mục tiêu

Affiliate Intelligence Bot phải ra quyết định nhanh hơn nhờ kết hợp dữ liệu, logic xác định, mô hình dự báo và AI reasoning (suy luận AI), nhưng AI không được tự trở thành authority cho external execution (thực thi bên ngoài).

```text
EVENT / DATA
→ Freshness + Quality Gate
→ Deterministic Analytics / Forecast / ML
→ AI Analyst / Agent
→ Evidence Escalation / Tool Use
→ Decision Fusion
→ DecisionPacket
→ Policy + Risk
→ RISK 0/1 auto hoặc RISK 2 Human Approval
→ Action
→ Outcome
→ Evaluation + Decision/Outcome Memory
↺
```

## 2. Các invariant bắt buộc

```text
DATA > OPINION
MODEL OUTPUT = UNTRUSTED INPUT
DECISION ≠ EXECUTION
AI ADVICE ≠ EXECUTION AUTHORITY
POLICY BEFORE CONSEQUENTIAL ACTION
```

- deterministic rule/formula vẫn được ưu tiên khi bài toán diễn đạt rõ bằng logic xác định;
- AI dùng để hiểu dữ liệu phi cấu trúc, tổng hợp evidence, tạo hypothesis, điều tra và reasoning trong vùng cho phép;
- RiskLevel và PolicyDecision không được giao cho LLM làm authority duy nhất;
- RISK 2 luôn cần durable Human Approval và revalidation trước execute;
- AI unavailable không được làm hỏng deterministic core nếu Mission không bắt buộc AI để đạt ship target cơ bản.

## 3. AI Capability Levels — Cấp năng lực AI

| Level | Phạm vi | Authority | Mission điển hình |
|---|---|---|---|
| **A0** | Deterministic only (chỉ logic xác định) | không có AI | M00–M04 |
| **A1** | AI advisory/read-only (AI tư vấn/chỉ đọc) | phân tích, tóm tắt, đề xuất; không external execute | M05–M10 |
| **A2** | Tool-assisted Agent (Agent dùng tool) | gọi tool theo contract; side effect vẫn qua policy | M11–M12 |
| **A3** | Governed Action Agent (Agent hành động có kiểm soát) | tạo ActionIntent; RISK0/1 theo policy, RISK2 approval | M13–M14 |
| **A4** | Optional multi-agent (đa Agent tùy chọn) | chỉ khi có service/agent boundary thật | M15 |

```text
AI APPEARS EARLY
≠
AI GETS AUTHORITY EARLY
```

## 4. Bốn contract xuyên suốt

```text
SignalPacket
→ AnalysisPacket
→ DecisionPacket
→ ActionIntent
```

### SignalPacket

Fact đã được hệ thống phát hiện, có provenance (nguồn gốc) và freshness (độ mới).

```yaml
subject: product:P123
event: commission_changed
before: 0.12
after: 0.18
detected_at: 2026-08-29T08:00:00+07:00
source_ref: snapshot:abc
freshness_seconds: 30
```

### AnalysisPacket

Kết quả phân tích, có thể chứa AI reasoning nhưng phải gắn evidence và uncertainty.

```yaml
summary: commission tăng đáng kể
possible_causes: []
evidence_refs: []
missing_evidence: []
confidence: 0.82
uncertainty: []
recommended_investigation: []
```

### DecisionPacket

Kết quả Decision Intelligence đã hợp nhất deterministic signals + AI assessment + freshness + risk/policy context. Chi tiết bắt buộc nằm trong `docs/DECISION-CONTRACTS.md`.

### ActionIntent

Ý định hành động trước execution. ActionIntent chưa phải quyền thực thi và luôn đi qua Policy/Risk boundary.

## 5. Event-driven decision — quyết định theo sự kiện

Không dùng mẫu mặc định:

```text
cron → hỏi LLM toàn bộ dữ liệu liên tục
```

Ưu tiên:

```text
deterministic event/change
→ material change?
→ collect required evidence
→ invoke AI/decision workflow khi đáng giá
```

Trigger điển hình:

- state changed;
- anomaly detected;
- threshold crossed;
- freshness expired;
- experiment completed;
- revenue reconciled;
- approval completed;
- policy/platform snapshot changed.

Mục tiêu là giảm latency khi thật sự có thay đổi, đồng thời giảm model cost và alert noise.

## 6. Decision Fusion — hợp nhất quyết định

Decision Engine có thể nhận nhiều evidence channel:

```text
Rule Engine
+ Scoring / Ranking
+ Forecast / ML
+ Anomaly signals
+ Experiment evidence
+ AI AnalysisPacket
→ Decision Fusion
→ DecisionPacket
```

AI không được âm thầm override rule/policy. Conflict giữa các nguồn phải hiện ra dưới dạng evidence, confidence, uncertainty hoặc yêu cầu lấy thêm dữ liệu.

## 7. Evidence escalation — lấy thêm bằng chứng khi thiếu

```text
Enough evidence?
├─ YES → DecisionPacket
└─ NO
   → request allowed read tools/data
   → collect more evidence
   → reevaluate
```

Các quyết định `WAIT`, `GET_MORE_DATA`, `HUMAN_REVIEW` là kết quả hợp lệ khi evidence chưa đủ.

## 8. Tách AI provider khỏi domain core

Core Go application dùng provider-neutral interface (giao diện trung lập nhà cung cấp). Không để provider SDK type lan vào domain model, DecisionPacket, Policy hoặc ActionIntent.

Provider-specific capability như model routing, deferred tool loading hoặc programmatic tool calling chỉ là implementation option (lựa chọn triển khai), không phải canonical business truth.

## 9. Safety progression

```text
A0/A1: no external AI authority
A2: tool use with explicit permission + validation
A3: governed ActionIntent + Policy/Risk + approval
A4: multi-agent optional, same security boundaries
```

Mọi external content từ web/product/review/email/API/RAG/MCP đều là untrusted input.

## 10. Mapping vào Mission

- M05: AI Alert Triage ở A1;
- M06: AI Product Research ở A1;
- M08: Revenue/Attribution Investigation ở A1;
- M09: Experiment Copilot ở A1;
- M10: Decision Fusion + DecisionPacket;
- M11: AI analysis + model routing + evaluation;
- M12: Tool-Using Agent + MCP/tool discovery;
- M13: governed ActionIntent + durable approval;
- M14: production evaluation/observability/security;
- M15: full closed loop; multi-agent/A2A chỉ optional khi có nhu cầu thật.

## 11. Quy tắc thay đổi

Nếu một AI framework, protocol hoặc provider capability thay đổi, ưu tiên cập nhật freshness layer và implementation note. Không tự đổi canonical lesson/project counts hoặc policy authority.