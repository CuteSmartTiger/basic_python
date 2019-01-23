#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 13:57
# @Author  : liuhu
# @File    : read_conf.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import ConfigParser

read_config = ConfigParser.SafeConfigParser()
read_config.read('mtr.conf')
print read_config.get('mtr','max_loss')
print read_config.get('mtr','max_delay')