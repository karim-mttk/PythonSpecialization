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