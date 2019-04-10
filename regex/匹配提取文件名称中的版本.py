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
filename = 'VDIAgentInstaller_x64_5.1.1.1.zip'
# filename = '5.1.1.1'
# pattern = r'(.*)(([0-9]{1,4}\.){3}[0-9]{1,4})?(.*)'
pattern = r'(.*[-|_])?((([0-9]{1,4}\.){3}[0-9]{1,4}){1})([-|_].*[\.]{1}.*?)'
# pattern = r'(.*[-|_])?((([0-9]{1,4}\.){3}[0-9]{1,4}){1})(.*)'
response = re.match(pattern, filename)


# print response.group(1)
# print response.group(2)
# print response.group(3)
# print response.group(4)
# print response.group(0)


def regex_version(filename):
    '''正则提取版本号'''
    pattern = r'(.*[-|_])?((([0-9]{1,4}\.){3}[0-9]{1,4}){1})([-|_].*)'
    response = re.match(pattern, filename)
    try:
        version = response.group(2)
        print version
    except AttributeError as e:
        return False, None
    else:
        return True, version


print regex_version(filename)


def check_suffix(filename):
    suffix_list = [
        'gz',
        'bz2',
        'zip',
        'tar',
        'tgz',
        'txz',
        '7z',
        'rar',
        'pdf',
        'doc',
        'docx',
        'xlsx',
        'xls',
        'ppt',
        'pptx',
        'exe',
        'EXE']
    try:
        version_split_list = filename.rsplit(".", 1)
    except Exception as e:
        return False
    else:
        if version_split_list[1] in suffix_list:
            return True
        else:
            return False


# print check_suffix(filename)

# version = '5.1.1.1aa'
# def check_verison(version):
#     pattern = r'(([0-9]{1,4}\.){3}[0-9]{1,4}){1}$'
#     response = re.match(pattern, version)
#     try:
#         version = response.group(1)
#     except Exception as e:
#         return False
#     else:
#         return True
#
# print check_verison(version)