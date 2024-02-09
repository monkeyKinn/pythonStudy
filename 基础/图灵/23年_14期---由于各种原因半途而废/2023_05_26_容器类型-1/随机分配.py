# -*- coding: utf-8 -*-

"""
@Time : 2023/5/30 22:27
@Author : 金圣聪
@File : 随机分配.py
@Project : pythonStudy
"""
import random

offices = [[], [], []]
teachers = ['t1', 't2', 't3', 't4', 't5', 't6', 't7']
# 随机分到教室里
for teacher in teachers:
    office_idx = random.randint(0, 2)
    offices[office_idx].append(teacher)

for idx, office in enumerate(offices):
    # print(idx, office)
    print(f'No.{idx+1} 教室有{len(office)}个老师,分别为以下老师"')
    for teacher in office:
        print(teacher, end=" ")
    print('\n')
    print('*' * 20)

