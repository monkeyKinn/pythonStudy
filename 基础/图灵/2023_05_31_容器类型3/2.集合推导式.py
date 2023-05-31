# -*- coding: utf-8 -*-

"""
@Time : 2023/5/31 20:30
@Author : 金圣聪
@File : 2.集合推导式.py
@Project : pythonStudy
"""
a = {x for x in range(1, 21) if x % 2 == 0}
print(type(a))
print(a)
# 跟列表序列一样