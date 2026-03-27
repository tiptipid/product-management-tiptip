# SatuSatu — AI-Assisted Product Management Playbook

> **Product Operations · March 2026**
> The single source of truth for how SatuSatu's product team thinks, prioritizes, builds, and measures.

---

## What This Playbook Is

This is the product operating system for SatuSatu. It codifies how the product team moves from insight to impact — translating competitive intelligence, customer journey data, and business constraints into a framework-driven, AI-augmented product development process.

**This playbook is NOT a strategy deck.** It is a working manual. Every page produces a reusable artifact — a prioritization table, a dependency graph, a metrics dashboard spec, an agent skill — that the team uses in daily work.

| Field                 | Value                                    |
| --------------------- | ---------------------------------------- |
| **Team Size**         | ~10 engineers                            |
| **Stage**             | Post-launch, pre-traction                |
| **Primary Framework** | Explore/Exploit → ICE → Kano → Dependencies (4-layer) |
| **Horizon Model**     | Now / Next / Later                       |
| **Growth Focus**      | Foreign visitor acquisition & conversion |
| **AI Philosophy**     | Simplify → Augment → Automate            |

---

## Team Roles & Ownership

| Role                      | Responsibility in This Playbook                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **CPO / Head of Product** | Framework selection, strategic framing, playbook governance, AI tool approval                    |
| **Product Manager (PM)**  | ICE scoring, PRD authoring, metrics ownership, sprint-level prioritization, AI agent skill usage |
| **Product Designer**      | Customer journey ownership, Figma design, UX audit, design review via AI agents                  |
| **Engineering PIC**       | Effort estimation (T-shirt sizing), dependency validation, MCP setup, technical risk assessment  |
| **Data / Analytics**      | Metrics instrumentation, dashboard setup (OpenPanel), funnel analysis                            |

### Squad Ownership

| Squad      | Full Name           | Primary Domain                                          |
|------------|---------------------|---------------------------------------------------------|
| **PAYCOM** | Payments & Commerce | Trust signals, booking flow, payment methods, auth, homepage |
| **CONTEX** | Content & Experience | Discovery, search, listing pages, ops tooling, reviews  |

---

## Document Conventions

| Convention                          | Meaning                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------ |
| `NOW` / `NEXT` / `LATER`            | Horizon: 0–1 months / 2–3 months / 3–6 months                                              |
| `P0` – `P3`                         | Priority level: P0 = Critical & Urgent, P1 = Must Have, P2 = Could Have, P3 = Nice to Have |
| `XS` – `XL`                         | Effort size: 1 day → 6+ weeks                                                              |
| ICE Score                           | Impact × Confidence × Ease (each 1–10, max 1000)                                           |
| Kano: Basic / Performance / Delight | Feature classification by user expectation                                                 |
| Explore / Exploit                   | James March's (1991) organizational learning model — strategic bet classification           |
| `⚠️ AI DRAFT — PM REVIEW REQUIRED`   | All AI-generated artifacts carry this header until PM signs off                            |
| `⚠ Inferred`                        | Data point not present in source files; reasoning provided                                 |
| Mermaid diagrams                    | All flowcharts and graphs use Mermaid.js for portability                                   |

### Glossary

| Abbreviation | Definition |
|---|---|
| **NSM** | North Star Metric — Weekly Qualified Bookings Completed (see Page 05) |
| **ABV** | Average Booking Value — mean IDR per confirmed transaction |
| **CVR** | Conversion Rate — typically visit-to-booking unless otherwise specified |
| **GMV** | Gross Merchandise Value — total revenue from confirmed bookings |
| **PIC** | Person In Charge — the designated owner of a task or domain |
| **ROAS** | Return on Ad Spend |
| **OTA** | Online Travel Agency |

---

## Table of Contents

