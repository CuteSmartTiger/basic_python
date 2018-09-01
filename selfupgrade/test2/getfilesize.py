#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: getfilesize.py
@time: 2018/8/26 13:38
@desc:
'''
with open("key.txt",'r') as f:
    lines = f.read().strip()
    # lines=f.readlines().
    # for line in lines:
    #     if '\n' in line:
    new_line = lines.replace('\n','')
    new_lines = new_line.replace(' ','')
import os
Size_file = os.path.getsize('key.txt')

print new_lines
print len(new_lines)
print Size_file