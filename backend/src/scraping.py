import requests
from bs4 import BeautifulSoup
from src.image_describer import ImageGridDescriber


class FalabellaScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36"
            )
        }
        self.soup = self._get_soup()

    def _get_soup(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(
                f"Error al acceder a la página. Código de estado: {response.status_code}"
            )
            return None

    def get_product_name(self):
        if self.soup:
            name_tag = self.soup.find("h1", class_="jsx-783883818 product-name")
            return name_tag.text.strip() if name_tag else "Nombre no encontrado"
        return None

    def get_product_price(self):
        if self.soup:
            price_tag = self.soup.find(
                "span",
                class_="copy12 primary senary jsx-2835692965 bold line-height-29",
            )
            return price_tag.text.strip() if price_tag else "Precio no disponible"
        return None

    def get_image_links(self):
        if self.soup:
            img_tags = self.soup.select('img[id^="testId-pod-image-"]')
            return [img.get("src") for img in img_tags if img.get("src")]
        return []

    def get_product_specifications(self):
        specs = {}
        if self.soup:
            spec_rows = self.soup.select("table.specification-table tr")
            for row in spec_rows:
                cols = row.find_all("td")
                if len(cols) == 2:
                    specs[cols[0].text.strip()] = cols[1].text.strip()
        return specs if specs else {"Especificaciones": "No disponibles"}

    def get_additional_info(self):
        if self.soup:
            info_tag = self.soup.find("div", class_="fb-product-information-tab__copy")
            return info_tag.text.strip() if info_tag else "Información no disponible"
        return None

    def get_available_sizes(self):
        sizes = []
        if self.soup:
            size_buttons = self.soup.select(
                ".size-options button:not(.size-button-unavailable)"
            )
            sizes = [button.text.strip() for button in size_buttons]
        return sizes if sizes else ["No se encontraron tallas"]

    def get_image_description(self, image_links):
        describer = ImageGridDescriber()
        concatenated_image = describer.concatenate_images_square(image_links)
        return describer.get_image_description(concatenated_image)

    def scrape(self):
        return {
            "title": self.get_product_name(),
            "price": self.get_product_price(),
            "image_description": self.get_image_description(self.get_image_links()),
            "description": self.get_product_specifications(),
            "additional_info": self.get_additional_info(),
            "available_sizes": self.get_available_sizes(),
        }
