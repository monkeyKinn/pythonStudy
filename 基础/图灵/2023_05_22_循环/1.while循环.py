# -*- coding: utf-8 -*-

"""
@Time : 2023/5/22 20:04
@Author : 金圣聪
@File : 1.while循环.py
@Project : pythonStudy
"""

i = 1
sum_ret = 0
while i <= 100:
    sum_ret += i
    i += 1
print(sum_ret)
# 计算1-100的偶数和
n = 1
sum_n = 0
while n <= 100:
    if n % 2 == 0:
        sum_n += n
    n += 1
print(sum_n)
# 计算1-100之间能被3整除,并能被7整除的累计和
sum_x = 0
x = 1
while x <= 100:
    if x % 3 == 0 and x % 7 == 0:
        sum_x += x
    x += 1
print(sum_x)

f = 1
while f <=5:
    print(f'{f} ---> {f*f}')
    f += 1