COLUMN = ['staff_id','name','age','phone','dep','enroll_date',]
db_file = 'staff_db'

def load_db(db_file):
    data = {}
    for i in COLUMN:
        data[i] = []

    with open(db_file,'r') as f:
        for line in f:
            staff_id,name,age,phone,dep,enroll_date = line.split(',')
            data['staff_id'].append(staff_id)
            data['name'].append(name)
            data['age'].append(age)
            data['phone'].append(phone)
            data['dep'].append(dep)
            data['enroll_date'].append(enroll_date)
        # print(data)
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

def syntax_find():
    pass

def syntax_update():
    pass

def syntax_add():
    pass

def syntax_delete():

    pass

def syntax_where(where_clause):
    pass

def syntax_parser(cmd):
    if cmd.split()[0] in ('find','add','delete','update'):
        query_clause,where_clause = cmd.split('where')
        # print(query_clause,where_clause)
        syntax_where(where_clause)
    else:
        print("\033[31:1m语法错误：\033[0m\n[find\\add\\del\\update] [column,,] from [staff_info] where [condition]")



def main():
    while True:
        cmd = input("[staff_data]:").strip()
        # print(cmd)
        if not cmd:continue
        syntax_parser(cmd)
main()










