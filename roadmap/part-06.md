# Phần 6 — PRODUCTION CLOSED LOOP

- Timeline: **Evidence-gated; includes a production observation window**.
- **Chapters:** C18–C20
- **Core:** 9 micro-lessons
- **Mission:** M11
- **Outcome:** Bot chạy qua một observation window thật, có recovery/security controls và tạo reviewed improvement từ outcome.

## Attempt trước knowledge pull

Deploy capability nhỏ nhất an toàn, chạy qua declared observation window, chủ động tạo một failure/restart case và thực hiện kill-switch drill. Không đợi “production hoàn hảo” mới quan sát operational evidence.

## Core checklist

### Chương 18 — Deploy và operate

- [ ] **18.1** — Configuration, packaging, migration và environment boundary
- [ ] **18.2** — Health check, structured logs, metrics và operational alerts
- [ ] **18.3** — Backup/restore, recovery verification, cost và SLO

### Chương 19 — Security và incident containment

- [ ] **19.1** — Secrets, authentication, authorization và data boundary
- [ ] **19.2** — Prompt injection/tool misuse test và least-privilege containment
- [ ] **19.3** — Incident drill, kill switch, replay và recovery evidence

### Chương 20 — Closed-loop learning

- [ ] **20.1** — Weekly business/decision review từ real outcomes
- [ ] **20.2** — Calibration, drift và reviewed proposed improvement
- [ ] **20.3** — End-to-end trace, capstone demo, retrospective và next cycle

## Part PASS

- [ ] M11 có Capability PASS, Reality verified cấp E6 và Operated
- [ ] Bot chạy qua declared observation window với operational evidence
- [ ] Recovery và kill-switch drill có artifact
- [ ] Trace nối được trigger → evidence → decision → action → outcome → evaluation
- [ ] Outcome learning tạo proposed change qua test/review, không tự sửa production behavior

[← Part trước](part-05.md) · [Roadmap tổng](../ROADMAP.md)
