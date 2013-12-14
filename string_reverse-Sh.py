"""
Reversing a string
"""

text = raw_input("Please enter a string: ")
characters = [i for i in text]

for i in range(len(text)-1, 0):
	print i
	reversed_characters.insert(0, characters[i])

print "Your reversed string is :", characters
