#!/usr/bin/python3

import sys

fd= open(sys.argv[1])
#fd= open("/media/sf_Shaed_with_ubuntu/snip.txt")
basefile = sys.argv[1].split("/")
basefilelen = len(basefile)
basefile = basefile[basefilelen-1]
value = fd.read()
iterator=1
#li = value.split("Start of SilentDiag")
li = value.split(sys.argv[2])
print(sys.argv[2])
print(sys.argv[3])
ter = li[0].split("\n") 
terlen = len(ter)
header = ter[terlen-1]
for val in li:
#	local_list=val.split("End of SilentDiag")
	local_list=val.split(sys.argv[3])
	if len(local_list)>1:
		filename =  basefile + "_" + str(iterator)
		print(li.index(val))
		newfd=open(filename,"w")
		newfd.write(header + sys.argv[2] + str(local_list[0]) + sys.argv[3])
		ter = val.split("\n")
		terlen = len(ter)
		header = ter[terlen-1]
		iterator=iterator+1

print("count of %s:%d " %  (sys.argv[2] , value.count(sys.argv[2])))
print("count of %s:%d " %  (sys.argv[3] , value.count(sys.argv[3])))


