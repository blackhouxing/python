#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/2 17:55
# @Author:张厚兴
# @Site：
# @File:main.py
# @Software:PyCharm


def jiajian():
    pass


def chengchu():
    pass


operator = {'+': lambda a, b: float(a) + float(b),
            '-': lambda a, b: float(a) - float(b),
            '*': lambda a, b: float(a) * float(b),
            '/': lambda a, b: float(a) / float(b),
            }
# for i in operator:
#     print(operator[i])


import re

exp_str = "1 - 2 * ( (60-30 +(-40/5)*(9-2*5/3 +7/3*99/4*2998 +10*568/14)) - (-4*3)/(16-3*2) )"


res1 = re.search(r'\([^()]+\)', exp_str, flags=re.MULTILINE).group()
print(res1)
res2 = re.search(r'[^(]+[^)$]', res1).group()
# print(res2)

operatorRes = re.search(r'[\*/]', res2).group()
# print(operatorRes)
numbList = re.split(operatorRes, res2)
# print(numbList)
a = numbList[0]
b = numbList[1]


if operatorRes in operator:
    res3 = operator[operatorRes](a, b)
    print(type(res3))
    res3 = str(int(res3))


new_str = re.sub(res1, res3, exp_str)

exp_str = new_str
print(exp_str)



