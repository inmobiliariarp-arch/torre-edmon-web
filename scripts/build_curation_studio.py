import os
from PIL import Image

raw_dir = "assets/raw_pure_extracted"
files = [f for f in sorted(os.listdir(raw_dir)) if f.endswith(('.jpeg', '.jpg', '.png'))]

items = []
valid_id = 0

for filename in files:
    src_path = os.path.join(raw_dir, filename)
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
        "w": w,
        "h": h,
        "is_new": False,
        "filename": filename
    })

# Add user's new planta
if os.path.exists("assets/plantas render.png"):
    img_u = Image.open("assets/plantas render.png")
    valid_id += 1
    items.append({
        "id": f"{valid_id:02d}",
        "webp": "assets/catalog_previews/render_34_planta_render.webp",
        "raw": "assets/plantas render.png",
        "res": f"{img_u.size[0]}x{img_u.size[1]}",
        "w": img_u.size[0],
        "h": img_u.size[1],
        "is_new": True,
        "filename": "plantas render.png"
    })

import json
items_json = json.dumps(items, ensure_ascii=False)

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
      --gold: #c5a059;
      --gold-light: #e5c158;
      --gold-glow: rgba(197, 160, 89, 0.3);
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --border: rgba(255, 255, 255, 0.1);
      --border-gold: rgba(197, 160, 89, 0.4);
      --radius: 12px;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      padding: 2rem 1.5rem;
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
    
    /* Instructions Bar */
    .instructions-card {{
      max-width: 1400px;
      margin: 0 auto 2rem;
      background: rgba(197, 160, 89, 0.08);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius);
      padding: 1.25rem 1.75rem;
      display: flex;
      align-items: center;
      gap: 1.5rem;
      font-size: 0.92rem;
    }}
    .instructions-card i {{
      font-size: 2rem;
      color: var(--gold);
    }}
    
    /* Stats bar */
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
    
    /* Grid */
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 1.75rem;
      max-width: 1400px;
      margin: 0 auto;
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
      border-color: var(--gold);
      box-shadow: 0 0 0 2px var(--gold-glow);
    }}
    .badge-id {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(0, 0, 0, 0.8);
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
      background: #00e676;
      color: #000;
      font-weight: 700;
      font-size: 0.75rem;
      padding: 0.25rem 0.65rem;
      border-radius: 20px;
      z-index: 2;
      text-transform: uppercase;
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
      padding: 0.5rem;
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

    /* ==========================================================================
       CURATION & CROPPER MODAL
       ========================================================================== */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(12px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}
    .modal-overlay.active {{
      display: flex;
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
      justify-content: flex-end;
      gap: 1rem;
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
      <p>Haz clic en cualquier imagen para <strong>1) Recortar bordes/anotaciones</strong> y <strong>2) Asignar su categoría exacta</strong>.</p>
    </div>
    <div class="top-actions">
      <button class="btn btn-secondary" onclick="exportData()"><i class="fas fa-download"></i> Descargar JSON</button>
      <button class="btn btn-gold" onclick="applyAllToProject()"><i class="fas fa-check-circle"></i> Guardar y Aplicar al Sitio</button>
    </div>
  </div>

  <div class="instructions-card">
    <i class="fas fa-crop-alt"></i>
    <div>
      <strong>Herramienta interactiva de curaduría:</strong><br>
      1. Haz clic en una imagen para abrir el panel de edición.<br>
      2. Mueve el recuadro de recorte para quitar cualquier marco, texto lateral o logo residual.<br>
      3. Elige si es <strong>Exterior, Amenities, Interiores, Planta o Descartar</strong> y haz clic en <strong>Guardar Cambios</strong>.
    </div>
  </div>

  <div class="stats-bar">
    <div class="stat-pill"><i class="fas fa-images"></i> Total: <strong>{len(items)} imágenes</strong></div>
    <div class="stat-pill"><i class="fas fa-check"></i> Clasificadas: <strong id="stat-classified">0</strong></div>
    <div class="stat-pill"><i class="fas fa-building"></i> Exteriores: <strong id="stat-exterior">0</strong></div>
    <div class="stat-pill"><i class="fas fa-swimming-pool"></i> Amenities: <strong id="stat-amenities">0</strong></div>
    <div class="stat-pill"><i class="fas fa-couch"></i> Interiores: <strong id="stat-interiores">0</strong></div>
    <div class="stat-pill"><i class="fas fa-drafting-compass"></i> Plantas: <strong id="stat-plantas">0</strong></div>
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
        <!-- Crop Tool -->
        <div class="cropper-container-wrap">
          <div class="cropper-img-wrapper">
            <img id="cropper-image" src="" alt="Editar render">
          </div>
          <div class="cropper-tools-bar">
            <button class="tool-btn" onclick="setRatio(NaN)"><i class="fas fa-vector-square"></i> Libre</button>
            <button class="tool-btn" onclick="setRatio(16/9)">16:9</button>
            <button class="tool-btn" onclick="setRatio(4/3)">4:3</button>
            <button class="tool-btn" onclick="resetCrop()"><i class="fas fa-undo"></i> Restablecer Recorte</button>
          </div>
        </div>

        <!-- Curation Panel -->
        <div class="curation-panel">
          <div>
            <div class="panel-section-title"><i class="fas fa-tags"></i> 1. Categoría del Proyecto</div>
            <div class="category-options">
              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="exterior">
                <span>🏢 <strong>Exterior / Fachadas</strong> (Vistas diurnas, nocturnas, entorno)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="amenities">
                <span>🏊 <strong>Amenities & Áreas Comunes</strong> (Piscina, Solárium, SUM, Hall)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="interiores">
                <span>🛋️ <strong>Interiores</strong> (Living, Cocina, Master Suite, Balcón al Río)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="plantas">
                <span>📐 <strong>Plantas & Planos</strong> (Distribución departamento, cocheras)</span>
              </label>

              <label class="category-radio-label" onclick="selectCatRadio(this)">
                <input type="radio" name="cat_choice" value="descartar">
                <span>❌ <strong>Descartar / No usar</strong></span>
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="item-label-input">2. Título o Descripción Específica</label>
            <input type="text" id="item-label-input" class="text-input" placeholder="Ej. Living Comedor con Vista al Río Paraná">
          </div>

          <div class="input-group">
            <label>Detalles del Archivo Original</label>
            <div id="item-meta-details" style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.5;"></div>
          </div>
        </div>
      </div>

      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeEditor()">Cancelar</button>
        <button class="btn btn-gold" onclick="saveCurrentItem()"><i class="fas fa-save"></i> Guardar Cambios de Esta Imagen</button>
      </div>
    </div>
  </div>

  <script>
    const ASSETS_DATA = {items_json};
    let curationState = JSON.parse(localStorage.getItem('torre_edmon_curation') || '{{}}');
    let currentItem = null;
    let cropper = null;

    function renderGrid() {{
      const container = document.getElementById('assets-grid');
      container.innerHTML = '';

      let countClassified = 0;
      let countExt = 0, countAmen = 0, countInt = 0, countPlan = 0;

      ASSETS_DATA.forEach(item => {{
        const saved = curationState[item.id] || {{}};
        const hasCat = !!saved.category;
        if (hasCat) countClassified++;
        if (saved.category === 'exterior') countExt++;
        if (saved.category === 'amenities') countAmen++;
        if (saved.category === 'interiores') countInt++;
        if (saved.category === 'plantas') countPlan++;

        const card = document.createElement('div');
        card.className = `card ${{hasCat ? 'classified' : ''}}`;
        card.onclick = () => openEditor(item);

        let catBadge = '';
        if (saved.category) {{
          const labels = {{
            'exterior': '🏢 Exterior',
            'amenities': '🏊 Amenities',
            'interiores': '🛋️ Interiores',
            'plantas': '📐 Plantas',
            'descartar': '❌ Descartada'
          }};
          catBadge = `<span class="badge-category">${{labels[saved.category] || saved.category}}</span>`;
        }} else if (item.is_new) {{
          catBadge = `<span class="badge-category" style="background:#00e676;">NUEVA PLANTA</span>`;
        }}

        card.innerHTML = `
          <span class="badge-id">ID #${{item.id}}</span>
          ${{catBadge}}
          <div class="card-img-wrap">
            <img src="${{saved.cropped_preview || item.webp}}" alt="Asset #${{item.id}}" loading="lazy">
          </div>
          <div class="card-body">
            <div>
              <div class="card-title">${{saved.label || (item.is_new ? 'Planta Render' : 'Imagen #' + item.id)}}</div>
              <div class="card-meta">${{item.res}} px • ${{item.filename}}</div>
            </div>
            <div class="card-btn-action">
              <i class="fas fa-crop-alt"></i> ${{hasCat ? 'Editar Recorte / Categoría' : 'Recortar y Categorizar'}}
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
      document.getElementById('item-label-input').value = saved.label || (item.is_new ? 'Planta Oficial de Distribución' : '');
      document.getElementById('item-meta-details').innerHTML = `
        <strong>Archivo:</strong> ${{item.filename}}<br>
        <strong>Dimensiones:</strong> ${{item.res}} px
      `;

      // Reset radio buttons
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

      // Setup Cropper
      const imgEl = document.getElementById('cropper-image');
      imgEl.src = item.raw;

      document.getElementById('editor-modal').classList.add('active');

      if (cropper) cropper.destroy();

      imgEl.onload = () => {{
        cropper = new Cropper(imgEl, {{
          viewMode: 1,
          autoCropArea: saved.cropData ? undefined : 0.95,
          data: saved.cropData || null,
          responsive: true,
          restore: true
        }});
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
      document.getElementById('editor-modal').classList.remove('active');
      if (cropper) {{
        cropper.destroy();
        cropper = null;
      }}
    }}

    function saveCurrentItem() {{
      if (!currentItem) return;

      const selectedRadio = document.querySelector('input[name="cat_choice"]:checked');
      const category = selectedRadio ? selectedRadio.value : '';
      const label = document.getElementById('item-label-input').value.trim();

      let cropData = null;
      let croppedPreview = null;

      if (cropper) {{
        cropData = cropper.getData(true); // integer coordinates
        const canvas = cropper.getCroppedCanvas({{ maxWidth: 1920, maxHeight: 1080 }});
        if (canvas) {{
          croppedPreview = canvas.toDataURL('image/jpeg', 0.85);
        }}
      }}

      curationState[currentItem.id] = {{
        id: currentItem.id,
        filename: currentItem.filename,
        raw_path: currentItem.raw,
        category: category,
        label: label || `Render #${{currentItem.id}}`,
        cropData: cropData,
        cropped_preview: croppedPreview
      }};

      localStorage.setItem('torre_edmon_curation', JSON.stringify(curationState));
      renderGrid();
      closeEditor();
    }}

    function exportData() {{
      const blob = new Blob([JSON.stringify(curationState, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'assets_curados_edmon.json';
      a.click();
    }}

    function applyAllToProject() {{
      exportData();
      alert('¡Excelente! Se ha descargado el archivo "assets_curados_edmon.json". Notifícame aquí en el chat para aplicar automáticamente los recortes exactos y montar la web definitiva.');
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

print("catalogo_assets.html generado como Estudio de Curaduría y Recorte!")
