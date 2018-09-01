#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: findfringer.py
@time: 2018/8/15 17:37
@desc:
'''
import os

# 先判断之前的文本在不在，如果在，就删除
if os.path.exists('finger.txt'):
    print "liuhu"

# 逐行读取文本内容：
with open("finger.txt",'r') as f:
    lines=f.readlines()
count_num = 0
host_finger_information = {}
num_modules_information = {}
for line in lines:
    if count_num == 4:
        split_line = line.split(':')
        host_key = split_line[1].strip()
        host_value = split_line[2].strip()
        num_modules_information[host_key] = host_value
    if count_num <= 3:
        split_line = line.split(':')
        host_key = split_line[0].strip()
        host_value = split_line[1][:-1].strip()
        host_finger_information[host_key] = host_value
        count_num+=1

print host_finger_information
import json
print json.dumps(host_finger_information)
print json.dumps(num_modules_information)
        # print line

# with open("finger.txt",'r') as f:
#     line=f.readline()
#     print line

# if 'host_fingerprint'in line:
#     print line.split(":")[1]
license_info_args = {'num modules': '', 'issue_date': '', 'host_fingerprint': ''}
lice= {'issue_to': '','module license expire day': '', 'module name': '', 'module license volume': ''}
license_info_args.update(lice)
print license_info_args
# def genwrate():
#     with open("finger.txt",'r') as f:
#         lines=f.readlines()
#         for line in lines:
#             if 'host_fingerprint' in line:
#                 break
#         print line

    # host_finger_info = line.split(':')
    #
    # if len(host_finger_info)==2:
    #     host_finger=host_finger_info[1]
    #     return host_finger
    # else:
    #     return 'No'

