#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 11:09
# @Author  : liuhu
# @File    : systembit.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import wmi

c = wmi.WMI()
# 获取操作系统版本
for sys in c.Win32_OperatingSystem():
    print "Version:%s" % sys.Caption, "Vernum:%s" % sys.BuildNumber
    print  sys.OSArchitecture  # 系统是32位还是64位的
    print sys.NumberOfProcesses  # 当前系统运行的进程总数