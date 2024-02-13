"""
This script scrapes the prices off of Wizeguy.se & highlights discounted prices.
"""
from bs4 import BeautifulSoup
import requests

URL = "https://www.wizeguy.se/sv/artiklar/airsoft/airsoft-gevr/index.html"

result = requests.get(URL, timeout=5)

soup = BeautifulSoup(result.content, "html.parser")

products = soup.find_all("div", class_="PT_Wrapper left span_3_of_12")

print("\033[1;32mScraping prices from wizeguy.se\033[0m")

for product in products:
    product_name = product.find("div", class_="PT_Beskr").text
    product_pris = product.find("div", class_="PT_Pris col span_7_of_12")

    discount = product.find(class_="PT_PrisKampanj")

    if discount:
        print(product_name, "-", discount.text, "\033[1;32m REA!\033[0m")
    else:
        print(product_name, "-", product_pris.text.strip())
