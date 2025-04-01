import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from groq import Groq


# Cargar variables del archivo .env
load_dotenv()


class GroqModelHandler:
    def __init__(self):
        # TODO: Load the Groq API key and model name from environment variables
        api_key = None
        model_name = None

        # TODO: Validate if the API key is provided
        if not api_key:
            raise ValueError(
                "La API Key de Groq no está configurada en el archivo .env"
            )

        # TODO: Initialize the Groq client and ChatGroq LLM
        self.client = None
        self.llm = None

    def get_client(self):
        # TODO: Return the Groq client instance
        return None

    def get_llm(self):
        # Example method for students to follow
        return self.llm
