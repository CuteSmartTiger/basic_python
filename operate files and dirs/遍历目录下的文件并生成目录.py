#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 17:06
# @Author  : liuhu
# @Site    : 
# @File    : 遍历目录下的文件并生成目录.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import os


def write_content(title, filename='目录.txt'):
    '''向file中写入标题'''
    with open('{0}'.format(filename), 'a+',encoding='utf-8') as f:
        f.write(title+'\n')


import re


def get_chapter(title):
    try:
        chapter = re.match(r'第([0-9]{1,2})(章.*)', title).group(1)
    except Exception as e:
        pass
    else:
        return int(chapter)


def generate_catalog(dir_path):
    '''输入文件路径，遍历文件目录'''
    dir_and_file_list = os.listdir(dir_path)
    # print(dir_and_file_list)
    # dir_and_file_list = sorted(os.listdir(dir_path), key=lambda x: get_chapter(x))
    # print(dir_and_file_list)
    depth = 0
    for dir_or_file in dir_and_file_list:
        dir_or_file_path = os.path.join(dir_path, dir_or_file)
        if os.path.isdir(dir_or_file_path):
            if len(dir_and_file_list) != 1:
                print(depth * ' ' + dir_or_file)
                # write_content(dir_or_file,filename='1.txt')
            generate_catalog(dir_or_file_path)
        else:
            if '.mp4' in dir_or_file:
                print(depth * ' ' + dir_or_file)
                # write_content(dir_or_file,filename='1.txt')
            else:
                continue


# dir_path = r'C:\Users\45310\Downloads\Selenium3 与 Python3 实战 Web自动化测试框架'
# dir_path = r'C:\Users\45310\Documents\1 微服务架构核心20讲'
dir_path = r'C:\Users\45310\Downloads\Selenium3 与 Python3 实战 Web自动化测试框架'
generate_catalog(dir_path)
