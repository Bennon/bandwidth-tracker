"""
Reversing a string
"""

text = raw_input("Please enter a string: ")
characters = [i for i in text]
reversed_characters=""
for i in range(len(text) - 1, -1, -1):
		reversed_characters += characters[i]
print "Your reversed string is :", reversed_characters
