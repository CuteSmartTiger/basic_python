#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 10:28
# @Author  : liuhu
# @File    : test_bat.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import os
import time
import subprocess
# res = subprocess.Popen([r'D:\github\basic_python\bat_cmd\test.bat'])
# res = subprocess.Popen([r'D:\github\basic_python\bat_cmd\test.bat'])
res = subprocess.Popen([r'python',r'D:\github\basic_python\bat_cmd\medi.py'])
print res.returncode
# print res.communicate()
# os.system(r'D:\github\basic_python\bat_cmd\test.bat')

