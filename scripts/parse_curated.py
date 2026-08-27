import json

with open("assets/data/assets_curados_edmon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total items curated by user: {len(data)}")
by_cat = {}
for k, v in sorted(data.items(), key=lambda x: int(x[0])):
    cat = v.get("category", "sin_categoria")
    by_cat.setdefault(cat, []).append((k, v.get("label", ""), v.get("cropData", {})))
    crop = v.get("cropData")
    crop_str = f"{crop.get('width')}x{crop.get('height')} @ ({crop.get('x')}, {crop.get('y')})" if crop else "Full"
    print(f"ID #{k:>2} -> Cat: {cat.upper():<12} | Label: '{v.get('label', '')}' | Crop: {crop_str}")

print("\nSummary by Category:")
for c, lst in by_cat.items():
    print(f"  • {c.upper()}: {len(lst)} items {[x[0] for x in lst]}")
