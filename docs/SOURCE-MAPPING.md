# Source-to-Roadmap Traceability Map

> Mục tiêu: mọi Part/Chapter/Lesson trong roadmap đều truy ngược được về nguồn, đồng thời phân biệt rõ **cấu trúc chuẩn**, **pacing/practice**, và **research supplement**.

## 1. Source precedence

Repo dùng ba nguồn do chủ repo cung cấp:

1. **`S` — `sources/SYLLABUS-v2026.08.md`**  
   Nguồn chuẩn cho cấu trúc curriculum: Part, Chapter, Lesson ID/title, Project, LAB, PASS Gate và mục tiêu chương trình.
2. **`T` — `sources/Noi-dung-dao-tao.txt`**  
   Nguồn bổ sung cho lộ trình 50 tuần, cách học, practice, project evolution và pacing ban đầu.
3. **`R` — `sources/Nghien-cuu.txt`**  
   Nguồn bổ sung cho rationale, ví dụ Affiliate Bot, Product Intelligence, feedback loop, architecture và định hướng triển khai.

Quy tắc:

```text
STRUCTURE: S > T > R
PACING CURRENT: 15/12-month plans > T
EXECUTION ORDER CURRENT: EXECUTION-MODEL > linear source schedule
EXAMPLES / RATIONALE: T + R supplement S
```

Không dùng `T` hoặc `R` để tự ý đổi Lesson ID/title/scope của syllabus.

## 2. Conflict rules

Khi nguồn khác nhau:

- **Part/Chapter/Lesson/Project/LAB/PASS Gate:** `S` thắng.
- **Timeline:** dùng [15-MONTH-PLAN](15-MONTH-PLAN.md) hoặc [12-MONTH-PLAN](12-MONTH-PLAN.md); số tuần trong `T` chỉ còn là provenance/context.
- **Tuần tự vs song song:** dùng [EXECUTION-MODEL](EXECUTION-MODEL.md).
- **Ví dụ/practice/architecture:** có thể lấy từ `T`/`R` nếu phù hợp scope của lesson, nhưng phải giữ nhãn supplemental.
- **Không có counterpart trực tiếp:** ghi `—`; không gán nguồn bằng suy đoán.
- **Chỉ tương đồng một phần:** ghi `(partial)` hoặc mô tả context cụ thể.
- **Platform/legal/tax/current-policy facts:** mapping nguồn không đồng nghĩa dữ kiện còn hiện hành. Lesson author phải kiểm chứng nguồn ngoài tại thời điểm viết nếu lesson yêu cầu factual freshness.

## 3. Source reference IDs

### Syllabus

```text
S:P{part}/C{chapter}/L{lesson}
```

Ví dụ:

```text
S:P0/C0/L0.1
S:P8/C27/L27.4
```

Ở chapter level:

```text
S:P8/C27
```

### Training source

```text
T:G{giai_doan}/W{week}
```

Ví dụ:

```text
T:G3/W13
T:G7/W29
```

Các section không nằm trong week dùng tên section:

```text
T:§3 Affiliate Intelligence Platform
T:G12 Expert Level
```

### Research source

Research file lặp lại phần lớn lộ trình 50 tuần của training source. Bảng dưới **không lặp lại toàn bộ mirror mapping**; cột Research chỉ ghi các insight bổ sung đáng kể ngoài provenance từ `T`.

Ví dụ:

```text
R:Product Intelligence
R:Affiliate Bot architecture
R:Technology stack
R:feedback loop
R:roadmap stages
```

## 4. Lesson-level mapping rule

Tất cả **671 lesson** có mapping canonical theo chính ID trong syllabus:

```text
Roadmap lesson X.Y
↔ S:P{part chứa chapter X}/C{X}/L{X.Y}
```

Ví dụ:

```text
roadmap/part-00.md → 0.1
↔ S:P0/C0/L0.1

roadmap/part-12.md → 38.4
↔ S:P12/C38/L38.4
```

`T` và `R` không phải lúc nào cũng có mapping 1:1 tới lesson. Khi author lesson, dùng chapter mapping dưới đây làm baseline, sau đó chỉ gắn `T`/`R` nếu section thực sự hỗ trợ nội dung lesson đó.

