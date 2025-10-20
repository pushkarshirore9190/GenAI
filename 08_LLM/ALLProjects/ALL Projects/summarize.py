import os
import google.generativeai as genai
import streamlit as st
st.title('Summarize')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Content",'Content')
model = genai.GenerativeModel('gemini-pro')


if(st.button('Summary')):
    prompt = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 2 lines.
    
    ```
    {user_input}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))