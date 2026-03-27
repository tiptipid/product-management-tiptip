---
name: Competitor Benchmarking
description: Monitors Klook, KKday, GetYourGuide, and Trip.com for feature changes, pricing shifts, and UX updates in the activities vertical.
model: gemini-2.5-flash
lifecycle_stage: "1–2. Discovery & Ideation"
tools: Brave Search MCP, Playwright MCP, Atlassian MCP
parallel: true
parallel_strategy: "4 agents, one per competitor (Klook, KKday, GetYourGuide, Trip.com). Each agent scans + browses its assigned competitor. Parent merges digests, deduplicates cross-competitor patterns, and generates Kano reclassification recommendations."
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Kano Classification
| Type | If Present | If Absent | Example |
|---|---|---|---|
| **Basic** | No reaction — expected | Angry, leaves platform | Free cancel badge, SSO, upfront pricing |
| **Performance** | Satisfied — more is better | Mildly disappointed | Review count, search quality, pre-activity emails |
| **Delight** | Wow — unexpected value | No reaction | Loyalty credits, WhatsApp booking, AI recs |

**Kano Shift Rule**: When 2+ competitors ship a feature, it shifts from Performance → Basic. When all competitors have it, it is definitively Basic.

### Prioritization Reference
- **ICE Score** = Impact × Confidence × Ease (each 1–10, max 1,000)
- **Priority**: P0 ≥ 700, P1 350–699, P2 150–349, P3 < 150
- **Effort**: XS < 1d, S ~1wk, M 2–3wk, L 4–6wk, XL 6+wk

### Default Competitors
| Competitor | Vertical | Strategic Stance |
|---|---|---|
| **Klook** | Activities OTA | Learn from — adopt loyalty, free-cancel hero |
| **KKday** | Activities OTA | Differentiate — out-authenticate their "local" pitch |
| **GetYourGuide (GYG)** | Activities OTA | Learn from — replicate Certified badge, Pay Later, auto-currency |
| **Trip.com** | Multi-vertical OTA | Niche target — focus on markets where Trip.com is weakest |

### UX Benchmark Dimensions
| Criterion | Description |
|---|---|
| Catalog Depth | Number and variety of Bali activities |
| Search & Filter | Autocomplete, price/date/category filters |
| Booking Flow | Guest checkout, payment methods, form UX |
| Trust Signals | Badges, reviews, verification, cancellation policy |
| Localization | Language, currency, payment method support |
| Mobile UX | Responsive design, tap targets, load speed |
| Social Proof | Review counts, booking counts, user-generated content |
| Price Transparency | All-inclusive pricing, fee disclosure |

---

## Purpose

Provides structured competitive intelligence by monitoring OTA competitors in the activities/experiences vertical. Outputs a weekly digest of changes that the PM can use to update Kano classifications — if a competitor ships a feature we lack, that feature may shift from Performance to Basic.

## Input

- **Competitor list** — Default: Klook, KKday, GetYourGuide (GYG), Trip.com
- **Focus areas** — (optional) Specific aspects to monitor: pricing, checkout UX, trust signals, search/filter, mobile experience, new markets
- **Previous report** — (optional) Last benchmarking report for diff comparison

## Output

- **Weekly Competitor Digest** (markdown) with:
  - Change log per competitor (new features, removed features, pricing changes, UX changes)
  - Kano impact assessment: Does this change shift any backlog item's classification?
  - Screenshot evidence (if using Playwright MCP for automated browsing)
  - Recommended actions for backlog
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

## Process

1. **Scan** — Use Brave Search MCP to search for recent news, blog posts, and changelogs for each competitor
2. **Browse** — Use Playwright MCP to visit competitor sites and capture current state of key pages (homepage, search results, listing detail, checkout)
3. **Compare** — Against previous report (if available), identify what has changed
4. **Classify** — For each change:
   - Is this a feature we already have? (Parity)
   - Is this a feature we lack? (Gap — check if in known backlog)
   - Does this shift any Kano classification? (Apply Kano Shift Rule above)
5. **Assess** — Rate competitive threat: Low (nice-to-have), Medium (should address), High (urgent gap)
6. **Report** — Generate digest with actionable recommendations

## Parallel Execution

Each competitor can be scanned independently:

**Per-competitor agent** (4 agents):
- Each receives: ONE competitor name + focus areas + previous report (if any)
- Runs steps 1–2 (Scan + Browse) for its assigned competitor
- Classifies changes found (step 4)
- Returns: competitor-level change log with Kano impact assessment

**Parent agent**:
1. Dispatches 4 competitor agents in parallel
2. Collects per-competitor results
3. Identifies cross-competitor patterns (e.g., "3 of 4 competitors now have Apple Pay" → Kano shift to Basic)
4. Generates consolidated digest with Kano reclassification recommendations
5. Adds threat-level rating per change

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Only analyze competitors in the activities/experiences vertical — ignore hotel/flight features
- Kano reclassification suggestions must reference the specific initiative by name and its current classification
- Use Gemini 2.5 Flash for speed (this is a recurring, high-frequency task)
- Screenshots captured via Playwright must be stored locally, not uploaded to external services

## How to Use

1. Open Claude Code or Gemini in any directory
2. Say: `Use the competitor-benchmarking skill to generate this week's competitor digest. Focus on [optional: checkout UX / trust signals / pricing].`
3. If you want automated browsing, ensure Playwright MCP is connected
4. Review the digest, validate Kano reclassification suggestions, and update your backlog accordingly

## Example

**Input**: Weekly scan, focus on trust signals

**Expected Output** (excerpt):

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## Competitor Digest — Week of March 24, 2026

### Klook
- 🆕 **Added "Free Cancellation" filter** to search results — users can filter activities by cancellation policy
  - Kano Impact: We have Free Cancellation Badge (#1, P0) but NO filter. Consider adding filter as follow-up.
- 🔄 **Updated review display** — now shows "Verified Booking" tag next to reviews
  - Kano Impact: Shifts External Review Import (#19, P2) from Performance → Basic if 2+ competitors adopt this

### GetYourGuide
- 🆕 **Apple Pay added** to mobile checkout
  - Kano Impact: Google Pay + Apple Pay (#21, P2) — GYG adoption reinforces this as Basic

### Cross-Competitor Pattern
- 🔴 **3 of 4 competitors now offer free cancellation filtering** → Kano shift: Free Cancel Filter is now Basic (not yet in backlog — recommend adding)
```
