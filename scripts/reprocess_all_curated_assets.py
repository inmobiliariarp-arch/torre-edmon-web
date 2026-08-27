import os
import json
from PIL import Image

# 1. Directorios de salida limpios
OUT_BASE = "assets/curated"
DIRS = [
    f"{OUT_BASE}/exterior",
    f"{OUT_BASE}/amenities",
    f"{OUT_BASE}/interiores",
    f"{OUT_BASE}/plantas",
    f"{OUT_BASE}/branding"
]

for d in DIRS:
    os.makedirs(d, exist_ok=True)

with open("assets/data/assets_curados_edmon.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

processed_catalog = {
    "exterior": [],
    "amenities": [],
    "interiores": [],
    "plantas": [],
    "branding": []
}

print(f"Iniciando reprocesamiento de {len(manifest)} items curados...")

for item_id, item_data in sorted(manifest.items(), key=lambda x: int(x[0])):
    cat = item_data.get("category", "").lower()
    if cat == "descartar" or not cat:
        print(f"[-] Saltando ID #{item_id} (Descartado)")
        continue

    raw_path = item_data.get("raw_path")
    if not os.path.exists(raw_path):
        print(f"[!] Archivo no encontrado: {raw_path}")
        continue

    img = Image.open(raw_path)
    img_w, img_h = img.size

    # Aplicar coordenadas de recorte exactas del usuario
    crop_data = item_data.get("cropData")
    if crop_data:
        x = max(0, int(round(crop_data.get("x", 0))))
        y = max(0, int(round(crop_data.get("y", 0))))
        cw = int(round(crop_data.get("width", img_w)))
        ch = int(round(crop_data.get("height", img_h)))
        
        # Limitar dentro de los límites de la imagen
        x2 = min(img_w, x + cw)
        y2 = min(img_h, y + ch)
        
        if x2 > x and y2 > y:
            cropped_img = img.crop((x, y, x2, y2))
        else:
            cropped_img = img
    else:
        cropped_img = img

    # Tratamiento especial para logos
    label = item_data.get("label", "")
    if "logo" in label.lower() or item_id in ["01", "33"]:
        target_cat = "branding"
    else:
        target_cat = cat

    # Guardar en WebP de alta fidelidad
    out_filename = f"{target_cat}_{item_id}.webp"
    out_filepath = f"{OUT_BASE}/{target_cat}/{out_filename}"
    
    # Redimensionar suavemente si supera 2400px de ancho manteniendo nitidez
    final_w, final_h = cropped_img.size
    if final_w > 2200:
        new_h = int(final_h * (2200 / final_w))
        cropped_img = cropped_img.resize((2200, new_h), Image.Resampling.LANCZOS)
        final_w, final_h = cropped_img.size

    cropped_img.save(out_filepath, "WEBP", quality=90, method=5)
    file_size_kb = os.path.getsize(out_filepath) / 1024

    item_info = {
        "id": item_id,
        "category": target_cat,
        "label": label if label and not label.startswith("Render #") else f"Vista {target_cat.capitalize()} #{item_id}",
        "src": out_filepath,
        "width": final_w,
        "height": final_h,
        "size_kb": round(file_size_kb, 1)
    }

    processed_catalog[target_cat].append(item_info)
    print(f"[+] ID #{item_id} -> {out_filepath} ({final_w}x{final_h}, {file_size_kb:.1f} KB)")

# Guardar catalogo definitivo en JSON
with open("assets/data/catalogo_curado_definitivo.json", "w", encoding="utf-8") as f:
    json.dump(processed_catalog, f, ensure_ascii=False, indent=2)

print("\n¡Reprocesamiento completado con éxito!")
for c, lst in processed_catalog.items():
    print(f"  • {c.upper()}: {len(lst)} imágenes listas")
