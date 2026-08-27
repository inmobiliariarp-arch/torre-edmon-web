import os

obsidian_dir = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana\Proyecto Web - Torre Edmond"
os.makedirs(obsidian_dir, exist_ok=True)

docs_dir = r"D:\Proyecto sitio web edificio\docs"
os.makedirs(docs_dir, exist_ok=True)

github_workflows = r"D:\Proyecto sitio web edificio\.github\workflows"
os.makedirs(github_workflows, exist_ok=True)

# 1. Dossier Web in Obsidian
doc1 = """---
id: "PROY-WEB-TORRE-EDMOND"
tipo: "Proyecto de Desarrollo Web y Material Digital"
proyecto: "Torre Edmond / Edificio Edmond"
fideicomiso: "[[Dossier Completo - Fideicomiso Costa Posadas]]"
fiduciario: "Don Ruben Mario Carreño"
comercializa: "Inmobiliaria Río Paraná"
ubicacion: "Posadas, Misiones, Argentina"
fecha_creacion: "Agosto 2026"
estado: "Completado / Listo para Produccion y Despliegue"
tags:
  - "#proyecto-web"
  - "#fideicomiso-costa-posadas"
  - "#torre-edmond"
  - "#inmobiliaria-rio-parana"
  - "#marketing-inmobiliario"
  - "#threejs"
---

# 🌐 Proyecto Web — Torre Edmond (Fideicomiso Costa Posadas)

> **Sitio Web Oficial e Interactivo de Comercializacion y Presentacion Arquitectonica**  
> **Emprendimiento**: Torre Edmond (Edificio Edmond)  
> **Marco Fiduciario**: [[Dossier Completo - Fideicomiso Costa Posadas]]  
> **Direccion y Gestion Fiduciaria**: Don Ruben Mario CARREÑO  
> **Comercializacion Exclusiva**: Inmobiliaria Rio Parana (Jujuy 2255 PB, Posadas, Misiones)  
> **Ubicacion del Desarrollo**: Posadas, Misiones

---

## 🎯 1. Objetivos del Proyecto Digital

1. **Posicionamiento Premium**: Transmitir la escala, confort y vanguardia de Torre Edmond a traves de una experiencia web inmersiva de alto impacto visual.
2. **Selector Interactivo de Unidades**: Facilitar a potenciales inversores y compradores la visualizacion clara de plantas arquitectonicas (1 dormitorio, 2 dormitorios, monoambientes y pisos exclusivos).
3. **Conversion y Captacion de Leads**: Integracion fluida y directa via WhatsApp empresarial con el equipo comercial de **Inmobiliaria Rio Parana**.
4. **Respaldo Institucional y Juridico**: Consolidar la confianza de los inversores respaldando el proyecto bajo el marco del **Fideicomiso Inmobiliario Costa Posadas**.

---

## 🏛️ 2. Estructura Institucional y Fiduciaria

```mermaid
graph TD
    A["Fideicomiso Inmobiliario Costa Posadas<br/>(Patrimonio Separado / Ley 24.441 y CCC)"] --> B["Fiduciario y Administrador:<br/>Don Ruben Mario Carreño"]
    B --> C["Desarrollo Edilicio:<br/>Torre Edmond (Posadas)"]
    C --> D["Sitio Web Oficial y Marketing Digital:<br/>Torre Edmond Interactive Web"]
    D --> E["Comercializacion:<br/>Inmobiliaria Rio Parana"]
    E --> F["Inversores y Fideicomisarios Adjudicatarios"]
```

- **Fideicomiso Matriz**: [[Dossier Completo - Fideicomiso Costa Posadas]]
- **Dossier de Inmueble**: [[Dossier Completo - Torre Edmond]]
- **Carpeta del Edificio en Boveda**: [Edificio Edmond](file:///D:/Boveda%20Obsidian%20Inmobiliaria/Inmobiliaria%20Rio%20Parana/Edificio%20Edmond)
- **Folleto Comercial Maestro (33 Paginas)**: [FOLLETO TORRE EDMON-2.pdf](file:///D:/Boveda%20Obsidian%20Inmobiliaria/Inmobiliaria%20Rio%20Parana/Edificio%20Edmond/FOLLETO%20TORRE%20EDMON-2.pdf)

---

## 💻 3. Ficha Tecnica del Desarrollo Web

| Atributo | Detalle Tecnico |
| :--- | :--- |
| **Stack Principal** | HTML5 Semantico, CSS3 Moderno (Custom Properties), JavaScript ES6+ Vanilla |
| **Graficos 3D** | Three.js (Canvas interactivo con particulas doradas y perspectiva arquitectonica) |
| **Audio Feedback** | Web Audio API nativo (sintetizador micro-tonal armonico de frecuencia 520Hz) |
| **Diseño y UX** | Responsive Design (Mobile-First, Tablet, Desktop 4K), Modo Claro / Modo Oscuro (*Eye-Care*) |
| **Optimizacion de Medios** | Imagenes comprimidas en formato Google WebP de alta fidelidad |
| **Infraestructura** | Git + GitHub Actions (CI/CD) + GitHub Pages / Vercel Edge Network |

---

## 📂 4. Modulos de Documentacion en la Boveda

- 🛠️ [[Manual de Arquitectura y Tecnologias Web]]: Detalles tecnicos del frontend, canvas 3D, sintetizador de audio y CSS tokens.
- 🎨 [[Catalogo de Activos y Renders]]: Guia completa de renders de fachada, interiores, amenities, planos de planta y creatividades 9:16.
- 🚀 [[Guia de Despliegue y Mantenimiento]]: Procedimientos para actualizacion de datos, pipeline de imagenes y sincronizacion con GitHub.

---

## 📁 5. Acceso al Codigo Fuente Local

- 💻 **Directorio del Proyecto Web**: `D:\Proyecto sitio web edificio`
- 🌐 **Pagina Principal**: [index.html](file:///D:/Proyecto%20sitio%20web%20edificio/index.html)
- 📊 **Visor de Catalogo de Assets**: [catalogo_assets.html](file:///D:/Proyecto%20sitio%20web%20edificio/catalogo_assets.html)
- 🎨 **Estilos Globales**: [main.css](file:///D:/Proyecto%20sitio%20web%20edificio/styles/main.css)
- ⚡ **Scripts Principales**: [app.js](file:///D:/Proyecto%20sitio%20web%20edificio/js/app.js) | [audio.js](file:///D:/Proyecto%20sitio%20web%20edificio/js/audio.js) | [three-scene.js](file:///D:/Proyecto%20sitio%20web%20edificio/js/three-scene.js)
"""

