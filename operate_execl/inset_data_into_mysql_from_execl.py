#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 19:00
# @Author  : liuhu
# @File    : inset_data_into_mysql_from_execl.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu
import xlrd
import mysql.connector

# 连接数据库
try:
    conn = mysql.connector.connect(host='192.168.6.96', port='3306', user='root', password='123123', database='desktop')
except:
    print "could not connect to mysql server"



# 打开Excel
execl_file_path = r'./liuhu.xlsx'
def open_excel():
    try:
        book = xlrd.open_workbook(execl_file_path)
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")
        return sheet
    except:
        print("locate worksheet in excel failed!")


def insert_deta():
    sheet = open_excel()
    cursor = conn.cursor(buffered=True)
    row_num = sheet.nrows
    for i in range(1, row_num):
        row_data = sheet.row_values(i)
        value = (row_data[0],row_data[1],row_data[2],row_data[3])
        print(i)
        sql = "INSERT INTO user(name,password,group_id,policy_id)VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, value)
        conn.commit()
    cursor.close()

open_excel()
insert_deta()