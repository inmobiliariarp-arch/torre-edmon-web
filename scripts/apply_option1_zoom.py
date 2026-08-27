import os

# 1. Update index.html
with open(r"D:\Proyecto sitio web edificio\index.html", "r", encoding="utf-8") as f:
    html = f.read()

target_planta = """      <div class="plan-container-card">
        <div id="plan-interactive-box" class="plan-interactive-wrapper">
          <button class="plan-zoom-badge-btn" data-lightbox data-hires="assets/curated/plantas/plantas_34.webp" data-caption="Planta Tipo - Distribución Oficial">
            <i class="fas fa-search-plus"></i> Zoom
          </button>
          <img id="plan-zoom-img" src="assets/curated/plantas/plantas_34.webp" alt="Planta Tipo Torre Edmon">
        </div>
      </div>"""

new_planta = """      <div class="plan-container-card">
        <!-- Floating Glassmorphic Control Toolbar -->
        <div class="plan-toolbar" role="toolbar" aria-label="Controles de visualización del plano">
          <span class="plan-zoom-indicator" id="plan-zoom-val" title="Nivel de zoom">100%</span>
          <div class="plan-toolbar-divider"></div>
          <button class="plan-tool-btn" id="plan-zoom-in" title="Acercar (+)" aria-label="Acercar zoom">
            <i class="fas fa-plus"></i>
          </button>
          <button class="plan-tool-btn" id="plan-zoom-out" title="Alejar (-)" aria-label="Alejar zoom">
            <i class="fas fa-minus"></i>
          </button>
          <button class="plan-tool-btn" id="plan-zoom-reset" title="Restablecer vista" aria-label="Restablecer vista">
            <i class="fas fa-redo-alt"></i>
          </button>
          <div class="plan-toolbar-divider"></div>
          <button class="plan-tool-btn highlight" id="plan-zoom-expand" data-lightbox data-hires="assets/curated/plantas/plantas_34.webp" data-caption="Planta Tipo - Distribución Oficial en Alta Definición" title="Pantalla Completa" aria-label="Pantalla completa">
            <i class="fas fa-expand"></i>
          </button>
        </div>

        <!-- Interactive Blueprint Viewport -->
        <div id="plan-interactive-box" class="plan-interactive-wrapper">
          <img id="plan-zoom-img" src="assets/curated/plantas/plantas_34.webp" alt="Planta Tipo Torre Edmon" draggable="false">
        </div>

        <!-- Footnote / Hint Bar -->
        <div class="plan-footer-bar">
          <span class="plan-hint-text"><i class="fas fa-mouse"></i> Usa la rueda del ratón o arrastra para explorar • Doble clic para zoom rápido</span>
        </div>
      </div>"""

if target_planta in html:
    html = html.replace(target_planta, new_planta)
    with open(r"D:\Proyecto sitio web edificio\index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html actualizado exitosamente.")
else:
    print("WARNING: target_planta no encontrado en index.html")

