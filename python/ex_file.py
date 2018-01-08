#!/usr/bin/python3

fd = open("tmp_read")
for line in fd:
	word= line.strip().split()
	for let in word:
		if(len(let)>10):
			print(let)				

