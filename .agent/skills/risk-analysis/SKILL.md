---
name: Risk & Trade-off Analysis
description: Auto-generates risk analysis tables from initiative briefs, including assumptions, failure modes, validation approaches, and RACI assignments.
model: claude-sonnet-4
lifecycle_stage: "3. Definition & 6. Post-Launch"
tools: Atlassian MCP, Sequential Thinking MCP
parallel: false  # Sequential reasoning required — each section builds on the previous (assumptions → risks → validation → RACI)
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Customer Journey Stages
| # | Stage | Goal |
|---|---|---|
| 1 | Inspiration | Discover Bali activities via social/search |
| 2 | Research | Browse options, compare platforms, read reviews |
| 3 | Evaluation | Trust audit — decide if platform is safe |
| 4 | Booking | Complete transaction with minimal friction |
| 5 | Pre-Experience | Logistics, reassurance between booking and activity |
| 6 | Post-Experience | Review, repeat, refer |

### Dependency Pillars
| Pillar | Core Question | Sequencing |
|---|---|---|
| **Trust** | "Will the visitor believe this is safe?" | Fix first |
| **Conversion** | "Can the visitor complete the booking?" | Fix second |
| **Discovery** | "Can the visitor find the right experience?" | Fix third |

### Prioritization Reference
- **ICE Score** = Impact × Confidence × Ease (each 1–10, max 1,000)
- **Priority**: P0 ≥ 700, P1 350–699, P2 150–349, P3 < 150
- **Kano**: Basic (must-have or churn), Performance (linear value), Delight (unexpected wow)
- **Effort**: XS < 1d, S ~1wk, M 2–3wk, L 4–6wk, XL 6+wk
- **Explore** = new capability/market bet; **Exploit** = improve existing flow

### RACI Defaults by Pillar
| Pillar | R (Responsible) | A (Accountable) |
|---|---|---|
| Trust | Ops | Product |
| Conversion | Engineering | Product |
| Discovery | Marketing | Product |

### Key Metrics (for validation design)
- **NSM**: Weekly Qualified Bookings Completed
- **Must-Have**: Checkout Initiation Rate, Booking Completion Rate, Booking Cancellation Rate (48h), D7 Return Visit Rate, Average Booking Value
- **Tools**: OpenPanel (product analytics), GA4 (acquisition/conversion)

---

## Purpose

Accelerates the pre-PRD risk gate by generating a draft risk analysis from an initiative brief. The PM provides initiative context and the AI produces a structured analysis. Reduces a 45-minute analysis to a 15-minute review-and-refine cycle.

Also used post-launch (Stage 6) to generate retrospective risk assessments based on actual outcomes vs. predictions.

## Input

- **Initiative name** — Canonical name from the backlog scoring table
- **Initiative context** — ICE score, Kano classification, Priority, Horizon, Pillar, Effort size
- **Initiative description** — What this initiative does and why it matters (2–5 sentences)
- **Dependencies** — Blocked By and Blocks relationships (which initiatives must ship first, which are unlocked by this one)
- **Post-launch data** — (optional, for retrospective) OpenPanel metrics, support ticket themes

## Output

- **Risk analysis table** (markdown) following the template below:
  - Key Assumptions (2–3 falsifiable statements)
  - Biggest Risk (specific failure mode)
  - Second Risk (different category from first)
  - Validation Approach (cheapest test with metric, duration, sample size)
  - RACI Table (7 roles filled)
  - Trade-offs Accepted (opportunity cost in engineering days)
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

### Risk Analysis Template

| Field | Content |
|---|---|
| **Initiative** | [Name] |
| **ICE Score** | [Score] · [Priority] · [Horizon] |
| **Key Assumptions** | What must be true for this initiative to produce its claimed impact? 2–3 specific, falsifiable statements. |
| **Biggest Risk** | Single most likely failure mode. What goes wrong, for whom, when? |
| **Second Risk** | Second failure mode — different category from first. |
| **Validation Approach** | Cheapest test: metric, duration, sample size threshold. |
| **RACI Table** | See below. |
| **Trade-offs Accepted** | What are we NOT doing? Opportunity cost in eng-days? |

