with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('<div class="section-tag">Ubicación Estratégica</div>', '<div class="section-tag">Ubicación del Proyecto</div>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Actualizado: 'Ubicación del Proyecto'!")
