from bs4 import BeautifulSoup
import requests

rillatest = requests.get('https://www.serebii.net/pokedex-swsh/', auth=('user', 'pass'))

soup = BeautifulSoup(rillatest.text, features="html.parser")
#print(r.text)
print(soup.title)
list1 = []
list1 = (soup.findAll("select"))
n = 0
#print(soup.findAll("select"))
#print(soup)
for j in list1:
    for g in j:
        d = str(g)
        sl = str(g)[29:]
        print(d[29:29 + int(sl.find("/"))])

        n += 1
    #i = str(j)
    #stri = i[28:]
    #print(j)

    #print("ENDDDD\n")
    #print(i[28:i.find("/")])
    #n += 1
print(n)