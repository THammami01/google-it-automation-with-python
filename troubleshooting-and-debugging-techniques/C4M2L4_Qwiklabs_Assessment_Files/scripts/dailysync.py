#!/usr/bin/env python

import subprocess
# import multiprocessing
# import os

src = "data/prod/"
dest = "data/prod_backup/"
subprocess.call(["rsync", "-zrvh", src, dest])
