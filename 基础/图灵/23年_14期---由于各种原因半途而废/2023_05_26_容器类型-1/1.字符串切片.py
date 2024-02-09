# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 0:25
@Author : 金圣聪
@File : 1.字符串切片.py
@Project : pythonStudy
"""

data = 'abcdef'
# 字符串切片 def
print(data[3:])

# 起始位(默认为0):结束下标位置(不包含结束下标位本身,所以要+1):步长(间隔[步长-1]个值取一次),如果是负数就是从右往左
print(data[0:3]) #等价于 data[:3]
# print(data[:3])
print(data[3: 5]) #de
print(data[1: -1: 3])
print(data[5: 1: -2])
