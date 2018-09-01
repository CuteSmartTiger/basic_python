#encoding:utf-8

def create_log_filesname():
    import time
    now_time = time.strftime("%Y%m%d-%H_%M_%S",time.localtime(time.time()))
    str_nowtime = str(now_time)
    log_filesname = "logfiles"+str_nowtime
    return log_filesname

L = create_log_filesname()
print L
# # 截取获得版本号：
# filename = "ClientInstaller-x86_64-x86_64-3.0.1.0324"
# # latest_version = filename[-10:]
# # location = filename.find("-")
# # version_test = filename[location+1:]
# l = filename.rsplit("-",20)
# print l
# nums=len(l)-1
# print nums
# target = l[nums]
# print target
# print type(target)


# print location
# print version_test
# 去除".",转换成数字进行比较大小，尽量不要用字符串进行比较
# new_version = latest_version.replace(".","")
# print new_version
# print type(latest_version)
# print int(new_version)


#
# # 拼接获得url地址(当链接的字符串选项很多时不推荐此方法)
# baseurl = "http://192.168.6.31/downloads/"
# uuid = "3e015263-7d04-435c-89f3-6d605c5d8f65"
# # 方法一：加号
# url = baseurl + uuid + "/" + filename
# print url
#
# # 方法二：join （推荐）
# liststr = [baseurl , uuid , "/" ,filename]
# url = "".join(liststr)
# print url
#
# #方法三：替换
# url="%s%s%s%s"%(baseurl,uuid,"/",filename)
# print url
#
#
# #
# # python is 主要是判断 2 个变量是否引用的是同一个对象，如果是的话，则返回 true，否则返回 false。
# # 判断数字相等不要用 is 操作符
# a = 257
# print id(a)
# b = 257
# print id(b)
#
# if a is b:
#     print "ok"
# else:
#     print "no"
#
#
#
# old_version = terminal_version


#
# def compare_new_and_old():
#     from datetime import datetime
#     if new_version > old_version:
#         start=datetime.time()
#         try:
#             "下载更新"
#             "失败则"
#         return "更新"
#     else:
#         return "跳转到用户登录界面"