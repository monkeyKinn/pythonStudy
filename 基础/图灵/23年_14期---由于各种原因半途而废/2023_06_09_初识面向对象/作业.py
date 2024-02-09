# -*- coding: utf-8 -*-

"""
@Time : 2023/6/10 0:14
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""
""""
第一题
    Python 使用____________________关键字来定义类
答: class

第二题(单选题)
    class Teacher:
        name = '大海'
        age = 18
        sex = '男'
    已知上面定义的类Teacher
    以下哪一个是添加类的属性
    A.print(Teacher.name)
    B.Teacher.name = '夏洛'
    C.Teacher.play = '篮球'
    D.del  Teacher.name
答: C

第三题
    声明一个矩形类
    实例化对象属性：长、宽
    方法：计算周长和面积，创建不同的矩形，并且打印其周长和面积
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_circumference(self):
        """
        计算周长,长加宽的和乘2
        :return:返回周长
        """
        return (self.length + self.width) * 2

    def compute_area(self):
        """
        计算面积,长乘宽
        :return: 返回面积
        """
        return self.length * self.width


r1 = Rectangle(10.5, 20)
r2 = Rectangle(30, 40)
r3 = Rectangle(5, 6)
print(f'area: {r1.compute_area()}, circumference: {r1.compute_circumference()}')
print("*" * 20)
print(f'area: {r2.compute_area()}, circumference: {r2.compute_circumference()}')
print("*" * 20)
print(f'area: {r3.compute_area()}, circumference: {r3.compute_circumference()}')

"""
第四题
定义一个Student类，有姓名、年龄，性别（实例/对象属性），定义一个自我介绍的方法，可以打印出自己的姓名，年龄和性别的信息。
"""
print('*' * 20 + '第四题' + '*' * 20)


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_self(self):
        print(f'My name is : {self.name},I am {self.age} years old,and I am a {self.gender}')


jsc = Student('jsc', 18, 'man')
wsx = Student('wsx', 16, 'woman')
jsc.print_self()
wsx.print_self()
