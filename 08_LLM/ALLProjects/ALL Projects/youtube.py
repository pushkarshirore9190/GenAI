import os
import google.generativeai as genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
st.title('Youtube Video Summarization')

os.environ['GOOGLE_API_KEY'] = "key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


video = st.text_input("Enter Video Link")


def vid(video):
    video1=video[17:28]
    return video1


def getts(video):
    transcript_text=YouTubeTranscriptApi.get_transcript(vid(video))

    ts = ""
    for i in transcript_text:
        ts += " " + i["text"]
        
    return ts

if(st.button('Summary')):
    transcript = getts(video)
    prompt = f"""
    You are an expert linguist, who is good at summarizing the content.
    Help me summarizing the content into: 100 words.
    
    ```
    {transcript}
    ```
    """
    response = model.generate_content(prompt)
    st.success("{}.".format(response.text))