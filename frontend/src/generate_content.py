import requests
from models.content_generation_models import ContentGeneration
import streamlit as st


def compute_content(payload: ContentGeneration, server_url: str):
    try:
        # TODO: Send a POST request to the server with the payload
        r = None

        # TODO: Raise an exception if the request fails
        r.raise_for_status()

        # TODO: Extract and return the generated content from the response
        generated_content = None
        return None
    except requests.exceptions.RequestException as e:
        # TODO: Handle request exceptions and return an error message
        return None