## 5. `source_refs` contract cho lesson

Canonical lesson template ở Step 5 phải hỗ trợ tối thiểu:

```yaml
source_refs:
  canonical:
    - "S:P0/C0/L0.1"
  training:
    - "T:G0/W0"
  research:
    - "R:roadmap stages"
  external: []
```

Quy tắc:

- `canonical` bắt buộc có ít nhất một `S:` ref.
- `training`/`research` chỉ thêm khi thực sự hỗ trợ lesson.
- `external` dành cho tài liệu kiểm chứng mới hơn, đặc biệt policy/legal/tax/platform facts.
- Không dùng source ref để thay thế citation/evidence khi lesson có claim cần kiểm chứng.

## 6. Chapter traceability — 23 Part / 89 Chapter

Track key:

- **A** — Affiliate Business & Marketing
- **B** — Data & Intelligence
- **C** — Engineering & AI
- **D** — Compliance & Operations

`Standard month` theo [15-MONTH-PLAN](15-MONTH-PLAN.md). Part 20 là conditional; Part 22 là post-core continuous mastery.

### Part 0 — ORIENTATION & AFFILIATE LAB
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 0 — Khởi động chương trình | `S:P0/C0` | T:G0/W0 | R:Roadmap stages | M1 | A/B/C/D |

### Part 1 — AFFILIATE FUNDAMENTALS
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 1 — Affiliate Marketing Foundation | `S:P1/C1` | T:G1/W1 | — | M1 | A |
| 2 — Affiliate Business Models | `S:P1/C2` | T:G1/W4 | — | M1 | A |
| 3 — Affiliate vs các mô hình kinh doanh khác | `S:P1/C3` | T:G1/W4 (partial) | — | M1 | A |

### Part 2 — AFFILIATE ECONOMICS
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 4 — Core Metrics | `S:P2/C4` | T:G1/W2 | — | M1–2 | A/B |
| 5 — Affiliate Unit Economics | `S:P2/C5` | T:G1/W2 + G2/W6 + G3/W12 | R:Money model example | M1–2 | A/B |
| 6 — Revenue Modeling | `S:P2/C6` | T:G1/W2 + G10/W46 (partial) | R:Money model + feedback loop | M1–2 | A/B |

### Part 3 — TRACKING & ATTRIBUTION
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 7 — Affiliate Tracking | `S:P3/C7` | T:G1/W3 + G2/W7 | — | M2 | B |
| 8 — Attribution | `S:P3/C8` | T:G1/W3 + G2/W7 | — | M2 | B |
| 9 — Advanced Measurement Architecture | `S:P3/C9` | — (syllabus expansion) | R:Affiliate Bot architecture (measurement context) | M2 | B |

### Part 4 — VIETNAM LEGAL, TAX & COMPLIANCE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 10 — Pháp lý Affiliate tại Việt Nam | `S:P4/C10` | — | — | M3 | D |
| 11 — Thuế & tài chính Affiliate | `S:P4/C11` | — | — | M3 | D |
| 12 — Content, Privacy & Intellectual Property | `S:P4/C12` | T:G2/W8 (partial) | R:anti-spam / human review | M3 | D |

### Part 5 — AFFILIATE PLATFORM EXPERT
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 13 — TikTok Shop Affiliate | `S:P5/C13` | T:G2/W5–6 | R:TikTok/Shopee ecosystem example | M3–4 | A/D |
| 14 — TikTok Creator Quality & Risk | `S:P5/C14` | T:G2/W8 | R:anti-spam / policy risk | M3–4 | A/D |
| 15 — Shopee Affiliate | `S:P5/C15` | T:G2/W7 | R:TikTok/Shopee ecosystem example | M3–4 | A/D |
| 16 — Platform Change Management | `S:P5/C16` | T:G2/W8 (risk context) | R:anti-spam / policy risk | M3–4 | A/D |

