# -*- coding:utf-8 -*-

import os, sys
import time
from socket import *

ipPort = ('127.0.0.1',9888)
bufferSize = 1024

timeServer = socket(AF_INET,SOCK_DGRAM)
timeServer.bind(ipPort)

while True:
    data, addr = timeServer.recvfrom(bufferSize)
    print(data)
    Now = time.strftime('%F %T')
    Mes = '当前服务器时间为:'+Now
    timeServer.sendto(Mes.encode('utf-8'),addr)