from pydantic import BaseModel,Field


class ContentGeneration(BaseModel):
    url: str = Field(..., description="URL del producto") # Example field for students to follow

    target_audience: str = Field(..., description="Nuevo público objetivo")  #field for the new target audience
    tone: str = Field(..., description="Tono del contenido") #field for the new tone
    language: str = Field(..., description="Idioma del contenido")  #field for the language
    