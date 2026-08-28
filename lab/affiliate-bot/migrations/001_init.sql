CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS product_snapshots (
    id BIGSERIAL PRIMARY KEY,
    product_id TEXT NOT NULL REFERENCES products(id),
    price NUMERIC(18,2) NOT NULL CHECK (price >= 0),
    commission_rate NUMERIC(8,6) NOT NULL CHECK (commission_rate >= 0 AND commission_rate <= 1),
    conversion_potential NUMERIC(8,6) NOT NULL CHECK (conversion_potential >= 0 AND conversion_potential <= 1),
    captured_at TIMESTAMPTZ NOT NULL,
    UNIQUE (product_id, captured_at)
);

CREATE INDEX IF NOT EXISTS idx_product_snapshots_product_time
ON product_snapshots(product_id, captured_at DESC);
