#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 13:12
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : test_retry.py
# @Software: PyCharm
# @Desc    :
from retrying import retry
i=1
def retry_if_io_error(exception):
    return isinstance(exception, ValueError)

def retry_if_http_error(exception):
    return isinstance(exception, IndexError)

@retry(retry_on_exception=retry_if_http_error, wait_fixed=2000)
@retry(retry_on_exception=retry_if_io_error, stop_max_attempt_number=3, wait_fixed=2000)
def test():
    global i
    i+=1
    print i

    if i>2:
        print 'sssss'
        raise IndexError
    else:
        print 'file'
        raise  ValueError
test()