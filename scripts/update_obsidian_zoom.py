import os

obsidian_file = r"D:\Boveda Obsidian Inmobiliaria\Inmobiliaria Rio Parana\Proyecto Web - Torre Edmond\Manual de Arquitectura y Tecnologias Web.md"
if os.path.exists(obsidian_file):
    with open(obsidian_file, "r", encoding="utf-8") as f:
        content = f.read()
    if "Architectural Panzoom Studio" not in content:
        extra = """

---

## 📐 6. Visor Arquitectónico Panzoom Studio con Delimitación Estricta
- **Control de Bordes (Boundary Clamping)**: El plano nunca puede salirse del marco ni mostrar franjas negras.
- **Focal-Point Zooming**: El zoom con rueda o táctil amplía hacia el punto exacto donde apunta el cursor.
- **Botonera Flotante Glassmorphism**: `[+]`, `[-]`, `[Restablecer]` y `[Pantalla Completa]` con indicador de porcentaje de zoom en tiempo real.
- **Mesa de Trabajo Blueprint**: Fondo técnico con retícula milimétrica dorada de alta gama.
- **Configuración Vercel**: Proyecto configurado con el alias `edmondposadas`.
"""
        content = content.strip() + "\n" + extra.strip() + "\n"
        with open(obsidian_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Manual de Arquitectura en Obsidian actualizado.")
