import os

docs_dir = r"D:\Proyecto sitio web edificio\docs"
os.makedirs(docs_dir, exist_ok=True)

workflows_dir = r"D:\Proyecto sitio web edificio\.github\workflows"
os.makedirs(workflows_dir, exist_ok=True)

# 1. docs/ARCHITECTURE.md
arch_content = """# 🏛️ Arquitectura Técnica y Especificación del Sistema Frontend

## 🌐 Visión General
El sitio web interactivo de **Torre Edmond** fue diseñado con una arquitectura **Vanilla Modular de Cero Dependencias Pesadas** (*Zero-Bloat SPA*). Prioriza la máxima velocidad de carga, fluidez a 60 FPS, adaptabilidad a cualquier tamaño de pantalla y una experiencia de usuario de lujo arquitectónico.

---

## 🧩 Componentes del Sistema

### 1. Núcleo Semántico (`index.html`)
- Estructura HTML5 accesible y orientada a SEO inmobiliario.
- Metadatos OpenGraph y Twitter Cards para previsualización enriquecida al compartir en redes sociales y WhatsApp.
- Secciones modulares:
  - **Hero Section**: Canvas 3D con partículas de oro, titulares cinéticos y llamadas a la acción (*CTA*).
  - **Concepto Arquitectónico**: Propuesta de valor, diseño de vanguardia y sustentabilidad.
  - **Visor Interactivo de Tipologías**: Selector en tiempo real de 1, 2 dormitorios, monoambientes y pisos exclusivos.
  - **Galería de Amenities & Rooftop**: Vistas 3D de piscina infinita, SUM climatizado y solárium.
  - **Ubicación Estratégica**: Mapa y entorno en Posadas, Misiones.
  - **Folleto & Descargas**: Enlace directo al folleto comercial de alta resolución.
  - **Contacto & Fideicomiso**: Integración directa con Inmobiliaria Río Paraná y marco legal del Fideicomiso Costa Posadas.

### 2. Capa de Estilos y Design Tokens (`styles/main.css`)
- **Variables CSS Nativas**:
  - `--gold-primary`: `#D4AF37` (Oro puro)
  - `--gold-light`: `#F3E5AB`
  - `--gold-dark`: `#AA7C11`
  - `--bg-dark`: `#0d0f12`
  - `--bg-light`: `#f8f9fa`
  - `--text-primary`: `#ffffff` (Dark) / `#1a1a1a` (Light)
- **Soporte Bimodal (Dark / Light Mode)**:
  - Selector conmutable con persistencia en `localStorage`.
  - Modo oscuro calibrado para mitigar la fatiga visual (*Eye-Care*).
- **Efectos Visuales**:
  - *Glassmorphism* con `backdrop-filter: blur(12px)`.
  - Bordes con gradientes metálicos simulando perfiles de aluminio y bronce.

### 3. Escena WebGL 3D (`js/three-scene.js`)
- Motor gráfico Three.js (v0.160.0).
- Nube de partículas de oro renderizada mediante `BufferGeometry`.
- Sistema de seguimiento de cursor (*Mouse Parallax*) con amortiguación suave.
- Destrucción y redimensionamiento seguro de escena ante cambios de resolución.

### 4. Motor de Audio Sintetizado (`js/audio.js`)
- Implementación nativa con **Web Audio API** del navegador.
- Sintetizador armónico sin archivos de audio externos (0 KB de transferencia de red).
- Frecuencia base de 520Hz con envolvente exponencial suave para dar feedback táctil acústico en clics y cambios de unidad.

### 5. Controlador de Estado y UI (`js/app.js`)
- Gestión de eventos de navegación fluida (*smooth-scroll*).
- Conmutador de tipologías arquitectónicas y actualización dinámica del DOM.
- Modales de visualización ampliada de planos y renders.
- Control de tema e interacción con el motor de audio.
"""

with open(os.path.join(docs_dir, "ARCHITECTURE.md"), "w", encoding="utf-8") as f:
    f.write(arch_content.strip() + "\n")

