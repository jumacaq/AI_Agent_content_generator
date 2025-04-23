#import os
import json
#from dotenv import load_dotenv
import streamlit as st
#from models.content_generation_models import ContentGeneration
from src.content_generation_model import ContentGeneration
from src.generate_content import compute_content


# Load environment variables from .env file
#load_dotenv()


# Set the title of the Streamlit app
st.title("AI-Powered Reel Content Generator")

# Add a description for the app
st.write(
    """
Ingresa una url de un producto para crear el guion
"""
)

# Create input fields for URL, target audience, tone, and language
input_url = st.text_input("Ingrese la URL de un producto")
new_target_audience = st.text_input("Nuevo público objetivo")
new_tone = st.text_input("Tono deseado")
language = st.text_input("Idioma del contenido")

# Add a button to trigger content generation
if st.button("Generar Guion"):
    if input_url and new_target_audience and new_tone and language:
        backend_url = st.secrets.get("BACKEND_URL", "http://backend:8004/content_generator")
        #backend_url = os.getenv("BACKEND_URL", "http://backend:8004/content_generator")
        # Create a payload using the ContentGeneration model
        payload = ContentGeneration(
            url=input_url,
            target_audience=new_target_audience,
            tone=new_tone,
            language=language,
        )
        
        # Call the compute_content function to generate the script
        refined_script = compute_content(payload, backend_url)

        # Display the generated script and add a download button
        st.header("Guion Finalizado")
        

        # Procesar respuesta si tiene la forma esperada
        try:
            text_block = refined_script["generated_content"]["text"]
    
            # Eliminar los backticks y el tipo de bloque
            clean_json_str = text_block.strip().replace("```json", "").replace("```", "").strip()

            # Convertir a diccionario real
            parsed_content = json.loads(clean_json_str)

            # Mostrar contenido generado
            generated_text = parsed_content.get("refined_content")
            if generated_text:
                st.text_area("Contenido Generado", generated_text, height=300)
            else:
                st.warning("No se encontró 'refined_content' dentro del JSON.")
        except Exception as e:
            st.error(f"Error procesando la respuesta: {e}")
        
        st.download_button(
            label="Descargar Guion en JSON",
            data=json.dumps(refined_script, ensure_ascii=False, indent=4),
            file_name="guion.json",
            mime="application/json",
        )
    else:
        # Show a warning if any input field is missing
        st.warning("Por favor, completa todos los campos.")
         

        
# Show the content nicely
