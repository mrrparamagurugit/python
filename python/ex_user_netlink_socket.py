#!/usr/bin/python3

import socket as s

fd = s.socket(s.AF_NETLINK,s.SOCK_DGRAM,23)

print(dir(s))

