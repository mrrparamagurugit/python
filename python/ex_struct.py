#!/usr/bin/python3

import struct as s


inputs=input("enter:")

packed = s.pack("H6s",0,inputs.encode('ascii'))
#packed = s.pack("Hp",0,"hello")
print(packed)

value,stringu = s.unpack("H6s",packed)
print(value,stringu)
#print(dir(struct))
