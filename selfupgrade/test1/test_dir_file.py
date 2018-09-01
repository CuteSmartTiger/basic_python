#encoding:utf-8
import os

# if os.path.isdir('D:\jobwork\pycharm test Python\selfupgrade\test'):  #不加r进行防止反转意，则失败
if not os.path.isdir(r'D:\jobwork\pycharm test Python\selfupgrade\test'):
    print "no"
else:
    print "ok"

import time
from datetime import datetime
timenow = datetime.now()
print timenow
