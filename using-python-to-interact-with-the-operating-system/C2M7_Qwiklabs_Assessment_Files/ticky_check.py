#!/usr/bin/env python3

import re
import operator
import csv


per_user = {}
error = {}

with open("./syslog.log", mode="r", encoding="UTF-8") as f:
    for line in f.readlines():
        line = line.strip()
        m = re.search(r"ticky: INFO .* \(([\w\.]*)\)", line)
        if m:
            per_user[m.group(1)] = per_user.get(m.group(1), [0, 0])
            per_user[m.group(1)][0] += 1

        m = re.search(r"ticky: ERROR ([\w ]*) .* \(([\w\.]*)\)", line)
        if m:
            per_user[m.group(2)] = per_user.get(m.group(2), [0, 0])
            per_user[m.group(2)][1] += 1
            error[m.group(1)] = error.get(m.group(1), 0) + 1
    f.close()


error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user = [(v[0], v[1][0], v[1][1]) for v in sorted(per_user.items(), key=operator.itemgetter(0))]

with open('error_message.csv','w') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(['Error', 'Count'])
    for row in error:
        csv_file.writerow(row)

with open('user_statistics.csv','w') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(['Username', 'INFO', 'ERROR'])
    for row in error:
        csv_file.writerow(row)
