from bs4 import BeautifulSoup
import requests
import unicodedata

rillatest = requests.get('https://www.serebii.net/pokedex-swsh/', auth=('user', 'pass'))

soup = BeautifulSoup(rillatest.text, features="html.parser")
#print(r.text)
print(soup.title)
list1 = []
list1 = (soup.findAll("select"))
n = 0
names = []
#print(soup.findAll("select"))
#print(soup)
for j in list1:
    for g in j:
        d = str(g)
        sl = str(g)[29:]
       # print(d[29:29 + int(sl.find("/"))])
        if str(d[29:29 + int(sl.find("/"))]) not in names:
            names.append(str(d[29:29 + int(sl.find("/"))]))

    #i = str(j)
    #stri = i[28:]
    #print(j)



rillatest2 = requests.get('https://www.serebii.net/pokedex-sm/', auth=('user', 'pass'))
soup2 = BeautifulSoup(rillatest2.text, features="html.parser")
list2 = []
list2 = (soup2.findAll("select"))
n = 0
#print(soup.findAll("select"))
#print(soup)
for j in list2:
    for g in j:
        d = str(g)
        sl = str(g)[39:]
        #print(str(d))
        try:
            #print(d[38:38 + (int(sl.find("<"))+1)])
            if str(d[38:38 + (int(sl.find("<"))+1)]) not in names:
                #names.append(str(d[38:38 + (int(sl.find("<"))+1)]))
                names.append(str(d[38:38 + (int(sl.find("<"))+1)]))
        #unicodedata.normalize('NFKD', d[38:38 + (int(sl.find("<"))+1)]).encode('ascii', 'ignore')
        #print(d[38:38 + (int(sl.find("<"))+1)].encode('utf8'))
        except:
            #print(unicodedata.normalize('NFKD', d[38:38 + (int(sl.find("<"))+1)]).encode('ascii', 'ignore'))
            if str(unicodedata.normalize('NFKD', d[38:38 + (int(sl.find("<"))+1)]).encode('ascii', 'ignore')) not in names:
                #names.append(str(d[38:38 + (int(sl.find("<"))+1)]))
                names.append(unicodedata.normalize('NFKD', d[38:38 + (int(sl.find("<"))+1)]).encode('ascii', 'ignore'))
#\xe2\x99\x80
#\xe2\x99\x82
for name in names:
    #if name.__contains__(" "):
    if name:
        if name[0] == "1" or  name[0] == "2" or  name[0] == "3" or  name[0] == "4" or  name[0] == "5" or  name[0] == "6" or  name[0] == "7" or  name[0] == "8" or  name[0] == "9" or  name[0] == "0":       
            name = name[4:]
            if name in names:
                names.remove(name)
    #print(name.encode('utf8'))
    #print(name)

    #print(n)
for name in names:
    if name[0] == " ":
        names.remove(name)
        name = name[1:]
        names.append(name)


names2 = []
for name in names:
    if name not in names2:
        names2.append(name)
        print(name)
        n += 1
print( n , " names")
    #print("ENDDDD\n")
    #print(i[28:i.find("/")])
    #n += 1
print(n)

t = " aa"
if (t[0] == " "):
    print(t[1:])