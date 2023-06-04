# -*- coding: utf-8 -*-

"""
@Time : 2023/6/4 23:24
@Author : 金圣聪
@File : 1.函数返回值.py
@Project : pythonStudy
"""


def add(n1: int, n2: int) -> int:
    return n1 + n2
    # 函数必须要有return,如果没有的话,默认return None

sum = add(1, 2)
print(sum)
