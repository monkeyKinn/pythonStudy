# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 20:38
@Author : 金圣聪
@File : 6.集合运算.py
@Project : pythonStudy
"""

num_1 = {1, 2, 3}
num_2 = {3, 4}

# 通过 | 求并集
print(num_1 | num_2)
# 通过 | 求交集
print(num_1 & num_2)
# 通过 | 求差集
print(num_1 - num_2)
