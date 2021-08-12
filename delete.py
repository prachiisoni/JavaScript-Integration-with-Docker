#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()


f = cgi.FieldStorage()
coname = f.getvalue('n')

cmd = f"sudo docker rm -f {coname}"
op = subprocess.getoutput(cmd)
print(op)


