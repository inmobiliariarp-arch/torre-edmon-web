import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'(?:src|href)=["\']([^"\']+)["\']', html)
missing = []
for m in matches:
    if not m.startswith('http') and not m.startswith('#') and not m.startswith('mailto') and not m.startswith('tel') and not m.startswith('javascript:'):
        if not os.path.exists(m):
            missing.append(m)

print(f"Total local references checked: {len(matches)}")
if missing:
    print("Missing files:", missing)
else:
    print("All local asset and script paths are 100% valid!")
