# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:34:49 2018

@author: lukep
"""

input_file=open("input","r")
lines=input_file.read().split("\n")
lines.remove("")

for x in range(len(lines)):
    for y in range(len(lines)):
        if x>y:
            word1=lines[x]
            word2=lines[y]
            if(word1!= word2):
                pos=[]
                for i in range(len(word1)):
                    if(word1[i] != word2[i]):
                            pos.append(i)
                if(len(pos) == 1):
                    newStr=word1.replace(word1[pos[0]],"")
                    print(newStr)
                    
                        
        
        
        
        