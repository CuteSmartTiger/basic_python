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
from Tkinter import *
import subprocess
import os

temp_mtr_log = '/var/log/mtr/mtr_temp.log'
mtr_conf = '/etc/mtr/mtr.conf'
real_time_mtr_info = {'proto': None, 'package_loss': None, 'net_delay': None}
abnormal_mtr_log_loc = r'/var/log/mtr/mtr_abnorm.log'


def get_ip():
    ip = None
    try:
        with open(r'/thinclient_config/vditerminal_config.yaml', 'r') as f:
            content = f.readline()
            ip = content.split(':', 1)[1].strip()
    except BaseException as e:
        pass
    return ip


# ouput data
def output_data(ip, temp_mtr_log):
    if not os.path.exists(temp_mtr_log):
        os.system(
            'sudo mkdir /var/log/mtr && sudo touch /var/log/mtr/mtr_temp.log && sudo chmod 777 {0}'.format(temp_mtr_log))
    else:
        os.system('sudo echo > {0}'.format(temp_mtr_log))
    command = r'mtr -4 -n -p {0} |tee {1}'.format(ip, temp_mtr_log)
    px = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = px.pid
    print pid
    return ''


# check last line
def check_last_line(temp_mtr_log):
    command = r'tail -f -n 1 {0}'.format(temp_mtr_log)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    pid = p.pid
    print 'pid:'.format(pid)
    return p


def get_mtr_info(mtr_conf):
    max_abnorm_info = {'max_loss': '', 'max_delay': ''}
    with open(mtr_conf, 'r') as f:
        while True:
            content = f.readline()
            if content:
                if 'max_loss' in content:
                    try:
                        max_loss = content.split(':', 2)[1].strip()
                        max_abnorm_info['max_loss'] = max_loss
                    except IndexError as e:
                        pass
                if 'max_delay' in content:
                    try:
                        max_delay = content.split(':', 2)[1].strip()
                        max_abnorm_info['max_delay'] = max_delay
                    except IndexError as e:
                        pass
            else:
                break
    return max_abnorm_info


def package_delay_info(p, ip):
    while True:
        content = p.stdout.readline().strip()
        if content:
            if ip in content:
                break
            else:
                continue
        else:
            break
    if content:
        try:
            split_content = content.split()
            package_loss = split_content[2]
            net_delay = split_content[7]
            real_time_mtr_info['package_loss'] = package_loss
            real_time_mtr_info['net_delay'] = net_delay
            print {'after delay info  ': real_time_mtr_info}
            return real_time_mtr_info
        except IndexError as e:
            pass
    real_time_mtr_info['package_loss'] = None
    real_time_mtr_info['net_delay'] = None
    return real_time_mtr_info


def protocol_info():
    print {'before proto info ': real_time_mtr_info}
    pro = 'protocol='
    command = r'ps aux | grep protocol='
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while True:
        content = popen.stdout.readline().strip()
        if content:
            if pro in content:
                try:
                    proto = content.split('?', 2)[2].split('&', 1)[0].split('=', 1)[1]
                except IndexError as e:
                    continue
                if len(proto):
                    real_time_mtr_info['proto'] = proto
                    return real_time_mtr_info
                else:
                    continue
            else:
                continue
        else:
            break
    real_time_mtr_info['proto'] = None
    return real_time_mtr_info


def save_abnormal_info(abnorm_mtr_log_loc, proto, package_loss, net_delay, max_loss, max_delay):
    if not os.path.exists(abnorm_mtr_log_loc):
        os.system('sudo touch /var/log/mtr/mtr_abnorm.log && sudo chmod 777 {0}'.format(abnorm_mtr_log_loc))
    from datetime import datetime
    now = datetime.now()
    time_part = now.strftime('%y-%m-%d %H:%M:%S')
    if proto == 'console' or package_loss >= max_loss or net_delay >= max_delay:
        print 'abnormal'
        os.system(
            r'echo {0}, protocol:{1}, package_loss:{2}, net_delay:{3} >> {4}'.format(time_part, proto,
                                                                                     package_loss,
                                                                                     net_delay, abnorm_mtr_log_loc))
        center_window(root)


disappear_tag = 0

def disappear(event):
    global disappear_tag
    if disappear_tag == 0:
        disappear_tag = 1
        center_window(root, 5, 1)
        root.attributes('-alpha', 0.5)
        root.update()
    else:
        pass


