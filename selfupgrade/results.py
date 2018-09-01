import requests
import json

# response = requests.get('http://192.168.6.35/packages/api/?mark_latest=0&type=1')
response = requests.get('http://192.168.6.31/packages/api/?type=0&name=agent-x64-1.0.87')

content_json = response.json()
print content_json
# version_info = content_json[0]['package_version']
filename = content_json[0]['filename']
uuid = content_json[0]['uuid']

baseurl = "http://192.168.6.31/downloads/"
# baseurl = "http://192.168.6.35/downloads/"
liststr = [baseurl , uuid , "/" ,filename]
url = "".join(liststr)
print url

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
# 目录文件名不可以有空格，否则下载时无法识别路径
local = 'D://lh/l/h/version.zip'
urllib.urlretrieve(url, local, callbackfunc)


