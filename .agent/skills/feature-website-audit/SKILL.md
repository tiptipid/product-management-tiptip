---
name: Feature & Website Audit
description: Periodic automated UX audit of the live site against customer journey criteria and trust signal checklist using Playwright browser automation.
model: claude-haiku-4
lifecycle_stage: "5–6. Execution & Post-Launch"
tools: Playwright MCP, Atlassian MCP
parallel: false  # Playwright browser sessions are sequential by nature — each page navigation depends on the previous state. Parallelizing would require separate browser instances with duplicated setup cost.
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Customer Journey — Audit Flow
The audit follows the user's natural journey through the site:
| Step | Page Type | Journey Stage | What to Verify |
|---|---|---|---|
| 1 | Homepage | Inspiration | Search bar, curated content, social proof, trust signals |
| 2 | Search Results | Research | Query relevance, filters, listing card completeness |
| 3 | Listing Detail | Evaluation | Trust signals, pricing, CTA, essential info, images |
| 4 | Checkout | Booking | Guest checkout, payment methods, price transparency, cancellation policy |
| 5 | Confirmation | Pre-Experience | Booking details, logistics, operator contact |

### Trust Signal Checklist
| Signal | Expected Location | Status Check |
|---|---|---|
| Free Cancellation Badge | Listing card + detail page + checkout | Visible above the fold? |
| Locally Curated / Verified Badge | Listing card + detail page | Present and prominent? |
| Star Rating + Review Count | Listing card + detail page | Data populated? |
| Social Proof Counter | Homepage + listing detail | Showing real numbers? |
| All-Inclusive Price | Listing card + detail page | No hidden fees at checkout? |

### Primary Persona
- **Who**: Foreign leisure traveler, age 28–42, mobile-first
- **Viewports**: Mobile = 375px, Desktop = 1280px
- **Core anxiety**: "Is this platform safe? Will my money be protected?"

---

## Purpose

Runs a structured UX audit of the live site to catch regressions, broken flows, and missing trust signals. Compares the current live state against the expected state defined in the journey flow and trust signal checklist. Designed to run weekly as a recurring check.

## Input

- **Target URL** — Production URL (or staging URL for pre-release audit)
- **Audit scope** — Full journey (all 5 page types) or specific page type (homepage, search, listing, checkout)
- **Previous audit report** — (optional) For diff comparison to identify new regressions
- **Specific initiative** — (optional) Check if a recently shipped feature is live and functioning

## Output

- **Audit report** (markdown) with:
  - Page-by-page checklist results
  - Regression alerts (items that were passing but now fail)
  - Trust signal completeness per page type
  - Performance observations (load time, broken images, dead links)
  - Screenshots captured via Playwright for evidence
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

## Process

1. **Navigate** — Use Playwright MCP to browse through the key user journey pages:
   - Homepage → Search results → Listing detail → Checkout → Confirmation
2. **Capture** — Take screenshots at each step for visual review
3. **Check** — For each page, verify the following checklists:

### Homepage Checklist
- [ ] Search bar visible above the fold
- [ ] Popular/curated activities displayed
- [ ] Trust signals: review count, booking count, or social proof visible
- [ ] Mobile: CTA and navigation accessible

### Search Results Checklist
- [ ] Results match query intent
- [ ] Filters functional (category, price, date)
- [ ] Each listing card shows: image, title, price, rating, cancellation badge
- [ ] No broken images or missing data

### Listing Detail Checklist
- [ ] Trust signals: Free Cancellation Badge, ratings, review count, Verified/Curated badge
- [ ] All-inclusive price visible (no hidden fees)
- [ ] CTA "Book Now" above the fold on mobile
- [ ] Essential details: date picker, meeting point, duration, what's included
- [ ] Image gallery functional with ≥3 photos

### Checkout Checklist
- [ ] Guest checkout / SSO available (when shipped)
- [ ] Payment methods visible and functional
- [ ] Price breakdown transparent
- [ ] Cancellation policy visible at checkout
- [ ] Form validation working (error messages visible)

4. **Compare** — Against previous audit to identify regressions
5. **Report** — Generate audit report with pass/fail per item, screenshots, and remediation priority

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Use Playwright MCP for all browser interactions — do not use external browser automation tools
- Audit must test at mobile viewport (375px) in addition to desktop (1280px)
- Use Claude Haiku 4 for vision analysis of captured screenshots
- Do not test with real payment credentials — stop at payment method selection
- Screenshots must be stored locally, not uploaded externally

## How to Use

1. Ensure Playwright MCP is connected in your Claude Code session
2. Say: `Use the feature-website-audit skill to run a full UX audit of [site URL]. Compare against last week's report.`
3. For a targeted audit: `Use the feature-website-audit skill to verify that Free Cancellation Badge is live on listing detail pages.`
4. Review the report with your designer and engineering PIC — file Jira tickets for regressions

## Example

**Input**: Full audit of the production site (mobile viewport)

**Expected Output** (excerpt):

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## Website Audit Report — March 25, 2026 (Mobile)

### Listing Detail Page: "Mount Batur Sunrise Trek"

| Check | Status | Notes |
|---|---|---|
| Free Cancellation Badge | ✅ Pass | Visible below price, above the fold |
| Star rating | ✅ Pass | 4.7/5 (128 reviews) displayed |
| Social Proof Counter | ❌ Fail | Not yet shipped |
| All-inclusive price | ⚠️ Partial | Base price shown; service fee appears at checkout only |
| CTA above fold | ✅ Pass | "Book Now" in sticky bottom bar |
| Meeting point | ❌ Fail | Hidden in collapsed accordion — requires 2 taps to see |

### Regressions Since Last Audit
- 🔴 **NEW**: Meeting point accordion collapsed by default — was expanded last week. Check if intentional design change.

### Summary
- Pages audited: 5
- Total checks: 32
- Pass: 24 (75%)
- Fail: 5 (16%)
- Partial: 3 (9%)
```
