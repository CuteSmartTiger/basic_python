#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 15:22
# @Author  : liuhu
# @File    : conf文件的获取存储.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import ConfigParser

myconfig = r'.\config.conf'
try:
    read_config = ConfigParser.SafeConfigParser()
    read_config.read(myconfig)
    upgraded = read_config.get('conf', 'upgraded')
except Exception as e:
    read_config.set('conf', 'upgraded','2')
    with open(myconfig, 'w') as fw:
        read_config.write(fw)
    # print res
    print str(e)
# print upgraded

