# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:40:02 2018

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
    
    return int(fromLeft),int(fromTop),int(wide),int(tall)
    

def procLine(fl,ft,w,t,sqs):
    for i in range(w):
        for j in range(t):
            sqs[ft+j][fl+i] = sqs[ft+j][fl+i]+1
            

for line in lines:
    fl,ft,w,t=readLine(line)
    procLine(fl,ft,w,t,squares)
    
counter=0

for i in range(1000):
    for j in range(1000):
        if squares[i][j] >= 2:
            counter+=1
        
print(counter)