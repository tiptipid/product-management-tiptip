---
name: PRD Review with Scoring
description: Scores a Product Requirements Document against a 7-dimension rubric and provides actionable feedback with a pass/fail recommendation.
model: claude-sonnet-4
lifecycle_stage: "3. Definition & Documentation"
tools: Atlassian MCP, Sequential Thinking MCP
parallel: true
parallel_strategy: "2 agents — Agent 1 scores user-facing dimensions (Problem Statement, User Stories, Acceptance Criteria); Agent 2 scores system-facing dimensions (Success Metrics, Dependencies, Risk Acknowledgment, Technical Feasibility). Parent aggregates weighted total."
---

## Embedded Context

This skill is self-contained. All referenced frameworks are embedded below.

### Customer Journey Stages
| # | Stage | User Goal | Core Anxiety |
|---|---|---|---|
| 1 | Inspiration | Discover Bali activities | "What should I do?" |
| 2 | Research | Compare platforms, read reviews | "Which platform is trustworthy?" |
| 3 | Evaluation | Trust audit, credibility check | "Is this site safe? Is it legit?" |
| 4 | Booking | Complete transaction | "Can I cancel? Can I pay my way?" |
| 5 | Pre-Experience | Logistics & reassurance | "Where do I go? What do I bring?" |
| 6 | Post-Experience | Review, repeat, refer | "Was it worth it? Would I return?" |

### Dependency Pillars
| Pillar | Core Question | Priority |
|---|---|---|
| **Trust** | "Will the visitor believe this is safe?" | Fix first |
| **Conversion** | "Can the visitor complete the booking?" | Fix second |
| **Discovery** | "Can the visitor find the right experience?" | Fix third |

**Trust chain**: Free Cancel Badge → Locally Curated Badge → External Review → Social Proof Counter → Review Nationality Display
**Conversion chain**: Move CTA → Guest Checkout + SSO → OTP Auth / My Booking / Guest Purchase; Google Pay → I8n Payment
**Discovery chain**: Destination Pages → SEO → Autocomplete + Filters → Discover Filter & Sort

### Key Metrics
- **NSM**: Weekly Qualified Bookings Completed (confirmed bookings, 24h cancel filter, 7-day rolling)
- **Must-Have Leading**: Checkout Initiation Rate, Payment Abandonment Rate, Search-to-Catalog CTR, Catalog Engagement Depth, Activation Rate, D7 Return Visit Rate, Search Zero-Result Rate, Paid Ad Landing Bounce Rate
- **Must-Have Lagging**: Weekly Qualified Bookings, Booking Conversion Rate, 30-Day Repeat Booking Rate, Booking Cancellation Rate (48h), Average Booking Value, Organic Branded Search Volume
- **Counter-metrics**: Booking Cancellation Rate (>15% alert), ABV (>15% MoM drop), D7 Return (<10%), Organic Search (declining while NSM grows)

### Risk Analysis Gate
A completed Risk & Trade-off Analysis is **required** before PRD review. The analysis must contain: Key Assumptions (2–3 falsifiable), Biggest Risk, Second Risk, Validation Approach, RACI Table, Trade-offs Accepted. If no risk analysis is provided, the review is **blocked**.

### Approved Tool Stack
Design: Figma. Project tracking: Jira (Atlassian MCP). Analytics: OpenPanel + GA4. AI: Claude Code, Gemini CLI.

---

## Purpose

Enforces PRD quality by scoring every draft against a standardized rubric before engineering commitment. Catches missing sections, vague acceptance criteria, and disconnected metrics — the three most common PRD failure modes.

## Input

- **Draft PRD** — Markdown, Confluence page (via Atlassian MCP), or pasted text
- **Initiative context** — Initiative name, ICE score, Kano classification, Dependency Pillar
- **Risk Analysis** — Completed risk analysis for this initiative (required input — see gate above)

## Output

- **Score card** (markdown) with:
  - Score per dimension (0–100 scale, 7 dimensions)
  - Weighted total score (0–100)
  - Pass/Fail recommendation (Pass ≥ 70, Conditional 50–69, Fail < 50)
  - Specific feedback per dimension with line-level citation
  - Missing sections checklist
- All outputs prefixed with `⚠️ AI DRAFT — PM REVIEW REQUIRED`

## Process

1. **Validate gate** — Confirm that a Risk & Trade-off Analysis exists for this initiative. If not, output: "⛔ BLOCKED: Complete Risk & Trade-off Analysis before PRD review. Use the risk-analysis skill to generate one."
2. **Parse** — Read the PRD and identify each section
3. **Score** — Rate each of the 7 dimensions on a 0–100 scale:

