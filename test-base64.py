import base64
import json
import urllib.request
import os

with open('asset/09-additional-topics_0.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

md_content = f"![Chart](data:image/png;base64,{b64})\nThis is a test base64 image."
print("Done base64 encoding")

# Write to a file instead of testing via python to allow MCP testing directly
with open('test-base64.md', 'w') as f:
    f.write(md_content)
