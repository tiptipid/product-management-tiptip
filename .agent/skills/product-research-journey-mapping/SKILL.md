---
name: Product Research & Journey Mapping
description: Analyzes support tickets, user feedback, and market data to identify themes, pain points, and opportunities mapped to the customer journey.
model: gemini-2.5-pro
lifecycle_stage: "1. Discovery & Research"
tools: NotebookLM MCP, Brave Search MCP, Atlassian MCP, Sequential Thinking MCP
parallel: true
parallel_strategy: "Up to 6 agents by journey stage — each agent categorizes and clusters tickets for one stage (Inspiration, Research, Evaluation, Booking, Pre-Experience, Post-Experience). Parent merges results, deduplicates cross-stage themes, and generates final report."
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Customer Journey — 6 Stages
| # | Stage | User Goal | Key Anxiety | Touchpoints |
|---|---|---|---|---|
| 1 | **Inspiration** | Discover Bali activities | "What should I do?" | Instagram, TikTok, YouTube, Google Search, friends |
| 2 | **Research** | Compare platforms, read reviews | "Which platform is trustworthy?" | Google Search, Klook/GYG, TripAdvisor, travel blogs |
| 3 | **Evaluation** | Trust audit, credibility check | "Is this site safe? Is it legit?" | Direct site visit, app store ratings, "is X legit?" searches |
| 4 | **Booking** | Complete transaction | "Can I cancel? Can I pay my way?" | Listing page, checkout, payment gateway, confirmation email |
| 5 | **Pre-Experience** | Logistics & reassurance | "Where do I go? What do I bring?" | Confirmation email, WhatsApp, Google Maps, app |
| 6 | **Post-Experience** | Review, repeat, refer | "Was it worth it? Would I return?" | Review email, Instagram/TikTok, WhatsApp groups |

### Dependency Pillars
| Pillar | Core Question | Priority Order |
|---|---|---|
| **Trust** | "Will the visitor believe this is safe?" | Fix first |
| **Conversion** | "Can the visitor complete the booking?" | Fix second |
| **Discovery** | "Can the visitor find the right experience?" | Fix third |

### Prioritization Reference
- **ICE Score** = Impact × Confidence × Ease (each 1–10, max 1,000)
- **Kano**: Basic (must-have), Performance (more-is-better), Delight (unexpected wow)
- **Priority**: P0 ≥ 700, P1 350–699, P2 150–349, P3 < 150

### Approved Tool Stack
Design: Figma. Analytics: OpenPanel + GA4. AI: Claude Code, Gemini CLI. No Sketch, Adobe XD, Mixpanel, Amplitude.

---

## Purpose

Automates the discovery phase by analyzing unstructured user data (support tickets, reviews, interview notes) and producing a structured research report. The output maps findings to journey stages and dependency pillars, enabling the PM to quickly identify which funnel stage has the most friction and which pillar needs attention.

## Input

- **Support tickets** — CSV or text export from support tool (minimum 50 tickets for meaningful patterns)
- **User reviews** — App store reviews, Google reviews, or TripAdvisor/social media mentions
- **Competitor data** — (optional) Screenshots or URLs of competitor features to benchmark against
- **Scope filter** — (optional) Limit analysis to a specific journey stage or pillar

## Output

- **Themes report** (markdown) with:
  - Top 10 themes ranked by frequency
  - Each theme mapped to: Journey Stage, Dependency Pillar, Severity (Blocking/Frustrating/Minor)
  - Frequency count and representative quotes per theme
  - Recommended actions tied to existing backlog items where applicable
- **Opportunity matrix** — 2×2 showing Frequency vs. Severity with theme placement
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

## Process

1. **Ingest** — Load all input data into context. If using NotebookLM MCP, create a notebook with the source files.
2. **Categorize** — For each ticket/review, classify:
   - Journey stage: Inspiration → Research → Evaluation → Booking → Pre-Experience → Post-Experience (use the stage definitions in Embedded Context)
   - Dependency Pillar: Trust / Conversion / Discovery (use pillar definitions above)
   - Severity: Blocking (user cannot proceed), Frustrating (user can proceed with friction), Minor (cosmetic/preference)
3. **Cluster** — Group classified items into themes (e.g., "Payment method confusion", "Missing cancellation info", "Search returns irrelevant results")
4. **Rank** — Sort themes by: (1) frequency, (2) severity weight (Blocking=3, Frustrating=2, Minor=1), (3) pillar priority (Trust > Conversion > Discovery)
5. **Cross-reference** — If the user provides backlog data, check each theme against known initiatives. Note the initiative name, ICE score, and current status.
6. **Report** — Generate the structured output following the format above

## Parallel Execution

When analyzing large datasets (200+ tickets), split by journey stage:

**Per-stage agent** (up to 6 agents):
- Each agent receives: all tickets + the definition of ONE journey stage
- Classifies tickets belonging to that stage → clusters into themes → ranks by severity
- Returns: stage-level themes with frequency, severity, pillar, and quotes

**Parent agent**:
1. Dispatches stage agents in parallel
2. Collects stage-level results
3. Deduplicates cross-stage themes (a ticket mentioning both "search" and "trust" may appear in multiple stages)
4. Merges into a single ranked report
5. Generates the opportunity matrix

**When NOT to parallelize**: If dataset is < 100 tickets or user specified a single-stage scope filter, run sequentially.

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Do NOT invent user quotes — only use direct text from the input data
- Do NOT recommend tools outside the approved stack (see Embedded Context)
- Severity classification must be falsifiable — provide the specific user action that was blocked or degraded
- Use Gemini 2.5 Pro for this skill (large context window needed for 200+ tickets)

## How to Use

1. Export support tickets or user feedback into a CSV or text file
2. Open Claude Code or Gemini in any directory
3. Say: `Use the product-research-journey-mapping skill to analyze these [N] support tickets. Focus on [optional: specific journey stage or pillar].`
4. Attach the data file(s)
5. Review the AI draft, validate theme classifications against your domain knowledge, and refine

## Example

**Input**: 150 support tickets from Q1 2026

**Expected Output** (excerpt):

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## Top Themes from Q1 2026 Support Tickets (n=150)

| # | Theme | Frequency | Journey Stage | Pillar | Severity | Existing Backlog Item |
|---|---|---|---|---|---|---|
| 1 | "Can I cancel for free?" — no visible cancellation policy | 23 (15%) | Booking | Trust | Blocking | Free Cancellation Badge (#1, P0) |
| 2 | Payment failed / no alternative method | 18 (12%) | Booking | Conversion | Blocking | Google Pay + Apple Pay (#21, P2) |
| 3 | Search returned wrong location results | 14 (9%) | Research | Discovery | Frustrating | Autocomplete + Search Filters (#27, P2) |
| 4 | "Is this a legit site?" — no reviews visible | 12 (8%) | Evaluation | Trust | Frustrating | External Review Import (#19, P2) |
| 5 | Forced to create account to book | 11 (7%) | Booking | Conversion | Blocking | Guest Checkout + SSO (#6, P1) |
```
