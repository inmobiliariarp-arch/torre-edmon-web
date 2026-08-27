import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

src_path = r"C:\Users\Administrator\.gemini\antigravity\brain\0c0b1ebb-7144-4b40-bf91-0da2839751f2\.user_uploaded\media_1787842963313.jpg"
out_path = r"D:\Proyecto sitio web edificio\assets\curated\exterior\mapa_ubicacion.webp"

img_bgr = cv2.imread(src_path)
h, w, c = img_bgr.shape
print(f"Dimensiones de la imagen: {w}x{h}")

# The star is roughly in the top-right quadrant (x between 65% and 85%, y between 10% and 25%)
roi_x1, roi_x2 = int(w * 0.65), int(w * 0.85)
roi_y1, roi_y2 = int(h * 0.08), int(h * 0.25)
roi = img_bgr[roi_y1:roi_y2, roi_x1:roi_x2]

# Detect the very dark/black pixels of the drawn star in ROI
gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray_roi, 30, 255, cv2.THRESH_BINARY_INV)

# Find contours in ROI
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
best_contour = None
max_area = 0

for cnt in contours:
    area = cv2.contourArea(cnt)
    if 50 < area < 5000:
        if area > max_area:
            max_area = area
            best_contour = cnt

if best_contour is not None:
    M = cv2.moments(best_contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"]) + roi_x1
        cy = int(M["m01"] / M["m00"]) + roi_y1
        print(f"Estrella encontrada exactamente en: ({cx}, {cy})")
    else:
        cx, cy = int(w * 0.732), int(h * 0.160)
else:
    # Fallback to approximate visual coordinate
    cx, cy = int(w * 0.732), int(h * 0.160)
    print(f"Coordenada aproximada: ({cx}, {cy})")

# Inpaint the black star to clean the background before drawing the luxury pin
mask = np.zeros((h, w), dtype=np.uint8)
cv2.circle(mask, (cx, cy), 22, 255, -1)
inpainted_bgr = cv2.inpaint(img_bgr, mask, 7, cv2.INPAINT_TELEA)

# Convert to PIL for anti-aliased luxury PIN drawing
pil_img = Image.fromarray(cv2.cvtColor(inpainted_bgr, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img, "RGBA")

# Draw a Luxury Architectural Gold Pin at (cx, cy)
pin_color_gold = (197, 160, 89, 255)
pin_color_gold_light = (240, 210, 134, 255)
pin_color_black = (10, 12, 16, 240)
pin_shadow = (0, 0, 0, 140)

# Pin shadow at bottom
draw.ellipse([cx - 16, cy - 4, cx + 16, cy + 6], fill=pin_shadow)

# Pin Body dimensions
pin_h = 60
pin_w = 40
top_cy = cy - pin_h + 20

# Draw Pin droplet shape
# Top circle
draw.ellipse([cx - 20, top_cy - 20, cx + 20, top_cy + 20], fill=pin_color_black, outline=pin_color_gold, width=3)
# Bottom point triangle
draw.polygon([(cx - 14, top_cy + 10), (cx + 14, top_cy + 10), (cx, cy)], fill=pin_color_black, outline=pin_color_gold)
# Redraw inner circle
draw.ellipse([cx - 14, top_cy - 14, cx + 14, top_cy + 14], fill=pin_color_gold_light)
draw.ellipse([cx - 9, top_cy - 9, cx + 9, top_cy + 9], fill=pin_color_black)

# Add a sleek luxury floating label badge above the pin: "TORRE EDMON"
badge_w = 140
badge_h = 28
bx1 = cx - badge_w // 2
by1 = top_cy - 46
bx2 = bx1 + badge_w
by2 = by1 + badge_h

# Badge background
draw.rounded_rectangle([bx1, by1, bx2, by2], radius=14, fill=(10, 12, 16, 245), outline=pin_color_gold, width=2)

try:
    font = ImageFont.truetype("arial.ttf", 13)
except:
    font = ImageFont.load_default()

text = "TORRE EDMON"
bbox = font.getbbox(text)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text((cx - tw // 2, by1 + (badge_h - th) // 2 - 2), text, font=font, fill=pin_color_gold_light)

# Save as WebP
pil_img.save(out_path, "WEBP", quality=92, method=6)
print(f"Mapa procesado y guardado con éxito en: {out_path} ({w}x{h})")
