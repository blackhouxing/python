#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/24 11:52
# @Author:张厚兴
# @Site：
# @File:main.py
# @Software:PyCharm

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from modules import manager
from modules import student
from modules import teacher
def login():
    print('''----------请选择角色----------
          1.学生
          2.老师
          3.管理员
          4.退出
------------------------------''')
    while True:
        choice = input('请选择角色：')
        if choice == '1':
            print('这是学生！')
            student

        elif choice == '2':
            print("这是老师")
            teacher

        elif choice == '3':
            print("这是管理员")
            manager

        elif choice == '4':
            break
            exit(0)

        else:
            print('输入正确选择！')


if __name__ == "__main__":
    login()

