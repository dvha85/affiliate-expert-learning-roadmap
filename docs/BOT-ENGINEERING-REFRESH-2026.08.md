# Bot Engineering Refresh — Cập nhật kỹ thuật Bot 2026.08

> Đây là **current-knowledge register (sổ đăng ký kiến thức hiện hành)** cho Go-first Bot Engineer track. [`../CURRICULUM.md`](../CURRICULUM.md) là active canonical; file này chỉ cung cấp current facts cho Core/Mission/Advanced/Reference và không tự thay đổi learning outcome hay authority boundary.

Các mapping kiểu `P15/C51` hoặc lesson ID cũ trong revision trước chỉ là historical provenance. Mapping hiện hành bên dưới dùng active Chapter `C0–C20`, Mission `M00–M11` và Advanced module; `sources/SYLLABUS-v2026.09.md` không còn là active authority.

Tiếng Việt là ngôn ngữ chính. English terminology và tên công nghệ được giữ để đối chiếu nguồn ngoài; khi quan trọng có nghĩa Việt đi kèm. Xem [`LANGUAGE-POLICY.md`](LANGUAGE-POLICY.md) và [`GLOSSARY-VI.md`](GLOSSARY-VI.md).

**Verified:** 2026-08-29  
**Scope:** Go runtime, MCP, durable workflows, observability, agent security/interoperability và current agent-tool implementation references.  
**Policy:** xem [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

## Bản đồ cập nhật chính

| Khu vực | Operating update | Curriculum mapping | Volatility |
|---|---|---|---|
| Go runtime | Go 1.27.0 phát hành 2026-08-19 | Core C0/C3–C4/C12/C18; M00–M01/M06/M11; Reference cookbook | MEDIUM |
| MCP | Spec `2026-07-28`: stateless core, MRTR, header routing, cacheable lists, auth hardening, extensions/Tasks | Advanced A09; optional adapter cho M08+; Reference | HIGH |
| MCP Go | Go SDK là Tier 1 current reference | Advanced A09; optional adapter cho C15/M08 | MEDIUM/HIGH |
| Durable workflows | Temporal Go SDK là reference cho long-running durable execution | Core C16–C19; M09–M11; Advanced A10 | MEDIUM |
| Agent tool discovery | Current provider runtimes có deferred tool loading/tool search và programmatic tool orchestration | Core C15/M08 ở concept level; Advanced A09 | HIGH |
| Durable HITL | Current Agent runtime có pattern serialize paused state → approve/reject → resume | Core C16–C17; M09–M10 | HIGH |
| Observability | OpenTelemetry Go traces/metrics stable; logs beta ở snapshot trước | Core C18–C20; M11 | MEDIUM |
| Agent security | Agent/tool system cần prompt-injection, tool-misuse và least-privilege controls | Core C15–C19; M08–M11 | MEDIUM/HIGH |
| Agent interoperability | A2A đáng theo dõi nhưng không phải Core dependency | Advanced A09; Reference watch | MEDIUM/HIGH |

## EXT:GO:RELEASES

- **Source:** Go project — Release History
- **URL:** https://go.dev/doc/devel/release
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** Core C0/C3–C4/C12/C18; M00–M01/M06/M11; Go Reference cookbook

Current reference: Go 1.27.0 phát hành ngày 2026-08-19.

Curriculum rule:

```text
use a currently supported stable Go release
```

Không biến `Go 1.27` thành permanent Core truth.

## EXT:MCP:SDK

- **Source:** Model Context Protocol — official SDK/spec release context
- **URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28/
- **Verified:** 2026-08-29
- **Volatility:** HIGH
- **Maps to:** Advanced A09; optional M08+ implementation; Reference tool-protocol notes

Đây là **compatibility source ID (ID nguồn tương thích)** được giữ để historical lesson/source refs tiếp tục resolve và bảo toàn provenance. Nó không khiến MCP trở thành Core prerequisite. Current operating detail được tách rõ hơn ở `EXT:MCP:2026-07-28` và `EXT:MCP:GO-SDK` bên dưới.

Không xóa/rename source ID đã được lesson tham chiếu chỉ vì freshness register được chi tiết hóa; nếu cần migration ID phải có explicit compatibility/migration plan.

## EXT:MCP:2026-07-28

- **Source:** Model Context Protocol Blog — The 2026-07-28 Specification
- **URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28/
- **Verified:** 2026-08-29
- **Volatility:** HIGH
- **Maps to:** Advanced A09; optional M08+ adapter; Reference interoperability/durable-workflow notes

Current official release facts:

- protocol core chuyển sang **stateless** request/response;
- request self-describing, optional discovery;
- `Mcp-Method` và `Mcp-Name` hỗ trợ header-based routing/authorization;
- Multi Round-Trip Requests (MRTR) thay server-initiated flow cần stream mở liên tục;
- list results có deterministic order/cache hints để cache catalog;
- authorization hardening;
- formal extensions framework;
- Tasks là một extension cho work kéo dài;
- TypeScript/Python/Go/C# SDKs được cập nhật theo release line.

Implication:

```text
MCP
≠
chỉ “LLM gọi tool”
```

Nếu M08+ chọn MCP làm adapter, implementation cần hiểu discovery, routing, auth, task/long-running interaction, tool identity và audit. Core chỉ yêu cầu explicit tool contract/permission/audit, không yêu cầu MCP. Stateless transport **không** loại bỏ durable application/workflow state.

Chi tiết repo: [`MCP-2026-OPERATING-NOTES.md`](MCP-2026-OPERATING-NOTES.md).

## EXT:MCP:GO-SDK

- **Source:** Official Model Context Protocol Go SDK
- **URL:** https://github.com/modelcontextprotocol/go-sdk
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** Advanced A09; optional C15/M08 adapter

Dùng SDK như current implementation reference; không để MCP SDK types leak vào domain Decision/Policy model.

## EXT:AGENT:TOOL-SEARCH-PROGRAMMATIC

- **Source:** OpenAI Agents SDK — Tools
- **URL:** https://openai.github.io/openai-agents-python/tools/
- **Verified:** 2026-08-29
- **Volatility:** HIGH
- **Maps to:** Core C15/M08 ở concept level; Advanced A09; Reference provider capability matrix

Current implementation reference:

- `ToolSearchTool` có thể defer large tool surfaces và load subset/namespace cần cho current turn;
- tools có thể group theo namespace;
- `ProgrammaticToolCallingTool` cho model coordinate eligible tools từ generated JavaScript;
- đây là **provider/runtime-specific capability**, không phải domain invariant.

Repo abstraction:

```text
Deferred Tool Discovery
+ Bounded Programmatic Tool Orchestration
```

có thể implement bằng provider feature hoặc deterministic Go workflow. External side-effect tools không được free-orchestrate ngoài Policy/Risk.

Xem [`TOOL-REGISTRY-STANDARD.md`](TOOL-REGISTRY-STANDARD.md) và [`PROGRAMMATIC-TOOL-ORCHESTRATION.md`](PROGRAMMATIC-TOOL-ORCHESTRATION.md).

## EXT:AGENT:DURABLE-HITL

- **Source:** OpenAI Agents SDK — Human-in-the-loop
- **URL:** https://openai.github.io/openai-agents-python/human_in_the_loop/
- **Verified:** 2026-08-29
- **Volatility:** HIGH
- **Maps to:** Core C16–C17; M09–M10; Reference provider runtime notes

Current implementation reference cho phép tool declare approval, Agent run pause khi có interruption, serialize `RunState`, approve/reject và resume. Đây phù hợp với repo durable HITL architecture nhưng **không** thay repo policy authority.

Rule:

```text
SDK approval mechanism
≠
Business Policy/Risk model
```

RISK2 vẫn phải revalidate business facts/policy sau approval và trước execution.

## EXT:TEMPORAL:GO-SDK

- **Source:** Temporal Go SDK
- **URL:** https://github.com/temporalio/sdk-go
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** Core C16–C19; M09–M11; Advanced A10

Temporal là reference cho durable, asynchronous, long-running workflow. Dạy durable concepts trước, chỉ dùng Temporal khi bài toán justify complexity.

## EXT:OTEL:GO

- **Source:** OpenTelemetry — Go language status
- **URL:** https://opentelemetry.io/docs/languages/go/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** Core C18–C20; M11; Reference observability recipe

Observability dùng OpenTelemetry concepts/semantic correlation khi phù hợp; exact package/version thuộc freshness layer.

## EXT:OWASP:AGENTIC-2026

- **Source:** OWASP GenAI Security Project — Top 10 for Agentic Applications 2026
- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** Core C15–C19; M08–M11; Reference security checklist

Agent system có thêm rủi ro goal hijacking, tool misuse, excessive privilege, supply-chain trust và unsafe execution.

Curriculum response:

- model output = untrusted input;
- tool permissions = least privilege;
- external input/tool metadata = untrusted;
- high-impact side effect qua deterministic policy/approval;
- prompt injection là system-boundary problem.

## EXT:A2A:SPEC

- **Source:** A2A Protocol specification
- **URL:** https://a2a-protocol.org/latest/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** Advanced A09; Reference technology watch

Curriculum status:

```text
MCP = MUST UNDERSTAND
A2A = SHOULD / WATCH
```

Chỉ adopt A2A khi có independent remote-agent interoperability use case thật. Multi-agent là Advanced, không phải Core default hay điều kiện hoàn thành M11.

## Những gì ổn định dù framework đổi

```text
context/cancellation
bounded concurrency
validation
provenance/freshness
retry/backoff
idempotency
durable state
explicit tool contracts
deferred tool discovery concept
least privilege
risk classification
human approval
tracing/audit
evaluation
kill switch
provider-neutral domain boundary
```

Framework/version change thường cập nhật example, adapter, test và freshness register; nó không tự ép Core/Mission đổi cấu trúc. Curriculum chỉ thay khi learner evidence hoặc operating risk cho thấy outcome/PASS boundary cần đổi.
