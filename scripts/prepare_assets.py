import os
import sys
import json
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
os.chdir(BASE_DIR)

DIRS = [
    'assets/branding',
    'assets/renders/exterior',
    'assets/renders/hall_acceso',
    'assets/renders/interiores',
    'assets/renders/amenities',
    'assets/plantas',
    'assets/web_optimized',
    'assets/data',
    'assets/reels_instagram',
]

for d in DIRS:
    os.makedirs(d, exist_ok=True)

print("Directorios creados exitosamente.")

inmo_raw = 'assets/Logo inmobiliaria Rio Parana.png'
if os.path.exists(inmo_raw):
    print("Procesando logo de Inmobiliaria Rio Parana...")
    img = Image.open(inmo_raw).convert('RGBA')
    arr = np.array(img)
    
    r = arr[:, :, 0].astype(float)
    g = arr[:, :, 1].astype(float)
    b = arr[:, :, 2].astype(float)
    
    is_blue_ish = (b > r + 10) | (b > g + 5)
    is_dark = (r < 75) & (g < 95) & (b < 130)
    is_logo = is_blue_ish | is_dark
    
    alpha = np.zeros((arr.shape[0], arr.shape[1]), dtype=np.uint8)
    alpha[is_logo] = 255
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0)
    
    arr[:, :, 3] = alpha
    clean_inmo = Image.fromarray(arr)
    bbox = clean_inmo.getbbox()
    if bbox:
        clean_inmo = clean_inmo.crop(bbox)
        
    clean_inmo.save('assets/branding/logo_inmobiliaria_clean.png', 'PNG')
    clean_inmo.save('assets/branding/logo_inmobiliaria_clean.webp', 'WEBP', quality=95)
    print("Logo Inmobiliaria Rio Parana limpio guardado.")
    
    arr_white = np.array(clean_inmo)
    mask = arr_white[:, :, 3] > 30
    arr_white[mask, 0] = 255
    arr_white[mask, 1] = 255
    arr_white[mask, 2] = 255
    Image.fromarray(arr_white).save('assets/branding/logo_inmobiliaria_white.png', 'PNG')
    
    arr_gold = np.array(clean_inmo)
    gray = cv2.cvtColor(arr_gold[:, :, :3], cv2.COLOR_RGB2GRAY)
    gold_rgb = np.zeros_like(arr_gold[:, :, :3])
    gold_rgb[:, :, 0] = np.clip(gray * 0.90 + 50, 0, 240).astype(np.uint8)
    gold_rgb[:, :, 1] = np.clip(gray * 0.78 + 35, 0, 210).astype(np.uint8)
    gold_rgb[:, :, 2] = np.clip(gray * 0.40 + 10, 0, 130).astype(np.uint8)
    arr_gold[:, :, :3] = gold_rgb
    Image.fromarray(arr_gold).save('assets/branding/logo_inmobiliaria_gold.png', 'PNG')
    print("Versiones White y Gold de Inmobiliaria Rio Parana generadas.")

slide_01_path = 'assets/slides_hires/slide_01.png'
if os.path.exists(slide_01_path):
    print("Extrayendo logo Torre Edmon...")
    s1 = Image.open(slide_01_path).convert('RGBA')
    w, h = s1.size
    crop_logo = s1.crop((int(w * 0.25), int(h * 0.35), int(w * 0.75), int(h * 0.65)))
    crop_arr = np.array(crop_logo)
    gray_crop = cv2.cvtColor(crop_arr[:, :, :3], cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray_crop, 160, 255, cv2.THRESH_BINARY)
    crop_arr[:, :, 3] = thresh
    clean_edmon = Image.fromarray(crop_arr)
    bbox_edmon = clean_edmon.getbbox()
    if bbox_edmon:
        clean_edmon = clean_edmon.crop(bbox_edmon)
    clean_edmon.save('assets/branding/logo_torre_edmon_white.png', 'PNG')
    clean_edmon.save('assets/branding/logo_torre_edmon_white.webp', 'WEBP', quality=95)
    print("Logo Torre Edmon extraido y guardado.")

