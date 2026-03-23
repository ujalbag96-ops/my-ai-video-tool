import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 My Personal Gemini AI")

# 1. Secrets se API Key check aur setup karna
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Pehle Streamlit Cloud ke Secrets mein 'GEMINI_API_KEY' add karein!")
    st.stop()

# Gemini setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model initialize (Latest stable version)
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat interface
user_input = st.text_input("Mujhse kuch bhi puchiye:", placeholder="Kaise ho?")

if st.button("Puchiye"):
    if user_input:
        try:
            with st.spinner("AI soch raha hai..."):
                response = model.generate_content(user_input)
                
                st.subheader("AI Ka Jawab:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Ek error aaya: {e}")
            st.info("Check karein ki aapki API Key valid hai aur quota khatam toh nahi hua.")
    else:
        st.warning("Pehle kuch type karein!")
