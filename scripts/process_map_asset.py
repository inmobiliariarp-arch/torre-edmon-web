from PIL import Image
import os

src_map = r"C:\Users\Administrator\.gemini\antigravity\brain\0c0b1ebb-7144-4b40-bf91-0da2839751f2\.user_uploaded\media_1787841922788.png"
dst_map = r"D:\Proyecto sitio web edificio\assets\curated\exterior\mapa_ubicacion.webp"

if os.path.exists(src_map):
    img = Image.open(src_map)
    # Convert and optimize
    img.save(dst_map, "WEBP", quality=92, method=6)
    print(f"Mapa de ubicacion procesado exitosamente en: {dst_map} ({img.size[0]}x{img.size[1]})")
else:
    print(f"Archivo de origen no encontrado: {src_map}")
