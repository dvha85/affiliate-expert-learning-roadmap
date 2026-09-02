#!/usr/bin/env python3
"""Create an ignored learner-local workspace without copying private data."""
from __future__ import annotations

import argparse
from pathlib import Path

FILES = {
    "README.md": """# Learner-local workspace\n\nThis directory is ignored by Git. Keep personal progress, raw exports, account\nreferences and private evidence here. Commit only reviewed/redacted summaries.\n\nRun O00 from the repository root:\n\n```bash\npython orientation/o00/run_o00.py --validate\n```\n""",
    "PROGRESS.md": """# Learner progress — local only\n\n- Curriculum version: 2\n- Current Mission: O00\n- Lesson credit retained from v1 (if any):\n- Capability: pending\n- Reality: NOT_REQUIRED for O00\n- Operated: pending\n- Blocker / next action:\n\nDo not put secrets, credentials, customer data or raw analytics in Git.\n""",
    "artifacts/local/.gitkeep": "",
}


def initialize(root: Path) -> list[Path]:
    created: list[Path] = []
    for relative, content in FILES.items():
        path = root / relative
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        created.append(path)
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize an ignored learner workspace")
    parser.add_argument("--path", type=Path, default=Path("workspace"))
    parser.add_argument("--init", action="store_true", help="perform the explicit local write")
    args = parser.parse_args()
    if not args.init:
        print(f"DRY RUN: would initialize {args.path}. Re-run with --init to create local files.")
        return 0
    created = initialize(args.path)
    print(f"Initialized {args.path} ({len(created)} file(s) created; existing files were left unchanged).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
