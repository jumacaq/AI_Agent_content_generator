import requests
from bs4 import BeautifulSoup
from src.image_describer import ImageGridDescriber

url = 'https://www.falabella.com.pe/falabella-pe/product/883158187/Polo-University-Club-Liso-Manga-Corta-100-Algodon/883158198'
class FalabellaScraper:
    def __init__(self, url):
        # Initialize the scraper with the provided URL and set up headers for the request
        self.url = url
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.soup = self._get_soup()

    def _get_soup(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        print(f"⚠️ Failed to fetch page: {response.status_code}")
        return None
        
    def get_product_title(self):
        # Example method for students to follow
        if self.soup:
            title_tag = self.soup.find("h1", class_="jsx-783883818 product-name")
            return title_tag.get_text(strip=True) if title_tag else "Nombre no encontrado"
        return None
      

    def get_product_price(self):
        if self.soup:
            price_tag = self.soup.find('span', class_='copy12 primary senary jsx-2835692965 bold      line-height-29')
            return price_tag.get_text(strip=True) if price_tag else "Precio no encontrado"
        return None
        
    
    def get_image_links(self):
        if self.soup:
            image_tags = self.soup.find_all("img")
            return [
                img.get("src") for img in image_tags
                if img.get("src") and img.get("src").endswith((".jpg", ".jpeg", ".png"))
            ]
        return []
    
    def get_product_specifications(self):
        if not self.soup:
            return {}

    # Optional: check for the presence of the section header
        header = self.soup.select_one('div.mkp-headerContainer span')
        if header:
            print("🔍 Section:", header.text.strip())
        else:
            print("⚠️ 'Especificaciones' header not found")

    # Extract the table rows
        rows = self.soup.select('tr.jsx-960159652')
        specs = {}
        for row in rows:
            name_tag = row.find('td', class_='property-name')
            value_tag = row.find('td', class_='property-value')
            if name_tag and value_tag:
                specs[name_tag.text.strip()] = value_tag.text.strip()

        return specs
      

    def get_additional_info(self):
        if not self.soup:
            return None

        # Try to find the product info container
        info_container = self.soup.select_one('div.fb-product-information__product-information-tab')
    
        if info_container:
        # Extract all visible text, separating with newlines for readability
            text = info_container.get_text(separator='\n', strip=True)
            return text
        else:
            print("⚠️ Additional info container not found.")
        return None
        

    def get_available_sizes(self):
        if not self.soup:
            return None

        size_buttons = self.soup.select('.size-options button')
        sizes = [btn.get_text(separator='\n', strip=True) for btn in size_buttons]

        return sizes if sizes else None
       
    
    def get_image_description(self, image_links):
        if not image_links:
            return None

        describer = ImageGridDescriber()
        concatenated_image = describer.concatenate_images_square(image_links)
        if concatenated_image:
            return describer.get_image_description(concatenated_image)
        return None
    

    def scrape(self):
        image_links = self.get_image_links()
        return {
            "title": self.get_product_title(),
            "price": self.get_product_price(),
            "image_links": image_links,
            "specifications": self.get_product_specifications(),
            "additional_info": self.get_additional_info(),
            "available_sizes": self.get_available_sizes(),
            "image_description": self.get_image_description(image_links),
            "description": self.get_image_description(image_links)
        }
        