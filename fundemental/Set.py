#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 集合的定义和赋值。
s1 = set('abcdefg')
s2 = {3, 5, 9, 10}
s3 = set([3, 5, 9, 10])
s4 = set('hi')
s5 = {i % 2 for i in range(10)}
s6 = set()
s7 = {}

list = [1, 2, 3, 'hello', 'a', 'world']
list_set = set(list)

# set的基本操作
s = {0}
print(s, len(s))  # 获取集合中的元素的总数
s.add("x")  # 添加一个元素
s.update([1, 2, 3])  # 添加多个元素
print(s, "x" in s)  # 成员资格测试
s.remove("x")  # 去掉一个元素
print(s, "x" not in s)
s.discard("x")  # 如果集合存在指定元素，则删除该元素
c = s.copy()  # 复制集合
print(s, s.pop())  # 弹出集合中的一个不确定元素，如果原集合为空则引发 KeyError
s.clear()  # 删除集合中的元素
print(s, c)

# 集合的交集并集等。
a = set('abracadabra')
b = set('alacazam')

var1 = a - b  # letters in a but not in b
var2 = a | b  # letters in either a or b
var3 = a & b  # letters in both a and b
var4 = a ^ b  # letters in a or b but not both

s = set('hi')
t = {'h', 'e', 'l', 'l', 'o'}

print(s.intersection(t), s & t)  # 交集
print(s.union(t), s | t)  # 并集
print(s.difference(t), s - t)  # 差集
print(s.symmetric_difference(t), s ^ t)  # 对称差集
print(s1.issubset(s2), s1 <= s2)  # 子集
print(s1.issuperset(s2), s1 >= s2)  # 包含
