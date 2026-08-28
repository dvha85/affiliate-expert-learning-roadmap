# Bot Engineering Refresh — 2026.08

> Current-knowledge register for the Go-first Bot Engineer track. This file supplements, but does not replace, the active canonical `sources/SYLLABUS-v2026.09.md`.

**Verified:** 2026-08-28  
**Scope:** Go runtime, MCP, durable workflows, observability, agent security and agent interoperability.  
**Policy:** see [`FRESHNESS-POLICY.md`](FRESHNESS-POLICY.md).

## Executive update map

| Area | Current operating update | Curriculum mapping | Volatility |
|---|---|---|---|
| Go runtime | Go 1.27.0 released 2026-08-19 | P15/C51; P19/C77; P22/C87 | MEDIUM |
| MCP | Go SDK is Tier 1; protocol line includes 2026-07-28 | P15/C51–52; P17/C61; P21; P22/C87 | MEDIUM/HIGH |
| Durable workflows | Temporal Go SDK is a strong current reference for long-running durable execution | P15/C53; P17/C66; P19/C74 | MEDIUM |
| Observability | OpenTelemetry Go traces/metrics stable; logs beta | P15/C51; P19/C73 | MEDIUM |
| Agent security | Agent/tool systems require prompt-injection, tool-misuse and least-privilege controls beyond classic API security | P17/C65–66; P19/C75–76 | MEDIUM/HIGH |
| Agent interoperability | A2A is relevant to watch, but not a Phase-1 requirement | P22/C87 | MEDIUM |

## EXT:GO:RELEASES

- **Source:** Go project — Release History
- **URL:** https://go.dev/doc/devel/release
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** 51.1–51.2, 77.x, 87.1

Current reference fact:

- Go 1.27.0 was released on 2026-08-19.

Curriculum rule:

```text
use a currently supported stable Go release
```

Do not turn `Go 1.27` into a permanent canonical lesson title.

## EXT:MCP:SDK

- **Source:** Model Context Protocol — official SDK tier documentation
- **URL:** https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/docs/2026-07-28/sdk.mdx
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 51.x, 52.2, 61.6, 83.4, 87.2

Current reference facts:

- Go is classified as a Tier-1 official MCP SDK language.
- The current SDK documentation covers the `2026-07-28` MCP protocol line.

Curriculum implication:

MCP is now mature enough to be a required interoperability concept for Bot Engineer, but it is still not mandatory for every integration. REST/webhooks/native APIs remain valid when simpler.

## EXT:MCP:GO-SDK

- **Source:** Official Model Context Protocol Go SDK
- **URL:** https://github.com/modelcontextprotocol/go-sdk
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 51.x, 61.6, 83.4

Use this as a current implementation reference, not a reason to couple domain logic directly to MCP SDK types.

## EXT:TEMPORAL:GO-SDK

- **Source:** Temporal Go SDK
- **URL:** https://github.com/temporalio/sdk-go
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM
- **Maps to:** 53.1–53.7, 66.4, 74.x

Current reference implication:

Temporal is a mature example of durable, asynchronous, long-running workflows where state and retries survive process restarts.

Curriculum rule:

```text
teach durable-execution concepts first
→ use Temporal as a reference implementation when the problem justifies it
```

Do not require Temporal for simple cron/job workers.

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

Observability should use OpenTelemetry concepts and semantic correlation where practical, while exact package/version decisions remain freshness-scoped.

## EXT:OWASP:AGENTIC-2026

- **Source:** OWASP GenAI Security Project — Top 10 for Agentic Applications 2026
- **URL:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 65.4, 75.x, 76.x

Security implication:

Agent systems introduce risks such as goal hijacking, tool misuse, excessive privilege, supply-chain trust and unsafe code/action execution. These cannot be solved only by authentication/API-key lessons.

Curriculum response:

- model output is untrusted input;
- tool permissions are least-privilege;
- high-impact side effects require deterministic policy and/or approval;
- prompt injection must be treated as a system-boundary problem, not only a prompt-writing problem.

## EXT:A2A:SPEC

- **Source:** A2A Protocol specification
- **URL:** https://a2a-protocol.org/latest/
- **Verified:** 2026-08-28
- **Volatility:** MEDIUM/HIGH
- **Maps to:** 87.2

Curriculum status:

```text
MCP = MUST UNDERSTAND
A2A = SHOULD / WATCH
```

The curriculum should adopt A2A only when a real remote-agent interoperability use case appears.

## What remains stable despite framework changes

The core Bot Engineer concepts should remain valid even if current libraries change:

```text
context/cancellation
bounded concurrency
validation
provenance
retry/backoff
idempotency
durable state
explicit tool contracts
least privilege
risk classification
human approval
tracing/audit
evaluation
kill switch
```

Framework/version changes should normally update examples and the freshness register, not force a new curriculum structure.
