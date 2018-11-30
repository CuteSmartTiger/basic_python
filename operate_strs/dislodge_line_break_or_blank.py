#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 14:06
# @Author  : liuhu
# @File    : dislodge_line_break_or_blank.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

str_list=[]
with open(r'test.txt','r') as f:
    while True:
        # content = f.readline()
        content = f.readline().strip()
        if not content:
            break
        str_list.append(content)
new_contents = ''.join(str_list)
print new_contents

# 输出指定行数的内容
# import linecache
# n_line = linecache.getline('test.txt',2)
# print n_line

