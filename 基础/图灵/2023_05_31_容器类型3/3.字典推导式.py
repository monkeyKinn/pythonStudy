# -*- coding: utf-8 -*-

"""
@Time : 2023/5/31 20:32
@Author : 金圣聪
@File : 3.字典推导式.py
@Project : pythonStudy
"""

# 获取1-10的key值作为当前序列值 value为当前key的平方
dict_data = {x: x ** 2 for x in range(1, 11)}
print(dict_data)

# 获取1-10的key值作为当前序列值 value为当前key+1
dict_data1 = {x: x + 1 for x in range(1, 11)}
print(dict_data1)
