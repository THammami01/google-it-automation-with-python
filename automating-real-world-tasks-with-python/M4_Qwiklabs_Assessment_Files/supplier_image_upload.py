#!/usr/bin/env python3

import os
from pathlib import Path
import requests

base_path = "./supplier-data/images/"
Path(base_path).mkdir(parents=True, exist_ok=True)
url = "http://localhost/upload/"

for file in os.listdir(base_path):
    if(file.endswith(".jpeg")):
        with open("{}{}".format(base_path, file), 'rb') as opened:
            requests.post(url, files={'file': opened})
