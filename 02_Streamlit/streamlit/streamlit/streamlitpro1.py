import re
import streamlit as st
user_input = st.text_area("Enter Your Email ID")

pattern = re.compile(r'([A-Za-z0-9]+[.])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')

def check(email):
    if re.fullmatch(pattern, email):
      return "Valid email id"
    else:
      return "Invalid email id"
      
if(st.button('Check')):
    response = check(user_input)
    st.success(response)
      
