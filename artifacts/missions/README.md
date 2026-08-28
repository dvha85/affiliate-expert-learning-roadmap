# Mission Evidence

Mission evidence should prove what was built, run, observed, tested and learned without duplicating the whole codebase.

Recommended structure:

```text
artifacts/missions/MXX/
├── README.md
├── test-output.md
├── result-before.md
├── result-after.md
└── decision-notes.md
```

Actual source code remains under the bot workspace. Artifact files should reference code paths and commit SHAs where useful.

Do not commit secrets, credentials or unnecessary personal/raw production data.

Mission evidence may be reused by canonical lessons/projects when it proves the same requirement. Reuse does not automatically mark either Mission, Lesson or Project PASS.