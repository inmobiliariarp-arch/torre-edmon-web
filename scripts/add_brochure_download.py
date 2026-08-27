import shutil
import os

src_pdf = r"D:\Proyecto sitio web edificio\assets\FOLLETO TORRE EDMON Posadas.pdf"
dst_pdf = r"D:\Proyecto sitio web edificio\assets\folleto_torre_edmon_posadas.pdf"

shutil.copyfile(src_pdf, dst_pdf)
print(f"Copia creada exitosamente: {dst_pdf} ({os.path.getsize(dst_pdf) / (1024*1024):.2f} MB)")

# Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Brochure button to navbar
old_nav_actions = """      <div class="nav-actions">
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

new_nav_actions = """      <div class="nav-actions">
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

html = html.replace(old_nav_actions, new_nav_actions)

# 2. Add Brochure download CTA button in El Proyecto section
old_proyecto_p = """          <p>
            El complejo cuenta con veintiséis departamentos de 217 m² y 218 m² propios, diseñados con amplitud y luminosidad. Sus amenities incluyen gimnasio, terraza con SUM, solárium y piscina, además de <strong>55 cocheras con infraestructura para cargadores de vehículos eléctricos (EV Ready)</strong> que garantizan comodidad y seguridad.
          </p>
        </div>"""

new_proyecto_p = """          <p>
            El complejo cuenta con veintiséis departamentos de 217 m² y 218 m² propios, diseñados con amplitud y luminosidad. Sus amenities incluyen gimnasio, terraza con SUM, solárium y piscina, además de <strong>55 cocheras con infraestructura para cargadores de vehículos eléctricos (EV Ready)</strong> que garantizan comodidad y seguridad.
          </p>
          <div style="margin-top: 1.75rem;">
            <a href="assets/folleto_torre_edmon_posadas.pdf" download="FOLLETO_TORRE_EDMON_Posadas.pdf" class="btn-primary" style="gap: 0.75rem;">
              <i class="fas fa-download"></i> Descargar Brochure Oficial (PDF)
            </a>
          </div>
        </div>"""

html = html.replace(old_proyecto_p, new_proyecto_p)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html actualizado con el botón de descarga del brochure!")
