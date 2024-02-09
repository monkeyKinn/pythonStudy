# -*- coding: utf-8 -*-

"""
@Time : 2023/5/22 18:57
@Author : 金圣聪
@File : 3.逻辑运算符.py
@Project : pythonStudy
"""

# and ==> 一假即假
'''
特殊情况下的逻辑运算符
    如果 and 左右两边不是比较运算的话，则返回的不是一个布尔类型的值
    如果 and 左边的值 不是 [0, 空字符串, 空列表, None]就返回右边的值,如果是的话就返回左边的值
    
    如果 or 两边不是比较运算的话,则返回的不是一个布尔类型的值
    如果 or 左边的值 是 [0,空字符串,空列表,None] 就返回右边的值,如果不是的话就返回左边的额值
'''
print(100 > 50 and 90 > 200)
# or ==> 一真即真
print(100 < 50 or 90 > 200)

# not 获取到表达式的布尔值以后会翻转布尔值
print(not 100 < 50)

print('----')
print(100 or 200)  # 100
print(100 or 100 > 50)  # 100
print(0 or 200)  # 200
print(0 or 100 > 50)  # True

print(0 or 200)  # 200
print('' or 300)  # 300
print([] or 400)  # 400
print(None or 500)  # 500
