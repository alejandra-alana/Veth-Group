# Varisource — Cold Email Campaign 1

Monday item: New Campaign Launches → "Varisource Cold Email Campaign" (13359717451)

## Woodpecker (key: `WOODPECKER_KEY_VARISOURCE`)
- Campaign **2503270** — "Varisource | Finance & Procurement | Wave 1 (250-2000 emp)" — status **DRAFT (not started)**
- 60 Victor Hou mailboxes attached; 10 new prospects/mailbox/day; Mon–Fri 08:00–17:00 prospect time zone (default America/New_York)
- Step 1: "A different kind of Savings Program" → Step 2 bump in same thread after 3 working days (copy from Monday, signature + P.S. on bump)
- Open tracking off, auto-pause same domain on reply/bounce, catch-all mode BALANCED
- Payload: `woodpecker_campaign_payload.json`

## Lists
| File | What |
|---|---|
| `lists/sample_enriched_all_430.csv` | Alejandra's 430-contact sample + email waterfall (Moltsets → QuickEnrich) + MillionVerifier result |
| `lists/sample_sendable_288.csv` | Send-ready: MV `ok`, or `catch_all` with Moltsets grade A; max 3/company; tagged Wave 1 (250–2,000 emp, 246 — loaded into 2503270) / Wave 2 (2,001–5,000, 42) |

## Full ICP list (GetLeads)
Filters in `scripts/filters.py`: US; CFO/VP Finance/Head of Finance (c-level, vp), FP&A + Controller (vp/director/manager), Procurement/Purchasing/Sourcing (c-level/vp/director); excludes schools, education, government, military, law enforcement, public policy; excludes analyst/assistant/buyer/coordinator/etc.; VALID emails only.

Counts on 2026-11-12 (verified email):
| Role | 250–2,000 | 2,001–5,000 |
|---|---|---|
| Finance leadership | 29,699 | 9,297 |
| FP&A / Controller | 27,096 | 12,424 |
| Procurement | 10,987 | 5,348 |

Export with `python3 scripts/build_full_list.py 250 2000 3000 lists/getleads_wave1.csv` once the GetLeads daily fair-use cap resets (00:00 UTC).
