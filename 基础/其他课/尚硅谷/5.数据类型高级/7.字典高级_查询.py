# _*_ coding : utf-8 _*_
# @Time : 2022/10/20 22:56
# @Author : 金圣聪
# @File : 7.字典高级_查询
# @Project : pythonStudy

# 定一个字典
person = {'name': '无钱', 'age': 99}

# 访问name 字典变量['key']
print(person['name'])
print(person['age'])
# 字典中不存在的key,用中括号会报错,所以要先判断有没有 类似于列表的remove
# print(person['qq'])

# 在字典中不存在的key get的时候不会报错返回None 类型是NoneType
print(person.get('name'))
print(person.get('age'))
strs = person.get('11')

print()
print(type(strs))
print(type(str(strs)))