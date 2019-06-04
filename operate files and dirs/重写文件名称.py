#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 22:51
# @Author  : liuhu
# @Site    : 
# @File    : 重写文件名称.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import os


def count_time(n):
    print(n)


print('import')


def get_files_name(dir_path):
    print(os.listdir(dir_path))
    return os.listdir(dir_path)


def rename_file(old_file_name, target, new):
    new_name = old_file_name.replace(target, new)
    print(new_name)
    return new_name

target_path = r"C:\Users\45310\Documents\Google资深工程师深度讲解Go语言\第12章 迷宫的广度优先搜索"
# target_path = r"C:\Users\45310\Documents\Google资深工程师深度讲解Go语言\第16章 数据存储和展示"
# target_path = r"C:\Users\45310\Documents\Google资深工程师深度讲解Go语言\第17章 分布式爬虫"
files_list = get_files_name(target_path)
for file_name in files_list:
    new_name = rename_file(file_name, '[www.52studyit.com] ', '')
    os.rename(target_path +"\\"+ file_name, target_path +"\\"+ new_name)
