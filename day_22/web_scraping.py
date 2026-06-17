# Day 22 - Web Scraping in Python
# Web scraping means collecting useful data from web pages.
#
# Common real-world uses:
# - collect product prices
# - collect news headlines
# - collect job listings
# - collect table data
# - monitor website changes
#
# Important:
# Always check a website's rules before scraping.
# Do not overload websites with too many requests.


import csv
import os
import re
from html.parser import HTMLParser


print("Day 22 - Web Scraping")
print("=" * 45)


# 1. What is HTML?
# Websites are made using HTML tags.
# Example:
# <h1>Title</h1>
# <p>Paragraph</p>
# <a href="https://example.com">Link</a>

sample_html = """
<html>
    <head>
        <title>Fresh Mart</title>
    </head>
    <body>
        <h1>Fresh Mart Products</h1>

        <div class="product">
            <h2>Rice</h2>
            <p class="price">1200</p>
            <p class="category">Grocery</p>
        </div>

        <div class="product">
            <h2>Tea</h2>
            <p class="price">250</p>
            <p class="category">Beverage</p>
        </div>

        <div class="product">
            <h2>Keyboard</h2>
            <p class="price">1299</p>
            <p class="category">Electronics</p>
        </div>

        <a href="https://example.com/contact">Contact Us</a>
        <a href="https://example.com/offers">Offers</a>
    </body>
</html>
"""

print("1. Sample HTML loaded")


print("-" * 45)


# 2. Extract title using regex
# This is simple for learning, but real projects usually use BeautifulSoup.
title_match = re.search("<title>(.*?)</title>", sample_html)

print("2. Extract page title")
if title_match:
    print("Page title:", title_match.group(1))


print("-" * 45)


# 3. Extract headings
headings = re.findall("<h2>(.*?)</h2>", sample_html)

print("3. Product headings")
print(headings)


print("-" * 45)


# 4. Extract links
links = re.findall('href="(.*?)"', sample_html)

print("4. Links found")
for link in links:
    print(link)


print("-" * 45)


# 5. Create a small HTML parser
# HTMLParser is built into Python.
# This parser collects product names, prices, and categories.
class ProductHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.products = []
        self.current_tag = ""
        self.current_class = ""
        self.current_product = {}

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_class = ""

        attrs_dict = dict(attrs)

        if tag == "div" and attrs_dict.get("class") == "product":
            self.current_product = {}

        if "class" in attrs_dict:
            self.current_class = attrs_dict["class"]

    def handle_data(self, data):
        clean_data = data.strip()

        if clean_data == "":
            return

        if self.current_tag == "h2":
            self.current_product["name"] = clean_data
        elif self.current_tag == "p" and self.current_class == "price":
            self.current_product["price"] = int(clean_data)
        elif self.current_tag == "p" and self.current_class == "category":
            self.current_product["category"] = clean_data

    def handle_endtag(self, tag):
        if tag == "div" and self.current_product:
            self.products.append(self.current_product)
            self.current_product = {}


parser = ProductHTMLParser()
parser.feed(sample_html)

print("5. Products extracted using HTMLParser")
for product in parser.products:
    print(product)


print("-" * 45)


# 6. Real-world example: find products above a price
expensive_products = []

for product in parser.products:
    if product["price"] >= 1000:
        expensive_products.append(product)

print("6. Products price >= 1000")
for product in expensive_products:
    print(product["name"], "-", product["price"])


print("-" * 45)


# 7. Real-world example: collect unique categories
categories = set()

for product in parser.products:
    categories.add(product["category"])

print("7. Unique categories:", categories)


print("-" * 45)


# 8. Real-world example: save scraped data to CSV
current_folder = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_folder, "scraped_products.csv")

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price", "category"])
    writer.writeheader()
    writer.writerows(parser.products)

print("8. Scraped data saved to:", output_file)


print("-" * 45)


# 9. Read scraped CSV data
print("9. Read scraped CSV data")

with open(output_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


print("-" * 45)


# 10. Real website scraping flow
# For real websites, install these packages:
# python -m pip install requests beautifulsoup4
#
# Example code:
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# title = soup.find("title").text
# print(title)
#
# BeautifulSoup is easier than regex for real HTML.

print("10. Real website scraping usually uses requests and BeautifulSoup")


print("-" * 45)


# 11. Basic scraping steps
scraping_steps = [
    "Choose the website URL",
    "Check if scraping is allowed",
    "Download page HTML",
    "Parse the HTML",
    "Find required tags/classes",
    "Extract clean data",
    "Save data to CSV, JSON, or database",
]

print("11. Basic scraping steps")
for step_number, step in enumerate(scraping_steps, start=1):
    print(step_number, "-", step)


print("-" * 45)


# 12. What should you know about web scraping?
# - Web scraping extracts data from web pages
# - HTML tags contain website content
# - Use requests to download pages
# - Use BeautifulSoup to parse real HTML
# - Use csv/json/file handling to save scraped data
# - Regex can help extract simple patterns
# - Always respect website rules
# - Do not send too many requests quickly
# - Some websites load data using JavaScript, which needs advanced tools
print("12. Summary completed")
