#!/usr/bin/env python3
"""Validate the O00 safety invariant through the shared contract registry."""
from __future__ import annotations

import argparse
from pathlib import Path

try:
    from scripts.validate_contract_registry import validate as validate_registry
except ModuleNotFoundError:
    from validate_contract_registry import validate as validate_registry


def validate(path: Path) -> list[str]:
    root = Path(__file__).resolve().parents[1]
    if path.resolve() == root / "contracts/examples/o00-trace.json":
        return validate_registry(root)
    return ["O00 validator only accepts the canonical contract trace; use validate_contract_registry for a copied fixture."]


def main() -> int:
    parser = argparse.ArgumentParser(description="Kiểm O00 synthetic walkthrough")
    parser.add_argument("--fixture", type=Path, default=Path(__file__).resolve().parents[1] / "contracts/examples/o00-trace.json")
    args = parser.parse_args()
    errors = validate(args.fixture)
    if errors:
        print("O00: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("O00: PASS — synthetic full trace is non-actionable and idempotent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
