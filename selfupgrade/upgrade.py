#encoding:utf-8

# 本代码主要目的是自己升级更新自己
# 思路：
# 1. 下载新版软件
# 2. 关闭当前运行的旧版软件
# 3. 删除旧版软件
# 3. 启动新的软件
import os
import sys
import subprocess



# 解压缩


with open("liuhu1.txt","w") as f:
    f.write("version.txt")

print f

#
#
# #编写bat脚本，删除旧程序，运行新程序
# def WriteRestartCmd(exe_name):
#     b = open("upgrade.bat",'w')
#     TempList = "@echo off\n"                                          #关闭bat脚本的输出
#     TempList += "if not exist "+exe_name+" exit \n"             #新文件不存在,退出脚本执行
#     TempList += "sleep 3\n"                                         #3秒后删除旧程序（3秒后程序已运行结束，不延时的话，会提示被占用，无法删除）
#     TempList += "del "+ os.path.realpath(sys.argv[0]) + "\n"        #删除当前文件
#     TempList += "start " + exe_name                                 #启动新程序
#     b.write(TempList)
#     b.close()
#     subprocess.Popen("upgrade.bat")
#     sys.exit()  #进行升级，退出此程序
#
#
#
# def main():
# #新程序启动时，删除旧程序制造的脚本
#     if os.path.isfile("upgrade.bat"):
#         os.remove("upgrade.bat")
#     WriteRestartCmd("newVersion.exe")
#
# if __name__ == '__main__':
#     main()
#     sys.exit()

# directory ="liuhu"
# if not os.path.exists(directory):
#     os.makedirs(directory)


# from datetime import datetime
# import time
# # # timeshow = datetime.now()
# # x=time.time()
# # y=time.localtime(x)
# # print x
# # print y
# dt_new = time.strftime("%Y%m%d-%H:%M:%S",time.localtime(time.time()))
# print dt_new
# # dt = "2016-05-05 20:28:54"
# print os.path.join("liuhu","jjj")
# #转换成时间数组
# timeArray = time.strptime(timeshow, "%Y-%m-%d %H:%M:%S")
# #转换成新的时间格式(20160505-20:28:54)
# dt_new = time.strftime("%Y%m%d-%H:%M:%S",timeArray)
# print dt_new
# # print x
# print type(timeshow)
# print str(timeshow)
# print type(str(timeshow))