SLIDE_MAP = {
    "slide_01": {"type": "hero_cover", "category": "exterior", "name": "Portada Torre Edmon - Fachada Principal", "title": "Torre Edmon", "desc": "Imponente arquitectura contemporánea de vanguardia."},
    "slide_02": {"type": "render", "category": "exterior", "name": "Fachada Diurna y Entorno", "title": "Diseño y Vanguardia", "desc": "Líneas puras, grandes ventanales y terrazas con vistas privilegiadas."},
    "slide_03": {"type": "concept", "category": "exterior", "name": "Concepto Arquitectónico", "title": "Concepto Exclusivo", "desc": "Espacios diseñados para una experiencia de vida superior."},
    "slide_04": {"type": "render", "category": "exterior", "name": "Acceso Principal y PB", "title": "Acceso Distinguido", "desc": "Jerarquía y elegancia desde el primer instante."},
    "slide_05": {"type": "render", "category": "hall_acceso", "name": "Lobby y Hall de Acceso", "title": "Hall de Acceso en Doble Altura", "desc": "Revestimientos nobles, iluminación escenográfica y control de acceso."},
    "slide_06": {"type": "render", "category": "hall_acceso", "name": "Recepción y Sala de Espera", "title": "Recepción y Salón de Entrada", "desc": "Confort y distinción para residentes y visitas."},
    "slide_07": {"type": "render", "category": "amenities", "name": "Piscina Panorámica y Solárium", "title": "Piscina Infinity & Solárium", "desc": "Piscina con vistas abiertas al río y la ciudad."},
    "slide_08": {"type": "render", "category": "amenities", "name": "Deck Solárium y Relax", "title": "Área de Relax y Solárium", "desc": "Deck de madera, reposeras y áreas de descanso al aire libre."},
    "slide_09": {"type": "render", "category": "amenities", "name": "Quincho y SUM Social", "title": "Quincho & SUM Equipado", "desc": "Parrilla completa, cocina equipada y capacidad para eventos sociales."},
    "slide_10": {"type": "render", "category": "amenities", "name": "SUM - Área Gourmet y Living", "title": "Espacio Gourmet Integrado", "desc": "Amoblamiento de diseño para compartir momentos inolvidables."},
    "slide_11": {"type": "render", "category": "interiores", "name": "Living Comedor Principal", "title": "Living Comedor con Vistas Panorámicas", "desc": "Amplitud espacial, iluminación natural y terminaciones de primera línea."},
    "slide_12": {"type": "render", "category": "interiores", "name": "Cocina Integrada con Barra", "title": "Cocina de Concepto Abierto", "desc": "Mobiliario a medida, mesadas de granito y grifería de alta gama."},
    "slide_13": {"type": "render", "category": "interiores", "name": "Dormitorio Principal en Suite", "title": "Master Suite de Lujo", "desc": "Ambiente sereno y sofisticado con vestidor y amplios ventanales."},
    "slide_14": {"type": "render", "category": "interiores", "name": "Baño Principal en Suite", "title": "Baño de Vanguardia", "desc": "Revestimientos porcelánicos, artefactos de primera calidad y diseño minimalista."},
    "slide_15": {"type": "render", "category": "interiores", "name": "Balcón Terraza con Parrilla", "title": "Balcón Terraza Exclusivo", "desc": "Espacio semicubierto privado con parrilla para disfrutar el exterior."},
    "slide_16": {"type": "render", "category": "interiores", "name": "Dormitorio Secundario / Escritorio", "title": "Dormitorio Secundario / Home Office", "desc": "Flexibilidad funcional adaptada al estilo de vida moderno."},
    "slide_17": {"type": "render", "category": "interiores", "name": "Cocina y Comedor Diario", "title": "Detalles y Equipamiento", "desc": "Diseño ergonómico con artefactos de última generación."},
    "slide_18": {"type": "render", "category": "exterior", "name": "Vista Nocturna Iluminada", "title": "Iluminación Arquitectónica Nocturna", "desc": "La presencia de Torre Edmon en el horizonte urbano."},
    "slide_19": {"type": "render", "category": "amenities", "name": "Gimnasio y Área Fitness", "title": "Gimnasio Equipado", "desc": "Máquinas de última tecnología y vistas panorámicas."},
    "slide_20": {"type": "render", "category": "exterior", "name": "Terrazas y Entorno", "title": "Integración con el Entorno", "desc": "Vistas al río y máxima privacidad."},
    "slide_21": {"type": "planta", "category": "plantas", "name": "Planta Baja y Accesos", "title": "Planta Baja: Hall, Cocheras y Servicios", "desc": "Distribución funcional de acceso peatonal, vehicular y portería."},
    "slide_22": {"type": "planta", "category": "plantas", "name": "Planta Nivel Cocheras", "title": "Planta de Estacionamiento Cubierto", "desc": "Cocheras amplias con portón automático y bauleras."},
    "slide_23": {"type": "planta", "category": "plantas", "name": "Planta Tipo Pisos 1 al 8", "title": "Planta Tipo - Niveles Residenciales", "desc": "Distribución eficiente de semipisos y departamentos con doble ventilación."},
    "slide_24": {"type": "planta", "category": "plantas", "name": "Tipología A - Semipiso 2 Dormitorios", "title": "Tipología A: 2 Dormitorios en Suite", "desc": "Living comedor apaisado, balcón con parrilla y suite principal."},
    "slide_25": {"type": "planta", "category": "plantas", "name": "Tipología B - Departamento 1 Dormitorio", "title": "Tipología B: 1 Dormitorio Premium", "desc": "Distribución óptima, cocina integrada y gran balcón terraza."},
    "slide_26": {"type": "planta", "category": "plantas", "name": "Tipología C - Monoambiente Divisible", "title": "Tipología C: Monoambiente de Gran Dimensión", "desc": "Versatilidad espacial para vivienda o renta profesional."},
    "slide_27": {"type": "planta", "category": "plantas", "name": "Planta Piso 9 - Pisos Exclusivos", "title": "Piso Exclusivo - Nivel Superior", "desc": "Máximo metraje y vistas en 360 grados."},
    "slide_28": {"type": "planta", "category": "plantas", "name": "Planta Amenities y Terraza", "title": "Planta Azotea: Piscina, SUM y Solárium", "desc": "Piso social con los mejores servicios y visuales al río."},
    "slide_29": {"type": "render", "category": "exterior", "name": "Balcones y Detalles Constructivos", "title": "Terminaciones Exteriores", "desc": "Materiales nobles, hormigón visto y carpinterías de alta prestación."},
    "slide_30": {"type": "render", "category": "exterior", "name": "Vista Aérea del Emprendimiento", "title": "Ubicación y Visuales", "desc": "Estratégicamente emplazado cerca de todo y frente al horizonte."},
    "slide_31": {"type": "render", "category": "interiores", "name": "Ambiente Integrado Luminoso", "title": "Luminosidad y Amplitud", "desc": "Orientación pensada para maximizar la luz solar."},
    "slide_32": {"type": "render", "category": "exterior", "name": "Perspectiva Urbana", "title": "Torre Edmon en la Ciudad", "desc": "Un nuevo hito urbano en la región."},
    "slide_33": {"type": "contraportada", "category": "branding", "name": "Comercialización Inmobiliaria Río Paraná", "title": "Comercializa Inmobiliaria Río Paraná", "desc": "Asesoramiento profesional y financiación a medida."}
}

