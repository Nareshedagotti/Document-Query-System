import os
from PyPDF2 import PdfReader
from docx import Document as DocxReader

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    try:
        doc = DocxReader(docx_path)
        text = " ".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"

# Function to extract text from TXT
def extract_text_from_txt(txt_path):
    try:
        with open(txt_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text.strip()
    except Exception as e:
        return f"Error extracting text from TXT: {e}"

# Function to process uploaded files
def process_uploaded_file(file):
    if file.name.endswith(".pdf"):
        return extract_text_from_pdf(file.name)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file.name)
    elif file.name.endswith(".txt"):
        return extract_text_from_txt(file.name)
    else:
        return "Unsupported file format. Please upload a PDF, DOCX, or TXT file."
