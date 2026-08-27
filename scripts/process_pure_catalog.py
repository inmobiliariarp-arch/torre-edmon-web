import os
from PIL import Image

os.makedirs("assets/nuevas_imagenes_usuario", exist_ok=True)
os.makedirs("assets/catalog_previews", exist_ok=True)

raw_dir = "assets/raw_pure_extracted"
files = [f for f in sorted(os.listdir(raw_dir)) if f.endswith(('.jpeg', '.jpg', '.png'))]

catalog_items = []
valid_id = 0

for filename in files:
    src_path = os.path.join(raw_dir, filename)
    img = Image.open(src_path)
    w, h = img.size
    
    # Ignore small logos/sub-icons < 600px width
    if w < 600 or h < 600:
        continue
        
    valid_id += 1
    out_name = f"render_{valid_id:02d}.webp"
    out_path = os.path.join("assets/catalog_previews", out_name)
    
    # Save optimized webp for instant loading
    img.save(out_path, "WEBP", quality=85, method=4)
    size_kb = os.path.getsize(out_path) / 1024
    
    catalog_items.append({
        "id": valid_id,
        "filename": filename,
        "preview": f"assets/catalog_previews/{out_name}",
        "original_res": f"{w}x{h}",
        "size_kb": round(size_kb, 1)
    })

print(f"Total pure renders processed for catalog: {len(catalog_items)}")