# 2. docs/COMMERCIAL_SPEC.md
comm_content = """# 🏢 Especificación Comercial y Marco Fiduciario — Torre Edmond

## 🏛️ 1. Estructura Jurídica: Fideicomiso Costa Posadas
- **Denominación**: Fideicomiso Inmobiliario Costa Posadas
- **Tipo**: Fideicomiso Inmobiliario de Construcción al Costo y Administración
- **Fiduciario & Administrador**: Don Ruben Mario CARREÑO
- **Marco Legal**: Código Civil y Comercial de la Nación (Arts. 1666 a 1700) y Ley 24.441.
- **Comercialización Exclusiva**: Inmobiliaria Río Paraná (Sede Jujuy 2255 PB, Posadas, Misiones).

---

## 🎯 2. Propuesta de Valor y Target
- **Inversores de Renta**: Monoambientes y unidades de 1 dormitorio con alta tasa de retorno por alquiler tradicional y temporario en Posadas.
- **Familias y Usuarios Finales**: Unidades de 2 y 3 dormitorios con amplios balcones aterrazados, parrillas individuales y cocheras cubiertas.
- **Ubicación Privilegiada**: Entorno residencial consolidado con fácil acceso al centro y a la Costanera de Posadas.

---

## 📐 3. Programa Arquitectónico y Amenities
1. **Piscina Panorámica & Solárium**: Ubicada en el último nivel con vistas 360° al Río Paraná y a la ciudad.
2. **SUM Climatizado con Parrilla**: Espacio social totalmente equipado para eventos y reuniones.
3. **Fitness Center / Gimnasio**: Equipamiento de entrenamiento cardiovascular y funcional.
4. **Cocheras y Bauleras**: Niveles de estacionamiento con portones automatizados y control de acceso.
5. **Seguridad y Accesos**: Control biométrico, cámaras de circuito cerrado (CCTV) y doble ascensor inteligente de última generación.
"""

with open(os.path.join(docs_dir, "COMMERCIAL_SPEC.md"), "w", encoding="utf-8") as f:
    f.write(comm_content.strip() + "\n")

# 3. docs/ASSETS_PIPELINE.md
assets_content = """# 🎨 Pipeline de Procesamiento de Activos y Renders

## 📂 Organización de Recursos
Los activos multimedia del proyecto se estructuran en `assets/`:

- `assets/web_optimized/`: Láminas del folleto oficial convertidas a WebP (resolución optimizada para web, compresión con calidad 85%).
- `assets/pure_images/`: Renders aislados de fachada, balcones, dormitorios, cocinas y rooftop.
- `assets/reels/`: Formato vertical 1080x1920 (relación de aspecto 9:16) para campañas en Instagram Reels, TikTok y YouTube Shorts.
- `assets/user_planta_tipo.png`: Plano maestro de distribución y planta tipo.

---

## ⚙️ Scripts de Automatización (Python)

El directorio `scripts/` contiene herramientas automatizadas para la regeneración y optimización de activos:

| Script | Propósito |
| :--- | :--- |
| `prepare_assets.py` | Extrae páginas del PDF maestro y las convierte en WebP de alta fidelidad. |
| `extract_pure_images.py` | Aísla los renders de las láminas para uso en fondos y galerías. |
| `build_asset_catalog.py` | Genera la página interactiva `catalogo_assets.html` para auditar los recursos. |
| `sync_new_masterplan.py` | Sincroniza las referencias de planos en el código HTML. |

---

## 🛠️ Requisitos para Ejecutar el Pipeline
- Python 3.10+
- Bibliotecas: `pip install Pillow PyMuPDF reportlab`
"""

with open(os.path.join(docs_dir, "ASSETS_PIPELINE.md"), "w", encoding="utf-8") as f:
    f.write(assets_content.strip() + "\n")

