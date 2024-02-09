# -*- coding: utf-8 -*-

"""
@Time : 2023/5/22 19:00
@Author : 金圣聪
@File : 4.用户登录.py
@Project : pythonStudy
"""

name = input("输入用户名")
pwd = input("输入密码")
if name == 'jsc' and pwd == '520':
    print('success')
else:
    print('账号或密码错误')
