#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/18 17:14
# @Author:张厚兴
# @Site：
# @File:SETTING.py
# @Software:PyCharm

import os
import logging


#
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_LEVEL = logging.INFO

LOG_TYPE = {
    'access': 'access.log',
    'transfer': 'transfer.log',
    }
LOG_PATH = os.path.join(BASE_DIR, 'log')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': '%s/user_db/account/' % BASE_DIR,
    }

TRANSFER_TYPE = {
    'withdraw': '',
    'check_info': '',
    'payback': '',
    'transfer': '',
    }
