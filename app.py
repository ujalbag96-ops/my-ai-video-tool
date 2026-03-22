import streamlit as st
import requests
import time

# Streamlit Secrets se token lena
try:
    hf_token = st.secrets["HF_TOKEN"]
except Exception:
    st.error("Secrets mein HF_TOKEN nahi mila!")
    st.stop()

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/animatediff-v2"
headers = {"Authorization": f"Bearer {hf_token}"}

st.title("🎥 AI Video Generator")
prompt = st.text_input("Describe your video:", "A small cat playing with a ball.")

if st.button("Generate Video"):
    if not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("AI is cooking your video... Please wait 1-2 minutes."):
            # Hugging Face API call
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
            
            if response.status_code == 200:
                st.video(response.content)
                st.success("Done!")
            elif response.status_code == 401:
                st.error("Error 401: Token invalid hai. Hugging Face se nayi WRITE token lijiye.")
            elif response.status_code == 503:
                st.info("Model load ho raha hai... 30 seconds baad phir se button dabayein.")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
