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
