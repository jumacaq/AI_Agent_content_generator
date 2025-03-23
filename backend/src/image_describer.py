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
        self.client = GroqModelHandler().get_client()
        self.vision_model = os.getenv("VISION_MODEL_NAME")

    @staticmethod
    def encode_image(image: Image.Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")

    def concatenate_images_square(self, urls, img_size=(200, 200)):
        images = [
            Image.open(BytesIO(requests.get(url).content)).resize(img_size)
            for url in urls
        ]

        grid_size = math.ceil(math.sqrt(len(images)))
        concatenated_image = Image.new(
            "RGB", (grid_size * img_size[0], grid_size * img_size[1])
        )

        for i, img in enumerate(images):
            concatenated_image.paste(
                img, ((i % grid_size) * img_size[0], (i // grid_size) * img_size[1])
            )

        return concatenated_image

    def get_image_description(self, concatenated_image):
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

