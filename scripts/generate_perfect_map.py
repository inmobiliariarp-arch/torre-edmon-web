import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

src_path = r"C:\Users\Administrator\.gemini\antigravity\brain\0c0b1ebb-7144-4b40-bf91-0da2839751f2\.user_uploaded\media_1787842963313.jpg"

img_bgr = cv2.imread(src_path)
h, w, c = img_bgr.shape
print(f"Original size: {w}x{h}")

# The user drew a black star near the coast on top right:
# Let's inspect coordinates around x: 740-760, y: 70-100
# Inpainting the black star
star_cx, star_cy = 751, 84
mask = np.zeros((h, w), dtype=np.uint8)
cv2.circle(mask, (star_cx, star_cy), 18, 255, -1)
inpainted_bgr = cv2.inpaint(img_bgr, mask, 5, cv2.INPAINT_TELEA)

pil_img = Image.fromarray(cv2.cvtColor(inpainted_bgr, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img, "RGBA")

# Draw a VERY clear, prominent, high-end location PIN with pulse rings and label
cx, cy = star_cx, star_cy

# 1. Subtle glowing pulse radar circles at base
draw.ellipse([cx - 24, cy - 8, cx + 24, cy + 8], fill=(197, 160, 89, 60), outline=(240, 210, 134, 180), width=2)
draw.ellipse([cx - 12, cy - 4, cx + 12, cy + 4], fill=(197, 160, 89, 140))

# 2. Main Location Pin (Droplet shape)
pin_h = 56
pin_top_y = cy - pin_h

# Shadow under pin
draw.ellipse([cx - 14, cy - 3, cx + 14, cy + 5], fill=(0, 0, 0, 180))

# Pin body with luxury gold gradient styling
# Outer red/gold pin body
draw.polygon([(cx - 16, pin_top_y + 24), (cx + 16, pin_top_y + 24), (cx, cy)], fill=(220, 38, 38, 255), outline=(255, 255, 255, 255))
draw.ellipse([cx - 20, pin_top_y, cx + 20, pin_top_y + 40], fill=(220, 38, 38, 255), outline=(255, 255, 255, 255), width=3)

# Inner white circle
draw.ellipse([cx - 12, pin_top_y + 8, cx + 12, pin_top_y + 32], fill=(255, 255, 255, 255))

# Center gold icon or building
draw.ellipse([cx - 7, pin_top_y + 13, cx + 7, pin_top_y + 27], fill=(197, 160, 89, 255))

# 3. Prominent Luxury Badge above the Pin
badge_text = "★ TORRE EDMON"
badge_w = 160
badge_h = 32
bx1 = cx - badge_w // 2
by1 = pin_top_y - 42
bx2 = bx1 + badge_w
by2 = by1 + badge_h

# Draw badge shadow & background
draw.rounded_rectangle([bx1 + 2, by1 + 3, bx2 + 2, by2 + 3], radius=16, fill=(0, 0, 0, 160))
draw.rounded_rectangle([bx1, by1, bx2, by2], radius=16, fill=(15, 18, 23, 245), outline=(240, 210, 134, 255), width=2)

try:
    font = ImageFont.truetype("arialbd.ttf", 14)
except:
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

bbox = font.getbbox(badge_text)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text((cx - tw // 2, by1 + (badge_h - th) // 2 - 2), badge_text, font=font, fill=(240, 210, 134, 255))

# Save outputs in multiple strategic locations
paths = [
    r"D:\Proyecto sitio web edificio\assets\curated\exterior\mapa_ubicacion_masterplan.webp",
    r"D:\Proyecto sitio web edificio\assets\mapa_ubicacion_masterplan.webp",
    r"D:\Proyecto sitio web edificio\assets\catalog_previews\render_35_mapa_masterplan.webp",
    r"D:\Proyecto sitio web edificio\assets\raw_pure_extracted\img_35_mapa_masterplan.jpeg"
]

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    pil_img.save(p, "WEBP" if p.endswith(".webp") else "JPEG", quality=95)
    print(f"Guardado exitosamente: {p}")
