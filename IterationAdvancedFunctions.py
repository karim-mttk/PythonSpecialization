#Problem 1:
def check_nums(lst):
    subs = []
    i = 0
    while i < len(lst) and lst[i] != 7:
        subs.append(lst[i])
        i += 1
    return subs

#Problem 2:
def sublist(lst):
    subs = []
    i = 0
    while i < len(lst) and lst[i] != "STOP":
        subs.append(lst[i])
        i += 1
    return subs

#problem 3:
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
i=0
sum2=0
while i < len(lst):
    sum2 += lst[i]
    i+=1

#problem 4:
def beginning(lst):
    subs = []
    i = 0
    while i < 10 and lst[i] != "bye":
        subs.append(lst[i])
        i += 1
    return subs
#problem 5:
def mult(x,y=6):
    return x * y

#problem 6:
def test(x, b=True, dict1={2: 3, 4: 5, 6: 8}):
    keys = dict1.keys()
    if b is True:
        if x in keys:
            return dict1[x]
    else:
        return False

#problem 7:
def checkingIfIn(s, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    keys = d.keys()
    if direction is True:
        if s in keys:
            return True
        else:
            return False
    else:
        if s not in keys:
            return True
        else:
            return False
