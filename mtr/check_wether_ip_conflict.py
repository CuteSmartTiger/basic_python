#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuhu
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: max_liuhu@163.com
@software: pycharm
@file: catch_data.py
@time: 2018/11/7 17:26
@desc:
'''

# cat /thinclient_config/vditerminal_config.yaml

# commands = "ifconfig %s | grep 'inet addr' | head -1 | awk  -F'[: ]+' '{print $4}'"
commands = "ifconfig enp3s0 | grep 'inet addr' | head -1 | awk  -F'[: ]+' '{print $4}'"

import subprocess
import os

# config_file = 'vditerminal_config.yaml'
config_file = '/thinclient_config/vditerminal_config.yaml'


def get_target(target):
    target_value = ''
    with open(config_file, 'r') as f:
        while True:
            content = f.readline()
            if content:
                if target in content:
                    try:
                        target_value = content.split(':', 1)[1].strip()
                        break
                    except BaseException:
                        pass
                else:
                    continue
            else:
                break
    return target_value


def check_ip_wether_conflict(ifacename):
    print 'wether'
    if ifacename == '':
        return False
    commands = "ifconfig %s | grep 'inet addr' | head -1 | awk  -F'[: ]+' '{print $4}'" % ifacename
    out = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,
                                      shell=True)
    print out
    ip = out.stdout.readline()
    if ip:
        exit_code = os.system("arping -c 1 -f -D -w 1 -I %s %s" % (ifacename, ip))
        print(exit_code)
        if exit_code != 0:
            return True
    return False


ifacename= get_target('ifacename')
print ifacename
print check_ip_wether_conflict(ifacename)
