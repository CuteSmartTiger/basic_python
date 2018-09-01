#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: find_terminal_ip.py
@time: 2018/8/31 19:41
@desc:
'''
with open('liuhu.txt','r') as f:
    info = f.readline().strip()
if "master" in info:
    # master_ip = info.split(':')[1].strip()
    master_ip = info.split(':')
    print master_ip