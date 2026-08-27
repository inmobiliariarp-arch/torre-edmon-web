from PIL import Image
import os

for s in ["slide_21.png", "slide_22.png", "slide_23.png", "slide_24.png", "slide_25.png", "slide_26.png", "slide_27.png", "slide_28.png"]:
    img = Image.open(os.path.join("assets/slides_hires", s))
    print(f"{s}: size={img.size}, mode={img.mode}")
