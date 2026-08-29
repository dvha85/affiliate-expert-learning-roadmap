# AI Provider Capability Matrix — Ma trận năng lực nhà cung cấp AI

> Đây là contract đánh giá capability, không phải danh sách version cố định. Version/model/API cụ thể thuộc freshness layer và phải re-verify trước production use.

## 1. Nguyên tắc

Domain core của Affiliate Intelligence Bot không được phụ thuộc trực tiếp vào một provider SDK.

```text
Go Domain / Decision / Policy
        ↓
AI Provider Interface
        ↓
Provider Adapter(s)
```

## 2. Capability cần đánh giá

| Capability | Câu hỏi đánh giá |
|---|---|
| Structured Output | Có enforce schema/typed output đủ tin cậy không? |
| Tool Calling | Tool schema, validation và multi-step flow hỗ trợ đến đâu? |
| Tool Discovery / Deferred Loading | Có thể chỉ nạp tool cần thiết theo task không? |
| Parallel / Programmatic Tool Use | Có bounded orchestration nhiều read calls hiệu quả không? |
| Reasoning | Có phù hợp investigation/decision ambiguity không? |
| Context / Retrieval | Grounding và retrieval integration ra sao? |
| Stateful / Resume | Có hỗ trợ pause/resume hoặc cần workflow layer ngoài? |
| Latency | p50/p95 thực tế cho task mục tiêu? |
| Cost | cost / analysis / decision? |
| Evaluation | Có trace/eval hooks hay export observability không? |
| Security / Data Controls | retention, region, privacy, enterprise controls? |
| Exit Path | Adapter có cho đổi provider mà không rewrite domain core không? |

## 3. Routing theo capability

Không mặc định dùng model mạnh nhất cho mọi việc.

```text
extract / classify / summarize
→ fast, low-cost capability

investigation / conflicting evidence
→ stronger reasoning capability

high-value ambiguous recommendation
→ strongest allowed reasoning capability
```

PolicyDecision và RiskLevel authority không được route sang LLM như một black-box policy replacement.

**Exact provider/model mapping nằm config/freshness layer**, không nằm trong domain Decision/Policy contract.

## 4. Fallback

Mission A1 phải định nghĩa deterministic fallback hoặc degraded mode phù hợp.

Ví dụ:

```text
AI triage unavailable
→ deterministic alert vẫn tồn tại
→ alert được đánh dấu chưa có AI analysis
```

## 5. Freshness

Khi ghi một capability cụ thể của provider, phải lưu ít nhất:

- source URL;
- verified date;
- volatility;
- affected Mission/Part;
- fallback nếu capability bị đổi/deprecate.

Không biến tên model hiện hành thành canonical Lesson title hoặc permanent invariant.

## 6. Adoption gate

Chỉ adopt provider-specific capability khi:

1. giảm latency/cost hoặc tăng quality đo được;
2. permission/risk model vẫn giữ nguyên;
3. có test/evaluation;
4. có fallback/exit path;
5. không làm provider type leak vào business/domain contracts.