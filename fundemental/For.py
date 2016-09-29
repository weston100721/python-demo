#!/usr/bin/python
# -*- coding: UTF-8 -*-

words = ['cat', 'window', 'defenestrate', 'window', 'defenestrate']

# for循环的基本操作。
for w in words:
    print w, len(w)

# 这里有一个问题没搞清楚，中间插入一个数据，那他的下标不是变了么？
# 答：原来word[:] 做切片后返回的是一个新的list.
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print 'words=', words

# range(开始下标,结束下标,步进)
print range(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(0, 10, 3)  # [0, 3, 6, 9]
print range(-10, -100, -30)  # [-10, -40, -70]
print range(2, 2)  # []

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

# break语句的使用，只跳出外面一层循环。
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n / x
            break
    else:
        print n, 'is a prime number'

# continue语句的使用
for num in range(2, 10):
    if num % 2 == 0:
        print "Found an even number", num
        continue
    print "Found a number", num


# pass语句的使用。
def initlog(*args):
    pass  # Remember to implement this!
