#Problem 1
addition_str = "2+5+10+20"
addition_list = addition_str.split("+")
#print(addition_list)

sum_val = 0
for i in addition_list:
    sum_val += int(i)
#print(sum_val)

#Problem 2
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
#print(week_temps_f)

avg_temp = 0

for i in week_temps_f:
    avg_temp += float(i)
avg_temp = avg_temp/len(week_temps_f)
#print(avg_temp)

#Problem 3
nums = []
for i in range(0,68):
    nums = nums + [i]
#print(nums)

#Problem 4
original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []

words = original_str.split()
for word in words:
    num_words_list.append(len(word))

#print(num_words_list)

#Problem 5
lett = ""
for i in range(0,7):
    lett += ("b")
print(lett)

