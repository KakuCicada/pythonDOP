# coding=utf-8
#

import socket

Sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Sock.connect(('8.8.8.8',80))
Lip = Sock.getsockname()
Pip = Sock.getpeername()
Sock.close()
print(Pip,Lip)
