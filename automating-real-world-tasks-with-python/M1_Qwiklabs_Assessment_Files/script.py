#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image

base_path = "./images/"
new_path = "./opt/icons/"
Path(new_path).mkdir(parents=True, exist_ok=True)

for file in os.listdir(base_path):
    if(file == ".DS_Store"):
        continue
    image = Image.open("{}{}".format(base_path, file))
    image = image.convert("RGB") \
        .rotate(-90) \
        .resize((128, 128)) \
        .save('{}{}.jpeg'.format(new_path, file), "JPEG")
