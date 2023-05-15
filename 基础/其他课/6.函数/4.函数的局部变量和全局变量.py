# _*_ coding : utf-8 _*_
# @Time : 2022/10/24 23:29
# @Author : 金圣聪
# @File : 4.函数的局部变量和全局变量
# @Project : pythonStudy

# 局部变量:在函数内部定义,在内部生效
# 全局变量:在文件里定义,在函数外也能生效

# def f1():
#     a = 1
#     print(a)
# 作用域范围在函数内部所以报错
# print(a)

a = 1


def f2():
    b = a+1
    print(b)

f2()
print('++++++++++++++')
print(a)
