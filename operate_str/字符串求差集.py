#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 14:45
# @Author  : liuhu
# @File    : 字符串求差集.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import re
H = 'liuhu'
L = 'liu'
# res = re.match(L,H)
# print res.group()


tes = iter(H)
for i in range(9):
    print next(tes,'non')