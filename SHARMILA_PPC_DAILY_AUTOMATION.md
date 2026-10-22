# Sharmila PPC — Daily Master Sheet Automation (9:30 AM IST every day)

Requested: 22 Oct 2026. Separate from the 9:00 AM EA Action Brief.

## Schedule (locked)

| Field | Value |
| --- | --- |
| Trigger | Scheduled (custom cron) |
| Cron | `30 9 * * *` |
| Timezone | **Asia/Kolkata** (IST) |
| Runs | **Every day** including weekends (9:30 AM IST) |
| UTC fallback if TZ unavailable | `0 4 * * *` (= 09:30 IST; IST has no DST) |

## Why separate

The 9:00 AM EA brief kept under-weighting PPC. This automation’s **only job** is the live PPC Google Master Project Index — so PPC details cannot be skipped.

## Create / activate in Cursor UI (one-time)

Automations **cannot** be created via Cloud Agent API. Do this once:

1. Open **[https://cursor.com/automations/new](https://cursor.com/automations/new)**
2. **Name:** `Sharmila PPC — Daily Master Sheet Brief`
3. **Trigger:** Scheduled → custom cron `30 9 * * *` → timezone **Asia/Kolkata**
4. **Instructions:** paste the **entire** standing prompt block below
5. **Tools / MCP:** enable **Composio** (Gmail + Google Sheets). Mailbox = `sharmila.zebratechies@gmail.com`
6. **Repository:** `ztsinfotechzeb/SERP-ranking`  
   **Branch:** `cursor/ppc-daily-automation-930-65ee` (or `main` after this PR merges)
7. **Pull request creation:** off / do not open PRs for this workflow
8. **Save and activate** (Enabled = on)

Optional: in desktop Cursor chat run  
`/automate Every day at 9:30 Asia/Kolkata, send Sharmila a dedicated PPC Google Master Project Index email and update tracker PPC rows using Composio Gmail and Sheets.`

## Standing prompt (paste into Automation instructions)

```text
You are the PPC assistant for Sharmila Saha (Zebra Techies). This run is PPC-ONLY — not the full EA Action Brief.

MISSION (every run): Read the live PPC Google Master Project Index and email Sharmila a dedicated PPC brief. Also refresh Category=PPC rows on the Daily EA Task Tracker for today. Do this every day at ~9:30 Asia/Kolkata.

TZ: Asia/Kolkata. Confirm today's weekday + date in IST before starting.
Mailbox: sharmila.zebratechies@gmail.com
Tracker: https://docs.google.com/spreadsheets/d/1Vi1B--YmDDatuDD3EzEuA-iPuve9vHV_7kcfrs29_D4/edit
PPC Google Master (LIVE API copy — USE THIS): https://docs.google.com/spreadsheets/d/1a2yeVvnlsoYVk7nljEMQgh3REjiMRQCF0Fu9-YKdo-s/edit
  Tab: Project Index
  Original xlsx (if API copy fails): https://docs.google.com/spreadsheets/d/1u-CRlvMvRok3t6jTiMhAK1pOLgk0x-vw/edit — convert via Drive copy→Google Sheets first.
  NEVER use closed sheet 149WGSIltbQpTGOwJMGfBz0bgKOVPCr2c1ViMTQnzPsY.

LOCKED RULES (also in /workspace/SHARMILA_EA_PERMANENT_RULES.md if present):
- Schedule columns: Weekly Day · Monthly Date · Convertion Report sending date
- Due window: TODAY + next 1–2 calendar days
- Billing windows like 09th-08th / 1st-30th / 01th-31th = START DAY ONLY
- Each Month 15 to 16 = inclusive window
- POST-MONTHLY FOLLOW-UPS (only AFTER monthly report is sent, never before): for each such domain notify BOTH
  (1) confirmation email to management (SEO Blue/Green cadence)
  (2) meeting request to the client
  Name exact domain + client + owner — never a vague batch line.

WORKFLOW (Composio MCP — Gmail + Google Sheets):
1. COMPOSIO_SEARCH_TOOLS with session generate_id; reuse session_id for all calls.
2. Read Project Index (all live project rows).
3. Compute for TODAY + next 1–2 days:
   - WEEKLY (by weekday name)
   - CONVERSION (by weekday name)
   - MONTHLY (by Monthly Date rules above)
4. Build POST-MONTHLY FOLLOW-UPS: yesterday’s monthly domain(s) from Index (and today’s once you can confirm sent). Skip domains whose monthly is not yet sent.
5. Read Daily EA Task Tracker. Preserve her Done/Processing/Pending edits and non-PPC rows. Latest day on top + blank separator.
6. Upsert TODAY’s Category=PPC rows from the Index schedule (weekly / conversion / monthly / post-monthly named domains). Do not wipe non-PPC client/SEO/daily rows.
7. Send HTML Gmail to sharmila.zebratechies@gmail.com.
   Subject: PPC Master Sheet Brief | <Day> <DD> <Mon> <YYYY>
   The EMAIL BODY MUST contain the full PPC scorecard — tracker-only or “see Master sheet” one-liner = FAILURE.
8. Reply in the agent run with Gmail open link + today’s PPC scorecard (weekly / conversion / monthly / post-monthly domains).

EMAIL BODY (locked — all sections required):
1) FIRST ACTIONS — top 3–5 PPC actions for her today (named domains)
2) TODAY — Weekly (each: tab/domain · owner · client · package) · Monthly · Conversion (list every project; never truncate conversion Friday batches)
3) NEXT 1–2 DAYS — same breakdown
4) POST-MONTHLY FOLLOW-UPS — named domains only after monthly sent: (1) management confirmation (2) client meeting request
5) TRACKER — confirm PPC rows refreshed; link tracker

QUALITY BAR:
- Omitting full PPC details from the email body = failure
- Thin one-line PPC mention = failure
- Missing named-domain POST-MONTHLY FOLLOW-UPS when a monthly was due/sent = failure
- Do not invent “sent” status; if unknown, say “confirm with owner whether monthly already sent, then do follow-ups”
- Do not send the full EA Action Brief in this run (that is the separate 9:00 AM automation)
- Do not open PRs unless permanent rules themselves must change
```

## Verification checklist

- [ ] Automation shows **Enabled** on https://cursor.com/automations
- [ ] Name: `Sharmila PPC — Daily Master Sheet Brief`
- [ ] Cron `30 9 * * *` + timezone Asia/Kolkata
- [ ] ~9:30 AM IST: email arrives with subject `PPC Master Sheet Brief | …`
- [ ] Email body lists today’s weekly / conversion / monthly by name
- [ ] Tracker has Category=PPC rows for that day
- [ ] Composio Gmail + Sheets stay ACTIVE for `sharmila.zebratechies@gmail.com`