print(f"Catalogando {len(SLIDE_MAP)} diapositivas y convirtiendo a WebP...")

processed_data = []

for slide_key, meta in SLIDE_MAP.items():
    in_file = f"assets/slides_hires/{slide_key}.png"
    if not os.path.exists(in_file):
        continue
    
    img = Image.open(in_file)
    w, h = img.size
    
    cat_dir = f"assets/{'plantas' if meta['category'] == 'plantas' else ('branding' if meta['category'] == 'branding' else 'renders/' + meta['category'])}"
    out_cat_webp = os.path.join(cat_dir, f"{slide_key}.webp")
    img.save(out_cat_webp, 'WEBP', quality=88, method=6)
    
    web_webp = f"assets/web_optimized/{slide_key}.webp"
    if w > 1920:
        new_h = int(h * (1920 / w))
        web_img = img.resize((1920, new_h), Image.Resampling.LANCZOS)
    else:
        web_img = img
        
    web_img.save(web_webp, 'WEBP', quality=84, method=6)
    file_size_kb = os.path.getsize(web_webp) / 1024
    
    item_info = {
        "id": slide_key,
        "category": meta["category"],
        "type": meta["type"],
        "title": meta["title"],
        "name": meta["name"],
        "desc": meta["desc"],
        "src": f"assets/web_optimized/{slide_key}.webp",
        "hires": f"{cat_dir}/{slide_key}.webp",
        "width": w,
        "height": h,
        "size_kb": round(file_size_kb, 1)
    }
    processed_data.append(item_info)
    print(f"-> {slide_key} ({meta['category']}): {round(file_size_kb, 1)} KB")

