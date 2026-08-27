import os

obsidian_root = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana"

# 1. Update 00 - Dossier Inmobiliario Maestro.md
file_00 = os.path.join(obsidian_root, "00 - Dossier Inmobiliario Maestro.md")
with open(file_00, "r", encoding="utf-8") as f:
    content_00 = f.read()

if "Dossier Web - Torre Edmond" not in content_00:
    target = " ┣ 🏙️ [[Dossier Completo - Torre Edmond]] (Folletería, plantas tipo y amenities)\n"
    replacement = target + " ┣ 🌐 [[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]] (Sitio web interactivo, arquitectura y visualización digital)\n"
    if target in content_00:
        content_00 = content_00.replace(target, replacement)
    else:
        # fallback insertion
        content_00 = content_00.replace("[[Dossier Completo - Torre Edmond]]", "[[Dossier Completo - Torre Edmond]]\n ┣ 🌐 [[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]]")
    with open(file_00, "w", encoding="utf-8") as f:
        f.write(content_00)
    print("00 - Dossier Inmobiliario Maestro actualizado.")

# 2. Update Dossier Completo - Torre Edmond.md
file_edmond = os.path.join(obsidian_root, "Dossier Completo - Torre Edmond.md")
with open(file_edmond, "r", encoding="utf-8") as f:
    content_edmond = f.read()

if "Dossier Web - Torre Edmond" not in content_edmond:
    web_section = """
---

## 🌐 Sitio Web Oficial y Material Digital
* 💻 **Dossier del Proyecto Web**: [[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]]
* 🛠️ **Manual de Arquitectura**: [[Manual de Arquitectura y Tecnologias Web]]
* 🎨 **Catálogo de Renders y Assets**: [[Catalogo de Activos y Renders]]
* 🚀 **Guía de Despliegue y Hosting**: [[Guia de Despliegue y Mantenimiento]]
* 🏛️ **Fideicomiso Administrador**: [[Dossier Completo - Fideicomiso Costa Posadas]]
* 📁 Carpeta del Proyecto Web: [D:\\Proyecto sitio web edificio](file:///D:/Proyecto%20sitio%20web%20edificio)
"""
    content_edmond = content_edmond.strip() + "\n" + web_section.strip() + "\n"
    with open(file_edmond, "w", encoding="utf-8") as f:
        f.write(content_edmond)
    print("Dossier Completo - Torre Edmond actualizado.")

# 3. Update Dossier Completo - Fideicomiso Costa Posadas.md
file_fideicomiso = os.path.join(obsidian_root, "Dossier Completo - Fideicomiso Costa Posadas.md")
with open(file_fideicomiso, "r", encoding="utf-8") as f:
    content_fideicomiso = f.read()

if "Dossier Web - Torre Edmond" not in content_fideicomiso:
    web_section_fide = """
---

## 🌐 Emprendimientos y Canales Digitales Activos
* 🏢 **Torre Edmond (Posadas)**: [[Dossier Completo - Torre Edmond]]
* 💻 **Sitio Web Oficial Torre Edmond**: [[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]] (Plataforma interactiva 3D y selector de tipologías para inversores).
"""
    content_fideicomiso = content_fideicomiso.strip() + "\n" + web_section_fide.strip() + "\n"
    with open(file_fideicomiso, "w", encoding="utf-8") as f:
        f.write(content_fideicomiso)
    print("Dossier Completo - Fideicomiso Costa Posadas actualizado.")
