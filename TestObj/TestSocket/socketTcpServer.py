# -*- coding:utf-8 -*-

import os, sys
import subprocess
from socket import *

ipPort = ('127.0.0.1',8787)
backLog = 5
bufferSize = 1024

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(ipPort)
tcpServer.listen(backLog)

while True:
    conn,addr = tcpServer.accept()
    print('新的客户端连接',addr)
    while True:
        try:
            # 接收客户端发送的命令
            cmd = conn.recv(bufferSize)
            if not cmd: break
            print('收到客户端命令',cmd)


            # 执行命令
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            # print(res.stderr.read())
            Error = res.stderr.read()
            if not Error:
                RET = res.stdout.read()
            else:
                RET = Error
                print(RET)

            # 发送命令输出
            conn.send(RET)
        except Exception as e:
            print(e)
            break
    conn.close()