#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/18 17:05
# @Author:张厚兴
# @Site：
# @File:auth.py
# @Software:PyCharm

#
# def auth(func):
#     def wapper(*args, **kwargs,):
#         logging_status = False
#         count = 3
#         while logging_status is False and count > 0:
#             if logging_status is False:
#                 user = input('请输入您好银行账号：')
#                 password = input('请输入密码：')
#
#                 if user == "user" and password == "password":
#                     print("登录成功！")
#                     logging_status = True
#                     func(*args, **kwargs)
#
#                 else:
#                     print("抱歉您输入的用户名或密码不正确，请重试！还有%s次机会" % count)
#                 count -= 1
#                 if count == 0:
#                     print("密码输入错误三次，账户已被锁定，请联系管理员")
#     return wapper()
#
#
# @auth
# def login(account, password):
#     print('银行首页！')

from .db_handler import load_account_data


def authenticate(account, password):
    account_data = load_account_data(account)
    if account_data['status'] == 0:
        account_data = account_data['data']
        if password == account_data['password']:
            return account_data
        else:
            return None
    else:
        return None


