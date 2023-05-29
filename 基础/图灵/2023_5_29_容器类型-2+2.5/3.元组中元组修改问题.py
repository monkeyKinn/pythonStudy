# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 20:08
@Author : 金圣聪
@File : 3.元组中元组修改问题.py
@Project : pythonStudy
"""
nums = (1, 2, 3)
# nums[1] = 4 # 元组中的元素不能修改

print(nums)

nums_1 = (1, [2, 3], 3)
nums_1[1][1] = 1  # 元组中的值的修改问题其实是类型问题
print(nums_1)

'''
在python中有些类型是不能改的
 元组
 布尔
 字符串
 数字类型
    int float 复数
当前元组与列表的使用方式相似
    元组主要功能是保护数据安全
'''

# 函数的返回值
