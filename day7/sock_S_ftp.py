#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/16 15:28
# @Author:张厚兴
# @Site：
# @File:sock_S.py
# @Software:PyCharm

import socket, os, time
import hashlib
import socketserver

server = socket.socket()
server.bind(('localhost', 6969))

server.listen()

while True:
    conn, addr = server.accept()
    print('conn', addr)

    while True:
        print("等待命令>>")
        data = conn.recv(1024)
        if not data:
            print("没有数据传输，终端连接！")
            break
        cmd, filename = data.decode().split()
        print("正在接收数据...", filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print("send done")

server.close()
