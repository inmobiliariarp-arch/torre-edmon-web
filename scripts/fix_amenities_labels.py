with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the titles in Amenities
old_amenities = """      <div class="amenities-grid">
        <!-- Piscina en terraza (ID #31) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_31.webp" data-caption="Piscina en Terraza con Vista al Río">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_31.webp" alt="Piscina en terraza" loading="lazy">
          </div>
          <h3>Piscina en Terraza</h3>
          <p>Ubicada en la azotea con vistas panorámicas al Río Paraná.</p>
        </div>

        <!-- Solarium en terraza (ID #30) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_30.webp" data-caption="Solárium en Terraza">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_30.webp" alt="Solárium en terraza" loading="lazy">
          </div>
          <h3>Solárium en Terraza</h3>
          <p>Deck exterior de descanso y relax al aire libre.</p>
        </div>

        <!-- SUM quincho (ID #32) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_32.webp" data-caption="SUM & Quincho Climatizado con Gran Parrilla">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_32.webp" alt="SUM quincho" loading="lazy">
          </div>
          <h3>SUM & Quincho</h3>
          <p>Salón climatizado equipado con gran parrilla para reuniones sociales.</p>
        </div>

        <!-- Hall acceso (ID #12) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_12.webp" data-caption="Hall de Acceso Principal">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_12.webp" alt="Hall de acceso" loading="lazy">
          </div>
          <h3>Hall de Acceso</h3>
          <p>Ingreso jerarquizado con recepción y control de acceso 24hs.</p>
        </div>
      </div>"""

new_amenities = """      <div class="amenities-grid">
        <!-- Piscina en terraza (ID #31) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_31.webp" data-caption="Piscina en Terraza">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_31.webp" alt="Piscina en terraza" loading="lazy">
          </div>
          <h3>Piscina en Terraza</h3>
          <p>Ubicada en la azotea con vistas panorámicas al Río Paraná.</p>
        </div>

        <!-- Solárium (ID #30) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_30.webp" data-caption="Solárium">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_30.webp" alt="Solárium" loading="lazy">
          </div>
          <h3>Solárium</h3>
          <p>Deck exterior de descanso y relax al aire libre.</p>
        </div>

        <!-- Gym (ID #32) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_32.webp" data-caption="Gym">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_32.webp" alt="Gym" loading="lazy">
          </div>
          <h3>Gym</h3>
          <p>Espacio fitness completamente equipado con vistas abiertas.</p>
        </div>

        <!-- Hall acceso (ID #12) -->
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_12.webp" data-caption="Hall de Acceso">
          <div class="amenity-img-wrap">
            <img src="assets/curated/amenities/amenities_12.webp" alt="Hall de acceso" loading="lazy">
          </div>
          <h3>Hall de Acceso</h3>
          <p>Ingreso jerarquizado con recepción y control de acceso 24hs.</p>
        </div>
      </div>"""

if old_amenities in content:
    content = content.replace(old_amenities, new_amenities)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Amenities actualizados con: Piscina en Terraza, Solárium y Gym!")
else:
    print("No se encontró el bloque exacto, reescribiendo plantilla...")
