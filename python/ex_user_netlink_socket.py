#!/usr/bin/python3

import socket as s

fd = s.socket(s.AF_NETLINK,s.SOCK_DGRAM,23)
#msg = 'Thank you for connecting'+ "\r\n"
chat=input(":")
space=' ' * 16 
new = space + chat #+ '\0'
fd.send(new.encode('ascii'))
 # clientid.send(msg.encode('ascii'))
#print(dir(s))

