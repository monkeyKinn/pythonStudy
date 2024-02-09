# -*- coding: utf-8 -*-

"""
@Time : 2023/6/4 23:29
@Author : 金圣聪
@File : 2.return关键词的特征.py
@Project : pythonStudy
"""


# 函数运行到return的时候会退出函数

def test():
    print("函数启动...")
    # 如果return没有返回的话,默认返回None
test()


def test1():
    name = 'jsc'
    num = 1
    info = [{'gender': '女'}, {'age': 18}]
    return name, num, info  # 链式编程


name, num, info = test1()
print(name, num, info)

"""
总结:
    1.可以使用return将函数的结果返回一个变量,也可以直接对函数调用表达式进行打印
    2.函数在运行的过程中遇到return会终止函数
    3.return可以一次返回多个值,并且使用元组进行返回
"""