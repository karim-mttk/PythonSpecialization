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