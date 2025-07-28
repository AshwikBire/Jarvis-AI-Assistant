import pdfplumber

def read_pdf_text(file):
    with pdfplumber.open(file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text