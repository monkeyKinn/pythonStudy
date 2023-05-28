# -*- coding: utf-8 -*-

"""
@Time : 2023/5/22 22:01
@Author : 金圣聪
@File : 5.作业.py
@Project : pythonStudy
"""

"""
第一题:
    Python 中用于表示逻辑与、逻辑或、逻辑非运算的关键字分别是_________、___________、_________
    答:  1.and
         2.or
         3.not
第二题（单选题):
    在 if...elif...else 的多个语句块中只会执行一个语句块？ 
        A.  正确。    B.  错误。 C.  根据条件决定。 D.  Pyhton 中没有 elif 语句
    答: C

第三题:
    语句 x = (3==3, 5) 执行结束后，变量 x 的值为?
    答: (True, 5)

第四题:
    写一个登录程序,要求用户输入用户名和密码，用户名和密码正确则打印字符串'登录成功'，否则打印字符串'登录失败'。
"""
# NO.4

name = input('输入用户名:')
pwd = input('输入密码:')

local_name = 'admin'
local_pwd = 'Admin@2023'

if local_name == name and local_pwd == pwd:
    print('登录成功~')
else:
    print('登录失败~')
