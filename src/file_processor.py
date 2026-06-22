import pdfplumber
from docx import Document


def extract_pdf_text(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_docx_text(file):
    doc = Document(file)

    return "\n".join([para.text for para in doc.paragraphs])


def extract_resume_text(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file)

    elif filename.endswith(".docx"):
        return extract_docx_text(file)

    return "Unsupported file format"