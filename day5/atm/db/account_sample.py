
import json

acc_dic = {
    'id':1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_date':'2017-01-10',
    'expire_date':'2020-01-10',
    'pay_day':10,
    'status':0 #0 = normal,1 = locked,2 = disabled

}
print(json.dumps(acc_dic))