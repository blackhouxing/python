#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/20 17:03
# @Author:张厚兴
# @Site：
# @File:logger.py
# @Software:PyCharm
import os
import logging
from conf import SETTINGS


def logger(log_type):
    logger = logging.getLogger(log_type) #定义日志类型
    logger.setLevel(SETTINGS.LOG_LEVEL)#确定记录日志的级别
    log_file = os.path.join(SETTINGS.LOG_PATH, SETTINGS.LOG_TYPE[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(SETTINGS.LOG_LEVEL)
    formatter = SETTINGS.LOG_FORMAT

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
