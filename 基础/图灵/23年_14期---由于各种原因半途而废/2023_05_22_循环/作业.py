# -*- coding: utf-8 -*-

"""
@Time : 2023/5/22 22:11
@Author : 金圣聪
@File : 作业.py
@Project : pythonStudy
"""

"""
第1题
    在循环语句中，___语句的作用是提前 结束 本层循环
    答:  break
第2题
    在循环语句中，___语句的作用是提前 进入 下一次循环
    答:  continue
第3题
    判断题:for循环是否能像while循环那样和break，continue连用（是/否)
    答:  可以
第4题
    代码 for i in range(3):print(i) 的执行结果为_____
    答: (注意:range当只有一个参数的时候,从0开始)
        0
        1
        2
第5题（单选题）
    以下代码的输出结果 for i in [0, 1]: print(i+1)
    A.        B.[2, 1]  C.2      D.0
    1
    2
    答: A
"""
# 第6题
#   使用 while 循环输出 1 2  4 5 6  9 10
print("第6题: ")
a = [1, 2, 4, 5, 6, 9, 10]
i = 0
while i < len(a):
    print(a[i])
    i += 1
print("----------")
# 第7题
#   使用 while 循环输出 1+ 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10的和
b = 1
sum_b = 0
while b <= 10:
    sum_b += b
    b += 1
print(f"第七题: {sum_b}")
print("----------")
# 第8题
#   判断1到10之间的奇偶数，如果是奇数，就输出奇数，如果是偶数，就输出偶数
#   需2种方式答题：while循环的方式，for循环的方式
print("第八题:")
print("Way 1 Start(By While):")
c = 1
while c <= 10:
    # 偶数能被2整除
    if c % 2 == 0:
        print(f"{c}是偶数")
    else:
        # 不能被2整除就是奇数
        print(f"{c}是奇数")
    c += 1
print("Way 1 End.")

print("----------")

print("Way 2 Start(By for):")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}是偶数")
    else:
        # 不能被2整除就是奇数
        print(f"{i}是奇数")
print("Way 2 End.")
