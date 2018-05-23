#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 10:32
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    :
# @File    : rm all file pyc
# @Software: PyCharm
# @Desc    :
import os
dir_name = r'D:\flask'
for a,b,c in os.walk(dir_name):
    for file in c:
        if file.endswith('.pyc'):
            file_path = os.path.join(a,file)
            os.remove(file_path)
            print file_path
