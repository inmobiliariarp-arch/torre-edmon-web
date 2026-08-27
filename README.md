# 🏢 Torre Edmond — Sitio Web Oficial e Interactivo

[![Despliegue GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Deploy-success?style=for-the-badge&logo=github)](https://inmobiliariarp-arch.github.io/torre-edmon-web/)
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
   https://inmobiliariarp-arch.github.io/torre-edmon-web/
   ```

### Opción 2: Vercel (Recomendado para Repositorios Privados)
1. Conecta tu repositorio privado en [Vercel](https://vercel.com).
2. Haz clic en **Deploy**.
3. Obtendrás una URL instantánea con SSL y CDN global:
   ```
   https://edmonposadas.vercel.app
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
