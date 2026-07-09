import os
import json 
import traceback 
import pandas as pd 
from dotenv import load_dotenv
from src.mcqs_gen.utils import read_file, get_table_data
import streamlit as st
from src.mcqs_gen.mcqgenerator import gen_mcq
from src.mcqs_gen.logger import logging

#loading json file
with open("../response.json", "r") as f:
    response = json.load(f)

#title of the app
st.title("MCQ Generator")
