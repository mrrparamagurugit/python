#!/usr/bin/python3

val = 'a',;
val2='b',;
val=val2
print(val,type(val))


def sumall(*arg):
	for i in arg:
		print(i)

sumall(4,5,6,1,2,3)
		