### RACI Table Template

| Role | R | A | C | I |
|---|---|---|---|---|
| Product | | | | |
| Engineering | | | | |
| Design | | | | |
| Ops | | | | |
| Marketing | | | | |
| Finance / Commercial | | | | |
| VC / Leadership | | | | |

**Rules**: Exactly ONE "A" per initiative. Use RACI Defaults by Pillar (see Embedded Context) as starting point.

## Process

1. **Context** — Load the initiative's full context from the user-provided brief and any attached backlog/dependency data
2. **Assumptions** — Use Sequential Thinking MCP to reason through: "What must be true for this initiative to deliver its claimed impact?" Generate 2–3 specific, falsifiable statements
3. **Risks** — Identify the two most likely failure modes:
   - Risk 1: What goes wrong for the USER? (behavioral/UX risk)
   - Risk 2: What goes wrong for the TEAM? (technical/operational/business risk)
4. **Validation** — Design the cheapest test:
   - What metric will confirm or refute the key assumption?
   - How long must the test run?
   - What is the minimum sample size for statistical significance?
5. **RACI** — Assign responsibilities across 7 roles using the pillar-based defaults as a starting point
6. **Trade-offs** — Calculate opportunity cost: effort size × engineering day rate. What else could be built with those days?
7. **Report** — Generate the complete analysis using the Risk Analysis Template above

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Assumptions must be FALSIFIABLE — not "users will like it" but "users will click the badge at a rate >5%"
- Validation approach must be the CHEAPEST test — prefer analytics over A/B, A/B over user study, user study over full build
- RACI must have exactly ONE "A" (Accountable) per initiative
- Use Claude Sonnet 4 for this skill (deep reasoning for nuanced risk identification)
- Risk categories should differ — if Risk 1 is behavioral, Risk 2 should be technical or operational

## How to Use

1. Gather the initiative context: name, ICE score, Kano class, priority, horizon, pillar, effort, dependencies
2. Open Claude Code in any directory
3. Say: `Use the risk-analysis skill to generate a risk analysis for [initiative name]. ICE: [score], Kano: [class], Priority: [P0-P3], Pillar: [Trust/Conversion/Discovery], Effort: [XS-XL].`
4. Add a brief description of the initiative and any known dependencies
5. Review the AI draft — validate assumptions against your domain knowledge, fill in RACI names

## Example

**Input**: "Wishlist / Save for Later" (P2, ICE 135, Performance, Discovery, S effort)

**Expected Output**:

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## Risk & Trade-off Analysis: Wishlist / Save for Later

`ICE: 135` · `P2` · `NEXT` · `S effort` · Kano: Performance · 🟣 Discovery

| Field | Content |
|---|---|
| **Key Assumptions** | (1) Foreign visitors browse multiple activities before deciding — a save feature reduces re-search friction. (2) Saved items will convert to bookings at >15% rate within 14 days. (3) Users will create accounts to save items — or guest saves via browser storage are sufficient. |
| **Biggest Risk** | Wishlist becomes a graveyard: users save items but never return. Feature adds development cost without measurable conversion lift. Industry data suggests wishlist-to-purchase rates for travel are 8–12% — lower brand recognition may push this below 5%. |
| **Second Risk** | Technical: guest saves via localStorage are lost when users switch devices (which foreign travelers frequently do — phone to hotel laptop). Requires account creation to sync, creating a dependency on Guest Checkout + SSO. |
| **Validation Approach** | Before building: check OpenPanel for "return visit" behavior. What % of foreign visitors view the same listing twice? If <10%, the re-search problem may not exist. If >20%, wishlist has strong product-market fit signal. Duration: 2 weeks of data analysis. No build required. |
| **Trade-offs Accepted** | S effort (~1 week). Opportunity cost: delays one P2 Conversion or Trust item by 1 sprint. Given P2 priority, acceptable if validation passes. |

| Role | R | A | C | I |
|---|---|---|---|---|
| Product | Feature spec | ✓ Owns outcome | | |
| Engineering | Implementation | | Browser storage vs. account sync | |
| Design | | | Save button UX | |
| Ops | | | | |
| Marketing | | | | Save-to-email flow |
```
