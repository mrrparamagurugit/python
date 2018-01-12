#!/usr/bin/python3

#fd = open("tmp_read")
#for line in fd:
#	word= line.strip().split()
#	for let in word:
#		if(len(let)>10):
#			print(let)				


import string
punc = string.punctuation
li = list(punc)

white= string.whitespace
white_list=list(white)
white_lenth=len(white_list)
print(white_lenth)
def whitespace_remover(item,pos):
	global white_list
	global white_lenth
	if(pos>(white_lenth-1)):
		print(item)
		return
	temp_list = item.strip().split(white_list[pos])
	for items in temp_list:
		whitespace_remover(items,pos+1)

def punc_remover(item,pos):
	global li
	if(pos>31):
		whitespace_remover(item,0)
		return
	temp_list = item.strip().split(li[pos])
	#print(temp_list)	
	for items in temp_list:
		punc_remover(items,pos+1)


st=" this is , a string }}}} and it is . needed !\"#$%&\'\()*+,-./:;<=>?@[\\]^_`{|}~ definitely"
length=len(li)
print(length)
punc_remover(st,0)
#li = st.strip().split(li[0])


#print(li)



#punc = string.punctuation
#for let in punc:
#	print(let)

#def task_1():
#	fd = open("tmp_read")
#	for line in fd:
#		for one_punc in punc:
#			words=line.strip().split(one_punc)
#		print(one_line)

#task_1()
