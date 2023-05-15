# _*_ coding : utf-8 _*_
# @Time : 2022/10/18 22:02
# @Author : 金圣聪
# @File : 5.逻辑运算符
# @Project : pythonStudy

# and   与    一假即假           左边恒走  右边只有左边为true的时候,才走 性能优化:在左边是false的时候 右边不走
# or    或    一真即真       左边恒走  右边只有左边为false的时候,才走 性能优化:在左边为true的时候 右边不走
# not   非(取反)

# 性能总结:
#     左边恒判断,
#       当为true的时候 and会判断后面           or 不会
#       当为false的时候 and 不会判断后面        or 会
a = 2
a == 3 and print("你麻麻1")
print("你麻麻2")  and a == 3

b = 3
b == 3 or print("你麻麻3")
print("你麻麻4") or b == 3
