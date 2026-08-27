import os

# 1. Update Obsidian note
obsidian_file = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana\Proyecto Web - Torre Edmond\Dossier Web - Torre Edmond (Fideicomiso Costa Posadas).md"
if os.path.exists(obsidian_file):
    with open(obsidian_file, "r", encoding="utf-8") as f:
        content = f.read()
    if "https://inmobiliariarp-arch.github.io/torre-edmon-web/" not in content:
        url_block = """
---

## 🌐 Enlaces Públicos en Vivo
* 🚀 **Sitio Web Oficial en Línea**: [https://inmobiliariarp-arch.github.io/torre-edmon-web/](https://inmobiliariarp-arch.github.io/torre-edmon-web/)
* 📊 **Catálogo y Curaduría de Renders**: [https://inmobiliariarp-arch.github.io/torre-edmon-web/catalogo_assets.html](https://inmobiliariarp-arch.github.io/torre-edmon-web/catalogo_assets.html)
* 🐙 **Repositorio GitHub**: [https://github.com/inmobiliariarp-arch/torre-edmon-web](https://github.com/inmobiliariarp-arch/torre-edmon-web)
"""
        content = content.strip() + "\n" + url_block.strip() + "\n"
        with open(obsidian_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Obsidian note updated with live URLs.")

# 2. Update README.md
readme_file = r"D:\Proyecto sitio web edificio\README.md"
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        rm = f.read()
    rm = rm.replace("https://<TU_USUARIO>.github.io/torre-edmon-web/", "https://inmobiliariarp-arch.github.io/torre-edmon-web/")
    rm = rm.replace("https://github.com", "https://inmobiliariarp-arch.github.io/torre-edmon-web/")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(rm)
    print("README.md updated with live URLs.")
