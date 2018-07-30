# coding:utf-8
#
import sys
from socket import *

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)

tcp_client.connect(ip_port)

while True:
    mes = input('----->:')
    tcp_client.send(mes.encode('utf-8'))
    print('客户端已发送消息',mes)
    data = tcp_client.recv(buffer_size)
    print('收到服务器消息 ',data.decode('utf-8'))

tcp_client.close()