#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 14:06
# @Author  : liuhu
# @File    : replace_line_break.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

with open(r'test.txt','r') as f:
    # content = f.readlines()
    content = f.read()
    print(content)
    if r'\n' in content:
        print('ok')
        pass