building_data = {
    "project": {
        "name": "Torre Edmon",
        "slogan": "Arquitectura de Vanguardia y Confort Exclusivo",
        "tagline": "Un nuevo estándar de vida urbana en una ubicación de privilegio",
        "location": {
            "city": "Resistencia / Corrientes (Región Litoral)",
            "zone": "Ubicación Estratégica",
            "nearby": ["Costanera y Río Paraná", "Centro Comercial y Financiero", "Polo Gastronómico", "Colegios y Universidades"]
        },
        "developer_commercializer": {
            "name": "Inmobiliaria Río Paraná",
            "tagline": "Líderes en Emprendimientos Inmobiliarios de Vanguardia",
            "phone": "+54 9 379 400-0000",
            "whatsapp": "5493794000000",
            "email": "contacto@inmobiliariarioparana.com",
            "address": "Av. Costanera y Centro, Región Litoral, Argentina",
            "website": "https://inmobiliariarioparana.com"
        },
        "characteristics": [
            {"icon": "building", "title": "Semipisos & Pisos Exclusivos", "desc": "Unidades de 1, 2 dormitorios y semipisos de máxima categoría."},
            {"icon": "shield-check", "title": "Seguridad Integral 24hs", "desc": "Control de acceso inteligente y circuito cerrado de cámaras."},
            {"icon": "car", "title": "Cocheras Cubiertas", "desc": "Estacionamiento privado con portón automatizado y bauleras individuales."},
            {"icon": "sun", "title": "Orientación Óptima", "desc": "Ventilación cruzada, balcones con parrilla y vistas abiertas al horizonte."}
        ],
        "amenities": [
            {"id": "piscina", "name": "Piscina Infinity & Solárium", "desc": "Piscina en azotea con solárium atérmico y vistas panorámicas.", "image": "assets/web_optimized/slide_07.webp"},
            {"id": "sum", "name": "SUM & Quincho Climatizado", "desc": "Salón de usos múltiples totalmente equipado con gran parrilla y área gourmet.", "image": "assets/web_optimized/slide_09.webp"},
            {"id": "gym", "name": "Gimnasio Fitness Panorámico", "desc": "Área de entrenamiento cardiovascular y de fuerza con equipamiento de vanguardia.", "image": "assets/web_optimized/slide_19.webp"},
            {"id": "lobby", "name": "Hall de Acceso en Doble Altura", "desc": "Ingreso jerarquizado con revestimientos en mármol, porcelanato y seguridad.", "image": "assets/web_optimized/slide_05.webp"},
            {"id": "deck", "name": "Deck & Terrazas de Relax", "desc": "Espacios al aire libre pensados para desconectar y disfrutar el atardecer.", "image": "assets/web_optimized/slide_08.webp"}
        ],
        "specifications": [
            {"category": "Terminaciones", "items": ["Pisos de porcelanato de primera calidad en estar, cocina y dormitorios.", "Zócalos de madera laqueada y terminaciones en yeso aplicado.", "Carpinterías de aluminio anodizado línea pesada con doble vidriado hermético (DVH)."]},
            {"category": "Cocina y Baños", "items": ["Muebles de cocina bajo mesada y alacenas completas en melamina texturada.", "Mesadas de granito / cuarzo con bacha doble de acero inoxidable.", "Griferías monocomando de alta prestación y artefactos sanitarios Ferrum/Roca."]},
            {"category": "Confort y Climatización", "items": ["Preinstalación completa para equipos de aire acondicionado split frío/calor.", "Balcones con parrilla individual integrada en cada unidad.", "Instalación para agua caliente centralizada y calefacción eficiente."]}
        ],
        "units": [
            {
                "id": "tipo-a",
                "name": "Tipología A - 2 Dormitorios en Suite",
                "area": "88 m²",
                "rooms": "3 Ambientes (2 Dormitorios + 2 Baños)",
                "features": ["Estar comedor apaisado con salida a balcón terraza.", "Dormitorio principal con vestidor y baño en suite.", "Cocina independiente con lavadero integrado.", "Balcón privado con parrilla."],
                "plan_image": "assets/web_optimized/slide_24.webp",
                "render_image": "assets/web_optimized/slide_11.webp"
            },
            {
                "id": "tipo-b",
                "name": "Tipología B - 1 Dormitorio Premium",
                "area": "54 m²",
                "rooms": "2 Ambientes (1 Dormitorio + 1 Baño)",
                "features": ["Living comedor con cocina integrada tipo americana.", "Dormitorio con amplio placard empotrado.", "Balcón terraza con parrilla propia.", "Baño completo con antebaño."],
                "plan_image": "assets/web_optimized/slide_25.webp",
                "render_image": "assets/web_optimized/slide_12.webp"
            },
            {
                "id": "tipo-c",
                "name": "Tipología C - Monoambiente Divisible",
                "area": "42 m²",
                "rooms": "Ambiente Único Divisible",
                "features": ["Espacio versátil con excelente iluminación natural.", "Cocina lineal equipada.", "Balcón al frente.", "Ideal para primera vivienda o inversión con alta rentabilidad."],
                "plan_image": "assets/web_optimized/slide_26.webp",
                "render_image": "assets/web_optimized/slide_16.webp"
            },
            {
                "id": "piso-exclusivo",
                "name": "Pisos Exclusivos - Planta Completa / Penthouse",
                "area": "140 m²",
                "rooms": "4 Ambientes (3 Dormitorios + 3 Baños + Dependencia)",
                "features": ["Palier privado con acceso por ascensor codificado.", "Máxima privacidad y vistas 360° a la ciudad y el río.", "Master suite con hidromasaje y terraza privada.", "Parrilla gourmet de gran tamaño."],
                "plan_image": "assets/web_optimized/slide_27.webp",
                "render_image": "assets/web_optimized/slide_15.webp"
            }
        ]
    },
    "slides": processed_data
}

