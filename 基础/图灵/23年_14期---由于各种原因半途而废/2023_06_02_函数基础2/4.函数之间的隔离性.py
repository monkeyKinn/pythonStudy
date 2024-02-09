# -*- coding: utf-8 -*-

"""
@Time : 2023/6/4 23:52
@Author : 金圣聪
@File : 4.函数之间的隔离性.py
@Project : pythonStudy
"""


def test1():
    num1 = 10
    print(num1)

# 再函数中定义的变量不能被共享
num1 = 100
def test1():
    print(num1)

def test2():
    print(num1)

test2()
test1()


"""
global用于不可变对象
不可变对象:
    数字类型
    bool
    str
    tuple(元组)
    
    
    
可变对象:
    list dict set
    
容器类型2的课件中有
"""