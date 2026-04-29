
#2Basic Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

#step1: Send an HTTP request to the website
url="https://www.brainyquote.com/topics/quotes"
response=requests.get(url)

#step2: parse the HTML content
soup=BeautifulSoup(response.text, "html.parser")

#step3: Extract and print quotes (adjust based on the site's HTML structure)
quotes=soup.find_all("a", title="view quote") #BrainyQuote uses <a> tags with title="view quote"

for quote in quotes:
    print(quote.text) #Extracts and prints each quote, removing any extra whitespace
    