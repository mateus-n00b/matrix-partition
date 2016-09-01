#!/usr/bin/python
from socket import *
import os
import numpy

mA = ""
mB = ""
matrixA = open("/tmp/mA",'w')
matrixB = open("/tmp/mB",'w')


tcp = socket(AF_INET,SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp.bind(('',2222))
tcp.listen(1)
P1 = []
conn, addr = tcp.accept()
arr = 0
arr2 = 0

data = conn.recv(1024)
#tam = int(data.split(':')[0])
mA = data.split(':')[0]
mB = data.split(':')[1]
mA = mA.replace("[", "")
mA = mA.replace("]", "")
mB = mB.replace("[", "")
mB = mB.replace("]", "")

print mA,'\n',mB

matrixA.write(str(mA))
matrixA.close()

matrixB.write(str(mB))
matrixB.close()

mA = [ map(int, line.split()) for line in file('/tmp/mA') if line.strip() ]
mB =   [ map(int, line.split()) for line in file('/tmp/mB') if line.strip() ]

tosend = numpy.dot(mA,mB)
conn.send(str(tosend))


'''for i in range(len(mA)):
    # iterate through columns of B
   for j in range(len(mB[0])):
        # iterate through rows of B	
       for k in range(len(mB)):	    	   	  
            P1[i][j] += arr[i][k] * arr2[k][j]         			   
print P1'''
