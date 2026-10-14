---
name: client-betterfit-google
description: Client playbook for the GOOGLE Ads account of Better Fit (betterfit.fit), a personalized fitness and workout-planner app (custom workout plans, workout builder, exercise guide, activity dashboard) promoted with Google App campaigns for installs, mainly on the Apple App Store, in Australia and New Zealand. Google Ads CID 733-662-3901, client contacts Ms Shivangi, her brother and their friend Mr Jordan Williams who owns Betterfit.fit, agency owner Utpal Dey. Budget in AUD. Use for ANY Google task on this account, such as app install campaigns, first-open / install tracking via the developer's SDK, App Store Connect and Play Console checks, video and image assets, the YouTube channel, results summaries to the client on WhatsApp, the monthly report, or updating the "Betterfit" tab of the PPC Master Sheet. Trigger on "Betterfit" (Google), "Better Fit Google", "betterfit.fit" with Google, "app install campaign", "Jordan Williams" or "733-662-3901". For the Meta account of the same app (ad account 1948012045806027, owner Aman Sharma, tab "Betterfit Meta") use client-betterfit-meta instead.
---

# Better Fit (betterfit.fit): Google Ads (App campaigns)

Use this skill together with the agency skill `ppc-agency-manager` (golden rules, approval gates,
report templates). This file holds only what is specific to this client.
Source: PPC Master Sheet, tab **`Betterfit`** (Master Profile row 5, entry date "08.02.2026"). The tab has no
update-log rows and no dated history beyond what is below.
Always re-read the live tab before acting. If the sheet and this file disagree, the sheet wins; then update this file.

Sibling account: the same client runs Meta App Promotion with us (tab `Betterfit Meta`, skill `client-betterfit-meta`,
owner Aman Sharma). The questionnaire covers both. Meta campaigns were at first managed by the client.

This is an **app-install account**, not a website lead or shop account. Keywords, negatives and landing pages do not
apply ("Not required" in the sheet). The extra columns used here are `PlayStore`, `Apps Store Access`, `YouTube Access`
and `Apps Strategy`.

## 1. Account card

| Field | Value |
|---|---|
| Website / app | https://betterfit.fit/ (iOS app on the Apple App Store; Android app on Google Play) |
| Sheet tab | `Betterfit` |
| Platform | Google Ads (App campaigns) |
| Google Ads CID | **733-662-3901** |
| Client contact | Ms Shivangi and her brother, and their friend Mr Jordan Williams, who owns Betterfit.fit |
| Account owner (agency) | Utpal Dey (Action Owner "Utpal") |
| Stage | 6-Live & Optimizing |
| Package | Bronze |
| Payment mode | PayPal Subscription |
| Start date | 08.02.2026 (format unclear: 2-Aug or 8-Feb). Campaigns started **10-Aug-2026** per the results message. |
| Confirmation received | 09.04.2026 (format unclear: 4-Sep or 9-Apr) |
| Monthly date | 10.02.2026 (as in sheet and Project Index; not a recurring day. Likely meant the 10th, matching the 10-Aug launch. Confirm.) |
| Budget | **800 AUD / month, 30 AUD / day** |
| Bidding | "Apps Installtion" (app install optimization) |
| Risk status | **Green** |
| Communication | WhatsApp group (created by Rajib da) |

## 2. Access & tracking tools

| Tool | Status |
|---|---|
| GA4 | Client shared Google Analytics with zebratechiessolutionppc. Stream IDs differ per app (iOS and Android have different app IDs). |
| GTM | No, not required (app account) |
| Google Play Console | Client shared access to the ztsinfotechglobal email. App dashboard: https://play.google.com/console/u/5/developers/5561782409595305302/app/4973623988969300751/app-dashboard |
| App Store Connect (Apple) | Client shared with the zebratechiessolutionppc@gmail.com Apple account. App ID 6754057782 (from the analytics URL in the sheet). |
| CMS (WordPress) | Login exists for https://betterfit.fit/wp-login.php |
| YouTube | Channel https://youtube.com/@betterfit-workoutplanner, created by us with utpaldey.zts@gmail.com. Note in sheet: we first created it from the PPC account but it showed a "violence" flag. |
| Merchant Center, GBP, GSC, Clarity, CRM, Meta BM | not in sheet |

**Credentials: the sheet holds an Apple account password and phone number (`Apps Store Access`) and a WordPress
password and username (`CMS Access`) in plain text. Never copy them here. Move them to the team vault and clear the cells.**

## 3. Business overview (from questionnaire)

- Fitness app that **automatically creates customised workouts** that adapt to goals, preferences and fitness level.
  Not a static video library.
- Features: personalized workout plans, workout builder, exercise guide, activity dashboard.
- Primary goal: **increase app installs and memberships**. Memberships (in-app subscriptions) are the main revenue.
- Audience: general fitness enthusiasts (no special segments).
- Campaign scope: Google Ads and Meta. Google Ads account shared with Zebra Techies.
- Status in questionnaire: awaiting client confirmation on current program details and performance metrics.
- App platforms: iOS and Android each need a separate app ID, tracking and campaign setup.
- Paid plan: install campaigns, conversion campaigns, remarketing campaigns; Facebook, Instagram and Google App
  campaigns.
- Organic plan (client side): 20 to 25 organic posts, live fitness sessions, influencer partnerships, stories.

### Products to promote
1. Apple App Store app (iOS) is the main focus. Android is secondary.

### Target locations
Australia and New Zealand. Major cities: Sydney, Melbourne, Brisbane. "Mainly the primary location, based on the user
that we suggested."

## 4. Audience

