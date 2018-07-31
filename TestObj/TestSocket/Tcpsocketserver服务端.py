# -*- coding:utf-8 -*-

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is ',self.request)
        print('addr is ',self.client_address)

        while True:
            try:
                # 收消息
                data = self.request.recv(1024)
                if not data:break
                print('收到客户端消息',data)

                # 发消息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1',8787),MyServer)  # 多线程
    # s = socketserver.ForkingTCPServer(('127.0.0.1',8787),MyServer)  # 多进程
    s.serve_forever()