# Varisource — Cold Email Campaign 1

Monday item: New Campaign Launches → "Varisource Cold Email Campaign" (13359717451)

## Woodpecker (key: `WOODPECKER_KEY_VARISOURCE`)
- Campaign **2503270** — "Varisource | Finance & Procurement | Wave 1 (250-2000 emp)" — status **DRAFT (not started)**
- 60 Victor Hou mailboxes attached; 10 new prospects/mailbox/day; Mon–Fri 08:00–17:00 prospect time zone (default America/New_York)
- Step 1: "A different kind of Savings Program" (full signature + address + P.S.) → Step 2 bump in same thread after 3 working days (full signature + address + P.S.)
- Open tracking off, auto-pause same domain on reply/bounce, catch-all mode BALANCED
- Payload: `woodpecker_campaign_payload.json`

## Lists
| File | What |
|---|---|
| `lists/sample_enriched_all_430.csv` | Alejandra's 430-contact sample + email waterfall (Moltsets → QuickEnrich) + MillionVerifier result |
| `lists/sample_sendable_288.csv` | Send-ready: MV `ok`, or `catch_all` with Moltsets grade A; max 3/company; tagged Wave 1 (250–2,000 emp, 246 — loaded into 2503270) / Wave 2 (2,001–5,000, 42) |

## Expanded list (Moltsets search) — 2026-11-12
`lists/moltsets_expanded_4101.csv` — 4,101 new contacts at ~3,500 companies (none overlap the sample).
Built with `scripts/moltsets_search.py` (9,000 raw records: 3 role groups × 3 size bands, US, excludes Education/Government) and `scripts/filter_moltsets.py`.
Rules: title must match the role group, no junior/AP/payroll/analyst titles, company 250–5,000 employees, no schools/government, Moltsets grade A/B email, MillionVerifier not `invalid`, max 3 per company (counted with the sample).
- Wave 1 (250–2,000 emp): **3,404 — loaded into campaign 2503270** (campaign total 3,650)
- Wave 2 (2,001–5,000 emp): 697 — not loaded yet (plus 42 from the sample)

## Full ICP list (GetLeads)
Filters in `scripts/filters.py`: US; CFO/VP Finance/Head of Finance (c-level, vp), FP&A + Controller (vp/director/manager), Procurement/Purchasing/Sourcing (c-level/vp/director); excludes schools, education, government, military, law enforcement, public policy; excludes analyst/assistant/buyer/coordinator/etc.; VALID emails only.

Counts on 2026-11-12 (verified email):
| Role | 250–2,000 | 2,001–5,000 |
|---|---|---|
| Finance leadership | 29,699 | 9,297 |
| FP&A / Controller | 27,096 | 12,424 |
| Procurement | 10,987 | 5,348 |

Export with `python3 scripts/build_full_list.py 250 2000 3000 lists/getleads_wave1.csv` once the GetLeads daily fair-use cap resets (00:00 UTC).
