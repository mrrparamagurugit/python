#!/usr/bin/python
#import subprocess
#subprocess.call(["ping", "-c 2", "www.cyberciti.biz"])
#subprocess.call(["ssh", "user@10.41.66.22"])

# Import the module
import subprocess

# Ask the user for input
#host = raw_input("Enter a host to ping: ")	

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ssh', 'user@10.41.66.22'], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print output
