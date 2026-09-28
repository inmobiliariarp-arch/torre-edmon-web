import os
import shutil

v2_dir = r"D:\Proyecto sitio web edificio\assets\curated_v2"
legacy_ext = r"D:\Proyecto sitio web edificio\assets\curated\exterior"
legacy_int = r"D:\Proyecto sitio web edificio\assets\curated\interiores"
legacy_ame = r"D:\Proyecto sitio web edificio\assets\curated\amenities"

# 1. Video
shutil.copy2(r"D:\Proyecto sitio web edificio\assets\torre_edmon_anime_hero.mp4", r"D:\Proyecto sitio web edificio\assets\video_drone_costanera.mp4")
print("Video reemplazado.")

# 2. Exterior
shutil.copy2(os.path.join(v2_dir, "fachada_torre_edmon.webp"), os.path.join(legacy_ext, "exterior_02.webp"))
print("exterior_02.webp reemplazado.")

# 3. Interiores
shutil.copy2(os.path.join(v2_dir, "balcon_terraza_parrilla.webp"), os.path.join(legacy_int, "interiores_27.webp"))
shutil.copy2(os.path.join(v2_dir, "living_comedor_rio.webp"), os.path.join(legacy_int, "interiores_26.webp"))
shutil.copy2(os.path.join(v2_dir, "master_suite_dormitorio.webp"), os.path.join(legacy_int, "interiores_28.webp"))
shutil.copy2(os.path.join(v2_dir, "cocina_gourmet_isla.webp"), os.path.join(legacy_int, "interiores_24.webp"))
print("Interiores reemplazados.")

# 4. Amenities
shutil.copy2(os.path.join(v2_dir, "piscina_rooftop_solarium.webp"), os.path.join(legacy_ame, "amenities_31.webp"))
shutil.copy2(os.path.join(v2_dir, "piscina_rooftop_solarium.webp"), os.path.join(legacy_ame, "amenities_30.webp"))
shutil.copy2(os.path.join(v2_dir, "gimnasio_fitness_center.webp"), os.path.join(legacy_ame, "amenities_32.webp"))
shutil.copy2(os.path.join(v2_dir, "hall_acceso_lobby.webp"), os.path.join(legacy_ame, "amenities_12.webp"))
print("Amenities reemplazados.")
