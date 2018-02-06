#!/usr/bin/python3

import socket as s

RTM_NEWLINK = 17

fd = s.socket(s.AF_NETLINK,s.SOCK_RAW,s.NETLINK_ROUTE)

fd.bind((s.AF_NETLINK,RTM_NEWLINK))

pak = fd.recv(1600)
print(pak)
print("helooooooooooo")
