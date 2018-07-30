# -*- coding:utf-8 -*-

from socket import *

ip_port = ('127.0.0.1',9099)
buffer_size = 1024


udp_client = socket(AF_INET,SOCK_DGRAM)

while True:
    mes = input('------>').strip()
    udp_client.sendto(mes.encode('utf-8'),ip_port)
    data,addr = udp_client.recvfrom(buffer_size)
    print(data.decode('utf-8'))