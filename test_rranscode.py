#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 16:55
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : test_rranscode.py
# @Software: PyCharm
# @Desc    :
import cProfile
import urllib
def main():


  data = {"name": "王尼玛", "age": "/", "addr": "abcdef"}
  print(urllib.urlencode(data))
  print(urllib.quote("短开衫"))
  print(urllib.unquote("hahaha%E4%BD%A0%E5%A5%BD%E5%95%8A%EF%BC%81"))

if __name__=='__main__':
  main()