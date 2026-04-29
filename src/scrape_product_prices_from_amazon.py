
#Python Code to Scrape Product Name & Price from Amazon
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Setup ChromeDriver
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

#Open Amazon Product Page
url="https://www.amazon.com/s?k=laptop"
driver.get(url)

#Wait for the page to Load (Important for dynamic elements)
time.sleep(5) #Adjust sleep time if needed

#Extract product titles and prices
titles=driver.find_elements(By.CSS_SELECTOR,"span.a-text-normal")
prices=driver.find_elements(By.CSS_SELECTOR,"span.a-price-whole")

#Print first 5 product details
for i in range(min(5, len(titles))): #Avoid IndexError if fewer results are found
    product_name=titles[i].text.strip()
    product_price=prices[i].text.strip() if i< len(prices) else "N/A"
    print(f"product: {product_name}, Price:${product_price}")


#Close the browser
driver.quit()
