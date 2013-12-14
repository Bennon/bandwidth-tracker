"""
Pig Latin Generator (Single word)
See wikipedia for more information
"""

# List vowels
vowels = 'aeiou'
# Pig latin
pig = 'ay'


# Get user input and convert to lowercase
word = raw_input("Please enter a single word: ").lower()

# If first letter is a vowel, we just add pig latin ('ay') to the end of the word
if word[0] in vowels:
	pigLatin = word + pig
# Otherwise, remove consonant (first letter) from original word, and add
# consonant and pig latin to end of original word.
else:
	# The [1:] prints everything after the first character
	pigLatin = word[1:] + '-' + word[0] + pig

print pigLatin
