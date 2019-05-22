#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/5 17:19
# @Author:张厚兴
# @Site：
# @File:SETTINGS.py
# @Software:PyCharm

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
DATADIR = {'path': '%s/data' % BASE_DIR}

LOG_LEVEL = logging.INFO


