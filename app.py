import streamlit as st
import requests

# Setup
API_URL = "https://api-inference.huggingface.co/models/THUDM/CogVideoX-5B"
HF_TOKEN = "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"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.set_page_config(page_title="My AI Video Gen", layout="centered")
st.title("🎥 Personal AI Video Generator")

prompt = st.text_area("Video Scene Describe Karein (English):", "A cinematic sunrise over the ocean, 4k ultra realistic")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI video bana raha hai... 2-5 minutes lag sakte hain."):
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                if response.status_code == 200:
                    st.video(response.content)
                    st.success("Video Taiyar Hai!")
                else:
                    st.error("Server Busy hai. Thodi der baad try karein.")
            except:
                st.error("Connection error.")
    else:
        st.warning("Pehle kuch likhiye!")
      
