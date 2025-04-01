import os
from dotenv import load_dotenv
import streamlit as st
from models.content_generation_models import ContentGeneration
from src.generate_content import compute_content


# TODO: Load environment variables from .env file
load_dotenv()


# TODO: Set the title of the Streamlit app
st.title("AI-Powered Reel Content Generator")

# TODO: Add a description for the app
st.write(
    """
Ingresa una url de un producto para crear el guion
"""
)

# TODO: Create input fields for URL, target audience, tone, and language
input_url = None
new_target_audience = None
new_tone = None
language = None

# TODO: Add a button to trigger content generation
if st.button("Generar Guion"):
    if input_url and new_target_audience and new_tone and language:
        backend_url = os.getenv("BACKEND_URL", "http://backend:8004/content_generator")
        # TODO: Create a payload using the ContentGeneration model
        payload = ContentGeneration(
            url=None,
            new_target_audience=None,
            new_tone=None,
            language=None,
        )

        # TODO: Call the compute_content function to generate the script
        refined_script = None

        # TODO: Display the generated script and add a download button
        st.header("Guion Finalizado")
        st.download_button(
            label="Descargar Guion en JSON",
            data=None,
            file_name=None,
            mime=None,
        )
    else:
        # TODO: Show a warning if any input field is missing
        st.warning("Por favor, completa todos los campos.")
