#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 10:26
# @Author  : liuhu
# @File    : 获取操作系统信息.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


# os = platform.system()
# print os
# print platform.platform()
# print platform.version()
# print platform.architecture()

import platform
import sys


def set_upgrade_package_list():
    '''根据操作系统位数确定对应的下载包'''
    # 获取操作系统的位数
    byte_num, _ = platform.architecture()
    # agent包安装后会重启，所以必须放在列最后
    print byte_num
    if '32' in byte_num:
        return ['VDIHelper', 'VDIMonitor32', 'Agent32']
    elif '64' in byte_num:
        return ['VDIHelper', 'VDIMonitor64', 'Agent64']
    else:
        return False


if __name__ == '__main__':
    print sys.platform
    print platform.system()
    package_list = set_upgrade_package_list()
    print package_list