# 4. docs/DEPLOYMENT_GUIDE.md
deploy_content = """# 🚀 Guía de Despliegue y Publicación en GitHub y Vercel

## 🌐 1. Publicación Automatizada en GitHub Pages

El repositorio cuenta con un flujo de integración continua en `.github/workflows/deploy.yml`.

### Pasos para Activar:
1. Sube el código al repositorio de GitHub:
   ```bash
   git remote add origin https://github.com/<TU_USUARIO>/<TU_REPOSITORIO>.git
   git branch -M main
   git push -u origin main
   ```
2. En GitHub, ve a **Settings** > **Pages**.
3. En el apartado **Build and deployment > Source**, elige **GitHub Actions**.
4. Cada vez que hagas un `git push` a `main`, GitHub Pages desplegará automáticamente la versión más reciente en:
   `https://<TU_USUARIO>.github.io/<TU_REPOSITORIO>/`

---

## ⚡ 2. Despliegue en Vercel (Recomendado para Repositorios Privados)

Si tu repositorio en GitHub es privado y tu cuenta de GitHub es del plan gratuito, **Vercel** permite desplegar repositorios privados de manera 100% gratuita, con CDN global ultrarrápido y certificados SSL automáticos.

### Pasos:
1. Crea una cuenta o inicia sesión en [Vercel](https://vercel.com).
2. Haz clic en **Add New...** > **Project**.
3. Conecta tu cuenta de GitHub y selecciona el repositorio privado de Torre Edmond.
4. En **Framework Preset**, déjalo en **Other** (sitio estático).
5. Haz clic en **Deploy**.
6. En pocos segundos tendrás una URL lista para compartir, por ejemplo:
   `https://torre-edmond.vercel.app`

---

## 💻 3. Ejecución Local

Para probar el sitio localmente en tu computadora:

### Con Python:
```bash
python -m http.server 8000
```
Luego abre tu navegador en `http://localhost:8000`.

### Con Node.js / npx:
```bash
npx serve .
```
"""

with open(os.path.join(docs_dir, "DEPLOYMENT_GUIDE.md"), "w", encoding="utf-8") as f:
    f.write(deploy_content.strip() + "\n")

