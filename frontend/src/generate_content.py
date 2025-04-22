import requests
from models.content_generation_models import ContentGeneration
import streamlit as st


def compute_content(payload: ContentGeneration, backend_url: str):
    try:
        # Send a POST request to the server with the payload
        r = requests.post(
            backend_url,
            json=payload.dict(),
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
    
        # Raise an exception if the request fails
        r.raise_for_status()

        # Extract and return the generated content from the response
        generated_content = r.json()
        return generated_content
    
    except requests.exceptions.RequestException as e:
        return {"error": "Hubo un problema al contactar el backend", "message": str(e)}
        # Handle request exceptions and return an error message
        
    

  