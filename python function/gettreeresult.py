#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: gettreeresult.py
@time: 2018/8/29 9:13
@desc:
'''
tree = [
    {
        "type": "root",
        "name": "Root",
        "parent": [
            ""
        ],
        "tree_id": "group_root"
    },
    {
        "category": "groups",
        "real": "group_1",
        "checked": "",
        "name": "Default",
        "parent": [
            "group_root"
        ],
        "label": "Default",
        "tree_id": "group_1_leaf",
        "selectable": "",
        "type": "leaf",
        "id": 1,
        "icon": "groups"
    },
    {
        "category": "useless",
        "checked": "",
        "name": "Default",
        "parent": [
            "group_root"
        ],
        "label": "组\"Default\"中的用户",
        "tree_id": "group_1",
        "selectable": "",
        "type": "branch",
        "id": 1
    },
    {
        "category": "users",
        "group": "Default",
        "name": "list4",
        "parent": [
            "group_1"
        ],
        "label": "list4",
        "tree_id": "user_34",
        "policy": "Default",
        "checked": "",
        "type": "leaf",
        "id": 34,
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "aaaaa",
        "parent": [
            "group_1"
        ],
        "label": "aaaaa",
        "tree_id": "user_49",
        "policy": "Default",
        "checked": "",
        "type": "leaf",
        "id": 49,
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "admin1",
        "parent": [
            "group_1"
        ],
        "label": "admin1",
        "tree_id": "user_35",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "35",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "admin5",
        "parent": [
            "group_1"
        ],
        "label": "admin5",
        "tree_id": "user_39",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "39",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "test21",
        "parent": [
            "group_1"
        ],
        "label": "test21",
        "tree_id": "user_46",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "46",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "aaaaaaaa",
        "parent": [
            "group_1"
        ],
        "label": "aaaaaaaa",
        "tree_id": "user_40",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "40",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "admin2",
        "parent": [
            "group_1"
        ],
        "label": "admin2",
        "tree_id": "user_36",
        "policy": "wee33",
        "checked": "false",
        "type": "leaf",
        "id": "36",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "111",
        "parent": [
            "group_1"
        ],
        "label": "111",
        "tree_id": "user_50",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "50",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "aaaasa",
        "parent": [
            "group_1"
        ],
        "label": "aaaasa",
        "tree_id": "user_41",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "41",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "test22",
        "parent": [
            "group_1"
        ],
        "label": "test22",
        "tree_id": "user_47",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "47",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "admin4",
        "parent": [
            "group_1"
        ],
        "label": "admin4",
        "tree_id": "user_38",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "38",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "111111",
        "parent": [
            "group_1"
        ],
        "label": "111111",
        "tree_id": "user_48",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "48",
        "icon": "users"
    },
    {
        "category": "users",
        "group": "Default",
        "name": "list3",
        "parent": [
            "group_1"
        ],
        "label": "list3",
        "tree_id": "user_33",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "33",
        "icon": "users"
    },
    {
        "category": "groups",
        "checked": "false",
        "name": "ssss",
        "parent": [
            "group_root"
        ],
        "label": "ssss",
        "tree_id": "group_10_leaf",
        "selectable": "true",
        "type": "leaf",
        "id": "10",
        "icon": "groups"
    },
    {
        "category": "groups",
        "real": "group_2",
        "checked": "false",
        "name": "test277",
        "parent": [
            "group_root"
        ],
        "label": "test277",
        "tree_id": "group_2_leaf",
        "selectable": "true",
        "type": "leaf",
        "id":"2" ,
        "icon": "groups"
    },
    {
        "category": "useless",
        "checked": "false",
        "name": "test277",
        "parent": [
            "group_root"
        ],
        "label": "组\"test277\"中的用户",
        "tree_id": "group_2",
        "selectable": "true",
        "type": "branch",
        "id": "2"
    },
    {
        "category": "users",
        "group": "test277",
        "name": "admin3",
        "parent": [
            "group_2"
        ],
        "label": "admin3",
        "tree_id": "user_37",
        "policy": "Default",
        "checked": "false",
        "type": "leaf",
        "id": "37",
        "icon": "users"
    }
]
print type(tree)
print len(tree)
for i in tree:
    print i