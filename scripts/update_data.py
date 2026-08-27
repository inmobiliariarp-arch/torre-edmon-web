import json

data = {
    "project": {
        "name": "Torre Edmon",
        "slogan": "Arquitectura de Vanguardia • Frente al Río Paraná",
        "tagline": "Semipisos residenciales de categoría superior donde todos los balcones miran al majestuoso Río Paraná.",
        "location": {
            "city": "Región Litoral, Argentina",
            "zone": "Ubicación Ribereña Estratégica",
            "highlights": "Frente costero privilegiado, conexión inmediata al centro urbano y polo gastronómico."
        },
        "developer_commercializer": {
            "name": "Inmobiliaria Río Paraná",
            "tagline": "Comercialización Exclusiva y Asesoramiento Integral",
            "phone": "+54 9 379 400-0000",
            "whatsapp": "5493794000000",
            "email": "contacto@inmobiliariarioparana.com",
            "address": "Av. Costanera y Centro, Región Litoral, Argentina"
        },
        "characteristics": [
            {
                "icon": "water",
                "title": "Todos los Balcones al Río Paraná",
                "desc": "Orientación frontal exclusiva: el 100% de las unidades cuenta con balcón terraza y parrilla con vista abierta al río."
            },
            {
                "icon": "charging-station",
                "title": "Cocheras con Cargadores Eléctricos",
                "desc": "Estacionamiento cubierto con portón automático e infraestructura prevista para la instalación de cargadores para vehículos eléctricos (EV Ready)."
            },
            {
                "icon": "building",
                "title": "Tipología Residencial Homogénea",
                "desc": "Planta tipo uniforme y equilibrada: semipisos diseñados con la misma jerarquía espacial, ventilación cruzada y terminaciones de lujo."
            },
            {
                "icon": "shield-alt",
                "title": "Seguridad & Acceso Inteligente",
                "desc": "Ingreso controlado las 24hs, cámaras de alta resolución y portería en el imponente hall de acceso en doble altura."
            }
        ],
        "amenities": [
            {
                "id": "piscina",
                "name": "Piscina Infinity & Solárium",
                "desc": "Piscina en la azotea con solárium atérmico y visuales panorámicas ininterrumpidas al Río Paraná.",
                "image": "assets/web_optimized/slide_07.webp"
            },
            {
                "id": "deck-relax",
                "name": "Deck Solárium & Azotea de Relax",
                "desc": "Áreas exteriores de descanso con decks de madera y reposeras para contemplar el atardecer sobre el río.",
                "image": "assets/web_optimized/slide_08.webp"
            },
            {
                "id": "sum-quincho",
                "name": "SUM & Quincho Climatizado",
                "desc": "Salón de usos múltiples totalmente equipado con gran parrilla, cocina completa, vajilla y área gourmet para eventos sociales.",
                "image": "assets/web_optimized/slide_09.webp"
            },
            {
                "id": "gourmet-living",
                "name": "Espacio Gourmet & Living de Azotea",
                "desc": "Amoblamiento de diseño contemporáneo integrado a la terraza para compartir momentos inolvidables.",
                "image": "assets/web_optimized/slide_10.webp"
            },
            {
                "id": "hall-acceso",
                "name": "Hall de Acceso en Doble Altura",
                "desc": "Ingreso jerarquizado con revestimientos en mármol, porcelanato, iluminación escenográfica y recepción.",
                "image": "assets/web_optimized/slide_05.webp"
            },
            {
                "id": "recepcion",
                "name": "Recepción & Sala de Estar",
                "desc": "Salón de bienvenida distinguido para recibir visitas con total confort y seguridad.",
                "image": "assets/web_optimized/slide_06.webp"
            }
        ],
        "unit_details": {
            "title": "Departamento Semipiso Tipo - Torre Edmon",
            "slogan": "Distribución interna completa optimizada con vistas frontales al Río Paraná",
            "features": [
                "Balcón terraza de gran dimensión con parrilla individual integrada y vista directa al Río Paraná.",
                "Living comedor apaisado con ventanales de piso a techo y Doble Vidriado Hermético (DVH).",
                "Dormitorio principal en suite con vestidor y antebaño.",
                "Dormitorios secundarios luminosos con placares empotrados completos.",
                "Cocina de concepto moderno con muebles bajo mesada, alacenas y barra desayunadora.",
                "Lavadero independiente y doble circulación de aire.",
                "Pisos de porcelanato rectificado de alta resistencia y terminaciones en yeso."
            ],
            "full_plan_image": "assets/web_optimized/slide_24.webp",
            "general_plan_image": "assets/web_optimized/slide_23.webp",
            "roof_plan_image": "assets/web_optimized/slide_28.webp",
            "parking_plan_image": "assets/web_optimized/slide_22.webp"
        },
        "specifications": [
            {
                "category": "Terminaciones & Estructura",
                "items": [
                    "Pisos de porcelanato rectificado de primera calidad en estar, cocina y dormitorios.",
                    "Aberturas de aluminio anodizado línea pesada con Doble Vidriado Hermético (DVH) de máxima aislación termoacústica.",
                    "Zócalos laqueados y enlucido de yeso en muros interiores.",
                    "Puertas de madera de diseño contemporáneo con herrajes de acero inoxidable."
                ]
            },
            {
                "category": "Cocina, Baños & Equipamiento",
                "items": [
                    "Mobiliario de cocina a medida con bajo mesada y alacenas en melamina texturada con cantos ABS.",
                    "Mesadas de granito / cuarzo con bacha doble de acero inoxidable y grifería monocomando de primera línea.",
                    "Artefactos sanitarios Ferrum / Roca de diseño minimalista con válvulas ecológicas de doble descarga.",
                    "Revestimientos cerámicos y porcelánicos de piso a techo en zonas húmedas."
                ]
            },
            {
                "category": "Instalaciones, Cocheras & Sustentabilidad",
                "items": [
                    "Infraestructura prevista en cocheras para la instalación de cargadores para vehículos eléctricos (EV Ready).",
                    "Parrilla individual con tiraje independiente en el balcón de cada departamento.",
                    "Preinstalación integral embutida para equipos de aire acondicionado split frío/calor.",
                    "Ascensores inteligentes de alta velocidad con cabinas de acero inoxidable y puertas automáticas."
                ]
            }
        ]
    }
}

with open("assets/data/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("assets/data/data.json actualizado con fidelidad 100%!")
