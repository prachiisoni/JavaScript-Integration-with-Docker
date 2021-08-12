#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess

#cmd = "sudo docker ps"
output = subprocess.getoutput("sudo docker ps")
print(output)

