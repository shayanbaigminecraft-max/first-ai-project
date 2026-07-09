import os
import json
import traceback
import pandas as pd
import PyPDF2

from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api = os.getenv("MISTRAL")
print("MISTRAL API KEY:", api)

llm = ChatMistralAI(
    api_key=api,
    model="mistral-large-latest",
    temperature=1,
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

response_path = os.path.join(BASE_DIR, "response.json")

with open(response_path, "r") as f:
    RESPONSE_JSON = json.load(f)

    print(RESPONSE_JSON)

template = """
You are an expert MCQ creator with strong knowledge of educational assessment.

Your task is to create a quiz based ONLY on the provided text.

TEXT:
{text}

Instructions:
- Generate exactly {number} multiple-choice questions.
- multiple choice question from {subject} subject.
- The difficulty level should be {tone}.
- Every question must have exactly four options labeled A, B, C, and D..
- Only one option should be correct.
- Do not create questions from information that is not present in the provided text.
- Ensure the questions are clear, relevant, and non-repetitive.
- Make sure the quiz is suitable for students.
- Return ONLY valid JSON.
- Do not include explanations, markdown, or additional text.

The JSON format must exactly match the following schema:

{response}
"""

prompt = PromptTemplate (
    input_variables=["text", "number", "subject", "tone", "response"],
    template=template,
)

chain1 = prompt | llm 

print(chain1)

template2 = """You are an expert English examiner and MCQ evaluator.

Subject:
{subject}


Task:
You must evaluate the given multiple choice questions based on cognitive and analytical level of students.

Instructions:
- Check if questions are clear, correct, and meaningful
- Check difficulty level according to students' understanding
- Identify any grammar or conceptual mistakes
- If quiz is not appropriate for students' cognitive level, suggest regeneration

Final Output Rules:
1. Provide a complete analysis in exactly 50 words
2. Clearly state whether quiz is GOOD or NEEDS IMPROVEMENT
3. If needed, suggest to regenerate improved version
4. Be strict and professional like an examiner
Quiz MCQs:
{quiz}

"""

prompt2 = PromptTemplate (
    input_variables=["subject","quiz"],
    template=template2,
)

chain2 = prompt2 | llm 


def gen_mcq(text, number, subject, tone):

    quiz = chain1.invoke({
        "text": text,
        "number": number,
        "subject": subject,
        "tone": tone,
       "response": json.dumps(RESPONSE_JSON)
    })

    review = chain2.invoke({
        "subject": subject,
        "quiz": quiz.content
    })

    return quiz.content, review.content

