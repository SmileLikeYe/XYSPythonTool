#!/usr/bin/env python
# coding:utf-8
# @Date    : 2017-01-01 20:38:38
# @Author  : Smile Hu (smile.hu@sap.com)
# @Link    : http://www.smilehu.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# from time import sleep, ctime
# def loop0():
#     print 'start loop 0 at:', ctime()
#     sleep(4)
#     print 'loop 0 done at:', ctime()
#
#
# def loop1():
#     print 'start loop 1 at:', ctime()
#     sleep(2)
#     print 'loop 1 done at:', ctime()
#
#
# def main():
#     print 'starting at:', ctime()
#     loop0()
#     loop1()
#     print 'all DONE at:', ctime()
#
#
# if __name__ == '__main__':
#     main()

from time import sleep, ctime
import thread


def loop0():
    print 'start loop 0 at:', ctime()
    sleep(4)
    print 'loop 0 done at:', ctime()


def loop1():
    print 'start loop 1 at:', ctime()
    sleep(2)
    print 'loop 1 done at:', ctime()


def main():
    print 'starting at:', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()