#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 9:36
# @Author  : liuhu
# @File    : module_zipfile.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
# import os
# import zipfile

# target_file = zipfile.ZipFile('./mysql-installer-web-community-5.7.24.0.zip')
# file_name_list = target_file.namelist()
# print file_name_list
# for name in file_name_list:
#     print name, type(name)
#     name_info = target_file.getinfo(name)
#     file_size = name_info.file_size
#     print file_size / (1024 * 1024)
#     file_compress_size = name_info.compress_size
#     print file_compress_size / (1024 * 1024)

import os
import zipfile


def aquire_info_from_zipfile(filepath, size=False):
    file_info = {'name': None, 'size': None}
    if not os.path.exists(filepath):
        return file_info
    if not filepath.endswith('.zip'):
        return file_info
    target_file = zipfile.ZipFile(filepath)
    file_name_list = target_file.namelist()
    if len(file_name_list) == 1:
        file_info['name'] = file_name_list[0]
        if size:
            file_size = target_file.getinfo(file_info['name']).file_size / (1024 * 1024)
            file_info['size'] = file_size
    return file_info
