part1 = """<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Torre Edmon | Arquitectura Residencial de Vanguardia • Frente al Río Paraná</title>
  <meta name="description" content="Torre Edmon: Emprendimiento residencial de alta categoría frente al Río Paraná, comercializado por Inmobiliaria Río Paraná. Semipisos de diseño exclusivo, todos los balcones con vista al río y parrilla, piscina infinity, solárium, SUM y cocheras con cargadores eléctricos.">
  <link rel="icon" type="image/png" href="assets/branding/logo_inmobiliaria_clean.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>
  <canvas id="three-canvas"></canvas>
  <nav class="navbar">
    <div class="container nav-container">
      <a href="#hero" class="brand-logo-wrap">
        <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="brand-logo-img">
        <span class="brand-text">TORRE EDMON</span>
      </a>
      <ul class="nav-links">
        <li><a href="#proyecto" class="nav-link">El Proyecto</a></li>
        <li><a href="#plantas" class="nav-link">Distribución & Planos</a></li>
        <li><a href="#amenities" class="nav-link">Amenities</a></li>
        <li><a href="#galeria" class="nav-link">Galería HD</a></li>
        <li><a href="#especificaciones" class="nav-link">Especificaciones</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>
      <div class="nav-actions">
        <button id="theme-toggle" class="btn-icon" aria-label="Cambiar Tema (Sol/Luna)" title="Modo Claro (Ojos descansados)">
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
  <header id="hero" class="hero">
    <div class="hero-bg">
      <img src="assets/web_optimized/slide_01.webp" alt="Torre Edmon Fachada Principal">
    </div>
    <div class="hero-overlay"></div>
    <div class="container hero-content">
      <div class="hero-badge">
        <i class="fas fa-gem"></i> Emprendimiento Residencial Exclusivo
      </div>
      <h1 class="hero-title">
        La Cumbre del Diseño <span class="text-gold-gradient">Frente al Río</span>
      </h1>
      <p class="hero-desc">
        Un hito arquitectónico contemporáneo comercializado por <strong>Inmobiliaria Río Paraná</strong>. Exclusivos semipisos de máxima jerarquía, donde <strong>todos los balcones cuentan con vista frontal y abierta al imponente Río Paraná</strong>.
      </p>
      <div class="hero-cta-group">
        <a href="#plantas" class="btn-primary">
          <i class="fas fa-search-plus"></i> Explorar Plano con Zoom
        </a>
        <a href="#galeria" class="btn-outline">
          <i class="fas fa-images"></i> Galería de Renders
        </a>
      </div>
      <div class="hero-stats">
        <div class="stat-item">
          <div class="stat-num">100%</div>
          <div class="stat-label">Balcones al Río Paraná</div>
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
          <div class="stat-num">Azotea VIP</div>
          <div class="stat-label">Piscina & Solárium</div>
        </div>
      </div>
    </div>
  </header>
"""
with open("scripts/part1.html", "w", encoding="utf-8") as f:
    f.write(part1)
print("Part 1 written")
