# M04 hint ladder

1. Freeze deterministic baseline and evidence refs before reading an advisory.
2. Validate schema/execution kind, then ref existence, then field/value support.
3. Treat unsupported claim, prompt injection, timeout and malformed output as
   rejected/unavailable with deterministic fallback.
4. Record replay/live truth and keep `live_provider_verified: pending` until a
   permitted live integration is actually verified.
