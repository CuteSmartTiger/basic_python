#encoding:utf-8
import requests
r = requests.get(r'http://192.168.6.38/packages/api/?mark_latest=1&type=1')
print r

get_version = '3.0.1.0324'
# 获取管理台最新版终端软件包的信息
def __get_newversion_infor():
    # 0代表最新版本，type数值1代表类型为终端软件包
    response = requests.get(r'http://192.168.6.38/packages/api/?mark_latest=1&type=1')
    content_json = response.json()
    newversion_filename = content_json[0]['filename']
    print(newversion_filename)
    newversion_uuid = content_json[0]['uuid']
    print(newversion_uuid)
    latest_version = content_json[0]['package_version']
    print(latest_version)

    # 基本路径   新版本包下载地址
    baseurl = "http://192.168.6.38/downloads/"
    liststr = [baseurl,newversion_uuid , "/" ,newversion_filename]
    newversion_url = "".join(liststr)
    print(newversion_url)


    if latest_version == get_version:
        print("版本已经比较")


# os.system("wget {!s}".format(self.newversion_url))
# os.system("bash ./{!s} install".format(self.newversion_filename))
# os.system("rm -f ./{!s}".format(self.newversion_filename))
# os.system("reboot")

if __name__ == "__main__":
    __get_newversion_infor()
