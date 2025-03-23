import os
from dotenv import load_dotenv
import streamlit as st
from models.content_generation_models import ContentGeneration
from src.generate_content import compute_content

load_dotenv()


st.title("AI-Powered Reel Content Generator")

st.write(
    """
Ingresa una url de un producto para crear el guion
"""
)

input_url = st.text_input("Ingrese la URL de un producto")
new_target_audience = st.text_input("Nuevo público objetivo")
new_tone = st.text_input("Nuevo tono")
language = st.selectbox("Idioma", ["Español", "Inglés", "Francés", "Portugués"])

if st.button("Generar Guion"):
    if input_url and new_target_audience and new_tone and language:
        backend_url = os.getenv("BACKEND_URL", "http://backend:8004/content_generator")
        payload = ContentGeneration(
            url=input_url,
            new_target_audience=new_target_audience,
            new_tone=new_tone,
            language=language,
        )
        refined_script = compute_content(payload, backend_url)

        st.header("Guion Finalizado")
        st.download_button(
            label="Descargar Guion en JSON",
            data=refined_script,
            file_name="guion.json",
            mime="application/json"
        )
    else:
        st.warning("Por favor, completa todos los campos.")
