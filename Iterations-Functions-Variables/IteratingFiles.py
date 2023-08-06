##contains all the code for the Iterating Files part

#problem 1:
with open("school_prompt2.txt", "r") as file:
    text = file.read()
    num_char = len(text)

print(num_char)

#problem 2:
with open("travel_plans2.txt", "r") as file:
    num_lines = len(file.readlines())

print(num_lines)

#problem 3:
with open ("emotion_words2.txt", "r") as file:
    first_forty = file.read(40)
print(first_forty)

#problem 4:
file = open("emotion_words.txt", "r")
num_lines = 0
for aline in file.readlines():
    num_lines += 1

#problem 5:
file_obj = open("squares.txt","w")
for number in range(1, 13):
    square = number * number
    file_obj.write(str(square) +'\n')
    #file_obj.write('\n')
file_obj.close()

new_file = open("squares.txt", "r")
print(new_file.read()[:8])

#problem 6:
with open("emotion_words.txt", "r") as file:
    num_words=0
    text=file.read()
    text=text.split()
    for words in text:
        num_words+=1

#problem 7:
with open("school_prompt.txt", "r") as file:
    text = file.readlines()
    num_lines=len(text)
    print(text)

#problem 8:
with open("school_prompt.txt","r") as file:
    beginning_chars = file.read(30)

#problem 9:
with open("school_prompt.txt") as file:
    lines = file.readlines()
    three = []
    for line in lines:
        words = line.split()
        if len(words) >= 3:
            three.append(words[2])

#problem 10:
with open("emotion_words.txt","r") as file:
    lines = file.readlines()
    emotions = []
    for line in lines:
        word=line.split()
        emotions.append(word[0])

#problem 11:
with open("school_prompt.txt","r") as file:
    text=file.read()
    text=text.split()
    p_words=[]
    for word in text:
        if "p" in word:
            p_words.append(word)

