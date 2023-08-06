#json loads and dumps:

#json.loads()
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

#json.dumps()
import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))

#nested iteration

L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'],
     ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for i in L:
    for j in i:
        if "b" in j:
            b_strings.append(j)

#deep_copy & shallow copy:
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)

#extracting from nexted loops:
import json
# print(type(res))
# print(res.keys())
res2 = res['statuses']
#print("----Level 2: a list of tweets-----")
#print(type(res2)) # it's a list!
#print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2:
   #print("----Level 3: a tweet----")
   #print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   #print("----Level 4: the user who wrote the tweet----")
   #print(type(res4)) # it's a dictionary
   #print(res4.keys())
   print(res4['screen_name'], res4['created_at'])

#problem 1:

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

# Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
for i in lst:
    for j in i:
        if "yellow" == j:
            yellow = True

# Test to see if 4 is in the second list of lst. Save to variable ``four``
for i in lst:
    for j in i:
        if 4 == j:
            four = True
        else:
            four = False

        # Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
for i in lst:
    for j in i:
        if "orange" == j:
            orange = True

#problem 2:
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for i in L:
    if "hola" == i:
        test1 = True
    else:
        test1 = False
# Test if [5, 8, 7] is in the list L. Save to variable name test2
for i in L:
    if i == [5, 8, 7]:
        test2 = True
# Test if 6.6 is in the third element of list L. Save to variable name test3
for i in L:
    for j in i:
        if j == 6.6:
            test3= True

#problem 3:
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women'][:]
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][-1]

#problem 4:

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = [nested_d['Beijing']['USA'], nested_d['London']['USA'], nested_d['Rio']['USA']]


#problem 5:
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third=[]
for i in l_of_l:
    third.append(i[2])

#problem 6:
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []

for lst in athletes:
    for name in lst:
        if 't' in name:
            t.append(name)
        elif 't' not in name:
            other.append(name)


