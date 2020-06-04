from bs4 import BeautifulSoup
import requests

rillatest = requests.get('https://serebii.net/pokedex-swsh/rillaboom/', auth=('user', 'pass'))

soup = BeautifulSoup(rillatest.text, features="html.parser")
#print(r.text)
print(soup.title)