#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/21 11:52
# @Author:张厚兴
# @Site：
# @File:socketserv.py
# @Software:PyCharm

import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:

            self.data = self.request.recv(1024).strip()
            print("{}wrote:".format(self.client_address[0]))
            print(self.data)
            if not self.data:
                print("客户端断开")
                break
            self.request.sendall(self.data.upper())


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever() #在同一时间处理一个请求，直至结束

