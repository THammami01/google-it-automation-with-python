#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

base_path = "./supplier-data/images/"
new_path = "./supplier-data/images/"
Path(new_path).mkdir(parents=True, exist_ok=True)

for file in os.listdir(base_path):
    if(file.endswith(".tiff")):
        image = Image.open("{}{}".format(base_path, file))
        image = image.convert("RGB") \
            .resize((600, 400)) \
            .save('{}{}.jpeg'.format(new_path, file[:-5]), "JPEG")
