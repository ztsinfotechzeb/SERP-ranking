---
name: client-flee-google
description: Client playbook for the GOOGLE Ads account of FLEE Escape (fleeescape.com), an immersive entertainment venue in Redmond, Washington (Greater Seattle) with movie-style escape rooms, Zero Latency (ZL) free-roam VR, birthday and corporate team-building packages. Client Mr. Kashyap Dadia, agency owner Tamasa Kundu, budget in USD. Account ID in the sheet is 1528528628550103 (that is the Meta ad account; the real Google Ads CID is not in the sheet). Use for ANY Google Ads task on this account, including campaigns, keywords, negatives, tracking, reports, client replies, or updating the "Flee Google" tab of the PPC Master Sheet. Trigger on "Flee Google", "FLEE Escape" with Google, "fleeescape", "Zero Latency", "Kashyap" with Google, or "Redmond escape room". For FLEE's Meta (Facebook/Instagram) ads use client-flee-meta (tab "Flee Meta", owner Aman Sharma) instead.
---

# FLEE Escape (fleeescape.com): Google Ads

Use this skill together with the agency skill `ppc-agency-manager` (golden rules, approval gates,
report templates). This file holds only what is specific to this client.
Source: PPC Master Sheet, tab **`Flee Google`** (Master Profile row 5, snapshot 01-Oct-2026). The tab has no
update-log rows; the client feedback summary and the 29-Sep-2026 meeting are written out in `references/history.md`.
Always re-read the live tab before acting. If the sheet and this file disagree, the sheet wins; then update this file.

Sibling account: FLEE also runs Meta Ads with us (tab `Flee Meta`, skill `client-flee-meta`, owner Aman Sharma).
Bing (Microsoft) Ads are also discussed in meetings, reported by Utpal. Budget decisions are made across Google, Meta
and Bing together.

## 1. Account card

| Field | Value |
|---|---|
| Website | https://fleeescape.com/ |
| Sheet tab | `Flee Google` |
| Platform | Google Ads |
| Account ID (sheet) | 1528528628550103. **This is the Meta ad account ID** (same as `Flee Meta`). Google Ads CID: not in sheet. |
| Client contact | Mr. Kashyap Dadia |
| Account owner (agency) | Tamasa Kundu (also Action Owner) |
| Stage | 6-Live & Optimizing |
| Package | Sheet says "Silver Meta Ads Campaign Management" (copied from the Meta tab; confirm the Google package) |
| Payment mode | PayPal Payment Invoice |
| Start date | 03.26.2026 (read as 26-Mar-2026) |
| Confirmation received | "waiting for this month" |
| Monthly cycle | 27th of every month |
| Budget | Sheet: **4,800 / month, $160.00/day** (USD by "$"; US client). The 29-Sep meeting set the **October Google budget at $3,600, excluding Halloween campaigns**. Confirm which is live. |
| Bidding | Maximise conversions; target CPA |
| Risk status | **Green** |
| Communication | Basecamp |

## 2. Access & tracking tools

| Tool | Status |
|---|---|
| GA4 | G-MPK7VRBTVS, via zebratechiessolutionppc@gmail.com |
| GTM | GTM-WVT42TG, via zebratechiessolutionppc@gmail.com |
| Microsoft Clarity | w9e0wrd78f |
| CRM | Bookeo (booking system), access on the agency PPC mail ID |
| Meta BM / Pixel | 125203908202371 (sheet shows ".0" number artifact) |
| Merchant Center, GBP | NA |

Credentials: never copy them here. Use the team vault.

## 3. Business overview (from questionnaire)

- Immersive entertainment venue in **Redmond, Washington**, serving Greater Seattle.
- Movie-style escape rooms: Prison Escape, Ancient Egypt, Museum Heist, Ice Walker, Steampunk Submarine, with
  different difficulty levels.
- **Zero Latency VR** (free-roam VR), party packages, facility rentals, corporate events.
- Serves friends, families, birthdays, date nights and corporate team building. Private rooms and group packages.
- Positioning: high-energy, immersive group entertainment combining story-driven escape rooms, VR, celebrations and
  team building.
- Corporate packages cost **$560 to $900** (client says many corporate groups find this expensive).

### Products to promote (priority order)
1. Birthday party package
2. Corporate party package
3. New Jumanji VR game (spelled "jumaji" in sheet; launch around December)

### Target locations (23 cities, all Washington, US)
Auburn, Bellevue, Bothell, Duvall, Edmonds, Everett, Federal Way, Issaquah, Kenmore, Kent, Kirkland, Lynnwood,
Mercer Island, Mill Creek, North Bend, Redmond, Renton, Sammamish, Seattle, Shoreline, Snoqualmie, Tacoma, Woodinville.

## 4. Audience

- **Primary:** friends and groups wanting unique entertainment; families and teenagers; couples / date night; birthday
  and celebration groups; corporate teams.