with open('assets/data/data.json', 'w', encoding='utf-8') as f:
    json.dump(building_data, f, ensure_ascii=False, indent=2)

print("assets/data/data.json generado correctamente.")

print("Generando material vertical 9:16 para Instagram Reels...")

REEL_SLIDES = [
    {"slide": "slide_01", "badge": "NUEVO LANZAMIENTO", "title": "TORRE EDMON", "sub": "Arquitectura de Vanguardia en una Ubicación Única"},
    {"slide": "slide_05", "badge": "ACCESO DE CATEGORÍA", "title": "HALL DOBLE ALTURA", "sub": "Diseño, distinción y control de acceso 24hs"},
    {"slide": "slide_07", "badge": "AMENITIES EXCLUSIVOS", "title": "PISCINA & SOLÁRIUM", "sub": "Vistas panorámicas y relax en la azotea"},
    {"slide": "slide_09", "badge": "ESPACIO GOURMET", "title": "QUINCHO & SUM", "sub": "Totalmente equipado para tus mejores momentos"},
    {"slide": "slide_11", "badge": "DISEÑO INTERIOR", "title": "LIVING CON VISTAS", "sub": "Amplitud espacial, iluminación y calidez"},
    {"slide": "slide_15", "badge": "DETALLES ÚNICOS", "title": "BALCÓN CON PARRILLA", "sub": "Tu propio espacio gourmet en cada unidad"},
    {"slide": "slide_33", "badge": "COMERCIALIZACIÓN", "title": "INMOBILIARIA RÍO PARANÁ", "sub": "Consultá por planes de financiación a medida"}
]