with open(os.path.join(obsidian_dir, "Dossier Web - Torre Edmond (Fideicomiso Costa Posadas).md"), "w", encoding="utf-8") as f:
    f.write(doc1.strip() + "\n")

# 2. Manual de Arquitectura
doc2 = """---
id: "MAN-ARQ-WEB-TORRE-EDMOND"
tipo: "Manual Tecnico de Arquitectura Web"
proyecto: "[[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]]"
tags:
  - "#arquitectura-web"
  - "#frontend"
  - "#threejs"
  - "#web-audio-api"
  - "#css-moderno"
---

# 🛠️ Manual de Arquitectura y Tecnologías Web — Torre Edmond

> Documentacion tecnica profunda del sitio web interactivo de Torre Edmond para el Fideicomiso Inmobiliario Costa Posadas.

---

## 🏗️ 1. Estructura y Capas de la Aplicacion

El proyecto fue desarrollado bajo una arquitectura **Vanilla Modular de Alto Rendimiento (Zero-Bloat)** sin sobrecargas de frameworks pesados, garantizando tiempos de carga inferiores a 0.5 segundos:

```
📦 Proyecto Web Torre Edmond (D:\Proyecto sitio web edificio)
 ┣ 📄 index.html                # Single Page Application (SPA) comercial principal
 ┣ 📄 catalogo_assets.html      # Galeria y curaduria de imagenes/renders en tiempo real
 ┣ 📂 styles/
 ┃ ┗ 📄 main.css                # Sistema de diseño con Design Tokens y Variables CSS3
 ┣ 📂 js/
 ┃ ┣ 📄 app.js                  # Control de interactividad, DOM, modales y tipologias
 ┃ ┣ 📄 audio.js                # Motor de audio sintetizado con Web Audio API
 ┃ ┗ 📄 three-scene.js          # Escena 3D WebGL con particulas y efecto parallax
 ┣ 📂 assets/
 ┃ ┣ 📂 web_optimized/          # Slides y laminas en formato WebP de alto rendimiento
 ┃ ┣ 📂 pure_images/            # Renders extraidos y aislados en alta definicion
 ┃ ┗ 📂 reels/                  # Formatos verticales 9:16 para redes sociales
 ┣ 📂 scripts/                  # Pipeline en Python para procesamiento de activos y HTML
 ┗ 📂 docs/                     # Documentacion tecnica para Git y GitHub
```

---

## 🎨 2. Sistema de Diseño y Tokens CSS (`styles/main.css`)

El diseño implementa una estética de **Lujo Arquitectónico Moderno** con paleta de tonos oro, arena y grafito con soporte bimodal nativo (Modo Claro / Modo Oscuro):

- **Paleta Primaria**:
  - `Oro Champagne`: `#D4AF37` / `#C5A059`
  - `Negro Grafito Profundo`: `#0d0f12` (Modo Oscuro)
  - `Gris Perla / Hueso`: `#F8F9FA` (Modo Claro)
  - `Acentos de Superficie`: `rgba(255, 255, 255, 0.05)` con efecto *Glassmorphism* (Backdrop Blur).
- **Tipografías**:
  - `Cinzel` / `Playfair Display`: Títulos aristocráticos y jerarquía editorial.
  - `Outfit` / `Inter`: Textos de lectura rápida, especificaciones y métricas.

---

## 🌌 3. Motor 3D Three.js (`js/three-scene.js`)

- **Canvas WebGL Flotante**: Renderiza una nube de partículas estelares doradas que reaccionan sutilmente a la posición del cursor del usuario (*cursor-tracking parallax*).
- **Consumo de Memoria Optimizado**: Utiliza `BufferGeometry` con `PointsMaterial` para mantener 60 FPS estables sin drenar batería ni calentar dispositivos móviles.
- **Detección de Rendimiento**: Si el dispositivo no soporta WebGL o tiene aceleración reducida, se degrada elegantemente a un fondo con gradiente radial CSS.

---

## 🔊 4. Sintetizador Armónico Web Audio API (`js/audio.js`)

- **Sin Archivos MP3 Pesados**: El sonido de interacción se sintetiza en tiempo real mediante el oscilador del navegador.
- **Frecuencia Armónica**: Onda senoidal modulada en 520Hz con envolvente ADSR suave (Attack: 10ms, Decay: 80ms) que produce un sonido cálido y de lujo al cambiar de tipología o accionar botones.

---

## 📱 5. Selector Interactivo de Tipologías (`js/app.js`)

- Conmuta instantáneamente entre las unidades:
  1. **1 Dormitorio**: Para profesionales o inversión de renta temporaria.
  2. **2 Dormitorios**: Confort familiar con balcón y parrilla.
  3. **Monoambientes Premium**: Máxima rentabilidad y diseño compacto.
  4. **Pisos Exclusivos y Amenities**: Terraza panorámica, piscina, SUM y gimnasio.
"""

