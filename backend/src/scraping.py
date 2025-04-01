import requests
from bs4 import BeautifulSoup
from src.image_describer import ImageGridDescriber


class FalabellaScraper:
    def __init__(self, url):
        # TODO: Initialize the scraper with the provided URL and set up headers for the request
        self.url = None
        self.headers = None
        self.soup = None

    def _get_soup(self):
        # TODO: Send a GET request to the URL and parse the HTML content using BeautifulSoup
        return None

    def get_product_name(self):
        # Example method for students to follow
        if self.soup:
            name_tag = self.soup.find("h1", class_="jsx-783883818 product-name")
            return name_tag.text.strip() if name_tag else "Nombre no encontrado"
        return None

    def get_product_price(self):
        # TODO: Find and extract the product price from the parsed HTML
        return None

    def get_image_links(self):
        # TODO: Find all image tags and extract their source links
        return []

    def get_product_specifications(self):
        # TODO: Extract product specifications from the HTML table
        return {}

    def get_additional_info(self):
        # TODO: Extract additional product information from the HTML
        return None

    def get_available_sizes(self):
        # TODO: Extract available sizes for the product
        return []

    def get_image_description(self, image_links):
        # TODO: Use the ImageGridDescriber to concatenate images and generate a description
        return None

    def scrape(self):
        # TODO: Scrape all relevant product data and return it as a dictionary
        return {}
