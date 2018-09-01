#encoding:utf-8

# 方法一： requests
# 缺点：需要已知下载文件的地址
import requests
# print "downloading with requests"
# url = 'http://192.168.6.35/downloads/ae7e5289-9258-4e48-abff-a3960eb84c4b/1.bat'
# url = 'http://192.168.6.38/downloads/18f113a6-fe99-4432-ab0d-92a3cb03c053/Setup-Subversion-1.8.17.msi'
url = 'http://192.168.6.33/static/uploads/9d872990-3137-4990-8f48-6afc4c8fd48d/putHeader.txt'
# url = 'http://192.168.6.35/downloads/logfiles/checklogs.zip'
# url = 'http://192.168.6.35/uploads/ae7e5289-9258-4e48-abff-a3960eb84c4b/1.bat'   #失败
r = requests.get(url)
print url
# with open("new_version.zip", "wb") as code:
#      code.write(r.content)
#      print "ok"


# # 读取文本中的中文信息或者读取中文名称的文本中的中文信息
# import sys
# codetype = sys.getfilesystemencoding()
# # 使用Unicode将文件名称进行编码,Unicode万国码，将各种语言转化成计算机可识别的数字语言
# f = open(unicode('liuhu1.txt',"utf-8"),'r')
# # 先解码然后再编码,用于识别文档内容中的中文
# m=f.read().decode(codetype).encode("utf-8")
# f.close()
# print m


# x = open("version.txt","r").read()
# print x
# print type(x)
#
#
# # 方法二：使用urllib的urlopen()函数
# # 缺点：需要已知下载文件的地址
import urllib2
# print "downloading with urllib2"
# url = 'http://192.168.6.35/downloads/db036197-9e07-4612-ae4b-64a96a2a31cb/bokeyuan.md'
# f = urllib2.urlopen(url)
# data = f.read()
# with open("demo2", "wb") as code:
#     code.write(data)
#     print "ok"



# 方法三：
#缺点：速度太慢
# urlretrieve(url, [filename=None, [reporthook=None, [data=None]]])
# 说明：
#
# 参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
#
# 参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
#
# # 参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，filename 表示保存到本地的路径，header 表示服务器的响应头。
# import urllib
# import os
# def Schedule(a,b,c):
#     '''''
#     a:已经下载的数据块
#     b:数据块的大小
#     c:远程文件的大小
#    '''
#     per = 100.0 * a * b / c
#     if per > 100 :
#         per = 100
#     print '%.2f%%' % per
# url = 'https://docs.python.org/3/archives/python-3.7.0-docs-pdf-letter.zip'
# #local = url.split('/')[-1]
# local = os.path.join('D:\jobwork\pycharm test Python\selfupgrade','Python-2.7.5.tar.bz2')
# urllib.urlretrieve(url,local,Schedule)