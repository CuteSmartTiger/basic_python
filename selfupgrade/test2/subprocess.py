#encoding:utf-8

import subprocess
import os

cmd = ['os.path.abspath(os.path.dirname(__file__))' + '/bin/licenseclient', '5555', 'unreg']
os.system('cmd')

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# communicate()函数比wait()好
out, err = p.communicate()

# print p
# print out
# print err