#!/usr/bin/python3

bigglobal = []

class First:

	myvar=0;
	mynewvar=1;
	called_count=10
	mylist = []
	mydic= {}
	def __init__(self):
		print("init called");
		self.myvar=0;
		self.mynewvar=1;
		global bigglobal
		bigglobal.append(self)
		self.mylist.append(self)

	def __add__(self,one):
		print(" frist add called")
		self.myvar=self.myvar+one.tempu
		return self.myvar

	def __str__(self):
		return "my first class %d" % (self.myvar)

	def sample_fun(self):
		print("class first")	
		self.called_count+=1

	def __radd__(self,newone):
		print("first radd called")

#	def sample_checker(self,nextclass):
#		print self.sample_fun(self) + nextclass.sample_fun()
#	def class_fun(self):
#		print("%2d %2d" %(self.myvar,self.mynewvar))


class Second:


	def __init__(self):
		print("second init called")
		global bigglobal
		bigglobal.append(self)
		
	called_count=0
	def sample_fun(self,fff):
		print("class second")
		#global called_count
		self.called_count+=1
		fff.sample_fun()

	def __add__(self,one):
                print(" second add called")

	def __radd__(self,newonw):
                print("second radd called")


#	def sample_checker(self,nextclass):
#		print sample_fun() + nextclass.sample_fun()




#newobj = First()
#secondobj= Second()
#secondobj.sample_fun(newobj)#secondobj.sample_checker(newobj)
#secondobj.sample_fun(newobj)
#print(secondobj.called_count)
#print(newobj.called_count)

#print(newobj+secondobj)
#print(secondobj+newobj)
#print(1+newobj)

#print(vars(newobj))

#print(getattr(newobj,'mylist'))

print(bigglobal)
print(globals())