### Part 6 — MARKET & NICHE INTELLIGENCE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 17 — Niche Selection | `S:P6/C17` | T:G1/W4 Project #1 (partial) | R:first niche example | M4 | A/B |
| 18 — Market Demand | `S:P6/C18` | T:G3/W9–10 | R:Product Intelligence | M4 | A/B |
| 19 — Competitive Intelligence | `S:P6/C19` | T:G3/W11 | R:Product Intelligence | M4 | A/B |

### Part 7 — CUSTOMER INTELLIGENCE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 20 — Customer Understanding | `S:P7/C20` | T:G4/W14 | R:Content/AI audience example | M5 | A |
| 21 — Customer Journey | `S:P7/C21` | T:G4/W14 + G5/W21 (partial) | R:feedback loop (partial) | M5 | A |
| 22 — Purchase Intent | `S:P7/C22` | T:G4/W18 + W14 | R:commercial content examples | M5 | A |

### Part 8 — PRODUCT INTELLIGENCE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 23 — Product Research | `S:P8/C23` | T:G3/W9 | R:Product Intelligence | M5–6 | A/B |
| 24 — Product Economics | `S:P8/C24` | T:G3/W12 + G2/W6 | R:Product Intelligence + money model | M5–6 | A/B |
| 25 — Product Trend | `S:P8/C25` | T:G3/W10 + G10/W44 | R:Product Intelligence | M5–6 | A/B |
| 26 — Product Competition | `S:P8/C26` | T:G3/W11 | R:Product Intelligence | M5–6 | A/B |
| 27 — Opportunity Score | `S:P8/C27` | T:G3/W13 | R:Opportunity Score example | M5–6 | A/B |

### Part 9 — CONTENT & CONSUMER PSYCHOLOGY
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 28 — Consumer Psychology | `S:P9/C28` | T:G4/W14 | R:Content Bot context | M6–7 | A |
| 29 — Hook Engineering | `S:P9/C29` | T:G4/W15 | R:AI content example | M6–7 | A |
| 30 — Affiliate Content Formats | `S:P9/C30` | T:G4/W16–18 | R:AI content example | M6–7 | A |
| 31 — Content Architecture | `S:P9/C31` | T:G4/W16–18 (partial) | R:AI content example | M6–7 | A |
| 32 — Content System | `S:P9/C32` | T:G4/W19 | R:Content Bot / manual publish | M6–7 | A |

### Part 10 — TRAFFIC & DISTRIBUTION
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 33 — Traffic Fundamentals | `S:P10/C33` | T:G5/W20 | R:feedback loop | M7 | A |
| 34 — Social Distribution | `S:P10/C34` | T:G5/W20 (social subset) | R:multi-channel content outputs | M7 | A |
| 35 — Search & Owned Media | `S:P10/C35` | T:G5/W20 (search/owned subset) | R:multi-channel content outputs | M7 | A |

### Part 11 — FUNNEL & CONVERSION
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 36 — Affiliate Funnel | `S:P11/C36` | T:G5/W21–22 | R:money flow + feedback loop | M7–8 | A/B |
| 37 — Conversion Optimization | `S:P11/C37` | T:G5/W22–23 | R:feedback loop | M7–8 | A/B |

### Part 12 — DATA ENGINEERING FOR AFFILIATE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 38 — Affiliate Data Model | `S:P12/C38` | T:G6/W24 | R:Technology stack | M8 | B/C |
| 39 — Historical Data | `S:P12/C39` | T:G6/W25 | R:Product Intelligence history | M8 | B/C |
| 40 — Data Quality | `S:P12/C40` | T:G11/W48 (partial) | R:Technology stack (partial) | M8 | B/C |
| 41 — Metrics Engine | `S:P12/C41` | T:G6/W26 | R:Analytics Bot metrics | M8 | B/C |

### Part 13 — AFFILIATE ANALYTICS
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 42 — Descriptive Analytics | `S:P13/C42` | T:G6/W27 | R:Analytics Bot metrics | M8–9 | B |
| 43 — Diagnostic Analytics | `S:P13/C43` | T:G5/W22 + G6/W27 | R:feedback loop | M8–9 | B |
| 44 — Segmentation | `S:P13/C44` | T:G6/W28 | R:feedback loop | M8–9 | B |
| 45 — Dashboard | `S:P13/C45` | T:G6/W27 | R:Analytics Bot metrics | M8–9 | B |

