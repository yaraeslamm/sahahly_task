import pdfplumber
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text.strip()

def extract_student_answer(text):
    if "Student Answer:" in text:
        return text.split("Student Answer:")[1].strip()
    return text