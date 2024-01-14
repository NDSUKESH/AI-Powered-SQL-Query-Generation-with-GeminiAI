from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

##connting api_key
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



##form query from the input and propt
def get_query(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

##get output
def sql_query(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name student and has the following columns -name char(30),
    class varchar(10), section varchar(10),mart int \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

st.set_page_config(page_title="SQL QUERY WITH AI",page_icon="🗃️")
st.header("Gemini App To Retrieve SQL Data")
# Just add it after st.sidebar:
st.sidebar.title("About SQL Query with AI")

st.sidebar.markdown(
    """
    This web application allows you to interact with a generative AI model to convert English questions into SQL queries. 
    Simply enter your question in the input box and click on "Ask the question" to get the corresponding SQL query. 
    The generated SQL query is then executed on a SQLite database named STUDENT.

    **Examples of questions you can ask:**
    - How many entries of records are present?
    - Tell me all the students studying in Data Science class.

    Make sure to frame your questions in a way that the AI can understand and generate meaningful SQL queries.

    **Note:**
    The SQL queries are executed on a predefined database, and the results are displayed below.

    *Powered by Gemini AI and Streamlit*
    """
)


question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_query(question,prompt)
    st.code(response)
    response=sql_query(response,"student.db")
    st.subheader("The Data is")
    for row in response:
        st.text(row)