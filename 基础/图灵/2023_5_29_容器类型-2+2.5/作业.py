# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 22:14
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

'''
第一题
    L = ['a','b','c','d']
    将L列表转换成元组，里面的元素不变
'''
print("No.1:")
L = ['a', 'b', 'c', 'd']
my_tuple = tuple(L)
print(type(my_tuple), f' ,and my_tuple:{my_tuple}')

'''
第二题
    对以下列表元素进行去重（提示用for循环和if判断）

    info =[
        {'name':'dahai','age':18},
        {'name':'xialuo','age':78},
        {'name':'xishi','age':8},
        {'name':'dahai','age':18},
        {'name':'dahai','age':18}
    ]

    得到结果:[{'name': 'dahai', 'age': 18}, {'name': 'xialuo', 'age': 78}, {'name': 'xishi', 'age': 8}]
'''

info = [
    {'name': 'dahai', 'age': 18},
    {'name': 'xialuo', 'age': 78},
    {'name': 'xishi', 'age': 8},
    {'name': 'dahai', 'age': 18},
    {'name': 'dahai', 'age': 18},
]

print("No.2:")
result = list()
for element in info:
    if element not in result:
        result.append(element)
print(result)
unique_info = list(set(tuple(sorted(d.items())) for d in info))
result = []
for i in unique_info:
    result.append(dict(i))
print(result)