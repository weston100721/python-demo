#!/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep, ctime


def loop0():
    """
    睡眠4秒。
    """
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()


def loop1():
    """
    睡眠2秒。
    """
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()


def main():
    """
这是一个单线程的程序。
    """
    print 'start:', ctime()
    loop0()
    loop1()
    print 'all end:', ctime()


if __name__ == '__main__':
    main()
