#!/usr/bin/python
#-*- coding:UTF-8 -*-
import numpy as np
import os,sys
import random
from socket import *
tcp = socket(AF_INET,SOCK_STREAM)
tcp.connect(('localhost',2222))
res = open("/tmp/res",'w')
bob = open("/tmp/out",'w')
mA = np.arange(100).reshape(10,10)
mB = mA

#print np.dot(mA[:len(mA), :len(mA)/2],mB[:len(mA)/2, :len(mA)])
print np.dot(mA,mB),'\n\n'

Aum = mA[:len(mA), :len(mA)/2]
Adois = mB[:len(mA)/2, :len(mA)]
Bum = mA[:len(mB), len(mA)/2:len(mA)]
Bdois = mB[len(mB)/2:len(mB), :len(mB)]

Cdois = np.dot(Bum,Bdois)

# -==================================== RECEIVER ====================================-  
tcp.send("%s : %s" % (Aum,Adois))
msg = tcp.recv(1050)
msg = msg.replace(".","")
msg = msg.replace("[", "")
msg = msg.replace("]", "")

res.write(msg)
res.close()
CUm = [ map(int, line.split()) for line in file('/tmp/res') if line.strip() ]

print np.add(CUm,Cdois)
# Esta pega as 2 prim col de mA e as 2 prim lin de mB #print mA[:len(mA), :len(mA)/2],'\n',mB[:len(mA)/2, :len(mA)]
# Esta pega as 2 ultimas col de mA e as 2 ult lin de mB#print '\n', mA[:len(mB), len(mA)/2:len(mA)], '\n', mB[len(mB)/2:len(mB), :len(mB)]


'''mA1 = mA[:len(mA)/2, :len(mA)]
mB1 = mB[:len(mB[0]), :len(mB)/2]
mA2 = mA[len(mA)/2:len(mA), :len(mA)] 
mB2 = mB[:len(mB[0]), len(mB)/2:len(mB)]
P1= []
'''       
