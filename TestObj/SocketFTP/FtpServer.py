# -*- coding:utf-8 -*-

import os, sys
from socket import *
import struct
import subprocess
import settings

ftpServer = socket(AF_INET,SOCK_STREAM)

ipPort = (settings.ServerMes['ip'],settings.ServerMes['port'])

class clientCMD(object):
    '''存储来自于client的命令方法
    '''
    def __init__(self, arg):
        self.arg = arg

    def Changedir(self):
        Dir = self.arg
        os.chdir(Dir)
        Mes = '目录切换至 %s 成功' %Dir
        return Mes

    def uploadfile(self):
        pass

    def downloadfile(self):
        pass

    def showfile(self):
        pass

def Getcmd(request):
    meslen = request.recv(4)
    loginlen = struct.unpack('i', meslen)[0]
    UserInfo = request.recv(loginlen)
    SendInfo = UserInfo.decode('utf-8').split(' ')
    return SendInfo

def SendMes(Mes):
    Pack = struct.pack('i', len(Mes))
    ftpServer.send(Pack)
    ftpServer.send(Mes.encode('utf-8'))


ftpServer.bind(ipPort)
ftpServer.listen(5)
print('服务器开始运行于%s的%s端口' %(settings.ServerMes['ip'],settings.ServerMes['port']))
while True:
    conn,addr = ftpServer.accept()
    print('新的客户端连接：',addr)
    try:
        # 当有新的链接进入时，需要进行登录操作
        Info = Getcmd(conn)
        SetUser = settings.UserMes
        if Info[0] in SetUser:
            print('*'*20)
            if Info[1] == SetUser[Info[0]]['passwd']:
                mes = '0 登录成功'
            else:
                mes = '1 登录失败'
        else:
            mes = '1 用户不存在'
        conn.send(mes.encode('utf-8'))

        while True:
            Usercmd = Getcmd(conn)
    except Exception as e:
        print(e)
        break