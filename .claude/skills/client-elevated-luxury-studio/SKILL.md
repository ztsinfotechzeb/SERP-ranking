---
name: client-elevated-luxury-studio
description: Client playbook for Elevated Luxury Studio (elevatedluxurystudio.com, "E.L.S."), an Australian luxury women's fashion brand (dresses, tailored shirts, skirts, knitwear, trench coats, matching sets, Heirloom Collection) sold on Shopify. Google Ads CID 823-235-4584 (Shopping + Demand Gen), client Tarryn Els, owner Tamasa Kundu. The client has given notice and the service ends 18-Oct-2026, so this skill mainly covers offboarding, the final report, handover, termination replies, Basecamp replies, negative keyword approvals, purchase attribution questions and updating the "ELS" tab of the PPC Master Sheet. Trigger on "ELS", "E.L.S.", "Elevated Luxury Studio", "elevatedluxurystudio", "Tarryn" (in a fashion/Shopify context) or "823-235-4584". Not for "kevin els" (Kevin Els Architects, CID 170-500-8592, South Africa): use client-kevin-els for that.
---

# Elevated Luxury Studio (elevatedluxurystudio.com): Google Ads

Use this skill together with the agency skill `ppc-agency-manager` (golden rules, approval gates,
report templates). This file holds only what is specific to this client.
Source: PPC Master Sheet, tab **`ELS`** (Master Profile row 5, snapshot 07-Oct-2026). The tab has no update-log rows;
the dated history is in the profile text and is written out in `references/history.md`.
Always re-read the live tab before acting. If the sheet and this file disagree, the sheet wins; then update this file.

**Status in one line: churning.** Notice given 27-Sep-2026, confirmed 30-Sep-2026. Contract ends **18-Oct-2026**
(end of the payment cycle). Risk **Red**. Priority now is a clean, honest exit.

## 1. Account card

| Field | Value |
|---|---|
| Website | elevatedluxurystudio.com (Shopify store) |
| Sheet tab | `ELS` |
| Platform | Google Ads |
| Google Ads CID | **823-235-4584** |
| Client contact | Tarryn Els (owner). Accounts sit under "E.L.S." |
| Account owner (agency) | Tamasa Kundu (also Action Owner) |
| Stage | 6-Live & Optimizing (in sheet). In reality: notice period, ends 18-Oct-2026. Set to "Churned" after the end date. |
| Package | Basic |
| Payment mode | PayPal Subscription |
| Start date | 06.18.2026 (read as 18-Jun-2026) |
| Confirmation received | 09.21.2026 (read as 21-Sep-2026) |
| Monthly cycle | 18th of every month |
| Budget | **A$900 / month, A$30.00 / day** (AUD stated in sheet). At launch on 25-Jun the budget was set at A$1,000/month. |
| Bidding | Sheet says "Maximize conversion value". The optimization notes say we kept Maximise Conversions and deferred Target ROAS. Check the live account. |
| Risk status | **Red**. Reason: "Google Ads not profitable". |
| Communication | Basecamp |

## 2. Access & tracking tools

| Tool | Status |
|---|---|
| GA4 | Measurement ID G-Z1VEBZXFED, Property ID 539926191 |
| GTM | GTM-M247FXGR, container under "zebra techies ppc". GTM re-install on the site is NOT agreed: we asked 3 times (23 to 25 Sep), no reply. |
| Merchant Center | Yes, ID 5800983906 |
| Shopify | We were given access in June (per optimization notes) |
| Microsoft Clarity | Project ID xj6m55d75o |
| GBP, GSC, CRM, CMS, Meta BM / Pixel | "-" (none recorded) |

Ownership: the client says Google Ads, Merchant Center and GA4 all sit under E.L.S. She will arrange access removal
from her side after the end date. Credentials: never copy them here. Use the team vault.

## 3. Business overview (from questionnaire)

- Luxury women's fashion brand. Timeless, sophisticated apparel for modern women.
- Focus: premium craftsmanship, quality fabrics, versatile pieces that mix elegance with everyday wear.
- Brand language the client wants: tailored, refined, timeless, **"designed in Sydney" / "designed in Australia"**.
  Never say "made in Australia". Do not overuse "luxury". Use only her images and her copy.
- The client said the shirts are not really "tailored" (we moved to button-up / button-down keywords).

### Products to promote (priority order)
1. Luxury women's dresses (occasionwear, events, elevated everyday)
2. Women's tops and shirts (tailored shirts, refined tops)
3. Luxury skirts (mini and maxi)
4. Premium knitwear (turtlenecks, polo knits)
5. Outerwear and trench coats
6. Matching sets and capsule wardrobe collections
7. Heirloom Collection (signature, long-lasting essentials)

### Target locations
Australia-wide. We chose Australia-wide over four cities so the small budget was not spread thin. She had planned a US
test, now moot.

