#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 9:36
# @Author  : liuhu
# @File    : module_zipfile.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import zipfile

target_file = zipfile.ZipFile('./ll/mysql-installer-web-community-5.7.24.0.zip')
file_name_list=target_file.namelist()
print file_name_list
for name in file_name_list:
    print name,type(name)
    name_info = target_file.getinfo(name)
    file_size = name_info.file_size
    print file_size/(1024*1024)
    file_compress_size = name_info.compress_size
    print file_compress_size/(1024*1024)
