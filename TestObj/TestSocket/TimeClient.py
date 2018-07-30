# -*- coding:utf-8 -*-

import os, sys
from socket import *

ipPort = ('127.0.0.1',9888)
bufferSize = 1024

timeClient = socket(AF_INET,SOCK_DGRAM)

timeClient.sendto('Time'.encode('utf-8'),ipPort)
data, addr = timeClient.recvfrom(bufferSize)
print(data.decode('utf-8'))