#!/usr/bin/python3

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

import cgi
import subprocess
import os

f=cgi.FieldStorage()  
coname = f.getvalue("coname")
osname= f.getvalue("osname")

#cmd= "sudo docker run -dit --name {0} {1}".format(coname,osname)
cmd = f"sudo docker run -dit --name {coname} {osname}"

output=subprocess.getoutput(cmd) 
    
print(output)



