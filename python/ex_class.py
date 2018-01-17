#!/usr/bin/python3

class First:

#	myvar=0;
#	mynewvar=1;
	def __init__(self):
		print("init called");
		self.myvar=0;
		self.mynewvar=1;

	def __add__(self,one):
		self.myvar=self.myvar+one
		return self.myvar

	def __str__(self):
		print("my first class",self.myvar)
		return self
#	def class_fun(self):
#		print("%2d %2d" %(self.myvar,self.mynewvar))


newobj = First()

#newobj.myvar=100
#newobj.mynewvar=200
print(newobj)
