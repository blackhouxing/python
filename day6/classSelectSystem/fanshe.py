#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/5/7 17:06
# @Author:张厚兴
# @Site：
# @File:fanshe.py
# @Software:PyCharm

#
# class Dog():
#     def __init__(self):
#         self.name = "zhanghouxing"
#
#     def eat(self):
#         print("%s is eatting..." % self.name)
#
#
# choice = input(">>:").strip()
#
#
# d = Dog()
#
# # print(hasattr(d, choice))
# # print(hasattr(d, "name"))
# # print(hasattr(d, "eat"))
# # setattr(d, "eat", "chihao")
# setattr(d, "name", "huaxia")
# # func = getattr(d, choice)
# # print(func())
# func = getattr(d, "eat")
# # print(func())
# nstr = getattr(d, "name")
# # print(nstr)
# delattr(d, "name")
# if hasattr(d, "name"):
#     nfunc = getattr(d, "eat")
#     print(nfunc())
# else:
#     print("参数已被删除！")


# names = ['hu', 'xia']
# data = {}
#
#
# try:
#     # names[3]
#     data['name']
# except Exception as e:
#     print("出错误", e)
#
# # except (IndexError, KeyError) as e:
# #     print("没有你查找的index", e)

class ZhanghouxingException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return "asdfadf "


try:
    raise ZhanghouxingException('我的异常')
except ZhanghouxingException as e:
    print(e)
    