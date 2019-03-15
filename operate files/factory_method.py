#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:23
# @Author  : liuhu
# @File    : factory_method.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

# 设计工厂方法：文件的上传，结构为上传过程与保存过程，同时增加文件信息读取功能
# 1. 上传过程需要完成的步骤 对文件类型进行识别，
# 1.0 上传的不同类型的文件zip(内部包含exe文件),Excel表'xls', 'xlsx'格式，或者其他类似PDF TXT类型文件

# 2. 保存文件时，需要完成的步骤，
# 2.1 zip文件内部允许包含的文件数量限制，对EXE文件验证，获取压缩包内部文件的名称
# 2.2 在知道文件存放地址时，获取文件信息，所有的包的大小超出要求则将文件删除
# 2.3 针Excel文件进行数据的读取，针对其他文件进行保存

import os


class AboutFile(object):
    def __init__(self, file_object, filepath):
        return

    def save_file(self, file_object, filepath, max_size):
        file_object.save(filepath)
        self.is_file_exist(filepath)
        if not self.allowed_max_size(max_size):
            self.remove_file(filepath)
        return True

    def remove_file(self, filepath):
        if self.is_file_exist(filepath):
            os.remove(filepath)

    def is_file_exist(self, filepath):
        if os.path.exists(filepath):
            return True
        else:
            raise ValueError('file not exists')

    def file_size(self, filepath):
        file_size = os.path.getsize(filepath)
        size_unit_mb = file_size / float(1024 * 1024)
        return size_unit_mb

    def allowed_max_size(self, max_size, filepath):
        '''max_size,Mb'''
        if self.file_size(filepath) <= max_size:
            return True
        else:
            return False


class UploadZipFile(AboutFile):
    def __init__(self, file_object):
        pass

    def valid_filename(self):
        pass

    def file_size(self, filepath):
        pass

    def inner_filename(self,filepath):


class UploadExcelFile(AboutFile):
    def __init__(self, filename):
        pass


def file_factory(file_object):
    """file_object: requests.file['file']"""
    file_name = getattr(file_object, 'filename', '')
    if not file_name:
        raise ValueError('Not requested file object')
    if file_name.endswith('.zip'):
        pass
    elif file_name.endswith(('.xlsx', '.xls')):
        pass
    elif file_name.endswith((('.gif', '.jpg', '.png', '.txt', '.pdf'))):
        pass
    else:
        raise ValueError('file type Not allowed ')
