#!/usr/bin/python3

stringval="""You could create a dictionary with characters as keys and counters as the corresponding 
values. The first time you see a character, you would add an item to the dictionary.
After that you would increment the value of an existing item."""

mydic= {}
#mydic = dict()
for letter in range(len(stringval)):
	if((stringval[letter]>='A' and stringval[letter]<='Z') or (stringval[letter]>='a' and stringval[letter]<='z') ):
		key = chr(ord(stringval[letter]) & 0xDF ) # dont differentiate captial and small letters. treat them both as same.
		if key in mydic:
			mydic[key]= mydic[key] + 1
		else:
			mydic[key]= 1

print(mydic)


#BELOW IN INBUILT METHOD
from collections import Counter
print(Counter(stringval))

