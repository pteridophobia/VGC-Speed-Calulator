from bs4 import BeautifulSoup
import requests

rillatest = requests.get('https://www.serebii.net/pokedex-swsh/', auth=('user', 'pass'))

soup = BeautifulSoup(rillatest.text, features="html.parser")
#print(r.text)
print(soup.title)
print(soup.find("select"))
#print(soup)