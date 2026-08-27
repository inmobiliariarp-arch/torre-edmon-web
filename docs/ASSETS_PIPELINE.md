# 🎨 Pipeline de Procesamiento de Activos y Renders

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