| #   | Page                                                         | File                             | Summary                                                                           |
| --- | ------------------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------------- |
| 00  | Introduction                                                 | `00-introduction.md`             | This page — overview, roles, conventions, tools                                   |
| 01  | [Customer Journey Map](./01-customer-journey-map.md)         | `01-customer-journey-map.md`     | Persona, 6-stage journey, emotion arc, UX audit, friction–backlog cross-reference |
| 02  | [Strategic Framing](./02-strategic-framing.md)               | `02-strategic-framing.md`        | Explore vs. Exploit theory, initiative quadrant, ratio analysis, startup guidance |
| 03  | [Prioritization Framework](./03-prioritization-framework.md) | `03-prioritization-framework.md` | ICE + Kano deep dive, scoring guide, worked examples, complete scoring table      |
| 04  | [Dependency Graph](./04-dependency-graph.md)                 | `04-dependency-graph.md`         | Trust / Conversion / Discovery chains, squad coding, sequencing rationale         |
| 05  | [North Star & Metrics](./05-north-star-metrics.md)           | `05-north-star-metrics.md`       | NSM, 14 must-have + 11 nice-to-have metrics, counter-metrics, PM review ritual    |
| 06  | [Risk & Trade-off Analysis](./06-risk-analysis.md)           | `06-risk-analysis.md`            | Pre-PRD risk gate, RACI template, completed analyses for top initiatives          |
| 07  | [AI-Assisted Development](./07-ai-assisted-development.md)   | `07-ai-assisted-development.md`  | 6-stage PM workflow with AI, agent skills, MCP servers, tool standards            |
| 08  | [Backlog Tracker](./08-backlog-tracker-guide.md)             | `08-backlog-tracker.csv`         | Full backlog with ICE/Kano/Horizon columns + Google Sheets guide                  |
| 09  | [Additional Topics](./09-additional-topics.md)               | `09-additional-topics.md`        | Future expansion roadmap                                                          |

---

## Standardized Tools & Technology Stack

> **Rule: If a tool is not on this list, it is not adviseable for product work but encouraged to be explored/compared and suggest. New tools require CPO approval.**

### Product & Design Tools

| Category                | Tool                  | Purpose                                                                                                                                                                | Owner     |
| ----------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **Diagramming**         | Mermaid (in Markdown) | All flowcharts, dependency graphs, journey maps, architecture diagrams. Renders in Confluence, GitHub, VS Code, Notion.                                                | PM / All  |
| **PRD & Documentation** | Confluence            | Single source of truth for PRDs, specs, decision logs. AI tools read from here (RAG).                                                                                  | PM        |
| **Design**              | Figma                 | All UI/UX design, prototyping, design system. Design review via agent skills + Figma MCP.                                                                              | Design    |
| **Project Management**  | Jira                  | Sprint tracking, backlog management, issue tracking. AI agents read/write via Atlassian MCP.                                                                           | PM + Eng  |
| **Analytics**           | OpenPanel             | Product analytics, event tracking, funnel measurement. AI reads data for metrics narratives.                                                                           | PM + Data |
| **Communication**       | Google Chat           | Team communication, AI bot integrations, async updates.                                                                                                                | All       |
| **Knowledge Base**      | Confluence + GitHub   | Confluence for product docs, GitHub for code + agent skills repo only for Product Manager, as Gitlab is being used for Engineers. Both serve as RAG sources if needed. | All       |
| **RAG / Research**      | NotebookLM            | Upload product docs, PRDs, and research to create grounded AI notebooks. Use alongside Claude Code (via NotebookLM MCP) for deep, source-cited Q&A. | PM        |

### LLM Model Standards

> **Principle**: Multi-model approach. Match cognitive demand to model capability. Standardize on **one paid subscription** (Claude Code Pro).

| Model | Primary Use Cases | When to Use | Context | Subscription |
|---|---|---|---|---|
| **Claude Sonnet 4** | PRD drafting & review, risk analysis, strategic docs, code review | Deep reasoning tasks requiring nuance | 200K | Claude Code Pro |
| **Claude Opus 4** | Complex multi-step analysis, architectural decisions | Highest-stakes documents requiring maximum quality | 200K | Claude Code Pro |
| **Claude Haiku 4** | Vision tasks (screenshot/Figma analysis), structured output, fast triage | Image inputs, quick structured responses, batch classification | 200K | Claude Code Pro |
| **Gemini 2.5 Pro** | Large-context analysis, data/spreadsheet work, Google ecosystem | Processing large docs (>100K tokens) or Google tools | 1M | Free tier |
| **Gemini 2.5 Flash** | Backlog tagging, quick summaries, triage, batch processing | High-volume, low-complexity tasks where speed matters | 1M | Free tier |

> **Cost Control**: The team standardizes on **1 paid subscription — Claude Code Pro** (Anthropic). Gemini is used on the **free tier** for supplementary tasks until further review. No OpenAI/GPT subscriptions needed.

