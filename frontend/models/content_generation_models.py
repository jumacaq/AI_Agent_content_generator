from pydantic import BaseModel

class ContentGeneration(BaseModel):
    url: str
    new_target_audience: str
    new_tone: str
    language: str
