import os
import PyPDF2
import json
import traceback

def read_file():
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print exception ("error reading pdf file")
    elif file.name.endswith(".txt"):
return file.read().decode("utf-8")
else:
raise exception ("Unsupported file format. Please upload a PDF or TXT file.")

def get_table_data():
    
