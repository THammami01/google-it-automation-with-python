#! /usr/bin/env python3

import os
import requests

DATA_PATH = "./data/feedback/"
IP = "34.134.1.145"

for file in os.listdir(DATA_PATH):
        with open("{}{}".format(DATA_PATH, file), "r") as f:
                req_body = {
                        "title": f.readline().strip(),
                        "name": f.readline().strip(),
                        "date": f.readline().strip(),
                        "feedback": f.read().strip()
                }

                response = requests.post("http://{}/feedback/".format(IP), json=req_body)
                print(response.status_code)
                f.close()
