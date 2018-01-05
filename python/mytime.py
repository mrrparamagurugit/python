#!/usr/bin/python3
import time
t=time.time()
days=int(int(t)/(24*60*60))
reminder=int(int(t)%(24*60*60))
hours=int(reminder/3600)
reminder=int(reminder%3600)
mins=int(reminder/60)
reminder=int(reminder%60)
print(days,hours,mins,reminder)
