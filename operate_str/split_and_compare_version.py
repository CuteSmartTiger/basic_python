#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 14:23
# @Author  : liuhu
# @File    : split_and_compare_version.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


old_version= '3.4.3.0105'
new_version= '3.4.5.0908'
def compare_version(old_version,new_version):
    """
    :param old_version: str,'3.4.3.0105'
    :param new_version:str,'3.4.5.0908'
    :return: if new version bigger than old version,return True ,or False
    """
    old_version_split_list = old_version.strip().split('.')
    print old_version_split_list
    new_version_split_list = new_version.strip().split('.')
    print new_version_split_list
    compare_value_list=zip(new_version_split_list,old_version_split_list)
    print compare_value_list
    for new_value,old_value in compare_value_list:
        if int(new_value) > int(old_value):
            return True
        else:
            continue
    return False

if compare_version(old_version,new_version):
    print 'ok'

