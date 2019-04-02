#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/3/20 17:11
# @Author:张厚兴
# @Site：
# @File:logics.py
# @Software:PyCharm

from .utils import print_warning
from .transaction import make_transaction
from .db_handler import load_account_data
from .db_handler import save_db


def view_account_info(account_data, *args, **kwargs):
    print(account_data)
    print("ACCOUNT INFO".center(50, '_'))
    for k, v in account_data['data'].items():
        if k not in ('password',):
            print("%20s: %s" % (k, v))
    print("END".center(50, '_'))


def with_draw(account_data, *args, **kwargs):
    trans_logger = kwargs.get("transaction_logger")
    curren_balance = '''-------------BALANCE INFO--------------
        Credit:    %s
        Balance:   %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(curren_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1m请输入取现金额：\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if (account_data['data']['balance'] / 2) >= withdraw_amount:
                transcation_result = make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
                if transcation_result['status'] == 0:
                    print('''\033[42;1mNEW Balance:%s\033[0m''' % (account_data['data']['balance']))
                else:
                    print(transcation_result)
            else:
                print_warning("可取余额不足，可提现%s" % (int(account_data['data']['balance'] / 2)))

        if withdraw_amount == 'b':
            back_flag = True


def pay_back(account_data, *args, **kwargs):
    """

    :param account_data:
    :param args:
    :param kwargs:
    :return:
    """
    trans_logger = kwargs.get("transaction_logger")
    current_balance = '''-------------Balance info------------
        Credit: %s
        Balance: %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(current_balance)
    pay_amount = input('\033[33;1m请输入还款金额：\033[0m').strip()
    if len(pay_amount) > 0 and pay_amount.isdigit():
        pay_amount = int(pay_amount)
        transaction_result = make_transaction(trans_logger, account_data, 'payback', pay_amount)
        if transaction_result['status'] == 0:
            print('''\033[42;1mNew Balance:%s\033[0m''' % (account_data['data']['balance']))
        else:
            print(transaction_result)


def transfer(account_data, *args, **kwargs):
    # print('这是转账')
    # print(account_data['data'])
    current_balance = '''--------Balance Info--------------
    Credit: %s
    Balance: %s''' % (account_data['data']['credit'],
                      account_data['data']['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:

        dest_account = input('\033[31;1m请输入转入账号：\033[0m').strip()
        dest_account_ack = input('\033[31;1m请再次输入转入账号：\033[0m').strip()
        if dest_account == dest_account_ack:
            new_account_data = load_account_data(dest_account_ack)["data"]
            dest_amount = input('\033[33;1m请输入转账金额：\033[0m').strip()
            choice = input("请问是否确认给%s转账%s? Y/n:" % (dest_account, dest_amount))
            if choice == "Y" or choice == "y":
                new_dest_amount = float(dest_amount)
                account_data['data']['balance'] = float(account_data['data']['balance'])
                new_account_data['balance'] = float(new_account_data['balance'])
                account_data['data']['balance'] -= new_dest_amount
                new_account_data['balance'] += new_dest_amount

                save_db(account_data['data'])
                save_db(new_account_data)
                print("转账成功！")
            else:
                break

        else:
            print("对不起，两次输入的账号不一致，请重新输入！")
            back_flag = True






