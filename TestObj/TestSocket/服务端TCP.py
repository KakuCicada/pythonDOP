# coding:utf-8
#
import sys
from socket import *

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET,SOCK_STREAM)
# 地址重用，在状态为FIN-WITE2的时候，可以重复使用配置的IP地址
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

print('服务端运行ing...')
conn,addr = tcp_server.accept()
print('双向链接 ',conn)
print('客户端地址', addr)

while True:
    data = conn.recv(buffer_size)
    print('接收到客户端消息',data.decode('utf-8'))
    conn.send(data.upper())


conn.close()
tcp_server.close()
