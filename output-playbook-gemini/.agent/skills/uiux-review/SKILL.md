---
name: UI/UX Review with Scoring
description: Design audit scoring accessibility, consistency, trust signals, and usability via Figma links or screenshots.
model: claude-haiku-4
lifecycle_stage: "4. Prototyping & Testing"
tools: Figma MCP (get_design_context, get_metadata, get_screenshot, get_variable_defs), Playwright MCP
parallel: true
parallel_strategy: "3 specialist agents — UX Conversion (Trust Signals + CTA Clarity), Info & Mobile Architect (Info Architecture + Mobile Responsiveness), Accessibility & SEO Engineer (Accessibility + cross-cutting SEO Impact Check). Merge agent combines scores into unified scorecard."
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Customer Journey Stages
| # | Stage | User Goal | UI Implication |
|---|---|---|---|
| 1 | Inspiration | Discover activities | Hero imagery, curated sections, editorial content |
| 2 | Research | Compare options, read reviews | Search/filter, listing cards, review display |
| 3 | Evaluation | Trust audit | Badges, social proof, cancellation policy, "is this legit?" signals |
| 4 | Booking | Complete transaction | CTA clarity, payment methods, price transparency, guest checkout |
| 5 | Pre-Experience | Logistics & reassurance | Confirmation details, maps, operator contact, reminders |
| 6 | Post-Experience | Review & return | Review prompts, loyalty hooks, referral flows |

### Trust Signal Checklist (must be visible on relevant pages)
| Signal | Where Expected | Priority |
|---|---|---|
| Free Cancellation Badge | Listing card + detail page + checkout | P0 |
| Locally Curated / Verified Badge | Listing card + detail page | P1 |
| Star Rating + Review Count | Listing card + detail page | P1 |
| Social Proof Counter ("X booked") | Homepage + listing detail | P1 |
| Review Nationality Flags | Detail page (when shipped) | P2 |
| Operator Verification Badge | Detail page | P2 |

### Primary Persona
- **Who**: Foreign leisure traveler (India, China, South Korea, Australia), age 28–42
- **Device**: Mobile-first (375px primary viewport)
- **Core anxiety**: "Is this platform safe? Will my money be protected?"

### Reviewer Persona (3 specialist perspectives)
| Perspective | Expertise | Evaluates |
|---|---|---|
| **UX Conversion Specialist** | Baymard checkout research, NNG mobile patterns, Fitts's Law, OTA trust patterns (Klook/GYG/Booking.com) | Trust Signals, CTA Clarity |
| **Information & Mobile Architect** | Nielsen heuristics, progressive disclosure, Core Web Vitals, Material Design / Apple HIG targets | Info Architecture, Mobile Responsiveness |
| **Accessibility & SEO Engineer** | WCAG 2.1 AA, semantic HTML, Schema.org structured data, image optimization | Accessibility + cross-cutting SEO impact |

### Design Standards Reference
| Standard | Used In | Key Threshold |
|---|---|---|
| Baymard Institute | Trust Signals | Trust signals before fold; single primary CTA |
| NNG F-pattern / thumb zone | CTA Clarity | Primary action in F-pattern hotspot or thumb zone |
| Fitts's Law | CTA Clarity | Larger + closer targets = faster click/tap |
| Nielsen heuristic #2, #6 | Info Architecture | Match real world; recognition over recall |
| Core Web Vitals | Mobile + SEO | LCP < 2.5s, CLS < 0.1, INP < 200ms |
| Material Design / Apple HIG | Mobile | Touch targets ≥ 48dp / 44pt |
| WCAG 2.1 AA | Accessibility | Contrast ≥ 4.5:1, focus visible, ARIA landmarks |
| Schema.org | SEO Impact | TourTrip, Event, AggregateRating for rich snippets |

### Figma MCP Tools (read-only, official server)
| Tool | What It Returns |
|---|---|
| `get_metadata` | Sparse XML — layer IDs, names, types, positions, sizes (lightweight structural data) |
| `get_screenshot` | Screenshot of the selected frame/layer (preserves visual layout fidelity) |
| `get_variable_defs` | Design tokens — colors, spacing, typography values and names |
| `get_design_context` | Code-ready design context (React+Tailwind default, configurable to Vue/HTML+CSS) |

