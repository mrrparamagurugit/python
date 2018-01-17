#!/usr/bin/python3

import ex_file
import sys

matcher = "read"
replacer = "GANDHI is"
try:
	fd=open("tmp_read").read()
	#print(fd.count(matcher)) to print the count of a certain sub-string in a string
	fd=fd.replace(matcher,replacer)
	open("TTT","w").write(fd)
except Exception as e:
	print("error in opening")
	print(e)
	exit(0)
