#!/usr/bin/python3

import socket

clientid=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = socket.gethostname()                           
host = '10.0.2.15'
port = 12346

clientid.connect((host,port))

chat=input(":")
clientid.send(chat.encode('ascii'))

msg=clientid.recv(1000)

clientid.close()

print(msg.decode('ascii'))
