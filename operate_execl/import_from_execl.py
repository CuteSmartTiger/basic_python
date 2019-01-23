#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 17:54
# @Author  : liuhu
# @File    : import_from_execl.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

import xlrd
execl_file_path = r'./liuhu.xlsx'
def open_excel():
    try:
        book = xlrd.open_workbook(execl_file_path)  #文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")   #execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")

def insert_deta():
    sheet = open_excel()
    # cursor = db.cursor()
    row_num = sheet.nrows
    for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        row_data = sheet.row_values(i)
        value = (row_data[0],row_data[1],row_data[2])
        print value
        print(i)
        # sql = "INSERT INTO demo_yangben(xxx,xxxx,xxxx,xxxx)VALUES(%s,%s,%s,%s)"
        # cursor.execute(sql, value)  # 执行sql语句
        # db.commit()
    # cursor.close()  # 关闭连接

insert_deta()