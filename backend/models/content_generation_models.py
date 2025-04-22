from pydantic import BaseModel, Field


class ContentGenerationScript(BaseModel):
    content: str = Field(..., description="Contenido textual del reel")


# ✅ Define ToneGenerationScript with refined content
class ToneGenerationScript(BaseModel):
    refined_content: str = Field(..., description="Contenido ajustado con tono y audiencia objetivo")


# ✅ Define ContentGeneration to hold metadata about generation context
class ContentGeneration(BaseModel):
    url: str = Field(..., description="URL del producto")
    target_audience: str = Field(..., description="Audiencia objetivo")
    tone: str = Field(..., description="Tono deseado del contenido")
    language: str = Field(..., description="Idioma del contenido")    


    