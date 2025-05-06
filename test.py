import streamlit as st
import google.generativeai as genai

# Configurar API Key desde secretos
genai.configure(api_key=st.secrets["AIzaSyAJL5bTjSrQXY13hP1PXtDHySUM--Gz1U4"])

st.title("🔮 Prueba de conexión con Gemini")

prompt = st.text_input("Escribe algo para preguntar a Gemini:")

if prompt:
    model = genai.GenerativeModel("gemini-2.0-pro")
    response = model.generate_content(prompt)
    st.write("**Respuesta de Gemini:**")
    st.write(response.text)
