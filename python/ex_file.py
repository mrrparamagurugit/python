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
		if(item!=''):
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
	for items in temp_list:
		punc_remover(items,pos+1)


#st=" this is , a string }}}} and it is . needed !\"#$%&\'\()*+,-./:;<=>?@[\\]^_`{|}~ definitely"
#length=len(li)
#print(length)
#punc_remover(st,0)
#li = st.strip().split(li[0])


def task_1():
	fd = open("tmp_read")
	for line in fd:
		punc_remover(line,0)

task_1()
