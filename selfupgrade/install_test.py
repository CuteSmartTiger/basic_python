#encoding:utf-8
import requests,json

class Person(object):
    def __init__(self):
        self.versioninfo = "88.88.88.8"


    # 获取管理台最新版终端软件包的信息
    def __get_newversion_infor(self):
        # 0代表最新版本，type数值1代表类型为终端软件包
        # response = requests.get('http://192.168.6.35/packages/api/?mark_latest=0&type=1')
        response = requests.get('http://192.168.6.22/packages/api/?name=userfile1&type=2')
        content_json = response.json()
        self.newversion_filename = content_json[0]['filename']
        self.newversion_uuid = content_json[0]['uuid']
        self.latest_version = content_json[0]['package_version']

        # 基本路径   新版本包下载地址
        baseurl = "http://192.168.6.35/downloads/"
        liststr = [baseurl , self.newversion_uuid , "/" ,self.newversion_filename]
        self.newversion_url = "".join(liststr)


    def __process(self):
        # 若最新版本比现有版本大，则下载，安装，移除，重启
        if self.latest_version > self.versioninfo:
           print "wget {!s}".format(self.newversion_url)
           print "bash ./{!s} install".format(self.newversion_filename)
           print"rm -f ./{!s}".format(self.newversion_filename)



# response = requests.get('http://192.168.6.35/packages/api/?mark_latest=0&type=1')
# print response.json()
#
# if response.json():
#     print 'ok'


response = requests.get('http://192.168.6.22/packages/api/?name=userfile1&type=2')
content_json = response.json()
newversion_filename = content_json[0]['filename']
newversion_uuid = content_json[0]['uuid']
# latest_version = content_json[0]['package_version']

# 基本路径   新版本包下载地址
baseurl = "http://192.168.6.35/downloads/"
liststr = [baseurl ,newversion_uuid , "/" ,newversion_filename]
newversion_url = "".join(liststr)
print newversion_url