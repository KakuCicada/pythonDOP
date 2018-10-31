# -*- coding:utf-8 -*-
#

from socket import *

IpPort = ('127.0.0.1',8999)
backLog = 5
bufferSize = 1024

TcpServer = socket(AF_INET,SOCK_STREAM)
TcpServer.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
TcpServer.bind(IpPort)
TcpServer.listen(backLog)

while True:
    conn, addr = TcpServer.accept()
    print('服务器开始运行...')
    while True:
        try:
            data = conn.recv(bufferSize)
            print('服务器接收到客户端发来的信息：',data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    conn.close()
    