#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: testtree.py
@time: 2018/8/28 19:36
@desc:
# '''
# dic = {"baseData": [{ "expand": "true","title": 'parent 1',"children":
#     [{"title": 'parent 1-0',"expand": "true","disabled": "true",
#     "children": [{"title": 'leaf',"disableCheckbox": "true" }, {"title": 'leaf',}]
#     }, {"title": 'parent 1-1', "expand": "true","checked": "true",
#     "children": [{"title": '<span style="color: red">leaf</span>'}]
#         }
#     ]
#                     }]}
#
# print dic["baseData"]

# lis = [{'children': [{'disabled': 'true', 'children': [{'disableCheckbox': 'true', 'title': 'leaf'},
# {'title': 'leaf'}], 'expand': 'true', 'title': 'parent 1-0'}, {'checked': 'true', 'children':
# [{'title': '<span style="color: red">leaf</span>'}], 'expand': 'true', 'title': 'parent 1-1'}],
# 'expand': 'true', 'title': 'parent 1'}]
# print lis[0]
# for key in lis[0]:
#     print key


def add_dic(ls):
    for i in range(len(ls)):
        k = ls[i]
        if k in data:
            l = data[k][:]
            add_dic(l)
            ls[i] = {k:l}


data = {'Tree_root':[1,2,3],
        1:[7,8,9,10],2:[11,12,13],3:[14,15,16],
        7:[99,100,101],8:[102,103,104],9:[105,106,107,108,109]}
nums = data['Tree_root'][:]
print nums
tree = {'Tree':data['Tree_root'][:]}
add_dic(tree['Tree'])

print(tree)