- **Secondary:** gamers and VR fans; tourists; school and youth groups; event planners; adventure and puzzle fans.
- **Exclude:** users outside the service area; very young children; people wanting non-interactive entertainment; job
  seekers; low-intent users.
- **Pain points:** finding unique group activities; need for something beyond normal outings; hard to plan memorable
  celebrations; few interactive team-building options; want immersive experiences.
- **Negative terms:** Basecamp thread https://app.basecamp.com/4839868/buckets/46649552/messages/9720639107

## 5. Competition & positioning

- Landscape: escape room venues, VR gaming centres, bowling and arcades, indoor entertainment centres, party and
  corporate activity providers.
- Differentiation: immersive story-driven rooms; real escape rooms plus free-roam VR in one venue; casual and corporate
  options; many themes and difficulty levels; private, group-focused.
- Proof points: movie-style rooms; Zero Latency VR; themes (Prison Escape, Ancient Egypt, Museum Heist); birthday,
  private party and corporate packages; team building; Redmond location serving Greater Seattle.
- Competitors seen in auction insights / ads: visitmirra.com, sandboxvr.com, www.dimensionxr.com,
  https://www.puzzlebreak.us/, https://realitybreakescapes.com/, https://cognitionescapes.com/
- Competitor campaigns: split into **two separate competitor campaigns, one for FLEE and one for ZL**. Results so far
  inconsistent and below core campaigns. Plan: a competitor landing page showing ZL/FLEE advantages.

## 6. Conversions & tracking

- Goal: **Purchase** (bookings). Split: Purchase, phone calls, lead forms.
- Setup: purchase tracking verified for ZL. Escape room purchases are verified **manually using Bookeo confirmations**.
- Tracking Status in sheet: **Verified**. But the client feedback lists open tracking issues:
  - Several purchases close together make keyword attribution hard.
  - UTM parameters and tracking info do not pass through the booking process consistently.
  - Google Ads form submissions do not match dashboard-reported conversions.
  - Conversion setup changes still need verifying in production.
  - Booking-flow bug: users sometimes return to the start after choosing a room.
- Client tracks ROAS. Google ROAS has been **4.4x to 5.2x** over recent months. Target: keep ROAS **above about 4.5**.

## 7. Campaigns & optimization

- Live: **Search and Performance Max**. Campaign themes: core escape rooms / ZL, Corporate Team Building (dedicated
  campaign), Birthday Party (dedicated Search campaign agreed), competitor (FLEE and ZL, separate), seasonal.
- **Halloween campaign launched 01-Oct-2026** (new Halloween ads and asset groups).
- Seasonal campaigns (July, Memorial Day, Labor Day) produced strong returns. Policy: "new campaign for every occasion".
- Best keywords (client-mentioned): "escape room team building", "team building activities near me".
- Routine (daily work): add negatives; change match types when needed; check auction insights; website CRO checks and
  suggestions; launch occasion campaigns.
- Budget rules agreed with the client: do not raise budgets aggressively at once; watch changes for 10 to 12 days
  before big budget moves; raise gradually on top campaigns; use campaign-level revenue and ROAS to decide.
- Files: keyword file / working doc https://docs.google.com/spreadsheets/d/1WRLodos9f9XdkFjAb53RG9dNvIOAjYdGNh2C5A2nML4/edit?usp=sharing
  (clusters tab gid=126893063). Ad assets: https://drive.google.com/drive/folders/1Yq8RxTMwVBmRjRF88g38Cj1_kwLbOeha?usp=sharing
- Negative and new keywords logged in Basecamp: https://app.basecamp.com/4839868/buckets/46649552/messages/9720639107

### Landing pages / CRO
- Birthday Party landing page: under discussion. The client is building a separate birthday page for the separate
  birthday campaign.
- ZL Jumanji landing page: pending (needed before the December release).
- Also planned: Team Building landing page (A/B test), competitor landing page.
- New landing page with integrated booking flow: owner Pradeep, due **mid-October**.
- Goals: keep visitors on the intended offer, stop leakage to other booking pages, A/B test, booking flow on the page.
- FLEE to fix the Zero Latency logo link on the website.

## 8. Performance snapshot (1-Aug-2026 to 30-Sep-2026)

| Spend | Impr. | Clicks | CTR | Conv. | CPA | Conv. rate | Qualified leads |
|---|---|---|---|---|---|---|---|
| 6,499.23 | 1,053,761 | 5,679 | 8.66% (sheet) | 1,102.03 | 5.90 | 6.18% (sheet) | not in sheet |

Spend currency is not stated in the cell (the budget uses "$"; US client, so USD is likely). Checks (computed): CTR 5,679 / 1,053,761 = **0.54%**, not
8.66%. Conversions per click 1,102.03 / 5,679 = **19.4%**, not 6.18%. CPA 6,499.23 / 1,102.03 = 5.90 (matches).
Spend is about 3,250 a month (computed), below the sheet's 4,800 monthly budget. Re-pull from Google Ads before
reporting. Revenue and ROAS per campaign: not in sheet (client feedback says 4.4x to 5.2x).

