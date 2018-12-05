# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:34:49 2018

@author: lukep
"""

input_file=open("input","r")
lines=input_file.read().split("\n")

douCount=0
triCount=0

for line in lines:
    if(len(line)!=0):
        letters={}
        contains2=False
        contains3=False
        
        for letter in line:
            if letter in letters:
                val=letters.get(letter)+1
                letters.update({letter:val})
            else:
                letters.update({letter:1})
        
        for let in letters:
            if letters[let]==2:
                contains2=True
            elif letters[let]==3:
                contains3=True
        
        if(contains2):
            douCount+=1
        if(contains3):
            triCount+=1
        
print(douCount * triCount)
        
        
        
        