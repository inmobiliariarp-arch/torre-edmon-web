import os
import shutil

src = r"D:\Proyecto sitio web edificio\.github\workflows\deploy.yml"
dst = r"D:\Proyecto sitio web edificio\docs\github-pages-workflow.yml"
if os.path.exists(src):
    shutil.copy2(src, dst)
    shutil.rmtree(r"D:\Proyecto sitio web edificio\.github")
    print("Workflow moved to docs/github-pages-workflow.yml")
