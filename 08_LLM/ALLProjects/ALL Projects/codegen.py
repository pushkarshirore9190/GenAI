import os
import google.generativeai as genai
import streamlit as st
st.title('Code Generator')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Problem Statement")
model = genai.GenerativeModel('gemini-pro')
option = st.selectbox(
     'Select Programming Language',
     ('Python', 'C', 'C++'))

if(st.button('Generate')):
    prompt = f"""
    You are an expert coder, who is good at coding a given problem statement into target programming language.
    Help me code the problem statement into: {option}.
    
    ```
    {user_input}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))