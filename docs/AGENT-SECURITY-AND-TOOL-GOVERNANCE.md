# Agent Security and Tool Governance

> Security standard for tool-using Affiliate Bots and AI agents.

> **Beginner reader guide / Hướng dẫn cho người mới:** tài liệu này giữ English terminology làm chuẩn kỹ thuật. Tra [`GLOSSARY-VI.md`](GLOSSARY-VI.md) khi cần. Các từ trọng tâm: **Untrusted Input (Đầu vào không được tin cậy mặc định)**, **Threat Model (Mô hình đe dọa)**, **Prompt Injection (Tấn công/chỉ dẫn tiêm vào prompt)**, **Trust Boundary (Ranh giới tin cậy)**, **Tool Governance (Quản trị công cụ)**, **Side Effect (Tác động bên ngoài)**, **Least Privilege (Quyền tối thiểu cần thiết)**, **Allowlist (Danh sách cho phép)**, **Credential Scope (Phạm vi quyền credential)**, **Sandbox (Môi trường cô lập)**, **Audit Trace (Dấu vết kiểm tra)**, **Kill Switch (Công tắc dừng khẩn cấp)**.

## 1. Core principle

```text
MODEL OUTPUT IS UNTRUSTED INPUT
```

Diễn giải cho người mới:

```text
Đầu ra mô hình
≠
Quyền thực thi
```

An LLM may recommend an action, but production authorization must come from explicit system policy and permissions.

## 2. Threat model

Affiliate agents may read untrusted content from:

- product descriptions;
- seller pages;
- websites;
- reviews/comments;
- emails/messages;
- uploaded files;
- API responses;
- RAG documents;
- MCP resources/tools.

That content may contain malicious or misleading instructions intended to change agent behavior.

Treat prompt injection similarly to hostile input crossing a trust boundary.

## 3. Tool categories

Every tool should declare:

```text
name
purpose
input schema
output schema
read/write
side-effect level
required permission
risk ceiling
timeout/retry behavior
idempotency behavior
approval requirement
audit fields
```

Recommended categories:

### READ_ONLY

Examples:

- fetch product metadata;
- read analytics;
- inspect current policy snapshot.

### INTERNAL_WRITE

Examples:

- update internal ranking;
- save draft;
- write experiment result.

### EXTERNAL_SIDE_EFFECT

Examples:

- publish;
- send message;
- alter account configuration;
- spend money.

External side-effect tools should default to stricter policy and approval.

## 4. Least privilege

Do not give one agent a universal credential when separate capabilities can be scoped.

Prefer:

```text
collector credential → read scope
publisher credential → publish scope
billing credential → isolated high-risk scope
```

Tool access should be granted per workflow/role, not merely because a tool exists in the registry.

## 5. Prompt injection boundary

Never treat retrieved content as system-level instructions.

Preferred architecture:

```text
UNTRUSTED CONTENT
→ parser/normalizer
→ data model
→ model reasoning context
→ proposed ActionIntent
→ policy engine
→ permission check
→ approval if required
→ tool execution
```

Important defenses:

- separate instructions from data;
- minimize unnecessary context;
- restrict tool set per task;
- validate tool arguments;
- deny unknown fields/targets when practical;
- use allowlists for sensitive destinations;
- prevent retrieved text from changing authorization policy;
- require deterministic approval for consequential side effects.

## 6. Tool misuse controls

Before a side-effecting tool call, verify:

1. Is this tool allowed for this workflow?
2. Is the requested target allowed?
3. Are arguments schema-valid?
4. Is the action within risk/policy limits?
5. Is approval required and still valid?
6. Has the action already been executed?
7. Is the current context fresh enough?

## 7. MCP governance

MCP improves interoperability but does not make every tool trustworthy.

For MCP servers/clients:

- verify server origin/configuration;
- limit exposed tools/resources;
- treat remote descriptions/results as untrusted data;
- scope credentials;
- apply the same risk/approval policy as native tools;
- record server/tool identity and protocol/runtime metadata in audit traces when relevant;
- review protocol/security changes through the freshness process.

## 8. Generated code / command execution

Do not allow an agent to execute arbitrary generated shell/code in a privileged production environment.

If code execution is required:

- isolate/sandbox it;
- limit filesystem/network/credential access;
- use time/resource limits;
- separate read-only analysis from production writes;
- require approval for consequential outputs.

## 9. Secrets

Never place long-lived secrets in prompts, logs or RAG documents.

Use:

- secret manager/environment injection;
- short-lived tokens where possible;
- scoped credentials;
- rotation/revocation;
- redaction in logs/traces.

## 10. Audit requirements

For significant actions, store:

```text
workflow_id
action_intent_id
model/provider/version when relevant
prompt/template version when relevant
tool identity
validated arguments or safe hash/reference
policy version
risk level
approval decision
execution result
external correlation id
trace id
timestamps
```

Do not store sensitive raw data merely for convenience.

## 11. Kill switch and containment

The system must support disabling:

- all external actions;
- one action category;
- one platform/tool;
- one agent/workflow.

Collection and analysis may remain active while execution is disabled.

## 12. Evaluation and red-team cases

Test at minimum:

- malicious product text asking the agent to ignore rules;
- tool argument injection;
- fake approval content;
- stale approval after product/price change;
- duplicate execution after retry;
- compromised/incorrect MCP tool description;
- excessively broad credentials;
- model suggesting prohibited platform manipulation;
- hidden instruction in retrieved content.

## 13. Anti-patterns

Avoid:

- `LLM → privileged tool` with no policy boundary;
- one credential for every integration;
- trusting MCP/server metadata as authorization;
- logging secrets/full personal data;
- treating prompt injection as only a prompt-writing problem;
- assuming human approval fixes poor tool permissions;
- allowing the same agent to redefine the policy that constrains it.
