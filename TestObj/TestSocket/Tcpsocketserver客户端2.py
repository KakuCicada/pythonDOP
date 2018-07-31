# -*- coding:utf-8 -*-

from socket import *

ipPort = ('127.0.0.1',8787)
backLog = 5
bufferSize = 1024


csock = socket(AF_INET,SOCK_STREAM)
csock.connect(ipPort)

while True:
    mes = input('--->:').strip()
    if not mes:continue
    if mes == 'quit':break

    csock.send(mes.encode('utf-8'))

    data = csock.recv(bufferSize)
    print('收到服务器返回信息：',data.decode('utf-8'))

csock.close()