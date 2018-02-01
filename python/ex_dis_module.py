#!/usr/bin/python3

import dis


def my_fun():
	aa=10
	bb=20
	aa= aa+bb
#	bb =aa
	print(aa,bb)



print(my_fun.__code__.co_consts)

for ch in my_fun.__code__.co_code:
	if(ch>99):
		print(ch,dis.opname[ch])
	else:
		print(ch)

print(my_fun.__code__.co_varnames)

my_fun()
dis.dis(my_fun)


#for ch in my_fun.__code__.co_varnames:
#	print(ch)
