# -*- coding:utf-8 -*-

import os, sys
import struct
from socket import *

import settings

ipPort = (settings.ServerMes['ip'],settings.ServerMes['port'])

ftpClient = socket(AF_INET,SOCK_STREAM)

ftpClient.connect(ipPort)

def Userinfo():
    user = input('请输入用户名：').strip()
    passwd = input('输入该用户密码：').strip()
    info = 'login ' + user + ' ' + passwd
    return info

def StreamPush(Action):
    Pack = struct.pack('i', len(Action))
    ftpClient.send(Pack)
    ftpClient.send(Action.encode('utf-8'))

def StreamPull():
    packlen = ftpClient.recv(4)
    # print(packlen)
    Meslen = struct.unpack('i', packlen)[0]
    # print(Meslen)
    ServMes = ftpClient.recv(Meslen)
    PackMes = ServMes.decode('utf-8')
    return PackMes.split(' ')


Help = '帮助信息：\nlogin\t必须登录账号密码\nls\t显示当前目录下的文件\nupload\t上传文件\ndown\t下载文件\ncd\t更换目录\nquit|exit\t退出当前用户'
print(Help)

# 首先验证用户合法性
UserMes = Userinfo()
StreamPush(UserMes)
L = StreamPull()
CmdList = [['ls','cd'],['quit','exit']]
if L[0]:
    while True:
        usercmd = input('请输入要执行的命令：').strip()
        if not usercmd:continue
        command = usercmd.split()[0]
        if command in CmdList[0]:
            StreamPush(usercmd)
            L = StreamPull()
            print(' '.split(L))
        elif command in CmdList[1]:
            pass
        elif command == 'upload':
            StreamPush(usercmd)
            filename = usercmd.split()[1]
            # 读取文件内容，并上传值服务器
            with open(filename) as f:
                FileStr = f.read()
            StreamPush(FileStr)
            L = StreamPull()
            print(' '.split(L))
        elif command == 'down':
            pass
        else:
            print('输入命令错误，请重新输入')
            continue