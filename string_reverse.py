"""
Reversing a string
"""

string = raw_input("Enter your string here: ")
characters = [c for c in string]

print characters[1]

for i in range(len(characters) / 2):
    characters[i], characters[len(characters) - i - 1] = characters[len(characters) - i - 1], characters[i]

print "Your reversed string is: ", (''.join(characters))


