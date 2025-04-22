import os
import base64
import requests
import math
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
from src.llm import GroqModelHandler
from math import ceil, sqrt

# Cargar variables del archivo .env
load_dotenv()

class ImageGridDescriber:
    def __init__(self):
        # TODO: Initialize the GroqModelHandler client and load the vision model name from environment variables
        self.client = GroqModelHandler().get_client()
        self.vision_model = os.getenv("VISION_MODEL_NAME")

    @staticmethod
    def encode_image(image: Image.Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
        

    def concatenate_images_square(self, urls, img_size=(200, 200)):
        images = []# Download and resize all images
        for url in urls:
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content)).convert("RGB")
                img = img.resize(img_size)
                images.append(img)
            except Exception as e:
                print(f"⚠️ Error loading image from {url}: {e}")

        if not images:
            print("❌ No valid images to display.")
            return None

    # Calculate grid size
        num_images = len(images)
        grid_size = ceil(sqrt(num_images))  # e.g., 5 images → 3x3 grid

    # Create a blank white image to paste all others into
        grid_img = Image.new('RGB', (img_size[0]*grid_size, img_size[1]*grid_size), 'white')

        for idx, img in enumerate(images):
            row = idx // grid_size
            col = idx % grid_size
            x = col * img_size[0]
            y = row * img_size[1]
            grid_img.paste(img, (x, y))

        return grid_img

        
        

    def get_image_description(self, concatenated_image): 
        base64_image = self.encode_image(concatenated_image)

        completion = self.client.chat.completions.create(
            model=self.vision_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe detalladamente la ropa de la persona que ves en la imagen,resaltando sus caracteristicas"},
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
   