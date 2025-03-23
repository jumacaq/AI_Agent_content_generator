import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from groq import Groq


load_dotenv()


class GroqModelHandler:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        model_name = os.getenv("MODEL_NAME")

        if not api_key:
            raise ValueError(
                "La API Key de Groq no está configurada en el archivo .env"
            )

        self.client = Groq(api_key=api_key)
        self.llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name=model_name)

    def get_client(self):
        return self.client

    def get_llm(self):
        return self.llm
