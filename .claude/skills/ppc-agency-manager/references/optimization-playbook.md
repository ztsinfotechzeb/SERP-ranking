# Optimization Playbook

Always compare against the project's `Conversion Goal` (target CPL / ROAS) and budget in Row 5.
Only count primary conversions for bidding decisions.

## Daily health check (every live project, 5–10 min)

1. Spend yesterday vs daily budget (flag >120% or <70%). Month-to-date pacing vs monthly budget.
2. Conversions yesterday; zero conversions for 3+ days on a normally converting account = check tracking first.
3. Disapproved ads / assets, limited-by-policy, billing issues, account suspension.
4. Tracking alive: conversion actions status "Recording", GA4 realtime, Meta events received.
5. Big swings (CPC, CTR, CPA ±30% vs 7-day avg) → investigate cause.
6. Search terms (last 1–3 days): add irrelevant terms as negatives; add converting/relevant new terms as keywords.
7. Log a "Daily Update" row and draft the daily brief (reporting.md).

### Negative keyword rules
- Add as phrase match by default; exact for single ambiguous words; broad only for clearly irrelevant words
  (e.g. "jobs", "free", "salary").
- Level: account list for universal negatives; campaign level for cross-campaign sculpting; ad group level
  to route queries.
- Never block a term that converted in the last 90 days. Check against the approved keyword list first.
- Also check the client's `Negative Terms That Exclude` and `Excluded Audiences` columns.

## Weekly (before the weekly report)

- Keywords: pause spend > 2× target CPA with 0 conv (30 days); raise bids/priority on converting keywords
  losing IS to rank.
- Ads: RSA ad strength, asset performance labels; replace "Low" assets; test one new message per ad group.
- Budgets: shift toward campaigns with the best CPA and budget-limited IS loss (proposal if above threshold).
- Device, location, hour/day performance: adjust or propose bid adjustments/exclusions.
- Audiences: observation audience performance; add exclusions.
- PMax: search-term insights, brand exclusions, asset group performance, placement exclusions.
- Meta: frequency (>3 on prospecting = refresh creative), CPM/CTR trends, learning phase status, placement
  breakdown, lead quality from CRM, audience overlap.
- Lead quality: compare platform conversions vs client-confirmed qualified leads (Conversion report).

## Monthly

- Auction insights and competitor ads review; landing page / CRO audit; QS review.
- Bid strategy review (move to tCPA/tROAS when ≥30 conv/30 days; adjust targets ±10–15% max per change).
- Account structure clean-up, new campaign/test proposals (Demand Gen, PMax, remarketing, new services).
- Refresh Row 5 rolling summaries and risk status.

## Troubleshooting quick map

| Symptom | Check in this order |
|---|---|
| Conversions dropped to 0 | Tag firing, site changes/form broken, GTM publish, consent mode, conversion action status |
| CPA up, CTR stable | Landing page / site issue, lead form, conv rate by device, competitor offers |
| CTR down | New competitors (auction insights), ad disapprovals, ad relevance, impression share on top |
| Spend not delivering | Budget/bid too low, bid strategy learning, keyword volume, disapprovals, billing |
| Leads poor quality | Search terms, location "presence", placements (PMax/Display), form spam (add captcha/qualifying question), Meta: switch to higher-intent form |

## Change safety
- One major change per campaign per week so the effect can be measured. Note each change in the log with the
  reason and expected impact, and review it after 7–14 days.
- Budget/bid-strategy changes above ±20%, new campaigns, pausing campaigns: team approval first (SKILL.md §0).
