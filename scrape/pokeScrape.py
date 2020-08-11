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


"""
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

"""
names2 = []
for name in names:
    if name not in names2:
        n += 1
        if (n != 101 and n > 2 and n != 468 and n != 363 and n != 248 and n != 199 and n != 149):
            if (n < 556):
                names2.append(name)
                #print(name, " ", n)
        
mons = 0
s = ""
for mon in names2:
    mons+=1
    print(mon)
    s = mon
print (s)
url_ = "https://www.serebii.net/pokedex-swsh/" + s + "/"
url_ = "https://www.serebii.net/pokedex-swsh/" + "dreepy" + "/"
print (url_) 
print( mons , " mons")
    #print("ENDDDD\n")
    #print(i[28:i.find("/")])
    #n += 1
print(n)

rillatest2 = requests.get(url_, auth=('user', 'pass'))

soup = BeautifulSoup(rillatest2.text, features="html.parser")
#print(r.text)
print(soup.title)
list1 = []
list1 = (soup.findAll("a"))
#print(soup.encode("utf-8"))
#find type
for a in list1:
    #print(type(a))
    if str(a).find("class=\"typeimg\"") > -1:
        print(a)
        print(str(a)[23:str(a).find(".shtml")])

list2 = []
list2 = (soup.findAll("td"))
#find dex nums
for td in list2:
    #print(td.encode("utf-8"))
    if (str(td).find("<tr><td><b>Galar</b>:")) > -1:
        print("start")
        print(str(td)[str(td).find("#")+1:str(td).find("#") + 4]) # National
        print("end")
        #print(td)
        #Galar
        print(str(td)[str(td).find("#", str(td).find("#")+1)+1:str(td).find("#", str(td).find("#")+1) + 4]) 
        print("last")
        #Isle of armor 
        print(str(td)[str(td).find("#", str(td).find("Isle of Armor"))+1:str(td).find("#", str(td).find("Isle of Armor"))+4])
    
#find abilites
abilites = []
list3 = []
list3 = (soup.findAll("a"))
for a in list3:
    if str(a).find("/abilitydex/") > -1:
        if str(a).find("<b>") > -1:
            #print(str(a)[str(a).find("<b>") +3: str(a).find("</b>")])
            if str(a)[str(a).find("<b>") +3: str(a).find("</b>")] not in abilites:
                abilites.append(str(a)[str(a).find("<b>") +3: str(a).find("</b>")])
for ab in abilites:
    print(ab)

#find stats
stats = []
list4 = []
list4 = (soup.findAll("td"))
stat = 0
for td in list4:
    if str(td).find("Base Stats - Total:") > -1:
        stat = 1
    if stat > 0:
        stats.append(str(td)[str(td).find(">")+1:str(td).find("</")])
        stat += 1
    if stat == 8:
        stat = 0

for s in stats:
    print(s)
    

        