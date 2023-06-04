# -*- coding: utf-8 -*-

"""
@Time : 2023/6/5 0:25
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

"""
第一题
    Python 中定义函数的关键字是____
答: def
第二题
    如果函数中没有 return 语句，那么该函数的返回值为___
答: None

第三题
    代码 def a(): pass 含义是？
        A. 定义一个列表，并初始化它。
        B. 定义一个函数，但什么都不做。
        C. 定义一个函数，并传递参数。
        D. 定义一个空的类。
答: B

第四题
    定义一个函数，计算1到990的和，用for循环完成
"""


def fuc_sum():
    result = 0
    for i in range(1, 991):
        result += i
    return result


print(f'第四题:{fuc_sum()}')

"""
第五题
    输入三个数字，写一个函数将三个数字从小到大输出
"""
n1 = input('请输入第1个数字:')
n2 = input('请输入第2个数字:')
n3 = input('请输入第3个数字:')

nums = [int(n1), int(n2), int(n3)]


def bubble_sort(nums):
    """
    冒泡排序
    :param nums: 需要排序的数字列表
    :return:
    """
    # 冒泡排序的次数
    for i in range(len(nums) - 1):
        # j是列表下标
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble_sort(nums))
