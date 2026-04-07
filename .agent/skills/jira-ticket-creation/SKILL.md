---
name: Jira Ticket Creation Planner
description: Guidelines and checklist for asking preliminary questions and ensuring mandatory fields are set before adding tickets to Jira.
tools: Atlassian MCP
---

## Purpose
Ensures that all Jira tickets are properly categorized with mandatory labels and components, assigned to the correct pod, and correctly scheduled (sprint vs backlog) before they are created. 

## Preliminary Questions
Before creating **ANY** Jira ticket on behalf of the user, you must ask the following clarifying questions to gather required metadata (unless the answers are already obvious from the context):

1. **Which pod does this belong to?** 
   - `pod-contex` (Content Experience)
   - `pod_paycom` (Payment & User)
   - *(Note: This must be added as a mandatory Label when creating the ticket).*
   
2. **Which components are affected?**
   - `SWA (Web Apps)`
   - `Back-End`
   - `Internal Tools (Retool)`
   - *(Note: These must be added to the Components field in Jira).*

3. **Which Jira Project does this belong to?**
   - e.g., `SATU` or other project keys.
   - *(Note: Required by Jira API to create the ticket).*

4. **Scheduling: Sprint or Backlog?**
   - Should this ticket be added to an active Sprint or placed in the Backlog?

5. **Priority Level (Optional but Recommended)**
   - `Highest`, `High`, `Medium`, `Low`, or `Lowest`?

6. **Issue Type & Hierarchy (Optional)**
   - Is this an Epic, Story, Task, or Bug?
   - If it's a Task/Story, does it belong to an existing Epic?

## Ticket Creation Guidelines
When using Jira tools (e.g., via the Atlassian MCP server) to create or edit tickets, ensure the following fields are strictly populated based on the answers:

- **Labels (Mandatory)**: Must include the identified pod label (e.g., `pod-contex`).
- **Components (Mandatory)**: Must include the identified components (e.g., `SWA (Web Apps)`).
- **Parent/Epic Link**: Attach to the proper Epic if applicable.
- **Format**: Ensure the task has a clear summary and an actionable description.

## Example Workflow
**User:** "Create a task to remove id-ID indexing."
**Agent:** "Sure! Before I create the ticket, could you please clarify:
1. Which pod does this belong to (`pod-contex` or `pod_paycom`)?
2. Which components does it affect (`SWA (Web Apps)`, `Back-End`, `Internal Tools`)?
3. Which Jira Project should this go in (e.g., SATU)?
4. Should this go into the current sprint or the backlog?"
**User:** "SATU project, Pod-contex, SWA, and backlog."
**Agent:** *[Creates the ticket in SATU with label: pod-contex and component: SWA (Web Apps), and leaves it in the backlog]*
