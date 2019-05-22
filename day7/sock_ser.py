#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/13 16:33
# @Author:张厚兴
# @Site：
# @File:sock_ser.py
# @Software:PyCharm

import socket, os, time
server = socket.socket()
server.bind(('localhost', 6969)) #绑定要监听的端口

server.listen()

while True:

    conn, addr = server.accept() #等待连接
    #conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print("conn", addr)

    while True:
        print('等待指令...')
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break

        print('执行指令:', data)
        cmd_rec = os.popen(data.decode()).read()#接受字符串
        print("before send:", len(cmd_rec))
        if len(cmd_rec) == 0:
            cmd_rec = "cmd has no output"

        conn.send(str(len(cmd_rec.encode())).encode())
        time.sleep(0.5)
        conn.send(cmd_rec.encode())
        print("send done")
        os.path.isfile()
        os.stat("sock")
server.close()