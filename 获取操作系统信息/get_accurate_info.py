#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 13:08
# @Author  : liuhu
# @File    : get_accurate_info.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import os
import sys
import platform

import os
import sys
import platform


def machine():
    """Return type of machine."""
    if os.name == 'nt' and sys.version_info[:2] < (2, 7):
        return os.environ.get("PROCESSOR_ARCHITEW6432",
                              os.environ.get('PROCESSOR_ARCHITECTURE', ''))
    else:
        return platform.machine()


def os_bits(machine_info):
    """Return bitness of operating system, or None if unknown."""
    machine2bits = {'AMD64': 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
    return machine2bits.get(machine_info, None)


def set_upgrade_package_list():
    '''根据操作系统位数确定对应的下载包'''
    machine_info = machine()
    # 获取操作系统的位数
    byte_num = os_bits(machine_info)
    # agent包安装后会重启，所以必须放在列最后
    if byte_num == 32:
        return ['VDIHelper', 'VDIMonitor32', 'Agent32']
    elif byte_num == 64:
        return ['VDIHelper', 'VDIMonitor64', 'Agent64']
    else:
        return False


if __name__ == '__main__':
    print (set_upgrade_package_list())
    print str(None)
