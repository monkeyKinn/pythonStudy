# -*- coding: utf-8 -*-

"""
@Time : 2023/7/3 14:04
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

"""
第一题（单选题）
    以下哪个代码是正确的读取一个文件？
    A. f = open("test.txt", "read")
    B. f = open("r","test.txt")
    C. f = open("test.txt", "r")
    D. f = open("read","test.txt")
答：C

第二题
    Python 内置函数_____用来打开或创建文件并返回文件对象
答：open()

第三题（单选题）
    python中用来抛出异常的关键字是（）
    A.try
    B.except
    C.raise
    D.finally
答：C

第四题
通过异常捕获获得以下字符串里面的字母字符
str_1='d52a733i2327ha244i982d23s553b245'
"""
print("第四题如下:")
str_1 = 'd52a733i2327ha244i982d23s553b245'
result = ''
for item in str_1:
    try:
        int(item)
    except:
        result += item
        pass
print(result)
