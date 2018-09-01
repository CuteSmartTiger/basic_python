#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: locals.py
@time: 2018/8/22 10:28
@desc:
'''

from enum import Enum
from flask_babel import lazy_gettext

class Version_Status(Enum):
    no_latest = 0
    latest = 1
Version_Status.latest.label = lazy_gettext("latest")
Version_Status.no_latest.label = lazy_gettext("no latest")

# locals()需要定义到一个函数或者一个类中使用，否则作为全局变
# 量将获取全局变量的信息，然后作为字典返回

def test_locals():
    locals()['Version_Status'] = Version_Status
    print Version_Status.__members__
    dic={}
    for k in locals()['Version_Status'].__members__:
        print k
        dic[k] = locals()['Version_Status'][k].value
    print dic



test_locals()
# result = {}
# results = []
# for k in locals()[].__members__:
#     result['id'] = locals()[][k].value
#     result['name'] = k
#     results.append(result)