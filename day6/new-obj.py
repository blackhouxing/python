#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/19 18:12
# @Author:张厚兴
# @Site：
# @File:new-obj.py
# @Software:PyCharm


class Pepole(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eatting' % self.name)

    def sleep(self):
        print('%s is sleepping!' % self.name)

    def drink(self):
        print('%s is drinking!' % self.name)


class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))


class Man(Pepole, Relation):
    # def __init__(self,name, age, money):
    #     #Pepole.__init__(self, name, age) #类方法的重构，经典类的写法
    #     super((Man, self).__init__(name, age, money)#和上面的重构作用相同，在之后的多继承上会带来方便，新式类的方式
    #     self.money = money
    #     print('%s 一出生就有 %s money' %(self.name, self.money))

    def piao(self):
        Pepole.eat(self)
        print('%s is piaoing....20s....done!' % self.name)

    def sleep(self):
        Pepole.sleep(self)
        print('%s 在睡觉！' % self.name)


class Woman(Pepole, Relation):
    def give_birth(self):
        print('%s 正在生孩子' % self.name)


m1 = Man('xiaoxiao', 22)
w1 = Woman('mimi', 24)


print(m1.make_friends(w1))
# print(w1.sleep())
