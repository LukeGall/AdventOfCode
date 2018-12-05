# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:21:34 2018

@author: lukep
"""

input_file = open("input","r")
lines=input_file.read().split("\n")

cur=0
twice=0
listOfValues={}

while twice==0:
    for line in lines:
        if(len(line) != 0):
            sign=line[0]
            
            if(sign=='+'):
                cur+=int(line[1:])
                
                if(cur in listOfValues):
                    val=int(listOfValues.get(cur))
                    listOfValues.update({cur:val+1})
                    
                    if(listOfValues[cur] >=2):
                        twice=cur
                        break
                else:
                    listOfValues.update({cur:1})
                
            else:
                cur-=int(line[1:])
                if(cur in listOfValues):
                    val=listOfValues.get(cur)
                    listOfValues.update({cur:val+1})
                    if(listOfValues[cur] >=2):
                        twice=cur
                        break
                else:
                    listOfValues.update({cur:1})


print(twice)