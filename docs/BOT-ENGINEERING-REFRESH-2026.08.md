# Bot Engineering Refresh — Cập nhật kỹ thuật Bot 2026.08

> Đây là **current-knowledge register (sổ đăng ký kiến thức hiện hành)** cho Go-first Bot Engineer track. File này bổ sung nhưng **không thay thế** active canonical `sources/SYLLABUS-v2026.09.md`.

Tiếng Việt là ngôn ngữ chính. English terminology (thuật ngữ tiếng Anh) và tên công nghệ được giữ để đối chiếu nguồn ngoài; khi quan trọng có nghĩa Việt đi kèm. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

**Verified (đã kiểm chứng):** 2026-08-28  
**Scope (phạm vi):** Go runtime, MCP, durable workflows, observability, agent security và agent interoperability.  
**Policy:** xem [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

## Bản đồ cập nhật chính

| Khu vực | Operating update (cập nhật vận hành) | Curriculum mapping | Volatility |
|---|---|---|---|
| Go runtime | Go 1.27.0 phát hành 2026-08-19 | P15/C51; P19/C77; P22/C87 | MEDIUM |
| MCP | Go SDK là Tier 1; protocol line có 2026-07-28 | P15/C51–52; P17/C61; P21; P22/C87 | MEDIUM/HIGH |
| Durable workflows | Temporal Go SDK là current reference mạnh cho durable long-running execution | P15/C53; P17/C66; P19/C74 | MEDIUM |
| Observability | OpenTelemetry Go traces/metrics stable; logs beta | P15/C51; P19/C73 | MEDIUM |
| Agent security | Agent/tool system cần prompt-injection, tool-misuse và least-privilege controls ngoài classic API security | P17/C65–66; P19/C75–76 | MEDIUM/HIGH |
| Agent interoperability | A2A đáng theo dõi nhưng chưa phải Phase-1 requirement | P22/C87 | MEDIUM |

Giải thích nhanh:

- **Runtime (Môi trường chạy)** — phiên bản Go đang dùng để build/run.
- **SDK (Bộ công cụ phát triển phần mềm)** — thư viện/chương trình hỗ trợ tích hợp chuẩn hoặc dịch vụ.
- **Interoperability (Khả năng liên thông)** — khả năng các hệ thống/tool/agent giao tiếp theo contract chung.
- **Durable Workflow (Workflow bền vững)** — workflow giữ state qua chờ lâu/restart.
- **Observability (Khả năng quan sát)** — hiểu hệ thống đang làm gì qua logs/metrics/traces.
- **Agent Security (Bảo mật tác tử AI)** — kiểm soát rủi ro khi model/agent được quyền gọi tool.
- **Least Privilege (Quyền tối thiểu)** — chỉ cấp quyền cần thiết cho nhiệm vụ.
- **Prompt Injection (Tấn công/chỉ dẫn tiêm vào prompt)** — nội dung không tin cậy cố điều khiển model/agent.
- **Side Effect (Tác động bên ngoài)** — hành động làm thay đổi hệ thống hoặc môi trường ngoài process.

## EXT:GO:RELEASES

- **Source:** Go project — Release History
- **URL:** https://go.dev/doc/devel/release
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** 51.1–51.2, 77.x, 87.1

Current reference fact (dữ kiện tham chiếu hiện hành):

- Go 1.27.0 phát hành ngày 2026-08-19.

Curriculum rule:

```text
use a currently supported stable Go release
(dùng một bản Go ổn định đang còn support)
```

Không biến `Go 1.27` thành lesson title hoặc permanent canonical truth. Bootstrap learner/reference của repo dùng Go 1.27 tại thời điểm verified này và phải được cập nhật khi freshness policy yêu cầu.

## EXT:MCP:SDK

- **Source:** Model Context Protocol — official SDK tier documentation
- **URL:** https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/sdk.mdx
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 51.x, 52.2, 61.6, 83.4, 87.2

Current reference facts:

- Go được phân loại là **Tier-1 official MCP SDK language**.
- SDK documentation hiện hành bao phủ protocol line `2026-07-28`.

Curriculum implication (hàm ý cho chương trình):

MCP đã đủ trưởng thành để là interoperability concept (khái niệm liên thông) Bot Engineer phải hiểu, nhưng **không** có nghĩa mọi integration đều phải dùng MCP. REST, webhook và native API vẫn đúng khi đơn giản hơn.

## EXT:MCP:GO-SDK

- **Source:** Official Model Context Protocol Go SDK
- **URL:** https://github.com/modelcontextprotocol/go-sdk
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 51.x, 61.6, 83.4

Dùng SDK này như current implementation reference, không coupling (gắn chặt) domain logic trực tiếp vào MCP SDK types nếu không cần.

## EXT:TEMPORAL:GO-SDK

- **Source:** Temporal Go SDK
- **URL:** https://github.com/temporalio/sdk-go
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** 53.1–53.7, 66.4, 74.x

Current implication:

Temporal là ví dụ trưởng thành cho durable, asynchronous, long-running workflow nơi state và retry có thể sống qua process restart.

Curriculum rule:

```text
teach durable-execution concepts first
(dạy khái niệm durable execution trước)
→ use Temporal as reference when the problem justifies it
(chỉ dùng Temporal khi bài toán thực sự cần)
```

Không bắt buộc Temporal cho cron/job worker đơn giản.

## EXT:OTEL:GO

- **Source:** OpenTelemetry — Go language status
- **URL:** https://opentelemetry.io/docs/languages/go/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** 51.5, 73.1–73.6

Current reference facts:

- traces: stable;
- metrics: stable;
- logs: beta.

Curriculum implication:

Observability nên dùng OpenTelemetry concepts và semantic correlation (liên kết dấu vết có ngữ nghĩa) khi phù hợp; package/version chính xác thuộc freshness layer.

## EXT:OWASP:AGENTIC-2026

- **Source:** OWASP GenAI Security Project — Top 10 for Agentic Applications 2026
- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 65.4, 75.x, 76.x

Security implication (hàm ý bảo mật):

Agent system tạo thêm rủi ro như goal hijacking (chiếm mục tiêu), tool misuse (lạm dụng công cụ), excessive privilege (quyền quá mức), supply-chain trust và unsafe code/action execution. Authentication/API key một mình không giải quyết được các rủi ro này.

Curriculum response:

- model output là untrusted input (đầu vào không được tin mặc định);
- tool permission theo least privilege;
- high-impact side effect phải qua deterministic policy và/hoặc approval;
- prompt injection phải được coi là system-boundary problem (vấn đề ranh giới hệ thống), không chỉ là prompt-writing problem.

## EXT:A2A:SPEC

- **Source:** A2A Protocol specification
- **URL:** https://a2a-protocol.org/latest/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 87.2

Curriculum status:

```text
MCP = MUST UNDERSTAND (phải hiểu)
A2A = SHOULD / WATCH (nên biết / theo dõi)
```

Chỉ adopt (áp dụng) A2A khi có remote-agent interoperability use case thật; không đưa multi-agent/A2A thành mặc định Phase 1.

## Những gì vẫn ổn định dù framework thay đổi

Core Bot Engineer concepts nên giữ giá trị ngay cả khi library hiện hành đổi:

```text
context/cancellation        ngữ cảnh/hủy
bounded concurrency         đồng thời có giới hạn
validation                  kiểm tra/xác thực dữ liệu
provenance                  nguồn gốc dữ liệu
retry/backoff               thử lại/tăng thời gian chờ
idempotency                 tính lặp an toàn
durable state               trạng thái bền vững
explicit tool contracts     hợp đồng công cụ rõ ràng
least privilege             quyền tối thiểu
risk classification         phân loại rủi ro
human approval              phê duyệt của con người
tracing/audit               theo dõi/ghi vết
evaluation                  đánh giá
kill switch                 công tắc dừng khẩn cấp
```

Framework/version change thường phải cập nhật example + freshness register trước, không tự động ép curriculum đổi cấu trúc.