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
    info = user + ' ' + passwd
    return info

def StreamPro(Action):
    Pack = struct.pack('i', len(Action))
    ftpClient.send(Pack)
    ftpClient.send(Action.encode('utf-8'))
    packlen = ftpClient.recv(4)
    Meslen = struct.unpack('i', packlen)[0]
    ServMes = ftpClient.recv(Meslen)
    PackMes = ServMes.decode('utf-8')
    print(PackMes.split(' ')[1:])
    return PackMes.split(' ')[0]


Help = '帮助信息：\nlogin\t必须登录账号密码\nls\t显示当前目录下的文件\nupload\t上传文件\ndown\t下载文件\ncd\t更换目录'
print(Help)

while True:
    usercmd = input('请输入要执行的命令：').strip()
    if usercmd == 'login':
        UserMes = Userinfo()
        StreamPro(UserMes)