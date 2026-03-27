# 07 — AI-Assisted Product Development

---

## Model Selection Guide

Different AI models excel at different cognitive tasks. Use the right model for the right job.

| Model                        | Best For                                                                    | Context Window | Cost Tier   | When to Use                                                                              |
| ---------------------------- | --------------------------------------------------------------------------- | -------------- | ----------- | ---------------------------------------------------------------------------------------- |
| **Claude Sonnet 4 / Opus 4** | Deep PRD reasoning, risk analysis, nuanced strategic docs                   | 200K tokens    | Medium–High | Quality-critical documents where reasoning depth matters more than speed                 |
| **Claude Haiku 4**           | Vision tasks (screenshots, Figma exports), fast triage, structured output   | 200K tokens    | Low         | UI screenshot audits, design review, batch classification                                |
| **Gemini 2.5 Pro**           | Large-context analysis, data/spreadsheet work, Google ecosystem integration | 1M tokens      | Medium      | Analyzing large datasets (full backlog CSV, support ticket exports, multi-doc synthesis) |
| **Gemini 2.5 Flash**         | High-volume quick tasks — backlog tagging, summaries, triage                | 1M tokens      | Low         | Cost-sensitive batch operations (tag 50 tickets, summarize 20 PRDs)                      |

> **Recommendation**: Multi-model approach. Claude for quality-critical docs and vision tasks, Gemini for speed/cost-sensitive tasks. See Page 00 for the full model standards and subscription guidance.

---

## 6-Stage Product Lifecycle with AI

Each stage defines the AI role, recommended tools, and the agent skill the team should build.

```mermaid
flowchart LR
    S1["1. Discovery<br/>& Research"]
    S2["2. Ideation<br/>& Strategy"]
    S3["3. Definition<br/>(PRD)"]
    S4["4. Prototyping<br/>& Testing"]
    S5["5. Execution<br/>& Delivery"]
    S6["6. Post-Launch"]

    S1 --> S2 --> S3 --> S4 --> S5 --> S6

    style S1 fill:#2563EB,color:#fff
    style S2 fill:#7C3AED,color:#fff
    style S3 fill:#DC2626,color:#fff
    style S4 fill:#F59E0B,color:#000
    style S5 fill:#16A34A,color:#fff
    style S6 fill:#0EA5E9,color:#fff
```

### Stage 1 — Discovery & Research

| Aspect                | Detail                                                                                          |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| **AI Role**           | Analyze user feedback, support tickets, interview transcripts → identify themes and pain points |
| **Recommended Tools** | Perplexity (web research), Gemini Deep Research (multi-source synthesis)                        |
| **Best Model**        | Gemini 2.5 Pro (large context for multi-doc analysis)                                           |
| **Input**             | Support tickets, user reviews, competitor data, market reports                                  |
| **Output**            | Themes report with frequency counts, pain point ranking, opportunity sizing                     |

**Agent Skill**: [Product Research & Journey Mapping](./.agent/skills/product-research-journey-mapping/SKILL.md)

**How to Use the Skill**:
1. Export support tickets or user feedback into a CSV/text file
2. Open Claude Code in the playbook directory
3. Say: `Use the product-research-journey-mapping skill to analyze these 150 support tickets. Focus on the Booking stage.`
4. Attach the data file(s)
5. Review the AI draft — themes are mapped to journey stages (Page 01) and dependency pillars (Page 04)

---

### Stage 2 — Ideation & Strategy

| Aspect                | Detail                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| **AI Role**           | Brainstorming partner for new ideas, market trend analysis, competitive intelligence reports      |
| **Recommended Tools** | Claude Sonnet 4 (deep reasoning), ChatGPT (broad brainstorming), Gemini 2.5 Pro (market analysis) |
| **Best Model**        | Claude Sonnet 4 (nuanced strategic reasoning)                                                     |
| **Input**             | Research findings from Stage 1, strategic framing (Page 02), current backlog                      |
| **Output**            | Initiative briefs with preliminary Explore/Exploit classification and Kano hypothesis             |

**Agent Skill**: [Competitor Benchmarking](./.agent/skills/competitor-benchmarking/SKILL.md)

