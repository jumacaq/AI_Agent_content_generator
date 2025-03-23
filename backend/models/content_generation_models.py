from pydantic import BaseModel, Field

class ContentGenerationScript(BaseModel):
    content: str = Field(..., description="Contenido textual del reel")

class ToneGenerationScript(BaseModel):
    content: str = Field(
        ..., description="Contenido textual del reel con el tono aplicado"
    )

class ContentGeneration(BaseModel):
    url: str
    new_target_audience: str
    new_tone: str
    language: str
