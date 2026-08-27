import os

# 1. Update Obsidian note
obsidian_file = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana\Proyecto Web - Torre Edmond\Dossier Web - Torre Edmond (Fideicomiso Costa Posadas).md"
if os.path.exists(obsidian_file):
    with open(obsidian_file, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("https://edmondposadas.vercel.app", "https://edmonposadas.vercel.app")
    with open(obsidian_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Obsidian note updated with edmonposadas.vercel.app.")

# 2. Update README.md
readme_file = r"D:\Proyecto sitio web edificio\README.md"
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as f:
        rm = f.read()
    rm = rm.replace("https://edmondposadas.vercel.app", "https://edmonposadas.vercel.app")
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(rm)
    print("README.md updated with edmonposadas.vercel.app.")

# 3. Update vercel.json
vj_file = r"D:\Proyecto sitio web edificio\vercel.json"
if os.path.exists(vj_file):
    with open(vj_file, "r", encoding="utf-8") as f:
        vj = f.read()
    vj = vj.replace('"name": "edmondposadas"', '"name": "edmonposadas"')
    with open(vj_file, "w", encoding="utf-8") as f:
        f.write(vj)
    print("vercel.json updated with edmonposadas.")