### Approved Design Tools
Figma only. No Sketch, no Adobe XD.

---

## Purpose

Provides structured design review by scoring UI designs via Figma links or screenshots against UX standards and customer journey requirements. Catches trust signal gaps, accessibility issues, and consistency problems before engineering builds the wrong thing.

Supports two input paths: **Figma link** (preferred — provides structural data + visual + design tokens) and **screenshots** (fallback — for live site audits or teams without Figma MCP). Uses Claude Haiku 4 for vision analysis.

## Input

- **Figma file link** (preferred) — URL to a Figma frame or page; agent extracts metadata, screenshot, and design tokens via Figma MCP automatically
- **Screenshots** (fallback) — PNG/JPG for teams without Figma MCP, or for auditing the live site vs. design
- **Context** — Which journey stage and initiative this UI belongs to
- **Device target** — Desktop, mobile, or both

## Output

- **Design scorecard** (markdown) with:
  - Score per dimension (0–10 scale, 5 dimensions)
  - Total score (0–50)
  - Pass/Fail recommendation (Pass ≥ 35, Conditional 25–34, Fail < 25)
  - Annotated feedback per dimension with specific UI element references
  - SEO Impact Notes for any dimension scoring below 6
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

## Process

1. **Load** — Determine input type:
   - If Figma link provided → call `get_metadata` for structural data (component tree, sizes, positions), `get_screenshot` for visual snapshot, and `get_variable_defs` for design tokens (colors, spacing, typography)
   - If screenshots provided → use directly for vision analysis
   - If BOTH provided → use Figma data for structural scoring (Information Architecture, Mobile Responsiveness, Accessibility) and screenshots for visual scoring (Trust Signals, CTA Clarity)
2. **Identify context** — Determine which journey stage and initiative this UI supports
3. **Score** — Dispatch 3 specialist agents in parallel (see Parallel Execution below), each scoring their assigned dimensions on 0–10 scale:

| Dimension | Weight | What to Check |
|---|---|---|
| **Trust Signals** | 25% | Cancellation badge visible? Social proof counter? Verified badge? Review ratings? (Use Trust Signal Checklist above.) Baymard: trust signals before fold reduces abandonment ~35%. Benchmark: Klook shows badges on every listing card. |
| **CTA Clarity** | 20% | Primary action obvious? One CTA per viewport? Action verb label? Fitts's Law: primary CTA in thumb zone on mobile. NNG: action verbs outperform generic labels. |
| **Information Architecture** | 20% | Pricing transparent (all-inclusive)? Essential details visible without scrolling? Nielsen #2: pricing must match user's mental model. Schema.org: check for TourTrip/Event structured data. |
| **Mobile Responsiveness** | 20% | Layout works at 375px? Tap targets ≥ 44pt (Apple HIG) / 48dp (Material)? Text readable without zooming? Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms. |
| **Accessibility** | 15% | Color contrast ≥ 4.5:1? Alt text? Keyboard navigable? WCAG 2.1 AA. Semantic HTML: single H1, logical heading hierarchy, ARIA landmarks. Screen reader: logical tab order. |

4. **SEO Impact Check** — For each dimension scored below 6, note the SEO consequence:
   - Trust Signals < 6 → missing AggregateRating structured data hurts rich snippets
   - CTA Clarity < 6 → CLS from layout shifts may trigger ranking penalty
   - Info Architecture < 6 → missing Schema.org TourTrip/Event; poor heading hierarchy hurts crawlability
   - Mobile < 6 → Core Web Vitals failure directly impacts Google mobile ranking
   - Accessibility < 6 → missing alt text hurts image search; no semantic HTML hurts crawlability
5. **Benchmark** — Compare against competitor UX (Klook, KKday, GYG) if screenshots are available
6. **Report** — Generate scorecard with actionable design-specific feedback + SEO Impact Notes

