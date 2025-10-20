import os
import google.generativeai as genai
import streamlit as st
st.title('Sentiment Analysis')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

user_input = st.text_area("Enter Your Review",'Review')
model = genai.GenerativeModel('gemini-pro')

if(st.button('Answer')):
    prompt = f"""
    You are an expert linguist, who is good at classifying customer review sentiments into Positive/Negative labels.
    Help me classify customer reviews into: Positive(Positive Review), and Negative(Negative Review).
    
    ```
    {user_input}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))