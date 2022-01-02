import os
from PIL import Image

# list images in /images folder
for file in os.listdir("./images"):
    if file.endswith(".webp"):
        print(file)

