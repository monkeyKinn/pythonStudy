# -*- coding: utf-8 -*-

"""
@Time : 2023/5/31 20:37
@Author : 金圣聪
@File : 4.拆包.py
@Project : pythonStudy
"""
nums = [1, 2, 3, 4]
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]
num4 = nums[3]
print(num1, num2, num3, num4)

# 拆包
num1, num2, num3, num4 = nums
print(num1, num2, num3, num4)

num_list = [[1, 2], [3, 4]]
n1, n2 = num_list
m1, m2 = n1
m3, m4 = n2
print(m1, m2, m3, m4)

# 元组 同
# 集合 同
'''
拆包过程中 需要注意:
    1.变量位置和元素位置 必须一致
    2.变量个数与元素个数 必须一致
'''
data = [1, 2, 3]
n2, n1, n3 = data
print(n2, n1, n3)

info = {
    'name': 'jsc',
    'age': 18
}

name, age = info.values()
print(name, age)
name, age = info.keys()
print(name, age)

# 需要对当前的字典进行整体拆包
for item in info.items():
    print(item)
for k, v in info.items():
    print(k, v)
