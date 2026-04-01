import json
import csv
from datetime import datetime

import sys

if len(sys.argv) < 3:
    print("Usage: python generate_csv.py <input_json_file> <output_csv_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

def get_initiative(issue):
    # Try to guess initiative, maybe from labels or custom fields
    labels = issue.get("fields", {}).get("labels", [])
    if labels:
        if any("eng" in l.lower() for l in labels): return "Engineering"
        if any("prod" in l.lower() for l in labels): return "Product"
    
    # Try components
    components = [c.get("name", "") for c in issue.get("fields", {}).get("components", [])]
    if any("Back-End" in c or "Front-End" in c for c in components):
        return "Engineering"
        
    return "Product"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

issues = data.get("issues", [])

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Activities", "Platform", "Release Date", "year", "Month", "Initiatives", "New/Improvement", "PIC"])

    for issue in issues:
        fields = issue.get("fields", {})
        
        # Activities
        activities = fields.get("summary", "")
        
        # Platform
        components = fields.get("components", [])
        platform = ", ".join([c.get("name", "") for c in components])
        
        # Release Date, year, Month
        res_date_str = fields.get("resolutiondate", "")
        release_date = ""
        year = ""
        month = ""
        if res_date_str:
            # e.g., 2026-03-30T12:26:02.641+0700
            try:
                dt = datetime.strptime(res_date_str[:19], "%Y-%m-%dT%H:%M:%S")
                release_date = dt.strftime("%d/%m/%Y")
                year = dt.strftime("%Y")
                month = dt.strftime("%m")
                # Remove leading zero for month to match "string/number" if needed
                month = str(int(month))
            except Exception as e:
                pass
                
        # Initiatives
        initiatives = get_initiative(issue)
        
        # New/Improvement
        issue_type = fields.get("issuetype", {}).get("name", "")
        new_imp = "I" if issue_type == "Improvement" else ("N" if issue_type in ["Story", "Epic"] else "")
        
        # PIC
        assignee = fields.get("assignee")
        pic = assignee.get("displayName", "") if assignee else ""
        
        writer.writerow([activities, platform, release_date, year, month, initiatives, new_imp, pic])

print(f"Generated CSV with {len(issues)} issues at: {output_file}")
