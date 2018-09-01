#encoding:utf-8
#!/bin/bash
#
# import requests
# import json
#
# response = requests.get('http://192.168.6.35/packages/api/?mark_latest=0&type=1')
# content_json = response.json()
# print response.json()
# print content_json[0]
# print type(content_json[0])
# print content_json[0]['uuid']
# print content_json[0]['package_version']
# data = content_json[0]['package_version']
# print type(data)
# st = data.encode()
# print st
# print type(st)
# latest_version = st
#
# gb = data.encode("utf-8")
#
#
# print type(gb)
# def test(st,gb):
#     if st == gb:
#         print "ok"
#     else:
#         print "no"
# print test(st,gb)



import requests
import json

response = requests.get('http://192.168.6.35/packages/api/?mark_latest=0&type=1')
# response = requests.get('http://192.168.6.31/packages/api/?type=0&name=agent-x64-1.0.87')

content_json = response.json()
# print content_json
# version_info = content_json[0]['package_version']
filename = content_json[0]['filename']
uuid = content_json[0]['uuid']

# baseurl = "http://192.168.6.31/downloads/"
baseurl = "http://192.168.6.35/downloads/"
liststr = [baseurl , uuid , "/" ,filename]
newversion_url = "".join(liststr)
print newversion_url

import urllib
def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent

# local = 'D://lh/1.md'
local = 'D://lh/l/h/version.zip'
local = 'D://lh/l/h/version.zip'
urllib.urlretrieve(url, local, callbackfunc)



# import urllib2
# f = urllib2.urlopen(url)
# print f
# data = f.read()
#
# with open("newversion.zip", "wb") as code:
#     code.write(data)
#     print "ok"

# import requests
# import os
# print "downloading with requests"
# os.chdir('./lh')
# r = requests.get(url)


# latest_version = version_info.encode('utf-8')
# terminal_version = version_info.encode('utf-8')





# def judge_version(new,old):
#     if new > old:

