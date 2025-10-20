from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import streamlit as st
import soundfile as sf
from datasets import load_dataset
import torch

load_dotenv(find_dotenv())
st.title('Text - Audio')
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
file = st.text_input("Enter Text",'Text')




if(st.button('Get Speech')):
    speech = synthesiser(file, forward_params={"speaker_embeddings": speaker_embedding})
    sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
    st.audio("speech.wav", format="wav")
    