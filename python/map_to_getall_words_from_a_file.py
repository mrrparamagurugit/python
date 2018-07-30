#!/usr/bin/python3
import sys

fd=open(sys.argv[1],'r')

mapper= map(lambda x: x.split(' ') ,fd.read().split('\n'))
#mapper= map(lambda x: x ,fd.read().split('\n'))

print(list(mapper))
