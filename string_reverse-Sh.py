"""
Reversing a string
"""

text_length = 0
text_reverse = ""
text = raw_input("Please enter a string: ")
print "Your entered string is: ", text

text_length = len(text)	

for i in range(text_length-1, 0):
	text_reverse + text(i)

print "Your reversed string is :", text_reverse
