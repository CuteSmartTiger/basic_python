#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 15:18
# @Author  : liuhu
# @File    : is_dict_has_key.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
dic = {'name':'liuhu','age':18,'e': 7,'a': 1, 'd': 4,  's': 5,'tes':None}

# 方法一：
test = dict['test'] if dic.has_key('test') else 'hh'
print test

print dic

print '1    '.strip()

print '========================='

# 方法二：
test = dict['test'] if 'test' in dic.keys() else 'hh'
print test

print '========================='


# dict 不能通过getattr来判断是否有key然后赋值
# getattr(dic,'tes','hj')
# getattr(dic,'test','hj')
# print dic