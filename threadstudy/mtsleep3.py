#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    # 创建线程
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # 开始线程
    for i in nloops:
        threads[i].start()

    # 等待所有结束线程
    for i in nloops:
        threads[i].join()

    print 'all end:', ctime()


if __name__ == '__main__':
    main()
