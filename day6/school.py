#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/23 16:31
# @Author:张厚兴
# @Site：
# @File:school.py
# @Software:PyCharm


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print('为学员%s 办理注册手续' % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, tech_obj):
        print('为老师%s 办理注册手续' % tech_obj.name)
        self.teachers.append(tech_obj)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---------info of Teacher:%s ----------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course：%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print('%s is teaching course [%s]' % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ---------info of Student:%s ----------
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade：%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print('%s has paid tuition for $%s' % (self.name, amount))


school = School('ITschool', '朝阳')

t1 = Teacher('lihua', 25, 'M', 10000, 'linux')
t2 = Teacher('zhangxia', 30, 'M', 20000, 'Python')

s1 = Student('huqian', 20, 'F', '00001', 'linux')
s2 = Student('zhangfei', 23, 'M', '00002', 'Python')
t1.tell()
s1.tell()

school.enroll(s1)
school.enroll(s2)
school.hire(t1)
school.hire(t2)

print(school.students)
print(school.teachers)
for i, j in enumerate(school.teachers):
    school.teachers[i].teach()

for stu in school.students:
    print(stu.pay_tuition(5000))
    
