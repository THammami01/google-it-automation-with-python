#!/usr/bin/env python3

import shutil
import psutil
import emails

# ! TODO: TO BE FIXED

USER = "student-02-d516bc8cad77"
subject = ""

time_interval = 4


cpu_usage = psutil.cpu_percent(time_interval)
available_disk_space = None
available_memory = None

# CPU usage is over 80%
# Error - CPU usage is over 80%
if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"

# Available disk space is lower than 20%
# Error - Available disk space is less than 20%
if available_disk_space > 80:
    pass

    # available memory is less than 500MB
    # Error - Available memory is less than 500MB
if available_memory > 80:
    pass


    # hostname "localhost" cannot be resolved to "127.0.0.1"
    # Error - localhost cannot be resolved to 127.0.0.1

    # SEND EMAIL
if subject:
    sender = "automation@example.com"
    receiver = "{}@example.com".format(USER)
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)
