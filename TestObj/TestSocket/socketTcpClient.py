# -*- coding:utf-8 -*-

import os, sys
from socket import *

ipPort = ('127.0.0.1',8787)
backLog = 5
bufferSize = 1024

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(ipPort)

while True:
    cmd = input('请输入要执行的命令:').strip()
    if not cmd:continue
    if cmd == 'quit':break

    print(cmd)
    tcpClient.send(cmd.encode('utf-8'))
    CmdRes = tcpClient.recv(bufferSize)
    print(CmdRes.decode('gbk'))

tcpClient.close()