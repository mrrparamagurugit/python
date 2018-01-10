#!/usr/bin/python3

# GATHER
def sumall(*arg): 
	val=0
	for i in arg:
		val +=i;
	return val;

print(sumall(4,5,6,1,2,3));



#SCATTER
def myprint(arg1,arg2):
	print(arg1,arg2);

li=["hi",[1,2,3]];

myprint(*li)
