"""
Pig latin generator (multiple words)
Probably need to store each word in an array and modify
in a similar manner to the single-word python script
"""

vowels = 'aeiou'
pig = 'ay'
count = 0
pigPhrase = []
solution = ""

phrase = raw_input("Please enter a phrase: ").lower()

word_list = phrase.split()

for word in word_list:

	if word[0] in vowels:
		pigLatin = word + pig
		pigPhrase.append(pigLatin)
		count = count + 1
	else:	
		pigLatin = word[1:] + '-' + word[0] + pig
		pigPhrase.append(pigLatin)
		count = count + 1

for i in pigPhrase:
	solution += i + " "

print solution
