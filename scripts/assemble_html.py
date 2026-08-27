with open("scripts/part1.html", "r", encoding="utf-8") as f1, \
     open("scripts/part2.html", "r", encoding="utf-8") as f2, \
     open("scripts/part3.html", "r", encoding="utf-8") as f3, \
     open("index.html", "w", encoding="utf-8") as fout:
    fout.write(f1.read() + f2.read() + f3.read())

print("index.html ensamblado exitosamente!")