- General fitness enthusiasts.
- Jobs to be done: assets were made mainly for app audiences.
- Pain point (ad hook): "Tired of generic YouTube workouts that aren't made for your body, your goal, your level".
- Negatives: none (App campaigns do not use negative keywords).
- Excluded audiences: not in sheet.

## 5. Competition & positioning

- Competitors analysed: MyFitnessPal, Fitbit, Strava, Nike Training Club, Centr, JEFIT.
- Differentiation: workouts adapt automatically to goal, preference and level.
- Proof points / USPs: personalized workout plans, workout builder, exercise guide, activity dashboard.
- Auction insights: "Not found anything" (normal for App campaigns).

## 6. Conversions & tracking

- Goal: **App install**. Optimization signal: first open / first user open.
- Setup: "Firefox, by using his developer". This almost certainly means **Firebase**, set up by the client's developer.
  Confirm with the developer.
- Tracking check: we check first opens against Play Store and App Store data.
- Gap: in-app subscription (membership) events are the revenue driver. Check whether they are imported as Google Ads
  conversions. Not in sheet.

## 7. Campaigns & optimization

- Live: Google App campaign(s), iOS main focus. Structure and strategy in the Apps Strategy doc:
  https://docs.google.com/document/d/11_TZqHqPXoYBXXwq3jkKwTPpC4dpG_G8tvVUSfN1D3A/edit?tab=t.0#heading=h.cchq1oogmgfh
- Ad assets, working doc and "keyword file" (one sheet):
  https://docs.google.com/spreadsheets/d/1iKdUMals2ZfUGsbr2HzVhk7TAqAu7YIYnohjVJCzNZU/edit?gid=0#gid=0
- Media doc: https://drive.google.com/drive/folders/1wWN-XXyfhrStcr2xFUtM3W5Vlf7hoBLI?usp=sharing
- Daily work: regular checks; we analyse user behaviour from Play Store and App Store and send data to the client.
- Last 3 months: optimized at campaign level for app installs / first opens.
- Negatives, new keywords, landing page/CRO: not required.
- Next action in sheet: keep running as is; plan to add more videos. Status "Started", due "Nothing urgent".

## 8. Performance snapshot (10-Aug-2026 to 24/25-Sep-2026)

Sheet period "08.10.2026 to 09.24.2026"; the client message says Aug 10 to Sep 25.

| Installs (iOS) | Sales | In-app purchases (subscriptions) | Spend | Impr. | Clicks | Cost per install |
|---|---|---|---|---|---|---|
| 330 | $126 (currency not stated) | 47 | not in sheet | not in sheet | not in sheet | not in sheet |

Computed: 47 / 330 = 14.2% of installs bought a subscription. Spend, CPI and ROAS cannot be computed without spend.
Pull them from Google Ads.

## 9. Reporting & meetings

- Results are sent as WhatsApp messages (example opening: "Hello Ma'am, We are actively running campaigns based on the
  Apple Store..."). Report installs, sales and in-app purchases with the period.
- Weekly report: No. Weekly conversion report: "Not specific date" (Project Index says Friday).
- Monthly report folder: https://drive.google.com/drive/folders/1EYuwavNz9VtMbJtExd0_-mBs-s4TGs2z
- Conversion reporting format, report/file sent link: No.
- Meetings: last meeting "at project start"; frequency "at a month"; next meeting "depends on client". MoM: none.
- Channel: **WhatsApp** group.

## 10. Client relationship

- Client is **happy with performance so far**. No complaint. Complaint status: No.
- Our stance: keep optimizing the campaign as it is.
- Three people on the client side (Shivangi, her brother, Jordan Williams as owner). Address the group politely
  ("Ma'am" is used).

## 11. Open actions & how to move this account forward

1. **Credentials clean-up (urgent, internal).** Move the Apple and WordPress logins out of the sheet into the team vault
   and clear the cells. Consider asking the client to change the exposed passwords.
2. **Add spend to reporting.** Pull spend, CPI and cost per subscription for 10-Aug to date and add them to the next
   WhatsApp summary and the monthly report. The client will want cost per subscriber, since memberships are the revenue.
3. **Check subscription tracking.** Confirm with the developer that Firebase sends in-app purchase / subscription
   events and that they are imported into Google Ads. If yes, propose testing an in-app action / value goal once
   volume allows (needs approval).
4. **Add videos** (the sheet's next step). Fix the YouTube channel issue (the "violence" flag) so video assets can serve.
   Brief: 16:9, 1:1 and 9:16, 10s+, hook on the pain point. Get client approval first.
5. **Android**: questionnaire says iOS and Android each need their own setup. Decide with the client whether to start an
   Android App campaign (Play Console access already shared). Needs approval.
6. **Coordinate with Betterfit Meta** (Aman Sharma) so both platforms report installs and subscriptions the same way and
   do not double-count.
7. **Set a fixed reporting rhythm**: agree a monthly date (sheet says 10.02.2026) and whether the weekly conversion
   report is Friday (Project Index) or none (tab).
8. Book a monthly check-in; there has been no meeting since project start.

## 12. Sheet update reminder

Tab name: `Betterfit`. Append a log row after every task (Entry Date, Updated By, Entry Type, project name), using the
column rules in `ppc-agency-manager/references/master-sheet-schema.md`.

## Data issues found in the sheet

- Plain-text credentials in `Apps Store Access` and `CMS Access`.
- Dates use an unclear format (08.02.2026, 09.04.2026, 10.02.2026); the period cell uses MM.DD (08.10.2026 to 09.24.2026).
- `Monthly Date` is a single date, not a monthly day.
- Weekly conversion date "Not Specific Date" in the tab vs "Friday" in the Project Index.
- Tracking setup says "Firefox" (likely Firebase).
- No spend, impressions or clicks recorded for the period.
