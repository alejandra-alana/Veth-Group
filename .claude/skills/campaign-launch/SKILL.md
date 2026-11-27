---
name: campaign-launch
description: Use when Alejandra asks to launch, load, tweak, QA, pause/unpause or check a Woodpecker or Instantly campaign, add or load leads, or build, enrich or verify a prospect list. Holds the API key labels for each tool and the mandatory MAGIC 2 and HARD DECK pre-launch checks. Not for unrelated tasks like email drafts or writing feedback.
---

# Campaign launch and list work

## API keys in this environment

The keys are environment variables. Never print, paste or share a key value. Refer to keys by their variable name only.

### Launching and running campaigns
When Alejandra says "Woodpecker" or "Instantly", use these keys. Each client has its own key.

| Variable | Tool | Use |
| --- | --- | --- |
| `WOODPECKER_KEY_<CLIENT>` | Woodpecker | One key per client account (e.g. `WOODPECKER_KEY_QUANTILE`, `WOODPECKER_KEY_UNA_JOE`, `WOODPECKER_KEY_UNA_LUKE`). `WOODPECKER_KEY_WARMUPONLY` is not a client key: it is for mailbox warm-up only, so never launch or load campaigns from it. API: `https://api.woodpecker.co/rest/v1/`, header `x-api-key`. |
| `INSTANTLY_KEY_<CLIENT>` | Instantly | One key per client workspace (e.g. `INSTANTLY_KEY_10LOUDER`). `INSTANTLY_KEY_VETHGROUP` is Veth Group's own workspace. For Newave use `INSTANTLY_KEY_NEWAVESOLUTIONS` (the duplicate `INSTANTLY_KEY_NewaveSolutions` opens the same workspace and is being removed). |

To find a client's key, list the variable names: `env | cut -d= -f1 | grep -i '<client>'`. If no key matches the client, say so and ask. Don't guess which account to use.

### Finding prospects (list building)
| Variable | Tool | Use |
| --- | --- | --- |
| `MOLTSETS_API_KEY` | Moltsets | Finding prospects. |
| `QUICKENRICH_API_KEY` | Quick Enrich | Finding prospects. **Never use Quick Enrich data in a list that is sent to a client.** Client-facing lists must come from another source. |
| `GETLEADS_API_KEY` | GetLeads | Finding prospects. |

### Finding and verifying emails
| Variable | Tool | Use |
| --- | --- | --- |
| `FINDYMAIL_API_KEY` | Findymail | Finding email addresses. |
| `ICYPEAS_API_KEY` | Icypeas | Finding email addresses. |
| `MILLIONVERIFIER_API_KEY` | MillionVerifier | Verifying email addresses before a list is loaded. |

### Sending infrastructure (domains and mailboxes)
| Variable | Tool | Use |
| --- | --- | --- |
| `INFRAMAIL_KEY` | Inframail | Mailboxes and domains. |
| `SCALEDMAIL_KEY_VETH` | ScaledMail | Mailboxes and domains. |

Don't use any other key in the environment (AWS, GitHub, LinkedIn and so on) for campaign work unless Alejandra asks.

## Campaign checks: run before launching or loading any campaign

Before launching or loading any campaign, run these checks and report pass or fail on each. **Do not launch if any check fails.**

### MAGIC 2 (every list load, every account)
1. No prospect can be in two ACTIVE (running) campaigns at once for the same client. Paused, completed and draft campaigns don't count, but re-check before unpausing one.
2. Nobody gets the same email copy twice. Confirm no one on the list has already received this copy. Also: no prospect ever gets the same template twice, even across different clients. Check the cross-client ledger first. (Where the ledger lives is not confirmed yet. Until it is, say the cross-client part of this check can't be completed, mark it as not checked, and ask Alejandra before launching.)

### HARD DECK CHECK (every launch)
1. No typos or grammar errors.
2. No links of any kind (no LinkedIn, Calendly or URLs).
3. First email has a signature with the client's physical address.
4. First email has a P.S. opt-out (e.g. "Just let me know if not relevant, and I won't follow up."), not a podcast P.S.
5. Sending mailboxes match the name in the signature.
6. Copy fits the list: titles, geography, and any city, industry or conference named only goes to people known to match.
7. No one on the list is in another running campaign.
8. Copy makes sense on every send date: no wrong-season or time-bound wording ("this week", holidays).
9. Merge fields are clean: first names, and company names with no "Inc." or "LLC".

Never launch or change copy without Alejandra's OK. Typo fixes are pre-approved.
