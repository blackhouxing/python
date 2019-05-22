#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/24 11:04
# @Author:张厚兴
# @Site：
# @File:多态.py
# @Software:PyCharm


class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('%s动物叫' % self.name)

    def run(self):
        print('正在跑')

    @staticmethod
    def animal_talk(obj): #定义类的静态方法，实现多态。
        obj.talk()
        obj.run()


class Cat(Animal):
    def talk(self):
        print('%s喵喵' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s汪汪汪' % self.name)


c1 = Cat('mimi')

d1 = Dog('wangcai')

Animal.animal_talk(d1)
Animal.animal_talk(c1)
'''
一种接口，多种实现,具体体现
'''




