#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/16 15:29
# @Author:张厚兴
# @Site：
# @File:sock_C.py
# @Software:PyCharm

import socket, hashlib


client = socket.socket()
client.connect(("localhost", 9999))
while True:
    cmd = input(">>:".strip())
    if len(cmd) == 0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_resp = client.recv(1024)

        print("服务器返回内容：", server_resp)
        client.send("准备接收了".encode())
        file_total_size = int(server_resp.decode())
        received_size = 0
        file_name = cmd.split()[1]
        f = open(file_name+'.new', 'wb')
        m = hashlib.md5()


        while received_size < file_total_size:

            if file_total_size - received_size > 1024:
                size = 1024
            else:
                size = file_total_size - received_size
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            new_file_md5 = m.hexdigest()

            print('cmd received done', received_size, file_total_size)
            f.close()
        server_file_md5 = client.recv(1012)
        print("server端的md5", server_file_md5)
        print("收到的文件MD5",new_file_md5)
client.close()
