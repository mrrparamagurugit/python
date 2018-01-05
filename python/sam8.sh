#!/usr/bin/python
import subprocess
listu = [ "ls" , "pwd" , "pwd" ] #"echo helloparam" ]
for it in listu:
#	print it
	subprocess.call(it)
