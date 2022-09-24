from dataclasses import dataclass
import requests as requests
from html import unescape
from typing import List
import unicodedata
import yaml


@dataclass
class Product:
    product_page_url: str
    text_to_check: str
    should_contain_text: bool


def get_products_from_yaml() -> List[Product]:
    with open("configuration.yaml", "r") as stream:
        yaml_data = yaml.safe_load(stream)
        raw_products = yaml_data["products"]

        products = []
        for raw_product in raw_products:
            products.append(
                Product(
                    raw_product["product_page_url"],
                    raw_product["text_to_check"],
                    bool(raw_product["should_contain_text"]),
                )
            )
        return products


def scrape() -> None:
    print("Starting scraping process...")
    products = get_products_from_yaml()
    for index, product_to_check in enumerate(products):
        print(f"\nChecking {index + 1}. product...")
        response = requests.get(product_to_check.product_page_url)
        page_content = response.text
        page_content = unescape(page_content)
        page_content = unicodedata.normalize('NFKC', page_content)

        if not product_to_check.should_contain_text and product_to_check.text_to_check not in page_content:
            print(f"\t-> AVAILABLE!!! Go get it: {product_to_check.product_page_url}")
            continue

        if product_to_check.should_contain_text and product_to_check.text_to_check in page_content:
            print(f"\t-> AVAILABLE!!! Go get it: {product_to_check.product_page_url}")
            continue

        print("\t-> Not available")


scrape()
