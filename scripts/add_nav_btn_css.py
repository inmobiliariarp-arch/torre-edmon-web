with open("styles/main.css", "r", encoding="utf-8") as f:
    css = f.read()

nav_btn_css = """
/* Brochure Secondary Nav Button */
.btn-secondary-nav {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.25rem;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-gold);
  color: var(--gold-primary);
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-decoration: none;
  border-radius: var(--radius-full);
  transition: var(--transition-smooth);
}

.btn-secondary-nav:hover {
  background: var(--gold-primary);
  color: #000;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px var(--gold-glow);
}
"""

if ".btn-secondary-nav" not in css:
    css += nav_btn_css
    with open("styles/main.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Estilos de .btn-secondary-nav agregados a main.css!")
