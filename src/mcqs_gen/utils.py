import os
import PyPDF2
import json
import traceback


def read_file(file):
    try:
        if file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""

            for page in pdf_reader.pages:
                text += page.extract_text()

            return text

        elif file.name.endswith(".txt"):
            return file.read().decode("utf-8")

        else:
            raise Exception("Unsupported file format. Please upload a PDF or TXT file.")

    except Exception as e:
        print("Error reading file:", e)
        raise

def get_table_data(quiz_dict):
    quiz_table_data = []

    for value in quiz_dict["quiz"]:

        mcq = value["question"]

        options = " | ".join(
            [
                f"{option}: {option_value}"
                for option, option_value in value["options"].items()
            ]
        )

        correct = value["correct_answer"]

        quiz_table_data.append(
            {
                "MCQ": mcq,
                "Choices": options,
                "Correct Answer": correct,
            }
        )

    return quiz_table_data