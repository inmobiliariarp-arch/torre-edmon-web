import json
import os
from PIL import Image

manifest_json = """{
  "10": {
    "id": "10",
    "filename": "img_10_p10_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_10_p10_2420x1361.jpeg",
    "category": "exterior",
    "label": "Render #10",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:50:09.529Z"
  },
  "11": {
    "id": "11",
    "filename": "img_11_p11_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_11_p11_2666x1499.jpeg",
    "category": "descartar",
    "label": "Render #11",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:50:22.487Z"
  },
  "12": {
    "id": "12",
    "filename": "img_12_p12_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_12_p12_2420x1361.jpeg",
    "category": "amenities",
    "label": "Hall acceso",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:31:57.165Z"
  },
  "13": {
    "id": "13",
    "filename": "img_13_p13_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_13_p13_2420x1361.jpeg",
    "category": "exterior",
    "label": "Render #13",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:52:43.857Z"
  },
  "14": {
    "id": "14",
    "filename": "img_14_p14_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_14_p14_2420x1361.jpeg",
    "category": "amenities",
    "label": "Hall acceso",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:32:30.137Z"
  },
  "15": {
    "id": "15",
    "filename": "img_15_p15_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_15_p15_2420x1361.jpeg",
    "category": "exterior",
    "label": "Render #15",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:52:55.563Z"
  },
  "16": {
    "id": "16",
    "filename": "img_16_p16_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_16_p16_2420x1361.jpeg",
    "category": "exterior",
    "label": "Render #16",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:53:00.299Z"
  },
  "17": {
    "id": "17",
    "filename": "img_17_p17_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_17_p17_2420x1361.jpeg",
    "category": "exterior",
    "label": "Hall acceso",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:32:47.662Z"
  },
  "18": {
    "id": "18",
    "filename": "img_18_p18_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_18_p18_2420x1361.jpeg",
    "category": "exterior",
    "label": "Render #18",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:53:10.812Z"
  },
  "19": {
    "id": "19",
    "filename": "img_19_p19_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_19_p19_2420x1361.jpeg",
    "category": "exterior",
    "label": "Hall acceso nocturno",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:33:06.340Z"
  },
  "20": {
    "id": "20",
    "filename": "img_20_p20_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_20_p20_2666x1499.jpeg",
    "category": "descartar",
    "label": "Render #20",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:50:41.808Z"
  },
  "21": {
    "id": "21",
    "filename": "img_21_p21_2934x1651.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_21_p21_2934x1651.jpeg",
    "category": "descartar",
    "label": "Render #21",
    "cropData": {
      "x": 73,
      "y": 41,
      "width": 2788,
      "height": 1569,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:50:48.347Z"
  },
  "22": {
    "id": "22",
    "filename": "img_23_p22_2934x1651.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_23_p22_2934x1651.jpeg",
    "category": "descartar",
    "label": "Render #22",
    "cropData": {
      "x": 354,
      "y": 500,
      "width": 1411,
      "height": 845,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:33:20.386Z"
  },
  "23": {
    "id": "23",
    "filename": "img_25_p23_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_25_p23_2666x1499.jpeg",
    "category": "descartar",
    "label": "Render #23",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:33:38.641Z"
  },
  "24": {
    "id": "24",
    "filename": "img_26_p24_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_26_p24_2666x1499.jpeg",
    "category": "interiores",
    "label": "Cocina",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:33:55.038Z"
  },
  "25": {
    "id": "25",
    "filename": "img_27_p25_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_27_p25_2420x1361.jpeg",
    "category": "descartar",
    "label": "Render #25",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:53:53.285Z"
  },
  "26": {
    "id": "26",
    "filename": "img_28_p26_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_28_p26_2420x1361.jpeg",
    "category": "interiores",
    "label": "Living",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:34:09.300Z"
  },
  "27": {
    "id": "27",
    "filename": "img_29_p27_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_29_p27_2420x1361.jpeg",
    "category": "interiores",
    "label": "Balcon",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:34:18.480Z"
  },
  "28": {
    "id": "28",
    "filename": "img_30_p28_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_30_p28_2420x1361.jpeg",
    "category": "interiores",
    "label": "Master bedroom",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 2298,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:34:37.509Z"
  },
  "29": {
    "id": "29",
    "filename": "img_31_p29_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_31_p29_2666x1499.jpeg",
    "category": "descartar",
    "label": "Render #29",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:54:20.375Z"
  },
  "30": {
    "id": "30",
    "filename": "img_32_p30_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_32_p30_2666x1499.jpeg",
    "category": "amenities",
    "label": "Solarium en terraza",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2268,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:35:04.042Z"
  },
  "31": {
    "id": "31",
    "filename": "img_33_p31_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_33_p31_2666x1499.jpeg",
    "category": "amenities",
    "label": "Piscina en terraza",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:54:50.536Z"
  },
  "32": {
    "id": "32",
    "filename": "img_34_p32_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_34_p32_2666x1499.jpeg",
    "category": "amenities",
    "label": "SUM quincho",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:35:11.219Z"
  },
  "33": {
    "id": "33",
    "filename": "img_35_p33_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_35_p33_2666x1499.jpeg",
    "category": "branding",
    "label": "logo inmobiliaria rio parana",
    "cropData": {
      "x": 770,
      "y": 255,
      "width": 1172,
      "height": 984,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:55:29.137Z"
  },
  "34": {
    "id": "34",
    "filename": "plantas render.png",
    "raw_path": "assets/plantas render.png",
    "category": "plantas",
    "label": "distribucion",
    "cropData": {
      "x": 42,
      "y": 24,
      "width": 1588,
      "height": 893,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T14:35:28.217Z"
  },
  "02": {
    "id": "02",
    "filename": "img_02_p02_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_02_p02_2420x1361.jpeg",
    "category": "exterior",
    "label": "Fachada principal",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 1580,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:47:16.491Z"
  },
  "03": {
    "id": "03",
    "filename": "img_03_p03_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_03_p03_2666x1499.jpeg",
    "category": "exterior",
    "label": "Ubicacion del edificio",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 1967,
      "height": 1313,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:48:50.228Z"
  },
  "05": {
    "id": "05",
    "filename": "img_05_p05_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_05_p05_2420x1361.jpeg",
    "category": "exterior",
    "label": "Entorno costero",
    "cropData": {
      "x": 729,
      "y": 34,
      "width": 1681,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:49:14.544Z"
  },
  "06": {
    "id": "06",
    "filename": "img_06_p06_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_06_p06_2666x1499.jpeg",
    "category": "exterior",
    "label": "Vista diurna",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:49:30.039Z"
  },
  "07": {
    "id": "07",
    "filename": "img_07_p07_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_07_p07_2420x1361.jpeg",
    "category": "exterior",
    "label": "Fachada y calle",
    "cropData": {
      "x": 531,
      "y": 34,
      "width": 1829,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:49:39.033Z"
  },
  "08": {
    "id": "08",
    "filename": "img_08_p08_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_08_p08_2420x1361.jpeg",
    "category": "exterior",
    "label": "Balcones al rio",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 1916,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:49:50.645Z"
  },
  "09": {
    "id": "09",
    "filename": "img_09_p09_2420x1361.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_09_p09_2420x1361.jpeg",
    "category": "exterior",
    "label": "Detalles arquitectura",
    "cropData": {
      "x": 61,
      "y": 34,
      "width": 1878,
      "height": 1293,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:50:01.384Z"
  },
  "01": {
    "id": "01",
    "filename": "img_01_p01_2666x1499.jpeg",
    "raw_path": "assets/raw_pure_extracted/img_01_p01_2666x1499.jpeg",
    "category": "branding",
    "label": "Logo del edificio",
    "cropData": {
      "x": 67,
      "y": 37,
      "width": 2532,
      "height": 1425,
      "rotate": 0,
      "scaleX": 1,
      "scaleY": 1
    },
    "cropped_preview": null,
    "timestamp": "2026-08-27T13:52:08.096Z"
  }
}"""