### AI IDE / GUI for Product Managers

> Which interface should PMs use to interact with LLMs? Claude Code Pro is the primary tool; Gemini free tier is supplementary.

| Dimension | Claude Code (Anthropic) — **Primary** | Gemini (Google) — **Supplementary** |
|---|---|---|
| **Interface** | Terminal-based agentic coding + Claude.ai web UI | Gemini CLI (terminal) + AI Studio / Gemini web UI |
| **Subscription** | Claude Code Pro ($20/mo → Claude.ai + Claude Code) | Free tier (rate-limited, no paid features) |
| **Best For PMs** | PRD writing, risk analysis, deep reasoning, agent skills with MCP servers | Data analysis, spreadsheet work, large-doc review, Google Workspace integration |
| **MCP Support** | ✅ Full — Atlassian, Figma, Sequential Thinking, GitHub | ⚠️ Limited on free tier |
| **Vision / Image** | ✅ Claude Haiku 4 for screenshots and Figma exports | ✅ Gemini Pro/Flash for screenshots and design analysis |
| **Context Window** | 200K tokens — sufficient for most PM docs | 1M tokens — better for analyzing large datasets or multiple docs at once |
| **Strengths** | Superior at nuanced writing, PRD quality, structured reasoning, and code | Faster processing, native Google Sheets/Docs integration, larger context window |
| **Weaknesses** | Smaller context window; no native Google Workspace integration | Free tier has rate limits; less nuanced long-form writing |

**Recommendation for PMs**:
- **Primary (paid)**: **Claude Code Pro** — Use for all PRD work, risk analysis, agent skills (via MCP), and any task requiring judgment and nuance.
- **Supplementary (free)**: **Gemini free tier** — Use for large-doc review (>200K context), quick data analysis, and Google Workspace tasks. Upgrade to Google AI Pro pending further review.
- **Rule of thumb**: If you need to *think*, use Claude. If you need to *process*, use Gemini.

### Recommended MCP Servers

MCP (Model Context Protocol) servers connect AI agents directly to your tools with real-time read/write access.

**Core (Must Install)**

| MCP Server                  | Purpose                                                         | Used By    |
| --------------------------- | --------------------------------------------------------------- | ---------- |
| **Atlassian MCP**           | Read/write Confluence pages + Jira issues. Primary RAG source.  | PM, Eng    |
| **Figma MCP** (Dev Mode)    | Pull real design data for AI-powered design review.             | Design, PM |
| **Sequential Thinking MCP** | Structured multi-step reasoning for complex scoring/risk tasks. | PM         |

**Recommended**

| MCP Server                        | Purpose                                      | Used By |
| --------------------------------- | -------------------------------------------- | ------- |
| **GitHub MCP**                    | Agent skills repo management, PR automation. | PM, Eng |
| **Google Drive MCP**              | Access shared docs, backlog spreadsheets.    | PM, All |
| **NotebookLM MCP**                | RAG over uploaded product docs; source-cited Q&A via Claude Code. | PM      |
| **Brave Search / Web Search MCP** | Market research and competitor monitoring.   | PM      |
| **Playwright MCP**                | Automated browser testing for UX audits.     | QA, PM  |

### Tool Adoption Rules

1. **No shadow tools** — All tools must be from the approved list above.
2. **AI outputs are drafts** — Every AI-generated artifact starts with `⚠️ AI DRAFT — PM REVIEW REQUIRED`.
3. **Confluence is the source of truth** — If it's not in Confluence, it doesn't exist.
4. **Mermaid for all diagrams** — No Lucidchart, no draw.io, no PowerPoint flowcharts.
5. **Figma for all design** — No Sketch, no Adobe XD. One design tool, one design system.

---

## How to Use This Playbook

1. **New initiative?** Start at Page 02 (Explore/Exploit) → Page 03 (ICE+Kano scoring) → Page 06 (Risk gate) → PRD
2. **Sprint planning?** Consult Page 03 (scoring table) + Page 04 (dependency graph) + Page 08 (backlog tracker)
3. **Metrics review?** Page 05 (North Star + ritual) defines what to check and when
4. **Need AI help?** Page 07 tells you which AI tool, model, and agent skill to use for each PM workflow stage
5. **Design review?** Page 07 → Stage 4 → UIUX/Figma Review agent skill with Figma MCP

---

*SatuSatu Product Management Playbook · v1.0 · March 2026*
