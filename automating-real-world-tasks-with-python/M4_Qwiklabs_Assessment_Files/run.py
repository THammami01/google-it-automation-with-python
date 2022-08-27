#! /usr/bin/env python3

import os
from pathlib import Path
import requests

descriptions_path = "./supplier-data/descriptions/"
images_path = "./supplier-data/images/"

Path(descriptions_path).mkdir(parents=True, exist_ok=True)
Path(images_path).mkdir(parents=True, exist_ok=True)
url = "http://localhost/fruits/"

for text_file in os.listdir(descriptions_path):
    if(text_file.endswith(".txt")):
        image_file = text_file[:-4] + ".jpeg"
        with open("{}{}".format(descriptions_path, text_file), 'r') as f:
            req_body = {
                "name": f.readline().strip(),
                "weight": int(f.readline().strip().strip("lbs")),
                "description": f.readline().strip(),
                "image_name": image_file
            }
            requests.post(url, req_body, json=req_body)
