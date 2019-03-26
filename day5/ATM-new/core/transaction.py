#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/25 15:58
# @Author:张厚兴
# @Site：
# @File:transaction.py
# @Software:PyCharm
from conf import SETTINGS
from .db_handler import save_db
import logging


def make_transaction(logger, user_obj, tran_type, amount, **kwargs):
    """
    :param logger:
    :param user_obj:
    :param tran_type:
    :param amount:
    :param kwargs:
    :return:
    """

    amount = float(amount)
    if tran_type in SETTINGS.TRANSFER_TYPE:
        interest = amount * SETTINGS.TRANSFER_TYPE[tran_type]['interest']
        old_balance = user_obj['data']['balance']
        if SETTINGS.TRANSFER_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif SETTINGS.TRANSFER_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            if new_balance < 0:
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s]，
                your current balance is [%s]\033[0m''' % (user_obj['data']['credit'], (amount + interest), old_balance))
                return {'status': 1, 'error': '交易失败，余额不足'}
        user_obj['data']['balance'] = new_balance
        save_db(user_obj['data'])

        logging.info('account:%s action:%s amount:%s interest:%s balance:%s'
                     % (user_obj['data']['id'], tran_type, amount, interest, new_balance))
        return {'status': 0, 'msg': '交易成功'}
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
        return {'status': 1, 'error': '交易失败，Transaction type [%s] is not exist!' % tran_type}



