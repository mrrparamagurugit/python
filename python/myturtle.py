#!/usr/bin/python3

def spiral(val,value):
	val.lt(90)
	while(value>0):
		val.fd(value)
		val.rt(90)
		val.fd(value)
		val.rt(90)
		value = value-10
		val.fd(value)
		val.rt(90)
		val.fd(value)
		val.rt(90)
		value = value-10

def circle(t,r):
	t.pu()
	i=1
	for i in range(360):
		t.rt(1)	
		t.fd(r-1)
		t.pd()
		t.fd(1)
		t.pu()
		t.bk(r)

import turtle
val= turtle.Turtle()
print(val)
#val.lt(90)
#val.fd(100)
#val.rt(90)
#val.fd(100)
#val.rt(90)
#val.fd(100)
#val.rt(90)
#val.fd(100)
#spiral(val,100)
circle(val,50)
#val.bk(200)
turtle.mainloop()