with open(os.path.join(obsidian_dir, "Manual de Arquitectura y Tecnologias Web.md"), "w", encoding="utf-8") as f:
    f.write(doc2.strip() + "\n")

# 3. Catalogo de Activos
doc3 = """---
id: "CAT-ASSETS-TORRE-EDMOND"
tipo: "Catalogo de Activos Digitales y Renders"
proyecto: "[[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]]"
tags:
  - "#renders"
  - "#material-comercial"
  - "#plantas-arquitectonicas"
  - "#reels"
---

# 🎨 Catálogo de Activos y Renders — Torre Edmond

> Registro inventariado de todas las láminas, planos arquitectónicos, renders 3D y creatividades digitales de Torre Edmond.

---

## 📊 1. Resumen de Materiales en el Proyecto

- **Láminas WebP Optimizadas**: 33 láminas extraídas de la folletería oficial (`assets/web_optimized/`).
- **Renders Puros y Vistas 3D**: Vistas de fachada nocturna/diurna, interiores, cocinas, livings y amenities (`assets/pure_images/`).
- **Creatividades Verticales 9:16**: Formatos adaptados para Instagram Reels, TikTok y Estados de WhatsApp (`assets/reels/`).
- **Documento PDF Maestro**: [FOLLETO TORRE EDMON-2.pdf](file:///D:/Boveda%20Obsidian%20Inmobiliaria/Inmobiliaria%20Rio%20Parana/Edificio%20Edmond/FOLLETO%20TORRE%20EDMON-2.pdf) (13.5 MB).

---

## 🏢 2. Tipologías y Planos Arquitectónicos

| Tipología | Distribución y Características | Ubicación en Assets |
| :--- | :--- | :--- |
| **Planta Tipo General** | Distribución con 2 ascensores de alta velocidad, escaleras de evacuación y núcleo de servicios. | `assets/user_planta_tipo.png` |
| **Departamento 1 Dormitorio** | Estar comedor, cocina integrada con barra, dormitorio con placard y balcón terraza. | `assets/pure_images/depto_1dorm.webp` |
| **Departamento 2 Dormitorios** | Suite principal con vestidor, 2do dormitorio, baño completo, estar amplio, terraza con parrilla. | `assets/pure_images/depto_2dorm.webp` |
| **Monoambientes** | Espacio flexible divisible, baño completo y kitchenette moderna. | `assets/pure_images/monoambiente.webp` |
| **Pisos Superiores y Amenities** | Rooftop con piscina infinita, solárium húmedo/seco, SUM equipado y fitness center. | `assets/pure_images/amenities_rooftop.webp` |

---

## 📸 3. Visor de Curaduría Digital

Para previsualizar y auditar todos los activos disponibles con su resolución y peso, abrir en el navegador:
- 🌐 [catalogo_assets.html](file:///D:/Proyecto%20sitio%20web%20edificio/catalogo_assets.html)
"""

