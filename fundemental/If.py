#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = int(raw_input("please input an integer:"))

# 单分支的条件判断。
if x > 0:
    print x

# 双分支的条件判断。
if x > 0:
    print x
else:
    print x * 2

# 多分支的条件判断。
if x < 0:
    x = 0
    print "Negative changed to zero"
elif x == 0:
    print "zero"
elif x == 1:
    print "Single"
else:
    print "more"
