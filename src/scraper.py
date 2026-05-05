import os
import csv
import requests
from bs4 import BeautifulSoup

base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "quotes.csv")

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote"])

    for quote in quotes:
        writer.writerow([quote.text])

print("quotes.csv created successfully")