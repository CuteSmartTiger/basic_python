#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 14:30
# @Author  : liuhu
# @File    : 向不存在的文件写入.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

def mark_information_in_txt(mark_file,value='0'):
    with open(mark_file,'w') as fw:
        res = fw.write(1/0)
        print res
    with open(mark_file,'r') as fr:
        content = fr.read()
        if content == value:
            return True
        else:
            return False


mark_information_in_txt('liuhu.txt','0')

import  os
if os.path.exists('liuhu.txt'):
    print 'lo'