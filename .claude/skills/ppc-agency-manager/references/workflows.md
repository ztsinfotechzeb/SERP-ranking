# Project Stage SOPs

Each stage ends with a Master Sheet update: set `Project Stage`, log a row, set `Next Action Plan`.

## Stage 1: New project and questionnaire

- [ ] Create project tab from `_TEMPLATE`, add the name to `Project Index`.
- [ ] Fill Row 5: project/website, platform, responsible employee, client name, payment mode, package,
      start date, monthly date, confirmation received date, monthly & daily budget, reporting dates,
      meeting frequency.
- [ ] Send welcome email + service questionnaire (`questionnaire.md`, template in `client-communication.md`).
- [ ] While waiting: audit the website, GBP and the top 5 SERP competitors so the kick-off call is informed.
- [ ] When answers arrive: fill Business Overview, Services, Locations, Audience (primary, secondary,
      excluded, negative terms, jobs to be done, use cases, pain points), Competition, Differentiation,
      Proof Points, Conversion Goal. Flag any gaps and ask the client in ONE consolidated message.

## Stage 2: Access

| Access | How to request / guide |
|---|---|
| Google Ads | Send MCC link request from the agency MCC to the client CID; client accepts in Admin > Access & security > Managers. No account: guide creation (skip-campaign expert mode), billing added by client. |
| Meta | Client adds agency Business Manager as partner (Business settings > Partners) for ad account, Page, Pixel/dataset, Instagram. |
| GA4 | Editor/Admin on the property to the agency email. |
| GTM | Publish access to the container. |
| GBP | Manager role. |
| GSC | Full user. |
| Merchant Center | Admin (ecommerce only). Link to Google Ads. |
| Microsoft Clarity | Team member or create project + install via GTM. |
| CRM / CMS | Dedicated user login for the agency (never the client's own password). Store in the vault. |

- [ ] Record each access + status in its column. Chase missing access every 2 business days, max 3 reminders,
      then escalate to the team member / meeting.
- [ ] Link Google Ads with GA4, GMC, GBP (location assets), and YouTube if used.

## Stage 3: Keyword research (service-cluster wise)

- [ ] One cluster per service / intent (e.g. "End of tenancy cleaning", "Office cleaning").
- [ ] Per keyword: cluster, keyword, match type, monthly volume, CPC range (low/high), competition, intent
      (transactional / commercial / info), priority, target landing page.
- [ ] Seed from: questionnaire, website pages, competitor ads & pages, GSC queries, Keyword Planner, OpenSEO.
- [ ] Build the starter negative list: jobs/careers, free, DIY/how to, training/course, wholesale (if not
      relevant), competitor brands (unless approved), out-of-area locations, excluded services.
- [ ] Budget check: estimated clicks/day = daily budget ÷ avg CPC. If fewer than ~10 clicks/day for a cluster,
      recommend fewer clusters or more budget.
- [ ] Save in the Keyword File, send for approval, log `Keyword Research / Clusters Status`.

## Stage 4: Ad assets

- [ ] RSA per ad group, all extensions/assets (sitelinks ×4+, callouts ×4+, structured snippets, call, location,
      image, logo, business name, lead form if useful, price, promotion).
- [ ] PMax/Demand Gen asset groups, Meta creatives if in scope (see SKILL.md §5 for specs).
- [ ] Image/video briefs or generated creatives saved in Media Doc.
- [ ] Policy check (claims, trademarks, special categories). Send for approval; log `Ad Assets Status`.

## Stage 5: Campaign build and conversion tracking

- [ ] Structure: brand vs non-brand separated; one campaign per budget priority; ad groups = clusters.
- [ ] Settings: locations "Presence" only, schedule by business hours if calls, networks (no Display on
      Search unless planned), language, audiences in observation, account-level negatives, brand exclusions.
- [ ] Bidding: new accounts start with Maximize Clicks (with CPC cap) or Maximize Conversions; move to tCPA/tROAS
      after ~30 conversions in 30 days.
- [ ] Tracking (choose what applies): GTM + GA4 events, Google Ads conversion tag + conversion linker,
      enhanced conversions, form submit (thank-you page or event), click-to-call + call from ads (≥60s),
      WhatsApp click, Meta Pixel + Conversions API, CRM offline conversion import where possible.
- [ ] Mark primary vs secondary conversions. Test every action (Tag Assistant / Meta Events Manager test events).
- [ ] Fill `Current Conversion Tracking Set Up Details`, `Tracking Status` = Verified.
- [ ] Get launch approval → enable → log `Campaign Build`, set Stage 6.

## Stage 6: Live and optimizing

Follow `optimization-playbook.md` and the cadence in SKILL.md §3. Strategy changes (new campaign types,
budget shifts, new landing page) are proposals: data → recommendation → client approval → implement → log.

### Landing page / CRO / Quality Score
- Compare client landing page vs top 3 competitor pages: headline-keyword match, above-the-fold CTA, phone,
  form length, trust (reviews, badges), speed (PageSpeed mobile), mobile UX, offer.
- Use Clarity heatmaps/recordings for drop-off.
- If QS ≤5 on key keywords due to landing page experience: recommend page edits, or a dedicated lead-gen
  page (hero with service+location, form above fold, USPs, proof, FAQ, sticky call/WhatsApp button).
  Provide wireframe + copy; log under `Landing Page / CRO Notes`.

### Competitor review (monthly)
- Auction insights (IS, overlap, outranking, top-of-page rate) vs last month.
- Google Ads Transparency Center + Meta Ad Library for competitor copy, offers, formats.
- Log under `Auction Insights / Competitor Ads Notes` and `Competitive Landscape` (Row 5).
