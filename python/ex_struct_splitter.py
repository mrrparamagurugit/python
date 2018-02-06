#!/usr/bin/python3
import sys

final_res={}

def find_struct_size(alist):
	struct_size=0
	for items in alist:
        	if 'int' in items:
                	struct_size +=4
	        elif 'char' in items:
        	        if '*' in items[1]:
                	        struct_size +=4
                        	#print("yes char pointer")
	                else:
        	                struct_size +=1
        	elif 'float' in items:
                	struct_size +=4
	return struct_size


def find_struct_name(value,pos):
#	print(value,pos)
	if(pos==0): #name is in front	
		res=value.split(' struct ')
		if len(res)>1:
			llist = res[1].split('\n')
			for item in llist:
				if item != '':
					return item
		return None
		
	else: # name is in back
		res = value.split('}')
		print(res)
		return res[1].split(';')[0]
	#print(res[1])
#	return res[1]

def c_struct_splitter(value,result):
	local_result=[]
#	one = value.split('{')
#	print(one)
#	find_struct_name(one[0])	
#	nextitem = one[1].split('}')
	nextitem = value.split('}')
#	print(nextitem)
	then = nextitem[0].split(';')
	#print(then)
	for items in then:
		llist = items.split('\n')
		for item in llist:
			if item != '':
				local_result.append(item)

	for items in local_result:
		result.append(items.split(' '))
		

def new_c_struct_splitter(value,local_result):
#	local_result={}
	one = value.split('{')
	print(one)
	value=0
	for items in one:
		print(items)
		print("---------------")
		#print(value,len(one))
		if ' struct ' in items:
			name = find_struct_name(one[value],0)
			if name==None:
				name = find_struct_name(one[value+1],1)
			local_result[name]= 0
			local=[]
			value +=1
			c_struct_splitter(one[value],local)
			size = find_struct_size(local)
			local_result[name]= size
		elif ' struct' in items:
			print("CATCH")
			print(items.split('struct'))
			if items.split('struct')[1]=='\n':
				name = find_struct_name(one[value+1],1)
				local_result[name]= 0
				local=[]
				value +=1
				c_struct_splitter(one[value],local)
				size = find_struct_size(local)
				local_result[name]= size
		else :
			value +=1

#	result = local_result


fd = open(sys.argv[1],'r')
value = fd.read()
new_c_struct_splitter(value,final_res)
print(final_res)
print(len(final_res))

