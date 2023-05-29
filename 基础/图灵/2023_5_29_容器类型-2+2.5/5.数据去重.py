# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 20:24
@Author : 金圣聪
@File : 5.数据去重.py
@Project : pythonStudy
"""

nums = {1,2,3,3,2,1,4,5,6,7,7}
print(nums)


# 不同的数据结构是可以进行类型互转的
stu_info = ['jsc','小吴','jsc','皮卡丘']
print(stu_info)
new_stu_info = set(stu_info)
print(list(new_stu_info))



# 如果不是可迭代对象不能强转类型