**How to Use the Skill**:
1. Ensure Brave Search MCP and Playwright MCP are connected
2. Open Claude Code in the playbook directory
3. Say: `Use the competitor-benchmarking skill to generate this week's competitor digest. Focus on checkout UX and trust signals.`
4. Review the digest — Kano reclassification suggestions should be validated against Page 03

---

### Stage 3 — Definition & Documentation (PRD)

| Aspect                | Detail                                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AI Role**           | Draft PRDs from context/constraints/user stories, review existing PRDs for completeness                     |
| **Recommended Tools** | Claude Opus 4 (deep reasoning PRDs), ChatPRD, Notion AI                                                     |
| **Best Model**        | Claude Opus 4 (complex document generation with cross-referencing)                                          |
| **Input**             | Initiative brief, Risk & Trade-off Analysis (Page 06), dependency context (Page 04), user journey (Page 01) |
| **Output**            | Draft PRD with user stories, acceptance criteria, edge cases, metrics to track                              |

> ⚠️ **Gate**: Risk & Trade-off Analysis (Page 06) MUST be completed before this stage begins. AI should reference the completed analysis in the PRD.

**Agent Skill**: [PRD Review with Scoring](./.agent/skills/prd-review/SKILL.md)

**How to Use the Skill**:
1. Complete the Risk & Trade-off Analysis (Page 06) first — this is a non-negotiable gate
2. Open Claude Code in the playbook directory
3. Say: `Use the prd-review skill to score this PRD for Guest Checkout + SSO. The Risk Analysis is complete.`
4. Paste or attach the PRD (or provide the Confluence page ID via Atlassian MCP)
5. Address all dimensions scoring below 60 before engineering handoff

**PRD Review Rubric**:

| Dimension             | Weight | What to Check                                                    |
| --------------------- | ------ | ---------------------------------------------------------------- |
| Problem Statement     | 15%    | Clear, specific, tied to user pain point                         |
| User Stories          | 20%    | Follows "As a [user], I want [action], so that [value]" format   |
| Acceptance Criteria   | 20%    | Testable, unambiguous, edge cases covered                        |
| Success Metrics       | 15%    | Tied to NSM or Must-Have metrics (Page 05)                       |
| Dependencies          | 10%    | Cross-referenced with Page 04 dependency chains                  |
| Risk Acknowledgment   | 10%    | References Page 06 analysis                                      |
| Technical Feasibility | 10%    | Engineering PIC (Person In Charge) has validated effort estimate |

---

### Stage 4 — Prototyping & Testing

| Aspect                | Detail                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------- |
| **AI Role**           | Rapid prototyping, simulate user interactions, design review                            |
| **Recommended Tools** | v0.dev (UI generation), Figma MCP (design context + screenshot + tokens)                |
| **Best Model**        | Claude Haiku 4 (vision — screenshot analysis for UI review)                              |
| **Input**             | PRD, Figma file links (via Figma MCP), screenshots (fallback or for live site)          |
| **Output**            | Design review feedback, accessibility audit, consistency check against design system    |

**Agent Skill**: [UI/UX Review with Scoring](./.agent/skills/uiux-review/SKILL.md)

**How to Use the Skill**:

**Path A — Figma link (preferred for design review)**:
1. Open Claude Code with Figma MCP connected
2. Say: `Use the uiux-review skill to score this checkout page design. Figma: [paste Figma link]. This is for Free Cancellation Badge at the Booking stage.`
3. The agent calls `get_metadata` + `get_screenshot` + `get_variable_defs` automatically

**Path B — Screenshots (for live site audit or no Figma MCP)**:
1. Take screenshots at mobile (375px) and desktop (1280px)
2. Say: `Use the uiux-review skill to score this checkout page design. This is for Free Cancellation Badge at the Booking stage.`
3. Attach screenshot(s)

Review the scorecard with your designer — prioritize dimensions scoring below 6

---

### Stage 5 — Execution & Delivery

