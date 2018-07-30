# -*- coding:utf-8 -*-

from socket import *

ip_port = ('127.0.0.1',9099)
buffer_size = 1024

udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    print('UDP服务器运行ing... ...')
    data,addr = udp_server.recvfrom(buffer_size)
    print(data)
    udp_server.sendto(data.upper(),addr)