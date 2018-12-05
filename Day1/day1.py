# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:21:34 2018

@author: lukep
"""

input_file = open("input","r")
lines=input_file.read().split("\n")

start=0

for line in lines:
    if(len(line) != 0):
        sign=line[0]
        
        if(sign=='+'):
            start+=int(line[1:])
        else:
            start-=int(line[1:])

print(start)