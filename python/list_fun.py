#!/usr/bin/python3

li = [1,2,3,4,5,6,7,8,1];
vi = ["hello","jjjj"];

def tester():
	global li,vi
	return li,vi
	
tem1,tem2=tester()
print(type(tem1),tem1,type(tem2),tem2)
