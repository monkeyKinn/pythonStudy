# -*- coding: utf-8 -*-

"""
@Time : 2023/6/25 15:37
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

"""
第一题
    写一个登录装饰器对以下函数进行装饰，要求输入账号和密码才能运行该函数
    （代码写好注释）
    def run():
        print('开始执行函数')
"""


def login(func):
    """
    定义一个登录装饰器
    :param func: 接收的函数
    :return: 无返回
    """

    def wrapper():
        # 从键盘接收账号和密码
        name = input('请输入账号: ')
        pwd = input('请输入密码: ')
        # 假定账号和密码分别为 ‘jsc’ 和 ‘520’
        if name == 'jsc' and pwd == '520':
            # 输入正确时，调用装饰器接收的函数
            func()
        else:
            # 输入错误时,打印错误日志
            print('账号或密码错误')

    # 返回内层函数[wrapper]的引用
    return wrapper


# 使用装饰器语法糖
@login
def run():
    # 打印
    print("开始执行函数")


# 无感调用原函数
run()
