import os
import google.generativeai as genai
import streamlit as st
st.title('Code Explainer')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Code")
model = genai.GenerativeModel('gemini-pro')
if(st.button('Explain')):
    prompt = f"""
    You are an expert linguist, who is good at explaining the code.
    You have to act as a python code explainer.
    Your task is to help me with a step
    by step explaination of given python code snippet also generate output for the same.
    Code snippet is shared below, delimited with triple backticks
    
    ```
    {user_input}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))