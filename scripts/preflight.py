#!/usr/bin/env python3
"""Beginner-friendly local preflight; it never needs an account, secret or Go."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Check:
    code: str
    ok: bool
    message: str
    remediation: str


def checks(root: Path) -> list[Check]:
    return [
        Check("PREFLIGHT001", root.exists() and (root / "README.md").exists(), "Repository root is available.", "Open the cloned repository folder."),
        Check("PREFLIGHT002", sys.version_info >= (3, 9), f"Python {sys.version.split()[0]} is available.", "Install Python 3.9 or newer, then re-run this command."),
        Check("PREFLIGHT003", shutil.which("git") is not None, "Git is available.", "Install Git from https://git-scm.com/downloads and reopen the terminal."),
        Check("PREFLIGHT004", (root / "orientation/o00/run_o00.py").exists(), "O00 safe orientation is present.", "Update/re-clone the repository, then run this command again."),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the minimum safe setup for Curriculum v2")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = checks(args.root.resolve())
    if args.json:
        print(json.dumps([asdict(item) for item in result], ensure_ascii=False, indent=2))
    else:
        for item in result:
            marker = "PASS" if item.ok else "BLOCKED"
            print(f"{marker} {item.code}: {item.message}")
            if not item.ok:
                print(f"  Next step: {item.remediation}")
        print("\nNext safe action: python orientation/o00/run_o00.py --validate")
    return 0 if all(item.ok for item in result) else 1


if __name__ == "__main__":
    raise SystemExit(main())
