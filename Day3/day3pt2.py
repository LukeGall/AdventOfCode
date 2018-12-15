# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:06:47 2018

@author: lukep
"""

input_file=open("input.txt","r")
lines=input_file.read().split("\n")
lines.remove("")

squares = [[0 for i in range(1000)] for j in range(1000)]

def readLine(line):
    poss=line[line.find('@')+2:line.find(':')]
    fromLeft,fromTop=poss.split(",")
    
    size=line[line.find(':')+2:]
    wide,tall=size.split('x')
    
    id=line[1:line.find(" ")]
    
    return int(fromLeft),int(fromTop),int(wide),int(tall),int(id)
    

def procLine(fl,ft,w,t,sqs):
    for i in range(w):
        for j in range(t):
            sqs[ft+j][fl+i] = sqs[ft+j][fl+i]+1
            

for line in lines:
    fl,ft,w,t,id=readLine(line)
    procLine(fl,ft,w,t,squares)
    
for line in lines:
    fl,ft,w,t,id=readLine(line)
    sing=True
    for i in range(w):
        for j in range(t):
            if squares[ft+j][fl+i] > 1:
                sing=False
    if sing:
        print(id)
        