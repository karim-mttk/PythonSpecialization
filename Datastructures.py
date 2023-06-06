#problem 1:
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('.')
num = text[pos:pos+5]
print(float(num))

