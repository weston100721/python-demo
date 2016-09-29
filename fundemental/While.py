#!/usr/bin/python
# -*- coding: UTF-8 -*-

count = 0
while count < 10:
    print "the value of the count is ", count
    count += 1
print "good bye!"

count = 0
while count < 11:
    count += 1
    if count % 2 == 0:
        continue
    print count

i = 0
while i < 10:
    if i > 5:
        break
    else:
        print i
    i += 1

var = 1
while var == 1:
    num = raw_input("please input a number : ")
    print "you entered:", num
    break

print "good bye"

count = 0
while count < 5:
    print count, " is  less than 5"
    count += 1
else:
    print count, " is not less than 5"
