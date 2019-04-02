#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/18 17:13
# @Author:张厚兴
# @Site：
# @File:main.py
# @Software:PyCharm

from .auth import authenticate
from .logger import logger
from core import logics
from .utils import print_error



transaction_logger = logger("transfer")
access_logger = logger("access")

features = [
    ('账户信息', logics.view_account_info),
    ('取现', logics.with_draw),
    ('还款', logics.pay_back),
    ('转账',logics.transfer),
]





def entrance():
    def out_wrapper(func):
        def inner(*args, **kwargs):
        # atm程序交互入口
            user_obj = {
                'is_authenticated': False,
                'data': None,
                }
            retry_count = 0
            while user_obj['is_authenticated'] is not True:
                account = input("\033[32;1maccount:\033[0m").strip()

                pwd = input("\033[32;1mpassword:\033[0m").strip()

                auth_data = authenticate(account, pwd)
                if auth_data:
                    user_obj['is_authenticated'] = True
                    user_obj['data'] = auth_data
                    print("登录成功!")
                    access_logger.info("user %s just logged in " % user_obj['data']['id'])
                    func(user_obj, *args, **kwargs)

                else:
                    print("用户名密码不正确请重试")
                retry_count += 1

                if retry_count == 3:
                    msg = "用户 %s 密码连续3次输入错误，已被锁定。请联系管理员！" % account
                    print_error(msg)
        return inner
    return out_wrapper


@entrance()
def controller(user_obj):
    """功能分配"""


    while True:
        for index,feature in enumerate(features):
            print(index, feature[0])
        choice = input("ATM>>:").strip()
        if not choice:continue
        if choice.isdigit():
            choice = int(choice)
            if choice < len(features) and choice >= 0:
                features[choice][1](user_obj, transaction_logger=transaction_logger, access_logger=access_logger)
            if choice == 'exit':
                exit("bye")