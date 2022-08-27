#!/usr/bin/env python3

import os
from datetime import datetime
from pathlib import Path
import reports
import emails


USER = "student-02-d516bc8cad77"
descriptions_path = "./supplier-data/descriptions/"
Path(descriptions_path).mkdir(parents=True, exist_ok=True)


def get_descriptions():
    Path(descriptions_path).mkdir(parents=True, exist_ok=True)
    descriptions = []
    for text_file in os.listdir(descriptions_path):
        with open("{}{}".format(descriptions_path, text_file), 'r') as f:
            descriptions.append(
                "name: {}<br />weight: {}".format(
                    f.readline().strip(), format(f.readline().strip())
                )
            )
            descriptions.append("")

    descriptions.pop()
    return descriptions


def main():
    # GENERATE REPORT
    filename = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(
        datetime.today().strftime('%d %B, %Y')
    )
    descriptions = get_descriptions()
    reports.generate(filename, title, descriptions)

    # SEND EMAIL
    sender = "automation@example.com"
    receiver = "{}@example.com".format(USER)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)


if __name__ == "__main__":
    main()
