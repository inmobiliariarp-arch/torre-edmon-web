with open("styles/main.css", "r", encoding="utf-8") as f:
    css = f.read()

footer_luxury_css = """
/* ==========================================================================
   QUIET LUXURY FOOTER & CONTACT MONOGRAPH
   ========================================================================== */
.luxury-footer {
  background: var(--bg-surface);
  border-top: 1px solid var(--border-glass);
  padding: 6rem 0 3.5rem;
  position: relative;
  z-index: 1;
}

.footer-monograph {
  max-width: 820px;
  margin: 0 auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.75rem;
}

.footer-brand-logo {
  height: 48px;
  width: auto;
  object-fit: contain;
  margin-bottom: 0.5rem;
}

.footer-tag {
  display: inline-block;
  font-size: 0.76rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--gold-primary);
  font-weight: 700;
  margin-bottom: 0.4rem;
}

.footer-brand-name {
  font-size: 2rem;
  color: var(--text-main);
  font-family: var(--font-serif);
  letter-spacing: 0.04em;
}

.footer-subtitle {
  font-size: 0.95rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}

.footer-contact-pills {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin: 1.5rem 0 2rem;
}

.contact-pill-link, .contact-pill-text {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.75rem 1.4rem;
  border-radius: var(--radius-full);
  font-size: 0.9rem;
  text-decoration: none;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-glass);
  color: var(--text-main);
  font-weight: 500;
  transition: var(--transition-smooth);
}

.contact-pill-link:hover {
  border-color: var(--gold-primary);
  color: var(--gold-primary);
  transform: translateY(-2px);
}

.contact-pill-link.highlight {
  background: var(--gold-gradient);
  color: #080a0d;
  font-weight: 700;
  border-color: transparent;
  box-shadow: 0 4px 15px var(--gold-glow);
}

.contact-pill-link.highlight:hover {
  box-shadow: 0 8px 25px rgba(197, 160, 89, 0.45);
  transform: translateY(-2px);
  color: #000;
}

.contact-pill-text {
  color: var(--text-muted);
}

.footer-legal {
  border-top: 1px solid var(--border-glass);
  width: 100%;
  padding-top: 2rem;
  margin-top: 1rem;
  font-size: 0.82rem;
  color: var(--text-muted);
}
"""

# Replace old footer styles or append
css += footer_luxury_css

with open("styles/main.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles/main.css actualizado con estilos de quiet luxury footer!")