| Aspect                | Detail                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------- |
| **AI Role**           | Automate project tracking, code review assistance, QA support                           |
| **Recommended Tools** | GitHub Copilot (code), Cursor/Antigravity (AI-native IDE), Linear AI (project tracking) |
| **Best Model**        | Claude Sonnet 4 (code review reasoning), Gemini 2.5 Flash (batch code analysis)         |
| **Input**             | PRD, design specs, codebase context                                                     |
| **Output**            | Code suggestions, automated test cases, deployment checklists                           |

**Agent Skill**: [Feature & Website Audit](./.agent/skills/feature-website-audit/SKILL.md)

**How to Use the Skill**:
1. Ensure Playwright MCP is connected in your Claude Code session
2. Say: `Use the feature-website-audit skill to run a full UX audit of satusatu.com. Compare against last week's report.`
3. For targeted checks: `Use the feature-website-audit skill to verify that Free Cancellation Badge is live on listing detail pages.`

---

### Stage 6 — Post-Launch

| Aspect                | Detail                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| **AI Role**           | Analyze A/B test results, monitor user sentiment, summarize feedback                               |
| **Recommended Tools** | Gemini 2.5 Flash (fast analysis), OpenPanel + AI (metrics narrative), Miro AI (retro facilitation) |
| **Best Model**        | Gemini 2.5 Flash (high-volume, cost-efficient analysis)                                            |
| **Input**             | A/B test data, OpenPanel metrics, user feedback, support tickets                                   |
| **Output**            | Test result interpretation, sentiment trends, recommended next actions                             |

**Agent Skill**: [Risk & Trade-off Analysis](./.agent/skills/risk-analysis/SKILL.md)

**How to Use the Skill**:
1. Gather initiative context from Page 03 scoring table and Page 04 dependency graph
2. Open Claude Code in the playbook directory
3. Say: `Use the risk-analysis skill to generate a risk analysis for Wishlist / Save for Later. ICE: 135, Kano: Performance, Priority: P2, Pillar: Discovery, Effort: S.`
4. Review the AI draft — validate assumptions against your domain knowledge, fill in RACI names

---

## Key Considerations

### 1. Human in the Loop

> **First pass by AI, final pass by PM.**

All AI outputs are drafts. PMs own:
- **Product judgment** — which problems to solve
- **Prioritization trade-offs** — what to build vs. defer
- **Stakeholder communication** — how to position decisions
- **Quality bar** — whether the output meets SatuSatu standards

AI accelerates; humans decide.

### 2. RAG-Style Data Grounding

Use Retrieval-Augmented Generation (RAG) to ground AI on company-specific data rather than generic knowledge:

| Data Source                 | How to Use                       | Reduces                                            |
| --------------------------- | -------------------------------- | -------------------------------------------------- |
| This playbook (Pages 00–09) | Attach as context when prompting | Generic advice that ignores SatuSatu's constraints |
| Support tickets             | Feed into Discovery stage        | Hallucinated user pain points                      |
| OpenPanel metrics           | Feed into Post-Launch stage      | Incorrect performance assumptions                  |
| PRD history                 | Feed into PRD drafting           | Inconsistent spec formats                          |

> **Practical tip**: Create a "SatuSatu PM Context Pack" folder with the latest versions of this playbook, the top 50 support tickets, and the current OpenPanel dashboard screenshots. Attach to every AI session.

### 3. Tool Selection Principle

Specialized tools for specific tasks, not one AI for everything.

| Cognitive Demand                            | Best Model               | Why                                        |
| ------------------------------------------- | ------------------------ | ------------------------------------------ |
| Deep reasoning (risk analysis, PRD)         | Claude Sonnet 4 / Opus 4 | Superior at nuanced trade-off analysis     |
| Large context (full backlog, ticket export) | Gemini 2.5 Pro           | 1M token window handles entire datasets    |
| Speed + cost (tagging, summaries, triage)   | Gemini 2.5 Flash         | Fast, cheap, good-enough for routine tasks |
| Vision (screenshot analysis, UI audit)      | Claude Haiku 4           | Vision-optimized with fast structured output |

---

## Agent Skills Summary

Six custom agent skills the team should build, mapped to lifecycle stages:

