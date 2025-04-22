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
        #Inicializa el generador de texto con un modelo LLM de Groq.
        self.llm = GroqModelHandler().get_llm()
        
    def create_parser(self):
        #Crea un parser para el contenido del reel."""
        return JsonOutputParser(pydantic_object=ContentGenerationScript)
        
    def create_tone_parser(self):
        #Crea un parser para el tono del reel.
        return JsonOutputParser(pydantic_object=ToneGenerationScript)

    def create_script_chain(self, template, parser, input_variables):
        #Crea la cadena de resumen con un PromptTemplate y el parser definido.
        prompt = PromptTemplate(
            input_variables=input_variables,
            template=template,
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        return LLMChain(llm=self.llm, prompt=prompt)
        

        
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

        # Run the chain with the input info
        result = content_chain.invoke({    
            "title": info.get("title"),
            "price": info.get("price"),
            "description": info.get("description"),
            "available_sizes": info.get("available_sizes"),
            "additional_info": info.get("additional_info"),
            "image_description": info.get("image_description"),
        })

        # Return the result in a consistent format
        return {"content": result}

    def apply_tone(self, script, new_target_audience, new_tone, language):
        parser_tone = self.create_tone_parser()
        generation_chain = self.create_script_chain(
            template=GENERATE_REFINED_INFO,
            parser=parser_tone,
            input_variables=["script", "new_target_audience", "new_tone", "language"],
        )
        return generation_chain.invoke({
            "previous_script": script,
            "new_target_audience": new_target_audience,
            "new_tone": new_tone,
            "language": language,
        })
        

    def generate_content(self, metadata, new_target_audience, new_tone, language):
        generated_text = self.generate_text(metadata)
        return self.apply_tone(
            script=generated_text["content"],
            new_target_audience=new_target_audience,
            new_tone=new_tone,
            language=language,
        )
        