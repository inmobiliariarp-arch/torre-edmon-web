import json

# Generador del sitio web minimalista y ultra elegante
html_code = """<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Torre Edmon | Arquitectura Residencial de Alta Gama • Frente al Río Paraná</title>
  <meta name="description" content="Torre Edmon: Emprendimiento residencial exclusivo frente al Río Paraná comercializado por Inmobiliaria Río Paraná. Semipisos de categoría con balcón aterrazado con parrilla mirando al río, piscina infinity, amenities y cocheras con cargadores eléctricos.">
  
  <link rel="icon" type="image/png" href="assets/branding/logo_inmobiliaria_clean.png">

  <!-- Typography: Cinzel & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>

  <!-- Three.js 3D Background Engine -->
  <canvas id="three-canvas"></canvas>

  <!-- Luxury Minimalist Navbar -->
  <nav class="navbar">
    <div class="container nav-container">
      <a href="#hero" class="brand-logo-wrap">
        <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="brand-logo-img">
        <span class="brand-text">TORRE EDMON</span>
      </a>

      <ul class="nav-links">
        <li><a href="#concepto" class="nav-link">El Concepto</a></li>
        <li><a href="#planta" class="nav-link">Distribución Oficial</a></li>
        <li><a href="#amenities" class="nav-link">Amenities</a></li>
        <li><a href="#galeria" class="nav-link">Galería</a></li>
        <li><a href="#especificaciones" class="nav-link">Especificaciones</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>

      <div class="nav-actions">
        <!-- Theme Switcher (Sun / Moon) -->
        <button id="theme-toggle" class="btn-icon" aria-label="Cambiar Tema" title="Modo Claro (Ojos descansados)">
          <i id="theme-icon" class="fas fa-sun"></i>
        </button>

        <a href="#contacto" class="btn-primary">
          <i class="fab fa-whatsapp"></i> Consultar
        </a>

        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Abrir Menú">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
  </nav>

  <!-- Hero Section (Clean & Cinematic) -->
  <header id="hero" class="hero">
    <div class="hero-bg">
      <img src="assets/curated/exterior/exterior_02.webp" alt="Torre Edmon Fachada Principal">
    </div>
    <div class="hero-overlay"></div>

    <div class="container hero-content">
      <div class="hero-badge">
        <i class="fas fa-gem"></i> Emprendimiento Residencial Exclusivo
      </div>
      <h1 class="hero-title">
        Vivir con Distinción <span class="text-gold-gradient">Frente al Río</span>
      </h1>
      <p class="hero-desc">
        Un nuevo estándar de vida urbana comercializado por <strong>Inmobiliaria Río Paraná</strong>. Semipisos de categoría donde <strong>el 100% de los balcones miran directamente al imponente Río Paraná</strong>.
      </p>

      <div class="hero-cta-group">
        <a href="#planta" class="btn-primary">
          <i class="fas fa-search-plus"></i> Ver Planta Oficial con Zoom
        </a>
        <a href="#galeria" class="btn-outline">
          <i class="fas fa-images"></i> Explorar Colección de Renders
        </a>
      </div>

      <div class="hero-stats">
        <div class="stat-item">
          <div class="stat-num">100%</div>
          <div class="stat-label">Balcones con Vista al Río</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">Semipisos</div>
          <div class="stat-label">Distribución Homogénea</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">EV Ready</div>
          <div class="stat-label">Cargadores Eléctricos</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">Piscina & SUM</div>
          <div class="stat-label">Azotea Panorámica</div>
        </div>
      </div>
    </div>
  </header>

  <!-- El Concepto (Minimalist Architecture) -->
  <section id="concepto" class="section-concept">
    <div class="container">
      <div class="section-tag">Arquitectura & Exclusividad</div>
      <h2 class="section-title">La Belleza de lo <span class="text-gold">Esencial</span></h2>
      <p class="section-subtitle">
        Diseñado con sobriedad y materiales nobles para brindar confort térmico, privacidad acústica y una relación permanente con el paisaje del río.
      </p>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon"><i class="fas fa-water"></i></div>
          <h3>Todos los Balcones al Río</h3>
          <p>Orientación frontal absoluta: cada semipiso disfruta de un amplio balcón terraza con parrilla propia y vista abierta al Río Paraná.</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fas fa-charging-station"></i></div>
          <h3>Cocheras EV Ready</h3>
          <p>Estacionamiento cubierto con portón automático e infraestructura prevista para la instalación de cargadores para vehículos eléctricos.</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fas fa-building"></i></div>
          <h3>Tipología Homogénea</h3>
          <p>Semipisos de jerarquía uniforme: amplitud espacial, doble ventilación cruzada y terminaciones de primera línea en cada unidad.</p>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fas fa-shield-alt"></i></div>
          <h3>Seguridad & Hall en Doble Altura</h3>
          <p>Ingreso jerarquizado con recepción, control de acceso 24hs y revestimientos nobles en mármol y porcelanato.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Planta Oficial Interactiva con Zoom & Pan -->
  <section id="planta" class="section-plans">
    <div class="container">
      <div class="section-tag">Distribución Arquitectónica Oficial</div>
      <h2 class="section-title">Planta Render & <span class="text-gold">Distribución Oficial</span></h2>
      <p class="section-subtitle">
        Explorá el plano de distribución del semipiso tipo. Podés <strong>hacer zoom con los controles o la rueda del mouse y arrastrar</strong> para examinar cada ambiente.
      </p>

      <div class="blueprint-master-card">
        <!-- Viewport Zoom & Pan -->
        <div id="plan-interactive-viewport" class="blueprint-viewport-wrapper">
          <div id="plan-canvas-container" class="blueprint-canvas-container">
            <img id="plan-zoom-img" src="assets/curated/plantas/plantas_34.webp" alt="Planta Oficial de Distribución">
            
            <div id="plan-hotspots-container" class="plan-hotspots">
              <div class="hotspot-pin" style="top: 25%; left: 30%;">
                <i class="fas fa-water"></i>
                <div class="hotspot-tooltip">
                  <strong>Balcón Terraza al Río Paraná</strong><br>
                  Parrilla individual integrada y vista frontal abierta al río.
                </div>
              </div>
              <div class="hotspot-pin" style="top: 45%; left: 48%;">
                <i class="fas fa-couch"></i>
                <div class="hotspot-tooltip">
                  <strong>Living Comedor Apaisado</strong><br>
                  Ventanales de piso a techo con DVH y ventilación cruzada.
                </div>
              </div>
              <div class="hotspot-pin" style="top: 35%; left: 75%;">
                <i class="fas fa-bed"></i>
                <div class="hotspot-tooltip">
                  <strong>Master Suite de Lujo</strong><br>
                  Dormitorio principal con vestidor exclusivo y baño en suite.
                </div>
              </div>
              <div class="hotspot-pin" style="top: 68%; left: 40%;">
                <i class="fas fa-utensils"></i>
                <div class="hotspot-tooltip">
                  <strong>Cocina de Concepto Abierto</strong><br>
                  Mobiliario a medida, mesadas de granito/cuarzo y barra desayunadora.
                </div>
              </div>
            </div>
          </div>

          <!-- Controls Bar -->
          <div class="plan-controls-bar">
            <button id="btn-zoom-out" class="plan-ctrl-btn" title="Alejar (-)"><i class="fas fa-minus"></i></button>
            <span id="zoom-level-badge" class="zoom-level-indicator">100%</span>
            <button id="btn-zoom-in" class="plan-ctrl-btn" title="Acercar (+)"><i class="fas fa-plus"></i></button>
            <button id="btn-zoom-reset" class="plan-ctrl-btn" title="Restablecer (100%)"><i class="fas fa-undo"></i></button>
            <button id="btn-zoom-fullscreen" class="plan-ctrl-btn" title="Pantalla Completa"><i class="fas fa-expand"></i></button>
          </div>
        </div>

        <!-- Sidebar Info -->
        <div class="blueprint-sidebar">
          <span class="plan-badge-pill">Unidades Homogéneas con Balcón al Río</span>
          <h3 style="font-size: 1.4rem; color: var(--gold); margin: 0.75rem 0 1rem;">Distribución Interna Completa</h3>
          
          <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">
            Semipisos diseñados para maximizar la superficie útil: estar comedor apaisado con salida al balcón terraza con parrilla propia, master suite con vestidor, segundo dormitorio luminoso y cocina integrada de diseño.
          </p>

          <ul class="plan-view-features">
            <li><i class="fas fa-check-circle"></i> Balcón terraza de gran dimensión con parrilla y vista frontal al Río Paraná.</li>
            <li><i class="fas fa-check-circle"></i> Living comedor apaisado con carpinterías herméticas DVH.</li>
            <li><i class="fas fa-check-circle"></i> Master Suite con vestidor privado y antebaño.</li>
            <li><i class="fas fa-check-circle"></i> Cocina moderna equipada con mesada en granito/cuarzo.</li>
            <li><i class="fas fa-check-circle"></i> Doble ventilación cruzada y pisos en porcelanato rectificado.</li>
          </ul>

          <div style="margin-top: 2rem;">
            <a href="#contacto" class="btn-primary" style="width: 100%; justify-content: center;">
              <i class="fab fa-whatsapp"></i> Consultar Disponibilidad
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Amenities en la Azotea & Áreas Comunes -->
  <section id="amenities" class="section-amenities">
    <div class="container">
      <div class="section-tag">Espacios Sociales & Relax</div>
      <h2 class="section-title">Amenities en la <span class="text-gold">Cúspide de la Torre</span></h2>
      <p class="section-subtitle">
        Fotografías reales y renders oficiales de los espacios sociales: piscina infinity en la azotea, solárium, quincho climatizado y hall de acceso.
      </p>

      <div class="amenities-grid">
        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_12.webp" data-caption="Piscina Infinity en Azotea con Vista al Río">
          <img src="assets/curated/amenities/amenities_12.webp" alt="Piscina Infinity" class="amenity-img" loading="lazy">
          <div class="amenity-overlay">
            <h3>Piscina Infinity en Azotea</h3>
            <p>Piscina panorámica con solárium atérmico y visuales ininterrumpidas al Río Paraná.</p>
          </div>
        </div>

        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_14.webp" data-caption="Deck Solárium y Relax">
          <img src="assets/curated/amenities/amenities_14.webp" alt="Deck Solárium" class="amenity-img" loading="lazy">
          <div class="amenity-overlay">
            <h3>Deck Solárium & Relax</h3>
            <p>Espacio al aire libre con reposeras para contemplar el atardecer sobre el río.</p>
          </div>
        </div>

        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_30.webp" data-caption="SUM & Quincho Climatizado con Parrilla">
          <img src="assets/curated/amenities/amenities_30.webp" alt="SUM y Quincho" class="amenity-img" loading="lazy">
          <div class="amenity-overlay">
            <h3>SUM & Quincho Gourmet</h3>
            <p>Salón de usos múltiples totalmente equipado con gran parrilla y mobiliario para eventos.</p>
          </div>
        </div>

        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_31.webp" data-caption="Hall de Acceso Principal en Doble Altura">
          <img src="assets/curated/amenities/amenities_31.webp" alt="Hall de Acceso" class="amenity-img" loading="lazy">
          <div class="amenity-overlay">
            <h3>Hall de Acceso en Doble Altura</h3>
            <p>Ingreso jerarquizado con revestimientos en mármol, porcelanato y recepción 24hs.</p>
          </div>
        </div>

        <div class="amenity-card" data-lightbox data-hires="assets/curated/amenities/amenities_32.webp" data-caption="Recepción y Sala de Estar">
          <img src="assets/curated/amenities/amenities_32.webp" alt="Recepción" class="amenity-img" loading="lazy">
          <div class="amenity-overlay">
            <h3>Recepción & Sala de Espera</h3>
            <p>Salón de bienvenida distinguido para recibir visitas con total confort y seguridad.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Galería Curada con Filtros -->
  <section id="galeria" class="section-gallery">
    <div class="container">
      <div class="section-tag">Colección Visual en Alta Definición</div>
      <h2 class="section-title">Galería de <span class="text-gold">Renders Curados</span></h2>
      <p class="section-subtitle">
        Perspectivas limpias y en alta resolución de Torre Edmon. Haz clic en cualquier imagen para verla en pantalla completa.
      </p>

      <div class="gallery-filter-bar">
        <button class="filter-btn active" data-filter="all">Todos</button>
        <button class="filter-btn" data-filter="exterior">Exteriores</button>
        <button class="filter-btn" data-filter="interiores">Interiores</button>
        <button class="filter-btn" data-filter="amenities">Amenities</button>
        <button class="filter-btn" data-filter="plantas">Plantas</button>
      </div>

      <div class="gallery-masonry">
        <!-- Exteriores -->
        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_02.webp" data-caption="Fachada Principal - Torre Edmon">
          <img src="assets/curated/exterior/exterior_02.webp" alt="Fachada Principal" loading="lazy">
          <div class="gallery-hover-info"><h4>Fachada Principal</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_05.webp" data-caption="Vista Arquitectónica de Acceso">
          <img src="assets/curated/exterior/exterior_05.webp" alt="Acceso" loading="lazy">
          <div class="gallery-hover-info"><h4>Acceso Principal</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_06.webp" data-caption="Fachada Diurna y Entorno">
          <img src="assets/curated/exterior/exterior_06.webp" alt="Fachada Diurna" loading="lazy">
          <div class="gallery-hover-info"><h4>Fachada Diurna</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_07.webp" data-caption="Perspectiva Urbana">
          <img src="assets/curated/exterior/exterior_07.webp" alt="Perspectiva" loading="lazy">
          <div class="gallery-hover-info"><h4>Perspectiva Urbana</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_08.webp" data-caption="Terrazas con Vistas al Río">
          <img src="assets/curated/exterior/exterior_08.webp" alt="Terrazas" loading="lazy">
          <div class="gallery-hover-info"><h4>Terrazas al Río</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_10.webp" data-caption="Iluminación Nocturna">
          <img src="assets/curated/exterior/exterior_10.webp" alt="Vista Nocturna" loading="lazy">
          <div class="gallery-hover-info"><h4>Vista Nocturna</h4><span>Exteriores</span></div>
        </div>

        <div class="gallery-item" data-category="exterior" data-lightbox data-hires="assets/curated/exterior/exterior_13.webp" data-caption="Detalles Constructivos de Fachada">
          <img src="assets/curated/exterior/exterior_13.webp" alt="Detalles Fachada" loading="lazy">
          <div class="gallery-hover-info"><h4>Detalles Constructivos</h4><span>Exteriores</span></div>
        </div>

        <!-- Interiores -->
        <div class="gallery-item" data-category="interiores" data-lightbox data-hires="assets/curated/interiores/interiores_03.webp" data-caption="Ubicación y Entorno Ribereño">
          <img src="assets/curated/interiores/interiores_03.webp" alt="Ubicación" loading="lazy">
          <div class="gallery-hover-info"><h4>Ubicación Estratégica</h4><span>Entorno</span></div>
        </div>

        <div class="gallery-item" data-category="interiores" data-lightbox data-hires="assets/curated/interiores/interiores_23.webp" data-caption="Living Comedor con Vistas al Río">
          <img src="assets/curated/interiores/interiores_23.webp" alt="Living Comedor" loading="lazy">
          <div class="gallery-hover-info"><h4>Living Comedor</h4><span>Interiores</span></div>
        </div>

        <div class="gallery-item" data-category="interiores" data-lightbox data-hires="assets/curated/interiores/interiores_26.webp" data-caption="Cocina Integrada con Barra Desayunadora">
          <img src="assets/curated/interiores/interiores_26.webp" alt="Cocina Integrada" loading="lazy">
          <div class="gallery-hover-info"><h4>Cocina Integrada</h4><span>Interiores</span></div>
        </div>

        <div class="gallery-item" data-category="interiores" data-lightbox data-hires="assets/curated/interiores/interiores_27.webp" data-caption="Master Suite con Vestidor">
          <img src="assets/curated/interiores/interiores_27.webp" alt="Master Suite" loading="lazy">
          <div class="gallery-hover-info"><h4>Master Suite</h4><span>Interiores</span></div>
        </div>

        <div class="gallery-item" data-category="interiores" data-lightbox data-hires="assets/curated/interiores/interiores_28.webp" data-caption="Balcón Terraza con Parrilla al Río">
          <img src="assets/curated/interiores/interiores_28.webp" alt="Balcón al Río" loading="lazy">
          <div class="gallery-hover-info"><h4>Balcón con Parrilla al Río</h4><span>Interiores</span></div>
        </div>

        <!-- Amenities -->
        <div class="gallery-item" data-category="amenities" data-lightbox data-hires="assets/curated/amenities/amenities_12.webp" data-caption="Piscina Infinity en Azotea">
          <img src="assets/curated/amenities/amenities_12.webp" alt="Piscina Infinity" loading="lazy">
          <div class="gallery-hover-info"><h4>Piscina Infinity</h4><span>Amenities</span></div>
        </div>

        <div class="gallery-item" data-category="amenities" data-lightbox data-hires="assets/curated/amenities/amenities_30.webp" data-caption="SUM & Quincho Climatizado">
          <img src="assets/curated/amenities/amenities_30.webp" alt="SUM y Quincho" loading="lazy">
          <div class="gallery-hover-info"><h4>SUM & Quincho</h4><span>Amenities</span></div>
        </div>

        <!-- Plantas -->
        <div class="gallery-item" data-category="plantas" data-lightbox data-hires="assets/curated/plantas/plantas_34.webp" data-caption="Planta Oficial de Distribución">
          <img src="assets/curated/plantas/plantas_34.webp" alt="Planta Distribución" loading="lazy">
          <div class="gallery-hover-info"><h4>Planta de Distribución</h4><span>Planos</span></div>
        </div>

        <div class="gallery-item" data-category="plantas" data-lightbox data-hires="assets/curated/plantas/plantas_22.webp" data-caption="Planta Nivel Semipisos">
          <img src="assets/curated/plantas/plantas_22.webp" alt="Planta Nivel" loading="lazy">
          <div class="gallery-hover-info"><h4>Planta Nivel Semipisos</h4><span>Planos</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Especificaciones Técnicas & Cocheras EV -->
  <section id="especificaciones" class="section-specs">
    <div class="container">
      <div class="section-tag">Máxima Calidad Constructiva</div>
      <h2 class="section-title">Especificaciones <span class="text-gold">Técnicas</span></h2>
      <p class="section-subtitle">
        Materiales de excelencia, aislación termoacústica y tecnología de vanguardia.
      </p>

      <div class="specs-container">
        <div class="spec-category-card">
          <h3><i class="fas fa-layer-group"></i> Terminaciones & Estructura</h3>
          <ul>
            <li>Pisos de porcelanato rectificado de primera calidad en estar, cocina y dormitorios.</li>
            <li>Aberturas de aluminio anodizado línea pesada con Doble Vidriado Hermético (DVH).</li>
            <li>Zócalos laqueados y terminaciones en enlucido de yeso en todos los muros interiores.</li>
            <li>Puertas de madera de diseño contemporáneo con herrajes de acero inoxidable.</li>
          </ul>
        </div>

        <div class="spec-category-card">
          <h3><i class="fas fa-utensils"></i> Cocina & Baños</h3>
          <ul>
            <li>Mobiliario a medida bajo mesada y alacenas en melamina texturada con cantos ABS.</li>
            <li>Mesadas de granito / cuarzo con bacha doble de acero inoxidable y grifería monocomando.</li>
            <li>Artefactos sanitarios Ferrum / Roca con válvulas de descarga ecológica.</li>
            <li>Revestimientos porcelánicos de piso a techo en baños y cocinas.</li>
          </ul>
        </div>

        <div class="spec-category-card">
          <h3><i class="fas fa-charging-station"></i> Cocheras EV & Instalaciones</h3>
          <ul>
            <li>Infraestructura prevista en cocheras para la instalación de <strong>cargadores para vehículos eléctricos (EV Ready)</strong>.</li>
            <li>Parrilla individual con tiraje independiente en el balcón de cada departamento.</li>
            <li>Preinstalación embutida completa para equipos de aire acondicionado split frío/calor.</li>
            <li>Ascensores inteligentes de alta velocidad con cabinas de acero inoxidable.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Comercialización & Contacto -->
  <section id="contacto" class="section-contact">
    <div class="container">
      <div class="commercial-card">
        <div class="inmo-branding">
          <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="inmo-logo-display">
          <div class="section-tag" style="margin: 0;">Comercialización Exclusiva</div>
          <h2 style="font-size: 2rem; margin: 0.5rem 0;">Inmobiliaria Río Paraná</h2>
          <p class="text-muted">
            Líderes en desarrollos de categoría en la región litoral. Te brindamos asesoramiento personalizado y financiación a medida para que seas parte de Torre Edmon.
          </p>

          <ul class="contact-info-list">
            <li><i class="fas fa-map-marker-alt"></i> Av. Costanera y Centro, Región Litoral, Argentina</li>
            <li><i class="fas fa-phone-alt"></i> +54 9 379 400-0000</li>
            <li><i class="fas fa-envelope"></i> contacto@inmobiliariarioparana.com</li>
            <li><i class="fas fa-clock"></i> Lunes a Viernes de 8:30 a 19:00 hs</li>
          </ul>

          <div style="display: flex; gap: 0.8rem; flex-wrap: wrap;">
            <a href="https://wa.me/5493794000000?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20informaci%C3%B3n%20sobre%20los%20semipisos%20de%20Torre%20Edmon" target="_blank" class="btn-primary">
              <i class="fab fa-whatsapp"></i> Chat WhatsApp Directo
            </a>
          </div>
        </div>

        <form id="contact-form" class="contact-form">
          <h3 style="font-size: 1.35rem; margin-bottom: 0.5rem;" class="text-gold">Solicitar Información & Financiación</h3>
          
          <div class="form-group">
            <label for="form-nombre">Nombre y Apellido</label>
            <input type="text" id="form-nombre" class="form-control" placeholder="Ej. Juan Pérez" required>
          </div>

          <div class="form-group">
            <label for="form-telefono">Teléfono / Celular</label>
            <input type="tel" id="form-telefono" class="form-control" placeholder="Ej. +54 9 379 1234567" required>
          </div>

          <div class="form-group">
            <label for="form-mensaje">Consulta o Pregunta</label>
            <textarea id="form-mensaje" class="form-control" rows="3" placeholder="Quisiera conocer disponibilidad de pisos y formas de pago..."></textarea>
          </div>

          <button type="submit" class="btn-primary" style="justify-content: center; width: 100%; font-size: 1rem; padding: 0.9rem;">
            <i class="fab fa-whatsapp"></i> Enviar Consulta a Inmobiliaria Río Paraná
          </button>
        </form>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div>
          <h3 class="font-serif" style="font-size: 1.4rem; margin-bottom: 0.75rem;">TORRE EDMON</h3>
          <p class="text-muted" style="max-width: 400px; font-size: 0.92rem;">
            Un emprendimiento residencial concebido para quienes buscan un estilo de vida superior frente al Río Paraná, comercializado por <strong>Inmobiliaria Río Paraná</strong>.
          </p>
        </div>

        <div>
          <h4 style="font-size: 1rem; margin-bottom: 1rem; color: var(--gold-primary);">Navegación</h4>
          <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.92rem;">
            <li><a href="#concepto" class="nav-link">El Concepto</a></li>
            <li><a href="#planta" class="nav-link">Distribución Oficial</a></li>
            <li><a href="#amenities" class="nav-link">Amenities</a></li>
            <li><a href="#galeria" class="nav-link">Galería</a></li>
            <li><a href="#especificaciones" class="nav-link">Especificaciones</a></li>
          </ul>
        </div>

        <div>
          <h4 style="font-size: 1rem; margin-bottom: 1rem; color: var(--gold-primary);">Comercialización Oficial</h4>
          <p class="text-muted" style="font-size: 0.92rem; margin-bottom: 0.5rem;">
            <strong>Inmobiliaria Río Paraná</strong>
          </p>
          <p class="text-muted" style="font-size: 0.88rem;">
            Región Litoral • Argentina<br>
            contacto@inmobiliariarioparana.com
          </p>
        </div>
      </div>

      <div class="footer-bottom">
        <span>&copy; 2026 Torre Edmon. Todos los derechos reservados. Comercializa Inmobiliaria Río Paraná.</span>
        <span>Renders, planos y especificaciones corresponden al folleto oficial del proyecto.</span>
      </div>
    </div>
  </footer>

  <!-- Lightbox Modal for HD Renders & Blueprints -->
  <div id="lightbox-modal" class="lightbox-modal" role="dialog" aria-hidden="true">
    <div class="lightbox-content">
      <button id="lightbox-close" class="lightbox-close" aria-label="Cerrar">&times;</button>
      <img id="lightbox-img" src="" alt="Vista previa" class="lightbox-img">
      <div id="lightbox-caption" class="lightbox-caption"></div>
    </div>
  </div>

  <!-- Floating WhatsApp CTA Button -->
  <a href="https://wa.me/5493794000000?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20consultar%20por%20los%20semipisos%20de%20Torre%20Edmon" target="_blank" class="floating-whatsapp" aria-label="Contactar por WhatsApp">
    <i class="fab fa-whatsapp"></i>
  </a>

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

print("index.html ensamblado con los assets curados definitivos!")
