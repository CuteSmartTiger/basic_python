#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: findzip.py
@time: 2018/8/21 16:41
@desc:
'''

with open("zip",'r') as f:
    content = f.readlines()
    count_nums = 0
    for line in content:
        new_line =  line.split(' ')[0]
        print new_line
        if "zip" == new_line:
            count_nums+=1
            print "zip exist"
print count_nums
if count_nums ==0:
    print "no"
else:
    pass


with open("zip",'r') as f:
    content = f.read().strip()
    print content