import fitz
doc = fitz.open("FOLLETO TORRE EDMON-2.pdf")
print("PDF pages count:", len(doc))
for i in range(20, 28):
    print(f"--- Page {i+1} ---")
    txt = doc[i].get_text()
    if txt.strip():
        print(txt)
    else:
        print("(Render / Image only)")
