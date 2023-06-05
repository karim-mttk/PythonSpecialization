#problem 1
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(",")
#print(rainfall_mi)
num_rainy_months = 0
for i in rainfall_mi:
    if float(i) > 3.0:
        num_rainy_months += 1
#print(num_rainy_months)

#problem 2
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence = sentence.split(" ")
same_letter_count=0
for string in sentence:
    if string[0]==string[-1]:
        same_letter_count += 1
#print(same_letter_count)

#problem 3
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num=0
for item in items:
    if "w" in item:
        acc_num += 1
#print(acc_num)

#problem 4
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence = sentence.split(" ")
num_a_or_e=0
for string in sentence:
    if ("a" in string) or ("e" in string):
        num_a_or_e+=1
#print(num_a_or_e)

#problem 5
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels=0
for i in s:
    if i in vowels:
        num_vowels+=1
#print(num_vowels)

#problem 6
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour:")
rh = float(rate)

if h > 40:
    exh = h - 40
    h = 40
else:
    exh = 0

tot = float((h * rh) + (exh * rh * 1.50))

print(tot)

#problem 7
try:
    score = float(input("Enter Score: "))

    if score >= 0.9 and score <=100:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')

except ValueError:
    print('Invalid input')

#problem 8
def computepay(h, r):
    if h > 40:
        x = h - 40
        h = 40
        return float((h*r) + (x*r*1.5))
    return float(h*r)

h=float(input('Enter hrs:'))
r=float(input('Enter rate:'))

p = computepay(h, r)
print("Pay", p)

#problem 9:
largest = None
smallest = None
lst = []
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        lst.append(int(num))
    except ValueError:
        print('Invalid input')

lst.sort()
print("Maximum is", max(lst))
print("Minimum is", min(lst))
