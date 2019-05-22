#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/10 20:26
# @Author:张厚兴
# @Site：
# @File:sock.py
# @Software:PyCharm

import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))

while True:
    cmd = input(">>:".strip())

    if len(cmd) == 0: continue

    client.send(cmd.encode())
    cmd_rec_size = client.recv(1024)
    print('命令结果大小：', cmd_rec_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_rec_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        received_data += data
    else:
        print('cmd res received done', received_size)
        print(received_data.decode())

client.close()