#### os.system的作用
```
import os
resp = os.system("echo hello ")
result = os.system(" echo hello ")
res = os.system("echo hello ")
# 以上三个命令使用shell执行，成功则返回值0：
if resp ==0 and result ==0 and res == 0:
    print "ok"
```

##### 编写脚本，自动比较版本，判断需要更新，则下载，安装，移除文件，以上三个全部执行成功，则系统重启
```
 if latest_version > get_versioninfo:
    result_download = os.system("wget {!s}".format(newversion_url))
    result_install = os.system("bash ./{!s} install".format(newversion_filename))
    result_rm = os.system("rm -f ./{!s}".format(newversion_filename))
    # 以上三个执行成功则重启
    if result_download == 0 and result_install == 0 and result_rm == 0 :
        os.system("reboot")

```

***补充：由于window与Linux中系统执行成功，均返回0，所有可以用0值判断，但是若执行报错，
则不同的错误返回的值不一样***
