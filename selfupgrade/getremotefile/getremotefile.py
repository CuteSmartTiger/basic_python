#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: getremotefile.py
@time: 2018/8/21 20:05
@desc:
'''
import os
# 1.拷贝本机/home/administrator/test整个目录至远程主机192.168.1.100的/root目录下
#  -r   代表复制目录
os.system('scp -r /home/administrator/test/ root@192.168.1.100:/root/')

# 2.拷贝单个文件至远程主机
os.system('scp /home/administrator/Desktop/old/driver/test/test.txt root@192.168.1.100:/root/')

#3.3、远程文件/文件夹下载
# 把192.168.62.10上面的/root/文件夹，下载到本地的/home/administrator/Desktop/new/下，使用远程端的root登陆

os.system('scp -r root@192.168.62.10:/root/ /home/administrator/Desktop/new/')
