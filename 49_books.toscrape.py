# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

# URL
url = "https://books.toscrape.com/"

# requête HTTP
page = requests.get(url)

# s'assurer que la page est lue en UTF-8
page.encoding = "utf-8"

# parser le HTML
soup = BeautifulSoup(page.text, "html.parser")

# trouver tous les livres
books = soup.find_all("article", class_="product_pod")

data = []

for book in books:

    # récupérer le titre
    title = book.h3.a["title"]

    # récupérer le prix
    price = book.find("p", class_="price_color").get_text()

    # récupérer les étoiles
    stars = book.find("p", class_="star-rating")["class"][1]

    # ajouter les infos dans une liste
    data.append([title, price, stars])

# afficher les résultats
for item in data:
    print(item)