---
name: Jira Monthly Release Report Generator
description: Generates a structured CSV report of all resolved Jira issues for a given month, mapping specific Jira fields into a standardized spreadsheet format for release tracking.
tools: Atlassian MCP, Python
---

## Purpose
Automates the creation of a monthly release report in CSV format based on Jira tickets from the 'SATU' project. The report extracts completed tasks (Stories, Improvements, Epics) and maps them to specific columns including Activities, Platform, Release Date, Year, Month, Initiatives, and a New/Improvement classification.

This skill assumes the AI agent starts from scratch and needs exact instructions on the JQL query, the fields to request, the data mapping logic, and the output format.

## Input
- **Target Month and Year**: The user should specify the month and year they want the report for (e.g., "March 2026").

## Tools Required
- `mcp_atlassian-mcp-server_searchJiraIssuesUsingJql`: To query the Jira database.
- `write_to_file` & `run_command`: To write and execute a Python script that parses the Jira JSON response into a CSV.

## Process

### Step 1: Query Jira Data
Use the Atlassian MCP tool (`searchJiraIssuesUsingJql`) with the following parameters:
- **jql**: `project = SATU AND resolutiondate >= "YYYY-MM-01" AND resolutiondate <= "YYYY-MM-end_of_month" AND issuetype IN (Story, Improvement, Epic) AND status = Done ORDER BY updated DESC`
  *(Replace the dates with the target month boundaries).*
- **maxResults**: `100` (or higher if needed).
- **fields**: `["summary", "components", "resolutiondate", "issuetype", "assignee", "labels"]`
  *(CRITICAL: You must explicitly request `resolutiondate` in the fields array, otherwise it may be missing from the API response).*

### Step 2: Parse and Map Data via Python
Once the Jira data is retrieved (usually saved to a local `.system_generated` output file by the MCP tool), use the included `generate_csv.py` script located in this skill's directory (`.agent/skills/jira-release-report/generate_csv.py`) to parse the JSON and write a CSV. 

Ensure the output CSV (`Jira_Release_Report.csv`) has the following **exact columns** and mapping logic:

1. **Activities**: Maps to the Jira `summary` field.
2. **Platform**: Maps to the Jira `components` field (join multiple component names with a comma).
3. **Release Date**: Maps to the `resolutiondate` field. Format this as `DD/MM/YYYY`.
4. **year**: Extract the year (YYYY) from `resolutiondate`.
5. **Month**: Extract the numeric month (e.g., `3`) from `resolutiondate`.
6. **Initiatives**: Determine if this is a "Product" or "Engineering" initiative.
   - *Logic suggestion: If `components` or `labels` contain "Back-End" or "eng", classify as "Engineering". Otherwise, default to "Product".*
7. **New/Improvement**: 
   - If `issuetype.name` is "Improvement", output `I`.
   - If `issuetype.name` is "Story" or "Epic", output `N` (New Feature).
8. **PIC**: Maps to the Jira `assignee.displayName`.

### Step 3: Execute and Deliver
1. Run the Python script using `run_command` with the input JSON file and output CSV file as arguments:
   `python ".agent/skills/jira-release-report/generate_csv.py" "<path_to_json_output>" "Jira_Release_Report_(month)_(year).csv"`
2. Verify the CSV was generated successfully.
3. Notify the user with the path to the generated `Jira_Release_Report_(month)_(year).csv`.

## Example Output Row
| Activities | Platform | Release Date | year | Month | Initiatives | New/Improvement | PIC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Web] Customer Support Modal | SMA (Mobile Apps), SWA (Web Apps) | 10/03/2026 | 2026 | 3 | Product | N | Luthfan Rasyad Maulana |
| Implement standard tracking | Back-End | 20/03/2026 | 2026 | 3 | Engineering | N | Zetra |

## How to Use
Just say: "Generate the Jira release report for [Month] [Year]" and the agent will execute the full query and CSV generation pipeline autonomously.
