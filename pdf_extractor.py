# import pdfplumber

# def extract_text_from_pdf(file):
#     text = ""
#     with pdfplumber.open(file) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     print(text)
#     return text
import pdfplumber
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    text = ""
    with pdfplumber.open(BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text.strip()
    

# from pdf2image import convert_from_path
# import pytesseract

# # 1. Convert PDF pages to list of images
# pages = convert_from_path('/Users/funnyflea7/Desktop/masters apps/ipcv/Bachelor_Degree.pdf', dpi=300)

# # 2. Iterate through pages and extract text
# full_text = ""
# for page in pages:
#     text = pytesseract.image_to_string(page)
#     full_text += text

# print(full_text)

if __name__ == "__main__":
    extract_text_from_pdf('/Users/funnyflea7/Desktop/masters apps/ipcv/Bachelor_Degree.pdf')