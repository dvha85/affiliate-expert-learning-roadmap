# Go Bot Engineering Stack

> Active implementation standard for the Go-first curriculum from v2026.09 onward.

## 1. Primary rule

```text
PRIMARY IMPLEMENTATION LANGUAGE = Go
```

C#/.NET is comparison/reference material, not the default implementation path.

## 2. Default architecture

Start with a modular monolith:

```text
Go application
├── api/
├── collectors/
├── adapters/
├── storage/
├── analytics/
├── decision/
├── policy/
├── approval/
├── executor/
├── workflows/
└── observability/
```

Split services only when independent scaling, security isolation, deployment ownership or failure containment justifies it.

## 3. Preferred stack

### Language/runtime

- use a currently supported stable Go release;
- use Go modules;
- prefer standard-library capabilities before adding frameworks.

### HTTP and external APIs

- `net/http` mental model first;
- `context.Context` for deadlines/cancellation;
- explicit retry/backoff policy;
- distinguish transient vs permanent failures;
- validate external data before it enters the core model.

### Concurrency

Use goroutines/channels/worker pools intentionally.

Teach:

- bounded concurrency;
- cancellation propagation;
- backpressure;
- race avoidance;
- worker lifecycle;
- graceful shutdown.

Do not equate “more goroutines” with better throughput when platform rate limits are the bottleneck.

### Database

Primary relational store:

```text
PostgreSQL
```

Use Redis only when a concrete requirement exists, such as caching, ephemeral coordination or rate-limit state.

### Workflow execution

Progression:

```text
function
→ job
→ scheduled worker
→ queue-backed workflow
→ durable workflow when state must survive restart/wait
```

A durable engine such as Temporal is a reference implementation, not mandatory for every bot.

### Tool boundary

Supported integration styles:

```text
REST API
Webhook
native SDK
file/export import
MCP when interoperability adds value
```

Tool contracts must define input/output schema, side effects, permissions, timeout, retry, idempotency, policy and audit behavior.

### AI layer

Use provider-neutral application interfaces where practical.

Preferred order:

```text
deterministic rule
→ deterministic algorithm
→ model call
→ tool-using agent
```

Do not use an LLM to replace deterministic business rules simply because an LLM is available.

### Observability

Baseline mental model:

```text
structured logs
+ metrics
+ traces
+ business events
+ workflow/action audit
```

OpenTelemetry is the current reference standard; current package/version details belong to the freshness layer.

### Packaging/deployment

- Docker where container deployment is useful;
- small Go binary/service footprint;
- environment/config validation at startup;
- graceful shutdown;
- health/readiness checks;
- database migrations as controlled deployment steps.

## 4. Reference freshness snapshot

Verified 2026-08-28:

- Go 1.27.0 released 2026-08-19;
- official MCP Go SDK is Tier 1 and supports MCP 2026-07-28;
- Temporal Go SDK is a reference for durable long-running workflows;
- OpenTelemetry Go: traces/metrics stable, logs beta.

Do not turn these exact versions into permanent lesson invariants.

## 5. Default development progression

```text
manual workflow
→ Go function
→ tested package
→ API/worker
→ reliable pipeline
→ durable workflow
→ AI-assisted workflow
→ tool-using agent
→ governed autonomous system
```

## 6. Anti-patterns

Avoid:

- microservices before operational need;
- unlimited goroutines;
- retry without idempotency;
- in-memory state for long approval waits;
- vendor SDK types leaking through the whole domain model;
- LLM direct access to high-impact side effects;
- tool calls without validation/audit;
- adding Redis/queues/workflow engines without a concrete problem;
- optimizing CPU before measuring external I/O and rate-limit bottlenecks.
