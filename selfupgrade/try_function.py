#encoding:utf-8

# how to use time
# how to use try and finnally

import time
def count_time(n):
    try:
        start = time.time()
        while n>0:
            time.sleep(0.1)
            n -= 1
        end = time.time()
        diff = end - start
        if diff > 2:
            print "long"
    finally:
        print "ok"
count_time(3)


from flask_uploads import configure_uploads, UploadSet
ARCHIVES = tuple('gz bz2 zip tar tgz txz 7z rar pdf doc docx xlsx xls ppt pptx exe EXE'.split())
archives = UploadSet('archives', ARCHIVES)
print ARCHIVES
print list(ARCHIVES)
print archives

# import requests
# r = requests.root_url
# print r
x = set()
print type(x)

exename = "liuhu"
with open('version.txt', 'w') as f:
    f.write(r'C:\vdiupdate\%s /S' % exename)


suffix_list = ['gz', 'bz2', 'zip', 'tar', 'tgz', 'txz', '7z', 'rar', 'pdf', 'doc', 'docx', 'xlsx', 'xls', 'ppt', 'pptx']
if "zip" in suffix_list:
    print "helo"

filename = "ClientInstaller-x86_64-x86_64-3.0.6.0704.zip"
def _get_package_version(filename):
    filenamelist = filename.split("-",30)
    namelocation = len(filenamelist)-1
    unjudge_version  = filenamelist[namelocation]
    unjudge_version_list = unjudge_version.rsplit(".",1)
    # print unjudge_version.rsplit(".",1)[0]
    if unjudge_version_list[1] in suffix_list:
        basename = unjudge_version_list[0]
    else:
        basename = unjudge_version
    print unjudge_version_list
    return basename


_get_package_version(filename)