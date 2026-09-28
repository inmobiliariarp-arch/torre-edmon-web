import re
import os

with open(r"D:\Proyecto sitio web edificio\index.html", "r", encoding="utf-8") as f:
    content = f.read()

srcs = re.findall(r'(?:src|data-hires|poster)=["\']([^"\']+)["\']', content)
print(f"Total asset paths to check: {len(srcs)}")
missing = []
for s in srcs:
    if s.startswith(("http://", "https://", "data:")):
        continue
    p = os.path.join(r"D:\Proyecto sitio web edificio", s.replace("/", os.sep))
    if not os.path.exists(p):
        missing.append(s)
        print("MISSING:", s)

if not missing:
    print("SUCCESS: ALL ASSET PATHS IN index.html EXIST AND ARE 100% VALID!")
