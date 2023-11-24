import streamlit as st
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


def generate_response(input_text,database_uri):     
     if not database_uri:
      #postgresql://sameeranamarnath:P6UClH5XpDdr@ep-floral-frog-97311990-pooler.ap-southeast-1.aws.neon.tech/omdb?sslmode=require
      db = SQLDatabase.from_uri(f"postgresql+psycopg2://sameeranamarnath:P6UClH5XpDdr@ep-floral-frog-97311990-pooler.ap-southeast-1.aws.neon.tech/omdb?sslmode=require&options=endpoint%3Dep%2Dfloral%2Dfrog%2D97311990%2Dpooler")
     else:
      db = SQLDatabase.from_uri(database_uri)

     llm = OpenAI(model="gpt-3.5-turbo-1106",  temperature=0, verbose=True, openai_api_key=openai_api_key,max_tokens=4096)
     db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
     st.info(db_chain.run(input_text))




st.title('Run Sql queries on database using natural language via langchain & gpt3.5')
openai_api_key = st.sidebar.text_input('Please enter your OpenAI API Key')

with st.form('data_form'):
  question = st.text_area('Enter a question in natural language for the AI on the  omdb movies postgres database')
  database_uri = st.text_area("share a sqlachemy compatible uri for a remote sql based db if you want to use another dataset ")
  
  st.text("currently used database is :postgresql+psycopg2://default:GT4dg3OemzlA@ep-curly-violet-36509009.us-east-1.postgres.vercel-storage.com:5432/verceldb")

  st.text("another sample database to try  is:   sqlite:////imdb-movie.sqlite    which is stored locally")
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(question,database_uri)