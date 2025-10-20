import streamlit as st
from openai import OpenAI

st.title("ChatBot")


setapi = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


if "model_response" not in st.session_state:
    st.session_state["model_response"] = "gpt-3.5-turbo"

if "input" not in st.session_state:
    st.session_state['input'] = []


for m in st.session_state['input']:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Pucho ji Pucho Sharmao matt")
if prompt:
    st.session_state['input'].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
with st.chat_message("assistant"):
        chatting = setapi.chat.completions.create(
            model=st.session_state["model_response"],
            messages=[
                {"role": chatt["role"], "content": chatt["content"]}
                for chatt in st.session_state['input']
            ],
            stream=True,
        )
        response = st.write_stream(chatting)
st.session_state['input'].append({"role": "assistant", "content": response})



