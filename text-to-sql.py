import os 

import streamlit as st
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


import sys


def generate_response(input_text):
     db = SQLDatabase.from_uri("sqlite:///imdb-movie.sqlite")
     llm = OpenAI(temperature=0, verbose=True, openai_api_key=openai_api_key)
     db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
     st.info(db_chain.run(input_text))


load_dotenv() #load the hugging face key
# Model name that we want to use
# https://huggingface.co/meta-llama/Llama-2-7b-chat-hf



st.title('Run Sql queries on database using natural language via langchain & gpt3.5- Amar.S')
openai_api_key = st.sidebar.text_input('Please enter your OpenAI API Key')

with st.form('my_form'):
  question = st.text_area('Enter a question in natural language for the AI on the  imdb movies sqlite database')
  database = st.file_uploader("Choose a file")
  if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(question)