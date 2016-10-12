#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

readFile = 'testfile/test.txt'
writeFile = 'testfile/writeFile.txt'

f = open(readFile, 'r')
fw = open(writeFile, 'a')
isFirstLine = True
for eachLine in f.readlines():
    if isFirstLine:
        fw.write('\n')
        isFirstLine = False
    fw.write(eachLine)

f.close()
fw.close()

for eachLine in open(writeFile, 'r'):
    print eachLine,
var = os.getcwd()
print
print var
