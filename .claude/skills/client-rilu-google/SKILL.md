---
name: client-rilu-google
description: Client playbook for RILU e-Bike on Google Ads (rilu-e-bike.com.au), an Australian e-bike brand (BOLT, ONYX, CRUZE, NOMAD, POGO, URBAN) that sells only through a nationwide dealer network. Google Ads Search and Performance Max, client Ms Payal (RSSL), agency owner Tamasa Kundu, budget A$50/day. The sheet's Account ID cell holds 520672787332225, which looks like the Meta ID (same as Rilu Meta), so confirm the Google Ads CID in the MCC. Use for ANY Google Ads task on this account, such as dealer outbound-click conversion tracking, state targeting (QLD and WA push, NSW paused, VIC and SA steady), keywords and negatives, Looker Studio monthly report on the 12th, the "Other" location question, Friday conversion report, Basecamp replies, or updating the "Rilu Google" tab of the PPC Master Sheet. Trigger on "Rilu Google", "RILU", "rilu-e-bike", "Payal", "RSSL" or "e-bike dealers" when the topic is Google Ads. For Meta (Facebook/Instagram) work on the same brand use `client-rilu-meta` instead.
---

# RILU e-Bike (rilu-e-bike.com.au): Google Ads

Use this skill together with the agency skill `ppc-agency-manager` (golden rules, approval gates,
report templates). This file holds only what is specific to this client's **Google Ads** account.
Meta work on the same brand lives in `client-rilu-meta` (owner Aman Sharma).
Source: PPC Master Sheet, tab **`Rilu Google`** (Master Profile row 5, entry date 01-Oct-2026). The tab has no
update-log rows. Always re-read the live tab before acting. If the sheet and this file disagree, the sheet wins;
then update this file.

## 1. Account card

| Field | Value |
|---|---|
| Website | https://www.rilu-e-bike.com.au/ |
| Platform | Google Ads |
| Account ID (sheet) | 520672787332225 (shown as 520672787332225.0). **Not a Google Ads CID format**; same number as the Rilu Meta tab. Google CID: not in sheet. |
| Client contact | Ms Payal (RSSL) |
| Account owner (agency) | Tamasa Kundu |
| Stage | 6-Live & Optimizing |
| Package | Bronze Google Ads |
| Payment mode | PayPal payment invoice |
| Start date | 21-May-2024 |
| Confirmation received | 14-Sep-2026 |
| Monthly cycle | 12th of every month |
| Budget | **A$1,500 / month** (sheet says "A$1500.00/day", which is a typo: A$50/day x 30 = A$1,500), **A$50 / day** |
| Bidding | Maximise conversions |
| Risk status | **Green** |

## 2. Access & tracking tools

| Tool | Status |
|---|---|
| GA4 | G-J051ECNLKH, access on zebratechiessolutionppc@gmail.com |
| GTM | GTM-M4NT82F, access via Kandy Heller |
| Microsoft Clarity | Project ID `npqt9b8wes` |
| Merchant Center | NA |
| GBP | NA |
| GSC, CRM, CMS | Not in sheet |

Credentials: never copy them here. Use the team vault.

## 3. Business overview (from questionnaire)

- Australian e-bike brand, **11+ years** nationwide. Street-legal electric bicycles for commuting, leisure,
  adventure and everyday mobility.
- Models: BOLT, ONYX, CRUZE, NOMAD, POGO, URBAN. Commuter, step-through, folding and fat-tire options.
- Features: Samsung batteries, low-step designs, suspension, long range, 25 km/h street-legal assistance.
- **Sales happen through a dealer network, not online.** The site sends buyers to dealers. Dealers offer test
  rides, spare parts and warranty support. The client will not change the site to direct online sales.
- Bikes cost over $2,000. Buyers do not purchase straight away.
- (The overview cell contains a stray "citeturn0search1" text artifact; ignore it.)

### Products to promote (priority order)
1. BOLT: practical everyday commuter.
2. ONYX: comfortable city and lifestyle riding.
3. NOMAD: adventure and off-road.
4. POGO: compact and versatile.
5. URBAN: everyday urban commuting.
(CRUZE is in the range but not in the priority list.)

### Target locations
VIC, QLD, WA, SA, TAS. **NSW is paused for now** (certificate requirements, client instruction).

## 4. Audience

- **Primary:** e-bike commuters; urban and city riders; eco-conscious consumers; leisure and recreational riders;
  adults looking for an alternative to cars.
- **Secondary:** adventure and off-road riders; fitness and cycling enthusiasts; older riders seeking assisted
  mobility; students and local commuters; delivery and everyday utility riders.
- **Exclude:** users outside Australia; traditional bicycle-only shoppers; people not interested in electric
  mobility; job seekers; low-intent audiences.
- **Negatives:** kept in Basecamp: https://app.basecamp.com/4839868/buckets/37610761/messages/9631713918
  (the same Basecamp message holds daily work, negatives added and new keywords).
- **Pain points (use in ads):** high fuel and commuting costs; traffic and parking; need for convenient everyday
  transport; limited affordable mobility options; wish for eco-friendly transport.

## 5. Competition & positioning

- Landscape: other e-bike brands, traditional bike retailers, e-scooter brands, online e-bike retailers, local
  bike shops.
- Differentiation: wide model range; commuting, leisure and adventure options; practical designs for Australian
  riders; test rides through dealers; nationwide dealer and support network.
- Proof points: 11+ years in the Australian e-bike market; models BOLT, ONYX, CRUZE, NOMAD, POGO and URBAN;
  street-legal options; nationwide dealers; test rides and after-sales support; warranty and spare parts.
- Auction note: in **WA and QLD a few RILU dealerships run their own ads**. Expect overlap on brand terms there.
- SEO visibility score 28 in Semrush (from the meeting).

