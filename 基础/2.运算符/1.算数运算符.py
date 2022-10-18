# _*_ coding : utf-8 _*_
# @Time : 2022/10/17 23:09
# @Author : 金圣聪
# @File : 2.运算符
# @Project : pythonStudy

a = 3
b = 2
# 5
print(a + b)
# 1
print(a - b)
# 6
print(a * b)
# 1.5
print(a / b)
# 整除,取整
# 1
print(a // b)
# 3.3333333333333335
print(10 / 3)
# 3
print(10 // 3)
# 取余 1
print(a % b)
print(5 % 3)

# 指数(幂) 3^2 = 9
print(a ** b)
# 指数(幂) 2^3 = 8
print(b ** a)

# 字符串在进行加法运算时候会变成拼接 只能是加法代表拼接
c = '123'
d = '456'
print(c + d)

# 在py中,+号两端都是字符串才能拼接
c = '123'
d = 456
# 会报错 : can only concatenate str (not "int") to str
# print(c + d)
# 只能str转int/int转str
# 123456
print(c+str(d))
# 576
print(int(c)+d)

e = '我爱你 你爱我!'
print(e * 3)
