
username = 'zhang'
password = '123456'

def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == 'local':
                print('local认证')
                Username = input('Username:')
                Password = input('Password:')
                if Username == username and Password == password:
                    print('登录成功')
                    return func(*args, **kwargs)
                else:
                    print('用户名或密码错误！')
            elif auth_type == 'ldap':
                print('ldap认证')
                return func(*args, **kwargs)
        return wrapper
    return out_wrapper

@auth('local')
def index():
    print("这是主页")



def home():
    print("这是首页")

@auth('ldap')
def bbs():
    print("这是bbs")


index()
home()
bbs()