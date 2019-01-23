#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 17:37
# @Author  : liuhu
# @File    : link_mysql.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
#Python2.7

import xlrd
# 导入MySQL驱动
import mysql.connector
# 连接mysql，括号内是服务器地址, 端口号, 用户名，密码，存放数据的数据库
conn = mysql.connector.connect( host='192.168.6.96', port='3306', user='root', password='123123', database='desktop')
cursor = conn.cursor(buffered=True) # Locate the Cursor, all that was required was for buffered to be set to true
#获得表中有多少条数据
sqlcom="select * from user" # SQL command
aa=cursor.execute(sqlcom) # Execute the command
print(aa)
#查询表中数据，并以每行一个元祖打印
rows = cursor.fetchall() #使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
for a in rows:
    print(a)
