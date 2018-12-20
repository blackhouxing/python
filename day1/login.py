#登录模块
#作者：houxing
#日期：2018-12-19


user = 'zhanghouxing'
password = '123456zhang'

count = 0

while count < 3:

    login_user = input('请输入用户名：')
    login_pwd = input('请输入密码：')

    if login_user == user and login_pwd == password:
        print('登录成功')
        break

    else:
        print('登录失败，用户名或密码错误！请重试!')
        count += 1

    if count == 3:
        print('输入错误超过3次，账户已被锁定，请联系管理员！')
        break



