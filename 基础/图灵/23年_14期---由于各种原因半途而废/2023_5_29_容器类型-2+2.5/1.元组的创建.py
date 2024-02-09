# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 20:02
@Author : 金圣聪
@File : 1.元组的创建.py
@Project : pythonStudy
"""
data = (1, 2, 3)
print(type(data))

# 如果当前元组中只有一个元素,则需要在这个元素后面加,
data_1 = (1,)
print(type(data_1))

# 申明元组 1
data_2 = ()
print(type(data_2))

# 申明元组 2
data_2 = tuple()
print(type(data_2))