from pydantic import BaseModel, Field


class ContentGenerationScript(BaseModel):
    content: str = Field(..., description="Contenido textual del reel")


# TODO: Define the ToneGenerationScript class with a field for the refined content
class ToneGenerationScript(BaseModel):
    pass


# TODO: Define the ContentGeneration class with fields for URL, target audience, tone, and language
class ContentGeneration(BaseModel):
    pass