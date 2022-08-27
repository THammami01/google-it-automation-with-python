#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate(filename, title, descriptions):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)

    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)

    report_data = [report_title, empty_line]
    for desc in descriptions:
        if desc == "":
            report_data.append(empty_line)
        else:
            report_data.append(Paragraph(desc, styles["BodyText"]))

    report.build(report_data)
