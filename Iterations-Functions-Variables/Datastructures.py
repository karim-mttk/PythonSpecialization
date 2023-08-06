#problem 1:
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('.')
num = text[pos:pos+5]
print(float(num))

#problem 2:
fname = input("Enter file name: ")

with open(fname, 'r') as fl:
    content = fl.read()
    content = content.rstrip()

mod_con = content.upper()

print(mod_con)

#problem 3:
def extract(line):
    words = line.split()  # Split the line into individual words
    for word in words:
        try:
            float_num = float(word)  # Attempt to convert each word to a float
            return float_num
        except ValueError:
            pass  # Ignore words that cannot be converted to floats

    return None


fname = input("Enter file name: ")
fh = open(fname)
nums = []
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        nums.append(extract(line))

avg = 0
s = 0
n = len(nums)
for i in nums:
    s += i
avg = round((s / n), 16)

print('Average spam confidence:', avg)

#problem 4:
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
temp = list()
for line in fh:
    line.rstrip()
    temp = line.split()

    for i in temp:
        if i not in lst:
            lst.append(i)

lst.sort()
print(lst)


#problem 5:
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
temp = []
lst = []

for line in fh:
    if line.startswith('From:'):
        temp = line.split()
        email = temp[1]
        #if email not in lst:
        lst.append(email)
        count += 1

for email in lst:
    print(email)

print("There were", count, "lines in the file with From as the first word")

#problem 6:
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
temp = []
lst = []

for line in fh:
    if line.startswith('From '):
        temp = line.split()
        email = temp[1]
        lst.append(email)

counts = {}
for item in lst:
    counts[item] = lst.count(item)

maxValue = max(counts.values())

for k, v in counts.items():
    if v == maxValue:
        print(k, v)

#problem 7:
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

lst = []
hrs = []
for line in fh:
    if line.startswith('From '):
        lst = line.split()
        lst = lst[5]
        hrs.append(lst[:2])

hrs.sort()
dhrs = {}

for item in hrs:
    dhrs[item] = hrs.count(item)

for k, v in dhrs.items():
    print(f"{int(k):02d}", v)


