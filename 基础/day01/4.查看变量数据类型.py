# _*_ coding : utf-8 _*_
# @Time : 2022/10/16 23:53
# @Author : 金圣聪
# @File : 4.查看变量数据类型
# @Project : pythonStudy


# int
# float
# boolean
# string
# list
# tuple
# dict

a = 1
print(a)
# <class 'int'>
print(type(a))

b = 1.2
print(b)
# <class 'float'>
print(type(b))

c = "c"
print(c)
# <class 'str'>
print(type(c))

d = True
print(d)
# <class 'bool'>
print(type(d))

e = [1, "2"]
print(e)
# <class 'list'>
print(type(e))

f = (1, "f")
print(f)
# <class 'tuple'>
print(type(f))

g = {"name": "jsc", "age": 20}
print(g)
# <class 'dict'>
print(type(g))
