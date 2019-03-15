#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 10:08
# @Author  : liuhu
# @File    : yield_list.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

lis= [1,2,3,4,5,6,7]
def iter_li(ob):
    for i in ob:
        yield i

# for n in iter_li(lis):
#     print n
print next(iter_li(lis))