## 4. Audience

- **Primary:** fashion-conscious women seeking premium clothing; shoppers for dresses, tops, skirts, knitwear and sets;
  women wanting polished outfits for occasions and elevated everyday wear.
- **Secondary:** gift shoppers; capsule-wardrobe and investment-piece buyers; luxury apparel fans; international
  shoppers interested in Australian-designed fashion.
- **Exclude:** budget shoppers; fast-fashion / heavy-discount seekers; wholesale/B2B; menswear and kidswear shoppers.
- **Jobs to be done:** look polished and confident at work, events and social occasions with timeless, versatile,
  quality pieces that feel worth the money.
- **Pain points:** hard to find distinctive luxury-looking designs; worry about fabric, fit and finish online; fast
  fashion feels generic; want long-lasting not trendy; need the product to match the photos; hesitation over price,
  sizing, shipping and returns.
- **Negative terms:** kept in Basecamp: https://app.basecamp.com/4839868/buckets/47755688/messages/10010196679
  Recent negatives: gift cards, skorts (approved 6-Oct), off-brand labels.
- **Brand-negative rule (client):** never add a competitor or aspirational brand as a negative without asking her
  first. Alpaca Jumper (removed 18-Sep) and Harris Tapper (removed 22-Sep) were taken out after she objected. We
  defended IE Clothing as a legitimate label.

## 5. Competition & positioning

- Competitive landscape, differentiation, proof points and auction insights: **not in sheet**.
- Competitor research was done in June (per optimization notes); the output is not linked separately.
- Positioning to use: Australian-designed, timeless, refined, quality fabrics, Heirloom Collection.

## 6. Conversions & tracking

- Goal: **Purchase**.
- Setup: purchase imported from GA4. Purchase is Primary. Add to Cart and Begin Checkout stayed Primary with her
  agreement. Page View and View Item moved to Secondary (9-Sep). Inactive "Purchase (Website)" deleted (20-Aug).
- Verified by COD test order **#1017** on 26-Aug-2026 (fired in GA4 Realtime). Tracking Status: **Verified**.
- Caution: because Add to Cart and Begin Checkout are still Primary, the "Conversions" column can overstate sales.
  The client watches this closely. Always report GA4 web purchases separately.
- Attribution disputes:
  - 4-Sep purchase (about $302): client says organic, not paid. No recorded decision on removing it from reports.
  - 5-Oct purchase of A$400 via "Google Shopping App Purchase": client **confirmed it came from Google Ads** (6-Oct).
  - Her Shopify order-level attribution showed no orders from paid Google clicks in Aug to Sep. She tracks blended
    MER herself (about 0.68 in August).

## 7. Campaigns & optimization

- Live now: **Standard Shopping** (launched 3-Jul, A$10/day) and **Demand Gen** (launched 2-Sep, A$20/day). Total
  about A$30/day.
- Paused: Search (paused 2-Sep at client request), Performance Max (on hold; briefly served about A$14 and 1,116
  impressions after the 18-Aug build). Old client-made test PMax was removed/paused in June.
- Demand Gen: static images only, her approved copy, warm remarketing audiences merged into one group (small lists),
  plus a prospecting layer. Gmail is included (re-confirmed 4-Sep; active with impressions and clicks by 5-Oct).
  YouTube off until she supplies video.
- On hold by client ("nothing new added this month", 22-Sep): PMax, video, any new campaign or addition.
- Keyword groups built: Dresses, Tailored Shirting, Outerwear, Knitwear, Skirts.
- Files (one sheet for keywords, assets, working doc):
  https://docs.google.com/spreadsheets/d/1Bf9RgN1TpANQeFFDW1zzss2admBTvTzMcYU1LBF9kBU/edit?gid=391594542#gid=391594542
- Daily work updates and negatives: Basecamp thread https://app.basecamp.com/4839868/buckets/47755688/messages/10010196679
- Full optimization history: `references/history.md`.

## 8. Performance snapshot (1-Aug-2026 to 30-Sep-2026)

| Spend | Impr. | Clicks | CTR | Conv. | CPA | Conv. rate | Qualified leads |
|---|---|---|---|---|---|---|---|
| A$1,838.98 | 72,881 | 1,382 | 1.9% | 11 | A$167.18 | 0.77% (sheet) | not in sheet |

- Computed check: 11 / 1,382 = 0.80% conv. rate (sheet shows 0.0077; small mismatch). CTR and CPA reconcile.
- Revenue, conversion value and ROAS: **not in sheet**. The client wants ROAS, cost per purchase and a Shopping vs
  Demand Gen split. Pull them from Google Ads and GA4 before any report.
- Client view: about A$1.7k spent with almost no purchases; MER about 0.68 (her figure).

## 9. Reporting & meetings

