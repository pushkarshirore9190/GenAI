from langchain_ollama.llms import OllamaLLM
import streamlit as st
llm =  OllamaLLM(model="llama3")

st.title('Sentence Completion')

user_input = st.text_area("Enter Your Sentence")
context = f"""
        My name is shridhar mankar. I am a teacher. I have done my Bacholers from AISSMS COE in 2015-2019.
        I Have completed my masters from COEP in 2021.
        """
if(st.button('Sentence')):
    prompt = f"""
    You are have to auto complete the sentence based on the context that i have provided between ## separator:
    ##
    {context}
    ##
    
    input sentence is mentioned below, delimited with triple backticks:
    
    ```
    {user_input}
    ```
    """
    response = llm.invoke(prompt)
    st.success("{}.".format(response))