import requests
from models.content_generation_models import ContentGeneration
import streamlit as st


def compute_content(payload: ContentGeneration, server_url: str):
    try:
        r = requests.post(
            server_url,
            json=payload.dict(),
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        r.raise_for_status()
        generated_content = r.json()
        return generated_content['generated_content']['text']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
