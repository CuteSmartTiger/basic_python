#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 11:06
# @Author  : liuhu
# @File    : 匹配提取文件名称中的版本.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# filename = 'VDIMonitor3454_3.11.1.0308'


import re

# re.match(pattern, string[, flags])




# print re.split(r'-|_',filename)
# res_list = re.split(r'[-|_]', filename)
# print res_list
# for str_info in res_list:
#     res = re.match(pattern, str_info)
#     if res:
#         print res.group(1)
#     # break


# print res.group(1)

# version = '3231.1.1.0308'


# print res.group(1)

# def regx_version(filename):
#     pattern = r'(^([0-9]{1,4}\.){3}[0-9]{1,4}$)'
#     if '-' or "_" in filename:
#         info_list = re.split(r'[-_]', filename)
#         if len(info_list) <= 3:
#             return False
#         for str_info in info_list:
#             res = re.match(pattern, str_info)
#             if res:
#                 return res.group(1)
#     return False
#
#
# print regx_version(filename)
filename = 'VDIAgentInstaller_x64_5.1.1.1-2019011614'
pattern = r'(.*)(([0-9]{1,4}\.){3}[0-9]{1,4})(.*)'
response = re.match(pattern, filename)
print response.group(2)