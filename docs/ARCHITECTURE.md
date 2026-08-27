# 🏛️ Arquitectura Técnica y Especificación del Sistema Frontend

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
