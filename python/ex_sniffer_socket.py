#!/usr/bin/python3

import socket as s
import binascii
import sys

count=0

def print_packet(pak):
	line=0
	global count
	hexvalue = binascii.hexlify(pak).decode()
	length = len(hexvalue)
	for i in range(0,length,2):
		print(hexvalue[i] + hexvalue[i+1],end=' ')
		#sys.stdout.write( hexvalue[i] + hexvalue[i+1] + ' ' )
		line+=1
		if line%30==0:
			print("\n")
	count +=1
	print("\n count:%d"% count)


ETH_P_ALL = 3 # to receive all packets

fd = s.socket(s.AF_PACKET,s.SOCK_RAW,s.htons(ETH_P_ALL))

while True:
	pak = fd.recv(1600)
	print_packet(pak)
