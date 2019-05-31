#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 12:21
# @Author  : liuhu
# @File    : list差集.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


a=[2,3,4,5]
b=[2,5,8]

print list(set(b).difference(set(a))) # b中有而a中没有的
print list(set(a).difference(set(b))) # a中有而b中没有的