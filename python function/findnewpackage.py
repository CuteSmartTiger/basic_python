#encoding:utf-8

from flask import session
# 类型：终端软件包
type= "\u7ec8\u7aef\u8f6f\u4ef6\u5305"
uuid = "3e015263-7d04-435c-89f3-6d605c5d8f65"
# 1.先根据类型分组查询，获取了所有终端软件包的信息
# 最新创建的用户排在前面，最新注册的也就是时间最大的
results = db.session.query().filter().order_by(Package.create_time.desc()).all()

# 查询一个最新终端包的所有信息,先导入package模型
package = Package.query.filter(type=type1).order_by(Package.create_time.desc()).first()
filename = package.filename
uuid = package.uuid



# 下载地址：url="http://192.168.6.31/"+"downloads"+"uuid"+"filename"
# 将查询数据进行拼接获得url
# 拼接获得url地址(当链接的字符串选项很多时不推荐此方法)
baseurl = "http://192.168.6.31/downloads/"
uuid = "3e015263-7d04-435c-89f3-6d605c5d8f65"
# 方法一：加号
# 注意：这里的url不是固定的
url = baseurl + uuid + "/" + filename
print url

# 方法二：join （推荐）
liststr = [baseurl , uuid , "/" ,filename]
url = "".join(liststr)
print url

#方法三：替换
url="%s%s%s%s"%(baseurl,uuid,"/",filename)
print url




# 获取web端的软件包的版本号
# 思路：对获取的版本号取右边十位
# 截取获得版本号：
filename = "ClientInstaller-x86_64-x86_64-3.0.1.0324"
latest_version = filename[-10:]
# 去除".",转换成数字进行比较大小，尽量不要用字符串进行比较
new_version = latest_version.replace(".","")
print new_version
