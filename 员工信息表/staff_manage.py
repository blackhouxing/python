
column = ['staff_id','name','age','phone','dept','enroll_date']
db_file = 'staff_info'


def load_db(db_file):
    #加载员工信息
    data = {}
    for i in column:
        data[i] = []

    with open('staff_info', 'r') as f:
        #转换员工新表格式，从文本转换为字典
        for line in f:
            # print(line)
            staff_id,name,age,phone,dept,enroll_date = line.split(",")
            data['staff_id'].append(staff_id)
            data['name'].append(name)
            data['age'].append(age)
            data['phone'].append(phone)
            data['dept'].append(dept)
            data['enroll_date'].append(enroll_date)
        return data
STAFF_DATA = load_db(db_file)

def op_gt():
    pass

def op_lt():
    pass

def op_eq():
    pass

def op_like():
    pass

def syntax_where(clause):


    '''
    解析where条件，并过滤数据
    :param clause:
    :return:
    '''

    operators = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like,
    }

    for op_key,op_func in operators.items():
        if op_key in clause:
            # print(clause)
            column,val = clause.split(op_key)

            # print(column,val)
            break
    else:
        print("语法错误：where条件只能支持[>,<,=,like]")


def syntax_parser(cmd):
    if cmd.split()[0] in ('find','add','del','update'):
        query_clause,where_clause = cmd.split('where')
        print(query_clause,where_clause)
        syntax_where(where_clause)

    else:
        print("\033[31;1m语法错误：\033[0m\n[find\\add\\del\\update] [columl,,] from [staff_info]")


def main():

    while True:
        cmd = input("[staff_id]:").strip()
        if not cmd:continue
        syntax_parser(cmd)

main()