import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from prompts.tone_generator import GENERATE_REFINED_INFO
from prompts.content_generation_prompts import GENERATE_INFO
from src.llm import GroqModelHandler
from models.content_generation_models import (
    ContentGenerationScript,
    ToneGenerationScript,
)

load_dotenv()


class ContentGenerator:
    def __init__(self):
        """Inicializa el generador de texto con un modelo LLM de Groq."""
        # TODO: Inicializar el manejador del modelo LLM de Groq
        self.llm = None

    def create_parser(self):
        """Crea un parser para el contenido del reel."""
        # TODO: Crear un JsonOutputParser para ContentGenerationScript
        return None

    def create_tone_parser(self):
        """Crea un parser para el tono del reel."""
        # TODO: Crear un JsonOutputParser para ToneGenerationScript
        return None

    def create_script_chain(self, template, parser, input_variables):
        """Crea la cadena de resumen con un PromptTemplate y el parser definido."""
        # TODO: Crear un PromptTemplate con el template, input_variables y format_instructions
        reduce_prompt = None
        # TODO: Crear un LLMChain con el modelo, el prompt y el parser
        return None

    def generate_text(self, info):
        """Genera un texto basado en la información de entrada."""
        parser = self.create_parser()
        content_chain = self.create_script_chain(
            template=GENERATE_INFO,
            parser=parser,
            input_variables=[
                "title",
                "price",
                "description",
                "available_sizes",
                "additional_info",
                "image_description",
            ],
        )

        return content_chain.invoke(
            {
                "title": info["title"],
                "price": info["price"],
                "description": info["description"],
                "available_sizes": info["available_sizes"],
                "additional_info": info["additional_info"],
                "image_description": info["image_description"],
            }
        )

    def apply_tone(self, script, new_target_audience, new_tone, language):
        # TODO: Crear el parser para el tono
        parser_tone = None
        # TODO: Crear la cadena de generación de tono
        generation_chain = None

        # TODO: Invocar la cadena con el script, audiencia, tono y lenguaje
        return None

    def generate_content(self, metadata, new_target_audience, new_tone, language):
        # TODO: Generar el texto inicial
        generate_text = None
        # TODO: Aplicar el tono al texto generado
        return None
