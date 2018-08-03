# -*- coding:utf-8 -*-

import os, sys
from socket import *
import struct
import subprocess
import settings

ftpServer = socket(AF_INET,SOCK_STREAM)

ipPort = (settings.ServerMes['ip'],settings.ServerMes['port'])
SetUser = settings.UserMes

def Changedir(Mes):
    Dir = Mes[1]
    os.chdir(Dir)
    mes = '目录切换至 %s 成功' %Dir
    print(mes)
    return mes

def uploadfile(request,Mes):
    Filename = Mes[1]
    Fileread = request.recv()
    with open(str(Filename),'rw+') as f:
        f.write(Fileread)
    return '上传文件成功'

def downloadfile(request,Mes):
    pass

def showfile(Mes):
    if len(Mes) == 1:
        RetMes = os.listdir()
    else:
        RetMes = os.listdir(Mes[1])
    return ' '.join(RetMes)

def login(Mes):
    # 读取配置文件里的信息，获取输入过来的账号密码作对比
    if Mes[1] in SetUser:
        if Mes[2] == SetUser[Mes[1]]['passwd']:
            mes = '0 登录成功'
            PWD = os.getcwd()
            UserHomeDir = PWD + SetUser[Mes[1]]['homedir']
            os.chdir(UserHomeDir)
        else:
            mes = '1 登录失败'
    else:
        mes = '1 用户不存在'
    return mes

def Getcmd(request):
    meslen = request.recv(4)
    loginlen = struct.unpack('i', meslen)[0]
    UserInfo = request.recv(loginlen)
    SendInfo = UserInfo.decode('utf-8').split(' ')
    return SendInfo

def SendMes(request,Mes):
    Pack = struct.pack('i', len(str(Mes).encode('utf-8')))
    # print(Pack)
    request.send(Pack)
    request.send(str(Mes).encode('utf-8'))
    print(str(Mes).encode('utf-8'))


ftpServer.bind(ipPort)
ftpServer.listen(5)
print('服务器开始运行于%s的%s端口' %(settings.ServerMes['ip'],settings.ServerMes['port']))
while True:
    conn,addr = ftpServer.accept()
    print('新的客户端连接：',addr)
    while True:
    # try:
        # 当有新的链接进入时，需要进行登录操作
        Info = Getcmd(conn)
        print(Info)
        print('*' * 40)
        if Info[0] == 'login':
            Mes = login(Info)
            SendMes(conn, Mes)
        elif Info[0] == 'cd':
            Mes = Changedir(Info)
            SendMes(conn, Mes)
        elif Info[0] == 'upload':
            Mes = '开始传输文件'
            SendMes(conn, Mes)
            uploadfile(conn,Info[1])

        elif Info[0] == 'down':
            Mes = downloadfile(Info)
        elif Info[0] == 'ls':
            Mes = showfile(Info)
            SendMes(conn, Mes)
        elif Info[0] == 'quit' or Info[0] =='exit':
            conn.close()
            break



    # except Exception as e:
    #     print(e)
    #     break