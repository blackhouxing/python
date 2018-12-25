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

exit_flag = False
while not exit_flag:
    for i in menu:
        print(i)
    choice = input('---choice1----按q退出:')
    if choice in menu:
        while not exit_flag:
            for i2 in menu[choice]:
                print(i2)
            choice2 = input('---choice2-----返回请按b，退出请按q:')
            if choice2 in menu[choice]:
                while not exit_flag:
                    for i3 in menu[choice][choice2]:
                        print(i3)
                    choice3 = input('-----choice3----返回请按b，退出请按q:')
                    if choice3 in menu[choice][choice2]:
                        for i4 in menu[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input('----最后一层----，返回请按b')
                        if choice4 == 'b':
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                    if choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            if choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = True

    elif choice == 'q':
        exit_flag = True