manifest = json.loads(manifest_json)

# Guardar en archivo
with open("assets/data/assets_curados_edmon.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

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

processed_catalog = {
    "exterior": [],
    "amenities": [],
    "interiores": [],
    "plantas": [],
    "branding": []
}

print(f"Reprocesando {len(manifest)} items del usuario...")

for item_id, item_data in sorted(manifest.items(), key=lambda x: int(x[0])):
    cat = item_data.get("category", "").lower()
    if cat == "descartar" or not cat:
        print(f"[-] Saltando ID #{item_id} (Descartado)")
        continue

    raw_path = item_data.get("raw_path")
    if not os.path.exists(raw_path):
        print(f"[!] No existe: {raw_path}")
        continue

    img = Image.open(raw_path)
    img_w, img_h = img.size

    crop_data = item_data.get("cropData")
    if crop_data:
        x = max(0, int(round(crop_data.get("x", 0))))
        y = max(0, int(round(crop_data.get("y", 0))))
        cw = int(round(crop_data.get("width", img_w)))
        ch = int(round(crop_data.get("height", img_h)))
        x2 = min(img_w, x + cw)
        y2 = min(img_h, y + ch)
        if x2 > x and y2 > y:
            cropped_img = img.crop((x, y, x2, y2))
        else:
            cropped_img = img
    else:
        cropped_img = img

    label = item_data.get("label", "").strip()
    target_cat = cat
    if "logo" in label.lower() or item_id in ["01", "33"]:
        target_cat = "branding"

    # Nombrado claro
    out_filename = f"{target_cat}_{item_id}.webp"
    out_filepath = f"{OUT_BASE}/{target_cat}/{out_filename}"

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
        "label": label if label else f"Item #{item_id}",
        "src": out_filepath,
        "width": final_w,
        "height": final_h,
        "size_kb": round(file_size_kb, 1)
    }

    processed_catalog[target_cat].append(item_info)
    print(f"[+] ID #{item_id:0>2} ({label}) -> {out_filepath} ({final_w}x{final_h})")

with open("assets/data/catalogo_curado_definitivo.json", "w", encoding="utf-8") as f:
    json.dump(processed_catalog, f, ensure_ascii=False, indent=2)

print("\n¡Reprocesamiento exacto completado!")
