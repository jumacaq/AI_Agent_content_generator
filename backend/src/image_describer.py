import os
import base64
import requests
import math
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
from src.llm import GroqModelHandler

# Cargar variables del archivo .env
load_dotenv()

class ImageGridDescriber:
    def __init__(self):
        # TODO: Initialize the GroqModelHandler client and load the vision model name from environment variables
        self.client = None
        self.vision_model = None

    @staticmethod
    def encode_image(image: Image.Image) -> str:
        # TODO: Encode an image to a base64 string
        return None

    def concatenate_images_square(self, urls, img_size=(200, 200)):
        # TODO: Concatenate multiple images into a square grid
        return None

    def get_image_description(self, concatenated_image):
        # Example method for students to follow
        base64_image = self.encode_image(concatenated_image)

        completion = self.client.chat.completions.create(
            model=self.vision_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe el producto en la imagen."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
        )

        return completion.choices[0].message.content

