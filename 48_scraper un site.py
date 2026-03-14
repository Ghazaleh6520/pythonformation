from bs4 import BeautifulSoup
import requests

# URL
page = requests.get('https://quotes.toscrape.com')

# Parse HTML
soup = BeautifulSoup(page.text, 'html.parser')

# Find all quote blocks
quotes = soup.find_all('div', class_='quote')

data = []

for q in quotes:
    citation = q.find('span', class_='text').get_text()
    auteur = q.find('small', class_='author').get_text()
    
    tags_html = q.find_all('a', class_='tag')
    tags = []
    
    for t in tags_html:
        tags.append(t.get_text())

    data.append([citation, auteur, tags])


# Print line by line
for item in data:
    print(item)