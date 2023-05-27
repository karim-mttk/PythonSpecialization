#Problem 1:
def total (l):
    tot=0
    for nums in l:
        tot+=nums
    return tot

#Problem 2:
def count(l):
    c=0
    for n in l:
        c+=1
    return c

#Problem 3:
def divide(n):
    return n//2

def sum(n):
    return divide(n) + 6

#problem 4:
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names=[]
p_number=[]
for i, j in pokemon.items():
    p_names.append(i)
    p_number.append(j)

#problem 5:

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events=[]
for i, j in track_medal_counts.items():
    track_events.append(i)

#problem 6:
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for i,j in gold.items():
    num_medals.append(j)