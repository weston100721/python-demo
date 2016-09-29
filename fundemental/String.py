#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1. 双引号中如果有双引号，需要转义（\）.

'''
# 单引号表示字符串。
print 'span eggs'

# 单引号中有单引号的，需要转义。
print 'doesn\'t'

# 单引号中有双引号的，不需要转义。
print '"yes,"  he said'

# 双引号也可以表示字符串。中间有单引号不需要转义。
print "doesn't"

# 双引号中如果有双引号，需要转义。
print "\"yes,\" he said"

# 这种情况尽量避免。
print '"Isn\'t," she said.'

# \n表示换行符。
print 'First line.\nSecond line.'  # \n means newline

# 采用 r'xxx' 表示原生输出，其中所有的转义字符不起作用。
print r'C:\some\name'  # note the r before the quote

print 'C:\some\name'  # here \n means newline!

# 三个双引号也表示字符串，其中的转义字符同样起作用。
print """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

# 在行尾加一个\表示将下一行跟此行连接起来。一般在一行中写不下，或注重格式的时候使用。
print "one line " \
      "one line"

# 字符串能进行加法和乘法，但不能进行减法和除法。
print 3 * 'un' + 'ium'  # 3 times 'un', followed by 'ium'
# print 'uuu' / 'u'
# print 'uuu' - 'u'

# 字符串可以通过空格连接，但是变量不行。
print 'Py' 'thon'
# prefix = 'py'
# prefix 'thon'

# 当将一个长句子分成多个短句时，下面这中方式非常有用。
text = ('Put several strings within parentheses '
        'to have them joined together.')
print text

# 字符串也可以看成是一个character数组，可通过下标索引。
word = 'python'
print word[0]
print word[-3]

# 下标超出范围会出错。
# print word[42]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# 不能对某个字符再赋值，因为字符串是不可变的。
# word[0] = 'J'

# 字符串能切片
print word[0:2]
print word[2:4]
print word[2:]
print word[:4]
print word[-2:]

# 要保证第一个参数表第二个参数小。否则返回为null
print word[-2:-4]

# 做切片的时候，下标超出范围不会报错。
print word[4:42]

'''
    字符串中索引的位置如下：

    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1
'''

# 前面加u表示为Unicode字符串
print u'Hello World !'
print u'Hello\u0020World !'

print ur'Hello\u0020World !'  # u'Hello World !'
print ur'Hello\\u0020World !'  # u'Hello\\\\u0020World !'
print u"abc"  # u'abc'
print str(u"abc")  # 'abc'
print u"äöü"
print unicode('\xc3\xa4\xc3\xb6\xc3\xbc', 'utf-8')

# string中的替换。
print "My name is %s and weight is %d kg!" % ('Weston', 66)

# 赋值的特殊方式。
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

#    +---+---+---+---+---+---+
#    | P | y | t | h | o | n |
#    +---+---+---+---+---+---+
#    0   1   2   3   4   5   6
#   -6  -5  -4  -3  -2  -1
