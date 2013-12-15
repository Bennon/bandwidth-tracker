"""
Pig latin generator (multiple words)
Probably need to store each word in an array and modify
in a similar manner to the single-word python script
"""

# List vowels
vowels = 'aeiou'
# Pig latin
pig = 'ay'
# Array to store words
word_list = []
# Counter
count = 0
# Letter storage
letters = []
# Word storage
word = ""

# Get user input and convert to lower case
phrase = raw_input("Please enter a phrase: ").lower()


for i in phrase:
	if i == " ":
		count = count + 1
		for char in letters:
			word += char
		word_list.append(word)
		letters = []
		word = ""
		print i,  count
	else:
		letters.append(i)
		print i,  count
print word_list

