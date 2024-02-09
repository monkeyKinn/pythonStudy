# -*- coding: utf-8 -*-

"""
@Time : 2023/6/13 22:23
@Author : 金圣聪
@File : 进阶作业.py
@Project : pythonStudy
"""

"""

第一题（单选题）
    以下代码的输出结果是
    class A:
        def __init__(self, i = 1):
    
            self.i = i
    class B(A):
        def __init__(self, j = 2):
            super().__init__()
            self.j = j
    b = B()
    print(b.i,b.j)
    
    A.0 1
    B.0 0
    C.1 2
    D.0 2
答: C

第二题（多选题）
    以下说法正确的是
    A.对象是特征与技能的结合体,而类则是一系列对象相同的特征与技能的结合体
    B.对象是具体存在的事物,而类则一个抽象的概念
    C.在现实世界中:先有一个个具体存在的对象,然后随着人类文明的发展才总结出类的概念
    D.站在不同的角度总结出的类与对象是不同的
答: A,B,(C),D


第三题
    定义一个人们类作为父类，学生类继承这个人们类作为子类。
    父类有一个__init__方法是可以生成对象的名字,年龄,性别属性，
    子类（学生类）重写__init__方法，
        在重写的__init__方法里面，子类（学生类）的__init__方法除了有父类的名字,年龄,性别的属性，
        还有一个派生的属性:分数属性。
    
    实例化学生类，打印学生对象的姓名,年龄,性别,分数属性。
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, score):
        super().__init__(name, age, gender)
        self.score = score

    def print_info(self):
        print(f'My name is: {self.name}.I am {self.age} years old,I am a {self.gender},and my score is: {self.score}')


student_1 = Student('jsc', 18, 'man', 99)
student_1.print_info()
