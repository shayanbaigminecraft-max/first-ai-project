import os
import json 
import traceback 
import pandas as pd 
from dotenv import load_dotenv
from src.mcqs_gen.utils import read_file, get_table_data
import streamlit as st
from src.mcqs_gen.mcqgenerator import gen_mcq
from src.mcqs_gen.logger import logging


#title of the app
st.title("MCQ Generator by Shayan Baig")

#use input form 
with st.form("my_form"):
    #subject input
    subject = st.text_input("Enter the subject:" , max_chars=20)
    #difficulty level input
    tone = st.selectbox("Select the difficulty level:", ["Easy", "Medium", "Hard"])
    #number of questions input
    number = st.number_input("Enter the number of questions:", min_value=5, max_value=50, value=5)
    #file upload input
    file = st.file_uploader("Upload a PDF file:", type=["pdf"])
    
    #submit button
    submitted = st.form_submit_button("Generate MCQs")
    
    if submitted:
        if not subject:
            st.error("Please enter a subject.")
        elif not file:
            st.error("Please upload a PDF file.")
        else:
            with st.spinner("Generating MCQs jusat wait...."):
                try:
                    #read the uploaded file
                    text = read_file(file)
                    #generate mcqs
                    quiz , review = gen_mcq(text, number, subject, tone)
                    #display the generated mcqs
                    st.success("MCQs generated successfully!")
                    st.subheader("Generated MCQs")
                    st.write(quiz)
              
                except Exception as e:
                    logging.error(traceback.format_exc())

                    st.error(str(e))
                    st.code(traceback.format_exc())