## 9. Reporting & meetings

- Weekly report: **every Monday**, same Google Sheet:
  https://docs.google.com/spreadsheets/d/1EeawoTPCEPOqfSvZ0BjFRuZ6f9xSurDoiGIE2cCGTQE/edit?gid=179105092#gid=179105092
- Weekly conversion report: **every Monday**, same sheet (Conversion Reporting Format).
- Monthly report: Looker Studio https://datastudio.google.com/reporting/393dfb9f-3508-4ae2-a272-0a981007d7cc
  (cycle on the 27th).
- Meetings: **monthly**. Last meeting 29-Sep-2026. Next meeting: NA in sheet (expect late October).
- Reports must show campaign-level revenue and ROAS, not just spend. Full search-term reports were requested for the
  corporate campaigns so the client can mark exclusions.
- Channel: **Basecamp**.

## 10. Client relationship

- Client is **satisfied**. He sees Google as the strongest platform, said Google and Meta ROAS are good, and asked to
  raise the budget. Open to more budget on high performers if efficiency holds.
- Complaint / issue list (status **In Progress**): birthday traffic not turning into birthday-package bookings;
  corporate traffic booking regular rooms instead of premium packages; tracking and attribution gaps; possible
  booking-flow bug; weak competitor campaigns; unfocused landing pages.
- Our actions so far: budget raised; dedicated corporate campaign; competitor campaign split into FLEE and ZL; client
  building a birthday landing page for a separate birthday campaign; Halloween ads and asset groups launched.

### Client priorities (in his order)
1. Scale budget while keeping ROAS above about 4.5.
2. Improve Birthday Party performance (US birthday season starts around September: priority).
3. Improve Corporate Team Building package conversions.
4. Fix tracking and booking-flow issues.
5. Launch dedicated landing pages and A/B tests.
6. Prepare Halloween and Jumanji campaigns.
7. Improve competitor campaigns.

Full feedback and the 29-Sep MoM: `references/history.md`.

## 11. Open actions & how to move this account forward

1. **Tracking audit (highest risk to ROAS claims).** Check that UTMs / gclid survive the Bookeo booking flow, compare
   Google Ads form conversions vs the dashboard, confirm the conversion changes are live in production, and reproduce
   the "back to start" booking bug. Report findings to the client. Consider changing Tracking Status to Partial until
   this is done. Changes to live tags need approval.
2. **Halloween (launched 1-Oct, ends 31-Oct).** Watch daily; Halloween budget sits outside the $3,600. Pause/remove
   Halloween ads after the event (needs approval).
3. **Birthday Party Search campaign**: build it now to use the client's new landing page when ready (needs approval to
   launch). Season already started.
4. **Mid-October checkpoint**: confirm Pradeep's landing page with booking flow is on track; plan an A/B test.
   The 7 to 10 day landing page behaviour analysis (Clarity w9e0wrd78f) was due around 6 to 9-Oct: send it if not sent.
5. **Corporate Team Building**: send the full search-term report (requested), add negatives, prepare the Team Building
   landing page A/B test. Consider ad copy that sets price expectations to filter low-value clicks.
6. **Jumanji (December)**: draft campaign plan and assets by mid-November; landing page is on FLEE's side.
7. **Budget scaling** (needs approval): after 10 to 12 days of October data, propose gradual increases on campaigns with
   ROAS above 4.5, using campaign-level revenue.
8. **Cross-platform**: Bing at about 1.6 ROAS; pause Bing for October and move budget to Google/Meta was discussed. Get
   the decision recorded. Coordinate with Utpal (seasonal revenue data for July, Memorial Day, Labor Day; Bing
   revenue in reports) and the Flee Meta owner.
9. **Sheet fixes**: add the real Google Ads CID; fix Package; reconcile budget (4,800 / $160 vs $3,600 October); correct
   CTR and Conv. rate; fill Next Meeting Date; get the monthly confirmation.

## 12. Sheet update reminder

Tab name: `Flee Google`. Append a log row after every task (Entry Date, Updated By, Entry Type, project name), using the
column rules in `ppc-agency-manager/references/master-sheet-schema.md`.

## Data issues found in the sheet

- Account ID 1528528628550103 is the Meta ad account (same in `Flee Meta` and in the Project Index for both tabs). No
  Google Ads CID recorded.
- Package reads "Silver Meta Ads Campaign Management" on the Google tab.
- Budget 4,800 / $160 per day vs the $3,600 October budget agreed on 29-Sep.
- CTR (0.0866) and Conv. rate (0.0618) do not match the impressions, clicks and conversions.
- Feedback column has many "Pasted text" artifacts from copy-paste.
- Tracking Status "Verified" while tracking discrepancies are an open issue.
