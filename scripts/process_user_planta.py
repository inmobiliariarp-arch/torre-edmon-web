import os
from PIL import Image

os.makedirs("assets/plantas", exist_ok=True)
os.makedirs("assets/catalog_previews", exist_ok=True)

src = "assets/plantas render.png"
if os.path.exists(src):
    img = Image.open(src)
    # Save in plantas
    out_plantas = "assets/plantas/planta_distribucion_render.webp"
    img.save(out_plantas, "WEBP", quality=90, method=5)
    
    # Save preview for catalog
    out_catalog = "assets/catalog_previews/render_34_planta_render.webp"
    img.save(out_catalog, "WEBP", quality=88, method=5)
    
    print(f"Planta render guardada en WebP: {os.path.getsize(out_plantas)/1024:.1f} KB")
