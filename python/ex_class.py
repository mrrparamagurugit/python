#!/usr/bin/python3

class First:

#	myvar=0;
#	mynewvar=1;
	def __init__(self):
		print("init called");
		self.myvar=0;
		self.mynewvar=1;

	def __add__(self,one):
		print("add called")
		self.myvar=self.myvar+one
		return self.myvar

	def __str__(self):
		return "my first class %d" % (self.myvar)
#	def class_fun(self):
#		print("%2d %2d" %(self.myvar,self.mynewvar))


newobj = First()
secondobj= First()
#newobj.myvar=100
#newobj.mynewvar=200
print(newobj+ secondobj)
