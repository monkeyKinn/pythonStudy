# -*- coding: utf-8 -*-

"""
@Time : 2023/6/20 0:15
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

"""
第一题
    以下代码的打印结果是
    （规定:不用python解释器运行获得结果，通过大脑思考获得答案）
    def func1(x):
        def func2(y):
            return x*y
        return func2
    func2=func1(3)
    print(func2(2))
    
    A.2
    B.3
    C.6
    D.8
    
答: C

第二题
    以下代码的打印结果是
    （规定:不用python解释器运行获得结果，通过大脑思考获得答案）
    def func1(x):
        a = 5
        def func2():
            return x*a
        return func2
    func2=func1(3)
    print(func2())
    
    A.5
    B.15
    C.3
    D.None
    
答: B

第三题
    写一个闭包函数，并说明每一行代码的含义。
"""


def homework(somebody_name):
    """
    作业方法.
    :param somebody_name: 第一个拿到作业的人
    :return:返回send_homework函数的引用
    """
    def send_homework(someone_name):
        """
        定义一个函数,作用是把本来是somebody_name的作业给someone_name
        :param someone_name: 最终拿到作业的人
        :return: 一个 字符串,大意是:把本来是somebody_name的作业给someone_name
        """
        return f"This is {someone_name}'s homework,not {somebody_name}'s"

    # 返回 someone_homework函数的引用
    return send_homework


jsc_hw = homework('Jsc')
hw_info = jsc_hw('Wsx')
print(hw_info)
