with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('<span class="footer-tag">Comercialización Exclusiva</span>', '<span class="footer-tag">Comercializa</span>')
html = html.replace('Atención personalizada y asesoramiento en inversiones de categoría.', 'Para consultas, precios y disponibilidad de unidades en Torre Edmon.')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html actualizado con 'Comercializa' y 'precios y disponibilidad'!")
