#!/usr/bin/python3

def factorial(n):
	if(n==0):
	  return 1
	else :
	  val = factorial(n-1)
	  val = val * n
	  return val	

print(factorial(3))
