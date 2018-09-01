#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: about_log.py
@time: 2018/9/1 16:38
@desc:
'''
# 目的：将日常的日志输出到屏幕及指定的文件里

import logging
import os

# 创建Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 终端Handler,显示屏幕上
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

# 获取当前运行文件的目录
logfile_dir = os.path.dirname(os.path.abspath(__file__))
logfile_name = 'test.log'  # log文件名
# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)
# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# 文件Handler
# filemode ：日志文件的打开模式。 默认值为'a'，表示日志消息以追加的形
# 式添加到日志文件中。如果设为'w', 那么每次程序启动的时候都会创建一个新的日志文件
fileHandler = logging.FileHandler(logfile_path, mode='w', encoding='UTF-8')
fileHandler.setLevel(logging.NOTSET)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 添加到Logger中
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# 打印日志
logger.debug('debug ')
logger.info('info ')
logger.warning('warn ')
logger.error('error ')
logger.critical('critical ')
logger.debug('debug' )





#
# import logging
# logging.info('this is info message')
# logging.debug('this is debug message')
# logging.warning('this is warning message')
# logging.error('this is error message')
# logging.critical('this is critical message')


# WARNING:root:this is warning message
# ERROR:root:this is error message
# CRITICAL:root:this is critical message
