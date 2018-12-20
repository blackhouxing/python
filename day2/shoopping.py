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
result = True
while result == True:
    for i in  enumerate(trade_list,1):
        print(i)

    choice = int(input('请输入商品序号：'))


    if trade_list[choice - 1][1] <= salary:
        shoopping_list.append(trade_list[choice-1])

        salary -= trade_list[choice - 1][1]

        print('已购买商品%s,工资剩余%s', shoopping_list,salary)

        choice_local = input('是否继续y|n？')
        if choice_local == 'y' or choice_local == 'Y':
            result = True
        else:
            result = False
    else:
        print('对不起，金额不足，无法购买！请选择其他产品')

