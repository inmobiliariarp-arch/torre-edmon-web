html_code = """<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Torre Edmon | Posadas Misiones</title>
  <meta name="description" content="Torre Edmon: Residencias exclusivas en Posadas Misiones. Comercializa Inmobiliaria Río Paraná.">
  
  <link rel="icon" type="image/png" href="assets/branding/logo_inmobiliaria_clean.png">

  <!-- Typography: Cinzel & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>

  <!-- Three.js Ambient Particle Background -->
  <canvas id="three-canvas"></canvas>

  <!-- Luxury Minimalist Navbar -->
  <nav class="navbar">
    <div class="container nav-container">
      <a href="#hero" class="brand-logo-wrap">
        <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="brand-logo-img">
        <span class="brand-text">TORRE EDMON</span>
      </a>

      <ul class="nav-links">
        <li><a href="#proyecto" class="nav-link">El Proyecto</a></li>
        <li><a href="#interiores" class="nav-link">Interiores</a></li>
        <li><a href="#planta" class="nav-link">Planta Tipo</a></li>
        <li><a href="#amenities" class="nav-link">Amenities</a></li>
        <li><a href="#ubicacion" class="nav-link">Ubicación</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>

      <div class="nav-actions">
        <button id="theme-toggle" class="btn-icon" aria-label="Cambiar Tema" title="Modo Claro">
          <i id="theme-icon" class="fas fa-sun"></i>
        </button>

        <a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20informaci%C3%B3n%20sobre%20Torre%20Edmon" target="_blank" class="btn-primary">
          <i class="fab fa-whatsapp"></i> Contacto
        </a>

        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Abrir Menú">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
  </nav>

  <!-- Hero Section with Full-Bleed Drone Video -->
  <header id="hero" class="hero">
    <div class="hero-video-bg">
      <video autoplay muted loop playsinline poster="assets/curated/exterior/exterior_02.webp">
        <source src="assets/video_drone_costanera.mp4" type="video/mp4">
      </video>
    </div>
    <div class="hero-overlay"></div>

    <div class="container hero-content">
      <div class="hero-tagline">Residencias Exclusivas</div>
      <h1 class="hero-title">
        TORRE EDMON<br>
        <span class="text-gold-gradient">Posadas Misiones</span>
      </h1>
      <div class="hero-gold-divider"></div>

      <div class="scroll-hint">
        <span>Descubrir</span>
        <i class="fas fa-chevron-down"></i>
      </div>
    </div>
  </header>

  <!-- El Proyecto (Editorial Minimalist Architecture) -->
  <section id="proyecto">
    <div class="container">
      <div class="features-minimal-grid">
        <div class="feature-editorial-text">
          <div class="section-tag">Arquitectura & Exclusividad</div>
          <h2 class="section-title" style="font-size: 2.3rem;">Conexión Única con el <span class="text-gold">Entorno</span></h2>
          <p>
            Con vistas panorámicas hacia la ciudad de Posadas y el río Paraná, cada unidad ofrece una conexión única con el entorno.
          </p>
          <p>
            El complejo cuenta con veintiséis departamentos de 217 m² y 218 m² propios, diseñados con amplitud y luminosidad. Sus amenities incluyen gimnasio, terraza con SUM, solárium y piscina, además de <strong>55 cocheras con infraestructura para cargadores de vehículos eléctricos (EV Ready)</strong> que garantizan comodidad y seguridad.
          </p>
        </div>
        <div class="feature-editorial-img" data-lightbox data-hires="assets/curated/exterior/exterior_02.webp" data-caption="Fachada Principal - Torre Edmon">
          <img src="assets/curated/exterior/exterior_02.webp" alt="Fachada Principal Torre Edmon">
        </div>
      </div>
    </div>
  </section>

  <!-- Interiores & Balcones (Architectural Monograph) -->
  <section id="interiores" style="padding-top: 0;">
    <div class="container">
      <div style="text-align: center; margin-bottom: 3.5rem;">
        <div class="section-tag">Detalles & Espacios</div>
        <h2 class="section-title">Interiores & <span class="text-gold">Balcones</span></h2>
      </div>

      <div class="interiors-grid">
        <!-- Balcon (ID #27) -->
        <div class="interior-card" data-lightbox data-hires="assets/curated/interiores/interiores_27.webp" data-caption="Balcón Terraza con Parrilla Propia al Río Paraná">
          <div class="interior-card-img">
            <img src="assets/curated/interiores/interiores_27.webp" alt="Balcón Terraza con Parrilla al Río" loading="lazy">
          </div>
          <div>
            <div class="interior-card-title">Balcón con Parrilla al Río</div>
            <div class="interior-card-desc">Terraza individual con tiraje independiente y visuales directas al agua.</div>
          </div>
        </div>

        <!-- Living (ID #26) -->
        <div class="interior-card" data-lightbox data-hires="assets/curated/interiores/interiores_26.webp" data-caption="Living Comedor Apaisado con Vista al Río">
          <div class="interior-card-img">
            <img src="assets/curated/interiores/interiores_26.webp" alt="Living Comedor con Vista al Río" loading="lazy">
          </div>
          <div>
            <div class="interior-card-title">Living Comedor Apaisado</div>
            <div class="interior-card-desc">Amplios ventanales con doble vidriado hermético y ventilación cruzada.</div>
          </div>
        </div>

        <!-- Master Bedroom (ID #28) -->
        <div class="interior-card" data-lightbox data-hires="assets/curated/interiores/interiores_28.webp" data-caption="Master Bedroom con Vestidor">
          <div class="interior-card-img">
            <img src="assets/curated/interiores/interiores_28.webp" alt="Master Bedroom con Vestidor" loading="lazy">
          </div>
          <div>
            <div class="interior-card-title">Master Bedroom</div>
            <div class="interior-card-desc">Dormitorio principal con vestidor exclusivo y baño en suite.</div>
          </div>
        </div>

        <!-- Cocina (ID #24) -->
        <div class="interior-card" data-lightbox data-hires="assets/curated/interiores/interiores_24.webp" data-caption="Cocina Integrada con Isla">
          <div class="interior-card-img">
            <img src="assets/curated/interiores/interiores_24.webp" alt="Cocina Integrada" loading="lazy">
          </div>
          <div>
            <div class="interior-card-title">Cocina Integrada</div>
            <div class="interior-card-desc">Mobiliario a medida, mesadas de granito/cuarzo y barra desayunadora.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Planta Tipo (In-place Smooth & Tactile Zoom) -->
  <section id="planta" style="padding-top: 2rem;">
    <div class="container">
      <div style="text-align: center; margin-bottom: 2.5rem;">
        <div class="section-tag">Distribución</div>
        <h2 class="section-title">Planta Tipo</h2>
      </div>

      <div class="plan-container-card">
        <div id="plan-interactive-box" class="plan-interactive-wrapper">
          <button class="plan-zoom-badge-btn" data-lightbox data-hires="assets/curated/plantas/plantas_34.webp" data-caption="Planta Tipo - Distribución Oficial">
            <i class="fas fa-search-plus"></i> Zoom
          </button>
          <img id="plan-zoom-img" src="assets/curated/plantas/plantas_34.webp" alt="Planta Tipo Torre Edmon">
        </div>
      </div>
    </div>
  </section>

  <!-- Amenities (Curated Clean Visual Cards) -->
  <section id="amenities">
    <div class="container">
      <div style="text-align: center; margin-bottom: 3.5rem;">
        <div class="section-tag">Espacios Comunes</div>
        <h2 class="section-title">Amenities</h2>
      </div>

      <div class="amenities-grid">
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
      </div>
    </div>
  </section>

  <!-- Ubicación & Entorno -->
  <section id="ubicacion">
    <div class="container">
      <div style="text-align: center; margin-bottom: 3.5rem;">
        <div class="section-tag">Ubicación Estratégica</div>
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
  </section>

  <!-- Contacto Inmobiliaria Río Paraná (Clean & Discreet) -->
  <section id="contacto" style="padding-bottom: 6rem;">
    <div class="container">
      <div class="contact-section-card">
        <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="contact-logo">
        <div class="section-tag" style="margin: 0 auto 0.5rem;">Comercialización Exclusiva</div>
        <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Inmobiliaria Río Paraná</h2>
        <p class="text-muted" style="max-width: 500px; margin: 0 auto;">
          Para consultas, valores y disponibilidad de unidades en Torre Edmon.
        </p>

        <div class="contact-details-row">
          <div class="contact-detail-item">
            <i class="fas fa-envelope"></i>
            <span>Correo Electrónico</span>
            <strong><a href="mailto:inmobiliariarp@gmail.com" style="color:inherit; text-decoration:none;">inmobiliariarp@gmail.com</a></strong>
          </div>

          <div class="contact-detail-item">
            <i class="fab fa-whatsapp"></i>
            <span>Celular / WhatsApp</span>
            <strong><a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20consultar%20por%20Torre%20Edmon" target="_blank" style="color:inherit; text-decoration:none;">+54 9 3764 765431</a></strong>
          </div>
        </div>

        <a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20consultar%20por%20Torre%20Edmon" target="_blank" class="btn-primary" style="padding: 0.9rem 2.2rem; font-size: 0.95rem;">
          <i class="fab fa-whatsapp"></i> Contactar por WhatsApp
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <p>&copy; 2026 Torre Edmon. Posadas, Misiones. Comercializa <strong>Inmobiliaria Río Paraná</strong>.</p>
    </div>
  </footer>

  <!-- Lightbox Modal for Full Resolution Views -->
  <div id="lightbox-modal" class="lightbox-modal" role="dialog" aria-hidden="true">
    <div class="lightbox-content">
      <button id="lightbox-close" class="lightbox-close" aria-label="Cerrar">&times;</button>
      <img id="lightbox-img" src="" alt="Vista previa" class="lightbox-img">
      <div id="lightbox-caption" class="lightbox-caption"></div>
    </div>
  </div>

  <!-- Three.js CDN -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <!-- Application Scripts -->
  <script src="js/three-scene.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("index.html actualizado con Posadas Misiones, mapa de ubicación, zoom táctil y texto exacto!")
