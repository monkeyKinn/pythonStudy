# -*- coding: utf-8 -*-

"""
@Time : 2023/5/29 21:08
@Author : 金圣聪
@File : 8.字典也是可迭代对象.py
@Project : pythonStudy
"""
stu_info = {
    'name': '安娜',
    'age': 18,
    'address': '长沙'
}
# 直接迭代字典只能获取字典的key
for s in stu_info:
    print(s)
print('*' * 20)
for i in stu_info.values():
    print(i)
print('*' * 20)
for i in stu_info.items():
    # 是一个元组,是key和value
    print(i)

print('*' * 20)
# 元组拆包
for key, value in stu_info.items():
    print(key, value)
