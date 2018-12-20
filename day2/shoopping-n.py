#shoopping
#author :zhanghouxing
#日期：2018-12-20


trade_list = [['shoots',300],
              ['bick',1000],
              ['hat',100],
              ['iphone',5000],
              ['MAC',14000]]

shoopping_list = []

salary = float(input('请输入您的工资：'))

while  True:
    for index,item in  enumerate(trade_list,1):
        print(index,item)

    user_choice = input('请输入商品序号(退出请按q|Q)：')
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice <= len(trade_list) and user_choice >0:
            if trade_list[user_choice - 1][1] <= salary:
                shoopping_list.append(trade_list[user_choice - 1])
                salary -= trade_list[user_choice - 1][1]
                print('已购买商品{},工资剩余{}'.format(shoopping_list,salary))
            else:
                print('对不起，金额不足，无法购买！请选择其他产品')
        else:
            print('抱歉,没有您选择的商品，请选择正在出售的商品！')

    elif user_choice == 'q' or user_choice == 'Q':
        print('您购买的商品为：')
        for i in enumerate(shoopping_list,1):
            print(i)
        print('您的存款还剩：',salary)
        exit()
    else:
        print('输入错误！')

