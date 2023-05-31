# -*- coding: utf-8 -*-

"""
@Time : 2023/5/31 20:08
@Author : 金圣聪
@File : 1.列表推导式.py
@Project : pythonStudy
"""

# 生成1-20内偶数序列
data = [item for  # 迭代出来的元素
        item in range(1, 21)  # 迭代的范围 [1,21)
        if item % 2 == 0]  # 迭代的条件
print(data)

# 获取 0-3 序列
data2 = [x for x in range(4)]
print(data2)

# 获取3序列
data3 = [x for x in range(3, 4)]
print(data3)

data4 = [x for x in range(1, 21) if x % 2 != 0]
print(data4)

data5 = [(x, y) for  # 是一个元组
         x in range(1, 3) for
         y in range(3)]
print(data5)

data6 = [x for x in range(1, 101)]
data6 = [data6[x:x + 3] for x in range(0, len(data6), 3)]
print(data6)

a = 2
b = 4
# a, b = b, a
a,b = b, a
# a = a + b  # 1+2
# b = a - b  # 1+2-2
# a = a - b  # 1+2-1-2+2
print(a,b)
