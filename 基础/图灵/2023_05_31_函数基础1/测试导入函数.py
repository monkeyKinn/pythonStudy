# -*- coding: utf-8 -*-

"""
@Time : 2023/5/31 21:17
@Author : 金圣聪
@File : 测试导入函数.py
@Project : pythonStudy
"""

# 这是引用一个方法,并重命名(也可以不命名)
from my_func import my_test as a
# 这是引用一个文件中的所有方法,用点 . 的形式调用所有方法
import my_func as b

a()
b.my_testG()