## 6. Conversions & tracking

- Goal: **Outbound Link Click** (to dealers).
- Set-up: GTM. Status: **Verified**.
- For each dealer, 4 outbound click conversions via GTM: (1) their own website, (2) their phone number,
  (3) their webpage, (4) their email.
- Done in the last 3 months: conversion actions built for all **7 dealerships in WA and QLD** and added to the
  campaigns.
- Gap: no sale data. The client "can't confirm" qualified leads. We asked for **monthly dealer-wise and
  model-wise sales data** (for example August sales by model per dealer).

## 7. Campaigns & optimization

- Live: **Search and Performance Max**.
- Keyword file / working doc / report-sent link (same sheet):
  https://docs.google.com/spreadsheets/d/1zy5CE-lbiFvkAo-Ja_rjMe72r3gavRVgEQMWWjrAz8Y/edit?usp=sharing
- Ad assets and media: https://drive.google.com/drive/folders/1a2z2e4lyL4-fXtutpVW5RIx1IknW1coJ?usp=sharing
- Daily work, negatives and new keywords: Basecamp message above.
- Last optimization: conversion actions for the 7 WA and QLD dealerships added; VIC and SA remain the key
  performing regions.

## 8. Performance snapshot (1-Aug to 30-Sep, year not stated, read as 2026; two months)

| Spend | Impr. | Clicks | CTR | Conv. | CPA (sheet) | Conv. rate (sheet) | Qualified leads |
|---|---|---|---|---|---|---|---|
| A$2,948.70 | 86,199 | 5,232 | 6.07% | 945.96 | A$3.14 | 16.64% | Client can't confirm |

- Computed check: CPA = A$3.12 and conversion rate = 18.08% from the numbers above. The sheet values (A$3.14,
  16.64%) do not match exactly. Recheck in Google Ads.
- Spend of A$2,948.70 over two months is about A$1,474/month (computed), in line with the A$1,500 budget.
- Conversions are outbound clicks, not sales. Say so whenever you quote CPA.

## 9. Reporting & meetings

- Weekly conversion report: **every Friday**. Weekly report / conversion format cell says "Conversion Report Of
  rilu-e-bike.com.au", but the link points to the website (http://rilu-e-bike.com.au/), not a sheet. Find the
  real file.
- Monthly report on the **12th** (Looker Studio):
  https://datastudio.google.com/reporting/e32dfa8f-0d75-49bd-8656-508a37ec809a
  The client asked many times what **"Other" in location** means. We fixed it by sending a separate location
  report from the Google Ads dashboard, merged into the PDF via Sejda. Keep doing this each month.
- Meetings: on request. Last meeting **18-Sep-2026**. Next meeting NA.
- Channel: **Basecamp** (Google Ads thread and Google Ads report thread).

## 10. Client relationship

- No complaint on Google Ads (status Resolved). She asked about WA and QLD campaigns; we acted and informed her.
- Meeting 18-Sep-2026 (MoM summary):
  - Payal said her side feels paid ads cost too much for the results, and asked whether spend should stop.
    We advised not to stop, because ad algorithms need conversion data, and the dealer model limits tracking.
  - We asked for monthly dealer sales data (by model and dealer) to refine model and radius bidding.
  - She wants **all dealers** promoted, not only top ones like Electric Bike Superstore. Focus on **QLD and WA**,
    where two dealers get no ad traffic.
  - **Pause NSW** for now (upcoming certificate requirements). Move that budget to QLD and WA. Keep VIC and SA.
  - We agreed to review WA and QLD and send a new strategy for Google and Meta.
- 29-Sep-2026 Basecamp: **Everyday Ebikes (QLD) is not responding to customers properly.** Bike Shop & Hire and
  Wobble In are performing well; push these two more. This applies to the Meta team too.
- Tone: practical and results-focused. She cares about dealer-level outcomes.

## 11. Open actions & how to move this account forward

1. **Act on the 29-Sep dealer feedback.** Shift QLD weight toward Bike Shop & Hire and Wobble In (location or
   radius targeting, dealer-specific ads), and reduce traffic to Everyday Ebikes. Tell the Meta owner (Aman,
   `client-rilu-meta`). Budget shifts need approval.
2. **Send the promised revised WA/QLD strategy** from the 18-Sep meeting, if not sent yet (not in sheet). Include
   the NSW pause and budget move.
3. **Check NSW is excluded** in every campaign, including PMax.
4. **Chase monthly dealer sales data** (by dealer and model). Without it, qualified leads stay "can't confirm".
   Chase every 2 business days and log it.
5. **Fix the Account ID**: put the real Google Ads CID in the tab and the Project Index.
6. **Recheck CPA and conversion rate** in the snapshot and correct the sheet.
7. Monthly report on **12-Oct** and **12-Nov**, with the separate location report so "Other" is explained.
8. Review whether 4 outbound actions per dealer inflate conversions. Consider making phone and email clicks
   primary and website clicks secondary (needs approval).
9. Watch dealer ads in WA and QLD in auction insights.

Data issues to fix in the sheet:
- Account ID 520672787332225 is not a Google CID and matches Rilu Meta.
- "Monthly Budget" says A$1500.00/day.
- Weekly report and conversion format links point to the website, not a report.
- Snapshot CPA and conversion rate do not match the raw numbers.
- Overview text has a "citeturn0search1" artifact. The MoM calls it the "Rio project" (transcription error).
- No "Weekly Reporting Date" column in this tab.

## 12. Sheet update reminder

Tab name: `Rilu Google`. Append a log row after every task (Entry Date, Updated By, Entry Type, project
name), using the column rules in `ppc-agency-manager/references/master-sheet-schema.md`. Post the same update in
the Basecamp Google Ads thread.
