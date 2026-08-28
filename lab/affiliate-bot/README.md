# Affiliate Bot Lab

This is the executable learning workspace for Build-First missions M00–M03.

## Run

```bash
cd lab/affiliate-bot
go run ./cmd/bot
```

Optional custom input:

```bash
go run ./cmd/bot path/to/products.json
```

## Test

```bash
go test ./...
```

## Current scope

- validated JSON product ingest;
- product domain validation;
- storage boundary + in-memory snapshot history for fast tests;
- PostgreSQL schema/migration path in `migrations/001_init.sql`;
- commission-only ranking;
- Expected-Value ranking;
- deterministic tie-breaking.

No external API, credentials, AI, publishing or money-moving side effects exist in the bootstrap version.

## Why PostgreSQL is not required for fast CI yet

M02 teaches the persistence boundary and ships the PostgreSQL migration contract, while unit tests use the in-memory Repository implementation. Wiring a PostgreSQL driver/integration environment is an on-demand next step; it should not block M00/M01 or make every curriculum-doc PR depend on a database service.

## Expected sample behavior

The supplied dataset intentionally demonstrates that the product with the highest commission rate is not necessarily the product with the highest simple Expected Value:

```text
commission-only top: A
expected-value top: B
```

This is the Build → Observe → Pull Knowledge → Improve teaching loop used by M03.