def show(event):
    global disappear_tag
    if disappear_tag == 1:
        disappear_tag = 0
        center_window(root)
        root.attributes('-alpha', 0.5)
        root.update()
    else:
        pass


def center_window(root, width=400, height=25):
    """
    :param root: object
    :param width: int
    :param height: int
    :return:
    """
    screenwidth = root.winfo_screenwidth()
    window_wide_center = (screenwidth - width) / 2
    size = '%dx%d+%d+%d' % (width, height, window_wide_center, 0)
    root.geometry(size)


def set_window(root):
    root.attributes('-alpha', 0.5, '-fullscreen', False, '-topmost', True)
    root.overrideredirect(True)
    root.grid()
    center_window(root)
    root.bind(sequence='<Leave>', func=disappear)
    root.bind(sequence='<Enter>', func=show)


root = Tk()
set_window(root)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
Label(textvariable=var1, fg='blue', font=("黑体", 12)).grid(row=1, column=0, padx=10, pady=2)
Label(textvariable=var2, fg='blue', font=("黑体", 12)).grid(row=1, column=1, padx=10, pady=2)
Label(textvariable=var3, fg='blue', font=("黑体", 12)).grid(row=1, column=2, padx=10, pady=2)

color_display_status = {'proto_status': False, 'loss_status': False, 'delay_status': False}


def change_display_info(proto, package_loss, net_delay, max_loss, max_delay):
    proto_status = color_display_status['proto_status']
    if proto == 'dsp':
        print ' proto dsp'
        if proto_status:
            color_display_status['proto_status'] = False
            Label(textvariable=var1, fg='blue', font=("黑体", 12)).grid(row=1, column=0, padx=10, pady=2)
        else:
            pass
    else:
        print 'no proto dsp'
        if not proto_status:
            color_display_status['proto_status'] = True
            Label(textvariable=var1, fg='Crimson', font=("黑体", 12)).grid(row=1, column=0, padx=10, pady=2)
        else:
            pass

    loss_status = color_display_status['loss_status']
    if package_loss < max_loss:
        print 'below max_loss'
        if loss_status:
            color_display_status['loss_status'] = False
            Label(textvariable=var2, fg='blue', font=("黑体", 12)).grid(row=1, column=1, padx=10, pady=2)
        else:
            pass
    else:
        if not loss_status:
            color_display_status['loss_status'] = True
            Label(textvariable=var2, fg='Crimson', font=("黑体", 12)).grid(row=1, column=1, padx=10, pady=2)
        else:
            pass

    delay_status = color_display_status['delay_status']
    if net_delay < max_delay:
        print 'no max_delay'
        if delay_status:
            color_display_status['delay_status'] = False
            Label(textvariable=var3, fg='blue', font=("黑体", 12)).grid(row=1, column=2, padx=10, pady=2)
        else:
            pass
    else:
        print 'over max_delay'
        if not delay_status:
            color_display_status['delay_status'] = True
            Label(textvariable=var3, fg='Crimson', font=("黑体", 12)).grid(row=1, column=2, padx=10, pady=2)
        else:
            pass


class CreateContain:

    def __init__(self, root):
        self.fm = Frame(root)

    #递推危险
    def update_all_info(self):
        package_delay_info(p, ip)
        protocol_info()
        global real_time_mtr_info
        proto = real_time_mtr_info['proto']
        package_loss = real_time_mtr_info['package_loss']
        net_delay = real_time_mtr_info['net_delay']
        save_abnormal_info(abnormal_mtr_log_loc, proto, package_loss, net_delay, max_loss, max_delay)
        change_display_info(proto, package_loss, net_delay, max_loss, max_delay)
        if proto == 'dsp':
            var1.set('连接协议：正常')
        else:
            var1.set('连接协议：维护')
        var2.set('丢包率：{0}%'.format(package_loss))
        var3.set('网络延迟：{0}ms'.format(net_delay))
        self.fm.after(1000, self.update_all_info)


if __name__ == '__main__':
    ip = get_ip()
    data = output_data(ip, temp_mtr_log)
    p = check_last_line(temp_mtr_log)
    mtr_conf_info = get_mtr_info(mtr_conf)
    max_loss = mtr_conf_info['max_loss']
    max_delay = mtr_conf_info['max_delay']
    create = CreateContain(root)
    create.update_all_info()
    mainloop()