### Part 14 — EXPERIMENTATION & STATISTICS
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 46 — Experimental Thinking | `S:P14/C46` | T:G9/W39 | R:feedback loop experimentation context | M9 | B |
| 47 — Statistics for Affiliate | `S:P14/C47` | T:G9/W41 | — | M9 | B |
| 48 — A/B Testing | `S:P14/C48` | T:G9/W40 | — | M9 | B |
| 49 — Experiment System | `S:P14/C49` | T:G9/W42 | R:feedback loop | M9 | B |

### Part 15 — AFFILIATE BOT ENGINEERING
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 50 — Bot Architecture | `S:P15/C50` | T:G7/W29 | R:Affiliate Bot architecture + Technology stack | M9–10 | C |
| 51 — Technology Stack | `S:P15/C51` | T:G7/W29 | R:Technology stack | M9–10 | C |
| 52 — Product Collector | `S:P15/C52` | T:G7/W30 | R:Product Finder Bot + Technology stack | M9–10 | C |
| 53 — Scheduler & Pipeline | `S:P15/C53` | T:G7/W31 | R:Technology stack | M9–10 | C |
| 54 — Product Tracker | `S:P15/C54` | T:G7/W31–32 | R:Product Intelligence | M9–10 | C |
| 55 — Change Detection | `S:P15/C55` | T:G7/W32 | R:Product Intelligence | M9–10 | C |
| 56 — Alert Bot | `S:P15/C56` | T:G7/W32–33 | R:Product Intelligence alert example | M9–10 | C |

### Part 16 — DECISION & RECOMMENDATION ENGINE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 57 — Rule Engine | `S:P16/C57` | T:G7/W33 (partial) | R:Opportunity Score V1 | M11 | B/C |
| 58 — Scoring Engine | `S:P16/C58` | T:G3/W13 + G7/W33 | R:Opportunity Score V1 | M11 | B/C |
| 59 — Ranking Engine | `S:P16/C59` | T:G7/W33 + G10/W43 | R:Product Finder Bot ranking | M11 | B/C |
| 60 — Recommendation Engine | `S:P16/C60` | T:G10/W43 + G8/W38 | R:Affiliate Intelligence actions | M11 | B/C |

### Part 17 — AI AFFILIATE BOT
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 61 — LLM Foundation | `S:P17/C61` | T:G8/W34 | R:AI layer / roadmap | M11–12 | C |
| 62 — AI Product Understanding | `S:P17/C62` | T:G8/W35 | R:AI product→content flow | M11–12 | C |
| 63 — AI Content Engine | `S:P17/C63` | T:G8/W36 | R:AI content example | M11–12 | C |
| 64 — Knowledge Base & RAG | `S:P17/C64` | T:G8/W34 + W37 | R:AI layer / knowledge feedback | M11–12 | C |
| 65 — AI Evaluation | `S:P17/C65` | T:G8/W34 (evaluation intro) | R:human review warning | M11–12 | C |
| 66 — Human-in-the-loop | `S:P17/C66` | T:G8/W36 | R:AI generates → human reviews | M11–12 | C |

### Part 18 — ADVANCED AFFILIATE INTELLIGENCE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 67 — Time-Series Analysis | `S:P18/C67` | T:G10/W44 | R:Product Intelligence history | M12–13 | B/C |
| 68 — Anomaly Detection | `S:P18/C68` | T:G10/W45 | R:Product Intelligence alert context | M12–13 | B/C |
| 69 — Forecasting | `S:P18/C69` | T:G10/W46 | R:money model + Affiliate Intelligence | M12–13 | B/C |
| 70 — Machine Learning Foundation | `S:P18/C70` | T:G12 Expert Level + G10/W46 context | R:Affiliate Intelligence roadmap | M12–13 | B/C |
| 71 — Learning to Rank | `S:P18/C71` | T:G12 Expert Level (Ranking Models) | R:Affiliate Intelligence roadmap | M12–13 | B/C |
| 72 — Explore vs Exploit | `S:P18/C72` | T:G12 Expert Level (Multi-Armed Bandit) | R:feedback loop / intelligence | M12–13 | B/C |