## Parallel Execution

3 specialist agents run concurrently, each scoring their assigned dimensions:

| Agent | Persona | Dimensions Scored | Standards Applied |
|---|---|---|---|
| **Agent 1: UX Conversion** | UX Conversion Specialist | Trust Signals (25%), CTA Clarity (20%) | Baymard Institute, NNG F-pattern, Fitts's Law |
| **Agent 2: Info & Mobile** | Information & Mobile Architect | Info Architecture (20%), Mobile Responsiveness (20%) | Nielsen heuristics, Core Web Vitals, Material Design / Apple HIG |
| **Agent 3: Accessibility & SEO** | Accessibility & SEO Engineer | Accessibility (15%) + cross-cutting SEO Impact Check | WCAG 2.1 AA, Schema.org, semantic HTML |

**Merge step**: A coordinator combines the 3 agent outputs into a single scorecard, resolves any cross-dimension conflicts (e.g., badge placement noted by both Agent 1 and Agent 2), calculates the total score, and generates the Priority Fixes list ordered by impact.

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Trust signals scoring MUST reference the specific items from the Trust Signal Checklist (see Embedded Context)
- Do NOT suggest tools outside the approved stack — e.g., no Sketch, no Adobe XD
- Use Claude Haiku 4 for this skill (vision-optimized, fast structured responses)
- Mobile review is mandatory — if only desktop screenshot is provided, flag mobile review as incomplete

## How to Use

1. Get the Figma frame link (right-click frame → "Copy link") OR take screenshots at mobile (375px) and desktop (1280px)
2. Open Claude Code in any directory (Figma MCP must be connected for link path)
3. Say: `Use the uiux-review skill to score this [page name]. Figma: [link]. This is for [initiative name] at the [journey stage] stage.`
   — OR attach screenshots if not using Figma MCP
4. Review the scorecard with your designer — prioritize dimensions scoring below 6

## Example

**Input**: Screenshot of listing detail page (mobile), Initiative: Free Cancellation Badge (#1, P0)

**Expected Output** (excerpt):

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## UI/UX Scorecard: Listing Detail Page (Mobile)
**Initiative**: Free Cancellation Badge (#1, P0) · **Journey Stage**: Evaluation/Booking

| Dimension | Score | Feedback |
|---|---|---|
| Trust Signals | 4/10 | ❌ Cancellation badge is present but placed below the fold — Baymard research shows above-fold trust signals reduce abandonment ~35%. Social proof counter missing. Klook shows both on every listing. |
| CTA Clarity | 7/10 | ✅ "Book Now" is prominent with action verb. ⚠️ "Add to Wishlist" competes — Fitts's Law: reduce secondary CTA visual weight so primary is the obvious target. |
| Information Architecture | 6/10 | ⚠️ Price shows base only — add-ons at checkout violate Nielsen #2 (match real world). Meeting point in collapsed accordion breaks progressive disclosure. Missing Schema.org TourTrip markup. |
| Mobile Responsiveness | 8/10 | ✅ Layout works at 375px. Tap targets meet Apple HIG 44pt. ⚠️ Image carousel swipe indicator barely visible — CLS risk if images load late. |
| Accessibility | 5/10 | ❌ Price text contrast 3.2:1 (WCAG AA requires ≥ 4.5:1). Badge icon has no alt text — hurts image search. No ARIA landmarks on page sections. |

### Total: 30/50 — ⚠️ CONDITIONAL PASS

### Priority Fixes
1. Move cancellation badge above the fold (Trust Signals — Baymard)
2. Fix price text contrast to ≥ 4.5:1 (Accessibility — WCAG AA)
3. Show all-inclusive price on listing (Info Architecture — Nielsen #2)

### SEO Impact Notes
- Trust Signals (4/10): No AggregateRating structured data → no star rating rich snippet in Google search
- Info Architecture (6/10): Missing Schema.org TourTrip markup → invisible to Google's activity carousel
- Accessibility (5/10): Badge images lack alt text → missed image search traffic; no heading hierarchy → poor crawlability
```
