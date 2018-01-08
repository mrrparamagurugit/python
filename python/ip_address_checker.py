#!/usr/bin/python3

def ip_address_checker(val):
	words=val.split(".")
	for word in words:
		if(int(word)>255 or int(word)<=0):
			return -1
	return 0


print(ip_address_checker("192.168.71.256"))
