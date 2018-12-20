# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:48:50 2018

@author: lukep
"""

input_file = open("input.txt", "r")
lines = input_file.read().split("\n")
lines.remove("")

lines.sort()


mins = [0]*60
guards = {}

startMin = 0
id = 0
sleepTime = 0
for line in lines:
    min = int(line[line.find(':')+1:line.find(':')+3])
    com = line[line.find(']')+2:]
    if com[0] == 'G':
        id = int(line[line.find('#')+1:line.find('b')-1])
        startMin = 0
        sleepTime = 0
    elif com[0] == 'f':
        startMin = min
    elif com[0] == 'w':
        sleepTime = min-startMin

    if id not in guards.keys():
        guards[id] = 0
    guards[id] += 1

max = 0
gId = 0
for key, val in guards.items():
    if val > max:
        max = val
        gId = key


for line in lines:
    min = int(line[line.find(':')+1:line.find(':')+3])
    com = line[line.find(']')+2:]
    if com[0] == 'G':
        id = int(line[line.find('#')+1:line.find('b')-1])
        startMin = 0
        endTime = 0
    elif com[0] == 'f':
        startMin = min
    elif com[0] == 'w':
        endTime = min

    if id == gId:
        for i in range(startMin, endTime):
            mins[i] += 1

maxMin = 0
minNo = 0
for m in range(60):
    if mins[m] > maxMin:
        maxMin = mins[m]
        minNo = m

print(gId, minNo)

print(gId * minNo)
