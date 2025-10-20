import os
import google.generativeai as genai
import streamlit as st
st.title('Language Translation')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Sentence")
model = genai.GenerativeModel('gemini-pro')
option = st.selectbox(
     'Select Language',
     ('Hindi', 'French', 'Spanish'))

if(st.button('Translate')):
    prompt = f"""
    You are an expert linguist, who is good at translating a given sentence into target language.
    Help me translate the sentence into: {option}.
    
    ```
    {user_input}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))