with open(os.path.join(obsidian_dir, "Catalogo de Activos y Renders.md"), "w", encoding="utf-8") as f:
    f.write(doc3.strip() + "\n")

# 4. Guia de Despliegue Obsidian
doc4 = """---
id: "GUIA-DESP-TORRE-EDMOND"
tipo: "Guia de Despliegue y Operaciones"
proyecto: "[[Dossier Web - Torre Edmond (Fideicomiso Costa Posadas)]]"
tags:
  - "#despliegue"
  - "#github-pages"
  - "#vercel"
  - "#ci-cd"
---

# 🚀 Guía de Despliegue y Mantenimiento — Torre Edmond

> Instrucciones de operación, integración continua (CI/CD) y actualización para el sitio web de Torre Edmond.

---

## 🌐 1. Despliegue en GitHub Pages

El proyecto incluye un pipeline automatizado de GitHub Actions configurado en `.github/workflows/deploy.yml`:

1. **Crear Repositorio en GitHub**:
   - Nombre recomendado: `torre-edmon-web` (Privado o Público).
2. **Vincular y Subir Código**:
   ```bash
   git remote add origin https://github.com/<TU_USUARIO>/torre-edmon-web.git
   git branch -M main
   git push -u origin main
   ```
3. **Activar GitHub Pages**:
   - Ir a `Settings` > `Pages`.
   - En *Source*, seleccionar **GitHub Actions**.
   - El sitio se publicará automáticamente en:
     `https://<TU_USUARIO>.github.io/torre-edmon-web/`

---

## ⚡ 2. Despliegue en Vercel (Recomendado para Repositorios Privados)

Vercel permite alojar sitios estáticos desde repositorios privados de GitHub de forma totalmente gratuita y ultrarrápida:

1. Ingresar a [vercel.com](https://vercel.com).
2. Conectar la cuenta de GitHub y hacer clic en **Import Repository**.
3. Seleccionar `torre-edmon-web`.
4. Dejar la configuración por defecto y pulsar **Deploy**.
5. Vercel asignará una URL instantánea tipo `https://torre-edmon-web.vercel.app` y actualizará el sitio con cada `git push`.

---

## 🔄 3. Mantenimiento y Actualización de Contenidos

- **Modificar Textos o Teléfonos**: Editar directamente `index.html` (los botones de WhatsApp apuntan al número comercial configurado).
- **Procesar Nuevas Imágenes**: Colocar imágenes de alta resolución en `assets/` y ejecutar:
  ```bash
  python scripts/prepare_assets.py
  ```
"""

with open(os.path.join(obsidian_dir, "Guia de Despliegue y Mantenimiento.md"), "w", encoding="utf-8") as f:
    f.write(doc4.strip() + "\n")

print("Notas de Obsidian creadas exitosamente.")
