#!/usr/bin/python3

import socket
socketid= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
ip = socket.gethostbyname(host)
host = '10.9.247.226'
print(ip)
host = ip
port = 12346

socketid.bind((host,port))
socketid.listen(3)

while True:
#	print("server running\n")
	clientid,addr=socketid.accept()
#	print("Got a connection from %s" % str(addr))
	print("%s: " % clientid.recv(100).decode('ascii') )
	msg = 'Thank you for connecting'+ "\r\n"
	clientid.send(msg.encode('ascii'))
	clientid.close()


