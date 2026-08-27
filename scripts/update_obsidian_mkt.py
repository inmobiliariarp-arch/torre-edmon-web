import os

obsidian_root = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana"

# 1. Update Dossier Web
dossier_web = os.path.join(obsidian_root, "Proyecto Web - Torre Edmond", "Dossier Web - Torre Edmond (Fideicomiso Costa Posadas).md")
if os.path.exists(dossier_web):
    with open(dossier_web, "r", encoding="utf-8") as f:
        content = f.read()
    if "Estrategia de Marketing y Redes Sociales" not in content:
        content = content.replace(
            "- 🚀 [[Guia de Despliegue y Mantenimiento]]",
            "- 🚀 [[Guia de Despliegue y Mantenimiento]]\n- 📢 [[Estrategia de Marketing y Redes Sociales]]: Campaña orgánica 100% gratuita para Google, IG, TikTok, FB y WhatsApp."
        )
        with open(dossier_web, "w", encoding="utf-8") as f:
            f.write(content)
        print("Dossier Web actualizado con link a Estrategia de Marketing.")

# 2. Update Dossier Completo - Torre Edmond
dossier_edmond = os.path.join(obsidian_root, "Dossier Completo - Torre Edmond.md")
if os.path.exists(dossier_edmond):
    with open(dossier_edmond, "r", encoding="utf-8") as f:
        content = f.read()
    if "Estrategia de Marketing y Redes Sociales" not in content:
        content = content.replace(
            "* 🚀 **Guía de Despliegue y Hosting**: [[Guia de Despliegue y Mantenimiento]]",
            "* 🚀 **Guía de Despliegue y Hosting**: [[Guia de Despliegue y Mantenimiento]]\n* 📢 **Campaña de Marketing Digital**: [[Estrategia de Marketing y Redes Sociales]]"
        )
        with open(dossier_edmond, "w", encoding="utf-8") as f:
            f.write(content)
        print("Dossier Completo - Torre Edmond actualizado.")
