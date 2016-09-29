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

# 三元操作符。
x = True
e = "x is True."
y = "x is False"
var = x if e else y

# 判断相等 ==
num = 5
if num == 3:  # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'roadman'  # 条件均不成立时输出

# 操作符 >= <= and or
num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print 'hello'
if 0 <= num <= 10:  # 判断值是否在0~10之间
    print 'hello'

if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefined'

num = 8
# 判断值是否在0~5或者10~15之间
# 此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，即大于和小于在没有括号的情况下会比与或要优先判断。
if (0 <= num <= 5) or (10 <= num <= 15):
    print 'hello'
else:
    print 'undefined'

# 操作符：不等于 !=
var = 100
if var != 100:
    print "变量 var 的值为100"
print "Good bye!"

# in 和 not in 操作符。
a = "Hello"
if "H" in a:
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if "M" not in a:
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"
