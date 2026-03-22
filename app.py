import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="My AI Assistant")
st.title("🤖 My Personal Gemini AI")

# Secrets se key check karna
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Pehle Streamlit Secrets mein API key add karein!")
    st.stop()

# Gemini setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat interface
user_input = st.text_input("Mujhse kuch bhi puchiye:", placeholder="Kaise ho?")

if st.button("Puchiye"):
    if user_input:
        with st.spinner("AI soch raha hai..."):
            response = model.generate_content(user_input)
            st.write("### AI Ka Jawab:")
            st.write(response.text)
    else:
        st.warning("Pehle kuch type karein!")
