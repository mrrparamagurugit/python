#!/usr/bin/python3

dic = {}
i=2;
while i>0:
	i-=1;
	li = [];
	li.append(input("enter first name"))
	print(li)
	li.append(input("enter last name"))
	print(li)
	num=input("enter no")
	tu = tuple(li)
	if tu in dic:
		print("already present")
	else:
		dic[tu]=num

print(dic)
