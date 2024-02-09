# _*_ coding : utf-8 _*_
# @Time : 2022/10/18 22:27
# @Author : 金圣聪
# @File : 1.输出
# @Project : pythonStudy

# 普通输出
print('故事里的小黄花,从出生那年就开着')

# 格式化输出
# scrapy框架 的时候  excel mysql redis
age = 18
name = 'jsc'
# 字符串不能+整数 必须转
print('我的年龄是' + str(age))

# %s 代表字符串 %d 代表数值
print('我的名字是%s,我的年龄是%d' % (name, age))

# 还可以这么写    f'{},{}'
a, b = 10, 11.1
print(f'a={a},b={b}')