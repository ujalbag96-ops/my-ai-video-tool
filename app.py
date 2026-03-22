import streamlit as st
import requests

# Stable Model for Quick Video Generation
API_URL = "https://api-inference.huggingface.co/models/facebook/animatediff-v2"
HF_TOKEN = "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"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.set_page_config(page_title="Deepak AI Video Tool", layout="centered")
st.title("🎥 AI Video Generator")
st.write("Create short AI videos easily!")

prompt = st.text_input("Describe your video:", "A cute cat playing in the garden")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI is working... creates video in 60 seconds!"):
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            
            if response.status_code == 200:
                st.video(response.content)
                st.success("Done!")
            elif response.status_code == 503:
                st.info("Model is loading... Please wait 30 seconds and click again.")
            else:
                st.error(f"Error: {response.status_code}. Try a different prompt.")
    else:
        st.warning("Please enter a prompt.")
