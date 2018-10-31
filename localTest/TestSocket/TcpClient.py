# -*- coding:utf-8 -*-
#

from socket import *

IpPort = ('127.0.0.1',8999)
backLog = 5
bufferSize = 1024

TcpClient = socket(AF_INET,SOCK_STREAM)
TcpClient.connect(IpPort)

while True:
    mes = input('----->').split()[0]
    if not mes:continue
    # if mes == 'quit':break
    TcpClient.send(mes.encode('utf-8'))
    data = TcpClient.recv(bufferSize)
    print('服务端发来信息：',data.decode('utf-8'))
    
TcpClient.close()