from PIL import Image
import os

# Adresář obsahující obrázky
directory = os.path.dirname(os.path.abspath(__file__))

# Seznam pro uchování načtených obrázků
axes = []

# Procházení všech souborů v adresáři
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        # Načtení obrázku a přidání do seznamu
        img = Image.open(os.path.join(directory, filename))
        axes.append(img)

