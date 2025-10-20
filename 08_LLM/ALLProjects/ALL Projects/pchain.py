import os
import google.generativeai as genai
import streamlit as st
st.title('Language Translation')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Content")
model = genai.GenerativeModel('gemini-pro')


if(st.button('Summary')):
    prompt1 = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 2 lines.
    
    ```
    {user_input}
    ```
    """
    response1 = model.generate_content(prompt1)
    
    prompt2 = f"""
    You need to analyse the sentiment of provided text as positive/negative.
    
    ```
    {response1}
    ```
    """
    response2 = model.generate_content(prompt2)
    st.success("Summary:  {}.".format(response1.text))
    st.success("Sentiment {}.".format(response2.text))