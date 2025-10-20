import streamlit as st
from langchain.chains import SequentialChain
from langchain import PromptTemplate
from langchain.chains import LLMChain

st.title('Langchain Project')
import os
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY'] = 'sk-'
llm = OpenAI(temperature = 0.6)

promptt = PromptTemplate(
    input_variables =['country'],
    template = "whats the capital of {country}"
)
chain1 = LLMChain(llm=llm, prompt=promptt, output_key="capital")

prompt_food = PromptTemplate(
    input_variables = ['capital'],
    template="""suggest some most famous food items of {capital}"""
)
chain2 = LLMChain(llm=llm, prompt=prompt_food, output_key="food")

final_chain = SequentialChain(
    chains = [chain1, chain2],
    input_variables = ['country'],
    output_variables = ['capital', 'food']
)
user_input = st.text_input("Enter Country")

if(st.button('Get Food')):
    response = final_chain.invoke({"country": user_input })
    st.success(response['country'])
    st.success(response['capital'])
    st.success(response['food'])