# 5. .github/workflows/deploy.yml
gh_workflow = """name: Deploy Static Website to GitHub Pages

on:
  push:
    branches:
      - main
      - master

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

with open(os.path.join(workflows_dir, "deploy.yml"), "w", encoding="utf-8") as f:
    f.write(gh_workflow.strip() + "\n")

# 6. vercel.json
vercel_config = """{
  "version": 2,
  "name": "torre-edmond-web",
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
"""

with open(r"D:\Proyecto sitio web edificio\vercel.json", "w", encoding="utf-8") as f:
    f.write(vercel_config.strip() + "\n")

# 7. README.md
readme_content = """# 🏢 Torre Edmond — Sitio Web Oficial e Interactivo

[![Despliegue GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Deploy-success?style=for-the-badge&logo=github)](https://github.com)
[![Three.js](https://img.shields.io/badge/Three.js-WebGL%203D-black?style=for-the-badge&logo=three.js)](https://threejs.org/)
[![Web Audio API](https://img.shields.io/badge/Web%20Audio%20API-Synthesizer-blue?style=for-the-badge)](https://developer.mozilla.org/es/docs/Web/API/Web_Audio_API)
[![WebP Optimized](https://img.shields.io/badge/Images-WebP%20Optimized-orange?style=for-the-badge)](https://developers.google.com/speed/webp)
[![Fideicomiso Costa Posadas](https://img.shields.io/badge/Fideicomiso-Costa%20Posadas-gold?style=for-the-badge)](docs/COMMERCIAL_SPEC.md)

Sitio web interactivo de alta gama para la presentación arquitectónica y comercialización de **Torre Edmond (Edificio Edmond)**, desarrollado bajo el marco legal del **Fideicomiso Inmobiliario Costa Posadas** (Administrado por Don Ruben Mario Carreño) y comercializado de forma exclusiva por **Inmobiliaria Río Paraná** en la ciudad de Posadas, Misiones.

---

## 🌟 Características y Experiencia Digital

- 🏙️ **Experiencia Arquitectónica 3D**: Canvas interactivo con **Three.js** que genera partículas estelares doradas y perspectiva dinámica con seguimiento del cursor.
- 📐 **Selector Interactivo de Plantas y Tipologías**: Visor interactivo para 1 dormitorio, 2 dormitorios, monoambientes y niveles de amenities con planos ampliables.
- 🌓 **Modo Claro / Modo Oscuro (*Eye-Care*)**: Selector estético con persistencia de preferencias y paleta de colores optimizada para reducir el cansancio visual.
- 🔊 **Audio Feedback Sintetizado**: Integración con **Web Audio API** para proveer retroalimentación sonora cálida sin requerir archivos MP3 pesados.
- 📱 **Diseño 100% Responsivo**: Adaptabilidad completa para smartphones, tablets, laptops y pantallas 4K.
- 💬 **Canal Comercial Directo**: Botones de contacto y cotización vinculados directamente al WhatsApp oficial de **Inmobiliaria Río Paraná**.
- 📥 **Descarga de Folleto Oficial**: Acceso instantáneo al folleto comercial de 33 páginas de alta definición.

---

## 📂 Estructura del Repositorio

```
📦 Torre Edmond - Web Project
 ┣ 📄 index.html                # Single Page Application (SPA) principal
 ┣ 📄 catalogo_assets.html      # Visor y curador de activos digitales
 ┣ 📄 vercel.json               # Configuración optimizada de despliegue en Vercel
 ┣ 📂 .github/workflows/
 ┃ ┗ 📄 deploy.yml              # CI/CD automático para GitHub Pages
 ┣ 📂 docs/                     # Documentación técnica completa
 ┃ ┣ 📄 ARCHITECTURE.md         # Arquitectura frontend, tokens y shaders
 ┃ ┣ 📄 COMMERCIAL_SPEC.md      # Marco del Fideicomiso Costa Posadas y tipologías
 ┃ ┣ 📄 ASSETS_PIPELINE.md      # Pipeline de optimización de imágenes con Python
 ┃ ┗ 📄 DEPLOYMENT_GUIDE.md     # Guía paso a paso de publicación y hosting
 ┣ 📂 styles/
 ┃ ┗ 📄 main.css                # Sistema de diseño, Glassmorphism y Dark/Light Mode
 ┣ 📂 js/
 ┃ ┣ 📄 app.js                  # Control del DOM, modales y selector de tipologías
 ┃ ┣ 📄 audio.js                # Sintetizador armónico Web Audio API
 ┃ ┗ 📄 three-scene.js          # Escena 3D WebGL con partículas Three.js
 ┣ 📂 assets/                   # Renders, planos y formatos WebP
 ┗ 📂 scripts/                  # Scripts en Python para curaduría y compilación
```

---

## 🚀 Despliegue y Visualización en Línea

### Opción 1: GitHub Pages (CI/CD Automático)
1. Sube este repositorio a tu cuenta de GitHub.
2. En GitHub, ingresa a **Settings > Pages** y en *Source* selecciona **GitHub Actions**.
3. Tu sitio estará disponible en:
   ```
   https://<TU_USUARIO>.github.io/torre-edmon-web/
   ```

### Opción 2: Vercel (Recomendado para Repositorios Privados)
1. Conecta tu repositorio privado en [Vercel](https://vercel.com).
2. Haz clic en **Deploy**.
3. Obtendrás una URL instantánea con SSL y CDN global:
   ```
   https://torre-edmond.vercel.app
   ```

---

## 💻 Ejecución Local

Para probar el sitio en tu entorno de desarrollo local:

```bash
# Con Python
python -m http.server 8000

# O con Node.js
npx serve .
```
Luego visita en tu navegador: `http://localhost:8000`

---

## 🏛️ Créditos e Institucional

- **Desarrollo Inmobiliario**: Torre Edmond / Edificio Edmond
- **Marco Legal**: [[Fideicomiso Costa Posadas]] — Administrador Fiduciario Don Ruben Mario Carreño
- **Comercialización Exclusiva**: Inmobiliaria Río Paraná (Jujuy 2255 PB, Posadas, Misiones)
"""

with open(r"D:\Proyecto sitio web edificio\README.md", "w", encoding="utf-8") as f:
    f.write(readme_content.strip() + "\n")

print("Todos los archivos de documentacion del repositorio fueron generados con exito.")
