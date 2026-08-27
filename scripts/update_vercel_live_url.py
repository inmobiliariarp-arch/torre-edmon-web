import os

# 1. Update Obsidian note
obsidian_file = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana\Proyecto Web - Torre Edmond\Dossier Web - Torre Edmond (Fideicomiso Costa Posadas).md"
if os.path.exists(obsidian_file):
    with open(obsidian_file, "r", encoding="utf-8") as f:
        content = f.read()
    if "https://edmondposadas.vercel.app" not in content:
        content = content.replace(
            "https://inmobiliariarp-arch.github.io/torre-edmon-web/",
            "https://edmondposadas.vercel.app"
        )
        with open(obsidian_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Obsidian note updated with edmondposadas.vercel.app.")

# 2. Update README.md
readme_file = r"D:\Proyecto sitio web edificio\README.md"
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        rm = f.read()
    rm = rm.replace("https://torre-edmond.vercel.app", "https://edmondposadas.vercel.app")
    rm = rm.replace("https://torre-edmon-web.vercel.app", "https://edmondposadas.vercel.app")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(rm)
    print("README.md updated with edmondposadas.vercel.app.")
