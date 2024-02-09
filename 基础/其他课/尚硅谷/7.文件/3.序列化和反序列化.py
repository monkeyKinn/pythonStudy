# _*_ coding : utf-8 _*_
# @Time : 2022/10/25 23:22
# @Author : 金圣聪
# @File : 3.序列化和反序列化
# @Project : pythonStudy

fp = open('text.txt', 'w')
# 默认情况下 我们只能将字符串写入文件中
# fp.write('hello Word')
# fp.close()

name_list = ['zs', 'ls']
# 默认情况对象是不能写入文件中的
# fp.write(name_list)

# 列表序列化
# 导入json模块到该文件中
import json

# 序列化
# 讲对象转换为json字符串,在使用scrapy框架时候,会返回一个对象,我们要把这个对象写入到文件中 就需要json
# 1. dumps()
# names = json.dumps(name_list)
# fp.write(names)

# 2.dump 将对象转换为字符串的同时,指定一个文件的对象,然后把转换后的字符串写入到这个文件中
json.dump(name_list, fp)

fp.close()

# 反序列化
# 把json的字符串变成一个py对象
fp = open('text.txt', 'r')
# content = fp.read()
# print(type(content))
# print(content)
# # 将json转换为对象
# result = json.loads(content)
# print(type(result))
# print(result)
# fp.close()
result = json.load(fp)
# <class 'list'>
print(type(result))
print(result)
fp.close()