with open("catalogo_assets.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
match = re.search(r'const ASSETS_DATA = (\[.*?\]);', html, re.DOTALL)
if match:
    import json
    data = json.loads(match.group(1))
    print(f"Total items in ASSETS_DATA: {len(data)}")
    for d in data[-5:]:
        print(d["id"], d.get("filename"), d.get("default_label"), d.get("raw"))
else:
    print("No se encontró ASSETS_DATA")
