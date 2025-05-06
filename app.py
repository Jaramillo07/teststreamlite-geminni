import streamlit as st
import google.generativeai as genai

# Configurar API Key desde secretos
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


st.title("🔮 Prueba de conexión con Gemini")

prompt = st.text_input("Escribe algo para preguntar a Gemini:")

if prompt:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    st.write("**Respuesta de Gemini:**")
    st.write(response.text)
