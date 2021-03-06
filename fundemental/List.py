#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import deque

# list的定义与赋值。
squares = [1, 4, 9, 16, 25]
squares1 = [x ** 2 for x in range(10)]

# for循环赋值，采取的格式为[ 表达式 for 变量 in 数组 if 布尔表达式]
vec = [-4, -2, 0, 2, 4]
var = [x * 2 for x in vec]
var = [x for x in vec if x >= 0]
var = [abs(x) for x in vec]

# list 的索引
print squares[0]  # indexing returns the item
print squares[-1]

# list 的切片，其返回结果是一个新的list.
print squares[-3:]
print squares[:]
print squares[3: len(squares)]

# list的拼接。
print squares + [36, 49, 64, 81, 100]

# list的增删改查操作
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7

# list能批量修改或替换。
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']

# list内置的一些非常有用的方法。
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333)
a.insert(2, -1)
print a.index(333)
a.remove(333)
print a.sort()
print a.pop()

# list可以当作堆栈来用。
stack = [3, 4, 5]
stack.pop()
stack.append(6)
stack.append(7)
stack.pop()
print stack

# 将list变成一个队列来用

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
print queue.popleft()  # The first to arrive now leaves
print queue.popleft()  # The second to arrive now leaves