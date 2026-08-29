# Effort model — Outcome-Driven Core

Lesson count không phải workload model. Core hiện có 63 micro-lesson nhưng phần lớn thời gian phải nằm ở build, debug, business observation, outcome window, review và retry.

## Planning envelope ban đầu

~~~text
Focused learner time: khoảng 240–360 giờ
Outcome waiting time: ghi riêng, không tính như focused work
Confidence: thấp cho tới khi có learner pilot M00–M05
~~~

| Gate | Missions | Forecast focused hours |
|---|---|---:|
| G1 — First Evidence-Backed Decision | M00 | 12–24 |
| G2 — Trustworthy Data & Grounded AI | M01–M02 | 35–60 |
| G3 — First Market Learning Loop | M03–M05 | 55–90 |
| G4 — Governed Production Loop | M06–M11 | 120–186 |
| **Tổng** | | **222–360** |

Dùng 240–360 giờ làm planning envelope để có khoảng review/integration tối thiểu. Đây là forecast, không phải promise.

## Draft Mission nominal estimates

Mission files đang author/draft có nominal estimate hẹp hơn Gate envelope và hữu ích để lập kế hoạch gần hạn:

| Mission | Nominal focused effort | Ghi chú |
|---|---:|---|
| M00 | ~10h | ready/pilot target |
| M01 | ~12h | draft |
| M02 | ~12h | draft |
| M03 | ~14h | draft |
| **M00→M03** | **~48h** | first tracked human market action nếu không có external blocker |

Các nominal estimate này **không override Gate envelope** và chưa đủ evidence để coi là duration chuẩn. Chúng chỉ ngăn calendar profile vô tình kéo bốn Mission đầu dài hơn nhiều so với chính Mission design.

Planning implication:

```text
focused hours decide near-term pace
external waiting decides calendar delay
calendar month does not decide PASS
```

Sau pilot, actuals thắng nominal estimate.

## Micro-lesson

- S: 20–30 phút knowledge pull + apply nhỏ;
- M: 30–45 phút;
- L: 45–75 phút, chỉ khi không thể chia mà vẫn giữ decision context.

Thời gian lesson phải gồm TRY/OBSERVE/APPLY/TEST, không chỉ thời gian đọc.

## Mission actuals

Ghi riêng:

- build;
- debug;
- operate;
- knowledge pull;
- review/retry;
- business observation/action;
- waiting for external outcome.

Không double-count. Waiting time có thể kéo calendar nhưng không được biến thành “giờ học”.

## First reality-feedback target

M03 là first tracked human market action. Curriculum nên đưa learner tới đó ngay khi M00–M02 prerequisites/evidence đủ; không trì hoãn chỉ để khớp 12/15-month calendar.

Ở nominal ~48 focused hours:

- 4 h/tuần → khoảng 12 tuần focused work;
- 5 h/tuần → khoảng 10 tuần;
- 6 h/tuần → khoảng 8 tuần;
- 8 h/tuần → khoảng 6 tuần.

Đây là arithmetic planning aid, không phải promise. External blockers/outcome waiting được cộng vào calendar riêng.

## Quy tắc reforecast

Sau M00–M05:

1. lấy median actual/planned theo learner;
2. tách setup, coding, business work, debug và review;
3. xác định blocker ngoài tầm kiểm soát;
4. chỉ áp hệ số cho Mission tương tự;
5. giữ nguyên evidence/safety gate và kéo dài timeline nếu cần.

Nên reforecast sớm sau M00 và M03 để phát hiện absolute-beginner overhead và real-market friction trước khi dự báo phần còn lại.

Không dùng một learner để tuyên bố duration phổ quát. Dữ liệu một người chỉ là preliminary calibration.
