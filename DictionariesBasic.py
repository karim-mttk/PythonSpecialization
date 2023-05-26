#problem 1:
olympics={'gold':7,'silver':8,'bronze':6}

#problem 2:
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016

#problem 3:
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps']= swimmers['Phelps'] + 5

#problem 4:
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds['Spain']=golds['Spain'] + 2

#problem 5:
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries=[]
for con in golds:
    countries.append(con)

#problem 6:
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total=0
for c in travel:
    travel[c]
    total+=travel[c]

#problem 7:
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
min_value=0
for c in placement:
    if c not in d:
        d[c]=0
    d[c]+=1
keys = list(d.keys())
min_value = keys[0]
for key in keys:
    if d[key] < d[min_value]:
        min_value = key

#problem 8:
product = "iphone and android phones"
lett_d ={}
for p in product:
    if p not in lett_d:
        lett_d[p] = 0
    lett_d[p] += 1
keys = list(lett_d.keys())
max_value = 0
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

#problem 9:
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for c in Junior:
    credits += Junior[c]

#problem 10:
str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for s in str1:
    if s not in freq:
        freq[s] = 0
    freq[s] += 1

#problem 11:
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
str1 = str1.split()
freq_words = {}
for s in str1:
    if s not in freq_words:
        freq_words[s]=0
    freq_words[s]+=1

#problem 12:
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
sent=sent.split()
for s in sent:
    if s not in wrd_d:
        wrd_d[s]=0
    wrd_d[s]+=1

#problem 13:
sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for c in sally:
    if c not in characters:
        characters[c]=0
    characters[c]+=1
worst_char=sally[0]
keys=list(characters.keys())
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char=key