import streamlit as st
import requests
import time

st.title("🎬 Free AI Video Generator")

# Free Model URL
API_URL = "https://router.huggingface.co/hf-inference/models/damo-vilab/text-to-video-ms-1.5m"
headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

prompt = st.text_input("Video Prompt Likhein:", "A cute cat running in the park")

if st.button("Generate Video"):
    if not prompt:
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Video ban raha hai... isme 1-2 minute lag sakte hain."):
            output = query({"inputs": prompt})
            
            if output.status_code == 200:
                st.video(output.content)
                st.success("Hogaya!")
            elif output.status_code == 503:
                st.error("Model abhi 'Loading' mode mein hai. 30 seconds baad phir se try karein.")
            else:
                st.error(f"Error: {output.status_code}. Model abhi free tier par available nahi hai.")

st.info("Note: Free models kabhi kabhi slow hote hain ya down ho jate hain.")
