#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print "sys.path's type =", type(sys.path)

sys.path.append("D:\\github-weston\\python-demo\\class")
sys.path.append("D:\\github-weston\\python-demo\\class")

# python 的系统路径。
for s in sys.path:
    print s

# 统计某个值出现的个数。
print sys.path.count("D:\\github-weston\\python-demo\\class")

print sys.path.pop(0)
print sys.path
