#!/usr/bin/env python3
import sys
import subprocess

with open(sys.argv[1]) as f:
        for old_file in f.readlines():
                old_file = old_file.strip()
                new_file = old_file.replace("jane", "jdoe")
                subprocess.run(["mv", old_file, new_file])
                f.close()
