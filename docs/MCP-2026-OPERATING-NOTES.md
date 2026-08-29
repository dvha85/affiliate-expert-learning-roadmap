# MCP 2026 Operating Notes — Ghi chú vận hành hiện hành

> **Verified:** 2026-08-29  
> **Volatility:** MEDIUM/HIGH  
> Đây là freshness/implementation note, không phải permanent canonical truth.

## 1. Nguồn chính

- Model Context Protocol Blog — The 2026-07-28 Specification  
  https://blog.modelcontextprotocol.io/posts/2026-07-28/

## 2. Các thay đổi quan trọng của protocol line 2026-07-28

Official release mô tả:

- stateless protocol core;
- request tự mô tả, discovery có thể optional;
- `Mcp-Method` / `Mcp-Name` header-based routing;
- Multi Round-Trip Requests (MRTR) cho server-to-client interaction mà không cần stream mở liên tục;
- list results deterministic + cache hints để cache tool/resource catalog;
- authorization hardening;
- formal extensions framework;
- Tasks là một extension cho work kéo dài;
- TypeScript/Python/Go/C# SDKs được cập nhật theo release line.

## 3. Curriculum/runtime implication

MCP không chỉ là “Agent gọi tool”. Khi dùng production cần hiểu:

```text
Discovery
+ Routing
+ Authorization
+ Tool/Resource Contract
+ Long-running Interaction / Tasks
+ Audit / Identity
```

Stateless protocol core không có nghĩa application/workflow state biến mất. Durable business state vẫn phải nằm trong application/workflow store rõ ràng.

## 4. Cacheable tool catalog

Tool discovery có thể cache khi protocol/runtime cho phép, nhưng permission/risk filtering vẫn phải re-evaluate theo workflow/user/action context.

```text
cached catalog
≠
cached authorization forever
```

## 5. MRTR / Tasks

Long interaction hoặc input-required flow không được dùng để bypass Human Approval. Nếu business action là RISK2, approval state vẫn theo repo Policy/Risk/HITL contract.

## 6. Security

Header routing/authorization improvement không làm remote MCP server trustworthy mặc định.

MCP metadata/result/tool description vẫn là untrusted external input; enforce:

- server identity/config review;
- least-privilege credentials;
- tool allowlist/risk ceiling;
- schema validation;
- policy/approval;
- audit.

## 7. Adoption

Use MCP when interoperability/standardized discovery adds measurable value. REST/webhook/native API vẫn ưu tiên nếu đơn giản hơn.

## 8. Reverification

Re-verify trước khi author/ship M08 hoặc production integration, và theo freshness/reference review khi spec/SDK/security có migration mới.
