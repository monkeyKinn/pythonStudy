# _*_ coding : utf-8 _*_
# @Time : 2022/10/20 22:18
# @Author : 金圣聪
# @File : 6.元组高级
# @Project : pythonStudy

# a_tuple = (1, 2, 3, 4, 5)
# # 元组和列表一样,通过下标访问
# print(a_tuple[0])
# # 元组不可以修改内容
# # a_tuple[4] = 6
# b_tuple = ('',)
# print(a_tuple)
# print(bool(b_tuple))
# print(type(b_tuple))
s = 'Hello World!'
print(s)
# o 字符串里的第4个元素
print(s[4])
# lo W 包含下标 3，不含下标 7
print(s[3:7])
# ello World! 从下标为1开始，取出 后面所有的元素（没有结束位）
print(s[1:])
# Hell 从起始位置开始，取到 下标为4的前一个元素（不包括结束位本身）
print(s[:4])
# el 从下标为1开始，取到下标为5的前一个元素，步长为2（不包括结束位本身）
print(s[1:5:2])
