from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PdfGenerator:
    def __init__(self, pdf_name="cv.pdf"):
        self.pdf_file = SimpleDocTemplate(pdf_name, pagesize=letter)
        self.content = []

    def generate_pdf(self, data):
        styles = getSampleStyleSheet()
        for section, value in data.items():
            if section != 'submit' and section != 'csrf_token':
                if value:
                    self.content.append(Paragraph(section.capitalize(), styles['Heading2']))
                    self.content.append(Paragraph(value, styles['Normal']))
                    self.content.append(Paragraph("", styles['Normal']))

    def finish_pdf(self):
        self.pdf_file.build(self.content)
        return send_file(self.pdf_file.filename, as_attachment=True)
