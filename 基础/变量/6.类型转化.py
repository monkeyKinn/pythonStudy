# _*_ coding : utf-8 _*_
# @Time : 2022/10/17 0:15
# @Author : 金圣聪
# @File : 6.类型转化
# @Project : pythonStudy

# 转换为整型
# str -> int

a = '123'
print(type(a))
# 强转
b = int(a)
print(type(b))

# float -> int
# 如果把 float 转换为 int  返回的是小数点前面的数 (取整)
c = 1.6
print(type(c))
d = int(c)
print(d)
print(type(d))

# bool 转换为 int
# true->1
# false->0
e = False
f = int(e)
print(f)
print(type(f))

# 字符串中有非法字符是不能转的
# g = '1.63'
# print(type(g))
# h = int(g)
# print(h)

# i = '12ab'
# print(type(i))
# print(type(int(i)))

# 转换为浮点数
# 在爬虫时候大部分是字符串类型
g = '12.34'
print(g)
print(type(g))
f_g = float(g)
print(f_g)
print(type(f_g))


h = 666
f_h = float(h)
print(f_h)
# 666.0
print(type(f_h))

# 转换为字符串
# 大部分情况下 是整型转换为字符串 页码的拼接
# i = 80
# print(i)
# print(type(str(i)))

# 浮点数转换为字符串
# i = 80.8
# print(i)
# print(str(i))
# print(type(str(i)))

# 将布尔类型转换为字符串,就是本身的字符
i = True
print(i)
print(str(i))
print(type(str(i)))

# 转换为bool
j = 1
print(type(j))
# 把整数转换为bool类型的数据
b_j = bool(j)
# True 非0(整数/负数)的都是True
print(b_j)
# <class 'bool'>
print(type(b_j))

j = 5
# 把整数转换为bool类型的数据
b_j = bool(j)
# True
print(b_j)
# <class 'bool'>
print(type(b_j))
j = 0
# 把整数转换为bool类型的数据
b_j = bool(j)
# False
print(b_j)
# <class 'bool'>
print(type(b_j))

j = 0.0
# 把整数转换为bool类型的数据
b_j = bool(j)
# False
print(b_j)
# <class 'bool'>
print(type(b_j))

j = ' '
# 把整数转换为bool类型的数据
b_j = bool(j)
# False
print(b_j)
# <class 'bool'>
print(type(b_j))

# 列表
j = [""]
# 把整数转换为bool类型的数据
b_j = bool(j)
# True
print(b_j)
print(111111)
# <class 'bool'>
print(type(b_j))

j = ('')
# 把整数转换为bool类型的数据
b_j = bool(j)
# False
print(b_j)
# <class 'bool'>
print(type(b_j))

j = {''}
# 把整数转换为bool类型的数据
b_j = bool(j)
# False
print(b_j)
# <class 'bool'>
print(type(b_j))

# 什么情况下为false
print('什么情况下为false(9种)')
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(("")))
print(bool(('')))
