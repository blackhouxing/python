from tabulate import tabulate

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
print(STAFF_DATA)

def save_db():
    f = open("%s.new"%db_file,'w',encoding='utf-8')
    for index,id in enumerate(STAFF_DATA['staff_id']):
        row = []
        for col in COLUMN:
            row.append(STAFF_DATA[col][index])
        f.write(','.join(row))
    f.close()


def print_log(msg,log_type = 'info'):
    if log_type == 'info':
        print(msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m"%msg)

def op_gt(column,condition_val):
    """

    :param column:
    :param condition_val:
    :return:
    """
    match_records = []
    for index,val in enumerate(STAFF_DATA[column]):
        if float(val) > float(condition_val):
            record = []
            for col in COLUMN:
                record.append(STAFF_DATA[col][index])
            match_records.append(record)
    return match_records

def op_lt(column,condition_val):
    match_records = []
    for index,val in enumerate(STAFF_DATA[column]):
        if float(val) < float(condition_val):
            record = []
            for col in COLUMN:
                record.append(STAFF_DATA[col][index])
            match_records.append(record)
    return match_records
def op_eq(column,condition_val):
    match_records = []
    for index,val in enumerate(STAFF_DATA[column]):
        if val == condition_val:
            record = []
            for col in COLUMN:
                record.append(STAFF_DATA[col][index])
            match_records.append(record)
    return match_records

def op_like(column,condition_val):
    match_records = []
    for index,val in enumerate(STAFF_DATA[column]):
        if condition_val in val:
            record = []
            for col in COLUMN:
                record.append(STAFF_DATA[col][index])
            match_records.append(record)
    return match_records

def syntax_find(data_set,query_clause):
    """

    :param data_set:
    :param query_clause:
    :return:
    """
    filter_cols_temp = query_clause.split("from")[0][4:].split(',')
    # print(filter_cols_temp)
    filter_cols = [i.strip() for i in filter_cols_temp] #干净的查询条件
    if '*' in filter_cols[0]:
        print(tabulate(data_set,headers=filter_cols,tablefmt="grid"))
    else:

        reformat_data = []
        for row in data_set:
            filtered_vals = []
            for col in filter_cols:
                col_index = COLUMN.index(col)
                filtered_vals.append(row[col_index])
            reformat_data.append(filtered_vals)

        # for i in reformat_data:
        #     print(i)
        print(tabulate(reformat_data,headers=filter_cols,tablefmt="grid"))
    print_log("匹配到%s条数据！"%len(data_set))
def syntax_update(data_set,query_clause):
    """

    :param data_set:
    :param query_clause: update staff_table set age=25
    :return:
    """

    formula_raw = query_clause.split('set')
    if len(formula_raw) >1:
        col_name,new_val = formula_raw[1].strip().split('=')
        # col_index = COLUMN.index(col_name)
        # print(data_set)
        for match_row in data_set:
            staff_id = match_row[0]
            staff_id_index = STAFF_DATA['staff_id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val

        print(STAFF_DATA)
        save_db()
        print_log("成功修改了%s条数据！"%len(data_set))
    else:
        print_log("语法错误：未检测到set关键字！",'error')

def syntax_add():
    pass

def syntax_delete(data_set,query_clause):
    print("这是删除操作")

def syntax_where(clause):
    operator = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like,
        }
    for op_key,op_func in operator.items():
        if op_key in clause:
            column,condition = clause.split(op_key)
            match_data = op_func(column.strip(),condition.strip())

            return match_data

    else:
        print_log("语法错误：where条件只能支持[>,<,=，like]","error")

def syntax_parser(cmd):
    """

    :param cmd:
    :return:
    """
    syntax_list = {
        'find':syntax_find,
        'del':syntax_delete,
        'update':syntax_update,
        'add':syntax_add,
        }

    if cmd.split()[0] in ('find','add','delete','update'):
        if 'where' in cmd:

            query_clause,where_clause = cmd.split('where')
            # print(query_clause,where_clause)
            match_records = syntax_where(where_clause)
        else:
            match_records = []
            for index,staff_id in enumerate(STAFF_DATA['staff_id']):
                record=[]
                for col in COLUMN:
                    record.append((STAFF_DATA[col][index]))
                match_records.append(record)

            query_clause = cmd
        cmd_action  = cmd.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](match_records,query_clause)


    else:
        print_log("语法错误：[find\\add\\del\\update] [column,,] from [staff_info] where [condition]","error")



def main():
    while True:
        cmd = input("[staff_data]:").strip()
        # print(cmd)
        if not cmd:continue
        syntax_parser(cmd.strip())
main()










