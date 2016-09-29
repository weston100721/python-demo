#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字典的定义，可以看作一个映射表。
tel = {'jack': 4098, 'sape': 4139}
var2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
var3 = {x: x**2 for x in (2, 4, 6)}
var4 = dict(sape=4139, guido=4127, jack=4098)

# 字典的增删改查
tel['guido'] = 4127
del tel['sape']
tel['jack'] = 41327
var = tel['jack']

# 获取所有的key。
tel.keys()
'guido' in tel


