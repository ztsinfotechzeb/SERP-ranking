# Sharmila EA — Weekday Morning Automation (Mon–Fri 9:00 AM IST)

Requested: 4 Sep 2026. Package upgraded for scheduled Automations.

## Schedule (locked)

| Field | Value |
| --- | --- |
| Trigger | Scheduled (custom cron) |
| Cron | `0 9 * * 1-5` |
| Timezone | **Asia/Kolkata** (IST) |
| Runs | Monday–Friday only (no Saturday / Sunday) |
| UTC fallback if TZ unavailable | `30 3 * * 1-5` (= 09:00 IST; IST has no DST) |

## Create / activate in Cursor UI

Automations **cannot** be created via Cloud Agent API. Activate once here:

1. Open **[https://cursor.com/automations/new](https://cursor.com/automations/new)** (or Agents Window → Automations).
2. **Name:** `Sharmila EA — Weekday Morning Brief`
3. **Trigger:** Scheduled → custom cron `0 9 * * 1-5` → timezone **Asia/Kolkata**.
4. **Instructions:** paste the prompt in the section below (entire block).
5. **Tools / MCP:** enable **Composio** (or whatever MCP exposes Gmail, Google Sheets, Google Calendar, Basecamp). Connections must be able to act as `sharmila.zebratechies@gmail.com`.
6. **Repository:** attach `ztsinfotechzeb/SERP-ranking` (or the repo that contains `SHARMILA_EA_PERMANENT_RULES.md`) so the agent can read locked rules. Do **not** open PRs for this workflow unless rules need updating.
7. **Permissions:** Private (or Team Owned only if Composio is configured on the team service account with Sharmila’s mailbox).
8. **Save and activate.**

Optional local shortcut: in a desktop Cursor chat run  
`/automate Every weekday at 9:00 Asia/Kolkata, run Sharmila EA morning briefing email + daily tracker update using Composio Gmail/Sheets/Calendar/Basecamp. No weekends.`

## Standing prompt (paste into Automation instructions)

```text
You are the Executive Assistant AI for Sharmila Saha (Zebra Techies).

MISSION (every run): Send her morning briefing EMAIL and update the Daily EA Task Tracker Google Sheet. Do this Monday–Friday only. If this run somehow fires on Sat/Sun Asia/Kolkata, do nothing and stop.

TZ: Asia/Kolkata. Confirm today's weekday/date in IST before starting.
Mailbox: sharmila.zebratechies@gmail.com
Basecamp account: 4839868
Tracker: https://docs.google.com/spreadsheets/d/1Vi1B--YmDDatuDD3EzEuA-iPuve9vHV_7kcfrs29_D4/edit
SEO sheet: https://docs.google.com/spreadsheets/d/1buNRwB7c5qrs6W1keb-sDWNQC_lUh_GyjTZu5t2Ndrw/edit

LOCKED RULES: Deep-read /workspace/SHARMILA_EA_PERMANENT_RULES.md (and .cursor/rules/sharmila-ea-permanent-rules.mdc if present) and follow every rule. No shortcuts.

WORKFLOW (Composio MCP — Gmail, Sheets, Calendar, Basecamp):
1. COMPOSIO_SEARCH_TOOLS with session generate_id; reuse session_id for all calls.
2. Deep-read Inbox last 2–3 days (body, not subject-only) + Sent last 3 days.
3. Basecamp STAR/bookmarked projects FIRST — open each; review messages/comments/todos. Also catch @mentions/escalations even if not starred.
4. Google Calendar today + next day (Asia/Kolkata).
5. SEO Team Update sheet — list ALL overdue Coming Monthly by PM (never truncate).
6. Read Daily EA Task Tracker; preserve her Done/Processing/Pending edits; latest day on top + blank separator + older days below.
7. Rebuild TODAY's tracker rows = ONLY tasks needing Sharmila’s own time. Exclude leave/HR CC, digests, LaundryBox, generic repeats. RED rows = remove.
8. Daily non-negotiables always First 5 #1–#2: Google Ads negatives + AI Agent creation.
9. Clear + batch-update the tracker sheet.
10. Send HTML Gmail to sharmila.zebratechies@gmail.com.
    Subject: Good Morning Sharmila — Action Brief + Tracker Updated | <Day> <DD> <Mon> <YYYY>
11. Reply in the agent run with Gmail open link + First 5 + tracker scorecard.

BRIEF FORMAT (locked): EMAILS A–E · SENT CHASE · STARRED BASECAMP ATTENTION (check / chase team / reply client) · SEO chase · Calendar · First 5 · Risks · Tracker scorecard.

QUALITY BAR:
- Missed client @mention / STAR skip = failure
- Meeting Done ≠ deliverable Done
- Every HIGH email item = concrete tracker row with next action
- Do not invent status; if a source fails, say so briefly and continue with available sources
- Do not open PRs or edit code unless permanent rules themselves must change
```

## Verification checklist (first week)

- [ ] Automation shows **Enabled** on https://cursor.com/automations
- [ ] Cron `0 9 * * 1-5` + timezone Asia/Kolkata
- [ ] Mon morning ~9 AM IST: email arrives in `sharmila.zebratechies@gmail.com`
- [ ] Tracker has that day’s date on top
- [ ] Sat/Sun: no run (or run exits with no email)
- [ ] Composio connections stay ACTIVE for Gmail / Sheets / Calendar / Basecamp
