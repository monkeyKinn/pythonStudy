# -*- coding: utf-8 -*-

"""
@Time : 2023/5/17 21:40
@Author : 金圣聪
@File : 8.格式化输出.py
@Project : pythonStudy
"""

# 用占位符完成字符串输出
age = 10
print('今年%d岁,哈哈' % age)
name = 'jsc'
print('我叫%s' % name)

# 会四舍五入
pi = 3.1415926
print('圆周率 %.2f' % pi)

print(f'圆周率 {pi}')

# 用format方法进行字符串格式化
print('年龄{}'.format(age))

# 用f表达式
print(f'年龄{age}')