### Part 19 — PRODUCTION, SECURITY & AUTOMATION
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 73 — Production Engineering | `S:P19/C73` | T:G11/W47–48 | R:Technology stack | M13–14 | C/D |
| 74 — Reliability | `S:P19/C74` | T:G11/W48 | R:Technology stack | M13–14 | C/D |
| 75 — Security | `S:P19/C75` | T:G11/W48 (partial) | R:anti-spam / platform safety context | M13–14 | C/D |
| 76 — Automation Governance | `S:P19/C76` | T:G11/W47 | R:do not auto-publish / anti-spam | M13–14 | C/D |
| 77 — Deployment | `S:P19/C77` | T:G11/W48 (partial) | R:Technology stack | M13–14 | C/D |

### Part 20 — AFFILIATE BUSINESS & SCALE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 78 — Affiliate Operating System | `S:P20/C78` | T:G11/W47–48 | R:feedback loop + automation stages | Conditional | A/D |
| 79 — Portfolio Strategy | `S:P20/C79` | T:G11/W50 + G12 (partial) | R:Affiliate Intelligence roadmap | Conditional | A/D |
| 80 — Creator Monetization | `S:P20/C80` | T:G1/W4 + G11/W50 (partial) | R:monetization framing | Conditional | A/D |
| 81 — Scaling | `S:P20/C81` | T:G11/W47–50 | R:roadmap stages | Conditional | A/D |
| 82 — Affiliate Bot → SaaS | `S:P20/C82` | T:G11/W50 | R:SaaS direction | Conditional | A/D |

### Part 21 — CAPSTONE
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 83 — Affiliate Intelligence Platform | `S:P21/C83` | T:§3 Affiliate Intelligence Platform | R:Affiliate Intelligence end-state | M14–15 | A/B/C/D |
| 84 — Capstone Versions | `S:P21/C84` | T:§3 Versions 0–10 | R:roadmap stages | M14–15 | A/B/C/D |

### Part 22 — CONTINUOUS MASTERY
| Chapter | Canonical syllabus ref | Training ref | Research supplement | Standard month | Track |
|---|---|---|---|---|---|
| 85 — Platform Watch | `S:P22/C85` | T:G2/W8 (partial) | R:platform policy warning | Post-core | A/B/C/D |
| 86 — Legal & Tax Watch | `S:P22/C86` | — | — | Post-core | A/B/C/D |
| 87 — Technology Watch | `S:P22/C87` | T:G12 Expert Level (partial) | R:Technology stack + future intelligence | Post-core | A/B/C/D |
| 88 — Research Practice | `S:P22/C88` | T:G12 Expert Level + §5 learning method | R:research-oriented roadmap / expert direction | Post-core | A/B/C/D |

## 7. Audit notes

- Chapter mapping count: **89/89**.
- Part coverage: **23/23**.
- Canonical lesson relation: deterministic for all **671** lesson IDs via `S:P/C/L`.
- `—` means source supplement does not contain a direct counterpart; it is intentional, not missing data.
- `(partial)` means source section supports only một phần scope của chapter.
- Research supplements are intentionally selective because `Nghien-cuu.txt` mirrors most of the 50-week training plan before adding extra bot/product/architecture material.

## 8. Authoring rule from Step 5 onward

Khi tạo lesson mới:

1. lấy ID/title/scope từ `S`;
2. tra chapter row trong file này;
3. đọc đúng `T`/`R` sections được map trước khi viết;
4. thêm only the refs actually used vào `source_refs`;
5. nếu cần dữ kiện hiện hành, thêm external verification riêng;
6. nếu source conflict, áp dụng precedence ở đầu tài liệu và ghi note nếu conflict ảnh hưởng nội dung.

Traceability không có nghĩa phải nhồi mọi nguồn vào mọi lesson. Mục tiêu là **biết nội dung đến từ đâu và biết khi nào nguồn không hỗ trợ một claim**.