import fitz
import os

doc = fitz.open("FOLLETO TORRE EDMON-2.pdf")
os.makedirs("assets/raw_pure_extracted", exist_ok=True)

img_count = 0
extracted_list = []

for page_idx, page in enumerate(doc):
    image_list = page.get_images(full=True)
    for img_idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        width = base_image["width"]
        height = base_image["height"]
        
        # Only keep real high-res images (ignore 1x1 or tiny icons < 100px)
        if width >= 200 and height >= 200:
            img_count += 1
            filename = f"img_{img_count:02d}_p{page_idx+1:02d}_{width}x{height}.{image_ext}"
            filepath = os.path.join("assets/raw_pure_extracted", filename)
            with open(filepath, "wb") as f:
                f.write(image_bytes)
            extracted_list.append((img_count, page_idx+1, width, height, filename, os.path.getsize(filepath)/1024))

print(f"Total pure images extracted: {len(extracted_list)}")
for item in extracted_list:
    print(f"ID #{item[0]:02d} | Pag {item[1]:02d} | Dim: {item[2]}x{item[3]} | Size: {item[5]:.1f} KB | {item[4]}")
