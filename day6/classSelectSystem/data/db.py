#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/5 17:19
# @Author:张厚兴
# @Site：
# @File:db.py.py
# @Software:PyCharm


import sys
from conf import SETTING 
import pickle

PATH = DATADIR/DB.pk


def dump(obj):
    f = open(PATH, 'wb')
    pickle.dump(obj, f)
    f.close()


def load():
    f = open(PATH, 'rb')
    infos = pickle.load(f)
    f.close()
    return infos
