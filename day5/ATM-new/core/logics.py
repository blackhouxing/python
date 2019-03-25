#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/20 17:11
# @Author:张厚兴
# @Site：
# @File:logics.py
# @Software:PyCharm


def view_account_info(account_data, *args, **kwargs):
    print(account_data)
    print("ACCOUNT INFO".center(50, '_'))
    for k, v in account_data['data'].items():
        if k not in ('password',):
            print("%15s: %s" % (k,v))
    print("END".center(50, '_'))

def with_draw():
    print("这是取现")


def pay_back():
    print("这是还款")
