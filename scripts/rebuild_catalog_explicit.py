import os
import json
from PIL import Image

# Build the curated list of all 35 assets explicitly
catalog_items = []

# 1. Extracted images 01 to 33
raw_dir = "assets/raw_pure_extracted"
files = [f for f in sorted(os.listdir(raw_dir)) if f.startswith("img_") and not "mapa" in f]

cur_id = 0
for filename in files:
    src_path = os.path.join(raw_dir, filename)
    img = Image.open(src_path)
    w, h = img.size
    if w < 600 or h < 600:
        continue
    cur_id += 1
    
    preview_path = f"assets/catalog_previews/render_{cur_id:02d}.webp"
    if not os.path.exists(preview_path):
        preview_path = f"assets/raw_pure_extracted/{filename}"

    catalog_items.append({
        "id": f"{cur_id:02d}",
        "webp": preview_path,
        "raw": f"assets/raw_pure_extracted/{filename}",
        "res": f"{w}x{h}",
        "w": w,
        "h": h,
        "is_new": False,
        "filename": filename,
        "default_label": f"Render #{cur_id:02d}"
    })

# 2. Add Planta Render (ID #34)
img_p = Image.open("assets/plantas render.png")
catalog_items.append({
    "id": "34",
    "webp": "assets/catalog_previews/render_34_planta_render.webp",
    "raw": "assets/plantas render.png",
    "res": f"{img_p.size[0]}x{img_p.size[1]}",
    "w": img_p.size[0],
    "h": img_p.size[1],
    "is_new": True,
    "filename": "plantas render.png",
    "default_label": "Planta Oficial de Distribución"
})

# 3. Add Mapa Masterplan con Pin (ID #35)
img_m = Image.open("assets/mapa_ubicacion_masterplan.webp")
catalog_items.append({
    "id": "35",
    "webp": "assets/mapa_ubicacion_masterplan.webp",
    "raw": "assets/mapa_ubicacion_masterplan.webp",
    "res": f"{img_m.size[0]}x{img_m.size[1]}",
    "w": img_m.size[0],
    "h": img_m.size[1],
    "is_new": True,
    "filename": "mapa_ubicacion_masterplan.webp",
    "default_label": "Mapa Masterplan Posadas (con Pin Torre Edmon)"
})

print(f"Total items in catalog: {len(catalog_items)}")
for it in catalog_items[-4:]:
    print(f"ID #{it['id']} -> {it['filename']} ({it['default_label']})")

