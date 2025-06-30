import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")
with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Availability"])
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()
        writer.writerow([title, price, availability])
