# Tiến độ người học

> File này theo dõi learner evidence. Authoring status của curriculum không tự thay đổi checkbox bên dưới.

## Trạng thái hiện tại

~~~text
Current Mission: M00
Learner Bot: pre-v0.1 scaffold
Capability PASS: chưa
Reality verified: chưa
Operated: chưa
Actual time: 0 giờ
~~~

Người học chưa bắt đầu. Bước tiếp theo là [chạy starter Bot trong Mission M00](missions/M00-first-evidence-backed-decision.md), rồi mới tạo observation công khai đầu tiên.

## Mission spine

| Mission | Ship target | AI/authority | Capability | Reality | Operated |
|---|---|---|---|---|---|
| M00 | First evidence-backed decision | A0 | ⬜ | ⬜ E1 | ⬜ |
| M01 | Trustworthy history | A0 | ⬜ | ⬜ E1 | ⬜ |
| M02 | Grounded AI advisor | A1 advisory | ⬜ | ⬜ E1 | ⬜ |
| M03 | First tracked manual publish | A1; human executes | ⬜ | ⬜ E2 | ⬜ |
| M04 | Real outcome analytics | A1 | ⬜ | ⬜ E3 | ⬜ |
| M05 | First real improvement loop | A1 | ⬜ | ⬜ E4 | ⬜ |
| M06 | Reliable automatic watcher | A0 + A1 triage | ⬜ | ⬜ E4 | ⬜ |
| M07 | Decision + abstention + memory | A1 | ⬜ | ⬜ E4 | ⬜ |
| M08 | Read-only tool agent | A2-RO | ⬜ | ⬜ E4 | ⬜ |
| M09 | Shadow action + durable approval | A3-shadow | ⬜ | ⬜ E4 | ⬜ |
| M10 | Limited governed automation | A3-limited | ⬜ | ⬜ E5 | ⬜ |
| M11 | Production closed loop | A3; A4 optional advanced | ⬜ | ⬜ E6 | ⬜ |

## Real Evidence Ladder

| Level | Bằng chứng |
|---|---|
| E0 | test/synthetic/replay, chỉ chứng minh plumbing/kỹ thuật |
| E1 | public observation có source, observed_at và access method |
| E2 | public artifact do learner review và thực hiện |
| E3 | analytics/export thật, kể cả observed value bằng 0 |
| E4 | Decision → Action → Outcome → Evaluation nối được |
| E5 | bounded governed canary có policy, audit và kill-switch evidence |
| E6 | closed-loop production evidence qua observation window, recovery và reviewed improvement |

Sample không thể nâng Reality level.

## Maturity milestones, không phải PASS gate

~~~text
REAL_EXPOSURE_OBSERVED:      ⬜
REAL_CLICK_OBSERVED:         ⬜
REAL_ORDER_OBSERVED:         ⬜
REAL_VALID_ORDER_OBSERVED:   ⬜
REAL_COMMISSION_PAID:        ⬜
~~~

Không bắt buộc learner tạo ra sale để PASS. Nếu platform thật báo 0, lưu 0; nếu chưa có dữ liệu, lưu missing/pending, không đổi thành 0.

## Actual-time calibration

Với M00–M05, ghi:

| Field | Giá trị |
|---|---:|
| planned_hours | — |
| actual_build_hours | 0 |
| actual_debug_hours | 0 |
| actual_operate_hours | 0 |
| actual_knowledge_hours | 0 |
| actual_retry_hours | 0 |
| waiting_for_outcome_hours | tách riêng, không tính focused time |

Chỉ reforecast chương trình sau learner pilot; không điều chỉnh PASS criteria để khớp lịch.
