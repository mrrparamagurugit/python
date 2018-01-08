#!/usr/bin/python3
""" this function to check that a string has a specific letter """
def avoider(val):
	user = input("enter the char")
	for temp in val:
		if temp==user:
			return False

	return True

print(avoider("hellloooaa"))

