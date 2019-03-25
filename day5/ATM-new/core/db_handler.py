#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/20 16:38
# @Author:张厚兴
# @Site：
# @File:account.py
# @Software:PyCharm

from conf import SETTINGS
import json
import os


def load_account_data(account):
    """根据account ID 找到对应的账户文件，并加载"""

    account_file = os.path.join(SETTINGS.DATABASE['path'], "%s.json" % account)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)
        print(data)
        f.close()
        return {'status': 0, 'data': data}
    else:
        return {'status': -1, 'error': "account file does not exist."}


def save_db(account_data):
    pass
