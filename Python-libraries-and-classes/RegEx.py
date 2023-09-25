"""
REGEX RULES:
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""

import re

#Problem 1:
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
#print(y)

#problem 2:
a = 'From stephen.marquard@uct.ac.za Sat Jan  5:0914:16 2008'
b = re.findall('\S+@\S+', a)
#print(b)

#problem 3:

file = open('files/actual_data.txt')
nums = []
for line in file:
    nums.extend(re.findall('[0-9]+', line))

total_sum = sum(map(int, nums))
print(total_sum)
