import os
import google.generativeai as genai
import streamlit as st
st.title('Question-Answers')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Question",'Question')
model = genai.GenerativeModel('gemini-pro')
if(st.button('Answer')):
    response = model.generate_content(user_input)
    st.success("Answer {}.".format(response.text))