items_json = json.dumps(catalog_items, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Estudio de Curaduría y Recorte de Assets - Torre Edmon</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cinzel:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Cropper.js for visual trimming -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.js"></script>

  <style>
    :root {{
      --bg: #090b0e;
      --card-bg: #12151d;
      --panel-bg: #181d28;
      --panel-elevated: #1f2533;
      --gold: #c5a059;
      --gold-light: #e5c158;
      --gold-glow: rgba(197, 160, 89, 0.35);
      --success: #00e676;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --border: rgba(255, 255, 255, 0.1);
      --border-gold: rgba(197, 160, 89, 0.45);
      --radius: 12px;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 2rem 1.5rem 6rem;
    }}
    .top-bar {{
      max-width: 1400px;
      margin: 0 auto 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .title-area h1 {{
      font-family: 'Cinzel', serif;
      font-size: 2rem;
      color: var(--gold-light);
      letter-spacing: 0.05em;
    }}
    .title-area p {{
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 0.25rem;
    }}
    .top-actions {{
      display: flex;
      gap: 1rem;
      align-items: center;
    }}
    .btn {{
      padding: 0.75rem 1.5rem;
      border-radius: 30px;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      border: none;
      transition: all 0.25s ease;
    }}
    .btn-gold {{
      background: linear-gradient(135deg, #f3d489 0%, #c5a059 100%);
      color: #000;
      box-shadow: 0 4px 15px var(--gold-glow);
    }}
    .btn-gold:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(197, 160, 89, 0.5);
    }}
    .btn-secondary {{
      background: var(--panel-bg);
      color: #fff;
      border: 1px solid var(--border);
    }}
    .btn-secondary:hover {{
      border-color: var(--gold);
    }}
    .btn-danger {{
      background: rgba(239, 68, 68, 0.15);
      color: #ef4444;
      border: 1px solid rgba(239, 68, 68, 0.3);
    }}
    .btn-danger:hover {{
      background: #ef4444;
      color: #fff;
    }}
    
    .stats-bar {{
      max-width: 1400px;
      margin: 0 auto 1.5rem;
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .stat-pill {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 0.5rem 1rem;
      border-radius: 20px;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .stat-pill strong {{
      color: var(--gold);
    }}
    
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 1.75rem;
      max-width: 1400px;
      margin: 0 auto 3rem;
    }}
    .card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow: hidden;
      cursor: pointer;
      position: relative;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }}
    .card:hover {{
      transform: translateY(-6px);
      border-color: var(--gold);
      box-shadow: 0 15px 30px rgba(0,0,0,0.6);
    }}
    .card.classified {{
      border-color: var(--success);
      box-shadow: 0 0 0 2px rgba(0, 230, 118, 0.3);
    }}
    .badge-id {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(0, 0, 0, 0.85);
      border: 1px solid var(--gold);
      color: var(--gold);
      font-weight: 800;
      font-size: 0.85rem;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      z-index: 2;
      backdrop-filter: blur(6px);
    }}
    .badge-category {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: var(--success);
      color: #000;
      font-weight: 800;
      font-size: 0.75rem;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      z-index: 2;
      text-transform: uppercase;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }}
    .badge-discarded {{
      background: #ef4444 !important;
      color: #fff !important;
    }}
    .card-img-wrap {{
      width: 100%;
      height: 200px;
      background: #000;
      overflow: hidden;
      position: relative;
    }}
    .card-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}
    .card:hover .card-img-wrap img {{
      transform: scale(1.05);
    }}
    .card-body {{
      padding: 1.25rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .card-title {{
      font-weight: 700;
      font-size: 1.05rem;
      color: #fff;
      margin-bottom: 0.25rem;
    }}
    .card-meta {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }}
    .card-btn-action {{
      background: var(--panel-bg);
      border: 1px solid var(--border);
      color: var(--gold);
      padding: 0.55rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }}
    .card:hover .card-btn-action {{
      background: var(--gold);
      color: #000;
      border-color: transparent;
    }}

    /* Modal Editor */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.94);
      backdrop-filter: blur(14px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}
    .modal-overlay.active {{
      display: flex !important;
    }}
    .modal-box {{
      background: var(--card-bg);
      border: 1px solid var(--border-gold);
      border-radius: 16px;
      width: 100%;
      max-width: 1200px;
      max-height: 92vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
    }}
    .modal-header {{
      padding: 1.25rem 1.75rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--panel-bg);
    }}
    .modal-header h2 {{
      font-size: 1.3rem;
      color: var(--gold-light);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}
    .close-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.8rem;
      cursor: pointer;
      line-height: 1;
    }}
    .close-btn:hover {{
      color: #fff;
    }}
    .modal-body {{
      display: grid;
      grid-template-columns: 1.6fr 1fr;
      flex: 1;
      overflow-y: auto;
    }}
    .cropper-container-wrap {{
      background: #050608;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 480px;
      border-right: 1px solid var(--border);
    }}
    .cropper-img-wrapper {{
      max-width: 100%;
      max-height: 440px;
    }}
    .cropper-img-wrapper img {{
      max-width: 100%;
      display: block;
    }}
    .cropper-tools-bar {{
      margin-top: 1rem;
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .tool-btn {{
      padding: 0.4rem 0.8rem;
      background: var(--panel-bg);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: 6px;
      font-size: 0.8rem;
      cursor: pointer;
    }}
    .tool-btn:hover {{
      border-color: var(--gold);
      color: var(--gold);
    }}
    
    .curation-panel {{
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      overflow-y: auto;
    }}
    .panel-section-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gold);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .category-options {{
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }}
    .category-radio-label {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      background: var(--panel-bg);
      border: 1px solid var(--border);
      padding: 0.75rem 1rem;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s ease;
      font-size: 0.92rem;
    }}
    .category-radio-label:hover {{
      border-color: var(--gold-light);
    }}
    .category-radio-label.selected {{
      border-color: var(--gold);
      background: rgba(197, 160, 89, 0.15);
      color: #fff;
    }}
    .category-radio-label input {{
      accent-color: var(--gold);
    }}
    
    .input-group {{
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}
    .input-group label {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }}
    .text-input {{
      padding: 0.75rem 1rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--panel-bg);
      color: #fff;
      font-family: inherit;
      font-size: 0.9rem;
    }}
    .text-input:focus {{
      outline: none;
      border-color: var(--gold);
      box-shadow: 0 0 0 2px var(--gold-glow);
    }}
    
    .modal-footer {{
      padding: 1.25rem 1.75rem;
      border-top: 1px solid var(--border);
      background: var(--panel-bg);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }}

    .toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--panel-elevated);
      border: 1px solid var(--success);
      color: #fff;
      padding: 1rem 1.5rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.95rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      z-index: 10000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .toast.active {{
      transform: translateY(0);
      opacity: 1;
    }}

    @media (max-width: 900px) {{
      .modal-body {{ grid-template-columns: 1fr; }}
      .cropper-container-wrap {{ border-right: none; border-bottom: 1px solid var(--border); }}
    }}
  </style>