| #   | Skill                         | Lifecycle Stage            | Input             | Output                            | Recommended Model |
| --- | ----------------------------- | -------------------------- | ----------------- | --------------------------------- | ----------------- |
| 1   | **PRD Review with Scoring**   | 3. Definition              | Draft PRD         | Score (0–100) + feedback          | Claude Sonnet 4   |
| 2   | **UI/UX Review with Scoring** | 4. Prototyping             | Screenshot(s)     | Score per dimension + suggestions | Claude Haiku 4    |
| 3   | **Product Research**          | 1. Discovery               | Research brief    | Competitor report + scoring       | Gemini 2.5 Pro    |
| 4   | **Risk & Trade-off Analysis** | 3. Definition              | Initiative brief  | Page 06 risk table (draft)        | Claude Sonnet 4   |
| 5   | **Feature/Website Audit**     | 5–6. Execution/Post-Launch | URL or screenshot | UX regression report              | Claude Haiku 4    |
| 6   | **Competitor Benchmarking**   | 1–2. Discovery/Ideation    | Competitor list   | Weekly change digest              | Gemini 2.5 Flash  |

---

## Skills Directory

All 6 agent skills are stored in this playbook's `.agent/skills/` directory:

```
.agent/skills/
├── product-research-journey-mapping/
│   ├── SKILL.md              # Discovery: analyze tickets, map to journey + pillars
│   └── prompts/
│       └── analyze.md         # Ready-to-use analysis prompt
├── competitor-benchmarking/
│   ├── SKILL.md              # Ideation: weekly OTA competitor digest
│   └── prompts/
│       └── weekly-scan.md     # Recurring scan prompt
├── prd-review/
│   ├── SKILL.md              # Definition: 7-dimension PRD scoring rubric
│   └── prompts/
│       └── review.md          # Scoring prompt with calibrated rubric
├── uiux-review/
│   ├── SKILL.md              # Prototyping: screenshot-based design audit
│   └── prompts/
│       └── audit.md           # Visual review prompt (Claude Haiku 4 vision)
├── feature-website-audit/
│   ├── SKILL.md              # Execution: automated UX audit via Playwright
│   └── prompts/
│       └── full-audit.md      # Full site audit checklist
└── risk-analysis/
    ├── SKILL.md              # Definition: Page 06 risk table generation
    └── prompts/
        └── generate.md        # Risk analysis generation prompt
```

**Each SKILL.md follows a standard format** (YAML frontmatter + markdown):
- `name`, `description`, `model`, `lifecycle_stage`, `tools` in frontmatter
- Sections: Purpose → Input → Output → Process → Constraints → How to Use → Example

**Team onboarding**:
1. Clone or pull the playbook repository
2. Open Claude Code in the playbook directory — skills are auto-detected from `.agent/skills/`
3. Invoke any skill by name: `Use the [skill-name] skill to [task description]`
4. For Gemini: paste the prompt from the `prompts/` subdirectory directly

**Useful reference repos**:
- `anthropics/skills` — Anthropic's official skill format
- `heilcheng/awesome-agent-skills` — Community skill collection

---

## Future Expansions

Topics to explore once the 6 core skills are operational:

| Expansion                              | What It Does                                                             | When to Build                              |
| -------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------ |
| **AI sprint retro analysis**           | Summarize retro notes → extract action items → track completion          | After 3 sprints of data                    |
| **Automated changelog generation**     | Read Jira closed tickets → generate user-facing changelog                | After Jira workflow is stable              |
| **AI customer feedback synthesis**     | Aggregate reviews + support tickets → weekly theme digest                | After OpenPanel + support tool integration |
| **Predictive feature adoption**        | Estimate adoption rate for new features based on historical data         | After 6 months of feature launch data      |
| **A/B test hypothesis generation**     | Given metrics + initiative → generate test hypotheses with expected lift | After first A/B test framework is live     |
| **Automated weekly metrics narrative** | Gemini reads OpenPanel → writes PM pulse summary                         | After Page 05 metrics are instrumented     |

> **Read next**: [Page 08 — Backlog Tracker Guide](./08-backlog-tracker-guide.md) for how to set up and maintain the backlog spreadsheet.
