#!/usr/bin/env python3
"""Print the O00 synthetic decision; it never performs an external action."""
from __future__ import annotations

import json
from pathlib import Path


def load() -> dict[str, object]:
    return json.loads(Path(__file__).with_name("o00-synthetic-decision.json").read_text(encoding="utf-8"))


def main() -> int:
    print(json.dumps(load(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
