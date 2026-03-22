import streamlit as st
import requests
import time

# Setup
API_URL = "https://api-inference.huggingface.co/models/THUDM/CogVideoX-5B"
HF_TOKEN = "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"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

st.set_page_config(page_title="My AI Video Generator", layout="centered")
st.title("🎥 Personal AI Video Generator")

prompt = st.text_area("Describe the scene (English):", "A cinematic sunrise over the ocean, 4k ultra realistic")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("AI is waking up... Isme 1-2 minute lag sakte hain agar server busy ho."):
            # First attempt to wake up the model
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            
            # Agar model load ho raha hai (Status 503), toh wait karein
            if response.status_code == 503:
                st.info("Model load ho raha hai... Hum 20 seconds mein fir try karenge.")
                time.sleep(20)
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

            if response.status_code == 200:
                st.video(response.content)
                st.success("Video Taiyar Hai!")
            else:
                st.error(f"Server busy hai (Error {response.status_code}). 1 minute baad button fir se dabayein.")
    else:
        st.warning("Pehle kuch likhiye!")
