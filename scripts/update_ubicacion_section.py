with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update the Ubicacion section to feature the new illustrated map with clean elegance
old_sec = """  <!-- Ubicación & Entorno -->
  <section id="ubicacion">
    <div class="container">
      <div style="text-align: center; margin-bottom: 3.5rem;">
        <div class="section-tag">Ubicación del Proyecto</div>
        <h2 class="section-title">Posadas, <span class="text-gold">Misiones</span></h2>
      </div>

      <div class="location-grid">
        <div class="location-map-wrap" data-lightbox data-hires="assets/curated/exterior/mapa_ubicacion.webp" data-caption="Mapa de Ubicación - Torre Edmon, Posadas Misiones">
          <img src="assets/curated/exterior/mapa_ubicacion.webp" alt="Mapa de Ubicación Torre Edmon">
        </div>

        <ul class="location-points-list">
          <li class="location-point-item">
            <span class="point-number">1</span>
            <span>Parque República del Paraguay</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">2</span>
            <span>Club Guaraní Antonio Franco</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">3</span>
            <span>Antares Posadas</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">4</span>
            <span>Escuela de Robótica</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">5</span>
            <span>Itapúa Tenis Club</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">6</span>
            <span>Supermercado California</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">7</span>
            <span>Cristóbal Café Posadas</span>
          </li>
          <li class="location-point-item">
            <span class="point-number">8</span>
            <span>Monumento Papa Juan Pablo II</span>
          </li>
        </ul>
      </div>
    </div>
  </section>"""

new_sec = """  <!-- Ubicación del Proyecto -->
  <section id="ubicacion">
    <div class="container">
      <div style="text-align: center; margin-bottom: 2.5rem;">
        <div class="section-tag">Ubicación del Proyecto</div>
        <h2 class="section-title">Posadas, <span class="text-gold">Misiones</span></h2>
        <p class="section-subtitle" style="margin: 0 auto 2.5rem;">
          Emplazado en una ubicación costera privilegiada sobre la Costanera de Posadas, con rápido acceso y visuales directas al Río Paraná.
        </p>
      </div>

      <div class="location-map-master-wrap" data-lightbox data-hires="assets/curated/exterior/mapa_ubicacion.webp" data-caption="Masterplan de Ubicación - Torre Edmon, Posadas Misiones">
        <img src="assets/curated/exterior/mapa_ubicacion.webp" alt="Masterplan Ubicación Torre Edmon">
        <div class="plan-caption-hint" style="margin-top: 1rem;"><i class="fas fa-search-plus"></i> Haz clic en el mapa para ampliar en alta definición</div>
      </div>
    </div>
  </section>"""

if old_sec in content:
    content = content.replace(old_sec, new_sec)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html actualizado con el nuevo masterplan ilustrado de ubicacion!")
else:
    print("Bloque no encontrado, revisando...")
