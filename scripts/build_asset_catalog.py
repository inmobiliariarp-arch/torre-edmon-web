import os
import json

raw_dir = "assets/raw_pure_extracted"
files = [f for f in sorted(os.listdir(raw_dir)) if f.endswith(('.jpeg', '.jpg', '.png'))]

items = []
valid_id = 0

for filename in files:
    src_path = os.path.join(raw_dir, filename)
    from PIL import Image
    img = Image.open(src_path)
    w, h = img.size
    if w < 600 or h < 600:
        continue
    valid_id += 1
    items.append({
        "id": f"{valid_id:02d}",
        "webp": f"assets/catalog_previews/render_{valid_id:02d}.webp",
        "raw": f"assets/raw_pure_extracted/{filename}",
        "res": f"{w}x{h}",
        "filename": filename
    })

cards_html = ""
for it in items:
    cards_html += f"""
    <div class="asset-card" onclick="openModal('{it['webp']}', 'Render #{it['id']} - {it['res']}')">
      <div class="card-badge">ID #{it['id']}</div>
      <div class="img-wrap">
        <img src="{it['webp']}" alt="Render #{it['id']}" loading="lazy">
      </div>
      <div class="card-info">
        <div class="card-title">Imagen #{it['id']}</div>
        <div class="card-res"><i class="fas fa-expand"></i> {it['res']} px</div>
        <div class="card-hint">Clic para ampliar en HD</div>
      </div>
    </div>
    """

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Catálogo de Assets Puros - Torre Edmon</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {{
      --bg: #0d1017;
      --card-bg: #161b24;
      --gold: #c5a059;
      --gold-light: #e5c158;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --border: rgba(255, 255, 255, 0.1);
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 2.5rem 1.5rem;
    }}
    .header {{
      max-width: 1300px;
      margin: 0 auto 2.5rem;
      text-align: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 2rem;
    }}
    .header h1 {{
      font-family: 'Cinzel', serif;
      font-size: 2.4rem;
      color: var(--gold-light);
      margin-bottom: 0.5rem;
      letter-spacing: 0.05em;
    }}
    .header p {{
      color: var(--text-muted);
      font-size: 1.05rem;
      max-width: 800px;
      margin: 0 auto 1.5rem;
      line-height: 1.6;
    }}
    .instructions-box {{
      background: rgba(197, 160, 89, 0.1);
      border: 1px solid var(--gold);
      border-radius: 12px;
      padding: 1.25rem 2rem;
      max-width: 860px;
      margin: 0 auto;
      text-align: left;
      font-size: 0.95rem;
      line-height: 1.6;
    }}
    .instructions-box strong {{
      color: var(--gold-light);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1.75rem;
      max-width: 1300px;
      margin: 0 auto;
    }}
    .asset-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      cursor: pointer;
      position: relative;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    }}
    .asset-card:hover {{
      transform: translateY(-6px);
      border-color: var(--gold);
      box-shadow: 0 15px 35px rgba(197, 160, 89, 0.25);
    }}
    .card-badge {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: var(--gold);
      color: #000;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 0.3rem 0.75rem;
      border-radius: 20px;
      z-index: 2;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }}
    .img-wrap {{
      width: 100%;
      height: 200px;
      background: #000;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}
    .asset-card:hover .img-wrap img {{
      transform: scale(1.06);
    }}
    .card-info {{
      padding: 1.2rem;
    }}
    .card-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
      color: #fff;
    }}
    .card-res {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }}
    .card-hint {{
      font-size: 0.75rem;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-weight: 600;
    }}
    /* Modal Zoom */
    .modal {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.92);
      backdrop-filter: blur(12px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      z-index: 9999;
    }}
    .modal.active {{
      display: flex;
    }}
    .modal-content {{
      max-width: 90vw;
      max-height: 90vh;
      text-align: center;
      position: relative;
    }}
    .modal-content img {{
      max-width: 100%;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8);
      border: 1px solid var(--border);
    }}
    .modal-caption {{
      color: #fff;
      margin-top: 1rem;
      font-size: 1.1rem;
      font-weight: 600;
    }}
    .close-btn {{
      position: absolute;
      top: -2.5rem;
      right: 0;
      background: none;
      border: none;
      color: #fff;
      font-size: 2rem;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <div class="header">
    <h1>TORRE EDMON • CATÁLOGO DE ASSETS PUROS</h1>
    <p>
      Se han extraído las <strong>33 imágenes y renders originales en alta resolución</strong> directamente del interior del folleto, sin los textos ni logotipos de la maqueta previa.
    </p>
    <div class="instructions-box">
      <strong>📋 Instrucciones para clasificar:</strong><br>
      Haz clic en cualquier imagen para verla en pantalla completa. Luego solo indícame los números de ID que corresponden a cada sector:<br>
      • <strong>Fachadas / Exteriores:</strong> Ej. #01, #02, #18...<br>
      • <strong>Amenities (Piscina / Solárium / SUM / Hall):</strong> Ej. #05, #07, #09...<br>
      • <strong>Interiores (Living / Cocina / Dormitorio):</strong> Ej. #11, #12, #13, #15...<br>
      • <strong>Plantas & Planos:</strong> Ej. #23, #24, #28...<br>
      • <strong>Nuevas imágenes:</strong> Si tienes fotos adicionales, puedes colocarlas en la carpeta: <br>
      <code>D:\Proyecto sitio web edificio\assets\nuevas_imagenes_usuario</code>
    </div>
  </div>

  <div class="grid">
    {cards_html}
  </div>

  <div id="zoom-modal" class="modal" onclick="closeModal()">
    <div class="modal-content" onclick="event.stopPropagation()">
      <button class="close-btn" onclick="closeModal()">&times;</button>
      <img id="modal-img" src="" alt="Vista previa">
      <div id="modal-caption" class="modal-caption"></div>
    </div>
  </div>

  <script>
    function openModal(src, caption) {{
      document.getElementById('modal-img').src = src;
      document.getElementById('modal-caption').textContent = caption;
      document.getElementById('zoom-modal').classList.add('active');
    }}
    function closeModal() {{
      document.getElementById('zoom-modal').classList.remove('active');
    }}
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeModal();
    }});
  </script>
</body>
</html>"""

with open("catalogo_assets.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("catalogo_assets.html generado exitosamente en Disco D:!")
