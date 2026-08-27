with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix navbar to eliminate duplicate "Contacto"
old_navbar = """      <ul class="nav-links">
        <li><a href="#proyecto" class="nav-link">El Proyecto</a></li>
        <li><a href="#interiores" class="nav-link">Interiores</a></li>
        <li><a href="#planta" class="nav-link">Planta Tipo</a></li>
        <li><a href="#amenities" class="nav-link">Amenities</a></li>
        <li><a href="#ubicacion" class="nav-link">Ubicación</a></li>
        <li><a href="#contacto" class="nav-link">Contacto</a></li>
      </ul>

      <div class="nav-actions">
        <a href="assets/folleto_torre_edmon_posadas.pdf" download="FOLLETO_TORRE_EDMON_Posadas.pdf" class="btn-secondary-nav" title="Descargar Brochure Oficial">
          <i class="fas fa-file-pdf"></i> <span>Brochure</span>
        </a>

        <button id="theme-toggle" class="btn-icon" aria-label="Cambiar Tema" title="Modo Claro">
          <i id="theme-icon" class="fas fa-sun"></i>
        </button>

        <a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20informaci%C3%B3n%20sobre%20Torre%20Edmon" target="_blank" class="btn-primary">
          <i class="fab fa-whatsapp"></i> Contacto
        </a>

        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Abrir Menú">
          <i class="fas fa-bars"></i>
        </button>
      </div>"""

new_navbar = """      <ul class="nav-links">
        <li><a href="#proyecto" class="nav-link">El Proyecto</a></li>
        <li><a href="#interiores" class="nav-link">Interiores</a></li>
        <li><a href="#planta" class="nav-link">Planta Tipo</a></li>
        <li><a href="#amenities" class="nav-link">Amenities</a></li>
        <li><a href="#ubicacion" class="nav-link">Ubicación</a></li>
      </ul>

      <div class="nav-actions">
        <a href="assets/folleto_torre_edmon_posadas.pdf" download="FOLLETO_TORRE_EDMON_Posadas.pdf" class="btn-secondary-nav" title="Descargar Brochure Oficial">
          <i class="fas fa-file-pdf"></i> <span>Brochure</span>
        </a>

        <button id="theme-toggle" class="btn-icon" aria-label="Cambiar Tema" title="Modo Claro">
          <i id="theme-icon" class="fas fa-sun"></i>
        </button>

        <a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20informaci%C3%B3n%20sobre%20Torre%20Edmon" target="_blank" class="btn-primary" title="Consultar por WhatsApp">
          <i class="fab fa-whatsapp"></i> <span>Consultar</span>
        </a>

        <button id="mobile-menu-btn" class="mobile-menu-btn" aria-label="Abrir Menú">
          <i class="fas fa-bars"></i>
        </button>
      </div>"""

html = html.replace(old_navbar, new_navbar)

# 2. Redesign Contact & Footer into a single, quiet luxury section
old_contact_and_footer = """  <!-- Contacto Inmobiliaria Río Paraná (Clean & Discreet) -->
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
  </footer>"""

new_contact_and_footer = """  <!-- Comercialización Oficial & Contacto (Quiet Luxury Monograph) -->
  <footer id="contacto" class="luxury-footer">
    <div class="container">
      <div class="footer-monograph">
        <img src="assets/branding/logo_inmobiliaria_clean.png" alt="Inmobiliaria Río Paraná" class="footer-brand-logo">
        
        <div class="footer-title-wrap">
          <span class="footer-tag">Comercialización Exclusiva</span>
          <h2 class="footer-brand-name">Inmobiliaria Río Paraná</h2>
          <p class="footer-subtitle">Atención personalizada y asesoramiento en inversiones de categoría.</p>
        </div>

        <div class="footer-contact-pills">
          <a href="mailto:inmobiliariarp@gmail.com" class="contact-pill-link">
            <i class="fas fa-envelope"></i> inmobiliariarp@gmail.com
          </a>
          <a href="https://wa.me/5493764765431?text=Hola%20Inmobiliaria%20R%C3%ADo%20Paran%C3%A1,%20quiero%20consultar%20por%20Torre%20Edmon" target="_blank" class="contact-pill-link highlight">
            <i class="fab fa-whatsapp"></i> +54 9 3764 765431
          </a>
          <span class="contact-pill-text">
            <i class="fas fa-map-marker-alt"></i> Posadas, Misiones
          </span>
        </div>

        <div class="footer-legal">
          <p>&copy; 2026 <strong>TORRE EDMON</strong> • Desarrollos Inmobiliarios de Alta Gama. Todos los derechos reservados.</p>
        </div>
      </div>
    </div>
  </footer>"""

html = html.replace(old_contact_and_footer, new_contact_and_footer)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html rediseñado con footer de contacto ultra elegante y sin duplicaciones!")