</head>
<body>

  <div class="top-bar">
    <div class="title-area">
      <h1>TORRE EDMON • CURADOR & RECORTE DE ASSETS</h1>
      <p>Catálogo completo con <strong>{len(catalog_items)} Assets</strong>. Incluye el nuevo <strong>Mapa Masterplan con Pin (ID #35)</strong>.</p>
    </div>
    <div class="top-actions">
      <button class="btn btn-secondary" onclick="exportData()"><i class="fas fa-download"></i> Descargar JSON</button>
      <button class="btn btn-gold" onclick="finishAndReprocess()"><i class="fas fa-magic"></i> Reprocesar Todos los Assets</button>
    </div>
  </div>

  <div class="stats-bar">
    <div class="stat-pill"><i class="fas fa-images"></i> Total: <strong>{len(catalog_items)} imágenes</strong></div>
    <div class="stat-pill"><i class="fas fa-check-circle" style="color:var(--success)"></i> Clasificadas: <strong id="stat-classified">0</strong></div>
    <div class="stat-pill"><i class="fas fa-building"></i> Exteriores: <strong id="stat-exterior">0</strong></div>
    <div class="stat-pill"><i class="fas fa-swimming-pool"></i> Amenities: <strong id="stat-amenities">0</strong></div>
    <div class="stat-pill"><i class="fas fa-couch"></i> Interiores: <strong id="stat-interiores">0</strong></div>
    <div class="stat-pill"><i class="fas fa-drafting-compass"></i> Plantas & Mapas: <strong id="stat-plantas">0</strong></div>
  </div>

  <div class="grid" id="assets-grid">
    <!-- Generated dynamically -->
  </div>

  <!-- Modal Editor -->
  <div id="editor-modal" class="modal-overlay">
    <div class="modal-box">
      <div class="modal-header">
        <h2 id="modal-item-title"><i class="fas fa-sliders-h"></i> Curar Asset</h2>
        <button class="close-btn" onclick="closeEditor()">&times;</button>
      </div>

      <div class="modal-body">
        <div class="cropper-container-wrap">
          <div class="cropper-img-wrapper">
            <img id="cropper-image" src="" alt="Editar render">
          </div>
          <div class="cropper-tools-bar">
            <button class="tool-btn" onclick="setRatio(NaN)"><i class="fas fa-vector-square"></i> Libre</button>
            <button class="tool-btn" onclick="setRatio(16/9)">16:9</button>
            <button class="tool-btn" onclick="setRatio(4/3)">4:3</button>
            <button class="tool-btn" onclick="resetCrop()"><i class="fas fa-undo"></i> Restablecer</button>
          </div>
        </div>

        <div class="curation-panel">
          <div>
            <div class="panel-section-title"><i class="fas fa-tags"></i> 1. Categoría</div>
            <div class="category-options">
              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="exterior">
                <span>🏢 <strong>Exterior / Fachadas & Mapa</strong></span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="amenities">
                <span>🏊 <strong>Amenities</strong> (Piscina, Solárium, SUM, Gym, Hall)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="interiores">
                <span>🛋️ <strong>Interiores</strong> (Balcón, Living, Master Suite, Cocina)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="plantas">
                <span>📐 <strong>Plantas & Planos</strong></span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="descartar">
                <span>❌ <strong>Descartar / No usar</strong></span>
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="item-label-input">2. Título o Descripción</label>
            <input type="text" id="item-label-input" class="text-input" placeholder="Ej. Mapa Masterplan Posadas">
          </div>

          <div class="input-group">
            <label>Detalles Técnicos</label>
            <div id="item-meta-details" style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;"></div>
          </div>
        </div>
      </div>

      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeEditor()">Cancelar</button>
        <button class="btn btn-gold" onclick="saveAndCloseCurrent()"><i class="fas fa-check"></i> Guardar Cambios y Continuar</button>
      </div>
    </div>
  </div>

  <div id="toast" class="toast">
    <i class="fas fa-check-circle" style="color:var(--success); font-size:1.4rem;"></i>
    <span id="toast-msg">Cambios guardados exitosamente</span>
  </div>

  <script>
    const ASSETS_DATA = {items_json};
    let curationState = JSON.parse(localStorage.getItem('torre_edmon_curation') || '{{}}');
    let currentItem = null;
    let cropper = null;

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toast-msg').textContent = msg;
      toast.classList.add('active');
      setTimeout(() => toast.classList.remove('active'), 2500);
    }}

    function renderGrid() {{
      const container = document.getElementById('assets-grid');
      container.innerHTML = '';

      let countClassified = 0;
      let countExt = 0, countAmen = 0, countInt = 0, countPlan = 0;

      ASSETS_DATA.forEach(item => {{
        const saved = curationState[item.id];
        const hasSaved = !!saved && !!saved.category;
        
        if (hasSaved) {{
          countClassified++;
          if (saved.category === 'exterior') countExt++;
          if (saved.category === 'amenities') countAmen++;
          if (saved.category === 'interiores') countInt++;
          if (saved.category === 'plantas') countPlan++;
        }}

        const card = document.createElement('div');
        card.className = `card ${{hasSaved ? 'classified' : ''}}`;
        card.onclick = () => openEditor(item);

        let catBadge = '';
        if (hasSaved) {{
          const isDisc = saved.category === 'descartar';
          const labels = {{
            'exterior': '🏢 Exterior',
            'amenities': '🏊 Amenities',
            'interiores': '🛋️ Interiores',
            'plantas': '📐 Plantas',
            'descartar': '❌ Descartada'
          }};
          catBadge = `<span class="badge-category ${{isDisc ? 'badge-discarded' : ''}}">${{labels[saved.category] || saved.category}}</span>`;
        }} else if (item.is_new) {{
          catBadge = `<span class="badge-category" style="background:#00e676;">NUEVO ASSET</span>`;
        }}

        card.innerHTML = `
          <span class="badge-id">ID #${{item.id}}</span>
          ${{catBadge}}
          <div class="card-img-wrap">
            <img src="${{item.webp}}" alt="Asset #${{item.id}}" loading="lazy">
          </div>
          <div class="card-body">
            <div>
              <div class="card-title">${{hasSaved && saved.label ? saved.label : item.default_label}}</div>
              <div class="card-meta">${{item.res}} px • ${{item.filename}}</div>
            </div>
            <div class="card-btn-action">
              <i class="fas fa-crop-alt"></i> ${{hasSaved ? 'Modificar Recorte / Categoría' : 'Recortar y Categorizar'}}
            </div>
          </div>
        `;
        container.appendChild(card);
      }});

      document.getElementById('stat-classified').textContent = `${{countClassified}} / ${{ASSETS_DATA.length}}`;
      document.getElementById('stat-exterior').textContent = countExt;
      document.getElementById('stat-amenities').textContent = countAmen;
      document.getElementById('stat-interiores').textContent = countInt;
      document.getElementById('stat-plantas').textContent = countPlan;
    }}

    function openEditor(item) {{
      currentItem = item;
      const saved = curationState[item.id] || {{}};

      document.getElementById('modal-item-title').innerHTML = `<i class="fas fa-sliders-h"></i> Curar Asset ID #${{item.id}}`;
      document.getElementById('item-label-input').value = saved.label || item.default_label;
      document.getElementById('item-meta-details').innerHTML = `
        <strong>Archivo:</strong> ${{item.filename}}<br>
        <strong>Dimensiones:</strong> ${{item.res}} px
      `;

      document.querySelectorAll('.category-radio-label').forEach(label => {{
        label.classList.remove('selected');
        const radio = label.querySelector('input');
        if (saved.category && radio.value === saved.category) {{
          radio.checked = true;
          label.classList.add('selected');
        }} else {{
          radio.checked = false;
        }}
      }});

      const imgEl = document.getElementById('cropper-image');
      imgEl.src = item.raw;

      document.getElementById('editor-modal').classList.add('active');

      if (cropper) {{
        cropper.destroy();
        cropper = null;
      }}

      imgEl.onload = () => {{
        try {{
          cropper = new Cropper(imgEl, {{
            viewMode: 1,
            autoCropArea: saved.cropData ? undefined : 0.95,
            data: saved.cropData || null,
            responsive: true,
            restore: true
          }});
        }} catch(e) {{}}
      }};
    }}

    function selectCatRadio(labelEl) {{
      document.querySelectorAll('.category-radio-label').forEach(l => l.classList.remove('selected'));
      labelEl.classList.add('selected');
      const radio = labelEl.querySelector('input');
      radio.checked = true;
    }}

    function setRatio(ratio) {{
      if (cropper) cropper.setAspectRatio(ratio);
    }}

    function resetCrop() {{
      if (cropper) cropper.reset();
    }}

    function closeEditor() {{
      const modal = document.getElementById('editor-modal');
      if (modal) modal.classList.remove('active');
      if (cropper) {{
        try {{ cropper.destroy(); }} catch(e) {{}}
        cropper = null;
      }}
      currentItem = null;
    }}

    function saveAndCloseCurrent() {{
      if (!currentItem) return;

      const selectedRadio = document.querySelector('input[name="cat_choice"]:checked');
      const category = selectedRadio ? selectedRadio.value : 'exterior';
      const label = document.getElementById('item-label-input').value.trim();

      let cropData = null;
      if (cropper) {{
        try {{
          cropData = cropper.getData(true);
        }} catch(err) {{}}
      }}

      try {{
        curationState[currentItem.id] = {{
          id: currentItem.id,
          filename: currentItem.filename,
          raw_path: currentItem.raw,
          category: category,
          label: label || currentItem.default_label,
          cropData: cropData,
          timestamp: new Date().toISOString()
        }};
        localStorage.setItem('torre_edmon_curation', JSON.stringify(curationState));
      }} catch (e) {{}}

      const savedId = currentItem.id;
      closeEditor();
      renderGrid();
      showToast(`¡ID #${{savedId}} guardado en el registro!`);
    }}

    function exportData() {{
      const dataStr = JSON.stringify(curationState, null, 2);
      const blob = new Blob([dataStr], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'assets_curados_edmon.json';
      a.click();
    }}

    function finishAndReprocess() {{
      exportData();
      alert('¡Registro guardado y descargado! Notifícame en el chat para aplicar los recortes.');
    }}

    window.addEventListener('DOMContentLoaded', renderGrid);
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeEditor();
    }});
  </script>
</body>
</html>
"""

with open("catalogo_assets.html", "w", encoding="utf-8") as f:
    f.write(html)

print("catalogo_assets.html generado con ID #34 Planta e ID #35 Mapa Masterplan!")