| Dimension | Weight | Scoring Criteria |
|---|---|---|
| **Problem Statement** | 15% | Is it clear, specific, and tied to a user pain point from a journey stage? (See journey stages above) |
| **User Stories** | 20% | Does it follow "As a [user], I want [action], so that [value]" format? Are edge cases covered? |
| **Acceptance Criteria** | 20% | Are criteria testable? Unambiguous? Do they cover happy path + error states? |
| **Success Metrics** | 15% | Are metrics tied to NSM or Must-Have metrics? (See Key Metrics above) Is the measurement plan specified? |
| **Dependencies** | 10% | Are dependencies identified with Blocked By / Blocks relationships? Does sequencing align with the dependency chains? |
| **Risk Acknowledgment** | 10% | Does the PRD reference the completed risk analysis? Are mitigations documented? |
| **Technical Feasibility** | 10% | Has the Engineering PIC validated the effort estimate? Are technical constraints noted? |

4. **Calculate** — Weighted total = Σ(dimension_score × weight)
5. **Recommend** — Pass (≥70), Conditional Pass (50–69), Fail (<50)
6. **Report** — Generate scorecard with specific, actionable feedback per dimension

## Parallel Execution

This skill can be split across 2 agents for faster review:

**Agent 1 — User-Facing Dimensions** (55% weight):
- Problem Statement (15%)
- User Stories (20%)
- Acceptance Criteria (20%)
- Uses: Journey stages, user pain points, edge case reasoning

**Agent 2 — System-Facing Dimensions** (45% weight):
- Success Metrics (15%)
- Dependencies (10%)
- Risk Acknowledgment (10%)
- Technical Feasibility (10%)
- Uses: Key metrics, dependency chains, risk analysis reference

**Parent agent**: Validates the gate (step 1), dispatches both agents with the PRD text + embedded context, collects scores, calculates weighted total, generates final recommendation.

## Constraints

- All outputs must begin with `⚠️ AI DRAFT — PM REVIEW REQUIRED`
- Do NOT pass a PRD that lacks a Risk Analysis reference — this is a non-negotiable gate
- Scoring must be strict: vague acceptance criteria = score ≤ 40 for that dimension
- Use Claude Sonnet 4 for this skill (deep reasoning required for nuanced evaluation)
- If using Sequential Thinking MCP, break the review into 7 reasoning steps (one per dimension)

## How to Use

1. Ensure a Risk & Trade-off Analysis is completed for the initiative (use the `risk-analysis` skill if needed)
2. Open Claude Code in any directory
3. Say: `Use the prd-review skill to score this PRD for [initiative name]. The Risk Analysis is complete.`
4. Paste or attach the PRD (or provide the Confluence page ID if Atlassian MCP is connected)
5. Review the scorecard — address all dimensions scoring below 60 before engineering handoff

## Example

**Input**: Draft PRD for "Free Cancellation Badge" (Initiative #1, P0)

**Expected Output** (excerpt):

```markdown
⚠️ AI DRAFT — PM REVIEW REQUIRED

## PRD Scorecard: Free Cancellation Badge

| Dimension | Score | Weight | Weighted | Feedback |
|---|---|---|---|---|
| Problem Statement | 85 | 15% | 12.8 | ✅ Clear: "Foreign visitors abandon checkout when cancellation policy is not visible." Tied to Evaluation/Booking stage. |
| User Stories | 70 | 20% | 14.0 | ⚠️ Missing edge case: what happens for activities with partial cancellation (e.g., 48h cutoff)? Add story for this variant. |
| Acceptance Criteria | 55 | 20% | 11.0 | ❌ Criteria say "badge is shown" but don't define WHERE (listing card? detail page? both?). Not testable as written. |
| Success Metrics | 80 | 15% | 12.0 | ✅ Tied to Checkout Initiation Rate (Must-Have leading metric). Missing: counter-metric monitoring (Booking Cancellation Rate). |
| Dependencies | 90 | 10% | 9.0 | ✅ No blockers. XS effort, no dependency chain. |
| Risk Acknowledgment | 75 | 10% | 7.5 | ✅ References risk analysis. Missing: mitigation plan for partial-cancel operators. |
| Technical Feasibility | 80 | 10% | 8.0 | ✅ PIC validated: <1 day, data model exists. |

### Total: 74.3 / 100 — ✅ PASS

### Action Items Before Handoff
1. Add user story for partial cancellation variant
2. Make acceptance criteria testable — specify exact badge placement
3. Add Booking Cancellation Rate as counter-metric to monitor
```
