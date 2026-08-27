with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_p = "que garantizan comodidad y seguridad."
new_p = "y <strong>ascensores con acceso directo a los departamentos</strong> que garantizan máxima privacidad, comodidad y seguridad."

if old_p in html:
    html = html.replace(old_p, new_p)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Texto actualizado con 'ascensores con acceso directo a los departamentos'!")
else:
    print("No se encontró la frase exacta, revisando...")