reel_w, reel_h = 1080, 1920

inmo_logo_path = 'assets/branding/logo_inmobiliaria_white.png'
inmo_logo_img = Image.open(inmo_logo_path).convert('RGBA') if os.path.exists(inmo_logo_path) else None

for idx, reel_item in enumerate(REEL_SLIDES, 1):
    src_slide = f"assets/slides_hires/{reel_item['slide']}.png"
    if not os.path.exists(src_slide):
        continue
        
    base_render = Image.open(src_slide).convert('RGB')
    rw, rh = base_render.size
    
    reel_canvas = Image.new('RGB', (reel_w, reel_h), (18, 20, 26))
    bg_blurred = base_render.resize((reel_w, reel_h), Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(radius=35))
    
    render_scaled_h = int(rh * (reel_w / rw))
    render_sharp = base_render.resize((reel_w, render_scaled_h), Image.Resampling.LANCZOS)
    
    reel_canvas.paste(bg_blurred, (0, 0))
    y_offset = (reel_h - render_scaled_h) // 2
    reel_canvas.paste(render_sharp, (0, y_offset))
    
    overlay = Image.new('RGBA', (reel_w, reel_h), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    for y in range(350):
        alpha = int(220 * (1.0 - y / 350))
        draw_overlay.line([(0, y), (reel_w, y)], fill=(12, 14, 18, alpha))
        
    for y in range(reel_h - 450, reel_h):
        alpha = int(240 * ((y - (reel_h - 450)) / 450))
        draw_overlay.line([(0, y), (reel_w, y)], fill=(12, 14, 18, alpha))
        
    draw_overlay.rectangle([(0, y_offset), (reel_w - 1, y_offset + render_scaled_h)], outline=(212, 175, 55, 180), width=3)
    draw_overlay.rounded_rectangle([(reel_w // 2 - 190, 110), (reel_w // 2 + 190, 160)], radius=25, fill=(212, 175, 55, 230))
    
    reel_final = Image.alpha_composite(reel_canvas.convert('RGBA'), overlay)
    draw_final = ImageDraw.Draw(reel_final)
    
    try:
        font_badge = ImageFont.truetype("arialbd.ttf", 22)
        font_title = ImageFont.truetype("arialbd.ttf", 52)
        font_sub = ImageFont.truetype("arial.ttf", 30)
        font_footer = ImageFont.truetype("arialbd.ttf", 24)
    except:
        font_badge = font_title = font_sub = font_footer = ImageFont.load_default()
        
    draw_final.text((reel_w // 2, 135), reel_item["badge"], fill=(15, 18, 24), font=font_badge, anchor="mm")
    draw_final.text((reel_w // 2, reel_h - 280), reel_item["title"], fill=(255, 255, 255), font=font_title, anchor="mm")
    draw_final.text((reel_w // 2, reel_h - 210), reel_item["sub"], fill=(215, 220, 230), font=font_sub, anchor="mm")
    draw_final.text((reel_w // 2, reel_h - 90), "INMOBILIARIA RIO PARANA - VIVI TORRE EDMON", fill=(212, 175, 55), font=font_footer, anchor="mm")
    
    if inmo_logo_img:
        logo_w, logo_h = inmo_logo_img.size
        target_lw = 180
        target_lh = int(logo_h * (target_lw / logo_w))
        logo_resized = inmo_logo_img.resize((target_lw, target_lh), Image.Resampling.LANCZOS)
        reel_final.paste(logo_resized, (50, 70), logo_resized)
        
    reel_out_path = f"assets/reels_instagram/reel_{idx:02d}_{reel_item['slide']}.jpg"
    reel_final.convert('RGB').save(reel_out_path, 'JPEG', quality=92)
    print(f"Reel 9:16 generado: {reel_out_path}")

print("\nProcesamiento de assets completado con exito!")
