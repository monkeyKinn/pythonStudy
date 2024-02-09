# _*_ coding : utf-8 _*_
# @Time : 2022/10/24 23:12
# @Author : 金圣聪
# @File : 2.函数的参数
# @Project : pythonStudy

# 使用函数计算1+2的和
def sum_self(a, b):
    print(a, b)
    print(a + b)


# 位置传参
sum_self(2, 2)

# 关键字传参 不常用
sum_self(b=9, a=1)
