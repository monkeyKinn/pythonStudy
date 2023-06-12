# -*- coding: utf-8 -*-

"""
@Time : 2023/6/12 19:36
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

""""
第一题
    关于 Python 类的继承正确的说法是?(多选)
    A. Python 类无法继承
    B. Python 类可以继承
    C. 可以有多个父类
    D. 只能有一个父类
答: B.C

第二题
    以下代码输出是什么?请给出答案________
    class Parent:
        x = 1
    class Child1(Parent):
        pass
    class Child2(Parent):
        pass
    print(Parent.x, Child1.x, Child2.x)
    Child1.x = 2
    print(Parent.x, Child1.x, Child2.x)
    Child1.x = 3
    print(Parent.x, Child1.x, Child2.x)
答: 1,1,1
    1,2,1
    1,3,1

第三题
    定义一个矩形类
    有长和宽两个实例/对象属性， 还有一个计算面积的方法；
    定义正方形类(继承矩形类)
    有一个方法:调用时打印正方形的边长(是矩形就打印不是正方形);
    正方形类进行实例化，并且获得面积会使用父类的方法
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        """
        计算面积,长乘宽
        :return: 返回面积
        """
        return self.length * self.width


class Square(Rectangle):
    def print_c(self):
        if self.width != self.length:
            print('不是正方形')
        else:
            print(self.length)


my_square = Square(20, 21)
my_square.print_c()
print(my_square.compute_area())
