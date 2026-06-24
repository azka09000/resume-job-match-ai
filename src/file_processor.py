import pdfplumber
from docx import Document


def clean_text(text):
    """
    Remove extra whitespace and newlines.
    """
    return " ".join(text.split())


def extract_pdf_text(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text.strip() + "\n"

    return clean_text(text)


def extract_docx_text(file):
    doc = Document(file)

    paragraphs = [
        para.text.strip()
        for para in doc.paragraphs
        if para.text.strip()
    ]

    text = "\n".join(paragraphs)

    return clean_text(text)


def extract_resume_text(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file)

    elif filename.endswith(".docx"):
        return extract_docx_text(file)

    return "Unsupported file format"