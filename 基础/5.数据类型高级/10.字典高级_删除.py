# _*_ coding : utf-8 _*_
# @Time : 2022/10/23 23:50
# @Author : 金圣聪
# @File : 10.字典高级_删除
# @Project : pythonStudy

# del
#     删除字典中指定的元素 del 字典['key']
#     删除整个字典,包括这个对象 del 字典
# 字典.clear()
# 清空字典  但是保留字典对象,将数据删除
person = {'name': '老金', 'age': 18}
# 删除之前
print(person)

del person['age']
# 删除之后
print(person)

# del person
# 删除之后不能打印因为没有这个对象了
# print(person)
person.clear()
print(person)

