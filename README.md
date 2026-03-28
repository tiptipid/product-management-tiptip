# SatuSatu Product Management Playbook

> An AI-assisted product management operating system for early-stage travel-tech startups.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![AI-Assisted](https://img.shields.io/badge/AI--Assisted-Claude%20%2B%20Gemini-purple)
![Format: Markdown](https://img.shields.io/badge/Format-Markdown-lightgrey)

---

## What Is This?

A 10-page product management playbook built for **SatuSatu** — an Online Travel Agency (OTA) platform under [TipTip](https://tiptip.com) focused on curated local experiences in Bali for foreign travelers.

The playbook covers the full PM lifecycle:

- **Customer journey mapping** — persona definition, 6-stage journey, emotion arc, UX audit
- **Strategic framing** — Explore/Exploit classification for every initiative
- **Prioritization** — ICE + Kano hybrid scoring with calibration tables
- **Dependency sequencing** — Trust, Conversion, and Discovery dependency chains
- **North Star metrics** — Weekly Qualified Bookings, leading/lagging indicators, PM review ritual
- **Risk analysis** — Pre-PRD risk gate with standardized templates and RACI
- **AI-assisted PM workflows** — 6-stage lifecycle with model selection, MCP servers, and agent skills
- **Backlog management** — Google Sheets tracker guide with formulas and Jira integration
- **Future expansion** — 8 additional topics queued for future phases

This playbook was generated with AI assistance (Claude Sonnet 4, Claude Opus 4, Gemini 2.5 Pro) and refined by the PM team.

---

## Why Is This Public?

This repository contains **no credentials, API keys, internal employee data, confidential financials, or proprietary algorithms**.

The playbook documents **PM methodology and frameworks** — not trade secrets. All content describes publicly observable product strategies, industry-standard frameworks (ICE, Kano, Explore/Exploit), and generic workflow patterns.

We made it public to:

1. **Share reusable PM frameworks** — The ICE+Kano hybrid, dependency chain model, and AI-assisted workflow are applicable to any early-stage product team
2. **Demonstrate AI-assisted product management** — Show how Claude and Gemini can be used to build structured PM documentation
3. **Serve as a reference for other startups** — Especially post-launch, pre-traction teams with small engineering squads (~10 people)

---

## Repository Structure

```
.
├── README.md
├── guide/                          # Playbook pages
│   ├── 00-introduction.md          # Playbook overview, conventions, tech stack, LLM standards
│   ├── 01-customer-journey-map.md  # Persona, 6-stage journey, UX audit, competitor scoring
│   ├── 02-strategic-framing.md     # Explore/Exploit quadrant, ratio analysis, all initiatives
│   ├── 03-prioritization-framework.md  # ICE+Kano framework, scoring table (49 initiatives)
│   ├── 04-dependency-graph.md      # Trust/Conversion/Discovery chains, Mermaid diagrams
│   ├── 05-north-star-metrics.md    # NSM definition, leading/lagging indicators, PM ritual
│   ├── 06-risk-analysis.md         # Risk template, RACI, 5 completed analyses
│   ├── 07-ai-assisted-development.md  # 6-stage AI workflow, model matrix, MCP servers
│   ├── 08-backlog-tracker-guide.md # Google Sheets setup, formulas, Jira import
│   ├── 09-additional-topics.md     # 8 future playbook expansion topics
│   └── implementation-plan.md      # Internal build plan (phased execution strategy)
└── .agent/
    └── skills/                     # AI agent skills (reusable)
        ├── competitor-benchmarking/
        ├── feature-website-audit/
        ├── prd-review/
        ├── product-research-journey-mapping/
        ├── risk-analysis/
        └── uiux-review/
```

---

## How to Use This Repository

### As a PM Reference

Read the guide pages sequentially (`00` → `09`) to understand the full framework. Start with [00 — Introduction](guide/00-introduction.md) for conventions and tech stack, then follow the page order.

### As a Template

Fork this repo, then replace SatuSatu-specific data with your own product context:

1. Update the **persona** in Page 01 with your target user
2. Reclassify initiatives in Page 02 using your own backlog
3. Re-score with ICE+Kano in Page 03 using your calibration
4. Redefine your **North Star Metric** in Page 05
5. Run the **risk analysis template** (Page 06) on your top initiatives

### With AI Agents

Use the `.agent/skills/` directory with Claude Code, Antigravity, or any AI IDE that supports skill files. Skills are auto-discovered when you open the project.

---

## Agent Skills

### Available Skills

| # | Skill | Description | Input | Output |
|---|---|---|---|---|
| 1 | **PRD Review with Scoring** | Scores a PRD against a 7-dimension rubric | PRD document | Score (0–100) + gap list + pass/fail |
| 2 | **UI/UX Review with Scoring** | Design audit for accessibility, consistency, trust signals, usability | Screenshot or Figma link | Rubric scores + violation list |
| 3 | **Product Research & Journey Mapping** | Analyzes feedback and market data to identify themes and pain points | Support tickets, feedback, market data | Structured report mapped to customer journey |
| 4 | **Competitor Benchmarking** | Monitors competitors for feature changes, pricing shifts, UX updates | Competitor list + criteria | Benchmarking table with scoring |
| 5 | **Risk & Trade-off Analysis** | Auto-generates risk tables from initiative briefs | Initiative brief | Risk table + RACI draft |
| 6 | **Feature & Website Audit** | Automated UX audit against customer journey criteria | URL or screenshot set | UX audit report with trust signal checklist |

### How to Install

#### Option 1: Copy into your project (recommended)

```bash
# Clone this repo
git clone https://github.com/nicepjg/product-management.git

# Copy the skills directory into your project
cp -r product-management/.agent /path/to/your/project/
```

#### Option 2: Use as a submodule

```bash
# Add as a Git submodule
git submodule add https://github.com/nicepjg/product-management.git pm-playbook
```

### Skill File Structure

Each skill follows a standard format:

```
.agent/skills/<skill-name>/
├── SKILL.md          # Metadata (YAML frontmatter) + detailed instructions
└── prompts/
    └── <action>.md   # Ready-to-use prompt template
```

### Usage with AI IDEs

| IDE | How to Use |
|---|---|
| **Claude Code / Antigravity** | Skills are auto-discovered from `.agent/skills/`. Open the project and reference skills by name. |
| **Cursor / Windsurf** | Copy the `SKILL.md` content into your project's `.cursorrules` or system prompt. |
| **Other AI IDEs** | Paste the `SKILL.md` content into your AI tool's project instructions or system prompt configuration. |

---

## Tech Stack

This playbook standardizes the following tools (detailed in [Page 00](guide/00-introduction.md)):

| Category | Tool |
|---|---|
| Documentation | Confluence |
| Project Management | Jira |
| Design | Figma |
| Analytics | OpenPanel |
| Communication | Google Chat |
| Diagrams | Mermaid (in Markdown) |
| AI (Primary) | Claude Sonnet 4 / Opus 4 / Haiku 4 |
| AI (Supplementary) | Gemini 2.5 Pro / Flash |

---

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

PRs are welcome for:

- Framework improvements and corrections
- New agent skill templates
- Additional playbook pages (see [Page 09](guide/09-additional-topics.md) for queued topics)
- Translations

Please open an issue first for significant changes.

---

_Built with AI assistance by the SatuSatu Product Team · March 2026_
