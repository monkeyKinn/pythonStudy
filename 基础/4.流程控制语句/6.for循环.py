# _*_ coding : utf-8 _*_
# @Time : 2022/10/19 21:36
# @Author : 金圣聪
# @File : 6.for循环
# @Project : pythonStudy

# 循环字符串
# range(5)
# range(1, 6)
# range(1, 10, 3)
# 循环一个列表

# for循环
# 格式:
# for 变量 in 要遍历的数据
#     方法体


# 遍历
s = 'china'
# 在字符串中 变量i代表字符 代表要操作的数据
for i in s:
    print(i)
print()

# 循环列表
# 场景  爬出了一个列表给我们
name = ['小a', '小臂', '小c', 1]
# 遍历列表
for i in name:
    print(i)
print()
# 遍历下标
print('获取name[]长度:%d' % len(name))
print('遍历下标')
for i in range(len(name)):
    print(i)
print()

# range(5) 从0开始到5结束,[0,5)
# range方法的结果 一个可以遍历的对象
for i in range(5):
    print(i)
print()

# range(1,6) [1,6)
for i in range(1, 6):
    print(i)
print()

# range(起始值,结束值,步长) [起始值,结束值) 步长3:  1,1+3=4,4+3=7,7+3=10
for i in range(1, 11, 3):
    print(i)
print()

# tuple 元组
tu = (99, '22')
for i in tu:
    print(i)
for i in range(len(tu)):
    print(i)