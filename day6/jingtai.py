#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/6 10:34
# @Author:张厚兴
# @Site：
# @File:jingtai.py
# @Software:PyCharm


"""
class Dog(object):
    n = 333
    def __init__(self, name):
        self.name = name

    @staticmethod
    # @classmethod
    def eat():
        print(" %s is eatting " % self.name)

    def talk(self):
        print('%s is talking' % self.name)


d = Dog('a')

d.eat()
d.talk()

"""


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def check_status(self):
        print("flight checking %s status!!" % self.flight_name)

        return 0

    @property                   #把flight_status方法变成静态属性
    def flight_status(self):
        status = self.check_status()
        if status == 0:
            print("flight got canceled....")

        elif status == 1:
            print("flight is arrived...")

        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter  #修改属性值 加上“setter”后属性值可以被修改
    def flight_status(self, status):
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departured",
        }
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))


    @flight_status.deleter #删除属性
    def flight_status(self):
        print("status got removed")

    def __str__(self):
        return '我是返回值'

f = Flight("MU5635")

f.flight_status    #变成静态属性后可以被实例直接调用，而不用关心后台动作。

f.flight_status = 1 #既然是属性，理论上是能赋值的。但此时还不能赋值


del f.flight_status

print(f)