
#1Basic Web Scraping with BeautifulSoup

import requests
from bs4 import BeautifulSoup

#step1: Send an HTTP request to the website
url="http://quotes.toscrape.com"
response=requests.get(url)

#step2: Parse the HTML content
soup=BeautifulSoup(response.text, "html.parser")

#step3: Extract and print quotes
quotes=soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text) #Extracts and prints each quote