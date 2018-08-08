#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 12:04
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : test_sys_stdout.py
# @Software: PyCharm
# @Desc    :
#输出不换行 \r
import sys
import time
if __name__ == '__main__':
    for i in range(1000):
        sys.stdout.write('\ri:{}'.format(i))
        sys.stdout.flush()
        time.sleep(2)