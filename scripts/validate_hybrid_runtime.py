#!/usr/bin/env python3
"""Compatibility entrypoint for the current runtime-architecture validator.

The canonical architecture guard moved to validate_runtime_architecture.py when
ADR-004 superseded Go-as-language-authority assumptions from ADR-003. Keep this
entrypoint so existing CI commands and tests remain stable.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from scripts.validate_runtime_architecture import *  # noqa: F401,F403
except ModuleNotFoundError:
    from validate_runtime_architecture import *  # type: ignore # noqa: F401,F403


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    problems = validate(root)
    if problems:
        for problem in problems:
            print(problem)
        print(f"Hybrid runtime validation failed with {len(problems)} problem(s).")
        return 1
    print(
        "Hybrid runtime validation passed: deterministic authority, implementation flexibility, "
        "visual-first AgentRuntime and negative authority guards are consistent."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