- Format agreed (21-Sep): only her chosen metrics. Spend, clicks, CTR, CPC, GA4 web purchases, revenue / conversion
  value, cost per purchase, ROAS, and the Shopping vs Demand Gen split. No activity metrics (users, page views,
  add-to-carts, engagement) as headline numbers.
- Monthly report: Looker Studio https://datastudio.google.com/reporting/e9216c99-7e5e-4497-993e-f5c568897d81/page/p_hl5e3y5psd
  Monthly date: 18th.
- Weekly reporting date, weekly conversion date, meeting dates: **not in sheet**.
- Channel: **Basecamp**.

## 10. Client relationship

- She is analytical and commercial. She checks Shopify attribution and MER herself. Lead with purchases, revenue
  and ROAS. Never with activity.
- Trust is low. Main reasons: reports felt too optimistic, the slow conversion-tracking fix (Jul to Aug), the PMax
  build against her hold, the Gmail confusion in Demand Gen, brand names added as negatives, and lack of
  proactive negative management.
- What she wants from us: follow instructions exactly, ask before brand negatives, be proactive on bad search terms,
  answer direct questions directly.
- Complaint: "I am making no money with Google." Spend "isn't delivering a return that justifies it."
- Open, unanswered direct questions (from her): notice period, final billing/service date, and whether campaigns
  keep running. Our 28-Sep to 1-Oct replies asked for more time but did not answer these.

### Most recent items
- 27-Sep: notice given. 30-Sep: confirmed contract ends at the end of the cycle (18-Oct).
- 30-Sep: we explained Meta vs Google attribution for a later order.
- 5-Oct: we reported a A$400 purchase via Google Shopping; Gmail shown active with screenshots.
- 6-Oct: she confirmed the A$400 order came from Google Ads and approved "skorts" as a negative. Asked again to
  confirm notice period, final billing date and campaign continuity.

## 11. Open actions & how to move forward (offboarding plan, today is mid-October)

1. **Answer her termination questions now, in one direct Basecamp reply** (draft, then team approval before
   sending). Confirm: service end 18-Oct-2026, final billing date, whether we stop managing at end of day 18-Oct,
   and that campaigns stay live in her account unless she asks us to pause them. Owner: Tamasa. This is overdue.
2. **Do not pause, change budgets or add anything** before 18-Oct without her written instruction (approval gate,
   and she has put new work on hold). Keep Shopping A$10/day + Demand Gen A$20/day running.
3. **Send the Gmail "where ads showed" placement report** (asked twice, promised, not sent).
4. **Final report by 18-Oct** in her format: Aug to Oct, GA4 web purchases, revenue, cost per purchase, ROAS,
   Shopping vs Demand Gen. Mark the 4-Sep (about $302) order as disputed/organic per her statement; count the
   5-Oct A$400 order as confirmed Google Ads. Be factual; do not soften the result.
5. **Handover document**: campaign structure, conversion actions and their primary/secondary status, negative list,
   Merchant Center fixes, GA4/GTM notes, open recommendations (add-to-cart drop-off diagnosis was promised and never
   delivered; include it or say clearly it was not completed).
6. **Access offboarding**: she will remove access from her side (Google Ads, Merchant Center and GA4 are under E.L.S.).
   Offer to unlink the MCC and to transfer or delete the GTM container GTM-M247FXGR and Clarity project xj6m55d75o.
   Close the GTM re-install question (no reply after three asks); do not chase it again.
7. Negatives until the end date: add only clear non-brand junk from search terms; ask her before any brand.
8. After 18-Oct: set Project Stage to "Churned", log the exit, run an internal lessons-learned (reporting format from
   day 1, Purchase-only primary goals, never act against a hold instruction).
9. **Data fixes in the sheet**: the website cell hyperlink points to https://www.cginsurancesb.com/ (another client);
   relink to elevatedluxurystudio.com. Add `ELS` to the Project Index (it is missing). Fix the bidding-strategy
   cell after checking the live account.

## 12. Sheet update reminder

Tab name: `ELS`. Append a log row after every task (Entry Date, Updated By, Entry Type, project name), using the
column rules in `ppc-agency-manager/references/master-sheet-schema.md`. Log the termination reply, final report,
handover and stage change as separate rows.

## Data issues found in the sheet

- `Name of the Project / Website` shows elevatedluxurystudio.com but its hyperlink goes to https://www.cginsurancesb.com/
  (CG Insurance, another client).
- The `ELS` tab is **not in the Project Index**, so portfolio runs miss it.
- Bidding: sheet says Maximize conversion value; notes say Maximise Conversions.
- Stage still "6-Live & Optimizing" although notice is given.
- Same first name "Tarryn" appears for the `kevin els` tab (Kevin Els Architects). Different business, CID and country.
- Dates in this tab use MM.DD.YYYY (06.18.2026, 09.21.2026).
