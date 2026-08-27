import os

# 1. Update index.html with advanced SEO, OpenGraph and JSON-LD Schema
with open(r"D:\Proyecto sitio web edificio\index.html", "r", encoding="utf-8") as f:
    html = f.read()

seo_head_target = """  <title>Torre Edmon | Posadas Misiones</title>
  <meta name="description" content="Torre Edmon: Residencias exclusivas en Posadas Misiones. Comercializa Inmobiliaria Río Paraná.">
  
  <link rel="icon" type="image/png" href="assets/branding/logo_inmobiliaria_clean.png">"""

seo_head_replacement = """  <title>Torre Edmon | Departamentos de Lujo en Posadas Misiones | Fideicomiso Costa Posadas</title>
  <meta name="description" content="Torre Edmon: Exclusivos departamentos de 217 m² y 218 m² en pozo frente al Río Paraná, Posadas Misiones. Amenities premium, piscina, SUM, cocheras EV y ascensores directos. Comercializa Inmobiliaria Río Paraná.">
  <meta name="keywords" content="Torre Edmon, Torre Edmond, departamentos en pozo Posadas, departamentos en pozo Posadas Misiones, inversion inmobiliaria Posadas, Fideicomiso Costa Posadas, Inmobiliaria Rio Parana, departamentos costanera Posadas, departamentos con vista al rio Posadas, Ruben Carreño">
  <meta name="author" content="Inmobiliaria Río Paraná">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://edmonposadas.vercel.app/">

  <!-- Open Graph / Facebook / WhatsApp Preview -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://edmonposadas.vercel.app/">
  <meta property="og:title" content="Torre Edmon — Residencias Exclusivas en Posadas Misiones">
  <meta property="og:description" content="Departamentos de alta gama en pozo frente al Río Paraná. 217 m² propios, balcón con parrilla individual, piscina en azotea y cocheras con cargador eléctrico.">
  <meta property="og:image" content="https://edmonposadas.vercel.app/assets/curated/exterior/exterior_02.webp">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="Torre Edmon Posadas">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://edmonposadas.vercel.app/">
  <meta name="twitter:title" content="Torre Edmon | Departamentos de Lujo en Posadas">
  <meta name="twitter:description" content="Emprendimiento residencial de vanguardia frente al Río Paraná en Posadas, Misiones. Comercializa Inmobiliaria Río Paraná.">
  <meta name="twitter:image" content="https://edmonposadas.vercel.app/assets/curated/exterior/exterior_02.webp">

  <!-- Schema.org JSON-LD for Google Rich Snippets & Real Estate SEO -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "ApartmentComplex",
        "@id": "https://edmonposadas.vercel.app/#building",
        "name": "Torre Edmon (Edificio Edmond)",
        "description": "Complejo residencial de alta gama con veintiséis departamentos de 217 m² y 218 m² propios, piscina, SUM, gimnasio, 55 cocheras con infraestructura EV y ascensores directos.",
        "url": "https://edmonposadas.vercel.app/",
        "image": "https://edmonposadas.vercel.app/assets/curated/exterior/exterior_02.webp",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Posadas",
          "addressRegion": "Misiones",
          "addressCountry": "AR"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": -27.3667,
          "longitude": -55.8969
        },
        "amenityFeature": [
          {"@type": "LocationFeatureSpecification", "name": "Piscina en Terraza con Vista al Río", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "SUM Climatizado con Parrilla", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Gimnasio Equipado", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "55 Cocheras con cargador para autos eléctricos (EV Ready)", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Ascensores con Acceso Directo a Departamentos", "value": true},
          {"@type": "LocationFeatureSpecification", "name": "Balcones Aterrazados con Parrilla Individual", "value": true}
        ]
      },
      {
        "@type": "RealEstateAgent",
        "@id": "https://edmonposadas.vercel.app/#agent",
        "name": "Inmobiliaria Río Paraná",
        "url": "https://edmonposadas.vercel.app/",
        "logo": "https://edmonposadas.vercel.app/assets/branding/logo_inmobiliaria_clean.png",
        "telephone": "+54-9-3764-765431",
        "email": "inmobiliariarp@gmail.com",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Jujuy 2255 PB",
          "addressLocality": "Posadas",
          "addressRegion": "Misiones",
          "postalCode": "3300",
          "addressCountry": "AR"
        }
      }
    ]
  }
  </script>

  <link rel="icon" type="image/png" href="assets/branding/logo_inmobiliaria_clean.png">"""

if seo_head_target in html:
    html = html.replace(seo_head_target, seo_head_replacement)
    with open(r"D:\Proyecto sitio web edificio\index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SEO tags y Schema.org JSON-LD insertados en index.html.")
else:
    print("WARNING: seo_head_target no encontrado en index.html.")

# 2. Create sitemap.xml
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://edmonposadas.vercel.app/</loc>
    <lastmod>2026-08-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <image:image>
      <image:loc>https://edmonposadas.vercel.app/assets/curated/exterior/exterior_02.webp</image:loc>
      <image:title>Fachada Principal Torre Edmon Posadas</image:title>
      <image:caption>Residencias de lujo Torre Edmon en Posadas, Misiones frente al Río Paraná</image:caption>
    </image:image>
    <image:image>
      <image:loc>https://edmonposadas.vercel.app/assets/curated/plantas/plantas_34.webp</image:loc>
      <image:title>Planta Tipo Torre Edmon</image:title>
      <image:caption>Plano de arquitectura y distribución de departamentos de 217 m² en Torre Edmon</image:caption>
    </image:image>
  </url>
  <url>
    <loc>https://edmonposadas.vercel.app/catalogo_assets.html</loc>
    <lastmod>2026-08-27</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>
"""

with open(r"D:\Proyecto sitio web edificio\sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content.strip() + "\n")
print("sitemap.xml creado.")

# 3. Create robots.txt
robots_content = """User-agent: *
Allow: /

Sitemap: https://edmonposadas.vercel.app/sitemap.xml
"""

with open(r"D:\Proyecto sitio web edificio\robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content.strip() + "\n")
print("robots.txt creado.")
