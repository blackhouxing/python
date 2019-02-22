#author：张厚兴#
#!_*_coding:utf-8_*_

import os
import time
import sys
import datetime

# print(time.process_time())
# print(time.time())#时间戳 1970-1-1 00:00至今的秒数
# print(time.asctime()) #
# # print(time.localtime())
# print(time.ctime())
# # print(sys.path)
#
# string_2_struck = time.strptime('2019/1/14','%Y/%m/%d')
#
# string_2_stamp  = time.mktime(string_2_struck)
# print(string_2_stamp)
# print(time.gmtime(time.time()-86640))
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #转换成制定格式化的本地时间

# x = time.localtime()
# y = time.mktime(x)
# print(x)
# print(y)

# print(datetime.datetime.now())
#
# time.sleep(3)
#
#
# print(datetime.date.fromtimestamp(time.time()))
#
# import random
#
#
# checkcode= ''
#
# for i in range(5):
#     current = random.randrange(0,5)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
#
# print(checkcode)


# print(os.listdir(r"C:\\Python"))
#
# print(os.sep)
#
# print(os.linesep)
# print(os.path.pardir(os.path.abspath(__file__)))


print(sys.platform)
print(sys.path)
sys.stdout.write('please:')