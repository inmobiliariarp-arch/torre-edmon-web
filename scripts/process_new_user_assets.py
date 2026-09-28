import os
import shutil
from PIL import Image

src_dir = r"C:\Users\Administrator\Desktop\Nueva carpeta"
target_dir = r"D:\Proyecto sitio web edificio\assets\curated_v2"
os.makedirs(target_dir, exist_ok=True)

# 1. Video
video_src = os.path.join(src_dir, "Anime.mp4")
video_dst = r"D:\Proyecto sitio web edificio\assets\torre_edmon_anime_hero.mp4"
shutil.copy2(video_src, video_dst)
print("Video Anime.mp4 copiado como torre_edmon_anime_hero.mp4")

# Extract video poster frame
try:
    import cv2
    cap = cv2.VideoCapture(video_dst)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 60) # frame at ~2.5s
    ret, frame = cap.read()
    if ret:
        poster_jpg = os.path.join(target_dir, "hero_poster.jpg")
        poster_webp = os.path.join(target_dir, "hero_poster.webp")
        cv2.imwrite(poster_jpg, frame)
        Image.open(poster_jpg).save(poster_webp, "WEBP", quality=90)
        print("Hero poster extraido y guardado como WebP.")
    cap.release()
except Exception as e:
    print("Error extrayendo poster:", e)

# 2. Process and optimize all images to WebP and high quality
image_map = {
    "Gemini_Generated_Image_xl9l4rxl9l4rxl9l.jfif": "fachada_torre_edmon.webp",
    "balcon.png": "balcon_terraza_parrilla.webp",
    "Living.png": "living_comedor_rio.webp",
    "Habitacion.jfif": "master_suite_dormitorio.webp",
    "Cocina.jfif": "cocina_gourmet_isla.webp",
    "Piscina.jfif": "piscina_rooftop_solarium.webp",
    "gym.jfif": "gimnasio_fitness_center.webp",
    "Hall acceso.jfif": "hall_acceso_lobby.webp",
    "Gemini_Generated_Image_qeig06qeig06qeig.jfif": "living_nocturno_rio.webp",
    "render_cocina_hacia_social_dreamina.jpg": "cocina_vista_social.webp"
}

for src_name, dst_name in image_map.items():
    src_fp = os.path.join(src_dir, src_name)
    if os.path.exists(src_fp):
        dst_fp = os.path.join(target_dir, dst_name)
        im = Image.open(src_fp)
        # convert if RGBA to RGB for webp
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        im.save(dst_fp, "WEBP", quality=92, method=6)
        print(f"Convertido: {src_name} -> {dst_name} ({im.size})")
    else:
        print(f"No encontrado: {src_name}")

print("Procesamiento de activos completado exitosamente.")
