from bs4 import BeautifulSoup
import requests
# Mettre l’URL dans une variable :
page = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(page.text, 'html.parser')
# Trouver tous les spans avec la classe text
quote = soup.find_all('span', class_='text')
print(quote)

for q in quote:
    find('span', class_='text').get_text()

# Exercice : afficher séparement (ligne par ligne) les données de la liste (indice : boucle for)
# Exercice : Scraper les données de telle manière à avoir plusieurs listes qui ressemblent à ceci :
# ["Citation", "Auteur", "Tags"]
# Vous pouvez utiliser des listes imbriquées