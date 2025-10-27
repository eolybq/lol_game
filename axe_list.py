from PIL import Image
import os

# Adresář obsahující obrázky
directory = os.path.join(os.getcwd(), "assets")

axe_paths = [os.path.join(directory, f"axe{i}.png") for i in range(1, 7)]

# Seznam pro uchování načtených obrázků
axes = []

# Procházení všech souborů v adresáři
for path in axe_paths:
    img = Image.open(path)
    axes.append(path)