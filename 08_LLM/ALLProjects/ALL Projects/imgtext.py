from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import streamlit as st

st.title('Image - Text')

load_dotenv(find_dotenv())

pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
def task1(url):
    text = pipe(url)
    return text
    
file = st.text_input("File Path",'Image')


if(st.button('Get Text')):
    output = task1(file)[0]['generated_text']
    st.success(output)

    