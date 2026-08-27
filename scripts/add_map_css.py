with open("styles/main.css", "r", encoding="utf-8") as f:
    css = f.read()

extra_css = """
/* Masterplan Map Wrap */
.location-map-master-wrap {
  background: var(--bg-surface);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--card-shadow);
  padding: 1.5rem;
  text-align: center;
  cursor: zoom-in;
}

.location-map-master-wrap img {
  width: 100%;
  height: auto;
  max-height: 650px;
  object-fit: contain;
  border-radius: var(--radius-sm);
  display: block;
  margin: 0 auto;
  transition: transform 0.4s ease;
}

.location-map-master-wrap:hover img {
  transform: scale(1.015);
}
"""

if ".location-map-master-wrap" not in css:
    css += extra_css
    with open("styles/main.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Estilos de location-map-master-wrap agregados a main.css!")
