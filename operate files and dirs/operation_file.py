import os
# 文本文件类型有：txt xml
# 二进制类型文件有： 图片 视频 音频


# 创建目录
# 1.1切换目录
os.chdir('../selfupgrade')
# 1.2在切换后的目录下创建目录,存在则无法创建，需要进行容错处理
if not os.path.exists('lihu'):
    os.mkdir('lihu')

# 创建文件
os.chdir('../files')
os.path.join(r'C:\liuhu\note\documents\basic python\files','liu.txt')


# 重名令文件
os.chdir('../files')
# 只能用于当前目录下，file/support_file.txt会报错
os.rename('support_file.txt','support_file.txt')

# 重命名目录
# os.rename('liuhu','fileliu')

# 重命名目录与目录下的文件,原目录下的文件会换到新建的目录下
# os.renames('../file/support_file.txt','../files/support_files.txt')

