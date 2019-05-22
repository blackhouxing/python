#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# @Time:2019/4/29 16:34
# @Author:张厚兴
# @Site：
# @File:select_system.py
# @Software:PyCharm


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.teachers = []
        self.students = []
        self.course = []
        self.grade = []

    def mam_grade(self):
        grade = Grade(grade_name, teacher, course)
        self.grade.append(grade)
        print('Grade:%s create seccessful ' % grade)
        return grade

    def mam_mem(self):
        teacher = Teacher(staff_id, nam)

    def mam_course(self):
        pass


class Grade(object):
    def __init__(self, grade_name, teacher, course):
        self.grade_name = grade_name
        self.teacher = teacher
        self.course = course


class Course(object):
    def __init__(self, course_name, period, tuition):
        self.course_name = course_name
        self.period = period
        self.tuition = tuition


class Mem(object):
    def __init__(self, name, age, sex)
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(Mem):
    def __init__(self, staff_id, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.staff_id = staff_id
        self.salary = salary
        self.course = course


class Student(Mem):
    def __init__(self, stu_id, name, age, sex):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
