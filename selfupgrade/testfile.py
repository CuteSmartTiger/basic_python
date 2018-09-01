import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
path = os.path.dirname(__file__)
print BASE_DIR
print path
file_path = os.path.join(BASE_DIR, 'filename')
print file_path
# D:\jobwork\pycharm test Python\selfupgrade

from flask_session import sessions
