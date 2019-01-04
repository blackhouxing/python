#author:zhanghouxing
#time:2018-12-25

menu = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

import chardet
with open('test.txt','rb') as f:
#
#     f.seek(4)
#     line = f.readline()
#
#     print(line)
#     f.seek(10)
#     a = f.tell()
#
#     print(a)



chardet.detect(f)
print(chardet.detect(f))