# 2. Update styles/main.css
with open(r"D:\Proyecto sitio web edificio\styles\main.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace planta tipo css section
target_css = """/* Planta Tipo with In-place Smooth Zoom & Tactile Pan */
.plan-container-card {
  background: var(--plan-viewport-bg);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--card-shadow);
  position: relative;
}

.plan-interactive-wrapper {
  min-height: 520px;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  touch-action: none;
  cursor: zoom-in;
}

.plan-interactive-wrapper img {
  max-width: 88%;
  max-height: 500px;
  object-fit: contain;
  user-select: none;
  -webkit-user-drag: none;
  pointer-events: none;
  transition: transform 0.08s ease-out;
}

/* Discrete Zoom Badge */
.plan-zoom-badge-btn {
  position: absolute;
  top: 1.2rem;
  right: 1.2rem;
  background: rgba(15, 18, 23, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-gold);
  color: var(--gold-primary);
  padding: 0.45rem 0.9rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
  z-index: 10;
  transition: var(--transition-fast);
}

.plan-zoom-badge-btn:hover {
  background: var(--gold-primary);
  color: #000;
}"""

new_css = """/* ==========================================================================
   PLANTA TIPO - ARCHITECTURAL PANZOOM STUDIO (STRICT BOUNDARY CLAMPING)
   ========================================================================== */
.plan-container-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
  position: relative;
  display: flex;
  flex-direction: column;
}

/* Technical Blueprint Grid Viewport */
.plan-interactive-wrapper {
  height: 580px;
  max-height: 70vh;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  touch-action: none;
  cursor: zoom-in;
  background-color: var(--bg-surface-elevated);
  background-image: 
    radial-gradient(var(--gold-glow) 1px, transparent 1px),
    linear-gradient(to right, rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 28px 28px, 140px 140px, 140px 140px;
  background-position: center center;
}

.plan-interactive-wrapper img {
  max-width: 92%;
  max-height: 92%;
  width: auto;
  height: auto;
  object-fit: contain;
  user-select: none;
  -webkit-user-drag: none;
  pointer-events: none;
  transform-origin: center center;
  will-change: transform;
  filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.25));
}

/* Floating Glassmorphic Toolbar */
.plan-toolbar {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  background: rgba(13, 15, 18, 0.82);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius-full);
  padding: 0.35rem 0.6rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  z-index: 20;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  transition: var(--transition-smooth);
}

[data-theme="light"] .plan-toolbar {
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
}

.plan-zoom-indicator {
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--gold-primary);
  padding: 0.2rem 0.5rem;
  letter-spacing: 0.05em;
  font-family: var(--font-sans);
  min-width: 44px;
  text-align: center;
}

.plan-toolbar-divider {
  width: 1px;
  height: 18px;
  background: var(--border-glass);
}

.plan-tool-btn {
  width: 32px;
  height: 32px;
  border-radius: var(--radius-full);
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-main);
  font-size: 0.85rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition-fast);
}

.plan-tool-btn:hover {
  background: rgba(197, 160, 89, 0.15);
  color: var(--gold-primary);
  border-color: var(--border-gold);
  transform: translateY(-1px);
}

.plan-tool-btn.highlight {
  background: var(--gold-gradient);
  color: #000;
  font-weight: 700;
}

.plan-tool-btn.highlight:hover {
  box-shadow: 0 0 12px var(--gold-glow);
  transform: translateY(-1px) scale(1.05);
}

/* Footer / Hint Bar */
.plan-footer-bar {
  padding: 0.75rem 1.5rem;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-glass);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.82rem;
  color: var(--text-muted);
}

.plan-hint-text {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

@media (max-width: 768px) {
  .plan-interactive-wrapper {
    height: 420px;
  }
  .plan-toolbar {
    top: 0.75rem;
    right: 0.75rem;
    padding: 0.25rem 0.4rem;
  }
  .plan-tool-btn {
    width: 28px;
    height: 28px;
    font-size: 0.75rem;
  }
  .plan-zoom-indicator {
    font-size: 0.7rem;
    min-width: 36px;
  }
}"""

if target_css in css:
    css = css.replace(target_css, new_css)
    with open(r"D:\Proyecto sitio web edificio\styles\main.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("styles/main.css actualizado exitosamente.")
else:
    print("WARNING: target_css no encontrado en styles/main.css")

# 3. Update js/app.js
with open(r"D:\Proyecto sitio web edificio\js\app.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace section 3 in js/app.js
js_target_start = "  // 3. SMOOTH IN-PLACE ZOOM & PAN FOR FLOOR PLAN"
js_target_end = "  // 4. LIGHTBOX MODAL"

start_idx = js.find(js_target_start)
end_idx = js.find(js_target_end)

if start_idx != -1 and end_idx != -1:
    new_js_section = """  // 3. ARCHITECTURAL PANZOOM STUDIO (STRICT BOUNDARY CLAMPING & FOCAL POINT)
  const planBox = document.getElementById('plan-interactive-box');
  const planImg = document.getElementById('plan-zoom-img');
  const zoomValDisplay = document.getElementById('plan-zoom-val');
  const zoomInBtn = document.getElementById('plan-zoom-in');
  const zoomOutBtn = document.getElementById('plan-zoom-out');
  const zoomResetBtn = document.getElementById('plan-zoom-reset');

  if (planBox && planImg) {
    let scale = 1;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    const MIN_SCALE = 1;
    const MAX_SCALE = 4.5;

    // Strict boundary clamping so plan edges never detach or reveal blank/black borders
    function clampPan(targetX, targetY, targetScale) {
      if (targetScale <= 1) return { x: 0, y: 0 };

      const boxRect = planBox.getBoundingClientRect();
      const imgNaturalRatio = (planImg.naturalWidth && planImg.naturalHeight) 
        ? (planImg.naturalWidth / planImg.naturalHeight) 
        : (boxRect.width / boxRect.height);

      let baseW = boxRect.width * 0.92;
      let baseH = baseW / imgNaturalRatio;
      if (baseH > boxRect.height * 0.92) {
        baseH = boxRect.height * 0.92;
        baseW = baseH * imgNaturalRatio;
      }

      const scaledW = baseW * targetScale;
      const scaledH = baseH * targetScale;

      const maxPanX = Math.max(0, (scaledW - boxRect.width) / 2);
      const maxPanY = Math.max(0, (scaledH - boxRect.height) / 2);

      const clampedX = Math.max(-maxPanX, Math.min(maxPanX, targetX));
      const clampedY = Math.max(-maxPanY, Math.min(maxPanY, targetY));

      return { x: clampedX, y: clampedY };
    }

    function updateTransform(animate = false) {
      scale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale));
      if (scale === 1) {
        panX = 0;
        panY = 0;
      } else {
        const clamped = clampPan(panX, panY, scale);
        panX = clamped.x;
        panY = clamped.y;
      }

      planImg.style.transition = animate ? 'transform 0.28s cubic-bezier(0.2, 0, 0.2, 1)' : 'none';
      planImg.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${scale})`;
      planBox.style.cursor = scale > 1 ? (isDragging ? 'grabbing' : 'grab') : 'zoom-in';

      if (zoomValDisplay) {
        zoomValDisplay.textContent = `${Math.round(scale * 100)}%`;
      }
    }

    function zoomToPoint(deltaFactor, focalX, focalY) {
      const boxRect = planBox.getBoundingClientRect();
      const centerX = (focalX !== undefined) ? (focalX - boxRect.left - boxRect.width / 2) : 0;
      const centerY = (focalY !== undefined) ? (focalY - boxRect.top - boxRect.height / 2) : 0;

      const prevScale = scale;
      const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale * deltaFactor));

      if (newScale !== prevScale) {
        const scaleRatio = newScale / prevScale;
        panX = centerX - (centerX - panX) * scaleRatio;
        panY = centerY - (centerY - panY) * scaleRatio;
        scale = newScale;
        updateTransform(true);
      }
    }

    // Wheel event with focal zoom
    planBox.addEventListener('wheel', (e) => {
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.18 : 0.82;
      zoomToPoint(delta, e.clientX, e.clientY);
    }, { passive: false });

    // Drag to Pan with mouse
    planBox.addEventListener('mousedown', (e) => {
      if (e.target.closest('.plan-toolbar')) return;
      if (scale > 1) {
        isDragging = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        planImg.style.transition = 'none';
        planBox.style.cursor = 'grabbing';
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform(false);
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        updateTransform(true);
      }
    });

    // Touch events for Mobile (Pinch-to-zoom & 1-finger drag)
    let initialPinchDist = 0;
    let initialPinchScale = 1;
    let pinchCenter = { x: 0, y: 0 };

    planBox.addEventListener('touchstart', (e) => {
      if (e.target.closest('.plan-toolbar')) return;
      if (e.touches.length === 2) {
        initialPinchDist = getDistance(e.touches[0], e.touches[1]);
        initialPinchScale = scale;
        pinchCenter = {
          x: (e.touches[0].clientX + e.touches[1].clientX) / 2,
          y: (e.touches[0].clientY + e.touches[1].clientY) / 2
        };
      } else if (e.touches.length === 1 && scale > 1) {
        isDragging = true;
        startX = e.touches[0].clientX - panX;
        startY = e.touches[0].clientY - panY;
        planImg.style.transition = 'none';
      }
    }, { passive: true });

    planBox.addEventListener('touchmove', (e) => {
      if (e.touches.length === 2 && initialPinchDist > 0) {
        const currentDist = getDistance(e.touches[0], e.touches[1]);
        const factor = currentDist / initialPinchDist;
        const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, initialPinchScale * factor));
        zoomToPoint(newScale / scale, pinchCenter.x, pinchCenter.y);
      } else if (e.touches.length === 1 && isDragging) {
        panX = e.touches[0].clientX - startX;
        panY = e.touches[0].clientY - startY;
        updateTransform(false);
      }
    }, { passive: true });

    planBox.addEventListener('touchend', (e) => {
      if (e.touches.length < 2) initialPinchDist = 0;
      if (e.touches.length === 0) {
        isDragging = false;
        updateTransform(true);
      }
    });

    function getDistance(t1, t2) {
      const dx = t1.clientX - t2.clientX;
      const dy = t1.clientY - t2.clientY;
      return Math.sqrt(dx * dx + dy * dy);
    }

    // Double-click/double-tap to toggle 1x and 2.2x
    let lastClick = 0;
    planBox.addEventListener('click', (e) => {
      if (e.target.closest('.plan-toolbar') || e.target.closest('.plan-footer-bar')) return;
      const now = Date.now();
      if (now - lastClick < 320) {
        if (scale > 1.1) {
          scale = 1;
          panX = 0;
          panY = 0;
          updateTransform(true);
        } else {
          zoomToPoint(2.3, e.clientX, e.clientY);
        }
      }
      lastClick = now;
    });

    // Toolbar button listeners
    if (zoomInBtn) {
      zoomInBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        zoomToPoint(1.35);
      });
    }
    if (zoomOutBtn) {
      zoomOutBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        zoomToPoint(0.75);
      });
    }
    if (zoomResetBtn) {
      zoomResetBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        scale = 1;
        panX = 0;
        panY = 0;
        updateTransform(true);
      });
    }
  }

"""
    js = js[:start_idx] + new_js_section + js[end_idx:]
    with open(r"D:\Proyecto sitio web edificio\js\app.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("js/app.js actualizado exitosamente.")
else:
    print("WARNING: marcadores no encontrados en js/app.js")

# 4. Update vercel.json
with open(r"D:\Proyecto sitio web edificio\vercel.json", "r", encoding="utf-8") as f:
    vj = f.read()

vj = vj.replace('"name": "torre-edmond-web"', '"name": "edmondposadas"')
with open(r"D:\Proyecto sitio web edificio\vercel.json", "w", encoding="utf-8") as f:
    f.write(vj)
print("vercel.json actualizado con nombre edmondposadas.")
